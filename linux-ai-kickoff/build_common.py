#!/usr/bin/env python3
"""Shared metadata and manuscript assembly helpers for Teach Yourself Anything."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

BOOK_DIR = Path(__file__).parent

TITLE = "Teach Yourself Anything"
SUBTITLE = "A Real-World Guide to AI, Linux, and Self-Directed Learning"
AUTHOR = "Lee Harrington"
PUBLISHER = "Leebase Press"
SLUG = "teach-yourself-anything"

COVER_PATH = BOOK_DIR / "TeachYourselfAnything.png"
MANUSCRIPT_PATH = BOOK_DIR / f"{SLUG}.md"
EPUB_PATH = BOOK_DIR / f"{SLUG}.epub"
DOCX_PATH = BOOK_DIR / f"{SLUG}.docx"
PDF_PATH = BOOK_DIR / f"{SLUG}.pdf"


@dataclass(frozen=True)
class SectionSpec:
    title: str
    markdown: str | None = None
    path: Path | None = None


SECTION_SPECS = [
    SectionSpec(title="More Than a Computer", path=BOOK_DIR / "chapters/introduction.md"),
    SectionSpec(title="Part 1: You're Not Stuck", markdown="# Part 1\n\n## You're Not Stuck"),
    SectionSpec(title="You're Not Stuck", path=BOOK_DIR / "chapters/part-1/ch-01-youre-not-stuck.md"),
    SectionSpec(
        title="What This Machine Really Gives You",
        path=BOOK_DIR / "chapters/part-1/ch-02-what-this-machine-gives-you.md",
    ),
    SectionSpec(
        title="Learning Without Permission",
        path=BOOK_DIR / "chapters/part-1/ch-03-learning-without-permission.md",
    ),
    SectionSpec(title="Part 2: Meet Your Machine", markdown="# Part 2\n\n## Meet Your Machine"),
    SectionSpec(title="Meet the Machine", path=BOOK_DIR / "chapters/part-2/ch-04-meet-the-machine.md"),
    SectionSpec(title="Move Through It", path=BOOK_DIR / "chapters/part-2/ch-05-move-through-it.md"),
    SectionSpec(
        title="The Terminal Is Not a Wall",
        path=BOOK_DIR / "chapters/part-2/ch-06-the-terminal-is-not-a-wall.md",
    ),
    SectionSpec(
        title="Read the Manual, Then Make It Yours",
        path=BOOK_DIR / "chapters/part-2/ch-07-read-the-manual-then-make-it-yours.md",
    ),
    SectionSpec(title="Part 3: Meet Your Teacher", markdown="# Part 3\n\n## Meet Your Teacher"),
    SectionSpec(
        title="AI Is Not a Vending Machine",
        path=BOOK_DIR / "chapters/part-3/ch-08-ai-is-not-a-vending-machine.md",
    ),
    SectionSpec(
        title="Pick the Right Hero",
        path=BOOK_DIR / "chapters/part-3/ch-09-pick-the-right-hero.md",
    ),
    SectionSpec(
        title="The Horse, Not the Car",
        path=BOOK_DIR / "chapters/part-3/ch-10-the-horse-not-the-car.md",
    ),
    SectionSpec(
        title="Ask, Refine, Test, Repeat",
        path=BOOK_DIR / "chapters/part-3/ch-11-ask-refine-test-repeat.md",
    ),
    SectionSpec(title="Part 4: Do Things That Matter", markdown="# Part 4\n\n## Do Things That Matter"),
    SectionSpec(
        title="Build Your Launchpad",
        path=BOOK_DIR / "chapters/part-4/ch-12-build-your-launchpad.md",
    ),
    SectionSpec(
        title="Make One Useful Tool",
        path=BOOK_DIR / "chapters/part-4/ch-13-make-one-useful-tool.md",
    ),
    SectionSpec(
        title="Fix What Breaks",
        path=BOOK_DIR / "chapters/part-4/ch-14-fix-what-breaks.md",
    ),
    SectionSpec(
        title="Ship a Small Win",
        path=BOOK_DIR / "chapters/part-4/ch-15-ship-a-small-win.md",
    ),
    SectionSpec(title="Part 5: Now You Choose", markdown="# Part 5\n\n## Now You Choose"),
    SectionSpec(
        title="Pick a Direction",
        path=BOOK_DIR / "chapters/part-5/ch-16-pick-a-direction.md",
    ),
    SectionSpec(
        title="Build Your Own Curriculum",
        path=BOOK_DIR / "chapters/part-5/ch-17-build-your-own-curriculum.md",
    ),
    SectionSpec(
        title="Keep Going Without Permission",
        path=BOOK_DIR / "chapters/part-5/ch-18-keep-going-without-permission.md",
    ),
    SectionSpec(title="You Can Keep Going", path=BOOK_DIR / "chapters/conclusion.md"),
    SectionSpec(
        title="Appendix: Translate This Book To Your Machine",
        path=BOOK_DIR / "chapters/appendices/appendix-translate-this-book-to-your-machine.md",
    ),
]


def iter_sections() -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    for spec in SECTION_SPECS:
        if spec.path is not None:
            markdown = spec.path.read_text(encoding="utf-8").strip()
        else:
            markdown = (spec.markdown or "").strip()
        sections.append((spec.title, f"{markdown}\n"))
    return sections


def assemble_manuscript() -> str:
    return "\n\n---\n\n".join(markdown.strip() for _, markdown in iter_sections()) + "\n"


def assemble_export_markdown(page_break: str = "\f") -> str:
    cover_page = (
        f"![Cover]({COVER_PATH.name})"
        "{width=80%}\n\n"
        f"# {TITLE}\n\n"
        f"## {SUBTITLE}\n\n"
        f"### {AUTHOR}\n\n"
        f"{page_break}\n"
    )
    return cover_page + "\n" + assemble_manuscript()
