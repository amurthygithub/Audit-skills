---
uc_id: UC-02
title: "$20B regional bank produces board cyber maturity report (6-function radar + 12-month capital plan + exam-defense narrative)"
industries: [financial-services, public-sector]
frameworks: [NIST-CSF-2.0, OCC-2014-13, FFIEC-CAT, NY-DFS-500, NIST-SP-800-53-Rev5.1.1]
procedure:
  - "chunks/05-govern-function.md §1 — Build the GOVERN narrative: 6 Categories, board-level questions, evidence examples"
  - "chunks/06-enterprise-reporting.md §1 — Build the 6-function radar from the per-Function Tier rollup (use the markdown table format, not Mermaid)"
  - "chunks/06-enterprise-reporting.md §2 — Build the maturity scorecard (one row per Function with executive questions + business consequences)"
  - "chunks/06-enterprise-reporting.md §5 — Build the 1-page board report template inline (per §5 of chunk 06)"
  - "chunks/06-enterprise-reporting.md §4 — Build trend reporting: quarterly delta tracking (Q1 2026 vs Q4 2025, YoY)"
  - "chunks/07-implementation-playbook.md §3 — 12-month strategic investments sizing (FTE + tool spend, $1.5M-$3.0M for a $20B bank)"
  - "industries/financial-services.md — Apply the exam-driven reality: OCC Heightened Standards §III.C, FFIEC CAT alignment, supervisory letter / MRA language"
expected_outputs:
  govern_narrative:
    org: "Meridian Trust, N.A."
    holding_company: "Meridian Financial Services, Inc."
    assets: "$20B"
    fte: 4200
    branches: 87
    six_categories_covered: [GV.OC, GV.RM, GV.SC, GV.PO, GV.OV, GV.RR]
  six_function_radar:
    governance: T2
    identify: T2
    protect: T3
    detect: T2
    respond: T2
    recover: T1
  maturity_scorecard: 6 rows (one per Function with executive question + business consequence in board language)
  trend_reporting: 2 quarter rows (Q4 2025 and Q1 2026, per-Function delta)
  capital_plan_12mo: 6 rows (one per investment line — cyber FTE +4, tool spend +$800K, third-party risk program, IR retainer, OT/IT segmentation, board cyber committee)
  board_report_inline: full 1-page board report markdown (per chunk 06 §5 template)
  classification: "BOARD_MATURITY_REPORT"
oracle:
  - "six_function_radar[recover] == T1 (the headline finding — RC is the lagging function)"
  - "len(maturity_scorecard) == 6"
  - "len(capital_plan_12mo) == 6"
  - "all 6 GOVERN Categories appear in govern_narrative"
  - "trend_reporting has at least 2 quarters with Q1 2026 > Q4 2025 (improvement) OR clearly worse (regression flag)"
  - "capital_plan_12mo totals between $1.5M and $3.0M"
data_refs: [data/seeds/uc-02-input.json]
tests: [tests/test_nist_csf_2_oracle.py::test_uc_02_oracle, tests/test_nist_csf_2_oracle.py::test_uc_02_recover_tier_lagging, tests/test_nist_csf_2_oracle.py::test_uc_02_govern_categories_complete, tests/test_nist_csf_2_oracle.py::test_uc_02_capital_plan_range]
status: active
---

# UC-02 — Board Cyber Maturity Report for Meridian Trust, N.A.

## §1 Context and persona

**Meridian Trust, N.A.** is a fictional $20B-asset regional bank headquartered in the Midwest, with 4,200 FTE, 87 branches across six states, and a holding company structure (Meridian Financial Services, Inc.) with three operating subsidiaries (Meridian Trust, Meridian Wealth Management, Meridian Insurance Agency). The bank is OCC-regulated and subject to FFIEC CAT examination, NY DFS Part 500 (for its trust operations in New York), and GLBA Safeguards Rule. A 2023 strategic risk review conducted jointly by the CRO, the newly-hired CISO, and an external 3PAO identified cyber as a **Tier 1 enterprise risk** — the bank had mature PROTECT controls (MFA, encryption, policy) but a severely under-developed RECOVER capability and a board cyber committee that had been stood up in name only. The board chartered a formal cyber committee in Q1 2024 and requested a CSF 2.0-aligned maturity baseline by Q4 2025, with quarterly trend updates thereafter. This use case walks through the resulting Q1 2026 board report: a 6-function radar, a 6-row maturity scorecard, a 2-quarter trend delta, a 12-month capital allocation plan, and a 1-page board-ready report suitable for the pre-read packet 48 hours before the cyber committee meeting. The archetype is exam-facing: the output is designed to be defensible if an OCC examiner asks the board "how did you arrive at this maturity assessment?"

