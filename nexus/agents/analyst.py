"""Analyst: group exact normalized problem statements."""
import re

def normalize_problem(value):
    return re.sub(r"\\s+", " ", re.sub(r"[^\\w\\s]", " ", value.casefold())).strip()

def analyze(records):
    groups = {}
    for item in records:
        key = normalize_problem(item["problem_statement"])
        if not key:
            continue
        group = groups.setdefault(key, {"problem_key": key, "records": [], "source_urls": set()})
        group["records"].append(item)
        group["source_urls"].add(item["source_url"])
    return sorted([{"problem_key": g["problem_key"], "recurrence_count": len(g["records"]),
                    "independent_source_count": len(g["source_urls"]), "records": g["records"],
                    "status": "pattern_to_review_not_proven_demand"} for g in groups.values()],
                  key=lambda x: (-x["recurrence_count"], x["problem_key"]))
