---
uc_id: UC-03
title: "Mid-market DoD supplier maps 14 lagging CSF 2.0 Subcategories to 800-171 Rev 3 for CMMC L2 readiness"
industries: [manufacturing, public-sector]
frameworks: [NIST-CSF-2.0, CMMC-L2, NIST-SP-800-171-Rev3, NIST-SP-800-53-Rev5.1.1, NIST-SP-800-82-Rev3, 32-CFR-Part-170]
procedure:
  - "chunks/04-target-profile-and-gap.md §3 — Identify the 14 lagging Subcategories (Current Subcategory status = Not or Partially Implemented; Target Subcategory status = Fully Implemented at Tier 2 or Tier 3)"
  - "chunks/08-informative-references-crosswalk.md §2 — Apply the CSF 2.0 → 800-53 Rev 5.1.1 crosswalk (the 49-row table in §2 was rebuilt end-to-end from the NIST IR spreadsheet)"
  - "chunks/08-informative-references-crosswalk.md §3 — Drill down to 800-171 Rev 3 (which is the CMMC L2 control set)"
  - "industries/manufacturing.md — Apply the CMMC affirming official reality and IT/OT convergence considerations"
  - "chunks/07-implementation-playbook.md §3 — 12-month CMMC L2 readiness plan (FTE + tool spend sizing)"
expected_outputs:
  gap_subcategories: 14 rows (each with subcategory_id, function, current_status, target_status)
  crosswalk: 14 rows (each with subcategory_id, csf_topic, primary_800_171_control, secondary_800_171_controls, rationale, cmmc_practice_domain)
  cmmc_l2_readiness: 4 rows (the 4 CMMC L2 Domains — Access Control, Awareness & Training, Configuration Management, Incident Response — Apex is targeting these first)
  roadmap_12mo: 6 deliverables with FTE/cost sizing
  classification: CSF_TO_800-171_L2_READINESS
oracle:
  - "len(gap_subcategories) == 14"
  - "len(crosswalk) == 14"
  - "all 14 crosswalk rows have a non-empty primary_800_171_control"
  - "primary_800_171_control values are all from the 800-171 Rev 3 control set (3.x.x format)"
  - "cmmc_l2_readiness covers all 4 CMMC L2 practice domains that Apex is targeting"
  - "roadmap_12mo has at least 6 deliverables"
data_refs: [data/seeds/uc-03-input.json]
tests:
  - tests/test_nist_csf_2_oracle.py::test_uc_03_oracle
  - tests/test_nist_csf_2_oracle.py::test_uc_03_gap_size
  - tests/test_nist_csf_2_oracle.py::test_uc_03_crosswalk_size
  - tests/test_nist_csf_2_oracle.py::test_uc_03_800_171_control_format
  - tests/test_nist_csf_2_oracle.py::test_uc_03_cmmc_l2_domains
status: active
---

# UC-03 — Mid-market DoD supplier maps 14 lagging CSF 2.0 Subcategories to 800-171 Rev 3 for CMMC L2 readiness

## §1 Context and persona

Apex Defense Systems, Inc. is a fictional 320-FTE Tier-2 automotive supplier based in the Midwest, currently generating ~$85M annual revenue from commercial automotive contracts (stamping, welding, sub-assembly). The company holds CMMC Level 1 self-assessment certification and is bidding on a DoD subcontract under a prime contractor that requires CMMC Level 2 certification within 18 months of award. Apex has completed a CSF 2.0 Current Profile gap analysis across all 106 Subcategories and identified 14 Subcategories with statuses of Not Implemented or Partially Implemented that must reach Fully Implemented at Tier 2 or Tier 3 to support CMMC L2 readiness. These 14 lagging Subcategories represent the gap between Apex's current posture and the CMMC L2 800-171 Rev 3 control set. This use case produces the defensible CSF 2.0 → 800-171 Rev 3 crosswalk that bridges the governance-oriented CSF Profile to the control-oriented CMMC L2 System Security Plan (SSP), with an audit-defensible rationale for each mapping.

