import unittest
from nexus.agents.explorer import collect
from nexus.agents.inspector import inspect
class EvidenceRuleTests(unittest.TestCase):
    def test_http_source_is_rejected(self):
        result=collect([{"problem_statement":"Need","source_title":"Page","source_url":"http://example.org","collected_at":"2026-11-23"}])
        self.assertEqual(len(result["accepted"]),0); self.assertEqual(len(result["rejected"]),1)
    def test_undated_source_needs_review(self):
        result=inspect([{"source_url":"https://example.org/a","source_title":"Page","collected_at":"2026-11-23","evidence_class":"fact"}])
        self.assertIn("publication_date_unknown",result[0]["issues"])
        self.assertEqual(result[0]["review_status"],"needs_human_review")
if __name__ == "__main__": unittest.main()
