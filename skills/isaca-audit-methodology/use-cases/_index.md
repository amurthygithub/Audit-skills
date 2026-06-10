# Use-Case Index - isaca-audit-methodology

| UC | Title | Industries | Status | Token baseline |
|----|-------|-----------|--------|----------------|
| UC-01 | SaaS COBIT 2019 maturity assessment | saas-technology | stub | TBD |
| UC-02 | ITGC finding in 5-part observation format | financial-services, saas-technology | stub | TBD |
| UC-03 | COBIT 2019 design factors assessment | financial-services | stub | TBD |

## How to read a use case

Each use case under `use-cases/uc-NN-*.md` follows the standard Spine shape:

- **YAML frontmatter** - `uc_id`, `title`, `industries`, `frameworks`, `inputs`, `procedure` (refs to chunks/), `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`.
- **Body** - scenario, walk-through, decision points, expected output samples.

A test harness can parse a use case by reading its frontmatter and running the test listed in its `tests:` field (in `tests/test_isaca_audit_methodology_oracle.py`) against the seed at `data/seeds/uc-NN-input.json`.
