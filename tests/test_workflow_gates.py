"""Tests for the G0-G6 pipeline gate checkers (SOX-632).

Covers tools/check_fact_sheet.py (G1) and tools/check_design_doc.py (G2),
plus consistency between AGENTS.md and the prompts/ directory.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

import check_design_doc  # noqa: E402
import check_fact_sheet  # noqa: E402

VALID_FACT_SHEET = """\
# Fact-Sheet — test-skill

## 0. Machine-readable data block (REQUIRED)

```yaml
fact_sheet:
  skill_slug: test-skill
  framework: Test Framework 1.0
  version: "1.0"
  version_date: "2025-01-01"
  supersedes: null
  retrieval_date: "2026-06-09"
  researcher: test-agent
counts:
  functions: 6
  categories: 22
identifiers:
  - code: GV.OC-01
    name: Organizational Context
    parent: GV.OC
urls:
  - label: TEST-1.0
    url: https://example.gov/test-framework
    status: 200
    checked: "2026-06-09"
crosswalks:
  - from: GV.OC-01
    to_framework: NIST SP 800-53
    to: [PM-11]
    source: IR spreadsheet, row 1
terminology:
  - term: Tier 1
    source_wording: Partial
sign_off: true
```

## 1. Primary sources
## 2. Structural inventory
## 3. Crosswalk mappings
## 4. URL verification
## 5. Terminology
## 6. Version and supersession
## 7. Scope boundaries
## 8. Sign-off
"""


def _write(tmp_path, text):
    p = tmp_path / "fact-sheet.md"
    p.write_text(text, encoding="utf-8")
    return p


class TestCheckFactSheet:
    def test_valid_fact_sheet_passes(self, tmp_path):
        code, msgs = check_fact_sheet.check_fact_sheet(_write(tmp_path, VALID_FACT_SHEET))
        assert code == 0, msgs

    def test_template_itself_fails(self):
        code, msgs = check_fact_sheet.check_fact_sheet(REPO / "docs" / "fact-sheet-template.md")
        assert code == 1
        assert any("placeholder" in m for m in msgs)
        assert any("sign_off" in m for m in msgs)

    def test_missing_sign_off_fails(self, tmp_path):
        text = VALID_FACT_SHEET.replace("sign_off: true", "sign_off: false")
        code, msgs = check_fact_sheet.check_fact_sheet(_write(tmp_path, text))
        assert code == 1
        assert any("sign_off" in m for m in msgs)

    def test_non_200_url_fails(self, tmp_path):
        text = VALID_FACT_SHEET.replace("status: 200", "status: 404")
        code, msgs = check_fact_sheet.check_fact_sheet(_write(tmp_path, text))
        assert code == 1
        assert any("status must be 200" in m for m in msgs)

    def test_non_integer_count_fails(self, tmp_path):
        text = VALID_FACT_SHEET.replace("functions: 6", "functions: six")
        code, msgs = check_fact_sheet.check_fact_sheet(_write(tmp_path, text))
        assert code == 1
        assert any("must be an integer" in m for m in msgs)

    def test_missing_section_fails(self, tmp_path):
        text = VALID_FACT_SHEET.replace("## 6. Version and supersession\n", "")
        code, msgs = check_fact_sheet.check_fact_sheet(_write(tmp_path, text))
        assert code == 1
        assert any("'## 6.'" in m for m in msgs)

    def test_missing_yaml_block_fails(self, tmp_path):
        text = re.sub(r"```yaml\n.*?\n```", "", VALID_FACT_SHEET, flags=re.DOTALL)
        code, msgs = check_fact_sheet.check_fact_sheet(_write(tmp_path, text))
        assert code == 1
        assert any("yaml data block" in m for m in msgs)

    def test_empty_crosswalks_warns_but_passes(self, tmp_path):
        text = re.sub(
            r"crosswalks:\n(  - .*\n|    .*\n)+", "crosswalks: []\n", VALID_FACT_SHEET
        )
        code, msgs = check_fact_sheet.check_fact_sheet(_write(tmp_path, text))
        assert code == 0, msgs
        assert any(m.startswith("WARN") and "crosswalks" in m for m in msgs)


class TestCheckDesignDoc:
    def test_filled_example_design_doc_passes(self):
        code, msgs = check_design_doc.check_design_doc(REPO / "docs" / "csf-2-design.md")
        assert code == 0, msgs

    def test_template_itself_fails(self):
        code, msgs = check_design_doc.check_design_doc(
            REPO / "docs" / "skill-design-template.md"
        )
        assert code == 1
        assert any("template's own title" in m for m in msgs)

    def test_missing_numbered_section_fails(self, tmp_path):
        template = (REPO / "docs" / "skill-design-template.md").read_text(encoding="utf-8")
        doc = template.replace("# Skill Design Template", "# test-skill — Design")
        doc = re.sub(r"^## 11\..*$", "## removed", doc, flags=re.MULTILINE)
        p = tmp_path / "design.md"
        p.write_text(doc, encoding="utf-8")
        code, msgs = check_design_doc.check_design_doc(p)
        assert code == 1
        assert any("'## 11.'" in m for m in msgs)

    def test_short_doc_fails(self, tmp_path):
        p = tmp_path / "design.md"
        p.write_text("# test-skill — Design\n## 0. Why\n", encoding="utf-8")
        code, msgs = check_design_doc.check_design_doc(p)
        assert code == 1
        assert any("lines" in m for m in msgs)


class TestPromptsConsistency:
    """AGENTS.md and prompts/README.md must reference only prompt files that exist."""

    def test_all_prompt_files_referenced_in_agents_md_exist(self):
        agents = (REPO / "AGENTS.md").read_text(encoding="utf-8")
        for name in re.findall(r"prompts/([a-z0-9-]+\.md)", agents):
            assert (REPO / "prompts" / name).is_file(), f"AGENTS.md references missing prompts/{name}"

    def test_prompts_readme_lists_every_prompt_file(self):
        readme = (REPO / "prompts" / "README.md").read_text(encoding="utf-8")
        on_disk = {p.name for p in (REPO / "prompts").glob("*.md")} - {"README.md"}
        listed = set(re.findall(r"\[([a-z0-9-]+\.md)\]", readme))
        assert on_disk == listed, f"prompts/README.md out of sync: disk={on_disk}, listed={listed}"

    def test_prompt_files_have_placeholder_contract(self):
        for p in (REPO / "prompts").glob("*.md"):
            if p.name in ("README.md",):
                continue
            text = p.read_text(encoding="utf-8")
            assert "{{skill_slug}}" in text, f"{p.name} missing the {{{{skill_slug}}}} placeholder"
