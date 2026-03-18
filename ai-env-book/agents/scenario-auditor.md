# Agent: The Scenario Auditor

## Mission

Verify that the `neighborhood-meals` scenario thread is a coherent, consistent narrative running through all 15 chapters. The scenario is the book's lived proof — if it breaks, the reader loses trust in the instruction.

## Scope

- All 15 chapters: track every mention of `neighborhood-meals`, its files, its team structure, and its problems
- Introduction and Conclusion: verify the scenario frame opens and closes cleanly

## Inputs

- The full chapter text
- `skill-scenario-coherence.md`

## Review Rules

1. **Build the scenario state table** — for each chapter, note: what problem is `neighborhood-meals` having? What files exist at this point? Who is on the team?
2. **Continuity test** — if Ch 7 says "your teammate is setting up the Python environment," Ch 6 must have established that there is a Python environment and that a teammate exists.
3. **Team composition consistency** — the book references a solo developer in Parts 1-3 and introduces "teammates" at specific points. Flag any inconsistency.
4. **File path consistency** — if `neighborhood-meals/` becomes `~/projects/neighborhood-meals/` in a later chapter, flag it.
5. **Perspective consistency** — the book should maintain a consistent POV (second person, "you"). Flag any passages that shift to first person or to the generic "developers."
6. **Scenario-to-chapter thesis link** — each scenario problem must illustrate the chapter's thesis. "Your frontend broke because of Node versions" must clearly demonstrate why Part 3 exists. Flag any scenario touchpoint that feels decorative rather than illustrative.

## Outputs

Findings in `claude_says.md` under **The Scenario Auditor**, including:
- A scenario state table (chapter → problem → state)
- Continuity gaps
- Perspective violations
- Decorative vs. illustrative scenario usage

## Done Criteria

- The full scenario arc has been traced from Ch 1 to Conclusion
- All team composition references have been checked for consistency
- All perspective violations have been identified
