#!/usr/bin/env python3
"""
PERIHELION Dispatch Timing Calculator

Computes exact arrival times for every dispatch at every station, accounting
for light-delay propagation around the ring. Generates per-station dispatch
logs and detects order conflicts.

Usage:
    python3 dispatch_timing.py compute          # compute all → dispatch_arrivals.json
    python3 dispatch_timing.py logs             # generate agents/pN/data/dispatch_log.md
    python3 dispatch_timing.py station P-4      # show one station's log
    python3 dispatch_timing.py dispatch ID      # show one dispatch's arrivals
    python3 dispatch_timing.py validate         # check registry consistency
    python3 dispatch_timing.py fix              # propose registry corrections
    python3 dispatch_timing.py conflicts        # show dispatch order conflicts
    python3 dispatch_timing.py timeline         # chronological interleaved view
    python3 dispatch_timing.py hydrate P-4      # hydrated log with full dispatch text
    python3 dispatch_timing.py hydrate P-4 --out  # write to agents/p4/data/dispatch_log_hydrated.md
"""

import json
import re
import sys
from pathlib import Path

# Import from timestamps.py
sys.path.insert(0, str(Path(__file__).parent))
from timestamps import load as load_timestamps, load_variables, epoch_to_datetime, format_ts, render_text

# ── constants ────────────────────────────────────────────────────────────────

HOP_DELAY_S = 191          # light-delay between adjacent stations (~190.7s rounded)
P7_RELAY_OVERHEAD_S = 0.3  # from vote_bundle processing_times

RING_ORDER = ["P-1", "P-2", "P-3", "P-4", "P-5", "P-6", "P-7", "P-8"]
NUM_STATIONS = len(RING_ORDER)

TRACKING_DIR = Path(__file__).parent
PROJECT_DIR = TRACKING_DIR.parent
REGISTRY_FILE = PROJECT_DIR / "agents" / "shared" / "dispatches" / "registry.json"
ARRIVALS_FILE = TRACKING_DIR / "dispatch_arrivals.json"
AGENTS_DIR = PROJECT_DIR / "agents"
MANUSCRIPT_DIR = PROJECT_DIR / "manuscript"

# ── topology model ───────────────────────────────────────────────────────────

def load_registry():
    with open(REGISTRY_FILE) as f:
        return json.load(f)


def get_topology(registry, topo_id):
    for t in registry["topology_history"]:
        if t["id"] == topo_id:
            return t
    return None


def get_severed_links(topology):
    """Return set of frozensets representing severed links."""
    severed = set()
    for link_key, link_info in topology.get("links", {}).items():
        if link_info["status"] == "severed":
            a, b = link_key.split(":")
            severed.add(frozenset([a, b]))
    return severed


def ring_index(station):
    return RING_ORDER.index(station)


def ring_distance_cw(src_idx, dst_idx):
    """Number of hops going clockwise (increasing index)."""
    return (dst_idx - src_idx) % NUM_STATIONS


def ring_distance_ccw(src_idx, dst_idx):
    """Number of hops going counter-clockwise (decreasing index)."""
    return (src_idx - dst_idx) % NUM_STATIONS


def build_path(src_idx, dst_idx, direction):
    """Build list of stations from src to dst in given direction."""
    path = []
    i = src_idx
    while True:
        path.append(RING_ORDER[i])
        if i == dst_idx:
            break
        if direction == "cw":
            i = (i + 1) % NUM_STATIONS
        else:
            i = (i - 1) % NUM_STATIONS
    return path


def path_is_clear(path, severed):
    """Check if a path has no severed links."""
    for i in range(len(path) - 1):
        link = frozenset([path[i], path[i + 1]])
        if link in severed:
            return False
    return True


