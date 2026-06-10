---
chunk_id: 06-enterprise-reporting
parent_skill: nist-csf-2
topic: "Executive reporting: 6-function radar, board-level maturity scorecard, and trend reports"
load_when: "user asks for a board report, executive summary, or 6-function radar"
---

# Chunk 06 — Enterprise Reporting

CSF 2.0 is the most executive-legible framework in the NIST family [NIST-CSF-2.0 §2.1] — its 6 Functions map almost 1:1 to the questions a board or audit committee asks ("do we know what to protect?", "are we protected?", "would we notice an attack?", "could we respond and recover?"). This chunk covers the reporting artifacts that translate the Current Profile (see `chunks/03-current-profile.md`), Target Profile (see `chunks/04-target-profile-and-gap.md`), and GOVERN outcomes (see `chunks/05-govern-function.md`) into board-ready output. The visualizations and templates here are common reporting conventions; they are not NIST-mandated.

## 1. The bridge reporting angle — why CSF is the executive framework

Of the 6 skills in this library, only `nist-csf-2` carries the `BOTH` persona (IT + executive). The other skills are IT-facing (`nist-800-53-rmf`, `audit-workpapers`), FIN-facing (`coso-internal-controls`, `aicpa-soc-reporting`), or GRC-facing (`isaca-audit-methodology`). The reporting angle here is the **bridge**: the same CSF language is spoken by the CISO in the SOC, the CIO in the steering committee, and the CISO in front of the board.

Three rules of CSF executive reporting:

1. **Lead with outcomes, not controls.** The board does not want to hear "AC-2(11) is not implemented"; they want to hear "we cannot yet enforce usage conditions on privileged accounts in 48 hours." Use the CSF Subcategory outcome language (`PR.AA-01` — "Identities and credentials are managed") and translate to board language in a one-line caption.
2. **Show the 6 Function scores, not the 106 Subcategories.** A 106-row table is unreadable in a 12-slide deck. The 6-function radar + per-Function Tier is the executive summary; the 106-row Subcategory table is the appendix the CISO walks through on request.
3. **Always show the gap, not just the current state.** The board cares about the trajectory: "we are at Tier 2 in DETECT today, Tier 3 by Q4 next year, Tier 4 within 24 months." Current state alone is a snapshot; gap + trend is the story.

## 2. The 6-Function radar (markdown table form)

The 6-function radar is the canonical CSF executive visualization. Each Function is scored on the Tier 1-4 scale (see `chunks/02-tiers-and-profiles.md`); the radar plots the 6 scores as a polygon. When a chart tool is unavailable, the markdown table below is the fallback (sortable, printable, paste-into-deck friendly).

Fractional Tier values (2.5, 3.5) and per-Function Tier scoring are a **practitioner house
convention** for radar plotting — NIST applies Tiers to Organizational Profiles and is explicit
that Tiers are not maturity levels. Label them as a management convention in any board artifact.

| Function | Current Tier | Target Tier | % Gap | Top 3 Subcategory Gaps |
|----------|-------------|-------------|-------|------------------------|
| **GOVERN** | 2.5 | 3.0 | 33% | `GV.SC-04`, `GV.OV-01`, `GV.RR-03` |
| **IDENTIFY** | 3.0 | 3.0 | 0% | (no gap) |
| **PROTECT** | 3.5 | 3.5 | 0% | (no gap) |
| **DETECT** | 2.0 | 3.0 | 50% | `DE.CM-01`, `DE.CM-09`, `DE.AE-02` |
| **RESPOND** | 3.0 | 3.0 | 0% | (no gap) |
| **RECOVER** | 3.0 | 3.0 | 0% | (no gap) |

**% gap formula** (per Function): `(target_tier - current_tier) / (4 - current_tier) * 100`. This expresses the gap as a fraction of the *remaining* journey to Tier 4 — it is the "how far do we still have to go" view, not a linear "25% per Tier" view. Worked: Tier 3 → target 4 = 100% (the whole remaining journey); Tier 2 → target 3 = 50%; Tier 2.5 → target 3.0 = 33%; Tier 2.0 → target 3.0 = 50% (the table above uses exactly these values). This is a planning heuristic, not a NIST calculation — consider whether a "% of remaining journey" metric helps your board before using it.

**Mermaid radar alternative** (for Markdown-rendering tools that support Mermaid):

```mermaid
%%{init: {"radar": {"axisLabels": ["GOVERN","IDENTIFY","PROTECT","DETECT","RESPOND","RECOVER"]}}}%%
radar
  title CSF 6-Function Radar (Tier 1-4)
  axis 1,2,3,4
  "Current" : 2.5, 3.0, 3.5, 2.0, 3.0, 3.0
  "Target"  : 3.0, 3.0, 3.5, 3.0, 3.0, 3.0
```

The radar and the table are the same data. Pick whichever renders in the consumer's tool.

## 3. The maturity scorecard (one row per Function)

The scorecard is the one-page artifact for the board pre-read. One row per Function, with the executive question, the current/target Tier, the top 3 lagging Subcategories, and the business consequence in board language.

