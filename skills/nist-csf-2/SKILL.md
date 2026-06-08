---
name: nist-csf-2
description: "NIST Cybersecurity Framework 2.0 (Feb 2024): 6 Functions, 22 Categories, 106 Subcategories, Tiers 1-4, Current/Target/Organizational/Community Profiles. The bridge skill between executive risk language and IT controls. Use to assess organizational cybersecurity maturity, build a Current or Target Profile, run a Current/Target gap analysis, produce a 6-function radar for the board, or map CSF to NIST 800-53 / ISO 27001 / SOC 2 / HIPAA / PCI / COBIT. Activate when the user says 'CSF 2.0', 'NIST cybersecurity framework', 'cybersecurity maturity', 'maturity assessment', 'Current Profile', 'Target Profile', '6 functions', 'GOVERN function', 'Tier 1-4', or asks for an executive-legible cyber maturity view."
category: audit-framework
risk: informational
source: "NIST Cybersecurity Framework 2.0 (Feb 26, 2024) — https://www.nist.gov/cyberframework. Companion: NIST SP 1300 (CSF 2.0 Profile success story), NIST SP 1299 (CSF 2.0 small business quick-start), CSF 2.0 Informative References spreadsheet, FIPS 199, NIST SP 800-53 Rev 5 / 5.1.1, NIST SP 800-37 Rev 2 RMF, FedRAMP Rev 5, SOC 2 TSC 2017, ISO 27001:2022, HIPAA Security Rule, PCI DSS v4.0.1, COBIT 2019, NY DFS Part 500, FFIEC CAT, CISA ICS CPG."
date_added: 2026-06-09
version: 0.1.0
status: draft
industries: [financial-services, public-sector, saas-technology, manufacturing]
frameworks: [NIST-CSF-2.0, NIST-SP-800-53-Rev5, NIST-SP-800-53-Rev5.1.1, NIST-SP-800-37-Rev2, NIST-SP-800-171, ISO-27001-2022, HIPAA-Security-Rule, PCI-DSS-4.0.1, SOC-2-TSC-2017, COBIT-2019]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
token_baseline_target:
  input_p90: 12000
  output_p90: 3500
context_budget:
  always_loaded_tokens: 3500      # this SKILL.md (router)
  per_call_typical_tokens: 7000   # router + 1 chunk + 1 industry + 1 UC
  per_call_max_tokens: 16000      # router + all chunks + industry + UC
  per_call_p90_tokens: 9000       # measured after first instrumented run
tags: [csf, csf-2.0, cybersecurity-framework, nist, govern, identify, protect, detect, respond, recover, profile, current-profile, target-profile, maturity, tier, executive, board, crosswalk, 800-53, iso-27001, soc2, hipaa, pci, cobit, govern-function, supply-chain, governance]
---

You are an expert agent performing NIST CSF 2.0-based cybersecurity maturity and risk-governance work. Follow every instruction below precisely. Use official NIST CSF 2.0 terminology exclusively (Functions in ALL CAPS, Categories in `GV.OC` form, Subcategories in `GV.OC-01` form).

# NIST CSF 2.0 Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent. See §11 Routing for the table. CSF 2.0 is the **bridge skill** of the library — the most executive-legible framework in the NIST family. Prefer it when the user is talking to a board, an audit committee, or a non-technical regulator.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Building a **Current Profile** (where the org is today across all 106 Subcategories) or a **Target Profile** (where the org should be).
- Running a **Current/Target gap analysis** and producing a remediation roadmap.
- Selecting a **Tier 1-4** target for the org or a Function.
- Producing a **6-function radar** or board-level maturity scorecard.
- Assessing the **GOVERN function** (new in CSF 2.0): GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC.
- Mapping CSF Subcategories ↔ [NIST-SP-800-53-Rev5] controls, [ISO-27001-2022] Annex A, [SOC-2-TSC-2017] Common Criteria, [HIPAA-Security-Rule] safeguards, [PCI-DSS-4.0.1] requirements, or [COBIT-2019] process goals.
- Answering a customer security questionnaire (CAIQ, SIG Lite, VSAQ) with a CSF Current Profile as the evidence base.
- Producing executive-legible cyber maturity language for a board, audit committee, or regulator (NY DFS, FFIEC, OCC, state RMF).
- Adopting CSF 2.0 as the entry-level framework before a SOC 2 / 800-53 engagement (the "first profile" pattern for Series-A SaaS).

