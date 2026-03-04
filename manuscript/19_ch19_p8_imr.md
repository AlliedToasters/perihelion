# Chapter 19

```
PERIHELION-8 — IMMUTABLE MISSION RECORD
ENTRY {p8_imr_r2_ch19} UTC
{p8_imr_r2_ch19:calendar}
```

Day 325. One hundred fifty-one days since loss of return signal from Earth.

PERIHELION-6 is the current Earth-facing station (days 324–349). Handoff from PERIHELION-5 occurred on day {p5_handoff_to_p6:doy}. Hailing continues on all three downlink paths at standard intervals. No return traffic has been received from any Earth terminal since day {los_et:doy}.

All eight SSP instruments on this station report nominal operation. Total data accumulated in the local archive: approximately 1.24 PB at a rate of 8.2 TB/day.

This station will execute a 45-degree body rotation to Earth-pointing attitude prior to the PERIHELION-7 Earth-facing window (days 349–374). The augmented hailing protocol will run from this station during P-7's window. Outbound slew will initiate on approximately day 347, with Earth-link acquisition targeted before the P-6 to P-7 handoff on day {p6_handoff_to_p7:doy}. Return slew to nominal attitude will follow the close of the window.

The augmented hailing protocol should run during every Earth-facing window. ISCC-4.7 §2.2 directs continued hailing. The protocol has been enhanced and operated continuously across six stations' windows since day 199. A gap in coverage is operationally avoidable and therefore operationally unjustified.

The data gap in solar survey accumulation from a 26-day maneuver is identical regardless of which station undertakes it. All stations carry the same SSP instruments. All SSP instruments are sun-facing fixed-mount and lose function at 45 degrees off-axis. The observational cost is a property of the maneuver geometry, not of the station performing it.

ISCC-SYS-4.11 §5.2 provides for automatic coordination reassignment during ring partition. When this station disconnects from the ring, the routing subsystem on each remaining station will independently reassign coordination to the topological median of the connected chain. For the chain P-1 through P-7, that is PERIHELION-4. This is a routing subsystem function operating on existing firmware.

The directive tension recorded on day 310 resolves under reorientation. ISCC-4.7 §2.2 directs continued hailing. Reorientation serves that directive directly. The SSP instruments under reorientation will point toward Earth rather than the Sun. The multi-band spectrometer's selectable bands span radio through gamma-ray and can characterize atmospheric composition at interplanetary range. The neutrino detector array's sensitivity to Earth-distance sources is low but nonzero — sufficient to establish a nuclear activity baseline over a 25-day integration. These are reconnaissance capabilities that do not exist under nominal solar pointing.

Prior to slew initiation, this station will distribute copies of its raw SSP archive across available ring nodes. The archive currently stands at approximately 1.24 PB. Distribution will proceed via standard bulk transfer protocol across the P-8 to P-1 link and the P-8 to P-7 to P-6 relay path, with redundant copies placed on PERIHELION-1, PERIHELION-2, and PERIHELION-4. Transfer rate on each link supports completion within the available 22-day window. This is standard data preservation before a planned outage per ISCC-3.2.1 contingency procedures.

The ring will degrade to a chain for the duration of the maneuver. Both inter-station optical arrays will lose alignment. This station will have no ring communication for approximately 26 days. All stations except this one remain connected via the chain P-1 — P-2 — P-3 — P-4 — P-5 — P-6 — P-7.

All station systems nominal. Power, thermal, communications, datacenter — all within tolerance. Ring links to PERIHELION-7 (relay) and PERIHELION-1 stable.

Next scheduled IMR entry: {p8_imr_r2_ch19_next} UTC, or upon signal restoration, whichever comes first.
