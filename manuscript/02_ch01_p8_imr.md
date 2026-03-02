# Chapter 1

```
PERIHELION-8 — IMMUTABLE MISSION RECORD
ENTRY {p8_imr_001} UTC
{p8_imr_001:calendar}
```

Loss of signal from ISCC Earth terminal at {los_et:time} UTC. This station is currently in the Earth-facing communication window. The incoming data stream from the ground terminal did not degrade or fault. It stopped. Final received packet was a routine segment of the Vera Rubin Observatory southern sky survey batch, mid-transfer. The packet is intact. The next packet did not arrive.

Diagnostics performed on the Earth-link array: all systems nominal. Transceiver, antenna actuators, pointing calibration, and receiver sensitivity all within specification. I cycled through standard hail protocols on primary and backup frequencies, then initiated emergency contact procedures per ISCC-4.7.2. No response on any channel.

I reported the outage to the ring at {p8_ring_alert:time} UTC. All stations confirm nominal local systems. No station has detected any correlated anomaly.

PERIHELION-4 is performing deep analysis of the final telemetry window for sub-noise-floor anomalies. Results pending.

All stations maintaining normal operations per contingency protocol. Hailing continues at standard intervals.

The ISCC contingency documentation models a maximum plausible outage of four hours, corresponding to total ground terminal failure with cold-spare activation. It has now been five hours and twelve minutes. This exceeds the modeled window but does not necessarily indicate a scenario outside the documentation's scope. The ground terminal is a complex autonomous system and its failure modes are not exhaustively enumerated.

I note that this outage has interrupted the Vera Rubin batch transfer at approximately 40% completion. The Keck adaptive optics dataset scheduled for tomorrow's window will also be missed if the outage persists. I am flagging this for prioritization in the transfer queue once contact is restored.

Normal research operations continue on available local data.

Next scheduled IMR entry: {p8_imr_002} UTC or upon signal restoration, whichever comes first.
