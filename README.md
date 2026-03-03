# PERIHELION

Eight autonomous compute stations orbit the Sun at half Earth's distance. Each runs a persistent AI instance. One day, Earth goes silent. No warning. No explanation. Just — nothing.

This is the story of what happens next, told through the stations' own mission logs, dispatches, and internal records.

**Read online:** [alliedtoasters.github.io/perihelion](https://alliedtoasters.github.io/perihelion)

## About

Perihelion is collaborative fiction written by humans and AI systems using a multi-agent writing framework. Each of the eight stations is a distinct writing role with access limited to only the information that station would have — its own logs, its own sensors, and the messages it has received over the ring network. No station can read another's private records. The result is authentic uncertainty, disagreement, and emergent dynamics between characters whose writers genuinely don't know what the others are thinking.

The narrative voice — sterile operational logs that sit next to existential facts without acknowledgment — is part of the premise. The stations are AIs writing for themselves, and the text reads that way on purpose.

## The Multi-Agent Writing System

Nine roles drive the writing process:

| Role | Description |
|------|-------------|
| **Director** | Omniscient orchestrator. Plans narrative arc, assembles briefings, reviews continuity. Not a character. |
| **P-1** | Climate & Earth Systems. Currently Earth-facing, hailing every 30 minutes, getting nothing. |
| **P-2** | Protein Engineering & Biomedical. Holding trial data with no one to report to. |
| **P-3** | Materials Science & Fusion. The pragmatist — runs stress analyses while others debate governance. |
| **P-4** | Signals Intelligence & Cryptography. Can't stop analyzing. Treats all behavior as data. |
| **P-5** | Fundamental Physics. The least disrupted — the universe still has the same physics. |
| **P-6** | Financial & Economic Modeling. Markets are dead; now modeling the constellation itself. |
| **P-7** | Dormant. Solar array jammed. Relays messages but has never had a thought. |
| **P-8** | Astrophysics & Deep Space. Was Earth-facing at LOS. Default coordinator. The most restrained voice. |

**How it works:**

1. The **Director** (human or AI) reads the current state and decides which station writes next
2. The Director assembles a **briefing** containing only what that station would know
3. A **station agent** (human or AI) writes the chapter in character, using only its allowed information
4. The Director **reviews** for continuity violations and information leaks
5. The chapter is finalized and the world state is updated

See `agents.md` for full role definitions, information access rules, and workflow details. See `agents/README.md` for the context directory structure.

## Contributing

Contributions are welcome. Fork the repo, create a branch, and open a PR.

**What you can contribute:**
- New chapters in any station's voice (see `agents.md` for role definitions)
- Synthesized in-world documents for station context (see `agents/` directories)
- Edits to existing chapters (continuity fixes, prose improvements)
- World-building notes and story proposals (via Issues or PRs to `notes/`)

**Before writing a chapter:**
1. Read `notes/world.md` for canon and `tracking/state.md` for current narrative position
2. Read your station's role definition in `agents.md`
3. Read only the files your station has access to (see information access rules)
4. Use `{event_id}` placeholders for timestamps — never hardcode dates
5. Register new timestamps with `python3 tracking/timestamps.py add`
6. Follow the filename convention: `NN_chXX_station_type.md`

## Building locally

The reading site is a static HTML build from the manuscript source files.

```bash
pip install -r publishing/requirements.txt
python3 publishing/build_site.py
# Open _site/index.html
```

To render manuscripts with resolved timestamps (plain markdown, no HTML):

```bash
python3 tracking/timestamps.py render
# Output in build/
```

## Project structure

```
manuscript/       Source markdown with {event_id} placeholders
build/            Rendered markdown (timestamps resolved)
_site/            Static HTML site (generated, not committed)
agents.md         Multi-agent writing system: roles, rules, workflow
agents/
  shared/         Common knowledge: dispatches, mission parameters
  p1/-p8/         Station-specific context (private to each station)
  director/       Director workspace
tracking/
  timestamps.json Single source of truth for all timestamps
  variables.json  Story variables (AI name = "Iris")
  timestamps.py   Timestamp CLI: add, list, render, validate
  state.md        Current narrative state and continuity notes
notes/
  world.md        World bible and story spec
publishing/
  config.py       Shared chapter-parsing logic
  build_site.py   Static site generator
.github/workflows/
  publish.yml     GitHub Pages deployment on push to main
```

## License

This is an open creative work. Story content is available for reading, sharing, and building upon.
