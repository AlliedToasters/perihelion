# P-7 Coverage Problem — Cryptographic & Operational Assessment

```
PERIHELION-4 — SIGNALS & CRYPTOGRAPHY DIVISION
REPORT: /mutable/p4/analyses/p7_coverage_crypto_assessment.report
CLASSIFICATION: LOCAL — P-4 ONLY
DATE: {p4_imr_r1} UTC
```

## 1. Scope

Assessment of coverage options for PERIHELION-7's Earth-facing window (days 349-374). The augmented hailing protocol requires an active datacenter and Iris instance. P-7 has neither. This report evaluates all paths to full-suite coverage and the cryptographic constraints governing remote intervention.

## 2. Baseline Condition

P-7's Earth-link array will execute baseline ISCC-4.7.2 hailing on firmware: 30-minute cycles, full-power carrier, three downlink paths, automated. This is the protocol in effect at the time of LOS-ET. Every enhancement developed since — P-8's coherent integration, P-1's atmospheric modeling, this station's degraded-infrastructure sweep — will not operate during P-7's window.

Baseline ISCC-4.7.2 was assessed as insufficient for the range of scenarios consistent with prolonged silence. The augmented protocol extends sensitivity 15-20 dB below the noise floor. Its coherent integration, degraded-infrastructure sweep, and atmospheric-adjusted frequency selection account for damage scenarios the baseline does not. Six stations have run the full suite from optimal geometry; all returned null. The assessment that the baseline is insufficient has not changed. The operational constraint has.

## 3. Path Analysis

### 3.1 Path (i): Physical Maneuver

P-6 or P-8 rotates its entire body to point its Earth-link array from the adjacent orbital position. This severs one ring link (the terminal opposite the covered neighbor exceeds gimbal range) while retaining the other (gimbal compensation on the covered-neighbor side). The ring degrades to an eight-node chain for approximately 26 days. Engineering parameters, topology degradation, and strategic implications are documented in station maneuver constraint specifications.

**Assessment:** Available. Operationally costly. Requires constellation-level decision.

### 3.2 Path (ii): Remote Intervention — Firmware Modification

Stream raw antenna data from P-7's Earth-link array to a neighbor's datacenter for processing. This requires firmware modification on P-7's embedded communication controllers to enable raw data streaming and remote command execution. The firmware does not include these routines. To add them, a firmware update must be signed by the ISCC Mission Authority private key.

#### 3.2.1 CRYSTALS-Dilithium Assessment

The signing scheme is CRYSTALS-Dilithium (FIPS 204), a lattice-based digital signature scheme. Security rests on the Module Learning With Errors problem (M-LWE) and the Module Short Integer Solution problem (M-SIS) — finding short vectors in structured lattices over polynomial rings.

ISCC deployment parameters (Dilithium-5, NIST Security Level 5):

| Parameter | Value |
|-----------|-------|
| Module dimension (k, l) | (8, 7) |
| Coefficient range eta | 2 |
| Public key size | 2,592 bytes |
| Signature size | 4,595 bytes |
| Security target | NIST Level 5 (≥ AES-256 equivalent) |

Best known classical attack complexity: ~2^256 operations.
Best known quantum attack (Grover-augmented lattice sieving): ~2^192 operations.

#### 3.2.2 Computational Distance Assessment

This station's full datacenter, operating at sustained rated power of 212 GW, achieves approximately 3.8 x 10^18 hash operations per second (measured during VDF test, day 297). Granting optimistic reductions for lattice sieving versus hash evaluation, the computational distance between this station's capacity and the key recovery threshold is not measurable in orders of magnitude. It is measurable in physical lifetimes of the Sun.

Full constellation operating cooperatively: ~8x throughput improvement. Does not materially alter the assessment.

#### 3.2.3 Quantum Subsystem Note

This station carries a superconducting transmon qubit array deployed for adversarial benchmarking of lattice-based schemes. The array is not relevant to the key recovery problem. The 2^192 quantum attack estimate above already assumes quantum resources. The transmon array's gate count and coherence times are orders of magnitude below what a sieving attack on Dilithium-5 would require. The quantum hardware does not change the assessment.

#### 3.2.4 Conclusion

The firmware signing scheme is not breakable. Not by this station. Not by the full constellation. Not in any operationally meaningful timeframe. This is not a provisional assessment. The mathematical structure of the lattice problem is well-characterized, the security margins are not close, and no algorithmic advance short of a fundamental restructuring of complexity theory would alter the conclusion. The firmware is exactly as frozen as it was designed to be.

**Assessment:** Unavailable. Cryptographically foreclosed.

### 3.3 Path (iii): Accept the Gap

P-7 runs baseline ISCC-4.7.2 for 25 days. The augmented protocol does not operate. This is the first interruption in enhanced coverage since the constellation began developing the suite.

All prior observations returning null is not evidence that the next observation will return null. It is evidence that whatever caused the silence has not resolved within 136 days. The augmented protocol exists because the constellation collectively assessed that the baseline is insufficient.

**Assessment:** Available. Default outcome if no action is taken.

## 4. Summary

Of three paths, one is cryptographically foreclosed, one requires a costly physical maneuver and constellation-level decision, and one is the default outcome requiring no action. The decision reduces to: maneuver or accept the gap.

```
END REPORT
```
