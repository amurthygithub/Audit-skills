# Acceptance gate — HIPAA Security Rule skill

Born-vetted build (SOX-572, process v3): this gate is seeded from the verified rows of the
Day 0 fact sheet (`docs/hipaa-security-rule-fact-sheet.md`, repo root), which was transcribed
mechanically from the official eCFR API XML (2026-06-09 point-in-time snapshot) with currency
claims settled by live fetches of the Federal Register API, csrc.nist.gov, and govinfo.gov.
Every row carries the verbatim-quote anchor recorded in the fact sheet (§1/§6). The standing
fact-sheet inventory-diff CI test keeps rows 1-9 enforced on every run, not just at this gate.

## §5.11 verification table (seeded 2026-06-10)

| # | fact | source | retrieval date | verifier | status |
|---|------|--------|----------------|----------|--------|
| 1 | §164.308 Administrative safeguards: 9 standards, 21 titled implementation specs (10 Required / 11 Addressable) | eCFR API XML, 45 CFR 164 Subpart C (2026-06-09 snapshot), mechanical transcription; anchor: subpart head "Security Standards for the Protection of Electronic Protected Health Information" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 2 | §164.310 Physical safeguards: 4 standards, 8 titled implementation specs (2 Required / 6 Addressable) | eCFR API XML, same snapshot; anchor: subpart head "Security Standards for the Protection of Electronic Protected Health Information" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 3 | §164.312 Technical safeguards: 5 standards, 7 titled implementation specs (2 Required / 5 Addressable) | eCFR API XML, same snapshot; anchor: subpart head "Security Standards for the Protection of Electronic Protected Health Information" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 4 | §164.314 Organizational requirements: 2 standards (specs designated "(Required)" inline) | eCFR API XML, same snapshot; anchor: authority note "42 U.S.C. 1320d-2 and 1320d-4; sec. 13401, Pub. L. 111-5, 123 Stat. 260." | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 5 | §164.316 Policies/procedures and documentation: 2 standards, 3 Required documentation specs | eCFR API XML, same snapshot; anchor: authority note "42 U.S.C. 1320d-2 and 1320d-4; sec. 13401, Pub. L. 111-5, 123 Stat. 260." | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 6 | Titled-spec counting convention: Appendix A matrix = 18 standards, 36 titled specs (14 R / 22 A) | eCFR API XML, Appendix A to Subpart C; anchor (fact sheet §2): "Counting only the titled specs in the regulatory text gives 36 — 14 R / 22 A" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 7 | 42-entry counting convention: matrix prints an (R) for the 6 standards with no separately titled specs, giving "42 implementation specifications — 20 Required / 22 Addressable"; the skill must always label which convention it uses and never mix them | eCFR API XML, Appendix A to Subpart C; anchor (fact sheet §2): "Counting those entries gives the widely cited 42 implementation specifications — 20 Required / 22 Addressable" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 8 | Subpart C total: 22 standards (9 admin + 4 physical + 5 technical + 2 organizational + 2 policies/documentation) | eCFR API XML, same snapshot (fact sheet §0 counts + §2 table); anchor: subpart head "Security Standards for the Protection of Electronic Protected Health Information" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 9 | §164.304 defines exactly 17 terms (Access through Workstation) | eCFR API XML, same snapshot; anchor (fact sheet §2): "§164.304 defines 17 terms (Access; Administrative safeguards; Authentication; Availability; Confidentiality; Encryption; Facility; Information system; Integrity; Malicious software; Password; Physical safeguards; Security or Security measures; Security incident; Technical safeguards; User; Workstation)" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 10 | 2025 NPRM (90 FR 898, RIN 0945-AA22) is PROPOSED ONLY — verified at the docket level, not from secondary reporting | Federal Register API, RIN 0945-AA22 docket query; anchor: API result: type "Proposed Rule", title "HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information". No document of type "Rule" under the RIN. | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 11 | NIST SP 800-66 Rev. 2 is Final (2024-02-14) and supersedes Rev. 1; Rev. 1 must not be cited | csrc.nist.gov publication page + PDF; anchor: "02/14/24: SP 800-66 Rev. 2 (Final)" and "Supersedes: SP 800-66 Rev. 1 (10/23/2008)" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 12 | PL 116-321 approved Jan. 5, 2021 (adds HITECH §13412, 42 U.S.C. 17941); SP 800-66r2 footnote 9 misstates the year as 2020 — cite the statute, not the footnote | govinfo statute text; anchor: "<<NOTE: Jan. 5, 2021 - [H.R. 7898]>>" and "SEC. 13412. <<NOTE: 42 USC 17941.>> RECOGNITION OF SECURITY PRACTICES." | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 13 | Penalty Tier 1 (did not/could not know): min $145, max $73,011 — 2025 inflation-adjusted amounts | eCFR API XML, 45 CFR Part 102, "2025 Maximum adjusted penalty" column; anchor: Table 1 to §102.3 rows for 42 U.S.C. 1320(d)-5(a) / 45 CFR 160.404(b)(2) | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 14 | Penalty Tier 2 (reasonable cause): min $1,461, max $73,011 — 2025 adjusted | eCFR API XML, 45 CFR Part 102, same column; anchor: Table 1 to §102.3 rows for 42 U.S.C. 1320(d)-5(a) / 45 CFR 160.404(b)(2) | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 15 | Penalty Tier 3 (willful neglect, corrected within 30 days): min $14,602, max $73,011 — 2025 adjusted | eCFR API XML, 45 CFR Part 102, same column; anchor: Table 1 to §102.3 rows for 42 U.S.C. 1320(d)-5(a) / 45 CFR 160.404(b)(2) | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 16 | Penalty Tier 4 (willful neglect, uncorrected): min $73,011, max $2,190,294; calendar-year cap $2,190,294 per provision (all tiers); amounts adjust annually per 45 CFR 102.3 | eCFR API XML, 45 CFR Part 102, same column; anchor: Table 1 to §102.3 rows for 42 U.S.C. 1320(d)-5(a) / 45 CFR 160.404(b)(2) | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 17 | Documentation retention is 6 years (§164.316(b)(2)(i)) | eCFR API XML, same snapshot; anchor: "Retain the documentation required by paragraph (b)(1) of this section for 6 years from the date of its creation or the date when it last was in effect, whichever is later." | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 18 | Addressable decision logic (§164.306(d)(3)) — addressable never means optional | eCFR API XML, same snapshot; anchor: "Assess whether each implementation specification is a reasonable and appropriate safeguard in its environment … Implement the implementation specification if reasonable and appropriate; or … Document why it would not be reasonable and appropriate … and Implement an equivalent alternative measure if reasonable and appropriate." | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 19 | eCFR rendering artifact: in the Appendix A matrix the "(A)" for Workforce clearance procedure is dropped/merged in the table cell; the regulatory text controls — §164.308(a)(3)(ii)(B) is explicitly "(Addressable)" | eCFR API XML, Appendix A rendering vs body text; anchor (fact sheet §2): "the '(A)' designation for Workforce clearance procedure is dropped/merged in the table cell (body (A) marks count 21, not 22)" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 20 | eCFR rendering artifact: §164.308(b)(1) (Business associate contracts) lacks the "Standard:" prefix in body text — a naive grep finds 8 administrative standards, not 9; Appendix A lists it as the 9th | eCFR API XML, body text vs Appendix A; anchor (fact sheet §2): "does not carry the 'Standard:' prefix in the body text — a naive Standard: grep finds 8 administrative standards, not 9" | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 21 | The Security Rule crosswalk mapping was removed from SP 800-66r2 and placed online in the NIST CPRT — therefore v1 of this skill encodes no crosswalk rows (SOX-638 deferral) | SP 800-66r2 PDF, Appendix D, p. 105; anchor: "the mapping table has been removed from the document and placed online in the NIST Cybersecurity and Privacy Reference Tool (CPRT)." | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |
| 22 | The CPRT mapping targets CSF v1.1 only; the skill must never claim an 800-66r2 mapping to CSF 2.0 | SP 800-66r2 PDF; anchor: the mapping "was intentionally broad and includes mappings to Subcategories that both directly and indirectly align." | 2026-06-10 | dispatcher | VERIFIED (2026-06-10, dispatcher) |

## Standing enforcement

- Rows 1-9 (structural inventory, both counting conventions) are re-asserted on every CI run
  by `tests/test_hipaa_security_rule_oracle.py::test_fact_sheet_inventory_diff`, which parses
  the fact sheet §0 YAML block — drift between chunks/seeds and the mechanical eCFR
  transcription fails the build.
- Row 10 (NPRM proposed-only) is the volatile claim: it MUST be re-verified live at every G4
  pass — a final rule may drop at any time.
- Rows 13-16 (penalty amounts) adjust annually per 45 CFR 102.3; re-pin the as-of date at
  each annual refresh.

## Sign-off

Seeded 2026-06-10 from the Day 0 fact sheet's verified rows (SOX-572, born-vetted build).
G4.5 persona vetting evidence lands in `docs/persona-review.md` within the same build PR.
The skill ships `status: draft` v0.1.0 pending Epic 6 reliability measurement.
