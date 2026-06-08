---
uc_id: UC-01
title: "Series-A SaaS builds first Organizational Profile (Tier 1→2) and identifies 5 highest-impact Subcategories for the 90-day roadmap"
industries: [saas-technology]
frameworks: [NIST-CSF-2.0, NIST-SP-800-53-Rev5.1.1, SOC-2-TSC-2017]
procedure:
  - "chunks/02-tiers-and-profiles.md — Pick Tier 2 (Risk Informed) as the Target Profile baseline for most Functions; Tier 3 (Repeatable) for GOVERN/IDENTIFY/PROTECT in 12 months."
  - "chunks/03-current-profile.md §5 — Build the Current Profile YAML by scoring each of the 106 Subcategories (Not/Partially/Largely/Fully Implemented)."
  - "chunks/03-current-profile.md §6 — Worked example: 50-FTE B2B SaaS archetype, 6 representative Subcategory scores, function-level Tier rollup."
  - "chunks/04-target-profile-and-gap.md §3 — Compare Current vs Target, output the Gap Analysis Table."
  - "chunks/04-target-profile-and-gap.md §4 — Prioritize gaps using the 2x2 (risk reduction vs cost) matrix; pick the top 5."
  - "chunks/07-implementation-playbook.md §1 — Stand up the cyber steering committee (covers GV.OV-01)."
  - "chunks/07-implementation-playbook.md §1 — Publish the cybersecurity policy (covers GV.PO-01)."
  - "chunks/07-implementation-playbook.md §1 — Enable MFA on all admin accounts (covers PR.AA-03)."
expected_outputs:
  current_profile:
    org: "DataRelay Inc."
    org_size: "50 FTE"
    current_tier_by_function: { GV: T1, ID: T1, PR: T2, DE: T1, RS: T1, RC: T1 }
    subcategory_scores: 6 representative rows (each with subcategory_id, function, status, evidence, owner)
  target_profile:
    org: "DataRelay Inc."
    target_tier_by_function_12mo: { GV: T3, ID: T3, PR: T3, DE: T2, RS: T2, RC: T2 }
  gap_analysis:
    prioritization: 5 rows (each with subcategory_id, current_status, target_status, delta, risk_reduction_score, cost_score, quadrant)
  roadmap_90_day: 5 deliverables
  classification: FIRST_ORGANIZATIONAL_PROFILE
oracle:
  - "current_tier_by_function[GV] == T1"
  - "current_tier_by_function[PR] == T2"
  - "len(subcategory_scores) == 6"
  - "len(gap_analysis.prioritization) == 5"
  - "all 5 of: cyber steering committee, cybersecurity policy, MFA on admin accounts, asset inventory scope, incident response plan are in roadmap_90_day"
  - "subcategory scores use valid status enum (Not|Partially|Largely|Fully)"
data_refs: [data/seeds/uc-01-input.json]
tests:
  - tests/test_nist_csf_2_oracle.py::test_uc_01_oracle
  - tests/test_nist_csf_2_oracle.py::test_uc_01_subcategory_status_enum
  - tests/test_nist_csf_2_oracle.py::test_uc_01_gap_prioritization_size
status: active
---

# UC-01 — Series-A SaaS builds first Organizational Profile (Tier 1→2)

## §1 Context and persona

**DataRelay Inc.** is a fictional 50-FTE B2B SaaS company providing analytics connectors to 6 mid-market customers, including 1 enterprise account preparing to demand SOC 2 Type II in 12 months. The company processes B2B contact data (~80,000 records), runs on AWS commercial with KMS-encrypted RDS, and has no dedicated security hire — security is 0.5 FTE inside a 4-person IT team. Pre-engagement, DataRelay has no formal cybersecurity program: no documented policy, no cyber steering committee, no MFA on admin accounts, no tested incident response plan, and no asset inventory beyond AWS Config. The current state is Tier 1 (Partial) across GOVERN, IDENTIFY, DETECT, RESPOND, and RECOVER, and Tier 2 (Risk Informed) for PROTECT because the engineering team already implements encryption-at-rest and SSO for production.

This use case walks through the 5-step procedure to build a defensible first Organizational Profile, identify the 5 highest-impact gaps, and produce a 90-day roadmap at an all-in cost of $0-15K and approximately 25% of one engineer's time. The fictional archetype mirrors the SaaS industry view in `industries/saas-technology.md` and the 90-day quick-wins playbook in `chunks/07-implementation-playbook.md` §1.

## §2 The 5-step procedure

