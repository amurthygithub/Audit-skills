---
chunk_id: 02-dcp-vs-icfr
parent_skill: sox-302-disclosure-controls
topic: "The spine: verbatim DC&P (13a-15(e)) and ICFR (13a-15(f)) definitions; DC&P ⊃ ICFR for financial matters plus the non-financial universe; why a DC&P failure need not be an ICFR failure"
load_when: "user asks the difference between disclosure controls and ICFR, what DC&P covers, the scope of disclosure controls, the Venn relationship, or whether a disclosure failure is an internal-control failure"
---

# Chunk 02 — DC&P vs ICFR (the spine)

This is the most-confused distinction in §302 work. **DC&P and ICFR are two distinct, separately defined control sets.** Both are defined in Rule 17 CFR 240.13a-15, and both are evaluated and certified — but their **scope** differs, and that difference drives every downstream conclusion. Quote the definitions; do not paraphrase them.

## 1. Disclosure controls and procedures (DC&P) — §240.13a-15(e), verbatim

> "For purposes of this section, the term disclosure controls and procedures means controls and other procedures of an issuer that are designed to ensure that information required to be disclosed by the issuer in the reports that it files or submits under the Act (15 U.S.C. 78a et seq.) is recorded, processed, summarized and reported, within the time periods specified in the Commission's rules and forms. Disclosure controls and procedures include, without limitation, controls and procedures designed to ensure that information required to be disclosed by an issuer in the reports that it files or submits under the Act is accumulated and communicated to the issuer's management, including its principal executive and principal financial officers, or persons performing similar functions, as appropriate to allow timely decisions regarding required disclosure." [CFR-17-240.13a-15 §e]

The operative phrase is **"information required to be disclosed … in the reports that it files or submits under the Act."** That is the **entire** universe of Exchange Act disclosure — financial AND non-financial.

## 2. Internal control over financial reporting (ICFR) — §240.13a-15(f), verbatim

> "The term internal control over financial reporting is defined as a process designed by, or under the supervision of, the issuer's principal executive and principal financial officers, or persons performing similar functions, and effected by the issuer's board of directors, management and other personnel, to provide reasonable assurance regarding the reliability of financial reporting and the preparation of financial statements for external purposes in accordance with generally accepted accounting principles and includes those policies and procedures that: (1) Pertain to the maintenance of records that in reasonable detail accurately and fairly reflect the transactions and dispositions of the assets of the issuer; (2) Provide reasonable assurance that transactions are recorded as necessary to permit preparation of financial statements in accordance with generally accepted accounting principles, and that receipts and expenditures of the issuer are being made only in accordance with authorizations of management and directors of the issuer; and (3) Provide reasonable assurance regarding prevention or timely detection of unauthorized acquisition, use or disposition of the issuer's assets that could have a material effect on the financial statements." [CFR-17-240.13a-15 §f]

The operative phrase is **"reasonable assurance regarding the reliability of financial reporting."** ICFR is bounded by **financial** reporting.

## 3. The relationship: ICFR is the financial-reporting subset of DC&P

- **DC&P is broader.** It spans all information required to be disclosed in Exchange Act reports — including non-financial disclosures: risk factors (Item 105), legal proceedings (Item 103), MD&A (Item 303), executive compensation, and timely 8-K events such as a material cybersecurity incident (8-K Item 1.05).
- **ICFR is narrower.** It is limited to the reliability of financial reporting and the preparation of GAAP financial statements.
- **Venn picture:** ICFR sits **inside** DC&P for the financial-statement universe; DC&P **adds** the non-financial disclosure universe on top. SEC Release 33-8238 discusses this overlap; the rule texts above define each set. There is overlap (financial-statement disclosures depend on both), but the sets are not equal.

```
+--------------------- DC&P (13a-15(e)) ----------------------+
|  All info required to be disclosed in Exchange Act reports  |
|                                                            |
|   +------------- ICFR (13a-15(f)) -------------+           |
|   |  Reliability of financial reporting only   |           |
|   +--------------------------------------------+           |
|                                                            |
|   Non-financial: risk factors, legal proceedings, MD&A,    |
|   exec comp, cyber 8-K (Item 1.05) — DC&P only             |
+------------------------------------------------------------+
```

## 4. Why a DC&P failure need not be an ICFR failure (and vice versa)

- **DC&P failure that is NOT an ICFR failure:** a material cybersecurity incident that should have triggered an 8-K Item 1.05 within 4 business days but did not (a timely-disclosure breakdown over a **non-financial** item) is a **DC&P** failure. It does not touch the reliability of financial reporting, so it need not be an ICFR material weakness. See `chunks/07-material-weakness-and-change.md`.
- **ICFR failure that IS also a DC&P matter:** a material weakness in ICFR over a financially significant, disclosure-relevant area is also a **DC&P** matter — the financial information was not reliably processed for disclosure, so officers generally cannot conclude DC&P is effective for that area. The MW-to-DC&P-conclusion logic lives in `chunks/07`.
- These are independent determinations. Evaluate DC&P against the full disclosure universe and ICFR against financial-reporting reliability; do not assume one conclusion follows automatically from the other.

## 5. Anti-hallucination

- **Never treat DC&P and ICFR as interchangeable.** DC&P (§240.13a-15(e)) = all required disclosure (financial + non-financial); ICFR (§240.13a-15(f)) = reliability of financial reporting only [CFR-17-240.13a-15 §e] [CFR-17-240.13a-15 §f].
- **ICFR is a subset of DC&P** for financial matters; DC&P adds the non-financial universe. Do not say ICFR is broader, or that they are the same.
- A missed cyber 8-K is a **DC&P** matter, never an ICFR matter. An ICFR material weakness over a disclosure-relevant area is **also** a DC&P matter.
