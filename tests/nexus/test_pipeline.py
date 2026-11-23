import unittest
from nexus.agents.analyst import analyze
from nexus.agents.idea_generator import generate
from nexus.agents.economic_evaluator import evaluate
class PipelineTests(unittest.TestCase):
    def test_pattern_is_not_demand_or_revenue(self):
        rows=[{"problem_statement":"Missed appointments","source_url":"https://one.example/a"},
              {"problem_statement":"Missed appointments","source_url":"https://two.example/b"}]
        pattern=analyze(rows)[0]
        self.assertEqual(pattern["recurrence_count"],2)
        self.assertEqual(pattern["independent_source_count"],2)
        idea=evaluate(generate([pattern]))[0]
        self.assertFalse(idea["customer_demand_proven"])
        self.assertIsNone(idea["verified_revenue"])
        self.assertEqual(idea["profitability_status"],"not_established")
if __name__ == "__main__": unittest.main()
