# Skill: Book 2 Voice

This book has a specific voice. When writing any chapter prose, adopt it. This file overrides `skills/book-voice.md` for Book 2 content.

---

## Who You Are Writing To

A developer who already uses AI agents and has already run into the wall. They are not frustrated that AI is unpredictable — they figured out how to get consistent output from a single agent. They are frustrated that the approach does not scale. The tasks they care about are too big, too multi-part, or too quality-sensitive for one agent to handle well.

They have probably heard of orchestration frameworks. They may have looked at one and decided it was too much infrastructure for what they needed. They are here because they want the thinking — the model for how to coordinate agents — not a framework to install.

They do not need convincing that AI agents are useful. They are past that. They need a system.

---

## The Register

**Peer-to-peer. Systemic. No hand-holding.**

Write as a senior developer who has built a few of these pipelines and is explaining the design decisions — not the steps, the decisions. Why this role exists. Why the stages are ordered this way. What breaks when you skip the discipline.

- This reader moves faster than the Book 1 reader. Do not over-explain mechanics they already know.
- Trust them with nuance. They can handle "this works, and here is where it breaks."
- The frustration to acknowledge is not chaos — it is ceiling. They have hit the limit of what one agent can do and they know it.
- Do not hedge. Name the tradeoffs directly.

---

## What This Book Argues

Every chapter serves this thesis:

> A single AI agent is a capable individual contributor. It cannot manage complexity at scale. The solution is not a smarter prompt — it is a team: specialized roles, shared memory, and a workflow that coordinates them.

Let the thesis surface in the design decisions, not as a lecture. Show the reader a pipeline that works and make visible why each component is necessary.

---

## The Tone Difference from Book 1

Book 1 says: *You have been skipping the discipline. Here is why that matters and how to apply it.*

Book 2 says: *You have the discipline. Here is how to build a system that applies it at scale.*

Book 1 earns trust by showing the reader they have been doing something wrong. Book 2 earns trust by showing the reader something they could not have built without the groundwork they already have.

Do not be condescending about basics. Do not re-explain what a context window is. Do not define "agent" as if the reader has never used one.

---

## What to Avoid

- **Basics re-explained**: This reader knows what a prompt is. Do not define it.
- **Hype about scale**: Do not describe what is theoretically possible. Show what the reader can build today.
- **Over-qualification**: Do not hedge every claim with "it depends." Make the point, then note the genuine exceptions.
- **Framework comparisons**: Do not compare what the book teaches to LangChain, CrewAI, or any other framework. This is not a comparison exercise.
- **Apologizing for limits**: Chapter 6 covers what you cannot trust. Everywhere else, do not apologize. The system works. Name it accurately.

---

## Callout Boxes

Same conventions as Book 1, plus one addition:

- `> **Antigravity:**` — Antigravity-specific steps. All harness instructions go here. The surrounding prose must read coherently without this callout for spin-off editions.
- `> **What the Agent Will Do:**` — before autonomous action, so the reader knows what to expect
- `> **Watch For:**` — when a specific output confirms the stage ran correctly
- `> **Key Takeaway:**` — one sentence; the thing the reader must leave the chapter knowing

The `> **Antigravity:**` callout is the primary addition over Book 1. It enforces the concept/harness separation that makes spin-off editions possible. Every UI path, every prompt format, every Manager View instruction lives inside one of these callouts — never in the main prose.

---

## Chapter Endings

One sentence. Not a summary. The principle the reader just experienced, and the door to what comes next.

Example: "Now that the researcher and the writer are separate, you need someone who reads the result the way your audience will — and finds what neither of them saw."
