# Limits & Disclaimers — nist-800-53-rmf

## 1. What this skill is NOT

- **Not a substitute for professional judgment.** Always have a qualified ISSO, ISSM, AO, or 3PAO review outputs.
- **Not legal advice.** FISMA, FedRAMP, and OMB memos are interpreted by agencies, the FedRAMP PMO, and (in disputes) the courts. This skill encodes a reasonable reading, not the only one.
- **Not a certification.** Using the skill does not confer CISA, CISSP, or any other credential.
- **Not an ATO.** The skill helps produce the artifacts (categorization, baseline, tailoring, SAR, POA&M, ATO letter). The **AO signs the ATO**; the skill does not.

## 2. Reconstructed numbering

| Section | Reconstructed? | Authoritative source | Verify against |
|---------|----------------|----------------------|----------------|
| §3.1 control families (20 + privacy) | No | NIST SP 800-53 Rev 5 / 5.1.1 | csrc.nist.gov |
| §3.2 baseline counts (156 / 325 / 421 for Rev 5; 161 / 341 / 437 for 5.1.1) | Yes — derived counts | NIST SP 800-53 / FedRAMP Rev 5 baseline | csrc.nist.gov, fedramp.gov |
| §4.4 finding severity → POA&M risk | No (typical pattern) | FedRAMP Continuous Monitoring Strategy Guide | fedramp.gov |
| §7 cross-references to other standards | Curated; verify | AICPA, ISO, PCI SSC, HHS, NIST | respective publishers |

The baseline control counts are **derived from the catalog and the count of base controls + enhancements**. The actual count varies depending on how one counts enhancements (and which version — 5.0 vs 5.1.1). **Always verify against the current NIST SP 800-53 Rev 5 / 5.1.1 publication and the FedRAMP baseline** for cloud services.

## 3. Regulatory currency

| Standard | Version cited | Publication date | Verify at |
|----------|---------------|------------------|-----------|
| NIST SP 800-53 | Rev 5 (Sept 2020) + 5.1.1 (2024) | 2020 / 2024 | csrc.nist.gov |
| NIST SP 800-37 | Rev 2 (Dec 2018) | 2018 | csrc.nist.gov |
| NIST SP 800-53A | Rev 5 (Jan 2022) | 2022 | csrc.nist.gov |
| FIPS 199 | (Feb 2004) | 2004 | nvlpubs.nist.gov |
| FIPS 200 | (Mar 2006) | 2006 | nvlpubs.nist.gov |
| FedRAMP | Rev 5 (and 5.1.1 overlays) | 2023 / 2024 | fedramp.gov |
| OMB A-130 | (July 28, 2016) | 2016 | whitehouse.gov |
| OMB M-22-15 | (2022) | 2022 | whitehouse.gov |
| AICPA TSC | 2017 (TSP §100, 2022 revised points of focus) | 2017 / 2022 | aicpa-cima.com |
| ISO 27001 | 2022 | 2022 | iso.org |
| PCI DSS | v4.0 (Mar 2022) | 2022 | pcisecuritystandards.org |
| HIPAA Security Rule | 45 CFR 164.302–164.318 | as amended | hhs.gov |
| NIST SP 800-66 | Rev 2 (Feb 2024) | 2024 | csrc.nist.gov |
| NIST CSF | 2.0 (Feb 2024) | 2024 | nist.gov/cyberframework |
| CMMC | 2.0 | as published | dodcio.defense.gov |

## 4. Known gaps

- **Rev 5 vs 5.1.1 selection** — the user/program may require 5.0, 5.1.1, or both. The skill frontmatter lists both; the user must confirm which baseline is in scope.
- **FedRAMP overlays** — FedRAMP's High baseline is not identical to NIST 800-53 High; FedRAMP adds a number of controls. The skill does not enumerate FedRAMP-specific additions; consult the current FedRAMP Baselines document on fedramp.gov.
- **DoD-specific overlays** — DoD Cloud Computing (DoD CC SRG) imposes IL4/IL5/IL6 levels that layer on top of FedRAMP. The skill does not enumerate these.
- **800-53A objective enumeration** — the assessment objectives are in 800-53A Rev 5; the enumeration varies by control and is not the same as the enhancement enumeration.
- **Categorization judgment** — the skill encodes the framework; the categorization call is professional judgment.

## 5. Out-of-scope inputs

- **Penetration testing results** — use a security testing skill.
- **Legal interpretations** — consult counsel.
- **Personal tax advice** — not applicable.
- **FedRAMP marketplace publication** — requires FedRAMP PMO engagement; the skill produces the package, not the marketplace listing.

## 6. When to refuse

The skill should be used cautiously or not at all when:

- The user asks for a categorical answer without the system context (e.g., "what's our FIPS 199 categorization?" without describing the system).
- The user provides contradictory information (e.g., claims MODERATE but lists HIGH-impact information types).
- The user's request would require hallucinating a specific 800-53 control that does not exist in the catalog.
- The user requests a FedRAMP authorization package without an actual system to authorize.

## 7. Privacy

This skill is **risk: high** in the frontmatter. It encodes the controls but does not certify compliance. The skill's outputs may contain PII, system names, or sensitive data; redact before sharing outside the engagement.

> This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source (current NIST SP 800-53 Rev 5 / 5.1.1, FIPS 199, SP 800-37 Rev 2, SP 800-53A Rev 5, OMB A-130, FedRAMP Rev 5 guidance, and the agency's policy).
