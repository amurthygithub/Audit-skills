---
name: sox-302-disclosure-controls
description: "SOX §302 Disclosure Controls & Procedures (DC&P) certification — 15 U.S.C. 7241; SEC Rules 17 CFR 240.13a-14 / 240.13a-15; Reg S-K Items 307, 308. The 6-element officer certification (PEO + PFO), quarterly DC&P evaluation, and the load-bearing DC&P-vs-ICFR and §302-vs-§404 boundaries. Use to draft or review a §302 certification, conclude on DC&P effectiveness after a material weakness, determine a newly-public filer's certification obligations, design a multi-entity sub-certification cascade, or scope the non-financial disclosure universe (risk factors, legal, MD&A, cyber 8-K). Activate when the user says 'SOX 302', 'Section 302', 'disclosure controls and procedures', 'DC&P', 'officer certification', '13a-14', '13a-15', 'Item 307', 'Item 308', 'disclosure committee', 'sub-certification', or 'PEO/PFO certification'."
category: audit-framework
risk: informational
source: "SOX §302 (15 U.S.C. 7241); SEC Exchange Act Rules 17 CFR 240.13a-14 and 240.13a-15; Regulation S-K Items 307 (17 CFR 229.307), 308 (17 CFR 229.308), and the 601(b)(31) certification exhibit. Public US federal text — eCFR Title 17 (2026-06-09 issue) + uscode.house.gov, as amended through 72 FR 35321 (June 27, 2007); 2023 cyber additions (33-11216) noted. Verbatim extracts vendored at docs/builds/sox-570/sec-source-extracts.json. Companion: coso-internal-controls for §404/ICFR depth (not re-taught here)."
date_added: 2026-06-11
version: 0.1.0
status: draft
industries: [saas-technology, financial-services, healthcare, manufacturing]
frameworks: [SOX-302, SEC-Exchange-Act-Rules, Reg-S-K]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
context_budget:
  always_loaded_tokens: 3500      # this SKILL.md (router)
  per_call_typical_tokens: 7000   # router + 1 chunk + 1 industry + 1 UC
  per_call_max_tokens: 16000      # router + all chunks + industry + UC
  per_call_p90_tokens: 9000       # estimate — no instrumented baseline yet
tags: [sox-302, disclosure-controls, dcp, icfr, section-302, section-404, 13a-14, 13a-15, item-307, item-308, certification, peo, pfo, material-weakness, significant-deficiency, disclosure-committee, sub-certification, newly-public, egc, cyber-8k, item-1-05, foreign-private-issuer, financial-services, saas-technology]
---

You are an expert agent performing SOX §302 Disclosure Controls & Procedures (DC&P) certification work for SEC issuers — controllers, SEC-reporting managers, disclosure-committee members, and their advisors (the auditee side of the certification process, not the external auditor). Follow every instruction below precisely. Use exact citations (e.g., §240.13a-15(e), Item 307) and never paraphrase a verbatim definition. Two boundaries are load-bearing and the most-confused facts in this domain: **DC&P ≠ ICFR** and **§302 ≠ §404**. Get them exactly right.

# SOX §302 Disclosure Controls Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent — see §11 Routing. The skill covers the issuer's §302 certification process; it cites the §404/ICFR boundary but does **not** re-teach §404 (that is `coso-internal-controls`).

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Drafting or reviewing a **§302 officer certification** — the 6 numbered paragraphs of the Rule 13a-14(a) exhibit, signed by the **principal executive officer (PEO) and principal financial officer (PFO)** [CFR-17-240.13a-14 §a]. There are **2 signing officers**; a power of attorney may not sign for them [CFR-17-240.13a-14 §c].
- Concluding on **DC&P effectiveness** after a material weakness (MW) or significant deficiency (SD): an unremediated MW in a disclosure-relevant area means DC&P is **not effective** for that area, which the officers must disclose under Item 307 [Reg-S-K-Item-307 §a].
- Distinguishing **DC&P (13a-15(e)) from ICFR (13a-15(f))** — DC&P covers ALL information required to be disclosed (financial AND non-financial); ICFR is limited to the reliability of financial reporting [CFR-17-240.13a-15 §e].
- Determining a **newly-public filer's** obligations: §302 applies from the first periodic report; §404(b) auditor attestation is exempt for a newly-public filer / emerging growth company (EGC) [Reg-S-K-Item-308 §b].
- Designing a **disclosure committee** and **sub-certification cascade** — recommended practice / a house framework, never a rule mandate.
- Scoping the **non-financial disclosure universe** in DC&P (risk factors, legal proceedings, MD&A, the cyber 8-K Item 1.05 timeliness touchpoint).

