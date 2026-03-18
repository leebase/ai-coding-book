# Chapter 4: Voice and Sequence

You now have three roles: a researcher, a writer, and an adversarial reader. Each one does its job. What you do not have yet is a team.

A collection of roles is not a team. A team has a shared register — it sounds like it came from the same place. A team has a sequence — each member knows what they receive and what they hand off. A team has a coordinator that enforces both.

This chapter builds two things: a voice constraint that gives your team a shared register, and a pipeline coordinator that sequences the stages in the right order every time. After this chapter, you have a team. Chapter 5 is where you run it.

---

## Why Voice Drifts

Each role you have built so far runs in its own session. The researcher's session has no knowledge of the writer's session. The writer's session has no knowledge of the adversarial reader's session. They share the research notes and the draft as files, but they do not share a register.

Register is the combination of tone, formality, sentence rhythm, and assumed relationship to the reader. When different sessions produce different parts of the same article, the register shifts — subtly, in ways that do not cause obvious errors but cause the finished piece to feel like it was assembled rather than written. The introduction sounds direct; the middle section sounds cautious; the conclusion sounds like a different article entirely.

You can add "write in a direct, developer-facing tone" to every prompt. That instruction will be interpreted differently by every session. What you need is a single, specific voice definition that every stage loads before it starts — a constraint, not a suggestion.

---

## Building `skills/voice.md`

Voice is not a style preference. It is a set of specific constraints that apply to every word the writer produces. The constraints answer questions that "write with a direct tone" leaves open:

- Who is the reader, and what do they already know?
- What is the relationship between writer and reader?
- What sentence structures are preferred? What are off-limits?
- What does "specific" mean in practice for this audience?

Create `skills/voice.md`. Here is a starting definition you will adapt:

```markdown
# Skill: Voice

## The Reader
A developer who has shipped code. Comfortable with tools.
Not a beginner. Has run into the problem this article addresses.
Does not need to be convinced the problem is real.

## The Register
Peer-to-peer. Write as a developer talking to another developer
who is slightly behind on this specific thing. Not a teacher.
Not a consultant. Someone who figured this out and is sharing it directly.

## Constraints
- Short sentences when the point is sharp.
  Expand only when the concept requires it.
- Specific examples over general principles wherever possible.
- Name the problem before offering the solution.
- No hedging. If something is true, say it.
- No throat-clearing. Start with the point.

## What to Avoid
- Academic register: "it can be observed that" → "notice that"
- Cheerleading: do not tell the reader how useful this will be
- False precision: do not use numbers or statistics you cannot source
- Generic examples: if the example could apply
  to anything, it applies to nothing
```

> **Antigravity:** Create `skills/voice.md` in your project directory. Paste the definition above, adjust the reader description to match your intended audience, and save it.

This file will be loaded at the start of every stage that produces prose. It does not change what the stages do — it changes what register they do it in.

---

## Why Sequence Matters

The roles you have built have dependencies. The writer depends on `research-notes.md`. The adversarial reader depends on `draft.md`. If you run the writer before the researcher is done, the writer has nothing to work from. If you run the adversarial reader before the draft exists, the same problem.

These dependencies are obvious. The less obvious constraint is this: earlier stages change what later stages can do. If the researcher runs without the voice constraint loaded, its output will be in whatever register the base model defaults to. The writer will have to translate that register, introducing inconsistency. If the adversarial reader runs before the draft has been voice-checked, it will find register problems mixed in with content problems — and the feedback will be harder to act on.

Sequence is not just about prerequisites. It is about what each stage can reasonably be asked to produce given what preceded it.

---

## Building `skills/article-pipeline.md`

The coordinator skill defines the stages, their order, what each stage receives, and what each stage produces. It is a playbook. When you load it at the start of a session, the AI knows what stage it is on, what role to adopt, what input to expect, and what output to produce.

Create `skills/article-pipeline.md`:

