---
chunk_id: 04-target-profile-and-gap
parent_skill: nist-csf-2
topic: "Target Profile construction and the gap analysis: Current → Target with priorities"
load_when: "user asks about gap analysis, target state, or what to fix first"
---

# Chunk 04 — Target Profile & Gap Analysis

The **Target Profile** is the "where we want to be" view of the org's cybersecurity outcomes. The **gap** between Current and Target is the **work plan** — the prioritized list of remediation items that drives the 12-month execution. This chunk is the second half of the standard CSF engagement: Current Profile (where we are) → Target Profile (where we're going) → Gap (the work) → Roadmap (when each gap closes). See `chunks/03-current-profile.md` for the Current Profile construction.

## 1. What a Target Profile is (and is not)

A Target Profile is:

- The desired set of outcomes the org should achieve, given its **risk tolerance**, **business objectives**, and **applicable regulation**.
- A per-Function **Tier target** (often not uniform — see §2).
- The destination the Current Profile is measured against.
- The bridge from CSF maturity to business strategy: the Target Profile is where the board's risk appetite meets the IT control catalog.

A Target Profile is **not**:

- A "best practice" benchmark copied from another org (it must reflect the org's specific risk).
- A single Tier number (Tiers are per Function).
- A guarantee (achieving the Target Profile is a 12-36 month journey; some Subcategories may never reach Fully Implemented).
- A regulatory requirement (CSF is voluntary; only some industries have CSF-aligned regulation, e.g., NY DFS 500).

## 2. How to set Target Tiers per Function

Target Tiers are **rarely uniform** across the 6 Functions. The typical pattern is:

| Function | Typical target Tier | Rationale |
|----------|---------------------|-----------|
| **GOVERN** | 2 → 3 (mid-market); 3 → 4 (regulated, large enterprise) | Tier 2 = risk-informed; Tier 3 = repeatable, board-visible; Tier 4 = continuous improvement |
| **IDENTIFY** | 3 (most orgs) | Asset inventory and risk assessment are table stakes |
| **PROTECT** | 3 (most orgs); 4 (regulated, high-value data) | Protective controls are the most-invested Function |
| **DETECT** | 2 → 3 | Most orgs lag in detection; Tier 2 is achievable; Tier 3 requires SOC/SIEM maturity |
| **RESPOND** | 2 → 3 | Most orgs have an IR plan at Tier 2; tested IR is Tier 3 |
| **RECOVER** | 2 → 3 | Tier 2 = documented BCP/DR; Tier 3 = tested, with RTO evidence |

**Setting the Target Tier per Function requires 4 inputs:**

1. **Risk tolerance** — how much cyber risk is the board willing to accept? Sets the floor on GOVERN and DETECT.
2. **Business objectives** — what is the org trying to do (new product line, federal customer, M&A target)? Sets the floor on PROTECT and ID.AM.
3. **Applicable regulation** — HIPAA, PCI, NY DFS 500, FFIEC, CMMC, FISMA. Each sets a non-negotiable minimum Tier.
4. **Customer / contractual requirements** — enterprise customers often demand CSF Tier 3+; federal customers demand 800-53 Moderate/High alignment (which forces CSF Tier 3+ in IDENTIFY and PROTECT).

A common **target pattern** is "Tier 3 for GOVERN, IDENTIFY, PROTECT and Tier 2 for DETECT, RESPOND, RECOVER" — this reflects the reality that most orgs can formalize governance and protection faster than they can build out a 24/7 SOC.

**Tier selection is not normative** [NIST-CSF-2.0 §3.1]. The org picks its target based on inputs above; there is no CSF-mandated formula. The heuristics in this chunk are planning aids, not rules.

## 3. Gap analysis workflow

**Procedure** (6 steps):

1. **Take the Current Profile** (per-Subcategory status, evidence, owner) — see `chunks/03-current-profile.md`.
2. **Set the Target Profile** (per-Function Tier target + per-Subcategory target status).
3. **Compute the gap** for each Subcategory: target_status − current_status. The gap is "delta" not "distance" — a Subcategory that is Partially → Fully is a 2-step gap; Not Implemented → Fully is a 3-step gap.
4. **Prioritize the gaps** using the dimensions in §4.
5. **Assign owner, target date, and estimated effort** per gap item. Use the 9-90-365 day windows (see `chunks/07-implementation-playbook.md`).
6. **Emit the Gap Analysis Table** (see §5) — this is the work plan handed to project management.

**Inputs the Target Profile needs from the org:**

- Documented risk tolerance statement (often in a board-approved ERM policy or risk appetite statement).
- Applicable regulation list (e.g., "we process credit card data → PCI DSS v4.0.1 applies").
- Customer contractual obligations (e.g., "we sell to federal agencies → CMMC L2 must be achieved in 18 months").
- Strategic objectives (e.g., "we are pursuing SOC 2 Type II in 9 months").
- 12-month resource envelope (people, budget, executive air cover).

## 4. Priority dimensions and the prioritization matrix

Not all gaps are equal. The 4 priority dimensions to score each gap on:

| Dimension | Question | Scale |
|-----------|----------|-------|
| **Risk reduction** | If we close this gap, by how much do we reduce the org's cyber risk exposure? | 1 (low) – 5 (high) |
| **Regulatory pressure** | Is this gap required by a regulator or contract? | 1 (no pressure) – 5 (immediate enforcement risk) |
| **Cost of implementation** | How much does it cost (in $ and people-months) to close this gap? | 1 (low) – 5 (very high) |
| **Customer demand** | Are customers asking about this specifically in questionnaires? | 1 (rarely) – 5 (blocker for new logos) |

**The prioritization matrix** (2x2 of risk-reduction vs cost-of-implementation):

```
                        Cost of implementation
                       Low            High
                  ┌──────────────┬──────────────┐
   Risk           │  QUICK WINS  │ STRATEGIC    │
   reduction      │  Do first    │ INVESTMENTS  │
   High           │  (90 days)   │ (12-18 mo)   │
                  ├──────────────┼──────────────┤
                  │  FILL-INS    │  DEPRIORITIZE│
                  │  Do as time  │  Or do with  │
                  │  allows      │  strong ROI  │
                  │  (180 days)  │  case        │
                  └──────────────┴──────────────┘
```

- **Quick wins** (high-risk-reduction, low-cost) — do in the first 90 days. Examples: MFA on all admin accounts (PR.AA-03), disable unused services (PR.PS-01), publish the IR plan (RS.MA-01), enable AWS CloudTrail in all regions (DE.CM-01).
- **Strategic investments** (high-risk-reduction, high-cost) — plan for 12-18 months. Examples: SIEM replacement (DE.CM-01 → Tier 3), IAM modernization (PR.AA-01 → Tier 3), third-party risk program (GV.SC-01 → Tier 3).
- **Fill-ins** (low-risk-reduction, low-cost) — do opportunistically between strategic projects. Examples: refine policy wording (GV.PO-01), update training curriculum (PR.AT-01).
- **De-prioritize or strong-ROI-case** (low-risk-reduction, high-cost) — defer or document the business case. Examples: full custom GRC tool (when a SaaS GRC suffices), building in-house SOC (when a co-managed SOC is half the cost).

The **regulatory pressure** and **customer demand** dimensions are **overrides**: any gap with regulatory pressure = 5 or customer demand = 5 should be elevated to "strategic investment" or "quick win" regardless of the cost/benefit position. A NY DFS 500 gap is a Tier-1 priority; an "ISO certification nice-to-have" is a Tier-4 priority.

## 5. Output template: Gap Analysis Table (YAML)

```yaml
profile_type: target
target_date: <YYYY-MM-DD>
profile_owner: <role or name>
function_target_tiers:
  GOVERN:   {tier: 3, rationale: "Board cyber committee + formal risk strategy"}
  IDENTIFY: {tier: 3, rationale: "Asset inventory and risk assessment are table stakes"}
  PROTECT:  {tier: 3, rationale: "Customer contractual obligations"}
  DETECT:   {tier: 2, rationale: "Realistic for current SOC maturity; Tier 3 in 18 months"}
  RESPOND:  {tier: 2, rationale: "IR plan documented; tested IR in 12 months"}
  RECOVER:  {tier: 2, rationale: "BCP/DR documented; tested in 12 months"}
gap_items:
  - gap_id: GAP-001
    subcategory_id: GV.SC-01
    current_status: Not Implemented
    target_status: Largely Implemented
    risk_reduction: 4
    regulatory_pressure: 3
    cost_of_implementation: 3
    customer_demand: 4
    priority_quadrant: STRATEGIC_INVESTMENT
    target_window: 9_months
    owner: <role>
    estimated_effort: <people-months>
    dependencies: [<gap_ids or external>]
  - gap_id: GAP-002
    subcategory_id: PR.AA-03
    current_status: Partially Implemented
    target_status: Fully Implemented
    risk_reduction: 5
    regulatory_pressure: 4
    cost_of_implementation: 1
    customer_demand: 5
    priority_quadrant: QUICK_WIN
    target_window: 90_days
    owner: <role>
    estimated_effort: <0.5 people-months>
summary:
  total_gaps: <int>
  quick_wins: <int>
  strategic_investments: <int>
  fill_ins: <int>
  de_prioritized: <int>
  estimated_total_effort: <people-months>
  estimated_total_cost_usd: <low-high>
```

This Gap Analysis Table is the **work plan** handed to project management and the input to the implementation playbook (`chunks/07-implementation-playbook.md`) and the informative-references crosswalk (`chunks/08-informative-references-crosswalk.md`) when the same evidence must satisfy 800-53, ISO 27001, SOC 2, HIPAA, or PCI.

## 6. Worked example (fictional): continuing the 50-FTE SaaS

**Organization**: "DataRelay Inc." — fictional 50-FTE B2B SaaS (continued from `chunks/03-current-profile.md` §6).

**Target Profile (set with input from CEO + CTO):**

- Function target Tiers: GOVERN 2.5, IDENTIFY 3.0, PROTECT 3.0, DETECT 2.5, RESPOND 2.5, RECOVER 2.5
- Risk tolerance: moderate (B2B SaaS, not regulated, no PHI); customer base is mid-market enterprise requiring SOC 2
- Drivers: SOC 2 Type II in 12 months, enterprise customer demand for "Tier 3-ish" cyber maturity

**Top gaps and prioritization** (subset of the full gap table):

| Gap ID | Subcategory | Current | Target | Risk↓ | Reg | Cost | Cust | Quadrant | Window |
|--------|-------------|---------|--------|-------|-----|------|------|----------|--------|
| GAP-001 | GV.SC-01 (supply chain) | Not Impl | Largely | 4 | 3 | 3 | 4 | Strategic | 9 mo |
| GAP-002 | PR.AA-03 (MFA all users) | Partially | Fully | 5 | 4 | 1 | 5 | Quick win | 30 days |
| GAP-003 | DE.CM-09 (compute monitoring) | Not Impl | Largely | 4 | 2 | 4 | 3 | Strategic | 12 mo |
| GAP-004 | GV.RR-01 (cyber RACI) | Partially | Fully | 3 | 2 | 1 | 2 | Fill-in | 6 mo |
| GAP-005 | RS.MA-01 (IR plan tested) | Partially | Fully | 4 | 3 | 2 | 4 | Quick win | 90 days |
| GAP-006 | DE.CM-01 (network monitoring) | Partially | Fully | 4 | 2 | 3 | 3 | Strategic | 9 mo |

**Summary:** 6 prioritized gaps, 2 quick wins (90 days), 3 strategic investments (9-12 months), 1 fill-in (6 months), estimated total effort ~7-9 people-months over 12 months, estimated cost $50K-$120K (mostly SOC tooling and external IR retainer).

This is a realistic first-roadmap for a 50-FTE SaaS targeting SOC 2 + CSF Tier 2.5/3 in 12 months.

## Cross-references

- `chunks/02-tiers-and-profiles.md` — Tiers 1-4 and the 4 Profile types; the Target Profile is one Profile type.
- `chunks/03-current-profile.md` — the Current Profile is the input to the gap analysis.
- `chunks/07-implementation-playbook.md` — how to sequence and resource the gap closure (9-90-365 day playbook).
- `chunks/08-informative-references-crosswalk.md` — when the gap closure must satisfy 800-53 / ISO 27001 / SOC 2 / HIPAA / PCI / COBIT, this is the crosswalk.

## Anti-hallucination

- **Authoritative source**: Target Profile and gap analysis concept is from NIST CSF 2.0 [NIST-CSF-2.0 §3.2] (Feb 26, 2024). The "gap = Target − Current" framing is standard practice; CSF 2.0 does not prescribe a specific calculation method.
- **The prioritization matrix is a planning heuristic**, not a NIST-mandated method. The 2x2 (risk reduction × cost) and the 4 priority dimensions (risk, regulatory, cost, customer) are common practice; the org can use any prioritization scheme that is documented and consistently applied.
- **Tier selection is not normative** [NIST-CSF-2.0 §3.1]. The "Tier 3 for GOVERN/IDENTIFY/PROTECT, Tier 2 for DETECT/RESPOND/RECOVER" pattern is a heuristic that reflects the reality of most mid-market orgs; it is not a CSF rule.
- **The worked example is fictional** ("DataRelay Inc." is a placeholder). The gap priorities, cost estimates, and target windows are illustrative of a typical 50-FTE SaaS; they are not an actual engagement.
- **Regulatory pressure is an override** in the prioritization matrix. A gap with regulatory pressure = 5 (immediate enforcement risk) should be elevated to top priority regardless of cost/benefit position. Do not apply the 2x2 matrix mechanically when an enforcement action is on the table.
- **The gap is the work plan, not the roadmap.** The roadmap adds sequencing, dependencies, resource constraints, and 9-90-365 day windows — that lives in `chunks/07-implementation-playbook.md`. The gap analysis is the input; the roadmap is the output.
