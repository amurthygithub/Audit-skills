# Use-Case Index -- aicpa-soc-reporting

| UC | Title | Industries | Status | Token baseline |
|----|-------|-----------|--------|----------------|
| UC-01 | Full SOC 2 Type II examination walkthrough | saas-technology, healthcare | stub | TBD |
| UC-02 | CUEC/CSOC identification for a multi-tenant SaaS | saas-technology | stub | TBD |
| UC-03 | Bridge letter for gap period between SOC 2 reports | saas-technology, financial-services | stub | TBD |
| UC-04 | Auditee preparation for SOC 2 Type II examination | saas-technology, healthcare, financial-services | stub | TBD |

## How to read a use case

Each use case under `use-cases/uc-NN-*.md` follows the standard Spine shape:

- YAML frontmatter: `uc_id`, `title`, `industries`, `frameworks`, `inputs`, `procedure` (refs to `SKILL.md` or `chunks/`), `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`, optional `token_baseline`.
- Body: scenario, walk-through (decision points with the exact skill section referenced), expected output samples, oracle assertion, variations and edge cases.
