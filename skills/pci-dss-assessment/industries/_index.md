---
title: "Industry views for PCI DSS v4.0.1 assessment"
parent_skill: pci-dss-assessment
type: industries-index
last_verified: "2026-06-11"
---

# Industry views — PCI DSS v4.0.1 assessment

PCI DSS is one standard (6 goals, 12 requirements, 10 SAQ types), but the path that applies — and the scope you can avoid — lands very differently on an e-commerce SaaS, a multi-channel retailer, a payment processor, and a healthcare provider that "just" takes card payments. Each industry view shows the sector-specific angle: which validation path dominates, which scope-minimization levers matter, and which adjacent regimes (SOC 2, HIPAA) get confused with PCI obligations.

## Available industry views (alphabetical)

| Industry | File | When to use | Sector angle | Anchor topics |
|---|---|---|---|---|
| Financial services | financial-services.md | Acquirer, processor, or large service provider handling cardholder data for others. | Full ROC by default; Appendix A1 multi-tenant separation; Appendix A3 DESV (brand-designated, not chosen); the responsibility matrix you owe your customers. | Full ROC, A1 multi-tenant, A3 DESV, customized approach + TRA |
| Healthcare | healthcare.md | Provider taking card payments (patient portal, front-desk terminal, phone payments) — the overlooked CDE. | Finding the CDE the HIPAA program forgot; scope-minimization via P2PE/outsourcing; PCI vs HIPAA are different data, same vendor-management discipline (one-way reference into `hipaa-security-rule`). | Overlooked CDE, scope minimization, vendor-management overlap |
| Retail / e-commerce | retail-ecommerce.md | Retailer accepting cards card-present and online; franchise multi-site. | POS/POI and the card-present CDE; store-network segmentation as scope reduction; the B/B-IP/C/C-VT/P2PE SAQ landscape; franchise sampling and compensating controls. | POS/POI, segmentation, B/B-IP/C/C-VT/P2PE, franchise multi-site |
| SaaS technology | saas-technology.md | E-commerce/SaaS merchant or service provider. | Merchant vs service-provider role; SAQ A vs A-EP and the client-side script requirements 6.4.3/11.6.1; cloud shared responsibility and the service-provider responsibility matrix. | SAQ A vs A-EP, 6.4.3/11.6.1, service-provider matrix |

## How the views map to the use cases

- `saas-technology.md` → UC-01 (CartNimbus, e-commerce SAQ A-EP selection and the client-side script requirements).
- `retail-ecommerce.md` → UC-02 (Ironvale Retail, full-ROC scoping/segmentation + customized approach) and UC-03 (the 30-location franchise compensating-control worksheet).
- `financial-services.md` → reuses the UC-02 full-ROC scoping and customized-approach method; the A1/A3 angles have no dedicated seeded UC in v1.
- `healthcare.md` → reuses the UC-01 SAQ-selection method (patient portal) and the UC-02 scoping method (provider systems); no dedicated seeded UC in v1.

## Industries not in scope (use a different skill or view)

| Need | Where to go instead |
|---|---|
| HIPAA Security Rule risk analysis, addressable dispositions, BAA checks | `hipaa-security-rule` — different data (ePHI vs cardholder data); `healthcare.md` references into it for the vendor-management discipline only, one-way |
| SOC 2 report content and engagement lifecycle for a service provider | `aicpa-soc-reporting` — pair with `saas-technology.md` for the SOC-2-plus-AOC evidence-reuse pattern (overlap, not equivalence) |
| Executive cyber-maturity narrative / NIST control-catalog depth | `nist-csf-2` and `nist-800-53-rmf` — the PCI↔CSF/800-53 mapping lives in the NIST OLIR catalog; this skill points to it and asserts no crosswalk rows in v1 |
| Card-brand level determination, fines, penalty amounts | Out of scope entirely — validation levels are brand-defined; penalties are pointer-only (no amounts) |

## How to use an industry view

1. Open the view matching your sector and read the framing questions first — they answer the most common scoping mistakes (e.g. "are we a merchant or a service provider?", "where is the CDE we forgot?").
2. Use the anchor-topics column above to jump into the right chunks (`chunks/01`–`chunks/08`).
3. Treat each view's anti-hallucination section as the known-traps list for that sector; every house decision convention is labeled where it appears.
4. For a seeded, test-verified worked example, follow the view's use-case cross-reference — the seeds in `data/seeds/` are the contract.
