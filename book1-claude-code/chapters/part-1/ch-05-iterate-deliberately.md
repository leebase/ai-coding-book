# Chapter 5: Iterate Deliberately

AI makes iteration cheap. You can prompt, get a result, prompt again, and repeat. This is genuinely useful — you can explore and refine quickly.

It is also a trap.

When iteration is cheap, the temptation is to iterate recklessly — pile on changes in a single prompt, accept whatever seems better, never quite stop to verify. You move fast. The code accumulates. Something breaks three iterations later and you cannot trace it back, because you were not tracking what changed when.

**The cost of reckless iteration is not speed — it is traceability.** When something goes wrong, you need to know which change caused it. If you made five changes in one prompt, you have no way to isolate the cause without untangling everything.

Deliberate iteration solves this by making the same rule explicit: one change at a time, verified, before the next. Not because it is slower — it often is not. Because it keeps the change history readable and the debugging tractable.

---

## The Reckless Iteration Trap

You have nine passing tests, a clean implementation, and a clear next feature: due dates. Tasks can optionally have a due date, `list` shows it, and a new `overdue` command shows tasks that are past due.

This is three changes: a data model update, a display update, and a new command. The temptation is to ask for all three at once.

Open Claude Code and start a new agent session. Type:

```
Add due dates to the task manager. Tasks can optionally have a due date.
Show due dates in the list command. Add an overdue command that shows
tasks past their due date that aren't done yet.
```

> **What the Agent Will Do:** The agent will modify the `add` command to accept a due date, update the `tasks.json` schema, change the `list` output format, and add the `overdue` command. It will make decisions about the date format, how to display missing due dates, and what "past due" means for tasks with no due date.

> **Watch For:** How many files changed. Run the tests immediately:

```bash
pytest tests/ -v
```

> **Watch For:** How many tests fail. With a combined change of this scope, you will likely see two or three failures — the list format changed, the add signature may have changed, and possibly a test for the `done` display breaks because the list output format is different.

Now try to fix the failures. Issue corrections for the failing tests.

> **Credit Note:** Each correction is another prompt. Each prompt may fix one test and break another. You are debugging a multi-change diff without a clear view of which change caused which failure.

Stop after two or three correction attempts. Count how many prompts you have used. Count how many tests are still failing. Notice: you cannot easily answer "which change broke the list display tests?" because three changes landed together.

This is the traceability problem. Not a catastrophe — but a debugging session that did not have to happen.

---

## The Increment Plan

The solution is to plan your increments before you open Claude Code, the same way you write a requirement before you build a feature.

An increment plan answers:
- What changes in this increment?
- What does NOT change?
- What does "verified" mean before moving to the next increment?

Here is the increment plan for due dates:

---

**Increment 1: Data model only**
- Change: `add` accepts `--due YYYY-MM-DD` (optional). Stores `due_date` in `tasks.json` (null if not provided).
- Does not change: `list` output format, `overdue` command does not exist yet
- Verified when: `add "task" --due 2026-04-01` stores `"due_date": "2026-04-01"` in JSON. `add "task"` stores `"due_date": null`. All 9 existing tests pass.

**Increment 2: List display**
- Change: `list` shows `[2026-04-01]` after the task description when a due date exists. Shows nothing extra when `due_date` is null.
- Does not change: `add` signature (already done), `overdue` command still does not exist
- Verified when: list output matches the new format. Update 1 existing test that checks list output. 9 tests pass.

**Increment 3: Overdue command**
- Change: `overdue` command lists tasks where `due_date` is before today's date and `done` is false. Tasks with no due date are never shown as overdue.
- Does not change: anything in increments 1 or 2
- Verified when: `overdue` shows the correct tasks. Add 2 new tests. 11 tests pass.

**Increment 4: Final check**
- Run the full suite. Manually test the feature end-to-end. Confirm the whole thing behaves as intended.

---

This plan took ten minutes to write. It will save more than that in debugging time.

---

## Four Increments, Four Verifications

Start from your Ch 4 end state: nine passing tests, reviewed `tasks.py`. If you followed the failure path at the start of this chapter and your code is now in a messy state, the simplest recovery is to open `tasks.py` and revert it manually to the last clean state, or re-run the Ch 4 success path if you did not save a copy. If you have been committing your work with git, `git checkout` to your last clean commit.

### Increment 1: Data Model

Start a fresh Claude Code session. Provide the full context of the current state, then the increment spec:

```
I have a Python CLI task manager in tasks.py with these commands:
add, list, done, delete (plus --priority flag on add).
Storage: tasks.json — array of task objects.

Increment 1 of 3: Add due date storage only.

Changes:
- add command accepts an optional --due flag: python tasks.py add "description" --due 2026-04-01
- Date format: YYYY-MM-DD only. Invalid format: print error, exit non-zero, do not add task.
- tasks.json stores "due_date": "2026-04-01" when provided, "due_date": null when not.

Do NOT change:
- list output format (no due date display yet)
- Any existing command behavior
- All 9 existing tests must still pass
```

