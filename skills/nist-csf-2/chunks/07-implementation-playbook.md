---
chunk_id: 07-implementation-playbook
parent_skill: nist-csf-2
topic: "Implementation: 90-day, 6-month, 12-month quick wins, sequencing, and resourcing"
load_when: "user asks how to implement CSF, prioritization, or resourcing"
---

# Chunk 07 — Implementation Playbook

A CSF Current Profile, Target Profile, and gap analysis (see `chunks/03-current-profile.md`, `chunks/04-target-profile-and-gap.md`) are the **input** to implementation; the playbook here is the **output**. CSF 2.0 itself ships an Implementation Examples appendix [NIST-CSF-2.0 Appendix] that is illustrative but not normative — the playbook below builds on those examples with sequencing, resourcing, and change-management guidance. The FTE estimates and quick-wins list are **heuristics drawn from practitioner experience**, not NIST-mandated. Adapt to the org's risk profile, regulation, and customer demands.

## 1. The 90-day quick wins (Tier-1 wins, low cost, high visibility)

The first 90 days are about **momentum**: deliver 5-10 visible wins that establish the program as credible. The goal is not full Tier 3 maturity; it is a Current Profile in hand, a Target Profile agreed, and a top-3 list of high-impact gaps already closed.

**Tier-1 quick wins (do in 90 days):**

1. **Document the existing practices.** Most orgs are doing 30-50% of CSF already; the first deliverable is a Current Profile YAML (see `chunks/03-current-profile.md` §5) that names what is in place. This is the cheapest, highest-leverage activity; it converts tacit knowledge into a Profile.
2. **Identify the 5 most-missing Subcategories.** CSF 2.0 has 106 Subcategories total; for the 90-day roadmap, pick the 5 with the largest delta from target (see Current Profile gap analysis). These become the 90-day roadmap.
3. **Stand up the cyber steering committee** (covers `GV.OV-01`). Monthly meeting; CISO + CIO + CFO + General Counsel + one business unit head. Charter in a 1-page memo. Cost: 4 hours/month of executive time.
4. **Publish the cybersecurity policy** (covers `GV.PO-01`). Even a 5-page "we follow NIST CSF 2.0 and SOC 2" policy is a 90-day win. Cost: 1-2 people-weeks of policy author time.
5. **Enable MFA on all admin accounts** (covers `PR.AA-03`). The single highest-leverage control change. Cost: 0-1 person-week; tool cost $0-$10/user/month.
6. **Publish the incident response plan** (covers `RS.MA-01`). Even an untested IR plan is a Subcategory win. Cost: 1-2 people-weeks.
7. **Run the first board cyber committee meeting** (covers `GV.OV-01`, `GV.OV-02`). Use the 1-page board report template in `chunks/06-enterprise-reporting.md §6`. Cost: 1-2 days of CISO prep.
8. **Document the asset inventory scope** (covers `ID.AM-01`). Not the full inventory — just the **scope** of the inventory. Full inventory is 6-12 months; scope is 90 days.
9. **Assign Subcategory owners** (covers `GV.RR-04`). One named owner per Subcategory, even if it is "the CISO" for 20 of them. Cost: 1 person-week of CISO time.
10. **Produce the 1-page board update** (covers `GV.OV-02`). Use the template in `chunks/06-enterprise-reporting.md`. Distribute to the board pre-read for the next meeting.

**Cost range (90 days)**: $0 (if all 10 are documentation work) to $50K (if MFA tooling, basic SIEM-lite, and policy-authoring contractor are involved). For a Series-A SaaS with 25% of one engineer's time, the realistic 90-day spend is $0-15K.

## 2. The 6-month mid-game (formalize, prioritize, first projects)

Months 4-6 are about **formalization**: the Current Profile is documented, the Target Profile is approved, and the first 3 gap-closure projects are in flight. By month 6, the org should be at Tier 2.0-2.5 average across the 6 Functions.

**6-month deliverables:**

