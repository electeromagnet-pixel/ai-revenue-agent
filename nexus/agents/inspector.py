"""Inspector: basic provenance and evidence-label checks."""
from urllib.parse import urlparse
VALID_CLASSES = {"fact", "hypothesis", "inference"}

def inspect(records):
    results = []
    for record in records:
        issues = []
        parsed = urlparse(record.get("source_url", ""))
        if parsed.scheme != "https" or not parsed.netloc: issues.append("source_url_not_https")
        if not record.get("source_title"): issues.append("missing_source_title")
        if not record.get("collected_at"): issues.append("missing_collection_date")
        if record.get("evidence_class", "fact") not in VALID_CLASSES: issues.append("invalid_evidence_class")
        if not record.get("published_at"): issues.append("publication_date_unknown")
        results.append({"source_url": record.get("source_url"), "issues": issues,
                        "review_status": "needs_human_review" if issues else "ready_for_human_verification"})
    return results
