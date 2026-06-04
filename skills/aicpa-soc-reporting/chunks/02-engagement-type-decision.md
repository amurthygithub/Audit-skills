---
chunk_id: 02-engagement-type-decision
parent_skill: aicpa-soc-reporting
topic: "Engagement Type Decision Tree and Type I vs Type II Report Decision"
load_when: "user needs to classify a SOC engagement, decide between SOC 1/2/3 or SOC for Cybersecurity/Supply Chain, or determine Type I vs Type II"
---

# Chunk 02 -- Engagement Type Decision

## Engagement Classification

When a user describes a service organization, execute this decision logic:

Step 1: Is the subject matter related to Internal Control Over Financial Reporting (ICFR)?
  -> YES: SOC 1 (AT-C 320)
     Ask: Does the user entity's financial statement auditor need this?
       -> YES: SOC 1 is the correct choice
       -> NO: Consider TSC criteria; go to Step 2
  -> NO: Proceed to Step 2

Step 2: Are Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy) the subject matter?
  -> YES: Ask about distribution requirements
     Restricted distribution acceptable (NDA)?
       -> YES: SOC 2 (AT-C 205 + TSP Section 100)
       -> NO: SOC 3 (AT-C 205 + TSP Section 100, general use)
     REMINDER: Security criteria ALWAYS in scope for SOC 2/SOC 3
  -> NO: Proceed to Step 3

Step 3: Is the subject matter an entity's cybersecurity risk management program?
  -> YES: SOC for Cybersecurity (AT-C 205 + Cybersecurity Description Criteria)
     Distinguish: covers the ENTIRE entity's cybersecurity program, not a specific system
     Determine Type I (point in time) or Type II (period of time)
  -> NO: Proceed to Step 4

Step 4: Is the subject matter a production, manufacturing, or distribution system?
  -> YES: SOC for Supply Chain (AT-C 205 + adapted TSP Section 100)
     Applies to entities that manufacture, produce, or distribute physical or digital products
  -> NO: This may not be a SOC engagement. Consider:
     AT-C 205 for custom examination, AT-C 210 for review, AT-C 215 for AUP
     Advise consulting a licensed CPA practitioner

Always walk through all steps before concluding. If the scenario does not fit any SOC type, explicitly state that and recommend alternative engagement types.

## Type I vs Type II Decision

Step 1: Does the user entity need assurance on operating effectiveness?
  -> YES: Type II is required
     Determine examination period:
       <6 months: advise minimum is 6 months; consider Type I first
       6-12 months: standard Type II period (12 months is most common)
       >12 months: rare; discuss with practitioner
  -> NO: Type I may be sufficient -> Step 2

Step 2: Is this a first-time SOC engagement?
  -> YES: Recommend Type I as readiness assessment to identify and remediate gaps
  -> NO: Type II is standard for established SOC programs

Step 3: What is the user entity requesting?
  - Only design assurance -> Type I
  - Design + operating effectiveness -> Type II
  - Not sure -> Default: Type II (most commonly requested)

Step 4: Confirm selection:
  Type I: Point in time, tests design suitability only, no Section IV
  Type II: Period of time (6-12 months), design + operating effectiveness, includes Section IV with detailed test procedures

## TSC Category Selection (SOC 2/SOC 3)

Security is ALWAYS required. Additional categories are optional:

- Availability: Include when the service organization makes commitments about uptime or availability
- Processing Integrity: Include when data processing accuracy and completeness are commitments
- Confidentiality: Include when confidential information requires specific protections
- Privacy: Include when PII is processed; maps to GDPR Articles 6-79 and AICPA GAPP

Document rationale for each included/excluded category.

## Citations in this chunk

- [AT-C-205] -- examination engagement decision
- [AT-C-320] -- SOC 1 engagement type
- [TSP-Section-100] -- TSC category selection

See SKILL.md Section 10 for the full citation manifest.
