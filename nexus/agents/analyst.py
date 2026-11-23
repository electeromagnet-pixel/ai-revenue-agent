"""Group evidence by explicit, human-curated themes; do not imply semantic discovery."""
import re
from urllib.parse import urlparse


def normalize_problem(value):
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", value.casefold())).strip()


def _source_group(item):
    explicit = item.get("independent_source_group")
    if isinstance(explicit, str) and explicit.strip():
        return explicit.strip().casefold()
    try:
        host = urlparse(item.get("source_url", "")).hostname
    except (TypeError, ValueError):
        host = None
    return host.casefold() if host else None


def analyze(records):
    groups = {}
    for item in records:
        theme_id = item.get("theme_id")
        if isinstance(theme_id, str) and theme_id.strip():
            key = "theme:" + theme_id.strip().casefold()
            label = item.get("theme_label") or theme_id
            method = "explicit_curated_theme"
        else:
            problem_key = normalize_problem(item.get("problem_statement"))
            if not problem_key:
                continue
            key = "problem:" + problem_key
            label = problem_key
            method = "exact_normalized_problem_text"
        group = groups.setdefault(
            key, {"theme_id": theme_id, "problem_key": label, "records": [],
                  "source_groups": set(), "classification_method": method}
        )
        group["records"].append(item)
        source_group = _source_group(item)
        if source_group:
            group["source_groups"].add(source_group)
    return sorted(
        [{
            "theme_id": group["theme_id"],
            "problem_key": group["problem_key"],
            "recurrence_count": len(group["records"]),
            "independent_source_count": len(group["source_groups"]),
            "classification_method": group["classification_method"],
            "records": group["records"],
            "status": "pattern_to_review_not_proven_demand",
        } for group in groups.values()],
        key=lambda item: (-item["recurrence_count"], item["problem_key"]),
    )