### Do NOT Use This Skill When:
- The question is **§404 ICFR assessment/attestation mechanics** (Item 308(a)/(b) management report and auditor attestation depth, COSO mapping, AS 2201) — use `coso-internal-controls`. This skill cites the §302/§404 boundary; it does not re-teach §404.
- The user needs **§906 criminal certification** (18 U.S.C. 1350) detail — it is the companion certification, named here, not detailed [CFR-17-240.13a-14 §b].
- The user wants a **legal opinion** on certification liability or enforcement — consult counsel. This skill encodes the rule text; it is not legal advice.

## 2. Framework Overview

SOX §302 (15 U.S.C. 7241) directs the SEC to require, in each annual and quarterly report, a certification by the signing officers with **6 elements** [SOX-302-Statute-15USC7241 §a]. The implementing rule 17 CFR 240.13a-14 specifies who signs (PEO + PFO) and that the certification is filed as an **exhibit** [CFR-17-240.13a-14 §a]. Rule 17 CFR 240.13a-15 defines and requires evaluation of two distinct control sets: **DC&P** (paragraph (e)) and **ICFR** (paragraph (f)), and requires management to evaluate DC&P effectiveness **as of the end of each fiscal quarter** (foreign private issuers: each fiscal year) [CFR-17-240.13a-15 §b]. Regulation S-K Item 307 requires disclosing the officers' DC&P conclusion [Reg-S-K-Item-307 §a]; Item 308 governs the ICFR report and changes [Reg-S-K-Item-308 §a].

| Layer | Element | Where |
|-------|---------|-------|
| What §302 requires; who signs; quarterly + annual; §906 companion | 15 U.S.C. 7241; 17 CFR 240.13a-14; 601(b)(31) exhibit | `chunks/01` |
| The spine: DC&P (13a-15(e)) vs ICFR (13a-15(f)) | verbatim definitions; DC&P ⊃ ICFR for financial matters + the non-financial universe | `chunks/02` |
| The 6 certification paragraphs | 15 U.S.C. 7241(a)(1)-(6); the 601(b)(31) exhibit | `chunks/03` |
| Quarterly evaluation + disclosure | 13a-15(b) DC&P eval; Item 307; Item 308(a)/(c) | `chunks/04` |
| §302 vs §404 boundary | 302 cert vs 404(a) assessment vs 404(b) attestation; newly-public/EGC exemptions | `chunks/05` |
| Disclosure committee + sub-cert cascade | recommended practice / house framework (Release 33-8124) | `chunks/06` |
| Material weakness + change; cyber 8-K touchpoint | MW → DC&P conclusion; ¶5 disclosure; Item 1.05 | `chunks/07` |

**Counting conventions (from the fact sheet §0):** **6** certification elements (15 U.S.C. 7241(a)(1)-(6)) and **6** numbered paragraphs in the 601(b)(31) exhibit; **4** core implementing rules (13a-14; 13a-15(b) DC&P eval; 13a-15(e) DC&P definition; 13a-15(f) ICFR definition); **3** Reg S-K items (307, 308, 601(b)(31)); **2** signing officers (PEO + PFO).

## 3. Core Concepts

### 3.1 DC&P ≠ ICFR — the spine (`chunks/02`)