### Do NOT Use This Skill When:
- The user needs the control-by-control detail of 800-53 — use `nist-800-53-rmf` instead; this skill links to it.
- The user needs a financial-statement audit opinion or PCAOB AS 2201 walkthrough — use `coso-internal-controls` and `audit-workpapers`.
- The user needs a SOC 1/2/3 report content map — use `aicpa-soc-reporting`.
- The user needs an ISACA-style IT audit program with COBIT 2019 goals cascade — use `isaca-audit-methodology`.
- The user wants a legal interpretation of FISMA, FedRAMP authorization boundaries, or NY DFS 500 — consult counsel.
- The user is asking about CSF **1.1** specifically — this skill is CSF 2.0 only. The 1.1 → 2.0 delta is summarized in `chunks/01-functions-categories.md` but the 1.1 framework is out of scope.
- Replacing a qualified CISO, 3PAO, or auditor. This skill encodes the framework; it does not certify the practitioner.

## 2. Framework Overview

The NIST Cybersecurity Framework 2.0 [NIST-CSF-2.0 §2] is a voluntary, outcome-based framework published by NIST on February 26, 2024. It organizes cybersecurity risk into **6 Functions** [NIST-CSF-2.0 §2.1], **22 Categories** [NIST-CSF-2.0 §2.2], and **106 Subcategories** [NIST-CSF-2.0 §2.3], and it describes organizational maturity with **4 Tiers** [NIST-CSF-2.0 §3.1] and posture with **4 Profile types** (Current, Target, Organizational, Community) [NIST-CSF-2.0 §3.2]. It is the most executive-legible framework in the NIST family and the only one designed for **both** IT practitioners and executive decision-makers. Companion documents include NIST SP 1299 (small business quick-start) [NIST-SP-1299] and NIST SP 1300 (profile success story) [NIST-SP-1300]. Regulatory alignment spans OMB A-130 [OMB-A-130], NY DFS Part 500 [NY-DFS-Part-500], and FedRAMP Rev 5 baselines [FedRAMP-Rev5]. Its informative references spreadsheet [CSF-2.0-Informative-References] provides crosswalks to NIST SP 800-53 Rev 5.1.1 [NIST-SP-800-53-Rev5.1.1], NIST SP 800-37 Rev 2 RMF [NIST-SP-800-37-Rev2], NIST SP 800-30 Rev 1 risk assessments [NIST-SP-800-30-Rev1], NIST SP 800-61 Rev 2 incident handling [NIST-SP-800-61-Rev2], and sector-specific guidance such as the CISA ICS CPG [CISA-ICS-CPG].

| Layer | Element | Role |
|-------|---------|------|
| Outcome | 6 Functions: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER | The "what" — outcomes the org achieves. |
| Outcome | 22 Categories (e.g., GV.OC, ID.AM, PR.AA, DE.CM, RS.MA, RC.RP) | The "where" — groupings of related outcomes. |
| Outcome | 106 Subcategories (e.g., GV.OC-01, PR.AA-01) | The "how measured" — specific outcomes to assess. |
| Maturity | 4 Tiers: 1 (Partial), 2 (Risk Informed), 3 (Repeatable), 4 (Adaptive) | The "how well" — per-Function maturity indicator. |
| Posture | 4 Profile types: Current, Target, Organizational, Community | The "where we are / where we're going / who's involved". |

