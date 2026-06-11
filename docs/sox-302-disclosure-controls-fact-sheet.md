# Fact Sheet — sox-302-disclosure-controls (Day 0, SOX-570)

> Pre-build research per `docs/fact-sheet-template.md`. All sources are **public-domain US
> federal text** (statute + eCFR + SEC releases) — fully machine-verifiable; verbatim extracts
> are vendored at `docs/builds/sox-570/sec-source-extracts.json` (license class: public, like
> the eCFR HIPAA build). The skill covers SOX §302 Disclosure Controls & Procedures (DC&P)
> certification — distinct from the §404/ICFR work in coso-internal-controls.

## 0. Machine-readable data block (REQUIRED — the G1 gate parses this)

```yaml
fact_sheet:
  skill_slug: sox-302-disclosure-controls
  framework: "SOX §302 Disclosure Controls & Procedures — 15 U.S.C. 7241; SEC Rules 17 CFR 240.13a-14 / 240.13a-15; Reg S-K Items 307, 308, 601(b)(31)"
  version: "Current eCFR (Title 17, 2026-06-09 issue) + 15 U.S.C. 7241; SOX 2002, implementing rules 2002-2003 as amended through 72 FR 35321 (2007)"
  version_date: "2007-06-27"
  supersedes: "n/a (original SOX §302 implementing rules 2002, amended 2003/2005/2006/2007)"
  retrieval_date: "2026-06-11"
  researcher: "Claude (Fable 5) dispatcher — eCFR XML + uscode.house.gov + SEC releases"
counts:
  certification_elements_302a: 6        # 15 U.S.C. 7241(a)(1)-(6)
  cert_paragraphs_in_exhibit: 6         # the numbered paragraphs in the 13a-14(a) exhibit certification
  implementing_rules_core: 4            # 13a-14, 13a-15(b) DC&P eval, 13a-15(e) DC&P def, 13a-15(f) ICFR def
  reg_sk_items: 3                       # Item 307 (DC&P disclosure), Item 308 (ICFR), 601(b)(31) (cert exhibit)
  signing_officers: 2                   # principal executive officer + principal financial officer
  dcp_eval_frequency_quarterly: 1       # 13a-15(b): each fiscal quarter (FPI: each fiscal year)
identifiers:
  - code: "15 U.S.C. 7241"
    name: "SOX §302 — Corporate responsibility for financial reports (the 6-element certification mandate)"
    parent: "Sarbanes-Oxley Act of 2002"
  - code: "17 CFR 240.13a-14"
    name: "Certification of disclosure in annual and quarterly reports (PEO + PFO sign; filed as an exhibit)"
    parent: "Securities Exchange Act rules"
  - code: "17 CFR 240.13a-15(b)"
    name: "Management evaluation of DC&P effectiveness as of the end of each fiscal quarter (FPI: each fiscal year)"
    parent: "17 CFR 240.13a-15"
  - code: "17 CFR 240.13a-15(c)"
    name: "Management annual evaluation of ICFR effectiveness"
    parent: "17 CFR 240.13a-15"
  - code: "17 CFR 240.13a-15(e)"
    name: "Definition: disclosure controls and procedures (DC&P) — broader than ICFR"
    parent: "17 CFR 240.13a-15"
  - code: "17 CFR 240.13a-15(f)"
    name: "Definition: internal control over financial reporting (ICFR)"
    parent: "17 CFR 240.13a-15"
  - code: "Reg S-K Item 307"
    name: "17 CFR 229.307 — disclose officers' conclusions on DC&P effectiveness"
    parent: "Regulation S-K"
  - code: "Reg S-K Item 308"
    name: "17 CFR 229.308 — management ICFR report (a) and ICFR changes (c)"
    parent: "Regulation S-K"
  - code: "Reg S-K Item 601(b)(31)"
    name: "17 CFR 229.601(b)(31) — the Rule 13a-14(a) certification exhibit form"
    parent: "Regulation S-K"
  - code: "Cert ¶1"
    name: "The signing officer has reviewed the report"
    parent: "13a-14(a) exhibit certification"
  - code: "Cert ¶2"
    name: "Based on knowledge, no untrue statement of material fact / no material omission"
    parent: "13a-14(a) exhibit certification"
  - code: "Cert ¶3"
    name: "Based on knowledge, the financial statements fairly present in all material respects"
    parent: "13a-14(a) exhibit certification"
  - code: "Cert ¶4"
    name: "Officers are responsible for, and have designed/evaluated, DC&P and ICFR"
    parent: "13a-14(a) exhibit certification"
  - code: "Cert ¶5"
    name: "Officers have disclosed to auditors and audit committee all ICFR significant deficiencies/material weaknesses and any fraud involving management"
    parent: "13a-14(a) exhibit certification"
  - code: "8-K Item 1.05"
    name: "Material cybersecurity incident — 4 business days from materiality determination (a DC&P touchpoint: non-financial timely disclosure)"
    parent: "Form 8-K"
urls:
  - label: "SOX-302-Statute-15USC7241"
    url: "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section7241&num=0&edition=prelim"
    status: 200
    checked: "2026-06-11"
  - label: "CFR-17-240.13a-14"
    url: "https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.13a-14"
    status: 200
    checked: "2026-06-11"
  - label: "CFR-17-240.13a-15"
    url: "https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.13a-15"
    status: 200
    checked: "2026-06-11"
  - label: "Reg-S-K-Item-307"
    url: "https://www.ecfr.gov/current/title-17/chapter-II/part-229/section-229.307"
    status: 200
    checked: "2026-06-11"
  - label: "Reg-S-K-Item-308"
    url: "https://www.ecfr.gov/current/title-17/chapter-II/part-229/section-229.308"
    status: 200
    checked: "2026-06-11"
crosswalks: []
terminology:
  - term: "Disclosure controls and procedures (DC&P) — verbatim 13a-15(e)"
    source_wording: "controls and other procedures of an issuer that are designed to ensure that information required to be disclosed by the issuer in the reports that it files or submits under the Act is recorded, processed, summarized and reported, within the time periods specified … [and] is accumulated and communicated to the issuer's management … as appropriate to allow timely decisions regarding required disclosure."
  - term: "ICFR — verbatim 13a-15(f)"
    source_wording: "a process designed by, or under the supervision of, the issuer's principal executive and principal financial officers … to provide reasonable assurance regarding the reliability of financial reporting and the preparation of financial statements for external purposes in accordance with [GAAP] …"
  - term: "DC&P is BROADER than ICFR (the skill's spine)"
    source_wording: "DC&P covers ALL information required to be disclosed in Exchange Act reports (financial AND non-financial — e.g., risk factors, legal proceedings, cyber 8-K). ICFR is limited to the reliability of financial reporting. ICFR is a subset of DC&P for financial-statement matters; DC&P adds the non-financial disclosure universe. (SEC Release 33-8238 discusses the overlap; the rule texts define each.)"
  - term: "Section 302 vs Section 404"
    source_wording: "§302 = officer CERTIFICATION (quarterly + annual) covering DC&P and ICFR conclusions, filed as a 601(b)(31) exhibit. §404 = management's ANNUAL ICFR assessment (Item 308(a)) plus, for accelerated/large accelerated filers, the auditor's ICFR attestation (AS 2201). §302 is quarterly and officer-signed; §404(a)/(b) is annual and assessment/attestation-based."
  - term: "Disclosure committee — practice, not a rule mandate"
    source_wording: "The SEC RECOMMENDED (did not mandate) a disclosure committee in the 2002 adopting release (33-8124). The skill must label the disclosure committee and the sub-certification cascade as recommended practice / house framework, NOT a rule requirement."
sign_off: true
```

