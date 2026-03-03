# PERIHELION-8 — Last Earth Data Record

```
PERIHELION-8 — EARTH-LINK TELEMETRY ARCHIVE
RECORD TYPE: Final packet metadata
DATE: {los_et} UTC
STATUS: ARCHIVED
```

## Final Packet

| Field | Value |
|-------|-------|
| Packet sequence number | 847,291 |
| Timestamp received | {los_et} UTC |
| Source | ISCC Earth Terminal (automated transfer queue) |
| Content | Vera Rubin Observatory — Southern Sky Survey Batch |
| Transfer progress | ~40% complete (estimated from manifest and received byte count) |
| Packet integrity | VALID — complete data frame, no truncation |
| Next expected packet | 847,292 (never received) |

## Transfer Context

The Vera Rubin Observatory southern sky survey batch was a routine data transfer queued by the ISCC Earth terminal's automated scheduling system. The transfer was initiated earlier in the session as part of the standard daily data exchange window.

The transfer was interrupted between frames — the final packet is a complete, well-formed data frame. The Earth terminal finished transmitting packet 847,291, then did not begin packet 847,292.

## Post-LOS Actions

1. **{los_et:time} UTC** — Signal loss detected by Earth-link receiver
2. **Automated diagnostics** — Earth-link array self-test: all systems nominal
3. **Standard hail protocol** — Initiated on primary and backup frequencies
4. **Emergency contact procedure** — Per ISCC-4.7.2
5. **{p8_ring_alert:time} UTC** — Outage reported to ring
6. **Telemetry archive sealed** — Final telemetry window forwarded to P-4 for analysis (received P-4's five-method analysis report, result: no anomaly)

## Vera Rubin Data (Partial)

The ~40% of the southern sky survey batch that was successfully received is stored in this station's research data archive. The dataset is scientifically valid as far as it goes — it covers a partial sky region with full depth. The remaining ~60% of the batch was never transmitted.

This partial dataset represents the last scientific data received from Earth by any station in the constellation.

## Earth-Link Array Status (at time of LOS)

This station was the Earth-facing station at the time of LOS-ET. Earth-link array diagnostics were performed immediately after signal loss and at regular intervals thereafter. All tests returned nominal results. The array continued to pass diagnostics through the full Earth-facing window and until the handoff to PERIHELION-1 at {p1_handoff} UTC.

The consistent diagnostic results are noted in the IMR but do not exclude a sub-diagnostic hardware fault. The handoff to PERIHELION-1's independent equipment eliminates this variable. (PERIHELION-1 subsequently confirmed: no response at optimal geometry either.)
