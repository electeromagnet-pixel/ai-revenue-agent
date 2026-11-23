import json
import tempfile
import unittest
from pathlib import Path

from nexus.pipeline.report import run


class ReportTests(unittest.TestCase):
    def test_report_exposes_rejection_and_review_counts(self):
        records = [
            {
                "problem_statement": "Late delivery",
                "source_title": "Customer discussion",
                "source_url": "https://example.org/post/1",
                "collected_at": "2026-11-23",
                "published_at": "2026-11-20",
                "evidence_class": "fact",
            },
            {
                "problem_statement": "Unsafe source",
                "source_title": "Insecure page",
                "source_url": "http://example.org/post/2",
                "collected_at": "2026-11-23",
            },
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.json"
            path.write_text(json.dumps(records), encoding="utf-8")
            report = run(path)
        self.assertEqual(report["records_submitted"], 2)
        self.assertEqual(report["records_accepted"], 1)
        self.assertEqual(report["records_rejected"], 1)
        self.assertEqual(len(report["rejection_details"]), 1)
        self.assertEqual(report["records_ready_for_human_verification"], 1)
        self.assertEqual(report["records_needing_human_review"], 0)
        self.assertFalse(report["external_actions_allowed"])
        self.assertIn("not that a source", report["warning"])


if __name__ == "__main__":
    unittest.main()
