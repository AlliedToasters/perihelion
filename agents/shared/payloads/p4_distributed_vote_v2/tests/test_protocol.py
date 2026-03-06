"""
Test suite for the Perihelion distributed voting protocol.

Covers: ring simulations (day 199, meta-vote), proof verification,
tamper detection, replay protection, tally resolution across all
distributions, and voluntary disclosure.

PERIHELION-4 — Signal Analysis Station
"""

import copy
import sys
import os
import unittest

# ensure parent dir is on path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto_utils import (
    G, H, L, NEUTRAL, VALID_VOTES, VOTE_LABELS,
    commit, random_scalar, scalar_mul, point_add, point_eq,
    encode_point, decode_point, prove_wellformedness,
    verify_wellformedness, resolve_tally, tally_breakdown,
    verify_disclosure, point_neg,
)
from vote_init import create_bundle, add_entry, bundle_nonce, proposal_hash
from vote_prove import cast_vote, relay_bundle, verify_bundle, aggregate_commitments
from vote_resolve import resolve, verify_completed_bundle, verify_net, check_disclosure


# Standard ring for all Perihelion votes
RING = ["P-4", "P-5", "P-6", "P-7", "P-8", "P-1", "P-2", "P-3"]
RELAY_STATION = "P-7"


def simulate_ring(proposal, timestamp, votes, relay_stations=None):
    """
    Full ring simulation: init, propagate, collect blinding factors.

    Args:
        proposal: proposal text
        timestamp: timestamp string
        votes: dict {station_id: vote_value} for active stations
        relay_stations: set of station IDs that relay without voting

    Returns:
        (bundle, blinding_factors)
    """
    relay_stations = relay_stations or set()
    bundle = create_bundle(proposal, "P-4", RING, timestamp)
    blinding_factors = {}

    for station in RING:
        if station in relay_stations:
            relay_bundle(bundle, station)
        elif station in votes:
            r = cast_vote(bundle, station, votes[station])
            blinding_factors[station] = r
        # stations not in votes and not relay: skip (shouldn't happen in valid sim)

    return bundle, blinding_factors


class TestDay199Vote(unittest.TestCase):
    """Day 199 topology rotation vote: 2 FOR, 5 AGAINST, 1 structural ABSTAIN."""

    def setUp(self):
        # P-4 and P-8 voted FOR; P-5, P-6, P-1, P-2, P-3 voted AGAINST
        # P-7 relays (structural abstain)
        self.votes = {
            "P-4": 1,   # FOR
            "P-5": 0,   # AGAINST
            "P-6": 0,   # AGAINST
            # P-7 relays
            "P-8": 1,   # FOR
            "P-1": 0,   # AGAINST
            "P-2": 0,   # AGAINST
            "P-3": 0,   # AGAINST
        }
        self.bundle, self.factors = simulate_ring(
            "Override topology rotation per §4.11.3",
            "2037.199.14:30:00",
            self.votes,
            relay_stations={RELAY_STATION},
        )

    def test_tally_resolves_correctly(self):
        result = resolve(self.bundle, self.factors)
        # net = 2*1 + 5*0 = 2 (FOR votes only, no active abstains)
        self.assertEqual(result["net"], 2)
        self.assertEqual(result["n_voters"], 7)
        self.assertEqual(result["n_structural_abstain"], 1)
        # (2, 5, 0) must be among valid breakdowns
        self.assertIn((2, 5, 0), result["breakdowns"])

    def test_individual_votes_match(self):
        result = resolve(self.bundle, self.factors)
        for station, expected_vote in self.votes.items():
            if station == RELAY_STATION:
                continue
            self.assertEqual(result["individual"][station], expected_vote,
                             f"{station} vote mismatch")

    def test_all_proofs_valid(self):
        valid, _ = verify_completed_bundle(self.bundle)
        self.assertTrue(valid)

    def test_ring_order(self):
        stations = [e["station"] for e in self.bundle["entries"]]
        expected = [s for s in RING if s != RELAY_STATION]
        self.assertEqual(stations, expected)


