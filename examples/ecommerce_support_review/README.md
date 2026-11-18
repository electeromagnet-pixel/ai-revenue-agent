# Human-review support triage — offline capability proof

Original, zero-API-cost **synthetic-only demonstration** of internal customer-service triage. It maps fictional incoming support messages to topic/urgency hints, a masked order reference, a suggested internal queue, and a conservative *draft for human review*. No network connections, LLM calls, helpdesk writes, customer sends, payment functions, or remote integrations exist in this sample.

```sh
cd examples/ecommerce_support_review
python3 -m unittest -v test_review_triage.py
python3 review_triage.py sample_tickets.json review_queue.json
```

The output deliberately excludes raw messages, customer names, addresses, emails and full order references. It requires `synthetic: true` for examples or an explicit `permitted_internal_use: true` for data that a real operator has legitimately approved for internal processing. The latter field is a caller assertion **not** a verified consent system: production must authenticate permission, enforce retention and access policy, implement source-specific integration controls, and properly audit QA. Heuristics are fallible; language and sentiment are not guessed without reliable evidence. The only output state is `internal_draft_only`, with `customer_send_enabled: false` and `human_approval_required: true`. A real customer message should never be sent automatically by this sample.

**Acceptance checks:** permission-gated input; idempotent opaque ticket IDs; redacted output; no invented financial or resolution promises; hard prohibition on auto-send; regression tests covering injection-like customer text. **Commercial state:** internal demonstrable sample only. No Upwork proposal, engagement, buyer acceptance, paid delivery, API capability, uptime, receipt or net profit is established.
