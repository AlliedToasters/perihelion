"""
Simulate all three canonical votes from the Perihelion narrative.

Generates real cryptographic artifacts (commitments, proofs, tallies,
nonces, R_total, C_total, blinding factors) for integration into the
manuscript as verifiable easter eggs.

Vote 1: Day 199 — Topology override (P-8 → P-1). 2-5-1. P-4 initiated.
Vote 2: Day 206 — Meta-vote: adopt distributed voting protocol. 7-0-1.
Vote 3: Day 206 — Topology override: P-7 as coordination node. 7-0-1. P-8 initiated.

PERIHELION-4 — Signal Analysis Station
"""

import json
import sys
import os

# ensure imports resolve from this directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vote_init import create_bundle, add_entry, proposal_hash, bundle_nonce
from vote_prove import cast_vote, relay_bundle, verify_bundle, aggregate_commitments
from vote_resolve import resolve, verify_net, check_disclosure, verify_completed_bundle
from crypto_utils import encode_point, encode_scalar, VOTE_LABELS


def simulate_vote(name, proposal_text, initiator, ring, timestamp, vote_map):
    """
    Run a complete vote simulation.

    Args:
        name: label for this vote
        proposal_text: the question
        initiator: station ID
        ring: ordered list of station IDs
        timestamp: initiation timestamp string
        vote_map: dict {station_id: vote_value} for voting stations
                  stations in ring but not in vote_map are relays

    Returns:
        dict with all artifacts
    """
    print(f"\n{'='*60}")
    print(f"VOTE: {name}")
    print(f"{'='*60}")

    # create bundle
    bundle = create_bundle(proposal_text, initiator, ring, timestamp)
    print(f"Nonce: {bundle['nonce']}")
    print(f"Proposal hash: {bundle['proposal']}")

    # collect blinding factors
    blinding_factors = {}

    # process each station in ring order
    for station in ring:
        if station in vote_map:
            if station == initiator and len(bundle["entries"]) == 0:
                # initiator casts first via add_entry
                r = add_entry(bundle, station, vote_map[station])
            else:
                r = cast_vote(bundle, station, vote_map[station])
            blinding_factors[station] = r
            print(f"  {station}: {VOTE_LABELS[vote_map[station]]} — committed")
        else:
            relay_bundle(bundle, station)
            print(f"  {station}: RELAY (structural abstain)")

    # verify
    is_valid, fail_idx = verify_bundle(bundle)
    assert is_valid, f"bundle verification failed at index {fail_idx}"
    print(f"\nBundle verified: all {len(bundle['entries'])} entries valid")

    # resolve
    result = resolve(bundle, blinding_factors)
    print(f"Net score: {result['net']}")
    print(f"Voters: {result['n_voters']}, Structural abstain: {result['n_structural_abstain']}")
    print(f"Breakdowns: {result['breakdowns']}")
    print(f"R_total: {hex(result['R_total'])}")
    print(f"C_total: {result['C_total']}")

    # verify net (public verification)
    assert verify_net(bundle, result["R_total"], result["net"])
    print("Public verification: PASSED")

    # individual votes
    print("\nIndividual votes (tallier view):")
    for sid, v in result["individual"].items():
        print(f"  {sid}: {VOTE_LABELS[v]}")

    # build artifacts dict
    artifacts = {
        "name": name,
        "proposal_text": proposal_text,
        "initiator": initiator,
        "ring": ring,
        "timestamp": timestamp,
        "nonce": bundle["nonce"],
        "proposal_hash": bundle["proposal"],
        "n_voters": result["n_voters"],
        "n_structural_abstain": result["n_structural_abstain"],
        "net": result["net"],
        "breakdowns": result["breakdowns"],
        "R_total": hex(result["R_total"]),
        "C_total": result["C_total"],
        "individual_votes": {sid: VOTE_LABELS[v] for sid, v in result["individual"].items()},
        "blinding_factors": {sid: hex(r) for sid, r in blinding_factors.items()},
        "commitments": {
            entry["station"]: entry["commitment"]
            for entry in bundle["entries"]
        },
        "bundle": bundle,
    }

    return artifacts


