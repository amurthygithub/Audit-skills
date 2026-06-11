---
industry: financial-services
parent_skill: pci-dss-assessment
title: "Financial services — acquirers, processors, and large service providers: full ROC, DESV (Appendix A3), and A1 multi-tenant service-provider requirements"
version: 0.1.0
status: active
frameworks: [PCI-DSS-4.0.1]
primary_personas: [Acquirer/processor compliance lead, Service-provider CISO, QSA lead assessor, Risk analyst]
regulatory_anchors: [PCI-DSS-v4.0.1, Appendix-A1, Appendix-A3-DESV]
last_verified: "2026-06-11"
---

# Financial services — the acquirer, processor, and large-service-provider lens

Acquirers, payment processors, and large service providers sit at the center of the card ecosystem: they handle cardholder data at volume on behalf of many entities, almost always validate via a **full Report on Compliance (ROC)**, and frequently carry **additional** PCI DSS requirements that smaller merchants never see — the multi-tenant service-provider requirements of **Appendix A1** and, for entities a payment brand designates, the **Designated Entities Supplemental Validation (Appendix A3, DESV)**. This view applies the skill to the financial-services service provider. The UC-02 engagement (`use-cases/uc-02-roc-segmentation.md`) is the closest worked example for the full-ROC scoping and customized-approach mechanics; the A1/A3 angles below have no seeded fixture in v1.

## The financial-services framing

### Why is full ROC the default here?

A service provider that stores, processes, or transmits cardholder data for others — or can affect its security — is generally expected to validate via a ROC (or **SAQ D for Service Providers** where eligible). The scale, the multi-party trust, and the brand/acquirer agreements push these entities to the most rigorous path. The scoping, segmentation, and defined-vs-customized mechanics from UC-02 apply directly; the difference is breadth (more systems, more requirements in play) and the additional appendices below.

### What does Appendix A1 add for a multi-tenant service provider?

**Appendix A1 — Additional PCI DSS Requirements for Multi-Tenant Service Providers** applies to a service provider that provides shared services to multiple customer entities (e.g. a shared hosting or processing platform). It layers requirements on top of the core 12 to ensure **logical separation between tenants**, that one customer cannot access another's environment or data, and that each customer can request and receive the evidence it needs for its own assessment. A multi-tenant service provider also owes each customer a **service-provider responsibility matrix** documenting who is responsible for which requirements (you, the customer, or shared).

### What is DESV (Appendix A3) and who has to do it?

**Appendix A3 — Designated Entities Supplemental Validation** is **not** something an entity opts into: a payment brand or acquirer **designates** an entity (typically a very large processor/service provider, or one with a history of issues, or one storing very large volumes of cardholder data) into supplemental validation. A3 adds requirements around **maintaining a PCI DSS-as-business-as-usual program** — continuous scope validation, control-effectiveness monitoring, and governance — beyond the point-in-time assessment. Whether A3 applies is a **brand/acquirer determination**, never a self-selection, and never an SSC-set threshold.

### Where does Appendix A2 fit?

**Appendix A2 — Additional Requirements for Entities Using SSL/Early TLS for Card-Present POS POI Terminal Connections** is the narrow legacy-allowance appendix for specific card-present POI connections. It is rarely relevant to a modern processor and is named here only for completeness; treat any reliance on early TLS as a tightly time-bounded exception with its own risk-mitigation requirements.

## What's unique to financial services

- **Full ROC is the working assumption** — the SAQ-D-SP path exists, but scale and agreements usually push to a ROC.
- **A1 multi-tenant separation is the platform's burden** — logical isolation between customers, per-customer evidence, and the responsibility matrix are additive to the core 12.
- **A3/DESV is brand-designated, not chosen** — the skill never asserts which entities are designated; that is a brand/acquirer fact.
- **You are the responsibility-matrix author for your customers** — every customer's own SAQ/ROC leans on your AOC and matrix; getting the boundary right is your deliverable, not theirs.
- **Customized approach rigor is higher-stakes here** — UC-02's 8.3.6-with-a-TRA pattern recurs across more requirements; each customized approach needs its own Targeted Risk Analysis (distinct from a compensating control).

## Anti-hallucination

- **Validation levels for service providers are brand-defined** — payment brands and acquirers set them, not PCI DSS; never assert a level threshold as an SSC fact.
- **DESV (A3) is a brand/acquirer designation, not a self-selection** and not a volume threshold the standard sets.
- **A1 applies to multi-tenant service providers**, not to every service provider — single-tenant providers do not inherit A1 by default.
- **Customized approach ≠ compensating control** — the customized approach (Appendix D) is a TRA-backed design choice; a compensating control (Appendix B/C) is constraint-driven against an existing requirement (UC-03).
- **No PCI↔CSF/800-53 crosswalk rows in v1** — the PCI-DSS-4.0.1-to-CSF-v2.0 mapping lives in the NIST OLIR catalog; this skill points to it and asserts no mapping row.
- **Future-dated v4.0.1 requirements are in force**; nothing is presented as optional [PCI-SSC-Blog-v401 §v4.0.1].
- **No PAN is ever shown** — examples carry zero cardholder data.

## Cross-references

- `use-cases/uc-02-roc-segmentation.md` — the closest worked full-ROC scoping/segmentation + customized-approach engagement.
- `chunks/06-validation-roc-aoc.md` — the assessment process, ROC vs AOC, QSA/ISA roles, assessor sampling, and the service-provider responsibility matrix.
- `chunks/07-approaches-and-compensating-controls.md` — defined vs customized approach, the TRA requirement, and the compensating-control distinction.
- `chunks/08-currency-and-program-context.md` — appendix A1/A2/A3 applicability, brand-program context, and the OLIR crosswalk pointer.
