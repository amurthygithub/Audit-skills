---
chunk_id: 03-current-profile
parent_skill: nist-csf-2
topic: "Building the Current Profile: what the org does today, by subcategory"
load_when: "user asks to build a profile, do a current-state assessment, or wants the first profile"
---

# Chunk 03 — Current Profile

The **Current Profile** is the "where we are today" snapshot of the organization's cybersecurity outcomes, scored by Subcategory. It is the starting point of any CSF engagement and the foundation for the Target Profile, the gap analysis, and the remediation roadmap (see `chunks/04-target-profile-and-gap.md`). A Current Profile is **not** a maturity number; it is a per-Subcategory evidence map that, when aggregated, yields a maturity Tier per Function.

## 1. What a Current Profile is (and is not)

A Current Profile is:

- A per-Subcategory record of the outcomes the org is achieving **today** across the 6 Functions, 22 Categories, and 106 Subcategories of CSF 2.0.
- An **evidence-backed** assessment — each score is supported by a document, observation, test, or attestation.
- A **snapshot** — it describes the org at a moment in time, not over a period.
- The **first artifact** in a CSF engagement; everything else (Target Profile, gap, roadmap) is built on top of it.

A Current Profile is **not**:

- A numeric risk score (CSF is maturity-based, not risk-score-based).
- A single Tier number for the org (Tiers are per Function; see `chunks/02-tiers-and-profiles.md`).
- A control-by-control audit (use 800-53A for that — see `nist-800-53-rmf`).
- A SOC 2 opinion (use `aicpa-soc-reporting` for SOC 2 work).
- A statement of intent (the Target Profile is that; the Current Profile is the as-is).

## 2. Evidence gathering: 4 sources

For each Subcategory, the assessor gathers evidence from up to 4 sources. The 4 evidence-quality tiers (in increasing quality):

| Tier | Evidence type | Example | Strength |
|------|---------------|---------|----------|
| 1 | **Documented** | Policy doc, procedure, standard | Shows intent; may be aspirational |
| 2 | **Observed** | Config screenshot, walkthrough observation, system inventory | Shows existence in practice |
| 3 | **Tested** | A control test result (similar to 800-53A test) | Shows the control operates effectively |
| 4 | **Attested** | Independent attestation (SOC 2 Type II, 3PAO assessment, ISO 27001 cert) | Shows external validation |

**Best practice:** require at least 2 evidence sources per Subcategory, including at least 1 "tested" or "attested" source for any Subcategory scored as "Fully Implemented". A Subcategory with status "Fully Implemented" but only "documented" evidence is a self-attestation risk (this is an adversarial test case in `tests/test_nist_csf_2_adversarial.py`).

**Evidence types by source method:**

- **Interviews** — talk to control owners (CISO, IT director, GRC manager, system owners). Best for "is the policy actually followed" questions.
- **Document review** — policies, procedures, system security plans, prior audit reports (SOC 2, ISO 27001, 800-53A). Best for "documented" tier.
- **Observation** — walkthroughs, system demonstrations, config reviews. Best for "observed" tier.
- **Testing** — re-perform a control (e.g., attempt an unauthorized change, run a vulnerability scan, test backup restore). Best for "tested" tier.
- **Existing attestations** — pull from SOC 2, ISO 27001, 800-53A test results, HITRUST, PCI ROC. Best for "attested" tier.

## 3. Scoring each Subcategory

This skill's 4-level Subcategory-status convention (NOT a NIST scale — CSWP 29 defines no implementation-status scale, and SP 1301's example is explicitly notional/free-format):

| Status | Definition | Tier indicator (heuristic) |
|--------|-----------|------------------------------|
| **Not Implemented** | No evidence the outcome is achieved | Tier 1 (Partial) |
| **Partially Implemented** | Some evidence; gaps exist | Tier 1 → Tier 2 |
| **Largely Implemented** | Most evidence; minor gaps | Tier 2 → Tier 3 |
| **Fully Implemented** | Comprehensive evidence; tested or attested | Tier 3 → Tier 4 |

