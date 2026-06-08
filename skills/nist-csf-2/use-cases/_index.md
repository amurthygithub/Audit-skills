---
title: "Use cases for NIST CSF 2.0"
parent_skill: nist-csf-2
type: use-cases-index
last_verified: "2026-06-07"
---

# Use cases — NIST CSF 2.0

CSF 2.0 use cases are end-to-end engagements: a persona + a scenario + inputs + expected outputs + oracle assertions that the test suite can verify. Each use case is the canonical worked example for a specific industry × Framework intersection.

## Available use cases

| UC | Title | Industry | Primary personas | Key output |
|---|---|---|---|---|
| [UC-01](uc-01-first-organizational-profile.md) | Series-A SaaS builds first Organizational Profile (Tier 1→2) and identifies 5 highest-impact Subcategories for the 90-day roadmap | saas-technology | SaaS CISO, Founder/CEO, VP Engineering | Current Profile YAML, Gap Analysis, 90-day roadmap |
| [UC-02](uc-02-board-maturity-report.md) | $20B regional bank produces board cyber maturity report (6-function radar + 12-month capital plan + exam-defense narrative) | financial-services, public-sector | CISO, CRO, Head of Operational Risk, Board Cyber Committee | 6-function radar, board report markdown, 12-month capital plan |
| [UC-03](uc-03-csf-to-800-53-crosswalk.md) | Mid-market DoD supplier maps 14 lagging CSF 2.0 Subcategories to 800-171 Rev 3 for CMMC L2 readiness | manufacturing, public-sector | CISO at DoD supplier, VP Manufacturing Operations, OT/ICS Lead, DCMA reviewer | Crosswalk table, CMMC L2 readiness scorecard, 12-month roadmap |

## How to use a use case

1. Open the UC file for the industry/persona combination you need.
2. Read the frontmatter first — it has the `inputs`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, and `status` fields that the lint and test suite validate.
3. Match the frontmatter `procedure` to the chunked skill — each procedure step names a specific chunk file, so the procedure is a navigation map through the skill.
4. The `expected_outputs` field is the structured artifact the stub returns when called with the matching `inputs` seed. The oracle tests assert specific fields of this output.
5. The `data_refs` field points to `data/seeds/uc-NN-input.json` — the canonical input for the use case.
6. The `tests` field is the list of pytest functions that validate the output. Failures here are the regression signal.

## Use case status lifecycle

- `status: stub` — frontmatter + procedure written, but no seed data, stub function, or oracle tests yet. **No current use cases are in stub state.**
- `status: active` — frontmatter complete, seed data exists in `data/seeds/`, stub function returns the expected output, and at least one oracle test passes.
- `status: draft` — partial work, known gaps, not yet ready for production use. **No current use cases are in draft state.**

All 3 current use cases are `status: active`.

## Use cases NOT in scope

These are valid engagement types but are not currently codified as use cases. They would be added in a future release if demand emerges.

- **M&A cyber due diligence** — buyer needs a 30-day CSF 2.0 Organizational Profile of the target
- **Cyber insurance application** — carrier requires a CSF 2.0 Profile; the AIG, Chubb, Beazley, and Travelers questionnaires all have similar fields
- **Annual SOC 2 + CSF 2.0 combined engagement** — the SaaS compliance bundle scenario
- **Regulator exam response (OCC, FDIC, Fed, NY DFS)** — bank needs to produce a CSF 2.0 Profile in response to an MRA
- **SEC cyber disclosure (8-K) post-incident** — public company needs to disclose a material cyber incident within 4 business days; CSF 2.0's Subcategories provide the post-incident impact assessment framework
- **Vendor security assessment using CSF 2.0** — enterprise customer assessing a SaaS vendor's CSF 2.0 Profile as part of a third-party risk program
