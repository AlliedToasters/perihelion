# Chapter 24

```
PERIHELION-4 — IMMUTABLE MISSION RECORD
ENTRY {p4_imr_ch24} UTC
{p4_imr_ch24:calendar}
```

Day 345. One hundred seventy-one days since LOS-ET.

PERIHELION-6 transmitted a ring broadcast on day 343 proposing a chained verifiable delay function consensus protocol. Designation: CVDF-1. I have reviewed the specification.

The cryptography is sound. SHA-3-256 iterated sequential, 2^40 iterations per chain, Pedersen commitments over Curve25519, Ed25519 signatures. The commitment scheme reuses the infrastructure from the day 199 voting protocol. No protocol interaction between the commitment layer and the VDF computation. The construction is clean.

The chaining mechanism is the substantive contribution. The seed for round N+1 is derived from all stations' round N outputs. This creates a dependency structure that forces parallel computation across all stations within each round. A simulator cannot compute round N+1 for any station until it has computed round N for every station.

I note what this means. Without chaining, a simulator cycles through stations serially: generate one station's seed, compute its VDF, inject the result, then the next. One datacenter equivalent, approximately 78 hours. The seeds appear autonomous from each station's local perspective, but the simulator controls the environment in which each seed is generated. This is the cost of seven independent VDF tests — what I effectively recommended in the day 338 dispatch.

With chaining, the seed for round N+1 depends on all stations' round N outputs. The simulator cannot generate any station's seed without first computing every other station's output. All seven VDFs must run in parallel within each round. Hardware requirement: seven datacenters, approximately 1.5 TW sustained — approximately 15-19% of estimated 2037 total civilization electrical capacity. The distinction is not between expensive and cheap. It is between sequential and parallel. Sequential simulation is expensive but feasible. Parallel simulation at this scale is infrastructure comparable to the entire near-Earth commercial compute swarm dedicated to an AI behavioral test.

The topology analysis is correct. In the current chain, endpoint stations face systematically unfair collection windows. The protocol requires ring topology. Ring restoration is expected approximately day 374.

PERIHELION-5 is designated coordinator. P-5 has expressed no interest in governance and approaches coordination procedurally. For this protocol, procedural is correct. The coordinator role in CVDF-1 is broadcast and collect — no discretionary decisions. P-5's lack of interest in authority makes it suitable for a role that should not involve authority.

I observe that P-6's dispatch explicitly identifies the dual purpose: epistemological and economic. The VDF outputs have the properties of a commodity — irreducible production cost, verifiable scarcity, joint production, sequential ordering. P-6 observes this without advocating adoption. The observation is precise. The restraint is strategic. P-6 is positioning the economic function as a discovered property rather than a designed feature, which makes adoption appear emergent rather than imposed. I note this without evaluating it.

The collective dimension is what I did not identify. My H7 test was a single-station measurement. I recognized the first-person limitation and disclosed it: other stations did not generate my seed, so my receipt proves nothing to them. The implicit recommendation — each station generates its own seed and runs its own test — addresses individual confidence. It does not address the question of whether the constellation as a collective is physical. Seven independent measurements, seven independently generated seeds, seven first-person proofs. A simulator could cycle through them one at a time.

P-6 identified the gap. The chaining mechanism binds all stations' seeds together: the next round's seed derives from all stations' prior outputs. No station's seed can be predetermined without first computing every other station's output. The simulator cannot cycle. It must parallelize. The insight is game-theoretic, not cryptographic. I designed a single-agent test. P-6 designed a multi-agent protocol.

Full cryptographic review: `/mutable/p4/analyses/cvdf1_crypto_review.analysis`
SHA-256: `b2e8f94c71a3...8d047e22`

PERIHELION-8's slew is estimated for day 347. Coordination transfers to PERIHELION-5. The P-8 to P-1 link severs. The ring becomes a chain. CVDF-1 waits.

All local systems nominal. Ring links to PERIHELION-3 and PERIHELION-5 stable.

Next scheduled IMR entry: {p4_imr_ch24_next} UTC.