The Tier indicator is a **heuristic mapping**. CSF 2.0 does not prescribe a formula (and implementation status ≠ Tier — see the anti-hallucination note below). This skill's reference executor (`tests/nist_csf_2_stub.py`) uses a documented demo heuristic: per Function, map statuses to ordinals (Not=1, Partially=2, Largely=2, Fully=3), take the median, and report T1/T2/T3 (a status-derived indicator can never exceed T3 — Tier 4's adaptive practices cannot be inferred from implementation status); Functions with no scored rows default to T1 with a "no evidence" note. Treat the output as an indicative starting point for the governance judgment, never as the Tier determination itself.

## 4. Mapping evidence to Subcategories

**Procedure** (5-7 steps):

1. **Scope the assessment** — which org units, which systems, which Functions are in scope. A Series-A SaaS at first-profile stage is typically the whole org; a $20B bank may scope to one business unit.
2. **Identify control owners per Function** — Governance owner, Identity/Asset owner, Protection owner, Detection owner, Response owner, Recovery owner. GOVERN-first: identify the GOVERN owner first because they set the assessment rules.
3. **Gather documentation** — request the org's policy library, prior audit reports, system inventory, risk register. Use the org's existing artifacts before inventing new ones.
4. **Walkthroughs and interviews** — schedule per Function; use the Subcategory grid as the question set (the canonical 106-row list is the NIST CSF 2.0 PDF Appendix A / CSRC reference export; representative samples in `chunks/01-functions-categories.md` §3 — this skill ships no derivative JSON).
5. **Score each Subcategory** — assign status (Not/Partially/Largely/Fully), cite evidence_refs, and identify the owner. Record contradictions explicitly.
6. **Aggregate to Function-level Tier** — compute the heuristic Tier per Function from the Subcategory scores.
7. **Document the Current Profile** — emit the Current Profile YAML (see §5) and flag the Subcategories that are Self-Attestation Risks (Fully Implemented with only Documented evidence).

## 5. Output template: Current Profile (YAML)

```yaml
profile_type: current
assessment_date: <YYYY-MM-DD>
assessor: <name or org>
scope: <org unit / system / Functions in scope>
function_tiers:
  GOVERN:   {tier: 1-4, fully_implemented_pct: 0-100, lagging_subcategories: [<list>]}
  IDENTIFY: {tier: 1-4, fully_implemented_pct: 0-100, lagging_subcategories: [<list>]}
  PROTECT:  {tier: 1-4, fully_implemented_pct: 0-100, lagging_subcategories: [<list>]}
  DETECT:   {tier: 1-4, fully_implemented_pct: 0-100, lagging_subcategories: [<list>]}
  RESPOND:  {tier: 1-4, fully_implemented_pct: 0-100, lagging_subcategories: [<list>]}
  RECOVER:  {tier: 1-4, fully_implemented_pct: 0-100, lagging_subcategories: [<list>]}
subcategories:
  - subcategory_id: GV.OC-01
    status: Not Implemented | Partially Implemented | Largely Implemented | Fully Implemented
    evidence_refs: [<doc-1>, <screenshot-2>, ...]
    evidence_tier: documented | observed | tested | attested
    owner: <role or name>
    notes: <1-2 sentences>
  - subcategory_id: PR.AA-01
    status: ...
    ...
self_attestation_risks:
  - <subcategory_id>  # Fully Implemented but only Documented evidence
contradictions:
  - <description of any tier-self-assessment vs evidence mismatch>
```

The full set of 106 Subcategory entries is the Current Profile; the per-Function aggregation is the visualization layer for board reporting (see `chunks/06-enterprise-reporting.md`).

## 6. Worked example (fictional): 50-person SaaS at Tier 2

**Organization**: "DataRelay Inc." — fictional 50-FTE B2B SaaS providing analytics connectors. AWS commercial, processes B2B contact data (~80k records), no dedicated security hire, security is 0.5 FTE inside a 4-person IT team. SOC 2 Type I in progress.

**Current Profile (abbreviated):**

