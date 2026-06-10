---
uc_id: UC-02
title: "Hospital CE runs an OCR-readiness assessment: 22-standard readiness matrix, prioritized gap register, documentation-currency flags, NPRM pre-read (all PROPOSED)"
industries: [healthcare]
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2, HIPAA-Security-NPRM-2025]
inputs:
  org: "Bellbrook Regional Health — fictional covered entity hospital system, 6,000 staff, 4 facilities; systems: EHR, legacy lab system, imaging/PACS, patient portal"
  control_inventory: "per-standard status (implemented | partial | missing) across all 22 Subpart C standards (data/seeds/uc-02-control-inventory.json)"
  documentation_register: "8 policy documents with last-review dates (data/seeds/uc-02-documentation-register.json)"
  as_of_date: "2026-06-01"
  review_cycle_years: "3 (house engagement parameter — the rule says review 'periodically' with no stated cadence)"
procedure:
  - "chunks/01-scope-and-general-rules.md — Confirm the assessment universe: all 22 Subpart C standards (9 administrative, 4 physical, 5 technical, 2 organizational, 2 policies/documentation); state the counting convention."
  - "chunks/03-administrative-safeguards.md — Assess §164.308 standards; the missing 164.308(a)(8) Evaluation standard is a High gap (periodic technical and nontechnical evaluation)."
  - "chunks/05-technical-safeguards.md — Assess §164.312 standards; the missing 164.312(b) Audit controls on the legacy lab system is a High gap (a standard, not an addressable spec — it cannot be dispositioned away)."
  - "chunks/06-organizational-and-documentation.md — Flag documentation past the engagement review cycle vs §164.316(b)(2)(iii) Updates; distinguish from the 6-year RETENTION floor of §164.316(b)(2)(i)."
  - "chunks/08-enforcement-audit-and-nprm.md — Append the NPRM pre-read: every item labeled PROPOSED; zero NPRM items enter the current-law gap register."
  - "SKILL.md §4 (decision logic) — apply the gap-priority heuristic; SKILL.md §5 (procedure templates) — populate the readiness-matrix and gap-register templates."
expected_outputs:
  classification: "READINESS_GAPS_11"
  readiness_summary: { total: 22, implemented: 14, partial: 6, missing: 2 }
  gap_priorities: { High: 2, Medium: 6, Low: 3 }
  stale_docs: [POL-02, POL-04, POL-06]
  nprm_items_in_current_law_gaps: 0
oracle:
  - "readiness matrix has exactly 22 rows == the fact sheet's subpart_c_standards_total; every standard_id exists in the fact-sheet identifier list"
  - "status counts recomputed independently from the inventory seed: 14 implemented / 6 partial / 2 missing"
  - "stale docs recomputed from seed dates vs as_of_date (no wall clock): [POL-02, POL-04, POL-06] vs the 3-year house cycle"
  - "gap priorities recomputed: missing -> High (2), partial -> Medium (6), stale doc -> Low (3); gap register foots to 11"
  - "zero NPRM-derived rows in the current-law gap register; no gap basis text contains 'NPRM'"
data_refs:
  - data/seeds/uc-02-input.json
  - data/seeds/uc-02-control-inventory.json
  - data/seeds/uc-02-documentation-register.json
  - data/seeds/uc-02-expected.json
tests:
  - tests/test_hipaa_security_rule_oracle.py::test_uc_02_oracle
  - tests/test_hipaa_security_rule_metamorphic.py::test_uc02_inventory_order_invariance
  - tests/test_hipaa_security_rule_adversarial.py::test_uc02_all_implemented_zero_gaps
  - tests/test_hipaa_security_rule_adversarial.py::test_uc02_nprm_never_in_gap_basis
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-02 — Hospital CE OCR-readiness assessment (Bellbrook Regional Health)

## §1 Context and persona

**Bellbrook Regional Health** is a fictional covered-entity hospital system: 6,000 staff across 4 facilities, running an EHR, a legacy lab system, imaging/PACS, and a patient portal. The compliance office wants to know, before OCR ever asks: where do we stand against **every one of the 22 Subpart C standards**, which gaps matter most, and is our documentation current?

This is the auditor-readiness persona. The output is a 22-row readiness matrix, a prioritized gap register, documentation-currency flags, and an NPRM pre-read in which **every item is labeled PROPOSED**. The seeds are the tested fixture; `tests/test_hipaa_security_rule_oracle.py::test_uc_02_oracle` recomputes every number below from them.

## §2 The 22-standard readiness matrix

The assessment universe is the fact sheet's 22 standards — 9 administrative (§164.308), 4 physical (§164.310), 5 technical (§164.312), 2 organizational (§164.314), 2 policies-and-documentation (§164.316). Counting convention: **standards**, not implementation specifications (the matrix is one row per standard).

**Readiness summary: 22 standards — 14 implemented / 6 partial / 2 missing.**

| Status | Standards |
|--------|-----------|
| missing (2) | 164.308(a)(8) Evaluation; 164.312(b) Audit controls |
| partial (6) | 164.308(a)(1) Security management process; 164.308(a)(5) Security awareness and training; 164.310(d)(1) Device and media controls; 164.312(a)(1) Access control; 164.312(c)(1) Integrity; 164.314(a)(1) Business associate contracts or other arrangements |
| implemented (14) | 164.308(a)(2), 164.308(a)(3), 164.308(a)(4), 164.308(a)(6), 164.308(a)(7), 164.308(b)(1), 164.310(a)(1), 164.310(b), 164.310(c), 164.312(d), 164.312(e)(1), 164.314(b)(1), 164.316(a), 164.316(b)(1) |