```markdown
# Skill: Article Pipeline

This skill coordinates writing one article. Load it at the
start of a session and follow the stages in order.
Do not proceed to the next stage until the current one is complete.

## What You Need to Start
- A topic and a target reader
- `skills/voice.md` loaded and available
- An empty project directory for this article

---

## Stage 1: Research

Role: load `agents/researcher.md`
Input: topic + research question
Output: `research-notes.md` (grounded, plausible, uncertain claims)

Produce research notes only. Do not write prose.

---

## Stage 2: Draft

Role: load `agents/writer.md` and `skills/voice.md`
Input: `research-notes.md`
Output: `draft.md`

Write from the Grounded and Plausible claims only.
Apply the voice constraints throughout.
Do not add examples or claims not present in research-notes.md.

---

## Stage 3: Adversarial Read

Role: load `agents/adversarial-reader.md`
Input: `draft.md`
Output: `reader-notes.md`

Find located gaps. No style feedback. No rewrites.

---

## Stage 4: Revise

Role: load `agents/writer.md` and `skills/voice.md`
Input: `draft.md` + `reader-notes.md`
Output: `final.md`

Address each located gap in reader-notes.md.
Minimal targeted changes. Do not rewrite sections
that do not have a located problem.

---

## ⛔ Gate (Optional)

You may stop after any stage to review the output before
proceeding. Stopping after Stage 1 (before writing begins)
is the most valuable gate — it is the last moment to catch
a research problem before prose is built on top of it.
```

> **Antigravity:** Create `skills/article-pipeline.md`. Paste the coordinator above. Save it.

You will notice Stage 2 references `agents/writer.md` — a role you have not built yet. Add it now: a simple role that receives research notes and voice constraints and produces a draft. The writer role does not need to be complex; the researcher and adversarial reader are doing the heavy lifting. The writer's constraint is straightforward: use the research notes, use the voice, produce prose.

```markdown
# Agent: Writer

You receive research-notes.md and skills/voice.md.
You write a draft article using only the claims in the
Grounded and Plausible sections of the research notes.
You apply the voice constraints throughout.
You do not add examples or claims not present in the research notes.
You produce draft.md.
```

> **Antigravity:** Create `agents/writer.md` with the role definition above. Save it.

---

## Two Kinds of Files

You now have four files in your project directory:

```
agents/researcher.md
agents/writer.md
agents/adversarial-reader.md
skills/voice.md
skills/article-pipeline.md
```

They look the same — markdown files with instructions — but they do two different things.

**Agent files define a role.** `agents/researcher.md` tells the AI who it is for one stage: what it receives, what it produces, what it is not allowed to do. It is a specialist identity, adopted for the duration of a stage and then set aside. Every stage in your pipeline uses an agent file.

**Skill files define a rule that persists.** There are two kinds: `skills/voice.md` is a shared constraint — a set of specific instructions loaded by every stage that produces prose. It does not define a stage; it shapes what all stages do. `skills/article-pipeline.md` is a coordinator — it defines the full sequence, which stage comes next, which agent role to adopt, and what each stage hands off. It does not do any of the work; it tells you who does.

The directory names are not decorative. When you see `agents/`, you are looking at a role — a job that gets done once at a specific point. When you see `skills/`, you are looking at a durable rule that either coordinates the whole sequence or applies throughout it.

This distinction will matter more as your teams grow. A new role becomes a new agent file. A new coordination sequence becomes a new skill file. You will never put a coordinator in `agents/` or a role definition in `skills/`.

---

## The Gate

The coordinator includes an optional gate after Stage 1. This is the most important stopping point in the pipeline: the moment before writing begins, when the research is committed and the voice is loaded, but no prose exists yet.

If the research notes look thin, or the voice definition feels wrong for the topic, stopping here is cheap. Stopping after Stage 3 — after the adversarial reader has run — costs a full draft. Stopping after Stage 4 costs a revision. The earlier you catch a problem, the less work you discard.

Whether to stop at the gate depends on how well you know the topic and how much you trust the researcher's output. For familiar topics with a mature researcher role, running the full pipeline without stopping is reasonable. For new topics or new audiences, the Stage 1 gate is worth taking.

This is the same calibration question you will face with every pipeline you build. More on it in Chapter 6.

---

> **Key Takeaway:** A coordinator turns a collection of roles into a pipeline. Sequence is a constraint, not a preference — and voice is a constraint you define before writing starts, not a style that emerges during it.
