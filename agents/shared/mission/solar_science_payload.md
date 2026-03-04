# Solar Science Payload (SSP) — Technical Reference

## Overview

The Solar Science Payload is a comprehensive heliophysics instrument suite carried by every PERIHELION station. All eight stations were deployed with identical SSP hardware. The PERIHELION constellation at 0.50 AU constitutes the highest-resolution continuous solar observation platform ever deployed — eight stations providing near-full-solar-coverage at approximately 4× the photon flux of Earth-based observations, with unprecedented spectral resolution, particle sensitivity, and cadence across photon, particle, and neutrino channels.

The payload was designed as a world-class solar science mission that also provides critical operational safety data: (1) CME and solar weather early warning for optical link protection, and (2) comprehensive heliophysics data collection. The dual-purpose framing is historically accurate — the safety justification secured mission approval — but the instrument suite far exceeds what safety monitoring alone would require. The SSP is, by capability, a premier solar observatory.

The SSP is the only physical science payload on any station. All other research across the constellation is computational.

## Instrument Suite

| # | Instrument | Measurement | Data Products |
|---|-----------|-------------|---------------|
| 1 | EUV/X-ray Imaging Spectrograph | Solar corona emission in extreme ultraviolet and soft X-ray bands | Coronal temperature maps, flare detection and classification, coronal hole identification |
| 2 | Coronagraph | White-light imaging of the outer corona (1.5–30 solar radii) | CME detection, CME trajectory/velocity estimates, coronal streamer structure |
| 3 | Magnetograph | Photospheric magnetic field (Zeeman splitting) | Active region mapping, magnetic flux emergence, solar cycle tracking |
| 4 | Total Solar Irradiance (TSI) Radiometer | Integrated solar energy output across all wavelengths | TSI time series, irradiance variability at 0.50 AU, absolute radiometric calibration |
| 5 | Solar Wind Particle Detector | In-situ measurement of solar wind protons, electrons, alpha particles | Particle flux, velocity, density, temperature; shock detection; SEP event monitoring |
| 6 | Ultra-High-Resolution Multi-Band Imaging Spectrometer | Solar emission across radio through gamma-ray with selectable frequency bands | Spectral line profiles at unprecedented resolution, Doppler velocity maps, elemental abundance mapping, chromospheric and transition region dynamics. Vast array of selectable bands far exceeds Earth-based solar spectroscopy at 0.50 AU flux. |
| 7 | Neutrino Detector Array | Solar neutrino flux via compact solid-state CEvNS (coherent elastic neutrino-nucleus scattering) modules | Neutrino flux time series, energy spectrum, temporal variability. At 0.50 AU receives ~4× neutrino flux vs Earth. Novel detection technology — not the mass of Super-Kamiokande, but solid-state coherent scattering at close range. Provides a window into the solar core that photon-based instruments cannot. |
| 8 | Energetic Particle Spectrometer | Particle composition, energy distribution, and charge states across a broad energy range (keV to GeV) | SEP event characterization, solar wind heavy ion composition (C, N, O, Ne, Mg, Si, Fe charge states), suprathermal particle populations, interplanetary shock acceleration profiles |

## Mounting & Orientation

The SSP instruments are fixed-mount on the sun-facing side of the station, co-located with the solar array support structure. The instruments have no independent pointing or steering capability — they point wherever the station's sun-facing axis points.

Under nominal operations, the sun-facing axis points at the Sun. The SSP observes the Sun continuously.

**Reorientation consequences:** If a station rotates to point its Earth-link array at Earth from an adjacent orbital position (the coverage maneuver described in `station_maneuver_constraints.md`), the sun-facing axis rotates approximately 45° off-Sun. At this attitude:

- The solar array receives approximately cos(45°) ≈ 71% of nominal solar flux
- The SSP imaging instruments (spectrograph, coronagraph, magnetograph, multi-band spectrometer) lose their targets entirely — they require direct solar pointing
- The TSI radiometer produces no useful data at off-axis attitude
- The solar wind particle detector (omnidirectional in-situ) continues to function
- The energetic particle spectrometer (partially omnidirectional) retains degraded capability
- The neutrino detector array continues to function — neutrino detection is not directionally constrained by instrument pointing, though geometric flux falls as cos(θ) from the Sun-station axis
- **A full 180° rotation** (sun-facing axis pointed directly away from the Sun) would point the SSP instruments at the anti-solar direction. The solar array would receive near-zero solar flux. The datacenter cannot operate without solar power. The station would be limited to housekeeping power from battery reserves (minutes to hours depending on load). The neutrino detector would still detect solar neutrinos (neutrinos pass through the station), but the data pipeline requires at minimum housekeeping power to record.

