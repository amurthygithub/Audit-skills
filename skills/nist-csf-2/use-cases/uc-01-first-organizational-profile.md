---
uc_id: UC-01
title: "Series-A SaaS builds first Organizational Profile (Tier 1→2) and identifies the 5 highest-impact Subcategories for the 90-day roadmap"
industries: [saas-technology]
frameworks: [NIST-CSF-2.0, NIST-SP-800-53-Rev5.1.1, SOC-2-TSC-2017]
procedure:
  - "chunks/02-tiers-and-profiles.md — Pick Tier 2 (Risk Informed) as the Target Profile baseline (90 days); Tier 3 for GOVERN/IDENTIFY/PROTECT at 12 months."
  - "chunks/03-current-profile.md §5 — Build the Current Profile YAML by scoring Subcategories (this skill's Not/Partially/Largely/Fully convention — not a NIST scale)."
  - "chunks/03-current-profile.md §6 — Worked example: 50-FTE B2B SaaS archetype (a DIFFERENT illustrative scoring of the same archetype; the seed below is the tested fixture)."
  - "chunks/04-target-profile-and-gap.md §3 — Compare Current vs Target, output the Gap Analysis Table."
  - "chunks/04-target-profile-and-gap.md §4 — Prioritize gaps using the 2x2 (risk reduction vs cost) matrix; pick the top 5."
  - "chunks/07-implementation-playbook.md §1 — 90-day quick wins (policy, IR plan, inventory scope, governance cadence)."