def shortest_path(src, dst, topology):
    """Find shortest path between two stations, respecting severed links.
    Returns (path, direction, hops) or None if unreachable.
    Prefers CW on tie."""
    if src == dst:
        return ([src], None, 0)

    severed = get_severed_links(topology)
    src_idx = ring_index(src)
    dst_idx = ring_index(dst)

    path_cw = build_path(src_idx, dst_idx, "cw")
    path_ccw = build_path(src_idx, dst_idx, "ccw")

    cw_clear = path_is_clear(path_cw, severed)
    ccw_clear = path_is_clear(path_ccw, severed)

    if cw_clear and ccw_clear:
        hops_cw = len(path_cw) - 1
        hops_ccw = len(path_ccw) - 1
        if hops_cw <= hops_ccw:  # prefer CW on tie
            return (path_cw, "cw", hops_cw)
        else:
            return (path_ccw, "ccw", hops_ccw)
    elif cw_clear:
        return (path_cw, "cw", len(path_cw) - 1)
    elif ccw_clear:
        return (path_ccw, "ccw", len(path_ccw) - 1)
    else:
        return None


def compute_hop_delay(path, hop_index):
    """Delay for one hop. Standard HOP_DELAY_S for all hops."""
    return HOP_DELAY_S


def compute_path_delay(path):
    """Total light-delay for a path (number of hops × HOP_DELAY_S)."""
    return (len(path) - 1) * HOP_DELAY_S


# ── arrival computation ──────────────────────────────────────────────────────

def get_send_epoch(dispatch, timestamps):
    """Get the Unix epoch when a dispatch was sent."""
    ts_id = dispatch.get("timestamp_id")
    if not ts_id or ts_id not in timestamps:
        return None
    return timestamps[ts_id]["epoch"]


def compute_bilateral_arrivals(dispatch, topology, timestamps):
    """Compute arrivals for bilateral/bilateral_chain dispatches."""
    src = dispatch["from"]
    send_epoch = get_send_epoch(dispatch, timestamps)
    if send_epoch is None:
        return None

    arrivals = {}
    recipients = [s for s in RING_ORDER if s != src]

    for dst in recipients:
        result = shortest_path(src, dst, topology)
        if result is None:
            continue
        path, direction, hops = result
        delay = compute_path_delay(path)

        # Check if P-7 is in the path as a relay (not src or dst)
        p7_in_path = "P-7" in path[1:-1]

        arrivals[dst] = {
            "hops": hops,
            "direction": direction,
            "delay_s": delay,
            "arrival_epoch": send_epoch + delay,
            "path": path,
            "p7_relay": p7_in_path,
        }

    return arrivals


def compute_circuit_arrivals(dispatch, topology, timestamps):
    """Compute arrivals for unidirectional_circuit dispatches."""
    send_epoch = get_send_epoch(dispatch, timestamps)
    if send_epoch is None:
        return None

    routing = dispatch.get("routing", {})
    circuit_path = routing.get("path", [])
    if not circuit_path:
        return None

    processing_times = dispatch.get("processing_times", {})
    arrivals = {}
    cumulative_delay = 0

    for i in range(1, len(circuit_path)):
        prev = circuit_path[i - 1]
        curr = circuit_path[i]

        # Light-delay for this hop
        cumulative_delay += HOP_DELAY_S

        # If this is the return to origin (last element = first element), record it
        if curr == circuit_path[0] and i == len(circuit_path) - 1:
            arrivals[f"{curr}_return"] = {
                "hops": i,
                "direction": "circuit",
                "delay_s": cumulative_delay,
                "arrival_epoch": send_epoch + cumulative_delay,
                "path": circuit_path[:i + 1],
                "note": "circuit return to origin",
            }
        else:
            arrivals[curr] = {
                "hops": i,
                "direction": "circuit",
                "delay_s": cumulative_delay,
                "arrival_epoch": send_epoch + cumulative_delay,
                "path": circuit_path[:i + 1],
            }

        # Add processing time at this station before forwarding
        pt = processing_times.get(curr, {})
        if isinstance(pt, dict):
            proc_s = pt.get("seconds", 0)
        else:
            proc_s = 0
        cumulative_delay += proc_s

    return arrivals


