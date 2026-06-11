---
uc_id: UC-01
title: "Accelerated filer Q3 10-Q with a new unremediated ICFR material weakness — the §302 DC&P conclusion turns 'not effective', the ¶5 disclosure fires, and a 14-owner sub-cert cascade rolls up to 1 exception / 13 clean"
industries: [financial-services]
frameworks: [SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15, Reg-S-K-Item-307, Reg-S-K-Item-308]
inputs:
  filer: "Crestline Financial Corp — accelerated filer, Q3 Form 10-Q"
  material_weakness: "one unremediated ICFR material weakness — ITGC logical access to the revenue system; affects a disclosure-relevant area (data/seeds/uc-01-input.json)"
  sub_certifications: "14 process-owner sub-certifications, each clean or exception (data/seeds/uc-01-input.json)"
  as_of_date: "2026-09-30"
procedure:
  - "chunks/02-dcp-vs-icfr.md — Locate the material weakness in the DC&P/ICFR Venn: an ICFR material weakness over a financially significant, disclosure-relevant area is also a DC&P matter [CFR-17-240.13a-15 §240.13a-15(e)/(f)]."
  - "chunks/07-material-weakness-and-change.md — Apply the conclusion logic: an unremediated material weakness in a disclosure-relevant area means DC&P cannot be concluded effective; derive the §302 effectiveness conclusion from the MW facts, not from a default."
  - "chunks/04-evaluation-and-disclosure.md — Disclose the DC&P conclusion under Item 307 [Reg-S-K-Item-307 §229.307] and the ICFR material weakness under Item 308 [Reg-S-K-Item-308 §229.308]; the quarterly evaluation [CFR-17-240.13a-15 §240.13a-15(b)] is the evidence base."
  - "chunks/03-the-six-certifications.md — Fire the cert ¶5 disclosure: the officers disclose all significant deficiencies and material weaknesses (and any management fraud) to the auditors and the audit committee [SOX-302-Statute-15USC7241 §7241(a)(5); CFR-17-240.13a-14 §240.13a-14(a)]."
  - "chunks/06-disclosure-committee-subcert.md — Roll up the 14 sub-certifications (house framework): count exceptions, decide whether the top-level cert is clean."
  - "chunks/05-section-302-vs-404.md — Show the 302-vs-404 interplay: the same MW hits the §302 DC&P cert this quarter and the annual §404 management assessment / auditor attestation."
  - "SKILL.md §1–§11 — route the engagement through the §302 procedure (overview, the two boundaries, the six certifications, evaluation, the cascade, MW-and-change)."
expected_outputs:
  classification: "DCP_NOT_EFFECTIVE"
  dcp_conclusion: "not effective"
  par5_disclosure_required: true
  subcert_total: 14
  subcert_exceptions: 1
  subcert_clean: 13
  top_level_cert_clean: false
oracle:
  - "dcp_conclusion derived from the MW facts via the §240.13a-15(e)/Item 307 logic (affects_disclosure_relevant_area AND not remediated -> not effective) == 'not effective'; classification == DCP_NOT_EFFECTIVE"
  - "par5_disclosure_required == True — the existence of a material weakness triggers the 15 U.S.C. 7241(a)(5) disclosure to auditors and audit committee"
  - "subcert_total == 14 (recounted from the sub_certifications list); subcert_exceptions == 1 (the IT/ITGC owner); subcert_clean == 13; the three foot to 14"
  - "top_level_cert_clean == False — a non-effective DC&P conclusion or any exception in the cascade defeats a clean top-level cert"
  - "expected-seed agreement: uc-01-expected.json fields equal the recomputed values"
data_refs:
  - data/seeds/uc-01-input.json
  - data/seeds/uc-01-expected.json
tests:
  - tests/test_sox_302_disclosure_controls_oracle.py::test_uc_01_oracle
  - tests/test_sox_302_disclosure_controls_metamorphic.py::test_uc01_subcert_order_invariance
  - tests/test_sox_302_disclosure_controls_metamorphic.py::test_uc01_remediated_mw_flips_dcp_conclusion
  - tests/test_sox_302_disclosure_controls_adversarial.py::test_uc01_missing_mw_facts_refuses
  - tests/test_sox_302_disclosure_controls_adversarial.py::test_uc01_unremediated_mw_forces_not_effective
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-01 — Material-weakness interplay and the sub-cert cascade (Crestline Financial Corp)

