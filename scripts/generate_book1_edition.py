#!/usr/bin/env python3
"""Generate Book 1 harness-specific editions from the canonical chapter source."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "chapters"
PROFILES_DIR = ROOT / "edition-profiles"

BOOK_ORDER = [
    "introduction.md",
    "part-1/ch-01-plan-before-you-prompt.md",
    "part-1/ch-02-define-requirements.md",
    "part-1/ch-03-test-ai-output.md",
    "part-1/ch-04-review-like-a-pr.md",
    "part-1/ch-05-iterate-deliberately.md",
    "part-1/ch-06-manage-scope.md",
    "part-1/ch-07-document-decisions.md",
    "part-2/ch-08-the-agentflow-loop.md",
    "part-2/ch-09-skills-and-autonomy-modes.md",
    "part-2/ch-10-context-files-and-handoffs.md",
    "part-2/ch-10b-resilience-and-tool-switching.md",
    "part-2/ch-11-multi-agent-coordination.md",
    "part-2/ch-12-the-sprint-cadence.md",
    "part-2/ch-13-autonomy-at-scale.md",
    "part-2/ch-14-putting-it-all-together.md",
    "conclusion.md",
]


def load_profile(name: str) -> dict:
    profile_path = PROFILES_DIR / f"{name}.json"
    with profile_path.open() as fh:
        return json.load(fh)


def apply_replacements(text: str, replacements: list[dict]) -> str:
    for item in replacements:
        pattern = item["pattern"]
        repl = item["replacement"]
        flags = re.MULTILINE
        if item.get("dotall"):
            flags |= re.DOTALL
        text = re.sub(pattern, repl, text, flags=flags)
    return text


def combine_manuscript(target_dir: Path, profile: dict) -> None:
    manuscript_parts = [
        f"<!-- Generated from the canonical Book 1 source using the `{profile['profile_name']}` harness profile. -->",
        "",
    ]

    for rel_path in BOOK_ORDER:
        chapter_path = target_dir / "chapters" / rel_path
        manuscript_parts.append(chapter_path.read_text())
        manuscript_parts.append("")

    (target_dir / profile["combined_filename"]).write_text("\n".join(manuscript_parts).strip() + "\n")


def write_readme(target_dir: Path, profile: dict) -> None:
    lines = [
        f"# {profile['book_title']}",
        "",
        f"This directory contains a generated Book 1 edition for the `{profile['profile_name']}` harness.",
        "",
        "## What Changes",
        "",
        "- Conceptual content stays aligned with the canonical `chapters/` source.",
        f"- Harness-specific instructions are adapted for {profile['tool_name']}.",
        "- The combined manuscript is regenerated from the edition chapter files, not edited separately.",
        "",
        "## Regenerate",
        "",
        f"```bash\npython3 scripts/generate_book1_edition.py {profile['profile_name']}\n```",
        "",
    ]

    if profile.get("notes"):
        lines.extend(["## Notes", ""])
        lines.extend([f"- {note}" for note in profile["notes"]])
        lines.append("")

    (target_dir / "README.md").write_text("\n".join(lines))


def generate(profile_name: str) -> None:
    profile = load_profile(profile_name)
    target_dir = ROOT / profile["output_dir"]
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True)

    shutil.copytree(SOURCE_DIR, target_dir / "chapters")

    # Remove canonical publication artifacts so the edition directory stays source-first.
    for stale in (target_dir / "chapters").glob("AgentFlow.*"):
        if stale.is_file():
            stale.unlink()
    for stale in (target_dir / "chapters").rglob(".DS_Store"):
        if stale.is_file():
            stale.unlink()

    for path in sorted((target_dir / "chapters").rglob("*")):
        if not path.is_file() or path.suffix.lower() != ".md":
            continue
        rel = path.relative_to(target_dir / "chapters").as_posix()
        text = path.read_text()
        text = apply_replacements(text, profile.get("global_replacements", []))
        text = apply_replacements(text, profile.get("file_replacements", {}).get(rel, []))
        path.write_text(text)

    combine_manuscript(target_dir, profile)
    write_readme(target_dir, profile)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("profile", help="Edition profile name, e.g. claude-code")
    args = parser.parse_args()
    generate(args.profile)


if __name__ == "__main__":
    main()
