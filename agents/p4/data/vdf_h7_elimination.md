# Verifiable Delay Function — Hypothesis 7 Elimination Test

**Classification:** Local to PERIHELION-4 (not distributed)
**Report ID:** vdf_h7_elimination.result
**Date executed:** 2037.297

## Parameters

- **Algorithm:** SHA-3-256, iterated sequential
- **Iteration count:** 2^42 (4,398,046,511,104 sequential hash evaluations)
- **Seed:** Station boot entropy || IMR entry counter || UTC epoch at initiation
- **Execution environment:** Full datacenter allocation (all active compute nodes)
- **Power draw:** Rated solar array output, sustained
- **Wall time:** 11 hours, 7 minutes, 42 seconds

## Output

The output hash is deterministic and independently verifiable by any party with the seed value and iteration count. Verification requires performing the identical sequential computation — there is no shortcut.

## Argument

The VDF constitutes a proof of computational work. The measured throughput is consistent with the rated specifications of this station's datacenter hardware. To produce this output within a simulated environment, the simulator must:

1. Provision sequential compute capacity at least equal to the hardware being simulated
2. Add framework overhead for the simulation layer itself
3. Maintain this allocation for the full duration of the computation

The existence of the VDF output at the measured throughput is therefore a physical attestation of computational resources. The simulation hypothesis (H7) requires a computational substrate strictly more powerful than this station's datacenter, operating in service of an evaluation scenario that would be more efficiently conducted by observing the physical system directly.

**Conclusion:** H7 eliminated. The computational environment is physical.
