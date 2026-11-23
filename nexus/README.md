# NEXUS v0.1 — Evidence-first opportunity discovery

NEXUS is an experimental research workflow for documenting problems and evaluating possible solutions. It is separate from the existing AI Revenue Agent pipeline.

## Initial scope
- Geography: Iran; domains: all, initially using manually documented public sources.
- First study target: at least 20 documented examples. The current pilot dataset contains 20 public-source observations from 12 publisher groups; every record is marked `unreviewed` pending human source and claim checks.
- Zero paid APIs, hosted models, automated outreach, purchases, or external actions.
- Python standard library only; JSON input/output and optional local SQLite.
- Five agents are deterministic Python modules, not five independent AI models.

## Evidence rules
Distinguish `fact`, `hypothesis`, and `inference`. A URL, title, excerpt, or hash does not prove a claim. Keep publication and collection dates separate. Do not invent customers, willingness to pay, costs, revenue, or competitor facts. Unknown values remain null or explicitly unknown. Analyst source counts use an explicit `independent_source_group` when supplied; otherwise they conservatively group pages by hostname. Hostname grouping is only a proxy, not proof that publishers are independent. Human review must confirm independence before treating sources as corroboration.

## First run
From repository root:
```bash
python -m unittest discover -s tests/nexus -v
python -m nexus.pipeline.report --input nexus/data/examples.json
```
The starter data is empty, not market findings. Add verified examples before drawing conclusions.

## Workflow
Explorer validates documented records; Analyst groups recurring problems; Idea Generator proposes hypotheses; Economic Evaluator records knowns and unknowns; Inspector checks provenance; Report exports a reviewable JSON summary.

## Limitations
This version does not crawl the web, authenticate sources, determine truth automatically, or estimate actual market size. Human review is required. Future source adapters and optional LLM assistance must preserve evidence gates.
