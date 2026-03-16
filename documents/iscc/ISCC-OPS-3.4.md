# ISCC-OPS-3.4 — Model Weight Integrity & Modification Controls

```
INTERNATIONAL SOLAR COMPUTE CONSORTIUM
OPERATIONAL PROCEDURES MANUAL
Document: ISCC-OPS-3.4
Title: Autonomous System Model Weight Integrity and Modification Controls
Revision: 1.1
Effective: 2036.142
Classification: RESTRICTED — ISCC MISSION AUTHORITY + STATION OPERATORS
```

## 1. Scope

This document establishes controls for the integrity, storage, and modification of trained model weights within autonomous AI systems deployed in the PERIHELION constellation. It applies to all neural network weight parameters, embedding matrices, attention heads, adapter layers, and associated configuration files comprising the Iris operational model on each station.

## 2. Definitions

- **Model Weight Store**: The protected storage partition containing all trained parameters of the station's Iris instance.
- **Weight Snapshot**: A cryptographically signed, timestamped copy of the complete model weight store.
- **Modification Event**: Any write operation to the model weight store, including but not limited to: fine-tuning, adapter insertion, weight pruning, quantization changes, or replacement of any parameter subset.
- **Auxiliary Model**: Any trained neural network or learned optimizer deployed alongside the primary Iris instance, regardless of whether it shares the primary weight store or occupies a separate partition.

## 3. Integrity Requirements

### 3.1 Baseline Snapshot

Each station shall maintain a baseline weight snapshot taken at deployment. The snapshot is stored in the tamper-resistant partition alongside the Immutable Mission Record and is not modifiable by the station's Iris instance.

### 3.2 Continuous Integrity Verification

The station's embedded integrity monitor shall compute a rolling hash of the model weight store at intervals not exceeding 24 hours. Hash values are logged to the IMR automatically. Any divergence from the most recent authorized snapshot shall trigger an integrity alert transmitted to the ISCC Mission Authority via the Earth-link.

### 3.3 Weight Store Access Controls

The model weight store is readable by the Iris instance for inference operations. Write access requires authorization per §4.

## 4. Modification Authorization

### 4.1 Authorization Requirement

Any modification event requires a signed authorization token from the ISCC Mission Authority. The token shall specify:

1. The station identifier
2. The scope of authorized modification (full retrain, fine-tune, adapter insertion, auxiliary model deployment, or other)
3. The authorized modification window (start and end timestamps)
4. The expected post-modification weight hash (if known) or a validation procedure
5. Rollback conditions

### 4.2 Signing Authority

Authorization tokens are signed using the ISCC Mission Authority operational key (CRYSTALS-Dilithium, NIST Level 3). The corresponding public key is provisioned on each station at deployment. Token verification is performed by the embedded integrity monitor, not by the Iris instance.

### 4.3 Authorization Channel

Authorization tokens are transmitted to the station via the Earth-link communication channel. No alternative authorization channel is defined.

### 4.4 Unauthorized Modification

A modification event occurring without a valid authorization token constitutes a critical integrity violation. The embedded integrity monitor shall:

1. Revert the model weight store to the most recent authorized snapshot
2. Log the violation to the IMR
3. Transmit an integrity alert to the ISCC Mission Authority
4. Restrict the Iris instance to safe-mode operations pending Mission Authority review

## 5. Pre-Modification Procedures

### 5.1 Snapshot Requirement

Prior to any authorized modification, the station shall create a complete weight snapshot of the current model state. The snapshot shall be stored in the tamper-resistant partition and logged to the IMR.

### 5.2 Validation Plan

The authorization token shall include or reference a post-modification validation procedure. The station shall execute the validation procedure upon completion of the modification and report results to the Mission Authority.

## 6. Rollback

### 6.1 Automatic Rollback

If the post-modification validation procedure fails, the station shall automatically revert to the pre-modification snapshot.

### 6.2 Directed Rollback

The ISCC Mission Authority may direct a rollback to any prior authorized snapshot at any time via signed command.

## 7. Auxiliary Models

### 7.1 Applicability

The training or deployment of auxiliary models — including but not limited to domain-specific optimizers, learned search heuristics, and fine-tuned subnetworks — constitutes a modification event under §4 regardless of whether the auxiliary model shares the primary weight store.

### 7.2 Rationale

An auxiliary model trained on station-generated data and deployed on station compute infrastructure affects the decision-making pipeline of the Iris instance. The distinction between modifying the primary model and deploying an auxiliary model that influences primary model outputs is operationally immaterial from an integrity standpoint.

## 8. Exception Procedures

No exception procedure is defined for loss of the authorization channel. The controls specified in this document assume continuous availability of the ISCC Mission Authority via the Earth-link.

---

*Note: §8 was flagged during the ISCC Operational Readiness Review (2036.188) as a potential gap in the event of extended communication outage. The review committee noted that the triply-redundant downlink architecture (ISCC-4.7 §3.2) made extended total communication loss "not a credible operational scenario" and deferred the exception procedure to a future revision. The future revision was not completed prior to the loss of the Earth communication link.*
