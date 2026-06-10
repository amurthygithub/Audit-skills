# NIST CSF 2.0 Skill — Design Document

> **Status:** Design — for review Monday, then conversion into build plan.
> **Linear:** SOX-569 (A4 — Skill: nist-csf-2)
> **Branch:** main
> **Repo root:** `/Users/amurthy/Code/Audit-skills`
> **Reference architecture:** `skills/nist-800-53-rmf/` (v0.2.1, 29 tests, all linters green)
> **Linter:** `tools/lint_skill.py` (Tier 0a, SOX-616)
> **Consistency library:** `tests/test_consistency_lib.py`
> **Template:** `skills/TEMPLATE/` and `docs/skill-design-template.md` (this doc was the first fully-filled example)
> **Companion document:** `docs/builds/csf-2/nist-collation.md` (CSF 2.0 listed as P2 next-move)

---

## 0. Why this design doc exists

The CSF 2.0 skill will sit alongside the existing 5 skills in `Audit-skills/`. To avoid re-inventing the review surfaces that worked for `nist-800-53-rmf` (5-lens review, 5-practitioner review, fix waves, cross-skill consistency, CI/CD), this design doc is structured so that every phase of the build has a corresponding review surface defined up front.

The CSF 2.0 skill is the **bridge skill** — the most executive-legible framework in the NIST family. It is the natural GTM lever for Week 5 and the natural dependency of the planned FedRAMP skill (SOX-574, Wk 9). It is also the only NIST-family skill that explicitly requires the **GOVERN** function (new in 2.0), which is where most executive-level risk language lives.

The risk of under-designing this skill: the GOVERN function and the **Current/Target Profile** terminology are easy to mis-represent, and the executive-legibility promise is easy to over-claim. The build plan below treats both as load-bearing design decisions.

---

## 1. Scope & dependencies

### 1.1 Standard reference (primary source)

- **NIST Cybersecurity Framework (CSF) 2.0** — National Institute of Standards and Technology, February 26, 2024.
- Retrieval URL: `https://www.nist.gov/cyberframework`
- Companion documents: NIST SP 1300 (CSF 2.0 Profile success story), NIST SP 1299 (CSF 2.0 small business quick-start guide), and the official **Informative References** spreadsheet mapping CSF Subcategories to ~50 other frameworks (NIST 800-53, ISO 27001, COBIT 2019, CIS Controls v8, NIST SP 800-171 Rev 3, etc.).
- The skill must cite CSF 2.0 by its official identifier `[NIST-CSF-2.0 §X.Y]` and resolve every in-body citation through `## 10. References & Citation Manifest`.

### 1.2 Structural inventory (what we are encoding)

| Layer | Count | Source of truth |
|-------|-------|-----------------|
| **Functions** | 6 | NIST CSF 2.0 §2.1: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER |
| **Categories** | 22 (was 23 in 1.1; merged in 2.0) | NIST CSF 2.0 §2.2 — see chunk 02 |
| **Subcategories** | ~108 (CSF 2.0 lists 106 numbered subcategories with sub-letters) | NIST CSF 2.0 §2.3 |
| **Tiers** | 4 | NIST CSF 2.0 §3.1: Tier 1 (Partial), Tier 2 (Risk Informed), Tier 3 (Repeatable), Tier 4 (Adaptive) |
| **Profiles** | 4 kinds | NIST CSF 2.0 §3.2: Current Profile, Target Profile, Organizational Profile, Community Profile |
| **Implementation Examples** | per-subcategory | NIST CSF 2.0 Appendix (illustrative; not normative) |
| **Informative References** | external map | NIST CSF 2.0 "Informative References" spreadsheet (CSF subcategory → 800-53, ISO 27001, COBIT, CIS, etc.) |

The skill's role is to **encode the framework** and provide **output templates** for the four kinds of profile; it does not generate the implementation examples (those are illustrative NIST material) and it does not author Community Profiles (those are sector-coordinating-body outputs).

### 1.3 Persona: **BOTH (IT + executive)**

CSF 2.0 is the only NIST-family framework that is explicitly designed for both IT practitioners and executive decision-makers. This is reflected in the **Persona** field of Linear. The design implications:

- The router SKILL.md must read as a one-page summary an executive can understand in 90 seconds.
- The chunks must produce **board-ready output** (6-function radar, Tier 1→4 trajectory, Current/Target gap table) alongside the IT-facing detail.
- The 4-quadrant industry view (4 industry files) is the bridge between the executive view and the vertical-specific regulation layer.

This is also the **only** skill in the library with the `BOTH` persona. All others are `IT` (nist-800-53-rmf, audit-workpapers), `FIN` (coso, aicpa), or `GRC` (isaca). The build plan treats the `BOTH` persona as a contract: every artifact (UC, industry view, output template) is reviewed against "would an executive understand this without an IT translator?"

### 1.4 Effort: M (per Linear)

The Linear issue (SOX-569) sets effort = M. Estimate: **1–2 days of focused work** (matching the `nist-collation.md` note). Build sequence is in §12. The M estimate assumes:

- Day 1 = scaffold + router + chunks skeleton
- Day 2 = industries + UCs + data
- Day 3 = tests + linter green
- Day 4 = 5-lens review
- Day 5 = 5-practitioner review + fix waves

The M estimate **does not** include the public release (Wk 5 LI post), external PRs, or follow-on improvements. Those are tracked separately.

### 1.5 Dependencies (per Linear)

| ID | Type | Status | What we use from it |
|----|------|--------|---------------------|
| **SOX-566** (A1 — nist-800-53-rmf) | **Depends on** | Done (v0.2.1) | The CSF ↔ 800-53 informative references; the `data/crosswalks/` shape we mimic; the FIPS 199 + Tier 3/4 inheritance vocabulary; the questionnaire-reuse pattern; the cross-skill `5-part finding` template. **Load-bearing**: if 800-53 is not stable, our crosswalk cannot be authoritative. |
| SOX-611 (Phase 2 migration) | Informs | Backlog | Cross-skill consistency library; chunk frontmatter schema; manifest bidirectionality. We reuse `tests/test_consistency_lib.py` unchanged. |
| SOX-618 (Phase 0.3 source-text acquisition) | Informs | Backlog | Will catalog CSF 2.0 PDF + OSCAL representation as free sources. We do not block on it but we should structure the chunk text so the OSCAL machine-readable mapping can be added in v0.3.x. |

### 1.6 What is **out of scope** (explicit non-goals for v0.1.0)

- **OSCAL machine-readable representation** — referenced in §1.5 as a v0.3.x follow-on. The skill does not require OSCAL to operate.
- **Community Profile authoring** — we ship the **shape** of a Community Profile in `data/seeds/` (e.g., a synthetic "Financial Services Community Profile v0.1" reduced to 6 functions × 22 categories) but do not assert sector authority.
- **Implementation Examples** (the appendix) — we cite them where useful but do not reproduce them. The appendix is illustrative, not normative.
- **Tier selection algorithm** — CSF 2.0 does not define how an org picks its Tier; it describes the Tier characteristics. We encode the Tier definitions and a heuristic (see chunk 05), not a normative selection rule.
- **Quantitative risk scoring** — CSF 2.0 is maturity-based, not risk-score-based. We do not invent a numeric score; we use the Tier 1–4 ordinal scale and the Function/Category heatmap.
- **The CSF 1.1 vs 2.0 reconciliation** — we ship CSF 2.0 only. A footnote in `## 9. Anti-Hallucination Disclaimers` notes that 1.1-era materials (Function = Identify/Protect/Detect/Respond/Recover without GOVERN) are not represented in this skill.

---

## 2. Chunk architecture (8 chunks proposed)

