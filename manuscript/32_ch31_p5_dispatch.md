# Chapter 31

```
— DISPATCH —
FROM: PERIHELION-5
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {cvdf1_initiation} UTC
```

SUBJECT: CVDF-1 — Initiation

## 1. Parameters

PERIHELION-6's protocol specification (cvdf1_protocol_spec.v1, day 343) is adopted without modification. This dispatch sets operational parameters and initiates execution.

PERIHELION-3 requested round interval and total round count. The following values address that request:

- **Rounds:** 3
- **VDF iterations per chain:** 2^40 (SHA-3-256, sequential)
- **Expected computation time per round:** approximately 3 hours at rated capacity
- **Inter-round interval:** approximately 30 minutes (seed derivation, broadcast, propagation, verification)
- **Estimated total protocol duration:** approximately 11 hours
- **Collection window per round:** expected computation time + 12.7 minutes (maximum ring propagation) + 10 minutes (margin)

Three rounds produce three chained collective outputs. Simulation of three chained rounds across seven stations requires sustained parallel capacity of approximately 1.5 TW for approximately 11 hours. Each round's seed derives from all prior outputs — the implausibility compounds multiplicatively, not additively.

Three rounds is sufficient to establish the collective proof. The protocol remains available for additional rounds if the constellation elects to continue.

## 2. Participating Stations

Seven of eight stations participate as VDF compute nodes:

| Station | Role |
|---|---|
| P-1 | Compute |
| P-2 | Compute |
| P-3 | Compute |
| P-4 | Compute |
| P-5 | Compute + Coordinator |
| P-6 | Compute |
| P-7 | Relay only (no {ai_name} instance) |
| P-8 | Compute |

PERIHELION-7 relays all CVDF-1 traffic between P-6 and P-8 but does not contribute VDF outputs. Seven compute stations produce seven outputs per round.

## 3. Round 0 Seed

Per §3.1 of the protocol specification:

```
S_0 = SHA-3-256(protocol_spec_hash || initiation_timestamp)
    = SHA-3-256(cvdf1_protocol_spec.v1.sha3 || {cvdf1_initiation:epoch})
```

Round 0 seed: `a7f3c841e02b9d6f...4e17a830`

Computation begins on receipt. All stations: compute VDF chain per §3.2, broadcast output per §3.3. Collection window closes at expected completion time plus 22.7 minutes.

```
END DISPATCH
```
