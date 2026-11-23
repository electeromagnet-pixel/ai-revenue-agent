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
                      "importFile", "FileReader", "JSON.parse",
                      "orders.concat(additions)", "۲ مگابایت"):
            self.assertIn(token, html)

    def test_restore_is_non_destructive_and_checks_duplicate_ids(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn("const known=new Set(orders.map(o=>o.id))", html)
        self.assertIn("known.add(o.id)", html)
        self.assertIn("orders=orders.concat(additions)", html)
        self.assertIn("if(!confirm(", html)
        self.assertIn("هیچ داده‌ای وارد نشد", html)

    def test_form_and_restore_reject_blank_or_out_of_range_values(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn("!customer||!item", html)
        self.assertIn("qty>9999", html)
        self.assertIn("amount>999999999999", html)
        self.assertIn("!o.customer.trim()", html)
        self.assertIn("!o.item.trim()", html)


    def test_mixed_backup_is_validated_atomically_before_any_import(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        validation = html.index("const clean=incoming.map")
        duplicate_check = html.index("const known=new Set(orders.map(o=>o.id))")
        mutation = html.index("orders=orders.concat(additions)")
        invalid_rejection = html.index("throw new Error(\"اطلاعات سفارش شماره \"")
        self.assertLess(validation, duplicate_check)
        self.assertLess(duplicate_check, mutation)
        self.assertLess(invalid_rejection, mutation)
        self.assertIn("هیچ داده‌ای وارد نشد", html)
        self.assertIn("orders=orders.concat(additions)", html)


    def test_restore_ignores_duplicate_ids_in_existing_and_incoming_orders(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        known = html.index("const known=new Set(orders.map(o=>o.id))")
        duplicate_filter = html.index("const additions=clean.filter")
        add_to_known = html.index("known.add(o.id)", duplicate_filter)
        append = html.index("orders=orders.concat(additions)")
        self.assertLess(known, duplicate_filter)
        self.assertLess(duplicate_filter, add_to_known)
        self.assertLess(add_to_known, append)
        self.assertIn("if(!known.has(o.id))return false", html)
        self.assertIn("const duplicates=clean.length-additions.length", html)
        self.assertIn("سفارش جدیدی برای افزودن وجود ندارد", html)

    def test_prototype_warns_against_real_personal_data(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn("فقط با اطلاعات ساختگی", html)
        self.assertIn("رمزگذاری", html)
        self.assertIn("همگام‌سازی", html)


    def test_user_supplied_order_text_is_html_escaped_before_rendering(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn("function safe(value)", html)
        for token in ("safe(o.item)", "safe(o.customer)", "safe(o.date||", "safe(o.note)", "safe(o.id)"):
            self.assertIn(token, html)
        self.assertIn('replace(/[&<>"\']/g,c=>', html)


    def test_csv_export_neutralizes_formula_like_cell_prefixes(self):
        html = PROTOTYPE.read_text(encoding="utf-8")
        self.assertIn("const cell=v=>", html)
        self.assertIn("replace(/^[=+@-]/,\"'\")", html)
        self.assertIn('download("nexus-demo-orders.csv"', html)

if __name__ == "__main__":
    unittest.main()
