# How To Start A New Book

> Use this when creating a new standalone book workspace in this repository.
>
> The goal is to prevent underbuilt scaffolding, missing review lenses, and
> process drift before drafting starts.

---

## Purpose

This guide exists because a new book should inherit the full sophistication of
the method, not just a blank directory and a few memory files.

The startup job is not only:

- create a folder
- create `context.md`
- create `sprint-plan.md`

The startup job is also:

- choose the right artifact set
- choose the right agent and reviewer stack
- choose the right voice layer
- choose the right process rules for this book's protagonist and stakes

If those decisions are not made up front, the draft will usually outrun the
scaffold.

---

## Startup Sequence

Do these in order.

### 1. Create the standalone workspace

Create the new book directory and at minimum add:

- `context.md`
- `result-review.md`
- `sprint-plan.md`
- `author-flow.md`
- `chapters/`

If the book is thesis-driven nonfiction, also plan for:

- thesis brief
- research support memo
- story bank or proof map
- framework notes
- positioning notes

Do not begin chapter drafting before the thinking artifacts exist.

### 2. Decide what kind of book this is

Name the protagonist and the pressure profile early.

Examples:

- consulting-firm book
- business-leader companion book
- personal handbook
- tutorial / instructional book
- memoir-adjacent argument book

This decision controls:

- the reviewer stack
- the voice layer
- the kinds of examples required
- the boundary rules

Do not inherit the previous book's reviewer set blindly.

### 3. Choose the correct base skills

At minimum, load the shared AuthorFlow layer:

- `skills/thought-leadership-book.md`

Then add the local book layer if needed.

Examples already in this repo:

- `skills/personal-empowerment-book.md`
- `skills/consulting-book-voice.md`
- `skills/sounds-like-lee.md`

If the new book has a distinctive voice, audience, or boundary profile and no
existing local skill covers it, create one immediately.

### 4. Build the role stack, not just one reviewer

Every serious book should explicitly support these core roles:

- `agents/thesis-architect.md`
- `agents/research-synthesizer.md`
- `agents/story-miner.md`
- `agents/positioning-editor.md`
- `agents/argument-writer.md`

Then add the reviewer stack that matches the book.

Examples:

**Consulting / business books**

- `agents/big-consulting-reviewer.md`
- `agents/mid-market-consulting-reviewer.md`
- `agents/independent-consultant-reviewer.md`
- `agents/enterprise-transformation-reviewer.md`
- `agents/business-unit-leader-reviewer.md`
- `agents/cfo-reviewer.md`

**Personal handbook books**

- `agents/human-empowerment-reviewer.md`
- `agents/reflective-working-adult-reviewer.md`
- `agents/practical-handbook-reviewer.md`
- `agents/skeptical-high-agency-reviewer.md`
- `agents/parenting-real-life-reviewer.md`
- `agents/meaning-and-identity-boundary-reviewer.md`

If the protagonist changes, the reviewer stack should usually change too.

### 5. Create any missing local skills or agents immediately

Do not wait until Chapter 5 to notice the workflow is too generic.

Create the missing layer as soon as you can name the gap.

Common gaps:

- local doctrine skill
- local voice skill
- local boundary-review skill
- local audience-review skill
- protagonist-specific reviewer agents

If a repeated correction is likely, promote it into a skill or reviewer file
instead of leaving it as a human memory burden.

### 6. Add the stack to the local workflow docs

Update:

- local `context.md`
- local `sprint-plan.md`
- local `author-flow.md`

Make the local process explicit:

- which skills this book uses
- which reviewers belong in the stack
- which review passes are required before calling a chapter done

If it is not written there, it is too easy to forget in the next session.

### 7. Add startup tasks to the sprint plan

Do not treat infrastructure as invisible setup.

Track these explicitly in Sprint 0 or Sprint 1:

- create local memory docs
- create local doctrine/voice skill if needed
- add book-specific reviewer agents
- decide the review stack
- choose the initial artifact set
- lock the canonical planning artifact

That keeps the scaffold visible and reviewable.

### 8. Add a voice and cadence rule early

Voice is not a late polish pass.

If the book has a distinctive cadence, create or link the skill early.

Examples:

- `skills/consulting-book-voice.md`
- `skills/sounds-like-lee.md`

Also decide whether the reviewer set needs to flag cadence anti-patterns such
as:

- stacked one-sentence paragraphs
- consultant-brand prose
- generic uplift language
- therapeutic fog

### 9. Define the review gates before prose gets deep

For a thesis-driven book, the minimum gates are usually:

1. thesis / concept gate
2. proof / story gate
3. positioning gate
4. voice and cadence gate
5. audience / persona review gate
6. handbook-value or practicality gate
7. boundary gate for sensitive material

Put these gates in the sprint plan before the middle of the manuscript exists.

### 10. Record the startup decisions in `author-flow.md`

Write down:

- what was inherited
- what was created new
- what review stack was chosen
- what gaps were noticed and fixed

That prevents the startup phase from being reconstructed inaccurately later.

---

## Minimum Definition Of Ready For Drafting

Do not draft chapters until these are true:

- the workspace has local memory files
- the canonical planning artifact is named
- the thesis is sharp enough to survive summary
- the proof and research layers exist in some usable form
- the local voice layer is chosen
- the reviewer stack is explicit
- the sprint plan includes review gates, not only draft tasks

If those are not true, keep building the scaffold.

---

## Anti-Patterns To Avoid

- Reusing the last book's reviewers without checking protagonist mismatch
- Creating one local reviewer and calling the stack done
- Drafting chapters before the voice layer exists
- Letting repeated corrections stay outside the process docs
- Treating cadence as polish instead of as part of authorship
- Assuming the shared AuthorFlow skill is specific enough on its own
- Forgetting to update `AGENTS.md` when the method evolves

---

## Startup Exit Checklist

Before calling startup complete, verify:

- local workspace exists
- local memory docs exist
- artifact set is chosen
- local skills exist or are deliberately not needed
- reviewer stack exists
- sprint plan tracks infrastructure tasks
- `author-flow.md` records the startup design
- `AGENTS.md` still matches the current method

If any of those are missing, startup is not done yet.
