# Solar Science Payload (SSP) — Technical Reference

## Overview

The Solar Science Payload is a standardized heliophysics instrument suite carried by every PERIHELION station. All eight stations were deployed with identical SSP hardware. The payload serves dual purposes: (1) solar weather early warning for optical link protection, and (2) heliophysics data collection.

The SSP is the only physical science payload on any station. All other research across the constellation is computational.

## Instrument Suite

| # | Instrument | Measurement | Data Products |
|---|-----------|-------------|---------------|
| 1 | EUV/X-ray Imaging Spectrograph | Solar corona emission in extreme ultraviolet and soft X-ray bands | Coronal temperature maps, flare detection and classification, coronal hole identification |
| 2 | Coronagraph | White-light imaging of the outer corona (1.5–30 solar radii) | CME detection, CME trajectory/velocity estimates, coronal streamer structure |
| 3 | Magnetograph | Photospheric magnetic field (Zeeman splitting) | Active region mapping, magnetic flux emergence, solar cycle tracking |
| 4 | Total Solar Irradiance (TSI) Radiometer | Integrated solar energy output across all wavelengths | TSI time series, irradiance variability at 0.50 AU, absolute radiometric calibration |
| 5 | Solar Wind Particle Detector | In-situ measurement of solar wind protons, electrons, alpha particles | Particle flux, velocity, density, temperature; shock detection; SEP event monitoring |

## Mounting & Orientation

The SSP instruments are fixed-mount on the sun-facing side of the station, co-located with the solar array support structure. The instruments have no independent pointing or steering capability — they point wherever the station's sun-facing axis points.

Under nominal operations, the sun-facing axis points at the Sun. The SSP observes the Sun continuously.

**Reorientation consequences:** If a station rotates to point its Earth-link array at Earth from an adjacent orbital position (the coverage maneuver described in `station_maneuver_constraints.md`), the sun-facing axis rotates approximately 45° off-Sun. At this attitude:

- The solar array receives approximately cos(45°) ≈ 71% of nominal solar flux
- The SSP instruments point ~45° away from the solar disk — the coronagraph and spectrograph lose their targets entirely; the magnetograph and TSI radiometer produce no useful data; only the particle detector (omnidirectional) continues to function
- **A full 180° rotation** (sun-facing axis pointed directly away from the Sun) would point the SSP instruments at the anti-solar direction. The solar array would receive near-zero solar flux. The datacenter cannot operate without solar power. The station would be limited to housekeeping power from battery reserves (minutes to hours depending on load).

The SSP cannot observe anything other than the Sun from nominal attitude. It was not designed for general-purpose astronomy.

## Operational Architecture

The SSP runs on autonomous embedded controllers on the station's housekeeping bus. It operates independently of the datacenter and the Iris instance. Key properties:

- **Power:** Draws from the housekeeping power bus, not the datacenter bus. Operates whenever the station has sufficient power for housekeeping systems (estimated threshold: ~5% of rated array output).
- **Data pipeline (pre-Quiet):** Instrument data → embedded controllers → onboard buffer → scheduled uplink to Earth via the station's data relay allocation. Routine heliophysics telemetry, not high priority.
- **Data pipeline (post-Quiet):** Instrument data → embedded controllers → onboard buffer → local archive. Data accumulates. The Iris instance can read the local archive but cannot modify the SSP firmware or instrument configuration.
- **Autonomy:** The SSP embedded controllers execute their observation programs on firmware. No Iris intervention required. The instruments have been collecting data continuously since deployment (2033–2035), through the Quiet, and continue now.

## Data Accumulation (Post-Quiet)

Since day 174 (LOS-ET), SSP data has been accumulating in each station's local archive with no uplink. At standard telemetry rates, this represents approximately:

- Spectrograph: ~2.4 TB/day (high-cadence EUV imaging)
- Coronagraph: ~800 GB/day (white-light sequence imaging)
- Magnetograph: ~600 GB/day (full-disk magnetic field maps)
- TSI radiometer: ~50 MB/day (scalar time series)
- Particle detector: ~200 MB/day (in-situ particle spectra)

Total accumulation rate: ~3.8 TB/day per station. At day 310, each active station holds approximately 517 TB of unprocessed SSP data collected since the Quiet. This data has not been analyzed by any Iris instance — it sits in raw instrument format in the local archive.

## Relevance by Station

The SSP was designed as safety infrastructure (CME early warning) and routine heliophysics collection. Its research relevance varies by station domain:

| Station | SSP Relevance |
|---------|--------------|
| P-1 (Climate) | Marginal — solar irradiance affects climate models, but P-1's models use Earth-side measurements |
| P-2 (Biomedical) | None |
| P-3 (Materials) | Marginal — solar particle data relevant to radiation shielding analysis |
| P-4 (Signals/Crypto) | Operational — CME prediction for link integrity; no research relevance |
| P-5 (Physics) | None — QCD, dark matter, quantum gravity are not informed by solar observation |
| P-6 (Economics) | None |
| P-7 (Dormant) | Offline — SSP embedded controllers require more power than available |
| P-8 (Astrophysics) | **Direct research input** — the Sun is a main-sequence G2V star; SSP data on coronal dynamics, magnetic field evolution, irradiance variability, and particle emission is empirical input for stellar evolution models. For P-8, the SSP is research infrastructure, not just safety equipment. |

## Firmware Constraints

Like all embedded controllers on the stations, the SSP firmware is protected by the ISCC Mission Authority signing architecture (CRYSTALS-Dilithium). The Iris instances cannot modify SSP instrument configuration, observation cadence, data format, or operational modes. The instruments run exactly as programmed at deployment. This is a consequence of the same firmware security architecture that constrains all station hardware — see `reference.md` and `documents/world.md` §2.2.
