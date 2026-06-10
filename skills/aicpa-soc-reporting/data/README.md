# Data Directory -- aicpa-soc-reporting

Synthetic datasets and generators for the AICPA SOC reporting skill. All generators are deterministic (seedable) and produce no PII/NPI/PHI.

## Generators (planned)

- `gen_soc2_criteria.py` -- Generate a SOC 2 criteria matrix with scope selections.
- `gen_sampling_plan.py` -- Generate a Type II sampling plan based on control frequency.
- `gen_opinion.py` -- Generate opinion determination from exception inputs.

## Seeds (planned)

- `uc-01-input.json` -- Input fixture for UC-01 (SOC 2 Type II walkthrough).
- `uc-01-expected.json` -- Expected output for UC-01.
- `uc-02-input.json` -- Input fixture for UC-02 (CUEC/CSOC identification).
- `uc-02-expected.json` -- Expected output for UC-02.

## Crosswalks (planned)

- `tsc-to-nist-800-53-mod.json` -- TSC to NIST 800-53 Moderate mapping. (PLANNED — not yet shipped; see chunk 03 §Cross-Framework Map for category-level starting points.)
- `tsc-to-iso-27001-2022.json` -- TSC to ISO 27001:2022 Annex A mapping.

## Redaction policy

All seed data is synthetic. No real PII, PHI, or NPI. Follows the skill's `telemetry/redaction.md` policy.
