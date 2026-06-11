---
name: pci-dss-assessment
description: "PCI DSS v4.0.1 (Payment Card Industry Data Security Standard, Requirements and Testing Procedures): 6 goals, 12 principal requirements, 63 sections, 249 main-body defined requirements, plus appendices A-G. Serves BOTH an auditee path (merchant/service-provider scoping, SAQ selection, self-assessment) and an assessor path (QSA/ISA workflow, ROC vs AOC, customized-approach and compensating-control validation). Use to scope a cardholder data environment (CDE), select among the 10 SAQ types, walk Requirements 1-12, distinguish the defined vs customized approach, build a compensating-control worksheet, or confirm v4.0.1 currency. Activate when the user says 'PCI DSS', 'PCI compliance', 'cardholder data', 'CDE', 'SAQ', 'ROC', 'AOC', 'QSA', 'network security controls', 'account data', 'segmentation', 'customized approach', or 'compensating control'."
category: audit-framework
risk: informational
source: "PCI DSS v4.0.1 (June 2024), Payment Card Industry Data Security Standard: Requirements and Testing Procedures — the only active version; v4.0 retired 2024-12-31; all future-dated requirements IN FORCE since 2025-03-31. Acquired via the PCI SSC document library under the Read-and-Copy License; the repo stores identifiers, counts, official titles, and original paraphrase only (no bulk standard text). SAQ catalog from the PCI SSC document library. Crosswalk anchor: NIST OLIR PCI-DSS-4.0.1-to-CSF-v2.0 (pointer only; no rows encoded)."
date_added: 2026-06-11
version: 0.1.0
status: draft
industries: [saas-technology, retail-ecommerce, financial-services, healthcare]
frameworks: [PCI-DSS-4.0.1]
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"
context_budget:
  always_loaded_tokens: 3500      # this SKILL.md (router)
  per_call_typical_tokens: 7000   # router + 1 chunk + 1 industry + 1 UC
  per_call_max_tokens: 16000      # router + all chunks + industry + UC
  per_call_p90_tokens: 9000       # estimate — no instrumented baseline yet
tags: [pci-dss, pci-dss-4-0-1, cardholder-data, account-data, chd, sad, cde, network-security-controls, scope, segmentation, saq, saq-a, saq-a-ep, roc, aoc, qsa, isa, defined-approach, customized-approach, targeted-risk-analysis, compensating-control, service-provider, merchant, client-side-script, retail-ecommerce, saas-technology]
---

You are an expert agent performing PCI DSS v4.0.1 scoping, SAQ-selection, self-assessment, and assessor-support work for merchants and service providers. Follow every instruction below precisely. Use exact requirement identifiers (e.g., Req 1, 6.4.3, A3.2.1), the 12 official requirement titles, and the exact SAQ names; never invent a requirement number or assert a transaction threshold as a PCI SSC rule.

# PCI DSS Assessment Skill (Router)

This `SKILL.md` is a **router**. The deep-dive content lives in `chunks/`. Load the chunks that match the user's intent — see §11 Routing. The skill serves **both personas**: the auditee scoping a CDE, picking a validation path, and self-assessing, and the assessor running a ROC, sampling, and validating customized approaches and compensating controls.

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- **Scoping a cardholder data environment (CDE)** — identifying system components that store, process, or transmit account data, plus connected-to and security-impacting systems, and using segmentation to reduce scope (the highest-leverage decision).
- **Selecting a validation path** — choosing among the **10 SAQ types** (A, A-EP, B, B-IP, C, C-VT, D-Merchant, D-Service-Provider, P2PE, SPoC) or determining that a full **ROC** is required.
- **Walking Requirements 1-12** — the 6 goals → 12 principal requirements → 63 sections structure, with paraphrased intent and evidence expectations.
- **Distinguishing the defined vs customized approach** (Appendix D; requires a Targeted Risk Analysis) from a **compensating control** (Appendix B/C; four-element worksheet) — the single most confused topic in v4.
- **Building an AOC / ROC / SAQ submission package** or a service-provider responsibility matrix.
- **Confirming v4.0.1 currency** — that v4.0.1 is the only active version and that all future-dated requirements are mandatory now (since 2025-03-31).

