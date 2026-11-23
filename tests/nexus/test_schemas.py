import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class SchemaFilesTests(unittest.TestCase):
    def test_schema_files_are_valid_json(self):
        for name in ("opportunity.schema.json", "evidence.schema.json"):
            data = json.loads((ROOT / "nexus" / "schemas" / name).read_text(encoding="utf-8"))
            self.assertEqual(data["type"], "object")
            self.assertIn("required", data)

    def test_evidence_schema_matches_manual_intake_contract(self):
        data = json.loads(
            (ROOT / "nexus" / "schemas" / "evidence.schema.json").read_text(encoding="utf-8")
        )
        self.assertTrue({
            "problem_statement", "source_url", "source_title", "collected_at"
        }.issubset(set(data["required"])))
        self.assertIn("evidence_class", data["properties"])
        self.assertFalse(data["additionalProperties"])

    def test_iran_pilot_has_twenty_unique_unreviewed_source_records(self):
        records = json.loads((ROOT / "nexus" / "data" / "examples.json").read_text(encoding="utf-8"))
        self.assertEqual(len(records), 20)
        self.assertEqual(len({row["source_url"] for row in records}), 20)
        self.assertTrue(all(row.get("review_status") == "unreviewed" for row in records))
        self.assertTrue(all(row.get("willingness_to_pay_evidence") is None for row in records))
        self.assertEqual(len({row["independent_source_group"] for row in records}), 12)


if __name__ == "__main__":
    unittest.main()