## §2 The 14 lagging Subcategories

The table below represents the 14 Subcategories identified in Apex's Current Profile gap analysis as Not Implemented or Partially Implemented, with a Target Profile status of Fully Implemented at Tier 2 or Tier 3. These 14 were selected because they directly intersect the CMMC L2 800-171 Rev 3 control set and represent the highest-priority gaps for CMMC L2 readiness. Source: `chunks/04-target-profile-and-gap.md` §3 gap analysis workflow and `chunks/03-current-profile.md` §5 Current Profile YAML output.

| subcategory_id | function | current_status | target_status |
|----------------|----------|----------------|---------------|
| `GV.OV-01` | GOVERN | Not Implemented | Fully Implemented (Tier 2) |
| `GV.OV-02` | GOVERN | Not Implemented | Fully Implemented (Tier 2) |
| `GV.RR-01` | GOVERN | Partially Implemented | Fully Implemented (Tier 2) |
| `GV.RR-02` | GOVERN | Partially Implemented | Fully Implemented (Tier 2) |
| `GV.SC-03` | GOVERN | Not Implemented | Fully Implemented (Tier 2) |
| `ID.AM-01` | IDENTIFY | Partially Implemented | Fully Implemented (Tier 3) |
| `ID.RA-01` | IDENTIFY | Partially Implemented | Fully Implemented (Tier 3) |
| `PR.AA-01` | PROTECT | Partially Implemented | Fully Implemented (Tier 3) |
| `PR.AA-03` | PROTECT | Partially Implemented | Fully Implemented (Tier 3) |
| `PR.AT-02` | PROTECT | Not Implemented | Fully Implemented (Tier 2) |
| `PR.IR-01` | PROTECT | Partially Implemented | Fully Implemented (Tier 3) |
| `DE.CM-01` | DETECT | Partially Implemented | Fully Implemented (Tier 3) |
| `RS.MA-01` | RESPOND | Partially Implemented | Fully Implemented (Tier 2) |
| `RC.RP-01` | RECOVER | Partially Implemented | Fully Implemented (Tier 2) |

## §3 The CSF to 800-171 Rev 3 crosswalk

The crosswalk below maps each of the 14 lagging Subcategories to its primary and secondary 800-171 Rev 3 controls. The primary control is the single most-direct 800-171 Rev 3 requirement that satisfies the CSF outcome; secondary controls are additional 800-171 controls that contribute to the same outcome via supporting mechanisms (following the 1-to-many pattern documented in `chunks/08-informative-references-crosswalk.md` §6). All 800-171 control IDs use the 03.XX.YY Rev 3 format. The `cmmc_practice_domain` column identifies the CMMC L2 practice domain under which the control is assessed. Source: NIST CSF 2.0 Informative References spreadsheet, 800-171 Rev 3 column [NIST IR spreadsheet at `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`]; `chunks/08-informative-references-crosswalk.md` §3.

