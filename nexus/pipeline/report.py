"""Run the offline deterministic workflow and print a JSON report."""
import argparse, json
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
    patterns = analyze(unique["unique"])
    ideas = evaluate(generate(patterns))
    return {"records_accepted": len(intake["accepted"]), "records_rejected": len(intake["rejected"]),
            "duplicates": len(unique["duplicates"]), "patterns": patterns, "ideas": ideas,
            "inspection": inspect(unique["unique"]), "external_actions_allowed": False,
            "warning": "Research signals are not proof of buyer demand or profitability."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="nexus/data/examples.json")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = run(args.input)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output: Path(args.output).write_text(rendered + "\\n", encoding="utf-8")
    print(rendered)
