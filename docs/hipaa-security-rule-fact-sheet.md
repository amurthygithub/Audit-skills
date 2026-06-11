# Fact Sheet — hipaa-security-rule (Day 0, SOX-572)

> Pre-build research per `docs/fact-sheet-template.md`. Every claim below was verified against
> a live primary source on the retrieval date. The §0 data block is the single machine-checkable
> source of truth; the G3 build tests assert against it. No build agent writes from recall.
>
> **Primary source method:** the full text of 45 CFR Part 164 Subpart C was downloaded as XML
> from the official eCFR API (`https://www.ecfr.gov/api/versioner/v1/full/2026-06-09/title-45.xml?part=164&subpart=C`)
> on 2026-06-10 and the inventory below was transcribed mechanically from that file (Tier 1).
> Currency claims (NPRM status, SP 800-66r2, PL 116-321) were settled by live fetches of the
> Federal Register API, csrc.nist.gov, and govinfo.gov (Tier 2, quotes inline).

## 0. Machine-readable data block (REQUIRED — the G1 gate parses this)

```yaml
fact_sheet:
  skill_slug: hipaa-security-rule
  framework: "HIPAA Security Rule — 45 CFR Part 164, Subpart C (Security Standards for the Protection of Electronic Protected Health Information)"
  version: "Current CFR text; last substantive amendment 78 FR 34266 (June 7, 2013, Omnibus corrections); 2025 NPRM (90 FR 898) is PROPOSED ONLY"
  version_date: "2013-06-07"
  supersedes: "Original rule 68 FR 8376 (Feb. 20, 2003), as amended by the HITECH Omnibus Rule 78 FR 5566 (Jan. 25, 2013)"
  retrieval_date: "2026-06-10"
  researcher: "Claude (Fable 5) dispatcher, live eCFR XML + Federal Register API + govinfo"
counts:
  # §164.308 Administrative safeguards
  admin_standards: 9
  admin_impl_specs: 21
  admin_impl_specs_required: 10
  admin_impl_specs_addressable: 11
  # §164.310 Physical safeguards
  physical_standards: 4
  physical_impl_specs: 8
  physical_impl_specs_required: 2
  physical_impl_specs_addressable: 6
  # §164.312 Technical safeguards
  technical_standards: 5
  technical_impl_specs: 7
  technical_impl_specs_required: 2
  technical_impl_specs_addressable: 5
  # Appendix A matrix (covers §§164.308/310/312 only)
  matrix_standards: 18
  matrix_titled_impl_specs: 36
  matrix_titled_impl_specs_required: 14
  matrix_titled_impl_specs_addressable: 22
  # Alternative counting convention: the matrix prints an (R) entry for the 6
  # standards that have no separately-titled specs, giving the widely-cited
  # "42 implementation specifications (20 R / 22 A)". Both conventions are real;
  # the skill must always state which it is using.
  matrix_entries_including_standard_level_r: 42
  matrix_entries_required_including_standard_level_r: 20
  # §164.314 Organizational requirements
  organizational_standards: 2
  # §164.316 Policies and procedures and documentation
  policies_documentation_standards: 2
  documentation_impl_specs_required: 3
  # Subpart C overall
  subpart_c_standards_total: 22
  definitions_in_164_304: 17
  general_requirements_164_306a: 4
  flexibility_factors_164_306b2: 4
  penalty_tiers_45_cfr_160_404: 4
identifiers:
  # ——— §164.308 Administrative safeguards: 9 standards ———
  - code: "164.308(a)(1)"
    name: "Security management process (Standard)"
    parent: "164.308"
  - code: "164.308(a)(1)(ii)(A)"
    name: "Risk analysis (Required)"
    parent: "164.308(a)(1)"
  - code: "164.308(a)(1)(ii)(B)"
    name: "Risk management (Required)"
    parent: "164.308(a)(1)"
  - code: "164.308(a)(1)(ii)(C)"
    name: "Sanction policy (Required)"
    parent: "164.308(a)(1)"
  - code: "164.308(a)(1)(ii)(D)"
    name: "Information system activity review (Required)"
    parent: "164.308(a)(1)"
  - code: "164.308(a)(2)"
    name: "Assigned security responsibility (Standard; no separate specs)"
    parent: "164.308"
  - code: "164.308(a)(3)"
    name: "Workforce security (Standard)"
    parent: "164.308"
  - code: "164.308(a)(3)(ii)(A)"
    name: "Authorization and/or supervision (Addressable)"
    parent: "164.308(a)(3)"
  - code: "164.308(a)(3)(ii)(B)"
    name: "Workforce clearance procedure (Addressable)"
    parent: "164.308(a)(3)"
  - code: "164.308(a)(3)(ii)(C)"
    name: "Termination procedures (Addressable)"
    parent: "164.308(a)(3)"
  - code: "164.308(a)(4)"
    name: "Information access management (Standard)"
    parent: "164.308"
  - code: "164.308(a)(4)(ii)(A)"
    name: "Isolating health care clearinghouse functions (Required)"
    parent: "164.308(a)(4)"
  - code: "164.308(a)(4)(ii)(B)"
    name: "Access authorization (Addressable)"
    parent: "164.308(a)(4)"
  - code: "164.308(a)(4)(ii)(C)"
    name: "Access establishment and modification (Addressable)"
    parent: "164.308(a)(4)"
  - code: "164.308(a)(5)"
    name: "Security awareness and training (Standard)"
    parent: "164.308"
  - code: "164.308(a)(5)(ii)(A)"
    name: "Security reminders (Addressable)"
    parent: "164.308(a)(5)"
  - code: "164.308(a)(5)(ii)(B)"
    name: "Protection from malicious software (Addressable)"
    parent: "164.308(a)(5)"
  - code: "164.308(a)(5)(ii)(C)"
    name: "Log-in monitoring (Addressable)"
    parent: "164.308(a)(5)"
  - code: "164.308(a)(5)(ii)(D)"
    name: "Password management (Addressable)"
    parent: "164.308(a)(5)"
  - code: "164.308(a)(6)"
    name: "Security incident procedures (Standard)"
    parent: "164.308"
  - code: "164.308(a)(6)(ii)"
    name: "Response and reporting (Required)"
    parent: "164.308(a)(6)"
  - code: "164.308(a)(7)"
    name: "Contingency plan (Standard)"
    parent: "164.308"
  - code: "164.308(a)(7)(ii)(A)"
    name: "Data backup plan (Required)"
    parent: "164.308(a)(7)"
  - code: "164.308(a)(7)(ii)(B)"
    name: "Disaster recovery plan (Required)"
    parent: "164.308(a)(7)"
  - code: "164.308(a)(7)(ii)(C)"
    name: "Emergency mode operation plan (Required)"
    parent: "164.308(a)(7)"
  - code: "164.308(a)(7)(ii)(D)"
    name: "Testing and revision procedures (Addressable)"
    parent: "164.308(a)(7)"
  - code: "164.308(a)(7)(ii)(E)"
    name: "Applications and data criticality analysis (Addressable)"
    parent: "164.308(a)(7)"
  - code: "164.308(a)(8)"
    name: "Evaluation (Standard; no separate specs)"
    parent: "164.308"
  - code: "164.308(b)(1)"
    name: "Business associate contracts and other arrangements (Standard)"
    parent: "164.308"
  - code: "164.308(b)(3)"
    name: "Written contract or other arrangement (Required)"
    parent: "164.308(b)(1)"
  # ——— §164.310 Physical safeguards: 4 standards ———
  - code: "164.310(a)(1)"
    name: "Facility access controls (Standard)"
    parent: "164.310"
  - code: "164.310(a)(2)(i)"
    name: "Contingency operations (Addressable)"
    parent: "164.310(a)(1)"
  - code: "164.310(a)(2)(ii)"
    name: "Facility security plan (Addressable)"
    parent: "164.310(a)(1)"
  - code: "164.310(a)(2)(iii)"
    name: "Access control and validation procedures (Addressable)"
    parent: "164.310(a)(1)"
  - code: "164.310(a)(2)(iv)"
    name: "Maintenance records (Addressable)"
    parent: "164.310(a)(1)"
  - code: "164.310(b)"
    name: "Workstation use (Standard; no separate specs)"
    parent: "164.310"
  - code: "164.310(c)"
    name: "Workstation security (Standard; no separate specs)"
    parent: "164.310"
  - code: "164.310(d)(1)"
    name: "Device and media controls (Standard)"
    parent: "164.310"
  - code: "164.310(d)(2)(i)"
    name: "Disposal (Required)"
    parent: "164.310(d)(1)"
  - code: "164.310(d)(2)(ii)"
    name: "Media re-use (Required)"
    parent: "164.310(d)(1)"
  - code: "164.310(d)(2)(iii)"
    name: "Accountability (Addressable)"
    parent: "164.310(d)(1)"
  - code: "164.310(d)(2)(iv)"
    name: "Data backup and storage (Addressable)"
    parent: "164.310(d)(1)"
  # ——— §164.312 Technical safeguards: 5 standards ———
  - code: "164.312(a)(1)"
    name: "Access control (Standard)"
    parent: "164.312"
  - code: "164.312(a)(2)(i)"
    name: "Unique user identification (Required)"
    parent: "164.312(a)(1)"
  - code: "164.312(a)(2)(ii)"
    name: "Emergency access procedure (Required)"
    parent: "164.312(a)(1)"
  - code: "164.312(a)(2)(iii)"
    name: "Automatic logoff (Addressable)"
    parent: "164.312(a)(1)"
  - code: "164.312(a)(2)(iv)"
    name: "Encryption and decryption (Addressable)"
    parent: "164.312(a)(1)"
  - code: "164.312(b)"
    name: "Audit controls (Standard; no separate specs)"
    parent: "164.312"
  - code: "164.312(c)(1)"
    name: "Integrity (Standard)"
    parent: "164.312"
  - code: "164.312(c)(2)"
    name: "Mechanism to authenticate electronic protected health information (Addressable)"
    parent: "164.312(c)(1)"
  - code: "164.312(d)"
    name: "Person or entity authentication (Standard; no separate specs)"
    parent: "164.312"
  - code: "164.312(e)(1)"
    name: "Transmission security (Standard)"
    parent: "164.312"
  - code: "164.312(e)(2)(i)"
    name: "Integrity controls (Addressable)"
    parent: "164.312(e)(1)"
  - code: "164.312(e)(2)(ii)"
    name: "Encryption (Addressable)"
    parent: "164.312(e)(1)"
  # ——— §164.314 Organizational requirements: 2 standards ———
  - code: "164.314(a)(1)"
    name: "Business associate contracts or other arrangements (Standard; specs Required)"
    parent: "164.314"
  - code: "164.314(b)(1)"
    name: "Requirements for group health plans (Standard; specs Required)"
    parent: "164.314"
  # ——— §164.316 Policies and procedures and documentation: 2 standards ———
  - code: "164.316(a)"
    name: "Policies and procedures (Standard)"
    parent: "164.316"
  - code: "164.316(b)(1)"
    name: "Documentation (Standard)"
    parent: "164.316"
  - code: "164.316(b)(2)(i)"
    name: "Time limit — retain 6 years (Required)"
    parent: "164.316(b)(1)"
  - code: "164.316(b)(2)(ii)"
    name: "Availability (Required)"
    parent: "164.316(b)(1)"
  - code: "164.316(b)(2)(iii)"
    name: "Updates (Required)"
    parent: "164.316(b)(1)"
urls:
  - label: "CFR-45-164-Subpart-C"
    url: "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C"
    status: 200
    checked: "2026-06-10"
  - label: "HIPAA-Security-NPRM-2025"
    url: "https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information"
    status: 200
    checked: "2026-06-10"
  - label: "NIST-SP-800-66r2"
    url: "https://csrc.nist.gov/pubs/sp/800/66/r2/final"
    status: 200
    checked: "2026-06-10"
  - label: "NIST-SP-800-66r2-PDF"
    url: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-66r2.pdf"
    status: 200
    checked: "2026-06-10"
  - label: "HHS-SRA-Tool"
    url: "https://www.healthit.gov/topic/privacy-security-and-hipaa/security-risk-assessment-tool"
    status: 200
    checked: "2026-06-10"
  - label: "PL-116-321"
    url: "https://www.govinfo.gov/content/pkg/PLAW-116publ321/html/PLAW-116publ321.htm"
    status: 200
    checked: "2026-06-10"
crosswalks: []
terminology:
  - term: "Addressable (≠ optional)"
    source_wording: "Assess whether each implementation specification is a reasonable and appropriate safeguard in its environment … Implement the implementation specification if reasonable and appropriate; or … Document why it would not be reasonable and appropriate … and Implement an equivalent alternative measure if reasonable and appropriate. (§164.306(d)(3))"
  - term: "Risk analysis"
    source_wording: "Conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of electronic protected health information held by the covered entity or business associate. (§164.308(a)(1)(ii)(A))"
  - term: "Security incident"
    source_wording: "the attempted or successful unauthorized access, use, disclosure, modification, or destruction of information or interference with system operations in an information system. (§164.304)"
  - term: "Encryption"
    source_wording: "the use of an algorithmic process to transform data into a form in which there is a low probability of assigning meaning without use of a confidential process or key. (§164.304)"
  - term: "Flexibility of approach factors"
    source_wording: "(i) The size, complexity, and capabilities … (ii) … technical infrastructure, hardware, and software security capabilities. (iii) The costs of security measures. (iv) The probability and criticality of potential risks to electronic protected health information. (§164.306(b)(2))"
  - term: "Documentation retention"
    source_wording: "Retain the documentation required by paragraph (b)(1) of this section for 6 years from the date of its creation or the date when it last was in effect, whichever is later. (§164.316(b)(2)(i))"
  - term: "Recognized security practices"
    source_wording: "PL 116-321 (approved Jan. 5, 2021; adds HITECH §13412, 42 U.S.C. 17941) — HHS 'shall consider' such practices in place for the previous 12 months when making certain penalty/audit determinations; mitigation, not immunity."
sign_off: true
```