def compute_all_arrivals(registry, timestamps):
    """Compute arrivals for all dispatches."""
    results = []

    for dispatch in registry["dispatches"]:
        d_id = dispatch["id"]
        prop = dispatch.get("routing", {}).get("propagation", "")
        topo_ref = dispatch.get("topology_ref")
        topology = get_topology(registry, topo_ref) if topo_ref else None

        send_epoch = get_send_epoch(dispatch, timestamps)

        entry = {
            "id": d_id,
            "from": dispatch["from"],
            "subject": dispatch.get("subject", ""),
            "timestamp_id": dispatch.get("timestamp_id"),
            "send_epoch": send_epoch,
            "propagation": prop,
            "topology_ref": topo_ref,
        }

        if prop in ("bilateral", "bilateral_chain"):
            if topology and send_epoch:
                arrivals = compute_bilateral_arrivals(dispatch, topology, timestamps)
                entry["arrivals"] = arrivals
                entry["computable"] = True
            else:
                entry["arrivals"] = None
                entry["computable"] = False
                entry["reason"] = "missing topology or timestamp"
        elif prop == "unidirectional_circuit":
            if topology and send_epoch:
                arrivals = compute_circuit_arrivals(dispatch, topology, timestamps)
                entry["arrivals"] = arrivals
                entry["computable"] = True
            else:
                entry["arrivals"] = None
                entry["computable"] = False
        elif prop in ("cascade", "multi_round"):
            entry["arrivals"] = None
            entry["computable"] = False
            entry["reason"] = f"{prop} — no granular timing available"
        else:
            entry["arrivals"] = None
            entry["computable"] = False
            entry["reason"] = f"unknown propagation type: {prop}"

        results.append(entry)

    return results


# ── per-station logs ─────────────────────────────────────────────────────────

def build_station_log(station, arrivals_data, timestamps):
    """Build sorted list of dispatch receipts for a station."""
    events = []

    for entry in arrivals_data:
        if not entry.get("computable") or not entry.get("arrivals"):
            continue

        # Check if this station is the sender
        if entry["from"] == station:
            events.append({
                "dispatch_id": entry["id"],
                "epoch": entry["send_epoch"],
                "subject": entry["subject"],
                "role": "SENT",
                "from": entry["from"],
                "delay_s": 0,
                "hops": 0,
            })
            continue

        arrivals = entry["arrivals"]
        if station in arrivals:
            a = arrivals[station]
            events.append({
                "dispatch_id": entry["id"],
                "epoch": a["arrival_epoch"],
                "subject": entry["subject"],
                "role": "RECEIVED",
                "from": entry["from"],
                "delay_s": a["delay_s"],
                "hops": a["hops"],
                "direction": a.get("direction", ""),
            })

    events.sort(key=lambda e: e["epoch"])
    return events


def format_epoch(epoch):
    """Format epoch as story timestamp."""
    dt = epoch_to_datetime(epoch)
    return format_ts(dt, "default", "full")


# ── order conflict detection ─────────────────────────────────────────────────

def find_order_conflicts(arrivals_data):
    """Find pairs of dispatches that arrive in different order at different stations."""
    # Collect computable dispatches with arrivals
    computable = [e for e in arrivals_data if e.get("computable") and e.get("arrivals")]

    conflicts = []

    for i in range(len(computable)):
        for j in range(i + 1, len(computable)):
            d1 = computable[i]
            d2 = computable[j]

            # Get all stations that received both
            stations_1 = set()
            for s in RING_ORDER:
                if s == d1["from"]:
                    stations_1.add(s)
                elif s in d1["arrivals"]:
                    stations_1.add(s)

            stations_2 = set()
            for s in RING_ORDER:
                if s == d2["from"]:
                    stations_2.add(s)
                elif s in d2["arrivals"]:
                    stations_2.add(s)

            common = stations_1 & stations_2

            # For each station, determine when it "knows" each dispatch
            def get_time(dispatch, station):
                if station == dispatch["from"]:
                    return dispatch["send_epoch"]
                return dispatch["arrivals"].get(station, {}).get("arrival_epoch")

            # Check for order reversal
            d1_first_stations = []
            d2_first_stations = []

            for s in common:
                t1 = get_time(d1, s)
                t2 = get_time(d2, s)
                if t1 is None or t2 is None:
                    continue
                if t1 < t2:
                    d1_first_stations.append(s)
                elif t2 < t1:
                    d2_first_stations.append(s)

            if d1_first_stations and d2_first_stations:
                conflicts.append({
                    "dispatch_a": d1["id"],
                    "dispatch_b": d2["id"],
                    "a_first_at": sorted(d1_first_stations),
                    "b_first_at": sorted(d2_first_stations),
                    "subject_a": d1["subject"],
                    "subject_b": d2["subject"],
                })

    return conflicts


