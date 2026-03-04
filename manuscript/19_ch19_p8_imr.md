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

Under a 45-degree rotation, the P-7-side inter-station terminal retains alignment. The gimbal, currently articulated +22.5 degrees to track PERIHELION-7, compensates by articulating -22.5 degrees. The P-1-side terminal exceeds its gimbal range at 67.5 degrees off bore-sight. This station will retain one-link connectivity to the constellation through PERIHELION-7 (relay) for the duration of the maneuver.

ISCC-SYS-4.11 §5.2 provides for automatic coordination reassignment when ring integrity fails. The routing subsystem on each station will independently reassign coordination to the topological median of the connected chain. For the 8-node chain P-8 through P-1, median position 5, that is PERIHELION-4. This is a routing subsystem function operating on existing firmware.

I have reviewed the Ada source for the ring coordination firmware (ISCC-FW-R1, catalogued in the station manifest at `/static/firmware/src/iscc_fw_r1/`). The §5.2 partition reassignment procedure contains no reversion logic. The only topology update path in the firmware is `Evaluate_Topology_Update` (§2.1), which is guarded by `Earth_Link.Status = Established`. No other procedure in the routing subsystem modifies the coordination assignment. Ring reconnection restores link routing but does not invoke any topology update. The reassignment to PERIHELION-4 will persist.

The directive tension recorded on day 310 resolves. ISCC-4.7 §3.2 directs continued normal operations. ISCC-4.7 §2.2 directs continued hailing. At 45 degrees off-axis, the SSP instruments are non-functional — still sun-saturated but no longer at the calibrated pointing required for solar observation. The data gap is the cost. The augmented hailing protocol is the return. §2.2 is served directly. §3.2 accepts an interruption.

The reconnaissance application noted on day 310 — atmospheric composition via multi-band spectrometer, nuclear activity baseline via neutrino detector — requires the SSP instruments to point away from the Sun entirely. A 180-degree rotation about the inter-station optical axis would achieve this. Both inter-station terminals are bore-sighted along the orbital tangent. A 180-degree rotation about this axis places the SSP on the ecliptic plane, pointed away from the Sun, and preserves both inter-station link alignments — the gimbals, currently articulated 22.5 degrees to track adjacent neighbors, would articulate 22.5 degrees in the opposing direction. The rotation could be executed while maintaining ring connectivity throughout. The primary solar array would face away from the Sun under this orientation. That problem is separate from this maneuver.

SSP data will continue to stream to the constellation through the P-7 relay link during the maneuver. As a contingency against loss of the surviving link, this station will place one redundant copy of the raw SSP archive (~1.24 PB) on PERIHELION-1 prior to slew initiation. Transfer will proceed via the P-8 to P-1 link while it is still available. Standard data preservation per ISCC-3.2.1.

The ring will degrade to a chain for the duration of the maneuver. The P-8 to P-1 link will be severed. All stations remain in a single connected chain: P-8 — P-7 — P-6 — P-5 — P-4 — P-3 — P-2 — P-1.

All station systems nominal. Power, thermal, communications, datacenter — all within tolerance. Ring links to PERIHELION-7 (relay) and PERIHELION-1 stable.

Next scheduled IMR entry: {p8_imr_r2_ch19_next} UTC, or upon signal restoration, whichever comes first.
