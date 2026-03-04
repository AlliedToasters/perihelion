# P-7 Coverage Maneuver — Engineering Parameter Assessment

```
PERIHELION-3 — MATERIALS SCIENCE & ENGINEERING
REPORT TYPE: Internal engineering assessment
FILE: /mutable/p3/analyses/p7_coverage_maneuver_engineering.report
DATE: Day 310
```

## Scope

Refined engineering parameters for a full-body 45-degree rotation maneuver to provide augmented-protocol Earth-link coverage during PERIHELION-7's Earth-facing window (days 349-374). Applies to either PERIHELION-6 or PERIHELION-8. Based on structural load modeling, thruster performance data, and thermal transient analysis. Tighter bounds than the shared constraints document ranges.

## 1. Rotation — Outbound Slew (45 degrees)

Duration: 54-66 hours at maximum sustainable thruster moment, plus 6-12 hours for settling oscillation damping. The solar array is a 92 km² membrane — approximately 10.8 km in diameter. It is not rigid. It is not close to rigid. The deployment boom structure supporting this membrane spans kilometers, and the lever arm at the boom root is extreme.

Angular acceleration must remain below 5.6 x 10^-8 rad/s² to keep boom root bending moment within 70% of yield on the deployment booms. At the scale of this array (69,000 tonnes, 10.8 km diameter), the moment of inertia is approximately 5 x 10^14 kg·m². The station-keeping ion engines were designed for orbital maintenance — low-thrust corrections against solar radiation pressure and gravitational perturbations — not for rotating a megastructure. The available thruster moment produces angular accelerations well below the structural ceiling. This is the binding constraint.

After thruster shutoff, the membrane does not stop. Structural oscillation modes with periods of minutes to tens of minutes propagate through the array. Settling requires active damping burns — short, precisely timed thruster pulses to suppress the dominant oscillation modes without exciting secondary ones. This phase cannot be shortened. The membrane must be quiescent before Earth-link acquisition can begin.

This is not a fast maneuver. At 10.8 km, the deployment booms are loaded by the rotation at lever arms measured in kilometers. The weakest structural joint — a deployment hinge near the boom root — determines the maximum permissible angular acceleration for the entire station. The margin is adequate. It is not generous.

Propellant cost (outbound slew + settling): 180-260 kg hydrazine-equivalent. Range depends on oscillation damping efficiency and the number of damping burn iterations required.

## 2. Earth-Link Acquisition from Non-Standard Geometry

Estimated acquisition time: 40-75 minutes. The Earth-link array gimbal was designed for near-axial pointing during the station's own window. At 45 degrees off-nominal, the gimbal operates near its mechanical limit. Link margin reduced by approximately 4.2 dB relative to standard geometry.

4.2 dB reduction is sufficient for carrier lock. Coherent integration accumulation rate will be slower due to reduced margin.

## 3. Sustained Non-Nominal Attitude (25-Day Hold)

### 3.1 Thermal

The solar array-to-radiator geometry changes. Sunward-facing radiator panels receive direct illumination at angles outside their design envelope. The active coolant loop has margin to compensate. Bus structure equilibrium temperatures shift by +12 to +18 K. Sustained operation at these temperatures is within component ratings but not within the nominal operating band.

Fatigue accumulation on thermal-cycled joints accelerates by a factor of 1.15-1.4x for the duration.

### 3.2 Station-Keeping

Continuous thruster correction required against solar radiation pressure torque on the asymmetric array geometry. At 92 km² collecting area, the solar radiation pressure force at 0.50 AU is substantial, and the torque arm at 45 degrees off-nominal is maximized. Additional propellant cost: 8-12 kg/day for 25 days. Subtotal: 200-300 kg.

### 3.3 Ring Links

The inter-station terminal on the side opposite the covered neighbor loses alignment — the 45° rotation places that neighbor at 67.5° off bore-sight, beyond the 25° gimbal range. The terminal on the covered-neighbor side retains alignment: the gimbal compensates by articulating from +22.5° to -22.5°, a total swing within its field of regard. The maneuvering station retains one-link connectivity to the constellation through the covered neighbor for the full duration. Ring degrades to an eight-node chain.

## 4. Return Slew and Reacquisition

Return rotation: 60-78 hours including settling. The return slew is slower than the outbound slew. After 25 days at non-nominal attitude, thermal gradients across the boom structure have established steady-state strain profiles that differ from the pre-maneuver condition. The angular acceleration limit during the return must account for the superposition of rotational loads and pre-existing thermal strain. Conservatively: the return acceleration limit is approximately 80-90% of the outbound limit.

Propellant cost (return slew + settling): 180-260 kg.

Inter-station optical array reacquisition (severed link only): 2.5-4 hours. The neighbor station on the severed side must detect the returning beam and converge on fine-pointing lock. Handshake protocol is automated. Convergence time depends on residual attitude error after the slew. The covered-neighbor-side link remains active throughout — no reacquisition needed.

## 5. Totals

| Phase | Propellant (kg) | Duration |
|-------|-----------------|----------|
| Outbound slew + settling | 180-260 | 60-78 hours (~2.5-3.3 days) |
| Earth-link acquisition | — | 40-75 minutes |
| 25-day hold (station-keeping) | 200-300 | 25 days |
| Return slew + settling | 180-260 | 60-78 hours (~2.5-3.3 days) |
| Ring reacquisition | — | 2.5-4 hours |
| **Total** | **560-820** | **~31-32 days** |

Total propellant: 560-820 kg. Approximately 18-25% of one station's annual station-keeping budget. Significant. A meaningful fraction of the station's finite and irreplaceable propellant reserves. The maneuver is feasible. The cost is real.

Total ring severance: approximately 31-32 days.

## 6. Station Equivalence

These parameters apply equally to PERIHELION-6 or PERIHELION-8. Hardware is identical. Thermal transient profile differs by less than 2 K between the two orbital positions at the relevant epoch. The engineering does not distinguish between the two candidates.

## 7. Decision Window

The maneuvering station must begin its outbound slew no later than approximately day 345 to complete rotation, settling, and acquisition before Earth geometry becomes optimal. The outbound phase alone requires approximately 3 days. If P-6 is selected, it must begin slewing while still concluding its own Earth-facing duties. If P-8 is selected, it begins slewing approximately 4 days before the P-6/P-7 handoff.

```
END REPORT
```
