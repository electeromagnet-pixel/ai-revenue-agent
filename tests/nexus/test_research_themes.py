import json
import unittest
from pathlib import Path

from nexus.agents.analyst import analyze
from nexus.pipeline.normalize import normalize

ROOT = Path(__file__).resolve().parents[2]


class IranPilotThemeTests(unittest.TestCase):
    def test_dataset_has_twenty_records_and_all_have_curated_themes(self):
        rows = json.loads((ROOT / "nexus" / "data" / "examples.json").read_text(encoding="utf-8"))
        self.assertEqual(len(rows), 20)
        self.assertTrue(all(row.get("theme_id") and row.get("theme_label") for row in rows))

    def test_top_three_theme_counts_and_publisher_groups(self):
        rows = json.loads((ROOT / "nexus" / "data" / "examples.json").read_text(encoding="utf-8"))
        patterns = {item["theme_id"]: item for item in analyze(normalize(rows))}
        self.assertEqual(patterns["DIGITAL_BUSINESS_CONTINUITY"]["recurrence_count"], 7)
        self.assertEqual(patterns["DIGITAL_BUSINESS_CONTINUITY"]["independent_source_count"], 4)
        self.assertEqual(patterns["AGRI_WATER_INPUT"]["recurrence_count"], 5)
        self.assertEqual(patterns["AGRI_WATER_INPUT"]["independent_source_count"], 3)
        self.assertEqual(patterns["SME_CAPABILITY_FINANCE"]["recurrence_count"], 3)
        self.assertEqual(patterns["SME_CAPABILITY_FINANCE"]["independent_source_count"], 3)
        self.assertTrue(all(
            item["classification_method"] == "explicit_curated_theme"
            for item in patterns.values()
        ))

    def test_no_theme_count_is_marked_as_customer_demand(self):
        rows = json.loads((ROOT / "nexus" / "data" / "examples.json").read_text(encoding="utf-8"))
        self.assertTrue(all(row.get("willingness_to_pay_evidence") is None for row in rows))
        self.assertTrue(all(row.get("review_status") == "unreviewed" for row in rows))


if __name__ == "__main__":
    unittest.main()
