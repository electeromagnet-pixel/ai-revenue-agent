"""Manual JSON intake; no network requests."""
import json
from pathlib import Path
from nexus.agents.explorer import collect

def load_records(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("input must be a JSON array of records")
    return collect(data)
