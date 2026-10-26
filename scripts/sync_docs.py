"""Sync repository-maintained reference documents into the MkDocs site.

The root-level files remain the canonical copies. Run this before building the
site so the website always reflects the current mod list, changelog, and guide.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SYNCED_FILES = {
    "MODLIST.md": "mod-list-full.md",
    "CHANGELOG.md": "changelog.md",
    "PERFORMANCE_GUIDE.md": "performance.md",
    "CONTRIBUTING.md": "contributing.md",
}

REPLACEMENTS = {
    "MODLIST.md": (
        ("PERFORMANCE_GUIDE.md", "performance.md"),
        ("CHANGELOG.md", "changelog.md"),
    ),
    "CHANGELOG.md": (
        (
            "[Lunchtime Cozy Create and Cooking v1.md](Lunchtime%20Cozy%20Create%20and%20Cooking%20v1.md)",
            "[development notes](https://github.com/wtfyls/Lunchtime-Cozy-Create-Farming/blob/main/Lunchtime%20Cozy%20Create%20and%20Cooking%20v1.md)",
        ),
    ),
    "CONTRIBUTING.md": (
        ("docs/ISSUE_TRIAGE.md", "ISSUE_TRIAGE.md"),
    ),
}


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    for source_name, target_name in SYNCED_FILES.items():
        source = ROOT / source_name
        target = DOCS / target_name
        content = source.read_text(encoding="utf-8")
        for old, new in REPLACEMENTS.get(source_name, ()):
            content = content.replace(old, new)
        target.write_text(content, encoding="utf-8")
        print(f"Synced {source_name} -> docs/{target_name}")


if __name__ == "__main__":
    main()