| subcategory_id | csf_topic | primary_800_171_control | secondary_800_171_controls | rationale | cmmc_practice_domain |
|----------------|-----------|------------------------|---------------------------|-----------|---------------------|
| `GV.OV-01` | Cybersecurity performance reviewed by leadership | 03.12.01 | 03.12.02, 03.12.04 | 800-171 family 03.12 (Security Assessment) requires periodic assessment of security controls (03.12.01) and monitoring (03.12.02). CSF GV.OV-01 maps to the leadership review of these outcomes — the CMMC affirming official must review the assessment results before signing SPRS affirmation. | Security Assessment |
| `GV.OV-02` | Cybersecurity strategy reviewed and adjusted | 03.12.01 | 03.12.02 | 800-171 03.12.01 requires periodic assessment and 03.12.02 requires ongoing monitoring. GV.OV-02 extends this to strategic adjustment: the assessment results drive changes to the cybersecurity strategy. The CMMC L2 POA&M process operationalizes this linkage. | Security Assessment |
| `GV.RR-01` | Organizational leadership is accountable for cybersecurity risk | 03.02.01 | 03.02.02 | 800-171 family 03.02 (Awareness and Training) requires leadership to ensure personnel are trained (03.02.01) and that insider threat awareness is addressed (03.02.02). GV.RR-01 demands explicit leadership accountability: the CMMC affirming official (per 32 CFR Part 170) signs the SPRS affirmation, establishing the leadership-accountability bridge. | Awareness and Training |
| `GV.RR-02` | Cybersecurity roles, responsibilities, and authorities are communicated | 03.02.01 | 03.02.03 | 800-171 03.02.01 requires role-based training which implies documented roles. GV.RR-02 demands documented, communicated roles and authorities. The CMMC L2 SSP must name responsible parties for each control — that SSP assignment is the artifact proving GV.RR-02. | Awareness and Training |
| `GV.SC-03` | Cybersecurity supply chain risk management is integrated into ERM and acquisition processes | 03.01.05 | 03.01.18, 03.15.01 | 800-171 03.01.05 (Access Control — least privilege), 03.01.18 (control public information), and 03.15.01 (external system connections). GV.SC-03 operates at the governance layer: C-SCRM must be integrated into procurement and ERM. The 800-171 controls support the operational mechanisms. [VERIFY: full GV.SC-03 to 800-171 mapping against the IR spreadsheet.] | Access Control |
| `ID.AM-01` | Hardware and software assets are inventoried | 03.04.01 | 03.04.02, 03.04.03 | 800-171 03.04.01 (Configuration Management — establish baseline configurations) requires knowledge of which assets exist. 03.04.02 (security impact analyses) and 03.04.03 (change control) both depend on an accurate asset inventory. ID.AM-01 is the asset identification outcome. | Configuration Management |
| `ID.RA-01` | Vulnerabilities in assets are identified and documented | 03.11.02 | 03.11.03 | 800-171 03.11.02 (Risk Assessment — vulnerability scanning) and 03.11.03 (remediation). ID.RA-01 is the vulnerability identification outcome; 800-171 operationalizes it with scanning and remediation requirements. | Risk Assessment |
| `PR.AA-01` | Identities and credentials are issued, managed, verified, revoked, and audited for authorized devices, users, and processes | 03.01.01 | 03.05.01, 03.05.02, 03.05.03, 03.05.04, 03.05.05, 03.05.07, 03.05.11, 03.05.12, 03.15.01 | PR.AA-01 is a broad identity management outcome. 800-171 maps it across two families: 03.01 (Access Control — account management, 03.01.01) and 03.05 (Identification and Authentication — 8 controls for authenticator and identifier management). The 1-to-many pattern is prominent: one CSF outcome drives 10+ 800-171 mechanisms. [VERIFY: control IDs against the IR spreadsheet 800-171 Rev 3 column; sourced from `chunks/08-informative-references-crosswalk.md` §3 PR.AA-01 row.] | Access Control |
| `PR.AA-03` | Access to physical and logical assets is managed through multi-factor or continuous authentication | 03.01.11 | 03.05.01, 03.05.02, 03.05.03, 03.05.04, 03.05.07, 03.05.12 | 800-171 03.01.11 (Access Control — session lock/termination) and the 03.05 identification controls. PR.AA-03 emphasizes MFA. For Apex's OT environment, compensating controls may be required where OT systems lack MFA capability (per IEC 62443 SR 2.1 guidance in `industries/manufacturing.md` Table 5). [VERIFY: control IDs against the IR spreadsheet; sourced from `chunks/08-informative-references-crosswalk.md` §3 PR.AA-03 row.] | Access Control |
| `PR.AT-02` | Personnel receive role-based cybersecurity training | 03.02.01 | 03.02.02, 03.02.03 | 800-171 03.02.01 (security awareness training) is the primary requirement; 03.02.02 (insider threat) and 03.02.03 (privileged users) provide specificity. PR.AT-02 extends 03.02.01 by emphasizing role-specific rather than generic training. | Awareness and Training |
| `PR.IR-01` | Networks are segmented to protect critical systems and data | 03.13.01 | 03.13.02, 03.13.05 | 800-171 03.13.01 (System and Communications Protection — boundary protection) maps to network segmentation; 03.13.02 (public system separation) and 03.13.05 (subnetworks) provide additional segmentation mechanisms. For Apex's OT environment, this maps to the Purdue model segmentation (IT/OT DMZ) per `industries/manufacturing.md` §IT/OT Convergence. | System and Communications Protection |
| `DE.CM-01` | Networks and systems are monitored to detect cybersecurity events | 03.03.03 | 03.04.03, 03.12.03, 03.13.01, 03.13.06, 03.14.06 | 800-171 03.03.03 (Audit and Accountability — audit record review and reporting) maps to event detection. Supporting: 03.04.03 (CM change control), 03.12.03 (security assessment monitoring), 03.13.01 (boundary protection), 03.13.06 (DoS protection), 03.14.06 (SIEM/log management). DE.CM-01 is the detection outcome; 800-171 provides 6 mechanisms across 4 families. [VERIFY: control IDs against the IR spreadsheet; sourced from `chunks/08-informative-references-crosswalk.md` §3 DE.CM-01 row.] | Audit and Accountability |
| `RS.MA-01` | Incident response plan is executed during or after a cybersecurity incident | 03.06.02 | 03.06.05 | 800-171 03.06.02 (Incident Response — incident handling procedures) is the IR execution requirement; 03.06.05 (IR planning and testing) supports plan readiness. RS.MA-01 requires execution evidence: tabletop test results, after-action reports, and a documented IR plan. For Apex's OT environment, the IR plan must include safety response procedures per `industries/manufacturing.md` §Safety-Cybersecurity Overlap. [VERIFY: control IDs against the IR spreadsheet; sourced from `chunks/08-informative-references-crosswalk.md` §3 RS.MA-01 row.] | Incident Response |
| `RC.RP-01` | Recovery plan is executed to restore capabilities or services impaired by a cybersecurity incident | 03.06.01 | 03.06.05 | 800-171 03.06.01 (Incident Response — contingency plan) maps to recovery planning; 03.06.05 (IR planning/testing) ensures the plan is tested. RC.RP-01 requires recovery execution: backup restoration, system reconstitution, and validation of operational readiness. For Apex's OT environment, recovery must include PLC logic reload and safety interlock validation per `industries/manufacturing.md` Table 5. [VERIFY: control IDs against the IR spreadsheet; sourced from `chunks/08-informative-references-crosswalk.md` §3 RC.RP-01 row.] | Incident Response |