1. **Formalize the Current Profile** (covers `chunks/03-current-profile.md` §5). All 106 Subcategories scored; per-Subcategory evidence refs and owners named. Update cadence: quarterly.
2. **Set the Target Profile** (covers `chunks/04-target-profile-and-gap.md` §2). Per-Function Tier target approved by the cyber steering committee and the board. Documented rationale per Function (regulatory, customer, risk-tolerance inputs).
3. **Start the first 3 gap-closure projects.** These are the 3 highest-priority items from the Gap Analysis Table (see `chunks/04-target-profile-and-gap.md` §4) in the "Strategic Investment" or "Quick Win" quadrants. Common first projects: MFA org-wide (PR.AA-03), SIEM/SOC tooling (DE.CM-01), third-party risk program (GV.SC-01 to GV.SC-04).
4. **Run the first IR tabletop exercise** (covers `RS.MA-01`, `RS.AN-03`). Use a scenario relevant to the org (e.g., ransomware on the ERP system, customer data breach via SaaS supplier). Cost: 1-2 people-weeks; can be internal. (Note: CSF 2.0 starts the RS.AN Subcategory numbering at RS.AN-03 — RS.AN-01 and RS.AN-02 are 1.1-only.)
5. **Complete the asset inventory for Tier-1 systems** (covers `ID.AM-01`, `ID.AM-08`). The Tier-1 systems are the ones that process regulated data (PII, PHI, PCI) or are critical to operations. The full inventory continues into 12-month.
6. **Publish the supply chain risk policy** (covers `GV.SC-01`). Most orgs have procurement policy; few have a cybersecurity supply chain policy. This is a 1-2 page document; cost: 1 person-week.
7. **Stand up the KPI/KRI dashboard** (covers `GV.OV-01`). 5-10 metrics, refreshed monthly. Examples: % of systems with MFA, mean time to detect (DE.CM), mean time to respond (RS.MA), % of policies reviewed in last 12 months (GV.PO-02).
8. **Conduct the first formal risk assessment** (covers `ID.RA-01`). Document threats, vulnerabilities, likelihood, impact for Tier-1 systems. Output: a risk register that feeds the ERM (Enterprise Risk Management) process.

**Cost range (6 months)**: $50K-$200K tool spend + 1-2 dedicated FTE for a mid-market org. For a Series-A SaaS, the realistic 6-month spend is $30K-$80K and 0.5-1 FTE.

## 3. The 12-month strategic investments (formal governance, supply chain, continuous improvement)

Months 7-12 are about **strategic maturity**: supply chain risk management (GV.SC), formal risk governance (GV.RM), continuous improvement, and the first independent assessment. By month 12, the org should be at Tier 2.5-3.0 average across the 6 Functions.

**12-month deliverables:**

1. **Formalize the supply chain risk management program** (covers `GV.SC-01` through `GV.SC-10`). This is the single largest source of new assessment work in CSF 2.0 vs 1.1 (see `chunks/05-govern-function.md` §3). The program includes: supplier inventory, criticality tiering, contracts with cyber requirements, supplier assessments, supplier IR coordination. Cost: 0.5-1 FTE for 6 months; tool spend $20K-$100K (TPRM platform or SaaS GRC).
2. **Integrate cyber into ERM** (covers `GV.RM-03`). The cyber risk register feeds the enterprise risk register; the board's risk committee sees cyber alongside financial, operational, and compliance risk. Cost: 0.25 FTE; mostly policy and governance work.
3. **Achieve the first independent assessment** (covers `GV.OV-03`). Internal audit, external firm, or 3PAO. The independent assessment produces an objective view of the Current Profile and a credibility anchor for the board report. Cost: $50K-$200K for a mid-market org.
4. **Build the detection engineering program** (covers `DE.CM-01`, `DE.AE-02`). This is the most-common strategic investment for orgs at Tier 2.0-2.5 in DETECT. Includes: SIEM/EDR deployment, detection rules authored and tested, on-call coverage. Cost: 1-2 FTE; tool spend $100K-$500K.
5. **Run the first SOC 2 Type II audit** (or equivalent attestation, depending on industry). This is the natural precursor/companion to a CSF Target Profile at Tier 3. Cost: $75K-$200K for a SaaS.
6. **Conduct the first supplier assessment cycle** (covers `GV.SC-04`). All Tier-1 suppliers (the 20 most-critical) assessed via CAIQ, SIG Lite, or equivalent. Cost: 0.5 FTE for 3 months; tool spend included in TPRM platform above.
7. **Mature the IR program to tested** (covers `RS.MA-01`, `RS.AN-03`). Two tabletop exercises in 12 months; one full-scale exercise with cross-functional participation. Cost: 0.25 FTE; tabletop facilitation $5K-$20K.
8. **Run the first annual program review** (covers `GV.OV-02`). Cyber steering committee reviews the year, adjusts the Target Profile, sets the next 12-month investment. This is the governance cadence that matures the program from project to discipline.

