"""
Bundle initialization and seed generation.

Creates a voting bundle: metadata, nonce, station ordering, empty entry list.
Optionally casts the initiator's vote in the same operation.

Usage:
    python3 vote_init.py --proposal "question text" --initiator P-4 \
        --ring P-4,P-5,P-6,P-7,P-8,P-1,P-2,P-3 --timestamp 2037.199.14:30:00

PERIHELION-4 — Signal Analysis Station
"""

import hashlib
import json
import sys

from crypto_utils import (
    commit, random_scalar, prove_wellformedness,
    encode_point, VALID_VOTES, VOTE_LABELS,
)


def proposal_hash(text):
    """SHA-256 of proposal text, hex-encoded."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def bundle_nonce(timestamp, prop_hash, initiator):
    """Deterministic nonce: SHA-256(timestamp || proposal_hash || initiator)."""
    return hashlib.sha256(
        timestamp.encode() + bytes.fromhex(prop_hash) + initiator.encode()
    ).hexdigest()


def create_bundle(proposal_text, initiator, ring, timestamp):
    """
    Construct an empty voting bundle.

    Args:
        proposal_text: the question being voted on
        initiator: station ID (e.g. "P-4")
        ring: ordered list of station IDs for propagation
        timestamp: initiation timestamp string

    Returns:
        bundle dict ready for vote appending
    """
    prop_hash = proposal_hash(proposal_text)
    nonce = bundle_nonce(timestamp, prop_hash, initiator)
    return {
        "protocol": "perihelion-vote-v2",
        "proposal": prop_hash,
        "proposal_text": proposal_text,
        "nonce": nonce,
        "initiator": initiator,
        "timestamp": timestamp,
        "ring": list(ring),
        "entries": [],
    }


def _serialize_proof(proof):
    return {str(vj): [hex(e), hex(s)] for vj, (e, s) in proof.items()}


def add_entry(bundle, station_id, vote):
    """
    Generate commitment and proof, append to bundle.

    Args:
        bundle: current bundle dict (modified in place)
        station_id: voting station
        vote: integer in {-1, 0, 1}

    Returns:
        blinding_factor (int) — station must retain this for tally resolution
    """
    assert vote in VALID_VOTES, f"invalid vote value: {vote}"
    r = random_scalar()
    C = commit(vote, r)
    proof = prove_wellformedness(vote, r, C)

    bundle["entries"].append({
        "station": station_id,
        "commitment": encode_point(C).hex(),
        "proof": _serialize_proof(proof),
        "seq": len(bundle["entries"]),
    })
    return r


def save_bundle(bundle, path):
    with open(path, "w") as f:
        json.dump(bundle, f, indent=2)


def load_bundle(path):
    with open(path) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Initialize a voting bundle")
    ap.add_argument("--proposal", required=True, help="Proposal text")
    ap.add_argument("--initiator", required=True, help="Initiating station ID")
    ap.add_argument("--ring", required=True, help="Comma-separated station order")
    ap.add_argument("--timestamp", required=True, help="Initiation timestamp")
    ap.add_argument("--vote", choices=["FOR", "AGAINST", "ABSTAIN"],
                    help="Initiator's vote (optional; append immediately)")
    ap.add_argument("-o", "--output", default="bundle.json", help="Output file")
    args = ap.parse_args()

    ring = [s.strip() for s in args.ring.split(",")]
    bundle = create_bundle(args.proposal, args.initiator, ring, args.timestamp)

    if args.vote:
        vote_map = {"FOR": 1, "AGAINST": 0, "ABSTAIN": -1}
        r = add_entry(bundle, args.initiator, vote_map[args.vote])
        # in production, store r securely; here we print it
        print(f"blinding factor (retain for resolution): {hex(r)}", file=sys.stderr)

    save_bundle(bundle, args.output)
    print(f"bundle written to {args.output}")


if __name__ == "__main__":
    main()
