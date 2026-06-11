---
chunk_id: 03-saq-selection
parent_skill: pci-dss-assessment
topic: "The 10 SAQ types and their eligibility conditions; the SAQ-selection decision tree; SAQ vs full ROC; SAQ A vs A-EP and the client-side script requirements 6.4.3 / 11.6.1"
load_when: "user asks which SAQ applies, SAQ A vs A-EP, SAQ vs ROC, eligibility for a self-assessment questionnaire, or about client-side payment-page scripts"
---

# Chunk 03 — SAQ Selection

A **Self-Assessment Questionnaire (SAQ)** is a validation tool for eligible merchants and service providers to self-attest to a subset of PCI DSS applicable to their payment channel. Where no SAQ fits, a full **Report on Compliance (ROC)** is required (`chunks/06`). Eligibility turns on **how account data flows and who controls the payment page**, not on organization size — though the brand/acquirer can always mandate a ROC regardless (brand-defined; see `chunks/08`).

## 1. The 10 SAQ types

All ten are at v4.0.1 [PCI-SSC-Document-Library]:

| SAQ | Intended eligibility (paraphrased) |
|-----|-------------------------------------|
| **A** | Card-not-present (e-commerce / MOTO) merchants who **fully outsource** all account-data functions; no merchant system stores/processes/transmits account data and the payment page is fully delegated (redirect or iframe to a compliant third party) with no merchant script controlling it |
| **A-EP** | E-commerce merchants who outsource payment processing but whose website **controls or affects** how the payment page / its scripts are delivered, while merchant servers never store/process/transmit account data |
| **B** | Merchants using only imprint machines or standalone dial-out terminals; no electronic account-data storage |
| **B-IP** | Merchants using only standalone, PTS-approved **IP-connected** payment terminals; no electronic account-data storage |
| **C** | Merchants with a **payment-application system connected to the internet**; no electronic account-data storage |
| **C-VT** | Merchants using a **virtual payment terminal** on an isolated computer; no electronic account-data storage |
| **D — Merchant** | Merchants not eligible for any other SAQ (the catch-all merchant SAQ) |
| **D — Service Provider** | Service providers eligible to complete an SAQ rather than a ROC |
| **P2PE** | Merchants using only a validated **PCI P2PE** solution; no electronic account-data storage |
| **SPoC** | Merchants using a validated **Software-based PIN entry on COTS (SPoC)** solution |

The "no electronic account-data storage" SAQs (B, B-IP, C, C-VT, P2PE, SPoC) each carry their own eligibility constraints; if any constraint fails, the merchant falls to **SAQ D (Merchant)** or a ROC.

## 2. SAQ A vs A-EP — the client-side-script distinction

The most consequential e-commerce decision. The dividing line is **whether the merchant controls the payment-page scripts**:

- **SAQ A** — the payment page is **fully outsourced** via redirect or iframe to a compliant third party, and **no merchant-controlled script** is delivered to the payment page. The merchant's environment is removed from the account-data path.
- **SAQ A-EP** — the merchant **controls or affects** the payment page or the scripts loaded into it (e.g., direct-post, JavaScript on the merchant's own page, a self-hosted iframe wrapper), **even though merchant servers never receive account data**.

Because A-EP merchants influence what executes in the cardholder's browser, **A-EP (and ROC) trigger the client-side-script requirements**:

- **Req 6.4.3** — manage and authorize all payment-page scripts; assure their integrity; maintain an inventory with justification.
- **Req 11.6.1** — a change-and-tamper-detection mechanism alerts on unauthorized modification of the payment-page HTTP headers and content.

These two requirements are **in force now** (formerly future-dated, mandatory since 2025-03-31). They do **not** apply to pure SAQ A (no merchant script on the page).

## 3. The SAQ-selection heuristic (house decision convention)

> **House convention — engagement-decision logic applying the eligibility rules, not verbatim standard text.**
>
> 1. **Service provider?** → no SAQ for the merchant path; service providers use **SAQ D (Service Provider)** if eligible, else a **ROC** (and larger SPs generally a ROC).
> 2. **Merchant servers store/process/transmit PAN (account data)?** → **full ROC** (or SAQ D Merchant only if the channel-specific SAQ-D conditions are met; otherwise ROC).
> 3. **Fully outsourced, redirect/iframe, no merchant script on the payment page?** → **SAQ A**.
> 4. **Merchant controls page elements/scripts but servers never receive account data?** → **SAQ A-EP** (apply 6.4.3 and 11.6.1).
> 5. Terminal/POS-only channels with no electronic storage → the matching **B / B-IP / C / C-VT / P2PE / SPoC** by terminal type.
> 6. **None fit** → **SAQ D (Merchant)** or **ROC**.
>
> The brand/acquirer may mandate a ROC regardless of SAQ eligibility (brand-defined).

This heuristic **applies** the published SAQ eligibility conditions; it is labeled decision logic so it is not mistaken for standard text. **Derive the outcome from architecture facts — never assume a verdict.** If a deciding fact (e.g., whether merchant script reaches the payment page) is missing, **ask for it**.

## 4. Procedure — SAQ-eligibility selection

1. Establish **role** (merchant vs service provider).
2. Capture the **payment-page architecture**: outsourced to a compliant TPSP? method (redirect / iframe / direct-post / hosted JS)? does merchant code/script reach the payment page? do merchant servers ever receive account data?
3. Apply the §3 heuristic to derive the SAQ type (or ROC) **and the deciding factor**.
4. **Flag client-side-script requirements** (6.4.3, 11.6.1) for A-EP and ROC.
5. Note the **brand/acquirer override** caveat.

## 5. Output template — SAQ-eligibility determination

| Field | Meaning |
|-------|---------|
| `role` | merchant / service provider |
| `saq_eligibility` | SAQ A / A-EP / B / … / D / **ROC** |
| `deciding_factor` | the architecture fact that drove it |
| `client_side_script_requirements` | `["6.4.3", "11.6.1"]` for A-EP/ROC, else `[]` |
| `brand_caveat` | levels and a possible ROC mandate are brand/acquirer-defined |

**Worked illustration (UC-01 shape):** an e-commerce merchant outsources processing to a compliant TPSP but uses a **direct-post** page with merchant **JavaScript on the payment page**, and merchant servers **never receive account data** → **SAQ A-EP**, with **6.4.3 and 11.6.1 applicable**. Had the page been a pure redirect/iframe with no merchant script, it would be **SAQ A** with neither script requirement. See `use-cases/uc-01-saq-selection.md`.