**Cost range (12 months)**: $200K-$500K for a mid-market org; $50K-$200K for a small org with heavy contractor use; $500K+ for a large enterprise.

## 4. Sequencing rules (the GOVERN-first rule, the IDENTIFY-second rule)

The implementation order is not arbitrary. CSF 2.0 [NIST-CSF-2.0 §2.1] is explicit: GOVERN sets the context for the other 5 Functions. Two sequencing rules follow from this:

**Rule 1 — assess GOVERN first (months 1-3).** The GOVERN answers (Who owns this? What is our risk appetite? Where is the board involved?) determine what "good" looks like for the other 5 Functions. A Current Profile that starts with PROTECT and gets to GOVERN at the end will produce inconsistent scores because the GOVERN context was not set. Concretely: the cyber steering committee (GV.OV-01), the policy (GV.PO-01), the supply chain policy (GV.SC-01), the risk appetite statement (GV.RM-02), and the roles/RACI (GV.RR-01) all come before the substantive PROTECT/DETECT work.

**Rule 2 — IDENTIFY second (months 2-4).** You cannot protect what you have not identified. The asset inventory (ID.AM-01) and risk assessment (ID.RA-01) are the input to PROTECT prioritization (which assets to protect first) and DETECT scope (which assets to monitor first). Skipping IDENTIFY produces a PROTECT program built on guessed-at scope, and a DETECT program with no clear monitoring target.

**Rule 3 — PROTECT, DETECT, RESPOND, RECOVER in parallel (months 4-12).** The other 4 Functions are not strictly sequential; they are the operational cycle and can be invested in concurrently. A common pattern: PROTECT in months 4-8 (MFA, encryption, training), DETECT in months 6-10 (SIEM/EDR, detection engineering), RESPOND in months 4-12 (IR plan, tabletop, on-call), RECOVER in months 8-12 (BCP/DR, backup testing).

**Anti-pattern — "implement 800-53 first, then map to CSF."** For orgs already subject to 800-53 (federal, DoD), the temptation is to use the 800-53 implementation as the substrate and derive the CSF profile from it. This works for the controls side (IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) but **fails for GOVERN** because 800-53's PM family is not the same as CSF 2.0's GOVERN Function. The board-facing governance language is in CSF GOVERN, not 800-53 PM. Build the GOVERN subcategories from the CSF side; let 800-53 evidence feed the other 5 Functions.

## 5. Resourcing (rough FTE estimates for orgs of various sizes)

The FTE estimates below are **heuristics**, not NIST-mandated. They assume the org is at Tier 1-2 today and targeting Tier 2.5-3.0 in 12 months. An org already at Tier 3 with a mature security program needs 25-50% of these FTE estimates for *maintenance*; this playbook is about *build*, not run.

| Org size (FTE) | Cyber FTE at Tier 1-2 | Cyber FTE at Tier 2.5-3 (12-month target) | Notes |
|----------------|------------------------|-------------------------------------------|-------|
| ≤50 (Series-A SaaS) | 0.25-0.5 (1 engineer at 25-50%) | 1-2 (1 dedicated security hire + 0.5-1 engineer at 25%) | First dedicated security hire usually at month 6-9 |
| 50-250 (Series-B SaaS, small mid-market) | 1-2 | 2-4 | First CISO hire usually at month 3-6 |
| 250-1,000 (mid-market) | 2-4 | 4-8 | CISO + 1-2 dedicated engineers + GRC analyst |
| 1,000-5,000 (large enterprise) | 4-10 | 10-20 | CISO + 5-10 engineers + 2-4 GRC + 1-2 IR |
| 5,000+ (very large enterprise) | 10-25 | 25-50+ | Full security org with SOC, GRC, IR, product security |

**Tool spend** (12-month) for a typical mid-market org ($200K-$500K): SIEM/EDR ($100K-$250K), TPRM platform ($20K-$100K), GRC platform ($25K-$75K), vulnerability management ($25K-$50K), MFA/SSO ($10-$25/user/month), IR retainer ($20K-$50K), training/awareness ($5K-$20K), backup/DR ($25K-$100K). For a small org, the same categories at 25-50% of the mid-market cost; for a large enterprise, 2-3x.

