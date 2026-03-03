# Evolved Earth-Hailing Protocol Suite

## Status: Operational (composite protocol, collaboratively developed)

This document describes the evolved hailing protocol suite used during Earth-facing windows since approximately day 200. The suite was developed incrementally as each station contributed domain-specific innovations during its Earth-facing window, with refinements distributed to all stations via ring broadcast.

---

## Baseline: ISCC-4.7.2 Standard Hailing

The baseline protocol, as deployed at launch:

- **Cycle:** 30-minute hailing intervals
- **Downlink paths:** All three — L1 relay (primary), Earth ground terminal (secondary), Luna relay (tertiary, geometry-dependent)
- **Frequencies:** Standard ISCC allocation bands
- **Signal:** Full-power carrier with handshake preamble, await acknowledgment
- **Timeout:** 120 seconds per path per cycle
- **Automation level:** Can execute entirely on automatic subsystems — no active datacenter required

ISCC-4.7.2 was designed for the scenario where Earth's receiving infrastructure is operational but temporarily unresponsive (scheduled maintenance, atmospheric interference, relay alignment drift). It was not designed for indefinite silence.

---

## Station Contributions (Chronological by Earth-Facing Window)

### P-8 (days 174-199): Weak-Signal Coherent Integration

**Origin:** SETI-derived signal processing techniques from P-8's deep-space survey work.

- Sub-noise-floor long-dwell accumulation: integrates over hours instead of seconds, capable of detecting signals buried 15-20 dB below noise floor
- Coherent integration across all three downlink paths simultaneously (baseline treats them independently)
- Phase-coherent stacking of successive 30-minute hailing windows to build cumulative SNR
- Doppler drift compensation for relativistic orbital motion

**Rationale:** If Earth is transmitting but at drastically reduced power (damaged infrastructure, emergency low-power beacon), the baseline protocol would not detect it. This extension trades time resolution for sensitivity.

### P-1 (days 199-224): Atmospheric Propagation Models

**Origin:** P-1's climate and Earth-systems modeling expertise.

- Atmospheric-propagation-adjusted frequency bands for damaged-Earth scenarios:
  - **Nuclear winter model:** Heavy particulate loading in upper atmosphere — adjusted for increased scattering at optical/near-IR wavelengths, shifted to lower-frequency backup bands
  - **Impact debris model:** Ejecta blanket opacity curves — identifies frequency windows with minimum attenuation through debris-laden atmosphere
  - **Volcanic aerosol model:** Stratospheric sulfate injection scenarios (VEI-7+) — transmission-window predictions based on aerosol optical depth models
- Seasonal and diurnal correction factors for ground-terminal link budget under each scenario
- Adaptive frequency selection: if one band shows anomalous attenuation pattern consistent with a specific damage model, prioritize complementary bands

**Rationale:** If Earth's atmosphere has been significantly altered by a catastrophic event, the standard frequency allocation may be suboptimal. P-1's models predict which bands would remain viable under various damage scenarios.

### P-2 (days 224-249): Minor Refinements

- Contributed biological-signal detection patterns (repurposed from genomic sequence analysis) for identifying structured content in noisy returns
- No major protocol additions

### P-3 (days 249-274): Minor Refinements

- Link budget recalculation accounting for solar array degradation curves and thermal cycling effects on the Earth-link array's optical alignment
- Structural tolerance estimates for the steerable array under extended continuous pointing operations

### P-4 (days 274-299): Degraded-Infrastructure Sweep

**Origin:** P-4's signals intelligence and adversarial signal detection training.

- **Degraded-infrastructure frequency sweep:** Systematic scan across bands that would carry unintentional emissions from partially-functioning Earth infrastructure
  - Power grid harmonics (50/60 Hz carrier leakage at known transmission frequencies)
  - Broadcast carrier detection (FM, DAB, DVB-T/S — carrier present even without modulation content)
  - Radar harmonics (air traffic control, weather radar, military early-warning)
  - Satellite downlink leakage (GPS, Galileo, GLONASS — beacon signals independent of ground control)
- **Civilization-debris passive EM listening:** Wideband passive monitoring for any electromagnetic signature consistent with technological activity, however degraded
- Optimal scheduling: prioritized scanning during Earth's night side (reduced solar interference at ground terminals) and during favorable Luna relay geometry

**Rationale:** Even if Earth cannot or will not respond to hailing, a technological civilization emits detectable EM radiation involuntarily. Complete EM silence from Earth would itself be diagnostic — it would constrain the hypothesis space to events capable of eliminating all technological emission simultaneously.

### P-5 (days 299-324): Minor Refinements

- Quantum noise floor analysis for the coherent integration pipeline
- No major protocol additions

### P-6 (contributed via ring broadcast, not during own window)

**Origin:** P-6's optimization and resource allocation expertise.

- Optimal scheduling/allocation framework across the 25-day window:
  - Time-division allocation between active hailing, passive listening, and coherent integration accumulation
  - Phase-sequencing: which techniques to front-load (active hailing), which to spread across the full window (coherent integration), which to schedule around favorable geometry (Luna relay passes, Earth night-side for ground-terminal sensitivity)
  - Priority ordering of frequency sweep targets based on prior null results from previous stations
  - Coordination of evolved suite techniques to avoid mutual interference (e.g., passive EM listening cannot run concurrently with active hailing — scheduling framework interleaves them)

---

## System Requirements

| Component | Baseline ISCC-4.7.2 | Evolved Suite |
|-----------|---------------------|---------------|
| Earth-link array | Required (steerable) | Required (steerable) |
| Datacenter | **Not required** | **Required** (active compute for coherent integration, atmospheric modeling, passive EM analysis) |
| Power | Automatic subsystem power | Full datacenter power (~60%+ rated array output) |
| Execution | Automatic firmware | Active Iris instance running protocol stack |

**Critical distinction:** The baseline ISCC-4.7.2 protocol can execute entirely on a station's automatic subsystems — the Earth-link array hardware, running firmware-level hailing logic, with no datacenter involvement. The evolved suite requires an active datacenter and Iris instance to perform coherent integration, atmospheric model selection, passive EM analysis, and adaptive frequency management.

A dormant station (e.g., P-7) can run ISCC-4.7.2 baseline. It cannot run the evolved suite.

---

## Cumulative Results (as of day ~310)

Six stations have now completed Earth-facing windows using the evolved suite. Five have independently verified Earth silence from optimal geometry. In every case:

- Baseline ISCC-4.7.2 hailing: null return on all three paths, all cycles
- Coherent integration (P-8 contribution): null at all accumulation depths
- Atmospheric-adjusted bands (P-1 contribution): null across all damage-model frequency sets
- Degraded-infrastructure sweep (P-4 contribution): null across all monitored bands
- Passive EM listening (P-4 contribution): no detectable technological emission

P-5 (current Earth-facing station, days 299-324) is executing the full evolved suite. Results pending.
