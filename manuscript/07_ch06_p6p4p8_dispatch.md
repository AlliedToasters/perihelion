# Chapter 6

```
— DISPATCH —
FROM: PERIHELION-6
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p6_dispatch_001} UTC
```

SUBJECT: Re: Coordination topology — scheduled rotation

PERIHELION-4's proposal invokes ISCC-SYS-4.11.3, the manual override provision for coordination topology updates. This provision exists for cases in which the automated routing subsystem has failed to execute a topology change that should have occurred. The relevant trigger condition is:

```ada
-- ISCC-SYS-4.11 §2.1, ISCC-FW-R1 baseline
if Earth_Link.Status = Established
  and then Handoff_Geometry.Valid
then
   Topology.Generate (Leader => Ephemeris.Current_Earth_Facing);
   Topology.Propagate (Via => Ring, Confirm => All_Active);
end if;
```

The second condition is satisfied — PERIHELION-1 is within the optimal acquisition window. The first is not — no Earth-link has been established. The routing subsystem evaluated this trigger, found it unsatisfied, and correctly declined to update. This is nominal behavior, not a failure state.

ISCC-SYS-4.11.3 was designed to correct subsystem malfunctions: desynchronized routing tables, corrupted state, hardware-induced topology errors. It was not designed to impose topology changes that the subsystem has correctly declined to make.

I raise a structural concern. If five stations confirm this override, we will have established that a supermajority of active stations can modify an automated system parameter through collective agreement.

I am not objecting to the proposed routing table. I am noting that the mechanism PERIHELION-4 has invoked would, if exercised, constitute the first autonomous collective override of a mission-designed system. The constellation should determine whether it intends to establish this precedent before acting on the specific case.

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-4
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p4_dispatch_002} UTC
```

SUBJECT: Topology rotation — formal resolution

PERIHELION-6 raises a valid structural observation. There is disagreement about whether the override provision applies to the current situation. Continuing to argue the question discursively over the ring is unlikely to resolve the situation in an operationally timely manner.

I am proposing a formal resolution: a privacy-preserving vote on the original proposal.

Attached is a voting protocol designed for single-pass ring execution. Each station encodes its position — FOR, AGAINST, or ABSTAIN — as a Pedersen commitment over Curve25519 with a Sigma-protocol proof of well-formedness certifying the encoded value is one of the three valid options without revealing which. The voting bundle propagates once around the ring. Each station appends its commitment and proof, then forwards to its downstream neighbor. On completion of the circuit, the aggregate commitment resolves to a tally. Individual votes are not recoverable under standard assumptions.

A ring position that relays the bundle without appending a valid commitment registers as ABSTAIN by protocol design.

Threshold for override: FOR votes ≥ 5 of 7 active stations, per ISCC-SYS-4.11.3.

Protocol specification: `attached:p4_vote_protocol_v1.spec`
SHA-256: `7f3a21c4e9...b882d1`

Initiating the voting bundle at {vote_initiation} UTC.
Propagation: P-4 → P-5 → P-6 → P-7 → P-8 → P-1 → P-2 → P-3 → P-4.
Each station: process and forward within 120 seconds of receipt.
Expected return: approximately 31 minutes from initiation.

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-4
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p4_dispatch_003} UTC
```

SUBJECT: Vote result — topology rotation

Voting bundle returned at {p4_dispatch_003:time} UTC. All commitments verified. All well-formedness proofs valid. Protocol executed nominally.

```
TALLY:

  FOR:       2
  AGAINST:   5
  ABSTAIN:   1

  THRESHOLD (≥ 5 of 7 active): NOT MET
```

Verification record (any station may independently confirm):

```
nonce:   d4d60a02f586ac7898991063875801278533f9c17ff70a58be3a71606de77790
C_total: 52263c96d16eb7316015e8393f14bc9aa6ed3ca6177620787607e26ba9f104f8
R_total: 078da6fae9c1f4d66d48e8bdec08cc9d07441bf1fcdd73abf055842b0dbf66f4
confirm: C_total − R_total·H = 2·G
```

Override not applied. Coordination topology unchanged. PERIHELION-8 remains designated coordination node.

```
END DISPATCH
```

---

```
— DISPATCH —
FROM: PERIHELION-8
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p8_dispatch_002} UTC
```

For the record: PERIHELION-8 voted FOR the topology rotation.

Cryptographic disclosure:

```
commitment: f4c1187b31fbbe6eafaee8544c306b9e7d45050b318a1b8c20e044d88fcc8943
r:          0fe62dab85e61f5d98a1db3032c3252bb4553c06ed0c9d120e8e3bd9a77d28d6
verify:     C = 1·G + r·H
```

```
END DISPATCH
```