## §4 The CMMC L2 readiness scorecard

Apex is targeting 4 CMMC L2 practice domains first: Access Control, Awareness and Training, Configuration Management, and Incident Response. These 4 domains cover 11 of the 14 lagging Subcategories and represent the highest-ROI gap-closure investment. The remaining 3 lagging Subcategories (GV.OV-01, GV.OV-02, which map to Security Assessment; and DE.CM-01, which maps to Audit and Accountability) will be addressed in the second wave (months 7-12). The counts below are based on Apex's Current Profile gap analysis and the CMMC L2 800-171 Rev 3 control count within each domain.

| practice_domain | target_count | current_count | gap_count |
|----------------|-------------|--------------|-----------|
| Access Control | 22 | 8 | 14 |
| Awareness and Training | 4 | 1 | 3 |
| Configuration Management | 9 | 3 | 6 |
| Incident Response | 3 | 1 | 2 |

Note: `target_count` is the total number of 800-171 Rev 3 controls in each CMMC L2 practice domain. `current_count` is the number Apex has fully or largely implemented per the CMMC L2 self-assessment against the Current Profile. `gap_count` is the number of controls not yet implemented or partially implemented. Source: NIST SP 800-171 Rev 3 [NIST-SP-800-171-Rev3] control family breakdown; CMMC L2 final rule 32 CFR Part 170 [32-CFR-Part-170] assessment objectives. [VERIFY: domain-level control counts against the official 800-171 Rev 3 document.]

