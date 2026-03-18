# Product Definition: Code with Agent Teams

> **What we're building and why.**

---

## The Book in One Sentence

A hands-on guide that teaches developers to build and run teams of AI agents — first through a content pipeline that makes the coordination patterns visible, then applied directly to a coding workflow — using Google Antigravity as the vehicle throughout.

---

## The Problem

Developers who have used AI agents long enough have hit the same wall: the agent is capable, but complex work degrades. The context fills, focus drifts, quality drops. The obvious response is a better prompt. It doesn't work. The problem is not the prompt — it is the architecture. One agent, one context, doing everything, produces inconsistent results at scale.

The solution is coordination: multiple specialized agents, each doing one thing well, passing structured work between them. But most developers have no model for what that looks like in practice. They know orchestration frameworks exist. They do not know how to think about the problem before reaching for one.

This book gives them that model, grounded in a discipline they can practice immediately — with no external tooling required.

---

## The Thesis

> A single AI agent is a capable individual contributor. It cannot manage complexity at scale. The solution is not a smarter prompt — it is a team: specialized roles, shared memory, and a workflow that coordinates them.

The book makes this thesis practical in two domains: content production (Part 1) and software development (Part 2). The same coordination pattern applies to both. The reader learns it once and applies it twice.

---

## The Reader

**Who they are:**
- Working developers with hands-on experience using AI agents
- Have hit the quality ceiling: agent output degrades on complex, multi-part tasks
- Know orchestration frameworks exist but have not used them (or found them too heavy)
- Want more leverage from agents without writing infrastructure

**What they believe when they open the book:**
- Better prompts are the path to better output (they're not)
- Multi-agent coordination requires code and infrastructure (it doesn't — for a start)
- The AI should handle complexity on its own if you describe the task well enough

**What they can do when they close it:**
- Design a team of specialized agent roles for any complex repeatable task
- Write skills that coordinate a team through staged workflows — no external orchestrator required
- Apply the same coordination pattern to content production and software development
- Recognize the ceiling of document-driven coordination and know what the next level requires

---

## Standalone

This book does not require Book 1. Readers who have read *The AI-Era Developer* will recognize AgentFlow patterns — they are not named here, but the structures are consistent. Readers who have not read Book 1 will encounter the same ideas freshly, through the team metaphor rather than the methodology label.

---

## The Tool

**Google Antigravity** (free tier) — an agent-first IDE from Google DeepMind. Used throughout both parts. Free tier is a constraint by design.

---

## Spin-Off Architecture

This book is the canonical version. Tool-specific spin-offs (Claude Code, Cursor, etc.) will exist later. To support them, the book maintains a clear two-layer structure:

**Concept layer** — tool-agnostic. Principles, role design, skill structure, shared memory patterns. This is the content that carries across editions.

**Harness layer** — Antigravity-specific. UI paths, prompt formats, Manager View instructions. Marked with `> **Antigravity:**` callouts throughout. A spin-off replaces these sections without touching the surrounding prose.

Every chapter is written with this separation in mind. Antigravity steps live in callouts, not embedded in the conceptual narrative.

---

## Book Structure

### Part 1 — Build a Content Team

The reader builds a newsletter article pipeline using Antigravity. The pipeline produces one article: a brief becomes research notes, research notes become a draft, a draft becomes a final piece. Each chapter adds one component to the pipeline.

The part opens with a single-prompt attempt (Chapter 1) and closes by running the completed pipeline on the same topic (Chapter 5). The difference is visible and specific. Chapter 6 names the ceiling honestly.

Chapters:
1. Run the prompt — one agent, one shot; the output passes; that is the problem
2. The grounding problem — researcher role, grounding skill; research and writing are different tasks
3. The reader problem — adversarial reader role; the writer cannot be the reader
4. Voice and sequence — voice skill, pipeline coordinator; order and consistency are constraints
5. Run the pipeline — same topic as Chapter 1; compare; name what the skills produced
6. What you cannot trust — the honest ceiling; external orchestration named and pointed to

### Part 2 — Code with Agent Teams

The same coordination pattern applied to a software development workflow. The reader builds a feature sprint pipeline: requirements become an implementation plan, implementation plan drives a code session, code gets reviewed and tested. Each chapter maps directly to its Part 1 counterpart.

Chapters:
7. Translating the pattern — content roles → coding roles; what changes, what doesn't
8. The coding team — Planner, Implementer, Reviewer, Tester roles
9. The feature skill — a coordinator for a development sprint
10. Running a sprint — parallel agents, merge discipline, quality gates
11. Your coding team at work — full sprint synthesis; closing reveal

---

## The Comparison Exercise

Chapter 1 and Chapter 5 use the same topic. The reader keeps the Chapter 1 output and does not revisit it until Chapter 5. At Chapter 5, they run the pipeline and place both outputs side by side. The differences should be nameable: specific voice (not generic), grounded examples (not invented), a failure path in the examples (not just the success case), identified misconceptions addressed (not a survey of what the subject is).

The comparison is the argument. The book does not tell the reader the skills produce better output — it lets them observe it.

---

## The Honest Ceiling

The book does not oversell document-driven coordination. Chapter 6 states plainly:

- The AI does not always follow the skill faithfully — stages get collapsed, roles drift
- Output varies between runs — same skill, different quality
- Long sessions accumulate context in ways you did not design
- The gate is your main quality instrument, which means quality depends on knowing what to look for

External orchestration — programmatic routing, independent contexts per stage, structured output validation — solves these problems. It requires building something. That path is named and pointed to; it is not in this book.

---

## Constraints

- **Free tier only**: No scenario requires a paid Antigravity subscription
- **Two project threads**: Content pipeline (Part 1) and feature sprint pipeline (Part 2) — each coherent within its part
- **Harness separation**: Antigravity steps in callouts; concept layer must read cleanly without them
- **No hype**: The book does not argue agents are good or bad. It teaches how to coordinate them.
- **No external orchestrator**: Everything taught requires only Antigravity and document files

---

## Success Criteria

A reader finishes the book able to:
1. Design a set of agent roles for any complex repeatable task — specifying input, output, and scope for each
2. Write a coordinator skill that sequences roles through staged work
3. Run that pipeline in Antigravity without manual intervention at every step
4. Apply the same pattern to a software development sprint
5. Explain what document-driven coordination cannot do and what the next level requires

---

## Out of Scope

- External orchestration frameworks — named, pointed to, not taught here
- Multi-model coordination — Antigravity is the vehicle throughout
- Team coordination with human team members — agents only
- Book 1 content — SE discipline is assumed, not re-taught
- Production deployment or scaling — development workflow only