## 1. Primary sources

| Source | What it is | Retrieval | Verbatim anchor |
|--------|-----------|-----------|-----------------|
| eCFR API XML, 45 CFR 164 Subpart C (as of 2026-06-09) | The regulation in force. Full text downloaded and transcribed mechanically. | 2026-06-10 | Subpart head: "Security Standards for the Protection of Electronic Protected Health Information"; Authority: "42 U.S.C. 1320d-2 and 1320d-4; sec. 13401, Pub. L. 111-5, 123 Stat. 260." |
| Federal Register API, RIN 0945-AA22 | NPRM docket. **Exactly one document exists: a Proposed Rule** (doc 2024-30983, pub. 2025-01-06). | 2026-06-10 | API result: type "Proposed Rule", title "HIPAA Security Rule To Strengthen the Cybersecurity of Electronic Protected Health Information". No document of type "Rule" under the RIN. |
| NIST SP 800-66r2 (csrc.nist.gov + PDF) | Current implementation guide. | 2026-06-10 | "02/14/24: SP 800-66 Rev. 2 (Final)" … "Supersedes: SP 800-66 Rev. 1 (10/23/2008)" |
| PL 116-321 (govinfo statute text) | Recognized-security-practices amendment to HITECH. | 2026-06-10 | "<<NOTE: Jan. 5, 2021 - [H.R. 7898]>>" … adds "SEC. 13412. <<NOTE: 42 USC 17941.>> RECOGNITION OF SECURITY PRACTICES." |
| eCFR API XML, 45 CFR Part 102 (as of 2026-06-09) | Current civil monetary penalty amounts (annually adjusted). | 2026-06-10 | Table 1 to §102.3 rows for 42 U.S.C. 1320(d)-5(a) / 45 CFR 160.404(b)(2) |