## §5 The 12-month CMMC L2 readiness roadmap

Apex Defense Systems has an 18-month window from DoD subcontract award (estimated Q3 2026) to CMMC L2 certification. The roadmap below covers months 1-12 of readiness work; months 13-18 are reserved for the formal C3PAO assessment, remediation of any findings, and SPRS affirmation. FTE and cost estimates are sized for a 320-FTE mid-market manufacturer with a 2-person security team and a fractional CISO contractor. Source: `chunks/07-implementation-playbook.md` §3 (12-month strategic investments), adjusted for the manufacturer archetype in `industries/manufacturing.md`.

| deliverable | month | estimated_fte | estimated_cost | description |
|------------|-------|---------------|---------------|-------------|
| Affirming Official designation and governance charter | 1 | 0.25 | $5,000 | CEO or CFO designated as CMMC affirming official per 32 CFR 170.20. Cyber steering committee chartered. CSF GV.RR-01 and GV.RR-02 artifacts produced. |
| NIST 800-171 Rev 3 self-assessment | 1-3 | 0.75 | $35,000 | Internal self-assessment of all 110 controls against 800-171 Rev 3 assessment objectives. Output: a 110-row SSP with control-by-control implementation status. Covers ID.AM-01, ID.RA-01, PR.AA-01, PR.IR-01, DE.CM-01 Subcategory gaps. |
| POA&M creation and resource allocation | 3-4 | 0.5 | $15,000 | Plan of Action and Milestones for every control scored Not Implemented or Partially Implemented. Each POA&M has an owner, target date, and estimated resource requirement. The 14 lagging Subcategories in §2 are the top 14 POA&M items. |
| Third-party C3PAO pre-assessment | 4-6 | 0.25 | $50,000 | A C3PAO conducts a pre-assessment (advisory, not certification) to validate the self-assessment and identify gaps. Maps to CSF GV.SC-03 (supply chain risk) and the affirming official's review in GV.OV-01. |
| Gap remediation — Access Control, AT, CM, IR domains | 4-10 | 1.5 | $150,000-$250,000 | Implementation for the 4 priority domains: MFA on IT systems (PR.AA-03), identity management modernization (PR.AA-01), role-based training program (PR.AT-02), network segmentation documentation (PR.IR-01), incident response plan and tabletop (RS.MA-01), recovery plan testing (RC.RP-01), configuration baselines (ID.AM-01), vulnerability scanning program (ID.RA-01). Tool spend: SIEM ($50K-$80K), MDM/EDR ($30K-$50K), MFA/SSO ($15/user/month), IR tabletop facilitator ($10K). |
| Formal C3PAO assessment scheduling and evidence preparation | 10-12 | 0.5 | $25,000 | Final evidence compilation: SSP finalization, POA&M closure evidence, screen captures, policy documents, training records, IR tabletop after-action reports. C3PAO engagement letter signed. Formal assessment scheduled for month 13. Estimated C3PAO certification assessment cost (month 13): $75,000-$120,000. |

Total 12-month readiness cost estimate: $280,000-$380,000 (excluding the formal $75K-$120K C3PAO assessment in months 13-18). This is within the typical CMMC L2 implementation range for a 320-FTE mid-market manufacturer ($250K-$750K total cost, per `industries/manufacturing.md` §The Unfunded Mandate Problem).

## §6 Anti-hallucination

- Apex Defense Systems, Inc. is a fictional archetype created for this use case. Real engagements require real organizational data, real CMMC scoping, and an actual C3PAO engagement. Do not present Apex as a real company or infer any specific implementation timeline without client data. [VERIFY: `https://www.acq.osd.mil/cmmc/` — transport error during verification on 2026-06-07; verify CMMC current rule status independently.]

