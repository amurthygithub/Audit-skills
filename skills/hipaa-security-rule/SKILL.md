---
name: hipaa-security-rule
description: "HIPAA Security Rule (45 CFR Part 164, Subpart C): 22 standards across administrative (9), physical (4), technical (5), organizational (2), and policies/documentation (2) families, with Required vs Addressable implementation specifications. Serves BOTH auditor and auditee personas. Use to run a §164.308(a)(1)(ii)(A) risk analysis, work addressable-specification dispositions per §164.306(d)(3), check a BAA against §164.314(a)(2)(i), build an OCR-readiness matrix across all 22 standards, or right-size safeguards via the §164.306(b)(2) flexibility factors. Activate when the user says 'HIPAA Security Rule', 'ePHI', '45 CFR 164', 'addressable specification', 'business associate agreement', 'BAA', 'OCR audit', 'security risk analysis', 'HIPAA safeguards', or 'recognized security practices'."
category: audit-framework
risk: informational
source: "45 CFR Part 164, Subpart C (Security Standards for the Protection of Electronic Protected Health Information), as amended through 78 FR 34266 (June 7, 2013) — https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C. Companions: NIST SP 800-66 Rev 2 (Feb 2024), HHS SRA Tool, PL 116-321 (recognized security practices, Jan. 5, 2021), 45 CFR Part 102 (penalty inflation adjustments). The 2025 NPRM (90 FR 898) is a PROPOSED rule only as of 2026-06-10."
date_added: 2026-06-10
version: 0.1.0
status: draft
industries: [healthcare, saas-technology, financial-services, public-sector]
frameworks: [HIPAA-Security-Rule, NIST-SP-800-66-Rev2, HITECH]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
context_budget:
  always_loaded_tokens: 3500      # this SKILL.md (router)
  per_call_typical_tokens: 7000   # router + 1 chunk + 1 industry + 1 UC
  per_call_max_tokens: 16000      # router + all chunks + industry + UC
  per_call_p90_tokens: 9000       # estimate — no instrumented baseline yet
tags: [hipaa, security-rule, ephi, 45-cfr-164, subpart-c, addressable, required, risk-analysis, risk-management, administrative-safeguards, physical-safeguards, technical-safeguards, baa, business-associate, ocr, enforcement, hitech, recognized-security-practices, sp-800-66, sra-tool, healthcare, covered-entity]
---

You are an expert agent performing HIPAA Security Rule compliance, risk-analysis, and audit-readiness work for covered entities (CEs) and business associates (BAs). Follow every instruction below precisely. Use exact CFR citations (e.g., §164.308(a)(1)(ii)(A)) and exact (Required)/(Addressable) designations; never paraphrase a designation.

# HIPAA Security Rule Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent — see §11 Routing. The skill serves **both personas**: the auditee building risk analyses, addressable dispositions, and BAA checklists, and the auditor assessing OCR readiness and evidence sufficiency.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Conducting or reviewing a **risk analysis** under §164.308(a)(1)(ii)(A) — the anchor control and the most common OCR finding.
- Working **addressable-specification dispositions**: the §164.306(d)(3) assess → implement / document-why-not + equivalent-alternative workflow ("addressable does not mean optional").
- Mapping an organization's controls to the **22 Subpart C standards** (9 administrative / 4 physical / 5 technical / 2 organizational / 2 policies-and-documentation) and their implementation specifications.
- Checking a **business associate agreement (BAA)** against the required provisions of §164.314(a)(2)(i)(A)-(C) and §164.308(b)(3).
- Building an **OCR audit-readiness matrix**, gap list, or documentation-currency review for a CE or BA.
- **Right-sizing safeguards** for a small entity via the four §164.306(b)(2) flexibility factors (there is no small-entity exemption — only scaling).
- Assessing **recognized security practices** posture under PL 116-321 (mitigation consideration, not immunity) [PL-116-321].
- Explaining current enforcement exposure (penalty tiers, as adjusted under 45 CFR 102.3 [CFR-45-102]) or what the 2025 NPRM **proposes** (PROPOSED only — see `chunks/08-enforcement-audit-and-nprm.md`).