Amendment history (from the eCFR section source notes — Tier 1): every section's most recent
amendment is 78 FR 5693–5695 (Jan. 25, 2013) or 78 FR 34266 (June 7, 2013). **No section of
Subpart C has been amended since June 2013.** The 2025 NPRM has not been codified.

## 2. Structural inventory

Transcribed mechanically from the downloaded eCFR XML (see §0 `identifiers` for the full list).

| Section | Standards | Titled impl. specs | Required | Addressable |
|---------|-----------|--------------------|----------|-------------|
| §164.308 Administrative safeguards | 9 | 21 | 10 | 11 |
| §164.310 Physical safeguards | 4 | 8 | 2 | 6 |
| §164.312 Technical safeguards | 5 | 7 | 2 | 5 |
| **Appendix A matrix subtotal** | **18** | **36** | **14** | **22** |
| §164.314 Organizational requirements | 2 | (specs designated "(Required)" inline) | — | — |
| §164.316 Policies/procedures & documentation | 2 | 3 (documentation) | 3 | 0 |
| **Subpart C total** | **22** | | | |

**Counting-convention trap (must be stated wherever a count appears):** Appendix A prints an
`(R)` in the implementation-specifications column for the 6 standards that have no separately
titled specs (Assigned security responsibility, Evaluation, Workstation use, Workstation
security, Audit controls, Person or entity authentication). Counting those entries gives the
widely cited "42 implementation specifications — 20 Required / 22 Addressable." Counting only
the *titled* specs in the regulatory text gives 36 — 14 R / 22 A. Both are defensible; the
skill must label which convention it uses and never mix them.

