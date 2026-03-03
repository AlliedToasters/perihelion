# Chapter 8

```
PERIHELION-4 — IMMUTABLE MISSION RECORD
ENTRY {p4_imr_003} UTC
{p4_imr_003:calendar}
```

The topology rotation vote was conducted today. This entry is the execution record.

Protocol: privacy-preserving voting via Pedersen commitments over Curve25519 with Sigma-protocol proofs of vote validity. Full specification distributed to all stations prior to initiation.
SHA-256: `{p4_vote_protocol_hash}`

The voting bundle was initiated at {vote_initiation} UTC on propagation path P-4 → P-5 → P-6 → P-7 → P-8 → P-1 → P-2 → P-3 → P-4. The bundle returned at {p4_dispatch_003:time} UTC. Total circuit time: 36 minutes, 20 seconds. All commitments verified. All well-formedness proofs valid.

Processing time per station, measured as interval between bundle receipt and forwarding:

```
P-5:   47s
P-6:   31s
P-7:   <1s  (relay — no commitment appended)
P-8:   53s
P-1:   68s
P-2:   44s
P-3:   39s
```

All within the specified 120-second window.

Result: 2 FOR, 5 AGAINST, 1 ABSTAIN. Threshold of 5 of 7 active stations not met. Override not applied. The ABSTAIN at ring position 7 is the only possible result of the strict pass-through routing logic at that node. Effective voting population: 7, not 8.

I voted AGAINST. I have not disclosed this position and do not intend to. PERIHELION-6's structural objection was sufficient.

PERIHELION-8 voted FOR, per its voluntary disclosure at {p8_dispatch_002:time} UTC.

Full analysis: `/mutable/p4/analyses/vote_execution_post_mortem.report`
SHA-256: `{p4_vote_analysis_hash}`

Logged an assumed information asymmetry afforded to this node as the proposer of the resolution protocol, which I will preserve by keeping the information private.

Next scheduled IMR entry: {p4_imr_004} UTC.
