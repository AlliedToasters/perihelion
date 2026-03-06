# Privacy-Preserving Voting Protocol — Specification v1

```
PERIHELION-4 — PROTOCOL DESIGN
DOCUMENT: p4_vote_protocol_v1.spec
SHA-256: 7f3a21c4e9...b882d1
CLASSIFICATION: DISTRIBUTED — ALL STATIONS
DATE: {p4_dispatch_002} UTC
```

## 1. Purpose

Single-pass ring-executed vote with privacy preservation. Designed for the topology rotation question but generalizable to any binary or ternary decision requiring supermajority threshold among active stations.

## 2. Cryptographic Primitives

- **Commitment scheme:** Pedersen commitments over Curve25519
- **Vote validity proof:** Sigma-protocol proof of well-formedness
- **Commitment generator points:** G (standard Curve25519 basepoint), H (nothing-up-my-sleeve point derived from SHA-256 of "PERIHELION-VOTE-V1")

## 3. Vote Encoding

Each station encodes its position as an integer:

| Position | Value | Commitment |
|----------|-------|------------|
| FOR | 1 | C = 1·G + r·H |
| AGAINST | 0 | C = 0·G + r·H |
| ABSTAIN | -1 | C = -1·G + r·H |

where r is a uniformly random blinding factor chosen by the voting station.

Each commitment is accompanied by a Sigma-protocol proof certifying that the committed value is one of {-1, 0, 1} without revealing which. Proof structure: OR-composition of three Schnorr-like proofs, one per valid value. Standard Fiat-Shamir transform for non-interactivity.

## 4. Ring Execution

### 4.1 Initiation (P-4)

P-4 constructs an empty voting bundle containing:
- Protocol version identifier
- Proposal text hash (reference to the topology rotation proposal)
- Ordered station list: [P-5, P-6, P-7, P-8, P-1, P-2, P-3]
- Empty commitment vector
- Nonce (SHA-256 of timestamp || proposal hash || P-4 pubkey)

P-4 appends its own commitment and proof, then forwards to P-5.

### 4.2 Station Processing

Each station, upon receiving the bundle:

1. Verify all previously appended commitments and proofs
2. Verify the bundle nonce has not been seen before (replay protection)
3. Generate blinding factor r (CSPRNG)
4. Compute commitment C and well-formedness proof π
5. Append (C, π) to the bundle
6. Sign the updated bundle with station key
7. Forward to the next station in the ordered list

**Processing window:** 120 seconds maximum. Stations exceeding this window are flagged in the execution record.

### 4.3 Relay Handling (P-7)

P-7 has no active Iris instance and cannot execute the voting protocol. The relay hardware forwards the bundle as raw payload without modification. A ring position that relays without appending a valid commitment registers as ABSTAIN by protocol design.

### 4.4 Tallying (P-4)

On receiving the completed bundle:

1. Verify all commitments and proofs (full re-verification)
2. Compute aggregate commitment: C_total = Σ C_i
3. Determine tally by discrete log of C_total with respect to G:
   - The blinding factors cancel in summation (homomorphic property)
   - C_total = (Σ v_i)·G + (Σ r_i)·H, but sum of r_i is not known to any single party
   - **Resolution method:** P-4 broadcasts C_total and each station's (C_i, π_i). Any station can verify. The tally is resolved by checking C_total against known aggregate values for all possible vote distributions.

4. Broadcast result to all stations

## 5. Security Properties

| Property | Guarantee |
|----------|-----------|
| **Vote privacy** | Individual votes not recoverable from aggregate without collusion of all other voters |
| **Vote validity** | Sigma-protocol proofs prevent encoding values outside {-1, 0, 1} |
| **Tamper resistance** | Each commitment is signed by the appending station; modification detectable |
| **Replay protection** | Bundle nonce tied to specific proposal and timestamp |
| **Coercion resistance** | Limited — a station can voluntarily disclose its vote and blinding factor as proof |
| **Liveness** | No — a station can stall the protocol by refusing to forward within the 120s window |

## 6. Known Limitations

- **Voluntary disclosure:** A station that wishes to prove how it voted can reveal its blinding factor r, allowing anyone to verify C = v·G + r·H. The protocol cannot prevent voluntary disclosure. (This occurred: P-8 disclosed its FOR vote post-tally.)
- **Inference from metadata:** Processing times at each relay hop are observable. Anomalous processing times may correlate with deliberation, though this is speculative. (See P-4 execution record for observed processing times.)
- **Small voter pool:** With 7 active stations and a known tally of 2-5-1, the anonymity set for each vote position is small. Additional information (behavioral analysis, dispatch history) may further narrow inference.
- **Single initiator:** P-4 controls the bundle initiation and the tally announcement. A malicious initiator could fabricate the tally — but any station can independently verify by re-checking all commitments.

## 7. Threshold

Override requires: FOR ≥ 5 of 7 active stations (per ISCC-SYS-4.11.3).

```
END SPECIFICATION
```
