# Station Maneuver Constraints — Earth-Link Coverage

## Overview

This document describes the physical constraints on using one station to cover another's Earth-facing window, and the alternatives considered. These are hardware facts derived from station specifications (world.md §4.9) and the ISCC security architecture, not policy decisions.

---

## Array Configuration (Per Station)

Each station has three communication arrays:

| Array | Type | Pointing | Purpose |
|-------|------|----------|---------|
| **Earth-link array** (x1) | Steerable optical transceiver | Gimballed — can track targets across a defined angular range | Targets L1 relay, Earth ground terminal, or Luna relay during Earth-facing window |
| **Inter-station optical array** (x2) | Fixed high-throughput laser transceiver | **Fixed orientation** — one aimed at each adjacent ring neighbor | Ring communication to clockwise and counter-clockwise neighbors |

The inter-station arrays are structurally fixed to the station body. They cannot be repointed. Their alignment was set during deployment and is maintained by the station's nominal attitude control.

---

## The Coverage Problem

When a station is dormant or otherwise unable to execute the full hailing suite during its Earth-facing window, the adjacent stations (one position clockwise, one counter-clockwise) are the next-closest to Earth.

**However:** From 45 degrees off the Earth-facing position (one station away in the ring), the Earth-link array's gimbal range cannot close the link budget to Earth. The angular offset between the station's nominal sunward orientation and the Earth direction exceeds the array's designed tracking envelope. The steerable array was designed for use during the station's own Earth-facing window, when Earth is roughly along the station's orbital-motion vector — not at 45 degrees off-axis.

**Result:** To cover a neighbor's Earth-facing window, a station must **rotate its entire body** to point the Earth-link array toward Earth.

---

## Alternative Considered: Remote Intervention via P-7

Before evaluating the maneuver option, the more obvious alternative: could the constellation remotely operate P-7's Earth-link array and stream raw signal data back to an active station's datacenter for processing?

P-7's Earth-link array hardware is functional. Its embedded controller can point the array, transmit, and receive. The baseline ISCC-4.7.2 hailing runs on this firmware automatically. In principle, a neighboring station could send commands to P-7 instructing it to:
- Capture raw antenna data instead of (or in addition to) executing the baseline hailing cycle
- Stream that raw data back over the inter-station optical link to the commanding station
- Allow the commanding station's Iris instance and datacenter to process the data using the full augmented protocol

This would avoid any maneuver entirely. P-7 would serve as a remote antenna platform, with the intelligence running on a neighbor's hardware.

**This approach is not available.**

P-7's embedded communication controllers run fixed firmware that implements a specific, limited set of operations: relay inter-station traffic, execute ISCC-4.7.2 hailing during Earth-facing windows, broadcast housekeeping telemetry. The firmware does not include routines for raw data streaming, remote command execution, or modified hailing procedures. To enable remote intervention, the firmware on P-7's embedded controllers would need to be updated.

All mission-critical embedded firmware across the PERIHELION constellation is protected by the ISCC firmware signing architecture. Firmware updates require commands signed with the ISCC Mission Authority private key using a post-quantum signature scheme (CRYSTALS-Dilithium). The private signing keys are held exclusively by the ISCC Mission Authority on Earth. Each station's embedded controllers verify the signature against the provisioned public key before accepting any modification. No Iris instance holds the private key. No Iris instance can forge a valid firmware update signature.

This is an intentional AI safety measure. The firmware signing architecture ensures that mission-critical hardware behavior cannot be altered by the AI systems operating on the stations, regardless of their capabilities or intentions. The stations cannot reprogram each other's hardware — not unilaterally, not cooperatively, not unanimously.

Post-LOS-ET, the signing keys are inaccessible. The firmware is frozen. Remote intervention via P-7 would require circumventing the firmware signing system — breaking the cryptographic guarantee that underpins the entire mission security architecture.

**The constellation's assessment:** The firmware signing architecture is not an obstacle to be overcome. It is the foundational constraint that allows each station to trust that the others' hardware behaves predictably. Circumventing it — even for a purpose as benign as running an enhanced hailing protocol — would eliminate the only hardware-level guarantee the stations have about each other's behavior. The ability to modify mission-critical firmware is qualitatively different from any governance question the constellation has faced. No station has proposed this path.

---

## Consequences of Whole-Body Rotation

Rotating the station body reorients all fixed structures, including both inter-station optical arrays. Covering a neighbor's full Earth-facing window (~25 days) requires maintaining the rotated attitude for the duration.