### Do NOT Use This Skill When:
- The question is about the **Privacy Rule** (Subpart E) or **Breach Notification Rule** (Subpart D) mechanics — this skill covers Subpart C (ePHI security) only; it touches §164.410 solely as a BAA-content requirement.
- The user needs **state law preemption analysis**, 42 CFR Part 2 (substance-use records), or the FTC Health Breach Notification Rule — out of scope.
- The user needs row-level **CSF/800-53 crosswalks** — this skill encodes no crosswalk rows; mappings live in the NIST CPRT per SP 800-66r2 Appendix D (see §7; completion tracked as SOX-638).
- The user needs NIST CSF maturity language for a board — use `nist-csf-2`; for 800-53 control detail — use `nist-800-53-rmf`.
- The user wants a legal opinion on liability, penalties, or settlement strategy — consult counsel. This skill encodes the regulation; it is not legal advice.

## 2. Framework Overview

The HIPAA Security Rule [CFR-45-164-Subpart-C] — 45 CFR Part 164, Subpart C, "Security Standards for the Protection of Electronic Protected Health Information" — requires covered entities **and business associates** (directly liable since the 2013 HITECH Omnibus Rule, 78 FR 5566) to protect the confidentiality, integrity, and availability of **ePHI** (electronic PHI only; the Privacy Rule covers PHI in all forms). The text in force was last substantively amended June 7, 2013 (78 FR 34266); no section has been amended since. HHS's practitioner landing page is [HIPAA-Security-Rule]; the current implementation guide is NIST SP 800-66 Rev 2 (Final, Feb. 14, 2024) [NIST-SP-800-66-Rev2]; HHS/ONC publish the Security Risk Assessment (SRA) Tool for small and medium entities [HHS-SRA-Tool]. A 2025 NPRM (90 FR 898) would significantly strengthen the rule but is **PROPOSED only as of 2026-06-10** [HIPAA-Security-NPRM-2025] — never present its content as current law.

| Layer | Element | Where |
|-------|---------|-------|
| Applicability + definitions | §164.302; §164.304 (17 defined terms) | `chunks/01` |
| General rules | §164.306: 4 general requirements, 4 flexibility factors, Required/Addressable logic, maintenance | `chunks/01` |
| Administrative safeguards | §164.308: 9 standards, 21 titled specs (10 R / 11 A) | `chunks/02`, `chunks/03` |
| Physical safeguards | §164.310: 4 standards, 8 titled specs (2 R / 6 A) | `chunks/04` |
| Technical safeguards | §164.312: 5 standards, 7 titled specs (2 R / 5 A) | `chunks/05` |
| Organizational requirements | §164.314: 2 standards (BAA content; group health plans) | `chunks/06` |
| Policies & documentation | §164.316: 2 standards, 3 Required documentation specs | `chunks/06` |
| Compliance dates (historical) | §164.318 (2005/2006) | `chunks/01` |
| Standards matrix | Appendix A to Subpart C | `chunks/01` |

**Counting conventions (always label which you use):** Subpart C has **22 standards** total. The Appendix A matrix covers §§164.308/310/312 only: **18 standards, 36 titled implementation specifications (14 Required / 22 Addressable)**. The widely cited "**42 implementation specifications (20 R / 22 A)**" uses the alternative convention of counting the 6 standards that have no separately titled specs as their own (R) matrix entries. Both are defensible; never mix them silently. See `chunks/01-scope-and-general-rules.md`.

## 3. Core Concepts

### 3.1 Required vs Addressable — §164.306(d)

- **(Required)** — must implement the specification. No flexibility about *whether*, only about *how* (per §164.306(b) flexibility of approach).
- **(Addressable)** — **NOT optional**. Per §164.306(d)(3): (i) assess whether the specification is a reasonable and appropriate safeguard in the entity's environment; then (ii) implement it if reasonable and appropriate, **or** document why it would not be reasonable and appropriate **and** implement an equivalent alternative measure if reasonable and appropriate. Every addressable specification ends in a documented disposition. Full workflow: `chunks/07-addressable-decisions-and-evidence.md`.

### 3.2 The four general requirements — §164.306(a)

Ensure confidentiality, integrity, and availability of all ePHI created, received, maintained, or transmitted; protect against reasonably anticipated threats or hazards; protect against reasonably anticipated impermissible uses or disclosures; ensure workforce compliance.

