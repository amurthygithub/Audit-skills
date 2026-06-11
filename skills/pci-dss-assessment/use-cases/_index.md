---
title: "Use cases for PCI DSS v4.0.1 assessment"
parent_skill: pci-dss-assessment
type: use-cases-index
last_verified: "2026-06-11"
---

# Use cases — PCI DSS v4.0.1 assessment

Each use case is an end-to-end engagement: a persona + a scenario + seeded inputs + expected outputs + derivability-oracle assertions the test suite verifies. The three UCs deliberately span the **three validation routes** (the SAQ path, the full-ROC + customized-approach path, and the compensating-control path), org sizes (~2M transactions / ~8M transactions / 30-location franchise), and both personas (merchant self-assessment and assessor support).

## Available use cases

| UC | Title | Industry | Persona | Key output |
|---|---|---|---|---|
| [UC-01](uc-01-saq-selection.md) | E-commerce SAQ selection — CartNimbus (~2M-transaction merchant) | saas-technology, retail-ecommerce | Auditee (merchant compliance lead) | SAQ eligibility = **SAQ A-EP** with the deciding factor (merchant controls payment-page scripts but its servers never receive PAN), and the client-side script requirements **6.4.3 / 11.6.1** that apply on A-EP/ROC but not pure SAQ A |
| [UC-02](uc-02-roc-segmentation.md) | Full ROC scoping + segmentation + customized approach — Ironvale Retail (~8M-transaction L1 merchant, L1 brand-defined) | retail-ecommerce, financial-services | Auditee (retail security manager + QSA support) | 14-system inventory scoped to **10 in-scope / 4 out-of-scope** (5 CDE), segmentation as scope reduction, one customized-approach request (req 8.3.6) with a TRA **accepted** |
| [UC-03](uc-03-compensating-control.md) | Compensating-control worksheet — Meridian QSA-Support (solo consultant, 30-location franchise on SAQ D) | retail-ecommerce, financial-services | Assessor support (solo consultant) | Legacy POS that cannot meet a Req-8 control → **compensating control** (not customized approach); all four Appendix-C worksheet elements present → **worksheet complete** |

All 3 use cases are `status: active`: seeds exist in `data/seeds/`, the stub executor returns the expected output, and the oracle/metamorphic/adversarial tests pass.

## How to use a use case

1. Open the UC file for the persona/scenario you need and read the frontmatter first — `inputs`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status` are the fields the lint and test suite validate.
2. The `procedure` steps name specific chunk files (`chunks/01`–`chunks/08`) — the procedure is a navigation map through the skill.
3. The seeds in `data_refs` are the tested fixture and the UC's source of truth; the doc describes exactly what the oracle derives from them.
4. The oracles are **derivability-based**: every expected number is recomputed independently from the seed files (no echo). If you change a seed, the oracle tells you what the new truth is.
5. House decision conventions (the SAQ routing rule, the in-scope/connected/out-of-scope scope categories) are labeled everywhere they appear — they are engagement heuristics applying PCI DSS v4.0.1 eligibility logic, not verbatim standard text.

## The three validation routes at a glance

- **SAQ path (UC-01):** smaller merchants whose architecture qualifies them for a Self-Assessment Questionnaire (the catalog has 10 SAQ types). The decision is architecture-driven, not volume-driven.
- **Full ROC + customized approach (UC-02):** larger merchants and service providers validating via a Report on Compliance, where scoping/segmentation governs cost and a customized approach (Appendix D) requires a Targeted Risk Analysis.
- **Compensating control (UC-03):** an existing defined requirement that cannot be met due to a legitimate constraint, documented on the Appendix-C worksheet — distinct from a customized approach.

## Use cases NOT in scope

Valid engagement types not codified in v1 (candidates for a future release):

- **Service-provider DESV (Appendix A3) engagement** — Designated Entities Supplemental Validation is covered narratively in `industries/financial-services.md`; no seeded fixture yet.
- **Multi-tenant service-provider A1 assessment** (Appendix A1) — narratively in `industries/financial-services.md`; no seeded fixture yet.
- **P2PE / SPoC scope-minimization engagement** — the P2PE and SPoC SAQ paths are in the selector; no seeded worked example in v1.
- **Card-brand level determination / penalty calculation** — out of scope entirely: validation levels are **brand-defined** and penalties are pointer-only (no amounts).
