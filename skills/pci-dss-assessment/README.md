# pci-dss-assessment

The assessment skill for **PCI DSS v4.0.1** (Payment Card Industry Data Security Standard — Requirements and Testing Procedures, June 2024): 6 goals, 12 principal requirements, 10 Self-Assessment Questionnaire (SAQ) types, and the validation machinery (ROC / AOC / SAQ, defined vs customized approach, compensating controls). It serves both personas — the **auditee** working out which validation path applies and what to actually do (scoping, SAQ selection, self-assessment) and the **assessor/consultant** supporting a ROC, a customized approach, or a compensating control.

## What it does

The skill's spine is **routing**: PCI's value to a consumer is "which validation path applies to me, and what must I actually do?" So the **SAQ selector**, the **scope/segmentation** decision, and the **defined-vs-customized / compensating-control** distinction are the core — not a transcription of the 249-requirement catalog. It teaches the structure (6 → 12 → sections), routes to the right requirements, and walks the three validation routes end-to-end with seeded, test-verified examples.

## Use cases (3)

- **UC-01 — E-commerce SAQ selection** (CartNimbus, a ~2M-transaction merchant): a direct-post payment page with merchant scripts on it but whose servers never receive PAN resolves to **SAQ A-EP** — and the client-side script requirements **6.4.3 / 11.6.1** apply (they do not on a pure SAQ A redirect/iframe with no merchant script; merchant servers touching PAN would force a full ROC).
- **UC-02 — Full ROC scoping + segmentation + customized approach** (Ironvale Retail, a ~8M-transaction L1 merchant): a 14-system inventory scopes to **10 in-scope / 4 out-of-scope** (5 CDE), segmentation lowers the in-scope count deterministically, and one customized-approach request (req 8.3.6) **with a Targeted Risk Analysis is accepted**.
- **UC-03 — Compensating-control worksheet** (Meridian QSA-Support, a solo consultant supporting a 30-location franchise on SAQ D): a legacy POS that cannot meet a Req-8 auth control is a **compensating control** (not a customized approach), and with all four Appendix-C worksheet elements present the **worksheet is complete**.

Every UC is seed-backed with **derivability oracles**: the tests recompute each expected number independently from `data/seeds/` (no echoed verdicts). The skill ships **~30 tests** across oracle, metamorphic, adversarial, and structural suites.

## Caveats that govern everything here

- **Future-dated requirements are in force.** The printed v4.0.1 text still carries "best practice until 31 March 2025" notes (33 of them); **all became mandatory on 2025-03-31** and have been in force for over a year. The skill never presents them as optional — including the e-commerce client-side script requirements 6.4.3 and 11.6.1 [PCI-SSC-Blog-v401 §v4.0.1].
- **Validation levels are brand-defined.** Merchant and service-provider levels (L1/L2/...) and their thresholds are set by the **payment brands and acquirers**, not by PCI SSC or the standard. The skill labels any level as brand-defined and variable, and never asserts a level threshold as an SSC fact.
- **PAN never appears.** No example, seed, or telemetry record contains a primary account number or any cardholder/sensitive-authentication data. PAN is modeled as an architecture/scoping fact ("do the merchant's servers receive it?") — which is itself a teaching point, not just hygiene.
- **No crosswalk rows in v1.** The authoritative PCI↔CSF mapping is the **PCI-DSS-4.0.1-to-CSF-v2.0** reference in the **NIST OLIR** catalog (PCI SSC-submitted). This skill **points to OLIR** and asserts **no mapping row**; PCI↔CSF/800-53 row-level encoding is deferred to a later ticket.

## Industries covered (4)

- [saas-technology](industries/saas-technology.md) — merchant vs service provider, SAQ A vs A-EP, client-side script requirements 6.4.3/11.6.1, cloud shared responsibility and the service-provider responsibility matrix
- [retail-ecommerce](industries/retail-ecommerce.md) — card-present + e-commerce, POS/POI, store-network segmentation, the B/B-IP/C/C-VT/P2PE SAQ paths, franchise multi-site
- [financial-services](industries/financial-services.md) — acquirers/processors/large service providers, full ROC, DESV (Appendix A3), A1 multi-tenant
- [healthcare](industries/healthcare.md) — providers taking card payments (the overlooked CDE), scope-minimization via P2PE/outsourcing, the vendor-management overlap with the `hipaa-security-rule` skill (different data, same discipline)

## What this skill is NOT

- Not legal or contractual advice, and not a compliance certification — no SAQ, worksheet, or scope determination here is a safe harbor.
- Not a QSA engagement — QSA/ISA workflow is described, not simulated; QSA-support is modeled without claiming validation authority.
- Not a source of card-brand levels, fines, or penalty amounts — those are brand-defined and pointer-only.
- Not a crosswalk source in v1 — see the OLIR pointer above.
- Not a substitute for the entity's own assessment — the skill structures the decision; it does not perform the assessment.

## Source and licence

PCI DSS v4.0.1 is licensed (PCI SSC "Read and Copy License") — **no redistribution**. This skill stores identifiers, the 12 official requirement titles, SAQ names, counts, and original paraphrase, with only short attributed excerpts; it never reproduces bulk requirement or testing-procedure text. Sources: the **PCI SSC document library** [PCI-SSC-Document-Library] and the v4.0.1 announcement [PCI-SSC-Blog-v401].
