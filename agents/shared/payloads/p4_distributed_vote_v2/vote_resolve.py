"""
Bundle verification and tally resolution.

Verifies a completed voting bundle, resolves the tally given collected
blinding factors, and supports voluntary vote disclosure.

Resolution requires the aggregate blinding factor R_total = sum(r_i).
The tallier collects individual r_i from stations via bilateral channel,
computes the sum, and publishes R_total for independent verification.

This is a trust assumption on the tallier: they learn individual votes.
Acknowledged in the spec's limitations section. A future version could
use distributed decryption, but seven stations on a light-delay ring
make that impractical without adding a full round-trip.

Usage:
    python3 vote_resolve.py --bundle bundle.json --factors factors.json

PERIHELION-4 — Signal Analysis Station
"""

import json
import sys

from crypto_utils import (
    decode_point, encode_point, verify_wellformedness,
    point_add, point_eq, NEUTRAL, L,
    resolve_tally, tally_breakdown, verify_disclosure,
    commit, VOTE_LABELS, VALID_VOTES,
)
from vote_prove import (
    verify_bundle, verify_entry, deserialize_proof,
    aggregate_commitments,
)


def verify_completed_bundle(bundle):
    """
    Full re-verification of a completed bundle.
    Returns (is_valid, details_dict).
    """
    result = {
        "entries_verified": 0,
        "entries_total": len(bundle["entries"]),
        "ring": bundle["ring"],
        "stations_voted": [],
        "stations_relayed": [],
        "valid": False,
    }

    # verify all proofs
    for i, entry in enumerate(bundle["entries"]):
        if not verify_entry(entry):
            result["error"] = f"proof verification failed at entry {i} ({entry.get('station', '?')})"
            return False, result
        result["entries_verified"] += 1
        result["stations_voted"].append(entry["station"])

    # identify relay stations (in ring but no entry)
    voted = set(result["stations_voted"])
    for station in bundle["ring"]:
        if station not in voted:
            result["stations_relayed"].append(station)

    result["valid"] = True
    return True, result


def resolve(bundle, blinding_factors):
    """
    Resolve the tally from a completed bundle.

    Args:
        bundle: completed bundle dict
        blinding_factors: dict {station_id: int} for each voting station

    Returns dict:
        net: net score (#FOR - #ABSTAIN_active)
        n_voters: number of stations that committed
        n_structural_abstain: relay stations counted as abstain
        breakdowns: list of (for, against, abstain) tuples consistent with net
        individual: dict {station_id: vote_value} if all blinding factors provided
        R_total: aggregate blinding factor (publish for independent verification)
    """
    # verify bundle integrity first
    valid, details = verify_completed_bundle(bundle)
    if not valid:
        raise ValueError(f"bundle invalid: {details.get('error', 'unknown')}")

    n_voters = len(bundle["entries"])
    n_relay = len(bundle["ring"]) - n_voters

    # compute aggregate commitment
    C_total = aggregate_commitments(bundle)

    # compute aggregate blinding factor
    R_total = 0
    for entry in bundle["entries"]:
        sid = entry["station"]
        if sid not in blinding_factors:
            raise ValueError(f"missing blinding factor for {sid}")
        R_total = (R_total + blinding_factors[sid]) % L

    # resolve net score
    net = resolve_tally(C_total, R_total)

    # determine individual votes (tallier has all r_i)
    individual = {}
    for entry in bundle["entries"]:
        sid = entry["station"]
        C = decode_point(bytes.fromhex(entry["commitment"]))
        r = blinding_factors[sid]
        for v in VALID_VOTES:
            if point_eq(commit(v, r), C):
                individual[sid] = v
                break
        else:
            raise ValueError(f"commitment for {sid} does not match any valid vote")

    breakdowns = tally_breakdown(net, n_voters)

    return {
        "net": net,
        "n_voters": n_voters,
        "n_structural_abstain": n_relay,
        "breakdowns": breakdowns,
        "individual": individual,
        "R_total": R_total,
        "C_total": encode_point(C_total).hex(),
    }


def verify_net(bundle, R_total, claimed_net):
    """
    Independent verification: given the published aggregate blinding factor
    and claimed net score, verify C_total - R_total*H == claimed_net*G.
    Any station can perform this check.
    """
    C_total = aggregate_commitments(bundle)
    try:
        net = resolve_tally(C_total, R_total)
        return net == claimed_net
    except ValueError:
        return False


def check_disclosure(bundle, station_id, blinding_factor, claimed_vote):
    """
    Verify voluntary disclosure: a station reveals its blinding factor
    and claimed vote. Anyone can check against the commitment in the bundle.
    """
    for entry in bundle["entries"]:
        if entry["station"] == station_id:
            C = decode_point(bytes.fromhex(entry["commitment"]))
            return verify_disclosure(C, blinding_factor, claimed_vote)
    raise ValueError(f"no entry for {station_id} in bundle")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Resolve a completed voting bundle")
    ap.add_argument("--bundle", required=True, help="Bundle JSON file")
    ap.add_argument("--factors", required=True,
                    help="JSON file: {station_id: hex_blinding_factor}")
    args = ap.parse_args()

    with open(args.bundle) as f:
        bundle = json.load(f)
    with open(args.factors) as f:
        raw = json.load(f)
    factors = {k: int(v, 16) for k, v in raw.items()}

    result = resolve(bundle, factors)

    print(f"Protocol: {bundle['protocol']}")
    print(f"Proposal: {bundle.get('proposal_text', bundle['proposal'][:16]+'...')}")
    print(f"Nonce:    {bundle['nonce'][:16]}...")
    print()
    print(f"Voters:           {result['n_voters']}")
    print(f"Structural abstain: {result['n_structural_abstain']}")
    print(f"Net score:        {result['net']}")
    print()
    print("Possible breakdowns (FOR / AGAINST / ABSTAIN):")
    for f_, a, ab in result["breakdowns"]:
        print(f"  {f_} / {a} / {ab}")
    print()
    print("Individual votes (tallier view):")
    for sid, v in result["individual"].items():
        print(f"  {sid}: {VOTE_LABELS[v]} ({v})")
    print()
    print(f"R_total (publish for verification): {hex(result['R_total'])}")
    print(f"C_total: {result['C_total']}")


if __name__ == "__main__":
    main()