| # | Function | Executive question | Current → Target | Top 3 lagging Subcategories | Business consequence (board language) |
|---|----------|--------------------|------------------|------------------------------|----------------------------------------|
| 1 | **GOVERN** | Are we governed for cyber risk? | 2.5 → 3.0 | `GV.SC-04`, `GV.OV-01`, `GV.RR-03` | "We have a third-party risk policy on paper but do not routinely assess our top-20 suppliers; board oversight cadence is informal." |
| 2 | **IDENTIFY** | Do we know what we are protecting? | 3.0 → 3.0 | (no gap) | "Asset inventory and risk assessment are at board-approved maturity." |
| 3 | **PROTECT** | Are our safeguards adequate? | 3.5 → 3.5 | (no gap) | "MFA, encryption, training, and platform security are formally approved and operating." |
| 4 | **DETECT** | Would we notice an attack? | 2.0 → 3.0 | `DE.CM-01`, `DE.CM-09`, `DE.AE-02` | "We can detect known-bad network traffic but lack a tested detection-engineering program for novel threats." |
| 5 | **RESPOND** | Could we contain and remediate? | 3.0 → 3.0 | (no gap) | "IR plan is documented, tested annually, with regulator notification playbook." |
| 6 | **RECOVER** | Could we restore operations? | 3.0 → 3.0 | (no gap) | "BCP/DR tested in the last 12 months; RTO/RPO documented and met." |

The "Business consequence" column is the one a board reads aloud. The "Top 3 lagging Subcategories" column is the one the CISO walks through on request. The two columns together satisfy the dual audience: board for narrative, CISO for depth.

## 4. Trend reporting (quarterly delta tracking)

Maturity is a *trajectory*, not a snapshot. The trend report tracks quarter-over-quarter (QoQ) movement in the 6 Function Tiers. Trend reporting requires at least 2 quarters of data; the first report establishes the baseline.

| Function | Q1 | Q2 | Q3 | Q4 | 12-mo Δ | Direction |
|----------|----|----|----|----|---------|-----------|
| GOVERN | 2.0 | 2.0 | 2.5 | 2.5 | +0.5 | Improving (CISO hired; cyber committee stood up) |
| IDENTIFY | 2.5 | 3.0 | 3.0 | 3.0 | +0.5 | Improving (asset inventory completed) |
| PROTECT | 3.0 | 3.5 | 3.5 | 3.5 | +0.5 | Improving (org-wide MFA deployed) |
| DETECT | 1.5 | 1.5 | 2.0 | 2.0 | +0.5 | Lagging (SOC engineering hiring in progress) |
| RESPOND | 2.5 | 3.0 | 3.0 | 3.0 | +0.5 | Improving (IR plan tested with regulator) |
| RECOVER | 2.5 | 2.5 | 3.0 | 3.0 | +0.5 | Improving (BCP/DR tabletop completed) |

**Trend interpretation rules:**

- **Sustained flatness** in a Function over 4+ quarters is a red flag, not a steady state. It usually means the program has no owner or no investment.
- **Q1-to-Q2 step-change** in any Function is suspicious: either the scoring methodology changed, or the Function was mis-scored in Q1. The narrative should explain the step.
- **Quarterly ±0.25 noise** is normal — do not over-report it. In practitioner experience, an actively-investing program moves about a half-Tier per quarter at most (unsourced heuristic — calibrate to your own history).
- **Reverse trend** (a Function dropping QoQ) is rare and always significant. Treat as a "stop the line" event; investigate before reporting.

## 5. Anti-trend bad signs (what "all green" really means)

A board report that shows "all Functions at target, no gaps" is **more suspicious** than one that shows honest gaps. The all-green report is the signal of a self-attestation problem: the org scored itself, did not get an independent view, and produced a feel-good report.

Bad signs to look for (and to avoid producing):

- **All Functions at the same Tier** (e.g., everything is Tier 3). Real postures are uneven — a common pattern in practitioner experience is stronger PROTECT than GOVERN (unsourced heuristic), not uniform scores.
- **No top-3 lagging Subcategories** in any Function. Even Tier 4 orgs have 1-2 Subcategories that are perpetually partially-implemented.
- **No business consequence in board language**. The Subcategory IDs are not in the board deck; the consequence of the gap is.
- **No 12-month investment ask**. If there is no investment tied to the gap, the report is not actionable.
- **No owner for any gap item**. The board is not the body that closes gaps; the CISO is, with named owners.
- **All trend arrows in the same direction**. Real trends are mixed: one Function improving while another stalls.

**Counter-signs of a credible report**: the radar is uneven; the GOVERN Function is usually the lowest Tier (because GOVERN is the new Function in 2.0 and most orgs under-invest in it); the top-3 lagging Subcategories include `GV.SC-*` (supply chain governance is the most-likely-incomplete area); the 12-month investment ask is named in dollars and people.

## 6. The 1-page board report template (inline, markdown)

This template is the one-page artifact the CISO hands the board 48 hours before the cyber committee meeting. It is **inline** in this chunk (per the spec — not a separate file) so the consumer can copy-paste it into a deck, a doc, or a Confluence page.

