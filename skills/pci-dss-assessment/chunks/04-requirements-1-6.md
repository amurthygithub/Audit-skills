---
chunk_id: 04-requirements-1-6
parent_skill: pci-dss-assessment
topic: "Requirements 1-6: build/maintain secure networks (1-2), protect account data (3-4), vulnerability management (5-6) — section-level map with paraphrased intent and evidence examples"
load_when: "user asks about Requirement 1-6, network security controls, secure configurations, protecting stored account data, transmission cryptography, anti-malware, or secure software development"
---

# Chunk 04 — Requirements 1-6

Section-level map (x.y) with **paraphrased intent** and evidence examples. Requirement bodies and testing procedures live in the licensed standard, not here. Several requirements once marked "best practice until 31 March 2025" are flagged **[in force now]** — mandatory since 2025-03-31, never optional.

## Req 1 — Install and Maintain Network Security Controls (5 sections)
Not "the firewall requirement" — NSCs include firewalls, cloud security groups, and virtual/software-defined controls.

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 1.1 | Governance: NSC processes/policies defined, documented, assigned | policies; roles |
| 1.2 | NSC configuration standards and change control | config standards; change tickets |
| 1.3 | Restrict inbound/outbound traffic to/from the CDE | ruleset; CDE boundary diagram |
| 1.4 | Control connections between trusted and untrusted networks | DMZ design; anti-spoofing |
| 1.5 | Manage risk from computing devices that connect to both the CDE and untrusted networks | endpoint controls for dual-homed devices |

## Req 2 — Apply Secure Configurations to All System Components (3 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 2.1 | Governance of secure-configuration processes | config-management policy |
| 2.2 | System components configured securely; **change vendor defaults** (passwords, settings) | hardening standards; default-changed evidence |
| 2.3 | Secure wireless configurations and change wireless vendor defaults | wireless config baseline |

## Req 3 — Protect Stored Account Data (7 sections)
**Account data = CHD + SAD.** SAD must not be retained after authorization. **No full PAN in any artifact** (teaching point).

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 3.1 | Governance of stored-data protection | data-retention policy |
| 3.2 | Keep stored account data to a minimum; defined retention/disposal | retention schedule; purge logs |
| 3.3 | Do not store SAD after authorization | SAD-handling review |
| 3.4 | Mask PAN when displayed (limit who sees full PAN) | masking config |
| 3.5 | Render stored PAN unreadable (e.g., strong cryptography, truncation, hashing, tokenization) | crypto/tokenization design |
| 3.6 | Protect cryptographic keys used to protect stored account data | key-management procedures |
| 3.7 | Key-management lifecycle (generation, distribution, rotation, retirement) | key-ceremony records |

## Req 4 — Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks (2 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 4.1 | Governance of transmission-protection processes | crypto policy |
| 4.2 | Strong cryptography for PAN in transit over open/public networks; trusted keys/certificates; never send unprotected PAN via end-user messaging | TLS config; cert inventory |

## Req 5 — Protect All Systems and Networks from Malicious Software (4 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 5.1 | Governance of anti-malware processes | AV/EDR policy |
| 5.2 | Anti-malware deployed, current, and active on applicable components | AV/EDR coverage report |
| 5.3 | Anti-malware mechanisms cannot be disabled/altered by users without authorization; periodic evaluations | tamper-protection config; scan logs |
| 5.4 | Anti-phishing mechanisms protect personnel **[in force now]** | phishing-defense controls |

## Req 6 — Develop and Maintain Secure Systems and Software (5 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 6.1 | Governance of secure-software processes | SDLC policy |
| 6.2 | Bespoke/custom software developed securely | secure-coding training; reviews |
| 6.3 | Identify and rank security vulnerabilities; patch within defined timeframes | vuln-management feed; patch SLAs |
| 6.4 | Protect public-facing web applications (WAF or review); **6.4.3 manage payment-page scripts [in force now]** | WAF/review records; script inventory |
| 6.5 | Manage changes to system components securely (change control) | change-management records |

**Appendix F pointer:** Req 6 can be supported by the PCI Software Security Framework (the SSF itself is out of scope; pointer only).

## Cross-references
Client-side script requirement **6.4.3** pairs with **11.6.1** (`chunks/05`) for A-EP/ROC e-commerce — see `chunks/03`. For "can we meet a Req-1/3/6 control differently or not at all," route to the defined-vs-customized and compensating-control logic in `chunks/07`.
