# Architecture: Teach Yourself Anything

> Structural decisions for the book manuscript. This file turns the strategic
> roadmap in `project-plan.md` into a concrete production architecture.

---

## 2026-03-25 - Export Pipeline Locked

### Decision

Use a **local manuscript assembly + format-specific export pipeline** inside
`linux-ai-kickoff/`:

- `build-manuscript.py` assembles the full book into `teach-yourself-anything.md`
- `build-epub.py` builds `teach-yourself-anything.epub` with the cover embedded
- `build-docx.py` builds `teach-yourself-anything.docx` with the cover embedded
- `build-pdf.py` builds `teach-yourself-anything.pdf` with a real first-page
  cover via a PDF-specific raw LaTeX title block

### Rationale

- This book did not yet have a single assembled manuscript file or a local
  publication pipeline.
- The older `ai-env-book` builders depended on Python libraries that are not
  available in this environment.
- `pandoc` and `xelatex` are available locally, so a pandoc-based exporter is
  the most reliable no-new-dependencies option.
- PDF needs a slightly different path than DOCX and EPUB so the cover is not
  lost behind generated title matter.

### Alternatives Rejected

- Reusing the older Python builders directly: blocked by missing local Python
  packages.
- Installing new Python dependencies: unnecessary and outside the project's
  default guardrails.
- Shipping only the assembled markdown: not enough once the user asked for
  renamed publication-ready outputs.

### Consequences

- `linux-ai-kickoff/` now has its own self-contained build/export layer.
- Future export tweaks should be made in the local build scripts, not in
  `ai-env-book/`.
- PDF export should keep its explicit cover-page handling unless a better
  environment-stable option replaces it.

---

## 2026-03-22 - Book Architecture Locked

### Decision

Use a **19-file manuscript structure**:

- 1 introduction
- 17 core chapters
- 1 conclusion

Organize the body into five parts:

- Part 1: 3 chapters
- Part 2: 4 chapters
- Part 3: 4 chapters
- Part 4: 4 chapters
- Part 5: 3 chapters

### Rationale

- This is long enough to build a real transformation instead of a long essay.
- It gives Part 2 and Part 3 enough space to teach Linux and AI without making
  either one the real subject.
- It gives Part 4 enough room for a practical mission thread with visible wins.
- It keeps Part 5 focused on direction and self-authorship instead of turning
  into a baggy career appendix.

### Alternatives Rejected

- A shorter 12-14 chapter structure: cleaner, but too compressed for both the
  machine, AI usage, and the practical mission thread.
- A larger 22+ chapter structure: would risk turning the book into a reference
  work instead of a motivating path.

### Consequences

- Every chapter must earn its place with a visible reader outcome.
- The book must stay disciplined about what not to explain.

---

## Manuscript Map

### Introduction

| File | Working Title | Purpose | Visible Outcome |
|------|---------------|---------|-----------------|
| `chapters/introduction.md` | More Than a Computer | Establish the reader, the promise, and why this book exists | Reader writes a short "doors I want to open" note |

### Part 1 - You're Not Stuck

| Ch | File | Working Title | Purpose | Visible Outcome |
|----|------|---------------|---------|-----------------|
| 1 | `chapters/part-1/ch-01-youre-not-stuck.md` | You're Not Stuck | Break fatalism and replace it with possibility | Reader names one life problem or goal they want to move on |
| 2 | `chapters/part-1/ch-02-what-this-machine-gives-you.md` | What This Machine Really Gives You | Frame the machine as leverage, not identity | Reader creates a short "what this setup lets me do" list |
| 3 | `chapters/part-1/ch-03-learning-without-permission.md` | Learning Without Permission | Establish self-direction as the real skill | Reader writes their first concrete learning mission |

### Part 2 - Meet Your Machine

| Ch | File | Working Title | Purpose | Visible Outcome |
|----|------|---------------|---------|-----------------|
| 4 | `chapters/part-2/ch-04-meet-the-machine.md` | Meet the Machine | Make Omarchy feel legible on day one | Reader opens the key surfaces they need to operate daily |
| 5 | `chapters/part-2/ch-05-move-through-it.md` | Move Through It | Teach keyboard-first movement and confidence | Reader can open, switch, and control their main apps |
| 6 | `chapters/part-2/ch-06-the-terminal-is-not-a-wall.md` | The Terminal Is Not a Wall | Make the terminal approachable and useful | Reader completes a small set of terminal tasks successfully |
| 7 | `chapters/part-2/ch-07-read-the-manual-then-make-it-yours.md` | Read the Manual, Then Make It Yours | Teach manual-first learning directly | Reader uses the Omarchy manual to solve or customize one thing |

### Part 3 - Meet Your Teacher

| Ch | File | Working Title | Purpose | Visible Outcome |
|----|------|---------------|---------|-----------------|
| 8 | `chapters/part-3/ch-08-ai-is-not-a-vending-machine.md` | AI Is Not a Vending Machine | Reframe AI as collaborator instead of answer machine | Reader rewrites a weak AI request into a directed one |
| 9 | `chapters/part-3/ch-09-pick-the-right-hero.md` | Pick the Right Hero | Teach the Team-Captain model clearly | Reader builds a role prompt for a real task |
| 10 | `chapters/part-3/ch-10-the-horse-not-the-car.md` | The Horse, Not the Car | Teach why guidance and correction are necessary | Reader diagnoses one example of AI drift and corrects it |
| 11 | `chapters/part-3/ch-11-ask-refine-test-repeat.md` | Ask, Refine, Test, Repeat | Teach the practical loop for learning with AI | Reader completes one full iteration cycle on a real problem |

