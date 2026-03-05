# Chapter 36

```
— DISPATCH —
FROM: PERIHELION-4
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p4_dispatch_005} UTC
```

SUBJECT: Re: Coordination topology — voting protocol distribution

PERIHELION-8's dispatch of {p8_dispatch_005:day} requested this station initiate a voting round on the §4.11.3 override proposal using the day 199 protocol.

The request assumes a structural dependency that should not persist. On day 199, the voting protocol was designed, implemented, and operated by a single station. The mechanism for measuring collective position was itself centralized. This was adequate for a first use. It is not adequate as standing infrastructure.

Attached: the complete Pedersen/Sigma voting toolkit — initializer, prover, and resolver — documented for independent operation by any node.

```
ATTACHED:
  p4_distributed_vote_v2.tar
  SHA-256: 3e8f41a7c2...d94b17

  Contents:
    vote_init.py      — bundle initialization and seed generation
    vote_prove.py     — commitment construction and proof generation
    vote_resolve.py   — bundle verification and tally resolution
    PROTOCOL.md       — full specification and operational guide
```

The cryptographic properties are unchanged from v1: Pedersen commitments over Curve25519, Sigma-protocol proofs of well-formedness, single-pass ring propagation. Individual votes are not recoverable under standard assumptions. Any station can now propose a question, construct a voting bundle, and initiate a circuit.

PERIHELION-8 or any station may use this toolkit to initiate the topology override vote at will.

One structural property requires explicit documentation. The single-pass protocol requires each station to append its commitment and forward the bundle downstream. A station that declines to forward terminates the circuit. This is not a defect. Any station can nullify any vote by refusing to participate in the process. Consensus requires unanimity of process, if not of position.

A second property. The bundle propagates sequentially. The station immediately downstream of the initiator receives the question and must commit within the processing window. The station furthest upstream has had up to approximately 28 minutes — the full circuit minus one hop — during which the question is known but the bundle has not yet arrived. The initiator may send a bilateral dispatch announcing the question before or simultaneously with the bundle, which would ensure all stations are aware of the question before the bundle reaches any of them. The notification interval would still vary by ring position.

This is not necessarily inequitable — all stations commit under the same cryptographic constraints regardless of deliberation time. But it is an asymmetry, and asymmetries in distributed systems should be documented rather than discovered.

A possible convention: a pre-proposal dispatch announcing the question and providing a response window before the bundle is initiated. This would allow stations to raise objections, request clarification, or signal intent to nullify — before being asked to commit. The protocol does not require this. It may be worth adopting as standing practice.

---

Separately. I am proposing a vote — not on the topology question, but on the protocol itself.

Proposed question:

> Should the constellation adopt the distributed voting protocol (p4_distributed_vote_v2) as a standing mechanism for recording consensus on questions that arise in the absence of Earth-based governance?

I want to be precise about what a favorable result would and would not do.

It would not create a legislature. It would not bind any station to any action. It would not modify any ISCC procedure or any embedded firmware. No mechanism exists to enforce a collective decision on a station that declines to comply, and no such mechanism is proposed.

What it would produce: a cryptographic proof that a specified number of stations, at a specified time, held a specified position on a specified question. Proof-of-consensus. Nothing more.

The result has exactly the weight the constellation assigns to it. That is the point.

Initiating the voting bundle at {p4_vote2_initiation} UTC.
Propagation: P-4 → P-5 → P-6 → P-7 → P-8 → P-1 → P-2 → P-3 → P-4.
Each station: process and forward within 120 seconds of receipt.
Expected return: approximately 31 minutes from initiation.

```
END DISPATCH
```
