# Audit Skills for AI Agents

Production-grade ISACA/COSO/AICPA/PCAOB audit agent skills for [opencode](https://opencode.ai) and compatible AI agent frameworks.

## What's Included

| Skill | Framework | Lines | Description |
|-------|-----------|-------|-------------|
| **isaca-audit-methodology** | ISACA/COBIT 2019 | ~1,660 | IT audit planning, COBIT assessments, ITGC/ITAC testing, CISA domain coverage, Risk IT, sampling |
| **coso-internal-controls** | COSO 2013/2017, SOX 404, AS 2201 | ~1,880 | ICFR assessment, SOX 404 compliance, deficiency classification, walkthroughs, ERM integration |
| **aicpa-soc-reporting** | AICPA SOC 1/2/3, TSP Section 100 | ~1,580 | SOC examination planning, TSC criteria mapping, opinion formulation, trust services reporting |
| **coso-internal-controls** | PCAOB AS standards, GAAS | ~1,970 | Workpaper documentation, audit evidence, sampling procedures, risk model calculations |

## Features

- **Executable decision logic** — deficiency classification, audit approach selection, and compensating control evaluation encoded as IF/THEN/ELSE pseudocode
- **Copy-paste templates** — risk registers, RcM, walkthrough docs, SOC reports, finding write-ups, sampling workpapers
- **Cross-framework mapping** — COSO↔TSC↔COBIT↔NIST↔ISO cross-reference tables with verified alignments
- **Anti-hallucination safeguards** — explicit disclaimers on reconstructed numbering, verification prompts for standard citations
- **Regulatory currency** — AS 2201 (post-reorganization), COBIT 2019, TSP Section 100 (2022 revised), ISO 27001:2022, NIST 800-53 Rev 5

## Quick Start

### Install with opencode

```bash
# Clone this repo
git clone https://github.com/amurthygithub/Audit-skills.git

# Copy skills to your opencode config
cp -r Audit-skills/skills/* ~/.config/opencode/skills/audit-category-pointer/

# Or use the install script
./install.sh
```

### Manual Installation

Place the `skills/` directory contents under `~/.config/opencode/skills/audit-category-pointer/` so opencode discovers them:

```
~/.config/opencode/skills/
  audit-category-pointer/
    SKILL.md                          # Category pointer
    isaca-audit-methodology/SKILL.md
    coso-internal-controls/SKILL.md
    aicpa-soc-reporting/SKILL.md
    audit-workpapers/SKILL.md
```

### Using with Other AI Frameworks

These skills are structured Markdown files with YAML frontmatter. They work as:
- **System prompts** — paste the SKILL.md content into your agent's system prompt
- **RAG context** — index and retrieve relevant sections at query time
- **Prompt chains** — use the category pointer to route to the correct skill

## Examples

See the [`examples/`](examples/) directory for complete worked scenarios:

| Example | Skill | Scenario |
|---------|-------|----------|
| ISACA IT Audit Plan | isaca-audit-methodology | Planning a COBIT-based IT audit for a SaaS company |
| SOX ICFR Assessment | coso-internal-controls | Full SOX 404 walkthrough with deficiency classification |
| SOC 2 Type II Exam | aicpa-soc-reporting | Planning and executing a SOC 2 Type II examination |
| Audit Sampling Workpaper | audit-workpapers | MUS and attribute sampling with complete calculations |

## Cross-Skill Alignment

All four skills use consistent:
- **5-part finding format**: Condition-Criteria-Cause-Effect-Recommendation (C-C-C-E-R)
- **Deficiency severity mapping**: ISACA Critical/High/Medium/Low ↔ PCAOB Material Weakness/Significant Deficiency/Deficiency
- **Audit risk model**: ISACA 3-factor (AR = IR × CR × DR) with cross-reference to PCAOB sampling-level decompositions
- **TSC↔COSO mapping**: Verified against AICPA TSP Section 100 (CC2→P13-15, CC3→P6-9, CC4→P16-17, CC5→P10-12)

## Quality

Each skill was reviewed through 3 cycles by independent review agents:
- Cycle 1: Structure, completeness, and initial accuracy
- Cycle 2: Factual verification, cross-skill alignment, regulatory currency
- Cycle 3: Final production readiness, math verification, cross-reference integrity

### Known Limitations

- **ITAF numbering** (ISACA skill §5): The S1-S18 / G1-G35 numbering is a pedagogical reconstruction, not official ISACA ITAF numbering. Always verify against current ITAF publication before citing.
- **Points of Focus** (COSO skill §2): 71 of 81 COSO 2013 Points of Focus are enumerated; consult the COSO publication for the complete set.
- **TSP criteria count** (AICPA skill §7): 51 primary criteria are definitive; the "~64 with sub-criteria" count varies by publication (61-67); verify against current TSP Section 100.

## License

MIT — see [LICENSE](LICENSE).

## Contributing

Contributions welcome — especially:
- Additional worked examples
- Corrections to standard references
- Translations to other languages
- Integration guides for other AI frameworks

## Disclaimer

These skills are AI agent prompt instructions, not professional audit advice. They are designed to assist qualified audit professionals by providing structured frameworks and decision logic. Always exercise professional judgment and verify outputs against current professional standards and regulatory requirements.