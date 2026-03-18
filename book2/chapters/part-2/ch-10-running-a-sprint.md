# Chapter 10: Running a Sprint

Load `skills/feature-sprint.md`. You are going to run `git-summary` from requirement to documented code.

This chapter is a walkthrough, not a tutorial. You have done every step before — you built all the roles, you built the coordinator, you know what each stage produces. What you have not done is run them together. That is what this chapter is.

---

## Stage 1: The Planner

Open a new session. Load the feature sprint coordinator. The coordinator will tell you to start with the Planner.

```
[paste full contents of skills/feature-sprint.md]

Ready to begin Stage 1.
Topic: git-summary
```

> **Antigravity:** Start a **New Session**. Paste the full contents of `skills/feature-sprint.md`, then a blank line, then "Ready to begin Stage 1. Topic: git-summary". The agent will load the Planner role and begin producing `plan.md`.
>
> **Watch For:** Structured output in the format specified in `agents/planner.md`: an Implementation approach section, Data structures, Edge cases and decisions, and Out of scope. The plan should address at minimum: what happens with fewer than 5 active files, what the tool does when the git command is not available, how "most recent commit message" is determined when a file has multiple commits in the period, and what constitutes a "valid git repository."

When `plan.md` is ready, stop. Read it before proceeding. This is the mandatory gate.

---

## The Mandatory Gate

Read `plan.md` against `requirement.md`. Work through the checklist:

**Does every requirement statement have a plan decision?**
The requirement specifies "Top 5 most-modified files." The plan should say what happens if fewer than 5 files were modified — does it show fewer, does it pad with zeros, does it show all files up to 5? If the plan does not specify, add it now.

**Are edge cases handled?**
What does the tool do if the repository has no commits in the period? What if the `--days` flag is 0? What if the path exists but is not a git repository? Each of these should be in the plan's Edge cases section.

**Is the Out of scope section explicit?**
The requirement's Out of scope list should appear in the plan, unchanged. If the Planner added anything, check whether you agree.

**Do you agree with the decisions?**
This is the judgment call only you can make. If the Planner decided that fewer than 5 files shows a "No activity found" message instead of the files that do exist — is that what you want? Change the plan now if not.

> **Antigravity:** Save the Planner's output as `plan.md`. Read it thoroughly. Add or adjust any decisions before proceeding. The plan is the spec from here.

When you are satisfied with `plan.md`, confirm to the session that Stage 1 is complete and Stage 2 is beginning. Use the exact transition message: `Stage 1 complete. Proceed to Stage 2.`

---

## Stage 2: The Implementer

> **Antigravity:** In the same session, paste the full contents of `requirement.md` and `plan.md`, then instruct the agent to proceed to Stage 2. It will load the Implementer role and produce `git_summary.py`.
>
> **Watch For:** Python code that references only the standard library. The implementation should follow the plan's data structures and approach. If the Implementer adds error handling beyond what the plan specified, or imports a library not in the standard library, note it — that is a scope violation the Reviewer will flag.

Save the output as `git_summary.py`. Read it once before proceeding to Stages 3 and 4.

---

## Stages 3 and 4: Running in Parallel

Stages 3 and 4 are independent — the Reviewer and Tester both need `git_summary.py` but not each other's output. This is where running two simultaneous sessions pays off.

What "parallel" means here is simple: both stages start from the same implementation file, but in separate contexts. They do not share memory, they do not wait on each other, and neither stage can silently bias the other. Each produces its own artifact. Stage 5 begins only after you have both.

> **Antigravity:** Click the grid icon (upper right) to open **Manager View**. You will see your current session as a card. Create a second agent card by clicking the **+** or **New Agent** button on the canvas.
>
> You now have two agent cards. In Card 1, load `agents/reviewer.md` and paste `requirement.md` and `git_summary.py`. In Card 2, load `agents/tester.md` and paste `requirement.md` and `git_summary.py`. Send both. They will run simultaneously.
>
> **Watch For:** Card 1 producing `review-notes.md` in the structured format (Correctness, Missing handling, Scope violations, Simplicity findings). Card 2 producing test code and a `test-report.md`. Neither card should be producing output that depends on the other.

If you prefer to run sequentially — one session for the Reviewer, then a second for the Tester — the output will be identical. Parallel is faster; sequential is simpler. Use whichever you are comfortable with.

Wait for both cards to complete before proceeding.

---

## Reading the Outputs

Before Stage 5, read both outputs together.

**From the Reviewer:** Are the findings located? Does each one cite a specific line or function? If the Reviewer produced general impressions ("this could be clearer"), the role constraint did not hold. Set that finding aside and act only on the located ones.

**From the Tester:** Which tests passed on first run? Which failed? For the failing tests: is the failure because the implementation is wrong, or because the test's assertion is wrong? Both are useful information. A test that fails because the implementation misses an edge case identified in the plan is a correctness failure. A test that fails because the tester wrote an assertion that contradicts the requirement is a test failure — fix the test, not the code.

Save `review-notes.md`, `test-report.md`, and `test_git_summary.py`.

---

## Stage 5: Addressing Findings

> **Antigravity:** Open a new session (or return to your Stage 2 session if the context is still clean). A session is still clean if it has only the Stage 2 exchange in it and the agent is still following the original implementation scope without commentary drift. Load `agents/implementer.md`. Paste `git_summary.py`, `review-notes.md`, and `test-report.md`. Instruct the agent to fix the correctness issues and failing tests.
>
> **Watch For:** Changes that are targeted — fixes for the specific issues raised, not rewrites of working sections. If the Implementer rewrites a section that had no findings, it has stepped outside its scope. Note it; that is scope drift.

When the revised `git_summary.py` is ready, run the tests again yourself. If the tester wrote `unittest` tests, run `python -m unittest test_git_summary.py`. If the tester wrote `pytest` tests and `pytest` is available in your environment, run `pytest test_git_summary.py` instead. They should pass. If they do not, the Stage 5 Implementer missed something — run Stage 5 again with the updated test output.

Check the optional gate: tests pass, review findings resolved, no new scope violations introduced. If yes, proceed.

---

## Stage 6: The Documenter

> **Antigravity:** Open a new session. Load `agents/documenter.md`. Paste `requirement.md`, the final `git_summary.py`, and `test-report.md`. Let the Documenter produce `README.md`.
>
> **Watch For:** A README with all required sections, including "What it does not do." The limitations should match the requirement's Out of scope section. If the test report showed a failing test that was not resolved, the README should note that limitation.

Save `README.md`. Read it as a user who has not seen the requirement or the implementation.

---

## What Just Happened

You ran six stages across five roles. The Planner filled the requirement's gaps before code was written. The Implementer built exactly what the plan specified. The Reviewer found the implementation issues the Implementer could not see from inside the code. The Tester confirmed which requirements were met with objective checks. The Implementer fixed what was found. The Documenter described the result for someone who was not in the room.

Each stage did one thing. Each handoff was a structured file. The coordinator held the sequence. The mandatory gate caught the underspecification before it became wrong code.

That is the pipeline. One more chapter to close the loop.

---

> **Key Takeaway:** Running the pipeline is following the sequence the coordinator defines, reading each output before confirming the next stage, and trusting that specialized roles produce better results than one agent doing everything — because you have now seen both.
