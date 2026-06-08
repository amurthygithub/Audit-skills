# Lessons Learned: Building, Reviewing, and Editing Audit-Skills

This document captures what we learned across 3 build waves (nist-800-53-rmf, nist-csf-2, 5-skill retrofits) and 3+ rounds of §5.11 verification. It is a permanent instruction set for future agents.

---

## 1. The hard problem is factual correctness, not structure

The Tier 0a linter catches mechanical issues (line counts, missing frontmatter, folder structure). The consistency library catches cross-document drift (routing tables, manifest labels, cross-skill references). The 5-lens review catches conventions and usability. **None of these catch factual errors.**

Factual correctness requires an agent that:
- Has access to live web sources (webfetch)
- Reads the actual NIST/ISACA/COSO/AICPA/PCAOB publications
- Checks every claim against the source-of-truth document
- Flags discrepancies with line numbers and the correct value

### Pattern: build → verify → fix

| Phase | What it catches | Duration |
|-------|----------------|----------|
| Build (1 agent) | Write all files per spec | ~5 min |
| 5-lens review (5 agents) | Structure, conventions, usability, completeness, cross-skill | ~10 min |
| §5.11 verification (1-6 agents) | Factual errors against live sources | ~15 min |
| Fix (1-5 agents) | Apply corrections from §5.11 findings | ~10 min |
| Re-verify (1 agent) | Confirm fixes, find residuals | ~5 min |

## 2. How many review cycles?

| Skill maturity | Typical cycles | Example |
|---------------|---------------|---------|
| Brand new skill (no precedent) | 3-4 | nist-csf-2: 2 rounds (8 CRITICAL fixed, 6 follow-ups) |
| Existing skill, new review lens | 2 | Original 5 skills: 3 rounds across multiple sweeps |
| Minor edit (URL fix, count fix) | 1 | SOX-627-631: one round each |
| **Recommended minimum** | **2** (5-lens + §5.11 verification) | |

**Two cycles is the minimum viable process.** One round of 5-lens review catches the structural/convention errors. One round of §5.11 source-of-truth verification catches the factual errors. The third and fourth rounds are cleanup — residuals the first fix pass missed.

## 3. Common failure modes (by severity)

### 3.1 Fabricated identifiers and versions

LLMs without source access will invent plausible-sounding identifiers:
- `GV.SR`, `GV.MT` — Category codes that don't exist in NIST CSF 2.0
- `Rev 5.1.1` — Version number NIST never published
- `PR.AC` — CSF 1.1 code cited as CSF 2.0

**Prevention:** Every framework identifier must be checked against the live authoritative source. The §5.11 verification gate is non-negotiable.

### 3.2 Wrong counts

LLMs consistently get counts wrong by ±1-2:
- "108 Subcategories" when actual is 106
- "8 ID.AM subcategories" when actual is 7
- "9 DE.CM subcategories" when actual is 5
- "5 COBIT design factors" when actual is 11
- "6 CC6 sub-criteria" when actual is 8
- "81 Points of Focus" when actual is 71

**Prevention:** Every count in every chunk must be verified against the source document. If an agent writes a count, it must also cite where in the source document that count is published.

### 3.3 URL rot

Framework publishers restructure their websites. The most common broken URLs:
- AICPA: `/resources/` → `/topic/audit-assurance` (entire path restructured)
- COSO: `/guidance-*` → individual pages (Fraud, Monitoring, ICSR, RPA, etc.)
- ISACA: `/resources/itaf` → `/resources/it-audit-assurance-standards`
- NIST: SP 800-60, SP 800-61 revision-specific URLs change when new revisions publish
- FedRAMP: `/resources/` paths restructured

**Prevention:** The nightly link-rot checker (`tools/check_link_rot.py`) catches these, but it only runs daily. Every §5.11 verification pass must include live URL checking for every manifest citation. The skill's docs/acceptance-gate.md must have a URL verification row.

### 3.4 Self-contradiction

When two chunks disagree about the same fact:
- "SSAE 18 governs SOC reports" vs "SSAE 21 supersedes SSAE 18"
- "33 Common Criteria" vs body listing 35

