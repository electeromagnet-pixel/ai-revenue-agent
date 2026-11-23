"""Normalize records into a stable, schema-aligned minimal shape."""
FIELDS = (
    "evidence_id", "problem_statement", "claim", "affected_group", "geography",
    "domain", "theme_id", "theme_label", "source_url", "source_title",
    "published_at", "collected_at", "excerpt", "evidence_class",
    "independent_source_group", "willingness_to_pay_evidence",
    "competing_solutions", "review_status",
)


def normalize(records):
    return [{key: record.get(key) for key in FIELDS} for record in records]
