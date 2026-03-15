# Skill: Ebook Writer

This skill coordinates writing a chapter of the software engineering tutorial ebook. The book teaches SE discipline through hands-on work in the Google Antigravity app (free tier). Do not skip stages. Do not write prose before the outline is approved.

## The Team

Each stage adopts a specific role. Load the agent file to take on that role's perspective and constraints.

| Role | Agent File | Responsibility |
|------|-----------|----------------|
| se-educator | `agents/se-educator.md` | Defines the principle and learning objective |
| scenario-designer | `agents/scenario-designer.md` | Designs the hands-on Antigravity scenario |
| antigravity-expert | `agents/antigravity-expert.md` | Reviews and writes Antigravity instructions |
| script-writer | `agents/script-writer.md` | Drafts chapter prose |
| continuity-editor | `agents/continuity-editor.md` | Guards the ongoing project thread |
| confused-beginner | `agents/confused-beginner.md` | Adversarial read from a first-time reader |
| agentflow-architect | `agents/agentflow-architect.md` | Plants Part 2 seeds; connects principles to AgentFlow |

---

## What You Need to Start

- The SE principle or concept this chapter will teach
- Which part of the book this chapter belongs to (Part 1: SE discipline / Part 2: AgentFlow)
- The current state of the ongoing project the reader is building
- The chapter number and its place in the sprint plan

---

## Stage 1: Define the Principle

**Role**: se-educator
**Load**: `agents/se-educator.md`, `skills/tutorial-writer/tutorial-interpretation.md`
**Produce**: Principle Brief

- What is the SE principle being taught?
- Why does it matter *more* in the AI era, not less?
- What misconception does the reader arrive with?
- What is the one-sentence learning objective?
- What moment in the scenario makes the principle visible?

---

## Stage 2: Design the Scenario

**Role**: scenario-designer
**Load**: `agents/scenario-designer.md`, `skills/scenario-builder.md`
**Produce**: Scenario Brief

- What is the project state at the start of this chapter?
- What prompt does the reader give the Antigravity agent?
- What does the agent do autonomously?
- What does success look like?
- What does the failure path look like — what breaks down when the discipline is skipped?

---

## Stage 3: Continuity Check

**Role**: continuity-editor
**Load**: `agents/continuity-editor.md`
**Produce**: Continuity Notes

- Does this scenario require state from a previous chapter that was established?
- Does it leave the project in a state the next chapter can build from?
- Flag any discontinuities before prose is written.

---

## Stage 4: Plan the Chapter

**Role**: tutorial-planner
**Load**: `agents/tutorial-planner.md`, `skills/tutorial-writer/tutorial-planning.md`
**Produce**: Chapter Outline

Structure:
1. The principle — what it is and why it matters in the AI era
2. The scenario — what the reader will do in Antigravity
3. The walkthrough — step-by-step instructions
4. What goes wrong — the failure path
5. The debrief — connecting experience back to principle
6. Key takeaway — one sentence

---

## ⛔ GATE — Human Approval Required

Stop here. Present the Principle Brief, Scenario Brief, Continuity Notes, and Chapter Outline to the human.

Do not proceed to Stage 5 until the outline is explicitly approved. Revise the outline — not the prose — if changes are needed.

---

## Stage 5: Write the Chapter

**Role**: script-writer
**Load**: `agents/script-writer.md`, `skills/tutorial-writer/tutorial-writing.md`, `skills/tutorial-writer/tutorial-narrative.md`, `skills/antigravity-guide.md`, `skills/book-voice.md`
**Produce**: Chapter Draft

- Write for a reader, not a source archive
- Use Antigravity callout patterns: `> **Free Tier Note:**`, `> **What the Agent Will Do:**`, `> **Watch For:**`
- Every Antigravity instruction must have an exact UI path and observable output
- Never hide a missing fact behind smooth prose

---

## Stage 6: Antigravity Review

**Role**: antigravity-expert
**Load**: `agents/antigravity-expert.md`, `skills/antigravity-guide.md`
**Produce**: Instruction Review

- Is every UI path exact and followable?
- Is every prompt specific enough for a first-time user?
- Are free tier constraints noted where they apply?
- Does every step tell the reader what to observe?

---

## Stage 7: Adversarial Read

**Role**: confused-beginner
**Load**: `agents/confused-beginner.md`, `skills/tutorial-writer/learner-confusion-attack.md`
**Produce**: Confusion Report

- Where would a first-time reader get stuck silently?
- Does the failure path feel real or too tidy?
- Is the principle felt, or just stated?

---

## Stage 8: AgentFlow Annotation (Part 1) / Connection Check (Part 2)

**Role**: agentflow-architect
**Load**: `agents/agentflow-architect.md`
**Produce**: Bridge Notes

- Part 1: Where should AgentFlow be seeded or foreshadowed?
- Part 2: Is every AgentFlow concept grounded in a Part 1 pain point?

---

## Stage 9: Refine

**Role**: script-writer
**Load**: `agents/script-writer.md`, `skills/tutorial-writer/review-response.md`
**Produce**: Final Chapter

Address all findings from Stages 6, 7, and 8. Do not mark the chapter done until all blocking issues are resolved.
