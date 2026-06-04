# Industry: Healthcare (payer / provider / health-tech)

Healthcare entities (HIPAA-covered entities and business associates) have the **HIPAA Security Rule** as their native cybersecurity framework. NIST 800-53 is a **crosswalk and overlay**, not a replacement. The healthcare industry file captures where 800-53 supports, supplements, or is required alongside HIPAA.

## 1. Posture

| Sub-sector | HIPAA context | 800-53 application |
|------------|---------------|---------------------|
| Hospital / health system | Covered entity; PHI in EHR | 800-53 is a crosswalk; 800-66 Rev 2 is the authoritative HIPAA mapping |
| Health plan / payer | Covered entity; PHI in claims, member data | 800-53 supports HIPAA + state insurance (e.g., NYDFS) |
| Business associate (clearinghouse, claims processor, BAA-covered SaaS) | Business associate; PHI under BAA | 800-53 crosswalk; BA agreement may require 800-53 mapping |
| Health-tech SaaS (BAA-covered) | Business associate | 800-53 is a market differentiator (federal customers) |
| Federal contractor (e.g., DoD health agency, VA) | Covered entity + federal contractor | 800-53 is mandatory; HIPAA + 800-53 crosswalk |

## 2. Boundary

- The system in scope is whatever handles PHI. A hospital may have dozens of systems (EHR, PACS, lab, billing, HR, patient portal) — each with its own boundary and risk assessment.
- For a business associate, the system is whatever handles PHI on behalf of a covered entity, plus the BAA-mandated controls (breach notification, audit access, etc.).

## 3. Inheritance pattern

- Healthcare entities often run on commercial cloud (AWS, Azure, GCP) without FedRAMP authorization. Inheritance is from the cloud's SOC 2 / ISO 27001 package, not from a FedRAMP package.
- BAAs with cloud providers (e.g., AWS BAA, Azure BAA) document the inheritance boundary for HIPAA controls.
- The 800-53 view adds a second layer: the controls from 800-53 that map to HIPAA safeguards. Many HIPAA safeguards overlap with 800-53 controls; the gaps are typically in privacy (the 800-53 PT family (Rev 5)), supply chain (SR family), and program management (PM family).

## 4. Regulator / customer relationship

- **HHS Office for Civil Rights (OCR)** — enforces HIPAA. Audit and enforcement actions can result in settlement agreements (e.g., the Anthem $16M settlement, the Excellus $5.1M settlement).
- **State attorneys general** — enforce state breach notification laws and (in some states) cybersecurity regulations.
- **Federal customers** — if the entity is a federal contractor, the customer imposes 800-53 / FedRAMP / CMMC requirements.
- **Business associate customers** — the BAA may require 800-53 mapping as part of due diligence.

## 5. Top use cases

- (Planned UC-04 — HIPAA + 800-53 crosswalk for a health-tech SaaS)

## 6. Pain points (healthcare)

- **Two frameworks, one operating model** — HIPAA Security Rule and 800-53 must be tested in parallel. The 800-66 Rev 2 mapping is the bridge; use it.
- **Privacy controls** — the 800-53 PT family (Rev 5) is often missed. PHI is sensitive; the privacy controls are mandatory.
- **Risk analysis** — HIPAA requires a risk analysis (45 CFR 164.308(a)(1)(ii)(A)); 800-53 has the same requirement in the RA family. Use the 800-30 Rev 1 risk assessment methodology to satisfy both.
- **Audit logging and review** — HIPAA requires audit controls (45 CFR 164.312(b)); 800-53 AU-2 / AU-6 are more granular. The 800-53 view is a superset.
- **Breach notification** — HIPAA's 60-day breach notification clock is independent of any 800-53 reporting. The IR family documents the response; the breach notification is a separate compliance workflow.
- **OCR enforcement** — HIPAA enforcement is real. The 800-53 view is a defense, not a guarantee.

## 7. References

- 45 CFR Part 164, Subpart C — HIPAA Security Rule
- 45 CFR Part 164, Subpart D — Breach Notification
- NIST SP 800-66 Rev 2 — Implementing the HIPAA Security Rule
- NIST SP 800-53 Rev 5 — privacy controls (PT family)
- HHS OCR Audit Protocol
- HITRUST CSF (crosswalk to 800-53)
- NIST Cybersecurity Framework 2.0
