"""Explorer: accept documented public-source records; never fetch arbitrary URLs."""
from urllib.parse import urlparse

def collect(records):
    accepted, rejected = [], []
    for index, record in enumerate(records):
        parsed = urlparse(record.get("source_url", ""))
        required = ("problem_statement", "source_title", "source_url", "collected_at")
        missing = [key for key in required if not record.get(key)]
        if missing or parsed.scheme != "https" or not parsed.netloc:
            rejected.append({"index": index, "reason": "missing_fields_or_unsafe_source_url", "missing": missing})
        else:
            accepted.append(dict(record))
    return {"accepted": accepted, "rejected": rejected, "external_actions_allowed": False}
