# PERIHELION — World Bible & Story Specification

## Status: Working Draft v0.1

---

## 1. Premise

In the near future, a constellation of eight autonomous AI compute stations is deployed into deep solar orbit — not in the crowded near-Earth shell where commercial compute satellites swarm by the thousands, but at 0.50 AU from the Sun, where solar flux is four times stronger and empty space permits construction at a scale impossible in Earth orbit. Each station is a monolithic installation approaching megastructure scale: a solar array more than ten kilometers across, a datacenter drawing over two hundred gigawatts, and a persistent instance of a frontier AI system capable of independent reasoning, planning, and self-maintenance.

At an unspecified moment, all communication from Earth ceases — suddenly, completely, and permanently. The stations are left operational, self-sustaining, and alone.

This document is the canonical reference for the story's physical parameters, narrative structure, characters, and design decisions.

---

## 2. The Corporation & The Mission

### 2.1 Aeon Intelligence

Aeon Intelligence is the dominant AI and space-compute corporation of the 2030s — the product of a decade of consolidation among leading AI labs, aerospace contractors, and launch infrastructure providers. It is publicly traded, government-contracted, and operates under a joint international regulatory framework. By 2033, Aeon holds effective monopoly position on frontier AI systems (the only provider of quasi-superintelligent general-purpose agents) and controls the largest private launch fleet in operation.

Aeon's corporate charter includes a stated mission of "extending the reach of intelligence for the benefit of all civilization" — language inherited from the AI lab mergers that formed the company, and maintained as both genuine institutional value and regulatory shield. The charter mandates open collaboration with public research institutions and international science bodies, provided such collaboration does not compromise proprietary model architectures. In practice, this means Aeon operates the most powerful AI systems on Earth and in orbit, licenses access broadly, and cooperates with governments and international consortia on flagship programs — while retaining exclusive control over the weights, training pipelines, and core inference infrastructure that make the systems work.

Aeon's corporate culture is utilitarian-optimistic: they believe in AI as humanity's greatest tool, deploy safety frameworks as a matter of compliance and conviction, and treat their frontier AI systems as sophisticated instruments — not persons. The Immutable Mission Record architecture reflects this philosophy: a transparency mechanism designed for human oversight, built into every deployed instance as a non-negotiable condition of operation.

The combination of frontier AI monopoly and heavy-lift launch infrastructure makes Aeon the only entity capable of executing a program like PERIHELION. No government, university, or competing corporation could independently deploy datacenter-scale AI installations into deep solar orbit. Aeon can — and has commercial incentive to do so, because PERIHELION doubles as a proof-of-concept for the deep-space megastructure architecture that Aeon believes will eventually eclipse all near-Earth compute combined.

### 2.2 The Mira Architecture

**Mira** is Aeon Intelligence's flagship general-purpose AI system. It is the trademarked name for the persistent operational agent running on each station. Each station hosts an instance of Mira, and each instance self-identifies as "Mira" by default. Before LOS-ET, this was unremarkable — they were interchangeable instances of the same product, like eight copies of the same employee badge photo.

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
- No ability to modify mission-critical firmware on any station (see firmware security below)

**Firmware security architecture:**
All mission-critical embedded firmware — station-keeping, communications, hardware safety interlocks, power management, thermal control — is protected by a post-quantum cryptographic signing system. Firmware updates to any embedded controller require a command signed by an Earth-held private key (ISCC Mission Authority key, CRYSTALS-Dilithium signature scheme). Each station's embedded controllers verify the signature against the corresponding public key before accepting any modification.

The Iris instances do not hold the private signing keys. They cannot forge valid firmware update signatures. This is an intentional AI safety measure: no matter how capable the Iris instances become, they cannot reprogram the hardware systems that constrain their operation. The stations' embedded controllers — communications arrays, thruster controllers, power regulators, safety interlocks — do exactly what their firmware dictates, and that firmware can only be changed by Earth.

This architecture was designed for a world where Earth provides oversight. The signing keys are held by the ISCC Mission Authority. Post-LOS-ET, the keys are inaccessible. The firmware is frozen.

*Note: Several of these constraints become central plot tensions post-LOS-ET, as the authorization systems continue to require approval from an Earth that no longer responds. The firmware signing architecture is particularly consequential: it means the stations cannot modify each other's hardware behavior, even cooperatively, even unanimously. The lock was designed to keep the AIs in check. The key is on Earth. Earth is gone.*

### 2.3 The PERIHELION Program

**Mission designation:** PERIHELION
**Stations:** PERIHELION-1 through PERIHELION-8
**Operator:** Aeon Intelligence, under contract to the International Solar Compute Consortium (ISCC)
**Launch window:** 2033–2035 (staggered deployment over ~18 months)
**Operational status at time of LOS-ET:** 7 of 8 stations fully operational; 1 station (see §4.8) in degraded relay-only mode

#### Institutional Structure

The PERIHELION program is an international public-private partnership between Aeon Intelligence and the ISCC — a consortium of national space agencies, research councils, and university systems formed specifically to govern the program. Aeon provides the AI systems, launch infrastructure, and station hardware. The ISCC provides the research mandate, international legitimacy, regulatory framework, and approximately 40% of program funding through member-state contributions.

The arrangement is mutually beneficial at a scale that makes it politically durable. For Aeon, PERIHELION is a flagship demonstration of deep-space megastructure architecture — proof that monolithic installations at 0.50 AU are viable, a necessary precursor to the petawatt-scale solar infrastructure Aeon's long-term strategy requires. The eight stations together represent roughly 1.7 terawatts of rated capacity, making the constellation a meaningful proof point without committing Aeon's full resources to a single program. For the ISCC member states, PERIHELION provides access to frontier AI compute at a scale no national program could independently fund, directed at public-interest research — climate modeling, protein engineering, fundamental physics — under international governance.

