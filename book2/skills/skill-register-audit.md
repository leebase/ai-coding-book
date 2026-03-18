# Skill: Register Audit

## Goal

Ensure the book consistently respects its reader — an experienced developer past the single-agent ceiling — and that the narrative project threads cohere across all chapters.

## Directives

### 1. Over-Explanation Detection

- The reader knows: what a prompt is, what a context window is, what an agent is, what API calls are, what version control is.
- Flag any paragraph that defines or re-explains one of these concepts from first principles.
- Flag any sentence that begins "In other words..." or "To put it simply..." — these are signals of distrust in the reader.
- Test: would a developer with three years of AI agent experience find this paragraph useful, or would they skip it?

### 2. Weasel Word Audit

- Search for: "basically," "actually," "just," "simply," "of course," "easy," "straightforward," "quickly."
- These dilute authority. Flag every instance with the chapter and sentence.
- "Just paste the role definition" is the worst offender — "just" makes friction invisible.

### 3. Part 1 Project Thread State Table

Build a file state table for Part 1 (Chapters 1–5 + Introduction):

| Chapter | Files Created | Files Modified | Files Referenced |
|---------|--------------|----------------|-----------------|
| Intro | — | — | — |
| Ch 1 | article-v1.md | — | — |
| Ch 2 | agents/researcher.md, research-notes.md | — | — |
| Ch 3 | agents/adversarial-reader.md, reader-notes.md | draft.md | research-notes.md |
| Ch 4 | skills/voice.md, skills/article-pipeline.md, agents/writer.md | — | — |
| Ch 5 | article-v2.md, final.md | — | article-v1.md, all agents, pipeline |
| Ch 6 | — | — | final.md |

Verify each chapter against this expected state. Flag any discrepancy.

### 4. Part 2 Project Thread State Table

Build a file state table for Part 2 (Chapters 7–11):

| Chapter | Files Created | Files Modified | Files Referenced |
|---------|--------------|----------------|-----------------|
| Ch 7 | requirement.md | — | — |
| Ch 8 | agents/planner.md, agents/implementer.md, agents/reviewer.md, agents/tester.md, agents/documenter.md | — | requirement.md |
| Ch 9 | skills/feature-sprint.md | — | all agents |
| Ch 10 | plan.md, git_summary.py, review-notes.md, test-report.md, test_git_summary.py | git_summary.py (revised) | requirement.md, all agents, feature-sprint.md |
| Ch 11 | README.md | — | all prior outputs |

Verify each chapter against this expected state. Flag any discrepancy.

### 5. Part 1 → Part 2 Transition Audit

- Does Chapter 7 open with an explicit reference to Part 1 that names what is being carried forward?
- Is the transition framed as "the same design decisions in a different domain" — or does it restart from zero?
- Does the reader feel continuous momentum, or does it feel like the book started over?
- Flag any Part 2 chapter that re-explains a design decision already made in Part 1 without naming the callback.