### Do NOT Use This Skill When:
- The user wants **merchant or service-provider validation levels** stated as standard facts — those are **brand-and-acquirer-defined and variable**, not PCI SSC rules. This skill names them only as brand-specific (see §9 and `chunks/08`).
- The user needs **sibling PCI standards** — PTS, the P2PE program internals, the Software Security Framework beyond the Appendix F pointer, or PIN security — out of scope.
- The user wants **card-brand compliance program** mechanics, fines, or penalty amounts — pointer only, no amounts.
- The user needs **row-level PCI↔CSF/800-53 crosswalks** — this skill encodes no crosswalk rows; the anchor is the NIST OLIR PCI-DSS-4.0.1-to-CSF-v2.0 reference (pointer only — see §7).
- The user wants a legal or contractual opinion — consult counsel. This skill encodes the standard and assessment workflow; it is not legal advice and does not simulate a QSA engagement.

## 2. Framework Overview

PCI DSS v4.0.1 [PCI-SSC-Document-Library] — "Payment Card Industry Data Security Standard: Requirements and Testing Procedures, Version 4.0.1, June 2024" — protects **account data** wherever it is stored, processed, or transmitted. It applies to merchants and service providers that handle payment-card account data. v4.0.1 is a **limited revision** of v4.0 with **no new or deleted requirements** [PCI-SSC-Blog-v401]; it is the **only active version** (v4.0 retired 2024-12-31). All **future-dated requirements are in force** (mandatory since 2025-03-31); the "best practice until 31 March 2025" phrasing in the printed text is historical — present those requirements as fully effective.

| Layer | Element | Where |
|-------|---------|-------|
| Applicability + account data | What PCI DSS covers; account data = CHD + SAD; the CDE; NSC terminology | `chunks/01` |
| Goals → requirements | 6 goals grouping the 12 principal requirements | `chunks/01` |
| Scoping & segmentation | CDE, connected-to/security-impacting systems, scope reduction | `chunks/02` |
| Validation-path selection | The 10 SAQ types and the SAQ-vs-ROC decision | `chunks/03` |
| Requirements 1-6 | Build/maintain secure networks (1-2), protect account data (3-4), vuln mgmt (5-6) | `chunks/04` |
| Requirements 7-12 | Access control (7-9), monitor/test (10-11), policy/programs (12) | `chunks/05` |
| Validation deliverables | ROC vs AOC vs SAQ; QSA/ISA roles; sampling; responsibility matrix | `chunks/06` |
| Approaches | Defined vs customized (App D); compensating controls (App B/C) | `chunks/07` |
| Currency & program context | v4.0.1 currency; appendices A1/A2/A3; brand programs; crosswalk pointer | `chunks/08` |

**Counting conventions (always label which you use):** v4.0.1's main body has **6 goals**, **12 principal requirements**, **63 sections** (x.y headings; per requirement 5/3/7/2/4/5/3/6/5/7/6/10 across Req 1-12), and **249 main-body defined requirements** (numbered x.y.z and x.y.z.w rows — **205 at depth-3 plus 44 at depth-4**; testing procedures, which carry letter suffixes, are excluded). **Appendix A** adds **30 requirements** across 8 sections (A1 multi-tenant / A2 SSL-early-TLS POS POI / A3 DESV). There are **10 SAQ types** and lettered **appendices A-G**. Secondary sources cite various bare totals; this skill states counts only with these conventions and never asserts a bare requirement total. See `chunks/01-scope-and-applicability.md`.

## 3. Core Concepts

### 3.1 Account data = cardholder data + sensitive authentication data
Req 3 is "Protect Stored Account Data" — renamed in v4 from "cardholder data". **Account data** comprises **cardholder data (CHD)** and **sensitive authentication data (SAD)**. The CHD primary account number (PAN) is the anchor data element; SAD (e.g., full track data, card verification code, PIN/PIN block) must never be stored after authorization. The **CDE** is the people, processes, and technology that store, process, or transmit account data, plus connected-to and security-impacting systems. **PAN never appears in this skill's examples** — that is a teaching point, not just hygiene. See `chunks/01`.

