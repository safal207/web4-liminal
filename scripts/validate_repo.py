from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "CARE-STACK-RFC.md",
    ROOT / "docs" / "ARCHITECTURE.md",
    ROOT / "spec" / "README.md",
    ROOT / "SECURITY.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / ".github" / "workflows" / "ci.yml",
    ROOT / ".github" / "workflows" / "security.yml",
]


def require_files() -> list[str]:
    errors: list[str] = []
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")
    return errors


def validate_readme() -> list[str]:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_markers = [
        "## Fast Validation Path",
        "## Repository Map",
        "## Governance",
        "## Care Stack Summary",
    ]
    for marker in required_markers:
        if marker not in readme:
            errors.append(f"README missing section: {marker}")
    return errors


def validate_local_markdown_links() -> list[str]:
    errors: list[str] = []
    markdown_files = list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md")) + list((ROOT / "spec").glob("*.md"))
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    for md in markdown_files:
        text = md.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith("http://") or target.startswith("https://") or target.startswith("#"):
                continue
            target_path = (md.parent / target).resolve()
            if not target_path.exists():
                rel = md.relative_to(ROOT)
                errors.append(f"broken local link in {rel}: {target}")
    return errors


def main() -> int:
    errors = []
    errors.extend(require_files())
    errors.extend(validate_readme())
    errors.extend(validate_local_markdown_links())

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())