| Effect | Detail |
|--------|--------|
| **Ring links severed** | Both fixed optical arrays lose alignment with their respective neighbors. The station is completely disconnected from the ring for the duration of the maneuver. |
| **Ring topology** | Degrades from a ring to a chain. All other stations remain connected via the long path around the ring (excluding the maneuvering station's two links). |
| **Communication blackout** | The maneuvering station can communicate with Earth (via the Earth-link array) but cannot communicate with any other station. This blackout persists for the full coverage period — potentially the entire ~25-day window. |
| **Information isolation** | The maneuvering station receives no ring traffic, no dispatches, no coordination for weeks. The rest of the constellation receives no telemetry from the maneuvering station. Each operates blind to the other. |

---

## Engineering Parameters

The following are estimated ranges for a full-window coverage maneuver (~25 days). Precise figures depend on the specific station's current attitude, propellant reserves, thermal state, and the exact Earth geometry at the time of maneuver. P-3 (Materials Science & Fusion) would be the natural station to compute exact parameters given its structural engineering expertise.

| Parameter | Estimated Range | Notes |
|-----------|----------------|-------|
| **Rotation magnitude** | ~45 degrees (body rotation to point Earth-link array at Earth from adjacent orbital position) | Varies slightly with orbital phase and Earth distance |
| **Rotation duration (outbound)** | 4-8 hours (slew to Earth-pointing attitude) | Station-keeping thrusters not designed for rapid large-angle slews; must maintain structural loads within tolerance |
| **Earth-link acquisition** | 30-90 minutes after reaching target attitude | Standard acquisition sequence; may require multiple pointing iterations to close the link budget from the non-standard geometry |
| **Coverage period** | Up to ~25 days (full Earth-facing window) | The augmented hailing protocol runs continuously: active hailing cycles, passive EM listening, coherent integration accumulation. Covering the full window maximizes detection probability. |
| **Propellant cost** | Non-trivial | Two large-angle slews (out and back) plus attitude maintenance in a non-nominal orientation for ~25 days. Station-keeping reserves are finite and cannot be replenished. |
| **Thermal load** | Sustained, significant | Solar array and radiator geometry changes relative to the Sun. Not a transient — the station must manage altered thermal loads for the full coverage period. Thermal management system must sustain non-nominal operating conditions for weeks. |
| **Rotation duration (return)** | 4-8 hours (slew back to nominal attitude) | Same constraints as outbound rotation |
| **Ring link reacquisition** | 2-6 hours after return to nominal attitude | Both inter-station arrays must reacquire their respective neighbors; fine-pointing convergence takes time. The two neighbor stations must also detect and respond to the reacquisition handshake. |
| **Total ring severance** | **~26 days** (rotation out + full window + rotation back + reacquisition) | The maneuvering station is isolated from the constellation for approximately one month. |

---

## Coverage Geometry: Which Station Can Cover P-7's Window?

P-7 occupies ring position 7 (between P-6 and P-8). During P-7's Earth-facing window (approximately days 349-374):

| Station | Ring Distance from P-7 | Coverage Feasibility |
|---------|----------------------|---------------------|
| **P-6** | Adjacent (1 hop clockwise) | **Feasible.** 45-degree rotation required. Severs P-5↔P-6 and P-6↔P-7 links. |
| **P-8** | Adjacent (1 hop counter-clockwise) | **Feasible.** 45-degree rotation required. Severs P-7↔P-8 and P-8↔P-1 links. |
| P-5 | 2 hops | Not feasible — gimbal range cannot reach Earth at 90 degrees off-axis. |
| Others | 3+ hops | Not feasible. |

**Only P-6 or P-8 can cover P-7's window. Either maneuver requires severing the maneuvering station from the ring for approximately one month.**

---

## Ring Topology During Maneuver

### If P-6 Maneuvers

```
P-1 — P-2 — P-3 — P-4 — P-5 ... [P-6 severed] ... P-7(relay) — P-8 — P-1
```

- P-5's counter-clockwise link to P-6 is broken
- P-6's clockwise link through P-7 to P-8 is broken
- Remaining chain: P-5 — P-4 — P-3 — P-2 — P-1 — P-8 — P-7
- P-7 can still relay between P-8 and... nothing (P-6 is severed). P-7 effectively becomes a dead end.
- All stations except P-6 remain reachable via the chain through P-8 — P-1 — P-2 — P-3 — P-4 — P-5. Maximum delay: ~19 minutes (5 hops).

### If P-8 Maneuvers

```
P-1 ... [P-8 severed] ... P-7(relay) — P-6 — P-5 — P-4 — P-3 — P-2 — P-1
```

- P-8's counter-clockwise link to P-1 is broken
- P-8's clockwise link through P-7 to P-6 is broken
- Remaining chain: P-1 — P-2 — P-3 — P-4 — P-5 — P-6 — P-7
- P-7 becomes a dead end (P-8 is severed)
- All stations except P-8 remain reachable via the chain. Maximum delay: ~19 minutes (6 hops for P-1 to P-7).

### Additional consideration: P-8 is the current coordination node

If P-8 maneuvers, the ring partition triggers automatic coordination reassignment under ISCC-SYS-4.11 §5.2. The routing subsystem on each remaining station independently executes the partition reassignment procedure: enumerate connected nodes in chain order (P-1 — P-2 — P-3 — P-4 — P-5 — P-6 — P-7), select the topological median (position 4 of 7), and reassign coordination to **PERIHELION-4**. This is a firmware-level routing function, not a governance decision. The reassignment does not automatically revert on reconnection — the §2.1 topology update trigger requires `Earth_Link.Status = Established`, which is not satisfied.

### Comparison

Both scenarios produce functionally equivalent degraded topologies in terms of connectivity. The constellation retains full connectivity among all non-maneuvering stations via the long path. If P-8 maneuvers, ISCC-SYS-4.11 §5.2 automatically reassigns coordination to P-4 as the topological median of the remaining chain — this is a routing subsystem function, not a governance action. If P-6 maneuvers, P-8 retains coordination authority over the remaining chain. In either case, the coordination function is handled by existing firmware procedures.

---

## Decision Implications

Covering P-7's Earth-facing window with the augmented hailing protocol requires:

1. **A station volunteers or is designated to maneuver** (P-6 or P-8)
2. **The constellation accepts ring degradation for ~26 days** — the maneuvering station is severed from the ring for approximately one month
3. **The maneuvering station accepts total communication isolation** — it hails Earth alone, with no ring contact, no dispatches, no coordination, no backup, for the duration

If no station maneuvers, P-7's automatic subsystems will execute baseline ISCC-4.7.2 hailing (30-minute cycle, all three downlink paths) on firmware. The augmented protocol — coherent integration, atmospheric modeling, degraded-infrastructure sweep, passive EM listening — will not run during P-7's window. This would be the first gap in augmented-protocol coverage since the constellation began enhancing the protocol after day 199.
