---
chunk_id: 08-currency-and-program-context
parent_skill: pci-dss-assessment
topic: "v4.0.1 currency; all future-dated requirements mandatory since 2025-03-31; no successor announced; brand-defined levels and programs (pointer); Appendix A1/A2/A3 applicability; relationship to CSF/800-53 (OLIR pointer, no rows)"
load_when: "user asks whether v4.0.1 is current, about future-dated requirements, merchant/service-provider levels, card-brand programs, DESV, Appendix A1/A2/A3, or PCI-to-CSF/800-53 mapping"
---

# Chunk 08 — Currency and Program Context

This chunk isolates the volatile material — version currency, the future-dated-now-in-force status, brand-defined programs, and the crosswalk pointer — for cheap re-verification on each pass.

## 1. Version currency (verified 2026-06-11)

- **PCI DSS v4.0.1 (June 2024) is the only active version.** It is a **limited revision** of v4.0 with **no new or deleted requirements** [PCI-SSC-Blog-v401].
- **v4.0 retired 2024-12-31**; v3.2.1 retired 2024-03-31.
- **No v4.1 or v5 has been announced** as of 2026-06-11. Re-verify version currency before any version-sensitive answer — it is this skill's primary trust factor.

## 2. Future-dated requirements are in force now

The v4.0.1 text carries **33** applicability notes phrased "best practice until 31 March 2025." **Every one of these requirements became mandatory on 2025-03-31** and has been in force for over a year. The "best practice until" phrasing is **historical** — present these requirements as **fully effective**, never as optional, upcoming, or aspirational. Examples flagged in-force in `chunks/03`-`05` include the client-side-script requirements (6.4.3, 11.6.1), broadened MFA into the CDE (8.4/8.5), automated log review (10.4.1), control-failure detection (10.7), anti-phishing (5.4.1), and Targeted Risk Analyses (12.3). If asked whether one of these is "still just a best practice," the answer is **no — it is mandatory now**.

## 3. Validation levels and card-brand programs are brand-defined

- **Merchant and service-provider levels** (L1/L2/etc.) and any **transaction-volume thresholds** are set by the individual **payment brands** and a merchant's **acquirer**, **not** by PCI SSC or the standard, and they **vary** by brand and agreement.
- **Card-brand compliance programs** (validation cadence, who must file what, fines/penalties) are likewise brand/acquirer matters. This skill is **pointer-only** on programs and **states no penalty amounts**.
- To "what level am I / what must I file," the correct answer is: **that is determined by your acquirer and the relevant payment brands** — consult them. Never assert a level threshold as a PCI SSC rule.

## 4. Appendix A applicability

Appendix A adds **30 requirements** in 8 sections, applicable only to specific entity types:

- **A1 — Multi-tenant service providers.** Additional requirements for providers hosting multiple customer environments (logical separation, per-customer controls, customer-facing evidence).
- **A2 — SSL / early TLS for card-present POS POI.** Applies **only** to entities still using SSL/early TLS for card-present POS POI terminal connections, under a documented risk-mitigation/migration posture.
- **A3 — Designated Entities Supplemental Validation (DESV).** Applies **only** where a payment brand or acquirer **designates** an entity for the enhanced validation in A3 (it is not self-selected). DESV adds governance, scope-validation, and continuous-monitoring expectations on top of the main body.

## 5. Relationship to CSF / 800-53 (pointer only — no rows)

The authoritative PCI↔CSF mapping anchor is the NIST **OLIR PCI-DSS-4.0.1-to-CSF-v2.0** final informative reference (PCI SSC-submitted) [NIST-OLIR], discoverable through the NIST CSF informative-references catalog [NIST-CSF-Informative-References]. This skill **encodes zero crosswalk rows** — row-level extraction is a separate, later ticket. For executive CSF maturity language use `nist-csf-2`; for 800-53 control detail use `nist-800-53-rmf`. Never fabricate a PCI↔CSF or PCI↔800-53 row.

## 6. Re-verification checklist (run each pass)

- [ ] v4.0.1 still the only active version; no successor announced [PCI-SSC-Document-Library].
- [ ] Future-dated requirements still presented as in force (since 2025-03-31).
- [ ] No level threshold asserted as an SSC fact.
- [ ] No crosswalk rows encoded; OLIR pointer intact [NIST-OLIR].
- [ ] No penalty amounts; brand programs pointer-only.
