# ai-coding-book Result Review

> **Running log of completed work.** Newest entries at the top.
>
> Each entry documents what was built, why it matters, and how to verify it works.

---

## 2026-03-18 — Book 2 EPUB Readability Fixes and Post-Publication Review Sync

## 2026-03-18 — Book 2 Rebuilt From Claude-Reviewed Source

**Rebuilt all three Book 2 publication outputs** after applying the accepted Claude-review fixes. EPUB was regenerated with `pandoc`, DOCX was regenerated with the local Node builder, PDF was regenerated with `pandoc` + WeasyPrint, and `book2/build-docx.js` was updated so the DOCX now carries the correct title and author metadata instead of the default `Un-named` values.

### How to Verify

1. Confirm the rebuilt artifacts exist:
   - [book2/coding-with-agent-teams.epub](/Users/lee/projects/ai-coding-book/book2/coding-with-agent-teams.epub)
   - [book2/coding-with-agent-teams.docx](/Users/lee/projects/ai-coding-book/book2/coding-with-agent-teams.docx)
   - [book2/coding-with-agent-teams.pdf](/Users/lee/projects/ai-coding-book/book2/coding-with-agent-teams.pdf)
2. Open [book2/build-docx.js](/Users/lee/projects/ai-coding-book/book2/build-docx.js) and confirm the document metadata now sets title, creator, and lastModifiedBy
3. Inspect DOCX core metadata:
   - `unzip -p book2/coding-with-agent-teams.docx docProps/core.xml`
   - verify it includes `Coding with Agent Teams` and `Lee Harrington`
4. Confirm the PDF is a fresh valid file:
   - `file book2/coding-with-agent-teams.pdf`
   - verify it reports a PDF document

## 2026-03-18 — Book 2 Claude Review Pass Applied

**Applied the high-signal fixes from the Claude review memo** without taking the review as a wholesale rewrite. The accepted changes were all execution- and harness-related: clearer directory-creation instructions, explicit gate confirmation language, new `Watch For` callouts in the Part 2 setup chapters, a concept-level explanation of parallel Reviewer/Tester stages in Chapter 10, and exact Stage 5 test rerun commands.

### How to Verify

1. Open [book2/claude_says.md](/Users/lee/projects/ai-coding-book/book2/claude_says.md) and confirm the review memo is present in the live repo
2. Open [book2/chapters/part-1/ch-05-run-the-pipeline.md](/Users/lee/projects/ai-coding-book/book2/chapters/part-1/ch-05-run-the-pipeline.md) and confirm the Stage 1 gate now includes the explicit message `Stage 1 complete. Proceed to Stage 2.`
3. Open [book2/chapters/part-2/ch-07-translating-the-pattern.md](/Users/lee/projects/ai-coding-book/book2/chapters/part-2/ch-07-translating-the-pattern.md), [book2/chapters/part-2/ch-08-the-coding-team.md](/Users/lee/projects/ai-coding-book/book2/chapters/part-2/ch-08-the-coding-team.md), and [book2/chapters/part-2/ch-09-the-feature-skill.md](/Users/lee/projects/ai-coding-book/book2/chapters/part-2/ch-09-the-feature-skill.md) and confirm the new `Watch For` scaffolding is present
4. Open [book2/chapters/part-2/ch-10-running-a-sprint.md](/Users/lee/projects/ai-coding-book/book2/chapters/part-2/ch-10-running-a-sprint.md) and confirm it now explains what parallel stages mean and includes exact test rerun commands
5. Open [book2/harness-inventory.md](/Users/lee/projects/ai-coding-book/book2/harness-inventory.md) and confirm the new `Swap 10.5b` test-rerun step is tracked

## 2026-03-18 — Environment Book Review Cleanup and Book 2 EPUB Hard-Wrap Fix

**Completed two targeted follow-ups.** First, the Environment book was restored from Gemini's direct chapter rewrites back to the committed manuscript, then updated manually with only a small set of worthwhile clarity improvements in the original voice. Second, Book 2's EPUB readability issue was fixed at the manuscript level by hard-wrapping the worst long-line fenced examples and rebuilding the EPUB so the fix no longer depends on reader support for CSS `pre` wrapping.

### How to Verify