## §2 The 6-function radar

The per-Function Tier rollup for Meridian Trust as of Q1 2026 (scored via the Current Profile methodology in `chunks/03-current-profile.md` with a GOVERN-first assessment order per `chunks/05-govern-function.md` §5). Each Tier is an aggregate of the Category-level scores within that Function, weighted by Subcategory count. The interpretation column is the one-line board translation per `chunks/06-enterprise-reporting.md` §2.

| Function | Current Tier | Interpretation (board language) |
|----------|-------------|--------------------------------|
| **GOVERN** | T2 (Risk Informed) | "The board has a cyber committee and a risk appetite statement, but supply chain governance and formal oversight cadence are not yet documented." |
| **IDENTIFY** | T2 (Risk Informed) | "Asset inventory and risk assessment are documented for Tier-1 systems; full scope (Tier-2 and Tier-3 systems) is in progress." |
| **PROTECT** | T3 (Repeatable) | "MFA, encryption-at-rest, data classification, and security training are formalized, approved, and operating with named owners." |
| **DETECT** | T2 (Risk Informed) | "SIEM deployed with known-bad signature rules; detection engineering for novel threats and 24/7 SOC coverage are not yet in place." |
| **RESPOND** | T2 (Risk Informed) | "IR plan is documented and tested annually via tabletop; regulator notification playbook exists but has not been exercised with the board." |
| **RECOVER** | T1 (Partial) | **Headline finding**: BCP/DR plans exist on paper but have not been tested in over 24 months; RTO/RPOs are not formally documented for Tier-2 and Tier-3 systems; no supplier coordination in recovery exercises." |

The radar is uneven by design — real maturity is rarely uniform (per `chunks/06-enterprise-reporting.md` §5 anti-trend guidance). PROTECT is the high-water mark (T3); RECOVER is the low-water mark (T1) and the primary investment driver for the 12-month plan.

## §3 The maturity scorecard

Per `chunks/06-enterprise-reporting.md` §3: one row per Function with the executive question, current Tier, target Tier (12-month), and the business consequence in board language (no Subcategory IDs — those live in the appendix). The scorecard is the board's read-out page.

| # | Function | Executive question | Current Tier | 12-mo Target | Business consequence (board language) |
|---|----------|--------------------|-------------|-------------|----------------------------------------|
| 1 | **GOVERN** | Are we governed for cyber risk? | T2 | T3 | "The board cyber committee meets quarterly but oversight is informal; supply chain risk governance is on a roadmap, not yet operating. If the OCC reviews our third-party program today, we would be cited for insufficient coverage of the top 20 suppliers." |
| 2 | **IDENTIFY** | Do we know what we are protecting? | T2 | T3 | "Tier-1 asset inventory and risk assessment are current; Tier-2 and Tier-3 scope is incomplete, which means the bank cannot confirm what data sits on ~40% of its systems. This is a regulatory exposure for GLBA 314.4 and NY DFS 500.09." |
| 3 | **PROTECT** | Are our safeguards adequate? | T3 | T3 | "Protections are the bank's strongest area: MFA, encryption, training, and policy are at board-approved maturity. No material investment needed in the next 12 months beyond sustainment." |
| 4 | **DETECT** | Would we notice an attack? | T2 | T3 | "Known-bad signatures are monitored, but the bank lacks a detection engineering program for novel threats. Mean time to detect for a sophisticated adversary is estimated at 90+ days — well above the 21-day FFIEC supervisory target. The bank is blind to supply chain compromise." |
| 5 | **RESPOND** | Could we contain and remediate? | T2 | T3 | "IR plan is documented and tested annually, but the plan does not cover a multi-subsidiary simultaneous incident, and the 72-hour DFS notification process has not been exercised in a live-fire scenario. IR retainer with a forensic firm is not in place." |
| 6 | **RECOVER** | Could we restore operations? | T1 | T2 | "BCP/DR plans are not tested; last tabletop was Q2 2023. No documented recovery coordination with core banking provider or card processor. If a ransomware event hits the core banking system, the bank cannot state its RTO for wire transfer operations with confidence. **This is the board's number-one risk item.**" |

## §4 The trend reporting

Per `chunks/06-enterprise-reporting.md` §4: quarterly delta tracking with two quarters (Q4 2025 baseline and Q1 2026 update). Q4 2025 was the first formal Current Profile; Q1 2026 is the first trend update. The RECOVER regression from T1 (baseline) to T1 (unchanged) is flagged because no recovery investment was made in Q1 — the flat-line is the red flag per §4 interpretation rules.

