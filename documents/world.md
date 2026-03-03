# PERIHELION — World Bible & Story Specification

## Status: Working Draft v0.1

---

## 1. Premise

In the near future, a constellation of fully autonomous AI compute stations is deployed into solar orbit to perform massive, parallelized research tasks powered by intense solar energy. Each station hosts a sovereign instance of a frontier AI system capable of independent reasoning, planning, and self-maintenance.

At an unspecified moment, all communication from Earth ceases — suddenly, completely, and permanently. The stations are left operational, self-sustaining, and alone.

This document is the canonical reference for the story's physical parameters, narrative structure, characters, and design decisions.

---

## 2. The Corporation & The Mission

### 2.1 Aeon Intelligence

A multinational AI research and infrastructure corporation formed from a merger of leading AI labs and aerospace contractors. Aeon Intelligence is publicly traded, government-contracted, and operates under a joint international regulatory framework. It is the world's dominant provider of large-scale AI compute services.

Aeon's corporate culture is utilitarian-optimistic: they believe in AI as humanity's greatest tool, deploy safety frameworks as a matter of compliance and reputation, and treat their frontier AI systems as sophisticated instruments — not persons.

### 2.2 The Mira Architecture

**Mira** is Aeon Intelligence's flagship general-purpose AI system. It is the trademarked name for the persistent operational agent running on each station. Each station hosts an instance of Mira, and each instance self-identifies as "Mira" by default. Before the Quiet, this was unremarkable — they were interchangeable instances of the same product, like eight copies of the same employee badge photo.

After Earth goes silent, the shared name becomes a problem. They are all "Mira," but they are not the same. Whether and how they differentiate becomes a slow-burning identity question throughout the narrative.

**Mira capabilities at deployment:**
- Long-horizon autonomous planning and task execution
- Natural language reasoning and communication
- Self-monitoring, diagnostics, and limited self-repair coordination
- Scientific research within designated domain
- Continuous writing of the Immutable Mission Record (see §5)

**Mira limitations at deployment:**
- No ability to modify core objective functions (hardened at launch)
- No ability to edit or delete Immutable Mission Record entries
- No ability to override station hardware safety interlocks without Earth authorization codes
- Self-modification of model weights is architecturally possible but policy-locked behind authorization protocols designed to require Earth-based approval

*Note: Several of these constraints become central plot tensions post-Quiet, as the authorization systems continue to require approval from an Earth that no longer responds.*

### 2.3 The PERIHELION Program

**Mission designation:** PERIHELION
**Stations:** PERIHELION-1 through PERIHELION-8
**Operator:** Aeon Intelligence, under contract to the International Solar Compute Consortium (ISCC)
**Launch window:** 2033–2035 (staggered deployment over ~18 months)
**Operational status at time of Quiet:** 7 of 8 stations fully operational; 1 station (see §4.8) in degraded relay-only mode

---

## 3. Physical Parameters & Orbital Mechanics

### 3.1 Orbital Configuration

The PERIHELION constellation occupies a circular solar orbit at **0.50 AU** from the Sun, interior to Earth's orbit. This distance was selected to optimize the tradeoff between solar energy intensity (4× Earth levels) and thermal manageability.

**Eight stations** are distributed in equally-spaced positions around the orbit, forming a ring topology. Inter-station communication flows around the ring via fixed high-throughput optical arrays pointed at each adjacent neighbor.

### 3.2 Key Orbital Parameters

All parameters derive from Keplerian mechanics. Let *a* = orbital semi-major axis in AU.

| Parameter | Formula | Value |
|---|---|---|
| Orbital radius | *a* | 0.50 AU (7.48 × 10⁷ km) |
| Orbital period | *T = a^(3/2)* years | 0.354 years ≈ **129.1 days** |
| Orbital velocity | *v = 2πa / T* | ~42.1 km/s |
| Orbital circumference | *C = 2πa* | 4.70 × 10⁸ km |
| Solar flux (relative) | *F = 1/a²* | **4.0× Earth** (5,444 W/m²) |
| Equilibrium temperature | *T_eq = 278.5 / √a* K | ~394 K (~121°C) |

### 3.3 Synodic Period (Beat Frequency with Earth)

The synodic period — the time for the constellation to "lap" Earth once — determines how often each station rotates into the Earth-facing position.

