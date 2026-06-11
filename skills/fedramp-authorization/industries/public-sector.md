---
industry: public-sector
parent_skill: fedramp-authorization
title: "Public sector — the sponsoring agency / authorizing official side: leveraging a package, the presumption of adequacy, ConMon oversight, the ATO decision, and multi-agency reuse"
version: 0.1.0
status: active
frameworks: [FedRAMP-Rev5, FedRAMP-Authorization-Act-2022, OMB-M-24-15, NIST-SP-800-53r5]
primary_personas: [Authorizing official (AO), Agency ISSO, Agency security reviewer, FedRAMP PMO reviewer]
regulatory_anchors: [OMB-M-24-15, FEDRAMP-ACT-2022, FEDRAMP-CONMON, FEDRAMP-PLAYBOOK, A2LA-3PAO]
last_verified: "2026-06-11"
---

# Public sector — the sponsoring agency / authorizing official lens

This view is the **agency side** of FedRAMP: the sponsoring agency that reviews a CSP's package, the **authorizing official (AO)** who grants the ATO, and the agencies that **leverage** an existing authorization rather than start from scratch. The CSP-side worked example is UC-01 (`use-cases/uc-01-moderate-agency-ato.md`, Acme Cloud Suite); the assessor-side roll-up the AO consumes is UC-03 (`use-cases/uc-03-third-party-assessment.md`, Example 3PAO) — the residual-high finding in UC-03 is exactly the risk an AO must accept or reject.

## The agency framing

### "Who grants the ATO now — the JAB?"

**No — the JAB and its P-ATO are retired.** The FedRAMP Authorization Act of 2022 created the statutory **FedRAMP Board** [FEDRAMP-ACT-2022 §3610], and OMB M-24-15 retired the JAB P-ATO model — legacy JAB P-ATOs were re-designated by the PMO [OMB-M-24-15 §authority]. Under the operative **Agency Authorization** path, the sponsoring agency's **AO** makes the ATO decision: a **risk-based** call on whether to authorize the system to operate. The 3PAO **recommends** and the SAR documents residual risk, but the authorization is the AO's — not the 3PAO's and not the FedRAMP PMO's.

### "Can we reuse another agency's authorization — and do we have to re-do the review?"

Yes, and largely no. OMB M-24-15 frames FedRAMP around a **single authorization** with a **presumption of adequacy**: an agency must **presume a FedRAMP package adequate** at a given impact level, so a second agency can **leverage** the existing package rather than re-assess from scratch [OMB-M-24-15 §presumption]. M-24-15 also adds **multi-agency authorization**. The leveraging agency still issues its **own ATO** for its own use of the system and reviews the package for its specific risk posture — but it does not re-test the controls the 3PAO already assessed.

### "What is the agency on the hook for after the ATO — ConMon oversight."

The CSP runs ConMon; the agency **oversees** it. After authorization the CSP submits a **monthly** ConMon package — updated POA&M, system inventory, and vulnerability-scan results [FEDRAMP-CONMON §monthly] — and the sponsoring agency reviews it for continued acceptable risk. The agency watches the POA&M against the severity SLAs (**30 / 90 / 180** days for high-critical / moderate / low) and decides whether residual or aging findings remain acceptable. A leveraging agency typically relies on the sponsoring agency's ConMon review plus its own risk monitoring.

### "What does the AO actually decide on?"

The AO weighs the **SAR's residual risk**. The 3PAO finding roll-up (UC-03) hands the AO the findings (CSP-owned failed controls), a severity rollup, and a note when any **residual high-severity** finding remains. A residual high finding does not auto-deny the ATO — it forces an explicit **AO risk-acceptance decision** before an ATO can issue. Inherited/leveraged controls are the underlying provider's responsibility and are not the CSP's findings, so they do not sit in this CSP's POA&M [A2LA-3PAO §17020].

## What's unique to the agency / AO side

- **The presumption of adequacy is the leverage mechanism** — it is what lets agencies reuse a package instead of re-authorizing from scratch [OMB-M-24-15 §presumption]. Reuse is the point of the program.
- **The ATO is a risk decision, not a checklist pass.** Residual high-severity findings are accepted or rejected by the AO; the skill encodes the program, it does not grant authorization.
- **ConMon oversight is continuous, not a one-time gate.** Monthly packages, severity-driven SLAs, and significant-change review keep the authorization current.
- **Inheritance shapes what the agency reviews.** Controls inherited from an authorized IaaS/PaaS belong to that provider's package — the agency reviews the CSP's own controls plus the inheritance relationship, not the inherited controls again.

## Anti-hallucination

- **The JAB and its P-ATO are retired** — the current authorizer is the statutory FedRAMP Board; under Agency Authorization the agency AO grants the ATO [FEDRAMP-ACT-2022 §3610; OMB-M-24-15 §authority].
- **The presumption of adequacy is real and directional** — an agency must presume a FedRAMP package adequate at its impact level; this enables multi-agency reuse [OMB-M-24-15 §presumption].
- **The ATO is the AO's risk-based decision** — the 3PAO recommends and the SAR documents residual risk; neither grants the ATO.
- **ConMon is monthly; SLAs are 30 / 90 / 180 days** (high-critical / moderate / low) [FEDRAMP-CONMON §monthly].
- **Inherited/leveraged controls are the provider's responsibility** — not in the leveraging CSP's POA&M, and not re-tested by the leveraging agency [A2LA-3PAO §17020].
- **FedRAMP 20x is emerging direction, not the settled Rev 5 process** — present the presumption-of-adequacy realization and KSIs as direction, not current rule.
- **This is not authorization or legal advice** — the AO's decision turns on the agency's specific risk posture and mission.

## Cross-references

- `use-cases/uc-03-third-party-assessment.md` — the SAR finding roll-up the AO consumes: findings, severity rollup, and the residual-high risk note.
- `use-cases/uc-01-moderate-agency-ato.md` — the CSP-side Moderate engagement the agency reviews and authorizes.
- `chunks/01-fedramp-and-governance.md` — the 2022 Act, the FedRAMP Board, M-24-15, and the JAB-retired fact.
- `chunks/03-authorization-paths.md` — Agency Authorization, the presumption of adequacy, multi-agency reuse, and the AO.
- `chunks/06-continuous-monitoring.md` — the monthly ConMon cadence the agency oversees.
- `chunks/07-poam-and-risk.md` — the POA&M lifecycle and the AO's risk-acceptance role.
