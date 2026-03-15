# Chapter 9: The Feature Skill

You have five roles and a requirement document. What you do not have is a coordinator that sequences them, defines what each stage receives, and holds the gate before implementation begins.

That is `skills/feature-sprint.md`. This chapter builds it.

---

## What the Coordinator Does

In Part 1, `skills/article-pipeline.md` did three things: it defined the stages in order, it specified the input and output of each stage, and it held an optional gate before writing began.

`skills/feature-sprint.md` does the same three things for a coding workflow — with one addition. In the coding pipeline, the gate after the Planner stage is not optional. It is mandatory.

Here is why: in the article pipeline, a weak research notes file produces a weaker article. That is recoverable — you revise the article, you do not throw away the draft. In the coding pipeline, a weak plan produces an implementation that does not match what the Reviewer and Tester are checking against. When the tests fail or the review surfaces mismatches, the Implementer runs again from scratch. The work is not recoverable — it is redone. The gate prevents that.

Every other gate in the feature sprint is optional, following the same calibration from Chapter 6: use it when you need it, skip it when you don't.

---

## Building `skills/feature-sprint.md`

Create `skills/feature-sprint.md`:

```markdown
# Skill: Feature Sprint

This skill coordinates implementing one feature from requirement
to documented, tested code. Load it at the start of a session
and follow the stages in order.

## What You Need to Start
- requirement.md — complete and reviewed
- agents/ directory with all five role files
- An empty implementation directory

---

## Stage 1: Plan

Role: load `agents/planner.md`
Input: requirement.md
Output: plan.md

Turn the requirement into a specific implementation plan.
Fill every gap. Specify every edge case decision.
If the requirement cannot be planned against, stop and report
what is missing. Do not proceed to Stage 2 without a complete plan.

---

## ⛔ Gate — Required

Stop here. Review plan.md before proceeding.

Check:
- Does every requirement statement have a corresponding plan decision?
- Are all edge cases from the requirement handled in the plan?
- Is the Out of scope section explicit?
- Do you agree with the Planner's decisions?

Do not proceed to Stage 2 until this gate is confirmed.
A bad plan produces work that gets thrown away.

---

## Stage 2: Implement

Role: load `agents/implementer.md`
Input: requirement.md, plan.md
Output: git_summary.py

Implement exactly what the plan specifies.
Do not add features not in the plan.
Do not write tests.

---

## Stage 3: Review (runs in parallel with Stage 4)

Role: load `agents/reviewer.md`
Input: requirement.md, git_summary.py
Output: review-notes.md

Read the code against the requirement.
Produce located findings only.

---

## Stage 4: Test (runs in parallel with Stage 3)

Role: load `agents/tester.md`
Input: requirement.md, git_summary.py
Output: test_git_summary.py, test-report.md

Write and run tests that verify the requirement.
Report all results — passing and failing.

---

## Stage 5: Address Review and Test Findings

Role: load `agents/implementer.md`
Input: git_summary.py, review-notes.md, test-report.md
Output: git_summary.py (revised), updated test results

Fix correctness issues and failing tests from Stages 3 and 4.
Do not add features. Do not refactor beyond what fixes require.
If a review finding and a test failure point to the same issue,
fix it once.

---

## ⛔ Gate — Optional

Review the revised code and updated test results before documenting.
If tests still fail, return to Stage 5.
If review findings were not addressed, return to Stage 5.
Proceed to Stage 6 only when tests pass and review findings are resolved.

---

## Stage 6: Document

Role: load `agents/documenter.md`
Input: requirement.md, git_summary.py, test-report.md
Output: README.md

Write documentation for a developer who has not seen the requirement.
Include what the tool does not do.

---
```

> **Antigravity:** Create `skills/feature-sprint.md`. Paste the coordinator above. Save it.

---

## Stages 3 and 4: Parallel

The coordinator marks Stages 3 and 4 as running in parallel. In the article pipeline, every stage ran sequentially — each one used the previous stage's output as its input. In the coding pipeline, the Reviewer and Tester both receive the same input (`git_summary.py`) and produce independent outputs. Neither needs to wait for the other.

Running them in parallel is not a requirement — you can run them sequentially. But it is an option, and Chapter 10 shows you how to take it using Antigravity's Manager View. For now, note the dependency structure in the coordinator: Stage 5 needs both `review-notes.md` and `test-report.md`, so it cannot start until both Stages 3 and 4 are complete.

---

## The Mandatory Gate

Reread the gate between Stages 1 and 2. It is not marked optional. The checklist is specific:

- Does every requirement statement have a corresponding plan decision?
- Are all edge cases handled?
- Is the Out of scope section explicit?
- Do you agree with the decisions?

That last question matters. The Planner made decisions to fill the requirement's gaps. Those decisions are now part of the spec. If you disagree with them — if you think the Planner's edge case handling is wrong, or its Out of scope decisions are too conservative — the place to address that is here, not after the Implementer has run.

After Stage 1 is the last cheap moment. Everything after it is built on the plan.

---

> **Key Takeaway:** The coordinator sequences the team and holds the gates. The mandatory gate after Stage 1 is the most important line in the whole skill file — it is the last cheap moment before work that cannot be recovered.
