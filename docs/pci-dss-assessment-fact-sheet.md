# Fact Sheet — pci-dss-assessment (Day 0, SOX-568)

> Pre-build research per `docs/fact-sheet-template.md`. The full standard PDF was acquired
> 2026-06-11 via the PCI SSC document library (licence acceptance authorized by and submitted
> with the maintainer's details) and stored OUTSIDE the repo at
> `~/Standards-licensed/PCI/PCI-DSS-v4_0_1.pdf` per process v3.1.
>
> **Licence class — a third class between eCFR and ISO:** the PCI SSC "Read and Copy License"
> grants download + copying *for internal purposes/study only*; no redistribution or
> modification; **no AI/extraction prohibition**. Consequences: (a) agents MAY machine-verify
> every fact against the local PDF (full Tier-2 automation — unlike ISO); (b) the public repo
> stores identifiers, counts, structure facts, and original paraphrase, with only short
> attributed excerpts — never bulk standard text (unlike eCFR). Inventory extraction was
> mechanical (`pdftotext -layout` + ID census); the artifact is
> `docs/builds/sox-568/pci-dss-inventory.json`.

## 0. Machine-readable data block (REQUIRED — the G1 gate parses this)

```yaml
fact_sheet:
  skill_slug: pci-dss-assessment
  framework: "PCI DSS v4.0.1 — Payment Card Industry Data Security Standard, Requirements and Testing Procedures"
  version: "v4.0.1 (June 2024); the ONLY active version — v4.0 retired 2024-12-31; all future-dated requirements IN FORCE since 2025-03-31"
  version_date: "2024-06-11"
  supersedes: "PCI DSS v4.0 (March 2022; retired 2024-12-31); v3.2.1 (retired 2024-03-31)"
  retrieval_date: "2026-06-11"
  researcher: "Claude (Fable 5) dispatcher — mechanical PDF extraction + doc-library JSON + live currency checks"
counts:
  goals: 6
  principal_requirements: 12
  sections_x_y: 63
  defined_requirements_main_body: 249
  defined_requirements_depth3: 205
  defined_requirements_depth4: 44
  appendix_sections: 8
  appendix_requirements: 30
  future_dated_markers_v401_text: 33
  saq_types: 10
  appendices_lettered: 7
identifiers:
  - code: "Req 1"
    name: "Install and Maintain Network Security Controls"
    parent: "Build and Maintain a Secure Network and Systems"
  - code: "Req 2"
    name: "Apply Secure Configurations to All System Components"
    parent: "Build and Maintain a Secure Network and Systems"
  - code: "Req 3"
    name: "Protect Stored Account Data"
    parent: "Protect Account Data"
  - code: "Req 4"
    name: "Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks"
    parent: "Protect Account Data"
  - code: "Req 5"
    name: "Protect All Systems and Networks from Malicious Software"
    parent: "Maintain a Vulnerability Management Program"
  - code: "Req 6"
    name: "Develop and Maintain Secure Systems and Software"
    parent: "Maintain a Vulnerability Management Program"
  - code: "Req 7"
    name: "Restrict Access to System Components and Cardholder Data by Business Need to Know"
    parent: "Implement Strong Access Control Measures"
  - code: "Req 8"
    name: "Identify Users and Authenticate Access to System Components"
    parent: "Implement Strong Access Control Measures"
  - code: "Req 9"
    name: "Restrict Physical Access to Cardholder Data"
    parent: "Implement Strong Access Control Measures"
  - code: "Req 10"
    name: "Log and Monitor All Access to System Components and Cardholder Data"
    parent: "Regularly Monitor and Test Networks"
  - code: "Req 11"
    name: "Test Security of Systems and Networks Regularly"
    parent: "Regularly Monitor and Test Networks"
  - code: "Req 12"
    name: "Support Information Security with Organizational Policies and Programs"
    parent: "Maintain an Information Security Policy"
  - code: "SAQ A"
    name: "Self-Assessment Questionnaire A — v4.0.1 (2025-01-30)"
    parent: "SAQ catalog"
  - code: "SAQ A-EP"
    name: "Self-Assessment Questionnaire A-EP — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "SAQ B"
    name: "Self-Assessment Questionnaire B — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "SAQ B-IP"
    name: "Self-Assessment Questionnaire B-IP — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "SAQ C"
    name: "Self-Assessment Questionnaire C — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "SAQ C-VT"
    name: "Self-Assessment Questionnaire C-VT — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "SAQ D Merchant"
    name: "Self-Assessment Questionnaire D for Merchants — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "SAQ D Service Provider"
    name: "Self-Assessment Questionnaire D for Service Providers — v4.0.1 (2025-01-16)"
    parent: "SAQ catalog"
  - code: "SAQ P2PE"
    name: "Self-Assessment Questionnaire P2PE — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "SAQ SPoC"
    name: "Self-Assessment Questionnaire SPoC — v4.0.1 (2024-10-11)"
    parent: "SAQ catalog"
  - code: "Appendix A1"
    name: "Additional PCI DSS Requirements for Multi-Tenant Service Providers"
    parent: "Appendix A"
  - code: "Appendix A2"
    name: "Additional PCI DSS Requirements for Entities Using SSL/Early TLS for Card-Present POS POI Terminal Connections"
    parent: "Appendix A"
  - code: "Appendix A3"
    name: "Designated Entities Supplemental Validation (DESV)"
    parent: "Appendix A"
  - code: "Appendix B"
    name: "Compensating Controls"
    parent: "Appendices"
  - code: "Appendix C"
    name: "Compensating Controls Worksheet"
    parent: "Appendices"
  - code: "Appendix D"
    name: "Customized Approach"
    parent: "Appendices"
  - code: "Appendix E"
    name: "Sample Templates to Support Customized Approach"
    parent: "Appendices"
  - code: "Appendix F"
    name: "Leveraging the PCI Software Security Framework to Support Requirement 6"
    parent: "Appendices"
  - code: "Appendix G"
    name: "PCI DSS Glossary of Terms, Abbreviations, and Acronyms"
    parent: "Appendices"
urls:
  - label: "PCI-SSC-Document-Library"
    url: "https://www.pcisecuritystandards.org/document_library/"
    status: 200
    checked: "2026-06-11"
  - label: "PCI-SSC-Blog-v401"
    url: "https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1"
    status: 200
    checked: "2026-06-11"
  - label: "NIST-CSF-Informative-References"
    url: "https://www.nist.gov/cyberframework/informative-references"
    status: 200
    checked: "2026-06-11"
  - label: "NIST-OLIR"
    url: "https://csrc.nist.gov/projects/olir"
    status: 200
    checked: "2026-06-11"
crosswalks: []
terminology:
  - term: "Defined approach vs customized approach"
    source_wording: "Most PCI DSS requirements can be met using either the defined or customized approach (v4.0.1 §8, Approaches for Implementing and Validating PCI DSS); the customized approach controls 'are expected to meet or exceed the security provided' by the defined requirement. Several requirements have no customized-approach option."
  - term: "Future-dated requirements (now in force)"
    source_wording: "Applicability note in v4.0.1 text: 'best practice until 31 March 2025' — 33 such markers in the main body; ALL are mandatory since 2025-03-31 (the skill must never present them as optional)."
  - term: "Network security controls (NSCs)"
    source_wording: "v4.0 renamed 'firewalls and routers' to network security controls (Req 1 title: 'Install and Maintain Network Security Controls'); the skill must not teach Req 1 as 'the firewall requirement'."
  - term: "Account data = cardholder data + sensitive authentication data"
    source_wording: "Req 3 title is 'Protect Stored Account Data' (v4 renamed from 'cardholder data') — account data comprises CHD and SAD; verify the precise Appendix G definitions against the local PDF at G4 (machine-checkable)."
  - term: "Merchant levels"
    source_wording: "Merchant/service-provider validation levels are defined by the PAYMENT BRANDS and acquirers, NOT by PCI SSC or the standard — the skill must label any level thresholds as brand-specific and variable."
sign_off: true
```

## 1. Primary sources

| Source | What | Retrieval | Verification anchor |
|--------|------|-----------|---------------------|
| PCI DSS v4.0.1 PDF (local oracle, outside repo) | The standard: 12 requirements, testing procedures, appendices A–G | 2026-06-11, via document-library licence acceptance (authorized) | Title page: "Payment Card Industry Data Security Standard: Requirements and Testing Procedures, Version 4.0.1, June 2024"; 4,458,346 bytes |
| PCI SSC doc-library JSON (`docs-pub.../doc_library.json`) | Authoritative machine-readable catalog: SAQ types/versions/dates, ROC/AOC templates, agreement metadata | 2026-06-11 | SAQ rows extracted verbatim (10 types, all v4.0.1) |
| PCI SSC blog "Just Published: PCI DSS v4.0.1" | 4.0.1 nature: "limited revision… no new or deleted requirements" | 2026-06-11 | URL 200 |
| NIST OLIR catalog | "PCI-DSS-4.0.1-to-CSF-v2.0" final informative reference (posted 2025-12-23, submitted by PCI SSC) — the public ID-level anchor + crosswalk source | 2026-06-11 | Search-level; pin the catalog entry at G3 crosswalk extraction |
| Mechanical inventory artifact | `docs/builds/sox-568/pci-dss-inventory.json` — full ID census (this is what G3 tests diff against) | 2026-06-11 | Counts below |

## 2. Structural inventory

All counts mechanical from the local PDF (conventions documented in the inventory artifact):

| Level | Count | Convention note |
|---|---|---|
| Goals | 6 | overview table groups; goal→requirement map in inventory JSON |
| Principal requirements | 12 | titles verified (Req 4 and Req 11 wrap across lines in the PDF text layer — extraction artifact documented) |
| Sections (x.y) | 63 | per-requirement: 5/3/7/2/4/5/3/6/5/7/6/10 (Req 1→12) |
| Defined requirements (main body) | 249 | numbered x.y.z (205) + x.y.z.w (44) rows; testing procedures excluded (letter suffixes) |
| Appendix A requirements | 30 (in 8 sections) | A1 multi-tenant, A2 SSL/early-TLS POS POI, A3 DESV |
| Future-dated markers | 33 | "best practice until 31 March 2025" applicability notes in v4.0.1 text — ALL IN FORCE since 2025-03-31 |
| SAQ types | 10 | A, A-EP, B, B-IP, C, C-VT, D-Merchant, D-Service-Provider, P2PE, SPoC (ticket's list of 6 was incomplete) |
| Lettered appendices | 7 | A–G; B/C compensating controls COEXIST with D/E customized approach in v4 |

**Counting caveat for §5.11:** secondary sources cite various totals ("~250", "264", "277+") for
v4 requirements depending on whether testing procedures, appendix rows, and section-level
statements are counted. The skill states counts ONLY with this fact sheet's conventions and
never asserts a bare total.

## 3. Crosswalk mappings

None encoded at G1. The authoritative source is the OLIR "PCI-DSS-4.0.1-to-CSF-v2.0" final
reference (PCI SSC-submitted, US-gov hosted) — extract at G3 with the proven CPRT/OLIR method
(same as the HIPAA crosswalk, SOX-638) and vendor IDs + relationship rows only.

## 4. URL verification

The four gate URLs above returned 200 on 2026-06-11. Known constraint: `docs-prv.…` PDF links
require the click-through (licence acceptance per download session) — cite the document-library
page in manifests, never deep PDF links.

## 5. Terminology

See §0 block. Additional G4 verification notes: precise Appendix G definitions (account data,
CHD, SAD, CDE, NSC, TRA) are machine-verifiable against the local PDF — terminology rows in
the skill must be verified at G4 against it, with short attributed excerpts only in the repo.

## 6. Version and supersession (all currency claims verified 2026-06-11)

- **v4.0.1 (June 2024) is the only active version**; a "limited revision" — no new or deleted
  requirements vs v4.0 (PCI SSC blog).
- **v4.0 retired 2024-12-31**; v3.2.1 retired 2024-03-31.
- **All future-dated requirements became mandatory 2025-03-31** — in force for over a year now.
  The v4.0.1 text still carries the "best practice until" notes (printed before the date); the
  skill must present these as fully effective.
- **No v4.1/v5 announced** as of 2026-06-11 (searched; no PCI SSC announcement found). Re-verify
  at every G4 pass — version currency is this skill's #1 trust factor per the ticket.
- SAQ catalog: all 10 SAQs at v4.0.1 (doc-library JSON, dates per identifier list).

## 7. Scope boundaries — what the skill does NOT cover

- **Merchant/SP levels are brand-defined** — never asserted as SSC facts; thresholds vary by
  payment brand and acquirer agreement.
- PTS, P2PE-standard internals, Software Security Framework (beyond the Appendix F pointer),
  PIN security — separate PCI standards, out of scope.
- Card-brand compliance programs and fines/penalties — pointer-only, no amounts.
- No legal/contractual advice; QSA engagement mechanics described, not simulated.
- Bulk standard text never enters the repo (licence: internal use only).

## 8. Sign-off — Day 0 research complete

- [x] Standard acquired (authorized licence acceptance), stored outside repo, licence class
      analyzed and recorded in `source-texts/manifest.json` (update pending in this PR)
- [x] Full mechanical inventory extracted (6/12/63/249/30 + 33 future-dated markers) with
      explicit counting conventions; artifact: `docs/builds/sox-568/pci-dss-inventory.json`
- [x] SAQ catalog (10 types) from the authoritative doc-library JSON — ticket's 6-type list corrected
- [x] Currency pinned: 4.0.1 only active version; future-dated now in force; no successor announced
- [x] OLIR PCI→CSF2.0 reference located as the public crosswalk anchor (extraction at G3)
- [x] Gate URLs 200; deep-PDF-link constraint documented
- [x] `python3 tools/check_fact_sheet.py docs/pci-dss-assessment-fact-sheet.md` passes