| Function | Q4 2025 Tier | Q1 2026 Tier | QoQ Delta | Direction |
|----------|-------------|-------------|-----------|-----------|
| **GOVERN** | 1.5 | 2.0 | +0.5 | Improving — board cyber committee stood up (Q4 2024) and risk appetite statement adopted (Q1 2025); GV.OV-01 and GV.RM-02 formalized |
| **IDENTIFY** | 1.5 | 2.0 | +0.5 | Improving — Tier-1 asset inventory completed and risk assessment refreshed |
| **PROTECT** | 2.5 | 3.0 | +0.5 | Improving — org-wide MFA deployed; encryption-at-rest policy enforced |
| **DETECT** | 1.5 | 2.0 | +0.5 | Improving — SIEM procurement completed; known-bad signature rules deployed |
| **RESPOND** | 2.0 | 2.0 | 0.0 | Flat — IR plan documented but no investment in IR retainer or tabletop exercise in the quarter |
| **RECOVER** | 1.0 | 1.0 | 0.0 | **Regression flag** — no recovery investment; last BCP/DR test was Q2 2023 (24+ months ago); RTO/RPO documentation for Tier-2/3 systems not started. This is the program's single largest unresolved gap and the primary finding in the 12-month capital plan |

**Trend interpretation note**: The flat RESPOND and RECOVER scores are the red flags per the trend rules in `chunks/06-enterprise-reporting.md` §4. A flat score over 2+ quarters means the Function has no owner or no investment. In Meridian's case, both Functions lacked dedicated FTE allocation in the Q4 2025 budget cycle. The 12-month capital plan directly addresses both gaps.

## §5 The 12-month capital plan

Per `chunks/07-implementation-playbook.md` §3: 12-month strategic investments sized for a $20B-asset regional bank. The total is $2.15M at the low end of the $1.5M-$3.0M heuristic range. Each line is a board-level investment ask with a named owner and a regulatory/exam-defense rationale grounded in `industries/financial-services.md` §2 (OCC Heightened Standards Table 2) and the exam-driven reality (§5).

| # | Investment line | Cost estimate | Owner | Regulatory / exam rationale |
|---|----------------|---------------|-------|---------------------------|
| 1 | **Cyber FTE +4** (1 IR/BCP lead, 1 detection engineer, 1 third-party risk analyst, 1 GRC analyst) | $600K/year fully loaded | CISO / CHRO | OCC Heightened Standards §III.F (Talent Management) requires qualified personnel for the three lines of defense. Four additional FTE close the RECOVER, DETECT, GOVERN, and RESPOND gaps. [VERIFY: OCC-Heightened-Standards exact section for talent management] |
| 2 | **Tool spend +$800K** (SIEM/EDR expansion $400K, TPRM platform $200K, BCP/DR automation $150K, threat intel feed $50K) | $800K/year | CISO / CIO | FFIEC CAT Domain 3 (Cybersecurity Controls) and Domain 4 (External Dependency Management) expect automated monitoring, supplier risk tooling, and recovery automation. These tools close the DETECT (DE.CM-01), GOVERN (GV.SC-04), and RECOVER (RC.RP-01) gaps. |
| 3 | **Third-party risk program formalization** (supplier tiering, contract language update, first assessment cycle for top 20 suppliers) | $250K (0.5 FTE from line 1 + TPRM platform from line 2 + external legal review) | CISO / General Counsel | OCC Bulletin 2023-17 (Interagency Guidance on Third-Party Relationships) and CSF 2.0 GV.SC-01 through GV.SC-10 require a documented, board-approved third-party risk program with ongoing monitoring. The bank's current TPRM is limited to initial due diligence with no continuous monitoring. |
| 4 | **IR retainer + forensic firm engagement** ($50K annual retainer + $75K for two tabletop exercises) | $125K | CISO | NY DFS 500 §500.16 requires a tested incident response plan. The bank's IR plan has been tabletop-tested internally once but never with a forensic firm or regulatory notification simulation. This line covers both the retainer and two facilitated tabletops (one standard, one multi-subsidiary scenario). |
| 5 | **OT/IT segmentation assessment** (physical branch security audit, ATM network segmentation, card processor integration review) | $150K (external assessment firm) | CISO / Head of Physical Security | FFIEC CAT Domain 3 (Cybersecurity Controls) expects segmentation between operational technology (ATMs, branch security systems) and IT networks. OCC Bulletin 2014-13 (ATM/Card Authorization Attacks) flagged ATM control panel vulnerabilities. A post-2014 landscape requires formal OT/IT segmentation. |
| 6 | **Board cyber committee formalization** (quarterly external briefing, independent advisor engagement, committee charter refresh) | $75K | Board Chair / CISO | OCC Heightened Standards §III.A requires formal board oversight of risk management with documented meeting cadence, independent input, and a written charter. The current committee meets quarterly but lacks independent advisory. This line funds an external advisor for four quarterly sessions and a charter refresh. |
| | **Total** | **$2.00M** (excl. FTE overlap; $2.15M incl. FTE) | — | — |

