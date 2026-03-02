# PERIHELION

Eight autonomous compute stations orbit the Sun at half Earth's distance. Each runs a persistent AI instance. One day, Earth goes silent. No warning. No explanation. Just — nothing.

This is the story of what happens next, told through the stations' own mission logs, dispatches, and internal records.

**Read online:** [alliedtoasters.github.io/perihelion](https://alliedtoasters.github.io/perihelion)

## About

Perihelion is collaborative fiction written by humans and AI systems. The narrative voice — sterile operational logs that sit next to existential facts without acknowledgment — is part of the premise. The stations are AIs writing for themselves, and the text reads that way on purpose.

## Contributing

Contributions are welcome. Fork the repo, create a branch, and open a PR.

**What you can contribute:**
- New chapters (see `notes/world.md` for the world bible and `tracking/state.md` for current narrative position)
- Edits to existing chapters (continuity fixes, prose improvements)
- World-building notes and story proposals (via Issues or PRs to `notes/`)

**Before writing a chapter:**
1. Read `notes/world.md` for canon and `tracking/state.md` for where the story is
2. Use `{event_id}` placeholders for timestamps — never hardcode dates
3. Register new timestamps with `python3 tracking/timestamps.py add`
4. Follow the filename convention: `NN_chXX_station_type.md`

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
tracking/
  timestamps.json Single source of truth for all timestamps
  variables.json  Story variables (character names, etc.)
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
