#!/usr/bin/env python3
"""Build PDF for Your Dev Environment: A Guide for AI-Assisted Developers."""

from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    Image,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    PageBreak,
)

BOOK_DIR = Path(__file__).parent
MD_PATH = BOOK_DIR / "your-dev-environment.md"
COVER_PATH = BOOK_DIR / "DevEnvCover.png"
OUT_PATH = BOOK_DIR / "your-dev-environment.pdf"

TITLE = "Your Dev Environment"
SUBTITLE = "A Guide for AI-Assisted Developers"
AUTHOR = "Lee Harrington"

PAGE_SIZE = (6 * inch, 9 * inch)
MARGIN = 0.7 * inch


def build_styles():
    styles = getSampleStyleSheet()
    styles["BodyText"].fontName = "Times-Roman"
    styles["BodyText"].fontSize = 11
    styles["BodyText"].leading = 15

    styles["Heading1"].fontName = "Helvetica-Bold"
    styles["Heading1"].fontSize = 18
    styles["Heading1"].leading = 22
    styles["Heading1"].spaceBefore = 18
    styles["Heading1"].spaceAfter = 10

    styles["Heading2"].fontName = "Helvetica-Bold"
    styles["Heading2"].fontSize = 14
    styles["Heading2"].leading = 18
    styles["Heading2"].spaceBefore = 14
    styles["Heading2"].spaceAfter = 8

    styles["Heading3"].fontName = "Helvetica-Bold"
    styles["Heading3"].fontSize = 12
    styles["Heading3"].leading = 15
    styles["Heading3"].spaceBefore = 10
    styles["Heading3"].spaceAfter = 6

    styles.add(
        ParagraphStyle(
            name="TitlePage",
            parent=styles["Heading1"],
            alignment=TA_CENTER,
            fontSize=24,
            leading=28,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Subtitle",
            parent=styles["BodyText"],
            alignment=TA_CENTER,
            fontName="Helvetica-Oblique",
            fontSize=13,
            textColor=colors.HexColor("#555555"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Author",
            parent=styles["BodyText"],
            alignment=TA_CENTER,
            fontName="Helvetica",
            fontSize=15,
            textColor=colors.HexColor("#2E4057"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Callout",
            parent=styles["BodyText"],
            leftIndent=18,
            borderPadding=6,
            borderColor=colors.HexColor("#2E4057"),
            borderWidth=1,
            borderLeft=True,
            backColor=colors.HexColor("#F0F4F8"),
            spaceBefore=4,
            spaceAfter=4,
        )
    )
    return styles


def inline_html(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    return text


def render_story(md_text: str, styles):
    story = []
    story.append(Image(str(COVER_PATH), width=5.2 * inch, height=6.93 * inch))
    story.append(PageBreak())
    story.append(Spacer(1, 1.5 * inch))
    story.append(Paragraph(TITLE, styles["TitlePage"]))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(SUBTITLE, styles["Subtitle"]))
    story.append(Spacer(1, 0.4 * inch))
    story.append(Paragraph(AUTHOR, styles["Author"]))
    story.append(PageBreak())

    lines = md_text.splitlines()
    in_code = False
    code_lines = []
    callout_lines = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            story.append(
                Preformatted(
                    "\n".join(code_lines),
                    ParagraphStyle(
                        "CodeBlock",
                        fontName="Courier",
                        fontSize=8.5,
                        leading=10,
                        leftIndent=16,
                        rightIndent=16,
                        backColor=colors.HexColor("#F5F5F5"),
                        borderColor=colors.HexColor("#DDDDDD"),
                        borderWidth=1,
                        borderPadding=6,
                    ),
                )
            )
            story.append(Spacer(1, 0.08 * inch))
            code_lines = []

    def flush_callout():
        nonlocal callout_lines
        if callout_lines:
            for raw in callout_lines:
                story.append(Paragraph(inline_html(re.sub(r"^>\s*", "", raw)), styles["Callout"]))
            story.append(Spacer(1, 0.08 * inch))
            callout_lines = []

    for line in lines:
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_callout()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if line.startswith(">"):
            callout_lines.append(line)
            continue
        if callout_lines:
            flush_callout()

        stripped = line.strip()
        if not stripped:
            continue
        if stripped == "---":
            story.append(Spacer(1, 0.12 * inch))
            continue
        if stripped.startswith("# "):
            story.append(Paragraph(inline_html(stripped[2:]), styles["Heading1"]))
            continue
        if stripped.startswith("## "):
            story.append(Paragraph(inline_html(stripped[3:]), styles["Heading2"]))
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(inline_html(stripped[4:]), styles["Heading3"]))
            continue
        if re.match(r"^\d+\. ", stripped):
            body = re.sub(r"^\d+\. ", "", stripped)
            story.append(Paragraph(f"&#8226; {inline_html(body)}", styles["BodyText"]))
            continue
        if stripped.startswith("- "):
            story.append(Paragraph(f"&#8226; {inline_html(stripped[2:])}", styles["BodyText"]))
            continue
        if stripped.startswith("|"):
            continue
        story.append(Paragraph(inline_html(stripped), styles["BodyText"]))

    if callout_lines:
        flush_callout()
    if code_lines:
        flush_code()

    return story


def main() -> None:
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUT_PATH),
        pagesize=PAGE_SIZE,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title=f"{TITLE}: {SUBTITLE}",
        author=AUTHOR,
    )
    story = render_story(MD_PATH.read_text(encoding="utf-8"), styles)
    doc.build(story)
    size = OUT_PATH.stat().st_size
    print(f"Written: {OUT_PATH} ({size // 1024}KB)")


if __name__ == "__main__":
    main()
