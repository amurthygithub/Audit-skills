---
title: "Use cases for FedRAMP cloud authorization (Rev 5; FedRAMP Authorization Act of 2022, 44 U.S.C. 3607-3616; OMB M-24-15)"
parent_skill: fedramp-authorization
type: use-cases-index
last_verified: "2026-06-11"
---

# Use cases — FedRAMP cloud authorization

Each use case is an end-to-end engagement: a persona + a scenario + seeded inputs + expected outputs + derivability-oracle assertions the test suite verifies. The three UCs span the three paths a FedRAMP professional actually walks — the **categorization → baseline → POA&M** chain, the **LI-SaaS eligibility** determination, and the **3PAO finding → POA&M roll-up with inheritance** — and exercise both load-bearing facts the skill exists to teach: **FedRAMP baselines ARE tailored 800-53 Rev 5 controls** (not a separate catalog) and **the FIPS 199 high-water mark drives the baseline**. Both the CSP-side (getting authorized) and the assessor/agency-side (assessing / leveraging) personas are covered.

## Available use cases

| UC | Title | Industry | Persona | Key output |
|---|---|---|---|---|
| [UC-01](uc-01-moderate-agency-ato.md) | SaaS FedRAMP Moderate via Agency Authorization — Acme Cloud Suite (C=Moderate, I=Low, A=Low; 5 SAR findings) | saas-technology | CSP ISSO | Overall **Moderate** (high-water mark); baseline **323** controls; POA&M deadlines by severity — High → 2025-03-31, Moderate → 2025-05-30, Low → 2025-08-28 (`FEDRAMP_MODERATE`) |
| [UC-02](uc-02-li-saas-readiness.md) | Cloud vendor LI-SaaS readiness — Beacon Forms (all-Low CIA, SaaS-delivered) | saas-technology | cloud-vendor founder | LI-SaaS **eligible** (Low + SaaS); baseline **156 controls (method-designated; the Rev 4 "66/90" split is not asserted)** (`LI_SAAS_ELIGIBLE`); Moderate+SaaS is the trap (not LI-SaaS) |
| [UC-03](uc-03-third-party-assessment.md) | Big-4 3PAO assessment of a Moderate CSP — Example 3PAO (8 controls; some failed/own, some inherited) | public-sector (assessor angle) | 3PAO assessor | **4** findings (CSP-owned failed controls AC-2, SI-2, AU-6, CM-6); inherited (SC-7, PE-3) excluded; severity rollup {High:2, Moderate:1, Low:1}; residual-high AO risk note (`SAR_FINDINGS_4`) |

All 3 use cases are `status: active`: seeds exist in `data/seeds/`, the stub executor returns the expected output, and the oracle/metamorphic/adversarial tests pass.

## How to use a use case

1. Open the UC file for the persona/scenario you need and read the frontmatter first — `inputs`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status` are the fields the lint and test suite validate.
2. The `procedure` steps name specific chunk files (`chunks/01`–`chunks/08`) and SKILL.md §1–§11 — the procedure is a navigation map through the skill.
3. The seeds in `data_refs` are the tested fixture and the UC's source of truth; the doc describes exactly what the oracle derives from them.
4. The oracles are **derivability-based**: every expected number is recomputed independently from the seed files (no echo) by `tests/fedramp_authorization_stub.py`. If you change a seed, the oracle tells you what the new truth is.
5. The framework constants (the baseline counts 156/323/410/156) are fixed from the PMO OSCAL profiles — the **derivation** is the seed-driven selection/computation (high-water mark, baseline lookup, due-date = date + SLA, finding selection), not the constants.

## How the use cases map to the industries

- `saas-technology.md` → UC-01 (Acme Cloud Suite — Moderate via Agency Authorization) and UC-02 (Beacon Forms — the LI-SaaS branch).
- `public-sector.md` → UC-03 (Example 3PAO — the SAR finding roll-up and residual-high risk note the AO consumes).
- `financial-services.md` → no dedicated seeded UC in v1; it reuses the UC-01 categorization method with a High-impact categorization (any objective High → overall High → 410).
- `healthcare.md` → no dedicated seeded UC in v1; it reuses the UC-01 / UC-02 categorization method with a PHI workload and a pointer to `hipaa-security-rule`.

## Use cases NOT in scope

Valid engagement types not codified in v1 (candidates for a future release):

- **The 800-53 Rev 5 control catalog / general RMF** (control families, the RMF steps, control selection mechanics) — owned by `nist-800-53-rmf`; this skill cites the boundary and does not re-teach the catalog [NIST-800-53R5 §baselines].
- **The full SSP / SAR document drafting** — the skill explains the package and the process; authoring a complete SSP is a downstream task, not a seeded fixture.
- **The ConMon monthly cycle as a standalone engagement** — the cadence and SLAs live in `chunks/06`; UC-01 exercises the POA&M-deadline derivation but not a full monthly submission.
- **DoD Impact Levels / DISA SRG, GovRAMP (formerly StateRAMP), CMMC** — distinct regimes, named as adjacent, not covered.
