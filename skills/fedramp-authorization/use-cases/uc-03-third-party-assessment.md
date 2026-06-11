---
uc_id: UC-03
title: "Big-4 3PAO assessment of a Moderate CSP — the SAR finding roll-up: a finding is a control the CSP OWNS that FAILED testing, so 4 CSP-owned failures (AC-2, SI-2, AU-6, CM-6) become POA&M items, the 2 inherited controls (SC-7, PE-3) are excluded, and the residual High findings force an AO risk-acceptance note"
industries: [public-sector]
frameworks: [FedRAMP-Rev5, FedRAMP-Authorization-Act-2022, OMB-M-24-15, NIST-SP-800-53r5]
inputs:
  system: "Acme Cloud Suite (3PAO assessment) — Moderate baseline; assessor Example 3PAO LLP (A2LA-accredited) (data/seeds/uc-03-input.json)"
  controls: "8 control-test results, each tagged tested/passed/inherited with a severity for failures — 4 CSP-owned failures (AC-2 High, SI-2 High, AU-6 Moderate, CM-6 Low), 2 CSP-owned passes (AU-2, CA-7), 2 inherited (SC-7 High, PE-3 Moderate) (data/seeds/uc-03-input.json)"
procedure:
  - "chunks/05-assessment-and-inheritance.md — Identify the findings: a finding is a control the CSP OWNS (not inherited/leveraged) that FAILED testing [A2LA-3PAO §17020]; findings = [c for c in controls if c.tested and not c.passed and not c.inherited]."
  - "chunks/05-assessment-and-inheritance.md — Exclude inherited controls: inherited/leveraged controls are the provider's responsibility and are not the leveraging CSP's findings or POA&M items [A2LA-3PAO §17020]."
  - "chunks/04-the-authorization-package.md — Roll up to the POA&M: poam_item_count == number of findings; one POA&M item per CSP-owned failed control [FEDRAMP-PLAYBOOK §ssp]."
  - "chunks/07-poam-and-risk.md — Severity rollup and the AO signal: count findings by severity; any residual High (or Critical) finding is a risk signal requiring AO risk acceptance before an ATO."
  - "chunks/03-authorization-paths.md — Note the boundary: the 3PAO recommends; the ATO decision itself is the authorizing official's [OMB-M-24-15 §authority]."
  - "SKILL.md §1-§11 — route the engagement through the 3PAO assessment -> finding roll-up -> inheritance -> AO risk note procedure."
expected_outputs:
  classification: "SAR_FINDINGS_4"
  controls_total: 8
  controls_tested_own: 6
  inherited_count: 2
  findings: ["AC-2", "SI-2", "AU-6", "CM-6"]
  poam_item_count: 4
  findings_by_severity: {High: 2, Moderate: 1, Low: 1}
  has_high_severity_finding: true
  recommendation_note: "residual high-severity finding(s) present — authorizing official risk acceptance required before an ATO decision"
oracle:
  - "findings recomputed = [c for c in controls if c.tested and not c.passed and not c.inherited] == [AC-2, SI-2, AU-6, CM-6]; classification == SAR_FINDINGS_4"
  - "poam_item_count == len(findings) == 4"
  - "inherited_count == 2 (SC-7, PE-3 excluded from the findings — provider's responsibility); controls_total == 8; controls_tested_own == 6"
  - "findings_by_severity recomputed by counting findings per severity == {High:2, Moderate:1, Low:1}; the three foot to 4"
  - "has_high_severity_finding == True (any finding severity in {High, Critical}); recommendation_note keys to the AO risk-acceptance signal"
  - "expected-seed agreement: uc-03-expected.json fields equal the recomputed values"
data_refs:
  - data/seeds/uc-03-input.json
  - data/seeds/uc-03-expected.json
tests:
  - tests/test_fedramp_authorization_oracle.py::test_uc_03_oracle
  - tests/test_fedramp_authorization_metamorphic.py::test_uc03_marking_a_failed_control_inherited_removes_the_poam_item
  - tests/test_fedramp_authorization_metamorphic.py::test_uc03_control_order_invariance
  - tests/test_fedramp_authorization_adversarial.py::test_uc03_inherited_high_finding_excluded_from_csp_poam
  - tests/test_fedramp_authorization_adversarial.py::test_uc03_empty_controls_zero_findings
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-03 — Big-4 3PAO assessment of a Moderate CSP (Example 3PAO)

## §1 Context and persona

**Example 3PAO LLP** — an independent, **A2LA-accredited** third-party assessment organization — has tested the controls of **Acme Cloud Suite** at the **Moderate** baseline and must produce the **SAR finding roll-up**: which failed controls become the CSP's POA&M items, which are excluded as inherited, and what residual risk the authorizing official has to weigh.

The persona is the **3PAO assessor**. The skill encodes how a finding is defined and how inheritance and severity drive the roll-up — but the **ATO decision itself is the AO's**, not the 3PAO's [OMB-M-24-15 §authority]. The 3PAO is A2LA-accredited to ISO/IEC 17020 [A2LA-3PAO §17020]. The seed `data/seeds/uc-03-input.json` is the tested fixture; every count below is recomputed from it by `tests/test_fedramp_authorization_oracle.py::test_uc_03_oracle`.

## §2 The control-test set

The 3PAO tested 8 controls. Each is tagged passed/failed and **inherited (the provider's)** or **own (the CSP's)**:

| Control | Tested | Passed | Inherited | Severity |
|---|---|---|---|---|
| AC-2 | yes | **failed** | own | High |
| SI-2 | yes | **failed** | own | High |
| AU-6 | yes | **failed** | own | Moderate |
| CM-6 | yes | **failed** | own | Low |
| AU-2 | yes | passed | own | — |
| CA-7 | yes | passed | own | — |
| SC-7 | no | — | **inherited** | High |
| PE-3 | no | — | **inherited** | Moderate |

