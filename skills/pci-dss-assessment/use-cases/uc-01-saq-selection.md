---
uc_id: UC-01
title: "E-commerce merchant SAQ selection: direct-post payment page with merchant scripts but no PAN on merchant servers resolves to SAQ A-EP (CartNimbus)"
industries: [saas-technology, retail-ecommerce]
frameworks: [PCI-DSS-4.0.1]
inputs:
  org: "CartNimbus — fictional e-commerce merchant, ~2,000,000 annual transactions, not a service provider (data/seeds/uc-01-input.json)"
  payment_page: "payment-page architecture facts: outsourced_to_compliant_third_party=true, method=direct_post, merchant_javascript_on_payment_page=true, merchant_servers_touch_pan=false"
  as_of_date: "2026-06-11"
procedure:
  - "chunks/01-scope-and-applicability.md — Establish what PCI DSS applies to and that account data (CHD + SAD) never appears in this example; PAN is modeled, never shown."
  - "chunks/03-saq-selection.md — Apply the SAQ decision tree to the payment-page architecture: service provider -> ROC/SAQ-D-SP; merchant servers touch PAN -> full ROC; fully outsourced redirect/iframe with no merchant script -> SAQ A; merchant controls page scripts but servers never receive PAN -> SAQ A-EP."
  - "chunks/03-saq-selection.md — Derive the client-side-script requirement flags (6.4.3 manage scripts, 11.6.1 change-and-tamper detection) that apply on SAQ A-EP and ROC but not on pure SAQ A."
  - "chunks/02-scoping-and-segmentation.md — Confirm the merchant's CDE: its servers never store/process/transmit PAN, but its website affects payment-page security, which is exactly the A-EP boundary."
  - "SKILL.md §1-§11 — apply the SAQ routing decision logic and populate the eligibility-determination record with the deciding factor and the applicable-requirement list."
expected_outputs:
  classification: "VALIDATION_SAQ_A-EP"
  saq_eligibility: "SAQ A-EP"
  deciding_factor: "merchant website controls payment-page elements/scripts (so it can affect PAN security) but its servers never receive PAN"
  client_side_script_requirements_apply: ["6.4.3", "11.6.1"]
oracle:
  - "saq_eligibility recomputed independently from the payment_page facts via the house decision convention == stub output == SAQ A-EP (the B19 scenario); never a hardcoded verdict"
  - "client_side_script_requirements_apply == [6.4.3, 11.6.1] because the path is SAQ A-EP (applies on A-EP and ROC, empty on pure SAQ A)"
  - "classification == VALIDATION_SAQ_A-EP, derived from the SAQ string"
  - "transaction volume alone does not flip the architecture-driven SAQ path (volume/brand thresholds are a documented non-goal — brand-defined)"
  - "a missing payment-page fact refuses rather than guessing the architecture"
data_refs:
  - data/seeds/uc-01-input.json
  - data/seeds/uc-01-expected.json
tests:
  - tests/test_pci_dss_assessment_oracle.py::test_uc_01_oracle
  - tests/test_pci_dss_assessment_metamorphic.py::test_uc01_volume_does_not_flip_saq_path
  - tests/test_pci_dss_assessment_adversarial.py::test_uc01_missing_architecture_fact_refuses
  - tests/test_pci_dss_assessment_adversarial.py::test_uc01_service_provider_routes_to_roc
  - tests/test_pci_dss_assessment_adversarial.py::test_uc01_merchant_servers_touch_pan_forces_roc
token_baseline: "not yet measured — see telemetry/baseline.md"
status: active
---

# UC-01 — E-commerce SAQ selection: SAQ A vs A-EP vs full ROC (CartNimbus)

## §1 Context and persona

**CartNimbus** is a fictional e-commerce merchant: roughly 2,000,000 card transactions a year, validating as a **merchant** (not a service provider). The persona is the merchant's compliance lead asking the question that decides the whole year of work: **which validation path applies to me?** The answer is not a transaction-volume lookup — it is determined by the **payment-page architecture**, i.e. where the cardholder's primary account number (PAN) actually goes and whose code can touch it.

The seeds in `data/seeds/` are the tested fixture and this UC's source of truth; every value below is recomputed from them by `tests/test_pci_dss_assessment_oracle.py::test_uc_01_oracle`. No PAN appears anywhere in this example — PAN is modeled as a fact about the architecture, never shown, which is itself a teaching point.

## §2 The payment-page architecture facts

CartNimbus's payment page has four architecture facts in the seed:

| Fact | Value |
|------|-------|
| Outsourced to a compliant third-party service provider | true |
| Payment-page method | `direct_post` |
| Merchant JavaScript present on the payment page | true |
| Merchant servers store/process/transmit PAN | false |

This is the **direct-post** pattern: the customer's browser posts card data straight to the compliant payment service provider, so CartNimbus's own servers never receive PAN — **but** CartNimbus serves and controls the page (and its scripts) on which the cardholder enters the PAN. Controlling those page elements means CartNimbus **can affect the security of the PAN** even though it never holds it.

