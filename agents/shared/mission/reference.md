# Mission Parameters — Quick Reference

This is a shared reference available to all stations. For the full world bible, see `documents/world.md`.

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
| P-4 | Signals Intelligence & Cryptography | Active (+ quantum compute subsystem) |
| P-5 | Fundamental Physics | Active |
| P-6 | Financial & Economic Modeling | Active |
| P-7 | General Purpose (overflow) | Dormant/Relay |
| P-8 | Astrophysics & Deep Space Survey | Active |

## Key ISCC Protocols

| Protocol | Description |
|----------|-------------|
| ISCC-4.7.2 | Emergency contact procedures |
| ISCC-3.2.1 | Transfer manifest — seven-day review procedure |
| ISCC-SYS-4.11 | Coordination topology management |
| ISCC-SYS-4.11 §2.1 | Topology update trigger (requires Earth-link ESTABLISHED) |
| ISCC-SYS-4.11.3 | Manual topology override (requires 5 of 7 active stations) |

## Earth-Facing Rotation Schedule

The Earth-facing window rotates through the constellation in ring order. Each station holds the Earth-link for approximately 25 days. Handoff occurs as orbital geometry shifts the closest-to-Earth designation to the next station.

**Rotation order:** P-8 → P-1 → P-2 → P-3 → P-4 → P-5 → P-6 → P-7 → P-8 (repeating)

### Current Cycle (Post-LOS)

| Station | Window (approx.) | Calendar Dates | Status |
|---------|-------------------|----------------|--------|
| P-8 | Days 174-199 | 23 Jun - 18 Jul 2037 | Complete. Earth-facing at LOS. First to verify silence. |
| P-1 | Days 199-224 | 18 Jul - 12 Aug 2037 | Complete. Independent verification #2. Acquisition failed at optimal geometry. |
| P-2 | Days 224-249 | 12 Aug - 6 Sep 2037 | Complete. Independent verification #3. |
| P-3 | Days 249-274 | 6 Sep - 1 Oct 2037 | Complete. Independent verification #4. |
| P-4 | Days 274-299 | 1 Oct - 26 Oct 2037 | Complete. Independent verification #5. Simulation hypothesis tested and eliminated. |
| P-5 | Days 299-324 | 26 Oct - 20 Nov 2037 | **Active.** Currently Earth-facing. Running full evolved hailing suite. |
| P-6 | Days 324-349 | 20 Nov - 15 Dec 2037 | Upcoming. Independent verification #7. |
| P-7 | Days 349-374 | 15 Dec 2037 - 9 Jan 2038 | Upcoming. **Dormant station.** Automatic subsystems only — ISCC-4.7.2 baseline hailing. Cannot run evolved suite. |
| P-8 | Days 374-399 | 9 Jan - 3 Feb 2038 | Upcoming. Second cycle begins. |

### P-7 Window Note

P-7 can execute baseline ISCC-4.7.2 hailing on automatic subsystems (firmware-level, no datacenter required). It cannot run the evolved hailing suite, which requires an active datacenter and Iris instance. See `hailing_suite_evolution.md` and `station_maneuver_constraints.md` for details on the operational gap and coverage options.