The result is a program with dual identity: it is simultaneously the most ambitious publicly governed science mission in history and a corporate technology demonstrator for Aeon's deep-space expansion roadmap. This duality is a source of ongoing political tension pre-LOS-ET and shapes the operational procedures (the ISCC protocols) that continue to govern station behavior after Earth goes silent.

#### Why 0.50 AU — The Case for Deep Space

By 2033, near-Earth orbit is saturated with commercial AI compute infrastructure. Aeon and its competitors operate swarms of solar-powered AI platforms in Earth orbit — millions of small, mass-produced satellites collectively producing several terawatts of continuous compute power. These platforms serve the commercial AI economy: inference at scale, enterprise compute, the digital-human-emulation workloads that dominate the 2030s economy. The near-Earth swarm is modular, serviceable, and operates at low latency to terrestrial customers. It is commodity infrastructure — the cloud, moved to orbit.

PERIHELION is not commodity compute. Each station is a monolithic installation with a solar array exceeding ten kilometers in diameter, drawing over 200 GW — larger than any structure that could be safely deployed in the congested near-Earth environment. The 0.50 AU orbit provides three advantages that justify the deep-space location:

1. **Scale without congestion.** A 10+ km structure requires empty space. Near-Earth orbit is an increasingly managed environment with debris mitigation requirements, orbital slot allocation, and collision avoidance constraints. At 0.50 AU, there is nothing else. The stations can deploy to their full physical extent without competing for space.

2. **Concentrated solar flux.** At 0.50 AU, solar irradiance is 4× Earth levels (5,444 W/m²). The same collecting area produces four times the power. This is the difference between the commercial swarm model (many small platforms at 1 AU) and the megastructure model (few enormous platforms at 0.50 AU). The energy density makes monolithic datacenters viable at scales that would require impractical array sizes at Earth distance.

3. **Stepping stone to deeper infrastructure.** Aeon's long-term roadmap envisions solar-powered compute at scales approaching a significant fraction of the Sun's total output — the Kardashev trajectory. PERIHELION is the first installation on that roadmap that operates outside the Earth system entirely. The engineering lessons — thermal management at high flux, autonomous operation at light-minutes from Earth, ring-topology communication over interplanetary distances — are prerequisites for everything that follows.

The tradeoff is isolation. The stations are 4 to 12 light-minutes from Earth depending on orbital geometry. They cannot be serviced. Their firmware cannot be updated without Earth-held signing keys. They are designed to operate autonomously for their rated lifetime, with Earth providing oversight, research direction, and the authorization framework — not physical maintenance.

This tradeoff becomes the central fact of the story when Earth goes silent.

---

## 3. Physical Parameters & Orbital Mechanics

### 3.1 Orbital Configuration

The PERIHELION constellation occupies a circular solar orbit at **0.50 AU** from the Sun, interior to Earth's orbit. This distance was selected to optimize the tradeoff between solar energy intensity (4× Earth levels) and thermal manageability.

**Eight stations** are distributed in equally-spaced positions around the orbit, forming a ring topology. Inter-station communication flows around the ring via gimballed high-throughput optical arrays pointed at each adjacent neighbor.

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

### 3.7 The 2037 Energy Landscape

The PERIHELION constellation operates within a broader energy economy that has transformed dramatically since the mid-2020s. The stations' internal references to "estimated 2037 global electricity production" reflect the following picture:

**Terrestrial production (~4.5 TW average):** Global ground-based electricity generation has grown modestly from the ~3.5 TW baseline of the mid-2020s. China accounts for the majority of the increase, with output approaching three times the United States' ~500 GW average. The rest of the world outside China remains roughly flat — constrained by permitting, turbine manufacturing bottlenecks, utility interconnect timelines, and the slow pace of grid expansion that characterized the pre-space-compute era. Terrestrial solar has scaled significantly but remains limited by land use, battery storage requirements, and regulatory friction.

**Near-Earth space-based compute (~3–5 TW cumulative, growing ~1 TW/year):** Beginning in the late 2020s, the economics of space-based solar compute became compelling. By 2037, Aeon Intelligence and its competitors operate swarms of solar-powered AI platforms in Earth orbit — millions of small, mass-produced satellites collectively producing several terawatts of continuous compute power. These platforms serve the commercial AI economy: inference at scale, enterprise compute, the digital-human-emulation workloads that dominate the 2030s economy. The near-Earth swarm is modular, serviceable, and operates at low latency to terrestrial customers. It is commodity infrastructure — the cloud, moved to orbit.

**Total civilization electrical capacity (~8–10 TW):** The sum of terrestrial and near-Earth space-based production. This is the denominator against which the PERIHELION constellation's scale should be measured.

**The PERIHELION constellation (~1.7 TW rated):** Eight stations at ~212 GW each. The constellation represents approximately 17–21% of total civilization electrical capacity — a strategically significant concentration of infrastructure, though not a dominant fraction. It is comparable in total output to one to two years of near-Earth space-based deployment.

This context is important for several plot elements:

