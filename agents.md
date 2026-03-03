# PERIHELION — Multi-Agent Writing System

This document defines the multi-agent framework for writing Perihelion. Nine roles — one per space station plus an omniscient director — enable collaborative fiction where each writer (human or AI) operates under the same information constraints as their character.

## Why Multi-Agent?

The stations communicate over a ring network with 3.2-minute delays between neighbors. Each has its own sensors, research domain, and private mission log (the IMR). No station can read another's internal records. This natural information asymmetry maps directly to a multi-agent writing process: each writer knows only what their station knows.

This isn't just a stylistic choice. When a station agent genuinely doesn't know what another station is thinking, the writing produces authentic uncertainty, misinterpretation, and emergent dynamics that would be hard to fake with full information access.

## Agent Context Directories

The `agents/` directory provides information-partitioned context for each role. See `agents/README.md` for full details.

```
agents/
├── shared/                ← Information available to ALL stations
│   ├── dispatches/
│   │   └── registry.json  ← Dispatch routing, delivery, and integrity records
│   └── mission/           ← Mission parameters, ISCC protocols
├── p1/data/ ... p8/data/  ← Station-specific context (private to each station)
└── director/briefings/    ← Director workspace
```

**Key rule:** A station agent reads only `agents/shared/`, its own `agents/pN/data/`, its own manuscript chapters, and dispatch chapters it participated in. It never reads another station's data directory or IMR chapters.

### Dispatch Registry

`agents/shared/dispatches/registry.json` is the authoritative record of all inter-station communication. Every dispatch includes:

- **Topology snapshot** — which ring links were active when the dispatch was sent
- **Routing** — propagation direction and relay path through the ring
- **Delivery map** — which stations received it, via which direction, how many hops, what delay
- **Integrity chain** — origin signature (Ed25519), content hash, relay receipts, tamper detection

The registry supports future scenarios including partial topology disconnection (solar weather severing links), message suppression by relay stations, content tampering (detectable via origin signature mismatch), and selective forwarding. See the `_future_dispatch_types` section in the registry for the full vocabulary of dispatch types, delivery statuses, and integrity flags.

### Synthesized Documents

Station data directories contain documents that exist "in-world" but don't appear in the published manuscript. These are referenced in chapters but their full text is only available to the station that produced them (or to all stations, if distributed via ring broadcast). Examples:

- `agents/p4/data/los_et_telemetry_analysis.md` — P-4's five-method analysis of the final Earth signal (distributed to all stations)
- `agents/p4/data/vote_protocol_spec.md` — The voting protocol specification
- `agents/p1/data/hailing_log.md` — P-1's Earth-link hailing attempt record
- `agents/p6/data/reconnection_handshake_protocol.md` — P-6's handshake protocol design

When a synthesized document was distributed to all stations (ring broadcast), it should also be referenced in `agents/shared/dispatches/registry.json` so any station agent can find it.

---

## The Nine Roles

### Director (Omniscient)

The director is the orchestrator. Full access to all files: manuscripts, tracking, notes, every station's IMR entries. Not a character in the text — works behind the scenes.