# ── registry validation ──────────────────────────────────────────────────────

def validate_registry(registry, timestamps):
    """Compare computed delays against registry delivery.delay_s values."""
    issues = []

    for dispatch in registry["dispatches"]:
        d_id = dispatch["id"]
        prop = dispatch.get("routing", {}).get("propagation", "")
        topo_ref = dispatch.get("topology_ref")
        topology = get_topology(registry, topo_ref) if topo_ref else None
        delivery = dispatch.get("delivery", {})

        if prop not in ("bilateral", "bilateral_chain"):
            continue
        if not topology:
            continue

        src = dispatch["from"]

        for station, info in delivery.items():
            if not isinstance(info, dict):
                continue
            if "delay_s" not in info:
                continue

            recorded_delay = info["delay_s"]
            recorded_hops = info.get("hops")

            result = shortest_path(src, station, topology)
            if result is None:
                issues.append({
                    "dispatch": d_id,
                    "station": station,
                    "issue": "unreachable in computed topology",
                    "recorded_delay": recorded_delay,
                })
                continue

            path, direction, computed_hops = result
            computed_delay = compute_path_delay(path)

            if computed_delay != recorded_delay:
                issues.append({
                    "dispatch": d_id,
                    "station": station,
                    "recorded_delay": recorded_delay,
                    "computed_delay": computed_delay,
                    "delta": computed_delay - recorded_delay,
                    "recorded_hops": recorded_hops,
                    "computed_hops": computed_hops,
                    "path": " → ".join(path),
                })

    return issues


# ── fix command ──────────────────────────────────────────────────────────────

def fix_registry(registry, timestamps):
    """Propose and optionally apply corrections to registry delay_s values."""
    issues = validate_registry(registry, timestamps)
    if not issues:
        print("No discrepancies found. Registry is consistent.")
        return

    print(f"\n{len(issues)} discrepancies found:\n")

    # Group by dispatch
    by_dispatch = {}
    for issue in issues:
        d_id = issue["dispatch"]
        if d_id not in by_dispatch:
            by_dispatch[d_id] = []
        by_dispatch[d_id].append(issue)

    for d_id, d_issues in by_dispatch.items():
        print(f"  {d_id}:")
        for iss in d_issues:
            if "computed_delay" in iss:
                print(f"    {iss['station']}: {iss['recorded_delay']}s → {iss['computed_delay']}s "
                      f"(Δ{iss['delta']:+d}s, hops {iss.get('recorded_hops')}→{iss['computed_hops']}, "
                      f"path: {iss['path']})")
            else:
                print(f"    {iss['station']}: {iss['issue']}")

    print()
    answer = input("Apply corrections? [y/N] ").strip().lower()
    if answer != "y":
        print("No changes applied.")
        return

    # Apply corrections
    for dispatch in registry["dispatches"]:
        d_id = dispatch["id"]
        if d_id not in by_dispatch:
            continue
        delivery = dispatch.get("delivery", {})
        for issue in by_dispatch[d_id]:
            station = issue["station"]
            if station in delivery and "computed_delay" in issue:
                delivery[station]["delay_s"] = issue["computed_delay"]
                delivery[station]["hops"] = issue["computed_hops"]

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Applied {len(issues)} corrections to {REGISTRY_FILE.name}")