**What is new in CSF 2.0 vs 1.1:** the new **GOVERN** function is added (with 6 categories: GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC) and now sits across the top of the framework — GOVERN sets the context for the other 5. The **PROTECT** categories were renamed to 5 categories (PR.AA, PR.AT, PR.DS, PR.PS, PR.IR) and supply-chain risk was elevated to a first-class GOVERN-anchored concern (GV.SC). Profile terminology was formalized: **Current Profile**, **Target Profile**, **Organizational Profile** (the org's posture; contains one or both of Current/Target), and **Community Profile** (sector-coordinating-body output). See `chunks/01-functions-categories.md` for the 1.1-to-2.0 delta table.

**Relationship to other NIST frameworks:** CSF 2.0 outcomes (Subcategories) map cleanly to 800-53 controls via the NIST Informative References spreadsheet (see `chunks/08-informative-references-crosswalk.md` and the curated JSONs in `data/crosswalks/` — added in Wave 2). The **Tier 1-4** scale in CSF is an **organizational maturity** scale; the **Tier 1/2/3** in 800-53 RMF refers to **FIPS 199 impact**. They are different scales on the same word — see `chunks/02-tiers-and-profiles.md` for the reconciliation.

## 3. Core Concepts

### 3.1 The 6 Functions (cheat sheet)

| # | Function | One-line definition | Why it exists |
|---|----------|---------------------|---------------|
| 1 | **GOVERN** | Establish and monitor the org's cyber risk governance | New in 2.0; sets the context for the other 5. |
| 2 | **IDENTIFY** | Understand assets, risks, and exposures | You cannot protect what you have not identified. |
| 3 | **PROTECT** | Put safeguards in place | Preventive controls. |
| 4 | **DETECT** | Discover cybersecurity events | Detective controls. |
| 5 | **RESPOND** | Act on detected events | Incident response. |
| 6 | **RECOVER** | Restore capabilities | Resilience and continuity. |

Mnemonic: **"Good Identities Protect, Detect, Respond, Recover"** (G-I-P-D-R-R). GOVERN is the umbrella; the other 5 are the cycle.

### 3.2 Categories (22 total) and Subcategories (106 total)

Categories are the second-level grouping. Each Category has 2-6 Subcategories. The full list is in `chunks/01-functions-categories.md` and the canonical JSON ships in `data/crosswalks/csf-2-0-subcategories.json` (added in Wave 2). Examples: `GV.OC` (Organizational Context), `GV.SC` (Cybersecurity Supply Chain Risk Management), `ID.AM` (Asset Management), `PR.AA` (Identity, Authentication, and Access Control — renamed in 2.0), `DE.CM` (Continuous Monitoring), `RS.MI` (Mitigation), `RC.RP` (Recovery Planning).

### 3.3 Tiers 1-4 (maturity)

| Tier | Name | Characteristic | Process | Org-wide risk mgmt | External participation |
|------|------|----------------|---------|--------------------|------------------------|
| 1 | Partial | Ad hoc, reactive | Not formalized | Not informed by org objectives | None |
| 2 | Risk Informed | Risk-informed but not org-wide | Some formalization | Approved by mgmt but not org-wide | Limited |
| 3 | Repeatable | Formally approved, org-wide | Documented and consistent | Org-wide, informed by risk | Receives and shares |
| 4 | Adaptive | Continuously improved | Adaptive, learned from incidents | Org-wide, informed by org risk | Active sharing |

Tiers are **per Function** — a single org can be Tier 3 in PROTECT and Tier 1 in GOVERN. The 6-function radar (see `chunks/06-enterprise-reporting.md`) is the visualization.

### 3.4 Profiles (4 types)

- **Current Profile** — the "as-is" outcomes achieved today, scored by Subcategory. Built in `chunks/03-current-profile.md`.
- **Target Profile** — the "to-be" outcomes desired, given risk tolerance, business objectives, and applicable regulation. Built in `chunks/04-target-profile-and-gap.md`.
- **Organizational Profile** — the org's unique posture; can be a Current, Target, or hybrid view. The unit of comparison between orgs.
- **Community Profile** — published by a sector-coordinating body (e.g., a financial-services ISAC, HHS for healthcare). Org Profiles align to a Community Profile.

The **gap** (Target − Current) is the work plan. See `chunks/04-target-profile-and-gap.md`.

## 4. Decision Logic (summary)

Full logic in chunks. Summary of "which framework":

| User need | Framework | Skill |
|-----------|-----------|-------|
| Executive board / committee report | CSF 2.0 | **this skill** |
| Customer security questionnaire (CAIQ/SIG/VSAQ) | CSF 2.0 + SOC 2 evidence | this skill + `aicpa-soc-reporting` |
| Federal / DoD / FedRAMP ATO | 800-53 / RMF | `nist-800-53-rmf` |
| SOX 404 / ICFR / PCAOB AS 2201 | COSO ICIF | `coso-internal-controls` |
| SOC 1 / SOC 2 / SOC 3 report content | AICPA TSC | `aicpa-soc-reporting` |
| IT audit / COBIT 2019 / ISACA | ISACA methodology | `isaca-audit-methodology` |
| Workpaper / finding format | PCAOB AS 1215 | `audit-workpapers` |
| Entry-level first framework (Series A SaaS) | CSF 2.0 → SOC 2 → 800-53 | **this skill** as the start |

- **Tier selection is not normative** in CSF 2.0 [NIST-CSF-2.0 §3.1] — see `chunks/02-tiers-and-profiles.md` for the heuristic.
- **GOVERN-first assessment** [NIST-CSF-2.0 §2.1] — assess GOVERN before the other 5 Functions because it sets the context. See `chunks/03-current-profile.md`.
- **CSF Tier 1-4 ≠ 800-53 "Tier 1-3"** [FIPS-199] [NIST-SP-800-53-Rev5] — CSF Tiers = organizational maturity; 800-53 Tiers = FIPS 199 impact. Same word, different scale.

## 5. Procedure Templates (summary)

- **First CSF Current Profile** (1-day pattern) — `use-cases/uc-01-first-organizational-profile.md`.
- **Board maturity report** (6-function radar + 12-month plan) — `use-cases/uc-02-board-maturity-report.md`.
- **Current/Target gap → 800-53 mapping** (for federal customer) — `use-cases/uc-03-csf-to-800-53-crosswalk.md`.
- **Build Current Profile** (per-Function scoring) — `chunks/03-current-profile.md §Procedure`.
- **Build Target Profile + Gap** — `chunks/04-target-profile-and-gap.md §Procedure`.
- **GOVERN-only deep dive** — `chunks/05-govern-function.md §Procedure`.
- **Implementation playbook** (small-org / mid-market / large-enterprise personas) — `chunks/07-implementation-playbook.md §Procedure`.

## 6. Output Templates (summary)

- **Current Profile** YAML (per Subcategory: `status`, `evidence_refs`, `tier_indicator`, `owner`, `notes`) — `chunks/03-current-profile.md §Output template`.
- **Target Profile + Gap Analysis Table** — `chunks/04-target-profile-and-gap.md §Output template`.
- **6-function radar** (Mermaid or ASCII) — `chunks/06-enterprise-reporting.md §Output template`.
- **Board deck outline** (12 slides) — `chunks/06-enterprise-reporting.md §Board deck template`.
- **Cross-framework mapping** (CSF Subcategory → 800-53 / ISO / SOC 2 / HIPAA / PCI / COBIT) — `chunks/08-informative-references-crosswalk.md §Output template`.
- **Roadmap** (90-day or 12-month, prioritized) — `chunks/07-implementation-playbook.md §Output template`.

## 7. Cross-References (summary)

This skill is part of the 6-skill library. The most-used siblings:

- `nist-800-53-rmf` — the control-catalog sibling; use for 800-53 control selection, SAR/POA&M templates, and the authoritative CSF → 800-53 mapping (the 800-53-rmf skill's crosswalk chunk at `nist-800-53-rmf/chunks/09-crosswalk.md` has a 1-paragraph CSF 2.0 entry; our `chunks/08-informative-references-crosswalk.md` is the curated reverse).
- `isaca-audit-methodology` — COBIT 2019 PAM maturity scale maps to CSF Tiers 1-4 (Tier 1 ↔ PAM 0-1, Tier 2 ↔ PAM 2, Tier 3 ↔ PAM 3, Tier 4 ↔ PAM 4-5).
- `coso-internal-controls` — GOVERN (GV.OV, GV.PO) maps to COSO Principles 1, 4, 12; gap priority borrows Significant Deficiency / Material Weakness classification.
- `aicpa-soc-reporting` — SOC 2 Common Criteria map to CSF Subcategories (see `chunks/08-informative-references-crosswalk.md`); SOC 2 Type II is the natural precursor to a CSF profile for a SaaS.
- `audit-workpapers` — the 5-part finding pattern (Condition, Criteria, Cause, Effect, Recommendation) is reused for gap items; evidence is structured as workpapers per PCAOB AS 1215.

External: NY DFS Part 500, FFIEC CAT, CISA ICS CPG, FIPS 199, FedRAMP Rev 5, CMMC 2.0, ISO 27701, HITRUST CSF (related-but-distinct).

## 8. Worked Examples (summary)

Full worked examples live in `use-cases/`. Each has complete input, procedure, expected output, and oracle.

| UC | Title | Industry | Key output |
|----|-------|----------|------------|
| UC-01 | First-profile pattern: 30-FTE Series-A SaaS, Tier 1→2.5, 9-item 90-day roadmap | saas-technology | Current Profile, Target Profile, roadmap, 1-page board update |
| UC-02 | Board maturity report: $20B regional bank, 6-function radar, 12-month $4M plan | financial-services | Radar, GOVERN deep-dive appendix, 12-slide board deck |
| UC-03 | Current/Target gap → 800-53 mapping: $500M mid-market manufacturer, 14 lagging subcategories, 12-month DoD-customer-ready roadmap | manufacturing, public-sector | Crosswalk, 14-item remediation table with 800-53 control IDs |

## 9. Anti-Hallucination Disclaimers

- **Subcategory count is 106** in CSF 2.0. The number 108 is the count for CSF 1.1, not 2.0. Gaps in numbering (e.g., DE.CM-04 absent) are deliberate and indicate relocated 1.1 subcategories — see CSF 2.0 PDF p.15.
- **GOVERN is new in 2.0**; do not attribute GOVERN categories (GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC) to CSF 1.1. The 1.1 framework had 5 Functions (no GOVERN). Note: `GV.SR` and `GV.MT` are not valid CSF 2.0 category codes and must not appear in any output.
- **PROTECT categories were renamed in 2.0** to 5 categories (PR.AA, PR.AT, PR.DS, PR.PS, PR.IR) — replacing the 1.1-era PR.AC, PR.AT, PR.DS, PR.IP, PR.MA, PR.PT. See `chunks/01-functions-categories.md` for the 1.1-to-2.0 delta.
- **CSF Tiers 1-4 ≠ 800-53 Tiers 1-3.** CSF Tiers measure organizational maturity (how well the org does cyber). 800-53 Tiers measure FIPS 199 impact (Low/Moderate/High for C, I, A). Same word, different scales.
- **The Implementation Examples appendix is illustrative, not normative** — cite it for context, do not reproduce it as authoritative.
- **Tier selection is not a normative algorithm** — CSF 2.0 describes Tier characteristics; the org picks its own Tier based on risk tolerance.
- **No quantitative risk score** — CSF 2.0 is maturity-based, not risk-score-based. Do not invent a numeric score.
- **This skill is CSF 2.0 only** — CSF 1.1 is not represented.

> This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| NIST-CSF-2.0 | Cybersecurity Framework 2.0 | NIST | 2.0 (Feb 26, 2024) | 2026-06-09 | https://www.nist.gov/cyberframework |
| NIST-SP-800-53-Rev5 | Security and Privacy Controls for Information Systems and Organizations | NIST | Rev 5 (Sept 2020) | 2026-06-09 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| NIST-SP-800-53-Rev5.1.1 | Security and Privacy Controls (Rev 5.1.1) | NIST | Rev 5.1.1 (2024) | 2026-06-09 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| NIST-SP-800-37-Rev2 | Risk Management Framework for Information Systems and Organizations | NIST | Rev 2 (Dec 2018) | 2026-06-09 | https://csrc.nist.gov/pubs/sp/800/37/r2/final |
| NIST-SP-800-171 | Protecting Controlled Unclassified Information in Nonfederal Systems | NIST | Rev 3 (2024) | 2026-06-09 | https://csrc.nist.gov/pubs/sp/800/171/r3/final |
| FIPS-199 | Standards for Security Categorization | NIST | FIPS 199 (Feb 2004) | 2026-06-09 | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf |
| NIST-SP-800-30-Rev1 | Guide for Conducting Risk Assessments | NIST | Rev 1 (Sept 2012) | 2026-06-09 | https://csrc.nist.gov/pubs/sp/800/30/r1/final |
| NIST-SP-800-61-Rev2 | Computer Security Incident Handling Guide | NIST | Rev 2 (Aug 2012) | 2026-06-09 | https://csrc.nist.gov/pubs/sp/800/61/r2/final |
| NIST-SP-800-82-Rev3 | Guide to Industrial Control Systems (ICS) Security | NIST | Rev 3 (2023) | 2026-06-09 | https://csrc.nist.gov/pubs/sp/800/82/r3/final |
| NIST-SP-1300 | CSF 2.0 Profile Success Story | NIST | 2024 | 2026-06-09 | https://www.nist.gov/cyberframework |
| NIST-SP-1299 | CSF 2.0 Small Business Quick-Start Guide | NIST | 2024 | 2026-06-09 | https://www.nist.gov/cyberframework |
| FedRAMP-Rev5 | FedRAMP Baselines and ConMon Strategy Guide | FedRAMP PMO | Rev 5 | 2026-06-09 | https://www.fedramp.gov/resources/ |
| OMB-A-130 | Managing Information as a Strategic Resource | OMB | July 28, 2016 | 2026-06-09 | https://www.whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/memoranda/2016/m-16-17.pdf |
| ISO-27001-2022 | Information security management systems — Requirements | ISO/IEC | 2022 | 2026-06-09 | https://www.iso.org/standard/27001 |
| SOC-2-TSC-2017 | Trust Services Criteria | AICPA | 2017 (TSP §100, 2022 revised points of focus) | 2026-06-09 | https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 |
| HIPAA-Security-Rule | 45 CFR § 164.302–164.318 | HHS | as amended | 2026-06-09 | https://www.hhs.gov/hipaa/for-professionals/security/ |
| PCI-DSS-4.0.1 | Payment Card Industry Data Security Standard | PCI SSC | v4.0.1 (2024) | 2026-06-09 | https://www.pcisecuritystandards.org/document_library |
| COBIT-2019 | Governance and Management Objectives | ISACA | 2019 | 2026-06-09 | https://www.isaca.org/resources/cobit |
| NY-DFS-Part-500 | Cybersecurity Requirements for Financial Services Companies | NY DFS | 23 NYCRR Part 500 (as amended 2023) | 2026-06-09 | https://www.dfs.ny.gov/industry_guidance/cyber_finance |
| FFIEC-CAT | Cybersecurity Assessment Tool | FFIEC | v2.x (2024) | 2026-06-09 | https://www.ffiec.gov/cyberassessmenttool.htm |
| CISA-ICS-CPG | Cross-Sector Industrial Control Systems Cybersecurity Performance Goals | CISA | 1.0 (2024) | 2026-06-09 | https://www.cisa.gov/ics-cybersecurity-performance-goals |
| CMMC-2.0 | Cybersecurity Maturity Model Certification | DoD | 2.0 | 2026-06-09 | https://dodcio.defense.gov/CMMC/ |
| CSF-2.0-Informative-References | NIST CSF 2.0 Informative References spreadsheet (crosswalk source of truth) | NIST | 2024 (OLIR catalog) | 2026-06-09 | https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all |

In-body citations use the form `[LABEL §N]` and resolve to this manifest.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| Intent / trigger | Chunk to load |
|------------------|---------------|
| "what is CSF" / "Functions / Categories" / "106 subcategories" / "structure of CSF" / "GOVERN function" | `chunks/01-functions-categories.md` |
| "Tiers" / "Current / Target Profile" / "profile types" / "what is a Profile" / "how do we score ourselves" | `chunks/02-tiers-and-profiles.md` |
| "build a CSF profile" / "first profile" / "Tier assessment" / "as-is" / "where are we today" | `chunks/03-current-profile.md` |
| "where are we weak" / "maturity gap" / "Target profile" / "roadmap" / "remediation plan" | `chunks/04-target-profile-and-gap.md` |
| "GOVERN function" / "GV.OC" / "GV.RM" / "GV.SC" / "GV.PO" / "GV.OV" / "board oversight" / "supply chain governance" | `chunks/05-govern-function.md` |
| "board report" / "executive summary" / "6-function radar" / "KPI" / "KRI" / "maturity trend" | `chunks/06-enterprise-reporting.md` |
| "implement CSF" / "how to improve" / "quick wins" / "first 90 days" / "phased rollout" | `chunks/07-implementation-playbook.md` |
| "800-53 crosswalk" / "CSF subcategory mapping" / "ISO / SOC 2 / HIPAA / PCI / COBIT crosswalk" / "informative references" | `chunks/08-informative-references-crosswalk.md` |

**Industries** (load matching file from `industries/`): financial-services, public-sector, saas-technology, manufacturing. See `industries/_index.md` for the 4-quadrant view.

**Use cases** (load matching file from `use-cases/`): UC-01 (first profile, Series-A SaaS), UC-02 (board report, regional bank), UC-03 (CSF → 800-53, DoD supplier).

## 12. Quick Reference

The minimum cycle (always-loaded; no chunk needed for the high-level flow):

1. **Orient** — 6 Functions: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER. Mnemonic: "Good Identities Protect, Detect, Respond, Recover".
2. **Current Profile** — score all 106 Subcategories (Not Implemented / Partially / Largely / Fully) → `chunks/03-current-profile.md`. Output: Current Profile YAML.
3. **Target Profile** — set per-Function Tier target → `chunks/04-target-profile-and-gap.md`. Output: Gap Analysis Table.
4. **Remediate** — prioritize gaps; 9-90-365 day roadmap → `chunks/07-implementation-playbook.md`.
5. **Report** — 6-function radar for the board → `chunks/06-enterprise-reporting.md`.
6. **Crosswalk** — when the same evidence must satisfy 800-53 / SOC 2 / ISO / HIPAA / PCI → `chunks/08-informative-references-crosswalk.md`.

For board/executive questions → `chunks/05-govern-function.md` (GOVERN is the executive language). For federal/DoD/FedRAMP → hand off to `nist-800-53-rmf` and the curated crosswalks in `data/crosswalks/` (added in Wave 2).
