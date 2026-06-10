#!/usr/bin/env bash
# Install audit skills for opencode.
#
# Skills are auto-discovered from skills/*/SKILL.md (TEMPLATE excluded), so this
# script can never go stale when a new skill ships. Each skill is installed as a
# full package (router, chunks, industries, use-cases, data, docs, telemetry) —
# not just the SKILL.md router. tests/ and __pycache__/ are excluded.
#
# Override the install location with AUDIT_SKILLS_INSTALL_DIR (used by
# tests/test_install_coverage.py).
set -euo pipefail

SKILLS_DIR="${AUDIT_SKILLS_INSTALL_DIR:-$HOME/.config/opencode/skills/audit-category-pointer}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing audit skills to $SKILLS_DIR..."

mkdir -p "$SKILLS_DIR"
cp "$SCRIPT_DIR/skills/SKILL.md" "$SKILLS_DIR/SKILL.md"

installed=0
for skill_md in "$SCRIPT_DIR"/skills/*/SKILL.md; do
  skill_dir="$(dirname "$skill_md")"
  name="$(basename "$skill_dir")"
  [ "$name" = "TEMPLATE" ] && continue

  mkdir -p "$SKILLS_DIR/$name"
  (cd "$skill_dir" && tar -cf - --exclude='./tests' --exclude='__pycache__' .) \
    | (cd "$SKILLS_DIR/$name" && tar -xf -)
  echo "  - $name (full package)"
  installed=$((installed + 1))
done

echo ""
echo "Installed $installed skills + the audit-category-pointer router."
echo "Restart opencode to activate."
