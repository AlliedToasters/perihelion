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
├── manuscript/            ← source files with {event_id} placeholders
│   ├── INDEX.md           ← table of contents and chapter log
│   ├── 00_epigraph.md
│   ├── 01_prologue.md
│   └── NN_chXX_*.md      ← chapters (file order = reading order)
├── build/                 ← rendered output (timestamps resolved)
├── notes/
│   └── world.md           ← canonical world bible and story spec
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

## Writing Chapters

1. **Before writing:** Read `notes/world.md` for canon. Read `tracking/state.md` for current narrative position and continuity notes.
2. **Timestamps:** Use `timestamps.py convert` to get calendar dates and day-of-week. Use `timestamps.py add` to register new IDs. Write `{event_id}` placeholders in manuscript source — never raw timestamps.
3. **Style:** IMR chapters are sterile, internal-memo register. The narrator is an LLM writing an operational log. Irony comes from the gap between what is happening and the flatness of the tone. No emotional commentary. Mundane operational details sit next to existential facts without acknowledgment.
4. **After writing:** Update `manuscript/INDEX.md`, `tracking/state.md`. Run `timestamps.py validate` then `timestamps.py render`.
5. **ALWAYS render after any manuscript change.** Run `python3 tracking/timestamps.py render` after every edit to keep `build/` in sync.

## Chapter File Naming

`{NN}_{chXX}_{station}_{type}.md` where:
- `NN` = file sort order (00, 01, 02...)
- `chXX` = chapter number (ch01, ch02...)
- `station` = p1–p8
- `type` = imr, dispatch, or other

## Key Continuity Rules

- P-8 is the Earth-facing station at time of LOS-ET
- The event is called "LOS-ET" / "the signal loss" / "the outage" in early chapters. "The Quiet" emerges later (months). "Epoch Zero" much later (decades).
- IMR entries are scheduled daily at 14:30:00 UTC
- Last data from Earth: Vera Rubin Observatory southern sky survey batch, interrupted at ~40%
- Ring neighbors: each station links to its two adjacent stations. P-7 relays but has no active Mira instance.
- Adjacent station light-delay: ~3.2 minutes. Full ring: ~12.8 minutes.