**Step 1 — Pick Tier targets.** Use `chunks/02-tiers-and-profiles.md` to select Tier 2 (Risk Informed) as the Target Profile baseline for most Functions, and Tier 3 (Repeatable) for GOVERN, IDENTIFY, and PROTECT in 12 months. In practice for DataRelay, this means the 90-day sprint targets Tier 2 across all Functions (the board doesn't yet exist for Tier 3 GOVERN), and the 12-month horizon targets Tier 3 for the three Functions that enterprise customers most often scrutinize: governance, asset management, and access controls. The Tier selection reflects the SaaS archetype's regulatory profile — unregulated B2B SaaS with no PHI/PCI — and the enterprise customer's stated requirement for "Tier 3-ish" cyber maturity before contract renewal.

**Step 2 — Build the Current Profile.** Use `chunks/03-current-profile.md` §5 to score each of the 106 Subcategories (Not Implemented / Partially Implemented / Largely Implemented / Fully Implemented) and emit a Current Profile YAML with evidence references, owners, and function-level Tier rollups. In practice, the 0.5-FTE engineer spends 2 weeks gathering documentation (AWS Config exports for ID.AM-01, KMS key policies for PR.DS-01, the drafted-but-untested IR plan for RS.MA-01) and interviewing the IT team. The Current Profile reveals DataRelay is already Largely or Fully Implemented on approximately 30 Subcategories — mostly in PROTECT — and Not Implemented on approximately 45 Subcategories, concentrated in GOVERN and DETECT. The scoring follows the GOVERN-first heuristic from `chunks/02-tiers-and-profiles.md` §3: assess GV.OC, GV.RM, GV.PO first, because the governance context determines what "good" looks like for the operational Functions.

**Step 3 — Use the worked example as a sanity check.** `chunks/03-current-profile.md` §6 provides the 50-FTE B2B SaaS archetype with 6 representative Subcategory scores and a function-level Tier rollup (GOVERN 1.5, IDENTIFY 2.5, PROTECT 3.0, DETECT 1.5, RESPOND 2.0, RECOVER 2.5). In practice, compare DataRelay's real scores against this fictional baseline: if DataRelay's PROTECT is scoring below 2.0, the assessment likely has evidence-gathering gaps (the engineering team's existing controls are not being captured). If GOVERN scores above 1.5, the self-assessment may be aspirational (the org has no board, no policy, no risk appetite statement — it cannot credibly exceed Tier 1 in GOVERN). This sanity check prevents both under-assessment (missing what's already in place) and over-assessment (claiming maturity without evidence).

**Step 4 — Compare Current vs Target and run the gap analysis.** Use `chunks/04-target-profile-and-gap.md` §3 to compute the delta for each Subcategory and output the Gap Analysis Table. The gap is Target status minus Current status: a Subcategory at Not Implemented targeting Largely Implemented is a 2-step gap; Not Implemented targeting Fully Implemented is a 3-step gap. In practice, DataRelay's 12-month target (Tier 3 for GV/ID/PR, Tier 2 for DE/RS/RC) produces approximately 25 Subcategories with a non-zero delta. The assessment focus is on the 5 highest-delta Subcategories because the first 90 days cannot close all gaps.

**Step 5 — Prioritize using the 2x2 matrix and produce the 90-day roadmap.** Use `chunks/04-target-profile-and-gap.md` §4 to place each gap into one of four quadrants (Quick Win / Strategic Investment / Fill-in / Deprioritize) based on risk reduction vs cost of implementation. Pick the top 5 from the Quick Win quadrant (high risk reduction, low cost) and feed them into `chunks/07-implementation-playbook.md` §1 as the 90-day deliverables. In practice, DataRelay's top 5 are all documentation-and-configuration items requiring no tool acquisition.

## §3 The 6-Subcategory Current Profile

Per `chunks/03-current-profile.md` §6. The 6 representative Subcategory scores for the DataRelay archetype (chosen because they map to the 5 quick-win priorities + 1 PROTECT baseline):

| Subcategory | Function | Status | Evidence | Owner |
|-------------|----------|--------|----------|-------|
| GV.OV-01 (cyber steering committee) | GOVERN | Not Implemented | No committee exists; no charter; no quarterly meeting cadence | CEO (proposed) |
| GV.PO-01 (cybersecurity policy) | GOVERN | Not Implemented | No written policy; informal Slack-channel guidelines | VP Engineering (proposed) |
| PR.AA-03 (MFA on admin accounts) | PROTECT | Largely Implemented | AWS IAM enforces MFA on root; per-user MFA enforcement on prod accounts is partial; service accounts lack MFA | VP Engineering |
| PR.DS-01 (data-at-rest encryption) | PROTECT | Fully Implemented | RDS instances all use KMS encryption; S3 buckets enforce SSE-KMS; EBS volumes encrypted | VP Engineering |
| ID.AM-01 (asset inventory) | IDENTIFY | Partially Implemented | AWS Config tracks AWS-side assets; no inventory of SaaS subscriptions, GitHub repos, or workstation endpoints | VP Engineering |
| RS.MA-01 (incident response plan) | RESPOND | Not Implemented | No written IR plan; no on-call rotation; no communication tree | VP Engineering (proposed) |

**Function-level Tier rollup (per `chunks/03-current-profile.md` §3.3):** GOVERN T1, IDENTIFY T1, PROTECT T2, DETECT T1, RESPOND T1, RECOVER T1 (per the §3.3 median-status heuristic applied to the 106-Subcategory full scoring; the 6 above are illustrative).

## §4 The 5-priority Gap Analysis

Per `chunks/04-target-profile-and-gap.md` §3-§4. The top 5 gaps from the 2x2 prioritization matrix (high risk reduction, low cost quadrant):

| Subcategory | Current → Target | Delta | Risk reduction | Cost | Quadrant |
|-------------|------------------|-------|----------------|------|----------|
| GV.OV-01 (cyber steering committee) | Not → Fully | 3 | High | Low ($0) | Quick Win |
| GV.PO-01 (cybersecurity policy) | Not → Fully | 3 | High | Low ($0-2K) | Quick Win |
| PR.AA-03 (MFA on admin accounts) | Largely → Fully | 1 | High | Low ($0-5K) | Quick Win |
| ID.AM-01 (asset inventory scope) | Partially → Largely | 1 | High | Low ($0-3K) | Quick Win |
| RS.MA-01 (incident response plan) | Not → Fully | 3 | High | Low ($0-5K) | Quick Win |

**All 5 fall in the Quick Win quadrant** because they are documentation-and-configuration items (no tool acquisition). The 2x2 matrix methodology is in `chunks/04-target-profile-and-gap.md` §4.

## §5 The 90-day roadmap

| Week | Deliverable | Subcategory covered | Owner | Cost estimate | Notes |
|------|-------------|---------------------|-------|---------------|-------|
| W1 | Stand up cyber steering committee (charter, meeting cadence) | GV.OV-01 | CEO + VP Engineering | $0 | 1-page charter; 4 quarterly meetings scheduled |
| W2 | Publish cybersecurity policy (5-page doc referencing CSF 2.0 + SOC 2) | GV.PO-01 | VP Engineering | $0-2K (policy author time) | Covers NIST CSF 2.0 + SOC 2 scope |
| W3 | Enable MFA on all admin accounts (prod + staging) | PR.AA-03 | VP Engineering | $0-5K (tooling) | AWS IAM + service account audit |
| W4-8 | Define asset inventory scope (AWS + SaaS + endpoints) | ID.AM-01 | VP Engineering | $0-3K | First-pass inventory YAML, 1 day of work |
| W9-12 | Publish incident response plan (template, on-call rotation, comm tree) | RS.MA-01 | VP Engineering | $0-5K | Covers the SOC 2 CC7.x expectations |
| | **Total** | | | **$0-15K** | ~25% of one engineer's time over 12 weeks |

## §6 Anti-hallucination section

- **DataRelay Inc. is a fictional archetype.** Real engagements should use a real org profile, real customer requirements, and a real assessment timeline.
- **Tier numbering: T1=Partial, T2=Risk Informed, T3=Repeatable, T4=Adaptive** (per NIST CSF 2.0 §3.1). T2 is the most common target for a Series-A SaaS in the 90-day horizon.
- **Status enum: Not Implemented | Partially Implemented | Largely Implemented | Fully Implemented** (per NIST CSF 2.0 §3.2). The 4-level scale is the official NIST scale.
- **MFA on admin accounts covers PR.AA-03 specifically.** Broader identity controls cover PR.AA-01 (identifiers), PR.AA-02 (authentication), PR.AA-04 (access reviews), PR.AA-05 (least privilege), PR.AA-06 (privileged account management) separately. Enabling MFA is one of the highest-leverage Tier 1→2 moves for a young SaaS.
- **The 90-day cost estimate ($0-15K) is a heuristic.** Real engagements depend on whether DataRelay already pays for an IdP (e.g., Okta, Google Workspace), what the existing AWS configuration includes, and whether the engineer wears other hats. The estimate is the *delta* cost; the *fully-loaded* cost is the engineer's existing salary.
- **The function-level Tier rollup heuristic in `chunks/03-current-profile.md` §3.3 is one of several valid approaches.** Real engagements may use weighted averages, rule-based rollups (e.g., any "Not Implemented" Subcategory pulls the function down by one Tier), or judgmental rollups. The choice should be documented in the assessment methodology section of the board report.
- **NIST CSF 2.0 Quick Start Guides (SP 1299, SP 1300, SP 1301, SP 1302)** are the primary practitioner resources for the Organizational Profile methodology. The Organizational Profile template (XLSX) on the NIST CSF 2.0 website is the authoritative input format. [VERIFY: SP 1300 title — was previously thought to be "Small Business Quick Start Guide" but may have a different official title. Confirm against the current NIST CSF 2.0 QSGs page.]
