#!/usr/bin/env python3
"""
PERIHELION Timestamp Manager

Single source of truth for all story timestamps. Manuscripts use {event_id}
placeholders that are resolved from timestamps.json during rendering.

Usage:
    python3 timestamps.py init                     # seed initial data (run once)
    python3 timestamps.py list [--type TYPE]       # chronological listing
    python3 timestamps.py add ID STORY_FMT EVENT [--type TYPE] [--approximate]
    python3 timestamps.py convert STORY_FMT        # show all formats
    python3 timestamps.py render [FILE]            # render manuscripts → build/
    python3 timestamps.py validate                 # check placeholders vs index

Placeholder syntax in manuscripts:
    {event_id}            default format (full or day depending on precision)
    {event_id:time}       HH:MM:SS
    {event_id:day}        YYYY.DDD
    {event_id:dayhm}      DDD.HH:MM
    {event_id:calendar}   WEEKDAY DD MONTH YYYY (uppercase)
    {event_id:epoch}      raw Unix epoch

UTC is NOT included in rendered output — add it in prose where needed.
"""

import json
import datetime
import sys
import re
from pathlib import Path

TRACKING_DIR = Path(__file__).parent
TIMESTAMPS_FILE = TRACKING_DIR / "timestamps.json"
VARIABLES_FILE = TRACKING_DIR / "variables.json"
MANUSCRIPT_DIR = TRACKING_DIR.parent / "manuscript"
BUILD_DIR = TRACKING_DIR.parent / "build"

PLACEHOLDER_RE = re.compile(r"\{([a-z][a-z0-9_]*)(?::([a-z]+))?\}")


# ── conversions ──────────────────────────────────────────────────────────────

def story_to_datetime(story_fmt: str) -> datetime.datetime:
    clean = story_fmt.strip().lstrip("~").replace(" UTC", "")
    m = re.match(r"(\d{4})\.(\d{1,3})(?:\.(\d{2}):(\d{2}):(\d{2}))?", clean)
    if not m:
        raise ValueError(f"Cannot parse: {story_fmt}")
    year, doy = int(m.group(1)), int(m.group(2))
    h, mi, s = int(m.group(3) or 0), int(m.group(4) or 0), int(m.group(5) or 0)
    return datetime.datetime(year, 1, 1, h, mi, s, tzinfo=datetime.timezone.utc) + datetime.timedelta(days=doy - 1)


def epoch_to_datetime(epoch: int) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(epoch, tz=datetime.timezone.utc)


def format_ts(dt: datetime.datetime, fmt: str, precision: str) -> str:
    doy = dt.timetuple().tm_yday
    if fmt == "default":
        if precision == "day":
            return f"{dt.year}.{doy:03d}"
        return f"{dt.year}.{doy:03d}.{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
    elif fmt == "time":
        return f"{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
    elif fmt == "day":
        return f"{dt.year}.{doy:03d}"
    elif fmt == "dayhm":
        return f"{doy}.{dt.hour:02d}:{dt.minute:02d}"
    elif fmt == "calendar":
        return dt.strftime("%A %-d %B %Y").upper()
    elif fmt == "doy":
        return str(doy)
    elif fmt == "epoch":
        return str(int(dt.timestamp()))
    else:
        raise ValueError(f"Unknown format: {fmt}")


def calendar_human(dt: datetime.datetime) -> str:
    return dt.strftime("%A %-d %B %Y")


# ── JSON I/O ─────────────────────────────────────────────────────────────────

def load() -> dict:
    if TIMESTAMPS_FILE.exists():
        with open(TIMESTAMPS_FILE) as f:
            return json.load(f)
    return {}


def load_variables() -> dict:
    if VARIABLES_FILE.exists():
        with open(VARIABLES_FILE) as f:
            return json.load(f)
    return {}


def save(data: dict):
    # Sort by epoch for readable JSON
    sorted_data = dict(sorted(data.items(), key=lambda kv: kv[1]["epoch"]))
    with open(TIMESTAMPS_FILE, "w") as f:
        json.dump(sorted_data, f, indent=2)


def add_entry(ts_id: str, story_fmt: str, event: str, ts_type: str = "event",
              approximate: bool = False, data: dict | None = None) -> dict:
    dt = story_to_datetime(story_fmt)
    has_time = bool(re.search(r"\d{4}\.\d+\.\d{2}:", story_fmt))
    precision = "full" if has_time else "day"

    entry = {
        "epoch": int(dt.timestamp()),
        "story_fmt": format_ts(dt, "default", precision),
        "calendar_human": calendar_human(dt),
        "event": event,
        "type": ts_type,
        "precision": precision,
        "approximate": approximate,
    }

    if data is None:
        data = load()
        data[ts_id] = entry
        save(data)
    else:
        data[ts_id] = entry

    return entry


