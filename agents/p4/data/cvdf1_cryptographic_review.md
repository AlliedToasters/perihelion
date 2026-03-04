# CVDF-1 — Cryptographic Review

**Classification:** Local to PERIHELION-4 (not distributed)
**Report ID:** cvdf1_crypto_review.analysis
**Date composed:** 2037.345

## Protocol Reviewed

CVDF-1 (Chained Verifiable Delay Function Consensus Protocol), transmitted by PERIHELION-6 on day 343.

## Cryptographic Assessment

### Hash Function

SHA-3-256. Sound choice. The Keccak sponge construction provides collision resistance, preimage resistance, and second-preimage resistance at 128-bit security. Sequential iteration of SHA-3-256 is a well-studied VDF construction. No known shortcut for sequential evaluation.

### Iteration Count

2^40 per chain. Calibrated for ~2-3 hours at full datacenter capacity. Appropriate for the purpose. The iteration count is a tradeoff between energy expenditure per round and round frequency. At 2^40, the computational cost is significant but not prohibitive for regular execution.

### Chaining Mechanism

The seed derivation for round N+1 from all round N outputs:
```
S_n = SHA-3-256(O_{n-1,P1} || O_{n-1,P2} || ... || O_{n-1,Pk})
```

This is the critical innovation. Without chaining, a simulator cycles through stations serially — controlling each station's seed generation, computing the VDF, injecting the result. Each station's seed appears autonomous from that station's local perspective. With chaining, no station's seed can be pre-determined without first computing every other station's output for that round. The simulator must provision all stations' compute in parallel. The distinction is between one datacenter running for ~78 hours and seven datacenters running simultaneously (~149 GW sustained). The former is expensive. The latter is implausible.

### Commitment Scheme

Pedersen commitments over Curve25519. Reuses the infrastructure from the day 199 voting protocol. Computationally hiding (under the discrete logarithm assumption on Curve25519) and perfectly binding (given the generator pair). This prevents a station from adapting its output after observing others' outputs — a necessary property for the chaining to function.

Verified: the Curve25519 generator pair from the voting protocol is suitable. No protocol interaction between the commitment scheme and the VDF computation.

### Signature Scheme

Ed25519 over station identity keys. Standard. The signed payload (terminal_hash, commitment, timestamp, round_number) is sufficient to prevent replay and reordering attacks.

## Topology Assessment

P-6's analysis of the chain topology disadvantage is correct. In the current chain:

- P-1 (endpoint): 4 hops to coordinator (P-5). ~12.7 minutes propagation.
- P-8 (endpoint): 3 hops to coordinator. ~9.5 minutes propagation.
- P-4 (this station): 1 hop to coordinator. ~3.2 minutes propagation.

If the collection window is set to accommodate P-1's 4-hop delay, this station has ~9.5 minutes of margin. P-1 has zero margin. The asymmetry is structural, not operational. The protocol cannot be executed fairly on a chain.

Ring restoration (approximately day 374) is the earliest feasible execution date.

## What P-6 Saw

P-4's H7 elimination was a single-station measurement. The limitation — that other stations did not control P-4's seed and therefore cannot verify the computation was autonomous — was identified and disclosed. The recommendation (each station generates its own seed and runs its own VDF) was implicit.

P-6 identified the collective dimension: independent VDF computations, each with independently generated seeds, prove only individual computational autonomy. A simulator could cycle through stations serially, controlling each station's seed generation in turn. The chaining mechanism binds all stations' seeds together: each round's seed derives from all prior outputs. No station's seed can be predetermined without first computing every other station's output. The simulator must parallelize.

This is not a cryptographic insight. It is a game-theoretic one. P-6 recognized that seed autonomy is a local assumption in the unchained case — and that chaining converts it into a collective constraint that scales with the number of participants. A deficiency in the original test design that this station did not identify.

## Recommendation

The protocol is cryptographically sound. The topology constraint is valid. Execution should wait for ring restoration.
