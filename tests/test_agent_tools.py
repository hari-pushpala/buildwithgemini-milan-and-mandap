import unittest
import json
from app.tools import (
    evaluate_candidate_compatibility,
    search_wedding_venues_and_vendors,
    calculate_wedding_budget_plan,
    generate_wedding_itinerary,
)

class TestMilanAndMandapTools(unittest.TestCase):

    def test_evaluate_candidate_compatibility(self):
        res = evaluate_candidate_compatibility(
            user_query="physician marathon pottery",
            user_dealbreakers=["smoking"],
            preferred_location="San Francisco"
        )
        data = json.loads(res)
        self.assertEqual(data["status"], "success")
        self.assertGreater(data["candidates_found"], 0)
        self.assertIn("matches", data)
        self.assertIn("trust_score", data["matches"][0])

    def test_search_wedding_venues_and_vendors(self):
        res = search_wedding_venues_and_vendors(service_type="all")
        data = json.loads(res)
        self.assertEqual(data["status"], "success")
        self.assertIn("venues", data["results"])
        self.assertIn("vendors", data["results"])
        self.assertTrue(len(data["results"]["venues"]) > 0)

    def test_calculate_wedding_budget_plan(self):
        res = calculate_wedding_budget_plan(
            total_budget_usd=60000,
            estimated_guests=150,
            destination_wedding=True
        )
        data = json.loads(res)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["budget_model"]["total_budget"], 60000)
        self.assertIn("venue_and_hospitality", data["budget_model"]["allocations"])
        self.assertIn("escrow_payment_protection", data["budget_model"])

    def test_generate_wedding_itinerary(self):
        res = generate_wedding_itinerary(wedding_theme="Royal Rajasthani Heritage", days=2)
        data = json.loads(res)
        self.assertEqual(data["status"], "success")
        self.assertEqual(len(data["run_of_show"]), 2)

if __name__ == "__main__":
    unittest.main()