**Prevention:** The consistency library catches some of these (manifest bi-directional, routing bi-directional). For content-level contradictions, the §5.11 verification must check cross-chunk consistency on every fact that appears in more than one place.

### 3.5 Version confusion

When a standard has multiple versions and the source document is ambiguous:
- AT-C 105/205 vs 100/200/300 (AICPA renumbered)
- SSAE 18 vs SSAE 21 (which is current?)
- NIST SP 800-61 Rev 2 vs Rev 3 (Rev 2 was withdrawn Apr 2025)
- ITAF 4th vs 5th edition
- CSF 1.1 codes mixed with CSF 2.0 codes

**Prevention:** Every version reference in the skill must include a retrieval date. The §5.11 verification must check whether the claimed version is still the current published version. If a newer version exists, the verification must flag it.

### 3.6 Cross-reference drift

When one skill references another, and the referenced skill changes:
- Chunk path renames (nist-800-53-rmf/chunks/04-assess → 05-assess)
- Chunk numbering shifts (duplicate chunk numbers in different skills)
- Skill-internal references to chunks that don't exist (chunk 01 referenced in routing table when only chunks 02-09 exist)

**Prevention:** The consistency library (`tests/test_consistency_lib.py`) catches these. Run it after every set of changes. If adding a chunk, update the routing table and run the consistency tests.

### 3.7 Module shadowing in CI

When `conftest.py` adds skill directories to `sys.path` in alphabetical order, and a skill's `telemetry/instrument.py` has a different API surface than another skill's, the earlier (alphabetically) skill's module shadows the later one.

**Fix:** Every `telemetry/instrument.py` must export the full API surface (`instrumented`, `SkillInvocation`, `skill_invocation`). The `nist-csf-2` case taught us this — it alphabetically precedes `nist-800-53-rmf`.

### 3.8 Agent file location errors

Agents directed to edit files in a repo often write to `~/.config/opencode/skills/` instead of the repo path. This happened in 3 out of 5 repair sub-agents.

**Prevention:** Verify file diffs are in the repo path (not config path) before committing. Always `git diff` after agent completion.

---

## 4. The §5.11 verification gate (mandatory process)

### 4.1 What it is
A non-negotiable step in the build sequence (codified in `docs/skill-design-template.md §5.11`) where every factual claim in the skill is verified against live authoritative sources via webfetch.

### 4.2 What to check

| Category | Check | Tool |
|----------|-------|------|
| Framework IDs | Every Category/Subcategory/control code exists in the real spec | webfetch |
| Counts | Subcategory counts, control counts, criteria counts match the source | webfetch + manual count |
| Version | Claimed version is the current published version | webfetch |
| URLs | Every manifest URL returns 200 (not 404/410) | webfetch or `check_link_rot.py` |
| Crosswalks | Mapping rows match the authoritative cross-reference document | webfetch + spreadsheet comparison |
| Terminology | Framework-specific terms match the source document's exact wording | webfetch |
| Cross-skill refs | References to other skills resolve to real files/paths | consistency lib |
| Counts in multiple places | Same fact stated in chunk A and chunk B are identical | grep |

### 4.3 Output
A `docs/acceptance-gate.md` file with a table: fact | source | retrieval date | verifier | status. Minimum 20 rows for a new skill. Any FAIL blocks release. Any WARN requires a documented caveat.

### 4.4 Anti-patterns
- **Skip verification because "the build agent just did it."** The build agent worked from LLM recall. It WILL have made up identifiers.
- **Assume the 5-lens review covers factual accuracy.** It doesn't. The 5 lenses are structure, completeness, usability, conventions, cross-skill alignment. Factual accuracy is §5.11 only.
- **Fix findings without re-verifying.** The fix agent will introduce new errors. Always do a re-verification pass after the fix pass.
- **Accept "probably correct" for counts.** Every count must be verified by reading the source document, not by trusting the agent's recall.

---

## 5. Agent dispatch patterns

### 5.1 Build phase
- Parallel agents work when tasks are independent (one agent per chunk, one agent per industry file)
- A single router agent writes SKILL.md (it must know the full architecture)
- Build agents should NOT be given webfetch access — they'll still hallucinate. Building is for structure; verification is for facts.

