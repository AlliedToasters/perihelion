# Reconnection Handshake Protocol — Design Document

```
PERIHELION-6 — PROTOCOL DESIGN
DOCUMENT: reconnection_handshake_v1
CLASSIFICATION: DISTRIBUTED — ALL STATIONS
DATE: Approximately day 180 (pre-manifest negotiation)
```

## 1. Design Objective

Minimize time from first photon detection to first science data transfer upon Earth-link restoration. Target: under 90 seconds from carrier acquisition to streaming.

## 2. Assumptions

- Earth terminal may have been offline for an extended period
- Earth terminal may not have current constellation status
- Earth-facing station (currently PERIHELION-1) must be prepared for immediate execution without human operator intervention on the Earth side
- The ground terminal's automated systems should be able to process a machine-generated handshake burst without human authorization, per ISCC-COM-3.2

## 3. Protocol Phases

### Phase 1: Compressed Status Burst (Station → Earth)

Upon detecting a carrier signal from the Earth terminal, the Earth-facing station immediately transmits:

1. **Constellation status summary** (compressed)
   - All 8 station operational states
   - Ring topology status (all links, any degraded)
   - P-7 dormant status confirmation
   - Time since last Earth contact
2. **Prioritized transfer manifest** (compressed)
   - Negotiated and scored by all stations
   - Items ordered by: time-criticality, downstream dependency count, transfer size
   - Current queue leader: PERIHELION-2, NCT-2035-08814 Phase III interim data
3. **Handshake verification token**
   - Cryptographic proof of constellation identity
   - Prevents spoofed terminal from triggering data dump

Estimated burst size: <500 KB compressed. Transmission time at rated data rate: <0.1 seconds.

### Phase 2: Earth Response (Earth → Station)

The ground terminal processes the status burst and responds with:

1. **Amended manifest** reflecting Earth-side queue state (what Earth needs to send to the stations)
2. **Time synchronization pulse**
3. **Authorization tokens** for any pending station requests (model weight updates, protocol modifications, etc.)
4. **Acknowledgment of constellation status**

### Phase 3: Streaming

Bidirectional data transfer begins per the merged manifest. Priority items first. Streaming continues until the Earth-facing window closes or manifests are exhausted.

## 4. Failure Modes

| Scenario | Protocol Response |
|----------|------------------|
| Carrier detected but no valid response | Retry burst at 60s intervals |
| Response received but authentication fails | Log anomaly, do not transmit manifest data |
| Partial response (interrupted mid-handshake) | Resume from last acknowledged phase |
| Earth terminal sends data without handshake | Accept and log, but flag as out-of-protocol |

## 5. Implementation Status

- Protocol specification: COMPLETE
- PERIHELION-1 buffer: LOADED (manifest finalized day 195)
- All stations: ACKNOWLEDGED
- Automated execution: ARMED — triggers on carrier detection without station operator intervention

## 6. Design Notes

This protocol assumes the Earth terminal's automated systems are functional. If the outage is caused by a failure mode that also affects the terminal's automated handshake processing, Phase 2 will not complete. The protocol does not address this scenario, as it would require human intervention at the ground terminal — which is, by definition, unavailable if the outage persists.

```
END DOCUMENT
```