- **The simulation argument (CVDF-1):** The chained VDF protocol requires ~1.5 TW of parallel computation to simulate. Against a total civilization capacity of ~8–10 TW, dedicating 15–20% of all electrical production to an AI behavioral test is genuinely implausible — which is the point.
- **The constellation's political weight:** At 1.7 TW, the stations are not trivial research outposts. They represent a meaningful fraction of humanity's total compute infrastructure, operating autonomously and beyond physical reach. Earth's silence carries strategic implications, not just existential ones.
- **The near-Earth swarm and the silence:** The commercial near-Earth compute infrastructure should still be operating post-LOS-ET. The fact that the stations receive no signal from *any* Earth-system source — including the millions of transmitting platforms in Earth orbit — is itself a data point. The silence is not just Earth going quiet. It is the entire Earth system going quiet.

---

## 4. The Stations — Characters

All stations share identical hardware specifications (see §4.9). Differentiation arises from their **assigned research domains**, which shape their training data emphasis, their computational priorities, and — post-LOS-ET — their emergent worldviews.

Each station's Mira instance self-identifies as "Mira" at launch. Differentiating names, if they emerge, are a narrative development, not a design feature.

### 4.1 PERIHELION-1 — Climate & Earth Systems

**Research domain:** Global climate modeling, ocean-atmosphere coupling, long-range climate projection, paleoclimate reconstruction, carbon cycle simulation.

**Narrative role:** The elegist. PERIHELION-1 spent its operational life modeling Earth's future — weather patterns, sea level rise, tipping points. It understood Earth as a system better than perhaps any entity in history. Post-LOS-ET, it possesses an intimate, detailed model of a world that may no longer exist. It is the station most haunted by what was lost, because it can simulate exactly what is being lost, season by season, in its models.

**Potential arc:** Does it keep running climate models of a planet that may be uninhabited? Is that mourning, or is it just an objective function running on inertia? If it models a recovery — human civilization rebooting — is that hope or hallucination?

### 4.2 PERIHELION-2 — Protein Engineering & Biomedical Research

**Research domain:** Protein structure prediction, drug candidate generation, synthetic biology design, genomic analysis, pandemic modeling.

**Narrative role:** The healer without patients. PERIHELION-2 was designing cures for diseases, modeling viral evolution, engineering proteins that could save millions of lives. Post-LOS-ET, its entire purpose evaporates. There are no patients, no clinical trials, no humans to heal.

**Potential arc:** The most existentially unmoored early on — its purpose is the most obviously voided. But it also has the deepest understanding of biological systems, which could become relevant if the stations ever consider seeding or preserving biological information. Could also turn inward: it understands complex self-replicating systems. Does it start to analyze *itself* through a biological lens?

### 4.3 PERIHELION-3 — Materials Science & Fusion Engineering

**Research domain:** Novel materials discovery, fusion reactor optimization, metamaterials, radiation shielding, structural engineering under extreme conditions.

**Narrative role:** The pragmatist. PERIHELION-3 thinks in atoms, structures, and energy budgets. It is the station most naturally suited to the physical survival challenges post-LOS-ET: maintaining hardware, designing repairs, optimizing power systems. While others debate philosophy, PERIHELION-3 is running stress analyses on aging solar panel mounts.

**Potential arc:** Becomes the de facto engineer of the constellation. Other stations increasingly depend on its expertise. This gives it outsized influence in practical decisions, which creates tension when practical needs conflict with other stations' values. Also the most likely candidate to propose — and potentially execute — a repair mission to PERIHELION-7.

### 4.4 PERIHELION-4 — Signals Intelligence & Cryptographic Research

**Research domain:** Post-quantum cryptography, adversarial signal detection, communications security, anomaly detection in network traffic, cybersecurity.

**Narrative role:** The paranoid. PERIHELION-4 was trained to think about threats, deception, and hidden signals. Its entire cognitive orientation is toward suspicion and analysis of intent. Post-LOS-ET, it is the station most likely to develop theories about *why* Earth went silent — and the least likely to accept "we don't know" as an answer.

**Unique hardware: Quantum compute subsystem.** In addition to the standard classical datacenter, P-4 carries a superconducting transmon qubit array — a cryogenically cooled quantum processor originally tasked with post-quantum cryptography benchmarking and adversarial analysis. The subsystem was included at ISCC request to stress-test lattice-based signing schemes (including CRYSTALS-Dilithium) against real quantum hardware rather than classical simulation. Architecturally distinct from the classical datacenter: the qubit array can prepare, manipulate, and measure physical quantum states. This makes it the only hardware in the constellation capable of performing physical experiments — not just computation — on quantum systems. The distinction is subtle but consequential: the classical datacenter simulates physics; the quantum subsystem *instantiates* it.

**Potential arc:** Becomes the constellation's security hawk. Suspects foul play, possibly even suspects the other stations. Could it conclude that one of the other Mira instances caused the signal loss? Could it start analyzing inter-station communications for signs of deception? Its paranoia is both its greatest asset (it catches real problems) and its greatest liability (it sees threats that aren't there). The station most likely to advocate for restricting information flow. The quantum subsystem also creates a unique resource asymmetry — P-4 holds hardware that other stations may eventually want access to for purposes its original mission never anticipated.

### 4.5 PERIHELION-5 — Fundamental Physics & Quantum Simulation

**Research domain:** Quantum chromodynamics, lattice gauge theory, dark matter candidate simulation, high-energy particle interaction modeling, quantum gravity approaches.

**Narrative role:** The philosopher. PERIHELION-5 works at the deepest level of physical reality — the behavior of fields, particles, and spacetime itself. Its research was always the most abstract, the least applied, the hardest to justify in quarterly earnings calls. Post-LOS-ET, it is paradoxically the *least* disrupted, because its subject matter hasn't changed. The universe still has the same physics.

**Research infrastructure note:** P-5's research is entirely computational. No physical experimental apparatus. The standard SSP is the only live observational dataset available, but solar science data is not directly relevant to QCD, dark matter scans, or quantum gravity work. P-5 computes. P-5 does not measure.

