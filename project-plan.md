# Project Plan: The AI-Era Developer

> **Strategic roadmap.** For tactical execution, see `sprint-plan.md`.

---

## Phases

### Phase 0 — Foundation (COMPLETE ✅)
- AgentFlow scaffold (AGENTS.md, CLAUDE.md, context.md)
- Writing pipeline (ebook-writer, agents, skills)
- Product definition and project plan
- Sprint plan for Phase 1

### Phase 1 — Part 1: Engineering in the AI Era (COMPLETE ✅)

Seven chapters. One project thread (task manager CLI) built across all of them.

| Chapter | Title | Principle | Status |
|---------|-------|-----------|--------|
| 1 | Plan Before You Prompt | Plan before you prompt | ✅ Done |
| 2 | Define Requirements | Define requirements before you build | ✅ Done |
| 3 | Test AI Output | Test what the AI produces | ✅ Done |
| 4 | Review Like a PR | Review AI output like a colleague's PR | ✅ Done |
| 5 | Iterate Deliberately | Iterate deliberately, not randomly | ✅ Done |
| 6 | Manage Scope | The AI will gold-plate if you let it | ✅ Done |
| 7 | Document Decisions | Document decisions, not just code | ✅ Done |

### Phase 2 — Part 2: The AgentFlow Methodology (COMPLETE ✅)

Seven chapters. Each formally answers a pain point from Part 1.

| Chapter | Title | AgentFlow Mechanism | Part 1 Pain It Solves | Status |
|---------|-------|--------------------|-----------------------|--------|
| 8 | The AgentFlow Loop | The five-stage loop | "My workflow is chaotic" (Ch 3, 5) | ✅ Done |
| 9 | Skills and Autonomy Modes | Skill system + autonomy modes | "I repeat myself every session" (Ch 2, 7) | ✅ Done |
| 10 | Context Files and Handoffs | Document system for continuity | "I lose context between sessions" (Ch 1) | ✅ Done |
| 11 | Multi-Agent Coordination | Parallel agents, merge review | "I don't know how much to trust it" (Ch 4) | ✅ Done |
| 12 | The Sprint Cadence | Sprint planning and execution | "Scope keeps expanding" (Ch 6) | ✅ Done |
| 13 | Autonomy at Scale | Calibration heuristics | "The AI does whatever it wants" (Ch 1, 6) | ✅ Done |
| 14 | Putting It All Together | Full system synthesis | "Switching tools breaks everything" (Ch 1, 7) | ✅ Done |

### Phase 3 — Polish & Publication Prep (ACTIVE 🔄)
- Introduction chapter
- Conclusion chapter
- Full continuity read (continuity-editor pass across all 14 chapters)
- Copyedit pass
- Format for publication (markdown → target format)
- Index / glossary (if applicable)

---

## The Project Thread

The reader builds **one project** across all of Part 1. The book uses a **personal task manager CLI** as the default project — familiar domain, no external dependencies, grows naturally across 7 chapters.

Readers who prefer to use their own project can do so, provided it meets the criteria below.

### Criteria for a Valid Part 1 Project

A suitable project must satisfy all of the following:

**Scope**
- Can be set up from scratch in under 30 minutes using free-tier Antigravity
- Has enough surface area to demonstrate all 7 SE principles without feeling forced
- Is not so large that any single chapter requires more than 1–2 hours of Antigravity work

**Independence**
- No external paid APIs or services required
- No authentication systems (adds complexity that distracts from SE principles)
- No real-time or infrastructure concerns (no databases, message queues, or cloud deployments)
- Runnable locally with a single command

**Growth potential**
- Can start minimal (Ch 1) and accumulate features across all 7 chapters without requiring rewrites
- Each chapter can add one meaningful capability to the project
- The failure scenarios in each chapter (what happens when discipline breaks down) are plausible within this project's domain

**Demonstrability**
- Has visible, testable output — the reader can see and verify what the AI built
- Supports meaningful unit tests (not just "does it run")
- Has a user-facing interface, even if minimal (CLI flags, a simple API, a UI)

**Good fits**: CLI tools, simple REST APIs, data processing scripts, personal automation tools, small web apps with no auth.

**Poor fits**: Games (too creative), data pipelines with external sources (too much setup), anything requiring a paid service, anything with real-time requirements.

---

## Content Directory

All chapter drafts live in `chapters/`:

```
chapters/
├── part-1/
│   ├── ch-01-plan-before-you-prompt.md
│   ├── ch-02-define-requirements.md
│   ├── ch-03-test-ai-output.md
│   ├── ch-04-review-like-a-pr.md
│   ├── ch-05-iterate-deliberately.md
│   ├── ch-06-manage-scope.md
│   └── ch-07-document-decisions.md
└── part-2/
    ├── ch-08-the-agentflow-loop.md
    ├── ch-09-skills-and-autonomy-modes.md
    ├── ch-10-context-files-and-handoffs.md
    ├── ch-11-multi-agent-coordination.md
    ├── ch-12-the-sprint-cadence.md
    ├── ch-13-autonomy-at-scale.md
    └── ch-14-putting-it-all-together.md
```

---

## Sprint Rhythm

One chapter per sprint. Each sprint follows the `ebook-writer.md` pipeline:
- Stage 1–3 + GATE → human approves outline
- Stage 5–9 → draft, review, refine
- Commit chapter draft
- Update context.md and sprint-plan.md
- Start next sprint

---

## Risks

| Risk | Mitigation |
|------|------------|
| Project thread breaks between chapters | continuity-editor review every chapter |
| Part 2 repeats Part 1 instead of building on it | agentflow-architect review, explicit Part 1 anchors |
| Chapters drift from the book's thesis | book-voice skill loaded every writing stage |
| Free-tier Antigravity changes | Antigravity steps marked clearly; update antigravity-guide.md if UI changes |
