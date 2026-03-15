# Product Definition: The AI-Era Developer

> **What we're building and why.**

---

## The Book in One Sentence

A hands-on guide that teaches software engineering discipline to developers who are building with AI — using Google Antigravity (free tier) as the vehicle and AgentFlow as the system.

---

## The Problem

AI coding tools are everywhere. Developers are using them. Most are frustrated.

The frustration has a root cause: they gave up engineering discipline when they picked up the AI. They stopped planning before building. They stopped defining requirements before asking the AI to implement them. They stopped treating test output as information. They accepted the first thing the AI produced.

The AI did not create this problem. The developer did, by treating the AI as a magic oracle instead of a capable but directionless collaborator.

---

## The Thesis

> Software engineering discipline does not disappear in the AI era. It moves up a level. The AI writes the code. You are responsible for everything the code is supposed to do.

This book makes that thesis practical, chapter by chapter, through real exercises in a real tool.

---

## The Reader

**Who they are:**
- Working developers with 2–10 years of experience
- Comfortable writing code, at least in one language
- Already using AI tools (autocomplete, chat, agents) — casually, not systematically
- Frustrated that AI-assisted development is less predictable than they expected

**What they believe when they open the book:**
- AI tools are powerful but unreliable
- Prompt engineering is the solution (it isn't)
- SE discipline is for big teams and enterprise projects (it isn't)

**What they can do when they close it:**
- Apply a repeatable engineering workflow to AI-assisted development
- Recognize when an AI is producing correct output vs. plausible-sounding garbage
- Use AgentFlow to maintain continuity across AI sessions, tools, and collaborators

---

## The Tool

**Google Antigravity** (free tier) — an agent-first IDE from Google DeepMind. The reader uses it throughout Part 1. Free tier is a constraint by design: it rewards planning before prompting.

---

## Book Structure

### Part 1 — Engineering in the AI Era

The reader builds one project from scratch across all of Part 1, using Antigravity. Each chapter introduces one SE principle through a hands-on scenario that shows both the disciplined path and the breakdown.

Principles covered (in order):
1. Plan before you prompt
2. Define requirements before you build
3. Test what the AI produces — don't assume it works
4. Review AI output like you'd review a colleague's PR
5. Iterate deliberately, not randomly
6. Manage scope — the AI will gold-plate if you let it
7. Document decisions, not just code

### Part 2 — The AgentFlow Methodology

Part 2 formalizes the discipline from Part 1. For every principle the reader experienced in Part 1, Part 2 introduces the AgentFlow mechanism that enforces it systematically.

Mechanisms covered:
- The document system (context.md, AGENTS.md, sprint-plan.md, etc.)
- The Development Loop
- Autonomy modes
- The skill system
- The backlog system
- Multi-session and multi-LLM continuity
- External review (sprint-review.md pattern)

---

## Constraints

- **Free tier only**: No scenario requires a paid Antigravity subscription
- **One project thread**: Part 1 builds one cohesive project — not a new toy per chapter
- **Principle first**: Every chapter earns its Antigravity steps by establishing the principle first
- **No hype**: The book does not argue AI is good or bad. It teaches how to work with it well.

---

## Success Criteria

A reader finishes the book able to:
1. Start a new AI-assisted project with a planning session before touching the tool
2. Write requirements specific enough that an AI agent can implement them without guessing
3. Evaluate AI output against the requirement, not against "does it look right"
4. Set up a basic AgentFlow document system for a new project in under 30 minutes
5. Hand off a session to a different AI (or a teammate) with zero context loss

---

## Out of Scope

- Teaching programming basics — the reader can already code
- Comparing AI tools — Antigravity is the vehicle, not the subject
- Covering every AgentFlow feature — Part 2 covers the essentials, not the advanced patterns
- Orchestration and multi-agent systems — out of scope for this edition
