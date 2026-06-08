# AGENTS.md — Runtime instructions for every agent in Audit-skills

This file is pre-loaded by every agent working on this repo. It is the single source of truth for how to work here.

---

## 0. Before you do anything

### 0.1 Read `docs/lessons-learned.md`
That file captures every mistake we have made across 3 build waves and 3 rounds of verification. Read it before starting any task. The short version:
- **Never trust your own recall for factual claims.** Verify against live sources via `webfetch`.
- **Counts are always wrong by ±2.** Verify every count against the source document.
- **Every manifest URL must be live-checked.** URL rot is the #1 silent failure mode.
- **Build agents produce plausible-sounding fabricated identifiers.** The §5.11 verification gate is the only guardrail.

### 0.2 Know the repo structure
- `skills/<slug>/SKILL.md` — router, ≤300 lines, frontmatter + all 12 sections
- `skills/<slug>/chunks/NN-slug.md` — content chunks, ≤200 lines each
- `skills/<slug>/industries/` — 3-4 industry view files + `_index.md`
- `skills/<slug>/use-cases/` — 3-4 use cases + `_index.md`
- `skills/<slug>/tests/` — 9 test files + `nist_csf_2_stub.py` (or `<slug>_stub.py`)
- `skills/<slug>/data/` — generators, seeds, crosswalks
- `skills/<slug>/docs/` — architecture, limits, changelog, acceptance-gate
- `skills/<slug>/telemetry/` — schema, instrument, redaction, baseline
- `tools/lint_skill.py` — Tier 0a linter
- `tests/test_consistency_lib.py` — cross-document consistency checks
- `docs/lessons-learned.md` — mandatory pre-read
- `docs/skill-design-template.md` — design doc template
- `docs/fact-sheet-template.md` — pre-build research template

---

## 1. When building a new skill