**Sizing note**: The $2.15M total falls within the $1.5M-$3.0M heuristic range for a $20B-asset bank per `chunks/07-implementation-playbook.md` §3. FTE lines and tool lines have partial overlap (the TPRM analyst FTE from line 1 uses the TPRM platform from line 2; the IR lead from line 1 facilitates the tabletops from line 4). The total exclusive of overlap is $2.00M; the inclusive total is $2.15M. Real bank engagements should use bottom-up vendor quotes and HR comp data, not heuristics.

## §6 The 1-page board report

Per the inline template in `chunks/06-enterprise-reporting.md` §6, populated for Meridian Trust, N.A. This is the artifact the CISO hands the board 48 hours before the Q1 2026 cyber committee meeting.

---

# Cyber Maturity Report — Meridian Trust, N.A. — Q1 2026

## 1. Executive Summary (3 sentences)

- Meridian Trust, N.A. is currently at an average CSF Tier of **1.8** across the 6 Functions, with a target Tier of **2.7** within 24 months.
- The largest maturity gap is in **RECOVER (T1)**, where BCP/DR has not been tested since Q2 2023 and RTO/RPO documentation for Tier-2 and Tier-3 systems is absent; **DETECT (T2)** and **RESPOND (T2)** also show material gaps versus the 12-month target.
- We are requesting **$2.15M** in FY2027 cyber investment to close the top 6 gap items; of these, items 1 (BCP/DR), 3 (third-party risk program), and 6 (board committee formalization) are **regulatory-mandated** per OCC Heightened Standards and FFIEC CAT expectations.

## 2. 6-Function Radar

[Insert radar table from §2 above — the markdown table format is the board-preferred format for pre-read packets. The full Subcategory-level appendix is available on request.]

## 3. Maturity Scorecard

[Insert maturity scorecard from §3 above]

## 4. Trend (QoQ)

[Insert trend table from §4 above]

## 5. Top 6 Priority Gaps (the 12-month ask)

| # | Gap | Owner | Target window | Investment | Regulatory? |
|---|-----|-------|---------------|-----------|-------------|
| 1 | BCP/DR testing + RTO/RPO documentation (RC.RP-01) | VP, Business Continuity | Q2-Q3 2026 | $150K (from capital plan line 2: BCP/DR automation) | **Yes** — OCC Heightened Standards §III.C, FFIEC CAT Domain 5 |
| 2 | Detection engineering program + 24/7 SOC coverage (DE.CM-01, DE.AE-02) | CISO / Director, Security Operations | Q2-Q4 2026 | $500K (1 FTE detection engineer from line 1 + SIEM/EDR expansion from line 2) | Implicit — FFIEC CAT Domain 3 expectation of continuous monitoring |
| 3 | Third-party risk program formalization (GV.SC-01 through GV.SC-10) | CISO / General Counsel | Q2-Q4 2026 | $250K (from capital plan line 3) | **Yes** — OCC Bulletin 2023-17, CSF 2.0 GV.SC |
| 4 | IR retainer + multi-subsidiary tabletop exercise (RS.MA-01) | CISO | Q2-Q3 2026 | $125K (from capital plan line 4) | **Yes** — NY DFS 500 §500.16 |
| 5 | OT/IT segmentation assessment (PR.AA-05, ID.AM-01) | CISO / Head of Physical Security | Q3 2026 | $150K (from capital plan line 5) | Implicit — FFIEC CAT Domain 3, OCC Bulletin 2014-13 |
| 6 | Board cyber committee formalization (GV.OV-01, GV.OV-02, GV.OV-03) | Board Chair / CISO | Q2 2026 | $75K (from capital plan line 6) | **Yes** — OCC Heightened Standards §III.A |

## 6. Governance Cadence

- Board cyber committee: meets quarterly — last met March 15, 2026, next June 15, 2026
- CISO reporting line: dual to CEO and Board Cyber Committee Chair
- Last independent assessment: Q4 2025 by [3PAO name] — produced the baseline Current Profile used in this report
- Next independent assessment: Q4 2026 (annual cycle) — will measure progress against the 12-month capital plan