## 1. Primary sources

| Source | What | Retrieval | Anchor |
|--------|------|-----------|--------|
| 15 U.S.C. 7241 (uscode.house.gov) | SOX §302 statute — the 6-element certification mandate | 2026-06-11 | "(a) … certify … that—(1) the signing officer has reviewed the report; (2) … no untrue statement of a material fact …" |
| 17 CFR 240.13a-14 (eCFR XML) | Who signs (PEO + PFO), filed as an exhibit | 2026-06-11 | "Each principal executive and principal financial officer … must sign a certification." |
| 17 CFR 240.13a-15(b)/(e)/(f) (eCFR XML) | Quarterly DC&P evaluation; DC&P definition; ICFR definition | 2026-06-11 | verbatim quotes in §0 terminology |
| Reg S-K Item 307 / 308 (eCFR XML) | DC&P disclosure; ICFR report + changes | 2026-06-11 | "Disclose the conclusions … regarding the effectiveness of … disclosure controls and procedures (as defined in § 240.13a-15(e))" |
| Reg S-K Item 601(b)(31) (eCFR XML) | The certification exhibit form | 2026-06-11 | "(31)(i) Rule 13a-14(a)/15d-14(a) Certifications" |

Public extracts vendored at `docs/builds/sox-570/sec-source-extracts.json` (US federal text,
public domain — full vendoring permitted, unlike the licensed PCI/ISO builds).