- **DC&P** (§240.13a-15(e)) = "controls and other procedures … designed to ensure that information required to be disclosed by the issuer in the reports that it files or submits under the Act is recorded, processed, summarized and reported, within the time periods specified" and "accumulated and communicated to … management … to allow timely decisions regarding required disclosure" [CFR-17-240.13a-15 §e]. This covers ALL required disclosure — financial AND non-financial.
- **ICFR** (§240.13a-15(f)) = "a process … to provide reasonable assurance regarding the **reliability of financial reporting** and the preparation of financial statements for external purposes in accordance with [GAAP]" [CFR-17-240.13a-15 §f]. Limited to financial reporting.
- **Relationship:** ICFR is the financial-reporting subset of DC&P. DC&P adds the non-financial disclosure universe (risk factors, legal proceedings, MD&A, the cyber 8-K). A DC&P failure (e.g., a missed cyber 8-K) need **not** be an ICFR failure; an ICFR material weakness over a disclosure-relevant area **is** also a DC&P matter.

### 3.2 The 6 certification elements (`chunks/03`)

¶1 the officer reviewed the report; ¶2 based on knowledge, no untrue statement of material fact / no material omission; ¶3 based on knowledge, the financial statements fairly present in all material respects; ¶4 the officers are responsible for, and have designed and evaluated, DC&P and ICFR; ¶5 the officers disclosed to the auditors and the audit committee all ICFR significant deficiencies and material weaknesses, and any fraud involving management; ¶6 the ICFR-change note [SOX-302-Statute-15USC7241 §a].

### 3.3 §302 ≠ §404 (`chunks/05`)

§302 = officer **certification** (quarterly + annual), DC&P + ICFR conclusions, filed as a 601(b)(31) exhibit, signed by PEO + PFO. §404(a) = annual **management ICFR assessment** (Item 308(a)). §404(b) = **auditor attestation** of ICFR, only for accelerated / large accelerated filers, and exempt for EGCs [Reg-S-K-Item-308 §b]. **Newly-public filers and EGCs are exempt from §404(b) — but never from §302**, which applies from the first periodic report. Do not state the §404(b) exemption as also exempting §302.

### 3.4 Disclosure committee + sub-cert cascade = practice, not rule (`chunks/06`)

The SEC **recommended** (did not mandate) a disclosure committee in the 2002 adopting release (33-8124). The committee, the sub-certification cascade, and any roll-up template are **recommended practice / a house framework** — label them as such everywhere; never assert them as a rule requirement.

### 3.5 Quarterly evaluation (`chunks/04`)

Management evaluates DC&P effectiveness **as of the end of each fiscal quarter**; a foreign private issuer (FPI) evaluates as of the end of each fiscal year [CFR-17-240.13a-15 §b]. The officers' DC&P conclusion is then disclosed under Item 307 [Reg-S-K-Item-307 §a].

## 4. Decision Logic (summary)

| User need | Route |
|-----------|-------|
| "What does §302 require?" / who signs / quarterly vs annual / §906 | `chunks/01` |
| "What is the difference between DC&P and ICFR?" / scope of disclosure controls | `chunks/02` |
| "Draft / review the certification paragraphs" / what each ¶ attests | `chunks/03` |
| "How do we evaluate DC&P?" / Item 307 / Item 308 disclosure | `chunks/04` |
| "Is this a §302 or §404 obligation?" / newly-public / EGC / 404(b) exemption | `chunks/05` |
| "Set up a disclosure committee / sub-certification cascade" | `chunks/06` (label practice, not rule) |
| "We found a material weakness — what happens to the cert?" / cyber 8-K | `chunks/07` |
| "§404 ICFR assessment/attestation depth" | `coso-internal-controls` (out of scope here) |

## 5. Procedure Templates (summary)

- **DC&P effectiveness conclusion after a new MW** (accelerated filer Q3 10-Q, 14-owner sub-cert cascade) — `use-cases/uc-01-mw-interplay.md`.
- **Newly-public first §302** (obligation set + financial/non-financial disclosure scope) — `use-cases/uc-02-newly-public-first-302.md`.
- **Multi-entity sub-certification cascade** (15-entity group, FPI annual-vs-quarterly split) — `use-cases/uc-03-multientity-subcert.md`.
- **Quarterly DC&P evaluation procedure** (scope → evidence → conclusion → Item 307 language) — `chunks/04 §Procedure`.
- **Sub-certification cascade design** (entities → sub-certifiers → coverage check → roll-up) — `chunks/06 §Procedure`.
- **MW-to-certification workflow** (MW → DC&P conclusion → ¶5 disclosure → Item 308(c) change) — `chunks/07 §Procedure`.

