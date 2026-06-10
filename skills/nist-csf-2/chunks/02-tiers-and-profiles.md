---
chunk_id: 02-tiers-and-profiles
parent_skill: nist-csf-2
topic: "Tiers 1-4 and Profile types: Current, Target, Organizational, Community"
load_when: "user asks about Tiers, Profiles, Current Profile, Target Profile, or how to start"
---

# Chunk 02 — Tiers & Profiles

CSF 2.0 [NIST-CSF-2.0 §3] layers two ideas on top of the Functions/Categories/Subcategories spine: **Tiers** characterize *the rigor* of the org's cybersecurity risk governance and management practices, and **Profiles** describe *what outcomes* the org is achieving today and aims to achieve in the future. **Tiers are not maturity levels** (NIST's long-standing FAQ position: "The Framework Implementation Tiers are not intended to be maturity levels"). Both Tiers and Profiles are needed to build a remediation roadmap (see `chunks/04-target-profile-and-gap.md`).

## 1. The 4 Tiers (rigor of risk governance and management)

Tiers [NIST-CSF-2.0 §3.2, Appendix B] characterize an organization's cybersecurity risk governance and management practices, and per CSWP 29 "can be applied to CSF Organizational Profiles" — i.e., NIST applies them at the **Organizational Profile** level. Scoring a separate Tier per Function (the radar in `chunks/06`) is a common **practitioner extension**, not framework text — label it as such in deliverables. Tiers are **not** prescriptive (CSF does not say "every org must reach Tier 4") and are not maturity levels; they describe characteristics so the org can position itself.

| Tier | Name | Process | Org-wide risk management | External participation |
|------|------|---------|--------------------------|------------------------|
| 1 | **Partial** | Ad hoc, reactive; cybersecurity risk is not formalized as part of the org's enterprise risk strategy | Not informed by org objectives; risk is managed case-by-case | None |
| 2 | **Risk Informed** | Some formalization; risk-informed practices exist but are not org-wide | Approved by management but not org-wide; awareness of risk at the business-unit level | Limited; org understands its role in the broader ecosystem |
| 3 | **Repeatable** | Formally approved and expressed as policy; documented and consistently applied org-wide | Org-wide; informed by risk; roles/responsibilities defined | Receives and shares; active in sector coordination |
| 4 | **Adaptive** | Continuously improved; lessons learned incorporated into plans; adaptive practices respond to evolving threats | Org-wide, informed by org-level risk; uses advanced tech and analytics | Active sharing across sector and with regulators; contributes to community resilience |

**Practical heuristic for selecting a target Tier per Function:**

- **Tier 1** is a starting point for a brand-new program (e.g., a 5-person shop with no documented cybersecurity practices).
- **Tier 2** is a common first target for small-to-mid orgs that have ad-hoc controls and need to formalize them.
- **Tier 3** is the typical target for mature commercial orgs, regulated financial services, federal contractors, and any org reporting to a board cyber committee.
- **Tier 4** is appropriate for orgs at the frontier of cyber risk management (large financial institutions, critical infrastructure operators with active ISAC participation, government agencies with mature continuous-monitoring programs).

**Tier selection is not normative** [NIST-CSF-2.0 §3.1]. The org picks its Tier based on risk tolerance, business objectives, and applicable regulation. There is no CSF-mandated formula. The "right" Tier depends on the org's threat profile and what its customers/regulators expect.

## 2. The 4 Profile types

Profiles [NIST-CSF-2.0 §3.2] align Functions/Categories/Subcategories to the org's mission, risk tolerance, and resources. CSF 2.0 formalized 4 Profile types — in 1.1, only "Current" and "Target" were named.

| Profile | What it is | Who authors it | When used |
|---------|-----------|----------------|-----------|
| **Current Profile** | Snapshot of the outcomes the org is achieving **today**, scored by Subcategory (Not Implemented / Partially / Largely / Fully Implemented) | The org itself (with optional assessor) | Starting point for any maturity conversation |
| **Target Profile** | The desired outcomes, given risk tolerance, business objectives, and applicable regulation | The org, with board/exec input | Defines the "to-be" state and the destination of the roadmap |
| **Organizational Profile** | The org's unique posture — can be a Current, Target, or hybrid view — that distinguishes one org from another | The org | The unit of comparison between orgs and the basis for sharing with partners/regulators |
| **Community Profile** | A published, sector-aligned baseline (e.g., a financial-services ISAC, HHS for healthcare, CISA for OT) | Sector-coordinating body | Org Profiles align to a Community Profile; orgs use Community Profiles as a reference target |

**Relationships:**

