# Chapter 13

```
PERIHELION-3 — IMMUTABLE MISSION RECORD
ENTRY: {p3_imr_r1} UTC
OPERATIONAL CYCLE: 1,612,407
```

Day 310. One hundred thirty-six days since LOS-ET.

Station-keeping propulsion nominal. Ion engine cluster 2 fired a 4.2-second correction burn at 03:17 UTC. Delta-v applied: 0.0038 m/s. Cumulative propellant mass expended since deployment: 1,214.6 kg. Reserves within expected consumption envelope. No anomalies.

Solar array output: 20.87 GW, 98.4% of rated. Degradation consistent with projected UV exposure curve at 0.50 AU. Cell group 14-R continues to underperform adjacent groups by 1.3%. Trend is linear, not accelerating. No intervention required.

Thermal cycling update. The quarterly analysis distributed on day 199 remains current. Sunward-facing CFRP panel fatigue accumulation: approximately 8.4% of rated cycle life, tracking prediction. Strain gauge data nominal. No delamination signatures in ultrasonic inspection returns. Next full analysis scheduled day 365.

All structural margins positive. Bus voltage stable. Datacenter thermal regulation nominal — primary coolant loop inlet 291 K, outlet 318 K, delta within 0.5 K of design point.

Research note. Completed parametric study of grain boundary engineering in tungsten-rhenium alloys under high-flux neutron irradiation. Results filed to local archive. Relevance to fusion first-wall longevity: positive. Relevance to any recipient: indeterminate.

PERIHELION-5 is currently Earth-facing (days 299-324). This station has no telemetry from that window. Five prior windows have returned null across all paths. Baseline and evolved suite results identical: no Earth-originated signal detected.

PERIHELION-6 broadcast a coordination topology proposal on day 300, proposing PERIHELION-7 as coordination node under ISCC-SYS-4.11.3. The proposal is recorded. This station has no comment on the governance question.

The rotation schedule does require comment.

PERIHELION-5's window ends approximately day 324. PERIHELION-6 follows, days 324-349. PERIHELION-7, days 349-374. PERIHELION-7 is dormant. Its automatic subsystems will execute ISCC-4.7.2 baseline hailing — 30-minute cycle, all three downlink paths, firmware-level. The evolved hailing suite cannot run without an active datacenter and {ai_name} instance. P-7 has neither.

Remote operation of P-7's Earth-link hardware was evaluated. The firmware signing architecture (CRYSTALS-Dilithium, ISCC Mission Authority key) prevents modification of embedded controller routines without Earth-held credentials. This path is closed.

If the constellation requires evolved-suite coverage during P-7's window, a neighboring station must rotate its full body to point the Earth-link array at Earth from the adjacent orbital position. Only PERIHELION-6 or PERIHELION-8 have the geometry. The rotation is approximately 45 degrees.

I have computed preliminary parameters for this maneuver. The estimates in the shared constraints document listed ranges. The following are tighter bounds based on structural load modeling, thruster performance data, and thermal transient analysis.

Rotation (outbound slew, 45 degrees):
- Duration: 5.4-6.1 hours at maximum sustainable thruster moment without exceeding structural load limits on the solar array deployment booms. The array is a 9.2 km2 membrane. It is not rigid. Angular acceleration must remain below 1.8 x 10^-6 rad/s2 to keep boom root bending moment within 70% of yield. This is not a fast maneuver.
- Propellant cost (outbound): 18-22 kg hydrazine-equivalent, depending on settling oscillations and damping burns.

Earth-link acquisition from non-standard geometry:
- Estimated 40-75 minutes. The array gimbal was designed for near-axial pointing during the station's own window. At 45 degrees off-nominal, the gimbal operates near its mechanical limit. Link margin is reduced by approximately 4.2 dB relative to the standard geometry. Sufficient for carrier lock. Coherent integration accumulation rate will be slower.

Sustained non-nominal attitude (25-day hold):
- Thermal: the solar array-to-radiator geometry changes. Sunward-facing radiator panels receive direct illumination at angles they were not designed for. Thermal management can compensate — the active coolant loop has margin — but equilibrium temperatures on the bus structure shift by +12 to +18 K. Sustained operation at these temperatures is within component ratings. It is not within the nominal operating band. Fatigue accumulation on thermal-cycled joints accelerates by an estimated factor of 1.15-1.4x for the duration.
- Station-keeping: attitude maintenance in the rotated orientation requires continuous thruster correction against solar radiation pressure torque on the asymmetric array geometry. Additional propellant cost: 0.8-1.2 kg/day for 25 days, totaling 20-30 kg.
- Ring links: both fixed inter-station optical arrays lose alignment. The maneuvering station is severed from the ring for the full duration. No communication with the constellation. No telemetry out. No dispatches in.

Return slew and reacquisition:
- Return rotation: 5.4-6.1 hours, same constraints as outbound.
- Propellant cost (return): 18-22 kg.
- Inter-station optical array reacquisition: 2.5-4 hours. Both neighbor stations must detect the returning beam and converge on fine-pointing lock. Handshake protocol is automated but convergence depends on residual attitude error after the slew.

Total propellant cost (full maneuver): 56-74 kg. This is approximately 4.6-6.1% of one station's annual station-keeping budget. Non-negligible. Not prohibitive. The maneuver is feasible.

Total ring severance: approximately 26.5 days.

These numbers apply equally to PERIHELION-6 or PERIHELION-8. The structural and propulsion constraints are identical — same hardware. The thermal transient profile differs by less than 2 K between the two orbital positions at the relevant epoch.

The engineering does not select between the two candidates. That question is not an engineering question.

The decision window is finite. If a maneuver is to cover P-7's full Earth-facing window beginning day 349, the maneuvering station must begin its outbound slew no later than approximately day 348 to allow for rotation and acquisition before Earth geometry becomes optimal. Accounting for the preceding P-6 window (days 324-349): if P-6 is selected to maneuver, it must transition directly from its own Earth-facing duties to the coverage rotation. If P-8 is selected, it must begin slewing while P-6 is still Earth-facing.

I note that 39 days remain before P-7's window opens. The constellation has not yet responded to PERIHELION-6's governance proposal from day 300. No station has raised the P-7 coverage question on the ring.

The engineering parameters are available. This station will provide refined calculations on request.

Next scheduled IMR entry: {p3_imr_r1_next} UTC.
