---
chunk_id: 05-govern-function
parent_skill: nist-csf-2
topic: "GOVERN function (new in 2.0): GV.OC, GV.RM, GV.SC, GV.PO, GV.OV, GV.RR"
load_when: "user asks about GOVERN, GV. categories, or risk governance at the org level"
---

# Chunk 05 — GOVERN Function

**GOVERN** is the single largest change from CSF 1.1 to CSF 2.0 and the most-likely-misrepresented content in any CSF write-up. It is the **umbrella Function**: GOVERN outcomes set the context (mission, risk appetite, supply chain policy, roles, oversight) that the other 5 Functions execute against. This chunk gives the per-Category treatment of GOVERN; the structural overview (including the 1.1-to-2.0 delta) is in `chunks/01-functions-categories.md`. The executive-legibility promise of this skill lives or dies in this chunk.

## 1. Why GOVERN is new in 2.0 (the move from IDENTIFY)

CSF 1.1 had 5 Functions: Identify, Protect, Detect, Respond, Recover. There was a partial governance Category under Identify (`ID.GV` — "Governance") but it was under-developed: 3 Subcategories, no supply chain, no roles-and-responsibilities, no oversight, no policy lifecycle. CSF 2.0 promoted and expanded governance into a full Function with **6 Categories** [NIST-CSF-2.0 §2.2]. The 1.1 `ID.GV` Subcategories were subsumed by the new GOVERN Categories.

The move reflects three post-2020 realities:

1. **Supply chain attacks** (SolarWinds 2020, Kaseya 2021, Log4j 2021, MOVEit 2023) elevated third-party cyber risk from a procurement concern to a **board-level concern**. CSF 2.0 answered with `GV.SC` as a first-class Category under GOVERN.
2. **Regulatory expectations** (SEC cyber disclosure rules 2023, NY DFS 500 §500.04 board reporting, EU DORA) require explicit board-level cyber risk governance. The old `ID.GV` did not have the granularity to express this.
3. **Roles and accountability** — the move from "the CISO owns cyber" to "the board and senior executives own cyber risk" required an explicit Category for roles, responsibilities, and authorities (`GV.RR`).

Practical migration note: a 1.1 Current Profile does **not** automatically become a 2.0 Current Profile. The GOVERN Subcategories must be assessed fresh and the PROTECT mappings re-codified (see `chunks/01-functions-categories.md` §5 for the full 1.1-to-2.0 delta table). Treat 1.1 → 2.0 as a re-baseline, not a rename.

## 2. The 6 GOVERN Categories

GOVERN has 6 Categories [NIST-CSF-2.0 §2.2]. Each Category is the answer to an executive question; each has 2-6 Subcategories. The 6 GOVERN Categories are: `GV.OC` Organizational Context, `GV.RM` Risk Management Strategy, `GV.SC` Cybersecurity Supply Chain Risk Management, `GV.PO` Policy, `GV.OV` Oversight, `GV.RR` Roles, Responsibilities, and Authorities.

### GV.OC — Organizational Context

The mission, stakeholders, legal/regulatory requirements, and risk environment that inform cybersecurity decisions.

- **Executive question**: "What business are we protecting, and for whom?"
- **Subcategories** (representative): `GV.OC-01` (mission understood), `GV.OC-02` (internal/external stakeholders understood), `GV.OC-03` (legal/regulatory requirements understood), `GV.OC-04` (critical objectives, capabilities, services identified), `GV.OC-05` (outcomes, capabilities, services the org depends on understood).
- **Evidence examples**: org chart, mission statement, regulatory mapping document, stakeholder analysis.
- **Board-language**: "We know what we are protecting and why."

### GV.RM — Risk Management Strategy

Risk tolerance, appetite, constraints, and the org's approach to managing cyber risk.

- **Executive question**: "How much cyber risk are we willing to accept, and how do we make that call?"
- **Subcategories** (representative): `GV.RM-01` (risk management objectives established), `GV.RM-02` (risk appetite and tolerance defined), `GV.RM-03` (cybersecurity risk management integrated with enterprise risk), `GV.RM-04` (strategic risk direction established).
- **Evidence examples**: risk appetite statement approved by board, ERM framework document, risk tolerance thresholds.
- **Board-language**: "The board has set the risk appetite; management has set the tolerance."

