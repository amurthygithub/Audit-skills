# PII / NPI / PHI Redaction Policy

Every telemetry event MUST be safe to persist. The Spine (skills/TEMPLATE) enforces this through `telemetry/instrument.py` and the `redaction_applied` flag on the schema.

## What must be redacted

| Class | Examples | Default pattern |
|-------|----------|-----------------|
| Government IDs | SSN, ITIN, EIN, TIN | `\b\d{3}-\d{2}-\d{4}\b` |
| Financial | Credit card, bank account (16+ digits) | `\b\d{16}\b` |
| Contact | Email, phone | regex above |
| Health (PHI) | Names tied to diagnoses, MRNs | **must be removed at source** |
| Customer (NPI) | Account numbers, secrets, tokens | **must be removed at source** |

Naive regex is a baseline, not a guarantee. For production:

- Use [Microsoft Presidio](https://github.com/microsoft/presidio) for entity-aware redaction.
- Hash tokens (SHA-256, salted per-tenant) for joinability without reversibility.
- Run redaction on input **and** output payloads; emit `redaction_applied: true` only when at least one field was transformed.

## Field-level rules

- **Free-form text** (`description`, `notes`, `findings`, `evidence_description`) — redact before persistence.
- **Structured IDs** (`control_id`, `finding_id`, `case_id`) — KEEP; these are audit artifacts, not PII. Whitelist by field name.
- **Embeddings / vectors** — DO NOT persist; drop before emit.

## When `redaction_applied: false` is acceptable

Only when the payload contains no free-form text (e.g., a pure classification call with no description). In that case the schema requires that the event contain no `payload` field at all — only structured outputs.

## What we do NOT log

- Raw user prompts or assistant responses.
- File contents from `data/seeds/` (only paths/IDs).
- Model API keys, OAuth tokens, or session cookies.