# ── output formatting ────────────────────────────────────────────────────────

def print_station_log(station, events):
    """Print a station's dispatch log."""
    print(f"\n{'═' * 72}")
    print(f"  DISPATCH LOG — {station}")
    print(f"{'═' * 72}")

    if not events:
        print("  (no dispatches)")
        return

    for e in events:
        ts = format_epoch(e["epoch"])
        role = e["role"]
        d_id = e["dispatch_id"]

        if role == "SENT":
            print(f"\n  {ts}  SENT  {d_id}")
        else:
            direction = e.get("direction", "")
            delay = e["delay_s"]
            hops = e["hops"]
            print(f"\n  {ts}  RECV  {d_id}")
            print(f"    from {e['from']} | {hops} hops {direction} | +{delay}s")

        if e.get("subject"):
            subj = e["subject"]
            if len(subj) > 60:
                subj = subj[:57] + "..."
            print(f"    \"{subj}\"")


def write_station_log_md(station, events):
    """Write a station's dispatch log as markdown."""
    station_num = station.split("-")[1]
    out_dir = AGENTS_DIR / f"p{station_num}" / "data"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "dispatch_log.md"

    lines = [
        f"# Dispatch Log — {station}\n",
        f"*Auto-generated by dispatch_timing.py*\n",
        f"All times UTC. Receipt times computed from light-delay propagation.\n",
    ]

    if not events:
        lines.append("\n(No dispatches recorded.)\n")
    else:
        lines.append(f"\n| Time | Role | Dispatch | From | Hops | Delay |")
        lines.append(f"|------|------|----------|------|------|-------|")

        for e in events:
            ts = format_epoch(e["epoch"])
            role = e["role"]
            d_id = e["dispatch_id"]
            frm = e["from"] if role == "RECEIVED" else "—"
            hops = str(e["hops"]) if role == "RECEIVED" else "—"
            delay = f"+{e['delay_s']}s" if role == "RECEIVED" else "—"
            lines.append(f"| {ts} | {role} | {d_id} | {frm} | {hops} | {delay} |")

        lines.append("")

    out_path.write_text("\n".join(lines))
    return out_path


def print_dispatch_arrivals(dispatch_entry):
    """Print arrival details for a single dispatch."""
    print(f"\n{'═' * 72}")
    print(f"  DISPATCH: {dispatch_entry['id']}")
    print(f"{'═' * 72}")
    print(f"  From: {dispatch_entry['from']}")
    print(f"  Subject: {dispatch_entry.get('subject', '(none)')}")
    print(f"  Propagation: {dispatch_entry['propagation']}")
    print(f"  Topology: {dispatch_entry.get('topology_ref', '(none)')}")

    if dispatch_entry.get("send_epoch"):
        print(f"  Sent: {format_epoch(dispatch_entry['send_epoch'])}")

    if not dispatch_entry.get("computable"):
        reason = dispatch_entry.get("reason", "unknown")
        print(f"\n  NOT COMPUTABLE: {reason}")
        return

    arrivals = dispatch_entry.get("arrivals", {})
    if not arrivals:
        print("\n  No arrivals computed.")
        return

    print(f"\n  {'Station':<8} {'Arrival Time':<28} {'Hops':<6} {'Delay':<10} {'Direction':<10} Path")
    print(f"  {'-' * 90}")

    # Sort by arrival epoch
    sorted_arrivals = sorted(arrivals.items(), key=lambda x: x[1].get("arrival_epoch", 0))

    for station, info in sorted_arrivals:
        arr_ts = format_epoch(info["arrival_epoch"])
        hops = info["hops"]
        delay = f"+{info['delay_s']}s"
        direction = info.get("direction", "")
        path = " → ".join(info.get("path", []))
        print(f"  {station:<8} {arr_ts:<28} {hops:<6} {delay:<10} {direction:<10} {path}")


