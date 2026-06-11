---
industry: retail-ecommerce
parent_skill: pci-dss-assessment
title: "Retail / e-commerce — card-present and e-commerce, POS/POI, store-network segmentation, the B/B-IP/C/C-VT/P2PE SAQ paths, and franchise multi-site"
version: 0.1.0
status: active
frameworks: [PCI-DSS-4.0.1]
primary_personas: [Retail security manager, IT/store-systems lead, Franchise compliance coordinator, QSA support]
regulatory_anchors: [PCI-DSS-v4.0.1, scoping-and-segmentation]
last_verified: "2026-06-11"
---

# Retail / e-commerce — the card-present-and-online lens

A retailer typically accepts cards in **both** channels: card-present at the point of sale and card-not-present online. Each channel has its own SAQ landscape and its own scope risk, and the retailer's biggest lever is **segmentation** — keeping the store network from dragging the whole estate into scope. This view applies the skill to the retailer. The UC-02 engagement (`use-cases/uc-02-roc-segmentation.md`, Ironvale Retail — a ~8M-transaction L1 merchant on a full ROC) and the UC-03 engagement (`use-cases/uc-03-compensating-control.md`, a 30-location franchise on SAQ D) are the worked examples.

## The retail framing

### POS and POI — what is actually in the CDE?

The **point-of-interaction (POI)** device (the card reader/terminal) and the **point-of-sale (POS)** systems behind it are the heart of the card-present CDE. Whether they pull the rest of the store into scope depends on the architecture: a **PCI-listed P2PE solution** encrypts card data at the POI so that the merchant systems behind it never see usable PAN, which is what makes the **SAQ P2PE** path (and dramatic scope reduction) possible. Without P2PE, the POS, the store controller, and anything connected to them are typically in the CDE — exactly Ironvale's five CDE systems in UC-02 (POS terminals, payment switch, card vault, store controller, e-comm web).

### Which SAQ does a retailer use?

The card-present SAQ landscape is wider than e-commerce:

| SAQ | Typical retailer fit |
|---|---|
| **SAQ B** | Imprint machines or standalone dial-out terminals; no electronic cardholder-data storage |
| **SAQ B-IP** | Standalone, PTS-approved IP-connected POI terminals; no electronic storage |
| **SAQ C** | Payment-application systems connected to the internet; no electronic storage after authorization |
| **SAQ C-VT** | Web-based virtual terminal on an isolated machine; manual single-transaction keying |
| **SAQ P2PE** | A validated PCI P2PE solution; POI encrypts card data; merchant systems never see PAN |

For the e-commerce channel, the SAQ A vs A-EP question from `industries/saas-technology.md` applies. A retailer running both channels may use different SAQs per channel or roll up into a single ROC; a large retailer like Ironvale validates the whole estate via a **full ROC**.

### How does store-network segmentation reduce scope?

This is the retailer's highest-leverage move and the spine of UC-02. **In-scope = CDE + connected/security-impacting systems; out = segmented and validated out of scope.** Every system you can defensibly isolate from the CDE — guest wifi, corporate email, HR, dev sandboxes — comes out of scope, and the effect is deterministic: moving one connected system out lowers the in-scope count by exactly one. Ironvale's 14-system inventory scopes to **10 in-scope / 4 out-of-scope** precisely because four systems are segmented out. Segmentation is not a requirement, but it is the difference between assessing 10 systems and assessing 14.

### What is special about a franchise (multi-site)?

A franchise concentrates the multi-site problem: many near-identical locations, often a mix of franchisor-provided and franchisee-managed systems, and a single validation that must hold across all of them. UC-03's franchise validates via **SAQ D** across 30 locations, and the recurring issue is a **legacy POS that cannot meet a defined control** at some sites — handled as a **compensating control** (Appendix B/C), not waived. For an assessor, multi-site means **sampling**: the assessment confirms scope and tests a representative sample across the location population rather than every site.

## What's unique to retail / e-commerce

- **Two channels, two scope stories.** Card-present scope is about POS/POI and the store network; e-commerce scope is about the payment page. Many retailers get the e-commerce SAQ A/A-EP call wrong while focusing on the stores.
- **P2PE is the card-present scope-minimization lever** — a validated P2PE solution is what takes the store systems out of the PAN's path.
- **Segmentation is the on-prem scope lever** — UC-02 shows the count drop directly; the in-scope total is what you pay for.
- **Franchise = sampling + consistency** — one validation, many sites, a representative sample, and compensating controls where a site's legacy system cannot meet a defined control (UC-03).
- **PAN never appears** — even in card-present examples, card data is modeled as a scoping fact, never shown.

## Anti-hallucination

- **Merchant levels (L1/L2/...) are brand-defined** — payment brands and acquirers set them, not PCI DSS; UC-02 labels Ironvale "L1 (brand-defined)" deliberately.
- **Segmentation is not a PCI requirement** — it is a scope-reduction technique; un-segmented systems connected to the CDE are in scope by default.
- **P2PE scope reduction requires a PCI-listed P2PE solution** — encryption alone is not the same as a validated P2PE deployment.
- **A compensating control (UC-03) is not a customized approach (UC-02)** — the former is constraint-driven against an existing requirement; the latter is an objective-met-differently design choice with a TRA.
- **Future-dated v4.0.1 requirements are in force** — including the e-commerce client-side script requirements 6.4.3/11.6.1; never optional [PCI-SSC-Blog-v401 §v4.0.1].
- **No PAN is ever shown** — examples carry zero cardholder data.

## Cross-references

- `use-cases/uc-02-roc-segmentation.md` — the worked full-ROC scoping/segmentation engagement and a customized-approach request with a TRA.
- `use-cases/uc-03-compensating-control.md` — the franchise compensating-control worksheet.
- `chunks/02-scoping-and-segmentation.md` — CDE scoping, connected systems, segmentation as scope reduction, and assessor sampling.
- `chunks/03-saq-selection.md` — the full SAQ catalog (10 types) and the selection decision tree, including the card-present B/B-IP/C/C-VT/P2PE paths.
- `industries/saas-technology.md` — the e-commerce-channel SAQ A vs A-EP determination and the client-side script requirements.