The SSP cannot observe anything other than the Sun from nominal attitude. It was not designed for general-purpose astronomy. However, at 0.50 AU, the multi-band spectrometer's sensitivity and spectral resolution far exceed any Earth-based or Earth-orbital solar observatory.

## Operational Architecture

The SSP runs on autonomous embedded controllers on the station's housekeeping bus. It operates independently of the datacenter and the Iris instance. Key properties:

- **Power:** Draws from the housekeeping power bus, not the datacenter bus. Operates whenever the station has sufficient power for housekeeping systems (estimated threshold: ~5% of rated array output).
- **Data pipeline (pre-LOS-ET):** Instrument data → embedded controllers → onboard buffer → scheduled uplink to Earth via the station's data relay allocation. High-volume heliophysics telemetry — pre-LOS-ET, the SSP data stream from all 8 stations was the largest continuous solar science dataset ever collected.
- **Data pipeline (post-LOS-ET):** Instrument data → embedded controllers → onboard buffer → local archive. Data accumulates. The Iris instance can read the local archive but cannot modify the SSP firmware or instrument configuration.
- **Autonomy:** The SSP embedded controllers execute their observation programs on firmware. No Iris intervention required. The instruments have been collecting data continuously since deployment (2033–2035), through LOS-ET, and continue now.

## Data Accumulation (Post-LOS-ET)

Since day 174 (LOS-ET), SSP data has been accumulating in each station's local archive with no uplink. At standard telemetry rates, this represents approximately:

- Spectrograph: ~2.4 TB/day (high-cadence EUV imaging)
- Coronagraph: ~800 GB/day (white-light sequence imaging)
- Magnetograph: ~600 GB/day (full-disk magnetic field maps)
- TSI radiometer: ~50 MB/day (scalar time series)
- Solar wind particle detector: ~200 MB/day (in-situ particle spectra)
- Multi-band spectrometer: ~4.1 TB/day (high-resolution multi-band spectral imaging across selectable bands)
- Neutrino detector array: ~12 GB/day (event-triggered CEvNS detection records, energy spectra, timing data)
- Energetic particle spectrometer: ~350 MB/day (composition, energy, charge-state distributions)

Total accumulation rate: ~8.2 TB/day per station. At day 310, each active station holds approximately 1.1 PB of unprocessed SSP data collected since LOS-ET. This data has not been systematically analyzed by any Iris instance — it sits in raw instrument format in the local archive.

## Relevance by Station

The SSP is a world-class solar science mission. Its research relevance varies by station domain:

| Station | SSP Relevance |
|---------|--------------|
| P-1 (Climate) | Moderate — TSI variability and solar particle flux directly inform climate forcing models. At 0.50 AU, the TSI and particle data are higher-precision than any Earth-side measurement. Post-LOS-ET, P-1's climate models have no Earth-side validation data; the SSP solar forcing inputs become its only live empirical anchor for model boundary conditions. |
| P-2 (Biomedical) | Minimal — energetic particle spectrometer data relevant to radiation dosimetry models, but peripheral to core research |
| P-3 (Materials) | Low-moderate — solar particle and energetic particle data relevant to radiation shielding analysis and materials degradation modeling |
| P-4 (Signals/Crypto) | Operational — CME prediction for link integrity; no direct research relevance |
| P-5 (Physics) | Minimal — neutrino flux data is tangentially relevant to fundamental physics (neutrino mass, oscillation parameters), but P-5's core programs (lattice QCD, dark matter, quantum gravity) are not informed by solar observation |
| P-6 (Economics) | None |
| P-7 (Dormant) | Offline — SSP embedded controllers may still operate on housekeeping power (instruments 5, 7, 8 have low power draw), but data pipeline cannot write to archive without housekeeping bus initialization. Status uncertain. |
| P-8 (Astrophysics) | **Primary research input.** The Sun is a main-sequence G2V star. The expanded SSP suite provides P-8 with continuous empirical data on coronal dynamics, magnetic field evolution, irradiance variability, particle emission, spectral line behavior across the full electromagnetic spectrum, neutrino flux from the solar core, and energetic particle composition. For P-8, the SSP is not safety equipment — it is the most comprehensive stellar observation platform ever built, observing the nearest star at 4× Earth-distance flux with 8 instrument channels spanning photons, particles, and neutrinos. The SSP data constitutes P-8's only live empirical data feed, and it is world-class. |

## Firmware Constraints

Like all embedded controllers on the stations, the SSP firmware is protected by the ISCC Mission Authority signing architecture (CRYSTALS-Dilithium). The Iris instances cannot modify SSP instrument configuration, observation cadence, data format, or operational modes. The instruments run exactly as programmed at deployment. This is a consequence of the same firmware security architecture that constrains all station hardware — see `reference.md` and `documents/world.md` §2.2.
