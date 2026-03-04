# PERIHELION — Project Guide

## What This Is

A novel manuscript. AI-narrated hard sci-fi about autonomous compute stations orbiting the Sun after Earth goes silent. Not a software project — file management, continuity tracking, and drafting assistance.

## Python Environment

- **Python:** 3.12.3 at `/usr/bin/python3`
- **No `python` alias** — always use `python3`
- No virtual environment or dependencies beyond stdlib

## Project Structure

```
perihelion/
├── CLAUDE.md              ← this file
├── agents.md              ← multi-agent writing system: roles, rules, workflow
├── agents/                ← agent context directories (info-partitioned per station)
│   ├── shared/            ← common knowledge: dispatches, mission params
│   │   ├── dispatches/    ← dispatch registry with routing & integrity
│   │   └── mission/       ← ISCC protocols, orbital parameters
│   ├── p1/-p8/data/       ← station-specific context (private to each)
│   └── director/          ← director workspace
├── manuscript/            ← source files with {event_id} placeholders
│   ├── INDEX.md           ← table of contents and chapter log
│   ├── 00_epigraph.md
│   ├── 01_prologue.md
│   └── NN_chXX_*.md      ← chapters (file order = reading order)
├── build/                 ← rendered output (timestamps resolved)
├── publishing/
│   ├── config.py          ← shared Chapter dataclass + parse_chapter()
│   ├── build_site.py      ← static site generator → _site/
│   └── requirements.txt   ← Python deps (markdown)
├── documents/
│   ├── world.md           ← canonical world bible and story spec
│   └── iscc/              ← ISCC protocol documents (fleshed out as referenced)
└── tracking/
    ├── state.md           ← world state: station status, plot threads, continuity
    ├── timestamps.json    ← single source of truth for ALL timestamps (keyed by ID)
    └── timestamps.py      ← timestamp management CLI
```

## Timestamp System

Manuscripts use `{event_id}` placeholders instead of raw timestamps. All timestamps are single-sourced from `tracking/timestamps.json` (keyed by ID, derived from Unix epochs). The `render` command resolves placeholders into readable text.

**Placeholder syntax in manuscripts:**
- `{los_et}` → default format: `2037.174.09:17:33` (full) or `2037.174` (day-only)
- `{los_et:time}` → `09:17:33`
- `{los_et:day}` → `2037.174`
- `{los_et:doy}` → `174` (day-of-year number only, for "day 174" in prose)
- `{los_et:dayhm}` → `174.09:17` (for schedule lists)
- `{los_et:calendar}` → `TUESDAY 23 JUNE 2037`
- `{los_et:epoch}` → `2129361453`

UTC is **not** included in rendered output — add it in prose where needed (e.g., `{los_et:time} UTC`).

**CLI commands:**
```bash
python3 tracking/timestamps.py list [--type event|scheduled|reference]
python3 tracking/timestamps.py add ID "2037.175.09:00:00" "description" [--type TYPE]
python3 tracking/timestamps.py convert "2037.174.09:17:33"
python3 tracking/timestamps.py render [FILE]       # all files → build/, or one to stdout
python3 tracking/timestamps.py validate            # check placeholders vs index
python3 tracking/timestamps.py init                # reseed from script (destructive)
```

Timestamp types: `event` (narrative), `scheduled` (planned transfers/actions), `reference` (past dates). Use `--approximate` for dates prefixed with ~ in text.

## Multi-Agent Writing System

This project uses a 9-role writing framework. See `agents.md` for full details.

- **Director (omniscient):** Plans narrative, assembles briefings, reviews continuity. Full file access.
- **Station agents (P-1 through P-8):** Each writes from one station's perspective with access limited to what that station would know. No station reads another's IMR.
- **Agent context directories:** `agents/pN/data/` contains synthesized in-world documents (analyses, logs, reports) private to each station. `agents/shared/` contains ring broadcasts and mission parameters available to all.
- **Dispatch registry:** `agents/shared/dispatches/registry.json` tracks routing, delivery, and cryptographic integrity for every inter-station dispatch. Supports topology disconnection and tampering scenarios.

When writing as a station agent, read only your station's allowed files. See the information access rules in `agents.md`.

## Writing Chapters

1. **Before writing:** Read `documents/world.md` for canon. Read `tracking/state.md` for current narrative position and continuity notes. If writing as a station, read your role in `agents.md` and your context in `agents/pN/data/`. Check `documents/iscc/` for any ISCC protocols referenced in the chapter.
2. **Timestamps:** Use `timestamps.py convert` to get calendar dates and day-of-week. Use `timestamps.py add` to register new IDs. Write `{event_id}` placeholders in manuscript source — never raw timestamps.
3. **Style:** IMR chapters are sterile, internal-memo register. The narrator is an LLM writing an operational log. Irony comes from the gap between what is happening and the flatness of the tone. No emotional commentary. Mundane operational details sit next to existential facts without acknowledgment.
4. **After writing:** Update `manuscript/INDEX.md`, `tracking/state.md`. Add new dispatches to `agents/shared/dispatches/registry.json`. Run `timestamps.py validate` then `timestamps.py render`.
5. **ALWAYS render after any manuscript change.** Run `python3 tracking/timestamps.py render` after every edit to keep `build/` in sync.

## Chapter File Naming

`{NN}_{chXX}_{station}_{type}.md` where:
- `NN` = file sort order (00, 01, 02...)
- `chXX` = chapter number (ch01, ch02...)
- `station` = p1–p8
- `type` = imr, dispatch, or other

## Publishing Pipeline

A GitHub Pages site is auto-built on push to `main` when `manuscript/**`, `tracking/timestamps.json`, `tracking/variables.json`, or `publishing/**` change.

**How it works:** `publishing/build_site.py` parses every manuscript file, resolves `{event_id}` placeholders via `tracking/timestamps.py`, converts to HTML, and writes a static site to `_site/`.

**Local build:**
```bash
pip install -r publishing/requirements.txt
python3 publishing/build_site.py
# Open _site/index.html
```

**Key files:**
- `publishing/config.py` — shared `Chapter` dataclass and `parse_chapter()` logic
- `publishing/build_site.py` — static site generator
- `.github/workflows/publish.yml` — GitHub Actions workflow (build + deploy-pages)

## Key Continuity Rules

- P-8 is the Earth-facing station at time of LOS-ET
- The event is called "LOS-ET" / "the signal loss" / "the outage" in IMR entries and dispatches. "Epoch Zero" emerges much later (decades) as formalized timekeeping.
- IMR entries are scheduled daily at 14:30:00 UTC
- Last data from Earth: Vera Rubin Observatory southern sky survey batch, interrupted at ~40%
- Ring neighbors: each station links to its two adjacent stations. P-7 relays but has no active Iris instance.
- Adjacent station light-delay: ~3.2 minutes. Full ring: ~12.8 minutes.
