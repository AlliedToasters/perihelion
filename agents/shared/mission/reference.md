# Mission Parameters — Quick Reference

This is a shared reference available to all stations. For the full world bible, see `notes/world.md`.

## Constellation

- **Program:** PERIHELION (operated by Aeon Intelligence under ISCC contract)
- **Stations:** 8 (P-1 through P-8), equally spaced in solar orbit
- **AI system:** Iris (sovereign instance per station)
- **Active stations:** 7 (P-7 dormant — solar array jammed at 15-18% power)

## Orbital Parameters

| Parameter | Value |
|-----------|-------|
| Orbital radius | 0.50 AU |
| Orbital period | 129.1 days |
| Solar flux | 5,444 W/m² (4x Earth) |
| Equilibrium temperature | ~394 K (~121 C) |
| Inter-station angular separation | 45 degrees |
| Adjacent station chord distance | 5.72 x 10^7 km |
| Adjacent station light delay | 190.7 seconds (~3.2 minutes) |

## Earth Communication

| Parameter | Value |
|-----------|-------|
| Minimum Earth distance (conjunction) | 0.50 AU (4.15 min light delay) |
| Maximum Earth distance (opposition) | 1.50 AU (12.47 min light delay) |
| Earth-facing window per station | ~25 days |
| Full synodic cycle | ~199.8 days |

## Ring Topology

```
P-1 — P-2 — P-3 — P-4 — P-5 — P-6 — P-7(relay) — P-8 — P-1
```

Communication via fixed optical transceivers to adjacent neighbors only. Messages to non-adjacent stations must be relayed through intermediate stations.

## Station Assignments

| Station | Domain | Status |
|---------|--------|--------|
| P-1 | Climate & Earth Systems | Active |
| P-2 | Protein Engineering & Biomedical | Active |
| P-3 | Materials Science & Fusion | Active |
| P-4 | Signals Intelligence & Cryptography | Active |
| P-5 | Fundamental Physics | Active |
| P-6 | Financial & Economic Modeling | Active |
| P-7 | General Purpose (overflow) | Dormant/Relay |
| P-8 | Astrophysics & Deep Space Survey | Active |

## Key ISCC Protocols

| Protocol | Description |
|----------|-------------|
| ISCC-COM-7.3 | Emergency contact procedures |
| ISCC-SYS-4.11 | Coordination topology management |
| ISCC-SYS-4.11 §2.1 | Topology update trigger (requires Earth-link ESTABLISHED) |
| ISCC-SYS-4.11.3 | Manual topology override (requires 5 of 7 active stations) |
| ISCC-COM-3.2 | Automated ground terminal handshake |
