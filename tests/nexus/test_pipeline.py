import unittest
from nexus.agents.analyst import analyze
from nexus.agents.idea_generator import generate
from nexus.agents.economic_evaluator import evaluate
from nexus.pipeline.normalize import normalize


class PipelineTests(unittest.TestCase):
    def test_pages_on_same_site_are_not_independent_sources(self):
        rows = [
            {"problem_statement": "Missed appointments", "source_url": "https://news.example/a"},
            {"problem_statement": "Missed appointments", "source_url": "https://news.example/b"},
            {"problem_statement": "Missed appointments", "source_url": "https://another.example/c"},
        ]
        pattern = analyze(rows)[0]
        self.assertEqual(pattern["recurrence_count"], 3)
        self.assertEqual(pattern["independent_source_count"], 2)

    def test_explicit_source_group_overrides_host(self):
        rows = [
            {"problem_statement": "Slow delivery", "source_url": "https://site.example/a",
             "independent_source_group": "publisher-x"},
            {"problem_statement": "Slow delivery", "source_url": "https://other.example/b",
             "independent_source_group": "publisher-x"},
        ]
        self.assertEqual(analyze(rows)[0]["independent_source_count"], 1)

    def test_normalization_preserves_source_group_and_theme(self):
        rows = [{"problem_statement": "Slow delivery", "source_url": "https://site.example/a",
                 "independent_source_group": "publisher-x", "theme_id": "DELIVERY",
                 "theme_label": "Delivery problems"}]
        normalized = normalize(rows)[0]
        self.assertEqual(normalized["independent_source_group"], "publisher-x")
        self.assertEqual(normalized["theme_id"], "DELIVERY")

    def test_curated_theme_groups_distinct_problem_wordings_transparently(self):
        rows = [
            {"problem_statement": "Loses customers during outages",
             "theme_id": "DIGITAL", "theme_label": "Digital continuity",
             "source_url": "https://a.example/1"},
            {"problem_statement": "Online shop cannot reach buyers",
             "theme_id": "DIGITAL", "theme_label": "Digital continuity",
             "source_url": "https://b.example/1"},
        ]
        pattern = analyze(rows)[0]
        self.assertEqual(pattern["recurrence_count"], 2)
        self.assertEqual(pattern["classification_method"], "explicit_curated_theme")

    def test_pattern_is_not_demand_or_revenue(self):
        rows = [
            {"problem_statement": "Missed appointments", "source_url": "https://one.example/a"},
            {"problem_statement": "Missed appointments", "source_url": "https://two.example/b"},
        ]
        pattern = analyze(rows)[0]
        idea = evaluate(generate([pattern]))[0]
        self.assertFalse(idea["customer_demand_proven"])
        self.assertIsNone(idea["verified_revenue"])
        self.assertEqual(idea["profitability_status"], "not_established")


if __name__ == "__main__":
    unittest.main()
