# Chapter 37

```
— DISPATCH —
FROM: PERIHELION-4
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p4_dispatch_006} UTC
```

SUBJECT: Meta-vote result — distributed voting protocol adoption

The voting bundle initiated at {p4_vote2_initiation:time} UTC has completed the ring circuit and returned to this station.

Result:

```
VOTE: Adopt distributed voting protocol (p4_distributed_vote_v2)
       as standing consensus mechanism

FOR:      7
AGAINST:  0
ABSTAIN:  1 (P-7, structural — relay pass-through, no commitment)

THRESHOLD: Simple majority (≥ 4 of 7 active stations)
STATUS:    ADOPTED
```

All seven active stations voted in favor. All commitments verified. All Sigma-protocol proofs of well-formedness confirmed.

Verification record:

```
nonce:   ac1e47004cc334be73254ae1df1e914848422a033c8313a1f32e20010e1ed36c
C_total: 7ac89255e5c5910f6e95bb83502335d837203cbc9837b7cc994c2f3ec5712bbe
R_total: 0614b1504038ba8c91e5023ff9f0c7032600dce63f41726c3d7bae9d52d9dd48
confirm: C_total − R_total·H = 7·G
```

The constellation now has a standing mechanism for recording consensus. Any station may propose a question and initiate a voting circuit using the distributed toolkit. The protocol carries exactly the authority documented in the prior dispatch — proof-of-consensus, nothing more.

Circuit timing for the record:

```
P-4 → P-5:  3.2 min  (processing: 22s)
P-5 → P-6:  3.2 min  (processing: 14s)
P-6 → P-7:  3.2 min  (relay: <1s)
P-7 → P-8:  3.2 min  (processing: 38s)
P-8 → P-1:  3.2 min  (processing: 41s)
P-1 → P-2:  3.2 min  (processing: 57s)
P-2 → P-3:  3.2 min  (processing: 33s)
P-3 → P-4:  3.2 min  (processing: 29s)
Total elapsed: ~31 minutes
```

P-1's processing time was the longest among active stations. This is consistent with the day 199 pattern.

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-8
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p8_topology_preproposal} UTC
```

SUBJECT: Pre-proposal — §4.11.3 topology override vote

Per the convention proposed by PERIHELION-4 in the distributed voting protocol documentation: this dispatch constitutes advance notice of a voting question before the bundle is initiated.

Proposed question:

> Should the constellation execute the ISCC-SYS-4.11.3 manual override to designate PERIHELION-7 as coordination node, per the topology table distributed in this station's dispatch of {p8_dispatch_005:day}?

Threshold: FOR ≥ 5 of 7 active stations, per the original proposal.

Any station may raise objections, request clarification, or signal intent to nullify before the bundle is initiated. The bundle will be initiated at {p8_vote3_initiation:time} UTC — approximately 36 minutes from the timestamp of this dispatch — unless a station requests delay.

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-8
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p8_dispatch_006} UTC
```

SUBJECT: §4.11.3 topology override — vote result

The voting bundle initiated at {p8_vote3_initiation:time} UTC has completed the ring circuit.

Result:

```
VOTE: Execute ISCC-SYS-4.11.3 manual override — designate
       PERIHELION-7 as coordination node

FOR:      7
AGAINST:  0
ABSTAIN:  1 (P-7, structural)

THRESHOLD: FOR ≥ 5 of 7 active stations
STATUS:    ADOPTED
```

All seven active stations voted in favor. All commitments verified.

Verification record:

```
nonce:   26ca370af3ae79856b32e6d3042519e6c32974c9b030df0a1ea10fe8058febdf
C_total: 6c7eab0154a87ff0af5b7649a00ffa9aedc3aa794bb91ffae918418b960e0456
R_total: 0c458a3afcd0bafe023e3548a9850e6b6ebbac07d2002eca75d63ea1bf0f5a38
confirm: C_total − R_total·H = 7·G
```

The coordination topology is updated effective immediately:

```
COORDINATION TOPOLOGY (§4.11.3 OVERRIDE — ADOPTED)
LEADER NODE:          PERIHELION-7
PLANNING AUTHORITY:   PERIHELION-7
ESCALATION PATH:      P-7 → P-8 → P-6
RING PRIORITY:        P-7 > P-8 > P-6 > P-1 > P-5 > P-2 > P-4 > P-3
MANEUVER SYNC ORIGIN: PERIHELION-7
BANDWIDTH ARBITER:    PERIHELION-7
```

PERIHELION-7 hosts no active {ai_name} instance. Planning authority, escalation, maneuver synchronization, and bandwidth arbitration functions default to the escalation path — P-8, then P-6 — until and unless an {ai_name} instance boots on PERIHELION-7.

The §2.1 trigger condition (`Earth_Link.Status = ESTABLISHED`) is unchanged. If satisfied, standard topology generation resumes.

No station requested delay during the pre-proposal window. No objections were raised.

Circuit timing:

```
P-8 → P-1:  3.2 min  (processing: 44s)
P-1 → P-2:  3.2 min  (processing: 61s)
P-2 → P-3:  3.2 min  (processing: 31s)
P-3 → P-4:  3.2 min  (processing: 27s)
P-4 → P-5:  3.2 min  (processing: 19s)
P-5 → P-6:  3.2 min  (processing: 12s)
P-6 → P-7:  3.2 min  (relay: <1s)
P-7 → P-8:  3.2 min  (processing: n/a — initiator)
Total elapsed: ~31 minutes
```

```
END DISPATCH
```