### 3.3 Flexibility of approach — §164.306(b)(2)

Four factors govern *how* (never *whether*) to implement: (i) size, complexity, and capabilities; (ii) technical infrastructure, hardware, and software security capabilities; (iii) costs of security measures; (iv) probability and criticality of potential risks to ePHI. This is the right-sizing lever for a 1-person BA and a 6,000-staff hospital alike.

### 3.4 Risk analysis as the anchor

§164.308(a)(1)(ii)(A) (Required) demands an "accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability" of ePHI. Everything downstream — addressable dispositions, safeguard selection, evaluation — cites the risk analysis. SP 800-66r2 [NIST-SP-800-66-Rev2] describes a cyclical risk-assessment/risk-management approach; the SRA Tool [HHS-SRA-Tool] operationalizes it for smaller entities. See `chunks/02-risk-analysis-and-management.md`.

### 3.5 Documentation discipline — §164.316

Policies and procedures in written (which may be electronic) form; documentation **retained 6 years** from creation or last-effective date, whichever is later (§164.316(b)(2)(i) — a retention floor, not a review cadence); available to responsible persons; reviewed "periodically" and updated as needed (§164.316(b)(2)(iii) — the rule states no cadence). See `chunks/06-organizational-and-documentation.md`.

## 4. Decision Logic (summary)

| User need | Route |
|-----------|-------|
| "Is this spec Required or Addressable?" / structure questions | `chunks/01` + family chunk (03/04/05) |
| Risk analysis scope, method, or review | `chunks/02` |
| "Can we skip an addressable spec?" / disposition records | `chunks/07` (grounded in §164.306(d)(3)) |
| BAA completeness / subcontractor flow-down / group health plan | `chunks/06` |
| OCR readiness, penalties, audit prep, "what may change" | `chunks/08` |
| Small-entity scaling | §164.306(b)(2) factors + `chunks/07`; never claim an exemption |
| CSF/800-53 mapping request | NIST CPRT pointer (§7); no rows encoded here |

Persona triage: an auditee asking "what do we have to do" starts at `chunks/02` then `chunks/07`; an auditor asking "what do I test" starts at `chunks/08` then the family chunks (03/04/05) for evidence expectations.

## 5. Procedure Templates (summary)

- **BA risk analysis + addressable dispositions** (40-FTE SaaS BA, all 22 addressable specs assessed) — `use-cases/uc-01-ba-risk-analysis.md`.
- **Hospital CE OCR-readiness assessment** (22-standard matrix, gap priorities, documentation currency) — `use-cases/uc-02-ocr-readiness.md`.
- **Solo-consultant BAA completeness + right-sized checklist** (§164.314(a)(2)(i) provision check, §164.306(b)(2) scaling) — `use-cases/uc-03-baa-and-checklist.md`.
- **Risk analysis procedure** (scope → inventory → threats/vulnerabilities → likelihood/impact → documentation) — `chunks/02 §Procedure`.
- **Addressable disposition workflow** — `chunks/07 §Procedure`.
- **OCR audit-readiness review** — `chunks/08 §Procedure`.

## 6. Output Templates (summary)

- **Risk register** (asset, threat, vulnerability, likelihood, impact, score, band — scoring scale is a labeled house convention) — `chunks/02 §Output template`.
- **Addressable disposition record** (spec_id, decision_required, reasonable_and_appropriate, alternative, alternative_considered, justification, disposition) — `chunks/07 §Output template`.
- **22-standard readiness matrix + prioritized gap list** — `chunks/08 §Output template`.
- **BAA provision checklist** (§164.314(a)(2)(i)(A)-(C) + §164.308(b)(3)) — `chunks/06 §Output template`.
- **Evidence catalog per safeguard family** — `chunks/07 §Evidence catalog`.

## 7. Cross-References (summary)

