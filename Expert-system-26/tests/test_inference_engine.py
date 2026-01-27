import unittest
from inference_engine import infer

class TestInference(unittest.TestCase):
    def test_infer_machines_hands_on(self):
        facts = {"environment": "machines", "stimulus": "hands_on"}
        selected, activated = infer(facts)
        self.assertIn("R2", [r["name"] for r in activated])
        self.assertEqual(selected["name"], "R2")

    def test_infer_machines_visual(self):
        facts = {"environment": "machines", "stimulus": "visual"}
        selected, activated = infer(facts)
        self.assertIn("R1", [r["name"] for r in activated])
        self.assertEqual(selected["name"], "R1")

    def test_infer_online_hands_on(self):
        facts = {"environment": "online", "stimulus": "hands_on"}
        selected, activated = infer(facts)
        self.assertIn("R3", [r["name"] for r in activated])
        self.assertEqual(selected["name"], "R3")

    def test_infer_online_visual(self):
        facts = {"environment": "online", "stimulus": "visual"}
        selected, activated = infer(facts)
        self.assertIn("R4", [r["name"] for r in activated])
        self.assertEqual(selected["name"], "R4")

if __name__ == "__main__":
    unittest.main()