```markdown
# Cyber Maturity Report — [ORG NAME] — [QUARTER / DATE]

## 1. Executive Summary (3 sentences)
- [Org] is currently at an average CSF Tier of [X.X] across the 6 Functions, with a target Tier of [Y.Y] within [12 / 18 / 24] months.
- The largest maturity gap is in [FUNCTION], where [N] Subcategories are not yet at target.
- We are requesting [$X.X]M in [FY] cyber investment to close the top [N] gap items; [N] are regulatory-mandated.

## 2. 6-Function Radar (visualization)
[Insert radar chart or table from §2 above]

## 3. Maturity Scorecard (one row per Function)
[Insert table from §3 above]

## 4. Trend (QoQ)
[Insert trend table from §4 above — omit on first report]

## 5. Top 3 Priority Gaps (the 12-month ask)
| # | Subcategory | Owner | Target window | Investment | Regulatory? |
|---|-------------|-------|---------------|-----------|-------------|
| 1 | [e.g., GV.SC-04 supplier assessment] | [Title] | [Q1-Q2] | $[X.X]M | [Yes/No] |
| 2 | [e.g., DE.CM-01 network monitoring] | [Title] | [Q2-Q3] | $[X.X]M | [Yes/No] |
| 3 | [e.g., PR.AA-03 MFA all users] | [Title] | [Q1] | $[X.X]M | [Yes/No] |

## 6. Governance Cadence
- Board cyber committee: [meets quarterly / bi-annually] — last met [date], next [date]
- CISO reporting line: [to CEO / to CIO / dual]
- Last independent assessment: [date] by [3PAO / internal audit / external firm]
- Next independent assessment: [date]

## 7. Risk Posture Statement
"The cyber program is [on track / at risk / off track] against the [12/24]-month target. The top risks are [R1], [R2], [R3] (see Appendix A). No [regulator enforcement actions / material incidents / unmitigated HIGH findings] in the reporting period."

## 8. Appendices (linked, not inline)
- A. Full 106-Subcategory Current Profile (YAML)
- B. Full Gap Analysis Table (YAML)
- C. 12-month Roadmap (Gantt or table)
- D. Crosswalk to [800-53 / SOC 2 / ISO 27001] (per chunk 08)
```

This 1-page template is a **suggested structure**, not NIST-mandated. Adapt to the org's reporting style; the load-bearing elements are the 6-function radar, the top-3 priority gaps, the investment ask, and the governance cadence.

## Cross-references

- `chunks/01-functions-categories.md` — the 6 Functions, Categories, and Subcategories that populate the radar.
- `chunks/04-target-profile-and-gap.md` — the Target Profile and gap table that feed the scorecard and the top-3 priority list.
- `chunks/05-govern-function.md` — the GOVERN deep-dive that becomes the executive-legible appendix (GV.OV, GV.SC subcategories populate the KPI/KRI dashboard).
- `chunks/07-implementation-playbook.md` — the implementation sequencing that the 12-month investment ask is grounded in.
- `aicpa-soc-reporting` — SOC 2 board reporting patterns (the board deck structure borrows from the SOC 2 reporting conventions in `aicpa-soc-reporting/assets/`).
- `isaca-audit-methodology` — COBIT 2019's goals cascade informs the Function → Category → KPI drill-down for the trend report.

## Anti-hallucination

- **Authoritative source**: CSF 2.0 [NIST-CSF-2.0 §2.1, §3.1, §3.2] is the framework reference. The 6-function radar is a **common reporting convention** used by GRC practitioners; it is not NIST-mandated. The 1-page board report template is a **suggested structure** drawn from SOC 2 board reporting and GRC practice; it is not NIST-mandated.
- **Per-Function Tier scoring, fractional Tiers, and Tier averages are practitioner conventions, NOT NIST methodology.** CSWP 29 applies Tiers to Organizational Profiles and Tiers are not maturity levels. If the radar/scorecard uses per-Function or fractional Tiers, state the methodology as the org's own on the face of the artifact, and never report a "Tier average" without that label — "how did you arrive at Tier 1.8 and whose methodology is it?" must have an answer.
- **The "all green" report is suspect.** Real maturity is uneven. A board report that shows no gaps in any Function is a self-attestation problem, not a mature program. The anti-trend-bad-signs in §5 are heuristics from GRC practice, not NIST rules.
- **% gap formula** in §2 is a planning heuristic, not a NIST calculation. CSF 2.0 does not prescribe how to compute a "gap percentage"; this skill uses `(target - current) / (4 - current) * 100` to express the gap as a fraction of the remaining journey to Tier 4.
- **The board report template** in §6 is a starting structure. Adapt to the org's governance culture, regulator expectations (e.g., NY DFS 500 §500.04 has board reporting specifics), and reporting cadence. Do not present it as a NIST template.
- **Trend reporting requires baseline data.** The first quarter of trend reporting establishes the baseline; QoQ deltas are meaningful from Q2 onward. Do not invent trend data to fill the trend table on a first report.
