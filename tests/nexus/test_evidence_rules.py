import unittest
from nexus.agents.explorer import collect
from nexus.agents.inspector import inspect


class EvidenceRuleTests(unittest.TestCase):
    def test_http_source_is_rejected(self):
        result = collect([{
            "problem_statement": "Need",
            "source_title": "Page",
            "source_url": "http://example.org",
            "collected_at": "2026-11-23",
        }])
        self.assertEqual(len(result["accepted"]), 0)
        self.assertEqual(len(result["rejected"]), 1)

    def test_non_object_record_is_rejected_without_crashing(self):
        result = collect([None, "not a record"])
        self.assertEqual(len(result["accepted"]), 0)
        self.assertEqual(len(result["rejected"]), 2)

    def test_url_with_embedded_credentials_is_rejected(self):
        result = collect([{
            "problem_statement": "Need",
            "source_title": "Page",
            "source_url": "https://user:pass@example.org/path",
            "collected_at": "2026-11-23",
        }])
        self.assertEqual(len(result["accepted"]), 0)

    def test_malformed_collection_date_needs_review(self):
        result = inspect([{
            "source_url": "https://example.org/a",
            "source_title": "Page",
            "collected_at": "yesterday",
            "published_at": "2026-99-99",
            "evidence_class": "fact",
        }])
        self.assertIn("invalid_or_missing_collection_date", result[0]["issues"])
        self.assertIn("invalid_publication_date", result[0]["issues"])
        self.assertEqual(result[0]["review_status"], "needs_human_review")

    def test_missing_evidence_class_is_not_silently_called_fact(self):
        result = inspect([{
            "source_url": "https://example.org/a",
            "source_title": "Page",
            "collected_at": "2026-11-23",
        }])
        self.assertIn("missing_or_invalid_evidence_class", result[0]["issues"])

    def test_valid_record_is_ready_for_human_verification_not_auto_verified(self):
        result = inspect([{
            "source_url": "https://example.org/a",
            "source_title": "Page",
            "collected_at": "2026-11-23",
            "published_at": "2026-11-20",
            "evidence_class": "fact",
        }])
        self.assertEqual(result[0]["review_status"], "ready_for_human_verification")
        self.assertEqual(result[0]["issues"], [])


if __name__ == "__main__":
    unittest.main()
