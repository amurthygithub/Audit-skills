---
chunk_id: 04-physical-safeguards
parent_skill: hipaa-security-rule
topic: "§164.310 physical safeguards: 4 standards, 8 titled specs (2 R / 6 A); facility, workstation, device and media controls"
load_when: "user asks about facility access, workstation use/security, device and media controls, disposal, or media re-use"
---

# Chunk 04 — Physical Safeguards (§164.310)

§164.310 [CFR-45-164-Subpart-C] contains **4 standards with 8 titled implementation specifications (2 Required / 6 Addressable)**. Physical safeguards (defined in §164.304) are "physical measures, policies, and procedures to protect a covered entity's or business associate's electronic information systems and related buildings and equipment, from natural and environmental hazards, and unauthorized intrusion." The two Required specs in this family — **Disposal** and **Media re-use** — are recurring enforcement themes: discarded or resold devices with recoverable ePHI. Addressable specs follow the §164.306(d)(3) workflow in `chunks/07-addressable-decisions-and-evidence.md`.

## 1. Facility access controls — §164.310(a)(1)

Limit physical access to electronic information systems and the facilities housing them, "while ensuring that properly authorized access is allowed."

| Spec | Title | Designation | Operative language |
|------|-------|-------------|--------------------|
| (a)(2)(i) | Contingency operations | (Addressable) | Procedures allowing facility access "in support of restoration of lost data under the disaster recovery plan and emergency mode operations plan in the event of an emergency" |
| (a)(2)(ii) | Facility security plan | (Addressable) | Safeguard "the facility and the equipment therein from unauthorized physical access, tampering, and theft" |
| (a)(2)(iii) | Access control and validation procedures | (Addressable) | Control and validate access "based on their role or function, including visitor control, and control of access to software programs for testing and revision" |
| (a)(2)(iv) | Maintenance records | (Addressable) | Document "repairs and modifications to the physical components of a facility which are related to security (for example, hardware, walls, doors, and locks)" |

All four specs are Addressable — common dispositions for cloud-hosted BAs document that the data-center facility controls are the cloud provider's responsibility under the shared-responsibility model, with the BAA/attestations as the alternative-measure evidence (see `industries/saas-technology.md`). **Evidence:** badge/key inventories, visitor logs, facility security plan, security-relevant maintenance tickets.

## 2. Workstation use — §164.310(b) (no separate specs)

Policies and procedures specifying "the proper functions to be performed, the manner in which those functions are to be performed, and the physical attributes of the surroundings of a specific workstation or class of workstation that can access" ePHI. Note the §164.304 definition of workstation includes laptops and "electronic media stored in its immediate environment" — remote and home-office settings are in scope. **Evidence:** acceptable-use/workstation-use policy by workstation class; remote-work rules.

## 3. Workstation security — §164.310(c) (no separate specs)

"Implement physical safeguards for all workstations that access electronic protected health information, to restrict access to authorized users." Where §164.310(b) governs *behavior*, (c) governs *physical protection*: placement, locks, screen privacy, theft deterrence. **Evidence:** workstation inventory; physical-security measures (cable locks, secured rooms, auto-lock screens as a complement to §164.312(a)(2)(iii)).

## 4. Device and media controls — §164.310(d)(1)

Govern "the receipt and removal of hardware and electronic media that contain electronic protected health information into and out of a facility, and the movement of these items within the facility."

| Spec | Title | Designation | Operative language |
|------|-------|-------------|--------------------|
| (d)(2)(i) | **Disposal** | **(Required)** | Address "the final disposition of electronic protected health information, and/or the hardware or electronic media on which it is stored" |
| (d)(2)(ii) | **Media re-use** | **(Required)** | Remove ePHI "from electronic media before the media are made available for re-use" |
| (d)(2)(iii) | Accountability | (Addressable) | "Maintain a record of the movements of hardware and electronic media and any person responsible therefore" |
| (d)(2)(iv) | Data backup and storage | (Addressable) | "Create a retrievable, exact copy of electronic protected health information, when needed, before movement of equipment" |

**Disposal and media re-use are the only two Required physical specs.** Treat decommissioning as a controlled process: sanitization or destruction before disposal/resale/return (including copiers, medical devices, and leased equipment with embedded storage), with certificates of destruction retained per §164.316(b)(2)(i). **Evidence:** media-disposition policy; sanitization/destruction certificates; asset-movement logs; pre-move backup records.

## 5. Anti-hallucination notes for this chunk

- Exactly **2 Required / 6 Addressable** titled specs in this family; the Required pair is Disposal (§164.310(d)(2)(i)) and Media re-use (§164.310(d)(2)(ii)). All four facility-access specs are Addressable.
- Workstation use (§164.310(b)) and Workstation security (§164.310(c)) have **no separate specs**; the standards themselves are mandatory. Appendix A prints an "(R)" for each — that is a standard-level entry under the 42-entry counting convention, not a titled spec (see `chunks/01 §6.2`).
- "Addressable" facility specs still require a documented disposition — a cloud tenant documents the provider-responsibility analysis; it does not silently skip the standard (§164.306(d)(3); `chunks/07`).
- The accountability spec's "therefore" (not "therefor") is the rule text's own spelling — quote it as printed.