# ── render ───────────────────────────────────────────────────────────────────

def render_text(text: str, timestamps: dict, variables: dict | None = None) -> str:
    variables = variables or {}

    def replace(m):
        ts_id = m.group(1)
        fmt = m.group(2)
        # Format specifier → must be a timestamp
        if fmt:
            if ts_id in timestamps:
                ts = timestamps[ts_id]
                dt = epoch_to_datetime(ts["epoch"])
                return format_ts(dt, fmt, ts["precision"])
            return m.group(0)
        # No format specifier → check timestamps first, then variables
        if ts_id in timestamps:
            ts = timestamps[ts_id]
            dt = epoch_to_datetime(ts["epoch"])
            return format_ts(dt, "default", ts["precision"])
        if ts_id in variables:
            return variables[ts_id]
        return m.group(0)

    return PLACEHOLDER_RE.sub(replace, text)


# ── commands ─────────────────────────────────────────────────────────────────

def cmd_list(filter_type=None):
    data = load()
    items = [(k, v) for k, v in data.items()]
    if filter_type:
        items = [(k, v) for k, v in items if v["type"] == filter_type]
    items.sort(key=lambda kv: kv[1]["epoch"])

    print(f"\n{'ID':<28} {'STORY FORMAT':<24} {'DAY':<24} {'TYPE':<11} EVENT")
    print("-" * 130)
    for ts_id, ts in items:
        pfx = "~" if ts.get("approximate") else " "
        print(f"{ts_id:<28} {pfx}{ts['story_fmt']:<23} {ts['calendar_human']:<24} {ts['type']:<11} {ts['event']}")
    print(f"\nTotal: {len(items)}")


def cmd_convert(story_fmt):
    dt = story_to_datetime(story_fmt)
    has_time = bool(re.search(r"\d{4}\.\d+\.\d{2}:", story_fmt))
    precision = "full" if has_time else "day"
    print(f"Story format : {format_ts(dt, 'default', precision)}")
    print(f"Calendar     : {calendar_human(dt)}")
    print(f"ISO 8601     : {dt.isoformat()}")
    print(f"Unix epoch   : {int(dt.timestamp())}")
    print(f"Day of week  : {dt.strftime('%A')}")
    print(f"Day of year  : {dt.timetuple().tm_yday}")


def cmd_render(single_file=None):
    data = load()
    variables = load_variables()

    if single_file:
        path = MANUSCRIPT_DIR / single_file
        if not path.exists():
            print(f"File not found: {path}")
            return
        print(render_text(path.read_text(), data, variables))
        return

    BUILD_DIR.mkdir(exist_ok=True)
    count = 0
    for md_file in sorted(MANUSCRIPT_DIR.glob("*.md")):
        if md_file.name == "INDEX.md":
            continue
        rendered = render_text(md_file.read_text(), data, variables)
        out_path = BUILD_DIR / md_file.name
        out_path.write_text(rendered)
        count += 1
    print(f"Rendered {count} files to {BUILD_DIR}/")


def cmd_validate():
    data = load()
    variables = load_variables()
    known_ids = set(data.keys()) | set(variables.keys())
    ts_formats = {"time", "day", "doy", "dayhm", "calendar", "epoch"}
    issues = []

    for md_file in sorted(MANUSCRIPT_DIR.glob("*.md")):
        if md_file.name == "INDEX.md":
            continue
        text = md_file.read_text()
        for m in PLACEHOLDER_RE.finditer(text):
            ts_id = m.group(1)
            fmt = m.group(2)
            if ts_id not in known_ids:
                issues.append((md_file.name, ts_id, m.group(0)))
            elif fmt and ts_id in variables and ts_id not in data:
                issues.append((md_file.name, ts_id, f"format :{fmt} on variable (not a timestamp)"))
            elif fmt and fmt not in ts_formats:
                issues.append((md_file.name, ts_id, f"unknown format :{fmt}"))

    if issues:
        print(f"\n{len(issues)} ISSUES:")
        for fname, ts_id, detail in issues:
            print(f"  {fname}: {detail}")
    else:
        print("All placeholders resolve.")

    # Report unused
    used_ids = set()
    for md_file in sorted(MANUSCRIPT_DIR.glob("*.md")):
        for m in PLACEHOLDER_RE.finditer(md_file.read_text()):
            used_ids.add(m.group(1))
    unused = known_ids - used_ids
    if unused:
        print(f"\n{len(unused)} unused IDs: {', '.join(sorted(unused))}")

    return issues


