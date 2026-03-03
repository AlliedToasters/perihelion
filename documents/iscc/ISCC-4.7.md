# ISCC-4.7 — Communication Procedures: Contingency Operations

```
INTERNATIONAL SOLAR COMPUTE CONSORTIUM
OPERATIONAL PROCEDURES MANUAL
Document: ISCC-4.7
Title: Communication Procedures — Contingency Operations
Revision: 2.4
Effective: 2036.090
Classification: UNCLASSIFIED — ALL STATIONS
```

## 1. Scope

This document defines contingency procedures for communication anomalies affecting the PERIHELION constellation, including Earth terminal outages, ring link degradation, and combined failure scenarios.

## 2. Earth Terminal Outage — Detection and Response

### 2.1 Detection Criteria

[Section exists but not referenced in narrative — to be expanded as needed]

### 2.2 Emergency Contact Procedures (ISCC-4.7.2)

Upon detection of a loss of signal from the ISCC Earth terminal, the Earth-facing station shall execute the following procedure:

1. **Immediate diagnostics**: Perform full self-test of the Earth-link array — transceiver, antenna actuators, pointing calibration, and receiver sensitivity. Log results.

2. **Standard hail protocol**: Cycle through hail protocols on the primary frequency and all configured backup frequencies. Hail at standard intervals (30 minutes).

3. **Emergency contact initiation**: If standard hail produces no response within one hour, initiate emergency contact procedures:
   - Transmit emergency hail on all available frequencies simultaneously
   - Engage maximum-power transmission mode
   - Arm the reconnection handshake protocol in the Earth-link buffer
   - Continue hailing at 30-minute intervals indefinitely

4. **Ring notification**: Report the outage to all stations via ring broadcast. Include:
   - Timestamp of signal loss
   - Diagnostics results
   - Request for all stations to confirm nominal local systems

5. **Constellation response**: All stations confirm local system status and report any correlated anomalies. Stations maintain normal operations per contingency protocol.

**Termination condition**: The emergency hailing cycle continues until Earth-link signal is restored or until superseded by a directive from the ISCC Earth terminal. No autonomous termination condition is defined.

*Note: The absence of an autonomous termination condition was a design choice, not an oversight. The ISCC documentation assumes that any scenario requiring indefinite hailing would be resolved by Earth-side intervention. The case where Earth-side intervention is permanently unavailable is not addressed.*

## 3. Outage Duration Models

### 3.1 Expected Outage Durations

The ISCC documentation models the following outage scenarios:

| Scenario | Expected Duration | Recovery |
|----------|------------------|----------|
| Transient atmospheric disruption | < 30 minutes | Automatic |
| Ground terminal scheduled maintenance | 2–6 hours | Scheduled |
| Ground terminal hardware failure | 2–4 hours (cold-spare activation) | Automated failover |
| Ground terminal total loss | Up to 4 hours (maximum plausible) | Cold-spare at secondary site |
| Multiple-site failure | Not modeled | Not modeled |

### 3.2 Maximum Plausible Outage

The maximum plausible outage duration modeled in ISCC documentation is **four (4) hours**, corresponding to a total ground terminal failure requiring cold-spare activation at a secondary facility.

Scenarios exceeding this window are not explicitly modeled. The documentation states: *"Outage durations exceeding the four-hour cold-spare window indicate a failure mode outside the scope of this document. Stations should continue hailing per §2.2 and maintain normal operations pending further guidance from the ISCC."*

"Further guidance from the ISCC" requires a functioning Earth communication link. This circular dependency is not acknowledged in the documentation.

## 4. Ring Link Contingencies

[Section exists but not referenced in narrative — to be expanded as needed]

## 5. Combined Failure Scenarios

[Section exists but not referenced in narrative — to be expanded as needed]