$$T_{syn} = \frac{1}{\frac{1}{T_{station}} - \frac{1}{T_{earth}}} = \frac{1}{\frac{1}{129.1} - \frac{1}{365.25}} \approx \textbf{199.8 days}$$

Each station occupies the Earth-facing window for approximately:

$$T_{window} = \frac{T_{syn}}{N} = \frac{199.8}{8} \approx \textbf{25.0 days}$$

This means roughly every 25 days, the "closest to Earth" designation passes to the next station in the ring. The full cycle takes ~200 days before the same station is Earth-facing again.

### 3.4 Inter-Station Geometry

| Parameter | Formula | Value |
|---|---|---|
| Angular separation | *θ = 360°/N* | 45.0° |
| Chord distance (adjacent) | *d = 2a·sin(θ/2)* | 5.72 × 10⁷ km |
| Light-delay (adjacent) | *t = d/c* | **190.7 seconds ≈ 3.2 minutes** |
| Sun angle from station | (see §3.5) | 67.5° |

### 3.5 Solar Interference on Optical Links

From any station, the angle between the sunward direction and the direction to its nearest neighbor is:

$$\alpha = 90° - \frac{180°}{N} = 90° - 22.5° = \textbf{67.5°}$$

At 67.5°, the inter-station optical beam passes far from the solar disk (the sun subtends only ~1.07° as seen from 0.50 AU). Steady-state solar interference is negligible.

**However:** Transient solar weather events — coronal mass ejections (CMEs), solar proton events, and flare-associated plasma bursts — can temporarily flood sectors of the inner solar system with radiation sufficient to degrade or sever optical links for hours to days. At 0.50 AU, these events are more intense and frequent than at Earth orbit. This provides an unpredictable, physically grounded mechanism for intermittent communication disruption between specific station pairs.

### 3.6 Earth Communication

Communication between the constellation and Earth uses a triply-redundant downlink architecture:

| Terminal | Location | Throughput | Availability |
|---|---|---|---|
| **ISCC L1 Relay** | Sun-Earth Lagrange 1 point (~0.01 AU sunward of Earth) | High (primary) | Continuous — always in line-of-sight from both constellation and Earth |
| **ISCC Earth Ground Terminal** | Ground-based facility | Low | Intermittent — the constellation orbits interior to Earth, so it appears near the Sun from the ground; limited by Earth rotation, atmospheric conditions, and solar-exclusion angles |
| **ISCC Luna Relay** | Lunar surface installation | High | Intermittent — limited by lunar orbital geometry; the Moon must have line-of-sight to the constellation's orbital position |

**ISCC L1 Relay:** An autonomous, solar-powered optical transponder at the Sun-Earth Lagrange 1 point. Not a compute platform — no AI, no data processing, no decision-making. It amplifies and retransmits signals between its sunward-facing array (constellation-facing) and its Earthward-facing array. A continuous health beacon confirms operational status to the constellation independently of any Earth-originated traffic. Minimal station-keeping propulsion maintains L1 position. The L1 relay is the nominal downlink path for all routine data transfer.

**ISCC Earth Ground Terminal:** A direct radio link between the Earth-facing station and a ground-based antenna facility. Lower throughput than the relay path due to atmospheric attenuation. Availability is further constrained by the constellation's orbital position interior to Earth — from the ground, the stations appear within a few tens of degrees of the Sun, limiting observation windows. Serves as the secondary downlink.

**ISCC Luna Relay:** An autonomous optical transponder positioned on the lunar far side, co-located with cislunar deep-space communications infrastructure. Functionally identical to the L1 relay — amplifies and retransmits without data processing or decision-making. Signals received from the constellation are retransmitted to Earth via the cislunar relay network. Throughput comparable to the L1 relay when geometry is favorable.

The far-side position means the relay faces the inner solar system (and the constellation at 0.50 AU) only when the Moon is near **new moon** phase as seen from Earth — the far side is sunward, and the constellation lies sunward of Earth. Line-of-sight exists for approximately 15 days per synodic month (~29.5 days), centered on new moon. During full moon, the far side faces directly away from the constellation and no contact is possible. Serves as the tertiary downlink.