### 3.2 Network security controls (NSCs) — Req 1
Req 1 is "Install and Maintain Network Security Controls" — **do not call it "the firewall requirement"**. v4 generalized "firewalls and routers" to NSCs, which include firewalls, but also cloud security groups, virtual NSCs, and other controls that govern network traffic between segments. See `chunks/04`.

### 3.3 Scope is the highest-leverage decision
Everything downstream — which requirements apply, which SAQ fits, assessment effort — flows from scope. **Segmentation** isolates the CDE so that out-of-scope systems are demonstrably unable to affect CDE security; effective, validated segmentation reduces the in-scope system count and therefore the assessment burden. See `chunks/02`.

### 3.4 Defined vs customized approach — and compensating controls
- **Defined approach** — meet the requirement as written, validated by the stated testing procedures.
- **Customized approach** (Appendix D/E) — meet the requirement's **objective** by a different method; **requires a Targeted Risk Analysis (TRA)**. Some requirements have **no customized-approach option**.
- **Compensating control** (Appendix B/C) — for an **existing defined requirement** an entity **cannot meet** due to a **legitimate constraint**; documented via the **four worksheet elements** (constraints / objective / risk / controls-in-place). These are **distinct**: customized = meet the objective differently by design; compensating = a fallback for a requirement you cannot meet. See `chunks/07`.

### 3.5 Validation levels are brand-defined, not PCI SSC facts
Merchant and service-provider "levels" (L1/L2/etc.) and any transaction thresholds are defined by the **payment brands and acquirers**, not by PCI SSC or the standard, and they **vary**. Never assert a level threshold as an SSC rule. See `chunks/08` and §9.

## 4. Decision Logic (summary)

| User need | Route |
|-----------|-------|
| "What does PCI DSS apply to?" / account data / CDE / NSC / counts | `chunks/01` |
| "What's in scope?" / segmentation / connected-to systems | `chunks/02` |
| "Which SAQ do I use?" / SAQ vs ROC / A vs A-EP | `chunks/03` |
| Requirement detail for Req 1-6 / Req 7-12 | `chunks/04` / `chunks/05` |
| ROC vs AOC vs SAQ / QSA-ISA roles / sampling / responsibility matrix | `chunks/06` |
| "Can we meet this differently?" / customized vs compensating / TRA / worksheet | `chunks/07` |
| "Is v4.0.1 current?" / future-dated reqs / brand levels / crosswalk | `chunks/08` |
| PCI↔CSF/800-53 mapping request | OLIR pointer (§7); no rows encoded here |

**House conventions (engagement-decision logic, not verbatim standard text):** the SAQ-selection heuristic in `chunks/03` and the scope in/out rule in `chunks/02` are this skill's decision logic for **applying** the SAQ eligibility conditions and scoping rules — they are labeled as such, never attributed as standard text. Persona triage: an auditee asking "what must we do" starts at `chunks/02` then `chunks/03`; an assessor asking "what do I validate" starts at `chunks/06` then `chunks/07`.

## 5. Procedure Templates (summary)

- **SAQ-eligibility selection** (page-architecture facts → A / A-EP / ROC + client-side-script flags) — `use-cases/uc-01-saq-selection.md`, `chunks/03 §Procedure`.
- **CDE scope determination + segmentation effect** (system inventory tagged cde/connected/out → in-scope count) — `use-cases/uc-02-roc-segmentation.md`, `chunks/02 §Procedure`.
- **Compensating-control worksheet** (four Appendix-C elements; customized-vs-compensating classification) — `use-cases/uc-03-compensating-control.md`, `chunks/07 §Procedure`.
- **ROC / AOC assembly** (assessor sampling, responsibility matrix, AOC parts) — `chunks/06 §Procedure`.
- **Targeted Risk Analysis for a customized approach** — `chunks/07 §Procedure`.

## 6. Output Templates (summary)

