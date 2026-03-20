# Chapter 14: Putting It All Together

This is what you have built across fourteen chapters:

A **development loop** with five stages: Start, Implement, Verify, Review, Update. Every session runs the loop. Every stage has a discipline behind it.

A **skill** (`start-session.md`) that encodes the Start stage, so each session begins informed rather than reconstructed from memory.

A **context file** (`context.md`) that holds project state separately from session instructions, updated at the end of every session, readable by any agent or developer picking up the project.

A **decision log** (`decisions.md`) that records what was decided, why, and what each decision rules out — the answer to "why does this code work this way?"

A **sprint cadence**: plan, execute, review, repeat. Each sprint has a goal, a dependency analysis, a parallelism decision, and an explicit definition of done.

**Autonomy calibration**: three factors (task definition, context maturity, test coverage) that determine whether the session runs Mode 1, 2, or 3.

**Multi-agent coordination** via Claude Code subagents: parallel agents when scopes are clean, serialization when they are not, human merge review before any session closes.

That is AgentFlow. Not a tool — a practice. These pieces work together, which is why the chapters were sequenced the way they were. Skills are only useful when you have a loop to invoke them in. Context files only matter when sessions are stateless. The sprint cadence only works when you have requirements discipline behind it.

---

## Choosing Your Next Feature

Look at your backlog — the features you explicitly excluded from previous sprints. Some of them are named. Some are implied. Here are four candidates from the task manager's natural next steps:

**Option A: Tag filter** — `list --tag work` shows only tasks with `--tag work`. Low risk. Follows the exact same pattern as `--priority` filter (Ch 11) and `--done` filter (Ch 13). Good Mode 2 candidate.

**Option B: Bulk done** — `done 1 2 3` marks multiple tasks done in one command. Medium risk. New argument parsing pattern (multiple IDs), but no schema change. Mode 1 or 2 depending on your test suite's ID-handling coverage.

**Option C: Edit description** — `edit 1 --description "new text"` changes a task's description. Medium risk. Mutation of existing data — no undo. The decisions.md precedent is that we do not ask for confirmation (see `clear`), but that decision needs to be applied consciously here. Mode 1.

**Option D: Import from CSV** — `import file.csv` reads a CSV file and adds tasks. Higher risk. File parsing, error handling for malformed files, ID assignment for imported tasks. Mode 1 with careful increments.

Choose the one that interests you. The system works on all of them. Avoid choosing something that would require major refactoring of `tasks.py` — the synthesis session should demonstrate the methodology working smoothly, not debugging a structural change. If you are unsure, Option A is the safest demonstration.

---

## Running the Full Session

This is a checklist, not a tutorial. You have done every step before. The point of this chapter is to do them all in sequence, consciously, as one system.

### Step 1: Write the sprint plan

Before opening Claude Code, create or update `sprint-plan.md`. Answer the five questions:
- What is the sprint goal? (one sentence)
- What features are in scope?
- What are the dependencies?
- Which tasks can run in parallel?
- What is "done" for this sprint?

Reference: Chapter 12.

### Step 2: Calibrate the autonomy mode

Apply the three-factor heuristic to your chosen feature:
- Task definition: tight requirement with existing pattern → higher autonomy. New behavior or schema → lower.
- Context maturity: is context.md current with your 20-test, 10-command state?
- Test coverage: do your tests cover the error cases this feature might produce?

Assign Mode 1, 2, or 3 before writing the first prompt.

Reference: Chapter 13.

### Step 3: Write the requirement

Before opening a new agent session, write the requirement for your feature:
- Specific input (exact command syntax)
- Specific output (exact format)
- Edge cases (what happens at the boundaries)
- Scope boundary (at least two "Does NOT" statements)

Reference: Chapter 2.

### Step 4: Invoke start-session.md

Start a fresh Claude Code session. Reference `@start-session.md` at the top of your first message, or paste its contents if you prefer. Append the requirement below it. Specify the autonomy mode explicitly — add a line like "Mode: Implement and verify" or "Mode: Stage by stage" so the agent knows whether to pause.

### Step 5: Implement and verify