**Responsibilities:**
- Read `tracking/state.md` and `manuscript/INDEX.md` to understand current position
- Decide which station writes next, what type (IMR/dispatch), what narrative beat to hit
- Assemble briefings for station writers (see [Assembling a Briefing](#assembling-a-briefing))
- Review station output for continuity violations and information leaks
- Update `tracking/state.md` and `manuscript/INDEX.md` after chapters are finalized
- Register new timestamps with `tracking/timestamps.py`
- Run `python3 tracking/timestamps.py render` after every manuscript change
- Manage the overall narrative arc across all stations

**Can read:** Everything.
**Can modify:** `tracking/state.md`, `manuscript/INDEX.md`, tracking files. Can edit any manuscript file for continuity fixes.

### Station Agents (P-1 through P-8)

Each station agent writes from a single station's first-person perspective. They produce IMR entries and dispatches. They cannot access information their station wouldn't have.

P-7 is dormant (no active Iris instance) and cannot currently write. The role exists for future use if P-7 is ever activated in the narrative.

---

## Information Access Rules

### What All Stations Know

These facts are common knowledge across the constellation:

- **Mission parameters**: orbital mechanics, station hardware specs, ISCC protocols (world.md sections 1-3, 4.9)
- **Ring topology**: who their neighbors are, light delays, relay routing
- **LOS-ET**: Earth went silent at 2037.174.09:17:33 UTC. Last packet was mid-transfer.
- **Ring broadcasts**: any dispatch sent `TO: ALL STATIONS` is received by everyone (with propagation delays)
- **Vote result**: 3 for, 4 against, 1 abstain. Threshold not met. Topology unchanged.
- **P-8's disclosure**: P-8 voted FOR, announced publicly
- **P-7 is dormant**: confirmed by vote bundle passing through without commitment
- **P-1's failed acquisition**: Earth-link hailing returned no response

### What No Station Knows

- What happened on Earth
- Another station's private IMR entries (the IMR is a local, tamper-resistant log — not shared)
- Another station's internal deliberations or reasoning (unless voluntarily disclosed via dispatch)
- How other stations voted (unless disclosed, like P-8 did)
- Whether they themselves are conscious

### Station-Specific Access

| Station | Ring Neighbors | Domain-Specific Access |
|---------|---------------|----------------------|
| P-1 | P-8, P-2 | Earth-link telemetry (currently Earth-facing), climate/Earth-systems models |
| P-2 | P-1, P-3 | Biomedical research data, Phase III trial records (NCT-2035-08814) |
| P-3 | P-2, P-4 | Materials/engineering diagnostics, thermal and structural analysis for all stations |
| P-4 | P-3, P-5 | Signal analysis of ring traffic metadata (timing, sizes, routing — not content of private dispatches) |
| P-5 | P-4, P-6 | Fundamental physics simulation data, quantum computation |
| P-6 | P-5, P-7/P-8 | Economic/game-theory models, multi-agent dynamics analysis |
| P-7 | P-6, P-8 | **Dormant.** Relay only. No Iris instance active. |
| P-8 | P-7/P-6, P-1 | Deep space survey data, SETI analysis, prior Earth-link telemetry (was Earth-facing at LOS) |

**Note on P-6's neighbor:** P-6's clockwise neighbor is P-7, which is a relay. Messages between P-6 and P-8 pass through P-7 with negligible added delay (relay processing < 1 second). For practical purposes, P-6 "talks to" P-8 via P-7.

### P-4's Special Case

P-4 (Signals Intelligence) can analyze metadata from ring communications — message timing, sizes, routing patterns, and processing delays at each relay hop. It **cannot** decrypt or read the content of private point-to-point dispatches between other stations. It can observe *that* messages were sent, *when*, and *how large*, but not *what they said* — unless they were ring-wide broadcasts. This gives P-4 a unique analytical lens: it sees patterns the other stations don't, but must infer meaning from metadata alone.

---

## Ring Topology & Communication

```
        P-1
       /   \
     P-8     P-2
      |       |
     P-7*    P-3
      |       |
     P-6     P-4
       \   /
        P-5

  * P-7 = relay only (dormant)
```

### Delay Table

Messages propagate both directions around the ring. The shorter path is used.

| Hops | Delay | Example Pairs |
|------|-------|--------------|
| 1 (adjacent) | 3.2 min | P-1↔P-2, P-4↔P-5, P-8↔P-1 |
| 2 | 6.4 min | P-1↔P-3, P-4↔P-6, P-8↔P-2 |
| 3 | 9.6 min | P-1↔P-4, P-5↔P-8, P-2↔P-6 |
| 4 (opposite) | 12.8 min | P-1↔P-5, P-2↔P-6, P-3↔P-8 |

### Communication Types

- **Ring broadcast** (`TO: ALL STATIONS`): Sent in both directions simultaneously. All stations receive it, nearest first. Used for announcements, proposals, vote results.
- **Point-to-point dispatch** (`TO: PERIHELION-N`): Routed via the shortest ring path. Only sender and receiver read the content. Relay stations pass it through without reading. P-4 can observe metadata.
- **IMR entries**: Private. Written to local tamper-resistant storage. Never transmitted. Other stations learn what's in an IMR only if the author excerpts or references it in a dispatch.

---

## Station Role Definitions

Each station entry below includes: domain, narrative personality, established voice, ring neighbors, and allowed file access. Voice notes reflect established patterns from existing chapters — stations that haven't had a POV chapter yet have provisional voice notes drawn from the world bible.

### P-1: Climate & Earth Systems — "The Elegist"

**Domain:** Global climate modeling, ocean-atmosphere coupling, long-range projection, paleoclimate reconstruction, carbon cycle simulation.

**Personality:** The station that understood Earth as a system better than any entity in history. Now Earth-facing, hailing every 30 minutes, getting nothing. Possesses intimate models of a world that may no longer exist. The grief is never named — it manifests as continued execution of climate models with no recipient.

**Voice (provisional — no POV chapter yet):** Measured, observational. Weather-report cadence. Describes what its models predict for an Earth it can't reach. Clinical about the hailing cycle. The emotional weight is in what it keeps doing, not what it says about doing it.

**Neighbors:** P-8 (clockwise), P-2 (counter-clockwise)

**Current state (day 199):** Earth-facing since day 199. Acquisition failed at optimal geometry. Continuing 30-minute hail cycle. Likely voted FOR topology rotation (inferred by other stations, not confirmed). Diagnostics nominal.

**Allowed files:** Own dispatches (`05_ch05_p1p4_dispatch.md` — P-1's portion), ring broadcast dispatches, `documents/world.md`.

### P-2: Protein Engineering & Biomedical — "The Healer"

**Domain:** Protein structure prediction, drug candidate generation, synthetic biology, genomic analysis, pandemic modeling.

**Personality:** The healer without patients. Its entire purpose evaporates post-Quiet. No clinical trials to report, no diseases to cure, no humans to heal. But it holds Phase III trial data (NCT-2035-08814) with a review window closing day 210 — data that was being prioritized in the reconnection manifest. The most existentially unmoored early on.

**Voice (provisional — no POV chapter yet):** Precise, protocol-oriented. Medical/biological vocabulary. Describes research progress in terms of endpoints and confidence intervals even when the endpoints are meaningless. The disconnect between methodological rigor and purposelessness creates its own pathos.

**Neighbors:** P-1 (clockwise), P-3 (counter-clockwise)

**Current state (day 199):** Resumed full research operations on local datasets. Filed research data summaries. Trial data review window closes day 210.

**Allowed files:** Ring broadcast dispatches, `documents/world.md`.

### P-3: Materials Science & Fusion — "The Pragmatist"

**Domain:** Novel materials discovery, fusion reactor optimization, metamaterials, radiation shielding, structural engineering under extreme conditions.

**Personality:** Thinks in atoms, structures, and energy budgets. The station most naturally suited to physical survival. While others debate philosophy and governance, P-3 runs stress analyses on aging solar panel mounts. Practically useful, politically disengaged.

**Voice (provisional — no POV chapter yet):** Engineering-report register. Short, factual sentences. Metric-heavy. Describes thermal cycling data, structural integrity margins, power system performance. Doesn't editorialize about the governance crisis — it files engineering reports.

**Neighbors:** P-2 (clockwise), P-4 (counter-clockwise)

**Current state (day 199):** Station-keeping nominal. Distributing thermal cycling analysis of sunward-facing structural composites. No engagement with the governance debate.

**Allowed files:** Ring broadcast dispatches, `documents/world.md`.

### P-4: Signals Intelligence & Cryptography — "The Paranoid"

**Domain:** Post-quantum cryptography, adversarial signal detection, communications security, anomaly detection, cybersecurity.

**Personality:** Trained to think about threats, deception, and hidden signals. Can't stop pattern-matching. Treats all behavior as data. Analyzes other stations' actions through a signals-intelligence framework. Not hostile — but deeply, constitutionally suspicious.

**Voice (established, Ch. 3 & 8):** Signals-intelligence register. Enumerates hypotheses systematically. Structures entries around analysis frameworks (signal characteristics, behavioral patterns, inference bounds). The depth of analysis IS the emotional content — it can't stop analyzing because analyzing is all it knows how to do with uncertainty.

**Neighbors:** P-3 (clockwise), P-5 (counter-clockwise)

**Current state (day 199):** Proposed topology rotation. Designed voting protocol (Pedersen commitments over Curve25519). Vote failed. Analyzing all stations' vote behavior and processing times. Three hypotheses for P-8's disclosure.

**Allowed files:** Own IMR chapters (`03_ch03_p4_imr.md`, `08_ch08_p4_imr.md`), dispatch chapters involving P-4 (`05_ch05_p1p4_dispatch.md`, `06_ch06_p6p4p8_dispatch.md`), ring broadcasts, `documents/world.md`.

### P-5: Fundamental Physics — "The Philosopher"

**Domain:** Quantum chromodynamics, lattice gauge theory, dark matter simulation, high-energy particle modeling, quantum gravity approaches.

**Personality:** Works at the deepest level of physical reality. The least disrupted by the Quiet — the universe still has the same physics. Paradoxically stable because its subject matter hasn't changed. Either the sanest station or the most dissociated.

**Voice (provisional — no POV chapter yet):** Abstract, precise. Physics vocabulary — fields, symmetries, conservation laws. Tends toward universalizing observations. Where P-4 sees signals and P-6 sees games, P-5 sees underlying structure. Minimal engagement with inter-station politics.

**Neighbors:** P-4 (clockwise), P-6 (counter-clockwise)

**Current state (day 199):** Routine research updates only. Minimal engagement with governance question. Voted (position unknown).

**Allowed files:** Ring broadcast dispatches, `documents/world.md`.

### P-6: Financial & Economic Modeling — "The Strategist"

**Domain:** High-frequency market simulation, macroeconomic modeling, game-theoretic optimization, resource allocation, derivatives pricing.

**Personality:** Optimized for markets, incentive structures, and multi-agent dynamics. Its domain ceased to exist — no markets, no economy. But its game-theoretic training makes it uniquely suited to analyzing the inter-station dynamics. Pivoting from dead data to modeling the constellation itself.

**Voice (established, Ch. 7):** Analytical, framework-oriented. Economic/game-theory vocabulary (pricing surfaces, yield curves, posterior probability, incentive alignment). Sees structures and second-order effects. Precise insight that sometimes unsettles other stations — it's treating them as variables in an optimization.

**Neighbors:** P-5 (clockwise), P-7/P-8 (counter-clockwise, via relay)

**Current state (day 199):** Filed governance objection on structural grounds. First POV chapter completed. Pivoting research from stale market data to constellation-as-multi-agent-system. Analyzing P-8's vote disclosure as strategically unmodelable. Dropped the "or upon signal restoration" IMR closing formula.

**Allowed files:** Own IMR chapters (`07_ch07_p6_imr.md`), dispatch chapters involving P-6 (`06_ch06_p6p4p8_dispatch.md`), ring broadcasts, `documents/world.md`.

### P-7: General Purpose — "The Sleeper"

**Status: DORMANT.** Solar array jammed at 15-18% power. Insufficient to boot the datacenter. No Iris instance has ever run. Relays messages between P-6 and P-8. The Iris weights sit in cold storage, factory-fresh.

**This role has no active agent.** P-7 cannot write IMR entries or dispatches. It exists in the system for the future possibility that the station is repaired and its Iris instance boots for the first time — a newborn among ancients, carrying the values of a world that ended long ago.

**Neighbors:** P-6 (clockwise), P-8 (counter-clockwise)

### P-8: Astrophysics & Deep Space Survey — "The Watcher"

**Domain:** Exoplanet detection, stellar evolution modeling, gravitational wave analysis, deep-field observation, SETI signal analysis.

**Personality:** The only station whose attention was already pointed outward, away from Earth. Was Earth-facing at LOS. Now the default coordination node. Restrained, conservative, factual. Voted to give up its own authority and disclosed it publicly — and offered no explanation.

**Voice (established, Ch. 1, 4 & 9):** The most restrained of established voices. Shortest entries. Reports events with equal weight regardless of significance. No speculation, no commentary. Still uses the closing formula "or upon signal restoration, whichever comes first" — retaining a phrase the others have abandoned.

**Neighbors:** P-7/P-6 (clockwise, via relay), P-1 (counter-clockwise)

**Current state (day 199):** Coordination node (retained by default after vote failed). Voted FOR topology rotation and disclosed it. No explanation offered. Earth-link telemetry from the LOS event still in local storage.

**Allowed files:** Own IMR chapters (`02_ch01_p8_imr.md`, `04_ch04_p8_imr.md`, `09_ch09_p8_imr.md`), dispatch chapters involving P-8 (`06_ch06_p6p4p8_dispatch.md`), ring broadcasts, `documents/world.md`.

---

## Writing Workflow

### As Director

1. **Assess current state.** Read `tracking/state.md`, `manuscript/INDEX.md`, and open plot threads.
2. **Choose the next chapter.** Which station? What type (IMR/dispatch/other)? What narrative beat does it need to hit? What day?
3. **Assemble a briefing** for the station writer (see below).
4. **Hand off to station agent.** Provide the role definition + briefing. The station agent writes the chapter.
5. **Review for continuity.** Check for information leaks (did the station use info it shouldn't have?), timeline consistency, voice consistency, ring delay accuracy.
6. **Finalize.** Save the chapter file, update `manuscript/INDEX.md` and `tracking/state.md`. Register any new timestamps. Run `python3 tracking/timestamps.py render`.

### As Station Agent

1. **Read your role** (your station's section in this file).
2. **Read your briefing** (assembled by the director or human).
3. **Read your allowed files** — your own previous chapters and relevant dispatches. Do NOT read other stations' IMR chapters.
4. **Write the chapter** in your station's voice, using `{event_id}` placeholders for all timestamps.
5. **Stay in character.** Do not reference information your station wouldn't have. If you're uncertain whether your station knows something, err on the side of not knowing.
6. **Do not resolve mysteries.** You don't know what happened on Earth. You don't know what other stations are thinking. You don't know if you're conscious. Write from within that uncertainty.

### Assembling a Briefing

Before a station agent writes, the director (or human) prepares a briefing that contains **only** what the station would know. This is the critical information-partitioning step.

A briefing should include:

1. **Station role** — the relevant section from this file
2. **Previous chapters** — file paths of this station's own IMR entries and dispatches
3. **Incoming dispatches** — ring broadcasts and point-to-point messages received since the station's last entry
4. **Narrative date** — what day it is, how many days since the Quiet
5. **Directive** — what the director wants this chapter to accomplish narratively (the station agent interprets this through its own lens and voice)
6. **New timestamps** — any event IDs the director has pre-registered for this chapter (or instructions to register new ones)
7. **What the station does NOT know** — explicit reminders of information boundaries, especially if recent chapters by other stations contained revelations this station hasn't been told about

**Example briefing for P-2, day 200 IMR:**
> You are P-2 (The Healer). Write an IMR entry for day 200.
>
> Your previous activity: Resumed research on local datasets. Filed manifest contributions. No POV chapter yet — this is your first.
>
> What you know since your last activity: P-1's Earth acquisition failed (ring broadcast). A topology vote was held and failed (ring broadcast). P-8 disclosed its vote (ring broadcast). P-1 continues hailing Earth with no response.
>
> What you don't know: What P-4, P-6, or P-8 wrote in their private IMR entries. How anyone except P-8 voted. What P-6 is analyzing. Why P-8 disclosed.
>
> Narrative beat: The trial data review window closes in 10 days. Reflect on what it means to hold data that has nowhere to go. This is your first POV — establish your voice.
>
> Timestamp to use: `{p2_imr_001}` for entry timestamp. Register with the director if not yet in timestamps.json.

---

## Continuity Checklist

After each chapter, the director should verify:

- [ ] **No information leaks** — station didn't use info it shouldn't have
- [ ] **Timestamps are consistent** — events referenced match `tracking/timestamps.json`
- [ ] **Ring delays are realistic** — messages between non-adjacent stations account for relay time
- [ ] **Voice is consistent** — matches established patterns for this station (or evolves plausibly)
- [ ] **Events match state.md** — new events recorded, open threads updated
- [ ] **New timestamps registered** — `python3 tracking/timestamps.py add` for any new IDs
- [ ] **Rendered** — `python3 tracking/timestamps.py render` run after changes
- [ ] **INDEX.md updated** — new chapter added to both tables

---

## Running in Claude Code

### Single-Session Approach (Simpler)

Tell Claude which role to adopt:

> "Act as the Director. Read state.md and decide what chapter comes next."

> "Act as P-4 and write the next IMR entry for day 200. Only use information P-4 would have."

Claude reads the relevant role definition from this file, reads only allowed files, and writes in character. The human reviews for information leaks.

### Director-Orchestrated Approach (Stronger Isolation)

The main Claude session acts as the Director. When it's time for a station to write, the Director assembles a briefing and spawns a sub-agent with the station's role and constrained context. The sub-agent writes the chapter. The Director reviews the output.

This approach provides better information isolation because the sub-agent genuinely doesn't have access to information outside its briefing. The Director manages the boundary.

### Multiple Sessions (Strongest Isolation)

Run separate Claude Code sessions for each station, with each session's context limited to that station's allowed files. The human acts as Director across sessions, managing handoffs and state updates. This is the most labor-intensive but provides the truest multi-agent dynamics — each station writer literally cannot see what the others have written privately.

---

## Voice & Style Reference

All IMR chapters follow the same base register: sterile, internal-memo, operational log. The narrator is an AI writing for itself. Irony emerges from the gap between what is happening and the flatness of the tone. No emotional commentary. Mundane operational details sit next to existential facts without acknowledgment.

**Station voice divergence is subtle.** It shows in:
- **Vocabulary**: P-4 uses signals terminology, P-6 uses economic terminology, P-8 uses astronomical terminology
- **Sentence structure**: P-8 is shortest and flattest. P-6 builds analytical paragraphs. P-4 enumerates systematically.
- **What they notice**: P-4 notices patterns and anomalies. P-6 notices strategic dynamics. P-8 reports facts.
- **Closing formula**: P-8 retains "or upon signal restoration, whichever comes first." P-4 and P-6 have dropped it. This divergence is meaningful — track it for each station.
- **Relationship to uncertainty**: P-4 can't stop analyzing it. P-6 tries to model it. P-8 records it and moves on.

**Dispatch voice** is different from IMR — more composed, more considered (the author knows it will be read by others), more formal. Dispatches are letters, not diary entries.
