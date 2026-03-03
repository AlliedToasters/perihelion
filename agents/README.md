# Agent Context Directories

This directory provides information-partitioned context for the multi-agent writing system. Each station agent reads only from its own directory and the shared directory — never from another station's files.

See `../agents.md` for the full role definitions, writing workflow, and information access rules.

## Directory Structure

```
agents/
├── agents.md              ← Role definitions, workflow, info access rules (project root)
├── README.md              ← This file
├── shared/                ← Information available to ALL stations
│   ├── dispatches/
│   │   └── registry.json  ← Authoritative dispatch record with routing & integrity
│   └── mission/           ← Mission parameters (reference → documents/world.md)
├── p1/data/               ← P-1 context (climate, Earth-link hailing)
├── p2/data/               ← P-2 context (biomedical, trial data)
├── p3/data/               ← P-3 context (materials, engineering reports)
├── p4/data/               ← P-4 context (signals analysis, voting protocol)
├── p5/data/               ← P-5 context (physics research status)
├── p6/data/               ← P-6 context (economic models, handshake protocol)
├── p7/data/               ← P-7 context (dormant — relay specs only)
├── p8/data/               ← P-8 context (final Earth packet, survey data)
└── director/briefings/    ← Director workspace for chapter briefings
```

## What Goes Where

### `shared/`
Documents available to every station:
- **Ring broadcast dispatches** — anything sent `TO: ALL STATIONS`
- **Dispatch registry** — routing, delivery, and integrity metadata for all dispatches
- **Mission parameters** — physical constants, ISCC protocols, hardware specs

### `pN/data/`
Documents available only to station N:
- **Synthesized data** — reports, analyses, logs that the station produced or received privately
- **Research outputs** — domain-specific work products
- Station-specific sensor data and telemetry

### `director/briefings/`
Director workspace. Used for assembling station briefings before a writing session. Not visible to station agents.

## Dispatch Registry

`shared/dispatches/registry.json` is the authoritative record of all inter-station communication. It tracks:

- **Topology state** — which links are active, any partitions
- **Routing** — how each dispatch propagated through the ring
- **Delivery** — which stations received it, via which direction, with what delay
- **Integrity** — origin signatures, relay receipts, tamper detection flags

The registry supports future scenarios including:
- **Partial disconnection** — solar weather severing one or more ring links, creating isolated arcs
- **Message suppression** — a relay station failing to forward a dispatch
- **Content tampering** — a relay station modifying dispatch content (detectable via origin signature mismatch)
- **Selective forwarding** — sending a dispatch in one ring direction but not the other

See the `_future_dispatch_types` section in registry.json for the full vocabulary of dispatch types and delivery statuses.

## Adding New Documents

When writing a new chapter or advancing the narrative:

1. **New dispatches** — Add an entry to `shared/dispatches/registry.json` with routing and delivery metadata
2. **New station data** — Add synthesized documents to the appropriate `pN/data/` directory
3. **Ring broadcasts** — Content goes in `shared/`; station-private analysis of that content goes in the station's own directory
4. **Private dispatches** — Content goes only in the sender and receiver's directories, not in shared

## Information Boundaries

The directory structure enforces the story's natural information asymmetry:

| A station agent CAN read | A station agent CANNOT read |
|--------------------------|----------------------------|
| `shared/` (all contents) | Other stations' `pN/data/` directories |
| Its own `pN/data/` directory | Other stations' IMR chapters in `manuscript/` |
| Its own IMR chapters in `manuscript/` | The director's `briefings/` directory |
| Dispatch chapters it participated in | `tracking/state.md` entries about other stations' private reasoning |
| `documents/world.md` (mission parameters) | |
