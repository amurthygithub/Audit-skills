---
title: "Industry views for NIST CSF 2.0"
parent_skill: nist-csf-2
type: industries-index
last_verified: "2026-06-07"
---

# Industry views — NIST CSF 2.0

CSF 2.0 is a framework-agnostic core. Industry views show how the framework is applied for a specific sector, including the regulatory anchors, common crosswalks, and a "what's unique" framing.

## Available industry views (alphabetical)

| Industry | When to use | Regulatory anchors | Headline crosswalks |
|---|---|---|---|
| [Financial services](financial-services.md) | Regulated bank, credit union, insurance carrier, or fintech. Heavy FFIEC / OCC / NY DFS / SOX exposure. | FFIEC CAT, OCC Heightened Standards, NY DFS Part 500, SOX 404 | CSF 2.0 → FFIEC CAT Domains, CSF 2.0 → OCC Heightened Standards §III.C, CSF 2.0 → NY DFS §500.XX, CSF 2.0 → SOX 404 ITGC |
| [Manufacturing](manufacturing.md) | Discrete manufacturer, automotive supplier, aerospace supplier, DoD supplier (CMMC). IT/OT convergence. | CMMC L1/L2/L3, NIST 800-171, NIST 800-172, IEC 62443, IATF 16949, ISO 21434 | CSF 2.0 → CMMC L2 Practices, CSF 2.0 → NIST 800-171, CSF 2.0 → IEC 62443, CSF 2.0 → IATF 16949 / ISO 21434, IT/OT convergence |
| [Public sector](public-sector.md) | US federal civilian agency, state government, or local/municipal government. FISMA / RMF / ATO / BOD 18-01. | FISMA, RMF (800-37), OMB A-130, BOD 18-01, FedRAMP, CJIS, IRS Pub 1075, CA SAM, TX DIR/TAC 202, TX-RAMP, CISA CPGs | CSF 2.0 → RMF Steps, CSF 2.0 → FISMA metrics, CSF 2.0 → CISA CPG, state-RMF variants |
| [SaaS technology](saas-technology.md) | Cloud/SaaS company (Series-A through pre-IPO). Compliance bundle: SOC 2 + ISO 27001 + customer questionnaires. | SOC 2 Type II, ISO 27001:2022, CAIQ v4, SIG Lite, VSAQ, GDPR, CCPA | CSF 2.0 → SOC 2 TSC, CSF 2.0 → ISO 27001 Annex A, CSF 2.0 → CAIQ v4, CSF 2.0 → customer questionnaire coverage |

## Industries deliberately deferred to v1.0

| Industry | Why deferred | Target version |
|---|---|---|
| Healthcare (HIPAA Security Rule + HITRUST) | HIPAA is regulated in 45 CFR Parts 160 and 164; HITRUST CSF is a separate certification; the crosswalk is interpretive and needs `data/crosswalks/csf-to-hipaa.json` to land. Healthcare also has state-specific laws (CA CMIA, NY SHIELD) that complicate the crosswalk. | v1.0 (when `data/crosswalks/` is fully populated) |

## Industries not in scope (use a different skill or industry file)

| Industry | Where to go instead |
|---|---|
| DoD / Intelligence Community classified environments | Use `nist-800-53-rmf` for the RMF-specific ATO; CMMC L4-L5 has its own compliance regime beyond CSF 2.0 |
| Pure OT/ICS / industrial automation | Use a dedicated IEC 62443 skill (not in this library); the `manufacturing.md` file covers IT/OT convergence but not standalone OT |
| Financial-services audit firms (Big 4 advisory) | Use `audit-workpapers` + `isaca-audit-methodology` — the auditor lens, not the auditee lens |
| Payment-card-only environments (no broader security program) | Use a PCI-DSS-specific skill (not in this library); CSF 2.0's mapping to PCI DSS 4.0 is partial |

## How to use an industry view

1. Open the industry file that matches your sector.
2. Read the 6-question framing first — it answers the most common "why CSF 2.0 and not [other framework]?" objection.
3. Use the crosswalk tables to anchor your engagement narrative (board memo, customer memo, regulatory response).
4. Apply the "What's unique to [sector]" section to anticipate sector-specific objections (e.g., for SaaS: the questionnaire fatigue problem; for federal civilian: the ATO-driven reality).
5. Cite the cross-references to other skills (e.g., `nist-800-53-rmf` for federal customers, `aicpa-soc-reporting` for SOC 2 cycles) when the engagement needs to cross framework boundaries.
6. Treat the anti-hallucination section as a known-gaps list — verify any unverified claim against the source before relying on it in a client deliverable.