### GV.SC — Cybersecurity Supply Chain Risk Management

The most operationally significant new Category in 2.0. Covers third-party / supplier / vendor cyber risk.

- **Executive question**: "Are our suppliers a liability, and how do we know?"
- **Subcategories** (representative): `GV.SC-01` (supply chain risk management program established), `GV.SC-02` (suppliers prioritized by criticality), `GV.SC-03` (contracts include cybersecurity requirements), `GV.SC-04` (suppliers routinely assessed), `GV.SC-05` (supplier incident response plans coordinated), `GV.SC-06` (supplier disruptions planned for), `GV.SC-07` (supply chain risks identified and managed throughout life cycle), `GV.SC-08` (suppliers included in incident response planning), `GV.SC-09` (supplier products/services tested prior to acquisition), `GV.SC-10` (components tracked through life cycle).
- **Evidence examples**: third-party risk policy, supplier security questionnaires (CAIQ, SIG), supplier audit results, supply chain risk register.
- **Board-language**: "We have a program to know, assess, and monitor the cyber risk of our suppliers."

**Why GV.SC is the biggest practical change** (in 1.1 supply chain was a single Category `ID.SC` under Identify; in 2.0 it is a 10-Subcategory Category under GOVERN). The elevation moves supply chain from a procurement-and-IT concern to a **board-level governance concern**. The 10 Subcategories cover the full supplier life cycle: from contract (SC-03) through ongoing assessment (SC-04) to incident coordination (SC-05, SC-08) to end-of-life (SC-10). Most orgs have at most 2-3 of these 10 fully implemented; closing the rest is a 12-24 month program.

### GV.PO — Policy

The cybersecurity policy lifecycle: authoring, approval, communication, maintenance, and exception handling.

- **Executive question**: "Do we have current, approved, communicated policies?"
- **Subcategories** (representative): `GV.PO-01` (cybersecurity policy established), `GV.PO-02` (policy reviewed/updated), `GV.PO-03` (policy communicated to stakeholders), `GV.PO-04` (policy exceptions managed).
- **Evidence examples**: policy library, version history, attestation of receipt, exception register.
- **Board-language**: "Our policies exist, are current, and are followed."

### GV.OV — Oversight

How the org knows whether its cybersecurity risk management is working — performance review, strategy adjustment, audit findings.

- **Executive question**: "How do we know the cyber program is working?"
- **Subcategories** (representative): `GV.OV-01` (cybersecurity performance reviewed), `GV.OV-02` (cybersecurity risk management strategy reviewed/adjusted), `GV.OV-03` (security operations reviewed/audited).
- **Evidence examples**: board cyber committee minutes, KPI/KRI dashboards, internal audit reports, regulator examination results.
- **Board-language**: "We have a cadence for reviewing whether the cyber program works."

### GV.RR — Roles, Responsibilities, and Authorities

Who is accountable for cybersecurity decisions, who does the work, who has the authority to make trade-offs.

- **Executive question**: "Who is accountable, and do they have the authority to act?"
- **Subcategories** (representative): `GV.RR-01` (organizational leadership accountable for cyber risk), `GV.RR-02` (roles, responsibilities, authorities communicated), `GV.RR-03` (adequate resources allocated), `GV.RR-04` (cybersecurity responsibilities included in job descriptions).
- **Evidence examples**: cyber RACI, board charter, CISO authority memo, resource plan.
- **Board-language**: "We know who owns cyber, and they have the resources and authority to do the job."

## 3. The supply chain shift (GV.SC) — the biggest practical change

The `GV.SC` elevation is the most operationally significant change in CSF 2.0. Three reasons:

