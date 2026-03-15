# CLAUDE.md — ai-coding-book

This project uses **AgentFlow**, a documentation-driven methodology for human-AI collaboration.

## Startup Protocol

At the start of every session, read in order:

1. `AGENTS.md` — guardrails and operating rules
2. `context.md` — current state and what to do next
3. `result-review.md` — recently completed work
4. `sprint-plan.md` — current sprint tasks and priorities

## Autonomy Mode

The `Mode` field in `context.md` controls independence:

| Mode | Name | Behavior |
|------|------|----------|
| 1 | Supervised | Ask before every significant action |
| 2 | Collaborative | Implement with check-ins; ask on decisions, not routine code |
| 3 | Autonomous | Execute independently; report results; ask only if blocked |

**Default: Mode 2.**

## Skills

Load the relevant skill file when the trigger applies:

| Trigger | Skill |
|---------|-------|
| Implementing a feature or fix | `skills/development-loop.md` |
| About to test | `skills/test-as-lee.md` |
| About to commit | `skills/documentation.md` |
| Creating a backlog item | `skills/backlog.md` |
| Closing a sprint / preparing release | `skills/code-review.md` |
| Writing or planning a tutorial or chapter | `skills/tutorial-writer/tutorial-writer.md` |
| Writing a book chapter | `skills/ebook-writer.md` |

## Guardrails

**Allowed:** write/modify code, create/update docs, add tests, research, update context and decision logs, create backlog items in `backlog/candidates/`.

**Not allowed without explicit permission:** add external runtime dependencies, make breaking API changes, delete files without confirming, skip tests or docs, commit to protected branches, move files out of `backlog/candidates/`.

## Task Rehydration

Before continuing any task mid-session: re-read `sprint-plan.md`, re-read modified files, confirm the objective. Agents drift — this prevents it.
