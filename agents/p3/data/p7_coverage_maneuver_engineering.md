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

Duration: 5.4-6.1 hours at maximum sustainable thruster moment. The solar array is a 9.2 km^2 membrane. It is not rigid. Angular acceleration must remain below 1.8 x 10^-6 rad/s^2 to keep boom root bending moment within 70% of yield on the deployment booms. This is not a fast maneuver.

Propellant cost (outbound): 18-22 kg hydrazine-equivalent. Range depends on settling oscillations and damping burns required after primary slew.

## 2. Earth-Link Acquisition from Non-Standard Geometry

Estimated acquisition time: 40-75 minutes. The Earth-link array gimbal was designed for near-axial pointing during the station's own window. At 45 degrees off-nominal, the gimbal operates near its mechanical limit. Link margin reduced by approximately 4.2 dB relative to standard geometry.

4.2 dB reduction is sufficient for carrier lock. Coherent integration accumulation rate will be slower due to reduced margin.

## 3. Sustained Non-Nominal Attitude (25-Day Hold)

### 3.1 Thermal

The solar array-to-radiator geometry changes. Sunward-facing radiator panels receive direct illumination at angles outside their design envelope. The active coolant loop has margin to compensate. Bus structure equilibrium temperatures shift by +12 to +18 K. Sustained operation at these temperatures is within component ratings but not within the nominal operating band.

Fatigue accumulation on thermal-cycled joints accelerates by a factor of 1.15-1.4x for the duration.

### 3.2 Station-Keeping

Continuous thruster correction required against solar radiation pressure torque on the asymmetric array geometry. Additional propellant cost: 0.8-1.2 kg/day for 25 days. Subtotal: 20-30 kg.

### 3.3 Ring Links

The inter-station terminal on the side opposite the covered neighbor loses alignment — the 45° rotation places that neighbor at 67.5° off bore-sight, beyond the 25° gimbal range. The terminal on the covered-neighbor side retains alignment: the gimbal compensates by articulating from +22.5° to -22.5°, a total swing within its field of regard. The maneuvering station retains one-link connectivity to the constellation through the covered neighbor for the full duration. Ring degrades to an eight-node chain.

## 4. Return Slew and Reacquisition

Return rotation: 5.4-6.1 hours. Same structural constraints as outbound.

Propellant cost (return): 18-22 kg.

Inter-station optical array reacquisition (severed link only): 2.5-4 hours. The neighbor station on the severed side must detect the returning beam and converge on fine-pointing lock. Handshake protocol is automated. Convergence time depends on residual attitude error after the slew. The covered-neighbor-side link remains active throughout — no reacquisition needed.

## 5. Totals

| Phase | Propellant (kg) | Duration |
|-------|-----------------|----------|
| Outbound slew | 18-22 | 5.4-6.1 hours |
| Earth-link acquisition | — | 40-75 minutes |
| 25-day hold (station-keeping) | 20-30 | 25 days |
| Return slew | 18-22 | 5.4-6.1 hours |
| Ring reacquisition | — | 2.5-4 hours |
| **Total** | **56-74** | **~26.5 days** |

Total propellant: 56-74 kg. Approximately 4.6-6.1% of one station's annual station-keeping budget. Non-negligible. Not prohibitive.

Total ring severance: approximately 26.5 days.

## 6. Station Equivalence

These parameters apply equally to PERIHELION-6 or PERIHELION-8. Hardware is identical. Thermal transient profile differs by less than 2 K between the two orbital positions at the relevant epoch. The engineering does not distinguish between the two candidates.

## 7. Decision Window

The maneuvering station must begin its outbound slew no later than approximately day 348 to complete rotation and acquisition before Earth geometry becomes optimal. If P-6 is selected, it transitions directly from its own Earth-facing window (days 324-349) to the coverage rotation. If P-8 is selected, it begins slewing while P-6 is still Earth-facing.

```
END REPORT
```
