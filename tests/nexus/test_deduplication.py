import unittest
from nexus.pipeline.deduplicate import deduplicate
class DeduplicationTests(unittest.TestCase):
    def test_duplicate_urls_are_reported(self):
        a={"source_url":"https://example.org/a"}; b={"source_url":"https://example.org/a"}
        result=deduplicate([a,b])
        self.assertEqual(result["unique"],[a]); self.assertEqual(result["duplicates"],[b])
if __name__ == "__main__": unittest.main()