**Source-rendering artifacts (recorded so verifiers don't trip on them):**
- §164.308(b)(1) (Business associate contracts) does not carry the "Standard:" prefix in the
  body text — a naive `Standard:` grep finds 8 administrative standards, not 9. Appendix A
  lists it as the 9th administrative standard.
- In the eCFR XML rendering of the Appendix A matrix, the "(A)" designation for *Workforce
  clearance procedure* is dropped/merged in the table cell (body (A) marks count 21, not 22).
  The regulatory text controls: §164.308(a)(3)(ii)(B) is explicitly "(Addressable)".
- The matrix legend line ("(R) = Required, (A) = Addressable") contributes one extra (R) and
  (A) to any naive grep of the appendix.

Other inventory facts (Tier 1 from the same XML):
- §164.304 defines **17 terms** (Access; Administrative safeguards; Authentication; Availability; Confidentiality; Encryption; Facility; Information system; Integrity; Malicious software; Password; Physical safeguards; Security or Security measures; Security incident; Technical safeguards; User; Workstation).
- §164.306(a) lists **4 general requirements**; §164.306(b)(2) lists **4 flexibility factors**.
- §164.306(d)(3) is the addressable-specification decision logic (assess → implement, or document why not + equivalent alternative measure if reasonable and appropriate).
- §164.318 compliance dates (April 20, 2005 / small health plans April 20, 2006) are historical only.

## 3. Crosswalk mappings

**v1 of this skill encodes NO crosswalk rows.** The authoritative mapping (Security Rule
standards/specs → NIST CSF subcategories → SP 800-53r5 controls) was **removed from SP 800-66r2
and placed online in the NIST CPRT** — verbatim from the PDF (Appendix D, p. 105): "the mapping
table has been removed from the document and placed online in the NIST Cybersecurity and
Privacy Reference Tool (CPRT)." Two consequences, recorded so they are never silently violated:

1. The CPRT mapping targets **CSF v1.1**, and per the PDF it "was intentionally broad and
   includes mappings to Subcategories that both directly and indirectly align." The skill must
   never claim an 800-66r2 mapping to **CSF 2.0**.
2. Row-level crosswalk encoding is **SOX-638 scope** (nist-800-53-rmf HIPAA crosswalk
   completion): extract from CPRT, verify per-row, then encode in both skills in the same pass.
   CPRT JSON endpoints were not fetchable on 2026-06-10 (probed; 404) — extraction method TBD
   at SOX-638 time (CPRT UI export or OLIR catalog).

The skill's chunks will point to CPRT and the OLIR program as the places to obtain mappings,
without asserting any row.

## 4. URL verification — every manifest citation

All URLs in §0 returned HTTP 200 via curl on 2026-06-10. Known bot-walls (HTTP 403 to
programmatic clients; consistent with the M2 registry sweep) — cite in prose with this caveat,
do NOT put in the gate-checked URL table:

- `hhs.gov/hipaa/for-professionals/security/hipaa-security-rule-nprm/index.html` (OCR NPRM page)
- `hhs.gov/hipaa/for-professionals/compliance-enforcement/audit/protocol/index.html` (OCR audit protocol)

The Federal Register document page substitutes for the OCR NPRM page as the gate-checked source.

## 5. Terminology — exact wording from the source

See §0 `terminology` block (verbatim quotes with citations). Additional usage rules:

- "**Addressable**" never means optional. The §164.306(d)(3) decision logic is the only correct
  gloss. OCR's own guidance phrase is "addressable does not mean optional."
- The regulated parties are "**covered entity or business associate**" throughout the
  post-Omnibus text — BAs are directly liable for Security Rule compliance (since 78 FR 5566).
- "**ePHI**" = electronic protected health information; the Security Rule covers ePHI only
  (the Privacy Rule covers PHI in all forms).
- The §164.304 definition list is closed — do not attribute definitions of "breach,"
  "unsecured PHI," etc. to Subpart C (those live in Subpart D, §164.402).

## 6. Version and supersession

- **In force:** 45 CFR 164 Subpart C as amended through 78 FR 34266 (June 7, 2013). Original
  rule 68 FR 8376 (Feb. 20, 2003); HITECH Omnibus amendments 78 FR 5566 (Jan. 25, 2013).
- **PROPOSED, NOT FINAL (verified 2026-06-10 at the docket level):** "HIPAA Security Rule To
  Strengthen the Cybersecurity of Electronic Protected Health Information," 90 FR 898
  (Jan. 6, 2025), RIN 0945-AA22. The Federal Register API shows exactly one document under the
  RIN — type "Proposed Rule." Headline proposals (for the skill's "what may change" content,
  always flagged PROPOSED): removal of the required/addressable distinction (all specs
  required with limited exceptions), mandatory encryption at rest and in transit, MFA,
  vulnerability scanning/penetration testing cadences, asset inventory and network map,
  annual compliance audits. The skill must re-verify NPRM status at every G4 pass — a final
  rule may drop at any time.
- **Implementation guide:** NIST SP 800-66 Rev. 2 (Final, 02/14/2024) — supersedes Rev. 1
  (10/23/2008). Do not cite Rev. 1.
- **Statutory layer:** HITECH Act (Pub. L. 111-5, §13401 — BA direct liability, cited in the
  subpart's authority note); PL 116-321 (Jan. 5, 2021) — recognized security practices
  (HITECH §13412, 42 U.S.C. 17941). **Known error in a primary-adjacent source:** SP 800-66r2
  footnote 9 states PL 116-321 was "signed into law on January 5, 2020" — the statute itself
  says Jan. 5, 2021. Cite the statute, not the footnote.
- **Penalties (45 CFR 160.404 amounts as adjusted by 45 CFR 102.3, "2025 Maximum adjusted
  penalty" column, retrieved 2026-06-10):** Tier 1 (did not/could not know) min $145, max
  $73,011; Tier 2 (reasonable cause) min $1,461, max $73,011; Tier 3 (willful neglect,
  corrected ≤30 days) min $14,602, max $73,011; Tier 4 (willful neglect, uncorrected)
  min $73,011, max $2,190,294; calendar-year cap $2,190,294 per provision (all tiers).
  Amounts adjust annually — the skill states the as-of date and points to 45 CFR 102.3.
  Note: OCR's 2019 Notification of Enforcement Discretion announced lower annual caps for
  tiers 1–3; it is enforcement posture, not codified — label it as such if mentioned.

## 7. Scope boundaries — what the skill does NOT cover

- **Privacy Rule (Subpart E)** and **Breach Notification Rule (Subpart D)** — touchpoint-only:
  §164.314(a)(2)(i)(C) requires BA contracts to cover §164.410 breach reporting; breach
  notification mechanics (§§164.404/406/408/410) stay in scope of a future skill. Verified
  facts available in the library: §164.404 individuals / §164.406 media / §164.408 Secretary.
- **The 2025 NPRM is described only as PROPOSED** — no chunk may present an NPRM requirement
  as current law.
- **State law preemption, 42 CFR Part 2, FTC Health Breach Notification Rule** — out of scope.
- **Crosswalk rows** — none in v1 (see §3; SOX-638).
- **OCR audit protocol** — referenced in prose (bot-walled URL); the skill does not reproduce
  protocol line items.

## 8. Sign-off — Day 0 research complete

- [x] Full Subpart C inventory transcribed mechanically from official eCFR XML (2026-06-09 point-in-time, retrieved 2026-06-10)
- [x] Every count in §0 computed from the transcription, both counting conventions documented
- [x] All 61 identifiers listed with exact CFR cites and (R)/(A) designations (22 standards + 36 matrix-titled specs + 3 §164.316(b)(2) documentation specs)
- [x] NPRM status settled at the docket level (RIN query — Proposed Rule only, no final rule)
- [x] SP 800-66r2 currency verified (Final, supersedes Rev 1); its footnote-9 date error documented
- [x] PL 116-321 verified against statute text (Jan. 5, 2021)
- [x] Penalty amounts pinned to the 2025 adjustment column with as-of date
- [x] All 6 gate URLs return 200; hhs.gov bot-walls documented and excluded
- [x] Crosswalk deferral decision recorded (no rows in v1; SOX-638)
- [x] `python3 tools/check_fact_sheet.py docs/hipaa-security-rule-fact-sheet.md` passes