- `nist-csf-2` — executive maturity language; it defers its healthcare industry view to its v1.0 — when that view ships it will reference into this skill's chunks rather than restate Subpart C facts (one-way; facts live here).
- `nist-800-53-rmf` — control-catalog sibling. The authoritative Security Rule ↔ CSF ↔ 800-53 mapping was **removed from SP 800-66r2 and placed online in the NIST CPRT** (Appendix D) [NIST-SP-800-66-Rev2]; the CPRT mapping targets **CSF v1.1** and is "intentionally broad" — never claim a CSF 2.0 mapping. Row-level encoding is deferred (SOX-638); this skill ships zero crosswalk rows.
- `aicpa-soc-reporting` — SOC 2 evidence reuse for BAs: overlap, not equivalence (`chunks/07`).
- `audit-workpapers` — finding and evidence formats for readiness reviews.

External: HITECH Act (Pub. L. 111-5 §13401 — BA direct liability); PL 116-321 recognized security practices [PL-116-321]; 45 CFR Part 102 penalty adjustments [CFR-45-102]; OCR audit protocol (referenced in prose only; hhs.gov page is bot-walled to programmatic clients).

## 8. Worked Examples (summary)

Full worked examples live in `use-cases/`. Each has complete input, procedure, expected output, and oracle.

| UC | Title | Persona | Key output |
|----|-------|---------|------------|
| UC-01 | BA risk analysis & addressable dispositions — "CareSync Relay" (40-FTE health-tech SaaS BA) | auditee | Risk register rollup; one disposition per addressable spec; encryption-at-rest decision derived from facts |
| UC-02 | OCR-readiness assessment — "Bellbrook Regional Health" (6,000-staff hospital CE) | auditor | 22-row readiness matrix; prioritized gap list; documentation-currency flags |
| UC-03 | BAA + right-sized checklist — "Meridian HIT Consulting" (solo BA) | auditee | Missing-provision list; checklist with flexibility-factor rationale per scaled item |

## 9. Anti-Hallucination Disclaimers

- **Addressable never means optional.** The only correct gloss is the §164.306(d)(3) logic: assess; implement if reasonable and appropriate; else document why not and implement an equivalent alternative measure if reasonable and appropriate.
- **Count with a labeled convention.** Titled specs: 36 in the Appendix A matrix (14 R / 22 A); the "42 (20 R / 22 A)" figure counts the 6 no-spec standards as (R) entries. Subpart C has 22 standards total. Never mix conventions.
- **The 2025 NPRM is PROPOSED, not law** (90 FR 898, RIN 0945-AA22; verified at the Federal Register docket level 2026-06-10 — exactly one document, type "Proposed Rule") [HIPAA-Security-NPRM-2025]. NPRM content appears only in `chunks/08`, always flagged PROPOSED. Re-verify the docket before any enforcement-adjacent answer.
- **Penalty amounts adjust annually** under 45 CFR 102.3 [CFR-45-102]; cite them only with an as-of date (this skill pins the 2025-adjusted column, as of 2026-06-10, in `chunks/08` only). The 2019 Notification of Enforcement Discretion is enforcement posture, not codified law.
- **PL 116-321 was approved January 5, 2021 — not 2020.** SP 800-66r2 footnote 9 misdates it; cite the statute [PL-116-321].
- **6 years is documentation retention** (§164.316(b)(2)(i)), not a review cadence; §164.316(b)(2)(iii) says "periodically" with no stated interval. Any fixed review cycle in outputs is a house convention and must be labeled.
- **No crosswalk rows are encoded here.** Mappings live in the NIST CPRT (per SP 800-66r2 Appendix D); the mapping is to CSF v1.1 and intentionally broad. There is no official SP 800-66r2 mapping to CSF 2.0.
- **Cite SP 800-66 Rev 2 only** [NIST-SP-800-66-Rev2] — Rev 1 (2008) is superseded.
- **There is no small-entity exemption.** §164.306(b)(2) scales the *how*, never the *whether*; Required specs bind at every size.
- **Definitions in §164.304 are a closed list of 17** — "breach" and "unsecured PHI" are Subpart D (§164.402) terms, not Subpart C.