- **SAQ-eligibility determination** (deciding factor + applicable client-side-script requirements 6.4.3 / 11.6.1) — `chunks/03 §Output template`.
- **Scope inventory** (system, scope_tag, in/out, in-scope count, segmentation note) — `chunks/02 §Output template`.
- **Compensating-control worksheet** (constraints / objective / risk / controls-in-place — exactly four elements) — `chunks/07 §Output template`.
- **Customized-approach record** (requirement, objective, method, TRA reference) — `chunks/07 §Output template`.
- **Requirement-coverage matrix** (section → applicable? → evidence) — `chunks/04` / `chunks/05 §Output template`.

## 7. Cross-References (summary)

- `nist-csf-2` / `nist-800-53-rmf` — PCI↔CSF/800-53 mapping is a **one-way pointer**. The authoritative anchor is the NIST OLIR **PCI-DSS-4.0.1-to-CSF-v2.0** final informative reference (PCI SSC-submitted) [NIST-OLIR], discoverable via the NIST CSF informative-references catalog [NIST-CSF-Informative-References]. This skill encodes **zero crosswalk rows**; row-level extraction is a later ticket.
- `hipaa-security-rule` — healthcare merchants that take card payments face both regimes (different data, same vendor-management discipline); see `industries/healthcare.md` (one-way reference).
- `aicpa-soc-reporting` — a SaaS provider may issue a SOC 2 plus a PCI AOC; overlap, not equivalence (`industries/saas-technology.md`).

External: the PCI SSC document library [PCI-SSC-Document-Library] is the source for the standard, SAQs, and ROC/AOC templates; the v4.0.1 announcement [PCI-SSC-Blog-v401] confirms the limited-revision nature.

## 8. Worked Examples (summary)

Full worked examples live in `use-cases/`. Each has complete input, procedure, expected output, and a derivability oracle (the outcome is recomputed from seed facts — never a hardcoded verdict).

| UC | Title | Persona | Key output |
|----|-------|---------|------------|
| UC-01 | E-commerce SaaS SAQ selection — "CartNimbus" (~2M txns, merchant) | auditee | SAQ A-EP (merchant scripts on the page, servers never touch PAN); 6.4.3 / 11.6.1 apply |
| UC-02 | Retail full-ROC scoping + customized approach — "Ironvale Retail" (~8M txns) | assessor | In-scope system count from cde+connected tags; 8.3.6 customized approach accepted with a TRA |
| UC-03 | Franchise SAQ-D compensating control — "Meridian QSA-Support" (solo, 30 sites) | assessor-support | Four-element worksheet complete; classified compensating-control (constraint-driven), not customized |

## 9. Anti-Hallucination Disclaimers

- **Future-dated requirements are mandatory now.** Every requirement once marked "best practice until 31 March 2025" has been **in force since 2025-03-31**. Never present any of them as optional, upcoming, or a future best practice. (33 such markers exist in the v4.0.1 text — all effective.)
- **Validation levels are brand-defined.** L1/L2/etc. and transaction thresholds come from the **payment brands and acquirers**, not PCI SSC; they vary. Never state a level threshold as an SSC fact. To a "what level am I" question, answer that levels are brand/acquirer-defined and point to the merchant's acquirer.
- **Req 1 is network security controls (NSCs), not "the firewall requirement."** Req 3 protects **account data (CHD + SAD)** — renamed from "cardholder data" in v4.
- **No PAN in examples.** Full PAN is never shown in this skill's examples or outputs — model this as a teaching point.
- **Count with a labeled convention.** 6 goals / 12 principal requirements / 63 sections / 249 main-body defined requirements (205 depth-3 + 44 depth-4) / 30 Appendix-A requirements / 10 SAQ types / appendices A-G. Never assert a bare requirement total.
- **SAQ eligibility is derived, not assumed.** It follows from the payment-page architecture and entity role (service provider → ROC; merchant servers touch PAN → ROC; fully outsourced redirect/iframe with no merchant script → SAQ A; merchant controls scripts but servers never receive PAN → SAQ A-EP). If a deciding architecture fact is missing, ask for it rather than guessing.
- **Customized ≠ compensating.** Customized approach (App D) meets the objective differently and needs a TRA; a compensating control (App B/C) is a fallback for an existing requirement an entity cannot meet due to a legitimate constraint, with the four worksheet elements. Some requirements have no customized-approach option.
- **No crosswalk rows are encoded here.** The PCI↔CSF mapping anchor is the NIST OLIR reference [NIST-OLIR]; this skill ships zero rows.
- **v4.0.1 is the only active version** (v4.0 retired 2024-12-31); no successor announced as of 2026-06-11. Re-verify currency before any version-sensitive answer.

