# Contributing to Audit-skills

Thanks! Open a PR using [the template](.github/pull_request_template.md). Run `python tools/lint_skill.py skills/nist-800-53-rmf skills/isaca-audit-methodology skills/coso-internal-controls skills/aicpa-soc-reporting skills/audit-workpapers` and `pytest skills/ tests/ -q` locally before pushing - paste the output into the PR. For new skills or schema changes, open an issue first. Questions: am@amurthy.ai.

## Adding a new skill

Before writing any code, copy [`docs/skill-design-template.md`](docs/skill-design-template.md) to `docs/<your-skill-slug>-design.md` and fill in all 15 sections. A design doc that doesn't hit all 15 sections is incomplete; the Monday review will bounce it back. The template is a checklist, not a guide — read [`docs/csf-2-design.md`](docs/csf-2-design.md) for a fully-filled example (1,391 lines) and use [`skills/nist-800-53-rmf/`](skills/nist-800-53-rmf/) as the load-bearing reference architecture.

Once the design is approved, scaffold the skill by copying `skills/TEMPLATE/` and renaming.