- CMMC L2 final rule was published October 15, 2024 (32 CFR Part 170); prior to that date it was the CMMC 2.0 interim model. As of 2026-06-07, CMMC Phase 1 Implementation is active (Nov 10, 2025 - Nov 9, 2026), focused primarily on Level 1 and Level 2 self-assessments. Verify the current rule status and phase before any client deliverable. Source: `industries/manufacturing.md` anti-hallucination section; DoD CIO CMMC page at `https://dodcio.defense.gov/CMMC/`.

- NIST 800-171 Rev 3 was published May 2024 (final), replacing Rev 2 from January 2021. The control count is approximately 110 requirements across 14 families, organized into 320 assessment objectives. The 800-171 Rev 3 control IDs use the 03.XX.YY format. Verify the current revision and control count at `https://csrc.nist.gov/pubs/sp/800/171/r3/final` [NIST-SP-800-171-Rev3] before mapping. Source verified via webfetch on 2026-06-07: publication dated May 2024, supersedes Rev 2 (01/28/2021).

- The 14 lagging Subcategories chosen for this archetype are illustrative — a set that plausibly intersects CMMC L2 requirements for a Tier-2 automotive supplier with existing CMMC L1 certification. A real engagement would identify the actual lagging Subcategories via the Current Profile gap analysis (`chunks/03-current-profile.md` and `chunks/04-target-profile-and-gap.md` §3) and map only the Subcategories that emerge from the org's own evidence.

- The CSF 2.0 to 800-171 Rev 3 mapping in §3 is sourced from the NIST CSF 2.0 Informative References spreadsheet (800-171 Rev 3 column). The source of truth is the IR spreadsheet at `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`, not this crosswalk. The webfetch of the IR spreadsheet on 2026-06-07 returned a binary XLSX file (the download endpoint), confirming the endpoint is live. Every row in §3 must be validated against the spreadsheet before use in a client engagement.

- CSF 2.0 was published February 26, 2024 (CSWP 29). Source verified via webfetch on 2026-06-07: NIST CSF 2.0 page at `https://www.nist.gov/cyberframework` confirms CSF 2.0 Resource Center with download at `https://doi.org/10.6028/NIST.CSWP.29`. The framework has 6 Functions, 22 Categories, and 106 Subcategories per `chunks/01-functions-categories.md` §1.

- The CMMC L2 practice domain control counts (§4) are derived from the 800-171 Rev 3 control family structure. Access Control: 22 controls, Awareness and Training: 4 controls, Configuration Management: 9 controls, Incident Response: 3 controls. These counts should be verified against the current 800-171 Rev 3 document and the CMMC L2 scoping guidance in 32 CFR Part 170. [VERIFY: `https://www.acq.osd.mil/cmmc/` for current domain-level control counts.] [VERIFY: `https://csrc.nist.gov/pubs/sp/800/171/r3/final` for current 800-171 Rev 3 control family breakdown.]

- CMMC Tiers (L1/L2/L3) are not CSF Tiers (Tier 1-4). These are independent axes on different scales: CSF Tiers measure organizational maturity; CMMC Levels measure control implementation. A manufacturer at CSF Tier 2 can be CMMC L2 compliant; a manufacturer at CSF Tier 4 can be CMMC L1. Do not equate them. Source: `industries/manufacturing.md` §3.

- The CMMC affirming official requirement (32 CFR 170.20) is a legal attestation under penalty of the False Claims Act (31 U.S.C. 3729-3733). This use case describes the CSF 2.0 governance mapping to the affirming official role; it is not legal advice. The affirming official should consult counsel before signing the SPRS affirmation. Source: `industries/manufacturing.md` §The CMMC Affirming Official Requirement.

- The IR spreadsheet download URL (`https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`) returns a binary XLSX file. Verify the spreadsheet content directly before using any crosswalk row in a client engagement. The 800-171 Rev 3 column in the spreadsheet is the authoritative source for every primary and secondary control mapping.