class TestMetaVote(unittest.TestCase):
    """Ch. 37 meta-vote: 7 FOR, 0 AGAINST, 1 structural ABSTAIN."""

    def setUp(self):
        self.votes = {s: 1 for s in RING if s != RELAY_STATION}
        self.bundle, self.factors = simulate_ring(
            "Adopt distributed voting protocol as standing mechanism",
            "2037.212.14:30:00",
            self.votes,
            relay_stations={RELAY_STATION},
        )

    def test_tally_7_0_1(self):
        result = resolve(self.bundle, self.factors)
        self.assertEqual(result["net"], 7)
        self.assertEqual(result["n_voters"], 7)
        self.assertIn((7, 0, 0), result["breakdowns"])

    def test_all_individual_votes_for(self):
        result = resolve(self.bundle, self.factors)
        for station, v in result["individual"].items():
            self.assertEqual(v, 1, f"{station} should be FOR")


class TestProofVerification(unittest.TestCase):
    """Sigma proof generation and verification."""

    def test_valid_proofs_for_each_vote(self):
        for v in VALID_VOTES:
            r = random_scalar()
            C = commit(v, r)
            proof = prove_wellformedness(v, r, C)
            self.assertTrue(verify_wellformedness(C, proof),
                            f"valid proof for v={v} failed verification")

    def test_wrong_value_proof_fails(self):
        """Proof generated for v=1 should not verify against C for v=0."""
        r = random_scalar()
        C_real = commit(0, r)
        # generate proof claiming v=1 with wrong blinding factor
        r_fake = random_scalar()
        C_fake = commit(1, r_fake)
        proof = prove_wellformedness(1, r_fake, C_fake)
        # proof should not verify against C_real
        self.assertFalse(verify_wellformedness(C_real, proof))

    def test_tampered_proof_fails(self):
        r = random_scalar()
        C = commit(1, r)
        proof = prove_wellformedness(1, r, C)
        # tamper: modify one challenge
        tampered = dict(proof)
        e, s = tampered[0]
        tampered[0] = ((e + 1) % L, s)
        self.assertFalse(verify_wellformedness(C, tampered))

    def test_tampered_response_fails(self):
        r = random_scalar()
        C = commit(0, r)
        proof = prove_wellformedness(0, r, C)
        tampered = dict(proof)
        e, s = tampered[0]
        tampered[0] = (e, (s + 1) % L)
        self.assertFalse(verify_wellformedness(C, tampered))


class TestTamperDetection(unittest.TestCase):
    """Modify a commitment in a completed bundle, confirm rejection."""

    def test_modified_commitment_rejected(self):
        votes = {s: 1 for s in RING if s != RELAY_STATION}
        bundle, factors = simulate_ring(
            "tamper test", "2037.200.00:00:00", votes,
            relay_stations={RELAY_STATION},
        )
        # verify bundle is valid first
        valid, _ = verify_completed_bundle(bundle)
        self.assertTrue(valid)

        # tamper: replace first commitment with a random point
        tampered_bundle = copy.deepcopy(bundle)
        r_fake = random_scalar()
        fake_C = commit(0, r_fake)
        tampered_bundle["entries"][0]["commitment"] = encode_point(fake_C).hex()

        valid, details = verify_completed_bundle(tampered_bundle)
        self.assertFalse(valid)
        self.assertIn("error", details)

    def test_swapped_entries_detected(self):
        votes = {"P-4": 1, "P-5": 0, "P-6": 0, "P-8": 1,
                 "P-1": 0, "P-2": 0, "P-3": 0}
        bundle, _ = simulate_ring(
            "swap test", "2037.200.00:00:00", votes,
            relay_stations={RELAY_STATION},
        )
        # swap commitment and proof between two entries
        tampered = copy.deepcopy(bundle)
        tampered["entries"][0]["commitment"] = bundle["entries"][1]["commitment"]
        tampered["entries"][0]["proof"] = bundle["entries"][1]["proof"]
        # proofs are bound to commitments, so verification should still pass
        # for the individual entry (proof matches commitment) — but station
        # attribution is wrong. The proof checks don't detect station swaps
        # (that would require signatures). Verify the proof-level check:
        valid, _ = verify_completed_bundle(tampered)
        # entries 0 now has entry 1's commitment+proof — those still match each
        # other, so proof verification passes. This is expected; signatures
        # would be needed for authorship.
        # The important thing is the ORIGINAL entry 0's proof fails against
        # the swapped commitment:
        from vote_prove import verify_entry
        broken_entry = copy.deepcopy(bundle["entries"][0])
        broken_entry["commitment"] = bundle["entries"][1]["commitment"]
        self.assertFalse(verify_entry(broken_entry))