| Subcategory | Status | Evidence tier | Notes |
|-------------|--------|---------------|-------|
| GV.OC-01 (mission) | Partially Implemented | Documented | Mission documented in employee handbook; not linked to cyber risk decisions |
| GV.SC-01 (supply chain) | Not Implemented | — | No third-party risk program |
| GV.RR-01 (roles) | Partially Implemented | Documented | RACI exists for IT; no cybersecurity-specific RACI |
| ID.AM-01 (HW inventory) | Fully Implemented | Tested | AWS Config + endpoint agent, monthly reconciliation |
| ID.RA-01 (vuln ID) | Largely Implemented | Tested | Quarterly external scan; no internal vuln program |
| PR.AA-01 (identity) | Largely Implemented | Tested | SSO + MFA for prod; service accounts not fully inventoried |
| PR.DS-01 (data-at-rest encryption) | Fully Implemented | Tested | KMS-encrypted RDS, S3 default encryption |
| DE.CM-01 (network monitoring) | Partially Implemented | Observed | VPC flow logs on; no IDS/IPS |
| DE.CM-09 (compute monitoring) | Not Implemented | — | No runtime anomaly detection |
| RS.MA-01 (IR plan) | Partially Implemented | Documented | Plan drafted; never tested |
| RC.RP-01 (recovery plan) | Largely Implemented | Tested | RPO/RTO defined; backup restore tested Q2 |

**Function-level Tiers (heuristic aggregation):**
- GOVERN: 1.5 (mostly Partially, some Not Implemented)
- IDENTIFY: 2.5
- PROTECT: 3.0
- DETECT: 1.5
- RESPOND: 2.0
- RECOVER: 2.5

**Top-3 lagging Subcategories** (input to Target Profile and roadmap): `GV.SC-01`, `DE.CM-09`, `GV.RR-01`.

**Self-attestation risks** (Flagged): none in this example — every "Fully Implemented" has at least a "Tested" evidence tier.

**Contradictions** (Flagged): "Partially Implemented" on `RS.MA-01` but staff self-described IR as "ready" — flagged for management-letter follow-up.

This 50-FTE SaaS is the realistic starting state for many orgs. The Target Profile and gap analysis (see `chunks/04-target-profile-and-gap.md`) turn this into a roadmap.

## Cross-references

- `chunks/01-functions-categories.md` — the Functions/Categories/Subcategories spine; the Current Profile scores against this grid.
- `chunks/02-tiers-and-profiles.md` — Tiers 1-4 and the 4 Profile types; the Current Profile is one Profile type.
- `chunks/04-target-profile-and-gap.md` — Target Profile construction and gap analysis (the next step after Current Profile).
- `chunks/05-govern-function.md` — the GOVERN Function deep-dive; assess GOVERN first when building a Current Profile.
- `nist-800-53-rmf/chunks/02-categorize.md` — FIPS 199 categorization (informs the scope of a Current Profile in a federal-customer environment; *not* the same as a CSF Tier).

## Anti-hallucination

- **Authoritative source**: the Subcategory IDs and the Profile concept are from NIST CSF 2.0 [NIST-CSF-2.0 §3.2] (Feb 26, 2024). The 4-level status scale (Not/Partially/Largely/Fully) is **this skill's convention, NOT a NIST scale** — CSWP 29 defines no implementation-status scale, and SP 1301 (Organizational Profiles QSG) shows only a notional free-text example, telling orgs to "use whatever format they prefer." Document whatever scale you use and apply it consistently.
- **Tier and Subcategory achievement are separate concepts.** A Subcategory can be Fully Implemented at a Tier 1 org (a single heroic SysAdmin can achieve the outcome without org-wide policy). Conversely, an org can have a documented policy (Tier 2) but a Subcategory only Partially Implemented (the policy is not followed in practice). The heuristic mapping in §3 is a planning aid, not a CSF rule.
- **The worked example is fictional** ("DataRelay Inc." is a placeholder). The Subcategory scores, evidence tiers, and Tier aggregations are illustrative of a typical 50-FTE SaaS; they are not an actual assessment.
- **A Current Profile is not a SOC 2 opinion.** It is an internal maturity view; SOC 2 is an external assurance report. The two inform each other (a SOC 2 Type II report provides "attested" evidence for many Subcategories) but they are not interchangeable.
- **A Current Profile is not a quantitative risk score.** Do not invent a numeric risk score (e.g., "cyber risk = 67/100"). CSF 2.0 is maturity-based; the outputs are statuses, Tiers, and gaps, not scalar scores.
- **Self-attestation risk**: any Subcategory scored "Fully Implemented" with only "documented" evidence is a self-attestation risk. The skill flags these explicitly in the `self_attestation_risks` field of the Current Profile YAML.
