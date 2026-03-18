# Skill: Ceiling Audit

## Goal

Verify that every claim the book makes about the reliability, quality, and limits of document-driven coordination is accurate, specific, and honest — including claims made before Chapter 6.

## Directives

### 1. Failure Mode Recognition Test

- The four failure modes are: stage collapse, role drift, output variance, context accumulation.
- For each failure mode, ask: would a reader who has just experienced this recognize it from the description?
- "Stage collapse" must be specific enough that a reader knows what to look for when the coordinator blends two stages. Flag vague descriptions.
- Check whether any failure mode appears implicitly in earlier pipeline instructions (e.g., a coordinator that runs stages sequentially is susceptible to stage collapse from the first use). If so, flag the missed acknowledgment.

### 2. Pre-Chapter 6 Honesty Audit

- Read Chapters 1–5 and 7–11 for implicit reliability claims.
- Any time the text says the pipeline "produces" or "ensures" a quality outcome, test the claim: does the pipeline actually guarantee this, or does it make it more likely?
- "The researcher produces grounded claims" is a role instruction, not a guarantee. Flag any passage that presents role constraints as guarantees.

### 3. External Orchestration Accuracy

- Verify the five frameworks named in Chapter 6 (LangGraph, CrewAI, OpenAI Agents SDK, Symphony, Microsoft Agent Framework) are described with enough specificity to be useful.
- Are any descriptions that were accurate at writing time now outdated?
- Is Symphony described accurately? (It monitors Linear, creates isolated workspaces per issue, spawns agents through ticket lifecycle stages, built on Elixir/BEAM.) Flag any imprecision.
- Does the text recommend checking for current comparisons? (It should, given the fast-moving landscape.)

### 4. Quality Improvement Claim Grounding

- The book claims the pipeline produces "specific, traceable improvement." Identify where these specific improvements are named.
- Are the three named dimensions (voice, examples, addressed misconceptions) actually traceable to specific stages?
- Flag any improvement described as "better" without being tied to a stage output.

### 5. Gate Reliability Audit

- The gate is the book's "main quality instrument." Is this claim supported?
- Does the book teach the reader what to look for at each gate? A gate checklist with items the reader can evaluate?
- What does the gate not catch? (E.g., the gate cannot catch output variance between runs.) Is this acknowledged?
