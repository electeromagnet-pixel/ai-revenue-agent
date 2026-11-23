# NEXUS evidence collection guide

## One record = one documented observation
Do not combine unrelated claims into one record. Use the exact public source URL and title. Keep the publication date separate from the date NEXUS collected the page.

## Required fields
- `problem_statement`: a short, neutral description of the observed problem.
- `source_url`: public HTTPS URL, without embedded credentials.
- `source_title`: title of the cited page or report.
- `collected_at`: ISO 8601 date or datetime when the source was checked.

## Recommended fields
- `evidence_id`: stable identifier such as `IR-0001`.
- `claim`: the narrow claim supported by the source.
- `affected_group`, `geography`, `domain`: describe who, where, and which area.
- `published_at`: source publication date; use null if unavailable.
- `excerpt`: short excerpt or faithful summary, maximum 500 characters.
- `evidence_class`: fact, hypothesis, or inference. Use fact only for what the source explicitly documents.
- `independent_source_group`: publisher group, not a URL. Related outlets or syndications must not be counted as independent.
- `willingness_to_pay_evidence`: null unless the source explicitly documents payment intent or actual payment.
- `competing_solutions`: only alternatives named by the source; otherwise an empty array.
- `review_status`: unreviewed until a human checks the source and claim.

## Evidence and opportunity safeguards
1. A report about a sector-wide problem is not proof that a specific customer will buy a solution.
2. A person's reported experience is an example, not a prevalence estimate.
3. A repeated URL is one source record; multiple pages from one publisher do not automatically mean independent corroboration.
4. Do not infer revenue, market size, price, cost, or willingness to pay from problem severity.
5. Keep uncertain dates null. Do not guess a publication date.
6. Never enter personal names, contact details, or other unnecessary personal data.

## Validation
Run:
```bash
python -m unittest discover -s tests/nexus -v
python -m nexus.pipeline.report --input nexus/data/examples.json
```

The JSON Schema checks the record's structure. The Inspector checks basic provenance fields. Neither automatically verifies truth.