- A **Current Profile** is one expression of an Organizational Profile (the "where we are" view).
- A **Target Profile** is another expression of an Organizational Profile (the "where we want to be" view).
- The **gap** between Current and Target is the **work plan** (see `chunks/04-target-profile-and-gap.md`).
- A **Community Profile** is the sector's recommended Organizational Profile — orgs compare their own Organizational Profile to a Community Profile to see how they stack up against sector peers.
- The same Subcategory grid is used for all 4 Profile types; only the *score* changes.

**Concrete Community Profile examples** (the org does not author these):

- Financial services: the CRI Profile and sector ISAC-published profiles (the FFIEC CAT was sunset effective Aug 31, 2025)
- Healthcare: HHS HPH Cybersecurity Performance Goals and 405(d) HICP (a healthcare view is a known gap in this skill)
- Public sector / critical infrastructure: CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0, Dec 2025) and sector overlays (FedRAMP, StateRAMP)
- Manufacturing/OT: CISA CPGs + SP 800-82 Rev 3 OT overlays

## 3. GOVERN's role in Tier setting

Because GOVERN is the umbrella Function, its Tier acts as a **ceiling** on the other 5 Functions in practice: an org at Tier 1 in GOVERN (no cyber risk strategy, no oversight, no defined roles) cannot credibly operate at Tier 3 in PROTECT (the org-wide policy and accountability scaffolding for Tier 3 PROTECT does not exist). The practical sequencing:

1. **Assess GOVERN first** when building a Current Profile (see `chunks/03-current-profile.md`).
2. **Target Tier for GOVERN** is typically set before the Target Tiers for the other 5 — it represents the org's commitment to cyber risk governance.
3. **GOVERN target Tier ≥ operational Function target Tiers** is a useful sanity check; the inverse (PROTECT Tier 3, GOVERN Tier 1) is almost always a self-attestation error.

This is a **planning heuristic**, not a CSF-mandated rule. CSF 2.0 does not specify a Tier-ordering constraint.

## 4. How to choose a starting Tier (heuristic)

CSF 2.0 does not provide a normative Tier-selection rule. The following heuristic is a planning aid, not a CSF mandate [NIST-CSF-2.0 §3.1]. Use it to position the org on the Tier ladder for the first assessment, then refine via Current Profile data.

**Inputs:**

- Org size and cyber team size
- Regulatory regime (HIPAA, PCI, NY DFS 500, FFIEC, CMMC, FISMA, etc.)
- Customer base (enterprise, federal, retail consumers, B2B SMB)
- Data sensitivity (PII volume, PHI, PCI cardholder data, CUI, OT)
- Threat profile (sector-targeted, opportunistic, nation-state)

**Decision tree (heuristic):**

```
IF org has < 50 FTE AND no dedicated cyber hire:
    starting Tier ≈ 1.5 to 2 across most Functions
    GOVERN Tier likely 1 (no board oversight, no documented risk strategy)
ELIF org is 50-1,000 FTE AND has 1-5 cyber/security FTE:
    starting Tier ≈ 2 to 3 across most Functions
    GOVERN Tier likely 2 (some policy, limited oversight)
ELIF org is > 1,000 FTE AND has 5+ cyber/security FTE:
    starting Tier ≈ 2.5 to 3.5
    GOVERN Tier likely 3 (board committee, formal risk strategy)
ELIF org is a federal agency or major federal contractor:
    starting Tier ≈ 3 across all Functions
    GOVERN Tier 3 (FISMA / OMB A-130 mandate)
ELIF org is a critical-infrastructure operator (energy, finance, healthcare):
    starting Tier ≈ 2.5 to 3.5
    GOVERN Tier likely 3 (sector regulation drives maturity)
```

The starting Tier is then **refined by the Current Profile**: if the Current Profile says 30% of Subcategories are Fully Implemented and 40% are Partially, the empirical Tier may be 2.0 not 2.5. The heuristic gives the prior; the Current Profile data gives the posterior.

## 5. Relationship to NIST SP 800-53 baselines (Low/Mod/High)

The word **"Tier"** collides across NIST constructs — and none of them is an "800-53 Tier" (no such thing exists; earlier versions of this chunk invented one). The reconciliation:

| Construct | What it describes | Values | Source |
|-------|------------------|--------|--------|
| **CSF Tier** | Rigor of cyber risk governance/management practices (applied to Organizational Profiles) | 1 (Partial) → 4 (Adaptive) | [NIST-CSF-2.0 §3.2, App. B] |
| **SP 800-39/800-37 risk-management Tiers** | LEVEL of the risk-management hierarchy, not a rating: Tier 1 = organization, Tier 2 = mission/business process, Tier 3 = system | 1 / 2 / 3 (levels, not scores) | NIST SP 800-39 / SP 800-37 Rev 2 |
| **FIPS 199 impact level** (drives the 800-53 baseline) | Worst-case impact of a system breach on C/I/A | Low / Moderate / High (impact LEVELS — never called "Tiers") | [FIPS-199] [NIST-SP-800-53-Rev5] |
| **COBIT 2019 CPM** | Process capability | 0 → 5 | COBIT 2019 |