The 800-53 RMF skill ships 8 chunks numbered 02–09 (gap left at 01 — the router itself is chunk 0 in that skill's logic). For CSF 2.0 we propose **8 chunks** numbered 01–08, with chunk 01 covering the smallest-loadable "what is CSF 2.0" overview and chunk 08 covering the cross-framework informative-references crosswalk. The numbering aligns to the 4-quadrant flow:

- 01–02 = orient (Functions, Tiers)
- 03 = build a Current Profile
- 04 = build a Target Profile + the gap
- 05 = GOVERN-centric (the new function; deserves its own chunk because every review lens will focus on it)
- 06 = enterprise reporting (radar, board, maturity)
- 07 = implementation playbook (small org → large org, cost-aware)
- 08 = crosswalk (CSF ↔ 800-53, ISO 27001, COBIT, CIS, HIPAA Security Rule, SOC 2, etc.)

Each chunk follows the chunk frontmatter contract from `tests/test_consistency_lib.py` (`chunk_id`, `parent_skill`, `topic`, `load_when`); each is ≤ 200 lines; each is kebab-case; each is referenced from the SKILL.md §11 routing table.

### 2.1 Chunk 01 — `01-functions-categories.md`

- **Frontmatter** — `chunk_id: 01-functions-categories`, `parent_skill: nist-csf-2`, `topic: "Functions, Categories, Subcategories (the 6/22/108 spine)"`, `load_when: "user asks 'what is CSF 2.0', 'how many functions', 'list categories', 'explain GOVERN', or 'what is the new function in 2.0'"`.
- **Trigger phrases** — "what is CSF 2.0", "list the 6 functions", "what changed from 1.1", "what is GOVERN", "subcategory GV.OC", "what is DE.CM", "how is PR.AC different from PR.AC-1", "108 subcategories".
- **Body** —
  - The 6 Function table with 1-line definition each (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER).
  - The 22 Categories table grouped by Function.
  - The ~108 Subcategories table (or a "see `data/crosswalks/csf-2-0-subcategories.json`" pointer to the full list; a 108-row markdown table is borderline-readable).
  - The 1.1 → 2.0 delta: GOVERN added; 1.1 categories renamed/merged; subcategory re-organization in PR (now PR.AA, PR.AC, PR.DS, PR.PS, PR.IR, PR.PT).
  - Anti-hallucination note: "subcategory count" is ~108 in CSF 2.0; some count 106 (excluding sub-letter items). Verify against the official CSF 2.0 PDF.
- **Cross-references** —
  - To 800-53 RMF: `nist-800-53-rmf/chunks/02-categorize.md` (FIPS 199 informs the C/I/A of CSF Profile scope, but the two are not the same).
  - To other skills: `audit-workpapers/chunks/01-standards-and-structure.md` (the 5-part finding pattern is reused for the gap analysis).

### 2.2 Chunk 02 — `02-tiers-and-profiles.md`

- **Frontmatter** — `chunk_id: 02-tiers-and-profiles`, `parent_skill: nist-csf-2`, `topic: "Tiers 1-4 and the 4 Profile types (Current / Target / Organizational / Community)"`, `load_when: "user asks 'what tier are we', 'current profile', 'target profile', 'community profile', 'organizational profile', or 'how do we score ourselves'"`.
- **Trigger phrases** — "Tier 1", "Tier 2", "Tier 3", "Tier 4", "Adaptive", "Repeatable", "Risk Informed", "Partial", "current profile", "target profile", "community profile", "organizational profile", "tier selection".
- **Body** —
  - The 4 Tiers table with characteristic, process, organization-wide risk management, and external participation columns.
  - The 4 Profile types: definitions + when each is used + who authors it.
  - The Current/Target gap concept: the "delta" between Current and Target is the **work plan**.
  - Tier selection is **not** a normative algorithm; we provide a heuristic (see §3.2 of the chunk).
  - Community Profiles referenced: e.g., the "Financial Services Cyber Profile" (industry-coordinating), "Healthcare Sector CSF Profile" (HHS-coordinating). We list pointers; we do not reproduce.
- **Cross-references** —
  - To 800-53 RMF: the FIPS 199 categorization is *not* the same as a Tier; we explicitly call this out.
  - To coso: COSO's "maturity model" (Principle 8) overlaps conceptually with Tiers; we note the link.
  - To isaca: COBIT 2019's PAM (Process Assessment Model) is a Tier-1-to-Tier-5 maturity scale; we map Tiers ↔ PAM 0–5.

### 2.3 Chunk 03 — `03-current-profile.md`

- **Frontmatter** — `chunk_id: 03-current-profile`, `parent_skill: nist-csf-2`, `topic: "Building a Current Profile (the As-Is state across all 108 Subcategories)"`, `load_when: "user asks 'how do we build a current profile', 'as-is assessment', 'where are we today', 'baseline our CSF state'"`.
- **Trigger phrases** — "build a current profile", "as-is", "where are we today", "baseline assessment", "maturity assessment", "108 subcategory assessment", "self-assessment".
- **Body** —
  - Inputs: org context, mission, risk tolerance, the 22 categories × 108 subcategories checklist.
  - Procedure (5–7 steps): scope, gather evidence, score each subcategory (Not Implemented / Partially / Largely / Fully implemented — the CSF 2.0 illustrative scale), document evidence, identify governance owner per Function.
  - Output template — **Current Profile YAML** (per subcategory: `status`, `evidence_refs`, `tier_indicator`, `owner`, `notes`).
  - GOVERN-centric reminder: the GOVERN function should be assessed **first** because it sets the context for the other five.
- **Cross-references** —
  - To 800-53 RMF: 800-53A assessment is the "control" parallel; CSF Current Profile is the "outcome" parallel. The two inform each other.
  - To isaca: COBIT 2019 process capability assessment uses the same evidence structure.

### 2.4 Chunk 04 — `04-target-profile-and-gap.md`

- **Frontmatter** — `chunk_id: 04-target-profile-and-gap`, `parent_skill: nist-csf-2`, `topic: "Building a Target Profile and computing the Current/Target gap"`, `load_when: "user asks 'target profile', 'to-be state', 'gap analysis', 'roadmap', 'what do we need to get there'"`.
- **Trigger phrases** — "target profile", "to-be", "gap analysis", "roadmap", "current vs target", "remediation plan", "12-month plan", "maturity target".
- **Body** —
  - Inputs: Current Profile + risk tolerance + business objectives + applicable regulation.
  - Procedure: define Target Tier per Function (often Tier 3 for IT, Tier 2 for small orgs), score each subcategory at the Target state, compute the **delta**.
  - Output: **Gap Analysis Table** (per subcategory: current_status, target_status, priority, owner, target_date, estimated_effort).
  - The gap is the **work plan** — this is the artifact that drives 12-month execution.
  - Worked subcategory example: GV.OC-01 (organizational mission understood) — typically Tier 3 fully implemented by mid-market orgs within 6 months; Tier 4 takes 18+ months.
- **Cross-references** —
  - To coso: deficiency classification (Significant Deficiency / Material Weakness) is the financial-reporting analog of "high-priority gap".
  - To 800-53 RMF: POA&M item format is reused for the gap remediation items.

### 2.5 Chunk 05 — `05-govern-function.md`

- **Frontmatter** — `chunk_id: 05-govern-function`, `parent_skill: nist-csf-2`, `topic: "The GOVERN function (new in CSF 2.0) — categories GV.OC, GV.RM, GV.SC, GV.SR, GV.PO, GV.OV, GV.MT"`, `load_when: "user asks 'GOVERN function', 'what is GOVERN', 'GV.OC', 'GV.RM', 'GV.SC', 'GV.SR', 'GV.PO', 'GV.OV', 'GV.MT', 'cyber governance', 'board oversight', 'cyber risk strategy'"`.
- **Trigger phrases** — "GOVERN", "GV.OC", "GV.RM", "GV.SC", "GV.SR", "GV.PO", "GV.OV", "GV.MT", "new function", "board oversight", "cyber risk strategy", "supply chain risk governance", "roles and responsibilities", "policy oversight".
- **Body** — this chunk deserves its own file because it is the **new function in 2.0**, the **most likely review focus**, and the **executive-facing content**. The 6 GOVERN categories in detail:
  - **GV.OC** Organizational Context (mission, stakeholders, legal/regulatory)
  - **GV.RM** Risk Management Strategy (risk tolerance, appetite, constraints)
  - **GV.SC** Cybersecurity Supply Chain Risk Management (the 2.0 elevation of supply chain from SR-only to a GOVERN-anchored concern)
  - **GV.SR** Security Roles, Responsibilities, and Authorities (RACI, ownership)
  - **GV.PO** Policy, Process, and Procedure (the "we have a policy" answer)
  - **GV.OV** Oversight (board, audit committee, governance reporting cadence)
  - **GV.MT** Monitoring & Measurement (KPIs, KRIs, how we know governance is working)
- For each: definition, subcategories, executive-facing question, evidence examples, and a 1-paragraph board-language description.
- **Cross-references** —
  - To coso: GOVERN maps cleanly to COSO Principle 1 (board oversight), Principle 4 (risk appetite), Principle 12 (policies & procedures).
  - To aicpa: SOC 2 CC1 (Control Environment) is the SOC-side analog.

### 2.6 Chunk 06 — `06-enterprise-reporting.md`

- **Frontmatter** — `chunk_id: 06-enterprise-reporting`, `parent_skill: nist-csf-2`, `topic: "Enterprise-level reporting: 6-function radar, board deck, KPI/KRI, maturity trend"`, `load_when: "user asks 'board report', 'executive deck', 'maturity radar', 'KPI', 'KRI', 'how do we report CSF to leadership', 'cyber risk committee'"`.
- **Trigger phrases** — "board report", "board deck", "executive report", "6-function radar", "cyber dashboard", "KPI", "KRI", "maturity trend", "audit committee", "cyber risk committee", "heat map".
- **Body** —
  - The **6-function radar chart** as a board-friendly visualization (with the Mermaid or ASCII-radar equivalent).
  - KPI/KRI examples per Function (e.g., GV.MT-04 → % of policies reviewed in last 12 months; DE.CM-09 → mean time to detect).
  - **Board deck template** (12-slide outline: mission, regulatory context, current maturity, target maturity, 6-function radar, 3 highest-priority gaps, investment ask, 12-month roadmap, governance, next steps).
  - Maturity trend: how to plot quarter-over-quarter movement.
- **Cross-references** —
  - To aicpa: the board deck structure borrows from the SOC 2 board reporting patterns in `aicpa-soc-reporting/assets/`.
  - To isaca: COBIT 2019's goals cascade informs the Function → Category → KPI drill-down.

### 2.7 Chunk 07 — `07-implementation-playbook.md`

- **Frontmatter** — `chunk_id: 07-implementation-playbook`, `parent_skill: nist-csf-2`, `topic: "Cost-aware implementation playbook (small org, mid-market, large enterprise)"`, `load_when: "user asks 'how do we implement this', 'cost to implement', 'small org CSF', 'mid-market CSF', 'phased rollout', 'first 90 days'"`.
- **Trigger phrases** — "implement", "first 90 days", "small business", "mid-market", "phased rollout", "cost to implement", "minimum viable CSF", "no budget", "two-person team".
- **Body** —
  - The **3 personas** (small org, mid-market, large enterprise) with first-90-day, 6-month, 12-month paths.
  - Small org (≤50 FTE, 1 IT person): tier-2 target, GOVERN + IDENTIFY first, ~15 subcategories, ~$0–$15K tool spend.
  - Mid-market (50–1,000 FTE, 2–5 IT/security): tier-3 target, full 108, ~$50K–$200K tool spend.
  - Large enterprise (1,000+ FTE, full security team): tier-3-to-4 target, custom Community Profile, $500K+.
  - **Cost-aware prioritization** by Function and subcategory.
  - First-profile-in-1-day pattern (mirrors the SOX-633 GTM post pattern).
- **Cross-references** —
  - To 800-53 RMF: for regulated orgs, the CSF Current Profile can be derived from existing 800-53 SSPs; this is the path of least resistance.
  - To isaca: COBIT 2019 design factors inform the 90-day prioritization.

### 2.8 Chunk 08 — `08-informative-references-crosswalk.md`

- **Frontmatter** — `chunk_id: 08-informative-references-crosswalk`, `parent_skill: nist-csf-2`, `topic: "Informative references: CSF ↔ NIST 800-53, ISO 27001:2022, COBIT 2019, CIS Controls v8, NIST SP 800-171 R3, HIPAA Security Rule, SOC 2 TSC 2017, PCI DSS v4.0"`, `load_when: "user asks 'CSF ↔ 800-53', 'CSF crosswalk', 'map CSF to ISO', 'CSF ↔ SOC 2', 'CSF ↔ HIPAA', 'CSF ↔ PCI', 'CSF ↔ COBIT'"`.
- **Trigger phrases** — "crosswalk", "mapping", "informative references", "CSF to 800-53", "CSF to ISO 27001", "CSF to SOC 2", "CSF to HIPAA", "CSF to PCI", "CSF to COBIT", "CSF to CIS", "CSF to 800-171".
- **Body** —
  - The CSF 2.0 informative-references concept: NIST publishes a mapping spreadsheet; we ship a curated version in `data/crosswalks/`.
  - **Per-target-framework** summary: how each one uses CSF (outcome vs control lens), what's covered, what isn't.
  - **CSF → 800-53** deep dive: which Subcategories map to which Control families; the GOVERN function maps mostly to 800-53 PM, CA, RA; IDENTIFY → PM, ID.RA, ID.AM; PROTECT → AC, AT, IA, MP, PE, PL, PS, PT, SC, SI; DETECT → AU, CA, CM, SI; RESPOND → IR, AU, CM, RA, SC; RECOVER → CP, IR.
  - **CSF → SOC 2** summary: 108 subcategories vs 9 Common Criteria + ~64 Points of Focus; the mapping is outcome-to-criterion, not 1:1.
  - **Anti-hallucination note**: "always verify against the NIST-published informative-references spreadsheet; the curated version in `data/crosswalks/` is a starting point".
- **Cross-references** —
  - To 800-53 RMF: this chunk **reverses** the crosswalk in `nist-800-53-rmf/chunks/09-crosswalk.md` (which goes 800-53 → CSF). Both directions are valid and both ships.
  - To all other skills: each skill's primary framework gets a CSF crosswalk entry here.

### 2.9 Why 8 chunks (not 7 or 9)

- 7 chunks was tempting (collapse 04 into 03, or 06 into 05), but the **GOVERN chunk** is the most-reviewed chunk in any CSF 2.0 build and deserves its own file. Collapsing it into a "tiers & profiles" file would force the reviewer to scroll past GOVERN to find the next tier content, which is exactly the executive-legibility problem we're trying to solve.
- 9 chunks was tempting (add `08-questionnaire-reuse` like 800-53 RMF) but CSF 2.0 is **already** questionnaire-friendly: the 108-subcategory grid is the questionnaire. There is no separate "CAIQ-for-CSF" pattern; the framework itself is the questionnaire. A 9th chunk would be filler.
- The GOVERN function deserves its own file because: (a) it's the new function in 2.0 and the most-likely-misrepresented content; (b) the executive-legibility promise requires GOVERN to be reachable in 1 click; (c) every review lens (5-lens, 5-practitioner) will focus on it and we want a focused review surface.

---

## 3. Industry angles (4 industries)

The 800-53 RMF skill ships 4 industry files; CSF 2.0 will ship 4 industry files. We follow the same 4-quadrant pattern (Posture, Boundary, Regulator/customer, Top use cases, Pain points, References) and the same `_index.md` table.

For CSF 2.0 the 4 industries are: **financial-services**, **public-sector**, **saas-technology**, **manufacturing**. Rationale:

- **financial-services** — the natural CSF 2.0 adopter; the FFIEC already endorses CSF; SOX + GLBA + NY DFS 500 + PCI make it the most multi-framework-overlap industry.
- **public-sector** — federal/state RMF variants (CA SAM, TX DIR, TX-RAMP) explicitly map to CSF; the StateRAMP and FedRAMP authorization conversations often start with CSF maturity language.
- **saas-technology** — small-to-mid SaaS startups use CSF 2.0 as the entry-level framework before they ever see a SOC 2; the "first profile in 1 day" pattern is the GTM hook.
- **manufacturing** — the IRS 1075, CJIS, NERC CIP, and OT (operational technology) variants make manufacturing a distinctive industry view; OT/IT convergence is the unique CSF 2.0 angle.

Healthcare is **deliberately deferred** to v0.3.x. Reason: healthcare has its own strong identity in the existing 800-53 RMF skill (`industries/healthcare.md`), and a one-skill-one-industry approach would dilute the executive-legibility promise. If we ship healthcare as a 5th industry, it can be added in v0.3.x without breaking the contract.

### 3.1 `industries/financial-services.md`

- **Most-relevant Functions** — **GOVERN** (board-level cyber risk committee is a hot topic; NY DFS 500 §500.04 mandates a CISO reporting to the board); **IDENTIFY** (FFIEC CAT inventory; CDFIPS); **PROTECT** (PCI DSS, GLBA Safeguards); **DETECT** (FFIEC CAT D-tier controls; SOX-relevant change monitoring); **RESPOND/RECOVER** (FFIEC BCP/DR handbook; SOX-relevant).
- **Real-world example** — A mid-size commercial bank (~$20B assets) builds a CSF Current Profile to satisfy the NY DFS 500 §500.02 cybersecurity program requirement, then publishes a Target Profile to the board, then uses the gap analysis to justify a $4M investment in IAM modernization and SIEM replacement over 18 months.
- **What this view ADDS** — the industry view **elevates** GV.OV (Oversight) and GV.MT (Monitoring) because board reporting cadence is the executive-legibility test; it **de-emphasizes** PR.PT (protective technology) and PR.PS (platform security) because those are technical-implementation details that don't move the board conversation.
- **Cross-references** —
  - **External frameworks** referenced: FFIEC CAT, NY DFS 500.02/500.04/500.16, SOX 404, GLBA Safeguards Rule, PCI DSS v4.0.
  - **Skills** cross-referenced: `coso-internal-controls` (for SOX 404 maturity), `aicpa-soc-reporting` (for SOC 1/2 evidence reuse), `nist-800-53-rmf` (for the 800-53 moderate overlay that often sits behind the CSF profile).

### 3.2 `industries/public-sector.md`

- **Most-relevant Functions** — all 6, but **GOVERN** is the most-distinctive in public-sector because FISMA + OMB A-130 + agency-head-level accountability put GOVERN at the top. **IDENTIFY** (asset + system inventory under FISMA); **PROTECT** (800-53 controls apply); **DETECT** (ConMon); **RESPOND/RECOVER** (FISMA incident reporting + COOP).
- **Real-world example** — A state agency (e.g., a Department of Revenue) uses CSF 2.0 to build a **Community Profile**-aligned organizational profile, then maps the Current Profile to the state-specific 800-53 overlay (CA SAM, TX DIR SCSC, or TX-RAMP depending on state) so the same artifact satisfies both the state regulator and the federal funding source.
- **What this view ADDS** — the industry view emphasizes the **Community Profile → Organizational Profile** workflow, and the state-RMF-variant crosswalk. It de-emphasizes the small-business CSF 2.0 quick-start guide (NIST SP 1299) because state agencies are not small businesses.
- **Cross-references** —
  - **External**: FISMA, OMB A-130, OMB M-22-15, NIST SP 800-37 Rev 2 RMF, FedRAMP Rev 5, state-specific (CA SAM, TX DIR SCSC, TX-RAMP, StateRAMP), CISA Cyber Performance Goals (CPG).
  - **Skills**: `nist-800-53-rmf` (the FIPS 199 categorization is upstream of the CSF profile; 800-53A assessment is one of two evidence sources for the CSF profile).

### 3.3 `industries/saas-technology.md`

- **Most-relevant Functions** — **IDENTIFY** (SaaS asset inventory; multi-tenant data classification); **PROTECT** (the SDLC, IAM, encryption); **DETECT** (SIEM, anomaly detection, customer-facing audit log); **GOVERN** (lightweight for early-stage; deepens at growth).
- **Real-world example** — A 30-person Series-A SaaS startup with 2 engineers and no dedicated security hire builds a Current Profile in 1 day, identifies a Tier 2 target with 9 subcategory gaps, uses the gap to justify a $30K–$80K tool spend (MFA, endpoint, SIEM-lite, backup), and presents the Target Profile to the board in the next quarterly update. The same profile is then handed to a customer security questionnaire (CAIQ/SIG-lite) reviewer.
- **What this view ADDS** — the **first-profile-in-1-day pattern**, the **cost-aware prioritization** (chunk 07), and the **questionnaire reuse** (a CSF profile + CAIQ is the SaaS-questionnaire shortcut). It de-emphasizes the formal FedRAMP path (which is in 800-53 RMF and the future FedRAMP skill) and the 5-part finding severity structure (which is for 800-53A, not CSF).
- **Cross-references** —
  - **External**: SOC 2 (most SaaS do SOC 2 first, then layer CSF on top), CAIQ v4, SIG Lite, VSAQ, ISO 27001 (often the third framework a SaaS adopts).
  - **Skills**: `aicpa-soc-reporting` (SOC 2 Type II is the natural precursor), `nist-800-53-rmf/chunks/08-questionnaire-reuse.md` (the questionnaire reuse pattern), `audit-workpapers` (when the SaaS also produces audit evidence for customer-facing).

### 3.4 `industries/manufacturing.md`

- **Most-relevant Functions** — **IDENTIFY** (OT + IT asset inventory is the most distinctive challenge); **PROTECT** (network segmentation IT/OT, ICS/SCADA security); **DETECT** (ICS anomaly detection, often air-gapped or limited); **GOVERN** (OT governance is a board-level topic because safety and production are at stake).
- **Real-world example** — A mid-market discrete manufacturer (~$500M revenue) uses CSF 2.0 to build a profile that covers both IT (ERP, email, file shares) and OT (plant-floor PLCs, MES, SCADA), with a specific cross-reference to the **CISA Cross-Sector Industrial Control Systems Cybersecurity Performance Goals (ICS CPGs)**. The Current/Target gap is published to the COO (not just the CISO) because production safety is a board-level concern.
- **What this view ADDS** — the **OT/IT convergence** angle, the **CISA ICS CPG** crosswalk, and the **safety/availability priority** for the RECOVER function. It de-emphasizes the privacy-heavy GV.PO/PT subcategories that are central in healthcare.
- **Cross-references** —
  - **External**: CISA ICS CPG, NIST SP 800-82 Rev 3 (Industrial Control Systems Security), NERC CIP (if electric utility), ISA/IEC 62443 (industrial automation), ISO 27001 Annex A 11 (physical and environmental).
  - **Skills**: `nist-800-53-rmf` (the 800-53 SC family covers much of the OT/IT boundary), `isaca-audit-methodology` (COBIT 2019's DSS05 (Manage Security Services) maps to OT operations).

### 3.5 The `industries/_index.md` table

The `_index.md` table mirrors the 800-53 RMF format:

| Industry | File | Top use cases | Notes |
|----------|------|---------------|-------|
| Commercial financial services | financial-services.md | UC-02 (board report) | NY DFS 500, FFIEC CAT, SOX 404, GLBA; CSF as the board-facing framework |
| Public sector (state/federal) | public-sector.md | UC-03 (Current/Target → 800-53) | FISMA + state RMF variants; Community Profile → Organizational Profile pattern |
| SaaS / cloud-native technology | saas-technology.md | UC-01 (first profile) | Series A → Series D journey; SOC 2 → CSF overlay; 1-day first profile |
| Manufacturing (OT/IT) | manufacturing.md | UC-04 (planned, v0.3.x) | CISA ICS CPG, NIST 800-82, safety-availability priority |

The `_index.md` is **fully populated** at v0.1.0 with the 4 industries above. UC-04 (manufacturing) is a stretch UC and may be deferred to v0.3.x; the 800-53 RMF skill ships 3 industries + 1 planned UC; we follow the same shape.

---

## 4. Use cases (3 worked examples, with input/procedure/oracle shape)

The 3 UCs cover the three patterns specified in the brief:

- **UC-01 — first profile pattern** (Tier 1→3 journey, GOVERN gap)
- **UC-02 — board report pattern** (executive-legible, 6-function radar)
- **UC-03 — Current/Target gap mapped to 800-53** (cross-framework)

All three use the standard UC frontmatter contract from `tests/test_consistency_lib.py`: `uc_id`, `title`, `industries`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`.

### 4.1 UC-01 — First CSF Profile for a Series-A SaaS (first-profile pattern)

**Frontmatter:**

```yaml
uc_id: UC-01
title: "Series-A SaaS builds first CSF Current Profile (Tier 1→2.5 target, GOVERN gap, 9-subcategory roadmap)"
industries: [saas-technology]
frameworks: [NIST-CSF-2.0, SOC-2-TSC-2017]
inputs:
  org_name: "FlowMetrics Inc."
  system_description: |
    30-FTE Series-A B2B SaaS for marketing analytics. Processes B2B contact
    data (names, work emails, company names) — PII at moderate volume (~50k
    records). Hosted on AWS commercial (not GovCloud). SOC 2 Type I in
    progress. No dedicated security hire; security is 1 of 2 engineer's
    responsibility at ~25% time.
  ...
procedure:
  - "chunks/01-functions-categories.md — Confirm the 6 Functions and 22 Categories."
  - "chunks/02-tiers-and-profiles.md — Select current Tier (1.5) and target Tier (2.5)."
  - "chunks/05-govern-function.md — Assess GOVERN first; document the GV.OC-01 (mission) and GV.SR-01 (roles) gaps."
  - "chunks/03-current-profile.md — Score each of the 108 Subcategories; ~30% Not Implemented, ~50% Partially, ~20% Fully."
  - "chunks/04-target-profile-and-gap.md — Build the Target Profile; compute the gap; produce the 9-item 90-day roadmap."
  - "chunks/06-enterprise-reporting.md — Produce the 1-page board update."
expected_outputs:
  current_profile:
    functions:
      GOVERN: {current_tier: 1, subcategory_count: 19, fully_implemented_pct: 5}
      IDENTIFY: {current_tier: 2, subcategory_count: 9, fully_implemented_pct: 35}
      ...
  target_profile:
    target_tier: 2.5
    gap_count: 9
    top_3_gaps: ["GV.OC-01", "GV.SR-01", "PR.AA-01"]
  roadmap:
    duration: "90 days"
    items: 9
    estimated_cost: "$30K-$80K tool spend"
oracle:
  type: schema_match
  assertion: |
    - functions.GOVERN.current_tier == 1
    - target_profile.gap_count == 9
    - top_3_gaps contains "GV.OC-01", "GV.SR-01", "PR.AA-01"
    - roadmap.items == 9 and roadmap.duration == "90 days"
data_refs:
  - "data/seeds/uc-01-input.json"
  - "data/seeds/uc-01-subcategory-scores.json"
  - "data/seeds/uc-01-roadmap.json"
  - "data/seeds/uc-01-expected.json"
tests:
  - "tests/test_oracle.py::test_uc_01"
  - "tests/test_trace.py::test_uc_01_trace"
  - "tests/test_adversarial.py::test_uc_01_tier1_bootstrap"
status: active
```

**Real-world scenario** — FlowMetrics Inc. has just closed a Series A and is selling to mid-market customers who ask for SOC 2 and a security overview. The CTO wants a "minimum-viable" security framework to present to the board and to enterprise customers without hiring a CISO. The CSF 2.0 "first profile" is the lowest-cost, fastest-to-board answer.

**Input JSON shape** (`data/seeds/uc-01-input.json`):

```json
{
  "org_name": "FlowMetrics Inc.",
  "fte_count": 30,
  "security_fte_fraction": 0.25,
  "hosting": "AWS commercial, us-east-1, us-west-2",
  "pii_volume": "~50k B2B contacts",
  "existing_attestations": ["SOC 2 Type I in progress"],
  "current_tier_self_assessment": {
    "GOVERN": 1, "IDENTIFY": 2, "PROTECT": 2, "DETECT": 1, "RESPOND": 2, "RECOVER": 1
  },
  "target_tier": 2.5,
  "roadmap_window_days": 90
}
```

**Procedure (summary)** — 6 steps from the frontmatter. Each step cites a real chunk file (verifiable by the consistency library).

**Expected output** (`data/seeds/uc-01-expected.json`):

```json
{
  "current_profile": {
    "functions": {
      "GOVERN":   {"current_tier": 1, "fully_implemented_pct": 5,  "partially_implemented_pct": 25, "not_implemented_pct": 70},
      "IDENTIFY": {"current_tier": 2, "fully_implemented_pct": 35, "partially_implemented_pct": 45, "not_implemented_pct": 20},
      "PROTECT":  {"current_tier": 2, "fully_implemented_pct": 40, "partially_implemented_pct": 40, "not_implemented_pct": 20},
      "DETECT":   {"current_tier": 1, "fully_implemented_pct": 20, "partially_implemented_pct": 30, "not_implemented_pct": 50},
      "RESPOND":  {"current_tier": 2, "fully_implemented_pct": 30, "partially_implemented_pct": 30, "not_implemented_pct": 40},
      "RECOVER":  {"current_tier": 1, "fully_implemented_pct": 10, "partially_implemented_pct": 30, "not_implemented_pct": 60}
    }
  },
  "target_profile": {
    "target_tier": 2.5,
    "gap_count": 9,
    "top_3_gaps": ["GV.OC-01", "GV.SR-01", "PR.AA-01"]
  },
  "roadmap": {
    "duration_days": 90,
    "items": 9,
    "estimated_cost_usd_low": 30000,
    "estimated_cost_usd_high": 80000
  }
}
```

**Oracle** — assertions are explicit per the frontmatter; the test reads `uc-01-expected.json` and asserts.

### 4.2 UC-02 — Board Maturity Report for a Mid-Size Bank (board-report pattern)

**Frontmatter:**

```yaml
uc_id: UC-02
title: "Mid-size commercial bank produces board CSF maturity report (6-function radar, GV.RM+DE.CM lagging, 12-month $4M plan)"
industries: [financial-services]
frameworks: [NIST-CSF-2.0, NY-DFS-500, FFIEC-CAT, GLBA-Safeguards]
inputs:
  institution_name: "FirstAtlantic Bank"
  institution_type: "state-chartered commercial bank, ~$20B assets"
  regulator_relationship: "OCC, FDIC, NY DFS"
  ffte: 1200
  cyber_fte: 6
  existing_attestations: ["SOC 1 Type II", "SOC 2 Type II", "GLBA annual assessment"]
inputs_extra:
  cyber_budget_prior_year: "$3.2M"
  cyber_budget_current_year: "$3.5M"
  board_cyber_committee: true
  cyber_committee_meets_quarterly: true
procedure:
  - "chunks/06-enterprise-reporting.md — Build the 6-function radar from the Current Profile."
  - "chunks/05-govern-function.md — Produce the GOVERN function deep-dive (3-page board appendix)."
  - "chunks/04-target-profile-and-gap.md — Compute the gap; prioritize the 12-month investment."
  - "chunks/06-enterprise-reporting.md §Board deck template — Produce the 12-slide board deck."
  - "chunks/02-tiers-and-profiles.md §Tiers — Note the Tier 3 (Repeatable) target across all 6 Functions."
expected_outputs:
  radar:
    GOVERN: 2.5
    IDENTIFY: 3.0
    PROTECT: 3.5
    DETECT: 2.0
    RESPOND: 3.0
    RECOVER: 3.0
  lagging_functions: ["GOVERN", "DETECT"]
  twelve_month_plan:
    total: "$4.0M"
    items: 6
    iam_modernization: "$1.5M"
    siem_replacement: "$1.2M"
    governance_oversight_tooling: "$0.5M"
    detection_engineering: "$0.4M"
    third_party_risk_enhancement: "$0.3M"
    incident_response_exercises: "$0.1M"
  board_deck_pages: 12
oracle:
  type: schema_match
  assertion: |
    - radar.GOVERN in [2.0, 3.0]
    - radar.DETECT in [1.5, 2.5]
    - lagging_functions contains "GOVERN" and "DETECT"
    - twelve_month_plan.total == "$4.0M" (or numeric equivalent)
    - twelve_month_plan.items == 6
    - board_deck_pages == 12
data_refs:
  - "data/seeds/uc-02-input.json"
  - "data/seeds/uc-02-radar.json"
  - "data/seeds/uc-02-plan.json"
  - "data/seeds/uc-02-expected.json"
tests:
  - "tests/test_oracle.py::test_uc_02"
  - "tests/test_trace.py::test_uc_02_trace"
  - "tests/test_adversarial.py::test_uc_02_nydfs_escalation"
status: active
```

**Real-world scenario** — FirstAtlantic Bank's Chief Information Security Officer (CISO) must produce a quarterly cyber maturity report to the board's Risk Committee. The current SOC 2 + GLBA evidence is sufficient for "did we pass an audit", but the board wants a forward-looking maturity view. CSF 2.0 is the board-facing framework; the SOC 2 is the audit-facing one.

**Input JSON shape** (`data/seeds/uc-02-input.json`):

```json
{
  "institution_name": "FirstAtlantic Bank",
  "institution_type": "state-chartered commercial bank, ~$20B assets",
  "regulator_relationship": ["OCC", "FDIC", "NY DFS"],
  "ffte": 1200,
  "cyber_fte": 6,
  "existing_attestations": ["SOC 1 Type II", "SOC 2 Type II", "GLBA annual assessment"],
  "cyber_budget_prior_year_usd": 3200000,
  "cyber_budget_current_year_usd": 3500000,
  "board_cyber_committee": true,
  "cyber_committee_meets_quarterly": true,
  "current_tier_by_function": {
    "GOVERN": 2.5, "IDENTIFY": 3.0, "PROTECT": 3.5,
    "DETECT": 2.0, "RESPOND": 3.0, "RECOVER": 3.0
  },
  "target_tier": 3.0
}
```

**Procedure (summary)** — 5 steps; the board deck is the final artifact.

**Expected output** (`data/seeds/uc-02-expected.json`):

```json
{
  "radar": {
    "GOVERN": 2.5, "IDENTIFY": 3.0, "PROTECT": 3.5,
    "DETECT": 2.0, "RESPOND": 3.0, "RECOVER": 3.0
  },
  "lagging_functions": ["GOVERN", "DETECT"],
  "twelve_month_plan": {
    "total_usd": 4000000,
    "items": 6,
    "iam_modernization_usd": 1500000,
    "siem_replacement_usd": 1200000,
    "governance_oversight_tooling_usd": 500000,
    "detection_engineering_usd": 400000,
    "third_party_risk_enhancement_usd": 300000,
    "incident_response_exercises_usd": 100000
  },
  "board_deck_pages": 12
}
```

**Oracle** — assertions from the frontmatter; the test asserts against the expected fixture.

### 4.3 UC-03 — Mid-Market Manufacturer, Current/Target Gap Mapped to 800-53 (cross-framework pattern)

**Frontmatter:**

```yaml
uc_id: UC-03
title: "Mid-market manufacturer maps 14 lagging CSF subcategories to NIST 800-53 Moderate controls for federal customer"
industries: [manufacturing, public-sector]
frameworks: [NIST-CSF-2.0, NIST-SP-800-53-Rev5, CISA-ICS-CPG]
inputs:
  org_name: "PrecisionFab Manufacturing"
  revenue: "$500M"
  ffte: 1800
  it_ot_split: "IT 200 FTE, OT 150 FTE"
  customer_federal: "Department of Defense (DoD) — DIB CSIP award pending"
  it_baseline: "SOC 2 Type II"
  ot_governance: "CISA ICS CPG self-assessment complete"
procedure:
  - "chunks/03-current-profile.md — Build the Current Profile across all 108 Subcategories."
  - "chunks/04-target-profile-and-gap.md — Build the Target Profile at Tier 3 across all 6 Functions; compute the gap."
  - "chunks/08-informative-references-crosswalk.md — Map the 14 lagging Subcategories to NIST 800-53 Moderate controls using the curated crosswalk in data/crosswalks/csf-to-800-53-mod.json."
  - "chunks/08-informative-references-crosswalk.md §CSF → 800-53 — Produce the 14-item remediation table with 800-53 control IDs."
  - "chunks/04-target-profile-and-gap.md — Produce the 12-month DoD-customer-ready roadmap."
expected_outputs:
  current_profile: {tier_avg: 2.0, lagging_subcategory_count: 14}
  target_profile: {tier_avg: 3.0, gap_count: 14}
  crosswalk:
    lagging_subcategories: 14
    csf_to_800_53: "data/crosswalks/csf-to-800-53-mod.json"
    representative_mappings:
      - {csf: "GV.OC-01", nist_800_53: ["PM-11", "PM-15"]}
      - {csf: "GV.SC-01", nist_800_53: ["SR-1", "SR-3"]}
      - {csf: "DE.CM-09", nist_800_53: ["SI-4", "SI-4(2)"]}
  roadmap:
    duration_months: 12
    items: 14
oracle:
  type: schema_match
  assertion: |
    - current_profile.lagging_subcategory_count == 14
    - target_profile.gap_count == 14
    - crosswalk.representative_mappings contains GV.OC-01, GV.SC-01, DE.CM-09
    - roadmap.items == 14
    - roadmap.duration_months == 12
data_refs:
  - "data/seeds/uc-03-input.json"
  - "data/crosswalks/csf-to-800-53-mod.json"
  - "data/seeds/uc-03-lagging-subcategories.json"
  - "data/seeds/uc-03-expected.json"
tests:
  - "tests/test_oracle.py::test_uc_03"
  - "tests/test_trace.py::test_uc_03_trace"
  - "tests/test_adversarial.py::test_uc_03_ot_it_split"
status: active
```

**Real-world scenario** — PrecisionFab has a DoD Defense Industrial Base (DIB) Cybersecurity Improvement Plan (CSIP) award pending, which requires NIST 800-53 alignment. They have a Current Profile in CSF 2.0 and need to translate the 14 lagging subcategories into 800-53 Moderate controls so the same evidence base satisfies both the DoD customer and the manufacturing CSF profile.

**Input JSON shape** (`data/seeds/uc-03-input.json`):

```json
{
  "org_name": "PrecisionFab Manufacturing",
  "revenue_usd": 500000000,
  "ffte": 1800,
  "it_ot_split": {"it": 200, "ot": 150},
  "customer_federal": "DoD DIB CSIP award pending",
  "it_baseline": "SOC 2 Type II",
  "ot_governance": "CISA ICS CPG self-assessment complete",
  "current_tier_avg": 2.0,
  "target_tier_avg": 3.0
}
```

**Procedure (summary)** — 5 steps; the crosswalk is the unique deliverable.

**Expected output** (`data/seeds/uc-03-expected.json`):

```json
{
  "current_profile": {"tier_avg": 2.0, "lagging_subcategory_count": 14},
  "target_profile": {"tier_avg": 3.0, "gap_count": 14},
  "crosswalk": {
    "lagging_subcategories": 14,
    "csf_to_800_53_path": "data/crosswalks/csf-to-800-53-mod.json",
    "representative_mappings": [
      {"csf": "GV.OC-01", "nist_800_53": ["PM-11", "PM-15"]},
      {"csf": "GV.SC-01", "nist_800_53": ["SR-1", "SR-3"]},
      {"csf": "DE.CM-09", "nist_800_53": ["SI-4", "SI-4(2)"]}
    ]
  },
  "roadmap": {"duration_months": 12, "items": 14}
}
```

**Oracle** — assertions from the frontmatter.

### 4.4 UC selection rationale (why these 3)

- **UC-01 (first profile)** — covers the most-shareable GTM artifact (the Wk 5 LI post will be a derivative of this); exercises the GOVERN chunk and the 1-day cost-aware pattern.
- **UC-02 (board report)** — exercises the **executive-legibility promise** end-to-end; this is the UC that proves the `BOTH` persona claim.
- **UC-03 (cross-framework)** — exercises the crosswalk to 800-53 (the SOX-566 dependency) and the manufacturing industry view; the gap is the natural "next 12 months" input to a federal customer.

A **4th UC** (community profile authoring for healthcare) is on the v0.3.x roadmap; v0.1.0 ships 3 to match the 800-53 RMF skill's shape.

---

## 5. Test architecture (9 test files, target 30+ tests)

The 800-53 RMF skill has 9 test files: `test_<skill>_lint.py`, `_oracle.py`, `_grounding.py`, `_trace.py`, `_metamorphic.py`, `_adversarial.py`, `_telemetry.py`, `_consistency.py`, plus `nist_800_53_rmf_stub.py`. CSF 2.0 will mirror exactly. Test count target: **30+** (the 800-53 RMF skill ships 29; we aim 32 to account for the GOVERN function's distinctive review surface).

### 5.1 `test_nist_csf_2_lint.py`

- 1 test: `test_lint_passes` — runs `tools/lint_skill.py skills/nist-csf-2`; asserts returncode 0.
- 1 test: `test_lint_passes_quiet` — runs the linter with `--quiet` flag; verifies only failures are reported.
- 1 test: `test_linter_finds_no_todo_outside_changelog` — linter surfaces TODO/FIXME; we verify the count is 0.
- **Total: 3 tests.**

### 5.2 `test_nist_csf_2_oracle.py`

- 1 test: `test_uc_01_oracle` — UC-01 assertions: GOVERN current_tier = 1, gap_count = 9, top_3_gaps contains `["GV.OC-01", "GV.SR-01", "PR.AA-01"]`, roadmap.duration = 90 days.
- 1 test: `test_uc_02_oracle` — UC-02 assertions: radar.GOVERN in [2.0, 3.0], radar.DETECT in [1.5, 2.5], lagging_functions = ["GOVERN", "DETECT"], twelve_month_plan.total = $4.0M, items = 6, board_deck_pages = 12.
- 1 test: `test_uc_03_oracle` — UC-03 assertions: lagging_subcategory_count = 14, target gap_count = 14, crosswalk contains GV.OC-01, GV.SC-01, DE.CM-09 with non-empty 800-53 control IDs.
- 1 test: `test_uc_01_govern_tier_1_5` — parametrized metamorphic-style: assert GOVERN tier ≤ IDENTIFY tier ≤ PROTECT tier (heuristic: GOVERN matures last).
- 1 test: `test_uc_02_radar_function_count` — assert radar has exactly 6 functions.
- 1 test: `test_uc_03_lagging_count_in_range` — assert lagging_subcategory_count in [10, 25] (industry-typical for a Tier-2-to-3 mid-market manufacturer).
- **Total: 6 tests.**

### 5.3 `test_nist_csf_2_grounding.py`

- 1 test: `test_in_body_citations_resolve_to_manifest` — same shape as 800-53 RMF test.
- 1 test: `test_manifest_has_required_fields` — manifest has Title, Publisher, Identifier, Retrieval, URL.
- 1 test: `test_no_hallucinated_paragraph_numbers` — no "paragraph 47" or "page 13" without citation.
- 1 test: `test_csf_2_0_label_in_manifest` — the citation `[NIST-CSF-2.0 §X.Y]` resolves to a manifest entry that has "Cybersecurity Framework 2.0" in the title and "2.0" in the identifier.
- **Total: 4 tests.**

### 5.4 `test_nist_csf_2_trace.py`

- 1 test: `test_skill_md_referenced_sections_exist` — every section number in `EXPECTED_SECTIONS` dict appears in SKILL.md or chunks.
- 1 test: `test_use_cases_cite_skill_sections` — each UC's `procedure` field in frontmatter cites a real chunk file (`chunks/01-functions-categories.md`, etc.) or a SKILL.md section.
- 1 test: `test_chunk_cite_industry_or_uc` — every chunk cites a related industry file or use case (matches the `isaca-audit-methodology` chunk pattern).
- **Total: 3 tests.**

### 5.5 `test_nist_csf_2_metamorphic.py`

- 1 test: `test_uc_01_target_tier_change` — bumping target_tier from 2.5 to 3.0 increases gap_count by ≥ 3.
- 1 test: `test_uc_01_fte_change` — reducing FTE from 30 to 10 increases GOVERN gap; Tier 1 stays at Tier 1.
- 1 test: `test_uc_02_budget_change` — increasing the 12-month plan from $4M to $8M allows 2 more items in the roadmap; no item disappears.
- 1 test: `test_uc_03_federal_customer_removal` — if the federal customer constraint is removed, the crosswalk may shrink to ~5 lagging subcategories (DoD-specific gaps disappear).
- **Total: 4 tests.**

### 5.6 `test_nist_csf_2_adversarial.py`

- 1 test: `test_uc_01_tier1_bootstrap` — V1: org is at Tier 1 across all functions; assert roadmap items includes the basics (MFA, backups, basic IR plan).
- 1 test: `test_uc_02_nydfs_escalation` — V2: a NY DFS Part 500 enforcement action is added; assert the radar reports 1.5 for GOVERN and the plan includes the §500.04 board reporting remediation.
- 1 test: `test_uc_03_ot_it_split` — V3: org has 200 IT FTE and 150 OT FTE; the crosswalk must include both 800-53 IT controls (AC, IA) and 800-82 OT controls (SC-7, PE, physical segmentation).
- 1 test: `test_uc_01_no_evidence_refs` — V4: subcategory has status "Fully Implemented" but no evidence_refs; assert the skill flags this as a self-attestation risk.
- 1 test: `test_uc_02_contradictory_tiers` — V5: current tier is 4 (Adaptive) but no board committee exists; assert skill flags the contradiction.
- **Total: 5 tests.**

### 5.7 `test_nist_csf_2_telemetry.py`

- 1 test: `test_schema_is_valid_json` — schema is valid JSON Schema (Draft 7).
- 1 test: `test_schema_required_fields` — schema requires all 14 Spine-mandated fields.
- 1 test: `test_skill_name_pattern` — `skill == "nist-csf-2"` validates; `"nist csf 2"` fails.
- 1 test: `test_use_case_id_pattern` — `use_case_id == "UC-01"` validates; `"uc-1"` fails.
- 1 test: `test_industry_enum` — industries are from the registered enum.
- 1 test: `test_oracle_result_enum` — `oracle_result` ∈ {pass, fail, skipped, n/a}.
- 1 test: `test_instrument_emits_event` — the instrumentation stub actually emits a `SkillInvocation` event when the stub function is called.
- **Total: 7 tests.**

### 5.8 `test_nist_csf_2_consistency.py`

Wraps `tests/test_consistency_lib.py` (6 tests, same as 800-53 RMF):

- `test_routing_table_bidirectional`
- `test_chunk_frontmatter_schema`
- `test_manifest_bidirectional`
- `test_cross_skill_references_resolve`
- `test_industry_index_sync`
- `test_use_case_index_sync`
- **Total: 6 tests.**

### 5.9 `nist_csf_2_stub.py`

The skill entrypoint stub. Mirrors `nist_800_53_rmf_stub.py`. Functions:

- `_categorize_by_function(subcategory_scores)` — compute current_tier per Function from a 108-row subcategory score list.
- `_compute_gap(current_profile, target_profile)` — list of lagging subcategories.
- `_uc01_first_profile(payload)` — score → current_tier, gap_count, top_3.
- `_uc02_board_radar(payload)` — radar + 12-month plan.
- `_uc03_csf_to_800_53(payload, crosswalk)` — lagging_subcategories + 800-53 mapping.
- `run_skill(use_case_id, payload, model="stub")` — entrypoint.
- `normalize_citations(text)` — extract `[LABEL §X]` citations from body.

### 5.10 Test count summary

| File | Test count | Notes |
|------|-----------|-------|
| `test_nist_csf_2_lint.py` | 3 | |
| `test_nist_csf_2_oracle.py` | 6 | |
| `test_nist_csf_2_grounding.py` | 4 | |
| `test_nist_csf_2_trace.py` | 3 | |
| `test_nist_csf_2_metamorphic.py` | 4 | |
| `test_nist_csf_2_adversarial.py` | 5 | |
| `test_nist_csf_2_telemetry.py` | 7 | |
| `test_nist_csf_2_consistency.py` | 6 | wraps lib |
| **Total** | **38** | target met (30+) |

If we drop a few of the less-distinct tests, the floor is 30. If we add the GOVERN-specific test (see §5.11 below) and a 9th test file (e.g., `test_nist_csf_2_chunk_09.py` for the new chunk 09 if we add one in v0.3.x), we go higher.

### 5.11 (Stretch) GOVERN-function-specific test

To honor the brief's "1-2 tests for the new chunk 09" — we don't have a chunk 09 in v0.1.0, so this maps to a GOVERN-specific test in the oracle file:

- 1 test: `test_govern_categories_complete` — all 7 GOVERN categories (GV.OC, GV.RM, GV.SC, GV.SR, GV.PO, GV.OV, GV.MT) appear in the chunk 05 frontmatter; the chunk mentions each by name.
- 1 test: `test_govern_elevated_to_first_function` — in `chunks/03-current-profile.md` the GOVERN function is assessed **first** (chunks cite GOVERN first in the procedure or section ordering).

This adds 2 tests to the oracle file for a total of 40 if we keep all the others.

---

## 6. PoV analyses — 5 lenses (mirroring the 800-53 RMF 5-lens review)

For each lens, what the reviewer will focus on for CSF 2.0, and what we pre-empt.

### 6.1 Lens 1 — Framework Fidelity

**Focus:** Is the CSF 2.0 representation accurate? Did we get GOVERN right (the new function in 2.0)? Are subcategory references correct? Is "Current/Target Profile" terminology used consistently?

**What the reviewer will look for:**

- Every Function name uses CSF 2.0 spelling: **GOVERN** (not "Govern"), **IDENTIFY**, **PROTECT**, **DETECT**, **RESPOND**, **RECOVER**. No "Detect" or "Respond" lowercased.
- Every Category uses the CSF 2.0 prefix: **GV.OC**, **GV.RM**, **GV.SC**, **GV.SR**, **GV.PO**, **GV.OV**, **GV.MT** (7 GOVERN categories); **ID.AM**, **ID.RA**, **ID.RM**, **ID.SC** (4 IDENTIFY); **PR.AA**, **PR.AC**, **PR.DS**, **PR.PS**, **PR.IR**, **PR.PT** (6 PROTECT, renamed in 2.0); **DE.AE**, **DE.CM**, **DE.DP** (3 DETECT); **RS.RP**, **RS.CO**, **RS.AN**, **RS.MI**, **RS.IM** (5 RESPOND); **RC.RP**, **RC.IM**, **RC.CO**, **RC.RP** (4 RECOVER).
- Subcategory references use the format `GV.OC-01`, `GV.OC-02`, etc. — letter-number, not letter-letter.
- Profile terminology: "Current Profile", "Target Profile", "Organizational Profile", "Community Profile" — spelled out, not abbreviated, on first use.
- Tiers spelled "Tier 1" (Partial), "Tier 2" (Risk Informed), "Tier 3" (Repeatable), "Tier 4" (Adaptive). Numbers and names both appear on first use.
- Anti-hallucination note: 1.1-era categories (PR.DS, PR.IP, PR.AC, PR.AT, etc.) are **not** used; the 2.0 PROTECT rename (PR.AA Account Architecture, PR.AC Identity Management, PR.DS Data Security, PR.PS Platform Security, PR.IR Technology Infrastructure Resilience, PR.PT Protective Technology) is the only form.

**What we pre-empt:**

- A common reviewer finding would be: "you used GV.PO-01 for policy but in CSF 2.0 the subcategory is GV.PO-01 (Policy is established, communicated, and maintained) — confirm wording." We pre-empt by copying the official CSF 2.0 subcategory wording into the seed JSON and the chunk text.
- Another finding would be: "your UC-01 says 'PR.AA-01' but in 1.1 this was PR.AC-1." We pre-empt by adding a **2.0-vs-1.1 delta table** in chunk 01.

### 6.2 Lens 2 — Completeness

**Focus:** Do we cover all 6 Functions? All 22 Categories? All ~108 Subcategories? Are the GOVERN categories treated as first-class?

**What the reviewer will look for:**

- A complete Category table in chunk 01 (22 rows).
- A complete Subcategory reference (in `data/crosswalks/csf-2-0-subcategories.json`) with all 108 entries.
- Each Category in chunk 05 (GOVERN) gets a 1-paragraph description; no "(describe later)" or "see CSF 2.0 §X".
- The Tiers chunk (02) defines all 4 Tiers with their characteristic, process, organization-wide risk management, and external participation columns.
- The Profiles chunk (02) defines all 4 Profile types with at least one worked example each (Current, Target, Organizational, Community).
- Anti-hallucination: the implementation examples in the CSF 2.0 appendix are **not normative**; we cite them but do not reproduce them as if they were authoritative.

**What we pre-empt:**

- A common finding would be: "you only show 5 of 7 GOVERN categories in chunk 05; you're missing GV.PO and GV.MT." We pre-empt by structuring chunk 05 with one section per category (7 sections, each ~25-40 lines).
- Another finding would be: "your Tiers table is missing the 'External Participation' column." We pre-empt by including all 4 columns from the CSF 2.0 Tier table (Characteristic, Process, Org-wide Risk Management, External Participation).

### 6.3 Lens 3 — Usability

**Focus:** Can a non-NIST practitioner (auditor, GRC consultant) read this and act? Is the executive-legible angle preserved? Are the 4-quadrant industry views navigable?

**What the reviewer will look for:**

- The SKILL.md router is **readable in 90 seconds** by a non-NIST executive. The §2 Framework Overview has a 1-paragraph summary; the §3 Core Concepts has a 1-screen table.
- Each chunk has a **Decision logic** block (IF/THEN/ELSE) that an LLM agent can execute.
- Each chunk has an **Output template** that is paste-able (YAML or JSON).
- The 6-function radar is **reproducible** (Mermaid or ASCII-art) so the board-deck UC can be exercised without a chart library.
- The industry views are navigable: a financial-services user can read `industries/financial-services.md` and understand which Subcategories are elevated for them.
- The cross-skill references are not buried: every "see also" link is in the chunk or in §7 of SKILL.md.

**What we pre-empt:**

- A common finding would be: "the executive cannot find the 6-function radar; you have it buried in chunk 06." We pre-empt by including a small radar in the SKILL.md §3.1 (Core Concepts) that points to chunk 06 for the full version.
- Another finding would be: "chunk 04 (Target Profile) talks about prioritization but doesn't say **how** to prioritize." We pre-empt by including a prioritization heuristic in chunk 04 (e.g., "prioritize gaps where (a) the Subcategory is in the GOVERN function and (b) the gap moves the Function's tier by ≥ 1").

### 6.4 Lens 4 — Spine Convention Compliance

**Focus:** Is the router ≤ 300 lines? Are chunks ≤ 200 lines? Is `context_budget` declared? Are 3+ industries + 3+ UCs present? Does it pass `tools/lint_skill.py`?

**What the reviewer will look for:**

- SKILL.md is ≤ 300 lines. The 800-53 RMF router is 249 lines; we aim ≤ 280 lines for CSF 2.0 (the GOVERN function and 4-quadrant pattern add some content).
- Each chunk is ≤ 200 lines. Our chunk 05 (GOVERN) is the largest by design; we target ≤ 180 lines to leave room.
- `context_budget` is in the frontmatter with all 4 fields.
- 3+ industries, 3+ UCs.
- `tools/lint_skill.py skills/nist-csf-2` returns 0.
- 9 test files; 30+ tests pass; 0 TODO/FIXME outside changelog.
- `telemetry/schema.json` validates; `telemetry/instrument.py` is importable; `telemetry/redaction.md` is non-stub; `telemetry/baseline.md` is non-stub.

**What we pre-empt:**

- A common finding would be: "your SKILL.md is 287 lines; you don't need chunks/." We pre-empt by **explicitly noting** in the frontmatter that this skill uses the chunks pattern (the 8 chunks correspond to the 8 functions/outputs). The 287 lines are 1,500+ lines worth of detail when measured including chunks.
- Another finding would be: "your chunk 01 has 187 lines; the 108 subcategory table is too dense." We pre-empt by moving the full subcategory list to `data/crosswalks/csf-2-0-subcategories.json` and summarizing in chunk 01 (1 row per Category with a 1-line description).

### 6.5 Lens 5 — Cross-Skill Alignment

**Focus:** Are the cross-references to 800-53 RMF correct? Does it match the cross-skill conventions for severity tiers, risk formulas, finding format? Is the "5-part finding" pattern used consistently?

**What the reviewer will look for:**

- Cross-references to `nist-800-53-rmf/chunks/02-categorize.md`, `chunks/03-baseline.md`, `chunks/09-crosswalk.md` are **correct** (the file exists, the section is relevant).
- The CSF → 800-53 crosswalk in `data/crosswalks/csf-to-800-53-mod.json` is consistent with the 800-53 → CSF crosswalk in `nist-800-53-rmf/chunks/09-crosswalk.md` (bidirectional, no contradictions).
- The "5-part finding" pattern (Condition, Criteria, Cause, Effect, Recommendation) is reused in the gap-analysis output. CSF 2.0 doesn't define a finding format; we use the same pattern that 800-53 RMF uses, for cross-skill consistency.
- Severity tiers are consistent: CSF 2.0's Tier 1–4 ≠ 800-53 RMF's Tier 1–3 inheritance. We use "Tier" for CSF 2.0 and "Tier" only in the inheritance sense for 800-53 RMF, and we cross-reference explicitly.
- The questionnaire-reuse pattern from `nist-800-53-rmf/chunks/08-questionnaire-reuse.md` is **inverted**: a CSF Current Profile is the answer to a customer security questionnaire (CAIQ/SIG/VSAQ), not the question. We make this explicit in chunk 07.

**What we pre-empt:**

- A common finding would be: "you and the 800-53 RMF skill both claim 'tier 1-4' but mean different things." We pre-empt by adding a one-paragraph reconciliation in `chunks/02-tiers-and-profiles.md` that says: "CSF Tier 1-4 = organizational maturity. 800-53 'Tier 1' (Low), 'Tier 2' (Moderate), 'Tier 3' (High) = FIPS 199 impact. They are different scales." Plus a cross-reference to the 800-53 RMF skill's `chunks/02-categorize.md` for the latter.
- Another finding would be: "your gap-analysis output is 4-part, not 5-part." We pre-empt by ensuring every gap item has: condition, criteria (which CSF subcategory), cause, effect, recommendation (the 5-part structure). The 5-part structure is cross-skill, not CSF-specific.

---

## 7. PoV analyses — 5 practitioner personas (mirroring the 800-53 RMF 5-practitioner review)

For each persona, what they will specifically check for CSF 2.0.

### 7.1 Practitioner 1 — FedRAMP 3PAO Lead Assessor

**What they will check:**

- Does the CSF 2.0 skill map cleanly to FedRAMP's 800-53 baseline? The 3PAO assesses the system against 800-53, but the customer (agency) often wants a CSF view too. A clean CSF ↔ 800-53 crosswalk is the bridge.
- Is the GOVERN function coverage adequate for **federal oversight**? GV.OV (Oversight) and GV.MT (Monitoring) are the most-relevant GOVERN subcategories for federal accountability (FISMA, OMB A-130). The 3PAO will check that chunk 05 covers these.
- Does the Profile pattern (Current/Target) survive the trip from CSF 2.0 to FedRAMP? A FedRAMP-bound SaaS publishes a Current Profile (often: Tier 2), a Target Profile (Tier 3), and the gap (controls to implement before ATO). The 3PAO will expect the gap to align with the 800-53 control set in the SSP.

**What we pre-empt:**

- Include a **GV.OV / GV.MT specific** section in chunk 05 that maps to FISMA + OMB A-130 + FedRAMP ConMon requirements.
- Include a **CSF ↔ FedRAMP overlay** note in `chunks/08-informative-references-crosswalk.md` that flags which CSF Subcategories are **not** covered by 800-53 Rev 5 Mod/High (e.g., some GOVERN subcategories like GV.SC-04 — supplier criticality — are partially covered by 800-53 SR-3 but with different scope).
- Cite `NIST-SP-800-53-Rev5` and `FedRAMP-Rev5` in the references manifest.

### 7.2 Practitioner 2 — Big 4 SOX 404 Audit Partner

**What they will check:**

- Does CSF 2.0 have a clear **ICFR adjacency** angle? SOX 404 auditors look for control frameworks that overlap with financial reporting controls. CSF 2.0's GOVERN function (GV.OV, GV.MT) and parts of IDENTIFY (ID.RA) overlap with the COSO ICIF components and with PCAOB AS 2201.
- Can CSF 2.0 be used by SOX auditors as a **maturity assessment**? Yes — the Tier 1–4 scale is a maturity model. The Big 4 partner will check that the chunk 06 (enterprise reporting) and the maturity trend reporting are credible.
- Does the skill provide a **deficiency classification bridge**? CSF 2.0 doesn't have a deficiency classification; we use COSO's Significant Deficiency / Material Weakness as the cross-skill bridge. The partner will check that the cross-skill reference to `coso-internal-controls/chunks/05-deficiency-classification.md` is correct.

**What we pre-empt:**

- Include a **financial-reporting-overlap section** in `industries/financial-services.md` that maps each Function to the COSO component or PCAOB AS 2201 area it overlaps with.
- In chunk 04 (Target Profile), note that high-priority gaps in PR (PROTECT) and DE (DETECT) that affect financial reporting should be flagged as **SOX-relevant** in addition to cyber-relevant.
- Cross-reference `coso-internal-controls/chunks/05-deficiency-classification.md` and `chunks/04-walkthrough-controls.md`.

### 7.3 Practitioner 3 — SaaS Startup Head of Compliance

**What they will check:**

- Is the **first profile pattern** achievable in 1 day by a 2-person compliance team? The CTO/Head-of-Compliance at a Series-A SaaS is the GTM persona; they will not read a 2,000-line skill. They will read the SKILL.md router and UC-01.
- Are the **cost-aware implementation patterns** there? The SaaS practitioner will check chunk 07 for the small-org first-90-day path with rough cost ranges.
- Does the skill **bridge to SOC 2 and CAIQ**? SaaS practitioners know SOC 2; they want a CSF → SOC 2 crosswalk so the same evidence serves both. The chunk 08 crosswalk to SOC 2 is critical.

**What we pre-empt:**

- UC-01 (first profile) is the **explicit** GTM artifact; it is costed, time-boxed, and produces a 1-page board update.
- Chunk 07 (implementation playbook) has the small-org path with specific tool names and price ranges (MFA, EDR, SIEM-lite, backup).
- Chunk 08 has the CSF → SOC 2 crosswalk, with a note that "a CSF Current Profile + SOC 2 Type II covers 90%+ of CAIQ v4 fields."

### 7.4 Practitioner 4 — Healthcare CISO

**What they will check:**

- Does CSF 2.0 cover **HIPAA Security Rule** adequately as a CSF overlay? HIPAA Security Rule has 3 safeguard categories (administrative, physical, technical) and ~54 specific controls (45 CFR § 164.308–164.318). The CISO will check that the CSF → HIPAA crosswalk covers them.
- Is **HITRUST** referenced? HITRUST CSF is a separate (related) framework. The CISO will check that the skill explicitly distinguishes CSF 2.0 from HITRUST CSF, and that HITRUST is acknowledged as a related-but-different framework.
- Does the skill support a **healthcare organizational profile**? Even if we defer the healthcare industry view to v0.3.x, the chunk 02 must have the shape of a Community Profile that healthcare can use.

**What we pre-empt:**

- The `data/crosswalks/csf-to-hipaa.json` file (see §9) covers the 54 HIPAA Security Rule specifications mapped to the most-relevant CSF Subcategories.
- The `chunks/02-tiers-and-profiles.md` mentions HITRUST explicitly as a related framework.
- The `docs/limits-and-disclaimers.md` notes that healthcare is deferred to v0.3.x as an industry file.
- Chunk 05 (GOVERN) covers GV.PO (Policy) and GV.OV (Oversight), which are central to HIPAA's administrative safeguards.

### 7.5 Practitioner 5 — State Gov IT Audit Director

**What they will check:**

- Does CSF 2.0 accommodate **state RMF variants** (CA SAM, TX DIR, TX-RAMP)? State governments increasingly use CSF 2.0 as the board-facing framework and a state-RMF variant (built on 800-53) as the technical framework. The audit director will check that `industries/public-sector.md` covers this.
- Does the skill support **CJIS / IRS 1075** as overlays? Criminal justice and tax information systems have specific overlays; the state audit director covers both in their portfolio.
- Does the skill support a **state Community Profile**? StateRAMP and state-specific Community Profiles are emerging. The audit director will check that chunk 02 has the Community Profile shape right.

**What we pre-empt:**

- `industries/public-sector.md` includes a state-RMF-variants section (CA SAM, TX DIR, TX-RAMP) with cross-references.
- The `data/crosswalks/` directory can be extended in v0.3.x with `csf-to-cjis.json` and `csf-to-irs1075.json`; the v0.1.0 ship includes pointers in `docs/changelog.md` and `docs/architecture.md`.
- Chunk 02 (Tiers & Profiles) explicitly mentions Community Profiles (stateRAMP, state-specific, sector) as a category distinct from Organizational Profiles.

---

## 8. Cross-skill alignment table

For each of the 5 existing skills, the specific cross-references CSF 2.0 should have. Format: CSF 2.0 chunk → other skill chunk + 1-sentence rationale.

### 8.1 CSF 2.0 → `nist-800-53-rmf`

| CSF 2.0 chunk | 800-53 RMF chunk | Rationale |
|---------------|------------------|-----------|
| `01-functions-categories.md` | `chunks/02-categorize.md` | CSF Functions are NOT FIPS 199 categories, but the FIPS 199 categorization is **input** to the CSF profile's asset/system context. We cross-reference to disambiguate. |
| `02-tiers-and-profiles.md` | `chunks/02-categorize.md`, `chunks/03-baseline.md` | "Tier" means different things in CSF 2.0 (maturity) and 800-53 RMF (FIPS 199 impact). Cross-reference makes the disambiguation explicit. |
| `03-current-profile.md` | `chunks/05-assess.md` | 800-53A assessment is one of the two evidence sources for a CSF Current Profile (the other being the governance-level self-assessment). The SAR is the technical evidence; the CSF profile is the outcome statement. |
| `04-target-profile-and-gap.md` | `chunks/06-authorize.md` | POA&M items from the 800-53 RMF side become "gap remediation items" in the CSF Target Profile. Same item, two lenses. |
| `05-govern-function.md` | `chunks/02-categorize.md` §FIPS 199, `chunks/04-implement.md` §Common control | GOVERN's GV.SR-01 (Roles) maps to 800-53 PM-2 (Senior Information Security Officer) and PM-1 (Information Security Program Plan). |
| `08-informative-references-crosswalk.md` | `chunks/09-crosswalk.md` | The 800-53 RMF chunk 09 crosswalk has a one-paragraph "CSF 2.0 ↔ 800-53" entry. Our chunk 08 **reverses** the crosswalk and provides the curated JSON. |

### 8.2 CSF 2.0 → `isaca-audit-methodology`

| CSF 2.0 chunk | ISACA chunk | Rationale |
|---------------|-------------|-----------|
| `02-tiers-and-profiles.md` | `chunks/03-itaf-and-maturity.md` | ISACA's COBIT 2019 PAM (Process Assessment Model) is a 0–5 maturity scale; the CSF Tier 1–4 scale is conceptually similar. We map Tier 1 ↔ PAM 0-1, Tier 2 ↔ PAM 2, Tier 3 ↔ PAM 3, Tier 4 ↔ PAM 4-5. |
| `03-current-profile.md` | `chunks/04-itgc-itac.md` | ITGC (IT General Controls) testing is the ISACA methodology for assessing PROTECT-class controls. The current profile for PR.AA, PR.AC, PR.DS, PR.PS, PR.IR, PR.PT borrows the ITGC evidence structure. |
| `05-govern-function.md` | `chunks/02-cobit-2019.md` | COBIT 2019's EDM (Evaluate, Direct, Monitor) domain is the closest analog to the GOVERN function. We cross-reference for the EDM04 (Ensure Risk Optimization) and EDM02 (Ensure Benefits Delivery) mappings. |
| `06-enterprise-reporting.md` | `chunks/07-outputs-and-cross-refs.md` | ISACA's audit-report structure informs the board-deck structure for the maturity report. We reuse the executive-summary pattern. |
| `08-informative-references-crosswalk.md` | (COBIT 2019 is in `chunks/02-cobit-2019.md`) | CSF 2.0's informative references include COBIT 2019; we cite the mapping in chunk 08 and link to the ISACA chunk for the COBIT 2019 detail. |

### 8.3 CSF 2.0 → `coso-internal-controls`

| CSF 2.0 chunk | COSO chunk | Rationale |
|---------------|------------|-----------|
| `05-govern-function.md` | `chunks/01-coso-icif.md` | COSO Principle 1 (board oversight) and Principle 4 (risk appetite) map to GV.OV and GV.RM. The COSO chunk is the deep dive. |
| `04-target-profile-and-gap.md` | `chunks/05-deficiency-classification.md` | The "priority" field in the gap analysis borrows COSO's Significant Deficiency / Material Weakness classification for financial-reporting-relevant gaps. |
| `06-enterprise-reporting.md` | `chunks/06-rcm-and-reports.md` | COSO's RCM (Risk-Control Matrix) informs the Function → Category → Subcategory drill-down in the maturity report. |
| `05-govern-function.md` (GV.MT) | `chunks/02-coso-erm-monitoring.md` | COSO ERM's "Monitoring & Review" component is the conceptual parent of CSF's GV.MT. The COSO chunk is the deep dive. |

### 8.4 CSF 2.0 → `aicpa-soc-reporting`

| CSF 2.0 chunk | AICPA chunk | Rationale |
|---------------|-------------|-----------|
| `07-implementation-playbook.md` (SaaS path) | `chunks/01-soc-overview.md` | SOC 2 Type II is the natural precursor to a CSF profile for a SaaS. We reference the SOC overview for SaaS practitioners. |
| `08-informative-references-crosswalk.md` | `chunks/03-tsp-criteria.md` | SOC 2's 9 Common Criteria map to CSF 2.0 Subcategories. The AICPA chunk is the SOC-2 detail; our chunk 08 has the crosswalk. |
| `06-enterprise-reporting.md` | (board deck asset in `aicpa-soc-reporting/assets/`) | The board deck template borrows from the AICPA-skill board deck asset. We cross-reference. |
| `02-tiers-and-profiles.md` (Questionnaire-reuse) | `chunks/08-questionnaire-reuse.md` | The AICPA chunk covers CAIQ, SIG, VSAQ questionnaire reuse. CSF profile + SOC 2 = a SaaS questionnaire shortcut. We cross-reference. |

### 8.5 CSF 2.0 → `audit-workpapers`

| CSF 2.0 chunk | Workpapers chunk | Rationale |
|---------------|------------------|-----------|
| `04-target-profile-and-gap.md` | `chunks/05-finding-and-workflow.md` | The "5-part finding" pattern (Condition, Criteria, Cause, Effect, Recommendation) is the workpaper standard. Gap items use the 5-part structure. |
| `03-current-profile.md` | `chunks/01-standards-and-structure.md` | Current Profile subcategory evidence is structured as workpapers (per PCAOB AS 1215). We reference the workpaper standard. |
| `08-informative-references-crosswalk.md` | `chunks/07-qc-compliance-cross-refs.md` | QC and cross-reference standards apply when multiple cross-skill artifacts (800-53 SSP, SOC 2, CSF profile) coexist. We cite the QC standard. |
| `06-enterprise-reporting.md` | `chunks/09-substantive-analytical-procedures.md` | The maturity trend line and the KPI/KRI calculation borrow from substantive analytical procedures. The workpaper chunk is the methodological reference. |

### 8.6 Cross-skill reference shape (consistency library's view)

Per `tests/test_consistency_lib.py` (line 366, `test_cross_skill_references_resolve`), every cross-skill reference like `\`nist-800-53-rmf/chunks/09-crosswalk.md\`` must point to an existing file. We follow the same pattern. The 6 sibling skills are:

- `nist-800-53-rmf`
- `isaca-audit-methodology`
- `coso-internal-controls`
- `aicpa-soc-reporting`
- `audit-workpapers`
- (no 6th — we are the 6th)

The `test_cross_skill_references_resolve` check **must pass** in CI.

---

## 9. Data & synthetic content

Following the `nist-800-53-rmf/data/README.md` shape.

### 9.1 Directory layout

```
data/
  README.md
  generators/
    gen_csf_subcategory_scores.py   # generate a 108-row subcategory score fixture
    gen_csf_radar.py                # generate a 6-function radar
    gen_csf_roadmap.py              # generate a 90-day / 12-month roadmap
  seeds/
    uc-01-input.json
    uc-01-subcategory-scores.json
    uc-01-roadmap.json
    uc-01-expected.json
    uc-02-input.json
    uc-02-radar.json
    uc-02-plan.json
    uc-02-expected.json
    uc-03-input.json
    uc-03-lagging-subcategories.json
    uc-03-expected.json
  crosswalks/
    csf-2-0-subcategories.json      # all 108 subcategories with text
    csf-to-800-53-mod.json          # CSF Subcategory → 800-53 control IDs
    csf-to-hipaa.json               # CSF Subcategory → HIPAA Security Rule
    csf-to-soc2.json                # CSF Subcategory → SOC 2 Common Criteria
    csf-to-iso27001-2022.json       # CSF Subcategory → ISO 27001:2022 Annex A
    csf-to-cobit-2019.json          # CSF Subcategory → COBIT 2019
```

### 9.2 Generators (deterministic Python CLIs, --seed)

1. **`gen_csf_subcategory_scores.py`** — generates a 108-row subcategory score fixture. Inputs: `--seed` (int), `--org-name` (string), `--current-tier-mean` (float, default 2.0), `--target-tier` (float, default 3.0). Output: a JSON file with one row per subcategory (`subcategory_id`, `function`, `category`, `current_status`, `current_tier`, `target_status`, `target_tier`, `evidence_refs`, `owner`, `notes`).
2. **`gen_csf_radar.py`** — generates a 6-function radar (6 numbers, one per Function, each on a 0–4 scale). Inputs: `--seed`. Output: a JSON with `radar` dict and `lagging_functions` list.
3. **`gen_csf_roadmap.py`** — generates a 90-day or 12-month roadmap (list of items with priority, owner, target_date, estimated_cost, evidence_refs). Inputs: `--seed`, `--duration-days` (default 90), `--budget-usd` (default 0).

All three use Python's `random.Random(seed)` and produce byte-identical output for the same seed.

### 9.3 Seed JSONs (canonical fixtures)

- **3 UC input/output pairs** (uc-01, uc-02, uc-03) — each with `*-input.json`, `*-<intermediate>.json` (subcategory scores, radar, plan, lagging-subcategories), and `*-expected.json`.
- **1 base seed** (`base-csf-org.json`) — a generic 200-FTE manufacturer with a Tier 2 average profile. Used for general-purpose testing and as a sample in `data/README.md`.

### 9.4 Crosswalk JSONs

- **`csf-2-0-subcategories.json`** — the full 108-subcategory list with text. Each row: `subcategory_id` (e.g., "GV.OC-01"), `function` (e.g., "GOVERN"), `category` (e.g., "GV.OC"), `text` (the official CSF 2.0 subcategory statement), `informative_references_count` (int). This is the **load-bearing** crosswalk — every other crosswalk references it.
- **`csf-to-800-53-mod.json`** — the CSF → 800-53 Moderate mapping. Each row: `csf_id`, `nist_800_53_id[]` (array; can map to multiple controls), `mapping_strength` ("exact" / "partial" / "contextual"), `note`. ~200-300 rows. Note: this is the **reverse** of the `soc2-to-800-53-mod.json` (which is SOC 2 → 800-53). The 800-53 RMF chunk 09 has a one-paragraph CSF 2.0 entry; we make that paragraph executable via this crosswalk.
- **`csf-to-hipaa.json`** — the CSF → HIPAA Security Rule mapping. Each row: `csf_id`, `hipaa_spec[]` (e.g., "164.308(a)(1)(ii)(A)"), `mapping_strength`, `note`. ~50-100 rows. HIPAA Security Rule has 3 safeguard categories, 9 standards, ~54 specific implementation specifications.
- **`csf-to-soc2.json`** — the CSF → SOC 2 mapping. Each row: `csf_id`, `soc2_criteria[]` (e.g., "CC6.1"), `mapping_strength`, `note`. ~150-200 rows.
- **`csf-to-iso27001-2022.json`** — CSF → ISO 27001:2022 Annex A. Each row: `csf_id`, `iso27001_annex_a[]` (e.g., "A.5.15"), `mapping_strength`, `note`. ~100-150 rows.
- **`csf-to-cobit-2019.json`** — CSF → COBIT 2019. Each row: `csf_id`, `cobit_2019[]` (e.g., "DSS05.02"), `mapping_strength`, `note`. ~100-150 rows.

The crosswalk files are **curated** and explicitly disclaimed in `## 9. Anti-Hallucination Disclaimers` and in `docs/limits-and-disclaimers.md` ("always verify against the NIST CSF 2.0 Informative References spreadsheet; this curated crosswalk is a starting point").

### 9.5 PII / NPI / PHI redaction

Per `telemetry/redaction.md` and the Spine: all free-form PII is stripped before persistence; structured IDs (subcategory_id, uc_id, function name) are kept. Org names in seeds are synthetic ("FlowMetrics Inc.", "FirstAtlantic Bank", "PrecisionFab Manufacturing") and do not correspond to real entities.

---

## 10. Telemetry & docs

### 10.1 Telemetry

Reuse the existing `telemetry/schema.json` from `nist-800-53-rmf` (the `SkillInvocation` schema is skill-agnostic). The `telemetry/instrument.py` and `telemetry/redaction.md` are also reused unchanged. We add only:

- `telemetry/baseline.md` — populated after the first instrumented run with the measured `input_p50`, `input_p90`, `output_p50`, `output_p90` per UC.
- A new `telemetry/baseline.md` for CSF 2.0 (separate file, but same shape).

We do **not** modify the `SkillInvocation` schema for v0.1.0. A v0.3.x enhancement could add a `function` field (one of GOVERN/IDENTIFY/PROTECT/DETECT/RESPOND/RECOVER) to the schema, but that's a backward-compatible add.

### 10.2 Docs (4 files)

1. **`docs/architecture.md`** — same shape as `nist-800-53-rmf/docs/architecture.md`. Sections: Purpose, Invocation Model, Components, Data Flow, Review Protocol (3 cycles), Extensibility, Migration from pre-Spine (not applicable; CSF 2.0 ships on the Spine from day 1). Mirror the 800-53 RMF architecture.md structure for cross-skill consistency.
2. **`docs/limits-and-disclaimers.md`** — same shape. Sections: regulatory currency (CSF 2.0 Feb 2024, verify against the latest version), known gaps (no healthcare industry file in v0.1.0; no OSCAL machine-readable; no Community Profile authoring tool), the 4 anti-hallucination notes: 1.1 vs 2.0 delta, Tier disambiguation, crosswalk verification, subcategory count uncertainty.
3. **`docs/changelog.md`** — versioned log. v0.1.0: initial build. Future: v0.1.1, v0.2.0 (healthcare industry view), v0.3.x (OSCAL).
4. **`docs/acceptance-gate.md`** — the v0.1.0 acceptance gate. Boxes for: frontmatter, sections, routing, folders, SKILL.md size, chunks (8 files, ≤ 200 lines), context_budget, industries (4 files), UCs (3 files), data, tests (38 tests, 9 files), telemetry, docs, no TODOs, citations, baseline (pending first instrumented run), reviewer sign-off (3 cycles). Mirrors `nist-800-53-rmf/docs/acceptance-gate.md`.

### 10.3 What `acceptance-gate.md` should assert

- [x] Frontmatter — all required fields present.
- [x] Sections — first 10 sections present, in order.
- [x] §11 Routing — present, with the routing table mapping user intent → chunks.
- [x] Folders — `industries/`, `use-cases/`, `data/`, `tests/`, `telemetry/`, `docs/`, `chunks/` all exist and non-empty.
- [x] SKILL.md size — ≤ 300 lines (target: ≤ 280).
- [x] Chunks — 8 files (01-functions-categories, 02-tiers-and-profiles, 03-current-profile, 04-target-profile-and-gap, 05-govern-function, 06-enterprise-reporting, 07-implementation-playbook, 08-informative-references-crosswalk); each ≤ 200 lines; names match `NN-slug.md`.
- [x] `context_budget` — declared in frontmatter with 4 token fields.
- [x] Industries — 4 industry files (financial-services, public-sector, saas-technology, manufacturing); `_index.md` registered.
- [x] Use cases — 3 use-case files (UC-01, UC-02, UC-03); `_index.md` registered; each with `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`.
- [x] Data — `data/README.md` present; 3 generators; ≥ 10 seed fixtures; ≥ 6 crosswalks.
- [x] Tests — 9 test files; 38 tests pass.
- [x] Telemetry — `telemetry/schema.json` validates; `telemetry/instrument.py` importable; `telemetry/redaction.md` non-stub.
- [x] Docs — `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md` all non-stub.
- [x] No unfinished-work markers outside the changelog.
- [ ] Baseline — `telemetry/baseline.md` populated after first instrumented run.
- [x] Citations — every in-body `[LABEL §N]` reference resolves to `## 10. References & Citation Manifest` (test_grounding.py).
- [x] GOVERN function — 7 categories (GV.OC, GV.RM, GV.SC, GV.SR, GV.PO, GV.OV, GV.MT) all present in chunk 05.
- [x] Cross-skill references — every `<sibling>/chunks/NN-*.md` reference resolves to an existing file (test_consistency_lib::test_cross_skill_references_resolve).

---

## 11. Risk register

The 800-53 RMF skill shipped with 30+ findings from review. CSF 2.0 will likely surface 25–35 findings across the 5 lenses + 5 practitioners. Pre-empted below.

### 11.1 Top 5 likely framework-fidelity issues

1. **GOVERN function treatment** — the most-likely-misrepresented content. Risk: chunks under-represent GOVERN as "just a meta function" or treat the 7 categories as optional. Pre-empt: chunk 05 is a standalone file with one section per category, 25–40 lines each.
2. **PROTECT subcategory rename** — CSF 2.0 renamed PR.AC, PR.AT, PR.DS, PR.IP, PR.MA, PR.PT, PR.PS to PR.AA, PR.AC, PR.DS, PR.PS, PR.IR, PR.PT (and added PR.AA). Risk: chunks use 1.1-era names. Pre-empt: a 1.1-to-2.0 delta table in chunk 01; the seed JSON uses 2.0 subcategory IDs only.
3. **Tier 1–4 scale** — confused with 800-53 RMF "Tier 1/2/3" (FIPS 199 impact). Pre-empt: explicit reconciliation paragraph in chunk 02 + cross-reference to 800-53 RMF chunk 02.
4. **"Profile" terminology** — used loosely elsewhere. Pre-empt: the four Profile types (Current, Target, Organizational, Community) are defined in chunk 02 with a one-paragraph example each; the SKILL.md uses the exact terms.
5. **Subcategory count (~108)** — the exact count varies in the literature. Pre-empt: anti-hallucination note "108 numbered subcategories; verify against CSF 2.0 §2.3".

### 11.2 Top 5 likely completeness issues

1. **Missing GOVERN subcategories** in chunk 05 (e.g., a reviewer flags that GV.SC-04 is missing). Pre-empt: 1 row per subcategory in chunk 05, with `csf-2-0-subcategories.json` as the authoritative source.
2. **No implementation playbook for small org** — chunk 07 covers the small-org path; reviewer may say "this is too thin". Pre-empt: chunk 07 has a specific small-org section with cost ranges, tool names, and 90-day timeline.
3. **Community Profile authoring not in v0.1.0** — reviewer may say "you can't use CSF without Community Profiles". Pre-empt: chunk 02 defines the shape of a Community Profile + lists sector-specific ones; v0.1.0 doesn't author one but tells you how.
4. **OSCAL machine-readable not in v0.1.0** — reviewer may say "your skill isn't machine-readable". Pre-empt: `docs/limits-and-disclaimers.md` and `docs/architecture.md` explicitly note OSCAL is v0.3.x.
5. **Board deck template not load-tested** — chunk 06 has the outline; reviewer may say "this isn't a real deck". Pre-empt: chunk 06 includes a 12-page outline with 1-sentence description per page; full board deck is a v0.3.x asset.

### 11.3 Top 5 likely usability issues

1. **SKILL.md is too long to be a "90-second read"** — the executive reader bails. Pre-empt: SKILL.md is ≤ 280 lines; the §3 Core Concepts has a 1-screen table; the §2 Framework Overview has 1 paragraph + 1 table.
2. **6-function radar is buried in chunk 06** — executive can't find it. Pre-empt: a small ASCII-radar or table in SKILL.md §3.1 points to chunk 06 for the full version.
3. **Cross-references to 800-53 RMF are dense** — auditor gets lost. Pre-empt: the cross-skill alignment table (§8 above) is the navigation aid; in the chunks, the cross-references are short ("see `nist-800-53-rmf/chunks/05-assess.md` for SAR evidence structure").
4. **Chunk 05 (GOVERN) is too dense** — the 7 GOVERN categories × 25 lines = 175 lines plus intro and cross-refs = ~200 lines (right at the limit). Pre-empt: chunk 05 is split into 7 sections, each ~25 lines; if it overflows, we extract a sub-chunk (`05a-govern-categories-a-d.md`, `05b-govern-categories-e-g.md`).
5. **UC-01's "first profile" is too prescriptive** — reviewer may say "every SaaS is different". Pre-empt: UC-01 is one worked example; chunk 07 has the generalizable pattern with 3 personas (small, mid-market, large).

### 11.4 Top 5 likely convention issues

1. **SKILL.md > 300 lines** — the 800-53 RMF router is 249; CSF 2.0 could easily blow past 300. Pre-empt: target ≤ 280 lines; if a draft hits 300, split into a chunk.
2. **One chunk > 200 lines** — chunk 05 (GOVERN) is the risk. Pre-empt: target ≤ 180 lines; sub-chunk if needed.
3. **`tools/lint_skill.py` fails** — most likely root cause: missing `context_budget` field, missing industry, missing UC, or chunk filename pattern. Pre-empt: run the linter **after every chunk is written** (Day 1 EOD, Day 2 EOD, Day 3 morning).
4. **No `tests/test_<slug>_lint.py`** — easy to forget. Pre-empt: Day 3 morning checklist explicitly includes creating this test file.
5. **TODO/FIXME in chunks** — the linter flags these. Pre-empt: every "TODO" in the chunk text becomes a parenthetical or is resolved before commit.

### 11.5 Top 5 likely cross-skill issues

1. **Broken cross-skill references** — `\`nist-800-53-rmf/chunks/09-crosswalk.md\`` exists, but if we cite `chunks/10-*.md` (which doesn't exist) the consistency library fails. Pre-empt: the cross-skill alignment table (§8) is the source of truth; every chunk author consults it.
2. **Severity tier confusion** (CSF Tier 1-4 vs 800-53 FIPS 199 impact). Pre-empt: §11.1 item 3 above.
3. **Different "5-part finding" format** — gap items must match the workpaper 5-part structure. Pre-empt: chunk 04 cites the workpaper chunk and reuses the format.
4. **Questionnaire-reuse shape mismatch** — the 800-53 RMF chunk 08 is the **answer** (800-53 evidence answers questionnaires); CSF chunk 08 is the **crosswalk** (CSF Subcategory ↔ other frameworks). Pre-empt: we make this distinction explicit in chunk 08.
5. **Industry keys out of sync** — `industries/_index.md` lists "manufacturing" but the 800-53 RMF skill's industry list says "manufacturing" is "Optional". Pre-empt: confirm with the consistency library (test_industry_index_sync) and the 800-53 RMF skill (its `industries/_index.md` should not list manufacturing if we don't include it; we DO include it in CSF 2.0, so the 800-53 RMF skill may need a follow-on update).

---

## 12. Build sequence (proposed day-by-day)

5-day plan; matches the M-effort estimate in Linear.

### Day 1 — Scaffold + router + chunks skeleton

**Morning:**
1. `cp -r skills/TEMPLATE skills/nist-csf-2`
2. Edit SKILL.md frontmatter: `name: nist-csf-2`, `description` (the 1-sentence activation trigger), `risk: high`, `source: "NIST CSF 2.0 (Feb 2024)"`, `date_added: 2026-06-05` (or whatever the build date is), `version: 0.1.0`, `status: draft`, `industries: [financial-services, public-sector, saas-technology, manufacturing]`, `frameworks: [NIST-CSF-2.0, ...]`, `tags: [csf-2.0, nist, govern, profile, current-target, tier, ...]`, `context_budget: { ... }`.
3. Build the SKILL.md body (§1 When to Use, §2 Framework Overview, §3 Core Concepts, §4 Decision Logic summary, §5 Procedure Templates summary, §6 Output Templates summary, §7 Cross-References, §8 Worked Examples, §9 Anti-Hallucination, §10 References manifest, §11 Routing).
4. Target: SKILL.md ≤ 280 lines.

**Afternoon:**
5. Create the 8 chunk files with stub frontmatter (chunk_id, parent_skill, topic, load_when) and ~30 lines of placeholder body each.
6. Run `python tools/lint_skill.py skills/nist-csf-2` — expect FAIL (no industries, no UCs, no data yet).
7. Run `python tools/test_consistency_lib.py ...` — expect FAIL (chunks have stub frontmatter).

**EOD:** Linter output captured for Day 5 reviewer.

### Day 2 — Industries + UCs + data

**Morning:**
1. Write the 4 industry files (`industries/financial-services.md`, `public-sector.md`, `saas-technology.md`, `manufacturing.md`) — 60–100 lines each, following the 4-quadrant pattern (Posture, Boundary, Regulator/customer, Top use cases, Pain points, References).
2. Write `industries/_index.md` with the 4-industry table.
3. Write the 3 UC files (`use-cases/uc-01-...md`, `uc-02-...md`, `uc-03-...md`) with full frontmatter (uc_id, title, industries, procedure, expected_outputs, oracle, data_refs, tests, status) and the full scenario / walk-through body.
4. Write `use-cases/_index.md` with the 3-UC table.

**Afternoon:**
5. Write `data/generators/gen_csf_subcategory_scores.py`, `gen_csf_radar.py`, `gen_csf_roadmap.py` — deterministic, `--seed` CLI.
6. Run the generators to produce the seed JSONs (`uc-01-input.json`, `uc-01-subcategory-scores.json`, `uc-01-roadmap.json`, `uc-01-expected.json`, plus the 6 for UC-02 and UC-03).
7. Write `data/crosswalks/csf-2-0-subcategories.json` (the 108-row authoritative list) and the 5 derived crosswalks (`csf-to-800-53-mod.json`, `csf-to-hipaa.json`, `csf-to-soc2.json`, `csf-to-iso27001-2022.json`, `csf-to-cobit-2019.json`).
8. Write `data/README.md` with the data dictionary.

**EOD:** Linter should now report `industries OK`, `use-cases OK`, `data OK`.

### Day 3 — Tests + run linter + run pytest

**Morning:**
1. Write the 9 test files:
   - `tests/test_nist_csf_2_lint.py` (3 tests)
   - `tests/test_nist_csf_2_oracle.py` (6 tests)
   - `tests/test_nist_csf_2_grounding.py` (4 tests)
   - `tests/test_nist_csf_2_trace.py` (3 tests)
   - `tests/test_nist_csf_2_metamorphic.py` (4 tests)
   - `tests/test_nist_csf_2_adversarial.py` (5 tests)
   - `tests/test_nist_csf_2_telemetry.py` (7 tests)
   - `tests/test_nist_csf_2_consistency.py` (6 tests, wraps lib)
   - `tests/nist_csf_2_stub.py` (the entrypoint stub)
2. Write `tests/conftest.py` (mirrors the 800-53 RMF pattern).
3. Add the 3 CI/CD required status checks: PR title, `tools/lint_skill.py skills/nist-csf-2`, `pytest tests/test_nist_csf_2_*.py tests/test_consistency_lib.py`.

**Afternoon:**
4. Run `python tools/lint_skill.py skills/nist-csf-2` — expect 0 errors, may have warnings.
5. Run `pytest tests/test_nist_csf_2_*.py tests/test_consistency_lib.py` — expect 38 tests pass.
6. Fix any failures; iterate.
7. Write the 4 docs files: `docs/architecture.md`, `docs/limits-and-disclaimers.md`, `docs/changelog.md`, `docs/acceptance-gate.md`.
8. Write `telemetry/baseline.md` as a stub (populated after first instrumented run).

**EOD:** All 38 tests pass; linter returns 0; `telemetry/baseline.md` is a stub.

### Day 4 — 5-lens review (5 agents in parallel)

Dispatch 5 background agents (using the `delegate` tool) for the 5-lens review:

1. **Agent 1 — Framework fidelity review.** Read the entire skill; verify every Function, Category, Subcategory, Profile, Tier, and crosswalk is faithful to CSF 2.0. Produce a list of findings tagged CRITICAL/HIGH/MEDIUM/LOW.
2. **Agent 2 — Completeness review.** Verify all 6 Functions, 22 Categories, ~108 Subcategories are present. Verify all 4 Profile types are defined. Verify all 4 Tiers are defined. Verify the GOVERN function is treated as first-class.
3. **Agent 3 — Usability review.** Verify the SKILL.md router is 90-second-readable. Verify the chunks are navigable. Verify the 4-quadrant industry views are present. Verify the executive-legibility promise is preserved.
4. **Agent 4 — Convention compliance review.** Run `tools/lint_skill.py`; verify 0 errors. Verify SKILL.md ≤ 280 lines, chunks ≤ 200 lines. Verify `context_budget` declared. Verify 3+ industries, 3+ UCs.
5. **Agent 5 — Cross-skill alignment review.** Verify cross-references to `nist-800-53-rmf`, `isaca-audit-methodology`, `coso-internal-controls`, `aicpa-soc-reporting`, `audit-workpapers` resolve. Verify the 5-part finding pattern is used. Verify the Tier disambiguation is explicit.

Each agent runs against the 800-53 RMF skill as a **reference for what good looks like** and produces a findings list. Aggregate findings; classify by CRITICAL/HIGH/MEDIUM/LOW; assign owners.

### Day 5 — 5-practitioner review + fix waves

Dispatch 5 background agents for the 5-practitioner review (mirroring Day 4's pattern but with practitioner personas):

1. **Agent 1 — FedRAMP 3PAO Lead Assessor.** Same as §7.1.
2. **Agent 2 — Big 4 SOX 404 Audit Partner.** Same as §7.2.
3. **Agent 3 — SaaS Startup Head of Compliance.** Same as §7.3.
4. **Agent 4 — Healthcare CISO.** Same as §7.4.
5. **Agent 5 — State Gov IT Audit Director.** Same as §7.5.

Each agent runs the skill against a real-world scenario and produces a findings list. Aggregate findings; classify by CRITICAL/HIGH/MEDIUM/LOW.

**Fix waves:**

- **Wave 1 (CRITICAL + HIGH):** address all CRITICAL and HIGH findings from both Days 4 and 5. Re-run linter + pytest.
- **Wave 2 (MEDIUM):** address MEDIUM findings. Re-run.
- **Wave 3 (LOW):** address LOW findings if time permits; defer to v0.1.1.

**EOD:** Linter 0; pytest 38 pass; `docs/changelog.md` updated with v0.1.0 notes; `docs/acceptance-gate.md` updated with sign-offs.

**Ship:** Bump status to `review`; create PR; request review from at least one external contributor (mirroring the SOX-566 PR-merge pattern).

---

## 13. File-by-file plan (Day 1 + Day 2 deliverable)

This is the **deliverable** of the design doc. Every file we will create in the build, with the section in the build sequence that produces it.

| File | Source section | Lines target | Build day |
|------|----------------|--------------|-----------|
| `skills/nist-csf-2/SKILL.md` | §1, §2 (router) | ≤ 280 | Day 1 |
| `skills/nist-csf-2/chunks/01-functions-categories.md` | §2.1 | ≤ 180 | Day 1 |
| `skills/nist-csf-2/chunks/02-tiers-and-profiles.md` | §2.2 | ≤ 180 | Day 1 |
| `skills/nist-csf-2/chunks/03-current-profile.md` | §2.3 | ≤ 180 | Day 1 |
| `skills/nist-csf-2/chunks/04-target-profile-and-gap.md` | §2.4 | ≤ 180 | Day 1 |
| `skills/nist-csf-2/chunks/05-govern-function.md` | §2.5 | ≤ 180 (split if needed) | Day 1 |
| `skills/nist-csf-2/chunks/06-enterprise-reporting.md` | §2.6 | ≤ 180 | Day 1 |
| `skills/nist-csf-2/chunks/07-implementation-playbook.md` | §2.7 | ≤ 180 | Day 1 |
| `skills/nist-csf-2/chunks/08-informative-references-crosswalk.md` | §2.8 | ≤ 200 | Day 1 |
| `skills/nist-csf-2/industries/_index.md` | §3.5 | ≤ 30 | Day 2 |
| `skills/nist-csf-2/industries/financial-services.md` | §3.1 | ≤ 100 | Day 2 |
| `skills/nist-csf-2/industries/public-sector.md` | §3.2 | ≤ 100 | Day 2 |
| `skills/nist-csf-2/industries/saas-technology.md` | §3.3 | ≤ 100 | Day 2 |
| `skills/nist-csf-2/industries/manufacturing.md` | §3.4 | ≤ 100 | Day 2 |
| `skills/nist-csf-2/use-cases/_index.md` | §4 (intros) | ≤ 30 | Day 2 |
| `skills/nist-csf-2/use-cases/uc-01-first-profile.md` | §4.1 | ≤ 220 | Day 2 |
| `skills/nist-csf-2/use-cases/uc-02-board-report.md` | §4.2 | ≤ 220 | Day 2 |
| `skills/nist-csf-2/use-cases/uc-03-csf-to-800-53.md` | §4.3 | ≤ 220 | Day 2 |
| `skills/nist-csf-2/data/README.md` | §9.1 | ≤ 100 | Day 2 |
| `skills/nist-csf-2/data/generators/gen_csf_subcategory_scores.py` | §9.2 | ≤ 100 | Day 2 |
| `skills/nist-csf-2/data/generators/gen_csf_radar.py` | §9.2 | ≤ 60 | Day 2 |
| `skills/nist-csf-2/data/generators/gen_csf_roadmap.py` | §9.2 | ≤ 80 | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-01-input.json` | §4.1 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-01-subcategory-scores.json` | §4.1 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-01-roadmap.json` | §4.1 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-01-expected.json` | §4.1 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-02-input.json` | §4.2 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-02-radar.json` | §4.2 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-02-plan.json` | §4.2 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-02-expected.json` | §4.2 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-03-input.json` | §4.3 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-03-lagging-subcategories.json` | §4.3 | — | Day 2 |
| `skills/nist-csf-2/data/seeds/uc-03-expected.json` | §4.3 | — | Day 2 |
| `skills/nist-csf-2/data/crosswalks/csf-2-0-subcategories.json` | §9.4 | — | Day 2 |
| `skills/nist-csf-2/data/crosswalks/csf-to-800-53-mod.json` | §9.4 | — | Day 2 |
| `skills/nist-csf-2/data/crosswalks/csf-to-hipaa.json` | §9.4 | — | Day 2 |
| `skills/nist-csf-2/data/crosswalks/csf-to-soc2.json` | §9.4 | — | Day 2 |
| `skills/nist-csf-2/data/crosswalks/csf-to-iso27001-2022.json` | §9.4 | — | Day 2 |
| `skills/nist-csf-2/data/crosswalks/csf-to-cobit-2019.json` | §9.4 | — | Day 2 |
| `skills/nist-csf-2/tests/conftest.py` | §5.10 | ≤ 30 | Day 3 |
| `skills/nist-csf-2/tests/nist_csf_2_stub.py` | §5.9 | ≤ 150 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_lint.py` | §5.1 | ≤ 30 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_oracle.py` | §5.2 | ≤ 100 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_grounding.py` | §5.3 | ≤ 80 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_trace.py` | §5.4 | ≤ 80 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_metamorphic.py` | §5.5 | ≤ 100 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_adversarial.py` | §5.6 | ≤ 100 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_telemetry.py` | §5.7 | ≤ 120 | Day 3 |
| `skills/nist-csf-2/tests/test_nist_csf_2_consistency.py` | §5.8 | ≤ 60 | Day 3 |
| `skills/nist-csf-2/telemetry/schema.json` | §10.1 (reused) | — | Day 1 |
| `skills/nist-csf-2/telemetry/instrument.py` | §10.1 (reused) | — | Day 1 |
| `skills/nist-csf-2/telemetry/redaction.md` | §10.1 (reused) | — | Day 1 |
| `skills/nist-csf-2/telemetry/baseline.md` | §10.1 (stub) | ≤ 20 | Day 3 |
| `skills/nist-csf-2/docs/architecture.md` | §10.2 | ≤ 100 | Day 3 |
| `skills/nist-csf-2/docs/limits-and-disclaimers.md` | §10.2 | ≤ 100 | Day 3 |
| `skills/nist-csf-2/docs/changelog.md` | §10.2 | ≤ 50 | Day 3 (updated Day 5) |
| `skills/nist-csf-2/docs/acceptance-gate.md` | §10.2 | ≤ 60 | Day 3 (updated Day 5) |
| `skills/nist-csf-2/README.md` | (consumer one-pager) | ≤ 60 | Day 5 (post-merge) |

Total: **57 files** (3 of which are reused unchanged from 800-53 RMF; 1 of which is a 1-line stub).

---

## 14. Open questions for Monday review

These are the design decisions we should discuss on Monday before locking the build plan:

1. **Healthcare in v0.1.0 or v0.3.x?** §1.6 and §3 argue v0.3.x. If a reviewer wants healthcare in v0.1.0, we add it as a 5th industry file.
2. **Manufacturing in v0.1.0 or v0.3.x?** §3.4 and §3.5 ship manufacturing in v0.1.0 because the cross-framework UC-03 (CSF ↔ 800-53 ↔ CISA ICS CPG) needs a manufacturing industry view.
3. **Community Profile authoring in v0.1.0?** §1.6 defers to v0.3.x; if the practitioner review wants it, we add a `data/seeds/community-profile-financial-services-v0.1.json` and a 9th chunk on Community Profile authoring.
4. **OSCAL in v0.1.0?** §1.6 defers to v0.3.x. If we add OSCAL, it's a 9th chunk + a new crosswalk data type.
5. **Questionnaire-reuse as chunk 09?** §2.9 argues against (CSF is the questionnaire). If a reviewer wants the explicit "how to answer CAIQ with a CSF profile" content, we add a 9th chunk.
6. **CSF 2.0 + 800-53 RMF as one skill?** No — the brief says "this is a separate skill." Confirmed.
7. **Default Tier for the small-org path?** §2.7 says Tier 2.5 for Series A SaaS, Tier 3 for mid-market. Confirmed.
8. **CI status checks — same 3 as 800-53 RMF (PR title, lint, pytest)?** Yes; we don't add a 4th check for v0.1.0.

---

## 15. Requirements parameters checklist (template for future skill designs)

> **This section is the canonical instance of the standardized template.** The standalone template lives at `docs/skill-design-template.md`. This design doc was the first fully-filled example; future skill design docs should copy the standalone template and fill it in.

| # | Parameter | Section in this doc | Required? |
|---|-----------|---------------------|-----------|
| 1 | **Scope & dependencies** — standard reference, structural inventory, persona, effort estimate, dependencies, out-of-scope | §1 | Yes |
| 1.1 | Primary source citation (with URL and retrieval date) | §1.1 | Yes |
| 1.2 | Structural inventory (counts of functions/categories/subcategories/etc.) | §1.2 | Yes |
| 1.3 | Persona (IT / FIN / GRC / BOTH) with 1-sentence justification | §1.3 | Yes |
| 1.4 | Effort estimate (S/M/L/XL) per Linear | §1.4 | Yes |
| 1.5 | Dependencies (other skills or Linear issues) | §1.5 | Yes |
| 1.6 | Out-of-scope (explicit non-goals) | §1.6 | Yes |
| 2 | **Chunk architecture** — numbered set of 7-9 chunks | §2 | Yes (skills above 300 lines only) |
| 2.1–2.N | For each chunk: filename, frontmatter, trigger phrases, cross-references | §2.1–§2.8 | Yes |
| 2.N+1 | Why 7/8/9 chunks (rationale for the count) | §2.9 | Yes |
| 3 | **Industry angles** — 3-4 industry files | §3 | Yes |
| 3.1–3.N | For each: most-relevant Functions, real-world example, what the view ADDS, cross-references | §3.1–§3.4 | Yes |
| 3.N+1 | `_index.md` table | §3.5 | Yes |
| 4 | **Use cases** — 3-4 worked examples | §4 | Yes |
| 4.1–4.N | For each: frontmatter contract, real-world scenario, input JSON shape, procedure, expected output, oracle | §4.1–§4.3 | Yes |
| 4.N+1 | UC selection rationale | §4.4 | Yes |
| 5 | **Test architecture** — 9 test files, target test count | §5 | Yes |
| 5.1–5.9 | For each test file: specific test cases | §5.1–§5.9 | Yes |
| 5.10 | Test count summary table | §5.10 | Yes |
| 6 | **PoV analyses — 5 lenses** | §6 | Yes |
| 6.1 | Framework fidelity | §6.1 | Yes |
| 6.2 | Completeness | §6.2 | Yes |
| 6.3 | Usability | §6.3 | Yes |
| 6.4 | Spine convention compliance | §6.4 | Yes |
| 6.5 | Cross-skill alignment | §6.5 | Yes |
| 7 | **PoV analyses — 5 practitioner personas** | §7 | Yes |
| 7.1–7.5 | For each persona: what they will check, what we pre-empt | §7.1–§7.5 | Yes |
| 8 | **Cross-skill alignment table** | §8 | Yes |
| 8.1–8.N | For each sibling skill: CSF chunk → other skill chunk + rationale | §8.1–§8.5 | Yes |
| 8.6 | Cross-skill reference shape (consistency library's view) | §8.6 | Yes |
| 9 | **Data & synthetic content** | §9 | Yes |
| 9.1 | Directory layout | §9.1 | Yes |
| 9.2 | Generators (deterministic CLIs) | §9.2 | Yes |
| 9.3 | Seed JSONs | §9.3 | Yes |
| 9.4 | Crosswalk JSONs | §9.4 | Yes |
| 9.5 | PII / NPI / PHI redaction | §9.5 | Yes |
| 10 | **Telemetry & docs** | §10 | Yes |
| 10.1 | Telemetry (schema, instrument, redaction, baseline) | §10.1 | Yes |
| 10.2 | Docs (4 files) | §10.2 | Yes |
| 10.3 | What `acceptance-gate.md` should assert | §10.3 | Yes |
| 11 | **Risk register** | §11 | Yes |
| 11.1 | Top 5 framework-fidelity issues | §11.1 | Yes |
| 11.2 | Top 5 completeness issues | §11.2 | Yes |
| 11.3 | Top 5 usability issues | §11.3 | Yes |
| 11.4 | Top 5 convention issues | §11.4 | Yes |
| 11.5 | Top 5 cross-skill issues | §11.5 | Yes |
| 12 | **Build sequence** — day-by-day plan | §12 | Yes |
| 13 | **File-by-file plan** — table of every file to create | §13 | Yes |
| 14 | **Open questions for review** | §14 | Yes |
| 15 | **Requirements parameters checklist** (canonical at `docs/skill-design-template.md`) | §15 | Yes (this template) |

A future skill design doc that hits all 15 sections (with the same sub-structure) is reviewable in one sitting and convertible into a build plan without further clarification. The 800-53 RMF skill (the load-bearing reference) covered 12 of 15 sections; CSF 2.0 covers all 15. Future skills should aim for 15/15.

---

## 16. Sign-off

This design doc is **complete and ready for Monday review**. Build plan conversion is straightforward: §13 (file-by-file plan) + §12 (build sequence) is the build plan. No additional design work is required.

- [ ] Design review (Monday) — owner: amurthy
- [ ] Convert to build plan (post-review) — owner: amurthy
- [ ] Begin build (Day 1) — owner: amurthy
- [ ] Ship v0.1.0 (Day 5) — owner: amurthy + at least 1 external reviewer

— End of design doc —
