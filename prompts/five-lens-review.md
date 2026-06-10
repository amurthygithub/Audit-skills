# 5-lens review — G4 pass 1

Dispatch **5 agents in parallel, one per lens**. Each agent receives this file with `{{skill_slug}}` filled and its `{{lens}}` assigned. Lenses do not overlap — stay in your lane; another agent owns the other lenses.

> **You are reviewing `skills/{{skill_slug}}/` through the {{lens}} lens only.**
> Read every file in the skill folder. Report findings as a table:
> `severity | file:line | finding | expected`
> Severities: CRITICAL / HIGH / MEDIUM / LOW (see prompts/README.md).
> Do NOT fix anything. Do NOT commit. Report only.

## Lens 1 — Framework fidelity (structure-level, not facts)
- Does the skill's structure mirror the framework's structure (functions/domains/criteria in the source's order and grouping)?
- Are framework terms used consistently across SKILL.md, chunks, industries, UCs (same term, same casing, same ID format)?
- Is the framework's own navigation logic (e.g. categorize → select → implement → assess) reflected in the decision logic?
- NOTE: factual accuracy of IDs/counts/URLs is NOT this lens — that is §5.11 verification.

## Lens 2 — Completeness
- Every section the SKILL.md frontmatter and §11 routing table promise actually exists.
- Every chunk listed in the routing table exists; every chunk that exists is in the routing table.
- Industries `_index.md` lists every industry file; UC `_index.md` lists every UC.
- Every UC has: input, procedure, expected output, oracle. No TODO/TBD/placeholder text anywhere.
- All 9 test files present; data/generators referenced by UCs exist.

## Lens 3 — Usability
- Can a practitioner find the right chunk from SKILL.md alone in under a minute? Is the routing table's "when to read" column decision-grade?
- Are output templates copy-paste usable (no abstract placeholders without an example)?
- Is the README quickstart real: install → first useful output in <10 minutes?
- Does each UC read as a worked example a stranger could replay, not a summary?

## Lens 4 — Spine convention compliance
- SKILL.md ≤300 lines; chunks ≤200 lines; frontmatter fields complete per `tools/lint_skill.py`.
- File naming: `chunks/NN-slug.md`, `uc-NN-slug.md`, industry slugs match `_index.md`.
- §10 manifest format, §11 routing format, citation format match `skills/TEMPLATE/`.
- telemetry/instrument.py exports `instrumented`, `SkillInvocation`, `skill_invocation`.

## Lens 5 — Cross-skill alignment
- Every reference to another skill resolves to a real file/path in this repo.
- Shared concepts (e.g. the audit risk model, deficiency ladder) state the same thing this skill's siblings state — list any contradiction with both file:line locations.
- Crosswalk references point at the owning skill's crosswalk data, not a duplicate.
- Routing tables of sibling skills that reference this skill still resolve.