### 1.1 Day 0: Research first
Before writing a single line of content:
1. Read the fact-sheet template at `docs/fact-sheet-template.md`
2. Dispatch a research agent with `webfetch` access to the authoritative sources
3. The research agent populates a fact-sheet (`docs/<slug>-fact-sheet.md`) with:
   - Every identifier (Categories, Subcategories, controls, etc.)
   - Every count (function count, category count, subcategory count, control count)
   - Every crosswalk mapping row
   - Every manifest URL (verified live, returns 200)
   - Version information (what's current, what was superseded)
   - Terminology (exact wording from the source document)
4. **Do not proceed to Day 1 until the fact-sheet is complete.**

### 1.2 Day 1-4: Build from the fact-sheet
1. Build agents reference ONLY the fact-sheet for factual claims — never their own recall
2. The fact-sheet is the single source of truth
3. If the fact-sheet is missing a fact needed by a build agent, the fact-sheet is incomplete — go back to Day 0

### 1.3 Day 5: Verify against the fact-sheet
1. A verification agent compares every factual claim in the built files against the fact-sheet
2. Any mismatch is a CRITICAL finding
3. Fix all CRITICALs before proceeding

### 1.4 The build contract
For every new skill, the minimum:
- Design doc (`docs/<slug>-design.md`) — follows `docs/skill-design-template.md`
- Fact-sheet (`docs/<slug>-fact-sheet.md`) — follows `docs/fact-sheet-template.md`, research agent populated
- File requirements spec (`docs/<slug>-file-requirements.md`) — exact file list
- Build: 1 router agent + N chunk agents in parallel (from fact-sheet, not recall)
- 5-lens review: 5 agents in parallel
- §5.11 verification: 1 agent comparing built files to fact-sheet
- Fix pass: 1 agent per skill
- Re-verify pass
- At least 30 tests per skill
- All linters PASS
- All `test_consistency_lib.py` tests PASS

---

## 2. When editing an existing skill

### 2.1 Minimum checklist
1. Read the files being edited AND their siblings that may be affected
2. Verify any changed facts against live sources via `webfetch`
3. Run: `python3 tools/lint_skill.py skills/<skill>`
4. Run: `python3 -m pytest skills/<skill>/tests/ tests/test_consistency_lib.py -q -p no:asyncio`
5. Run: `python3 -m pytest skills/ tests/ -q -p no:asyncio` (full suite)
6. Verify `git diff` shows changes in the repo path (`/Users/amurthy/Code/Audit-skills`), NOT in `~/.config/opencode/skills/`
7. Commit with a conventional commit message

---

## 3. Commit message format

```
type(skill-slug): description
```

Types: `feat` (new content), `fix` (correction), `docs` (non-content docs), `chore` (tooling/CI)

Examples:
- `feat(iso-27001): scaffold SKILL.md and 7 chunks`
- `fix(nist-800-53-rmf): replace fabricated Rev 5.1.1 with Rev 5`
- `docs: add fact-sheet template for Day 0 research phase`

Never use: `Merge`, `WIP`, `stuff`, mixed-case scopes, periods at end of subject.

---

## 4. Test commands

```bash
# Per-skill linter
python3 tools/lint_skill.py skills/<slug>

# Per-skill tests
python3 -m pytest skills/<slug>/tests/ tests/test_consistency_lib.py -q -p no:asyncio

# Full test suite
python3 -m pytest skills/ tests/ -q -p no:asyncio

# All linters
python3 tools/lint_skill.py skills/nist-800-53-rmf skills/isaca-audit-methodology \
  skills/coso-internal-controls skills/aicpa-soc-reporting \
  skills/audit-workpapers skills/nist-csf-2
```

---

## 5. Common mistakes (do NOT do these)

### 5.1 Fabricating identifiers
Bad: writing `GV.SR`, `GV.MT`, `PR.AC` from recall.
Good: copying identifiers from the Day 0 fact-sheet (populated from live sources).

### 5.2 Wrong counts
Bad: "108 Subcategories" (CSF 1.1), "81 Points of Focus" (wrong).
Good: verify every count against the fact-sheet.

### 5.3 Writing to config path
Bad: agent writes to `~/.config/opencode/skills/<skill>/` instead of the repo.
Prevention: always `git diff` after agent completion. If diff is empty but agent says it edited files, the files went to the wrong path.

### 5.4 Not running tests before declaring done
Bad: "All done, 266/266 pass" without actually running `pytest`.
Good: run `python3 -m pytest skills/ tests/ -q -p no:asyncio` and paste the output.

### 5.5 Creating stub telemetry/instrument.py without full API surface
Bad: `nist-csf-2/telemetry/instrument.py` exports only `emit` and `timed`.
Good: every `telemetry/instrument.py` must export `instrumented`, `SkillInvocation`, `skill_invocation` to prevent module shadowing in CI.

### 5.6 Committing without conventional commit format
Bad: `"fixed some stuff in nist"`
Good: `"fix(nist-800-53-rmf): correct ATO duration from 3yr to 1yr"`

### 5.7 Not re-verifying after a fix pass
Bad: fix agent applies corrections, no follow-up verification.
Good: after every fix pass, dispatch a re-verification agent. Fix agents introduce new errors.

---

## 6. Dispatch patterns

### 6.1 Build agents
- Parallel for independent tasks (one per chunk, one per industry file)
- Single router agent for SKILL.md (must know full architecture)
- Build agents read from the fact-sheet, NOT from their own recall

### 6.2 Review agents
- 5-lens review: 5 agents in parallel, one per lens
- §5.11 verification: 1 agent per skill, webfetch access required
- All review agents receive explicit checklists

### 6.3 Fix agents
- 1 agent per skill, dispatched in parallel
- Each receives EXACT findings with line numbers and expected values
- Instructed: "Do NOT commit or push"
- After completion: verify `git diff` is in repo path

---

## 7. When in doubt

- Read `docs/lessons-learned.md`
- Run the linter and full test suite
- Verify against live sources via webfetch
- Ask before assuming