These are **independent axes**:

- An org with FIPS 199 **Low** systems can still be CSF **Tier 4** (Adaptive).
- An org with FIPS 199 **High** systems can be CSF **Tier 1** (Partial) — the systems are sensitive but the org has not built the governance scaffolding.
- CSF Tiers inform **how rigorously** the org manages risk; FIPS 199 impact levels inform **what control baseline** applies to a system; 800-39 Tiers say **at which organizational level** a risk decision lives.

When a conversation says "we're a Tier 3 org", verify which construct is meant — a federal practitioner saying "Tier 3" most likely means the SYSTEM level of the 800-39 hierarchy, not a maturity score and not FIPS 199 Moderate. See `nist-800-53-rmf/chunks/02-categorize.md` for the baseline selection flow.

## 6. Community Profile pointers (where to look)

Community Profiles are authored by sector-coordinating bodies, not by the org or this skill. The org aligns its Organizational Profile to a relevant Community Profile to benchmark against sector peers. The following are illustrative pointers — verify currency before citing.

- **Financial services**: the FFIEC sunset the CAT effective Aug 31, 2025 and pointed institutions to CSF 2.0 and industry profiles such as the CRI Profile; sector ISACs publish CSF-aligned profiles. NY DFS 500.02 requires a cybersecurity program; the program can be expressed as a CSF Organizational Profile.
- **Public sector / critical infrastructure**: CISA's Cross-Sector Cybersecurity Performance Goals (CPG 2.0, Dec 2025 — ~34 goals, IDs like 1.A grouped under the six CSF 2.0 Functions) are a Community Profile-style minimum baseline.
- **Public sector (state)**: State-specific overlays (CA SAM, TX DIR SCSC, TX-RAMP, StateRAMP) often map to CSF. Many state regulators accept a CSF-aligned Organizational Profile as evidence.
- **Healthcare**: HHS publishes the HPH Cybersecurity Performance Goals and 405(d) HICP — the real sector baselines (a healthcare view is a known gap in this skill). The HIPAA Security Rule is a regulation, not a Community Profile.
- **Manufacturing / OT**: CISA CPGs plus SP 800-82 Rev 3 OT overlay guidance are the most direct OT-aligned baselines.
- **Cross-sector**: the NIST CSF 2.0 Informative References spreadsheet itself is a cross-sector reference.

This skill does not author Community Profiles; it ships the *shape* (6 Functions × 22 Categories × 106 Subcategories grid) that any Community Profile uses.

## Cross-references

- `chunks/01-functions-categories.md` — the Functions/Categories/Subcategories spine that Profiles score against.
- `chunks/03-current-profile.md` — procedure to build the Current Profile (the "where we are" view).
- `chunks/04-target-profile-and-gap.md` — Target Profile construction and the gap analysis (the work plan).
- `chunks/05-govern-function.md` — the GOVERN Function deep-dive; GOVERN Tier sets the ceiling for the other 5 in practice.
- `nist-800-53-rmf/chunks/02-categorize.md` — FIPS 199 categorization (the 800-53 "Tier" — different scale, same word).

## Anti-hallucination

- **Authoritative source**: Tier definitions and Profile types are from NIST CSF 2.0 [NIST-CSF-2.0 §3.1-§3.2] (Feb 26, 2024). Verify wording against the official PDF at https://www.nist.gov/cyberframework. Do not paraphrase the Tier names: **Partial, Risk Informed, Repeatable, Adaptive** are the official labels.
- **There is no "800-53 Tier."** CSF Tiers characterize rigor of risk governance/management (and are not maturity levels); FIPS 199 defines impact LEVELS (Low/Moderate/High); SP 800-39/800-37 Tiers 1-3 are organization/mission/system LEVELS of the risk-management hierarchy. Always disambiguate when a stakeholder says "Tier".
- **Tier selection is not a normative algorithm.** CSF 2.0 describes the Tier characteristics and lets the org pick. The heuristic in §1 is a planning aid, not a CSF rule.
- **Profile types are 4** in CSF 2.0 (Current, Target, Organizational, Community). In CSF 1.1 only Current and Target were named; the Organizational and Community types are formalized in 2.0.
- **A Community Profile is not authored by the org** — it is published by a sector-coordinating body (ISAC, regulator, HHS, CISA). The org uses Community Profiles as a reference target; it does not produce them. This skill ships the *shape* of Community Profiles but does not author sector-specific content.
- **Per-Function Tier scoring is a practitioner extension, not NIST framework text.** CSWP 29 applies Tiers to Organizational Profiles. If you use the per-Function radar (`chunks/06-enterprise-reporting.md`), label it as a management convention and never present fractional or per-Function Tiers as NIST methodology.