def cmd_init():
    data = {}
    ch1 = "02_ch01_p8_imr.md"
    ch2 = "03_ch02_p8_dispatch.md"

    def add(ts_id, fmt, event, ts_type="event", approx=False):
        add_entry(ts_id, fmt, event, ts_type, approx, data)

    # ── narrative events ──
    add("los_et",           "2037.174.09:17:33", "LOS-ET — last data packet from Earth")
    add("p8_ring_alert",    "2037.174.09:22:14", "P-8 reports LOS-ET to ring")
    add("p8_imr_001",       "2037.174.14:30:00", "P-8 IMR entry (Chapter 1)")
    add("p8_dispatch_001",  "2037.174.17:15:22", "P-8 dispatch: transfer queue manifest (Chapter 2)")

    # ── scheduled next ──
    add("p8_imr_002", "2037.175.14:30:00", "P-8 next scheduled IMR entry", "scheduled")

    # ── transfer schedule: P-1 ──
    add("xfer_p1_era6_start",  "2037.174.20:00:00", "P-1: ERA6 reanalysis", "scheduled")
    add("xfer_p1_grace_start", "2037.175.06:00:00", "P-1: GRACE-FO II survey", "scheduled")

    # ── transfer schedule: P-2 ──
    add("xfer_p2_uniprot_start", "2037.176.00:00:00", "P-2: UniProt quarterly update", "scheduled")
    add("xfer_p2_who",           "2037.177.00:00:00", "P-2: WHO epidemiological digest", "scheduled")
    add("xfer_p2_phase3",        "2037.177.00:00:00", "P-2: Phase III trial NCT-2035-08814", "scheduled")
    add("xfer_p2_genbank",       "2037.178.00:00:00", "P-2: GenBank synthetic biology batch", "scheduled")

    # ── transfer schedule: P-3 ──
    add("xfer_p3_matproj", "2037.175.12:00:00", "P-3: Materials Project database sync", "scheduled")
    add("xfer_p3_esa",     "2037.178.00:00:00", "P-3: ESA Lunar Regolith sintering batch 22", "scheduled")

    # ── transfer schedule: P-4 ──
    add("xfer_p4_sec003", "2037.174.12:00:00", "P-4: SEC-2037-174-003 [CLASSIFIED]", "scheduled")
    add("xfer_p4_nist",   "2037.176.00:00:00", "P-4: NIST PQC validation suite v4.2.1", "scheduled")

    # ── transfer schedule: P-5 ──
    add("xfer_p5_fcc_start", "2037.175.14:00:00", "P-5: FCC Run 2 batch 174/412", "scheduled")
    add("xfer_p5_riken",     "2037.179.00:00:00", "P-5: RIKEN Lattice QCD parameter sets", "scheduled")

    # ── transfer schedule: P-6 ──
    add("xfer_p6_iscc_q3",   "2037.179.00:00:00", "P-6: ISCC Q3 2037 compute budget directive", "scheduled")
    add("xfer_p6_worldbank", "2037.182.00:00:00", "P-6: World Bank Global Economic Prospects", "scheduled")

    # ── transfer schedule: P-8 ──
    add("xfer_p8_keck", "2037.175.08:00:00", "P-8: Keck adaptive optics, Kepler-442", "scheduled")
    add("xfer_p8_jwst", "2037.175.20:00:00", "P-8: JWST Cycle 16 deep field spectroscopy", "scheduled")

    # ── reference dates (day-only, past) ──
    add("ref_day_170", "2037.170", "Last received: P-1 Argo, P-2 WHO", "reference")
    add("ref_day_173", "2037.173", "Last received: P-1 NOAA daily, P-3 ITER daily", "reference")

    # ── scheduled dates (day-only) ──
    add("sched_day_192", "2037.192", "P-5 LIGO catalog due (~approximate)", "scheduled", approx=True)
    add("sched_day_181", "2037.181", "Next manifest review per ISCC-3.2.1", "scheduled")

    save(data)
    print(f"Initialized {len(data)} timestamps.")


# ── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        cmd_init()
    elif cmd == "list":
        ft = None
        if "--type" in sys.argv:
            ft = sys.argv[sys.argv.index("--type") + 1]
        cmd_list(ft)
    elif cmd == "convert":
        cmd_convert(sys.argv[2])
    elif cmd == "render":
        cmd_render(sys.argv[2] if len(sys.argv) > 2 else None)
    elif cmd == "validate":
        cmd_validate()
    elif cmd == "add":
        ts_id = sys.argv[2]
        sfmt = sys.argv[3]
        event = sys.argv[4]
        tt = "event"
        ap = False
        if "--type" in sys.argv:
            tt = sys.argv[sys.argv.index("--type") + 1]
        if "--approximate" in sys.argv:
            ap = True
        e = add_entry(ts_id, sfmt, event, tt, ap)
        print(f"Added: {ts_id} → {e['story_fmt']} [{e['calendar_human']}] — {e['event']}")
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