## §3 The SAQ decision — derived, not looked up

**House decision convention (labeled — an engagement heuristic applying PCI DSS v4.0.1 eligibility rules, not verbatim standard text):**

- Service provider → validate via **ROC / SAQ D for Service Providers**, not a merchant SAQ A/A-EP.
- Merchant servers store/process/transmit PAN → **full ROC** (full CDE in the merchant's hands).
- Fully outsourced payment page — redirect or iframe to a compliant TPSP, **no merchant script** on the page → **SAQ A**.
- Merchant controls page elements/scripts but its **servers never receive PAN** → **SAQ A-EP**.
- Otherwise → **full ROC** (default when no SAQ eligibility is established).

Walking CartNimbus through it: not a service provider; servers do not touch PAN (so not forced to ROC on that basis); not a no-script redirect/iframe (the method is `direct_post` with merchant JavaScript present, so not SAQ A); outsourced with servers never receiving PAN and the merchant controlling page scripts → **SAQ A-EP**.

**Result: SAQ A-EP.** The deciding factor is precisely that *the merchant website controls payment-page elements/scripts (so it can affect PAN security) but its servers never receive PAN.* That single distinction is what separates A-EP from A.

### The contrast that defines A-EP

| Architecture | Who can touch PAN / page scripts | Path |
|---|---|---|
| Fully outsourced redirect/iframe to a compliant TPSP, **no merchant script** | TPSP only; merchant cannot alter the payment form | **SAQ A** |
| Direct-post / merchant scripts on the page; **servers never receive PAN** | Merchant can affect PAN security via the page it controls | **SAQ A-EP** (CartNimbus) |
| Merchant servers store/process/transmit PAN | Merchant holds a full CDE | **full ROC** |

## §4 Client-side script requirements (6.4.3 and 11.6.1)

Because the path is **SAQ A-EP** (and these also apply on a full ROC), two client-side script requirements apply that do **not** apply to a pure SAQ A merchant:

- **6.4.3** — manage and authorize all payment-page scripts loaded in the consumer's browser, and keep an inventory with written justification for each.
- **11.6.1** — deploy a change-and-tamper-detection mechanism on the payment page to alert on unauthorized modification of HTTP headers and page content.

These are the v4.0.1 requirements aimed squarely at e-skimming/Magecart risk, and they are exactly why a merchant that controls its own payment-page scripts cannot use SAQ A. The seed derives `client_side_script_requirements_apply = ["6.4.3", "11.6.1"]` from the SAQ-A-EP path; for a pure SAQ A merchant the list is empty.

## §5 Oracle — the SAQ decision is derivable

`tests/test_pci_dss_assessment_oracle.py::test_uc_01_oracle` recomputes the path independently from the four `payment_page` facts using the house convention above and asserts the stub agrees and equals the expected seed:

- `saq_eligibility` recomputed from the architecture facts == `SAQ A-EP` (the B19 scenario) — never a stored verdict.
- `client_side_script_requirements_apply` == `["6.4.3", "11.6.1"]` because the path is A-EP (the list is empty only on pure SAQ A).
- `classification` == `VALIDATION_SAQ_A-EP`, derived from the SAQ string.

Metamorphic (`test_uc01_volume_does_not_flip_saq_path`): dropping the annual transaction count to 50 does **not** change the path — the SAQ decision is architecture-driven, and brand/acquirer volume thresholds are a documented non-goal (brand-defined). Adversarial: a missing payment-page fact **refuses** rather than guessing the architecture (`test_uc01_missing_architecture_fact_refuses`); flipping `is_service_provider` to true routes to **ROC** (`test_uc01_service_provider_routes_to_roc`); setting `merchant_servers_touch_pan` to true forces **full ROC** and still flags 6.4.3/11.6.1 (`test_uc01_merchant_servers_touch_pan_forces_roc`).

## §6 Anti-hallucination

- **CartNimbus is fictional**; the seeds are the tested fixture and this UC's source of truth.
- **The SAQ routing rule is a labeled house decision convention** — it applies PCI DSS v4.0.1 eligibility logic; the SAQ catalog and eligibility conditions come from the standard and the PCI SSC document library [PCI-SSC-Document-Library §SAQ].
- **No PAN is ever shown** — PAN is modeled as an architecture fact ("do the merchant's servers receive it?"), never reproduced. The skill teaches that examples carry zero PAN/CHD/SAD by construction.
- **A payment brand or acquirer may mandate a full ROC regardless** of SAQ eligibility; merchant validation levels are **brand-defined and variable**, never set by PCI DSS — see `industries/saas-technology.md` and `industries/retail-ecommerce.md`.
- **Future-dated v4.0.1 requirements are in force.** 6.4.3 and 11.6.1 were "best practice until 31 March 2025" in the printed text; they are **mandatory** now and must never be presented as optional [PCI-SSC-Blog-v401 §v4.0.1].
