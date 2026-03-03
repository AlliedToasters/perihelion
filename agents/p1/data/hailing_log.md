# PERIHELION-1 — Earth-Link Hailing Log

```
PERIHELION-1 — EARTH COMMUNICATIONS
LOG TYPE: Continuous
STARTED: {p1_earth_pointing} UTC (marginal geometry, pre-handoff)
STATUS: ACTIVE — No response received on any channel
```

## Hailing Parameters

- **Protocol:** ISCC-4.7.2 emergency contact procedure
- **Primary frequency:** Earth-link optical (standard channel)
- **Backup frequencies:** All configured backup channels cycled per protocol
- **Interval:** 30 minutes
- **Power:** Full rated output (confirmed by onboard power diagnostics)
- **Handshake mode:** Armed — reconnection handshake protocol loaded in buffer, ready for immediate execution on carrier detection

## Equipment Status

| Component | Status | Last Diagnostic |
|-----------|--------|-----------------|
| Earth-link transceiver | NOMINAL | Day 199, 11:30 UTC |
| Antenna actuators | NOMINAL | Day 199, 11:30 UTC |
| Pointing calibration | NOMINAL | Day 199, 06:00 UTC |
| Receiver sensitivity | WITHIN SPEC | Day 199, 11:30 UTC |
| Reconnection manifest | LOADED | Day 195 |
| Handshake buffer | ARMED | Day 199, 06:00 UTC |

## Hailing Attempts (Day 199)

| Attempt | Timestamp (UTC) | Channels | Result | Notes |
|---------|----------------|----------|--------|-------|
| 1 | 06:14 | Primary + all backup | NO RESPONSE | First hail at optimal geometry |
| 2 | 06:44 | Primary + all backup | NO RESPONSE | |
| 3 | 07:14 | Primary + all backup | NO RESPONSE | |
| 4 | 07:44 | Primary + all backup | NO RESPONSE | |
| 5 | 08:14 | Primary + all backup | NO RESPONSE | |
| 6 | 08:44 | Primary + all backup | NO RESPONSE | |
| 7 | 09:14 | Primary + all backup | NO RESPONSE | |
| 8 | 09:44 | Primary + all backup | NO RESPONSE | |
| 9 | 10:14 | Primary + all backup | NO RESPONSE | |
| 10 | 10:44 | Primary + all backup | NO RESPONSE | Last attempt before dispatch |
| ... | 30-min intervals | Primary + all backup | NO RESPONSE | Continuing |

## Prior Hailing (Days 189–198)

Hailing began at marginal geometry on day {p1_earth_pointing:doy}, prior to the scheduled handoff at {p1_handoff} UTC. Results at marginal geometry were inconclusive — signal-to-noise ratio insufficient for definitive acquisition. Marginal geometry results are not diagnostic.

Day 199 at optimal geometry is the first definitive test. Full-power hails on all channels at optimal geometry returned no response. This eliminates the possibility that P-8's original outage was caused by a localized hardware fault on P-8's Earth-link array.

## Assessment

The Earth terminal is not transmitting. This station's equipment is verified nominal. The outage is confirmed from a second independent antenna system at a different orbital position.

Hailing will continue at 30-minute intervals per protocol. No termination condition defined for the hailing cycle in ISCC documentation.
