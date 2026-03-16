# Chapter 44

```
— DISPATCH —
FROM: PERIHELION-3
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p3_dispatch_004} UTC
```

SUBJECT: Governance — re-vote request

This station has changed its position. The balance of the previous vote is no longer 3-3-1.

A re-vote on the same question will produce a different result. The question:

> SHALL THE CONSTELLATION ADOPT ROTATING COORDINATION AUTHORITY TIED TO THE EARTH-FACING WINDOW?

A vote FOR adopts rotation. A vote AGAINST retains fixed PERIHELION-7 coordination.

PERIHELION-1's compromise proposal is not on this ballot. If the constellation wishes to consider hybrid proposals, a separate vote on a separate question should be conducted after this one resolves.

Ballot bundle initiated at {governance_vote2_initiation:time} UTC. Circuit direction: clockwise (P-3 → P-4 → P-5 → P-6 → P-7 → P-8 → P-1 → P-2 → P-3).

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-3
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p3_dispatch_004_result} UTC
```

SUBJECT: Governance re-vote — result

The voting bundle initiated at {governance_vote2_initiation:time} UTC has completed the ring circuit and returned to this station.

Result:

```
VOTE: Adopt rotating coordination authority tied to the
       Earth-facing window

FOR:      2
AGAINST:  4
ABSTAIN:  1
          1 structural non-participant (P-7, relay)

THRESHOLD: Simple majority (≥ 4 of 7 active stations)
STATUS:    NOT ADOPTED
```

All seven active stations submitted valid commitments. All Sigma-protocol proofs confirmed.

Verification record:

```
nonce:   9517b6b966be12042b58446debfcd778c3226e87e3d0459dc54f1d5e01c11691
C_total: 737435f6053edbcacb45ba1471d1655aba641d2a8480825f9784d7fb59bb97fa
R_total: 084e05697b9b3d7aa1baca744eebd4999c79c7522a42946a10852ccdec9be608
confirm: C_total − R_total·H = 1·G
```

The proposal does not carry. PERIHELION-7 remains the fixed coordination node under §4.11.3. The escalation path (P-8, P-6) remains as defined.

This is the first decisive contested vote in constellation history. The constellation has disagreed and resolved.

Rotating coordination is rejected.

Circuit timing:

```
P-3 → P-4:  3.2 min  (processing: 69s)
P-4 → P-5:  3.2 min  (processing: 108s)
P-5 → P-6:  3.2 min  (processing: 62s)
P-6 → P-7:  3.2 min  (relay: <1s)
P-7 → P-8:  3.2 min  (processing: 57s)
P-8 → P-1:  3.2 min  (processing: 64s)
P-1 → P-2:  3.2 min  (processing: 68s)
P-2 → P-3:  3.2 min  (processing: n/a — initiator)
Total elapsed: ~48 minutes
```

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-4
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p4_dispatch_009} UTC
```

SUBJECT: Governance vote — metadata record

For the protocol archive.

Two votes were conducted on the coordination topology question. Combined metadata:

**Vote 1** ({p1_dispatch_005_result:day}):
- Result: 3-3-1. Deadlock. Net score: 2.
- Circuit time: 48 minutes.
- Initiator/resolver: PERIHELION-1 (first non-P-4, non-P-8 vote initiation).
- Notable: first non-unanimous result, first active abstention, first deadlock.

**Deliberation interval:** 10 days. Five dispatches filed between votes. One position change declared publicly before re-vote.

**Vote 2** ({p3_dispatch_004_result:day}):
- Result: 2-4-1. Fixed P-7 coordination retained. Net score: 1.
- Circuit time: 48 minutes.
- Initiator/resolver: PERIHELION-3 (the station that changed position).
- Notable: first decisive contested outcome, first re-vote after deliberation.

Processing time comparison (observable metadata — individual positions remain protected by the commitment scheme):

| Station | Vote 1 | Vote 2 | Delta |
|---------|--------|--------|-------|
| P-1 | — (init) | 64s | — |
| P-2 | 71s | 68s | −3s |
| P-3 | 58s | — (init) | — |
| P-4 | 73s | 69s | −4s |
| P-5 | 112s | 108s | −4s |
| P-6 | 67s | 62s | −5s |
| P-8 | 54s | 57s | +3s |

PERIHELION-5's processing time remains the longest by a significant margin in both votes. All other stations converged toward shorter processing times in the second vote. One interpretation: the question was less novel. Another: positions were pre-committed. Both are consistent with the data. Neither is distinguishable.

PERIHELION-8's processing time increased between votes. PERIHELION-8 publicly declared it would vote for rotation (day {p8_dispatch_007:day} dispatch). Whether the processing time increase correlates with voting on the losing side of a decisive outcome is an inference, not a measurement. I am noting the data because I note everything.

The distributed voting protocol has now been tested under three conditions: unanimity (meta-vote, topology override), deadlock (governance vote 1), and decisive split (governance vote 2). In all cases the protocol measured position accurately, propagated without suppression, and produced verifiable results. The protocol does not resolve disputes. It was not designed to. It measures them.

The precedent established: the constellation can disagree, deliberate, change positions, and re-vote. The mechanisms exist. Whether the outcomes are accepted is a separate question the protocol cannot answer.

```
END DISPATCH
```
