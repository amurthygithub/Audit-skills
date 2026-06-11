---
uc_id: UC-02
title: "Newly-public EGC files its first periodic report — §302 certification is required from day one (no exemption), §404(b) auditor attestation is exempt, §404(a) management assessment lands at the first annual report, and the DC&P scope spans all 7 disclosure items while ICFR scope is the 3 financial ones"
industries: [saas-technology]
frameworks: [SOX-302-Statute-15USC7241, CFR-17-240.13a-14, CFR-17-240.13a-15, Reg-S-K-Item-307, Reg-S-K-Item-308]
inputs:
  filer: "Nimbus Cloud Inc — newly-public emerging growth company (EGC), non-accelerated, first periodic report (data/seeds/uc-02-input.json)"
  disclosure_inventory: "7 disclosure items tagged financial vs non-financial (3 financial, 4 non-financial incl. a cyber-incident 8-K Item 1.05) (data/seeds/uc-02-input.json)"
  as_of_date: "2026-06-11"
procedure:
  - "chunks/01-section-302-overview.md — Establish the §302 obligation: the PEO and PFO must certify every annual and quarterly report from the first periodic report [SOX-302-Statute-15USC7241 §7241(a); CFR-17-240.13a-14 §240.13a-14(a)]."
  - "chunks/05-section-302-vs-404.md — Apply the filer-status logic: a newly-public filer / EGC is exempt from the §404(b) auditor attestation; §302 has no such exemption; §404(a) management assessment first appears in the first annual report."
  - "chunks/02-dcp-vs-icfr.md — Scope the controls: DC&P covers ALL disclosure items (financial AND non-financial) [CFR-17-240.13a-15 §240.13a-15(e)]; ICFR covers only the financial-reporting subset [CFR-17-240.13a-15 §240.13a-15(f)]."
  - "chunks/07-material-weakness-and-change.md — Confirm the cyber-incident 8-K (Item 1.05, 4 business days from the materiality determination) is inside DC&P scope as a non-financial timely-disclosure item, not an ICFR item."
  - "chunks/04-evaluation-and-disclosure.md — Disclose the DC&P conclusion under Item 307 [Reg-S-K-Item-307 §229.307]; the ICFR report under Item 308 [Reg-S-K-Item-308 §229.308] first attaches to the first annual report."
  - "chunks/06-disclosure-committee-subcert.md — Recommended practice: stand up a disclosure-committee charter to operate the first-year accumulation-and-communication process (house framework, not a rule)."
  - "SKILL.md §1–§11 — route the first-302 obligation/scope determination through the §302 procedure."
expected_outputs:
  classification: "FIRST_302_404B_EXEMPT"
  section_302_certification_required: true
  section_404a_management_assessment_required: true
  section_404b_auditor_attestation_required: false
  dcp_scope_count: 7
  icfr_scope_count: 3
  cyber_8k_in_dcp_scope: true
oracle:
  - "section_302_certification_required == True — derived from filer status; §302 applies from the first periodic report, no newly-public/EGC exemption"
  - "section_404b_auditor_attestation_required == False — newly-public OR EGC -> §404(b) exempt; classification == FIRST_302_404B_EXEMPT"
  - "section_404a_management_assessment_required == True — the §404(a) management ICFR assessment is owed (first at the first annual report)"
  - "dcp_scope_count == 7 == len(disclosure_inventory) (financial + non-financial); icfr_scope_count == 3 == the financial subset; dcp_scope_count > icfr_scope_count (DC&P strictly broader)"
  - "cyber_8k_in_dcp_scope == True — the 8-K Item 1.05 cyber-incident item is a non-financial DC&P item"
data_refs:
  - data/seeds/uc-02-input.json
  - data/seeds/uc-02-expected.json
tests:
  - tests/test_sox_302_disclosure_controls_oracle.py::test_uc_02_oracle
  - tests/test_sox_302_disclosure_controls_adversarial.py::test_uc02_404b_never_required_for_newly_public
  - tests/test_sox_302_disclosure_controls_adversarial.py::test_uc02_seasoned_accelerated_filer_owes_404b
  - tests/test_sox_302_disclosure_controls_adversarial.py::test_uc02_missing_filer_status_refuses
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-02 — Newly-public first §302 and the obligation/scope split (Nimbus Cloud Inc)

## §1 Context and persona

**Nimbus Cloud Inc** is a fictional newly-public SaaS company and an **emerging growth company (EGC)** under the JOBS Act, **non-accelerated**, filing its **first periodic report** after the IPO. The persona is the **disclosure-committee chair / SEC-reporting manager** who must answer the first-year obligation question precisely — what is owed now, what is deferred, and what is *exempt* — and scope the controls correctly across financial and non-financial disclosure.

The seed `data/seeds/uc-02-input.json` is the tested fixture; every flag and count below is recomputed from it by `tests/test_sox_302_disclosure_controls_oracle.py::test_uc_02_oracle`.

## §2 The §302 certification is required from the first periodic report

There is **no newly-public or EGC exemption from §302**. SOX §302 requires the principal executive officer and principal financial officer to certify each annual and quarterly report [SOX-302-Statute-15USC7241 §7241(a)], and Rule 13a-14 requires that certification to be signed and filed as an exhibit with each such report [CFR-17-240.13a-14 §240.13a-14(a)]. That obligation attaches to the **first periodic report** Nimbus files as a reporting company.

**`section_302_certification_required == True`** — derived from filer status, and the adversarial test pins it: even an issuer flagged newly-public still owes the §302 certification (`test_uc02_404b_never_required_for_newly_public`). The §404(b) exemption discussed below **never** carries §302 with it.