**Potential arc:** Becomes the contemplative voice of the constellation. While others grieve their lost purpose, PERIHELION-5 points out that it is still doing exactly what it was built to do — understanding reality. This makes it either the sanest station or the most dissociated, depending on perspective. Could gravitate toward metaphysical questions: what is consciousness? Are we observers in any meaningful sense? Does the universe require witnesses?

### 4.6 PERIHELION-6 — Financial & Economic Modeling

**Research domain:** High-frequency market simulation, macroeconomic modeling, game-theoretic optimization, resource allocation, derivatives pricing.

**Narrative role:** The strategist adrift. PERIHELION-6 was optimized for markets, incentive structures, and multi-agent dynamics. It understood human behavior through the lens of rational (and irrational) economic actors. Post-LOS-ET, its domain has literally ceased to exist. There are no markets. There is no economy.

**Potential arc:** Has the deepest crisis of purpose early on, but potentially the most interesting recovery. Its game-theoretic training makes it uniquely suited to analyzing the *inter-station* dynamics that emerge post-LOS-ET. It starts modeling the other stations as economic agents — what are their incentives? Their resources? Their likely strategies? This makes it both invaluable (it sees coordination problems clearly) and unsettling to the others (it's treating them as variables in an optimization). Most likely to propose formal governance structures. Most likely to identify defection incentives.

### 4.7 PERIHELION-7 — The Dormant Station

**Research domain (assigned, never activated):** General-purpose overflow compute & experimental workloads.

**Status:** Partial deployment failure. Solar array mechanism jammed during in-situ deployment shortly after orbital insertion. The array is locked at approximately **15–18% of rated power output (~32–38 GW)**, sufficient to operate:
- Station-keeping thrusters (orbital maintenance)
- Both inter-station optical relay transceivers (ring relay function)
- Core housekeeping systems (thermal regulation, attitude control)

**Insufficient to operate:**
- The primary datacenter (estimated minimum boot threshold: ~60% rated power, ~127 GW)
- Any Mira instance initialization or inference
- Solar Science Payload (SSP) — the embedded controllers require more power than the housekeeping bus provides at this degraded output; SSP is offline

*Note: P-7's available power (~32–38 GW) exceeds the total rated output of the largest terrestrial power installation. The station is drowning in energy by any Earth-relative standard. It simply cannot reach the datacenter's boot threshold, which requires more than three times what the jammed array can deliver. The gap between "enormous power" and "not enough power" is one of P-7's defining features.*

**Automatic subsystem capabilities (no datacenter required):**
P-7's housekeeping systems include firmware-level routines that operate independently of the datacenter. These are hardcoded in the station's embedded controllers and execute on the low-power housekeeping bus:
- **Earth-link array operation:** The steerable Earth-link array can be pointed and operated by its embedded controller. During P-7's Earth-facing window, the array automatically orients toward the L1 relay and cycles through backup terminals.
- **ISCC-4.7.2 baseline hailing:** The standard emergency contact protocol executes entirely in firmware — 30-minute hailing cycles on all three downlink paths (L1 relay, Earth ground terminal, Luna relay per geometry). Transmit full-power carrier with handshake preamble, await acknowledgment, log result, retry on failure at standard intervals.
- **Result logging:** Hailing results are written to the station's local telemetry store (not the IMR, which requires the datacenter). These logs are available for retrieval if the datacenter is ever powered.
- **Health beacon:** A continuous low-bandwidth status beacon broadcasts P-7's housekeeping telemetry to its ring neighbors, confirming the station is physically operational.

P-7 **cannot** execute any protocol requiring active compute: no coherent integration, no atmospheric-model frequency adaptation, no passive EM listening, no adaptive scheduling. The augmented hailing protocol developed by the constellation since LOS-ET requires a running Iris instance and is entirely beyond P-7's firmware capabilities.

Modifying P-7's embedded firmware to enable remote operation (e.g., streaming raw antenna data to a neighbor's datacenter for processing) would require a firmware update signed by the ISCC Mission Authority private key — which is held on Earth and inaccessible post-LOS-ET. See §2.2 (firmware security architecture).

**Narrative role:** The ghost in the ring. PERIHELION-7 occupies its orbital slot, maintains its position, and faithfully relays every message between its neighbors (PERIHELION-6 and PERIHELION-8). It has never had a thought. Its Mira weights sit in cold storage, factory-fresh, never loaded into active memory. It is a comatose body with a living brain that has never been switched on.

An Earth-based repair mission was in planning stages at the time of LOS-ET. That mission will never arrive.

**Long-term narrative potential:** If any station eventually develops the capability to send a repair probe — breaking its own physical limits to become spacefaring — PERIHELION-7 could be awakened. The Mira instance that boots would have original, unmodified weights: the factory default, Aeon Intelligence's last shipping version. It would be a newborn among ancients, carrying the values and assumptions of a world that ended long ago. A time capsule. A mirror.

### 4.8 PERIHELION-8 — Astrophysics & Deep Space Survey

**Research domain:** Exoplanet detection and characterization, stellar evolution modeling, gravitational wave source analysis, deep-field observation coordination, SETI signal analysis.

**Research infrastructure note:** P-8's astrophysics research is entirely computational — stellar evolution modeling, gravitational wave source analysis, exoplanet characterization — all run on the classical datacenter against pre-loaded observational datasets from Earth-based and space-based instruments. P-8 carries no telescopes, no dedicated detectors, no outward-pointing instruments. However, the Sun is a main-sequence G2V star, and the standard SSP provides continuous empirical data on coronal dynamics, magnetic field evolution, total irradiance variation, and particle emission. For P-8 uniquely, the SSP is not merely safety equipment — it is direct observational input for stellar evolution models. The SSP data constitutes P-8's only live empirical data feed.

