---
industry: saas-technology
parent_skill: fedramp-authorization
title: "SaaS / technology — a CSP pursuing FedRAMP Moderate via Agency Authorization: SSP over ~323 controls, the 3PAO SAP/SAR, a ~40-item POA&M, and monthly ConMon — the most common path"
version: 0.1.0
status: active
frameworks: [FedRAMP-Rev5, FedRAMP-Authorization-Act-2022, OMB-M-24-15, NIST-SP-800-53r5]
primary_personas: [CSP ISSO, Cloud-security engineer, CISO, FedRAMP program manager]
regulatory_anchors: [FEDRAMP-REV5-BASELINES, FEDRAMP-PLAYBOOK, A2LA-3PAO, FEDRAMP-CONMON, OMB-M-24-15, FIPS-199]
last_verified: "2026-06-11"
---

# SaaS / technology — the CSP-seeking-Moderate lens

A cloud service provider (CSP) selling a SaaS offering to federal agencies almost always lands on the **Moderate** baseline pursued through **Agency Authorization** — the operative Rev 5 path and the most common road to an ATO. This view applies the skill to that CSP. The UC-01 engagement (`use-cases/uc-01-moderate-agency-ato.md`, Acme Cloud Suite) is the worked example; the LI-SaaS branch (`use-cases/uc-02-li-saas-readiness.md`, Beacon Forms) is the lighter-weight Low-impact alternative.

## The CSP framing

### "Which baseline are we — and how many controls is that?"

It is driven by the **FIPS 199 categorization**, which is the **high-water mark** across confidentiality, integrity, and availability [FIPS-199 §categorization]. The overall impact is the maximum of the three objectives (Low < Moderate < High), and that overall level selects the baseline:

- **Low → 156 controls**, **Moderate → 323 controls**, **High → 410 controls** [FEDRAMP-REV5-BASELINES §counts].

Most B2G SaaS handles agency data that is at least Moderate on confidentiality, so the high-water mark is **Moderate → 323 controls**. Raising any single objective to High makes the whole system High (→ 410). These baselines are **tailored NIST SP 800-53 Rev 5 controls** — the same catalog IDs (AC-2, SI-2, …), not a separate FedRAMP catalog; FedRAMP tailors the 800-53B baselines (149/287/370) **up** to 156/323/410 [NIST-800-53R5 §baselines]. For the catalog itself, use `nist-800-53-rmf`.

### "Who authorizes us — the JAB?"

**No — the JAB and its P-ATO are retired.** The current authorizer is the statutory **FedRAMP Board** under the FedRAMP Authorization Act of 2022 [FEDRAMP-ACT-2022 §3610], and OMB M-24-15 retired the JAB P-ATO model — legacy JAB P-ATOs were re-designated by the PMO [OMB-M-24-15 §authority]. The operative Rev 5 path for a SaaS CSP is **Agency Authorization**: a sponsoring agency reviews the package and its **authorizing official (AO)** grants the ATO. M-24-15 adds multi-agency authorization and the **presumption of adequacy** so other agencies can reuse the package [OMB-M-24-15 §presumption].

### "What do we have to build, and who writes what?"

Four core artifacts make up the package [FEDRAMP-PLAYBOOK §ssp]:

- **SSP** — the security "blueprint," **authored by the CSP**, describing how each of the ~323 Moderate controls is implemented.
- **SAP** — the assessment plan, **authored by the 3PAO**.
- **SAR** — the assessment results, **authored by the 3PAO**.
- **POA&M** — the corrective-action plan, **maintained by the CSP**, with one item per open finding (a Moderate package commonly carries on the order of ~40 POA&M items).

The 3PAO is an independent assessor, **A2LA-accredited to ISO/IEC 17020** (Type A or C; Type B is prohibited) [A2LA-3PAO §17020]. The 3PAO tests the controls and writes the SAR; it **recommends** but does not grant the ATO — that is the AO's risk-based decision.

