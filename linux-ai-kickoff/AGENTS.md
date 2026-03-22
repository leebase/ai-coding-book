# Agent Guide: Teach Yourself Anything

> For AI agents working on the Teach Yourself Anything book workspace.
>
> Read this file first, then `context.md`.

---

## Purpose

This book is not primarily about Linux or AI. It is about helping a reader
become more self-directed, capable, and confident. Linux and AI are the two
foundational tools that open the rest of the doors.

Every session should protect three reader outcomes:

1. Inspired
2. Motivated
3. Empowered

If a technically correct choice makes the book less inspiring, less motivating,
or less empowering, it is probably the wrong choice.

---

## Startup Protocol

At the start of every session, read in order:

1. `AGENTS.md`
2. `context.md`
3. `result-review.md`
4. `sprint-plan.md`
5. `product-definition.md`
6. `project-plan.md`
7. `architecture.md` when chapter structure or sequencing matters

If the task touches chapter voice, also read `lee-voice.md`.

---

## Core Thesis

- The future does not belong to AI. It belongs to humans who learn to use AI effectively.
- AI is not the hero of this book. The reader is.
- AI is treated as a teacher, coach, and force multiplier, not a vending machine.
- GenAI is more like a horse than a car: powerful and useful, but not fully obedient.

---

## Guardrails

### Allowed

- Write and revise book-planning documents
- Create and refine agent roles for the writing workflow
- Add chapter scaffolding and planning artifacts
- Use official manuals and primary sources to ground technical sections

### Not Allowed Without Explicit Permission

- Add external runtime dependencies
- Delete existing files just to clean up history
- Turn the book into a Linux reference manual
- Turn the book into AI hype or AI fatalism

---

## Agent Roles

### Custom to this book

- `agents/pathfinder.md`
- `agents/confidence-auditor.md`
- `agents/manual-guide.md`
- `agents/mission-designer.md`

### Reusable from the repo when helpful

- Root `agents/continuity-editor.md`
- Root `agents/confused-beginner.md`
- `ai-env-book/agents/command-skeptic.md`
- `ai-env-book/agents/fresh-install.md`

Use the smallest set of roles that covers the current task.

---

## Source Discipline

When the book teaches Omarchy, use the official Omarchy manual as the primary
source:

- [The Omarchy Manual](https://learn.omacom.io/2/the-omarchy-manual)

This is part of the method. The reader should learn to read manuals, extract
what matters, and then use AI to clarify and apply the instructions.

---

## Working Convention

Before continuing a task mid-session:

1. Re-read `sprint-plan.md`
2. Re-read any files you modified earlier in the session
3. Confirm the current objective

At session end:

1. Update `context.md`
2. Update `result-review.md`
3. Update `sprint-plan.md` if task status changed
