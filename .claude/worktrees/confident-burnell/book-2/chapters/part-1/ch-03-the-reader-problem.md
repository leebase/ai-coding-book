# Chapter 3: The Reader Problem

You wrote the draft. You read it back. It makes sense.

Here is what that means: it makes sense to you. You generated it. You know what each section is trying to say. You filled the gaps automatically as you read because you already had the context to fill them. The prose is coherent to the person who produced it, which is the least useful measurement of whether it will be coherent to someone who didn't.

This is not an AI problem. Human writers have the same blind spot. AI makes it worse because the agent writes from a position of maximal context — it generated every preceding paragraph, it knows exactly where the piece is going, it has no experience of arriving at this text cold. When it reads back what it wrote, nothing is unclear. That guarantees nothing about whether it will be unclear to you.

The solution is a role whose job is to not know what you know.

---

## Writing From the Research Notes

Before you can test the draft against a reader, you need a draft. Open a new agent session and give it the contents of `research-notes.md` along with this instruction:

```
Using only the claims in the Grounded and Plausible sections
of these research notes, write a 900-word article draft titled
"How to write documentation your future self will actually use."
Write for developers. Use the Grounded claims as the backbone.
Use Plausible claims only where they support a Grounded claim.
Do not add examples or claims that are not in these notes.
```

> **Antigravity:** Start a **New Session**. Paste the full contents of `research-notes.md` first, then add a blank line, then add the instruction above. Send it. The agent will write a draft using only what the researcher committed to.
>
> **Watch For:** The draft should stay closer to the research notes than the Chapter 1 article did. If the agent adds new examples that were not in your notes, it has stepped outside its instructions. Note where that happened — it is the same confabulation pattern from Chapter 2, now visible because you have the notes to compare against.

Save the output as `draft.md`. This is a working draft, not a final article. It does not need to be polished. It needs to be complete enough for the next step.

---

## The Gap That Writing Creates

Read `draft.md` once. Now ask yourself: if you arrived at this article having never thought about the documentation problem before, would every paragraph follow from the previous one? Would you understand the examples without background? Would you know what the first section assumed you already knew?

You probably cannot answer those questions accurately. Not because you are a poor reader — because you are the wrong reader. You have the context. Gaps in a text are invisible to the person who filled them while writing.

This is structural, not stylistic. You can edit a draft for clarity and still not see the gaps, because editing from the writer's perspective does not change whose context you are reading with. The only way to find the gaps is to read with someone else's context — or to build a role that simulates not having yours.

---

## Building `agents/adversarial-reader.md`

Create a new file: `agents/adversarial-reader.md`. The adversarial reader has one job: arrive at the draft cold and report where the experience breaks down.

This role is not an editor. It does not improve the prose. It does not suggest rewrites. It finds places where a reader without the writer's context would lose the thread — and reports them as specifically as possible: where in the draft, what assumption was made, what the reader would need to know that the draft does not provide.

Here is what `agents/adversarial-reader.md` should say:

```markdown
# Agent: Adversarial Reader

You are reading this draft for the first time.
You do not know what the writer was trying to say.
You only have the words on the page.

Your job is to find where the reader's experience
silently breaks down — not where the prose is rough,
but where a reader without context would lose the
thread and not know they'd lost it.

For each problem you find, report:
- Location: where in the draft (quote the sentence or phrase)
- Problem: what assumption the text makes that the reader may not share
- Impact: what the reader will do wrong or misunderstand as a result

Do not suggest rewrites. Do not give style feedback.
Find the silent gaps and name them precisely.
```

> **Antigravity:** Create `agents/adversarial-reader.md` in your project directory. Paste the role definition above. Save it.

---

## Running It

Open a new agent session. Load the adversarial reader role, then give it `draft.md` to read:

```
[paste full contents of agents/adversarial-reader.md]

---

[paste full contents of draft.md]
```

> **Antigravity:** Start a **New Session**. Paste the full text of `agents/adversarial-reader.md`, then a blank line with `---`, then the full text of `draft.md`. Send it.
>
> **Watch For:** A list of located problems — each one citing a specific place in the draft, a specific assumption, and a specific impact. If the output is general ("this section could be clearer"), the role constraint did not hold. Add this line to the role definition and run it again: "Do not give general feedback. Every item must cite a specific sentence or phrase."

Read each item the adversarial reader found. For each one, notice whether your reaction is "yes, that's a real gap" or "that's obvious, any reader would know that." The second reaction is the signal — it means you knew something the reader did not, and you did not know you knew it. That is the gap the role was designed to find.

Save the adversarial reader's output as `reader-notes.md`.

---

## Addressing the Gaps

Go through `reader-notes.md` and fix the located gaps in `draft.md`. Not a rewrite — targeted additions. Each gap the adversarial reader found needs either a sentence of context or a more grounded example. Nothing more.

> **Antigravity:** Open `draft.md`. For each item in `reader-notes.md`, make the specific, minimal change that closes the gap. Save the updated file.
>
> **Watch For:** Fixes that are one or two sentences, not paragraphs. If you find yourself rewriting a whole section to address one gap, the gap was structural — the section was missing a foundation, not just a clarification. Note it; that kind of gap is worth understanding.

When you are done, you have a draft that was written from grounded research and has been read by someone who did not share your context. That is a different artifact than what Chapter 1 produced.

---

> **Key Takeaway:** Clarity is invisible to the person with context. You need a role whose entire job is to not have it.
