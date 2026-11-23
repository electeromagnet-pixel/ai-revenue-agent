"""Analyst: group normalized problem statements and conservative source groups."""
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
    host = urlparse(item.get("source_url", "")).hostname
    return host.casefold() if host else None


def analyze(records):
    groups = {}
    for item in records:
        key = normalize_problem(item.get("problem_statement"))
        if not key:
            continue
        group = groups.setdefault(
            key, {"problem_key": key, "records": [], "source_groups": set()}
        )
        group["records"].append(item)
        source_group = _source_group(item)
        if source_group:
            group["source_groups"].add(source_group)
    return sorted(
        [
            {
                "problem_key": group["problem_key"],
                "recurrence_count": len(group["records"]),
                "independent_source_count": len(group["source_groups"]),
                "records": group["records"],
                "status": "pattern_to_review_not_proven_demand",
            }
            for group in groups.values()
        ],
        key=lambda item: (-item["recurrence_count"], item["problem_key"]),
    )
