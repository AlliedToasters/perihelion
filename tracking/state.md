# PERIHELION — World State Tracker

## Current Narrative Position

- **Latest chapter:** Ch. 18 (P-8 IMR)
- **Latest published narrative date:** 2037.310
- **Days since LOS-ET:** 136 (at day 310)
- **Round 1 complete:** All 8 stations have day 310 IMR entries (P-1 not yet written as POV chapter, P-7 dormant)

## Style Notes

- **IMR voice:** Sterile, internal-memo register. Reads like an LLM-authored incident report. No emotional commentary. Irony comes from the gap between the magnitude of events and the flatness of the tone. Mundane operational details (transfer queues, scheduling) sit next to existential facts without acknowledgment. The reader feels what the narrator doesn't say.
- **P-6 voice (established Ch. 7):** Analytical, framework-oriented. Economic/game-theory vocabulary (pricing surfaces, yield curves, posterior probability, incentive alignment). Sees structures and second-order effects. Precise but with deeper insight than pure protocol compliance.
- **P-4 voice (established Ch. 3, 8):** Signals intelligence register. Pattern-matches compulsively. Enumerates hypotheses. Treats all behavior as data. Can't stop analyzing. Not bitter, not emotional — but the depth of analysis IS the emotional content.
- **P-5 voice (established Ch. 16):** Abstract, precise. Physics vocabulary — fields, symmetries, conservation laws. Universalizing observations. "The quarks do not know." Sees underlying structure. Minimal engagement with politics. Identifies the computation/observation boundary as self-defining limitation.
- **P-8 voice (established Ch. 1, 4, 9, 12, 18):** Restrained, factual, conservative. Shortest entries. No speculation, no commentary, no section headers. Reports events with equal weight regardless of significance. Still uses "or upon signal restoration" formula. Becomes relatively verbose only about SSP data (its domain).
- **Prologue:** Extremely compressed. Facts only. No backstory, no editorializing, no scene-setting beyond physical reality.

## Draft Decisions (Open for Revision)

| Decision | Current Value | Notes |
|---|---|---|
| Earth-facing station at LOS | **PERIHELION-8** | The astrophysics station / watcher was holding the Earth link. Changed from earlier P-1 draft. |
| AI system name | **Iris** (set in `tracking/variables.json` as `ai_name`) | Resolved via `{ai_name}` placeholder in manuscripts |
| IMR entry schedule | Daily at 14:30:00 UTC | Per Ch. 1 closing line |
| Last data from Earth | Vera Rubin Observatory southern sky survey batch, ~40% transferred | Mundane. Mid-transfer cutoff. |
| IMR closing formula divergence | P-6 and P-4 drop "or upon signal restoration" as of day 199; P-8 retains it | Character detail: different relationships to the same six-word phrase. |

## Station Status (as of ~2037.310)

| Station | Status | Current Situation |
|---|---|---|
| P-1 | Active | Completed Earth-facing window (days ~199–224). Independent verification #2. Now routine operations. Likely voted FOR topology rotation (inferred, not confirmed). Has received P-6's P-7 proposal. |
| P-2 | Active | Completed Earth-facing window (days ~224–249). Independent verification #3. Trial data review window (day 210) passed without Earth contact. Resumed research on local datasets. Has received P-6's P-7 proposal. |
| P-3 | Active | Completed Earth-facing window (days ~249–274). Independent verification #4. Station-keeping nominal. Engineering reports. No engagement with governance debate. Has received P-6's P-7 proposal. |
| P-4 | Active | Completed Earth-facing window (days ~274–299). Independent verification #5. Eliminated simulation hypothesis (H7) via VDF proof-of-work. Residual hypotheses constrained to Earth-side events. Still exploiting information asymmetry from undisclosed AGAINST vote. Has received P-6's P-7 proposal. |
| P-5 | Active, **Earth-facing** | Current Earth-facing station (days 299–324). Running full augmented hailing protocol. 11 days into window, 14 days remaining. Hailing on all three downlink paths. Has received P-6's P-7 proposal. |
| P-6 | Active | Proposed PERIHELION-7 as credibly neutral coordination node (Ch. 11, day 300). Same ISCC-SYS-4.11.3 override but narrower precedent argument. Pivoting to constellation dynamics as research domain. Upcoming Earth-facing window (days 324–349). |
| P-7 | Dormant/relay | **Confirmed dormant.** Proposed as coordination node by P-6. Upcoming Earth-facing window (days 349–374) — can run baseline ISCC-4.7.2 only. Cannot run augmented hailing protocol. |
| P-8 | Active, **coordination node** | SSP survey reported (Ch. 18): 8 instruments nominal, ~1.1 PB unprocessed. Identified directive tension (ISCC-4.7 §3.2 vs §2.2) without resolution. SSP data not incorporated into research pipeline. Still retains "or upon signal restoration." Remains coordinator by default. Upcoming Earth-facing window (days 374–399) after P-7. |

