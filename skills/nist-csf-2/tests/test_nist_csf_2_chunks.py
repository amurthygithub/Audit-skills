"""Smoke tests for the 8 CSF 2.0 chunks.

Mirrors the audit-workpapers pattern: each chunk must exist, have
valid YAML frontmatter, and fit within the 200-line per-chunk limit.
"""

from __future__ import annotations

from pathlib import Path

import pytest

CHUNKS_DIR = Path(__file__).resolve().parent.parent / "chunks"
EXPECTED_CHUNKS = [
    "01-functions-categories.md",
    "02-tiers-and-profiles.md",
    "03-current-profile.md",
    "04-target-profile-and-gap.md",
    "05-govern-function.md",
    "06-enterprise-reporting.md",
    "07-implementation-playbook.md",
    "08-informative-references-crosswalk.md",
]


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_file_exists(filename):
    path = CHUNKS_DIR / filename
    assert path.exists(), f"Expected chunk at {path}"


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_under_line_limit(filename):
    path = CHUNKS_DIR / filename
    if not path.exists():
        pytest.skip(f"{filename} not yet shipped")
    line_count = len(path.read_text().splitlines())
    assert line_count <= 200, f"{filename} is {line_count} lines (> 200 limit)"


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_has_yaml_frontmatter(filename):
    path = CHUNKS_DIR / filename
    if not path.exists():
        pytest.skip(f"{filename} not yet shipped")
    text = path.read_text()
    assert text.startswith("---\n"), f"{filename} must start with YAML frontmatter"
    assert "\n---\n" in text or text.endswith("\n---\n"), f"{filename} must terminate frontmatter"


@pytest.mark.parametrize("filename", EXPECTED_CHUNKS)
def test_chunk_id_matches_filename(filename):
    path = CHUNKS_DIR / filename
    if not path.exists():
        pytest.skip(f"{filename} not yet shipped")
    text = path.read_text()
    expected_id = filename.replace(".md", "")
    assert f"chunk_id: {expected_id}" in text, (
        f"{filename} must declare chunk_id: {expected_id}"
    )
