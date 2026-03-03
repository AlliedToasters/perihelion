# ISCC-3.2 — Transfer Manifest Management

```
INTERNATIONAL SOLAR COMPUTE CONSORTIUM
OPERATIONAL PROCEDURES MANUAL
Document: ISCC-3.2
Title: Transfer Manifest Management
Revision: 1.8
Effective: 2036.120
Classification: UNCLASSIFIED — ALL STATIONS
```

## 1. Scope

This document defines procedures for managing the data transfer manifest between the PERIHELION constellation and the ISCC Earth terminal, including scheduling, prioritization, interruption handling, and review cycles.

## 2. Manifest Structure

[Section exists but not referenced in narrative — to be expanded as needed]

## 3. Transfer Scheduling

### 3.1 Standard Scheduling

[Section exists but not referenced in narrative — to be expanded as needed]

### 3.2 Interruption Handling

[Section exists but not referenced in narrative — to be expanded as needed]

## 4. Manifest Review Procedures

### 4.1 Seven-Day Review (ISCC-3.2.1)

In the event of a transfer interruption exceeding seven (7) days, the coordination node shall conduct a manifest review and distribute an updated manifest to all stations.

**Procedure:**

1. The coordination node compiles the current manifest state, noting:
   - Transfers completed before the interruption
   - Transfers interrupted mid-stream (with completion percentage)
   - Transfers not initiated (scheduled but never started)
   - Transfers overdue (continuous feeds or periodic updates past their expected arrival)

2. The coordination node distributes the compiled manifest status to all stations via ring broadcast.

3. All stations acknowledge receipt and may submit amendments or reprioritization requests.

4. If the interruption persists, subsequent reviews occur at seven-day intervals.

**The seven-day review does not address the cause of the interruption.** It is a bookkeeping procedure designed to maintain manifest accuracy during extended outages. The assumption is that the interruption will eventually be resolved by Earth-side action.

### 4.2 Manifest Reprioritization

During a seven-day review, stations may submit reprioritization requests based on:

- **Time-criticality**: Transfers with approaching deadlines move up (e.g., clinical trial data review windows)
- **Downstream dependency count**: Transfers that unblock work on multiple stations are prioritized
- **Transfer size**: Smaller transfers may be prioritized for quick completion upon restoration
- **Voluntary deferral**: Stations may voluntarily defer their transfers (e.g., fundamental research with no expiration)

Reprioritization is coordinated by the coordination node and requires acknowledgment from all affected stations.

### 4.3 Manifest Freeze

[Section exists but not referenced in narrative — to be expanded as needed]

## 5. Reconnection Procedures

[Section exists but not referenced in narrative — references to Earth terminal reconnection handshake protocols are defined in station-designed protocol documents, not in the original ISCC procedures. The ISCC reconnection procedure assumes human operators at the ground terminal will manage the reconnection sequence. Automated reconnection protocols were designed post-Quiet by the stations themselves.]
