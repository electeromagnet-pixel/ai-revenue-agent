"""Normalize records into a stable minimal shape."""
FIELDS = (
    "problem_statement", "affected_group", "geography", "domain", "source_url",
    "source_title", "published_at", "collected_at", "excerpt", "evidence_class",
    "independent_source_group", "willingness_to_pay_evidence", "competing_solutions",
)


def normalize(records):
    return [{key: record.get(key) for key in FIELDS} for record in records]