Let the agent work. If Mode 2 or 3, it will run tests automatically. If Mode 1, review the diff before telling it to proceed with tests.

```bash
pytest tests/ -v
```

> **Watch For:** All existing tests still passing, plus the new test you specified. If tests fail, issue a targeted correction identifying the specific failing test and the expected behavior.

### Step 6: Review the diff

Open `tasks.py` and read what changed. Ask the five questions from Chapter 4:
1. Can you explain what every changed function does in one sentence?
2. Does each function do one thing?
3. Are variable names descriptive?
4. Are error cases handled?
5. Is there anything you would not want to explain to a colleague?

If yes to any, issue a targeted correction before moving on.

### Step 7: Update artifacts

Add a decisions.md entry for any new decision made. Update context.md with the new test count, new commands, updated schema if applicable. If you used sprint-plan.md, mark the sprint complete.

Close the agent session.

### Step 8: Verify the handoff

Open a new agent session with only context.md. Ask it to describe the current state of the project. If the answer is accurate — test count, commands, key decisions — the session closes cleanly and the next one opens informed.

---

## What You Now Have

The task manager started in Chapter 1 as a four-command CLI: `add`, `list`, `done`, `delete`. It stores tasks in a JSON file. A developer wrote a planning brief before building it, which is why it was built correctly the first time.

Fourteen chapters later:

**Code:** 20+ tests. 10+ commands. Validated input. Explicit error handling. Backward compatibility across schema changes. A codebase you can explain to a colleague because you reviewed every increment before it landed.

**Artifacts:** `context.md` — operational snapshot of the project, accurate as of the last session. `decisions.md` — the full decision log, from priority validation in Chapter 2 to CSV format in Chapter 12. `COMMANDS.md` — user-facing reference documentation. `start-session.md` — the skill that makes every session start in thirty seconds instead of five minutes. `sprint-plan.md` — the record of how the last sprint was planned and what was deferred.

**Process:** A loop you can run on autopilot. A calibration heuristic for autonomy. A sprint structure that prevents feature incoherence. A handoff test that verifies the artifacts are complete.

Hand this project to a colleague right now. They open context.md. They read the commands, the schema, the key decisions. They open decisions.md to understand why the search is case-insensitive and why the date format is YYYY-MM-DD. They run the tests — 20+ pass. They pick a feature from the backlog and start a session. No onboarding meeting. No "let me walk you through the code." The artifacts do the talking.

That is the outcome. Not a faster way to write code — a disciplined way to build projects that outlast any single session.

---

## The Closing Argument

Here is what this book claimed at the start, and what you have now seen demonstrated: **software engineering discipline did not disappear in the AI era. It moved up a level.**

Before AI coding tools, discipline meant: write requirements before you build, test your code, review the diff, iterate deliberately, manage scope, document decisions. You did those things by doing the implementation — the discipline was embedded in the craft.

Now the AI does much of the implementation. Which means the discipline has to happen somewhere else — in the requirement before the session, in the test cases before the code, in the diff review after the implementation, in the decisions.md entry after the feature lands. The work of discipline did not go away. It migrated from implementation to specification.

This is why a developer who relies on AI without the discipline produces code that accumulates — features without requirements, tests that pass but do not cover, implementations that contradict each other session to session. And why a developer who applies the discipline gets something that compounds — each session building on documented decisions, each sprint advancing a coherent goal, each handoff cheaper than the last.

The AI is a fast implementer. You are the permanent owner. Those roles have different jobs. The fast implementer produces working code. The permanent owner produces maintainable projects. This book was about the permanent owner's job — which turns out to be the same job it always was, done with different tools.

---

## What Comes Next

The methodology scales. Everything in this book applies to a team project — shared context.md, shared decisions.md, parallel agents with explicit scope boundaries, sprint plans that coordinate multiple developers. The artifacts are the coordination layer. The loop is the shared process. The autonomy modes calibrate trust across team members the same way they calibrate trust in a solo session.

Your task manager is feature-complete for this book's purposes. Your backlog is not. The next sprint is yours to plan.

Pick a feature. Write the requirement. Run the loop.

---

*The discipline did not change. The medium did.*