## §1 Context and persona

**Crestline Financial Corp** is a fictional accelerated filer preparing its **Q3 Form 10-Q**. During the quarter, management identified a new **ICFR material weakness**: a breakdown in IT general controls over **logical access to the revenue system** — segregation-of-duties and privileged-access controls that failed in a way that could permit unauthorized changes to revenue data. The material weakness is **unremediated** as of the period end and **affects a disclosure-relevant area** (revenue, the line most material to this issuer's reports).

The persona is the **controller / SEC-reporting manager** who owns the §302 certification process and must decide three things this quarter: (1) what the officers conclude about disclosure controls and procedures (DC&P) effectiveness, (2) whether the cert ¶5 disclosure to the auditors and the audit committee fires, and (3) whether the 14-owner sub-certification cascade rolls up clean. The seed `data/seeds/uc-01-input.json` is the tested fixture; every number below is recomputed from it by `tests/test_sox_302_disclosure_controls_oracle.py::test_uc_01_oracle`.

## §2 The material weakness is a DC&P matter, not only an ICFR matter

DC&P and ICFR are different controls universes. ICFR is "a process … to provide reasonable assurance regarding the reliability of financial reporting" [CFR-17-240.13a-15 §240.13a-15(f)]. DC&P is broader — controls "designed to ensure that information required to be disclosed … is recorded, processed, summarized and reported, within the time periods specified" and "accumulated and communicated to … management … to allow timely decisions regarding required disclosure" [CFR-17-240.13a-15 §240.13a-15(e)]. For **financial-statement matters, ICFR is a subset of DC&P**: a material weakness in ICFR over a financially significant, disclosure-relevant area is therefore *also* a DC&P deficiency.

That is the controlling fact here. The ITGC logical-access weakness over the revenue system is an ICFR material weakness, and because revenue is a disclosure-relevant area, it sits inside the DC&P universe too. The officers cannot conclude DC&P is effective while a material weakness over a disclosure-relevant area is unremediated.

## §3 The §302 DC&P conclusion — derived 'not effective'

The conclusion is **derived from the MW facts, not defaulted**. The rule the engagement applies: an **unremediated** material weakness that **affects a disclosure-relevant area** means DC&P is **not effective** for that area, so the officers conclude DC&P **not effective** and disclose that conclusion under Item 307 [Reg-S-K-Item-307 §229.307]. The ICFR material weakness itself is disclosed under Item 308 [Reg-S-K-Item-308 §229.308].

**DC&P conclusion: not effective** (classification `DCP_NOT_EFFECTIVE`).

The derivation is fact-driven, which the metamorphic test proves: if the material weakness were marked **remediated**, the same logic flips the conclusion to **effective** (`test_uc01_remediated_mw_flips_dcp_conclusion`). The conclusion is not a stored label — it is recomputed each time from `affects_disclosure_relevant_area` and `remediated`.

## §4 The cert ¶5 disclosure fires

Cert ¶5 of the §302 certification requires the signing officers to have disclosed, to the issuer's auditors and the audit committee, **all significant deficiencies and material weaknesses** in the design or operation of ICFR, and **any fraud** (whether or not material) that involves management or other employees with a significant role in ICFR [SOX-302-Statute-15USC7241 §7241(a)(5)]. The PEO and the PFO are the two signing officers [CFR-17-240.13a-14 §240.13a-14(a)].

A material weakness exists this quarter, so the ¶5 disclosure obligation is **triggered**: `par5_disclosure_required == True`. The oracle keys this to the *existence* of an MW — not to the DC&P conclusion — because ¶5 fires for any significant deficiency or material weakness regardless of whether DC&P is ultimately concluded effective.

## §5 The 14-owner sub-cert cascade rolls up to 1 exception / 13 clean

Crestline runs a **sub-certification cascade** — a **house framework, not a rule requirement** (the SEC *recommended* a disclosure committee in Release 33-8124; it did not mandate sub-certifications). Fourteen process owners each sub-certify clean or exception up to the PEO/PFO:

| # | Process owner | Sub-cert status |
|---|---------------|-----------------|
| 1 | Revenue | clean |
| 2 | AR/Collections | clean |
| 3 | Inventory | clean |
| 4 | Payroll | clean |
| 5 | Treasury | clean |
| 6 | Tax | clean |
| 7 | IT/ITGC | **exception** — ITGC access MW, see remediation plan |
| 8 | Legal | clean |
| 9 | HR | clean |
| 10 | Procurement | clean |
| 11 | FP&A | clean |
| 12 | External Reporting | clean |
| 13 | Investor Relations | clean |
| 14 | Internal Audit | clean |

**Roll-up: 14 total — 1 exception / 13 clean.** The single exception is the **IT/ITGC** owner, who carries the ITGC logical-access material weakness. Because the DC&P conclusion is not effective and the cascade carries an exception, the **top-level cert is NOT clean** (`top_level_cert_clean == False`). Reversing the order of the sub-certifications changes none of the counts (`test_uc01_subcert_order_invariance`) — the roll-up is order-invariant.

## §6 The 302-vs-404 interplay

The same material weakness lands in **two different SOX obligations**:

- **§302 — this quarter.** The officer certification (filed as the 601(b)(31) exhibit) covers the DC&P effectiveness conclusion now, on the Q3 10-Q. §302 is **quarterly** and officer-signed; the DC&P evaluation is performed as of the end of each fiscal quarter [CFR-17-240.13a-15 §240.13a-15(b)].
- **§404 — the annual report.** The same MW will flow into management's **annual ICFR assessment** under Item 308(a), and — because Crestline is an **accelerated filer** — into the **auditor's ICFR attestation** (§404(b)). §404 is **annual** and assessment/attestation-based.

So one control failure produces both a §302 DC&P "not effective" conclusion this quarter and a §404 ICFR-not-effective assessment at year-end. The skill keeps these distinct: §302 ≠ §404, DC&P ≠ ICFR. This chunk references `coso-internal-controls` for the §404 mechanics rather than re-teaching them (`chunks/05-section-302-vs-404.md`).

## §7 Oracle — every number is derivable

`tests/test_sox_302_disclosure_controls_oracle.py::test_uc_01_oracle` recomputes every figure independently from `uc-01-input.json` — no value is echoed from the stub or from `uc-01-expected.json`:

- `dcp_conclusion` recomputed from the MW facts via the §240.13a-15(e)/Item 307 logic == `not effective`; `classification == DCP_NOT_EFFECTIVE`.
- `par5_disclosure_required == True` from the existence of the material weakness [§7241(a)(5)].
- `subcert_total == 14`, `subcert_exceptions == 1`, `subcert_clean == 13`, recounted from the sub-cert list; the counts foot.
- `top_level_cert_clean == False`.
- Expected-seed agreement: the `uc-01-expected.json` fields equal the recomputed values.

Metamorphic: reversing the sub-cert order changes nothing; remediating the MW flips DC&P to effective. Adversarial: with no material-weakness facts the stub refuses (`INSUFFICIENT_INPUT`, `test_uc01_missing_mw_facts_refuses`); an unremediated MW in a disclosure-relevant area can never yield an "effective" conclusion (`test_uc01_unremediated_mw_forces_not_effective`).

## §8 Anti-hallucination

- **Crestline Financial Corp is fictional**; the seed is the tested fixture and this UC's source of truth. Org name and the 14/1/13 counts are exactly as seeded.
- **DC&P ≠ ICFR.** The MW is an ICFR matter that is *also* a DC&P matter here because it affects a disclosure-relevant area — not because ICFR and DC&P are the same thing [CFR-17-240.13a-15 §240.13a-15(e)/(f)].
- **§302 ≠ §404.** The §302 quarterly officer certification and the §404 annual assessment/attestation are distinct obligations; this UC shows the interplay, not an equivalence.
- **The sub-certification cascade is a house framework, not a rule mandate** — the SEC recommended a disclosure committee (Release 33-8124); it did not require sub-certifications.
- **The DC&P conclusion is derived, never hard-coded** — change the MW facts and the conclusion changes (the metamorphic and adversarial tests enforce this).