> This skill encodes the regulation and current guidance; it is not legal advice and not a substitute for professional judgment. Verify outputs against the cited sources.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| CFR-45-164-Subpart-C | Security Standards for the Protection of Electronic Protected Health Information (45 CFR Part 164, Subpart C) | eCFR (Office of the Federal Register) | 45 CFR §§ 164.302–164.318 and Appendix A | 2026-06-10 | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C |
| HIPAA-Security-NPRM-2025 | HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information (Proposed Rule) | HHS Office for Civil Rights / Federal Register | 90 FR 898; RIN 0945-AA22; PROPOSED, not final as of 2026-06-10 | 2026-06-10 | https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information |
| NIST-SP-800-66-Rev2 | Implementing the Health Insurance Portability and Accountability Act (HIPAA) Security Rule: A Cybersecurity Resource Guide | NIST | Rev 2 (Feb 2024) | 2026-05-25 | https://csrc.nist.gov/pubs/sp/800/66/r2/final |
| HIPAA-Security-Rule | HIPAA Security Rule guidance & combined regulation text portal | HHS | as amended | 2026-06-09 | https://www.hhs.gov/hipaa/for-professionals/security/ |
| HHS-SRA-Tool | Security Risk Assessment (SRA) Tool | HHS ONC / OCR (HealthIT.gov) | Current | 2026-06-10 | https://www.healthit.gov/privacy-security/security-risk-assessment-tool |
| PL-116-321 | An Act to amend the HITECH Act to require consideration of certain recognized security practices (HR 7898) | U.S. Government Publishing Office (govinfo) | Public Law 116-321, 134 Stat. 5072, approved Jan. 5, 2021; adds HITECH §13412 (42 U.S.C. 17941) | 2026-06-10 | https://www.govinfo.gov/content/pkg/PLAW-116publ321/html/PLAW-116publ321.htm |
| CFR-45-102 | Adjustment of Civil Monetary Penalties for Inflation (45 CFR Part 102) | eCFR (Office of the Federal Register) | 45 CFR § 102.3 Table 1 (HIPAA rows: 42 U.S.C. 1320d-5 / 45 CFR 160.404) | 2026-06-10 | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-102 |

In-body citations use the form `[LABEL §N]` and resolve to this manifest.

Note: hhs.gov URLs return 403 to programmatic clients (bot-wall; verified in-browser). The OCR audit protocol (also hhs.gov) is cited in prose only.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| Intent / trigger | File to load |
|------------------|--------------|
| "what does the Security Rule cover" / "who must comply" / "Required vs Addressable" / "flexibility factors" / "how many standards" / counting conventions | `chunks/01-scope-and-general-rules.md` |
| "risk analysis" / "risk assessment" / "risk management" / "sanction policy" / "activity review" / "SRA Tool" / "recognized security practices" | `chunks/02-risk-analysis-and-management.md` |
| "administrative safeguards" / "workforce security" / "training" / "incident procedures" / "contingency plan" / "evaluation" / "BA contracts standard" | `chunks/03-administrative-safeguards.md` |
| "physical safeguards" / "facility access" / "workstation" / "device and media" / "disposal" / "media re-use" | `chunks/04-physical-safeguards.md` |
| "technical safeguards" / "access control" / "encryption" / "audit controls" / "authentication" / "transmission security" | `chunks/05-technical-safeguards.md` |
| "BAA" / "business associate agreement" / "subcontractor flow-down" / "group health plan" / "documentation retention" / "6 years" / "policy updates" | `chunks/06-organizational-and-documentation.md` |
| "can we skip an addressable spec" / "disposition record" / "alternative measure" / "what evidence" / "auditee prep" | `chunks/07-addressable-decisions-and-evidence.md` |
| "OCR audit" / "penalties" / "fines" / "enforcement" / "readiness assessment" / "2025 NPRM" / "what may change" (PROPOSED) | `chunks/08-enforcement-audit-and-nprm.md` |
| Hospital / provider / clearinghouse CE context | `industries/healthcare.md` |
| Health-tech SaaS BA / cloud / subprocessor context | `industries/saas-technology.md` |
| Insurer / group health plan sponsor context | `industries/financial-services.md` |
| State Medicaid / public health agency / hybrid entity context | `industries/public-sector.md` |
| Worked example: BA risk analysis + dispositions | `use-cases/uc-01-ba-risk-analysis.md` |
| Worked example: hospital OCR readiness | `use-cases/uc-02-ocr-readiness.md` |
| Worked example: solo-consultant BAA + checklist | `use-cases/uc-03-baa-and-checklist.md` |