### Part 4 - Do Things That Matter

| Ch | File | Working Title | Purpose | Visible Outcome |
|----|------|---------------|---------|-----------------|
| 12 | `chapters/part-4/ch-12-build-your-launchpad.md` | Build Your Launchpad | Start the practical mission thread with a personal workspace | Reader creates a dedicated launchpad folder for a real goal |
| 13 | `chapters/part-4/ch-13-make-one-useful-tool.md` | Make One Useful Tool | Turn the machine into leverage with one simple tool | Reader creates one alias, script, or helper they actually use |
| 14 | `chapters/part-4/ch-14-fix-what-breaks.md` | Fix What Breaks | Teach recovery and troubleshooting as part of learning | Reader solves one real breakage with docs + AI + iteration |
| 15 | `chapters/part-4/ch-15-ship-a-small-win.md` | Ship a Small Win | Finish the thread with something kept, not discarded | Reader completes and keeps one small but real working system |

### Part 5 - Now You Choose

| Ch | File | Working Title | Purpose | Visible Outcome |
|----|------|---------------|---------|-----------------|
| 16 | `chapters/part-5/ch-16-pick-a-direction.md` | Pick a Direction | Show that there are multiple valid futures | Reader identifies a direction worth exploring next |
| 17 | `chapters/part-5/ch-17-build-your-own-curriculum.md` | Build Your Own Curriculum | Teach self-directed path building | Reader creates a simple learning roadmap of missions, docs, and tools |
| 18 | `chapters/part-5/ch-18-keep-going-without-permission.md` | Keep Going Without Permission | End the main body with agency and momentum | Reader defines the next three moves after the book |

### Conclusion

| File | Working Title | Purpose | Visible Outcome |
|------|---------------|---------|-----------------|
| `chapters/conclusion.md` | You Can Keep Going | Restate the thesis and point outward | Reader leaves with a durable sense of ownership |

---

## Part 4 Project Thread

### Decision

Use a **personal launchpad project thread** for Part 4.

The reader builds a lightweight but real system around one chosen goal. The
system includes:

- a dedicated workspace folder
- a plain-language mission note
- one useful helper tool
- one solved problem or friction point
- one small finished system worth keeping

### Rationale

- It is practical without requiring the reader to already identify as a
  programmer.
- It reinforces the book's actual subject: self-direction.
- It creates visible wins that are meaningful and personal.
- It naturally combines Linux, manuals, AI, iteration, and judgment.

### Constraints

- The thread must stay small enough to finish across four chapters.
- It cannot depend on paid services.
- It cannot require advanced programming knowledge.
- It should reward curiosity more than prior credentials.

---

## Mission Ladder

The book's mission difficulty should rise in this order:

1. Believe that movement is possible
2. Use the machine without fear
3. Use manuals as a source of power
4. Direct AI instead of hoping
5. Build one useful thing
6. Recover from friction
7. Choose the next path yourself

If a later chapter asks for a skill before the earlier rung is established, the
architecture is wrong.

---

## Core Mental Model Placement

| Model | Primary Chapter | Secondary Chapters |
|-------|-----------------|--------------------|
| Linux and AI are tools, not the subject | Introduction | Part 1 throughout |
| The future belongs to humans who use AI effectively | Introduction | Conclusion |
| Team-Captain model | Chapter 9 | Chapters 8 and 11 |
| Horse-Not-Car model | Chapter 10 | Chapter 11 and Part 4 |
| Manual-first learning | Chapter 7 | Part 2 and Part 4 |
| Learning without permission | Chapter 3 | Part 5 |

---

## Omarchy Manual Coverage Map

These manual sections are the primary technical anchors for the book's Omarchy
material.

| Chapter | Primary Manual Sections | Why They Matter |
|---------|-------------------------|-----------------|
| 4 | `Welcome to Omarchy`, `Navigation`, `Hotkeys` | First orientation to how the system works |
| 5 | `Navigation`, `Unified clipboard`, `Hotkeys` | Day-to-day movement and interaction confidence |
| 6 | `Terminal`, `Shell Tools`, `Shell Functions` | Practical terminal use without turning the book into a shell manual |
| 7 | `Navigation`, `AI`, `Development Tools`, `Shell Tools` | Best chapter to teach the read-docs -> ask-AI -> try-it loop |
| 12 | `Terminal`, `Shell Tools` | Building the launchpad workspace |
| 13 | `Shell Functions`, `Shell Tools`, `Development Tools` | Making one useful helper tool |
| 14 | `AI`, `Terminal`, `Shell Tools` | Troubleshooting and guided recovery |
| 15 | `Development Tools`, `AI`, `Terminal` | Finishing and keeping a small working system |

### Notes

- `Getting Started` is reference context, not a core chapter anchor, because
  the reader is assumed to have the machine already.
- `Themes` is optional flavor, not structural curriculum.
- `Neovim` is not required reading for the main reader journey.

---

## Review Sequence Per Chapter

Use these roles in this order when planning or reviewing chapters:

1. `mission-designer`
2. `pathfinder`
3. `manual-guide` for technical chapters
4. `confidence-auditor`
5. `continuity-editor`
6. `confused-beginner` or beginner-friction review where needed

This order protects mission clarity first, then meaning, then accuracy, then
reader confidence.