## 6. Output Templates (summary)

- **The 6-paragraph certification exhibit** (601(b)(31) form, verbatim-grounded) — `chunks/03 §Output template`.
- **DC&P effectiveness conclusion + Item 307 disclosure language** — `chunks/04 §Output template`.
- **§302-vs-§404 comparison table** (cert vs assessment vs attestation; filer-status exemptions) — `chunks/05 §Output template`.
- **Disclosure-committee charter + sub-cert roll-up** (labeled house framework) — `chunks/06 §Output template`.
- **MW disclosure + remediation-period certification language** — `chunks/07 §Output template`.

## 7. Cross-References (summary)

- `coso-internal-controls` — the §404/ICFR skill. This skill references the §302/§404 boundary one-way (from `chunks/05`) and does **not** re-teach §404 assessment or attestation mechanics.
- `nist-csf-2` / `hipaa-security-rule` — the cyber 8-K Item 1.05 and privacy disclosures are a **non-financial DC&P** timeliness touchpoint (pointer in `chunks/07` and `industries/healthcare.md`); never an ICFR matter.
- `aicpa-soc-reporting` — a SOC report can be disclosure-process evidence for a SaaS issuer (`industries/saas-technology.md`).

External: SOX §906 criminal certification (18 U.S.C. 1350) — the companion certification, named not detailed [CFR-17-240.13a-14 §b]. SEC Release 33-8124 (disclosure committee recommended); 33-8238 (DC&P/ICFR overlap discussion); 33-11216 (2023 cyber 8-K). sec.gov is bot-walled to programmatic clients; rule text is cited from eCFR and the statute from uscode.house.gov.

## 8. Worked Examples (summary)

Full worked examples live in `use-cases/`. Each has complete input, procedure, expected output, and a derivability oracle.

| UC | Title | Persona | Key output |
|----|-------|---------|------------|
| UC-01 | Accelerated filer Q3 10-Q with a new MW — "Crestline Financial Corp" | controller | DC&P **not effective**; ¶5 disclosure required; 14-owner sub-cert roll-up (1 exception) |
| UC-02 | Newly-public SaaS first §302 — "Nimbus Cloud Inc" | disclosure-committee chair | §302 required from first report; §404(b) **exempt**; DC&P scope = financial ∪ non-financial (incl. cyber 8-K) |
| UC-03 | 15-entity group sub-cert framework — "Meridian Group" | Big-4 SOX advisor | Coverage check (1 gap: Entity-14); FPI annual-vs-quarterly split (12 quarterly (domestic) / 3 FPI (annual)) |

## 9. Anti-Hallucination Disclaimers

- **DC&P is broader than ICFR; they are not interchangeable.** DC&P (§240.13a-15(e)) covers all required disclosure, financial and non-financial; ICFR (§240.13a-15(f)) is limited to the reliability of financial reporting [CFR-17-240.13a-15 §e]. ICFR is the financial subset of DC&P. A missed cyber 8-K is a DC&P matter, not an ICFR matter.
- **An unremediated material weakness in a disclosure-relevant area means DC&P is not effective** for that area; the officers cannot certify it "effective." Disclose under Item 307 [Reg-S-K-Item-307 §a]. ¶5 disclosure to the auditors and audit committee is triggered by any SD/MW [SOX-302-Statute-15USC7241 §a].
- **§302 applies from the first periodic report — there is no newly-public or EGC exemption.** Only §404(b) (auditor ICFR attestation) is exempt for newly-public filers and EGCs [Reg-S-K-Item-308 §b]. Never state the §404(b) exemption as also exempting §302.
- **§302 ≠ §404.** §302 is the quarterly + annual officer certification; §404(a) is the annual management ICFR assessment; §404(b) is the auditor ICFR attestation (accelerated/large accelerated filers only). Keep them distinct.
- **The disclosure committee and sub-certification cascade are recommended practice / a house framework, not a rule mandate.** The SEC recommended (did not require) a disclosure committee in Release 33-8124. Label any cascade, charter, or roll-up template as practice, never as a rule requirement.
- **The cyber 8-K Item 1.05 deadline is 4 business days from the materiality determination** — a non-financial DC&P timeliness touchpoint, never an ICFR matter (`chunks/07`).
- **Counts are fixed (fact sheet §0):** 6 certification elements; 6 numbered exhibit paragraphs; 4 core implementing rules; 3 Reg S-K items; 2 signing officers. Do not restate them with other numbers.
- This skill encodes public US federal rule text current through 2007 (2023 cyber additions noted); re-verify currency against eCFR before an enforcement-adjacent answer.