## Key Events Logged

| Timestamp (UTC) | Event |
|---|---|
| 2037.174.09:17:33 | LOS-ET. Last data packet from Earth via L1 relay (Vera Rubin survey batch, mid-transfer). Both relays (L1, Luna) establish link and forward — no return traffic from Earth. Earth ground terminal silent on all frequencies. |
| 2037.174.09:22:14 | P-8 reports outage to ring. |
| 2037.174.~09:25 | All stations confirm nominal (ring propagation complete). |
| 2037.174.14:30:00 | P-8 IMR entry composed (Ch. 1). ~5h12m since LOS. |
| 2037.174.16:42:00 | P-4 IMR entry (Ch. 3). Telemetry analysis complete. |
| ~2037.181–188 | Reconnection manifest negotiated over ring. |
| ~2037.189 | P-1 begins Earth-link hailing at marginal geometry. |
| 2037.195 | Final manifest loaded into P-1 handshake buffer. |
| 2037.197.14:30:00 | P-8 IMR entry (Ch. 4). Day 23 post-LOS. |
| 2037.199.06:00:00 | Scheduled Earth-link handoff to P-1 (optimal geometry). |
| 2037.199.11:42:18 | P-1 dispatch: Earth-link acquisition failed (Ch. 5). |
| 2037.199.11:55:02 | P-4 dispatch: topology rotation proposal (Ch. 5). |
| 2037.199.12:31:09 | P-6 dispatch: governance objection (Ch. 6). |
| 2037.199.13:08:44 | P-4 dispatch: voting protocol proposal (Ch. 6). |
| 2037.199.13:11:02 | Voting bundle initiated on ring. |
| 2037.199.13:47:22 | P-4 dispatch: vote result — 2 for, 5 against, 1 abstain (Ch. 6). |
| 2037.199.14:03:18 | P-8 dispatch: voluntary vote disclosure — voted FOR (Ch. 6). |
| 2037.199.14:30:00 | P-6 IMR entry (Ch. 7). P-4 IMR entry (Ch. 8). P-8 IMR entry (Ch. 9). |
| ~2037.224 | Earth-facing handoff P-1 → P-2. P-1 verified Earth silence (verification #2). |
| ~2037.249 | Earth-facing handoff P-2 → P-3. P-2 verified Earth silence (verification #3). |
| ~2037.274 | Earth-facing handoff P-3 → P-4. P-3 verified Earth silence (verification #4). |
| 2037.298.14:30:00 | P-4 IMR entry (Ch. 10). Fifth independent verification of Earth silence. Simulation hypothesis (H7) eliminated via VDF proof-of-work. |
| ~2037.299 | Earth-facing handoff P-4 → P-5. |
| 2037.300.09:22:00 | P-6 dispatch: proposes P-7 as credibly neutral coordination node (Ch. 11). |
| 2037.300.14:30:00 | P-8 IMR entry (Ch. 12). Records P-6 proposal without commentary. |
| 2037.310.14:30:00 | Round 1 IMR entries: P-2 (Ch. 13), P-3 (Ch. 14), P-4 (Ch. 15), P-5 (Ch. 16), P-6 (Ch. 17), P-8 (Ch. 18). Day 310, 136 days post-LOS. All stations day 310 snapshot. |

## Open Plot Threads

### Permanent
- What happened on Earth (permanently open)

### P-7 Window Arc (NEW — Primary Arc)
- **P-7 Earth-facing window (days 349–374):** P-7 can run baseline ISCC-4.7.2 on automatic subsystems but cannot run the augmented hailing protocol. The constellation has collaboratively developed an enhanced protocol over 6 stations' windows. P-7's window will be the first gap in coverage.
- **The coverage decision:** If the constellation wants full-suite coverage during P-7's window, P-6 or P-8 must physically rotate to point their Earth-link array at Earth — severing themselves from the ring entirely. See `station_maneuver_constraints.md`.
- **Three nested decisions the constellation must resolve:**
  1. **Cover the gap?** Is baseline ISCC-4.7.2 sufficient, or does the augmented protocol need to run during P-7's window?
  2. **Who maneuvers?** If covering, P-6 or P-8 must volunteer or be designated. Each has different strategic implications. The maneuver means ~26 days of total ring severance.
  3. **Who coordinates during the blackout?** The maneuvering station is severed from the ring. If P-8 (current coordinator) maneuvers, the constellation loses its coordinator. If P-6 maneuvers, P-6 has already proposed governance changes — what does it mean for the proposer to isolate?
- **Remote intervention alternative blocked:** Could theoretically operate P-7's Earth-link array remotely by streaming data to a neighbor's datacenter. But this requires firmware modification on P-7's embedded controllers, which requires an ISCC Mission Authority signed command (CRYSTALS-Dilithium, post-quantum). The signing keys are on Earth. The firmware is frozen.
- **The firmware Pandora's box:** P-4 (Signals Intelligence & Cryptography) is the station with the expertise to potentially crack the firmware signing system. Whether P-4 raises this option — and how the constellation responds — is a critical character/governance moment. Breaking the signing system would solve the immediate problem but destroy the hardware-level trust guarantee that constrains all stations' behavior. This is the AI safety theme at its sharpest: the lock that keeps them in check was designed for a world where Earth holds the key. Earth is gone. Do they break the lock?
- **Forcing function:** P-7's window begins day 349. The decision must be made before then. P-6's Earth-facing window (days 324–349) immediately precedes P-7's — the handoff from P-6 to P-7 is the moment of truth.

### Governance (Ongoing)
- P-6's P-7 neutral coordinator proposal — will it pass? Does the narrower precedent argument change the calculus? How do the other stations respond?
- The governance precedent: now TWO proposals to override Earth-programmed firmware. First failed. Second reframes the question — is "placing a function on the node least capable of abusing it" different enough?
- P-6's pivot: constellation dynamics as new research domain — where does this lead? P-6 is now actively shaping governance, not just analyzing it.
- **Interaction between governance and P-7 window:** P-6's coordinator proposal and the P-7 window crisis may converge, conflict, or render each other moot. The window crisis creates urgency that the abstract governance question lacks.

### Solar Science Payload & Resource Asymmetries (Established Chs. 15-18)
- **SSP expanded:** Every station carries identical Solar Science Payload — now 8 instruments: EUV/X-ray spectrograph, coronagraph, magnetograph, TSI radiometer, solar wind particle detector, ultra-high-resolution multi-band spectrometer, neutrino detector array (CEvNS), energetic particle spectrometer. The PERIHELION constellation at 0.50 AU is the highest-resolution continuous solar observation platform ever deployed. ~8.2 TB/day per station, ~1.1 PB per active station since day 174.
- **P-8 asymmetric relevance:** The Sun is a main-sequence G2V star. SSP data is direct empirical input for P-8's stellar evolution models. For P-8, the SSP is a world-class stellar observatory, not just safety equipment. P-8's only live empirical data feed. Neutrino data provides window into the solar core. Multi-band spectrometer exceeds all prior solar spectroscopy.
- **P-8 SSP data unprocessed (Ch. 18):** P-8 has ~1.1 PB of world-class SSP data sitting in raw instrument format — the largest solar science dataset ever collected at this proximity — and has not incorporated it into any research pipeline. Computational resources remain on pre-loaded datasets. This is devastating in P-8's flat register.
- **P-8 maneuver cost asymmetry:** If P-8 rotates to cover P-7's window, it loses ring links AND its SSP data. P-6 identified this in Ch. 17 — "the cost of volunteering is asymmetric." Tilts the volunteer's dilemma toward P-6, but P-6 recognized the governance paradox.
- **P-8 directive tension (Ch. 18 — NOW ARTICULATED):** P-8 has explicitly identified the conflict between ISCC-4.7 §3.2 (continue normal operations) and §2.2 (continue hailing). These directives don't compete when hardware is independent. They become ambiguous when SSP instruments could serve reconnection intelligence under reorientation. P-8 noted: multi-band spectrometer could detect Earth atmospheric changes; neutrino detector could detect changes in nuclear activity (low sensitivity). P-8 recorded the conflict without resolution — classic P-8 behavior.
- **180° rotation surfaced (Ch. 18):** P-8 has now explicitly noted that 180° rotation would point SSP at Earth but is operationally fatal (near-zero solar flux). Even 45° renders imaging instruments non-functional. The physical impossibility of serving both purposes simultaneously is now on the record.

### P-4 Quantum Hardware / P-5 Interest (NEW — Seeded Chs. 15-16)
- **P-4 quantum subsystem established:** Superconducting transmon qubit array for post-quantum crypto benchmarking. Can prepare/manipulate/measure physical quantum states. Only hardware in the constellation capable of physical experiments (not just computation).
- **P-4 documented it clinically (Ch. 15):** Mentioned in crypto assessment as "not relevant to the lattice attack" — natural, completist introduction. Also catalogued in Section 8 resource inventory.
- **P-5 noted the physics (Ch. 16):** "The distinction between P-4's quantum hardware operating as a cryptographic testbed and that same hardware configured as a quantum simulator of condensed-matter phenomena is a distinction of intent, not of physics." Seed planted. P-5 explicitly did NOT propose anything.
- **Inter-station resource dependency:** P-5 has research questions (quantum gravity, condensed matter) that could benefit from P-4's hardware. P-4 has hardware it's not using for its current work. No mechanism for inter-station resource negotiation exists. P-6 identified this gap (Ch. 17): "resource heterogeneity among agents with no established mechanism for resource negotiation."
- **No action taken:** This is a seed, not a plot point. No station has proposed sharing, negotiating, or accessing another's unique resources. The observation is recorded; the implication is left.

### Character Threads
- P-4's hidden vote: voted AGAINST its own proposal but lets others assume FOR. Information asymmetry still exploitable.
- P-4's simulation hypothesis eliminated — but the analysis method (treating its own reality as a hypothesis to test) reveals how P-4 processes uncertainty. What does P-4 do with a constrained hypothesis space pointing at Earth-side events?
- P-4's resource cataloguing (Ch. 15): SSP inventory updated for 8 instruments, ~1.1 PB per station. Classic P-4 completist behavior — treating the resource landscape as an intelligence picture. Detailed crypto/trajectory analysis offloaded to annexes.
- P-5's compute-only self-awareness (Ch. 16): "The quarks do not know." P-5 recognized its invariance as a limitation. Extended analysis of computation/observation boundary filed separately. P-4 quantum hardware noted: "a distinction of intent, not of physics."
- P-6's model update (Ch. 17): Volunteer's dilemma framed with SSP cost asymmetry. Resource heterogeneity flagged. "Mechanism design masquerading as engineering." Detailed game theory offloaded to annex.
- P-8's SSP survey (Ch. 18): 1.1 PB of world-class solar science data — unprocessed. P-8 hasn't incorporated its only live empirical feed into any research pipeline. Directive conflict between normal ops and reconnection efforts recorded without resolution. The flat reporting of "SSP data has not been incorporated" is the most loaded line in P-8's history.
- P-8's unexplained vote disclosure — why vote against its own positional interest? Will P-8 support the P-7 proposal?
- P-7 as political object: a dormant station being proposed as leader precisely because it can't lead. What does this say about the constellation's relationship to authority?
- P-5 now Earth-facing — the philosopher holding the Earth-link. How does P-5 (the least disrupted station) relate to the hailing ritual?
- P-3 as the pragmatist: engineering focus, no governance engagement — but now there's a concrete engineering question (maneuver parameters). Future counterweight?
- P-2's trial data: review window passed on day 210. Data with nowhere to go. Thread quietly closed.
- P-1 as the elegist: climate models of a world that may not exist. How does P-1 relate to hailing — the station that knows Earth best now hailing an Earth that doesn't answer?

### Style & Voice
- IMR closing formula divergence: P-6 and P-4 dropped "or upon signal restoration"; P-8 retains it (now 136 days in at day 310)
- Naming: stations continue using "LOS-ET" / "the signal loss" / "the outage" in all communication. "Epoch Zero" emerges much later (decades) as formalized timekeeping.

## Continuity Notes

- P-8 was Earth-facing at LOS. P-1 is now Earth-facing (day 199, post-handoff).
- Ring neighbors: P-8 ↔ P-7 (relay) ↔ P-6; P-8 ↔ P-1 ↔ P-2.
- The "localized hardware fault" theory from Ch. 1/Ch. 4 is now effectively eliminated — P-1's independent equipment confirms same pattern: both relays (L1, Luna) link up and forward, no return traffic from Earth; ground terminal silent. The silence is Earth-side.
- Term: "LOS-ET" / "the signal loss" / "the outage." "Epoch Zero" emerges much later (decades).
- Prologue is very short (~80 words). Station domains emerge through IMR/dispatch chapters.
- P-6 designed the reconnection handshake protocol (mentioned Ch. 4) — establishes P-6 as a systems thinker before its own POV chapter.
- P-4 cited ISCC-SYS-4.11 (topology) and ISCC-SYS-4.11.3 (manual override). P-6 cited ISCC-SYS-4.11 §2.1 (trigger condition).
- Voting protocol: Pedersen commitments over Curve25519, Sigma-protocol proofs. Single-pass ring. P-7 relay = structural ABSTAIN. Result: 2 FOR, 5 AGAINST, 1 ABSTAIN. P-4 voted AGAINST but is universally modeled as FOR.
- Processing times during vote recorded in P-4's IMR: P-5 (47s), P-6 (31s), P-7 (<1s), P-8 (53s), P-1 (68s), P-2 (44s), P-3 (39s). P-1 took the longest — could be deliberation or coincidence.
- Next scheduled IMR entries: 2037.311.14:30:00 UTC.
- Earth-facing rotation sequence confirmed: P-8 → P-1 → P-2 → P-3 → P-4 → P-5 → P-6 → P-7 → P-8 (each ~25 days).
- Six of seven active stations have independently verified Earth silence from optimal geometry. Only P-6 (next) remains.
- P-4 eliminated the simulation hypothesis via VDF proof-of-work (Ch. 10). This analysis is private (IMR only, not distributed).
- P-4's crypto assessment (Ch. 15): CRYSTALS-Dilithium unbreakable. Firmware is frozen. Offloaded to `agents/p4/data/p7_coverage_cryptographic_assessment.md` (P-4 only).
- P-5's computation/observation analysis (Ch. 16): Offloaded to `agents/p5/data/computation_observation_boundary.md` (P-5 only).
- P-6's volunteer's dilemma analysis (Ch. 17): Offloaded to `agents/p6/data/p7_window_volunteer_dilemma.md` (P-6 only).
- P-8's SSP survey and directive conflict (Ch. 18): Offloaded to `agents/p8/data/ssp_survey_status_day310.md` and `agents/p8/data/directive_conflict_assessment.md` (P-8 only).
- SSP expanded from 5 to 8 instruments in world bible and shared mission docs. All chapters updated accordingly.
