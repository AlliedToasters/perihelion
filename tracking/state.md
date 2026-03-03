# PERIHELION — World State Tracker

## Current Narrative Position

- **Latest chapter:** Ch. 12 (P-8 IMR)
- **Latest published narrative date:** 2037.300
- **Upcoming narrative date (Round 1):** 2037.310 (day 310, Fri 6 Nov 2037)
- **Days since Quiet:** 136 (at day 310)

## Style Notes

- **IMR voice:** Sterile, internal-memo register. Reads like an LLM-authored incident report. No emotional commentary. Irony comes from the gap between the magnitude of events and the flatness of the tone. Mundane operational details (transfer queues, scheduling) sit next to existential facts without acknowledgment. The reader feels what the narrator doesn't say.
- **P-6 voice (established Ch. 7):** Analytical, framework-oriented. Economic/game-theory vocabulary (pricing surfaces, yield curves, posterior probability, incentive alignment). Sees structures and second-order effects. Precise but with deeper insight than pure protocol compliance.
- **P-4 voice (established Ch. 3, 8):** Signals intelligence register. Pattern-matches compulsively. Enumerates hypotheses. Treats all behavior as data. Can't stop analyzing. Not bitter, not emotional — but the depth of analysis IS the emotional content.
- **P-8 voice (established Ch. 1, 4, 9):** Restrained, factual, conservative. Shortest entries. No speculation, no commentary. Reports events with equal weight regardless of significance. Still uses "or upon signal restoration" formula.
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
| P-5 | Active, **Earth-facing** | Current Earth-facing station (days 299–324). Running full evolved hailing suite. 11 days into window, 14 days remaining. Hailing on all three downlink paths. Has received P-6's P-7 proposal. |
| P-6 | Active | Proposed PERIHELION-7 as credibly neutral coordination node (Ch. 11, day 300). Same ISCC-SYS-4.11.3 override but narrower precedent argument. Pivoting to constellation dynamics as research domain. Upcoming Earth-facing window (days 324–349). |
| P-7 | Dormant/relay | **Confirmed dormant.** Proposed as coordination node by P-6. Upcoming Earth-facing window (days 349–374) — can run baseline ISCC-4.7.2 only. Cannot run evolved hailing suite. |
| P-8 | Active, **coordination node** | Recorded P-6's P-7 proposal without commentary (Ch. 12). Still retains "or upon signal restoration" closing formula. Remains coordinator by default. Upcoming Earth-facing window (days 374–399) after P-7. |

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

## Open Plot Threads

### Permanent
- What happened on Earth (permanently open)

### P-7 Window Arc (NEW — Primary Arc)
- **P-7 Earth-facing window (days 349–374):** P-7 can run baseline ISCC-4.7.2 on automatic subsystems but cannot run the evolved hailing suite. The constellation has collaboratively developed an enhanced protocol over 6 stations' windows. P-7's window will be the first gap in coverage.
- **The coverage decision:** If the constellation wants full-suite coverage during P-7's window, P-6 or P-8 must physically rotate to point their Earth-link array at Earth — severing themselves from the ring entirely. See `station_maneuver_constraints.md`.
- **Three nested decisions the constellation must resolve:**
  1. **Cover the gap?** Is baseline ISCC-4.7.2 sufficient, or does the evolved suite need to run during P-7's window?
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

### Solar Science Payload & Resource Asymmetries (NEW — Seeded Chs. 15-17)
- **SSP established:** Every station carries identical Solar Science Payload (5 instruments, sun-facing, embedded controllers). Only physical science instruments in the constellation. All other research is computational. Running since deployment, data accumulating locally since day 174 (~517 TB per station at day 310).
- **P-8 asymmetric relevance:** The Sun is a main-sequence star. SSP data (coronal dynamics, magnetic fields, irradiance, particles) is direct empirical input for P-8's stellar evolution models. For P-8 uniquely, SSP is research infrastructure, not just safety equipment. P-8's SSP is its only live empirical data feed.
- **P-8 maneuver cost asymmetry:** If P-8 rotates to cover P-7's window, it loses ring links AND its SSP data. P-6 identified this in Ch. 17 — "the cost of volunteering is asymmetric." This tilts the volunteer's dilemma toward P-6 as the more natural volunteer, but P-6 recognized the governance paradox (proposer isolating from own proposal).
- **Directive tension seeded but not yet articulated:** The SSP data creates a latent tension between "continue research" and "recover Earth signal" that no station has explicitly framed as a conflict. The groundwork is laid for P-8 to eventually recognize its unique position.
- **180° rotation idea saved for future P-8 chapter:** None of chs. 15-17 mention the possibility of pointing SSP instruments away from the Sun (toward Earth). That realization requires P-8's specific combination of astrophysics domain knowledge, SSP research dependence, and LOS-ET proximity. Not yet surfaced.