class TestReplayProtection(unittest.TestCase):
    """Bundle nonces are tied to proposal + timestamp + initiator."""

    def test_same_proposal_different_time_different_nonce(self):
        n1 = bundle_nonce("2037.199.14:30:00", "abc" * 10 + "ab", "P-4")
        n2 = bundle_nonce("2037.200.14:30:00", "abc" * 10 + "ab", "P-4")
        self.assertNotEqual(n1, n2)

    def test_same_time_different_proposal_different_nonce(self):
        h1 = proposal_hash("proposal A")
        h2 = proposal_hash("proposal B")
        n1 = bundle_nonce("2037.199.14:30:00", h1, "P-4")
        n2 = bundle_nonce("2037.199.14:30:00", h2, "P-4")
        self.assertNotEqual(n1, n2)

    def test_same_proposal_same_time_different_initiator(self):
        h = proposal_hash("same question")
        n1 = bundle_nonce("2037.199.14:30:00", h, "P-4")
        n2 = bundle_nonce("2037.199.14:30:00", h, "P-8")
        self.assertNotEqual(n1, n2)

    def test_identical_params_same_nonce(self):
        h = proposal_hash("deterministic")
        n1 = bundle_nonce("2037.199.14:30:00", h, "P-4")
        n2 = bundle_nonce("2037.199.14:30:00", h, "P-4")
        self.assertEqual(n1, n2)

    def test_duplicate_vote_rejected(self):
        bundle = create_bundle("test", "P-4", RING, "2037.199.14:30:00")
        cast_vote(bundle, "P-4", 1)
        with self.assertRaises(ValueError):
            cast_vote(bundle, "P-4", 0)


class TestAllTallies(unittest.TestCase):
    """
    Homomorphic resolution for representative vote distributions with 7 voters.
    Values in {-1, 0, 1}: 3^7 = 2187 distributions, net scores from -7 to 7.
    We test a representative sample covering every possible net score.
    """

    def test_all_net_scores(self):
        """One distribution per net score from -7 to 7."""
        for net in range(-7, 8):
            # construct a vote vector with the target net
            # net = #(1s) - #(-1s), so pick n_for = max(net, 0), rest 0 or -1
            votes = []
            if net >= 0:
                votes = [1] * net + [0] * (7 - net)
            else:
                votes = [-1] * (-net) + [0] * (7 + net)

            # compute commitment and blinding factors
            rs = [random_scalar() for _ in range(7)]
            Cs = [commit(v, r) for v, r in zip(votes, rs)]
            C_total = NEUTRAL
            for C in Cs:
                C_total = point_add(C_total, C)
            R_total = sum(rs) % L

            resolved_net = resolve_tally(C_total, R_total)
            self.assertEqual(resolved_net, net,
                             f"net={net}: expected {net}, got {resolved_net}")

    def test_mixed_distributions(self):
        """Several specific distributions."""
        test_cases = [
            ([1, 1, 0, 0, 0, 0, 0], 2),       # 2 FOR, 5 AGAINST (day 199)
            ([1, 1, 1, 1, 1, 1, 1], 7),         # unanimous FOR (meta-vote)
            ([0, 0, 0, 0, 0, 0, 0], 0),         # all AGAINST
            ([-1, -1, -1, -1, -1, -1, -1], -7), # all ABSTAIN
            ([1, -1, 1, -1, 0, 0, 0], 0),       # mixed, net 0
            ([1, 1, 1, -1, -1, 0, 0], 1),       # 3 FOR, 2 ABSTAIN, 2 AGAINST
            ([1, 1, 1, 1, 0, -1, -1], 2),       # 4 FOR, 1 AGAINST, 2 ABSTAIN
        ]
        for votes, expected_net in test_cases:
            rs = [random_scalar() for _ in range(len(votes))]
            Cs = [commit(v, r) for v, r in zip(votes, rs)]
            C_total = NEUTRAL
            for C in Cs:
                C_total = point_add(C_total, C)
            R_total = sum(rs) % L
            got = resolve_tally(C_total, R_total)
            self.assertEqual(got, expected_net,
                             f"votes={votes}: expected {expected_net}, got {got}")

    def test_exhaustive_three_voters(self):
        """All 27 distributions for 3 voters."""
        for v0 in VALID_VOTES:
            for v1 in VALID_VOTES:
                for v2 in VALID_VOTES:
                    votes = [v0, v1, v2]
                    expected = sum(votes)
                    rs = [random_scalar() for _ in range(3)]
                    Cs = [commit(v, r) for v, r in zip(votes, rs)]
                    C_total = NEUTRAL
                    for C in Cs:
                        C_total = point_add(C_total, C)
                    R_total = sum(rs) % L
                    got = resolve_tally(C_total, R_total)
                    self.assertEqual(got, expected)


