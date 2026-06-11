# Fact-Sheet Template — Pre-Build Research (Day 0)

> **Use this for every new skill BEFORE any build agent writes a single line.**
> Status: required template (added 2026-06-08 after the CSF 2.0 build taught us that build agents fabricate identifiers).
> Output: save as `docs/<skill-slug>-fact-sheet.md`.
> Researcher: an agent with `webfetch` access to the authoritative sources.

## Why this template exists

When we shipped NIST CSF 2.0 (June 2026), 9 parallel build agents wrote plausible-looking content from LLM recall. A subsequent §5.11 verification pass found 8 CRITICAL factual errors: fabricated Category codes (`GV.SR`, `GV.MT` that don't exist), wrong subcategory counts (108 vs 106), ~10 wrong crosswalk rows, and 1.1 codes cited as 2.0 codes.

The 5-lens review would NOT have caught these — it checks structure and conventions, not factual accuracy against live sources. The lesson: **research must happen BEFORE the build, not after.** This fact-sheet is the single source of truth for every build agent. No build agent writes from recall.

---

## How to use this template

1. **A research agent** (with `webfetch` access) populates every section.
2. **Every claim must cite a specific source** (URL + line number where the fact was found).
3. **Every URL in the URL table must be live-verified** (returns 200, not 404/410/30x).
4. **Every count must be verified by reading the source document**, not by trusting LLM recall.
5. **Every crosswalk mapping row must come from an authoritative reference spreadsheet/database**.
6. **The §0 machine-readable data block mirrors the prose tables** — it is what the G3 build tests assert against.
7. **Do not proceed to build (Day 1) until `python3 tools/check_fact_sheet.py docs/<slug>-fact-sheet.md` passes.**

---

## 0. Machine-readable data block (REQUIRED — the G1 gate parses this)

Mirror the prose tables below into this YAML block. Counts, identifiers, URLs, and crosswalks here are the **single machine-checkable source of truth**: `tools/check_fact_sheet.py` validates this block (the G1 gate), and the skill's G3 tests assert that every count and identifier in the built chunks matches it. If the prose tables and this block disagree, the block wins — fix the prose.

```yaml
fact_sheet:
  skill_slug: <slug>                  # must match skills/<slug>/
  framework: <framework full name>
  version: "<version>"
  version_date: "<YYYY-MM-DD>"
  supersedes: "<previous version, or null>"
  retrieval_date: "<YYYY-MM-DD>"
  researcher: <agent or person>
counts:                               # every count a chunk may state
  <level_name>: <N>                   # e.g. functions: 6, categories: 22, subcategories: 106
identifiers:                          # every code a build agent may reference (mirrors §2.2)
  - code: <GV.OC-01>
    name: <Organizational Context>
    parent: <GV.OC>
urls:                                 # every manifest citation (mirrors §4)
  - label: <NIST-CSF-2.0>
    url: <https://doi.org/10.6028/NIST.CSWP.29>
    status: 200                       # must be 200 at retrieval; anything else fails the gate
    checked: "<YYYY-MM-DD>"
crosswalks:                           # every crosswalk row the skill will encode (mirrors §3)
  - from: <GV.OC-01>
    to_framework: <NIST SP 800-53>
    to: [<PM-11>]
    source: <IR spreadsheet, row N>
terminology:                          # exact source wording (mirrors §5)
  - term: <Tier 1>
    source_wording: <Partial>
sign_off: false                       # flip to true ONLY when the §8 checklist is fully complete
```

---

## 0.5 Licensed-source workflow (only when the framework text is licence-restricted)

If the normative text is licensed (ISO, COSO): build everything machine-verifiable from free
sources; for requirement-semantics claims add `verification: pending_human_verification` plus
a clause pointer to the row/section, generate the worksheet per
`prompts/human-verification-worksheet.md`, and record the acquisition in
`source-texts/manifest.json`. The gate refuses `sign_off: true` while any pending rows
remain. Verified rows carry `verification: human-licensed-copy (<copy>, <date>)` and NO
verbatim quote (§5.11 check 15a — the one exception to the quote rule).

## 1. Primary sources

| # | Source | URL | Version/Edition | Retrieval date | Verifier |
|---|--------|-----|-----------------|----------------|----------|
| 1 | The standard itself (PDF) | `<URL>` | `<version>` | `<date>` | `<agent name>` |
| 2 | Informative references / crosswalk (spreadsheet/database) | `<URL>` | `<version>` | `<date>` | `<agent name>` |
| 3 | FAQ / quick start guides | `<URL>` | `<current>` | `<date>` | `<agent name>` |
| 4 | ... | ... | ... | ... | ... |

---

## 2. Structural inventory

### 2.1 Top-level breakdown

| Level | Name | Count | Source | Verified? |
|-------|------|-------|--------|-----------|
| Functions | `<list>` | `<N>` | `<URL>, §X.Y` | ✓ |
| Categories | `<list or count>` | `<N>` | `<URL>, §X.Y` | ✓ |
| Subcategories | `<count>` | `<N>` | `<URL>, Appendix A` | ✓ |
| Controls | `<count>` | `<N>` | `<URL>, control catalog` | ✓ |

### 2.2 Detailed breakdown (table of every identifier)

For every code/identifier the skill will encode, list it with its:
- **Code** (e.g., `GV.OC-01`)
- **Name** (e.g., "Organizational Context")
- **Parent** (e.g., `GV.OC` / GOVERN → Organizational Context)
- **Source** (where in the source document this code appears)

| Code | Name | Parent | Source | Verified? |
|------|------|--------|--------|-----------|
| `<GV.OC-01>` | `<full name>` | `<GV.OC>` | `<URL>, p.X` | ✓ |
| ... | ... | ... | ... | ... |

**Rule:** if the build agents reference it, it must be in this table. If it's not in this table, it doesn't exist.

---

## 3. Crosswalk mappings

### 3.1 Framework-to-framework mappings

For each mapping the skill will encode:

| From (this skill's framework) | To (target framework) | To code(s) | Strength | Source | Verified? |
|-------------------------------|-----------------------|------------|----------|--------|-----------|
| `<GV.OC-01>` | `<NIST SP 800-53>` | `<PM-11>` | `<1-to-1>` | `<IR spreadsheet, row N>` | ✓ |
| `<RS.MA-01>` | `<NIST SP 800-53>` | `<IR-6, IR-7, IR-8, SR-3, SR-8>` | `<1-to-many>` | `<IR spreadsheet, row M>` | ✓ |
| ... | ... | ... | ... | ... | ... |

**Rule:** every crosswalk row in the skill must appear in this table. If it's not in this table, it's fabricated.

---

## 4. URL verification — every manifest citation

Every URL the skill's §10 manifest will cite must be live-checked:

| Label | URL | HTTP status | Source page title | Verified? |
|-------|-----|-------------|-------------------|-----------|
| `<NIST-CSF-2.0>` | `<https://doi.org/10.6028/NIST.CSWP.29>` | `<200>` | `<Cybersecurity Framework>` | ✓ |
| `<ISACA-ITAF>` | `<https://www.isaca.org/resources/it-audit-assurance-standards>` | `<200>` | `<IT Audit and Assurance Standards>` | ✓ |
| ... | ... | ... | ... | ... |

**Rule:** if a URL returns 404/410/30x, find the correct URL and update it in this table. The build agent will copy URLs from this table, NOT from recall.

---

## 5. Terminology — exact wording from the source

Framework-specific terms the skill will use. The build agent must use the EXACT wording from the source document:

| Term | Source wording (verbatim) | Source | Notes (if any) |
|------|--------------------------|--------|----------------|
| `<Tier 1>` | `<"Partial">` | `<CSF 2.0 §3.1>` | Not "Initial" |
| `<Tier 4>` | `<"Adaptive">` | `<CSF 2.0 §3.1>` | Not "Advanced" |
| `<Current Profile>` | `<"Current Profile">` | `<CSF 2.0 §3.2>` | Not "Baseline Profile" |
| `<Target Profile>` | `<"Target Profile">` | `<CSF 2.0 §3.2>` | Not "Desired Profile" |
| ... | ... | ... | ... |

**Rule:** if the build agent uses a different term than the source document, it's a factual error. Copy-paste from this table.

---

## 6. Version and supersession

| Claim | Source | Verified? |
|-------|--------|-----------|
| Current version of the standard | `<URL>, cover page` | ✓ |
| Previous version (superseded) | `<URL>, cover page or FAQ>` | ✓ |
| Date of current version | `<URL>, cover page>` | ✓ |
| What changed from previous version | `<URL>, changelog or FAQ>` | ✓ |

**Rule:** if the skill references a version, that version must be in this table. If the table shows a newer version than the skill references, the skill must be updated.

---

## 7. Scope boundaries — what the skill does NOT cover

| Domain | In scope? | Reason (if out of scope) |
|--------|-----------|------------------------|
| `<Healthcare>` | `<No>` | `<Deferred to v0.3.x; covered by HIPAA skill>` |
| `<CMMC L3>` | `<No>` | `<Only CMMC L2 self-assessment covered in v0.1.0>` |
| ... | ... | ... |

**Rule:** explicit scope boundaries prevent scope creep and help build agents know where to stop.

---

## 8. Sign-off — Day 0 research complete

- [ ] Every structural identifier is in §2.2
- [ ] Every count is verified against the source document (§2.1)
- [ ] Every crosswalk row is sourced from an authoritative reference (§3)
- [ ] Every manifest URL returns 200 (§4)
- [ ] Terminology is copy-paste from the source (§5)
- [ ] Version and supersession are confirmed (§6)
- [ ] Scope boundaries are explicit (§7)
- [ ] §0 data block mirrors all of the above; `sign_off: true` set
- [ ] `python3 tools/check_fact_sheet.py docs/<slug>-fact-sheet.md` passes

**After sign-off:** this fact-sheet is the single source of truth for all Day 1-5 build agents. No build agent writes from recall.

---

— End of fact-sheet template —
