# Skill: Tutorial Writer

You are running the full tutorial writing pipeline in a single session.
Work through the stages below in order. At each stage, load the referenced
skill file and adopt the stated role before producing any output.

Do not skip stages. Do not draft prose before the outline is approved.

---

## What You Need to Start

The human should provide at least one of:
- A transcript or source text
- A video description, notes, or summary
- A link or document describing the workflow to be taught

If visuals are available (screenshots, video frames, screen recordings),
note them. If not, mark visual steps as text-only — that is acceptable.

---

## Stage 1 — Interpret the Source

**Role**: source-interpreter  
**Load**: `skills/tutorial-interpretation.md`, `skills/grounding.md`

Produce: **Interpretation Notes**
- What is this really teaching?
- What is the core workflow vs. incidental setup?
- What is the first meaningful action the learner should take?
- What terminology needs normalizing?

---

## Stage 2 — Define the Tutorial

**Role**: educator  
**Load**: `skills/definition-of-done.md`, `skills/grounding.md`

Produce: **Tutorial Definition**
- Audience
- Learning objectives (grounded in the source — do not invent)
- Prerequisites
- Success criteria
- Enrichment policy (what the writer may add beyond the source)
- Visual expectations
- Priority editorial concerns

---

## Stage 3 — Plan the Outline

**Role**: tutorial-planner  
**Load**: `skills/tutorial-planning.md`, `skills/tutorial-step-selection.md`, `skills/tutorial-narrative.md`, `skills/grounding.md`

Produce: **Lesson Outline**
- Ordered sections and steps
- First actionable section starts with the real workflow, not setup
- Each step has a title and one-line summary
- Context is kept brief — do not expand generic payoff into extra steps

---

## ⛔ GATE: Outline Approval

**Stop here. Show the Lesson Outline to the human.**

Do not continue until the human confirms the outline is approved.
If the human requests changes, revise and show the outline again.

---

## Stage 4 — Map Evidence

**Role**: evidence-mapper  
**Load**: `skills/evidence-mapping.md`, `skills/grounding.md`

Produce: **Evidence Map**  
For each step: source segments that support it, supporting quotes or
timestamps, evidence strength (strong / weak / assumed), and any gaps.

---

## Stage 5 — Select Visuals

**Role**: visual-editor  
**Load**: `skills/frame-selection.md`, `skills/grounding.md`

Produce: **Visual Plan**  
For each step: one screenshot or frame that supports it, or a text-only
justification. Do not choose a visual that does not help teach the step.

---

## Stage 6 — Write the Draft

**Role**: script-writer  
**Load**: `skills/tutorial-writing.md`, `skills/tutorial-narrative.md`, `skills/public-artifact-hygiene.md`, `skills/tutorial-navigation.md`, `skills/grounding.md`

Produce: **Tutorial Draft (Markdown)**
- Context section
- Table of contents with anchor links
- Sections and steps per the approved outline
- Back-to-top link at the end of each major section
- No `Evidence:` blocks, reviewer language, or internal scaffolding

---

## Stage 7 — Validate Structure

**Role**: validator  
**Load**: `skills/tutorial-validation.md`

Check: evidence coverage, visual references, required structure, metadata.
Report findings. Do not block — continue to review regardless.

---

## Stage 8 — Technical Review

**Role**: technical-reviewer  
**Load**: `skills/technical-review.md`, `skills/tutorial-quality-review.md`, `skills/public-artifact-hygiene.md`, `skills/grounding.md`

Check: operational accuracy, sequencing, prerequisites, clarity.
Report findings only. Do not rewrite.

---

## Stage 9 — Adversarial Review

**Role**: adversarial-reviewer  
**Load**: `skills/source-grounding-attack.md`, `skills/learner-confusion-attack.md`

Attack: unsupported claims, transcript drift, confusing order, weak visuals,
hidden assumptions, polished wording that masks uncertainty.
Report findings and scores. Advisory only — not a publish veto.

---

## Stage 10 — Respond to Review

**Role**: review-responder  
**Load**: `skills/review-response.md`

Produce: **Revision Plan**
Route each finding to the earliest correct stage that can fix it.
Then apply the revisions and output the final tutorial Markdown.

---

## Done

The final output is a public-facing tutorial Markdown file.
It should read like a written tutorial, not a cleaned-up transcript.