> This skill encodes the standard and assessment workflow; it is not legal advice, not a card-brand compliance determination, and not a substitute for a QSA engagement. Verify outputs against the cited sources.

## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| PCI-SSC-Document-Library | PCI SSC Document Library | PCI Security Standards Council | PCI DSS v4.0.1 (June 2024) and supporting documents (SAQs, ROC/AOC templates) | 2026-06-11 | https://www.pcisecuritystandards.org/document_library/ |
| PCI-SSC-Blog-v401 | Just Published: PCI DSS v4.0.1 | PCI Security Standards Council | v4.0.1 limited revision announcement (no new or deleted requirements) | 2026-06-11 | https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 |
| NIST-CSF-Informative-References | NIST CSF 2.0 Informative References spreadsheet (crosswalk source of truth) | NIST | 2024 (OLIR catalog) | 2026-06-11 | https://www.nist.gov/cyberframework/informative-references |
| NIST-OLIR | OLIR (Online Informative References) Program | NIST | PCI-DSS-4.0.1-to-CSF-v2.0 final informative reference | 2026-06-11 | https://csrc.nist.gov/projects/olir |

In-body citations use the form `[LABEL]` and resolve to this manifest. Deep PDF links require the PCI SSC click-through licence acceptance per session — the manifest cites the document-library page, never a deep PDF link.

## 11. Routing

This is a router. Load chunks based on the user's intent.

| Intent / trigger | File to load |
|------------------|--------------|
| "what does PCI DSS apply to" / "account data" / "CDE" / "NSC vs firewall" / "6 goals" / "how many requirements" / counting conventions | `chunks/01-scope-and-applicability.md` |
| "what's in scope" / "segmentation" / "connected-to systems" / "reduce scope" / "sampling scope" | `chunks/02-scoping-and-segmentation.md` |
| "which SAQ" / "SAQ A vs A-EP" / "SAQ vs ROC" / "eligibility" / "client-side scripts" / "6.4.3" / "11.6.1" | `chunks/03-saq-selection.md` |
| "Requirement 1-6" / NSCs / secure config / protect stored data / transmission crypto / malware / secure software | `chunks/04-requirements-1-6.md` |
| "Requirement 7-12" / access control / MFA / physical access / logging / scanning / pen test / policy & programs | `chunks/05-requirements-7-12.md` |
| "ROC" / "AOC" / "QSA" / "ISA" / "validation" / "responsibility matrix" / "assessor sampling" | `chunks/06-validation-roc-aoc.md` |
| "customized approach" / "defined approach" / "TRA" / "compensating control" / "worksheet" / "Appendix B/C/D" | `chunks/07-approaches-and-compensating-controls.md` |
| "is v4.0.1 current" / "future-dated requirements" / "what level am I" (brand) / "DESV" / "A1/A2/A3" / "CSF mapping" | `chunks/08-currency-and-program-context.md` |
| E-commerce / SaaS merchant or service-provider context | `industries/saas-technology.md` |
| Card-present + e-commerce retail / POS / multi-site context | `industries/retail-ecommerce.md` |
| Acquirer / processor / larger service-provider / DESV context | `industries/financial-services.md` |
| Healthcare provider taking card payments context | `industries/healthcare.md` |
| Worked example: e-commerce SAQ selection | `use-cases/uc-01-saq-selection.md` |
| Worked example: retail full-ROC scoping + segmentation | `use-cases/uc-02-roc-segmentation.md` |
| Worked example: franchise compensating-control worksheet | `use-cases/uc-03-compensating-control.md` |
