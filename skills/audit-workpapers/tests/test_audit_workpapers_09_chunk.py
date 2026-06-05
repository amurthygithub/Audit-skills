"""Smoke test for chunk 09-substantive-analytical-procedures.

Verifies:
- File exists with expected frontmatter
- chunk_id matches the filename slug
- load_when trigger text matches what the SKILL.md routing table advertises
- File fits within the per-chunk line limit (200 lines)
"""

from __future__ import annotations

from pathlib import Path

import yaml

CHUNK = Path(__file__).resolve().parent.parent / "chunks" / "09-substantive-analytical-procedures.md"


def test_chunk_file_exists():
    assert CHUNK.exists(), f"Expected chunk file at {CHUNK}"


def test_chunk_frontmatter():
    text = CHUNK.read_text()
    assert text.startswith("---\n"), "Chunk must start with YAML frontmatter"
    end = text.find("\n---\n", 4)
    assert end > 0, "Chunk must terminate frontmatter with ---"
    fm = yaml.safe_load(text[4:end])
    assert fm["chunk_id"] == "09-substantive-analytical-procedures", (
        f"chunk_id mismatch: {fm['chunk_id']!r}"
    )
    assert fm["parent_skill"] == "audit-workpapers", (
        f"parent_skill mismatch: {fm['parent_skill']!r}"
    )
    assert "topic" in fm and fm["topic"]
    assert "load_when" in fm and fm["load_when"]


def test_chunk_under_line_limit():
    line_count = len(CHUNK.read_text().splitlines())
    assert line_count <= 200, f"Chunk is {line_count} lines (> 200 limit)"


def test_chunk_referenced_in_skill_md():
    skill_md = (Path(__file__).resolve().parent.parent / "SKILL.md").read_text()
    assert "09-substantive-analytical-procedures" in skill_md, (
        "New chunk must be referenced in SKILL.md (routing table, "
        "decision logic, and output templates)"
    )
    assert "Substantive Analytical Procedures" in skill_md