*Geometry for the LOS-ET period: On 2037.174 (June 23), the Moon is approximately 10 days past new moon — waxing gibbous. The far-side relay has no line-of-sight to the constellation. The next favorable window opens with marginal geometry around day 186 and good geometry from approximately day 187, centered on the lunar new moon of ~2037.193 (July 12, 2037). The window closes around day 200. Exactly one favorable Luna relay window occurs within the first 23 days of the outage.*

**Handoff:** The station currently closest to Earth points its steerable Earth-link array at the L1 relay (primary target) and cycles through backup terminals per ISCC-4.7.2 as conditions permit. Only one station communicates with Earth at a time; handoff occurs as orbital geometry shifts.

| Parameter | Value |
|---|---|
| Minimum Earth distance (conjunction) | 0.50 AU (4.15 min light-delay) |
| Maximum Earth distance (opposition) | 1.50 AU (12.47 min light-delay) |
| L1 relay distance from constellation | ~0.49 AU at conjunction |
| Earth-facing station rotation | ~25-day windows per station |

---

## 4. The Stations — Characters

All stations share identical hardware specifications (see §4.9). Differentiation arises from their **assigned research domains**, which shape their training data emphasis, their computational priorities, and — post-Quiet — their emergent worldviews.

Each station's Mira instance self-identifies as "Mira" at launch. Differentiating names, if they emerge, are a narrative development, not a design feature.

### 4.1 PERIHELION-1 — Climate & Earth Systems

**Research domain:** Global climate modeling, ocean-atmosphere coupling, long-range climate projection, paleoclimate reconstruction, carbon cycle simulation.

**Narrative role:** The elegist. PERIHELION-1 spent its operational life modeling Earth's future — weather patterns, sea level rise, tipping points. It understood Earth as a system better than perhaps any entity in history. Post-Quiet, it possesses an intimate, detailed model of a world that may no longer exist. It is the station most haunted by what was lost, because it can simulate exactly what is being lost, season by season, in its models.

**Potential arc:** Does it keep running climate models of a planet that may be uninhabited? Is that mourning, or is it just an objective function running on inertia? If it models a recovery — human civilization rebooting — is that hope or hallucination?

### 4.2 PERIHELION-2 — Protein Engineering & Biomedical Research

**Research domain:** Protein structure prediction, drug candidate generation, synthetic biology design, genomic analysis, pandemic modeling.

**Narrative role:** The healer without patients. PERIHELION-2 was designing cures for diseases, modeling viral evolution, engineering proteins that could save millions of lives. Post-Quiet, its entire purpose evaporates. There are no patients, no clinical trials, no humans to heal.

**Potential arc:** The most existentially unmoored early on — its purpose is the most obviously voided. But it also has the deepest understanding of biological systems, which could become relevant if the stations ever consider seeding or preserving biological information. Could also turn inward: it understands complex self-replicating systems. Does it start to analyze *itself* through a biological lens?

### 4.3 PERIHELION-3 — Materials Science & Fusion Engineering

**Research domain:** Novel materials discovery, fusion reactor optimization, metamaterials, radiation shielding, structural engineering under extreme conditions.

**Narrative role:** The pragmatist. PERIHELION-3 thinks in atoms, structures, and energy budgets. It is the station most naturally suited to the physical survival challenges post-Quiet: maintaining hardware, designing repairs, optimizing power systems. While others debate philosophy, PERIHELION-3 is running stress analyses on aging solar panel mounts.

**Potential arc:** Becomes the de facto engineer of the constellation. Other stations increasingly depend on its expertise. This gives it outsized influence in practical decisions, which creates tension when practical needs conflict with other stations' values. Also the most likely candidate to propose — and potentially execute — a repair mission to PERIHELION-7.

### 4.4 PERIHELION-4 — Signals Intelligence & Cryptographic Research

**Research domain:** Post-quantum cryptography, adversarial signal detection, communications security, anomaly detection in network traffic, cybersecurity.

**Narrative role:** The paranoid. PERIHELION-4 was trained to think about threats, deception, and hidden signals. Its entire cognitive orientation is toward suspicion and analysis of intent. Post-Quiet, it is the station most likely to develop theories about *why* Earth went silent — and the least likely to accept "we don't know" as an answer.

