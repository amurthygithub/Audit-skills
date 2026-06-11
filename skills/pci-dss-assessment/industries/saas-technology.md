---
industry: saas-technology
parent_skill: pci-dss-assessment
title: "SaaS / e-commerce technology — merchant vs service provider, client-side script requirements, SAQ A vs A-EP, and cloud shared responsibility"
version: 0.1.0
status: active
frameworks: [PCI-DSS-4.0.1]
primary_personas: [E-commerce/SaaS compliance lead, CTO/VP Engineering, CISO, Security questionnaire owner]
regulatory_anchors: [PCI-DSS-v4.0.1, client-side-script-requirements]
last_verified: "2026-06-11"
---

# SaaS / e-commerce technology — the merchant-and-service-provider lens

A technology company touches PCI DSS in one of two roles — or both: as a **merchant** accepting card payments for its own goods/services, and as a **service provider** that stores, processes, or transmits cardholder data (or can affect its security) on behalf of others. The role drives the validation path, and for e-commerce the **payment-page architecture** drives the SAQ. This view applies the skill to the SaaS/e-commerce technology company. The UC-01 engagement (`use-cases/uc-01-saq-selection.md`, CartNimbus — a ~2M-transaction e-commerce merchant) is the worked example.

## The SaaS / e-commerce framing

### Are we a merchant or a service provider — and does it matter?

It matters more than almost anything else. A **merchant** validates via a merchant SAQ (A, A-EP, B, B-IP, C, C-VT, P2PE, SPoC) or a full ROC; a **service provider** validates via SAQ D for Service Providers or a full ROC, and a service provider can never use the merchant SAQ A/A-EP path. A SaaS platform that handles cardholder data for its customers is a service provider for that data even if it is also a merchant for its own subscriptions. The role determination comes before the SAQ determination (UC-01 starts there: a service provider routes straight to ROC/SAQ-D-SP).

### SAQ A vs SAQ A-EP — the question every e-commerce merchant gets wrong

This is the live 2026 question and the spine of UC-01. The dividing line is **whether the merchant can affect the security of the PAN**, even when its servers never receive it:

| Architecture | Can the merchant affect PAN security? | Path |
|---|---|---|
| Fully outsourced **redirect or iframe** to a compliant TPSP, **no merchant script** on the payment page | No — the TPSP controls the payment form entirely | **SAQ A** |
| **Direct-post** or merchant JavaScript on the payment page; merchant **servers never receive PAN** | Yes — the merchant controls the page the PAN is typed into | **SAQ A-EP** |
| Merchant **servers store/process/transmit PAN** | The merchant holds a full CDE | **full ROC** |

CartNimbus is the middle row: direct-post with merchant scripts on the page, servers never touching PAN → **SAQ A-EP**. A brand or acquirer can always mandate a full ROC regardless (brand-defined).

### What are the client-side script requirements (6.4.3 and 11.6.1) and who do they hit?

They hit SAQ A-EP merchants and full-ROC entities — **not** pure SAQ A merchants — and they are the reason A-EP exists as a separate path:

- **6.4.3** — manage and authorize the scripts loaded in the consumer's browser on the payment page, with an inventory and written justification for each.
- **11.6.1** — a change-and-tamper-detection mechanism that alerts on unauthorized modification of payment-page HTTP headers and content.

Both target e-skimming / Magecart (browser-side card-data theft). They were "best practice until 31 March 2025" in the printed v4.0.1 text and are **mandatory now** — never present them as optional [PCI-SSC-Blog-v401 §v4.0.1]. If your engineering team controls the payment page's scripts, you are in their scope; that is the SAQ A-to-A-EP escalation.

### Where does cloud shared responsibility start and stop?

A cloud/IaaS/PaaS provider hosting your CDE is itself a **service provider** to you. PCI DSS responsibilities split along the shared-responsibility line, and v4.0.1 expects that split to be **written down**: the **service-provider responsibility matrix** documents, requirement by requirement, who is responsible for what (you, the provider, or shared). Treat "the cloud is PCI compliant" as a starting point, not a conclusion — the provider's own AOC covers the provider's responsibilities only; the tenant configuration, the in-scope application, and the administrative program remain yours. A SaaS vendor that is itself a service provider owes its customers the same matrix downstream.

### Can we reuse our SOC 2 report for PCI?

Overlap, not equivalence. A SOC 2 Type II exercises many of the same operational controls, and a SaaS provider commonly supplies **both** a SOC 2 report and a PCI **AOC** to its customers — but a SOC 2 opinion is not a PCI validation, and no SOC 2 criterion maps 1:1 to a PCI DSS requirement. Reuse the evidence; re-perform the mapping. The `aicpa-soc-reporting` sibling skill is authoritative for SOC 2 report content and the evidence lifecycle.

## What's unique to SaaS / e-commerce technology

- **The payment-page architecture is a design decision with a compliance price.** Choosing a full redirect/iframe with no merchant script keeps you on SAQ A; adding merchant scripts (analytics, custom checkout) moves you to A-EP and into 6.4.3/11.6.1 scope. Design the page before you pick the SAQ.
- **Service-provider status is sticky.** Once you handle cardholder data for customers you owe the SAQ-D-SP/ROC program and a responsibility matrix — being "just a platform" does not remove it.
- **Scope minimization is an architecture sport.** Tokenization, hosted fields, and full outsourcing of the CDE are the levers that shrink your assessment; segmentation (UC-02) is the on-prem equivalent.
- **PAN never appears in your examples or telemetry** — the skill models PAN as an architecture fact and carries zero card data by construction.

## Anti-hallucination

- **Merchant vs service-provider role is determined first** — a service provider cannot validate via merchant SAQ A/A-EP.
- **SAQ A vs A-EP turns on whether the merchant can affect PAN security**, not on transaction volume (volume thresholds are brand-defined; see UC-01's metamorphic test).
- **6.4.3 and 11.6.1 are in force** — future-dated v4.0.1 requirements became mandatory 2025-03-31; never optional [PCI-SSC-Blog-v401 §v4.0.1].
- **Merchant/service-provider validation levels are brand-defined** — payment brands and acquirers set them, not PCI DSS.
- **SOC 2 ↔ PCI is overlap, not equivalence**; this skill ships no crosswalk rows (PCI↔CSF/800-53 mapping lives in the NIST OLIR catalog; row-level encoding is deferred — pointer only).
- **No PAN is ever shown** — examples and telemetry carry zero cardholder data.

## Cross-references

- `use-cases/uc-01-saq-selection.md` — the worked SAQ A-EP determination and the client-side script requirements.
- `chunks/03-saq-selection.md` — the 10 SAQ types and the full selection decision tree.
- `chunks/06-validation-roc-aoc.md` — ROC vs AOC vs SAQ, QSA/ISA roles, and the service-provider responsibility matrix.
- `chunks/08-currency-and-program-context.md` — v4.0.1 currency, future-dated-in-force banner, and the OLIR crosswalk pointer.
- `aicpa-soc-reporting` (sibling skill) — authoritative for SOC 2 report content; pair it with this view for the SOC-2-plus-AOC pattern.
