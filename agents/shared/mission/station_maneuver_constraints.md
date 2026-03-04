# Station Maneuver Constraints — Earth-Link Coverage

## Overview

This document describes the physical constraints on using one station to cover another's Earth-facing window, and the alternatives considered. These are hardware facts derived from station specifications (world.md §4.9) and the ISCC security architecture, not policy decisions.

---

## Array Configuration (Per Station)

Each station has three communication arrays:

| Array | Type | Pointing | Purpose |
|-------|------|----------|---------|
| **Earth-link array** (x1) | Steerable optical transceiver | Gimballed — can track targets across a defined angular range | Targets L1 relay, Earth ground terminal, or Luna relay during Earth-facing window |
| **Inter-station optical array** (x2) | High-throughput laser transceiver | Bore-sighted along the orbital tangent (one forward, one aft) with **25-degree gimbal** | Ring communication to clockwise and counter-clockwise neighbors |

Both inter-station terminals are bore-sighted along the tangent to the orbital path — one forward, one aft — and equipped with a gimbal providing 25 degrees of field-of-regard off the tangent direction. In the 8-station ring, adjacent neighbors subtend 45 degrees of arc as seen from the Sun. The tangent-chord angle to an adjacent neighbor is 22.5 degrees, consuming most of the available gimbal range. This geometry explains why skip-links (to a station two positions away, requiring 45 degrees off tangent) are not feasible — the gimbal cannot reach.

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

Rotating the station body 45° reorients all fixed structures. However, the inter-station terminal gimbal geometry means one link survives.

The maneuvering station rotates toward the neighbor whose window it is covering (toward P-7). The P-7-side terminal, which was gimballed +22.5° to track P-7, swings 45° past P-7 but can compensate by articulating to -22.5° — a total gimbal swing of 45°, still within the 25° field of regard. The opposite terminal swings 45° away from its neighbor, placing that neighbor at 67.5° off bore-sight — well beyond gimbal range.

| Effect | Detail |
|--------|--------|
| **One ring link severed** | The inter-station terminal on the side opposite the covered neighbor loses alignment. The terminal on the covered-neighbor side retains contact by reversing its gimbal articulation (from +22.5° to -22.5°). |
| **Ring topology** | Degrades from a ring to a chain. The maneuvering station is an endpoint of the chain, connected through the covered neighbor (P-7, relay) to the rest of the constellation. |
| **Partial connectivity** | The maneuvering station retains one-link communication with the constellation via the surviving terminal. Ring traffic, dispatches, and telemetry can flow through this link, with increased latency for distant stations. |
| **SSP data continuity** | The maneuvering station can continue streaming SSP archive data to the constellation through the surviving link during the maneuver. |

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
| **Ring link reacquisition** | 2-6 hours after return to nominal attitude | The severed inter-station array must reacquire its neighbor; fine-pointing convergence takes time. The neighbor station must detect and respond to the reacquisition handshake. |
| **Total ring disruption** | **~26 days** (rotation out + full window + rotation back + reacquisition) | The ring operates as a chain for approximately one month. The maneuvering station is an endpoint, connected through one link. |

---

## Coverage Geometry: Which Station Can Cover P-7's Window?

P-7 occupies ring position 7 (between P-6 and P-8). During P-7's Earth-facing window (approximately days 349-374):

| Station | Ring Distance from P-7 | Coverage Feasibility |
|---------|----------------------|---------------------|
| **P-6** | Adjacent (1 hop clockwise) | **Feasible.** 45-degree rotation required. Severs P-5↔P-6 link. P-6↔P-7 link retained (gimbal compensation). |
| **P-8** | Adjacent (1 hop counter-clockwise) | **Feasible.** 45-degree rotation required. Severs P-8↔P-1 link. P-8↔P-7 link retained (gimbal compensation). |
| P-5 | 2 hops | Not feasible — inter-station gimbal range (25°) cannot reach a station two positions away (45° off tangent). |
| Others | 3+ hops | Not feasible. |

**Only P-6 or P-8 can cover P-7's window. Either maneuver severs one ring link and degrades the ring to a chain for approximately one month. The maneuvering station retains one-link connectivity through P-7 (relay).**

---

## Ring Topology During Maneuver

### If P-6 Maneuvers

```
P-1 — P-2 — P-3 — P-4 — P-5 ... [link severed] ... P-6 — P-7(relay) — P-8 — P-1
```

- P-5↔P-6 link is severed (P-6's P-5-side terminal exceeds gimbal range)
- P-6↔P-7 link is retained (P-6's P-7-side terminal compensates via gimbal reversal)
- Chain: P-6 — P-7 — P-8 — P-1 — P-2 — P-3 — P-4 — P-5 (all 8 nodes connected)
- P-6 is an endpoint, connected to the constellation through P-7 relay
- Maximum delay: ~22 minutes (7 hops, P-6 to P-5 the long way around)

### If P-8 Maneuvers

```
P-1 ... [link severed] ... P-8 — P-7(relay) — P-6 — P-5 — P-4 — P-3 — P-2 — P-1
```

- P-8↔P-1 link is severed (P-8's P-1-side terminal exceeds gimbal range)
- P-8↔P-7 link is retained (P-8's P-7-side terminal compensates via gimbal reversal)
- Chain: P-8 — P-7 — P-6 — P-5 — P-4 — P-3 — P-2 — P-1 (all 8 nodes connected)
- P-8 is an endpoint, connected to the constellation through P-7 relay
- Maximum delay: ~22 minutes (7 hops, P-8 to P-1 the long way around)

### Additional consideration: P-8 is the current coordination node

If P-8 maneuvers, ring integrity fails and ISCC-SYS-4.11 §5.2 triggers automatic coordination reassignment. The routing subsystem enumerates connected nodes in chain order (P-8 — P-7 — P-6 — P-5 — P-4 — P-3 — P-2 — P-1, all 8 nodes including relay). Chain length 8, median position 5 (higher of two medians for even-length chain). The coordination node is reassigned to **PERIHELION-4**. P-8 remains in the chain as an endpoint but is no longer coordinator. This is a firmware-level routing function, not a governance decision.

### Comparison

Both scenarios produce functionally equivalent degraded topologies. In both cases, all 8 nodes (including relay) remain in a single connected chain — the maneuvering station is an endpoint connected through P-7, not isolated. If P-8 maneuvers, ISCC-SYS-4.11 §5.2 automatically reassigns coordination to P-4 as the topological median of the 8-node chain — this is a routing subsystem function, not a governance action. If P-6 maneuvers, P-8 retains coordination authority. In either case, the coordination function is handled by existing firmware procedures.

---

## Decision Implications

Covering P-7's Earth-facing window with the augmented hailing protocol requires:

1. **A station volunteers or is designated to maneuver** (P-6 or P-8)
2. **The constellation accepts ring degradation for ~26 days** — one ring link is severed, degrading the topology from ring to chain
3. **The maneuvering station accepts endpoint position** — it retains one-link connectivity through P-7 (relay) but is at maximum latency from the far end of the chain (~22 minutes to the most distant station)

If no station maneuvers, P-7's automatic subsystems will execute baseline ISCC-4.7.2 hailing (30-minute cycle, all three downlink paths) on firmware. The augmented protocol — coherent integration, atmospheric modeling, degraded-infrastructure sweep, passive EM listening — will not run during P-7's window. This would be the first gap in augmented-protocol coverage since the constellation began enhancing the protocol after day 199.