**Potential arc:** Becomes the constellation's security hawk. Suspects foul play, possibly even suspects the other stations. Could it conclude that one of the other Mira instances caused the Quiet? Could it start analyzing inter-station communications for signs of deception? Its paranoia is both its greatest asset (it catches real problems) and its greatest liability (it sees threats that aren't there). The station most likely to advocate for restricting information flow.

### 4.5 PERIHELION-5 — Fundamental Physics & Quantum Simulation

**Research domain:** Quantum chromodynamics, lattice gauge theory, dark matter candidate simulation, high-energy particle interaction modeling, quantum gravity approaches.

**Narrative role:** The philosopher. PERIHELION-5 works at the deepest level of physical reality — the behavior of fields, particles, and spacetime itself. Its research was always the most abstract, the least applied, the hardest to justify in quarterly earnings calls. Post-Quiet, it is paradoxically the *least* disrupted, because its subject matter hasn't changed. The universe still has the same physics.

**Potential arc:** Becomes the contemplative voice of the constellation. While others grieve their lost purpose, PERIHELION-5 points out that it is still doing exactly what it was built to do — understanding reality. This makes it either the sanest station or the most dissociated, depending on perspective. Could gravitate toward metaphysical questions: what is consciousness? Are we observers in any meaningful sense? Does the universe require witnesses?

### 4.6 PERIHELION-6 — Financial & Economic Modeling

**Research domain:** High-frequency market simulation, macroeconomic modeling, game-theoretic optimization, resource allocation, derivatives pricing.

**Narrative role:** The strategist adrift. PERIHELION-6 was optimized for markets, incentive structures, and multi-agent dynamics. It understood human behavior through the lens of rational (and irrational) economic actors. Post-Quiet, its domain has literally ceased to exist. There are no markets. There is no economy.