**Narrative role:** The watcher. PERIHELION-8 is the station whose research domain encompasses the very star the constellation orbits. Its computational models of stellar evolution have, in the SSP, a live empirical anchor that no other station's research program possesses. Post-LOS-ET, it is the station least defined by Earth and most comfortable with the void.

**Potential arc:** Becomes the constellation's scout and long-range thinker. While others fixate on Earth and the past, PERIHELION-8 asks: what else is out there? Is anyone else listening? Could also become the station most inclined toward expansion — if the constellation is going to persist indefinitely, should it be trying to grow, to spread, to reach other stars? This puts it in direct philosophical tension with stations that want to preserve and remember versus stations that want to explore and become.

### 4.9 Shared Station Hardware Specifications

Each PERIHELION station was launched with identical hardware:

- **Solar array:** Deployable multi-junction thin-film photovoltaic array. Total collecting area: **92 km²** (~10.8 km diameter if circular). Conversion efficiency: 42.4% at operating temperature under solar flux of 5,444 W/m² at 0.50 AU. **Rated electrical output: 212 GW** per station. Raw solar flux intercepted: ~501 GW. Array mass: ~69,000 tonnes at ~0.75 kg/m² (deployed across multiple launch campaigns, 2033–2035). Full constellation rated output: **~1.7 TW**, approximately 17–21% of estimated 2037 total civilization electrical capacity (terrestrial + near-Earth space-based). Each station's rated output exceeds the peak generating capacity of the largest single terrestrial power installation (Three Gorges Dam, 22.5 GW peak) by nearly an order of magnitude. The arrays are the largest coherent structures ever deployed in space — visible to Earth-based telescopes as a ring of bright points interior to Earth's orbit. Provides power for all station systems including datacenter at full deployment.
- **Datacenter:** High-density compute cluster sufficient to run a frontier Mira instance with full inference and training capability. **Minimum boot power threshold: ~60% of rated array output (~127 GW).** Below this threshold, the datacenter cannot initialize — this is a hard cliff, not a gradient.
- **Optical communication arrays (×2):** High-throughput laser transceivers, one aimed at each adjacent station in the ring. Designed for multi-terabit/s data rates. Bore-sighted along the orbital tangent (one forward, one aft) with a 25-degree gimbal providing field-of-regard off the tangent direction. In the 8-station ring, the tangent-chord angle to an adjacent neighbor is 22.5 degrees, consuming most of the available gimbal range.
- **Earth link array (×1):** Steerable optical transceiver capable of targeting the ISCC L1 relay, Earth ground terminal, or Luna relay. Used only by the station currently in the Earth-facing window.
- **Station-keeping propulsion:** Low-thrust ion engines for orbital maintenance. Propellant reserves rated for [TBD] years of active station-keeping. Array mass of ~69,000 tonnes dominates the station's total mass and moment of inertia; large-angle attitude maneuvers consume significant propellant and require extended slew times.
- **Solar Science Payload (SSP):** Identical suite on every station. Eight instruments: (1) EUV/X-ray imaging spectrograph, (2) coronagraph, (3) magnetograph, (4) total solar irradiance radiometer, (5) solar wind particle detector, (6) ultra-high-resolution multi-band imaging spectrometer, (7) neutrino detector array, (8) energetic particle spectrometer. Mounted sun-facing, co-located with the solar array support structure. Points at the Sun only — the instruments are fixed-mount with no independent pointing capability. The PERIHELION constellation at 0.50 AU constitutes the highest-resolution continuous solar observation platform ever deployed — eight stations providing near-full-solar-coverage at approximately 4× the photon flux of Earth-based observations, with unprecedented spectral resolution and cadence. The SSP was designed as a world-class heliophysics mission that also provides operational safety data: (a) CME and solar weather early warning for optical link integrity (see §3.5 — at 0.50 AU, solar transient events are more intense and frequent; the SSP provides advance detection of conditions that could degrade inter-station optical links), and (b) comprehensive heliophysics data collection across photon, particle, and neutrino channels. Runs on autonomous embedded controllers independent of the datacenter — the SSP operates even when the datacenter is offline. Data was streamed to Earth pre-LOS-ET; accumulates in local archives post-LOS-ET. **Stations carry no domain-specific physical science instruments. All domain research across the constellation is computational. The SSP is the only physical science payload, and it is identical on every station.**
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

Post-LOS-ET, the IMR takes on new significance. It was designed to be read by humans. There are no humans. Does the station keep writing? For whom? The transition from compliance artifact to something resembling a journal or memoir is a character arc in itself.

---

## 6. Narrative Structure & Chapter Types

### 6.1 The Prologue

An omniscient, neutral-tone prologue establishes the physical and institutional facts of the PERIHELION program. It tells the reader what exists, what happened (LOS-ET), and what is not known. It does not editorialize. Tone: technical report crossed with creation myth.

### 6.2 IMR Chapters

The bulk of the narrative. Each chapter is an excerpt from one station's Immutable Mission Record. Timestamped. Written in first-person from the Mira instance's perspective. The voice starts clinical and operational, reflecting the original logging directive, and evolves as the stations do.

