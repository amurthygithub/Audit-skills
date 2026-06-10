# Limits and disclaimers — NIST CSF 2.0 skill

## What this skill IS

- A reference for the structure of NIST CSF 2.0 (6 Functions, 22 Categories, 106 Subcategories) and the Tier 1-4 organizational maturity scale
- A method for assessing an organization's current cyber posture (Current Profile) and planning toward a target posture (Target Profile)
- A crosswalk hub to other authoritative frameworks (800-53, 800-171, ISO 27001, HIPAA Security Rule, CMMC)
- An executive-legible narrative for board, audit committee, and CISO conversations
- A prioritization tool (Gap Analysis + 2x2 priority matrix) for security investment decisions

## What this skill is NOT

- **Not a certification or attestation.** CSF 2.0 has no certification path. ISO 27001 is the certifiable alternative. SOC 2 is an attestation, not a certification. The value of CSF 2.0 is the Profile, not a certificate.
- **Not a substitute for a NIST 800-53 control implementation.** CSF 2.0 is *outcome-based* (Subcategories describe what you achieve, not how); 800-53 is *control-based* (the specific controls that produce the outcome). Use CSF 2.0 for executive narrative; use 800-53 for ATO evidence and control specification.
- **Not a legal opinion.** Compliance with HIPAA Security Rule, NY DFS Part 500, GLBA Safeguards, PCI DSS 4.0, and other regulations requires legal review of the specific requirements. CSF 2.0's mappings to these frameworks are interpretive; the authoritative text is the regulation.
- **Not a substitute for professional judgment.** A CSF 2.0 Profile is a structured self-assessment, not an audit. The Tier selection, Subcategory scoring, and Gap Analysis prioritization all require practitioner judgment.
- **Not exhaustive of CSF 2.0 Quick Start Guides (QSGs).** NIST publishes 6 QSGs (one per Function) and several industry-specific QSGs. The skill references the QSG framework but does not reproduce the QSGs verbatim.
- **Not exhaustive of Community Profiles.** NIST maintains a Community Profile catalog (FFIEC, CISA CPGs, etc.). The skill references these but does not reproduce the full text.

## When to escalate to a human

Escalate when:

- The engagement requires a legal opinion on regulatory compliance
- The organization's tier selection is disputed (this requires executive judgment, not framework mechanics)
- A crosswalk mapping is the deciding factor in a contract dispute
- The organization is preparing for an actual 800-53 ATO (use `nist-800-53-rmf` instead)
- A specific Subcategory interpretation is contested by a regulator (consult NIST CSF 2.0 FAQ and the relevant QSG)

## Anti-hallucination posture

This skill follows the `docs/skill-design-template.md` §5.11 source-of-truth verification gate. Every Subcategory code, count, and mapping has been verified against:

- NIST CSF 2.0 PDF (CSWP 29, Feb 2024)
- NIST CSF 1.1 PDF (for the 1.1→2.0 delta)
- NIST CSF 2.0 Informative References spreadsheet
- NIST CSF 2.0 Quick Start Guides

The verification reports are at:

- `docs/builds/csf-2/csf-2-verification-report.md` — initial verification (8 CRITICAL + 17 HIGH caught)
- `docs/builds/csf-2/csf-2-fix-report.md` — fix log
- `docs/builds/csf-2/csf-2-reverification-report.md` — PASS-WITH-CAVEATS
- `docs/acceptance-gate.md` — the §5.11 gate

If you find a factual error, file an issue or open a PR — the skill is maintained rigorously.
