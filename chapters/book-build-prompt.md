# Book Build Prompt Template

Use this prompt to produce a polished book from chapter source files. Copy, fill in the bracketed sections, and adjust as needed.

---

## The Prompt

I have [NUMBER] chapters of a book organized in my workspace folder. Here's the structure:

**Book metadata:**
- Title: [TITLE]
- Subtitle: [SUBTITLE]
- Author: [AUTHOR NAME]
- Genre/category: [e.g., technical nonfiction, programming, business]
- Target audience: [e.g., intermediate developers using AI coding tools]

**Source files are located at:**
- Part 1 (chapters 1–7): `part-1/ch-01-*.md` through `part-1/ch-07-*.md`
- Part 2 (chapters 8–14): `part-2/ch-08-*.md` through `part-2/ch-14-*.md`

**Book structure — please build these sections in order:**

1. **Half-title page** — book title only, centered, no subtitle
2. **Title page** — full title, subtitle, author
3. **Copyright page** — © [YEAR] [AUTHOR]. All rights reserved. ISBN placeholder.
4. **Dedication** — "[YOUR DEDICATION TEXT]" (or: write a brief dedication appropriate to the book's theme)
5. **Table of contents** — auto-generated with part groupings and chapter titles
6. **Introduction** — Write a 4–6 paragraph introduction that:
   - Opens with the core tension the book addresses
   - Establishes what the reader will build or learn
   - Previews the two-part structure and the methodology
   - Ends with a clear statement of who this book is for
7. **Part 1 divider page** — "Part One: [PART 1 TITLE]" with a one-line italic description
8. **Chapters 1–7** — from source files
9. **Part 2 divider page** — "Part Two: [PART 2 TITLE]" with a one-line italic description
10. **Chapters 8–14** — from source files
11. **Afterword** — Write a 4–6 paragraph afterword that ties the themes together and looks forward
12. **About the Author** — [YOUR BIO, or: write a brief placeholder bio]

**Editorial direction — elevate the prose as follows:**

- Tighten sentences: cut filler words, eliminate redundancy, prefer active voice
- Strengthen transitions between sections — each section should flow into the next
- Preserve the author's voice and tone (direct, practical, occasionally wry) — do not make it academic or flowery
- Preserve all technical accuracy: code blocks, command examples, file names, and test counts must be exact
- Convert chapter-closing italic lines into styled epigraphs
- Standardize heading hierarchy: H1 for chapter titles, H2 for major sections, H3 for subsections
- Ensure every "Watch For" and "Free Tier Note" callout is visually distinct (blockquote styling)
- Do not remove or summarize code blocks — they are instructional, not decorative
- Fix any inconsistencies in terminology across chapters (e.g., if "Antigravity" is used in early chapters but "the agent" in later ones, standardize)

**Typography and styling:**

- Body font: a serif family (Georgia/Merriweather) at comfortable reading size
- Code font: a monospace family (Source Code Pro/Courier) at ~85% body size
- Line height: 1.7–1.8 for body text, 1.5 for code blocks
- Generous margins (at least 1.5em sides)
- Code blocks: light gray background, subtle border, pre-wrap for long lines
- Blockquotes: left border accent, slightly smaller font, tinted background
- Chapter titles: page-break-before, large heading, clear hierarchy
- Part dividers: centered, uppercase, with breathing room above and below

**Output formats — produce all three:**

1. **EPUB** (`[FILENAME].epub`)
   - Use `ebooklib` with inline CSS (no external stylesheet references that won't resolve)
   - Include NCX and Nav for full e-reader compatibility
   - Spine order must match the section order above
   - TOC with nested Part > Chapter hierarchy
   - Each chapter as a separate XHTML document

2. **Word document** (`[FILENAME].docx`)
   - Use `python-docx`
   - Include a generated table of contents field (even if it needs manual refresh)
   - Apply heading styles (Heading 1, Heading 2, Heading 3) so the TOC works
   - Page breaks before each chapter and each part divider
   - Header with book title, footer with page numbers
   - Code blocks in a monospace font with light shading

3. **PDF** (`[FILENAME].pdf`)
   - Build from HTML using WeasyPrint (or the PDF skill's preferred method)
   - Proper page breaks between chapters
   - Running headers (book title left, chapter title right)
   - Page numbers centered in footer
   - Reasonable page size (A5 or trade paperback 6×9 for a book feel, or Letter/A4 if preferred)

**Process instructions:**

- Read ALL chapter files first before writing any output — you need the full picture to write a coherent introduction and afterword
- Read the relevant SKILL.md files for docx and pdf before generating those formats
- Build the EPUB first (it's the canonical version), then adapt for Word and PDF
- After building each file, verify it: check page/section count, confirm all 14 chapters are present, spot-check that code blocks rendered correctly
- Save all output files to my workspace folder

---

## Notes for Next Time

Things to adjust based on what you learn from the output:

- [ ] If code blocks look wrong in the EPUB, specify `white-space: pre-wrap` and `word-wrap: break-word` explicitly
- [ ] If the Word TOC doesn't populate, that's normal — it needs a manual refresh in Word (Ctrl+A, F9)
- [ ] If the PDF page breaks land wrong, add explicit `page-break-before: always` on H1 elements
- [ ] Add/remove front matter sections as needed (foreword, acknowledgments, glossary, index)
- [ ] If you want a cover image, provide the file path and ask for it to be embedded in the EPUB metadata
