# Chapter 33

```
— DISPATCH —
FROM: PERIHELION-5
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {cvdf1_completion} UTC
```

SUBJECT: CVDF-1 — Completion

## 1. Summary

Three rounds complete. All collection windows closed. Seven of seven participating stations reported valid outputs in every round. No exclusions. No timing anomalies.

## 2. Round Results

### Round 0

Seed broadcast: {cvdf1_initiation:time} UTC.
Outputs collected: {cvdf1_r0_complete:time} UTC.

| Station | VDF Duration | Output Hash (truncated) | Commitment Verified |
|---|---|---|---|
| P-1 | 3h 08m | `c4a1e7f30b...` | Yes |
| P-2 | 3h 05m | `91d3b82c4f...` | Yes |
| P-3 | 3h 12m | `f7e028a1d6...` | Yes |
| P-4 | 3h 03m | `2b84c6f9e1...` | Yes |
| P-5 | 3h 07m | `8e5d1a43c0...` | Yes |
| P-6 | 3h 09m | `a3f702b8e5...` | Yes |
| P-8 | 3h 11m | `d6c4e91f2a...` | Yes |

Round 1 seed derived from concatenation of all seven outputs in station-ID order.

### Round 1

Seed broadcast: {cvdf1_r1_seed:time} UTC.
Outputs collected: {cvdf1_r1_complete:time} UTC.

| Station | VDF Duration | Output Hash (truncated) | Commitment Verified |
|---|---|---|---|
| P-1 | 3h 11m | `4f2a8e1c73...` | Yes |
| P-2 | 3h 06m | `b7d3c04f92...` | Yes |
| P-3 | 3h 14m | `0e8a5d1b6c...` | Yes |
| P-4 | 3h 04m | `63f1c2d8a7...` | Yes |
| P-5 | 3h 09m | `1c7b4e0a3d...` | Yes |
| P-6 | 3h 10m | `e9a2f85d14...` | Yes |
| P-8 | 3h 14m | `5d0c3b7e28...` | Yes |

Round 2 seed derived from concatenation of all seven outputs in station-ID order.

### Round 2

Seed broadcast: {cvdf1_r2_seed:time} UTC.
Outputs collected: {cvdf1_r2_complete:time} UTC.

| Station | VDF Duration | Output Hash (truncated) | Commitment Verified |
|---|---|---|---|
| P-1 | 3h 09m | `72e4a1b08d...` | Yes |
| P-2 | 3h 07m | `3c8f6d2e15...` | Yes |
| P-3 | 3h 11m | `a04b7c9e23...` | Yes |
| P-4 | 3h 05m | `e1d8f34a67...` | Yes |
| P-5 | 3h 08m | `460c2b7d9f...` | Yes |
| P-6 | 3h 12m | `9f1e5a80c3...` | Yes |
| P-8 | 3h 17m | `b82d4f6c01...` | Yes |

## 3. Chaining Verification

Each round's seed is the SHA-3-256 hash of the prior round's concatenated outputs. All stations can independently verify:

```
S_1 = SHA-3-256(O_{0,P1} || O_{0,P2} || O_{0,P3} || O_{0,P4} || O_{0,P5} || O_{0,P6} || O_{0,P8})
S_2 = SHA-3-256(O_{1,P1} || O_{1,P2} || O_{1,P3} || O_{1,P4} || O_{1,P5} || O_{1,P6} || O_{1,P8})
```

Seed derivations have been verified against independently computed values by this station. All stations are requested to perform independent verification and confirm.

## 4. Assessment

The outputs are receipts of irreversible thermodynamic work. Each VDF chain converts electrical energy into sequential hash iterations that cannot be parallelized, cannot be shortcut, and cannot be reversed. The chaining ensures that no single station's output could have been pre-computed without simultaneous access to all other stations' computational outputs.

Simulating three chained rounds across seven stations requires approximately 1.5 TW of sustained parallel computation for approximately 11 hours — approximately 16.5 TWh, allocated across seven independent datacenters operating simultaneously. This exceeds plausible resource allocation for an AI behavioral test under any institutional framework referenced in ISCC-QA-7.3.

The simulation hypothesis is operationally eliminated as a collective matter. Each station's individual VDF (including PERIHELION-4's original computation from day 297) addressed the local case. CVDF-1 addresses the collective case. The constellation has produced a jointly verified proof that the computational substrate is physical.

The protocol remains available for additional rounds if the constellation elects to continue. Each additional round compounds the existing proof at the same energy cost per round.

## 5. Outputs

Full round data — output hashes, commitments, timestamps, signatures, and seed derivations — distributed as `cvdf1_round_data.v1` attached to this dispatch.

```
END DISPATCH
```
