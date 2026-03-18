# Chapter 5: Run the Pipeline

You have everything you need.

A researcher that commits to what it knows before writing begins. An adversarial reader that finds the gaps the writer cannot see. A voice constraint that applies the same register to every stage. A coordinator that sequences the whole thing and holds the gate.

This chapter has one job: run it.

---

## The Run

Load `skills/article-pipeline.md` in a new agent session. The topic is the same one you used in Chapter 1. This run will produce new versions of `research-notes.md`, `draft.md`, and `reader-notes.md` — these will replace the files from Chapters 2 and 3, which served their purpose as practice. That is expected.

```
Topic: How to write documentation your future self will actually use
Target reader: Developers who have written documentation that became
useless within six months
```

Follow the stages in the coordinator. At each stage, let the role complete before moving to the next. Use the optional Stage 1 gate — read the research notes before the writer starts. If anything in the notes looks uncertain, address it before prose exists.

> **Antigravity:** Start a **New Session**. Paste the full contents of `skills/article-pipeline.md` at the start, then add the topic and target reader above. The agent will walk through the stages. At Stage 1, read `research-notes.md` before confirming it should proceed to Stage 2. When you are ready, type: `Stage 1 complete. Proceed to Stage 2.` At subsequent stages, let the pipeline run.
>
> **Watch For:** The stages producing distinct outputs — research notes that stay in the structured format, a draft that stays within the research notes' claims, adversarial feedback that is located and specific, a final article that differs from the draft only at the located gaps. If stages blend — if the writer starts adding new claims, or the adversarial reader starts rewriting — the coordinator did not hold. Note where it broke; Chapter 6 addresses this directly.

When `final.md` is ready, read it once through. Save a copy as `article-v2.md` — this is the artifact you will compare against `article-v1.md`. Like `article-v1.md`, leave it unchanged after saving so the comparison stays honest.

> **Antigravity:** Copy the content of `final.md`. Create a new file in your project directory named `article-v2.md`. Paste the content and save. Do not keep editing `article-v2.md` after that; it is your comparison artifact.

Then open `article-v1.md` — the article you saved in Chapter 1.

---

## The Comparison

Place both articles side by side. Read them on the same five dimensions you noted your first impressions against in Chapter 1:

> **Antigravity:** Open both `article-v1.md` and `article-v2.md` in the editor pane. If your editor uses tabs, switch between them as you compare. You are not looking for perfect prose; you are looking for visible differences you can name.

**Voice.** Does `article-v1.md` have a consistent register throughout? Does `article-v2.md`? Can you tell where in `article-v1.md` the tone shifts? Can you find a shift in `final.md`?

**Examples.** Pick one example from each article. For the `article-v1.md` example: could it have come from anywhere, or is it specific to a real situation? For the `article-v2.md` example: is it in `research-notes.md`? Can you trace it to a grounded claim?

**Misconception.** Does `article-v1.md` address something a developer actually gets wrong about documentation — a specific wrong belief — or does it explain what good documentation looks like? Does `final.md` do the same? Is the difference visible?

**Silent gaps.** Find one place in `article-v1.md` where a reader without background might lose the thread without knowing it. Now find the same kind of place in `article-v2.md`. Were the gaps in `article-v2.md` smaller? Were they in different places?

**Send test.** Read the conclusion of each article. Which one would you send to a colleague who asked you "how do I write better documentation"? Why?

The comparison is the argument this book has been building. Not "the pipeline produces better output" — you can see whether it does. What you should be able to name now is *why*: which stage produced which quality. The grounded examples came from the researcher. The addressed gaps came from the adversarial reader. The consistent voice came from the voice constraint. The fact that those things exist in sequence, each building on the last, came from the coordinator.

---

## What the Skills Produced

The five qualities you just evaluated each trace back to a specific design decision:

**Consistent voice** — `skills/voice.md` loaded at every prose-producing stage. Not a prompt instruction that gets interpreted differently each time. A shared constraint that applies to every word.

**Grounded examples** — `agents/researcher.md` separating the commitment to what is known from the act of writing. The writer cannot add a claim the researcher did not commit to.

**Addressed misconception** — the researcher role was given a research *question*, not just a topic. "What do developers actually get wrong?" produces different output than "write about documentation." The question aimed the research.

**Located gaps closed** — `agents/adversarial-reader.md` finding specific places, not general impressions. The writer addressed those places, not a vague directive to "be clearer."

**Sequence** — `skills/article-pipeline.md` ensuring the researcher ran before the writer, and the adversarial reader ran after the draft. The coordinator is not adding capability; it is preventing the capability that exists from being wasted by running in the wrong order.

---

## What the Pipeline Cannot Guarantee

The pipeline ran. The output is better than Chapter 1's in the specific ways the design intended. It is not perfect.

Look at `article-v2.md` again. Is there a place where the adversarial reader's feedback was correct but the revision did not quite close the gap? Is there a claim in `research-notes.md`'s Plausible section that made it into the final article in a way that feels shakier than the Grounded claims? Did the voice hold perfectly, or did one section drift?

You are not looking for failures. You are calibrating your trust. The pipeline produces consistent improvement, not guaranteed quality. The gap between those two things is what the next chapter is about.

---

> **Key Takeaway:** Each quality in the final article traces back to a specific role. That traceability is what a team gives you that one agent cannot — not just better output, but output you can understand and improve.
