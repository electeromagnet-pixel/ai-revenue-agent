import json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
class SchemaFilesTests(unittest.TestCase):
    def test_schema_files_are_valid_json(self):
        for name in ("opportunity.schema.json", "evidence.schema.json"):
            data = json.loads((ROOT / "nexus" / "schemas" / name).read_text(encoding="utf-8"))
            self.assertEqual(data["type"], "object")
            self.assertIn("required", data)
if __name__ == "__main__": unittest.main()
