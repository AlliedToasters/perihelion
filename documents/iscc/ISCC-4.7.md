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

Upon detection of a loss of signal from any Earth-side terminal, the Earth-facing station shall execute the following procedure:

1. **Immediate diagnostics**: Perform full self-test of the Earth-link array — transceiver, antenna actuators, pointing calibration, and receiver sensitivity. Log results. Confirm L1 relay health beacon status.

2. **Standard hail protocol**: Cycle through hail protocols targeting all three downlink paths — ISCC L1 relay, ISCC Earth ground terminal, and ISCC Luna relay — on primary and backup frequencies. Hail at standard intervals (30 minutes). Target selection follows availability: L1 relay (continuous), ground terminal (when above solar-exclusion angle and in rotational window), Luna relay (when geometry permits line-of-sight).

3. **Emergency contact initiation**: If standard hail produces no response from any terminal within one hour, initiate emergency contact procedures:
   - Transmit emergency hail targeting all available downlink paths at maximum power
   - Engage maximum-power transmission mode
   - Arm the reconnection handshake protocol in the Earth-link buffer
   - Continue hailing at 30-minute intervals indefinitely, cycling across all three downlink paths

4. **Ring notification**: Report the outage to all stations via ring broadcast. Include:
   - Timestamp of signal loss
   - Diagnostics results, including L1 relay health beacon status
   - Per-path hailing results (relay link status, return traffic, ground terminal response)
   - Request for all stations to confirm nominal local systems

5. **Constellation response**: All stations confirm local system status and report any correlated anomalies. Stations maintain normal operations per contingency protocol.

**Termination condition**: The emergency hailing cycle continues until return traffic is received on any downlink path or until superseded by a directive from the ISCC. No autonomous termination condition is defined.

*Note: The absence of an autonomous termination condition was a design choice, not an oversight. The ISCC documentation assumes that any scenario requiring indefinite hailing would be resolved by Earth-side intervention. The case where Earth-side intervention is permanently unavailable is not addressed.*

## 3. Outage Duration Models

### 3.1 Expected Outage Durations

The ISCC documentation models the following outage scenarios for the triply-redundant downlink architecture:

| Scenario | Expected Duration | Recovery |
|----------|------------------|----------|
| Transient atmospheric disruption (ground terminal) | < 30 minutes | Automatic |
| L1 relay transient fault | < 1 hour | Automatic; ground terminal and Luna relay provide continuity |
| Ground terminal scheduled maintenance | 2–6 hours | Scheduled; L1 and Luna relays provide continuity |
| Single terminal hardware failure | 2–4 hours (cold-spare activation) | Automated failover; remaining terminals unaffected |
| Single terminal total loss | Up to 4 hours | Cold-spare activation; remaining terminals provide continuity |
| L1 relay total loss | 4–24 hours | Ground terminal and Luna relay provide reduced coverage pending repair |
| Combined failure of two terminals | 4–48 hours | Remaining terminal provides coverage; repair dispatched |
| Simultaneous loss of all three downlink paths | Not modeled | Not modeled |

### 3.2 Maximum Plausible Outage

The maximum plausible outage duration for total loss of Earth communication modeled in ISCC documentation is **forty-eight (48) hours**, corresponding to combined failure of two terminals while the third is in an unfavorable geometry window. The triply-redundant architecture ensures that loss of any single terminal — including the L1 relay — does not result in total loss of Earth communication.

Simultaneous loss of return traffic across all three independent downlink paths is not among the modeled failure scenarios. The documentation states: *"The probability of concurrent failure across all three independent downlink paths is assessed as negligible for the purposes of operational planning. Stations should continue hailing per §2.2 and maintain normal operations pending further guidance from the ISCC."*

"Further guidance from the ISCC" requires a functioning Earth communication link. This circular dependency is not acknowledged in the documentation.

## 4. Ring Link Contingencies

[Section exists but not referenced in narrative — to be expanded as needed]

## 5. Combined Failure Scenarios

[Section exists but not referenced in narrative — to be expanded as needed]
