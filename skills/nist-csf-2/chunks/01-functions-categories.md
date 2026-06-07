---
chunk_id: 01-functions-categories
parent_skill: nist-csf-2
topic: "6 Functions, 22 Categories, 108 Subcategories — the CSF 2.0 structure"
load_when: "user asks about CSF structure, functions, categories, subcategories, or the GOVERN function"
---

# Chunk 01 — Functions & Categories

The NIST Cybersecurity Framework 2.0 (Feb 26, 2024) organizes cybersecurity outcomes into a 3-layer taxonomy: **6 Functions → 22 Categories → ~108 Subcategories**. The Functions are the executive-legible spine; the Categories are the practitioner-legible groupings; the Subcategories are the assessable outcomes. This chunk is the structural reference — load it whenever a question turns on "what is CSF 2.0" or on a specific Category / Subcategory ID.

## 1. The 6 Functions (the spine)

CSF 2.0 [NIST-CSF-2.0 §2.1] organizes cybersecurity outcomes into 6 Functions. The first one (GOVERN) is new in 2.0; the other five preserve the 1.1 cycle.

| # | Function | Code | One-line definition | Role |
|---|----------|------|---------------------|------|
| 1 | **GOVERN** | GV | Establish and monitor the org's cyber risk management strategy, expectations, and policy | New in 2.0; sets context for the other 5 |
| 2 | **IDENTIFY** | ID | Understand the org's assets, suppliers, and related cyber risks | You cannot protect what you have not identified |
| 3 | **PROTECT** | PR | Implement safeguards to manage cybersecurity risk | Preventive controls |
| 4 | **DETECT** | DE | Discover and analyze cybersecurity events | Detective controls |
| 5 | **RESPOND** | RS | Take action regarding a detected cybersecurity incident | Incident response |
| 6 | **RECOVER** | RC | Restore assets and operations affected by a cybersecurity incident | Resilience and continuity |

Mnemonic: **"Good Identities Protect, Detect, Respond, Recover"** (G-I-P-D-R-R). GOVERN is the umbrella; the other 5 are the operational cycle.

## 2. The 22 Categories (the groupings)

Each Function decomposes into Categories. CSF 2.0 has **22 Categories** total (down from 23 in CSF 1.1 — one merger plus the new GOVERN block). Codes use the `<Function>.<Category>` form, e.g., `GV.OC`, `ID.AM`, `PR.AA`.

### GOVERN (6 Categories — new in 2.0)

| Code | Category | Focus |
|------|----------|-------|
| GV.OC | Organizational Context | Mission, stakeholders, legal/regulatory requirements |
| GV.RM | Risk Management Strategy | Risk tolerance, appetite, risk management process |
| GV.SC | Cybersecurity Supply Chain Risk Management | Third-party / supply-chain cyber risk (elevated in 2.0) |
| GV.RR | Roles, Responsibilities, and Authorities | RACI, accountability, ownership |
| GV.PO | Policy | Cybersecurity policy lifecycle |
| GV.OV | Oversight | Performance review, strategy adjustment |

### IDENTIFY (3 Categories)

| Code | Category | Focus |
|------|----------|-------|
| ID.AM | Asset Management | Hardware, software, data, services, people inventory |
| ID.RA | Risk Assessment | Threats, vulnerabilities, likelihood, impact |
| ID.IM | Improvement | Lessons learned, plan testing, continuous improvement |

### PROTECT (5 Categories — renamed in 2.0)

| Code | Category | Focus |
|------|----------|-------|
| PR.AA | Identity Management, Authentication, and Access Control | IAM, MFA, least privilege (renamed in 2.0) |
| PR.AT | Awareness and Training | User training, role-based training |
| PR.DS | Data Security | Encryption, integrity, retention |
| PR.PS | Platform Security | Configuration, vulnerability management, secure SDLC |
| PR.IR | Technology Infrastructure Resilience | Network segmentation, redundancy |

### DETECT (2 Categories)

| Code | Category | Focus |
|------|----------|-------|
| DE.CM | Continuous Monitoring | Network, personnel, environment monitoring |
| DE.AE | Adverse Event Analysis | Event correlation, impact analysis, alerts |

### RESPOND (4 Categories)

| Code | Category | Focus |
|------|----------|-------|
| RS.MA | Incident Management | Triage, declaration, escalation |
| RS.AN | Incident Analysis | Forensics, root cause, scope |
| RS.CO | Incident Response Reporting and Communication | Internal/external/regulator notifications |
| RS.MI | Incident Mitigation | Containment, eradication |

### RECOVER (2 Categories)