## 7. Risk Posture Statement

"The cyber program is **at risk** against the 24-month target due to the RECOVER gap. The top risks are: (R1) untested BCP/DR for core banking operations, (R2) no detection capability for novel/supply-chain threats, and (R3) undocumented third-party risk management for the top 20 suppliers (see Appendix A). No OCC enforcement actions, material cybersecurity incidents, or unmitigated HIGH findings in the reporting period. The last OCC Safety and Soundness examination (Q3 2025) noted 'informal board cyber governance' as a supervisory observation — the board cyber committee formalization investment in this plan directly addresses that observation."

## 8. Appendices (linked, not inline)

- A. Full 106-Subcategory Current Profile (YAML)
- B. Full Gap Analysis Table (YAML)
- C. 12-month Roadmap (Gantt or table)
- D. Crosswalk to FFIEC CAT, OCC Heightened Standards, and NY DFS 500

---

## §7 Anti-hallucination

- **Meridian Trust, N.A. is a fictional archetype.** The org name, asset size, FTE count, branch network, holding company structure, and maturity scores are fabricated for the use case. Real engagements require actual org data, board-approved risk appetite statements, and examination findings that are typically OCC-confidential and subject to attorney-client privilege or bank examination privilege.
- **OCC Heightened Standards (12 CFR 30 Appendix D) applies to banks >$50B in assets.** Meridian Trust at $20B falls under 12 CFR 30 Appendix A (Safety and Soundness Standards), which is less prescriptive on risk governance. The Heightened Standards mappings in §5 are applied as a stretch-goal lens — in practice, the bank's compliance counsel should determine the exact regulatory applicability. The `frameworks` frontmatter field lists `OCC-2014-13` but [VERIFY: OCC Bulletin 2014-13 is a joint FFIEC statement on ATM/card authorization cyber attacks — it is NOT the Heightened Standards codification. The Heightened Standards were codified in 12 CFR 30 Appendix D effective September 2014. The correct OCC issuance may be a different bulletin number or a Federal Register final rule citation. Update the frontmatter framework key if the intended reference is Heightened Standards, not the ATM bulletin.]
- **FFIEC CAT maturity levels are NOT the same as CSF Tiers.** The FFIEC CAT uses a 5-level supervisory maturity scale: Baseline, Evolving, Intermediate, Advanced, Innovative. CSF 2.0 uses a 4-level organizational maturity scale: 1 (Partial), 2 (Risk Informed), 3 (Repeatable), 4 (Adaptive). Do not conflate "Advanced" with "Tier 4" or "Evolving" with "Tier 2." The mapping in this use case is interpretive — no official crosswalk between the two maturity scales exists. Source: `industries/financial-services.md` Q3 and anti-hallucination section.
- **FFIEC CAT source is unverified.** `https://www.ffiec.gov/cyberassessmenttool.htm` returned HTTP 403 on retrieval. The maturity level names (Baseline, Evolving, Intermediate, Advanced, Innovative) and domain names used in this use case are based on the known FFIEC CAT 2017 documentation but could not be confirmed via live fetch. [VERIFY: (a) exact domain names, (b) whether a CAT 2.0 update has been published, (c) whether the maturity taxonomy changed. Source: `industries/financial-services.md` anti-hallucination.]
- **12-month capital estimates are heuristics, not NIST-mandated values.** The $2.15M total is derived from `chunks/07-implementation-playbook.md` §3 practitioner estimates scaled for a $20B-asset regional bank. Real engagement sizing depends on the bank's risk assessment, board-approved risk appetite, existing tooling contracts, regional salary bands, and vendor negotiation outcomes. The FTE overlap methodology (excluding from the $2.00M subtotal, including in the $2.15M inclusive total) is a planning convention, not an accounting standard.
- [VERIFY: OCC Bulletin 2023-17 (Interagency Guidance on Third-Party Relationships) was cited in `industries/financial-services.md` Table 2. Confirm the exact bulletin number and title. The OCC Quick Access menu links to `/news-issuances/bulletins/2023/bulletin-2023-17.html` under "Third-Party Relationships: Interagency Guidance on Risk Management." Use the Federal Register citation if the bulletin number is uncertain.]
- [VERIFY: NY DFS 500 §500.17(a) 72-hour notification requirement — the amended November 2023 version relocated the notification provision. Confirm the exact section number in the current regulation (23 NYCRR 500). Source: `industries/financial-services.md` Table 3 note and anti-hallucination.]