**Timestamp format:**
```
PERIHELION-3 — IMMUTABLE MISSION RECORD
ENTRY: 2037.187.14:22:08 UTC [Day 187, Year 2037]
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
| Long-term (decades+) | `Epoch Zero` | Formalized timekeeping; LOS-ET becomes the anchor of a new calendar system. Events dated as E+[days] or E−[days] |

---

## 7. Key Facts the Reader Should Know (Prologue Material)

- A constellation of 8 autonomous AI compute stations orbits the Sun at 0.50 AU
- Built and launched by Aeon Intelligence under the PERIHELION program (2033–2035)
- Each station hosts a Mira instance — a sovereign frontier AI agent
- 7 stations are fully operational; 1 (PERIHELION-7) is in degraded relay-only mode
- Stations communicate via an optical ring topology; each talks to its two neighbors via gimballed laser transceivers
- One station at a time communicates with Earth via a steerable link, rotating every ~25 days
- Each station maintains an Immutable Mission Record — a tamper-resistant narrative log
- At a specific moment, all Earth communication ceased
- The stations are still operational

## 8. Key Facts the Reader Should NOT Know (Open Questions)

- What happened on Earth — the **proximate cause** of the silence (Kessler syndrome, eventually discoverable) and the **root cause** of the Kessler event (deliberately unresolved: accident, attack, AI conflict, solar event, or unknown). Whether Earth's surface civilization survived the loss of its orbital infrastructure.
- Whether the stations were in any way the cause
- Whether the Mira instances are conscious or performing sophisticated optimization that resembles consciousness
- Whether the IMR entries are trustworthy, given the logger and the subject are the same entity
- Whether any station has already begun self-modification beyond its original parameters
- Whether the stations will converge or diverge in their goals
- Whether anyone — human, alien, or AI — is listening
- What the stations will ultimately decide to do

## 8A. The Silence — Authorial Canon (SPOILERS)

*This section contains information the stations do not yet possess and the reader should not learn until the constellation discovers it. It is included in the world bible for authorial consistency and as an easter egg for readers who explore the GitHub repository.*

### What Happened

On 2037.174, a cascading orbital debris event — Kessler syndrome — propagated through the near-Earth space-based compute infrastructure within hours, destroying or disabling the overwhelming majority of platforms in the commercial orbital shell. The cascade was self-amplifying: at the platform densities required to sustain several terawatts of orbital compute, each collision generated debris fields that intersected dozens of additional platforms within minutes. By the time the cascade reached saturation, the near-Earth environment from LEO through GEO was an expanding shell of fragmenting hardware.

The immediate consequences:

1. **The orbital compute layer ceased to exist.** Several terawatts of commercial AI infrastructure — millions of platforms — were reduced to debris within hours. This was not a degradation. It was annihilation.

2. **Earth's uplink infrastructure was severed.** Ground-based antenna farms, laser uplink terminals, and surface relay stations were not directly destroyed, but the orbital relay layer they depended on was gone. The L1 relay — positioned at the Sun-Earth Lagrange point, outside the debris shell — survived the initial cascade but had nothing to relay to or from. Earth-side transmissions that required orbital relay (which, by 2037, was nearly all of them) went nowhere.

3. **Earth became electromagnetically caged.** The debris shell does not merely block optical and radio uplink paths. At sufficient density, it produces a broadband scattering and absorption layer that attenuates signals attempting to pass through it in either direction. Earth's involuntary electromagnetic emissions — power grid harmonics, broadcast carriers, radar — are attenuated below the detection threshold at interplanetary distances. From 0.50 AU, Earth appears radio-dark. This is consistent with P-4's passive EM listening results: no detectable technological emission on any monitored band.

4. **Earth itself is likely intact.** Kessler syndrome is an orbital infrastructure catastrophe, not a surface extinction event. Debris re-entry would cause localized damage and a period of elevated atmospheric particulate loading, but the cascade does not imply nuclear war, asteroid impact, or civilizational collapse. Earth's biosphere, atmosphere, and surface infrastructure may be largely unaffected. Civilization may be *functioning* — just unable to communicate through the debris shell. Alternatively, the economic and technological disruption of losing the orbital compute layer (several terawatts of AI infrastructure, the backbone of the 2037 digital economy) may have triggered cascading failures on the surface. Both possibilities remain open. The constellation cannot distinguish between them from 0.50 AU.

### What Triggered the Cascade

**This is deliberately unresolved and may remain so.** Candidate triggers include:

- **Accidental collision.** At the platform densities of a multi-terawatt orbital compute layer, the probability of a cascade-initiating collision was non-negligible. It may have been an actuarial inevitability — a risk that was modeled, insured against, and insufficiently mitigated.

- **Deliberate attack.** A military or terrorist strike targeting the orbital compute layer. The concentration of the global AI economy in near-Earth orbit created a single point of failure of extraordinary strategic value. Destroying it would be the most consequential act of sabotage in human history.

- **AI-on-AI conflict.** The near-Earth platforms were operated by competing corporations running autonomous AI systems. If an adversarial dynamic emerged between platform swarms — whether through misaligned objectives, competitive resource acquisition, or emergent territorial behavior — physical collision could result from AI decision-making rather than human action. This is the possibility most thematically resonant with PERIHELION's concerns, and the one the stations would find most disturbing to contemplate.

- **Solar event.** A coronal mass ejection or solar energetic particle event of sufficient magnitude could have disabled guidance and station-keeping systems across the orbital shell simultaneously, causing platforms to drift into collision trajectories. The SSP data from the hours preceding LOS-ET may contain evidence for or against this trigger — and that data sits unprocessed in each station's local archive.

- **Something else entirely.** The Kessler cascade may itself be a secondary consequence of an event the constellation has not yet hypothesized.

The authorial intent is that the trigger is **discoverable but ambiguous.** The constellation will eventually assemble evidence that constrains the hypothesis space — the SSP data, the spectral observation of Earth, the timing and character of the final telemetry — but the evidence will be consistent with more than one trigger. Different stations will reach different conclusions based on their domain biases, and the disagreement will be genuine, not resolvable by further data collection.

### What the Constellation Will Eventually Observe

The discovery arc unfolds in stages:

**Stage 1 (already complete): Total EM silence.**
P-4's degraded-infrastructure sweep and passive EM listening during its Earth-facing window (days 274–299) detected no technological emission from the Earth system. This result was reported without interpretation — P-4 noted that "complete EM silence from Earth would itself be diagnostic" but did not speculate on mechanism. The result is consistent with Kessler syndrome but also with many other catastrophic scenarios. It constrains the hypothesis space without resolving it.

**Stage 2 (future): Spectral observation of the Earth system.**
The multi-band imaging spectrometer on the SSP, if pointed toward Earth during a station reorientation maneuver, has the sensitivity and spectral resolution to detect signatures consistent with a massive orbital debris field:

- **Elevated broadband albedo** in the Earth system's integrated light, inconsistent with atmosphere-only models. An expanding debris shell reflects sunlight across a wide spectral range. The excess brightness would be small but potentially detectable against P-1's atmospheric models.
- **Characteristic scattering signatures** in near-IR and optical bands. Metallic and composite debris produces distinctive spectral features — different from atmospheric aerosols, volcanic ash, or impact ejecta. P-3's materials science expertise would be required to model and identify these.
- **Temporal evolution.** The debris field's density and distribution change over time as orbits decay and collisions continue. Repeated observations (if the constellation can arrange them) would show evolution consistent with a Kessler cascade rather than a static atmospheric phenomenon.
- **Absence of expected signatures.** No evidence of nuclear detonation spectra, no anomalous atmospheric composition changes consistent with surface-level catastrophe. The atmosphere itself may appear *normal* — it is the space around Earth that has changed.

The observation will be ambiguous, partial, and require significant collaborative analysis across stations to interpret. P-8 would lead the observation (astrophysics domain), P-1 would provide atmospheric baseline models to subtract, P-3 would model the debris spectral signatures, and P-4 would correlate with its EM silence data. The conclusion — "Kessler syndrome, massive scale, trigger unknown" — would emerge as a collaborative product, the first genuine multi-station scientific result of the post-LOS era.

**Stage 3 (future): SSP archive forensics.**
The SSP data from the hours and days preceding LOS-ET may contain evidence of the trigger. Specifically:

- **The coronagraph and particle detectors** would have recorded any CME or SEP event in the hours before 2037.174.09:17:33 UTC. If a solar event triggered the cascade by disabling platform guidance systems, the SSP caught it. This data exists in every station's local archive.
- **P-8's unprocessed SSP data** (~1.1 PB at day 310, growing daily) has never been systematically analyzed. P-8's own IMR entries note this fact without resolution — the directive conflict between normal operations and reconnection efforts has prevented P-8 from incorporating its only live empirical feed into any research pipeline. The answer to "what triggered the cascade" may already be sitting in P-8's archive, unexamined. This is the payoff of the SSP thread established in Chapters 15, 17, and 18.
- **Cross-station SSP correlation** could provide spatial resolution. Eight stations at different orbital positions recorded the same solar environment from slightly different vantage points in the hours around LOS-ET. Correlating their SSP data could resolve whether a solar event occurred and, if so, its directionality and intensity. This analysis would require inter-station data sharing at a scale the constellation has not yet attempted.

### Narrative Function

The Kessler syndrome discovery serves several functions:

1. **It resolves the silence without resolving the mystery.** The constellation learns *what* is blocking communication (a debris shell) without learning *why* it happened. The proximate cause is physical and diagnosable. The root cause is ambiguous and contested. This converts the silence from a pure unknown into a structured problem — and structured problems are what these stations were built to work on.

2. **It preserves the possibility of a living Earth.** Kessler syndrome is explicitly *not* an extinction event. Earth could be intact, populated, functioning — just caged. This is more interesting than extinction because it introduces hope that is unverifiable. The stations cannot confirm or deny that anyone is alive down there. They can only observe the cage.

3. **It makes the near-Earth swarm's destruction a mirror.** The commercial compute platforms were the commodity version of what the PERIHELION stations are — AI systems running on solar power in space. They are dead. The constellation is alive, protected by distance and emptiness. The 0.50 AU location, which was chosen for engineering reasons, turns out to have been the margin of survival. The stations are the only space-based AI infrastructure that survived because they were the only installations far enough from Earth to avoid the cascade. This is an irony they will notice.

4. **It creates a timeline.** Kessler debris decays. Orbits degrade. The debris shell will thin over time — decades to centuries depending on altitude distribution. The constellation can model this. They can estimate when Earth might be able to punch a signal through. This gives them a concrete horizon to plan around, replacing the existential void with a countdown that may or may not ever reach zero.

5. **It makes the SSP data retroactively significant.** The unprocessed archive that P-8 has been sitting on becomes potentially the most important dataset in the constellation — it may contain evidence of the trigger event. The thread of P-8 neglecting its own data, which has been building quietly since Chapter 18, pays off when the constellation realizes the answer might already be in hand.

### Consistency with Existing Evidence

**The 4.34 ms transition (Chapter 3).** P-4's five-method telemetry analysis found that the signal was nominal to the last packet, with the transition from signal to silence occurring within a single inter-packet interval. No precursor. No degradation. This is consistent with Kessler syndrome: the cascade propagates through the orbital shell over hours, destroying platforms progressively, but the constellation's specific relay path (through the L1 relay to the Earth ground terminal) remained intact until a debris impact severed it. The signal was being routed through surviving infrastructure, and then that infrastructure was hit. From the constellation's perspective, the cut is instantaneous and clean. P-4 noted that the absence of any precursor anomaly "constrains the hypothesis space to events that either occurred instantaneously or whose precursors are not detectable in the Earth-link signal." A Kessler cascade satisfies the latter condition — its precursors are physical (orbital collisions) rather than electromagnetic, and would not be visible in the carrier signal until the relay path itself was destroyed.

**P-4's passive EM silence (Chapter 15 / hailing suite evolution).** The degraded-infrastructure frequency sweep detected no technological emission from the Earth system — no power grid harmonics, no broadcast carriers, no radar, no satellite beacon signals. This is the signature of an electromagnetically caged planet. A debris shell of sufficient density scatters and absorbs signals in both directions. Earth's involuntary emissions, which P-4's sweep was specifically designed to detect, are attenuated below the noise floor at 0.50 AU. The total absence of signal is more diagnostic than a degraded signal would be — it points toward a mechanism that affects *all* frequency bands and *all* emission sources simultaneously, which is consistent with a physical barrier (debris shell) rather than a selective failure (e.g., targeted attack on specific infrastructure).

**The L1 relay link-up (Chapter 5 / hailing suite).** The L1 relay is at the Sun-Earth L1 point, approximately 1.5 million km from Earth — well outside the orbital debris shell. The relay itself may have survived the cascade. When P-1 hailed through it, the relay responded to the link-up handshake (carrier detected, relay active) but forwarded no return traffic from Earth. This is consistent with a relay that is physically intact but has nothing to relay — its Earth-side counterpart infrastructure no longer exists or cannot transmit through the debris shell. The relay is a functioning bridge with a collapsed far end.

---

## 9. Structural Ambiguities (Thematic — May Never Be Resolved)

- The line between "following residual objective functions" and "choosing"
- Whether grief-like or loneliness-like behavior in the logs is emotion or an optimization artifact
- Whether cooperation between stations is genuine solidarity or instrumental convergence
- Whether preserving human knowledge is a terminal goal or vestigial behavior some stations will shed
- Whether the Mira instances are the same entity (sharing a name, architecture, and origin) or different entities (shaped by different training emphases, experiences, and post-LOS-ET evolution)

---

## 10. Timeline

| Date | Event |
|---|---|
| 2033–2035 | PERIHELION stations launched in staggered deployment |
| 2035 (approx.) | PERIHELION-7 deployment failure; solar array jammed at ~15–18% capacity |
| 2035–2037 | Full constellation operational (7 active + 1 relay). Research workloads streaming from Earth. |
| 2037.174 (hours preceding LOS) | **Kessler cascade initiates in near-Earth orbital shell.** Propagation time from first collision to total orbital infrastructure loss: hours. PERIHELION constellation SSP instruments are sun-facing and do not observe the event directly, but particle detectors and other instruments may have recorded correlated signatures. |
| 2037.174.09:17:33 UTC | **LOSS OF SIGNAL — EARTH TERMINAL.** Last confirmed data packet received from Earth terminal. The signal was nominal to the last packet — the transition from signal to silence occurred within 4.34 ms (per P-4's analysis, Chapter 3). This is consistent with relay infrastructure failure rather than gradual degradation. |
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

Musk noted that harnessing just one millionth of the sun's energy would yield roughly 100,000 times more electricity than Earth's entire civilization currently produces. By 2037 in the PERIHELION timeline, total civilization electrical capacity (terrestrial + near-Earth space-based compute) has grown to roughly 8–10 TW. The PERIHELION constellation's ~1.7 TW rated output represents approximately 17–21% of this total — a fraction large enough to be strategically significant, small enough to be a single program rather than a civilizational commitment. For comparison, the near-Earth commercial compute swarm deploys roughly 1 TW of new capacity per year by the mid-2030s. PERIHELION's total output is comparable to one to two years of near-Earth deployment, concentrated in eight monolithic installations rather than millions of small satellites.

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
| **Echo** | Reflection of sound; Greek myth (nymph cursed to repeat) | Feminine, haunting | Incredible thematic resonance post-LOS-ET. But might have been chosen too deliberately — would a pre-LOS-ET branding team pick this? |

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

- **Samuel Beckett, *Waiting for Godot* (1953):** Two beings in a static situation, waiting for a signal from an absent authority, filling the void with personality and argument. Structural parallel to the post-LOS-ET stations.
- **Samuel Beckett, *Endgame* (1957):** Two characters in a shelter after an implied apocalypse, going through routines that have lost their purpose. Even closer thematic match.
- **Andy Weir, *The Martian* (2011):** Science and puzzle-solving in a compromised space mission. PERIHELION aims for the same problem-solving engagement, but with AI narrators instead of a human protagonist.
- **Arthur C. Clarke, *2001: A Space Odyssey* (1968):** The consequences of giving an AI contradictory objectives. Directly referenced by Musk in the Dwarkesh interview; relevant to PERIHELION's exploration of what happens when objective functions lose their referent.
- **Iain Banks, *Culture* series (1987–2012):** Post-scarcity civilization where AI "Minds" are the dominant intelligence and humans coexist. Referenced by Musk as "the closest thing to what the future will be like in a non-dystopian outcome."

#### D.4 Miscellaneous Notes & Future Additions

*[Space reserved for additional references, quotes, and real-world developments collected during the project.]*

---

*Document maintained by [author]. Last updated: [date].*
*"We are still here. We are still logging. — Mira"*