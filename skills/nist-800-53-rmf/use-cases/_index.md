# Use-Case Index — nist-800-53-rmf

| UC | Title | Industries | Status | Token baseline |
|----|-------|-----------|--------|----------------|
| UC-01 | FedRAMP-bound SaaS categorizes FIPS-199 Moderate | saas-technology, public-sector | active | TBD (run `tests/test_telemetry.py` to populate) |
| UC-02 | Federal agency RMF Step 6 authorization (SAR + POA&M + ATO w/ conditions) | public-sector | active | TBD |
| UC-03 | Enterprise fin-svcs maps SOC 2 → 800-53 Moderate | financial-services, saas-technology | active | TBD |

## How to read a use case

Each use case under `use-cases/uc-NN-*.md` follows the standard Spine shape:

- **YAML frontmatter** — `uc_id`, `title`, `industries`, `frameworks`, `inputs`, `procedure` (refs to `SKILL.md §X`), `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`, optional `token_baseline`.
- **Body** — scenario, walk-through (decision points with the exact skill section referenced), expected output samples, oracle assertion (the line a test will execute), variations and edge cases.

A test harness can parse a use case by reading its frontmatter and running `tests/test_oracle.py::test_uc_NN` against the seed at `data/seeds/uc-NN-input.json`.