expected_outputs:
  current_profile:
    org: "DataRelay Inc."
    org_size: "50 FTE"
    current_tier_by_function: { GV: T1, ID: T2, PR: T2, DE: T2, RS: T1, RC: T1 }
    subcategory_scores: 8 rows from the seed (each with subcategory_id, status, evidence)
  gap_analysis:
    prioritization: 5 rows (the seed's lowest-status Subcategories — GV.OC-01, GV.PO-01, RS.MA-01, ID.AM-01, PR.AA-01)
  roadmap_90_day: 5 deliverables (one per prioritized gap)
  classification: FIRST_ORGANIZATIONAL_PROFILE
oracle:
  - "current_tier_by_function[GV] == T1 and [PR] == T2; all 6 Functions present; RC defaults to T1 (no scored rows)"
  - "len(subcategory_scores) == 8 (the seed's full sample)"
  - "len(gap_analysis.prioritization) == 5"
  - "roadmap covers the 5 prioritized gaps: risk context statement (GV.OC-01), cybersecurity policy (GV.PO-01), access-control policy (PR.AA-01), asset inventory scope (ID.AM-01), incident response plan (RS.MA-01)"
  - "subcategory scores use the documented status convention (Not|Partially|Largely|Fully Implemented)"
data_refs: [data/seeds/uc-01-input.json]
tests:
  - tests/test_nist_csf_2_oracle.py::test_uc_01_oracle
  - tests/test_nist_csf_2_oracle.py::test_uc_01_subcategory_status_enum
  - tests/test_nist_csf_2_oracle.py::test_uc_01_gap_prioritization_size
status: active
---

# UC-01 — Series-A SaaS builds first Organizational Profile (Tier 1→2)

## §1 Context and persona

**DataRelay Inc.** is a fictional 50-FTE B2B data-integration SaaS (founded 2024, AWS commercial, mid-market customers) with no dedicated security hire — security is part-time work inside a small IT/engineering team. Its strengths are engineering-led: **MFA has been enforced on all admin and developer accounts since day 1**, data is KMS-encrypted at rest, and AWS GuardDuty is enabled. Its gaps are governance-led: no published cybersecurity policy, no formal risk context statement, no documented incident response runbook, no formal asset inventory beyond AWS tags, and no subcategory owners. An enterprise customer will demand SOC 2 Type II within 12 months.

This use case builds the first Organizational Profile from the seed (`data/seeds/uc-01-input.json` — the tested fixture), identifies the 5 highest-impact gaps, and produces a 90-day roadmap at $0-15K and roughly 25% of one engineer's time (heuristic per `chunks/07` §1).

## §2 The 5-step procedure

1. **Pick Tier targets** (`chunks/02`): Tier 2 (Risk Informed) across all Functions for the 90-day horizon; Tier 3 for GOVERN/IDENTIFY/PROTECT at 12 months. Tier selection is a governance judgment, not a formula.
2. **Build the Current Profile** (`chunks/03 §5`): score Subcategories with the skill's 4-level status convention and evidence references. The seed carries an 8-row representative sample; a real engagement scores all 106.
3. **Roll up indicative Function tiers**: the reference executor applies the documented demo heuristic (`chunks/03 §3`): per Function, map Not=1 / Partially=2 / Largely=2 / Fully=3, take the median, cap at T3; unscored Functions (RECOVER here) default to T1 with a "no evidence" note. These are **indicative status-derived values to seed the governance judgment — not Tier determinations** (and per-Function Tiers are themselves a practitioner convention; NIST applies Tiers to Organizational Profiles).
4. **Gap analysis** (`chunks/04 §3-§4`): delta per Subcategory; prioritize via the 2x2 (risk reduction vs cost) matrix; pick the top 5.
5. **90-day roadmap** (`chunks/07 §1`): one deliverable per prioritized gap, each with owner and cost.

## §3 The 8-row Current Profile sample (from the seed)

| Subcategory | Status | Evidence |
|-------------|--------|----------|
| GV.OC-01 (mission informs cyber risk mgmt) | Not Implemented | Mission documented in company handbook; no formal risk context statement |
| GV.PO-01 (cybersecurity policy) | Not Implemented | No published cybersecurity policy; founders handle security ad hoc |
| ID.AM-01 (hardware inventory) | Partially Implemented | AWS asset inventory via tags; no formal record-keeping |
| PR.AA-01 (identities and credentials managed) | Partially Implemented | AWS IAM with groups; no formal access control policy |
| PR.AA-03 (users/services/hardware authenticated) | Fully Implemented | MFA enforced on all admin and developer accounts since day 1 |
| PR.DS-01 (data-at-rest protected) | Partially Implemented | KMS encryption at rest; data classification not formalized |
| DE.CM-01 (networks monitored) | Largely Implemented | AWS GuardDuty enabled; SIEM in evaluation; no 24/7 SOC |
| RS.MA-01 (IR plan executed) | Not Implemented | No documented IR plan; engineer-on-call paged on alerts but no runbook |

**Indicative Function tiers (stub heuristic on the 8-row sample):** GV T1, ID T2, PR T2, DE T2, RS T1, RC T1 (RECOVER unscored → defaults to T1). A full-106 assessment may land differently — treat these as the starting hypothesis for the Tier discussion, not the answer.

## §4 The 5-priority Gap Analysis

The five lowest-status Subcategories from the seed (the stub's deterministic prioritization; in the 2x2 matrix all five are Quick Wins — documentation-and-configuration work, no tool purchases):

| Subcategory | Current → Target | Why it leads |
|-------------|------------------|--------------|
| GV.OC-01 (risk context) | Not → Largely | Everything else hangs off the org's risk context; 1-page statement |
| GV.PO-01 (policy) | Not → Largely | Enterprise customers and SOC 2 both require a published policy |
| RS.MA-01 (IR plan) | Not → Largely | Highest operational risk: an incident today has no runbook |
| ID.AM-01 (inventory) | Partially → Largely | SOC 2 scoping needs an inventory beyond AWS tags |
| PR.AA-01 (access mgmt) | Partially → Largely | IAM groups exist; the policy and review cadence do not |

Note PR.AA-03 (MFA) is **not** a gap — it is the org's strength. The 90-day work for MFA is evidence capture (config export, service-account audit), not enablement.

## §5 The 90-day roadmap

| Week | Deliverable | Covers | Owner | Cost |
|------|-------------|--------|-------|------|
| W1-2 | Risk context statement + governance cadence (1-page, founders + VP Eng monthly) | GV.OC-01 | CEO + VP Engineering | $0 |
| W2-4 | Publish cybersecurity policy (5-page, CSF 2.0 + SOC 2 scope) | GV.PO-01 | VP Engineering | $0-2K |
| W3-6 | Formalize access-control policy (IAM group definitions, review cadence, joiner/leaver) — plus MFA evidence capture | PR.AA-01 (+PR.AA-03 evidence) | VP Engineering | $0-3K |
| W4-8 | Define asset inventory scope (AWS + GitHub + SaaS subscriptions + endpoints) | ID.AM-01 | VP Engineering | $0-3K |
| W8-12 | Publish incident response plan (runbook, on-call rotation, comms tree) | RS.MA-01 | VP Engineering | $0-5K |
| | **Total** | | | **$0-15K**, ~25% of one engineer |

## §6 Anti-hallucination

- **DataRelay Inc. is a fictional archetype**; the seed (`data/seeds/uc-01-input.json`) is the tested fixture. The worked example in `chunks/03 §6` is a DIFFERENT illustrative scoring of the same archetype — when they disagree, the seed is this UC's source of truth.
- **Tier names: T1=Partial, T2=Risk Informed, T3=Repeatable, T4=Adaptive** (NIST CSF 2.0). NIST applies Tiers to Organizational Profiles and they are NOT maturity levels; per-Function values here are a labeled practitioner convention.
- **The status scale (Not/Partially/Largely/Fully Implemented) is this skill's convention, not a NIST scale** — CSWP 29 defines none, and SP 1301's Profile example is explicitly notional ("use whatever format they prefer").
- **PR.AA texts** (verified): PR.AA-01 identities/credentials managed; PR.AA-02 identity proofing; PR.AA-03 users/services/hardware authenticated; PR.AA-04 identity assertions protected; PR.AA-05 access permissions/least privilege; PR.AA-06 physical access.
- **Cost figures are heuristics** per `chunks/07 §1`; real costs depend on existing tooling and staffing.
- **CSF 2.0 Quick-Start Guides** (verified 2026-06-10): SP 1299 Resource & Overview, SP 1300 Small Business, SP 1301 Organizational Profiles, SP 1302 Tiers, SP 1303 ERM, SP 1305 C-SCRM. The Organizational Profile template (XLSX) on the NIST CSF site is the recommended input format.