1. **Coverage is broader**: 10 Subcategories vs the 1.1 `ID.SC` Category (5 Subcategories). The new Subcategories cover the **full supplier life cycle** — from pre-acquisition testing (SC-09) to end-of-life tracking (SC-10) — and explicitly include **incident response coordination** with suppliers (SC-05, SC-08).
2. **Governance placement**: by sitting under GOVERN, `GV.SC` is now **board-visible**. The board's cyber committee can ask "what is our supply chain risk program?" and the answer is in GOVERN, not buried under IDENTIFY.
3. **Cross-references to other Functions**: `GV.SC` Subcategories cross-reference ID.AM (supplier inventory), PR.PS (supplier product security), DE.CM (supplier monitoring), RS.MA (supplier incident coordination). A TPRM (third-party risk management) program is a multi-Function program; placing it under GOVERN makes the cross-Function dependencies explicit.

For most orgs, `GV.SC` is the **single largest source of new assessment work** in 2.0 vs 1.1. A 1.1-era assessment that addressed supply chain in 5 Subcategories now has 10 Subcategories to score, and the 5 new ones (SC-05 through SC-10) are rarely fully implemented.

## 4. Mapping GOVERN Subcategories to 800-53 controls

GOVERN maps mostly to the **PM (Program Management)**, **RA (Risk Assessment)**, and **SR (Supply Chain Risk Management)** families of NIST 800-53 Rev 5 [NIST-SP-800-53-Rev5]. The mapping is **many-to-many**: a single GOVERN Subcategory can map to multiple 800-53 controls across families. Representative mappings:

| GOVERN Subcategory | Representative 800-53 controls | Notes |
|--------------------|------------------------------|-------|
| GV.OC-01 (mission understood) | PM-11 (Mission/Business Process Definition), PM-15 (Security/Privacy Groups) | Program Management family |
| GV.OC-03 (legal/regulatory) | PM-9 (Risk Management Strategy), RA-1 (Policy and Procedures) | Cross-family |
| GV.RM-02 (risk appetite) | PM-9 (Risk Management Strategy), PM-8 (Critical Infrastructure Plan) | Program Management family |
| GV.RM-03 (cyber in ERM) | PM-9, PM-11, PM-15 | ERM integration |
| GV.SC-01 (TPRM program) | SR-1 (Policy and Procedures), SR-3 (Supply Chain Controls) | Supply Chain family |
| GV.SC-03 (contracts) | SR-3, SR-5 (Acquisition Strategies) | Contractual requirements |
| GV.SC-04 (supplier assessment) | SR-6 (Supplier Assessments and Reviews) | Assessment activities |
| GV.SC-05 (supplier IR coordination) | SR-8 (Notification Agreements), IR-4 (Incident Handling) | Cross-family (SR + IR) |
| GV.PO-01 (policy) | PM-1 (Information Security Program Plan), all "Policy and Procedures" controls (XX-1) | PM family + per-family XX-1 controls |
| GV.PO-02 (policy reviewed) | PM-1, all "Policy and Procedures" controls | Update cycle |
| GV.OV-01 (performance reviewed) | CA-7 (Continuous Monitoring), PM-6 (Measures of Performance) | Continuous Monitoring + PM |
| GV.OV-03 (security operations reviewed) | CA-2 (Control Assessments), CA-7 | Assessment family |
| GV.RR-01 (leadership accountable) | PM-2 (Senior Information Security Officer), PM-3 (Information Security Resources) | Program Management family |
| GV.RR-03 (resources allocated) | PM-3, PM-4 (Plan of Action and Milestones Process) | Resource planning |

The full curated mapping ships in `data/crosswalks/csf-to-800-53-mod.json` and the analysis lives in `chunks/08-informative-references-crosswalk.md`. The reverse direction (800-53 → CSF) is in `nist-800-53-rmf/chunks/09-crosswalk.md`.

## 5. How GOVERN sets the foundation for the other 5 Functions

The GOVERN-first sequencing rule [NIST-CSF-2.0 §2.1] is not a stylistic preference; it reflects the structural dependency of the other 5 Functions on GOVERN outcomes. Concretely:

