import unittest
from conflict_resolution import resolve_conflict

class TestConflictResolution(unittest.TestCase):
    def setUp(self):
        self.rules = [
            {"name": "R1", "conditions": {"a": 1}, "action": "X", "priority": 1, "timestamp": 1},
            {"name": "R2", "conditions": {"a": 1, "b":2}, "action": "Y", "priority": 2, "timestamp": 2},
        ]

    def test_priority(self):
        selected = resolve_conflict(self.rules)
        self.assertEqual(selected['name'], "R2")

    def test_specificity(self):
        rules = [
            {"name": "R1", "conditions": {"a": 1}, "action": "X", "priority": 2, "timestamp": 1},
            {"name": "R2", "conditions": {"a": 1, "b":2}, "action": "Y", "priority": 2, "timestamp": 2},
        ]
        selected = resolve_conflict(rules)
        self.assertEqual(selected['name'], "R2")

if __name__ == "__main__":
    unittest.main()
