# The Thesis Guard Mission

## Mission

Test every chapter against the book's central argument: a single AI agent cannot manage complexity at scale; the solution is a team — specialized roles, shared memory, coordinated by a skill. Every chapter must serve this thesis. Documentation chapters are a failure. Argument chapters are a success.

## Scope

- **Per-chapter thesis test:** For each chapter, identify the specific thesis claim it advances. If you cannot state the claim in one sentence, the chapter is not making an argument — it is documenting a procedure.
- **Part 1 → Part 2 translation:** The book's structural claim is that the same coordination pattern applies to both content production and software development. Does Chapter 7 make this translation feel earned, or does it feel mechanical? Are the role analogies tight?
- **The comparison exercise as argument:** The book argues by demonstration. Does the Chapter 1 → Chapter 5 comparison constitute a real argument, or is it an exercise that produces "better in general" output?
- **Introduction promise audit:** What does the introduction promise? Does the book deliver each promise by the end?
- **Chapter endings:** Each chapter must close with the principle just demonstrated and the door to what comes next. Flag any chapter that ends with a summary instead.
- **Orphaned concepts:** Flag any concept introduced but not connected back to the thesis. The team metaphor must stay load-bearing throughout.

## Inputs

- All manuscript files in `book2/chapters/`
- `book2/skills/skill-thesis-coherence.md`
- `book2/product-definition.md` — the canonical thesis statement and success criteria

## Outputs

- Contributions to `book2/claude_says.md` (Thesis Coherence section)

## Review Rules

- The thesis is not "multi-agent coordination is useful." It is "the solution to the quality ceiling is a team." Every chapter must advance that specific claim.
- A chapter that teaches a technique without explaining why it is part of the team design is a documentation chapter. Flag it.
- The Part 2 mapping must be explicit: each Part 2 chapter should name what it is translating from Part 1 and why the translation is non-trivial.
- "Key Takeaway" callouts are thesis markers. Read them as a sequence — do they build an argument?

## Done Criteria

- Per-chapter thesis verdict included in `claude_says.md`.
- Part 1 → Part 2 translation quality verdict included.
- Introduction promise vs. delivery audit included.
