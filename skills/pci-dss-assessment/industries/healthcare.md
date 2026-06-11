---
industry: healthcare
parent_skill: pci-dss-assessment
title: "Healthcare — providers taking card payments (the overlooked CDE), scope-minimization via P2PE/outsourcing, and the vendor-management overlap with HIPAA"
version: 0.1.0
status: active
frameworks: [PCI-DSS-4.0.1]
primary_personas: [Healthcare revenue-cycle/IT lead, Practice administrator, CISO, Compliance officer]
regulatory_anchors: [PCI-DSS-v4.0.1, scope-minimization]
last_verified: "2026-06-11"
---

# Healthcare — the overlooked card-data environment

Healthcare providers are HIPAA-focused by reflex, so the **card-data environment is the part everyone forgets**: the front-desk terminal, the patient-portal "pay my bill" page, the phone payments revenue-cycle staff take, the kiosk in the lobby. Every one of those accepts a PAN, and PCI DSS applies to that PAN exactly as it does to a retailer's. This view applies the skill to a healthcare provider acting as a **merchant**. There is no seeded PCI UC dedicated to healthcare in v1; the provider reuses the UC-01 SAQ-selection method (for the patient-portal payment page) and the UC-02 scoping method (for the practice's systems).

## The healthcare framing

### Where is the CDE in a clinic or hospital that "doesn't do retail"?

Wherever a PAN is accepted, stored, processed, or transmitted:

- The **patient-portal payment page** — an e-commerce CDE with the same SAQ A vs A-EP question as any online merchant (does the practice control the payment-page scripts, and do its servers receive PAN?). Use the UC-01 method.
- **Front-desk / point-of-care terminals** — a card-present CDE; the POS/POI and store-network considerations from `industries/retail-ecommerce.md` apply.
- **Phone (MOTO) payments** — revenue-cycle staff keying card data is card-not-present processing that pulls the workstation, the recording system, and the path into scope.
- **Third-party billing/payment vendors** — frequently the actual processor; the provider's job is to confirm their compliance and document the responsibility boundary.

The recurring mistake is treating PCI as "not our problem because we're a hospital." If you take a card, it is your problem.

### How does a provider minimize PCI scope?

Same levers as any merchant, and the goal is to keep the PAN out of the provider's systems entirely:

- **Outsource the payment page** to a compliant TPSP (redirect/iframe, no merchant scripts) to stay on **SAQ A** for the portal — adding merchant scripts moves you to **SAQ A-EP** and the 6.4.3/11.6.1 scope (UC-01).
- **Use a PCI-listed P2PE solution** at front-desk terminals so the POI encrypts card data and the practice systems never see usable PAN (the **SAQ P2PE** path; see `industries/retail-ecommerce.md`).
- **Outsource MOTO/phone payments** to a compliant vendor and keep card data out of recordings and notes.
- **Segment** any remaining in-scope systems away from the clinical network (the UC-02 method).

The smaller the PAN's footprint in your environment, the smaller and cheaper the assessment.

### How do PCI DSS and HIPAA relate — and where do they not?

They protect **different data**: PCI DSS protects **cardholder data** (the PAN and related account data); the HIPAA Security Rule protects **electronic protected health information (ePHI)**. A patient's payment-card number is not ePHI, and a diagnosis is not cardholder data — do not conflate the two scopes, and do not assume a HIPAA control satisfies a PCI requirement (or vice versa).

What **does** transfer is the **discipline**, especially **vendor management**. Both regimes require you to know which third parties touch the regulated data and to obtain assurances they protect it: HIPAA does this through business-associate agreements (§164.308(b) / §164.314(a)), and PCI DSS does it through service-provider due diligence and the responsibility matrix (the Requirement 12 third-party program). A provider that already runs a mature HIPAA vendor-management program has the muscle to run the PCI one — same discipline, different data and different paperwork.

For the HIPAA Security Rule itself — risk analysis, addressable dispositions, BAA completeness — use the **`hipaa-security-rule` skill**; this view references into it for the vendor-management pattern and does not restate Security Rule facts here.

## What's unique to healthcare

- **The CDE hides behind the HIPAA program** — the first deliverable is finding every place a PAN is accepted, which the HIPAA-centric inventory usually misses.
- **Different data, same vendor-management muscle** — reuse the third-party diligence discipline you already run for business associates; do not reuse the *mapping* (no control equivalence between the regimes).
- **Scope minimization is the whole game** — outsourcing and P2PE keep the PAN out of clinical systems entirely, so PCI never touches the EHR.
- **PAN and ePHI are separate scopes** — keep the inventories, the controls, and the assessments distinct even where the same vendor appears in both.
- **PAN never appears** — card data is modeled as a scoping fact, never shown (and never lands in a clinical record).

## Anti-hallucination

- **PCI DSS and HIPAA protect different data** — cardholder data vs ePHI; a control in one regime does not automatically satisfy the other, and this skill asserts no PCI↔HIPAA control-mapping rows.
- **Taking a card payment makes you a merchant** — "we're a healthcare provider, not a retailer" does not remove PCI DSS applicability.
- **The HIPAA reference is one-way** — for Security Rule mechanics use the `hipaa-security-rule` skill; this view borrows only the vendor-management discipline.
- **Merchant levels are brand-defined** — payment brands and acquirers set them, not PCI DSS.
- **Future-dated v4.0.1 requirements are in force**, including the patient-portal client-side script requirements 6.4.3/11.6.1; never optional [PCI-SSC-Blog-v401 §v4.0.1].
- **No PAN is ever shown** — examples carry zero cardholder data, and card data never belongs in a clinical record.

## Cross-references

- `use-cases/uc-01-saq-selection.md` — the SAQ A vs A-EP method for the patient-portal payment page.
- `use-cases/uc-02-roc-segmentation.md` — the scoping/segmentation method for a provider's systems.
- `industries/retail-ecommerce.md` — the card-present POS/POI and P2PE scope-minimization angles for front-desk terminals.
- `chunks/02-scoping-and-segmentation.md` — finding the CDE and minimizing scope.
- `hipaa-security-rule` (sibling skill) — authoritative for the HIPAA Security Rule; this view references into it for the vendor-management discipline (different data, same diligence) and does not restate Subpart C facts.