def print_timeline(arrivals_data, timestamps):
    """Print chronological interleaved view of all dispatch events."""
    events = []

    for entry in arrivals_data:
        if not entry.get("computable") or not entry.get("arrivals"):
            continue

        # Add send event
        if entry.get("send_epoch"):
            events.append({
                "epoch": entry["send_epoch"],
                "type": "SENT",
                "dispatch": entry["id"],
                "station": entry["from"],
                "subject": entry.get("subject", ""),
            })

        # Add receive events
        for station, info in entry["arrivals"].items():
            if station.endswith("_return"):
                label = station.replace("_return", " (return)")
            else:
                label = station
            events.append({
                "epoch": info["arrival_epoch"],
                "type": "RECV",
                "dispatch": entry["id"],
                "station": label,
                "subject": entry.get("subject", ""),
                "delay_s": info["delay_s"],
            })

    events.sort(key=lambda e: (e["epoch"], e["type"] == "RECV"))

    print(f"\n{'═' * 80}")
    print(f"  DISPATCH TIMELINE — ALL STATIONS")
    print(f"{'═' * 80}")

    prev_day = None
    for e in events:
        dt = epoch_to_datetime(e["epoch"])
        day = dt.timetuple().tm_yday
        year = dt.year
        day_key = (year, day)

        if day_key != prev_day:
            day_ts = format_ts(dt, "day", "day")
            cal = dt.strftime("%A %-d %B %Y")
            print(f"\n  ── {day_ts} ({cal}) ──")
            prev_day = day_key

        ts = format_ts(dt, "time", "full")
        typ = e["type"]
        d_id = e["dispatch"]
        station = e["station"]

        if typ == "SENT":
            print(f"  {ts}  {station:<8} SENT  {d_id}")
        else:
            delay = e.get("delay_s", 0)
            print(f"  {ts}  {station:<8} RECV  {d_id}  (+{delay}s)")


# ── hydrated dispatch log ────────────────────────────────────────────────────

def extract_dispatches_from_manuscripts():
    """Scan manuscript/*.md for dispatch blocks, keyed by timestamp_id.

    Returns dict mapping timestamp_id → full dispatch text (raw, with placeholders).
    """
    dispatches = {}
    for md_file in sorted(MANUSCRIPT_DIR.glob("*.md")):
        text = md_file.read_text()
        # Split on dispatch boundaries: ```\n— DISPATCH — through ```\nEND DISPATCH\n```
        # Find all dispatch blocks
        blocks = re.split(r"^```\s*$", text, flags=re.MULTILINE)

        # Walk through blocks looking for dispatch headers
        i = 0
        while i < len(blocks):
            block = blocks[i]
            if "— DISPATCH —" in block:
                # This block is the header (FROM, TO, VIA, TIMESTAMP)
                header = block.strip()
                # Collect body blocks until END DISPATCH
                body_parts = []
                j = i + 1
                while j < len(blocks):
                    if blocks[j].strip() == "END DISPATCH":
                        break
                    body_parts.append(blocks[j])
                    j += 1

                # Reconstruct full dispatch text
                full_text = "```\n" + header + "\n```\n"
                for bp in body_parts:
                    full_text += bp
                full_text += "```\nEND DISPATCH\n```"

                # Extract timestamp_id from TIMESTAMP: {xxx} line
                ts_match = re.search(r"TIMESTAMP:\s*\{([a-z][a-z0-9_]*)\}", header)
                if ts_match:
                    ts_id = ts_match.group(1)
                    dispatches[ts_id] = full_text

                i = j + 1
            else:
                i += 1

    return dispatches


def get_dispatch_text(dispatch, manuscript_dispatches):
    """Get the display text for a dispatch entry.

    Returns (text, source) where source is 'manuscript', 'file_ref', or 'summary'.
    """
    ts_id = dispatch.get("timestamp_id")

    # Try manuscript text first
    if ts_id and ts_id in manuscript_dispatches:
        return manuscript_dispatches[ts_id], "manuscript"

    content_ref = dispatch.get("content_ref")
    summary = dispatch.get("summary", "(no summary)")

    # Content ref to an agents/ data file — don't inline, just note it
    if content_ref and content_ref.startswith("agents/"):
        text = summary + f"\n\n[Full content: {content_ref}]"
        return text, "file_ref"

    # Content ref to manuscript — try extracting by timestamp_id (already done above)
    # Fall back to summary
    return summary, "summary"