**Contractor vs FTE**: the first 90 days are often heavier on contractor time (policy author, IR plan author, Current Profile facilitation) than FTE. The 6-12 month window is the FTE build-out. A common pattern: 1-2 contractors in months 1-3, the first dedicated FTE hire at month 3-6, the team at steady-state headcount by month 9-12.

## 6. Change management (board, executive, operational)

A CSF program fails more often from change-management gaps than from technical gaps. Three audiences need separate engagement:

**Board (cyber committee)**: engage via the 1-page board report (see `chunks/06-enterprise-reporting.md §6`). Cadence: quarterly. Tone: business consequence, not control detail. Ask: budget approval for the 12-month investment. Risk if not engaged: the program loses funding at the first budget cycle.

**Executive (CEO, CFO, COO, General Counsel)**: engage via the cyber steering committee (monthly) and the ERM integration (quarterly). Tone: risk register entries, regulatory exposure, customer contractual obligations. Ask: cross-functional support for the program (Legal for contract language, HR for training, Procurement for TPRM). Risk if not engaged: the program becomes "the CISO's project" and stalls on cross-functional dependencies.

**Operational (IT, engineering, business unit leaders)**: engage via the Subcategory ownership (GV.RR-04), the KPI/KRI dashboard, and the tabletop exercises. Tone: concrete tasks, named owners, measurable outcomes. Ask: time allocation to close specific gaps. Risk if not engaged: the program produces a Current Profile but no actual gap closure.

**The single biggest change-management failure mode**: treating the CSF program as an annual audit deliverable rather than a quarterly operating cadence. The first board report that produces a Target Profile and a 12-month investment ask is the inflection point. Before that, the program is documentation; after that, the program is operations.

## Cross-references

- `chunks/03-current-profile.md` — the Current Profile YAML is the input to the 90-day quick wins; the 5 most-missing Subcategories are the first roadmap.
- `chunks/04-target-profile-and-gap.md` — the Target Profile + Gap Analysis Table is the input to the 6-month and 12-month deliverables; the prioritization matrix (2x2) is the sequencing rule.
- `chunks/05-govern-function.md` — the GOVERN-first sequencing rule (§4) is the rationale for the 90-day governance work.
- `chunks/06-enterprise-reporting.md` — the 1-page board report template and the trend reporting cadence that the change-management plan is grounded in.
- `nist-800-53-rmf/chunks/04-implement.md` — for orgs subject to 800-53, the CSF Current Profile can be derived from existing 800-53 SSPs (the "800-53 first, then CSF" anti-pattern is discussed in §4 above; the converse is also valid).
- `isaca-audit-methodology` — COBIT 2019 design factors inform the 90-day prioritization and the 12-month strategic investment sequencing.

## Anti-hallucination

- **Authoritative source**: the Implementation Examples in CSF 2.0 [NIST-CSF-2.0 Appendix] are illustrative, not normative. The playbook above is a heuristic built on those examples plus practitioner experience; it is not NIST-mandated.
- **FTE estimates are heuristics, not rules.** The numbers in §5 reflect typical mid-market engagements; an org in a heavily-regulated industry (financial services, healthcare, federal) will run 25-50% higher. An org in a lightly-regulated industry (B2B SaaS, no PHI/PCI) will run 25-50% lower.
- **The quick-wins list is not a checklist of "the only right answers."** The 10 items in §1 are the common first 90 days; an org with a specific regulatory deadline (e.g., NY DFS 500 compliance, CMMC L2 certification) will substitute or reprioritize items. The list is a starting point, not a contract.
- **The GOVERN-first sequencing rule is structural**, not stylistic. The CSF 2.0 publication [NIST-CSF-2.0 §2.1] places GOVERN at the top of the framework, and the per-Category treatment in `chunks/05-govern-function.md` §5 explains the dependency. Skipping GOVERN to "get to the controls faster" produces an inconsistent Current Profile and a Target Profile that does not reflect the org's actual risk tolerance.
- **The 800-53-first anti-pattern is a warning, not a prohibition.** Some orgs (federal, DoD) genuinely start with 800-53 because the federal customer demands it. The warning is about not *deriving* the CSF GOVERN from 800-53 PM; the GOVERN subcategories should be assessed from the CSF side regardless.
- **Change management is more important than the technical work.** Most CSF programs that fail (lose funding, stall at Tier 2 indefinitely) do so because the board or executive engagement lapses, not because the technical work is wrong. The §6 change-management guidance is a load-bearing part of the playbook.
