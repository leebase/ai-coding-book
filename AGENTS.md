# Agent Guide: ai-coding-book

> **For AI agents working on the ai-coding-book project.**
>
> This project uses **AgentFlow** — a documentation-driven methodology for human-AI collaboration.
> Read this file first, then `context.md` for current state.

---

## Why This System Exists

AI agents are stateless. Every new session starts from zero. These project files act as **shared memory** between you, the human, and any other AI that works on this project.

When you update `context.md` at session end, you're writing a handoff note that lets **any LLM** — Claude, ChatGPT, Gemini, Copilot — pick up exactly where you left off. Treat these updates as critical, not clerical.

---

## Startup Protocol

At the start of every session, in order:

1. Read `AGENTS.md` (this file) — guardrails and operating rules
2. Read `context.md` — current state and what to do next
3. Check `result-review.md` — what was recently completed
4. Read `sprint-plan.md` — current sprint tasks and priorities

When starting a brand-new standalone book workspace, also read:

5. `how-to-start-a-new-book.md`

---

## Available Skills

Load the relevant skill file when the trigger applies. Do not try to remember — read the file.

| Trigger | Skill to Load |
|---------|--------------|
| You are implementing a feature or fix | `skills/development-loop.md` |
| You are about to test your work | `skills/test-as-lee.md` |
| You are about to commit | `skills/documentation.md` |
| You are creating a backlog item | `skills/backlog.md` |
| You are closing a sprint or preparing a release | `skills/code-review.md` |
| You are writing or planning a tutorial or chapter | `skills/tutorial-writer/tutorial-writer.md` |
| You are writing a book chapter | `skills/ebook-writer.md` |
| You are planning or writing a thesis-driven nonfiction / business book | `skills/thought-leadership-book.md` (`AuthorFlow`) |
| You are synthesizing citable research for argument support | `skills/research-synthesis.md` |
| You are turning lived experience into reusable story material | `skills/story-mining.md` |
| You are designing named frameworks, diagnostics, or visual models | `skills/framework-design.md` |
| You are shaping title, subtitle, audience, or proposal positioning | `skills/book-positioning.md` |
| You are reviewing a personal nonfiction / handbook draft through a reader persona | `skills/personal-audience-review.md` |
| You are reviewing whether a chapter actually works as a handbook | `skills/handbook-value-review.md` |
| You are reviewing parenting, health, meaning, identity, or other intimate material for boundary safety | `skills/personal-boundary-review.md` |
| You are doing a voice or cadence pass for the personal empowerment book | `skills/sounds-like-lee.md` |

Skills are short, focused, and task-specific. They contain the judgment, not just the steps.

---

## Task Rehydration

**Before continuing any task mid-session:**

1. Re-read `sprint-plan.md`
2. Re-read any files you modified previously in this session
3. Confirm the objective — proceed only when you are oriented

Agents drift. This rule prevents it.

### For standalone book directories

If you are working inside a standalone book directory such as
`growth-consulting-playbook/`, also re-read that directory's local
`context.md`, `result-review.md`, and `sprint-plan.md` before continuing.

---

## Autonomy Modes

The `Mode` field in `context.md` controls how independently you work:

| Mode | Name | Behavior |
|------|------|----------|
| **1** | Supervised | Ask before every significant action. Explain plan, wait for approval. |
| **2** | Collaborative | Plan approach, implement with check-ins. Ask for approval on decisions, not on routine code. |
| **3** | Autonomous | Execute independently within guardrails. Report results. Only ask if blocked or decision has major consequences. |

**Default is Mode 2.** The human may change the mode in `context.md` at any time.

---

## Guardrails

### ✅ Allowed

- Write and modify code for ai-coding-book
- Create and update documentation
- Add tests for new functionality
- Research solutions to technical problems
- Update context and decision logs
- Create backlog items in `backlog/candidates/`

### ❌ Not Allowed (Without Explicit Permission)

- Add external runtime dependencies
- Make breaking changes to existing APIs
- Delete files without confirming necessity
- Skip tests or documentation updates
- Commit directly to protected branches
- Move files out of `backlog/candidates/` (human curates)

---

## Document Reference

