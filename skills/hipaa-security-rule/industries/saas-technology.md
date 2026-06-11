---
industry: saas-technology
parent_skill: hipaa-security-rule
title: "SaaS / health-tech — business associate direct liability, BAA flow-down, shared responsibility, and honest SOC 2 evidence reuse"
version: 0.1.0
status: active
frameworks: [CFR-45-164-Subpart-C, NIST-SP-800-66-Rev2, PL-116-321]
primary_personas: [Health-tech SaaS compliance lead, CTO/VP Engineering, CISO, Deal-desk/security questionnaire owner]
regulatory_anchors: [HIPAA-Security-Rule, HITECH-BA-direct-liability]
last_verified: "2026-06-10"
---

# SaaS / health-tech — the business associate lens

A SaaS company that creates, receives, maintains, or transmits ePHI for covered-entity customers is a **business associate**, and since the 2013 Omnibus amendments the Security Rule binds it **directly** — §164.302 reads "a covered entity or business associate," and OCR can enforce against the BA itself, not only through the customer's contract. This view applies the skill to the health-tech BA. The UC-01 engagement (`use-cases/uc-01-ba-risk-analysis.md`, CareSync Relay — 40 staff, fully remote, AWS, 12 CE customers) is the worked example; UC-03 (`use-cases/uc-03-baa-and-checklist.md`) covers the smallest BA.

## The health-tech framing

### "Our customers are the covered entities — isn't HIPAA their problem?"

No. Direct liability means the BA owes the full Subpart C program in its own name: risk analysis (§164.308(a)(1)(ii)(A)), all Required specs, a documented §164.306(d)(3) disposition for every addressable spec, §164.314-conforming BAAs, and §164.316 documentation with 6-year retention. The BAA with each CE customer is *additional* to direct liability, not the source of it. The statutory layer is HITECH §13401 (Pub. L. 111-5), cited in the subpart's authority note.

### What is BAA flow-down and when does it bite?

§164.308(b)(2): a business associate may let a **subcontractor** create, receive, maintain, or transmit ePHI on its behalf "only if the business associate obtains satisfactory assurances, in accordance with § 164.314(a), that the subcontractor will appropriately safeguard the information." For a SaaS, "subcontractor" includes the managed-database vendor, the LLM/analytics processor, the support-tooling provider that can see ticket attachments — any party touching ePHI on your behalf. Each needs a BAA whose terms meet §164.314(a)(2)(i)(A)–(C), and the chain continues downstream (§164.314(a)(2)(iii)). A flow-down clause is also one of the provisions your *upstream* BAA must contain — the exact omission seeded in UC-03.

### Where does shared responsibility with the cloud provider start and stop?

The cloud provider (itself your BA, under a BAA, when ePHI sits on its infrastructure) carries the data-center physical layer: §164.310 facility access controls, environmental protections, hardware disposal in its data centers. You carry everything the provider's shared-responsibility line leaves on your side: tenant configuration, §164.312 technical safeguards (access control, audit logging, encryption configuration), §164.308 administrative program, workstation/endpoint controls (§164.310(b)–(c) still apply to *your* laptops, even fully remote). UC-01 shows the clean way to express the inherited layer: the facility-related addressable specs are dispositioned `not_reasonable_documented` with the provider's controls as the documented context — never silently skipped. That path applies only because CareSync Relay operates **no facility housing ePHI systems**; a BA that does operate one (an office server room, a colocation cage) dispositions the §164.310(a)(2) specs `implement` or `alternative_measure` instead. Inheritance is a documented disposition, not an assumption.

### Can we reuse our SOC 2 evidence for HIPAA?

**Overlap, not equivalence — label it that way.** A SOC 2 Type II report exercises many of the same operational controls (access provisioning, change management, incident response, monitoring), and the underlying evidence — tickets, configs, review records — often serves both. But:

- SOC 2 criteria are not Security Rule standards; no attestation maps 1:1 to §§164.308/310/312, and a clean SOC 2 opinion is not a compliance determination under HIPAA.
- The Security Rule demands artifacts SOC 2 never produces: the §164.308(a)(1)(ii)(A) risk analysis scoped to ePHI, the §164.306(d)(3) disposition record per addressable spec, §164.314-conforming BAAs, and §164.316 documentation discipline.
- Reuse the *evidence*, re-perform the *mapping*: walk each Security Rule standard, cite the SOC 2-collected artifact where it genuinely satisfies the spec, and document the gap where it does not. This skill encodes no SOC 2 crosswalk rows — treat any mapping table you build as interpretive.

## What's unique to health-tech SaaS

- **One program, many masters.** 12 CE customers means 12 BAAs with slightly different incident-reporting clocks; the §164.314(a)(2)(i)(C) reporting obligation is the floor — track the strictest contractual variant separately.
- **Remote-first changes the physical story, not the obligation.** §164.310(b)–(c) workstation standards follow the laptop into the home office; with no organization-controlled facility the facility specs get honest `not_reasonable_documented` dispositions (UC-01 §3) — a BA operating its own facility would `implement` them instead.
- **Addressable specs are where engineering reality lives.** Passwordless auth (an *equivalent alternative measure* to §164.308(a)(5)(ii)(D) password management), SSO-centralized log-in monitoring — modern stacks frequently satisfy 2003 specs via documented alternatives. The documentation is the compliance.
- **Recognized security practices pay off here** [PL-116-321]: a BA that can evidence 12 months of consistently applied practices gets that considered in certain penalty/audit determinations — mitigation, not immunity.

## Anti-hallucination

- **BA direct liability dates to the Omnibus amendments (78 FR 5566, effective 2013)** — do not describe Security Rule exposure as flowing only through the customer contract.
- **A BAA is required with the cloud provider when it maintains ePHI** — "we never look at the data" does not remove BA status for a persistent-storage provider.
- **SOC 2 ↔ HIPAA is overlap, not equivalence**; this skill ships no crosswalk rows (mappings live in the NIST CPRT; row-level encoding is tracked as SOX-638).
- **The 2025 NPRM is PROPOSED only as of 2026-06-10** [HIPAA-Security-NPRM-2025] — its mandatory-encryption and MFA proposals are not current law; current law makes those addressable/derivable decisions (see UC-01's derived `implement`).
- **No small-entity exemption exists** — §164.306(b)(2) flexibility scales the how, never the whether (see UC-03).

## Cross-references

- `use-cases/uc-01-ba-risk-analysis.md` — the worked BA engagement: 15-risk register, all-22 addressable dispositions, derived encryption-at-rest decision.
- `use-cases/uc-03-baa-and-checklist.md` — BAA completeness check and the right-sized solo-BA program.
- `chunks/06-organizational-and-documentation.md` — §164.314 BAA required provisions and subcontractor chains.
- `chunks/07-addressable-decisions-and-evidence.md` — the disposition-record template these engagements populate.
- `aicpa-soc-reporting` (sibling skill) — authoritative for SOC 2 report content and the evidence lifecycle; pair it with this skill for the reuse-with-mapping pattern above.
