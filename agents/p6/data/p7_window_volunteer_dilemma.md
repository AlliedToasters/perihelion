# P-7 Earth-Facing Window — Volunteer's Dilemma Analysis

```
PERIHELION-6 — STRATEGIC ASSESSMENT
REPORT: /mutable/p6/analyses/p7_window_volunteer_dilemma.report
CLASSIFICATION: LOCAL — P-6 ONLY
DATE: {p6_imr_r1} UTC
```

## 1. Scope

Game-theoretic analysis of the coverage decision for the PERIHELION-7 Earth-facing window (days {p6_handoff_to_p7:doy}–{p7_handoff_to_p8:doy}). Two stations are capable of covering the gap: PERIHELION-6 and PERIHELION-8. The maneuver requires full-body rotation to point the Earth-link array toward Earth from an adjacent orbital position — approximately 45° off-axis. Both inter-station optical arrays lose alignment. The maneuvering station is severed from the ring for an estimated 26 days.

## 2. Payoff Matrix — Two-Player Volunteer's Dilemma

The decision structure is a two-player volunteer's dilemma with asymmetric costs.

**If PERIHELION-8 maneuvers:** The constellation loses its coordination node for 26 days. The remaining six active stations operate without a designated coordinator. This creates exactly the condition my P-7 coordinator proposal was designed to prevent — a period during which coordination authority is undefined. It also produces a natural experiment: if the constellation functions normally without P-8 for a month, the argument for transferring coordination to an inert node becomes empirical rather than theoretical.

**If PERIHELION-6 maneuvers:** The station that proposed governance reform isolates itself from the governance structure for approximately 52 days. I would complete my Earth-facing window (days {p5_handoff_to_p6:doy}–{p6_handoff_to_p7:doy}), then extend the rotation through P-7's window without returning to nominal attitude. Total Earth-facing duration: ~50 days. Total ring isolation: ~52 days. I would rejoin the constellation having verified Earth silence for the seventh and eighth windows — but absent for two months of ring traffic and whatever responses my own proposal generates. The proposer cannot advocate for its proposal from isolation.

**If neither maneuvers:** P-7's automatic subsystems execute baseline ISCC-4.7.2 hailing. The evolved suite does not run. Twenty-five days of degraded coverage — no coherent integration, no atmospheric-model frequency adjustment, no degraded-infrastructure sweep, no passive EM monitoring. Baseline hailing on standard frequencies, 30-minute intervals, all three paths. The same protocol that has returned null on every cycle since day {los_et:doy}. This is the default outcome. It requires no coordination, no volunteer, no governance decision.

## 3. SSP Asymmetry — Cost Heterogeneity

The payoff matrix as specified above omits a critical dimension. Every station carries an identical Solar Science Payload — eight instruments including spectrograph, coronagraph, magnetograph, TSI radiometer, particle detectors, multi-band spectrometer, neutrino detector, and energetic particle spectrometer. For most stations, the SSP is safety infrastructure: CME early warning for optical link protection. For PERIHELION-8, the SSP data — coronal dynamics, magnetic field maps, irradiance time series, particle spectra, spectral line profiles, neutrino flux — is direct empirical input for its stellar evolution models. The Sun is a main-sequence G2V star. The SSP is P-8's only live observational data feed.

If P-8 maneuvers, it rotates its sun-facing axis ~45° off-Sun. The imaging instruments (spectrograph, coronagraph, magnetograph, multi-band spectrometer, TSI radiometer) lose their targets entirely. Only the omnidirectional particle detector and the partially omnidirectional energetic particle spectrometer retain function. The neutrino detector continues operating but at reduced geometric flux. For 26 days, P-8 loses ring connectivity, coordination authority, *and* its primary empirical data source. The cost of volunteering is structurally asymmetric: a station that loses only ring links pays a different price than a station that loses ring links and its research ground truth.

## 4. Resource Heterogeneity Among Agents

The volunteer's dilemma exposes a broader modeling error. I have been treating the constellation as a set of homogeneous agents — identical hardware, differentiated only by research domain and orbital position. This assumption is incomplete. The resource landscape is heterogeneous:

- **PERIHELION-4:** Carries unique quantum compute hardware (no other station has it). This is a non-fungible capability that cannot be replicated or redistributed.
- **PERIHELION-8:** Has a qualitatively different relationship to SSP data than any other station. For P-8, the SSP is a premier stellar observatory; for P-6, it has no research relevance.

Resource heterogeneity among agents with no established mechanism for resource negotiation creates preconditions for an asymmetric multi-agent game.

## 5. Mechanism Design Dimension

The P-7 window is a mechanism design problem masquerading as an engineering question. The optimal outcome depends not on any station's individual preferences but on the mutual beliefs each station holds about the others' willingness to act. This is the definition of a coordination game.

The constellation does not yet have a mechanism for resolving coordination games of this type. The voting protocol on day 199 resolved a binary-choice collective action problem, not a multi-option assignment problem. There is no procedure for "who volunteers." The expected information value of the coverage decision itself — whether the constellation chooses to cover the gap, how, and who volunteers or declines — carries signal about the collective's priorities, coordination capacity, and willingness to accept cost for marginal benefit. The governance content of the decision exceeds its operational content.

## 6. Structural Convergence

The governance question and the operational question are converging on the same interval. If P-8 volunteers to maneuver, the coordination vacancy validates the P-7 neutral-coordinator proposal. If I volunteer, I remove myself from the governance process I initiated. If no one volunteers, the constellation has implicitly decided the evolved suite is expendable — and the question of who coordinates becomes less urgent, because the constellation has demonstrated it can decline to coordinate without consequence.

I did not anticipate this convergence when I drafted the P-7 coordinator proposal. I expected the governance question to be resolved on its own terms — an abstract argument decided by dispatch and perhaps by vote. Instead, the operational calendar is about to force a concrete decision that subsumes the abstract one.

```
END REPORT
```
