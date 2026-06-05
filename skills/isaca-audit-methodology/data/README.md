# Data - isaca-audit-methodology

Synthetic datasets and generators that drive the use cases and tests. Every dataset is **deterministic** (seeded) so test runs are reproducible.

## Layout

```
data/
  README.md
  generators/        # Python CLI generators; --seed for reproducibility
  seeds/             # canonical fixtures (planned)
  crosswalks/        # cross-framework mappings (planned)
```

## Data Dictionary (Planned)

### `seeds/uc-01-input.json` - UC-01 COBIT maturity assessment input

| Field | Type | Description |
|-------|------|-------------|
| `organization_name` | string | Organization identifier |
| `industry` | string | Industry key (saas-technology, etc.) |
| `processes_in_scope` | array | List of COBIT process IDs to assess |
| `current_evidence` | array | Evidence items per process area |

### `seeds/uc-02-input.json` - UC-02 ITGC observation input

| Field | Type | Description |
|-------|------|-------------|
| `finding_context` | string | Description of the audit context |
| `applications_in_scope` | array | List of applications reviewed |
| `sample_results` | array | Test results per application |

## PII / NPI / PHI Redaction

Per `telemetry/redaction.md` and the Spine (skills/TEMPLATE):

- All generators strip free-form PII before persisting.
- Free-form description fields use synthetic placeholders.
- Structured IDs (finding_id, uc_id) are kept.