## 2. Structural inventory

The §302 certification (13a-14(a) exhibit, mirroring 15 U.S.C. 7241(a)) has **6 numbered
paragraphs**; the statute lists **6 certification elements**. Core implementing rules: **4**
(13a-14; 13a-15(b) DC&P eval; 13a-15(e) DC&P def; 13a-15(f) ICFR def). Reg S-K items: **3**
(307, 308, 601(b)(31)). **2 signing officers** (PEO + PFO). DC&P evaluation frequency:
**each fiscal quarter** (foreign private issuers: each fiscal year).

**The boundary the skill exists to teach:** DC&P (302) ⊃ ICFR (404) for financial matters, and
DC&P additionally covers the **non-financial** disclosure universe (risk factors, legal
proceedings, MD&A, cyber 8-K Item 1.05). A material weakness in ICFR is also a DC&P matter; but
a DC&P failure (e.g., a missed cyber 8-K) need not be an ICFR failure.

## 3. Crosswalk mappings

None encoded in v1. The natural cross-reference is to **coso-internal-controls** (the §404/ICFR
skill — the dependency named in the ticket) and to **nist-csf-2 / hipaa** for the cyber-8-K
DC&P touchpoint. One-way prose references only; no rows.

## 4. URL verification

The five gate URLs returned 200 on 2026-06-11. Known bot-wall: **sec.gov** rejects programmatic
clients (use eCFR for rule text and uscode.house.gov for the statute; cite SEC release numbers in
prose). The certification exhibit text is reproduced from the public 601(b)(31) / form
instructions.

## 5. Terminology

See §0. Usage rules: DC&P ≠ ICFR (the #1 confusion); the disclosure committee and sub-
certification cascade are **recommended practice / house framework**, not rule requirements
(label everywhere); "302 vs 404" must be stated precisely (quarterly cert vs annual assessment +
attestation). Cyber 8-K Item 1.05 = **4 business days from the materiality determination** (a
verified library fact; a DC&P timeliness touchpoint, not an ICFR matter).

## 6. Version and supersession (verified 2026-06-11)

- SOX §302 enacted 2002; implementing rules adopted 2002-2003 (33-8124, 33-8238), amended through
  72 FR 35321 (June 27, 2007). The eCFR Title-17 2026-06-09 issue is current.
- No pending change to 13a-14/13a-15 or Items 307/308 found as of 2026-06-11 (re-verify at G4).
- Cyber disclosure (33-11216, 2023) added 8-K Item 1.05 and Reg S-K Item 106 — a DC&P scope
  expansion for non-financial timely disclosure; relevant to B26.

## 7. Scope boundaries — what the skill does NOT cover

- **§404 ICFR assessment/attestation mechanics** — that is coso-internal-controls; this skill
  references the boundary, does not re-teach §404.
- **§906 criminal certification** (18 U.S.C. 1350) — mention as the companion cert, do not detail.
- Auditor attestation standards (AS 2201) — pointer only.
- No legal advice; the disclosure-committee charter and sub-cert cascade are templates/house
  framework, explicitly labeled.

## 8. Sign-off — Day 0 research complete

- [x] All primary sources fetched from public federal text (statute + eCFR); verbatim DC&P/ICFR
      definitions captured; extracts vendored (public domain)
- [x] 6-element certification structure verified against 15 U.S.C. 7241(a) and the 601(b)(31) exhibit
- [x] DC&P-vs-ICFR boundary (the skill's spine) grounded in the verbatim (e)/(f) definitions
- [x] Disclosure committee + sub-cert cascade flagged as recommended practice, not rule
- [x] Gate URLs 200; sec.gov bot-wall documented (eCFR/uscode substitutes)
- [x] Currency: rules current through 2007 amendments; 2023 cyber additions noted; no pending change
- [x] `python3 tools/check_fact_sheet.py docs/sox-302-disclosure-controls-fact-sheet.md` passes