| Code | Category | Focus |
|------|----------|-------|
| RC.RP | Incident Recovery Plan Execution | Restore systems, validate restoration |
| RC.CO | Incident Recovery Communication | Public, customer, internal recovery messaging |

## 3. The ~108 Subcategories (the assessables)

Each Category decomposes into Subcategories — the outcome-level statements that get scored during a Profile assessment. CSF 2.0 publishes **~108 Subcategories** (the precise count varies by how sub-letter items are tallied; the NIST PDF lists ~106 numbered + a handful of sub-letters). Subcategories use the `<Category>-<NN>` form.

Representative sample (full canonical list lives in `data/crosswalks/csf-2-0-subcategories.json` and the official NIST CSF 2.0 PDF Appendix):

| Subcategory | Outcome |
|-------------|---------|
| GV.OC-01 | The organizational mission is understood and informs cybersecurity risk management |
| GV.OC-05 | Outcomes, capabilities, and services that the org depends on are understood and communicated |
| GV.RM-01 | Risk management objectives are established and agreed to by stakeholders |
| GV.SC-01 | A cybersecurity supply chain risk management program is established |
| ID.AM-01 | Inventories of hardware managed by the organization are maintained |
| ID.AM-08 | Systems, hardware, software, services, and data are managed throughout their life cycles |
| ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded |
| PR.AA-01 | Identities and credentials for authorized users, services, and hardware are managed |
| PR.AA-05 | Access permissions, entitlements, and authorizations are defined and managed |
| PR.DS-01 | Confidentiality, integrity, and availability of data-at-rest are protected |
| DE.CM-01 | Networks and network services are monitored to find potentially adverse events |
| DE.CM-09 | Computing hardware and software, runtime environments, and their data are monitored |
| RS.MA-01 | The incident response plan is executed in coordination with relevant third parties |
| RC.RP-01 | The recovery portion of the incident response plan is executed once initiated |

Subcategories-per-Category counts are uneven: `GV.OC` has 5 Subcategories, `ID.AM` has 8, `PR.AA` has 6, `DE.CM` has 9, `RS.MA` has 5, etc. The full counts are in the NIST CSF 2.0 PDF Appendix.

## 4. GOVERN: the new Function (the executive layer)

GOVERN is the single largest change from CSF 1.1 → 2.0 and the most-likely-misrepresented content in any CSF write-up. It deserves dedicated attention because it is the **executive-legible** entry point to the framework. Three things to know:

**First**, GOVERN is positioned at the **top** of the Function model — it is not a sixth peer of the operational cycle, it is the **umbrella**. GOVERN outcomes set the context (mission, risk appetite, policy, oversight) that the other 5 Functions execute against. In practice this means: assess GOVERN **first** when building a Current Profile, because the GOVERN answers (Who owns this? What is our risk appetite? Where is the board involved?) determine what "good" looks like for the other 5.

**Second**, GOVERN absorbed two concerns that were under-represented in 1.1: (a) **supply chain risk** (now its own Category `GV.SC` — elevated from a single 1.1 ID.SC Category to a board-level GOVERN concern), and (b) **roles and responsibilities** (now `GV.RR` — explicit accountability for cybersecurity decisions). Both reflect the post-SolarWinds, post-Kaseya regulatory environment.

**Third**, GOVERN is where executive-facing language lives. The 6 GOVERN Categories map almost 1:1 to the questions a board's Audit/Risk Committee asks: GV.OC ("what business are we protecting?"), GV.RM ("how much risk are we willing to take?"), GV.SC ("are our suppliers a liability?"), GV.RR ("who is accountable?"), GV.PO ("do we have policies?"), GV.OV ("how do we know it's working?"). For deep-dive treatment of each GOVERN Category and its Subcategories, see `chunks/05-govern-function.md`.

## 5. Relationship to 800-53 control families and CSF 1.1

**CSF Categories are not 800-53 control families.** CSF Categories are **outcome-grouped**; 800-53 control families are **control-mechanism-grouped**. The two taxonomies are complementary but **not 1:1** — a single CSF Category typically maps to controls across multiple 800-53 families:

- **GV.OC** (Organizational Context) → 800-53 `PM-11`, `PM-15`, `RA-1` (Program Management + Risk Assessment families)
- **GV.SC** (Supply Chain Risk Management) → 800-53 `SR-1` through `SR-12` (the entire SR family, plus `PM-30`)
- **PR.AA** (Identity & Access Control) → 800-53 `AC`, `IA`, `PS` families (Access Control + Identification & Authentication + Personnel Security)
- **DE.CM** (Continuous Monitoring) → 800-53 `SI-4`, `AU-2`, `AU-6`, `CA-7` (Information Integrity + Audit + Continuous Monitoring)
- **RS.MA** (Incident Management) → 800-53 `IR-4`, `IR-5`, `IR-6` (Incident Response family)
- **RC.RP** (Recovery Plan Execution) → 800-53 `CP-2`, `CP-10`, `IR-8` (Contingency Planning + Incident Response)

