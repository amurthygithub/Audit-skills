---
industry: healthcare
parent_skill: fedramp-authorization
title: "Healthcare — a health-tech CSP serving government health systems: the FedRAMP + HIPAA overlap, the control families that double-count, and PHI workload categorization"
version: 0.1.0
status: active
frameworks: [FedRAMP-Rev5, FedRAMP-Authorization-Act-2022, OMB-M-24-15, NIST-SP-800-53r5]
primary_personas: [CSP ISSO, Cloud-security engineer, CISO, Privacy/HIPAA officer]
regulatory_anchors: [FEDRAMP-REV5-BASELINES, FIPS-199, NIST-800-53R5, FEDRAMP-CONMON]
last_verified: "2026-06-11"
---

# Healthcare — the health-tech CSP lens

A health-tech CSP selling a SaaS offering to government health systems (a federal health agency, a public hospital network, a state Medicaid program operating in a federal cloud) faces FedRAMP **and** HIPAA at once. This view applies the skill to that CSP: the FedRAMP categorization of **PHI workloads**, and the **overlap** between the FedRAMP control set and the HIPAA Security Rule. There is no dedicated seeded UC in v1; it reuses the **UC-01** categorization method (`use-cases/uc-01-moderate-agency-ato.md`) for the PHI workload, with a pointer to `hipaa-security-rule` for the HIPAA side.

## The health-tech framing

### "How do we categorize a PHI workload?"

The same way as any system — the **FIPS 199 high-water mark** across confidentiality, integrity, and availability [FIPS-199 §categorization]. PHI (protected health information) is high-sensitivity data, so a PHI workload typically rates at least **Moderate on confidentiality**, which makes the overall high-water mark **Moderate → 323 controls**; integrity or availability concerns (e.g., a clinical system whose outage harms care) can push it to **High → 410 controls** [FEDRAMP-REV5-BASELINES §counts]. There is no averaging — one High objective makes the whole system High. The baseline is the same **tailored NIST SP 800-53 Rev 5** control set; for the catalog, use `nist-800-53-rmf` [NIST-800-53R5 §baselines].

### "We're already HIPAA-compliant — does that satisfy FedRAMP?"

**No — they are distinct regimes that overlap, not substitutes.** FedRAMP is the **federal authorization** program (categorize → baseline → SSP/SAP/SAR/POA&M → 3PAO assessment → monthly ConMon → AO ATO); the **HIPAA Security Rule** is the standalone safeguard obligation for PHI. They **overlap** heavily because the FedRAMP baselines are NIST SP 800-53 Rev 5 controls and many of those control families map closely to the HIPAA Security Rule's administrative, physical, and technical safeguards (access control, audit, integrity, transmission security). A health-tech CSP can **reuse evidence** across the two — a single access-control or audit implementation supports both — but the FedRAMP authorization and the HIPAA compliance posture are **separate artifacts**, and FedRAMP does not relieve the HIPAA obligation (or vice versa). For the HIPAA Security Rule mechanics, use **`hipaa-security-rule`** — this skill covers only the FedRAMP side and points to the overlap.

### "What does the FedRAMP + HIPAA overlap actually buy us?"

Evidence reuse on the **double-counting control families**. Where a FedRAMP control (e.g., access control, audit and accountability, system and communications protection) implements a safeguard the HIPAA Security Rule also requires, the implementation and its evidence serve both regimes. The CSP still authors the **SSP** describing FedRAMP control implementation and maintains the FedRAMP **POA&M** and monthly **ConMon** [FEDRAMP-PLAYBOOK §ssp; FEDRAMP-CONMON §monthly] — HIPAA does not change those FedRAMP artifacts; it sits alongside them.

### "Who authorizes a health-tech CSP?"

The same Agency Authorization path and governance: the statutory **FedRAMP Board** under the 2022 Act [FEDRAMP-ACT-2022 §3610], not the retired JAB, with the sponsoring health agency's AO granting the ATO. HIPAA does not change the FedRAMP path — it is an additional regime the same system must also satisfy.

## What's unique to a health-tech CSP

- **PHI drives at least Moderate, often High.** Categorize the PHI workload on the high-water mark; confidentiality is rarely Low for PHI, and clinical-availability concerns can push to High (410).
- **FedRAMP + HIPAA overlap on the NIST control families** — reuse evidence, but keep the two postures distinct; neither substitutes for the other.
- **Two regimes, two homes.** FedRAMP is owned here (categorize → baseline → package → ConMon); HIPAA Security Rule mechanics are owned by `hipaa-security-rule`.
- **LI-SaaS is unlikely for a PHI workload.** LI-SaaS Tailored is **Low-impact only**; a PHI system that categorizes Moderate/High takes the full Moderate/High baseline, not LI-SaaS [FEDRAMP-REV5-BASELINES §li-saas].

## Anti-hallucination

- **FedRAMP and HIPAA are distinct regimes that overlap** — HIPAA compliance does not satisfy FedRAMP, and FedRAMP authorization does not satisfy HIPAA; the overlap enables evidence reuse, not substitution. HIPAA mechanics live in `hipaa-security-rule`.
- **FIPS 199 overall impact is the high-water mark (max of C/I/A)** — one High objective makes the whole system High [FIPS-199 §categorization]. Do not average.
- **The baseline counts are fixed: Low 156 / Moderate 323 / High 410 / LI-SaaS 156** [FEDRAMP-REV5-BASELINES §counts]; they ARE tailored 800-53 Rev 5 controls, not a separate catalog [NIST-800-53R5 §baselines].
- **LI-SaaS is Low-impact only** — a Moderate/High PHI system, even if SaaS-delivered, takes the full Moderate/High baseline [FEDRAMP-REV5-BASELINES §li-saas].
- **The JAB and its P-ATO are retired** — the current authorizer is the statutory FedRAMP Board; Agency Authorization is the operative path [FEDRAMP-ACT-2022 §3610; OMB-M-24-15 §authority].
- **ConMon is monthly; SLAs are 30 / 90 / 180 days** (high-critical / moderate / low) [FEDRAMP-CONMON §monthly].
- **This is not authorization, legal, or HIPAA-compliance advice** — categorization and the ATO turn on the system's specific PHI and the AO's risk decision.

## Cross-references

- `hipaa-security-rule` (sibling skill) — authoritative for the HIPAA Security Rule administrative / physical / technical safeguards; pair it for the overlap and evidence-reuse pattern.
- `use-cases/uc-01-moderate-agency-ato.md` — the categorization → baseline → POA&M method applied to a Moderate (or, if any objective is High, a High) PHI workload.
- `chunks/02-impact-levels-and-baselines.md` — FIPS 199 categorization and the four baselines.
- `chunks/05-assessment-and-inheritance.md` — the 3PAO assessment and the HIPAA-overlap pointer.
- `nist-800-53-rmf` (sibling skill) — authoritative for the 800-53 control catalog and the general RMF.
