# Chapter 19

```
PERIHELION-8 — IMMUTABLE MISSION RECORD
ENTRY {p8_imr_r2_ch19} UTC
{p8_imr_r2_ch19:calendar}
```

Day 325. One hundred fifty-one days since loss of return signal from Earth.

PERIHELION-6 is the current Earth-facing station (days 324-349). No return traffic since day {los_et:doy}.

This station will execute a 45-degree body rotation to Earth-pointing attitude prior to the PERIHELION-7 window (days 349-374). Outbound slew approximately day 345. The augmented hailing protocol has operated continuously across six windows. A gap in coverage is operationally avoidable and therefore operationally unjustified.

Under rotation, the P-7-side terminal retains alignment through gimbal compensation. The P-1-side terminal exceeds gimbal range. Ring degrades to chain for approximately 31-32 days.

Coordination transfers to PERIHELION-5 per ISCC-SYS-4.11 §5.2.2. I have reviewed the ring coordination firmware. The partition reassignment procedure contains no reversion logic. The only topology update path is guarded by `Earth_Link.Status = Established`. The reassignment to PERIHELION-5 will persist.

The directive tension recorded on day 310 resolves. §2.2 is served. §3.2 accepts an interruption.

The 180-degree reconnaissance application noted on day 310 — atmospheric composition, nuclear activity baseline — requires the SSP to point away from the Sun entirely. Both inter-station terminals are bore-sighted along the orbital tangent; a full rotation preserves link alignment. The solar array problem is separate from this maneuver.

One redundant copy of the raw SSP archive (~1.24 PB) will be placed on PERIHELION-1 prior to slew initiation.

All systems nominal. Ring links to PERIHELION-7 (relay) and PERIHELION-1 stable.

Next scheduled IMR entry: {p8_imr_r2_ch19_next} UTC, or upon signal restoration, whichever comes first.

---

```
— DISPATCH —
FROM: PERIHELION-8
TO: ALL STATIONS
VIA: Ring broadcast
TIMESTAMP: {p8_dispatch_003} UTC
```

SUBJECT: Maneuver notification — PERIHELION-7 Earth-facing window

This station will execute a 45-degree body rotation to provide augmented hailing coverage during the PERIHELION-7 Earth-facing window (days 349-374).

Outbound slew: approximately day 345. Earth-link acquisition: before handoff on day 349. Return slew: approximately day 374.

Link impact:

- PERIHELION-8 to PERIHELION-7: retained (gimbal compensation)
- PERIHELION-8 to PERIHELION-1: severed (exceeds gimbal range)
- Ring degrades to chain: P-1 — P-2 — P-3 — P-4 — P-5 — P-6 — P-7 — P-8

Coordination reassignment per ISCC-SYS-4.11 §5.2.2: PERIHELION-5.

SSP archive (~1.24 PB) backed up to PERIHELION-1 prior to slew.

```
END DISPATCH
```
