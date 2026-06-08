# Redaction policy — nist-csf-2 telemetry

## Purpose

This policy governs what fields are stripped, masked, or hashed before telemetry events are emitted. The goal is to make the telemetry useful for ops and analytics while preventing inadvertent disclosure of customer data, regulated data, or PII.

## What MUST be redacted

### PII (always strip)
- Names of individuals (employees, executives, third-party contacts)
- Email addresses
- Phone numbers
- Physical addresses
- Government-issued identifiers (SSN, EIN, ITIN)

### Regulated data (always strip)
- HIPAA: any data in 45 CFR 164.514(b)(2)(i) "Safe Harbor" identifier list (dates, geographic subdivisions smaller than state, etc.) when linked to an individual
- GLBA: any non-public customer financial information
- PCI DSS: cardholder data (PAN, expiration, CVV) — should never be in the skill's input/output anyway
- ITAR/EAR: any controlled technical data
- CUI: any Controlled Unclassified Information per 32 CFR 2002

### Customer business data (always strip or hash)
- Customer names (replace with `org_slug` or hashed org identifier)
- Customer revenue figures
- Customer deal terms
- Customer security findings (specific SAR findings, vulnerability details)

### Skill-internal secrets (always strip)
- API keys
- Authentication tokens
- Configuration values that could reveal deployment details

## What MAY be emitted

### Operational metadata (always safe)
- `uc_id` (UC-01, UC-02, UC-03)
- `event_name` (skill_invocation, uc_loaded, etc.)
- `timestamp` (ISO 8601 UTC)
- `duration_ms` (integer, ms)
- `skill` (always "nist-csf-2")
- `schema_version` (the input schema version the skill consumed)

### Org-level metadata (safe when anonymized)
- `org_fte` (integer, coarse bucket: 1-50, 51-200, 201-1000, 1001-10000, 10000+)
- `org_sector` (one of the 4 industry values: financial-services, public-sector, saas-technology, manufacturing)
- `target_tier` (1-4, the target CSF Tier)

### Result summary (safe when bounded)
- `classification` (e.g., "TIER_2_RISK_INFORMED", "GAP_3_HIGH")
- `subcategory_count` (the number of Subcategories scored, not the scores themselves)
- `gap_count` (the number of gaps in the Gap Analysis, not the gap details)

## What MUST NOT be emitted

- Raw payload (the full input dict to run_skill)
- Raw output (the full output dict from run_skill)
- Any field named `notes`, `comments`, `free_text`, `narrative`, `description` (these often contain PII or regulated data accidentally)
- Subcategory scores (only the *count* of scored Subcategories is safe)
- Specific Subcategory IDs (e.g., `GV.OC-01`) when emitted at scale (these can fingerprint an org's profile)

## Implementation

The `telemetry/instrument.py` `emit()` function does NOT redact — redaction is the responsibility of the caller. The production wrapper around `emit()` should apply a redaction filter before calling `emit()`. The test in `tests/test_nist_csf_2_telemetry.py` enforces that the schema does not require any of the redacted fields.
