# Agent Guide: ai-env-book

> **For AI agents working on the ai-env-book project.**
>
> This project uses **AgentFlow** — a documentation-driven methodology for human-AI collaboration.
> Read this file first, then `context.md` for current state.

---

## Why This System Exists

AI agents are stateless. Every Symphony run starts from zero. These project files act as
shared memory between the human, Symphony, and any other AI that works on this project.

The BACKLOG.md is the canonical planning ledger. Linear is the execution queue.
Progress means a landed artifact in the live repo, not commentary or issue churn.

---

## Startup Protocol

At the start of every session or Symphony run, read in order:

1. `AGENTS.md` (this file) — guardrails and operating rules
2. `context.md` — current state and what to do next
3. `BACKLOG.md` — find the active AENV-xxx issue and read its full entry
4. The agent mission file named in the issue entry (`agents/`)
5. The skill files listed in the issue entry (`skills/`)

Do not act until you have read all five. Agents drift — this prevents it.

---

## Operating Mode

This project uses **Symphony + Linear in manual mode**.

- A human reads `BACKLOG.md`, selects a ready item, and stages it in Linear
- Symphony executes one issue at a time
- The `after_run` guard validates the artifact before allowing Done
- There is no hourly automation, no autonomous queue selection, no heartbeat

One active `Todo` at all times. Everything else in `Backlog`.

---

## Agent Roles

| Agent | Mission File | When to Use |
|-------|-------------|-------------|
| Program Director | `agents/program-director.md` | Framing issues, scope decisions, staging runway |
| Researcher | `agents/researcher.md` | Chapter brief issues (AENV-xxx research brief) |
| Writer | `agents/writer.md` | Chapter draft and final issues |
| Editor and QA | `agents/editor-and-qa.md` | Chapter review issues |

Default pattern per chapter:
1. Researcher produces the brief
2. Writer drafts from the brief
3. Editor and QA reviews the draft
4. Writer produces the final from the review notes

---

## Skills

Load the skill files named in the BACKLOG.md issue entry. Do not guess — read the file.

| Skill | File | Purpose |
|-------|------|---------|
| Book voice | `skills/book-voice.md` | Voice register for new-dev reader. Load for all draft and final issues. |
| Env explainer | `skills/env-explainer.md` | How to explain environment concepts. Load for all brief and draft issues. |
| New-dev validator | `skills/new-dev-validator.md` | Attack drafts from zero-context reader perspective. Load for all review issues. |
| Scenario thread | `skills/scenario-thread.md` | Canonical scenario state. Load for all issues. |
| Warp expert | `skills/warp-expert.md` | Warp.dev patterns and features. Load for all Part 4 issues. |

**`skills/scenario-thread.md` is loaded by every issue without exception.**

---

## Guardrails

### Allowed

- Write chapter briefs, drafts, review memos, and final chapters
- Write and update skill files
- Update `context.md` and `BACKLOG.md` status fields at run end
- Leave a blocked reason in `.symphony-state/blocked.md` if blocked

### Not Allowed Without Explicit Permission

- Modify `WORKFLOW.md`, `scripts/`, or other orchestration files during a chapter issue
- Move an issue to `Done` directly — write `.symphony-state/completion-ready.md` instead
- Edit chapters outside the active issue scope
- Add new AENV-xxx issues to `BACKLOG.md` (human curates)
- Modify `skills/scenario-thread.md` without flagging the change explicitly

---

## Completion Protocol

When the artifact is verified:

1. Write `.symphony-state/completion-ready.md` immediately
2. Include: artifact path, word count or section count, verification command and result
3. Make only minimum required updates to `context.md` and `BACKLOG.md`
4. Stop — do not start another implementation loop

The external `after_run` guard handles Done promotion. Do not set Done yourself.

---

## Document Reference

| File | Read When | Update When |
|------|-----------|-------------|
| `AGENTS.md` | Every run start | Conventions change |
| `context.md` | Every run start | Every run end |
| `BACKLOG.md` | Every run start | Issue status changes |
| `architecture.md` | Tech or structure decisions | Decisions made |
| `project-plan.md` | Direction unclear | Phase completes |
| `sprint-plan.md` | Staging decisions | Phase changes or runway restaged |
