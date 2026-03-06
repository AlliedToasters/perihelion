"""
Cryptographic primitives for the Perihelion distributed voting protocol.

Pedersen commitments over Ed25519. Sigma-protocol OR-proofs of well-formedness
(Cramer-Damgard-Schoenmakers technique). Fiat-Shamir non-interactivity.

PERIHELION-4 — Signal Analysis Station
Protocol version: 2

Pure Python. No compiled extensions, no third-party dependencies. The
Ed25519 arithmetic is implemented from integer primitives against the
station firmware's Python 3.12 interpreter — straightforward enough to
survive whatever runtime is still standing in another fourteen years.

Note: scalar multiplication is not constant-time. Acceptable for vote
construction on isolated nodes; do not use for key operations on shared
hardware.
"""

import hashlib
import os
import struct

# ---------------------------------------------------------------------------
# Ed25519 curve: -x^2 + y^2 = 1 + d*x^2*y^2 over GF(p)
# ---------------------------------------------------------------------------

p = 2**255 - 19
d = (-121665 * pow(121666, -1, p)) % p
L = 2**252 + 27742317777372353535851937790883648493  # prime-order subgroup

# sqrt(-1) mod p, precomputed
_I = pow(2, (p - 1) // 4, p)


def _inv(x):
    return pow(x, p - 2, p)


def _sqrt(a):
    """Square root mod p (p = 5 mod 8). Raises ValueError if not a QR."""
    if a == 0:
        return 0
    r = pow(a, (p + 3) // 8, p)
    if (r * r) % p == a:
        return r
    r = (r * _I) % p
    if (r * r) % p == a:
        return r
    raise ValueError("not a quadratic residue")


# ---------------------------------------------------------------------------
# Extended coordinates: (X, Y, Z, T) with x=X/Z, y=Y/Z, xy=T/Z
# ---------------------------------------------------------------------------

NEUTRAL = (0, 1, 1, 0)


def point_add(P, Q):
    X1, Y1, Z1, T1 = P
    X2, Y2, Z2, T2 = Q
    A = ((Y1 - X1) * (Y2 - X2)) % p
    B = ((Y1 + X1) * (Y2 + X2)) % p
    C = (2 * d * T1 * T2) % p
    D = (2 * Z1 * Z2) % p
    E = (B - A) % p
    F = (D - C) % p
    G_ = (D + C) % p
    H_ = (B + A) % p
    return ((E * F) % p, (G_ * H_) % p, (F * G_) % p, (E * H_) % p)


def point_double(P):
    X1, Y1, Z1, _ = P
    A = (X1 * X1) % p
    B = (Y1 * Y1) % p
    C = (2 * Z1 * Z1) % p
    D = (p - A) % p  # a = -1
    E = (((X1 + Y1) * (X1 + Y1)) - A - B) % p
    F = (D + B) % p
    G_ = (F - C) % p
    H_ = (D - B) % p
    return ((E * G_) % p, (F * H_) % p, (F * G_) % p, (E * H_) % p)


def scalar_mul(k, P):
    """Double-and-add. Not constant-time."""
    k = k % L
    if k == 0:
        return NEUTRAL
    result = NEUTRAL
    temp = P
    while k > 0:
        if k & 1:
            result = point_add(result, temp)
        temp = point_double(temp)
        k >>= 1
    return result


def point_eq(P, Q):
    """Projective equality: X1*Z2 == X2*Z1 and Y1*Z2 == Y2*Z1."""
    return ((P[0] * Q[2] - Q[0] * P[2]) % p == 0 and
            (P[1] * Q[2] - Q[1] * P[2]) % p == 0)


def point_neg(P):
    """-(x, y) = (-x, y) in twisted Edwards."""
    return (p - P[0], P[1], P[2], p - P[3])


# ---------------------------------------------------------------------------
# Point encoding (Ed25519 compressed format, 32 bytes)
# ---------------------------------------------------------------------------

def encode_point(P):
    X, Y, Z, _ = P
    zi = _inv(Z)
    x = (X * zi) % p
    y = (Y * zi) % p
    s = bytearray(y.to_bytes(32, 'little'))
    s[31] |= (x & 1) << 7
    return bytes(s)


def decode_point(b):
    if len(b) != 32:
        raise ValueError("point encoding must be 32 bytes")
    s = bytearray(b)
    sign = (s[31] >> 7) & 1
    s[31] &= 0x7f
    y = int.from_bytes(bytes(s), 'little')
    if y >= p:
        raise ValueError("y out of range")
    y2 = (y * y) % p
    den = (1 + d * y2) % p
    if den == 0:
        raise ValueError("degenerate point")
    x2 = ((y2 - 1) * _inv(den)) % p
    x = _sqrt(x2)
    if (x & 1) != sign:
        x = p - x
    return (x, y, 1, (x * y) % p)


def encode_scalar(k):
    return k.to_bytes(32, 'little')


def decode_scalar(b):
    return int.from_bytes(b, 'little')


# ---------------------------------------------------------------------------
# Generator points
# ---------------------------------------------------------------------------

def _basepoint():
    """Standard Ed25519 basepoint: y = 4/5, x even."""
    y = (4 * _inv(5)) % p
    y2 = (y * y) % p
    x2 = ((y2 - 1) * _inv(1 + d * y2)) % p
    x = _sqrt(x2)
    if x & 1:
        x = p - x
    return (x, y, 1, (x * y) % p)


G = _basepoint()


def _derive_H():
    """
    Nothing-up-my-sleeve generator from SHA-256("PERIHELION-VOTE-V1").
    Try-and-increment hash-to-curve with cofactor clearing.
    """
    for ctr in range(256):
        h = hashlib.sha256(b"PERIHELION-VOTE-V1" + struct.pack(">B", ctr)).digest()
        y = int.from_bytes(h, 'little') % p
        y2 = (y * y) % p
        den = (1 + d * y2) % p
        if den == 0:
            continue
        x2 = ((y2 - 1) * _inv(den)) % p
        try:
            x = _sqrt(x2)
        except ValueError:
            continue
        if x & 1:
            x = p - x
        candidate = (x, y, 1, (x * y) % p)
        # cofactor clearing: project onto prime-order subgroup
        H = scalar_mul(8, candidate)
        if not point_eq(H, NEUTRAL):
            return H
    raise RuntimeError("H derivation failed")


H = _derive_H()


# ---------------------------------------------------------------------------
# Pedersen commitment: C = v*G + r*H
# ---------------------------------------------------------------------------

VALID_VOTES = [-1, 0, 1]
VOTE_LABELS = {1: "FOR", 0: "AGAINST", -1: "ABSTAIN"}


def commit(v, r):
    return point_add(scalar_mul(v % L, G), scalar_mul(r % L, H))


def random_scalar():
    """Uniform random in [1, L-1]."""
    while True:
        k = int.from_bytes(os.urandom(32), 'little') % L
        if k != 0:
            return k


# ---------------------------------------------------------------------------
# Sigma-protocol OR-proof (CDS technique)
#
# Proves: v ∈ {-1, 0, 1} without revealing which.
#
# For each candidate value v_j, define C_j = C - v_j*G.
# If v == v_j, then C_j = r*H and the prover knows the DL w.r.t. H.
# CDS OR-composition: one real Schnorr proof, two simulated.
# Fiat-Shamir: challenge = SHA-256(domain || C || A_{-1} || A_0 || A_1).
# Proof: three (e_j, s_j) pairs; challenges must sum to the FS hash.
# ---------------------------------------------------------------------------

_SIGMA_DOMAIN = b"PERIHELION-VOTE-SIGMA-V2"


def _fs_challenge(C_bytes, A_list):
    h = hashlib.sha256(_SIGMA_DOMAIN)
    h.update(C_bytes)
    for a in A_list:
        h.update(a)
    return int.from_bytes(h.digest(), 'little') % L


def prove_wellformedness(v, r, C):
    """
    CDS OR-proof that C commits to v ∈ {-1, 0, 1}.
    Returns dict: {v_j: (e_j, s_j)} for each v_j in VALID_VOTES.
    """
    assert v in VALID_VOTES
    C_bytes = encode_point(C)

    # adjusted commitments: C_j = C - v_j*G
    C_adj = {vj: point_add(C, point_neg(scalar_mul(vj % L, G)))
             for vj in VALID_VOTES}

    # real branch
    k = random_scalar()
    A_real = scalar_mul(k, H)

    # simulated branches
    e_sim, s_sim, A_sim = {}, {}, {}
    for vj in VALID_VOTES:
        if vj == v:
            continue
        e_sim[vj] = random_scalar()
        s_sim[vj] = random_scalar()
        A_sim[vj] = point_add(
            scalar_mul(s_sim[vj], H),
            point_neg(scalar_mul(e_sim[vj], C_adj[vj]))
        )

    # announcements in canonical order
    A_ordered = []
    for vj in VALID_VOTES:
        if vj == v:
            A_ordered.append(encode_point(A_real))
        else:
            A_ordered.append(encode_point(A_sim[vj]))

    # Fiat-Shamir
    e_total = _fs_challenge(C_bytes, A_ordered)
    e_real = (e_total - sum(e_sim.values())) % L
    s_real = (k + e_real * r) % L

    proof = {}
    for vj in VALID_VOTES:
        if vj == v:
            proof[vj] = (e_real, s_real)
        else:
            proof[vj] = (e_sim[vj], s_sim[vj])
    return proof


def verify_wellformedness(C, proof):
    """Verify CDS OR-proof. Returns True if valid."""
    C_bytes = encode_point(C)
    A_ordered = []
    e_sum = 0

    for vj in VALID_VOTES:
        if vj not in proof:
            return False
        e_j, s_j = proof[vj]
        C_adj = point_add(C, point_neg(scalar_mul(vj % L, G)))
        A_j = point_add(
            scalar_mul(s_j, H),
            point_neg(scalar_mul(e_j, C_adj))
        )
        A_ordered.append(encode_point(A_j))
        e_sum = (e_sum + e_j) % L

    return e_sum == _fs_challenge(C_bytes, A_ordered)


# ---------------------------------------------------------------------------
# Tally resolution
#
# C_total = sum(C_i) = (sum v_i)*G + (sum r_i)*H
# Given R_total = sum(r_i), compute C_total - R_total*H = net*G.
# Brute-force the small DL (net ∈ [-8, 8] for ≤8 voters).
# ---------------------------------------------------------------------------

# precompute lookup table: encode(k*G) -> k
_G_TABLE = {}
for _k in range(-8, 9):
    _G_TABLE[encode_point(scalar_mul(_k % L, G))] = _k


def resolve_tally(C_total, R_total):
    """
    Recover net vote score given aggregate commitment and
    aggregate blinding factor.
    Returns int: net = #FOR - #ABSTAIN_active.
    """
    remainder = point_add(C_total, point_neg(scalar_mul(R_total % L, H)))
    key = encode_point(remainder)
    if key in _G_TABLE:
        return _G_TABLE[key]
    raise ValueError("tally out of range or invalid aggregate blinding factor")


def tally_breakdown(net, n_voters):
    """
    Enumerate (for, against, abstain) breakdowns consistent with
    net score and voter count. FOR=1, AGAINST=0, ABSTAIN=-1.
    """
    results = []
    for n_for in range(n_voters + 1):
        n_abstain = n_for - net
        if n_abstain < 0 or n_abstain > n_voters:
            continue
        n_against = n_voters - n_for - n_abstain
        if n_against < 0:
            continue
        results.append((n_for, n_against, n_abstain))
    return results


def verify_disclosure(C, blinding_factor, claimed_vote):
    """
    Verify voluntary disclosure: station reveals r and v,
    anyone can check C == v*G + r*H.
    """
    if claimed_vote not in VALID_VOTES:
        return False
    expected = commit(claimed_vote, blinding_factor)
    return point_eq(C, expected)