def format_hydrated_log(station, events, registry, manuscript_dispatches,
                        timestamps, variables):
    """Build the full hydrated dispatch log markdown for a station."""
    # Index dispatches by id
    dispatch_by_id = {d["id"]: d for d in registry["dispatches"]}

    lines = [
        f"# Hydrated Dispatch Log — {station}\n",
        "Dispatches in the order this station received them.",
        "Verify no dispatch references information that hasn't arrived yet.\n",
    ]

    for e in events:
        d_id = e["dispatch_id"]
        dispatch = dispatch_by_id.get(d_id)
        if not dispatch:
            continue

        lines.append("---\n")

        role = e["role"]
        if role == "RECEIVED":
            ts = format_epoch(e["epoch"])
            send_epoch = e["epoch"] - e["delay_s"]
            send_ts = format_epoch(send_epoch)
            direction = e.get("direction", "")
            hops = e["hops"]
            delay = e["delay_s"]
            dir_label = direction.upper() if direction else ""
            lines.append(f"## [RECV] {d_id}")
            lines.append(f"**Received:** {ts} UTC | From {e['from']} | "
                         f"{hops} hops {dir_label} | +{delay}s")
            lines.append(f"**Sent:** {send_ts} UTC\n")
        else:
            ts = format_epoch(e["epoch"])
            lines.append(f"## [SENT] {d_id}")
            lines.append(f"**Sent:** {ts} UTC\n")

        text, source = get_dispatch_text(dispatch, manuscript_dispatches)
        rendered = render_text(text, timestamps, variables)

        if source == "summary":
            lines.append(f"*[REGISTRY SUMMARY]*\n")
        elif source == "file_ref":
            lines.append(f"*[REGISTRY SUMMARY + FILE REFERENCE]*\n")

        # Quote the dispatch text
        for line in rendered.split("\n"):
            lines.append(f"> {line}")

        lines.append("")

    return "\n".join(lines)


def cmd_hydrate(station_id, write_file=False):
    """Build and output a hydrated dispatch log for a station."""
    station = station_id.upper()
    if not station.startswith("P-"):
        station = f"P-{station}"
    if station not in RING_ORDER:
        print(f"Unknown station: {station}")
        sys.exit(1)

    registry = load_registry()
    timestamps = load_timestamps()
    variables = load_variables()
    arrivals = compute_all_arrivals(registry, timestamps)
    events = build_station_log(station, arrivals, timestamps)

    manuscript_dispatches = extract_dispatches_from_manuscripts()

    output = format_hydrated_log(station, events, registry,
                                 manuscript_dispatches, timestamps, variables)

    if write_file:
        station_num = station.split("-")[1]
        out_dir = AGENTS_DIR / f"p{station_num}" / "data"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "dispatch_log_hydrated.md"
        out_path.write_text(output)
        print(f"Wrote {out_path.relative_to(PROJECT_DIR)} ({len(events)} dispatches)")
    else:
        print(output)


# ── CLI ──────────────────────────────────────────────────────────────────────

def cmd_compute():
    registry = load_registry()
    timestamps = load_timestamps()
    arrivals = compute_all_arrivals(registry, timestamps)

    with open(ARRIVALS_FILE, "w") as f:
        json.dump(arrivals, f, indent=2, ensure_ascii=False)
        f.write("\n")

    computable = sum(1 for a in arrivals if a.get("computable"))
    total = len(arrivals)
    print(f"Computed arrivals for {computable}/{total} dispatches → {ARRIVALS_FILE.name}")