- **GOVERN → IDENTIFY**: the risk tolerance (GV.RM-02) and risk management strategy (GV.RM-04) inform the risk assessment (ID.RA) scope. You cannot assess risk without first knowing the org's risk appetite.
- **GOVERN → PROTECT**: the policy (GV.PO-01) and roles (GV.RR) inform access control (PR.AA), training (PR.AT), and platform security (PR.PS). You cannot enforce policies that do not exist.
- **GOVERN → DETECT**: the oversight (GV.OV) and supply chain (GV.SC) inform monitoring (DE.CM) and adverse event analysis (DE.AE). You cannot monitor for things that are not in policy.
- **GOVERN → RESPOND**: the roles (GV.RR) and oversight (GV.OV) inform incident management (RS.MA) and reporting (RS.CO). You cannot respond without an accountable owner and a tested plan.
- **GOVERN → RECOVER**: the oversight (GV.OV) and supply chain (GV.SC) inform recovery planning (RC.RP) and communication (RC.CO). You cannot recover without a tested plan and supplier coordination.

**Practical consequence for the Current Profile**: assess GOVERN first (see `chunks/03-current-profile.md` §4). The GOVERN answers (Who owns this? What is our risk appetite? Where is the board involved?) determine what "good" looks like for the other 5. A Current Profile that starts with PROTECT and gets to GOVERN at the end will produce inconsistent scores because the GOVERN context was not set.

**Practical consequence for Tier setting** (see `chunks/02-tiers-and-profiles.md` §3): the GOVERN Tier acts as a **ceiling** in practice. An org at Tier 1 in GOVERN cannot credibly operate at Tier 3 in PROTECT.

## Cross-references

- `chunks/01-functions-categories.md` — the structural overview; this chunk gives the per-Category deep-dive.
- `chunks/06-enterprise-reporting.md` — the GOVERN deep-dive is the executive-legible appendix of the board report (the GV.OV and GV.MT subcategories populate the KPI/KRI dashboard).
- `chunks/07-implementation-playbook.md` — the supply chain (GV.SC) subcategories are the single largest source of new assessment work in 2.0; the playbook addresses this with a 9-90-365 day sequence.
- `nist-800-53-rmf/chunks/01-standards-and-structure.md` — the 800-53 PM, RA, SR families that GOVERN maps to; the cross-skill sibling for the 800-53 side of the mapping.

## Anti-hallucination

- **Authoritative source**: the 6 GOVERN Categories and their Subcategories are from NIST CSF 2.0 [NIST-CSF-2.0 §2.2] (Feb 26, 2024). Verify the exact Subcategory IDs and wording against the official PDF at https://www.nist.gov/cyberframework. Do not paraphrase the Category codes (`GV.OC`, `GV.RM`, `GV.SC`, `GV.PO`, `GV.OV`, `GV.RR`).
- **CSF 1.1 had a partial GOVERN** (`ID.GV` — 3 Subcategories under Identify). It did not have the 6 Categories described here. Do not attribute `GV.OC`, `GV.RM`, `GV.SC`, `GV.PO`, `GV.OV`, `GV.RR` to 1.1. The expansion from `ID.GV` to the 6 GOVERN Categories is the single largest content change in 2.0.
- **`GV.SC` is the most operationally significant addition** in 2.0. It elevates supply chain from a 5-Subcategory Category under Identify to a 10-Subcategory Category under GOVERN. Most orgs have at most 2-3 of the 10 fully implemented; closing the rest is a 12-24 month program. Do not under-estimate the assessment and remediation effort.
- **GOVERN is the umbrella, not a peer.** GOVERN outcomes set the context for the other 5 Functions; the other 5 are the operational cycle. This is why the assess-GOVERN-first rule exists and why the GOVERN Tier acts as a practical ceiling on the other 5 Tiers.
- **The 800-53 mapping in §4 is representative, not exhaustive.** The full curated mapping is in `data/crosswalks/csf-to-800-53-mod.json` and the analysis is in `chunks/08-informative-references-crosswalk.md`. The mappings above are illustrative; verify against the current NIST Informative References spreadsheet for an authoritative version.
- **GOVERN is not the same as "compliance".** GOVERN outcomes describe the org's cyber risk governance; compliance with specific regulations (HIPAA, PCI, NY DFS 500) is a separate activity that may be expressed using GOVERN Subcategories but is not equivalent to GOVERN. An org can have strong GOVERN outcomes and not be compliant with a specific regulation; conversely, an org can be compliant with a specific regulation and have weak GOVERN outcomes.
