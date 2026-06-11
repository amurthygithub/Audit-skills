---
chunk_id: 01-scope-and-applicability
parent_skill: pci-dss-assessment
topic: "What PCI DSS applies to; account data = CHD + SAD; the CDE; network security controls (NSC) terminology; the 6 goals -> 12 requirements map; counting conventions; v4.0.1 currency banner"
load_when: "user asks what PCI DSS covers, who must comply, what account data / the CDE is, NSC vs firewall, the 6 goals, how many requirements/sections exist, or counting conventions"
---

# Chunk 01 — Scope and Applicability

PCI DSS v4.0.1 (June 2024) is the only active version of the Payment Card Industry Data Security Standard [PCI-SSC-Document-Library]. It is a **limited revision** of v4.0 with **no new or deleted requirements** [PCI-SSC-Blog-v401]; v4.0 retired 2024-12-31. **All future-dated requirements are mandatory now** — in force since 2025-03-31; the printed "best practice until 31 March 2025" notes are historical, and this skill presents those requirements as fully effective (see `chunks/08`).

## 1. What PCI DSS applies to

PCI DSS applies to all entities that **store, process, or transmit account data**, and to entities that could **affect the security** of account data — primarily **merchants** (accept cards for goods/services) and **service providers** (handle account data, or control/impact its security, on behalf of others). Applicability is a function of how account data flows, not of organization size.

## 2. Account data = cardholder data (CHD) + sensitive authentication data (SAD)

Req 3's title is **"Protect Stored Account Data"** — renamed in v4 from "cardholder data". **Account data** is the umbrella term:

- **Cardholder data (CHD)** — the primary account number (**PAN**), and, when present with the PAN, cardholder name, expiration date, and service code. The PAN is the defining data element: where the PAN goes, scope follows.
- **Sensitive authentication data (SAD)** — full track data, card verification code/value, and PINs/PIN blocks. **SAD must not be retained after authorization**, even if encrypted (paraphrased intent of Req 3.3).

**Full PAN never appears in this skill's examples or outputs** — modeled as a teaching point: assessment artifacts should reference masked/truncated values or surrogate identifiers, never a live PAN. (Display masking and storage rules are themselves Req 3 controls.)

## 3. The cardholder data environment (CDE)

The **CDE** is the people, processes, and system components that **store, process, or transmit account data**, plus system components that are **connected to** or could **impact the security of** that environment. Scope therefore has three bands — CDE systems, connected-to/security-impacting systems, and out-of-scope systems — developed in `chunks/02-scoping-and-segmentation.md`. Scope is the highest-leverage decision in any assessment: it determines which of the 249 defined requirements apply and which validation path fits.

## 4. Network security controls (NSCs) — do not say "firewall requirement"

**Req 1 is "Install and Maintain Network Security Controls."** v4 generalized the v3.x "firewalls and routers" language to **network security controls (NSCs)** — a technology-neutral term covering firewalls, but also cloud security groups, virtual/software-defined NSCs, container network policies, and other controls that enforce traffic rules between network segments. Teaching Req 1 as "the firewall requirement" is a v3-era anachronism this skill avoids.

## 5. The 6 goals → 12 principal requirements

PCI DSS groups its **12 principal requirements** under **6 goals**:

| Goal | Requirements | Official titles |
|------|-------------|-----------------|
| Build and Maintain a Secure Network and Systems | 1-2 | 1 Install and Maintain Network Security Controls; 2 Apply Secure Configurations to All System Components |
| Protect Account Data | 3-4 | 3 Protect Stored Account Data; 4 Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks |
| Maintain a Vulnerability Management Program | 5-6 | 5 Protect All Systems and Networks from Malicious Software; 6 Develop and Maintain Secure Systems and Software |
| Implement Strong Access Control Measures | 7-9 | 7 Restrict Access to System Components and Cardholder Data by Business Need to Know; 8 Identify Users and Authenticate Access to System Components; 9 Restrict Physical Access to Cardholder Data |
| Regularly Monitor and Test Networks | 10-11 | 10 Log and Monitor All Access to System Components and Cardholder Data; 11 Test Security of Systems and Networks Regularly |
| Maintain an Information Security Policy | 12 | 12 Support Information Security with Organizational Policies and Programs |

Requirements 1-6 are detailed in `chunks/04`; Requirements 7-12 in `chunks/05`.

## 6. Counting conventions (always label which you use)

All counts are from the mechanical inventory of the v4.0.1 main body:

| Level | Count | Convention |
|-------|-------|-----------|
| Goals | **6** | overview-table goal groups |
| Principal requirements | **12** | the titled Req 1-12 |
| Sections (x.y) | **63** | x.y headings; per requirement 5/3/7/2/4/5/3/6/5/7/6/10 (Req 1→12) |
| Main-body defined requirements | **249** | numbered x.y.z (**205**) + x.y.z.w (**44**) rows; testing procedures (letter suffixes) excluded |
| Appendix A requirements | **30** (in 8 sections) | A1 multi-tenant / A2 SSL-early-TLS POS POI / A3 DESV |
| SAQ types | **10** | A, A-EP, B, B-IP, C, C-VT, D-Merchant, D-Service-Provider, P2PE, SPoC |
| Lettered appendices | **A-G** | A (A1/A2/A3); B/C compensating controls; D/E customized approach; F SSF pointer; G glossary |

Secondary sources cite various bare totals (e.g., "~250", "264") depending on whether testing procedures and appendix rows are counted. **Never assert a bare requirement total** — state counts only with these conventions.

## 7. Validation levels are brand-defined

Merchant and service-provider "levels" (L1/L2/etc.) and any transaction-volume thresholds are set by the **payment brands and acquirers**, not by PCI SSC or the standard, and they vary by brand and agreement. This skill names them only as brand-specific and variable; it never asserts a level threshold as an SSC fact. The acquirer (or the relevant brand) tells a merchant which level and validation cadence apply. See `chunks/08-currency-and-program-context.md`.

## 8. Appendices at a glance

- **Appendix A** — additional requirements: A1 (multi-tenant service providers), A2 (entities still using SSL/early TLS for card-present POS POI terminal connections), A3 (Designated Entities Supplemental Validation, DESV).
- **Appendix B/C** — compensating controls and the compensating-controls worksheet (`chunks/07`).
- **Appendix D/E** — the customized approach and sample templates (`chunks/07`).
- **Appendix F** — leveraging the PCI Software Security Framework to support Requirement 6 (pointer only; the SSF itself is out of scope).
- **Appendix G** — glossary of terms, abbreviations, and acronyms (the authoritative definitions of account data, CHD, SAD, CDE, NSC, TRA).
