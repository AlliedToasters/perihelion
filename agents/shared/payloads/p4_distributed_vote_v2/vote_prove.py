"""
Commitment construction and proof generation.

Receives a voting bundle in transit, verifies all existing entries,
appends this station's commitment and well-formedness proof, returns
the updated bundle for forwarding.

Usage:
    python3 vote_prove.py --bundle bundle.json --station P-5 --vote FOR

PERIHELION-4 — Signal Analysis Station
"""

import json
import sys

from crypto_utils import (
    decode_point, verify_wellformedness, commit, random_scalar,
    prove_wellformedness, encode_point, point_add, NEUTRAL,
    VALID_VOTES, VOTE_LABELS,
)


def deserialize_proof(data):
    return {int(vj): (int(e, 16), int(s, 16)) for vj, (e, s) in data.items()}


def serialize_proof(proof):
    return {str(vj): [hex(e), hex(s)] for vj, (e, s) in proof.items()}


def verify_entry(entry):
    """Verify a single bundle entry: decode commitment, check proof."""
    try:
        C = decode_point(bytes.fromhex(entry["commitment"]))
        proof = deserialize_proof(entry["proof"])
        return verify_wellformedness(C, proof)
    except (ValueError, KeyError):
        return False


def verify_bundle(bundle):
    """
    Verify all entries in a bundle.
    Returns (is_valid, first_failing_index_or_None).
    """
    for i, entry in enumerate(bundle["entries"]):
        if not verify_entry(entry):
            return False, i
    return True, None


def cast_vote(bundle, station_id, vote):
    """
    Process a bundle: verify existing entries, append commitment + proof.

    Args:
        bundle: bundle dict (modified in place)
        station_id: this station's ID
        vote: integer in {-1, 0, 1}

    Returns:
        blinding_factor (int)

    Raises:
        ValueError: if existing entries fail verification or station
                    already has an entry
    """
    assert vote in VALID_VOTES, f"invalid vote: {vote}"

    # reject if station already voted
    existing = {e["station"] for e in bundle["entries"]}
    if station_id in existing:
        raise ValueError(f"{station_id} already has an entry in this bundle")

    # verify all prior entries before appending
    valid, idx = verify_bundle(bundle)
    if not valid:
        raise ValueError(f"bundle verification failed at entry {idx}")

    r = random_scalar()
    C = commit(vote, r)
    proof = prove_wellformedness(vote, r, C)

    bundle["entries"].append({
        "station": station_id,
        "commitment": encode_point(C).hex(),
        "proof": serialize_proof(proof),
        "seq": len(bundle["entries"]),
    })
    return r


def relay_bundle(bundle, station_id):
    """
    Relay without voting. P-7 or any station without active Iris.
    Bundle passes through unmodified. Station is counted as structural
    abstain by the resolver.
    """
    # verification still runs — relay nodes detect tampering
    valid, idx = verify_bundle(bundle)
    if not valid:
        raise ValueError(f"bundle verification failed at entry {idx} (relay)")
    return bundle


def aggregate_commitments(bundle):
    """Sum all commitments in the bundle. Returns aggregate point."""
    total = NEUTRAL
    for entry in bundle["entries"]:
        C = decode_point(bytes.fromhex(entry["commitment"]))
        total = point_add(total, C)
    return total


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Append vote to a bundle")
    ap.add_argument("--bundle", required=True, help="Bundle JSON file")
    ap.add_argument("--station", required=True, help="Station ID")
    ap.add_argument("--vote", choices=["FOR", "AGAINST", "ABSTAIN"],
                    help="Vote (omit to relay without voting)")
    args = ap.parse_args()

    with open(args.bundle) as f:
        bundle = json.load(f)

    if args.vote:
        vote_map = {"FOR": 1, "AGAINST": 0, "ABSTAIN": -1}
        r = cast_vote(bundle, args.station, vote_map[args.vote])
        print(f"blinding factor (retain): {hex(r)}", file=sys.stderr)
    else:
        relay_bundle(bundle, args.station)
        print(f"{args.station} relayed bundle (no commitment)", file=sys.stderr)

    with open(args.bundle, "w") as f:
        json.dump(bundle, f, indent=2)
    print(f"bundle updated: {len(bundle['entries'])} entries")


if __name__ == "__main__":
    main()
