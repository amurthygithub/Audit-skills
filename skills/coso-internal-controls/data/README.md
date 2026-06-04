# Data — coso-internal-controls

Synthetic datasets and generators that drive the use cases and tests. Every dataset is deterministic.

## Layout

```
data/
  README.md     # this file
```

## Current state

Data generators and seed fixtures are planned for UC-01 and UC-02. Currently no seed data is generated (use-case status: stub).

The data layer will contain:
- `generators/` — deterministic Python CLIs with --seed.
- `seeds/` — canonical fixtures (input + expected output).

## PII / NPI / PHI Redaction

Per telemetry/redaction.md and the Spine:
- All generators strip free-form PII before persisting.
- Structured IDs (control_id, finding_id, uc_id) are kept.
