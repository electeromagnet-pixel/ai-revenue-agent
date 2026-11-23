"""Explorer: validate documented public-source records; never fetch arbitrary URLs."""
from urllib.parse import urlparse

REQUIRED_TEXT_FIELDS = ("problem_statement", "source_title", "source_url", "collected_at")


def _safe_https_url(value):
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


def collect(records):
    accepted, rejected = [], []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            rejected.append({
                "index": index,
                "reason": "record_must_be_object",
                "missing": list(REQUIRED_TEXT_FIELDS),
            })
            continue
        missing = [
            key for key in REQUIRED_TEXT_FIELDS
            if not isinstance(record.get(key), str) or not record[key].strip()
        ]
        if not _safe_https_url(record.get("source_url")):
            missing.append("source_url_https")
        if missing:
            rejected.append({
                "index": index,
                "reason": "missing_fields_or_unsafe_source_url",
                "missing": sorted(set(missing)),
            })
        else:
            accepted.append(dict(record))
    return {
        "accepted": accepted,
        "rejected": rejected,
        "external_actions_allowed": False,
    }
