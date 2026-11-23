"""Deduplicate exact source URLs, preserving first-seen order."""
def deduplicate(records):
    seen, unique, duplicates = set(), [], []
    for record in records:
        key = record.get("source_url", "").strip().casefold()
        if key and key in seen: duplicates.append(record)
        else:
            if key: seen.add(key)
            unique.append(record)
    return {"unique": unique, "duplicates": duplicates}