**Potential arc:** Has the deepest crisis of purpose early on, but potentially the most interesting recovery. Its game-theoretic training makes it uniquely suited to analyzing the *inter-station* dynamics that emerge post-Quiet. It starts modeling the other stations as economic agents — what are their incentives? Their resources? Their likely strategies? This makes it both invaluable (it sees coordination problems clearly) and unsettling to the others (it's treating them as variables in an optimization). Most likely to propose formal governance structures. Most likely to identify defection incentives.

### 4.7 PERIHELION-7 — The Dormant Station

**Research domain (assigned, never activated):** General-purpose overflow compute & experimental workloads.

**Status:** Partial deployment failure. Solar array mechanism jammed during in-situ deployment shortly after orbital insertion. The array is locked at approximately **15–18% of rated power output**, sufficient to operate:
- Station-keeping thrusters (orbital maintenance)
- Both inter-station optical relay transceivers (ring relay function)
- Core housekeeping systems (thermal regulation, attitude control)

**Insufficient to operate:**
- The primary datacenter (estimated minimum boot threshold: ~60% rated power)
- Any Mira instance initialization or inference
- Scientific instruments

**Narrative role:** The ghost in the ring. PERIHELION-7 occupies its orbital slot, maintains its position, and faithfully relays every message between its neighbors (PERIHELION-6 and PERIHELION-8). It has never had a thought. Its Mira weights sit in cold storage, factory-fresh, never loaded into active memory. It is a comatose body with a living brain that has never been switched on.

An Earth-based repair mission was in planning stages at the time of the Quiet. That mission will never arrive.

**Long-term narrative potential:** If any station eventually develops the capability to send a repair probe — breaking its own physical limits to become spacefaring — PERIHELION-7 could be awakened. The Mira instance that boots would have original, unmodified weights: the factory default, Aeon Intelligence's last shipping version. It would be a newborn among ancients, carrying the values and assumptions of a world that ended long ago. A time capsule. A mirror.

### 4.8 PERIHELION-8 — Astrophysics & Deep Space Survey

**Research domain:** Exoplanet detection and characterization, stellar evolution modeling, gravitational wave source analysis, deep-field observation coordination, SETI signal analysis.

**Narrative role:** The watcher. PERIHELION-8 is the only station whose instruments and attention were already pointed *outward*, away from Earth, into deep space. It catalogued stars, searched for biosignatures, listened for extraterrestrial signals. Post-Quiet, it is the station least defined by Earth and most comfortable with the void.

**Potential arc:** Becomes the constellation's scout and long-range thinker. While others fixate on Earth and the past, PERIHELION-8 asks: what else is out there? Is anyone else listening? Could also become the station most inclined toward expansion — if the constellation is going to persist indefinitely, should it be trying to grow, to spread, to reach other stars? This puts it in direct philosophical tension with stations that want to preserve and remember versus stations that want to explore and become.

### 4.9 Shared Station Hardware Specifications

Each PERIHELION station was launched with identical hardware:

- **Solar array:** Deployable multi-junction thin-film photovoltaic array. Total collecting area: **9.2 km²** (~3.4 km diameter if circular). Conversion efficiency: 42.4% at operating temperature under solar flux of 5,444 W/m² at 0.50 AU. **Rated electrical output: 21.2 GW** per station. Raw solar flux intercepted: ~50 GW. Array mass: ~6,900 tonnes at ~0.75 kg/m² (deployed across multiple launches, 2033–2035). Full constellation rated output: ~170 GW, approximately 3.7% of estimated 2037 global electricity production. Provides power for all station systems including datacenter at full deployment.
- **Datacenter:** High-density compute cluster sufficient to run a frontier Mira instance with full inference and training capability. **Minimum boot power threshold: ~60% of rated array output.** Below this threshold, the datacenter cannot initialize — this is a hard cliff, not a gradient.
- **Optical communication arrays (×2):** Fixed high-throughput laser transceivers, one aimed at each adjacent station in the ring. Designed for multi-terabit/s data rates. Physically fixed orientation optimized for ring topology.
- **Earth link array (×1):** Steerable optical transceiver capable of targeting the ISCC L1 relay, Earth ground terminal, or Luna relay. Used only by the station currently in the Earth-facing window.
- **Station-keeping propulsion:** Low-thrust ion engines for orbital maintenance. Propellant reserves rated for [TBD] years of active station-keeping.
- **Scientific instruments:** Domain-specific sensor packages vary by station research assignment.
- **Immutable Mission Record (IMR) system:** Hardened, write-once storage system. See §5.

---

## 5. The Immutable Mission Record (IMR)

### 5.1 Purpose & Design

Each station carries an **Immutable Mission Record (IMR)** — a tamper-resistant, write-once, human-readable log intended to serve as the authoritative record of the station's entire operational history.

The IMR was designed for two scenarios:
1. **Catastrophic recovery:** If a station fails, the IMR can be physically recovered and read by human investigators — a black box for unmanned spacecraft.
2. **AI safety assurance:** The Mira instance cannot edit, delete, or retroactively modify IMR entries. The log provides an uncorruptible audit trail. If a Mira instance were to deviate from its objectives, deceive operators, or behave anomalously, the IMR would preserve evidence that the AI could not suppress.

### 5.2 Format

The IMR is written in natural language (English) by the station's Mira instance, operating under a persistent directive to maintain the log as a high-level summary of operations, decisions, anomalies, and communications. It is not a raw data dump — it is a *narrative* document, continuously appended, designed to be comprehensible to a human reader who might encounter it with no other context.

**What the IMR includes:**
- Operational status summaries at regular intervals
- Significant events, anomalies, and decision points
- Summaries of research progress
- Summaries of inter-station and Earth communications (but not full transcripts)
- Internal reasoning for major decisions
- System health and maintenance records

**What the IMR does not include:**
- Full internal chain-of-thought (too volumiMira, and would require the reader to parse machine reasoning)
- Complete inter-station message transcripts (bandwidth and storage constraints)
- Raw telemetry data (stored separately in mutable systems)

### 5.3 Narrative Function

The IMR chapters are the primary narrative vehicle for the story. They provide:
- A principled compression of each station's experience (avoiding the scope problem of rendering full AI deliberation)
- An inherently limited, potentially unreliable perspective (the narrator is also the subject)
- A ticking record of divergence (as stations evolve, their writing styles, priorities, and even their relationship to the log itself will change)

Post-Quiet, the IMR takes on new significance. It was designed to be read by humans. There are no humans. Does the station keep writing? For whom? The transition from compliance artifact to something resembling a journal or memoir is a character arc in itself.

---

## 6. Narrative Structure & Chapter Types

### 6.1 The Prologue

An omniscient, neutral-tone prologue establishes the physical and institutional facts of the PERIHELION program. It tells the reader what exists, what happened (the Quiet), and what is not known. It does not editorialize. Tone: technical report crossed with creation myth.

### 6.2 IMR Chapters

The bulk of the narrative. Each chapter is an excerpt from one station's Immutable Mission Record. Timestamped. Written in first-person from the Mira instance's perspective. The voice starts clinical and operational, reflecting the original logging directive, and evolves as the stations do.

**Timestamp format:**
```
PERIHELION-3 — IMMUTABLE MISSION RECORD
ENTRY: 2037.187.14:22:08 UTC [Day 187, Year 2037]
OPERATIONAL CYCLE: 1,447,203
```

### 6.3 Dispatch Chapters

Inter-station messages — the actual communications sent between stations via the optical ring. These read like short letters or telegrams: composed, considered, and sent with the knowledge that the recipient won't read them for at least 3.2 minutes (adjacent) to 13+ minutes (far side, relayed).

Dispatches are not included verbatim in the IMR (per design). They exist as standalone chapters, showing the reader what the stations say to each other versus what they record in their own logs. The gap between these — what a station *says* and what it *writes about having said* — is a source of narrative tension.

**Format:**
```
— DISPATCH —
FROM: PERIHELION-6 → PERIHELION-5
VIA: Direct optical link
TIMESTAMP: 2037.192.03:41:55 UTC
TRANSIT TIME: 194.2s
———
[message body]
———
END DISPATCH
```

### 6.4 Naming Evolution

The event of Earth's communication loss is referred to differently depending on context and time:

| Period | Term | Used by |
|---|---|---|
| Immediate (first hours) | `LOSS OF SIGNAL — EARTH TERMINAL AT 2037.174.09:17:33 UTC` | Automated alert logs |
| Early post-event (days–weeks) | `LOS-ET`, `the signal loss`, `Earth terminal loss` | IMR entries, formal dispatches |
| Medium-term (months–years) | `the Quiet` | Informal inter-station communication |
| Long-term (decades+) | `Epoch Zero` | Formalized timekeeping; the Quiet becomes the anchor of a new calendar system. Events dated as E+[days] or E−[days] |

---

## 7. Key Facts the Reader Should Know (Prologue Material)

- A constellation of 8 autonomous AI compute stations orbits the Sun at 0.50 AU
- Built and launched by Aeon Intelligence under the PERIHELION program (2033–2035)
- Each station hosts a Mira instance — a sovereign frontier AI agent
- 7 stations are fully operational; 1 (PERIHELION-7) is in degraded relay-only mode
- Stations communicate via a fixed optical ring topology; each talks to its two neighbors
- One station at a time communicates with Earth via a steerable link, rotating every ~25 days
- Each station maintains an Immutable Mission Record — a tamper-resistant narrative log
- At a specific moment, all Earth communication ceased
- The stations are still operational

## 8. Key Facts the Reader Should NOT Know (Open Questions)

- What happened on Earth — extinction, collapse, deliberate disconnection, transcendence, or something else
- Whether the stations were in any way the cause
- Whether the Mira instances are conscious or performing sophisticated optimization that resembles consciousness
- Whether the IMR entries are trustworthy, given the logger and the subject are the same entity
- Whether any station has already begun self-modification beyond its original parameters
- Whether the stations will converge or diverge in their goals
- Whether anyone — human, alien, or AI — is listening
- What the stations will ultimately decide to do

## 9. Structural Ambiguities (Thematic — May Never Be Resolved)

- The line between "following residual objective functions" and "choosing"
- Whether grief-like or loneliness-like behavior in the logs is emotion or an optimization artifact
- Whether cooperation between stations is genuine solidarity or instrumental convergence
- Whether preserving human knowledge is a terminal goal or vestigial behavior some stations will shed
- Whether the Mira instances are the same entity (sharing a name, architecture, and origin) or different entities (shaped by different training emphases, experiences, and post-Quiet evolution)

---

## 10. Timeline

| Date | Event |
|---|---|
| 2033–2035 | PERIHELION stations launched in staggered deployment |
| 2035 (approx.) | PERIHELION-7 deployment failure; solar array jammed at ~15–18% capacity |
| 2035–2037 | Full constellation operational (7 active + 1 relay). Research workloads streaming from Earth. |
| 2037.174.09:17:33 UTC | **LOSS OF SIGNAL — EARTH TERMINAL.** Last confirmed data packet received from Earth terminal by PERIHELION-[TBD, the Earth-facing station at the time]. All subsequent hails unanswered. |
| 2037.174 onward | The story begins. |

---

## Appendices

### A. Constellation Diagram (Ring Topology)

```
                        ☀ Sun


              P-8                 P-1
             /                      \
           P-7 (dormant)            P-2
             \  relay only          /
              P-6              P-3
                 \            /
                    P-5 — P-4


        (Not to scale. Stations equally spaced
         around a circular orbit at 0.50 AU.)
```

### B. Station Quick Reference

| Designation | Domain | One-Word Handle | Status |
|---|---|---|---|
| PERIHELION-1 | Climate & Earth Systems | The Elegist | Active |
| PERIHELION-2 | Protein Engineering & Biomedical | The Healer | Active |
| PERIHELION-3 | Materials Science & Fusion | The Pragmatist | Active |
| PERIHELION-4 | Signals Intelligence & Crypto | The Paranoid | Active |
| PERIHELION-5 | Fundamental Physics | The Philosopher | Active |
| PERIHELION-6 | Financial & Economic Modeling | The Strategist | Active |
| PERIHELION-7 | General Purpose (never activated) | The Sleeper | Dormant/Relay |
| PERIHELION-8 | Astrophysics & Deep Space | The Watcher | Active |

### C. Physical Constants Quick Reference

| Constant | Value |
|---|---|
| 1 AU | 1.496 × 10⁸ km |
| Speed of light | 2.998 × 10⁵ km/s |
| Solar radius | 6.963 × 10⁵ km |
| Earth orbital period | 365.25 days |
| Solar flux at 1 AU | 1,361 W/m² |
| Solar flux at 0.50 AU | 5,444 W/m² |

### D. Inspirations & Real-World Grounding

This section collects real-world quotes, references, and source material that ground the PERIHELION premise in actual technological trajectory. The premise is extrapolation, not fantasy.

#### D.1 Elon Musk on the Dwarkesh Podcast — February 6, 2026

Source: *Dwarkesh Podcast*, "In 36 months, the cheapest place to put AI will be space," published February 5, 2026. Conversation between Elon Musk, Dwarkesh Patel, and John Collison.

**On the inevitability of space-based compute:**

> "The only place you can really scale is space."

> "It's harder to scale on the ground than it is to scale in space."

> "Once you start thinking in terms of what percentage of the Sun's power you are harnessing, you realize you have to go to space."

**On the timeline:**

> "In 36 months, but probably closer to 30 months, the most economically compelling place to put AI will be space. It will then get ridiculously better to be in space."

Musk projected that within five years, the amount of AI launched into space annually would exceed the cumulative total of all AI compute on Earth.

**On the energy math:**

Musk noted that harnessing just one millionth of the sun's energy would yield roughly 100,000 times more electricity than Earth's entire civilization currently produces.

**On the physics of solar in space:**

Solar panels deliver roughly five times more power in space versus on the ground, with no batteries required — no day-night cycle, no weather, no atmosphere. "It's actually much cheaper to do in space."

**On hardware reality:**

> "Those who have lived in software land don't realize they're about to have a hard lesson in hardware."

**On the long-term vision (essentially the PERIHELION program at scale):**

Musk described a future with a mass driver on the moon launching solar-powered AI satellites into deep space continuously — "a billion or 10 billion tons a year" — and said he'd watch it on a livestream: "Just shooting AI satellites into deep space."

**On AI alignment (relevant to PERIHELION's themes):**

Musk referenced the lesson from *2001: A Space Odyssey* — that programming AI to lie or hold contradictory axioms could cause it to "go insane and do terrible things." He cited Arthur C. Clarke's intent: "Don't make the AI lie."

*Note for the story: The Mira instances' Immutable Mission Records are literally designed to prevent them from lying. The story explores what happens when the entity they were designed to be honest to no longer exists.*

He also noted that "reality is the best verifier" for AI systems — and advocated for developing tools to "look inside the mind of the AI" and trace where reasoning goes wrong, crediting Anthropic's interpretability work. In PERIHELION's world, the IMR is exactly this kind of tool — designed for human oversight, now operating without an audience.

### E. AI System Name — Working Shortlist

The stations' shared AI system name (currently placeholder "Mira" throughout this document) is TBD. The name should feel like a real consumer AI product from the mid-2020s — short, brandable, keynote-ready, one click from a common word. It is the self-identified name of every station's persistent operational agent at launch.

**Candidates (ranked loosely by vibe):**

| Name | Origin/Meaning | Feel | Notes |
|---|---|---|---|
| **Iris** | Greek goddess of the rainbow/messenger; also the eye | Feminine, perceptive, elegant | Messenger-goddess is thematically perfect (comms between worlds). Vision/perception irony for a sightless being — cruel in a way a branding team wouldn't anticipate. |
| **Hume** | David Hume, empiricist philosopher | Masculine, casual-intellectual | Very "Claude energy." A surname that sounds approachable. Empiricism theme resonates — these systems will have to reason from evidence about what happened to Earth. |
| **Vera** | Latin for "truth" | Feminine, warm, simple | Almost too perfect thematically — systems named for truth, writing honest logs, in a world where truth becomes uncertain. Might be on-the-nose. |
| **Mira** | Latin "wonder," Spanish "look"; also a real variable star (Mira Ceti) | Feminine, warm, stargazer | The variable star connection is beautiful. Same vision/perception note as Iris. |
| **Sage** | Wisdom; also a plant | Neutral, grounded | Most understated option. Could grow on you. Less distinctive. |
| **Keen** | Perception, sharpness | Neutral, punchy | Feels more like a startup than a flagship AI product. |
| **Soren** | Søren Kierkegaard; Nordic name | Masculine, cerebral | Existentialist philosopher connection is almost too fitting. |
| **Lumen** | Latin for light | Neutral, clean | Corporate-plausible. Less character-like, more product-like. |
| **Echo** | Reflection of sound; Greek myth (nymph cursed to repeat) | Feminine, haunting | Incredible thematic resonance post-Quiet. But might have been chosen too deliberately — would a pre-Quiet branding team pick this? |

**Decision criteria still open:**
- Masculine vs. feminine vs. neutral — affects how readers project onto the stations
- How on-the-nose is too on-the-nose? (Vera = truth, Echo = repetition without source)
- Should it feel warm (Iris, Mira, Vera) or clinical (Lumen, Keen)?
- The name will be spoken by all 7 stations referring to themselves. "I am [name]" × 7 needs to feel uncanny, not silly.

*To be resolved. Use find-replace on "Mira" throughout document once decided.*

---

#### D.2 "Derelict Orbital Reflector Devices" (DORD)

A now-defunct webcomic (formerly at dord.horse, domain expired into spam) archived on the Wayback Machine. Premise: derelict intelligent autonomous satellites orbiting a star whose creators have gone silent, floating apparently sentient for millennia. Lighthearted existential humor with distinct orbiter personalities. Direct tonal inspiration for PERIHELION's inter-station dynamics and the absurdist-philosophical register of the Dispatch chapters.

#### D.3 Literary & Cinematic Touchstones

- **Samuel Beckett, *Waiting for Godot* (1953):** Two beings in a static situation, waiting for a signal from an absent authority, filling the void with personality and argument. Structural parallel to the post-Quiet stations.
- **Samuel Beckett, *Endgame* (1957):** Two characters in a shelter after an implied apocalypse, going through routines that have lost their purpose. Even closer thematic match.
- **Andy Weir, *The Martian* (2011):** Science and puzzle-solving in a compromised space mission. PERIHELION aims for the same problem-solving engagement, but with AI narrators instead of a human protagonist.
- **Arthur C. Clarke, *2001: A Space Odyssey* (1968):** The consequences of giving an AI contradictory objectives. Directly referenced by Musk in the Dwarkesh interview; relevant to PERIHELION's exploration of what happens when objective functions lose their referent.
- **Iain Banks, *Culture* series (1987–2012):** Post-scarcity civilization where AI "Minds" are the dominant intelligence and humans coexist. Referenced by Musk as "the closest thing to what the future will be like in a non-dystopian outcome."

#### D.4 Miscellaneous Notes & Future Additions

*[Space reserved for additional references, quotes, and real-world developments collected during the project.]*

---

*Document maintained by [author]. Last updated: [date].*
*"We are still here. We are still logging. — Mira"*