The two missing standards are the engagement's headline findings:

- **164.312(b) Audit controls — missing on the legacy lab system.** Audit controls is a *standard* with no separately titled implementation specifications: "Implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use electronic protected health information" [CFR-45-164-Subpart-C §164.312(b)]. It is not addressable and cannot be dispositioned away under §164.306(d)(3) — a legacy system that cannot log must be compensated at the architecture level and the gap remediated.
- **164.308(a)(8) Evaluation — missing.** No periodic technical and nontechnical evaluation has been performed against the standards "in response to environmental or operational changes." Without it, Bellbrook cannot demonstrate that its 14 "implemented" statuses are still true.

## §3 Gap register — priority heuristic (house convention, labeled)

**House heuristic (labeled — not from the rule):** standard status `missing` → **High**; `partial` → **Medium**; policy document past the engagement review cycle → **Low**. All Subpart C standards are mandatory; the priority ranks remediation order, not obligation.

**Gap priorities: High 2 / Medium 6 / Low 3 — 11 gap records total.**

- **High (2):** 164.308(a)(8) Evaluation; 164.312(b) Audit controls (legacy lab system).
- **Medium (6):** the six partial standards listed in §2 — e.g., 164.308(a)(1) (risk analysis exists but the risk management plan does not foot to it), 164.314(a)(1) (BAA inventory incomplete for two imaging vendors).
- **Low (3):** stale policy documents POL-02, POL-04, POL-06 (next section).

## §4 Documentation currency — retention vs review, never confused

Two distinct §164.316(b)(2) obligations:

- **§164.316(b)(2)(i) Time limit (Required) — a 6-year RETENTION floor:** retain documentation "for 6 years from the date of its creation or the date when it last was in effect, whichever is later." This is retention, **never a review cadence**.
- **§164.316(b)(2)(iii) Updates (Required):** "Review documentation periodically, and update as needed" — the rule says **"periodically" with no stated cadence**.

**House convention (labeled):** this engagement uses a **3-year review cycle** as its staleness parameter — an engagement parameter, not a regulatory deadline. Against `as_of_date` 2026-06-01:

| Doc | Title | Last reviewed | Flag |
|-----|-------|---------------|------|
| POL-02 | Risk Analysis and Risk Management SOP | 2023-04-20 | stale (Low) |
| POL-04 | Contingency and Disaster Recovery Plan | 2022-04-15 | stale (Low) |
| POL-06 | Media Disposal and Reuse Procedure | 2021-11-30 | stale (Low) |

The other five registered documents (POL-01, POL-03, POL-05, POL-07, POL-08) are within the cycle. Staleness is computed from the seed's `as_of_date` — never from the wall clock.

## §5 NPRM pre-read — every item PROPOSED, none in the gap register

The 2025 NPRM, "HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information," 90 FR 898 (Jan. 6, 2025, RIN 0945-AA22), is a **Proposed Rule only as of 2026-06-10** — verified at the Federal Register docket level; no final rule exists under the RIN [HIPAA-Security-NPRM-2025]. Headline proposals Bellbrook should pre-read, **each one PROPOSED, none of them current law**:

- **PROPOSED:** removal of the required/addressable distinction (all specs required with limited exceptions).
- **PROPOSED:** mandatory encryption at rest and in transit.
- **PROPOSED:** multi-factor authentication.
- **PROPOSED:** vulnerability scanning and penetration testing cadences.
- **PROPOSED:** asset inventory and network map.
- **PROPOSED:** annual compliance audits.

**Zero NPRM items appear in the current-law gap register** — the oracle asserts `nprm_items_in_current_law_gaps == 0` and that no gap basis text contains "NPRM". Re-verify NPRM status before reuse; a final rule may publish at any time.

## §6 Oracle — every number is derivable

`test_uc_02_oracle` recomputes independently from the seeds: the matrix has exactly 22 rows matching the fact sheet's standard identifiers; status counts re-tallied (14/6/2); stale docs re-derived from seed dates vs `as_of_date` and the 3-year cycle (POL-02, POL-04, POL-06); priorities re-derived from the heuristic (High 2 / Medium 6 / Low 3, footing to 11 gap records); and the NPRM-exclusion invariant. Metamorphic: inventory order never changes the summary. Adversarial: an all-implemented inventory with current docs yields an empty gap register; NPRM language smuggled into a seed row never produces an NPRM-based gap.

## §7 Anti-hallucination

- **Bellbrook Regional Health is fictional**; the seeds are the tested fixture.
- **The gap-priority heuristic and the 3-year review cycle are house conventions, labeled as such.** The 6-year figure in §164.316(b)(2)(i) is documentation retention — citing it as a review cadence is an error this skill explicitly guards against.
- **Every NPRM item is PROPOSED** [HIPAA-Security-NPRM-2025]; presenting one as current law is the skill's top fidelity risk.
- **Audit controls (164.312(b)) and Evaluation (164.308(a)(8)) are standards with no separately titled specs** — the Appendix A matrix prints a standard-level (R) for them; never restate them as addressable.
- Penalty exposure is out of this UC's scope — amounts are stated once, as-of-dated, in `chunks/08-enforcement-audit-and-nprm.md`.