> **What the Agent Will Do:** The agent will add the `--due` flag to the `add` command's argument parser, add basic date format validation, and update the task object construction to include `due_date`. It will not touch `list` or any other command.

> **Watch For:** The agent making a small, targeted change. Open `tasks.py` after — the diff should be 10-20 lines, not a rewrite.

Verify:

```bash
# Test storing a due date
python tasks.py add "Dentist appointment" --due 2026-04-01
python tasks.py list
# Expected: task appears, list format unchanged (no due date shown yet)

# Check tasks.json directly — open it in the editor
# Expected: "due_date": "2026-04-01" in the new task's JSON object

# Test no due date
python tasks.py add "Buy groceries"
# Check tasks.json — Expected: "due_date": null for this task

# Run the full test suite
pytest tests/ -v
```

> **Watch For:** All 9 tests passing. If any fail, the increment changed something it should not have. Issue a targeted correction before moving to Increment 2.

### Increment 2: List Display

Start a fresh Claude Code session. Give the agent the current state and increment 2:

```
The task manager now stores due_date in tasks.json ("YYYY-MM-DD" or null).

Increment 2 of 3: Update list display only.

Changes:
- list shows due date after description when present: [1] [medium] Buy milk [due: 2026-04-01]
- list shows nothing extra when due_date is null: [1] [medium] Buy groceries
- Completed tasks: [1] [medium] [done] Buy milk [due: 2026-04-01]

Do NOT change:
- add command (already done)
- overdue command (does not exist yet)
- Any other behavior
```

> **What the Agent Will Do:** The agent will modify the `list` command's output formatting to append the due date when present. One function, a few lines.

Update the test that checks `list` output format — it now needs to account for the `[due: YYYY-MM-DD]` suffix. In the same agent session, issue a follow-up prompt if the agent did not update the tests automatically:

```
Update test_tasks.py: the test that checks list output format should now
expect [due: 2026-04-01] appended when a task has a due date, and nothing
appended when due_date is null.
```

Verify:

```bash
pytest tests/ -v
```

> **Watch For:** 9 tests passing (the updated list-format test now reflects the new output).

### Increment 3: Overdue Command

Start a fresh Claude Code session. Give the agent the full current state and increment 3:

```
The task manager has add (with --priority and --due), list (shows due dates),
done, and delete commands. tasks.json schema:
{"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}

Increment 3 of 3: Add the overdue command.

Specification:
- python tasks.py overdue — lists tasks where due_date is before today's date
  AND done is false
- Output format: same as list — [ID] [priority] description [due: date]
- Tasks with due_date: null are never shown as overdue
- If no tasks are overdue, print "No overdue tasks."
- Today's date comparison uses the local system date (specifying this prevents the agent from using UTC, which can produce wrong results for users in some timezones)

Add exactly 2 new tests:
1. overdue shows tasks with due dates in the past and done=false
2. overdue does not show tasks with due_date: null, done=true, or future dates

Do NOT change any existing commands or tests.
```

> **What the Agent Will Do:** The agent will add an `overdue` command handler that filters `tasks.json` by due date relative to today. It will add 2 new tests to `test_tasks.py`.

Verify:

```bash
pytest tests/ -v
```

> **Watch For:** 11 tests passing. Then manually verify the command:

```bash
# Add an overdue task (use a past date)
python tasks.py add "Overdue task" --due 2024-01-01
python tasks.py overdue
# Expected: the overdue task appears

# Add a future task
python tasks.py add "Future task" --due 2099-12-31
python tasks.py overdue
# Expected: future task does not appear
```

### Increment 4: Final Verification

Run the complete suite one more time:

```bash
pytest tests/ -v
```

> **Watch For:** 11 tests passing, clean output, no warnings.

Then do a full end-to-end manual test — add tasks with and without due dates, mark some done, run `overdue`, run `list`. Make sure the feature behaves as intended across realistic usage, not just the test cases.

---

## Debrief

Three increments. Three new agent sessions. Eleven passing tests, up from nine. At every point in this process, you could answer: which change am I currently verifying?

Compare this to the failure path, where you could not answer that question after two prompts.

**Traceability is the product of deliberate iteration.** When something goes wrong — and in a long project, something will — you need a clear record of when and where it was introduced. One change per verified increment gives you that record. Everything-at-once does not.

Notice also what you just wrote before you opened Claude Code: an increment plan. It is not a formal document. It is a sequenced list of changes with verification criteria. In Part 2, you will recognize this as the structure of a sprint plan — the same discipline applied to larger units of work coordinated across multiple AI sessions and agents. Every sprint has a defined scope and a definition of done. Every increment has the same. The scale differs; the pattern is identical.

---

*One change, verified, before the next. This is how you stay in control of a project the AI is building.*
