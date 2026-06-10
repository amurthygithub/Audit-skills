---
uc_id: UC-02
title: "$24B regional bank produces board cyber posture report (6-function radar + 12-month capital plan + exam-defense narrative)"
industries: [financial-services]
frameworks: [NIST-CSF-2.0, NY-DFS-500, NIST-SP-800-53-Rev5.1.1]
procedure:
  - "chunks/05-govern-function.md §2 — Build the GOVERN narrative: 6 Categories, board-level questions, evidence examples"
  - "chunks/06-enterprise-reporting.md §2 — Build the 6-function radar from the per-Function Tier values (markdown table; label per-Function Tiers as the bank's own scoring convention)"
  - "chunks/06-enterprise-reporting.md §3 — Build the maturity scorecard (one row per Function with executive question + business consequence)"
  - "chunks/06-enterprise-reporting.md §4 — First report = baseline; do NOT invent trend data (trend tables start in Q2)"
  - "chunks/06-enterprise-reporting.md §6 — Populate the 1-page board report template"
  - "industries/financial-services.md — Apply the exam-driven reality (FFIEC IT Examination Handbook; the CAT was sunset Aug 31, 2025; NY DFS Part 500)"
expected_outputs:
  govern_narrative:
    org: "Pinecrest National Bank"
    assets: "$24B"
    fte: 8500
    branches: 187
    primary_regulator: OCC
    six_categories_covered: [GV.OC, GV.RM, GV.SC, GV.PO, GV.OV, GV.RR]
  six_function_radar:
    governance: T3
    identify: T3
    protect: T3
    detect: T2
    respond: T2
    recover: T1
  maturity_scorecard: 6 rows (one per Function, executive question + business consequence in board language)
  baseline_note: "first formal Current Profile — trend reporting begins next quarter (no invented history)"
  capital_plan_12mo: 6 rows totaling $2.0M (the seed's investment capacity), each with owner + regulatory rationale
  board_report_inline: 1-page board report markdown (chunk 06 §6 template)
  classification: "BOARD_MATURITY_REPORT"
oracle:
  - "six_function_radar[recover] == T1 (the headline finding — RC is the lagging function and the radar minimum)"
  - "len(capital_plan_12mo) == 6, each row with cost_estimate, owner, regulatory_rationale"
  - "all 6 GOVERN Categories appear in govern_narrative"
  - "capital plan totals the seed's $2.0M investment capacity"
  - "first report carries a baseline note instead of a fabricated trend table"
data_refs: [data/seeds/uc-02-input.json]
tests: [tests/test_nist_csf_2_oracle.py::test_uc_02_oracle, tests/test_nist_csf_2_oracle.py::test_uc_02_recover_tier_lagging, tests/test_nist_csf_2_oracle.py::test_uc_02_govern_categories_complete, tests/test_nist_csf_2_oracle.py::test_uc_02_capital_plan_range]
status: active
---

# UC-02 — Board Cyber Posture Report for Pinecrest National Bank

## §1 Context and persona

**Pinecrest National Bank** is a fictional $24B-asset OCC-regulated regional bank with 8,500 FTE and 187 branches (the seed at `data/seeds/uc-02-input.json` is the tested fixture). The board chartered a cyber committee and requested a CSF 2.0-aligned posture baseline with quarterly updates thereafter. This use case produces that FIRST report: a 6-function radar, a 6-row scorecard, a 12-month capital plan sized to the board-approved $2.0M investment capacity, and a 1-page board pre-read. The output is exam-facing: defensible if an OCC examiner asks "how did you arrive at this assessment?" — which is why every methodological convention is labeled as the bank's own.

**Methodology disclosure (goes on the face of the report):** per-Function Tier values and any aggregation are the bank's documented scoring convention. NIST applies CSF Tiers to Organizational Profiles, and Tiers are not maturity levels. Do not present per-Function or fractional Tiers as NIST methodology, and never report a "Tier average" — the first examiner question ("whose methodology?") must have an answer.

## §2 The 6-function radar (from the seed)

| Function | Tier (bank convention) | Interpretation (board language) |
|----------|------------------------|--------------------------------|
| **GOVERN** | T3 (Repeatable) | "Board risk committee approves the risk appetite annually; CISO reports to the CRO and quarterly to the board; policy hierarchy (enterprise + 14 domain policies + 47 procedures) is current." |
| **IDENTIFY** | T3 (Repeatable) | "Asset inventory and risk assessment are formalized and current; third-party program covers 412 critical vendors including 18 fourth-party dependencies." |
| **PROTECT** | T3 (Repeatable) | "Access management, encryption, and training operate org-wide with named owners." |
| **DETECT** | T2 (Risk Informed) | "Monitoring exists but is not yet 24/7 with threat-intelligence integration — the SOC uplift in the capital plan addresses this." |
| **RESPOND** | T2 (Risk Informed) | "IR plan documented and tested annually; multi-subsidiary scenarios and regulator-notification exercises are not yet routine." |
| **RECOVER** | T1 (Partial) | **Headline finding:** "DR/BCP exists on paper but recovery exercises are not performed on a defined cycle; RTO/RPO documentation is incomplete. This is the board's number-one gap and the largest line-item driver in the capital plan." |

The radar is uneven by design — real postures are (see `chunks/06` §5). RECOVER (T1) is the radar minimum and the primary investment driver.

## §3 The maturity scorecard

One row per Function (chunk 06 §3 shape): executive question, current Tier, 12-month target, business consequence. Sample rows:

| # | Function | Executive question | Current → 12-mo target | Business consequence (board language) |
|---|----------|--------------------|------------------------|----------------------------------------|
| 1 | GOVERN | Are we governed for cyber risk? | T3 → T3 (sustain) | "Governance is the program's strength; the ask is sustainment, not build." |
| 4 | DETECT | Would we notice an attack? | T2 → T3 | "Without 24/7 monitoring with threat intelligence, a sophisticated intrusion could persist undetected. The SOC uplift closes this." (Benchmark detection times only against named, sourced industry studies — no regulator publishes an MTTD target.) |
| 6 | RECOVER | Could we restore operations? | T1 → T2 | "If ransomware hit core banking today, the bank could not state its wire-operations RTO with confidence. This is the board's number-one risk item." |

## §4 Baseline note (first report — no trend table)

Per `chunks/06` §4: trend reporting requires at least 2 quarters of data, and the chunk's anti-hallucination rule is explicit — **do not invent trend data on a first report**. This report establishes the baseline; the QoQ trend table begins next quarter. (The seed contains no historical quarters; an earlier version of this UC fabricated a 2-quarter trend, which is exactly the failure mode the rule exists to stop.)

## §5 The 12-month capital plan (from the seed — totals $2.0M)

| # | Investment line | Cost | Owner | Regulatory rationale |
|---|----------------|------|-------|----------------------|
| 1 | Identity & Access Management modernization (PAM rollout) | $400K | CISO | 12 CFR 30 App. B (access controls on customer information systems) |
| 2 | Third-party risk management (continuous monitoring of critical vendors) | $300K | TPRM Lead | Interagency Guidance on Third-Party Relationships (2023); NY DFS §500.11 |
| 3 | SOC uplift (24/7 monitoring + threat intelligence) | $500K | SOC Director | Supervisory expectation: FFIEC IT Examination Handbook (continuous monitoring) |
| 4 | DR & resilience testing (4 recovery exercises, hot-site failover) | $250K | BCP Lead | FFIEC Business Continuity Management booklet |
| 5 | Training & awareness (board training + phishing simulation + role-based) | $150K | People Security Lead | NY DFS §500.14 (training); FFIEC IT Examination Handbook (security awareness) |
| 6 | GRC tooling consolidation (3 point tools → 1 platform) | $400K | GRC Director | 12 CFR 30 App. B (information security program governance) |
| | **Total** | **$2.0M** | | equals the board-approved investment capacity in the seed |

**Mandate honesty rule:** label each ask *mandated* (citable rule applicable to THIS bank), *supervisory expectation* (examiner guidance), or *discretionary*. OCC Heightened Standards (12 CFR 30 App. D) apply to banks **>$50B** — at $24B, Pinecrest is under App. A/B and the interagency guidelines; telling the board an App. D item is "regulatory-mandated" would misstate a legal obligation. Have counsel confirm applicability before the pre-read goes out.

## §6 The 1-page board report

Populate `chunks/06` §6 with the values above. Executive-summary discipline: state the RECOVER finding and the $2.0M ask in plain language; report per-Function Tier values with the methodology label; no Tier averages; no invented benchmarks; appendices carry the 106-Subcategory profile and gap table.

## §7 Anti-hallucination

- **Pinecrest National Bank is a fictional archetype**; the seed is the tested fixture. Real engagements need actual org data and examination findings (typically confidential supervisory information).
- **FFIEC CAT is sunset** (effective Aug 31, 2025, per the FFIEC's Aug 2024 statement; the May 2017 version was the last — there was never a "CAT v2"). Anchor exam-defense language to the FFIEC IT Examination Handbook and current interagency guidance, or to CSF 2.0/industry profiles (e.g., CRI Profile) as the FFIEC suggested.
- **No regulator publishes an MTTD/MTTR numeric target** — any detection-time benchmark must cite a named industry study (an earlier version of this UC invented a "21-day FFIEC supervisory target").
- **OCC Heightened Standards apply >$50B** (12 CFR 30 App. D). At $24B, cite 12 CFR 30 App. A/B and interagency guidance.
- **NY DFS Part 500 cites** (post-Nov 2023 amendment): §500.11 TPSP policy, §500.14 training/monitoring, 72-hour incident notice under §500.17(a) — verify section numbers against the current 23 NYCRR 500 text before quoting in a deliverable.
- **Tiers/averages**: per-Function Tier values are the bank's convention; NIST applies Tiers to Organizational Profiles; Tiers are not maturity levels; never report fractional "Tier averages" as if NIST-defined.
