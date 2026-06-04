# Data Dictionary -- audit-workpapers

## Directory Structure

- `generators/` -- Deterministic Python CLIs (--seed) for generating synthetic audit populations and seed fixtures.
- `seeds/` -- Canonical seed fixtures.

## Data Policy

- All synthetic data; no real client information.
- Seeds are deterministic (pinned by --seed parameter).
- Files follow the shape expected by each use case's `data_refs` frontmatter field.

## PII/NPI Redaction

- No PII, NPI, or PHI in any data file.
- Client names, amounts, and references are synthetic.
- If any data file is found to contain real information, redact before committing and notify the skill owner.

## Seed Files

| File | Use Case | Description |
|------|----------|-------------|
| `uc-01-input.json` | UC-01 | AR population for MUS sampling |
| `uc-02-input.json` | UC-02 | AP cutoff finding details |

## Adding New Seeds

1. Name the file `uc-NN-input.json` matching the use case.
2. Ensure it is valid JSON.
3. Register in this README.
4. Add a generator under `generators/` if the input is non-trivial.
