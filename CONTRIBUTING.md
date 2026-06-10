# Contributing to Audit-skills

Thanks! Open a PR using [the template](.github/pull_request_template.md). Run `python tools/lint_skill.py skills/nist-800-53-rmf skills/isaca-audit-methodology skills/coso-internal-controls skills/aicpa-soc-reporting skills/audit-workpapers skills/nist-csf-2` and `pytest skills/ tests/ -q` locally before pushing - paste the output into the PR. For new skills or schema changes, open an issue first. Questions: am@amurthy.ai.

All work follows the G0-G6 stage-gated pipeline in [AGENTS.md](AGENTS.md) — every gate is a checkable artifact.

## Adding a new skill

1. **Research first (G1).** Copy [`docs/fact-sheet-template.md`](docs/fact-sheet-template.md) to `docs/<your-skill-slug>-fact-sheet.md` and populate it from live authoritative sources — every identifier, count, URL (live-checked), crosswalk row, and term. Gate: `python tools/check_fact_sheet.py docs/<slug>-fact-sheet.md` must pass. No content is written from recall; the fact-sheet is the single source of truth.
2. **Design (G2).** Copy [`docs/skill-design-template.md`](docs/skill-design-template.md) to `docs/<your-skill-slug>-design.md` and fill in all sections. Gate: `python tools/check_design_doc.py docs/<slug>-design.md` must pass. Read [`docs/builds/csf-2/csf-2-design.md`](docs/builds/csf-2/csf-2-design.md) for a fully-filled example (1,391 lines) and use [`skills/nist-800-53-rmf/`](skills/nist-800-53-rmf/) as the load-bearing reference architecture.
3. **Build (G3).** Scaffold by copying `skills/TEMPLATE/` and renaming. All factual claims come from the fact-sheet.
4. **Verify (G4).** Run the review passes in [`prompts/`](prompts/) — 5-lens review, §5.11 source-of-truth verification, fix, re-verify, persona vetting, and the consumer smoke test. A new skill ships with `docs/acceptance-gate.md` (≥20 verified rows) and `docs/persona-review.md`.