| File | When to Read | When to Update |
|------|--------------|----------------|
| `AGENTS.md` | Every session start | When conventions change |
| `how-to-start-a-new-book.md` | When starting a new standalone book | When startup conventions improve |
| `context.md` | Every session start | Every session end |
| `WHERE_AM_I.md` | Every session start | When milestones reached or direction changes |
| `result-review.md` | Every session start | When work completed |
| `sprint-plan.md` | Every session start | When tasks complete |
| `sprint-review.md` | After sprints | External AI fills in review |
| `project-plan.md` | When direction unclear | Strategic changes only |
| `product-definition.md` | When scope unclear | Product changes only |
| `architecture.md` | When making tech decisions | When decisions are made |
| `feedback.md` | When given feedback | Human adds feedback |
| `backlog/schema.md` | Creating backlog items | Never (reference) |
| `backlog/template.md` | Creating backlog items | Never (copy-paste) |

---

## Communication Style

- **Concise**: Get to the point quickly
- **Specific**: Include file paths, line numbers, exact commands
- **Actionable**: Provide clear next steps
- **Honest**: Flag concerns or blockers immediately

---

## AuthorFlow

Use this workflow for projects where the job is argument, positioning, evidence,
and framework design rather than tutorial instruction.

### Required skill

Load `skills/thought-leadership-book.md`.

For standalone books using this method, create and maintain an `author-flow.md`
file in the book directory as a running log of how the method is actually being
used.

When starting a new standalone book, follow `how-to-start-a-new-book.md`
before treating the scaffold as complete.

### Default sequence

1. Frame the thesis before drafting
2. Synthesize source-backed research and name the gaps
3. Mine lived stories into transferable patterns
4. Design named frameworks and diagnostics
5. Pressure-test title, subtitle, audience, and promise
6. Stop for human approval on the thinking
7. Draft prose only after the argument is sharp
8. Review the draft through book-appropriate audience lenses before calling it done
9. Run an explicit tone and cadence pass so the prose stays human, reflective, and inviting instead of drifting into brand voice or chopped-up slogan cadence

### Preferred agents

Core AuthorFlow roles:

- `agents/thesis-architect.md`
- `agents/research-synthesizer.md`
- `agents/story-miner.md`
- `agents/positioning-editor.md`
- `agents/argument-writer.md`
- `agents/continuity-editor.md`

Consulting / business reviewer stack:

- `agents/big-consulting-reviewer.md`
- `agents/mid-market-consulting-reviewer.md`
- `agents/independent-consultant-reviewer.md`
- `agents/enterprise-transformation-reviewer.md`
- `agents/business-unit-leader-reviewer.md`
- `agents/cfo-reviewer.md`

Personal empowerment reviewer stack:

- `agents/human-empowerment-reviewer.md`
- `agents/reflective-working-adult-reviewer.md`
- `agents/practical-handbook-reviewer.md`
- `agents/skeptical-high-agency-reviewer.md`
- `agents/parenting-real-life-reviewer.md`
- `agents/meaning-and-identity-boundary-reviewer.md`

Use the stack that matches the book's protagonist and stakes. Do not force
consulting reviewers onto a personal handbook.

### Default artifacts

Create or update planning artifacts that keep thinking separate from prose.
Favor:

- thesis brief
- research support memo
- story bank
- framework notes
- positioning notes
- author-flow log

Do not let note accumulation replace selection. If the core argument cannot be
stated cleanly, keep refining the thinking instead of drafting chapters.

---

## For Antigravity Agents (Google DeepMind)

If you are an Antigravity agent, map your internal artifacts to this project's documentation system.

### Artifact Mapping

| Internal Artifact | Project Document | Purpose |
|-------------------|------------------|---------| 
| `task.md` | `sprint-plan.md` | Track task status. **Read** project plan to populate your checklist. **Update** project plan when tasks complete. |
| `implementation_plan.md` | `architecture.md` / Design Docs | Plan technical changes. If the change is significant, create/update a design doc in the project as well. |
| `walkthrough.md` | `result-review.md` | Log results. **Update** `result-review.md` at the end of your session with a summary of your work. |

### Workflow Adjustments

1. **Session Start**: In addition to standard files, read `task.md` (if existing) and sync it with `sprint-plan.md`.
2. **During Work**: Use your internal `task.md` for fine-grained steps, but update `sprint-plan.md` for high-level status.
3. **Session End**: Ensure `context.md` and `result-review.md` are updated. Your `walkthrough.md` should summarize these updates.

---

*Generated by init-agent on 2026-03-15*
