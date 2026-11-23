"""Run the offline deterministic workflow and print an auditable JSON report."""
import argparse
import json
from pathlib import Path

from nexus.pipeline.collect import load_records
from nexus.pipeline.normalize import normalize
from nexus.pipeline.deduplicate import deduplicate
from nexus.agents.analyst import analyze
from nexus.agents.idea_generator import generate
from nexus.agents.economic_evaluator import evaluate
from nexus.agents.inspector import inspect


def run(input_path):
    intake = load_records(input_path)
    unique = deduplicate(normalize(intake["accepted"]))
    inspections = inspect(unique["unique"])
    patterns = analyze(unique["unique"])
    ideas = evaluate(generate(patterns))
    needs_review = sum(
        item["review_status"] == "needs_human_review" for item in inspections
    )
    ready_for_human = sum(
        item["review_status"] == "ready_for_human_verification"
        for item in inspections
    )
    return {
        "records_submitted": len(intake["accepted"]) + len(intake["rejected"]),
        "records_accepted": len(intake["accepted"]),
        "records_rejected": len(intake["rejected"]),
        "rejection_details": intake["rejected"],
        "duplicates": len(unique["duplicates"]),
        "unique_records": len(unique["unique"]),
        "records_needing_human_review": needs_review,
        "records_ready_for_human_verification": ready_for_human,
        "patterns": patterns,
        "ideas": ideas,
        "inspection": inspections,
        "external_actions_allowed": False,
        "warning": (
            "Research signals are not proof of buyer demand or profitability. "
            "Ready means provenance fields passed basic checks, not that a source "
            "or claim has been independently verified."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="nexus/data/examples.json")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = run(args.input)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
