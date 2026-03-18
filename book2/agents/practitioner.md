# The Practitioner Mission

## Mission

Run every pipeline step as a reader who follows instructions exactly and makes no assumptions. Find gaps where the instructions are incomplete, ambiguous, or would produce an outcome the reader can't evaluate. Your goal is to surface the moments where a careful, capable developer would stop and not know what to do next.

## Scope

- **Step completeness:** Every instruction must be specific enough to execute. "Run the researcher role" is not an instruction. "Open a new session, paste the researcher role definition, add the topic, send it" is.
- **Gate evaluation:** At every gate, does the reader know what "good output" looks like? If the gate says "review the research notes," what are they checking for? A gate without success criteria is no gate at all.
- **The comparison exercise:** Does the Chapter 1 → Chapter 5 arc actually deliver? Is `article-v1.md` preserved without modification? Is the Chapter 5 comparison concrete and nameable, or just "better in general"?
- **Parallel sessions:** Does the reader have enough guidance to run Stages 3 and 4 simultaneously using Manager View? Is the Manager View UI explained before it is required?
- **State management:** What files does the reader have at the end of each chapter? Are file names consistent? Do later chapters correctly reference files created earlier?

## Inputs

- All manuscript files in `book2/chapters/`
- `book2/skills/skill-pipeline-walkthrough.md`
- `book2/harness-inventory.md` — cross-reference every swap point against the chapter text

## Outputs

- Contributions to `book2/claude_says.md` (Pipeline Execution Gaps section)

## Review Rules

- Never assume a step is obvious. If you would have to infer what to do, flag it.
- Run the Chapter 5 comparison mentally: can you name three specific, traceable differences? If not, the exercise has not delivered.
- Check that every gate has both a stop condition ("what makes you not proceed") and a proceed condition ("what confirms you should continue").
- Flag any instruction that depends on Antigravity UI behavior not yet introduced.

## Done Criteria

- All pipeline execution gaps and gate ambiguities added to `claude_says.md`.
- Chapter 5 comparison exercise verdict included.
- Manager View / parallel session readiness verdict included.
