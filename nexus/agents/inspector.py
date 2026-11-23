"""Inspector: validate provenance fields without claiming that sources are true."""
from datetime import date, datetime
from urllib.parse import urlparse

VALID_CLASSES = {"fact", "hypothesis", "inference"}


def _valid_date(value):
    if not isinstance(value, str) or not value.strip():
        return False
    candidate = value.strip()
    try:
        date.fromisoformat(candidate)
        return True
    except ValueError:
        pass
    try:
        datetime.fromisoformat(candidate.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def _valid_https_url(value):
    if not isinstance(value, str):
        return False
    try:
        parsed = urlparse(value.strip())
        return (
            parsed.scheme == "https"
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
        )
    except ValueError:
        return False


def inspect(records):
    results = []
    for record in records:
        issues = []
        if not isinstance(record, dict):
            results.append({
                "source_url": None,
                "issues": ["record_must_be_object"],
                "review_status": "needs_human_review",
            })
            continue
        if not _valid_https_url(record.get("source_url")):
            issues.append("source_url_not_safe_https")
        if not isinstance(record.get("source_title"), str) or not record["source_title"].strip():
            issues.append("missing_source_title")
        if not _valid_date(record.get("collected_at")):
            issues.append("invalid_or_missing_collection_date")
        if record.get("evidence_class") not in VALID_CLASSES:
            issues.append("missing_or_invalid_evidence_class")
        published_at = record.get("published_at")
        if published_at is not None and not _valid_date(published_at):
            issues.append("invalid_publication_date")
        if published_at is None:
            issues.append("publication_date_unknown")
        results.append({
            "source_url": record.get("source_url"),
            "issues": issues,
            "review_status": "needs_human_review" if issues else "ready_for_human_verification",
        })
    return results