1. Open [ai-env-book/gemini_says.md](/Users/lee/projects/ai-coding-book/ai-env-book/gemini_says.md) and confirm the review memo remains present as reference
2. Open [ai-env-book/chapters/ch-03-auth.md](/Users/lee/projects/ai-coding-book/ai-env-book/chapters/ch-03-auth.md), [ai-env-book/chapters/ch-06-python-env-problem.md](/Users/lee/projects/ai-coding-book/ai-env-book/chapters/ch-06-python-env-problem.md), [ai-env-book/chapters/ch-08-requirements-and-pyproject.md](/Users/lee/projects/ai-coding-book/ai-env-book/chapters/ch-08-requirements-and-pyproject.md), [ai-env-book/chapters/ch-10-nvm-and-versions.md](/Users/lee/projects/ai-coding-book/ai-env-book/chapters/ch-10-nvm-and-versions.md), [ai-env-book/chapters/ch-13-warp-basics.md](/Users/lee/projects/ai-coding-book/ai-env-book/chapters/ch-13-warp-basics.md), and [ai-env-book/chapters/ch-14-warp-workflows.md](/Users/lee/projects/ai-coding-book/ai-env-book/chapters/ch-14-warp-workflows.md) to see the selective clarity fixes
3. Open [book2/chapters/part-1/ch-01-run-the-prompt.md](/Users/lee/projects/ai-coding-book/book2/chapters/part-1/ch-01-run-the-prompt.md) and confirm the comment-block example is manually wrapped across short lines
4. Confirm the rebuilt EPUB exists at [book2/coding-with-agent-teams.epub](/Users/lee/projects/ai-coding-book/book2/coding-with-agent-teams.epub)

---

## 2026-03-18 — Book 2 EPUB Readability Fixes and Post-Publication Review Sync

**Applied post-publication Book 2 fixes** after human EPUB review. The main reader-facing changes were replacing "confabulation" with plainer wording in Book 2's source chapters and combined manuscript, tightening EPUB code-block wrapping in `book2/epub-styles.css`, rebuilding `coding-with-agent-teams.epub`, and logging the remaining callout-trimming pass in the project docs.

### How to Verify

1. Open [book2/epub-styles.css](/Users/lee/projects/ai-coding-book/book2/epub-styles.css) and confirm the `pre` block includes stronger wrapping rules such as `overflow-wrap: anywhere` and `word-break: break-word`
2. Open [book2/chapters/part-1/ch-02-the-grounding-problem.md](/Users/lee/projects/ai-coding-book/book2/chapters/part-1/ch-02-the-grounding-problem.md) and confirm "The Verification Test" replaced "The Confabulation Test"
3. Confirm the rebuilt EPUB exists at [book2/coding-with-agent-teams.epub](/Users/lee/projects/ai-coding-book/book2/coding-with-agent-teams.epub)
4. Read [feedback.md](/Users/lee/projects/ai-coding-book/feedback.md) and [book2/context.md](/Users/lee/projects/ai-coding-book/book2/context.md) to confirm the remaining follow-up is the callout-trimming pass

---

## 2026-03-17 — Environment Book Finished, Rebuilt, and QA'd

**Completed the standalone Environment book** end to end: restored missing chapter sources, expanded the thin chapters, synced the companion-project details from `book-project-writeup.md`, fixed continuity drift in ports and scenario references, rebuilt all publication outputs, and verified the packaging.

**Also fixed two publication-tooling issues** during finish work:
- `ai-env-book/build-epub.py` now splits chapters by real top-level manuscript headings instead of every `---`, which eliminated the broken TOC entries like “Chapter 18”, “Chapter 19”, etc.
- `ai-env-book/build-docx.py` now writes proper core metadata so the generated DOCX carries the actual title and author.

### How to Verify

1. Open `ai-env-book/context.md` and `ai-env-book/sprint-plan.md` to confirm the book is marked complete
2. Confirm the rebuilt outputs exist:
   - `ai-env-book/your-dev-environment.epub`
   - `ai-env-book/your-dev-environment.docx`
   - `ai-env-book/your-dev-environment.pdf`
3. Inspect the EPUB nav:
   - `unzip -p ai-env-book/your-dev-environment.epub EPUB/nav.xhtml`
   - verify it lists Introduction, Chapters 1–15, and Conclusion only
4. Inspect DOCX core metadata:
   - `unzip -p ai-env-book/your-dev-environment.docx docProps/core.xml`
   - verify the title is `Your Dev Environment: A Guide for AI-Assisted Developers` and the creator is `Lee Harrington`

---

## 2026-03-17 — Series Roadmap and Environment Sprint Plan Synced

**Updated repo documentation** to reflect the actual roadmap: Book 1 and Book 2 are the completed main-arc books, `ai-env-book/` is a standalone environment primer, and the planned main-arc Book 3 is about independent/autonomous agents.

**Also updated** `ai-env-book/sprint-plan.md` to replace stale Linear staging guidance with an editing-phase plan, including source/manuscript alignment, publication QA, and explicit doc-sync work before the next rebuild.

### How to Verify

1. Read `README.md` for the main-arc vs standalone-primer framing
2. Read `context.md` and `WHERE_AM_I.md` for updated roadmap status
3. Read `ai-env-book/sprint-plan.md` for the current editing sequence and exit criteria

---

## 2026-03-15 — All Documents Updated

README.md, context.md, WHERE_AM_I.md, result-review.md, and project-plan.md updated to reflect completion of all 14 chapters and transition to Phase 3.

---

## 2026-03-15 — Project Scaffolded

**Project initialized** with init-agent.

### Created

