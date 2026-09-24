"""Validate the portable ai-engineer skill without third-party dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ai-engineer"
MANIFEST = SKILL / "SKILL.md"


def main() -> int:
    errors: list[str] = []
    text = MANIFEST.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        errors.append("SKILL.md must begin with YAML frontmatter")
    else:
        header = parts[1]
        if not re.search(r"(?m)^name: ai-engineer$", header):
            errors.append("frontmatter name must be ai-engineer")
        if not re.search(r"(?m)^description: .+", header):
            errors.append("frontmatter description is required")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds the 500-line progressive disclosure limit")
    if not (SKILL / "agents" / "openai.yaml").is_file():
        errors.append("missing agents/openai.yaml")
    links = re.findall(r"\[[^\]]+\]\((references/[^)]+\.md)\)", text)
    for link in links:
        if not (SKILL / link).is_file():
            errors.append(f"missing linked reference: {link}")
    references = set((SKILL / "references").glob("*.md"))
    unlinked = references - {SKILL / link for link in links}
    for path in sorted(unlinked):
        errors.append(f"unlinked reference: {path.name}")
    for path in references:
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty reference: {path.name}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"OK: ai-engineer skill, {len(references)} linked references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
