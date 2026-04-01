#!/usr/bin/env python3
"""Shared metadata and manuscript assembly helpers for the personal empowerment book."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

BOOK_DIR = Path(__file__).parent

TITLE = "The Personal Empowerment with AI Handbook"
SUBTITLE = "How to Use AI as a Thinking Partner to Become More Capable, Creative, and Self-Directed"
AUTHOR = "Lee Harrington"
PUBLISHER = "Leebase Press"
SLUG = "personal-empowerment-with-ai-handbook"

COVER_PATH = BOOK_DIR / "PersonalEmpowermentCover.png"
MANUSCRIPT_PATH = BOOK_DIR / f"{SLUG}.md"
DOCX_PATH = BOOK_DIR / f"{SLUG}.docx"
EPUB_PATH = BOOK_DIR / f"{SLUG}.epub"
PDF_PATH = BOOK_DIR / f"{SLUG}.pdf"
EPUB_CSS_PATH = BOOK_DIR / "epub-styles.css"


@dataclass(frozen=True)
class SectionSpec:
    title: str
    markdown: str | None = None
    path: Path | None = None


SECTION_SPECS = [
    SectionSpec(title="Introduction", path=BOOK_DIR / "chapters/introduction-this-is-not-about-going-faster.md"),
    SectionSpec(title="Part I", markdown="# Part I — Reframe the Relationship"),
    SectionSpec(title="Chapter 1", path=BOOK_DIR / "chapters/chapter-1-you-are-the-executive.md"),
    SectionSpec(title="Chapter 2", path=BOOK_DIR / "chapters/chapter-2-think-in-stereo.md"),
    SectionSpec(title="Chapter 3", path=BOOK_DIR / "chapters/chapter-3-forge-dont-factory.md"),
    SectionSpec(title="Chapter 4", path=BOOK_DIR / "chapters/chapter-4-expand-dont-replace.md"),
    SectionSpec(title="Part II", markdown="# Part II — Use AI Across a Real Human Life"),
    SectionSpec(title="Chapter 5", path=BOOK_DIR / "chapters/chapter-5-turn-curiosity-into-output.md"),
    SectionSpec(title="Chapter 6", path=BOOK_DIR / "chapters/chapter-6-think-better-about-work-and-learning.md"),
    SectionSpec(title="Chapter 7", path=BOOK_DIR / "chapters/chapter-7-use-ai-for-reflection-parenting-and-decisions.md"),
    SectionSpec(title="Chapter 8", path=BOOK_DIR / "chapters/chapter-8-explore-meaning-belief-identity-without-losing-yourself.md"),
    SectionSpec(title="Part III", markdown="# Part III — Stay Human While Using Powerful Tools"),
    SectionSpec(title="Chapter 9", path=BOOK_DIR / "chapters/chapter-9-real-insight-real-surprise.md"),
    SectionSpec(title="Chapter 10", path=BOOK_DIR / "chapters/chapter-10-the-risks-of-getting-weaker-with-better-tools.md"),
    SectionSpec(title="Part IV", markdown="# Part IV — Build a Personal Empowerment Practice"),
    SectionSpec(title="Chapter 11", path=BOOK_DIR / "chapters/chapter-11-build-your-personal-empowerment-practice.md"),
    SectionSpec(title="Conclusion", path=BOOK_DIR / "chapters/conclusion-become-more-of-yourself.md"),
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
    return "\n\n".join(markdown.strip() for _, markdown in iter_sections()) + "\n"


def assemble_markdown_book() -> str:
    front = [
        f"![Cover]({COVER_PATH.name})",
        "",
        f"# {TITLE}",
        "",
        f"## {SUBTITLE}",
        "",
        f"### {AUTHOR}",
        "",
        "---",
        "",
    ]
    return "\n".join(front) + assemble_manuscript()


def assemble_export_markdown(page_break: str = "\f") -> str:
    front = [
        f"![Cover]({COVER_PATH.name})" + "{width=80%}",
        "",
        f"# {TITLE}",
        "",
        f"## {SUBTITLE}",
        "",
        f"### {AUTHOR}",
        "",
        page_break,
        "",
    ]
    return "\n".join(front) + assemble_manuscript()
