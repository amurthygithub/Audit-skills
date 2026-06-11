# Acceptance gate — PCI DSS assessment skill

Born-vetted build (SOX-568, process v3, M5 cycle 1): this gate is seeded from the verified rows
of the Day 0 fact sheet (`docs/pci-dss-assessment-fact-sheet.md`, repo root), which was
extracted mechanically from the maintainer's licensed copy of the PCI DSS v4.0.1 PDF
(`PCI-DSS-v4_0_1.pdf`, retrieved 2026-06-11, stored outside the repo per the Read-and-Copy
licence) plus the PCI SSC document-library JSON catalog, with currency claims settled by live
source checks. Each row cites requirement IDs, section numbers, and structure references —
**never verbatim standard text** (the standard is licensed; this skill paraphrases and cites).
PCI DSS is machine-verifiable against the local licensed copy, so no human-licensed-row
exception is needed: the structural rows below are mechanically re-checkable against the PDF and
the inventory artifact. The standing fact-sheet inventory-diff CI test keeps the structural rows
enforced on every run, not just at this gate.

## §5.11 verification table (seeded 2026-06-11)

| # | fact | source | retrieval date | verifier | status |
|---|------|--------|----------------|----------|--------|
| 1 | 6 goals group the 12 principal requirements (Build & Maintain a Secure Network and Systems; Protect Account Data; Maintain a Vulnerability Management Program; Implement Strong Access Control Measures; Regularly Monitor and Test Networks; Maintain an Information Security Policy) | PCI DSS v4.0.1 PDF (licensed local copy), overview goal→requirement table; mechanical extraction into `docs/builds/sox-568/pci-dss-inventory.json` | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 2 | 12 principal requirements, Req 1 through Req 12, titles per the fact sheet §0 identifier list | PCI DSS v4.0.1 PDF, requirement title pages; ID census in the inventory artifact | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 3 | Req 1 is "Install and Maintain Network Security Controls" — NSCs, not "firewalls and routers"; the skill must not teach Req 1 as "the firewall requirement" (v4 renamed the control class) | PCI DSS v4.0.1 PDF, Req 1 title; fact sheet §5 terminology row "Network security controls (NSCs)" | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 4 | Req 3 is "Protect Stored Account Data" — account data = cardholder data (CHD) + sensitive authentication data (SAD); v4 renamed from "cardholder data"; precise Appendix G definitions are machine-checkable against the PDF | PCI DSS v4.0.1 PDF, Req 3 title + Appendix G; fact sheet §5 terminology row "Account data = cardholder data + sensitive authentication data" | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 5 | 63 sections (x.y) across the 12 requirements: per-requirement 5/3/7/2/4/5/3/6/5/7/6/10 (Req 1→12) | PCI DSS v4.0.1 PDF, section enumeration; inventory artifact convention note | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 6 | 249 defined requirements in the main body = 205 depth-3 (x.y.z) + 44 depth-4 (x.y.z.w); testing procedures (letter suffixes) excluded by the documented counting convention | PCI DSS v4.0.1 PDF, ID census; inventory artifact; fact sheet §0 counts (205 + 44 = 249) | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 7 | 30 appendix requirements across 8 appendix sections (A1 multi-tenant service providers, A2 SSL/early-TLS POS POI, A3 DESV) | PCI DSS v4.0.1 PDF, Appendix A; inventory artifact | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 8 | 33 future-dated markers ("best practice until 31 March 2025" applicability notes) in the v4.0.1 main-body text — ALL in force since 2025-03-31; the skill must never present them as optional | PCI DSS v4.0.1 PDF, applicability-note census; fact sheet §5 terminology row "Future-dated requirements (now in force)" + §6 currency | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 9 | 10 SAQ types: A, A-EP, B, B-IP, C, C-VT, D-Merchant, D-Service-Provider, P2PE, SPoC — all at v4.0.1 (the ticket's original 6-type list was incomplete; corrected to 10) | PCI SSC document-library JSON catalog (authoritative, machine-readable); fact sheet §0 identifier list (SAQ rows) | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 10 | SAQ catalog versions/dates per the doc-library JSON: SAQ A v4.0.1 (2025-01-30), A-EP/B/B-IP/C/C-VT/D-Merchant/P2PE/SPoC v4.0.1 (2024-10-11), SAQ D Service Provider v4.0.1 (2025-01-16) | PCI SSC document-library JSON catalog; fact sheet §0 identifier list | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 11 | Defined vs. customized approach: most requirements can be met by either; the customized approach is expected to meet or exceed the defined requirement's security and is driven by a documented Targeted Risk Analysis (TRA); several requirements have no customized-approach option | PCI DSS v4.0.1 PDF, §8 "Approaches for Implementing and Validating PCI DSS"; fact sheet §5 terminology row "Defined approach vs customized approach" | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 12 | Compensating control (Appendix B/C) requires exactly four worksheet elements: constraints documented, objective of the original requirement stated, identified risk documented, controls in place described | PCI DSS v4.0.1 PDF, Appendix B & Appendix C (Compensating Controls Worksheet); stub `WORKSHEET_ELEMENTS` (len == 4, asserted in the oracle) | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 13 | Compensating control vs. customized approach are distinct mechanisms: a compensating control addresses an EXISTING defined requirement an entity cannot meet due to a legitimate constraint (Appendix B/C); a customized approach meets the objective by a different method with a TRA and is NOT constraint-driven (Appendix D/E) | PCI DSS v4.0.1 PDF, Appendix B/C vs Appendix D/E; UC-03 seed + oracle | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 14 | 7 lettered appendices A–G; Appendix B (Compensating Controls) and C (Worksheet) COEXIST with Appendix D (Customized Approach) and E (Sample Templates) in v4 — they are not alternatives to each other | PCI DSS v4.0.1 PDF, appendix table of contents; fact sheet §0 identifier list (Appendix B–G) + §2 table | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 15 | v4.0.1 (June 2024) is the ONLY active version; v4.0 retired 2024-12-31; v3.2.1 retired 2024-03-31; v4.0.1 is a "limited revision" with no new or deleted requirements vs v4.0 | PCI SSC blog "Just Published: PCI DSS v4.0.1" (URL 200) + document-library; fact sheet §6 | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 16 | No successor version (v4.1 / v5) announced as of 2026-06-11 — searched, no PCI SSC announcement found; version currency is this skill's #1 trust factor and must be re-verified at every G4 pass | PCI SSC document-library + announcement search (live); fact sheet §6 | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 17 | Merchant/service-provider validation levels (L1, L2, …) are defined by the PAYMENT BRANDS and acquirers, NOT by PCI SSC or the standard; thresholds vary by brand and are labeled brand-specific in all fixtures | PCI DSS v4.0.1 PDF (no level thresholds in the standard) + brand-program documentation; fact sheet §5 terminology row "Merchant levels" + §7 scope boundary | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 18 | SAQ A vs SAQ A-EP turns on payment-page script control: SAQ A = fully outsourced (redirect/iframe to a compliant TPSP) with no merchant code on the payment page; SAQ A-EP = the merchant website controls payment-page elements/scripts (so it can affect PAN security) but its servers never receive PAN | PCI SSC SAQ A and SAQ A-EP eligibility criteria (doc-library); UC-01 seed + oracle (house routing convention applying the eligibility rules) | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 19 | Client-side script requirements 6.4.3 (manage payment-page scripts) and 11.6.1 (detect tampering/unauthorized changes) apply on SAQ A-EP and full ROC, not on pure SAQ A; both were among the future-dated requirements now in force | PCI DSS v4.0.1 PDF, Req 6.4.3 and Req 11.6.1 IDs + SAQ applicability; UC-01 oracle (`client_side_script_requirements_apply`) | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 20 | Counting caveat: secondary sources cite various v4 totals ("~250", "264", "277+") depending on whether testing procedures, appendix rows, and section-level statements are counted; the skill states counts ONLY with the fact sheet's documented conventions and never asserts a bare total | Fact sheet §2 counting caveat; inventory artifact convention notes | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 21 | PCI DSS standard text is licensed under the PCI SSC "Read and Copy License" (internal use/study only; no redistribution or modification; no AI/extraction prohibition); the public repo stores identifiers, counts, structure, and original paraphrase with only short attributed excerpts — never bulk standard text | PCI SSC Read-and-Copy License terms; fact sheet header licence-class analysis | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 22 | No PCI → CSF crosswalk rows encoded in v1; the authoritative anchor is the NIST OLIR final informative reference "PCI-DSS-4.0.1-to-CSF-v2.0" (PCI SSC-submitted, US-gov hosted); the skill points to OLIR and the NIST CSF informative-references catalog without asserting any row | NIST OLIR catalog (URL 200) + NIST CSF Informative References (URL 200); fact sheet §3 crosswalks (empty) | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 23 | Gate URL liveness sweep: PCI-SSC-Document-Library 200, PCI-SSC-Blog-v401 200, NIST-CSF-Informative-References 200, NIST-OLIR 200 (deep `docs-prv` PDF links require licence click-through and are never cited directly) | Live status checks of the four registry URLs; fact sheet §0 urls + §4 | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |
| 24 | UC ↔ seed coherence re-derived independently of CI: UC-01 → SAQ A-EP with [6.4.3, 11.6.1]; UC-02 → 14 systems, 5 CDE, 10 in scope, 4 out, customized 8.3.6 accepted (TRA present); UC-03 → compensating control, 4/4 worksheet elements complete — all match the expected seeds and the oracle recompute | Recomputation from `data/seeds/*.json` + pytest run (`test_pci_dss_assessment_oracle.py`) | 2026-06-11 | dispatcher | VERIFIED (2026-06-11, dispatcher) |

## Standing enforcement

- The structural rows (goals, principal requirements, sections, defined-requirement counts, SAQ
  types) are re-asserted on every CI run by
  `tests/test_pci_dss_assessment_oracle.py::test_fact_sheet_inventory_diff`, which parses the
  fact sheet §0 YAML block — drift between chunks/seeds and the mechanical PDF extraction fails
  the build.
- Version currency (row 15/16), the SAQ catalog versions (row 10), and the future-dated-now-in-
  force status (row 8) are the volatile claims: they MUST be re-verified live at every G4 pass —
  the active version, the SAQ catalog, and the absence of a successor are this skill's top trust
  factors.
- The OLIR crosswalk anchor (row 22) is re-checked when row encoding is undertaken.

## Sign-off

Seeded 2026-06-11 from the Day 0 fact sheet's verified rows (SOX-568, born-vetted build, M5
cycle 1). G4.5 persona vetting evidence lands in `docs/persona-review.md` within the same build
PR. The skill ships `status: draft` v0.1.0 pending reliability measurement.
