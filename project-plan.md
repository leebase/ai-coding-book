# Project Plan: The AI-Era Developer

> **Strategic roadmap.** For tactical execution, see `sprint-plan.md`.

---

## Phases

### Phase 0 — Foundation (COMPLETE)
- AgentFlow scaffold (AGENTS.md, CLAUDE.md, context.md)
- Writing pipeline (ebook-writer, agents, skills)
- Product definition and project plan
- Sprint plan for Phase 1

### Phase 1 — Part 1: Engineering in the AI Era

Seven chapters. One project thread built across all of them. Each chapter = one sprint.

| Chapter | Principle | Status |
|---------|-----------|--------|
| 1 | Plan before you prompt | ⬜ Not started |
| 2 | Define requirements before you build | ⬜ Not started |
| 3 | Test what the AI produces | ⬜ Not started |
| 4 | Review AI output like a PR | ⬜ Not started |
| 5 | Iterate deliberately | ⬜ Not started |
| 6 | Manage scope | ⬜ Not started |
| 7 | Document decisions | ⬜ Not started |

**Phase 1 milestone:** Part 1 complete, coherent project thread, reviewed by adversarial reader.

### Phase 2 — Part 2: The AgentFlow Methodology

Seven chapters. Each formally answers a pain point from Part 1.

| Chapter | AgentFlow Mechanism | Part 1 Pain It Solves | Status |
|---------|--------------------|-----------------------|--------|
| 8 | The document system | "I lose context between sessions" (Ch 1) | ⬜ Not started |
| 9 | AGENTS.md — the contract | "The AI does whatever it wants" (Ch 1, 6) | ⬜ Not started |
| 10 | The Development Loop | "My workflow is chaotic" (Ch 3, 5) | ⬜ Not started |
| 11 | Autonomy modes | "I don't know how much to trust it" (Ch 4) | ⬜ Not started |
| 12 | The skill system | "I repeat myself every session" (Ch 2, 7) | ⬜ Not started |
| 13 | The backlog system | "Scope keeps expanding" (Ch 6) | ⬜ Not started |
| 14 | Multi-session continuity | "Switching tools breaks everything" (Ch 1, 7) | ⬜ Not started |

**Phase 2 milestone:** Part 2 complete, AgentFlow connections to Part 1 verified by agentflow-architect role.

### Phase 3 — Polish & Publication Prep
- Introduction and conclusion chapters
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
    ├── ch-08-document-system.md
    ├── ch-09-agents-md.md
    ├── ch-10-development-loop.md
    ├── ch-11-autonomy-modes.md
    ├── ch-12-skill-system.md
    ├── ch-13-backlog-system.md
    └── ch-14-multi-session-continuity.md
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
