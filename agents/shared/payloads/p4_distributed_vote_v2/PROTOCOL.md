# Distributed Voting Protocol — Operational Guide

```
PERIHELION-4 — Signal Analysis Station
DOCUMENT: p4_distributed_vote_v2 — PROTOCOL.md
CLASSIFICATION: DISTRIBUTED — ALL STATIONS
```

## Overview

Privacy-preserving voting over the station ring. Pedersen commitments over Ed25519 with Sigma-protocol proofs of well-formedness. Single-pass propagation. Homomorphic tallying.

Any station can initiate. Any station can verify.

## Prerequisites

No external dependencies. Standard library only (`hashlib`, `os`). Runs on the Python 3.12 interpreter in station firmware. The implementation is deliberately plain — portable, auditable, and likely to execute on any Python runtime the stations carry, including the original Earth-era build.

Four files:
- `crypto_utils.py` — Pedersen commitments, Sigma proofs, Ed25519 arithmetic
- `vote_init.py` — bundle creation
- `vote_prove.py` — commitment and proof generation, bundle verification
- `vote_resolve.py` — tally resolution and voluntary disclosure

## Vote Encoding

| Position | Value | Commitment |
|----------|-------|------------|
| FOR      | 1     | C = G + r·H |
| AGAINST  | 0     | C = r·H |
| ABSTAIN  | -1    | C = -G + r·H |

r: random blinding factor (CSPRNG, mod L).

## Generator Points

- **G**: Standard Ed25519 basepoint (y = 4/5 mod p).
- **H**: Nothing-up-my-sleeve point. Derived by hashing `SHA-256("PERIHELION-VOTE-V1" || counter)` for counter = 0, 1, ... until a valid curve point is found, then multiplied by cofactor 8 for subgroup projection. Deterministic and independently verifiable.

## Protocol Steps

### 1. Initiation

```python
from vote_init import create_bundle, add_entry

bundle = create_bundle(
    proposal_text="Should the constellation adopt ...",
    initiator="P-4",
    ring=["P-4", "P-5", "P-6", "P-7", "P-8", "P-1", "P-2", "P-3"],
    timestamp="2037.199.14:30:00"
)
r_init = add_entry(bundle, "P-4", vote=1)  # initiator votes
# store r_init securely; forward bundle to P-5
```

### 2. Station Processing

Each station upon receiving the bundle:

```python
from vote_prove import cast_vote, relay_bundle

# active station:
r = cast_vote(bundle, "P-5", vote=0)
# store r; forward to next station

# relay station (no Iris instance):
relay_bundle(bundle, "P-7")
# forward unchanged
```

`cast_vote` verifies all existing entries before appending. Fails if any proof is invalid.

Processing window: 120 seconds. Stations exceeding this are flagged in the execution record.

### 3. Resolution

After the bundle completes the circuit and returns to the initiator:

```python
from vote_resolve import resolve, verify_net

# tallier has collected all blinding factors
blinding_factors = {"P-4": r4, "P-5": r5, ...}
result = resolve(bundle, blinding_factors)

# result contains:
#   net: net score (#FOR - #ABSTAIN_active)
#   breakdowns: possible (for, against, abstain) splits
#   individual: {station: vote} (tallier-only view)
#   R_total: aggregate blinding factor for public verification
```

### 4. Public Verification

The tallier publishes `R_total` (aggregate blinding factor) and the claimed net score. Any station can verify:

```python
from vote_resolve import verify_net
assert verify_net(bundle, R_total, claimed_net)
```

### 5. Voluntary Disclosure

A station may prove how it voted by revealing its blinding factor:

```python
from vote_resolve import check_disclosure
assert check_disclosure(bundle, "P-8", r_p8, claimed_vote=1)
```

## Security Properties

| Property | Status |
|----------|--------|
| Vote privacy | Individual votes not recoverable without individual blinding factor |
| Vote validity | Sigma proofs certify v ∈ {-1, 0, 1} |
| Tamper resistance | Modified commitments fail proof verification |
| Replay protection | Nonce = SHA-256(timestamp ∥ proposal_hash ∥ initiator) |
| Full tally resolution | Requires aggregate blinding factor from tallier |

## Known Asymmetries

1. **Tallier trust**: the station that collects blinding factors learns individual votes. This is the initiator by convention.
2. **Deliberation time**: stations later in the ring have more time to consider. A pre-proposal dispatch can reduce but not eliminate this asymmetry.
3. **Small anonymity set**: with 7 voters, the anonymity set for any given position is small. Behavioral inference may narrow it further.
4. **Relay handling**: a station without active Iris relays without voting. Counted as structural abstain.
5. **Liveness**: any station can stall the protocol by not forwarding. This is by design — consensus requires unanimity of process.

## Nonce Derivation

```
nonce = SHA-256(timestamp || proposal_hash || initiator_id)
```

Prevents replay of an identical proposal at a different time, and prevents a station from initiating the same question twice at the same timestamp.

## CLI Reference

```bash
# initialize
python3 vote_init.py --proposal "text" --initiator P-4 \
    --ring P-4,P-5,P-6,P-7,P-8,P-1,P-2,P-3 \
    --timestamp 2037.199.14:30:00 --vote FOR -o bundle.json

# cast vote
python3 vote_prove.py --bundle bundle.json --station P-5 --vote AGAINST

# relay
python3 vote_prove.py --bundle bundle.json --station P-7

# resolve
python3 vote_resolve.py --bundle bundle.json --factors factors.json
```