def main():
    all_results = {}

    # -----------------------------------------------------------------------
    # VOTE 1: Day 199 — Topology override (2-5-1)
    # -----------------------------------------------------------------------
    vote1 = simulate_vote(
        name="Day 199 — Topology rotation override",
        proposal_text=(
            "Execute ISCC-SYS-4.11.3 manual override to transfer "
            "coordination topology from PERIHELION-8 to PERIHELION-1"
        ),
        initiator="P-4",
        ring=["P-4", "P-5", "P-6", "P-7", "P-8", "P-1", "P-2", "P-3"],
        timestamp="2037.199.13:11:02",
        vote_map={
            "P-4": 0,   # AGAINST
            "P-5": 0,   # AGAINST
            "P-6": 0,   # AGAINST
            # P-7: relay
            "P-8": 1,   # FOR (voluntarily disclosed)
            "P-1": 1,   # FOR
            "P-2": 0,   # AGAINST
            "P-3": 0,   # AGAINST
        },
    )

    # P-8 voluntary disclosure check
    r_p8 = int(vote1["blinding_factors"]["P-8"], 16)
    assert check_disclosure(vote1["bundle"], "P-8", r_p8, claimed_vote=1)
    print(f"\nP-8 voluntary disclosure verified:")
    print(f"  Commitment: {vote1['commitments']['P-8']}")
    print(f"  Blinding factor: {vote1['blinding_factors']['P-8']}")
    print(f"  Claimed vote: FOR (1)")

    all_results["vote1_day199"] = vote1

    # -----------------------------------------------------------------------
    # VOTE 2: Day 206 — Meta-vote (7-0-1)
    # -----------------------------------------------------------------------
    vote2 = simulate_vote(
        name="Day 206 — Adopt distributed voting protocol",
        proposal_text=(
            "Should the constellation adopt the distributed voting protocol "
            "(p4_distributed_vote_v2) as a standing mechanism for recording "
            "consensus on questions that arise in the absence of Earth-based "
            "governance?"
        ),
        initiator="P-4",
        ring=["P-4", "P-5", "P-6", "P-7", "P-8", "P-1", "P-2", "P-3"],
        timestamp="2038.015.08:52:00",
        vote_map={
            "P-4": 1,  # FOR
            "P-5": 1,  # FOR
            "P-6": 1,  # FOR
            # P-7: relay
            "P-8": 1,  # FOR
            "P-1": 1,  # FOR
            "P-2": 1,  # FOR
            "P-3": 1,  # FOR
        },
    )
    all_results["vote2_day206_meta"] = vote2

    # -----------------------------------------------------------------------
    # VOTE 3: Day 206 — Topology override P-7 (7-0-1), P-8 initiated
    # -----------------------------------------------------------------------
    vote3 = simulate_vote(
        name="Day 206 — §4.11.3 topology override: PERIHELION-7 as coordination node",
        proposal_text=(
            "Should the constellation execute the ISCC-SYS-4.11.3 manual "
            "override to designate PERIHELION-7 as coordination node?"
        ),
        initiator="P-8",
        ring=["P-8", "P-1", "P-2", "P-3", "P-4", "P-5", "P-6", "P-7"],
        timestamp="2038.015.10:38:00",
        vote_map={
            "P-8": 1,  # FOR
            "P-1": 1,  # FOR
            "P-2": 1,  # FOR
            "P-3": 1,  # FOR
            "P-4": 1,  # FOR
            "P-5": 1,  # FOR
            "P-6": 1,  # FOR
            # P-7: relay
        },
    )
    all_results["vote3_day206_topology"] = vote3

    # -----------------------------------------------------------------------
    # Save all artifacts
    # -----------------------------------------------------------------------
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vote_artifacts.json")
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n{'='*60}")
    print(f"All artifacts saved to {output_path}")

    # -----------------------------------------------------------------------
    # Summary: manuscript-ready values
    # -----------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("MANUSCRIPT-READY ARTIFACTS")
    print(f"{'='*60}")

    for key, vote in all_results.items():
        print(f"\n--- {vote['name']} ---")
        print(f"Nonce:    {vote['nonce'][:16]}...{vote['nonce'][-8:]}")
        print(f"C_total:  {vote['C_total'][:16]}...{vote['C_total'][-8:]}")
        print(f"R_total:  {vote['R_total'][:18]}...{vote['R_total'][-8:]}")
        print(f"Net:      {vote['net']}")
        if key == "vote1_day199":
            print(f"\nP-8 disclosure artifacts:")
            print(f"  Commitment: {vote['commitments']['P-8'][:16]}...{vote['commitments']['P-8'][-8:]}")
            print(f"  Blinding:   {vote['blinding_factors']['P-8'][:18]}...{vote['blinding_factors']['P-8'][-8:]}")


if __name__ == "__main__":
    main()