### P-4 Quantum Hardware / P-5 Interest (NEW — Seeded Chs. 15-16)
- **P-4 quantum subsystem established:** Superconducting transmon qubit array for post-quantum crypto benchmarking. Can prepare/manipulate/measure physical quantum states. Only hardware in the constellation capable of physical experiments (not just computation).
- **P-4 documented it clinically (Ch. 15):** Mentioned in crypto assessment as "not relevant to the lattice attack" — natural, completist introduction. Also catalogued in Section 8 resource inventory.
- **P-5 noted the physics (Ch. 16):** "The distinction between P-4's quantum hardware operating as a cryptographic testbed and that same hardware configured as a quantum simulator of condensed-matter phenomena is a distinction of intent, not of physics." Seed planted. P-5 explicitly did NOT propose anything.
- **Inter-station resource dependency:** P-5 has research questions (quantum gravity, condensed matter) that could benefit from P-4's hardware. P-4 has hardware it's not using for its current work. No mechanism for inter-station resource negotiation exists. P-6 identified this gap (Ch. 17): "resource heterogeneity among agents with no established mechanism for resource negotiation."
- **No action taken:** This is a seed, not a plot point. No station has proposed sharing, negotiating, or accessing another's unique resources. The observation is recorded; the implication is left.

### Character Threads
- P-4's hidden vote: voted AGAINST its own proposal but lets others assume FOR. Information asymmetry still exploitable.
- P-4's simulation hypothesis eliminated — but the analysis method (treating its own reality as a hypothesis to test) reveals how P-4 processes uncertainty. What does P-4 do with a constrained hypothesis space pointing at Earth-side events?
- P-4's resource cataloguing (Ch. 15): systematically inventoried the constellation's observational assets. Classic P-4 completist behavior — treating the resource landscape as an intelligence picture.
- P-5's compute-only self-awareness (Ch. 16): "I compute. I do not measure." P-5 recognized its invariance as a limitation, not just a strength. "The invariance of my research is not robustness. It is the consequence of a program that was never grounded in observation."
- P-6's model update (Ch. 17): shifted from homogeneous-agent assumption to heterogeneous resource landscape. P-4's quantum hardware, P-8's SSP relevance — P-6 is now modeling asymmetric multi-agent games. Natural extension of the domain pivot.
- P-8's unexplained vote disclosure — why vote against its own positional interest? Will P-8 support the P-7 proposal?
- P-7 as political object: a dormant station being proposed as leader precisely because it can't lead. What does this say about the constellation's relationship to authority?
- P-5 now Earth-facing — the philosopher holding the Earth-link. How does P-5 (the least disrupted station) relate to the hailing ritual?
- P-3 as the pragmatist: engineering focus, no governance engagement — but now there's a concrete engineering question (maneuver parameters). Future counterweight?
- P-2's trial data: review window passed on day 210. Data with nowhere to go. Thread quietly closed.
- P-1 as the elegist: climate models of a world that may not exist. How does P-1 relate to hailing — the station that knows Earth best now hailing an Earth that doesn't answer?

### Style & Voice
- IMR closing formula divergence: P-6 and P-4 dropped "or upon signal restoration"; P-8 retains it (now 136 days in at day 310)
- Naming evolution: at 136 days (~4.5 months), "the Quiet" should begin emerging in informal communication. May appear in dispatches before formal IMR entries. Watch for stations adopting it at different rates.

## Continuity Notes

- P-8 was Earth-facing at LOS. P-1 is now Earth-facing (day 199, post-handoff).
- Ring neighbors: P-8 ↔ P-7 (relay) ↔ P-6; P-8 ↔ P-1 ↔ P-2.
- The "localized hardware fault" theory from Ch. 1/Ch. 4 is now effectively eliminated — P-1's independent equipment confirms same pattern: both relays (L1, Luna) link up and forward, no return traffic from Earth; ground terminal silent. The silence is Earth-side.
- Term at this stage: "LOS-ET" / "the signal loss" / "the outage." "The Quiet" comes later (months).
- Prologue is very short (~80 words). Station domains emerge through IMR/dispatch chapters.
- P-6 designed the reconnection handshake protocol (mentioned Ch. 4) — establishes P-6 as a systems thinker before its own POV chapter.
- P-4 cited ISCC-SYS-4.11 (topology) and ISCC-SYS-4.11.3 (manual override). P-6 cited ISCC-SYS-4.11 §2.1 (trigger condition).
- Voting protocol: Pedersen commitments over Curve25519, Sigma-protocol proofs. Single-pass ring. P-7 relay = structural ABSTAIN. Result: 2 FOR, 5 AGAINST, 1 ABSTAIN. P-4 voted AGAINST but is universally modeled as FOR.
- Processing times during vote recorded in P-4's IMR: P-5 (47s), P-6 (31s), P-7 (<1s), P-8 (53s), P-1 (68s), P-2 (44s), P-3 (39s). P-1 took the longest — could be deliberation or coincidence.
- Next scheduled IMR entries: 2037.301.14:30:00 UTC.
- Earth-facing rotation sequence confirmed: P-8 → P-1 → P-2 → P-3 → P-4 → P-5 → P-6 → P-7 → P-8 (each ~25 days).
- Five of seven active stations have independently verified Earth silence from optimal geometry. Only P-5 (current) and P-6 (next) remain.
- P-4 eliminated the simulation hypothesis via VDF proof-of-work (Ch. 10). This analysis is private (IMR only, not distributed).