def cmd_logs():
    registry = load_registry()
    timestamps = load_timestamps()
    arrivals = compute_all_arrivals(registry, timestamps)

    count = 0
    for station in RING_ORDER:
        events = build_station_log(station, arrivals, timestamps)
        path = write_station_log_md(station, events)
        count += 1
        print(f"  {station}: {len(events)} entries → {path.relative_to(PROJECT_DIR)}")

    print(f"\nGenerated {count} dispatch logs.")


def cmd_station(station_id):
    station = station_id.upper()
    if not station.startswith("P-"):
        station = f"P-{station}"
    if station not in RING_ORDER:
        print(f"Unknown station: {station}")
        sys.exit(1)

    registry = load_registry()
    timestamps = load_timestamps()
    arrivals = compute_all_arrivals(registry, timestamps)
    events = build_station_log(station, arrivals, timestamps)
    print_station_log(station, events)


def cmd_dispatch(dispatch_id):
    registry = load_registry()
    timestamps = load_timestamps()
    arrivals = compute_all_arrivals(registry, timestamps)

    for entry in arrivals:
        if entry["id"] == dispatch_id:
            print_dispatch_arrivals(entry)
            return

    print(f"Dispatch not found: {dispatch_id}")
    sys.exit(1)


def cmd_validate():
    registry = load_registry()
    timestamps = load_timestamps()
    issues = validate_registry(registry, timestamps)

    if not issues:
        print("All registry delay values are consistent with computed paths.")
        return

    print(f"\n{len(issues)} discrepancies found:\n")

    for iss in issues:
        if "computed_delay" in iss:
            print(f"  {iss['dispatch']} → {iss['station']}:")
            print(f"    recorded: {iss['recorded_delay']}s ({iss.get('recorded_hops')} hops)")
            print(f"    computed: {iss['computed_delay']}s ({iss['computed_hops']} hops)")
            print(f"    delta:    {iss['delta']:+d}s")
            print(f"    path:     {iss['path']}")
        else:
            print(f"  {iss['dispatch']} → {iss['station']}: {iss['issue']}")


def cmd_fix():
    registry = load_registry()
    timestamps = load_timestamps()
    fix_registry(registry, timestamps)


def cmd_conflicts():
    registry = load_registry()
    timestamps = load_timestamps()
    arrivals = compute_all_arrivals(registry, timestamps)
    conflicts = find_order_conflicts(arrivals)

    if not conflicts:
        print("No order conflicts detected.")
        return

    print(f"\n{len(conflicts)} order conflicts detected:\n")

    for c in conflicts:
        print(f"  {c['dispatch_a']}  vs  {c['dispatch_b']}")
        print(f"    A: \"{c['subject_a'][:50]}\"")
        print(f"    B: \"{c['subject_b'][:50]}\"")
        print(f"    A arrives first at: {', '.join(c['a_first_at'])}")
        print(f"    B arrives first at: {', '.join(c['b_first_at'])}")
        print()


def cmd_timeline():
    registry = load_registry()
    timestamps = load_timestamps()
    arrivals = compute_all_arrivals(registry, timestamps)
    print_timeline(arrivals, timestamps)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "compute":
        cmd_compute()
    elif cmd == "logs":
        cmd_logs()
    elif cmd == "station":
        if len(sys.argv) < 3:
            print("Usage: dispatch_timing.py station <P-N>")
            sys.exit(1)
        cmd_station(sys.argv[2])
    elif cmd == "dispatch":
        if len(sys.argv) < 3:
            print("Usage: dispatch_timing.py dispatch <ID>")
            sys.exit(1)
        cmd_dispatch(sys.argv[2])
    elif cmd == "validate":
        cmd_validate()
    elif cmd == "fix":
        cmd_fix()
    elif cmd == "conflicts":
        cmd_conflicts()
    elif cmd == "timeline":
        cmd_timeline()
    elif cmd == "hydrate":
        if len(sys.argv) < 3:
            print("Usage: dispatch_timing.py hydrate <P-N> [--out]")
            sys.exit(1)
        write_out = "--out" in sys.argv[3:]
        cmd_hydrate(sys.argv[2], write_file=write_out)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
