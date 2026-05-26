#!/usr/bin/bash
# Install audit skills for opencode
set -e

SKILLS_DIR="$HOME/.config/opencode/skills/audit-category-pointer"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing audit skills to $SKILLS_DIR..."

mkdir -p "$SKILLS_DIR"
mkdir -p "$SKILLS_DIR/isaca-audit-methodology"
mkdir -p "$SKILLS_DIR/coso-internal-controls"
mkdir -p "$SKILLS_DIR/aicpa-soc-reporting"
mkdir -p "$SKILLS_DIR/audit-workpapers"

cp "$SCRIPT_DIR/skills/SKILL.md" "$SKILLS_DIR/SKILL.md"
cp "$SCRIPT_DIR/skills/isaca-audit-methodology/SKILL.md" "$SKILLS_DIR/isaca-audit-methodology/SKILL.md"
cp "$SCRIPT_DIR/skills/coso-internal-controls/SKILL.md" "$SKILLS_DIR/coso-internal-controls/SKILL.md"
cp "$SCRIPT_DIR/skills/aicpa-soc-reporting/SKILL.md" "$SKILLS_DIR/aicpa-soc-reporting/SKILL.md"
cp "$SCRIPT_DIR/skills/audit-workpapers/SKILL.md" "$SKILLS_DIR/audit-workpapers/SKILL.md"

echo "Installed 5 skill files:"
echo "  - audit-category-pointer (pointer)"
echo "  - isaca-audit-methodology"
echo "  - coso-internal-controls"
echo "  - aicpa-soc-reporting"
echo "  - audit-workpapers"
echo ""
echo "Restart opencode to activate."