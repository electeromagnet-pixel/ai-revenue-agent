import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROTOTYPE = ROOT / "nexus" / "prototypes" / "offline_order_ledger.html"


class OfflinePrototypeContractTests(unittest.TestCase):
    def test_prototype_is_self_contained_and_has_no_remote_dependencies(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn('dir="rtl"', html)
        self.assertIn('localStorage', html)
        self.assertNotIn('<script src=', html)
        self.assertNotIn('<link rel="stylesheet" href="http', html)
        self.assertNotIn('fetch(', html)
        self.assertNotIn('XMLHttpRequest', html)

    def test_core_order_workflow_and_data_export_exist(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        for token in ("orderForm", "customer", "item", "qty", "amount",
                      "preparing", "followup", "exportJson", "exportCsv",
                      "importJson", "importFile", "FileReader", "JSON.parse",
                      "orders.concat(additions)", "۲ مگابایت"):
            self.assertIn(token, html)

    def test_restore_is_non_destructive_and_checks_duplicate_ids(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn("const known=new Set(orders.map(o=>o.id))", html)
        self.assertIn("known.add(o.id)", html)
        self.assertIn("orders=orders.concat(additions)", html)
        self.assertIn("if(!confirm(", html)
        self.assertIn("هیچ داده‌ای وارد نشد", html)

    def test_prototype_warns_against_real_personal_data(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn("فقط با اطلاعات ساختگی", html)
        self.assertIn("رمزگذاری", html)
        self.assertIn("همگام‌سازی", html)


if __name__ == "__main__":
    unittest.main()