So: **8 controls total**, **6 CSP-owned controls that were tested** (`controls_tested_own == 6`), and **2 inherited** (`inherited_count == 2`).

## §3 What counts as a finding — CSP-owned and failed

A **finding** is a control the CSP **owns** (not inherited/leveraged) that **failed** testing [A2LA-3PAO §17020]:

```
findings = [c for c in controls if c.tested and not c.passed and not c.inherited]
```

Applying that to the set: **AC-2, SI-2, AU-6, CM-6** — the four CSP-owned controls that failed (classification `SAR_FINDINGS_4`). The two passing CSP-owned controls (AU-2, CA-7) are not findings; the two inherited controls are excluded by the next step.

## §4 Inherited controls are excluded — the provider's POA&M, not the CSP's

**SC-7 and PE-3 are inherited.** Inherited/leveraged controls (e.g., from an authorized IaaS/PaaS) are the **underlying provider's responsibility** — they belong to the provider's package and POA&M, and they are **not re-tested by, and not in the POA&M of, the leveraging CSP** [A2LA-3PAO §17020]. So even though **SC-7 is tagged High**, it is **not** an Acme finding — it does not enter Acme's POA&M.

This is the load-bearing inheritance rule, and the tests prove it both ways: marking a CSP-owned failed control `inherited` **removes** it from the CSP's POA&M (`test_uc03_marking_a_failed_control_inherited_removes_the_poam_item`), and an inherited High finding is excluded from the CSP's POA&M (`test_uc03_inherited_high_finding_excluded_from_csp_poam`).

## §5 The POA&M roll-up and the severity counts

Each finding becomes one POA&M item, so **`poam_item_count == len(findings) == 4`**. Counting the findings by severity:

| Severity | Findings | Count |
|---|---|---|
| High | AC-2, SI-2 | 2 |
| Moderate | AU-6 | 1 |
| Low | CM-6 | 1 |

**`findings_by_severity == {High: 2, Moderate: 1, Low: 1}`** — and the three foot to 4. The inherited SC-7 (High) and PE-3 (Moderate) are **not** in this rollup because they are not Acme findings.

## §6 The residual-high signal — an AO decision, not the 3PAO's

Two findings are **High** (AC-2, SI-2), so `has_high_severity_finding == True`. A residual high-severity finding is a **risk signal for the authorizing official**: the roll-up sets

> "residual high-severity finding(s) present — authorizing official risk acceptance required before an ATO decision."

This does **not** auto-deny the ATO and the 3PAO does **not** decide it — the 3PAO **recommends** and documents residual risk; the **ATO is the AO's risk-based call** [OMB-M-24-15 §authority]. If there were no residual High/Critical findings in the CSP-owned set, the note would instead read that none are present.

## §7 Oracle — every count is derivable

`tests/test_fedramp_authorization_oracle.py::test_uc_03_oracle` recomputes every count independently from `uc-03-input.json` — no value is echoed from `uc-03-expected.json`:

- `findings` recomputed = `[c for c in controls if c.tested and not c.passed and not c.inherited]` == `[AC-2, SI-2, AU-6, CM-6]`; `classification == SAR_FINDINGS_4`.
- `poam_item_count == len(findings) == 4`.
- `inherited_count == 2` (SC-7, PE-3 excluded); `controls_total == 8`; `controls_tested_own == 6`.
- `findings_by_severity` recomputed by counting findings per severity == `{High:2, Moderate:1, Low:1}` (foots to 4).
- `has_high_severity_finding == True`; the `recommendation_note` keys to the AO risk-acceptance signal.
- Expected-seed agreement: the `uc-03-expected.json` fields equal the recomputed values.

**Metamorphic:** marking a failed CSP-owned control `inherited` removes it from the POA&M (`test_uc03_marking_a_failed_control_inherited_removes_the_poam_item`); reordering the controls changes none of the counts (`test_uc03_control_order_invariance`). **Adversarial:** an inherited High finding is excluded from the CSP's POA&M (`test_uc03_inherited_high_finding_excluded_from_csp_poam`); an empty control set yields zero findings (`test_uc03_empty_controls_zero_findings`).

## §8 Anti-hallucination

- **Example 3PAO LLP and Acme Cloud Suite are fictional**; the seed is the tested fixture and this UC's source of truth. The 8/6/2 counts and the {High:2, Moderate:1, Low:1} rollup are exactly as seeded.
- **A finding is a CSP-owned control that failed** — inherited/leveraged controls are the provider's responsibility and are excluded from the CSP's findings and POA&M [A2LA-3PAO §17020].
- **`poam_item_count == len(findings)`** — one POA&M item per CSP-owned failed control; the count is derived, never hard-coded.
- **The 3PAO is independent, A2LA-accredited to ISO/IEC 17020** (Type A or C; Type B prohibited) — it tests controls and writes the SAR [A2LA-3PAO §17020].
- **The ATO decision is the authorizing official's** — the 3PAO recommends and documents residual risk; a residual high-severity finding forces an explicit AO risk-acceptance decision, it does not auto-deny [OMB-M-24-15 §authority].
- **The JAB and its P-ATO are retired** — the current authorizer is the statutory FedRAMP Board; the AO grants the ATO under Agency Authorization [FEDRAMP-ACT-2022 §3610; OMB-M-24-15 §authority].
- **This is not authorization or legal advice** — the SAR informs the AO; it does not grant the ATO.
