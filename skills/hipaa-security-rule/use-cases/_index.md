---
title: "Use cases for the HIPAA Security Rule (45 CFR Part 164 Subpart C)"
parent_skill: hipaa-security-rule
type: use-cases-index
last_verified: "2026-06-10"
---

# Use cases — HIPAA Security Rule

Each use case is an end-to-end engagement: a persona + a scenario + seeded inputs + expected outputs + derivability-oracle assertions the test suite verifies. The three UCs deliberately span org sizes 1 / 40 / 6,000 — §164.306(b)(2) flexibility of approach demonstrated, not just asserted — and both personas (auditee preparation and auditor readiness).

## Available use cases

| UC | Title | Industry | Persona | Key output |
|---|---|---|---|---|
| [UC-01](uc-01-ba-risk-analysis.md) | BA risk analysis and addressable dispositions — CareSync Relay (40-staff fully remote health-tech SaaS BA, AWS, 12 CE customers) | saas-technology | Auditee (BA compliance lead) | 15-risk register (High 4 / Medium 6 / Low 5), disposition record for all 22 addressable specs (15 implement / 3 alternative_measure / 4 not_reasonable_documented), derived encryption-at-rest decision |
| [UC-02](uc-02-ocr-readiness.md) | Hospital CE OCR-readiness assessment — Bellbrook Regional Health (6,000 staff, 4 facilities) | healthcare | Auditor-readiness (CE compliance office) | 22-standard readiness matrix (14 implemented / 6 partial / 2 missing), prioritized gap register (High 2 / Medium 6 / Low 3), stale-doc flags, NPRM pre-read (all PROPOSED) |
| [UC-03](uc-03-baa-and-checklist.md) | Solo consultant BAA check + right-sized safeguard checklist — Meridian HIT Consulting (headcount 1) | healthcare, saas-technology | Auditee (solo BA) | BAA completeness vs §164.314(a)(2)(i)(A)–(C) + §164.308(b)(3) (2 missing provisions), 10-item checklist with 3 §164.306(b)(2)(i)-scaled items |

All 3 use cases are `status: active`: seeds exist in `data/seeds/`, the stub executor returns the expected output, and the oracle/metamorphic/adversarial tests pass.

## How to use a use case

1. Open the UC file for the persona/scenario you need and read the frontmatter first — `inputs`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status` are the fields the lint and test suite validate.
2. The `procedure` steps name specific chunk files — the procedure is a navigation map through the skill.
3. The seeds in `data_refs` are the tested fixture and the UC's source of truth; the doc describes exactly what the oracle derives from them.
4. The oracles are **derivability-based**: every expected number is recomputed independently from the seed files (no echo). If you change a seed, the oracle tells you what the new truth is.
5. House conventions (UC-01 risk bands, UC-02 gap-priority heuristic and 3-year review cycle) are labeled everywhere they appear — they are engagement parameters, not regulatory requirements.

## Use cases NOT in scope

Valid engagement types not codified in v1 (candidates for a future release):

- **Breach response and notification** — Subpart D (§§164.400–414) mechanics are a different rule; this skill stops at the §164.314(a)(2)(i)(C) BAA touchpoint.
- **Health care clearinghouse isolation assessment** (§164.308(a)(4)(ii)(A)) — the only CE type with a dedicated Required isolation spec.
- **Group health plan document amendment engagement** (§164.314(b)) — covered narratively in `industries/financial-services.md`; no seeded fixture yet.
- **Post-final-rule NPRM gap migration** — becomes a UC only if/when the 2025 NPRM (90 FR 898) is finalized; it is a Proposed Rule as of 2026-06-10.