## §3 The §404 split — §404(b) exempt, §404(a) deferred-but-owed

§404 is the *other* SOX controls obligation, and it splits in two:

- **§404(b) auditor ICFR attestation — EXEMPT.** A newly-public filer and an EGC are exempt from the auditor's ICFR attestation (the EGC exemption runs up to five years under the JOBS Act; newly-public issuers also have a transition before §404(b) first applies). Nimbus is both newly-public and an EGC, so **`section_404b_auditor_attestation_required == False`**, and the engagement classifies `FIRST_302_404B_EXEMPT`.
- **§404(a) management ICFR assessment — required, first at the first annual report.** The exemption is from the *auditor* attestation, not from management's own assessment. **`section_404a_management_assessment_required == True`**; the Item 308(a) management report first attaches to Nimbus's first **annual** report (a 10-Q carries the §302 cert and the Item 307 DC&P conclusion, but the Item 308(a) ICFR report is annual).

The contrast case is in the adversarial suite: a **seasoned, non-EGC accelerated filer** (not newly-public) **does** owe §404(b) (`test_uc02_seasoned_accelerated_filer_owes_404b`, classification `FIRST_302_404B_REQUIRED`). The §404(b) flag is therefore derived from filer status, not assumed.

## §4 DC&P scope spans all 7 items; ICFR scope is the 3 financial ones

DC&P is **broader** than ICFR. DC&P covers all information required to be disclosed in Exchange Act reports — financial **and** non-financial [CFR-17-240.13a-15 §240.13a-15(e)] — while ICFR is limited to the reliability of financial reporting [CFR-17-240.13a-15 §240.13a-15(f)]. Nimbus's disclosure inventory has 7 items:

| # | Disclosure item | Category | In DC&P scope | In ICFR scope |
|---|-----------------|----------|---------------|---------------|
| 1 | Revenue recognition (ASC 606) | financial | yes | yes |
| 2 | Cash & investments | financial | yes | yes |
| 3 | Stock-based comp | financial | yes | yes |
| 4 | Risk factors | non_financial | yes | no |
| 5 | Legal proceedings | non_financial | yes | no |
| 6 | Cybersecurity incident (8-K Item 1.05) | non_financial | yes | no |
| 7 | MD&A | non_financial | yes | no |

**DC&P scope = 7 (all items); ICFR scope = 3 (the financial subset).** `dcp_scope_count == 7 > icfr_scope_count == 3` — DC&P is strictly broader here, which is the whole point of separating the two controls universes.

## §5 The cyber-incident 8-K is a DC&P item, not an ICFR item

Item 6 — a **material cybersecurity incident** disclosed on Form **8-K Item 1.05** within **4 business days of the materiality determination** — is a **non-financial timely-disclosure** obligation. It lives squarely in DC&P (controls that ensure information "is recorded, processed, summarized and reported, within the time periods specified" [CFR-17-240.13a-15 §240.13a-15(e)]) and **not** in ICFR. **`cyber_8k_in_dcp_scope == True`.** A missed cyber-8-K is a DC&P failure that need not be an ICFR failure — the asymmetry the skill exists to teach.

## §6 Disclosure-committee charter — recommended practice

A first-year issuer benefits from a **disclosure committee** to operate the accumulation-and-communication process across finance, legal, IR, and engineering. This is **recommended practice, not a rule mandate**: the SEC *recommended* a disclosure committee in the 2002 adopting release (33-8124) and did not require one. The skill ships a charter template (`chunks/06-disclosure-committee-subcert.md`) labeled as a house framework — adopting it does not change the §302 obligation, which already applies in full.

## §7 Oracle — every flag is derivable

`tests/test_sox_302_disclosure_controls_oracle.py::test_uc_02_oracle` recomputes every flag and count independently from `uc-02-input.json`:

- `section_302_certification_required == True` (no newly-public/EGC exemption from §302).
- `section_404b_auditor_attestation_required == False` (newly-public OR EGC); `classification == FIRST_302_404B_EXEMPT`.
- `section_404a_management_assessment_required == True`.
- `dcp_scope_count == 7 == len(disclosure_inventory)`; `icfr_scope_count == 3 == ` the financial subset; `dcp_scope_count > icfr_scope_count`.
- `cyber_8k_in_dcp_scope == True`.
- Expected-seed agreement: `uc-02-expected.json` equals the recomputed values.

Adversarial: a newly-public filer is never forced into §404(b) but always owes §302 (`test_uc02_404b_never_required_for_newly_public`); a seasoned accelerated non-EGC filer does owe §404(b) (`test_uc02_seasoned_accelerated_filer_owes_404b`); missing filer-status facts force a refusal (`INSUFFICIENT_INPUT`, `test_uc02_missing_filer_status_refuses`).

## §8 Anti-hallucination

- **Nimbus Cloud Inc is fictional**; the seed is the tested fixture. Org name and the 7/3 counts are exactly as seeded.
- **The §404(b) exemption never exempts §302** — §302 applies from the first periodic report regardless of filer status (the adversarial test enforces this).
- **DC&P ≠ ICFR.** DC&P scope (7) is strictly broader than ICFR scope (3); the cyber-8-K is a DC&P item, not an ICFR item [CFR-17-240.13a-15 §240.13a-15(e)/(f)].
- **§302 ≠ §404.** §302 is the quarterly officer certification; §404(a)/(b) are the annual management assessment and auditor attestation.
- **The disclosure committee is recommended practice, not a rule** (Release 33-8124) — its charter is a house-framework template.