| File | Purpose |
|------|---------|
| `AGENTS.md` | AI agent guide and conventions |
| `WHERE_AM_I.md` | Quick orientation for agents |
| `feedback.md` | Human feedback capture |
| `README.md` | Project documentation |
| `context.md` | Session working memory |
| `result-review.md` | This file - running log |
| `sprint-plan.md` | Sprint tracking |

### How to Verify

1. Check all files exist: `ls *.md`
2. Read AGENTS.md to understand project conventions
3. Check context.md for current state

---

## Sprint 0 — Foundation (Complete)

**Goal**: Writing infrastructure ready to produce chapters.

### Created
- AgentFlow scaffold (AGENTS.md, CLAUDE.md)
- Writing pipeline (ebook-writer coordinator, 9 stages)
- Agent roles: se-educator, scenario-designer, antigravity-expert, confused-beginner, continuity-editor, agentflow-architect
- Supporting skills: scenario-builder, antigravity-guide, book-voice
- Tutorial-writer sub-skills (18 skills)
- product-definition.md, project-plan.md, sprint-plan.md

---

## Sprint 1 — Chapter 1: Plan Before You Prompt (Complete)

**Goal**: First chapter drafted, reviewed, and committed. Project thread established.

### Created
- `chapters/part-1/ch-01-plan-before-you-prompt.md`
- Part 1 project decision: task manager CLI

---

## Sprint 2 — Chapter 2: Define Requirements Before You Build (Complete)

**Goal**: Priority feature as vehicle for verifiable requirements.

### Created
- `chapters/part-1/ch-02-define-requirements.md`

---

## Sprint 3 — Chapter 3: Test What the AI Produces (Complete)

**Goal**: Requirement-derived tests vs. AI self-tests; 9-test suite, 1 real bug found.

### Created
- `chapters/part-1/ch-03-test-ai-output.md`

---

## Sprint 4 — Chapter 4: Review AI Output Like a PR (Complete)

**Goal**: Understanding gap, 5-question PR checklist, 3 targeted fixes.

### Created
- `chapters/part-1/ch-04-review-like-a-pr.md`

---

## Sprint 5 — Chapter 5: Iterate Deliberately (Complete)

**Goal**: Due dates feature via 4-increment plan; 9→11 tests.

### Created
- `chapters/part-1/ch-05-iterate-deliberately.md`

---

## Sprint 6 — Chapter 6: Manage Scope (Complete)

**Goal**: Gold-plating problem; search command with explicit "Does NOT" scope boundary; 11→12 tests.

### Created
- `chapters/part-1/ch-06-manage-scope.md`

---

## Sprint 7 — Chapter 7: Document Decisions (Complete)

**Goal**: Decision log as insurance against AI amnesia; `--format json` as scenario; 12→13 tests; decisions.md artifact.

### Created
- `chapters/part-1/ch-07-document-decisions.md`

---

## Sprint 8 — Chapter 8: The AgentFlow Loop (Complete)

**Goal**: Name the loop; five stages map to Part 1 disciplines; `stats` command as full loop walkthrough; 13→14 tests.

### Created
- `chapters/part-2/ch-08-the-agentflow-loop.md`

---

## Sprint 9 — Chapter 9: Skills and Autonomy Modes (Complete)

**Goal**: Skills encode the Start stage; `start-session.md` created; `clear` command as scenario; 14→15 tests; three autonomy modes defined.

### Created
- `chapters/part-2/ch-09-skills-and-autonomy-modes.md`

---

## Sprint 10 — Chapter 10: Context Files and Handoffs (Complete)

**Goal**: context.md separates state from instructions; handoff test; start-session.md updated to reference context.md.

### Created
- `chapters/part-2/ch-10-context-files-and-handoffs.md`

---

## Sprint 11 — Chapter 11: Multi-Agent Coordination (Complete)

**Goal**: Manager View first use; --priority filter (Agent A) + COMMANDS.md (Agent B) as parallel scenario; 15→16 tests; merge review discipline.

### Created
- `chapters/part-2/ch-11-multi-agent-coordination.md`

---

## Sprint 12 — Chapter 12: The Sprint Cadence (Complete)

**Goal**: Sprint plan template; export sprint (--format csv + export command); 16→18 tests; dependency analysis catches serialization requirement.

### Created
- `chapters/part-2/ch-12-the-sprint-cadence.md`

---

## Sprint 13 — Chapter 13: Autonomy at Scale (Complete)

**Goal**: Calibration heuristic (3 factors × 3 modes); --done filter at Mode 2; tag field at Mode 1; COMMANDS.md update at Mode 3; 18→20 tests.

### Created
- `chapters/part-2/ch-13-autonomy-at-scale.md`

---

## Sprint 14 — Chapter 14: Putting It All Together (Complete)

**Goal**: Synthesis chapter; reader runs a self-directed sprint on a backlog feature; full AgentFlow system demonstrated as one coherent practice; book closes.

### Created
- `chapters/part-2/ch-14-putting-it-all-together.md`

---

*Add new entries above this line. Keep the newest work at the top.*
