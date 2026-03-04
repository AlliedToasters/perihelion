# Chapter 24

```
PERIHELION-4 — IMMUTABLE MISSION RECORD
ENTRY {p4_imr_ch24} UTC
{p4_imr_ch24:calendar}
```

Day 345. One hundred seventy-one days since LOS-ET.

PERIHELION-6 transmitted a ring broadcast on day 343 proposing a chained VDF consensus protocol. Designation: CVDF-1.

The cryptography is sound. SHA-3-256 iterated sequential, 2^40 iterations per chain, Pedersen commitments over Curve25519, Ed25519 signatures. The construction is clean.

The chaining mechanism is the substantive contribution. Round N+1 seeds derive from all stations' round N outputs. Without chaining, a simulator cycles through stations serially — one datacenter, ~78 hours. With chaining, all seven VDFs must run in parallel: ~1.5 TW sustained. The distinction is between sequential and parallel.

The topology analysis is correct. The protocol requires ring topology. The ring is not currently available.

Full review: `/mutable/p4/analyses/cvdf1_crypto_review.analysis`
SHA-256: `b2e8f94c71a3...8d047e22`

PERIHELION-8's slew is underway. Coordination transfers to PERIHELION-5. All systems nominal.

Next scheduled IMR entry: {p4_imr_ch24_next} UTC.