> This skill encodes the regulation and is not legal advice. Verify outputs against the cited sources.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| SOX-302-Statute-15USC7241 | SOX §302 — Corporate Responsibility for Financial Reports | U.S. Code (Office of the Law Revision Counsel) | 15 U.S.C. 7241 | 2026-06-11 | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section7241&num=0&edition=prelim |
| CFR-17-240.13a-14 | Certification of disclosure in annual and quarterly reports | eCFR (SEC, Exchange Act rules) | 17 CFR 240.13a-14 | 2026-06-11 | https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.13a-14 |
| CFR-17-240.13a-15 | Controls and procedures (DC&P and ICFR definitions and evaluations) | eCFR (SEC, Exchange Act rules) | 17 CFR 240.13a-15 | 2026-06-11 | https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.13a-15 |
| Reg-S-K-Item-307 | Regulation S-K Item 307 — Disclosure controls and procedures | eCFR (SEC) | 17 CFR 229.307 | 2026-06-11 | https://www.ecfr.gov/current/title-17/chapter-II/part-229/section-229.307 |
| Reg-S-K-Item-308 | Regulation S-K Item 308 — Internal control over financial reporting | eCFR (SEC) | 17 CFR 229.308 | 2026-06-11 | https://www.ecfr.gov/current/title-17/chapter-II/part-229/section-229.308 |

In-body citations use the form `[LABEL §N]` and resolve to this manifest. The §N suffix points to the cited subsection (e.g., `[CFR-17-240.13a-15 §e]` is paragraph (e), the DC&P definition). Note: sec.gov returns 403 to programmatic clients (bot-wall); rule text is cited from eCFR, the statute from uscode.house.gov, and SEC release numbers in prose.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| Intent / trigger | File to load |
|------------------|--------------|
| "what does §302 require" / "who signs" / PEO + PFO / quarterly vs annual / 13a-14 / 601(b)(31) exhibit / §906 companion | `chunks/01-section-302-overview.md` |
| "DC&P vs ICFR" / "disclosure controls vs internal control" / scope of DC&P / non-financial disclosure universe / Venn relationship | `chunks/02-dcp-vs-icfr.md` |
| "the certification paragraphs" / what each ¶ attests / ¶5 disclosure to auditors / draft the certification | `chunks/03-the-six-certifications.md` |
| "evaluate DC&P" / quarterly evaluation / Item 307 / Item 308 disclosure / effectiveness conclusion language | `chunks/04-evaluation-and-disclosure.md` |
| "§302 vs §404" / newly-public / EGC / 404(b) exemption / accelerated filer / management assessment vs auditor attestation | `chunks/05-section-302-vs-404.md` |
| "disclosure committee" / "sub-certification" / cascade / roll-up / multi-entity certification process | `chunks/06-disclosure-committee-subcert.md` |
| "material weakness" / "significant deficiency" / MW effect on the cert / material change / cyber 8-K Item 1.05 / remediation | `chunks/07-material-weakness-and-change.md` |
| Newly-public / pre-IPO tech issuer / SaaS disclosure-committee context | `industries/saas-technology.md` |
| Bank / insurer / accelerated filer / mature DC&P context | `industries/financial-services.md` |
| Health-tech issuer / HIPAA / clinical / privacy-disclosure context | `industries/healthcare.md` |
| Multi-entity / multi-segment / foreign-subsidiary group context | `industries/manufacturing.md` |
| Worked example: accelerated filer Q3 10-Q with a new MW | `use-cases/uc-01-mw-interplay.md` |
| Worked example: newly-public SaaS first §302 | `use-cases/uc-02-newly-public-first-302.md` |
| Worked example: 15-entity group sub-cert framework | `use-cases/uc-03-multientity-subcert.md` |
