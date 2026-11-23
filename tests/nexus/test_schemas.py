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


if __name__ == "__main__":
    unittest.main()