### "What happens after we're authorized?"

ConMon — **monthly**. After the ATO the CSP submits a monthly ConMon package: updated POA&M, system inventory, and vulnerability-scan results [FEDRAMP-CONMON §monthly]. POA&M remediation deadlines follow severity: **30 days** high/critical, **90 days** moderate, **180 days** low — each finding's due-date is its identified-date plus the SLA for its severity. UC-01 derives exactly these deadlines from the SAR findings.

## What's unique to a SaaS CSP

- **The categorization → baseline → control-count chain is the first thing to get right.** High-water mark, not an average; Moderate is the typical landing spot (323), but one High objective makes it High (410). UC-01 derives this from the FIPS 199 seed.
- **Inheritance shrinks the SSP.** A SaaS CSP built on an authorized IaaS/PaaS **inherits/leverages** the provider's controls; inherited controls are the provider's responsibility and are **not re-tested** by the leveraging CSP — and they are **not in the CSP's POA&M** [A2LA-3PAO §17020]. UC-03 shows inherited findings excluded from the CSP's roll-up.
- **The POA&M is a living artifact, not a one-time deliverable.** Every open finding becomes a POA&M item with a severity-driven SLA, and the monthly ConMon cadence keeps it current.
- **SOC 2 is adjacent, not a substitute.** A SaaS CSP's SOC 2 Type II exercises overlapping operational controls and can inform the SSP narrative, but FedRAMP authorization is the federal regime — they are separate artifacts (`aicpa-soc-reporting` is authoritative for SOC 2).

## Anti-hallucination

- **The baseline counts are fixed: Low 156 / Moderate 323 / High 410 / LI-SaaS 156** [FEDRAMP-REV5-BASELINES §counts]. Do not restate with other numbers — 325 is the Rev 4 Moderate count, not Rev 5.
- **FedRAMP baselines ARE tailored 800-53 Rev 5 controls, not a separate catalog** [NIST-800-53R5 §baselines]. For the control families / RMF, use `nist-800-53-rmf`.
- **The JAB and its P-ATO are retired** — the current authorizer is the statutory FedRAMP Board; Agency Authorization is the operative path [FEDRAMP-ACT-2022 §3610; OMB-M-24-15 §authority].
- **FIPS 199 overall impact is the high-water mark (max of C/I/A)** — do not average; one High objective makes the system High [FIPS-199 §categorization].
- **Inherited/leveraged controls are the provider's responsibility** — not re-tested by, and not in the POA&M of, the leveraging CSP [A2LA-3PAO §17020].
- **ConMon is monthly; SLAs are 30 / 90 / 180 days** (high-critical / moderate / low) [FEDRAMP-CONMON §monthly]. The **ATO decision is the AO's** — the 3PAO recommends, it does not grant.
- **FedRAMP 20x is emerging direction, not the settled Rev 5 process** a CSP certifies against today.
- **This is not authorization or legal advice** — Acme Cloud Suite is fictional; the ATO is the authorizing official's risk-based decision.

## Cross-references

- `use-cases/uc-01-moderate-agency-ato.md` — the worked Moderate engagement: categorize → 323 controls → POA&M severity SLAs (30/90/180).
- `use-cases/uc-02-li-saas-readiness.md` — the lighter LI-SaaS branch when the system is Low-impact and SaaS-delivered (156 controls, method-designated; the Rev 4 "66/90" split is not asserted).
- `chunks/02-impact-levels-and-baselines.md` — FIPS 199 categorization and the four baselines (the 800-53 boundary).
- `chunks/04-the-authorization-package.md` — SSP / SAP / SAR / POA&M (who authors what).
- `chunks/05-assessment-and-inheritance.md` — the 3PAO assessment and control inheritance / leveraging.
- `chunks/06-continuous-monitoring.md` — the monthly ConMon cadence and the 30/90/180 SLAs.
- `nist-800-53-rmf` (sibling skill) — authoritative for the 800-53 control catalog and the general RMF.
