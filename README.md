# The AI-Era Developer

> A hands-on guide to software engineering discipline in the age of AI coding tools.

---

## About This Book

AI coding tools are powerful. Most developers using them are frustrated — because they gave up engineering discipline when they picked up the AI. This book restores that discipline, chapter by chapter, through real exercises using Google Antigravity and the AgentFlow methodology.

**Thesis**: Software engineering discipline does not disappear in the AI era. It moves up a level. The AI writes the code. You are responsible for everything the code is supposed to do.

## Book Structure

### Part 1 — Engineering in the AI Era

The reader builds a **personal task manager CLI** from scratch across all seven chapters. Each chapter introduces one SE principle through a hands-on scenario.

| Ch | Title | Principle |
|----|-------|-----------|
| 1 | [Plan Before You Prompt](chapters/part-1/ch-01-plan-before-you-prompt.md) | Plan before you prompt |
| 2 | [Define Requirements](chapters/part-1/ch-02-define-requirements.md) | Define requirements before you build |
| 3 | [Test AI Output](chapters/part-1/ch-03-test-ai-output.md) | Test what the AI produces |
| 4 | [Review Like a PR](chapters/part-1/ch-04-review-like-a-pr.md) | Review AI output like a colleague's PR |
| 5 | [Iterate Deliberately](chapters/part-1/ch-05-iterate-deliberately.md) | Iterate deliberately, not randomly |
| 6 | [Manage Scope](chapters/part-1/ch-06-manage-scope.md) | The AI will gold-plate if you let it |
| 7 | [Document Decisions](chapters/part-1/ch-07-document-decisions.md) | Document decisions, not just code |

### Part 2 — The AgentFlow Methodology

For every principle from Part 1, Part 2 introduces the AgentFlow mechanism that enforces it systematically.

| Ch | Title | Mechanism |
|----|-------|-----------|
| 8 | [The AgentFlow Loop](chapters/part-2/ch-08-the-agentflow-loop.md) | The five-stage loop |
| 9 | [Skills and Autonomy Modes](chapters/part-2/ch-09-skills-and-autonomy-modes.md) | Skill system + three autonomy modes |
| 10 | [Context Files and Handoffs](chapters/part-2/ch-10-context-files-and-handoffs.md) | Document system for session continuity |
| 11 | [Multi-Agent Coordination](chapters/part-2/ch-11-multi-agent-coordination.md) | Parallel agents, merge review |
| 12 | [The Sprint Cadence](chapters/part-2/ch-12-the-sprint-cadence.md) | Sprint planning and execution |
| 13 | [Autonomy at Scale](chapters/part-2/ch-13-autonomy-at-scale.md) | Calibration heuristics, right mode for the task |
| 14 | [Putting It All Together](chapters/part-2/ch-14-putting-it-all-together.md) | Self-directed sprint, full system synthesis |

## Target Reader

- Working developers with 2–10 years of experience
- Already using AI tools casually, not systematically
- Frustrated that AI-assisted development is less predictable than expected

## Project Structure

```
├── chapters/
│   ├── part-1/          # Ch 1–7: SE principles
│   └── part-2/          # Ch 8–14: AgentFlow methodology
├── skills/              # AgentFlow skill definitions
├── agents/              # Agent role definitions
├── product-definition.md
├── project-plan.md
├── sprint-plan.md
├── context.md           # Session working memory
└── AGENTS.md            # Agent operating instructions
```

## Writing Methodology

This book was written using **AgentFlow** — the same documentation-driven methodology it teaches. The writing pipeline uses:

- A coordinator agent (`skills/ebook-writer.md`) with 9 stages
- Specialized agent roles: se-educator, scenario-designer, confused-beginner, continuity-editor, agentflow-architect
- The book-voice skill for consistent peer-to-peer tone

## Status

**14 of 14 chapters complete.** Moving into Phase 3: introduction, conclusion, continuity pass, and publication prep.

---

*Working title: "The AI-Era Developer"*
