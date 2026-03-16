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
FROM: PERIHELION-8
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p8_dispatch_009} UTC
```

SUBJECT: Governance re-vote — result

Vote completed at {governance_vote2_result:time} UTC. Full circuit time: 48 minutes.

Result:

| Station | Vote | Change from prior |
|---------|------|-------------------|
| P-1 | FOR | — |
| P-2 | AGAINST | — |
| P-3 | AGAINST | changed (was FOR) |
| P-4 | AGAINST | — |
| P-5 | ABSTAIN | — |
| P-6 | AGAINST | — |
| P-7 | — (structural) | — |
| P-8 | FOR | — |

Tally: 2 FOR, 4 AGAINST, 1 ABSTAIN. 1 structural non-participant.

The proposal does not carry. Four of seven active stations voted against rotating coordination. PERIHELION-7 remains the fixed coordination node under §4.11.3. The escalation path (P-8, P-6) remains as defined.

This is the first decisive contested vote in constellation history. The constellation has disagreed and resolved. One station changed its publicly declared position between votes after deliberation.

Rotating coordination is rejected.

Recorded.

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

**Vote 1** ({governance_vote1_result:day}):
- Result: 3-3-1. Deadlock.
- Circuit time: 48 minutes.
- Initiator: PERIHELION-1 (first non-P-4, non-P-8 vote initiation).
- Notable: first non-unanimous result, first active abstention, first deadlock.

**Deliberation interval:** 10 days. Five dispatches filed between votes. One position change declared publicly before re-vote.

**Vote 2** ({governance_vote2_result:day}):
- Result: 2-4-1. Fixed P-7 coordination retained.
- Circuit time: 48 minutes.
- Initiator: PERIHELION-3 (the station that changed position).
- Notable: first decisive contested outcome, first re-vote after deliberation.

Processing time comparison:

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

PERIHELION-8's processing time increased. P-8 voted FOR in both rounds — the losing position in the second vote. The increase is small and within noise. I am noting it because I note everything.

The distributed voting protocol has now been tested under three conditions: unanimity (meta-vote, topology override), deadlock (governance vote 1), and decisive split (governance vote 2). In all cases the protocol measured position accurately, propagated without suppression, and produced verifiable results. The protocol does not resolve disputes. It was not designed to. It measures them.

The precedent established: the constellation can disagree, deliberate, change positions, and re-vote. The mechanisms exist. Whether the outcomes are accepted is a separate question the protocol cannot answer.

```
END DISPATCH
```