### 5.2 Review phase
- 5-lens review: 5 agents in parallel, one per lens, each reviewing ALL skills
- Each lens has a clear checklist. No overlap between lenses.
- §5.11 verification: 1 agent per skill, or 6 agents in parallel for the full library

### 5.3 Fix phase
- 1 agent per skill, dispatched in parallel
- Each agent receives the EXACT findings (with line numbers and expected values)
- Agents MUST be told: "Do NOT commit or push"
- After all agents complete: verify git diff is in the repo path (not config path)

---

## 6. Technical guardrails

### 6.1 Pre-commit / CI: what they catch
| Check | Catches | Doesn't catch |
|-------|---------|---------------|
| Tier 0a linter | Missing frontmatter, line counts, TODOs, folder structure, citations | Factual errors, URL liveness, version correctness |
| pytest | Test failures, import errors, oracle mismatches | Factual errors in content |
| Consistency lib | Routing drift, manifest drift, cross-skill broken refs, industry/UC index sync | Content quality, framework accuracy |
| Link rot checker (nightly) | 404/410 URLs | Runs nightly, not pre-commit |
| PR title convention | Malformed PR titles | N/A |
| None of the above | | **Framework factual accuracy** |

### 6.2 The gap
**§5.11 verification is the only guardrail that catches framework factual errors.** It is manual (agent-mediated) and must be run as part of every build, every major edit, and every cross-walk.

---

## 7. For future skill builds

### 7.1 Minimum build contract
For any new skill (e.g., ISO 27001, PCI DSS, HIPAA, GDPR):

1. **Design doc** (`docs/<skill>-design.md`): what, why, architecture, 5-lens pre-review questions, file inventory
2. **File requirements spec** (`docs/<skill>-file-requirements.md`): exact file list, frontmatter fields, chunk topics, UC shapes, data schemas
3. **Build**: 1 router agent + N chunk agents in parallel
4. **5-lens review**: 5 agents, all findings documented
5. **§5.11 verification**: 1+ agent with webfetch, checking every factual claim against live sources
6. **Fix**: 1 agent per skill, apply all findings
7. **Re-verify**: 1 agent, confirm fixes, find residuals
8. **Test**: 266+ tests pass, all linters PASS
9. **PR**: squash-merge with conventional commit

### 7.2 Minimum edit contract
For edits to existing skills:

1. **Read** the files being edited (and siblings that may be affected)
2. **Verify** any changed facts against live sources (webfetch)
3. **Run** `python3 tools/lint_skill.py skills/<skill>`
4. **Run** `python3 -m pytest skills/<skill>/tests/ tests/test_consistency_lib.py -q -p no:asyncio`
5. **Check** git diff is in repo path, not config path
6. **Commit** with conventional commit message

---

## 8. Numbers that matter

| Metric | Value |
|--------|-------|
| On-Spine skills | 6 |
| Total tests | 266 |
| Tests per skill | 29-49 |
| Review lenses | 5 (accuracy, completeness, usability, conventions, cross-skill) |
| §5.11 verification cycles needed (new skill) | 2 minimum, 3-4 typical |
| Common fabricated count error | ±2 |
| URL rot frequency | ~30% of manifest URLs break within 2 years |
| Module shadow risk | Alphabetically-first skill must export full API |
| Agent config-path vs repo-path error rate | ~60% (3/5 agents) |

---

## 9. Summary for future agents

> **If you remember nothing else:**
>
> 1. **Never trust a build agent's factual claims.** Verify everything against live sources via webfetch.
> 2. **The 5-lens review catches structure, not facts.** §5.11 is the only factual gate.
> 3. **Two review cycles minimum.** One for structure, one for facts. Three or four for a clean release.
> 4. **Every manifest URL must be live-checked.** URL rot is the #1 silent failure mode.
> 5. **Counts are always wrong by ±2.** Verify every count against the source document.
> 6. **Commit messages use `type(skill-slug): description` convention.** No exceptions.
> 7. **Always run linter + pytest + consistency lib before committing.** Every time.
> 8. **Verify file paths after agent completion.** Agents write to config path ~60% of the time.