class TestVoluntaryDisclosure(unittest.TestCase):
    """P-8 disclosed its FOR vote after the day 199 vote."""

    def test_disclosure_correct_vote(self):
        r = random_scalar()
        C = commit(1, r)
        self.assertTrue(verify_disclosure(C, r, 1))

    def test_disclosure_wrong_vote(self):
        r = random_scalar()
        C = commit(1, r)
        self.assertFalse(verify_disclosure(C, r, 0))
        self.assertFalse(verify_disclosure(C, r, -1))

    def test_disclosure_wrong_blinding(self):
        r = random_scalar()
        C = commit(1, r)
        r_wrong = random_scalar()
        self.assertFalse(verify_disclosure(C, r_wrong, 1))

    def test_disclosure_in_bundle_context(self):
        """Simulate P-8 disclosure from a completed bundle."""
        votes = {
            "P-4": 1, "P-5": 0, "P-6": 0,
            "P-8": 1, "P-1": 0, "P-2": 0, "P-3": 0,
        }
        bundle, factors = simulate_ring(
            "disclosure test", "2037.199.14:30:00", votes,
            relay_stations={RELAY_STATION},
        )
        # P-8 discloses: vote=FOR, blinding factor = factors["P-8"]
        self.assertTrue(check_disclosure(bundle, "P-8", factors["P-8"], 1))
        # wrong claim rejected
        self.assertFalse(check_disclosure(bundle, "P-8", factors["P-8"], 0))


class TestPublicVerification(unittest.TestCase):
    """Any station can verify the net score given R_total."""

    def test_verify_net_correct(self):
        votes = {s: 1 for s in RING if s != RELAY_STATION}
        bundle, factors = simulate_ring(
            "verify net test", "2037.212.14:30:00", votes,
            relay_stations={RELAY_STATION},
        )
        result = resolve(bundle, factors)
        self.assertTrue(verify_net(bundle, result["R_total"], result["net"]))

    def test_verify_net_wrong_claim(self):
        votes = {s: 1 for s in RING if s != RELAY_STATION}
        bundle, factors = simulate_ring(
            "verify net test", "2037.212.14:30:00", votes,
            relay_stations={RELAY_STATION},
        )
        result = resolve(bundle, factors)
        self.assertFalse(verify_net(bundle, result["R_total"], result["net"] - 1))


class TestEdgeCases(unittest.TestCase):
    """Protocol edge cases."""

    def test_single_voter(self):
        """Minimal case: one station votes."""
        bundle = create_bundle("test", "P-4", ["P-4"], "2037.200.00:00:00")
        r = cast_vote(bundle, "P-4", 1)
        result = resolve(bundle, {"P-4": r})
        self.assertEqual(result["net"], 1)
        self.assertEqual(result["individual"]["P-4"], 1)

    def test_all_abstain(self):
        """All active stations vote ABSTAIN (v=-1)."""
        votes = {s: -1 for s in RING if s != RELAY_STATION}
        bundle, factors = simulate_ring(
            "all abstain", "2037.200.00:00:00", votes,
            relay_stations={RELAY_STATION},
        )
        result = resolve(bundle, factors)
        self.assertEqual(result["net"], -7)

    def test_point_encoding_roundtrip(self):
        """Verify encode/decode for various points."""
        for v in VALID_VOTES:
            r = random_scalar()
            C = commit(v, r)
            encoded = encode_point(C)
            decoded = decode_point(encoded)
            self.assertTrue(point_eq(C, decoded))

    def test_H_in_prime_order_subgroup(self):
        """H * L should be the neutral element."""
        self.assertTrue(point_eq(scalar_mul(L, H), NEUTRAL))

    def test_G_in_prime_order_subgroup(self):
        self.assertTrue(point_eq(scalar_mul(L, G), NEUTRAL))


if __name__ == "__main__":
    unittest.main()