The full curated mapping ships in `data/crosswalks/csf-to-800-53-mod.json` and the analysis lives in `chunks/08-informative-references-crosswalk.md`. Orientation: **CSF tells you the outcome you want; 800-53 tells you the controls that produce that outcome**. Use CSF for executive conversations and Profile maturity; use 800-53 for control specification and ATO evidence.

**CSF 1.1 → 2.0 delta** (for migration):

| Change | 1.1 | 2.0 |
|--------|-----|-----|
| Function count | 5 (Identify/Protect/Detect/Respond/Recover) | 6 (added GOVERN) |
| Category count | 23 | 22 (one PROTECT merger; PROTECT categories renamed) |
| Supply chain | 1 Category (ID.SC) under IDENTIFY | Elevated to GV.SC under GOVERN |
| PROTECT codes | PR.AC, PR.AT, PR.DS, PR.IP, PR.MA, PR.PT | PR.AA, PR.AT, PR.DS, PR.PS, PR.IR (renamed/restructured) |
| Profile types | Current, Target | Current, Target, Organizational, Community (formalized) |
| Tiers | 4 (Partial, Risk Informed, Repeatable, Adaptive) | 4 (unchanged) |

Practical migration note: a 1.1 Current Profile does not automatically become a 2.0 Current Profile. The GOVERN Subcategories must be assessed fresh and the PROTECT mappings re-codified. Treat 1.1 → 2.0 as a re-baseline, not a rename.

## Cross-references

- `chunks/02-tiers-and-profiles.md` — Tiers 1-4 and the 4 Profile types (the maturity and posture layers built on top of this structural spine).
- `chunks/05-govern-function.md` — Deep dive on the GOVERN Function (the new content in 2.0; this chunk gives the structural intro, chunk 05 gives the per-Category treatment).
- `chunks/08-informative-references-crosswalk.md` — Full CSF Subcategory → 800-53 / ISO 27001 / SOC 2 / HIPAA / PCI / COBIT mappings.
- `nist-800-53-rmf/chunks/02-categorize.md` — FIPS 199 categorization (informs CSF Profile scope; note the "Tier" word collision called out in §5 above and in `chunks/02-tiers-and-profiles.md`).
- `nist-800-53-rmf` (skill root) — control catalog sibling; 800-53 control families (`AC`, `AU`, `CA`, `CM`, `CP`, `IA`, `IR`, `MP`, `PE`, `PL`, `PM`, `PS`, `PT`, `RA`, `SA`, `SC`, `SI`, `SR`, `AT`) are the implementation surface for the CSF outcomes described here.

## Anti-hallucination

- **Authoritative source**: the Subcategory IDs, exact wording, and Category groupings cited here come from the NIST CSF 2.0 publication [NIST-CSF-2.0 §2.1-§2.3] (Feb 26, 2024). When in doubt, verify against the official PDF at https://www.nist.gov/cyberframework. The Subcategory IDs (`GV.OC-01`, `PR.AA-01`, etc.) are the **authoritative reference**; do not paraphrase them or invent new IDs.
- **Subcategory count is ~108** in CSF 2.0; the precise count varies between 106 and 108 depending on whether sub-letter items are counted. The "~108" figure used across this skill is intentional; cite the official NIST PDF for an exact tally.
- **2.0 changed from 1.1**: the GOVERN Function (and its 6 Categories) did not exist in 1.1. Do not attribute `GV.*` Subcategories to 1.1. The PROTECT Category codes were renamed (1.1 used `PR.AC`, `PR.IP`, `PR.MA`; 2.0 uses `PR.AA`, `PR.PS`, `PR.IR`). When users cite a 1.1-era Subcategory ID, flag it and re-map to the 2.0 equivalent.
- **CSF Categories are not 800-53 control families**. A statement like "GV.OC is a control family" is wrong. CSF Categories are outcome groupings; 800-53 families are mechanism groupings. The mapping is many-to-many. See `chunks/08-informative-references-crosswalk.md` for the curated mapping.
- **The "Tier" word collides** with FIPS 199 / 800-53 RMF "Tier" (Low/Moderate/High impact). CSF Tiers (1-4) are organizational maturity; 800-53 Tiers are FIPS 199 impact. Different scales, same word. See `chunks/02-tiers-and-profiles.md`.
- This chunk encodes the framework structure; it does not assert what Subcategories any particular organization implements. Profile content is org-specific and lives in `chunks/03-current-profile.md` and the use-case files.
