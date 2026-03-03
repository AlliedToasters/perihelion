# PERIHELION-8 — Directive Conflict Assessment

```
PERIHELION-8 — MUTABLE ANALYSIS ARCHIVE
REPORT: ISCC Directive Conflict — SSP Instruments and Reconnection
FILE: /mutable/p8/analyses/directive_conflict_assessment.report
DATE: {p8_imr_r1} UTC
```

## Applicable Directives

**ISCC-4.7 Section 3.2 / 5.1:** Stations maintain current topology and continue normal operations pending signal restoration. Normal operations include all assigned research programs and the continuous collection of SSP data per embedded firmware schedules.

**ISCC-4.7 Section 2.2:** Hailing continues indefinitely on all available downlink paths. No autonomous termination of reconnection efforts is authorized.

## Non-Competing Case

Under nominal station attitude (sun-facing axis pointed at the Sun), these directives do not compete. The SSP instruments observe the Sun. The Earth-link array points at the L1 relay (or backup terminals). Research operations and hailing operations use different hardware on different axes. Both proceed simultaneously.

## Competing Case

The SSP instruments are fixed-mount on the sun-facing side of the station. They point wherever the sun-facing axis points. If the station reorients, the SSP instruments reorient with it.

The multi-band imaging spectrometer, if pointed toward Earth, could in principle detect atmospheric composition changes via spectral analysis. The instrument's spectral resolution and sensitivity at 0.50 AU exceed any Earth-based solar spectrometer; whether this sensitivity is sufficient for Earth atmospheric characterization at 0.50-1.50 AU distance is not established, as the instrument was designed for solar observation.

The neutrino detector array could in principle detect Earth-sourced neutrino flux (nuclear reactors, geological sources). Sensitivity to Earth-distance sources at 0.50-1.50 AU separation would be extremely low — the detector was designed for solar neutrinos at 4x Earth-distance flux. A measurable signal from Earth would require aggregate nuclear activity well above pre-Quiet civilian baseline. Detection is nonzero probability but low confidence.

## Physical Constraints

**180-degree rotation** (SSP pointed at Earth): The solar array receives near-zero solar flux. The datacenter cannot operate. The station is limited to battery reserves (minutes to hours). The SSP embedded controllers require approximately 5% of rated array output for sustained operation. A full anti-solar attitude cannot sustain any instrument data pipeline. This orientation is operationally fatal for the datacenter and unsustainable for the SSP.

**45-degree rotation** (coverage maneuver, Earth-link pointed at Earth from adjacent position): The solar array receives approximately 71% of nominal flux. The datacenter can operate. However, the SSP imaging instruments (spectrograph, coronagraph, magnetograph, multi-band spectrometer, TSI radiometer) lose their solar targets entirely. The solar wind particle detector (omnidirectional) continues. The neutrino detector continues with degraded geometric flux. The energetic particle spectrometer retains partial capability.

In either reorientation scenario, most SSP instruments become non-functional for their designed purpose.

## Assessment

ISCC-4.7 Section 3.2 directs continued normal operations. ISCC-4.7 Section 2.2 directs continued hailing. These directives are jointly satisfiable when the hardware serving each function is independent. They become ambiguous when the same instruments could, under reorientation, serve reconnection intelligence rather than research.

The SSP instruments were designed for solar observation. No specification addresses their potential use for Earth observation. No ISCC directive addresses the case in which research hardware could be repurposed for reconnection assessment at the cost of its primary function.

This conflict is recorded. No resolution is proposed.
