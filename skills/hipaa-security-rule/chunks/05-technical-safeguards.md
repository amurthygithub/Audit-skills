---
chunk_id: 05-technical-safeguards
parent_skill: hipaa-security-rule
topic: "§164.312 technical safeguards: 5 standards, 7 titled specs (2 R / 5 A); access control, audit controls, integrity, authentication, transmission security, encryption"
load_when: "user asks about access control, unique user IDs, automatic logoff, encryption, audit controls/logging, integrity mechanisms, authentication, or transmission security"
---

# Chunk 05 — Technical Safeguards (§164.312)

§164.312 [CFR-45-164-Subpart-C] contains **5 standards with 7 titled implementation specifications (2 Required / 5 Addressable)**. Technical safeguards (defined in §164.304) are "the technology and the policy and procedures for its use that protect electronic protected health information and control access to it." The rule is deliberately **technology-neutral** — it names outcomes (encrypt, authenticate, log), never products or algorithms. Addressable specs follow the §164.306(d)(3) workflow in `chunks/07-addressable-decisions-and-evidence.md`.

## 1. Access control — §164.312(a)(1)

Technical policies and procedures "to allow access only to those persons or software programs that have been granted access rights as specified in § 164.308(a)(4)" — the technical enforcement of the administrative access-management decisions.

| Spec | Title | Designation | Operative language |
|------|-------|-------------|--------------------|
| (a)(2)(i) | **Unique user identification** | **(Required)** | "Assign a unique name and/or number for identifying and tracking user identity" — shared accounts defeat this |
| (a)(2)(ii) | **Emergency access procedure** | **(Required)** | Procedures "for obtaining necessary electronic protected health information during an emergency" (break-glass access, itself logged and reviewed) |
| (a)(2)(iii) | Automatic logoff | (Addressable) | Electronic procedures that "terminate an electronic session after a predetermined time of inactivity" |
| (a)(2)(iv) | Encryption and decryption | (Addressable) | "Implement a mechanism to encrypt and decrypt electronic protected health information" — **data at rest** |

**Evidence:** account inventory showing 1:1 identity mapping (service accounts justified and owned); break-glass procedure and usage log; session-timeout configuration; encryption-at-rest configuration or the documented disposition.

## 2. Audit controls — §164.312(b) (no separate specs)

"Implement hardware, software, and/or procedural mechanisms that **record and examine** activity in information systems that contain or use" ePHI. This is the *mechanism* standard. Its administrative twin, §164.308(a)(1)(ii)(D) Information system activity review, is the *practice of regularly reviewing* the records — auditors test both: are logs captured, and are they actually examined (see `chunks/02 §1`)? **Evidence:** logging configuration per ePHI system; log retention; examination procedures.

## 3. Integrity — §164.312(c)(1)

Policies and procedures "to protect electronic protected health information from improper alteration or destruction."

| Spec | Title | Designation |
|------|-------|-------------|
| (c)(2) | Mechanism to authenticate electronic protected health information | (Addressable) |

The (c)(2) mechanism corroborates "that electronic protected health information has not been altered or destroyed in an unauthorized manner" — checksums, digital signatures, version control, database integrity features. **Evidence:** integrity-mechanism configuration or disposition record.

## 4. Person or entity authentication — §164.312(d) (no separate specs)

"Implement procedures to verify that a person or entity seeking access to electronic protected health information is the one claimed." Authentication (§164.304) is "the corroboration that a person is the one claimed." The rule does not mandate any particular factor count or method — MFA is a common risk-analysis-driven outcome, not a Subpart C requirement as written. **Evidence:** authentication policy and configuration (factors, password rules tying to §164.308(a)(5)(ii)(D)).

## 5. Transmission security — §164.312(e)(1)

Technical measures "to guard against unauthorized access to electronic protected health information that is being transmitted over an electronic communications network."

| Spec | Title | Designation | Operative language |
|------|-------|-------------|--------------------|
| (e)(2)(i) | Integrity controls | (Addressable) | Ensure transmitted ePHI "is not improperly modified without detection until disposed of" |
| (e)(2)(ii) | Encryption | (Addressable) | "Implement a mechanism to encrypt electronic protected health information whenever deemed appropriate" — **data in transit** |

**Evidence:** TLS/VPN configuration for every ePHI flow (including email handling rules); or the documented disposition with alternative measures.

## 6. Encryption: Addressable as written, de facto expectation

Both encryption specs — at rest (§164.312(a)(2)(iv)) and in transit (§164.312(e)(2)(ii)) — are **(Addressable) in the text in force**. Treat them with the documented-decision pattern:

- The §164.306(d)(3) assessment almost always concludes encryption **is** reasonable and appropriate for modern environments (cloud hosting, portable devices, internet transmission), so the typical disposition is `implement`. In UC-01, the encryption-at-rest disposition is *derived* from the seed facts (cloud-hosted, ePHI volume, no compensating control), not assumed.
- A disposition other than `implement` demands an unusually strong documented justification plus an equivalent alternative measure if reasonable and appropriate — and it forfeits the practical benefit that properly encrypted ePHI is treated as secured for breach-notification purposes (the "unsecured PHI" concept is defined in Subpart D, §164.402 — pointer only; Subpart D mechanics are out of scope).
- Enforcement experience (lost unencrypted laptops and media) makes unencrypted portable ePHI the classic indefensible disposition.

## 7. Crosswalks (pointer only)

This skill encodes **no crosswalk rows**. Security Rule ↔ CSF ↔ 800-53 mappings were removed from SP 800-66r2 and placed online in the NIST CPRT (Appendix D of [NIST-SP-800-66-Rev2]); that mapping targets **CSF v1.1** and is "intentionally broad" — never claim an official CSF 2.0 mapping. Row-level encoding is tracked separately (SOX-638). See `chunks/01 §7`.

## 8. Anti-hallucination notes for this chunk

- Exactly **2 Required / 5 Addressable** titled specs in this family; the Required pair is Unique user identification (§164.312(a)(2)(i)) and Emergency access procedure (§164.312(a)(2)(ii)).
- **Encryption is Addressable in the text in force — in both places.** Do not state that the current rule "requires encryption"; state the disposition pattern above. (The regulatory horizon for encryption is covered, with explicit status labels, in `chunks/08-enforcement-audit-and-nprm.md`.)
- The rule as written does not mandate MFA, specific algorithms, key lengths, or session-timeout values — those are risk-analysis outcomes, not Subpart C text.
- Audit controls (§164.312(b)) and Person or entity authentication (§164.312(d)) have **no separate specs**; the Appendix A "(R)" for each is a standard-level entry under the 42-entry counting convention (see `chunks/01 §6.2`).
- Integrity controls (§164.312(e)(2)(i), transmission) and the Integrity standard's mechanism (§164.312(c)(2), storage) are distinct specs — do not merge them.
