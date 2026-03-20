# Chapter 7: Document Decisions

The AI that helped you build this task manager has no memory of it.

Not a figure of speech — literally none. Every new agent session starts blank. The session that added the `--priority` flag has no knowledge of the session that added the `overdue` command. The session you open today cannot remember that you decided invalid priority values should error rather than silently default, or that list output should always show tasks in creation order, or that search should always be case-insensitive with no flag.

You remember these things. For now. But projects outlast working memory.

**Code records what was built. It does not record why.** Open `tasks.py` right now and find the line that handles an invalid priority value. It errors and exits non-zero. Why? Because you wrote a requirement six sessions ago that said so. Is that visible in the code? Only if someone reads the error message carefully — and even then, they do not know that the alternative (silent default) was explicitly ruled out.

A decision log captures the why. Not for documentation's sake. For operational reasons: every new agent session that works on this project needs to know what you decided, or it will make its own decisions — plausibly, confidently, and incorrectly.

---

## The Amnesia Problem

Here is how the problem surfaces. You are adding a `--format` flag to the `list` command. Users want to export tasks as JSON for other tools. Reasonable feature, small change.

Start a fresh Claude Code session in your project directory. Type:

```
I have a Python CLI task manager in tasks.py with 12 passing tests.
Current commands: add (--priority, --due), list, done, delete, overdue, search.

Add a --format flag to the list command:
- python tasks.py list --format json outputs all tasks as a JSON array
- Default (no flag) keeps the existing text format unchanged
```

> **What the Agent Will Do:** The agent will add a `--format` flag to the `list` command and implement JSON output. It will make decisions you have not specified: which fields to include in the JSON, what happens when an invalid format is passed, and whether the JSON output matches the schema in `tasks.json` exactly.

> **Watch For:** How the agent handles an invalid format value. Run this after it finishes:

```bash
python tasks.py list --format csv
```

The agent will likely either print an error or silently fall back to the default text format. Neither is wrong by itself. But one of them contradicts a decision you made in Chapter 2.

Now run the tests:

```bash
pytest tests/ -v
```

> **Watch For:** The tests may all pass — the new flag does not necessarily break existing behavior. But run this check manually: does `list --format csv` produce an error message and exit non-zero? Or does it silently output the default format?

If it silently defaults, the agent made a different call than the one you established in Chapter 2: invalid input should print an error and exit non-zero. The agent had no way to know this. It was not told. The decision lived in your head and in a requirement you wrote six sessions ago in a different context.

> **Credit Note:** This is a subtle failure. The tests pass. The feature works. The implementation just contradicts a principle you established earlier, and you will only discover it when a user passes an invalid flag and gets silence instead of an error.

Stop here. Do not fix it. You are going to write the decision log first.

---

## Writing decisions.md

A decision log is not a changelog and it is not documentation. It is a short list of choices that constrain future behavior — the calls you made that a new AI session would not know about unless you told it.

The format is minimal on purpose. For each decision:
- **Decision**: the call you made
- **Reason**: why you made it
- **Rules out**: what this decision explicitly excludes

Three fields, one line each. Here is decisions.md for the task manager after six chapters:

---

```markdown
# Task Manager: Decision Log

## Error behavior
- **Decision**: Invalid input (bad priority, bad date format, bad --format flag) prints an error message and exits non-zero. Does not add or modify data.
- **Reason**: Silent defaults make errors invisible to users and scripts.
- **Rules out**: Silent fallback to defaults on invalid input.

## Missing fields
- **Decision**: Tasks in tasks.json missing optional fields (priority, due_date) display with defaults (medium, no date shown) without modifying stored data.
- **Reason**: Backward compatibility — old tasks should not break new features.
- **Rules out**: Erroring on missing fields; auto-migrating stored data.

## Output format
- **Decision**: list output always shows all fields for a task in a fixed format. JSON output (--format json) includes all task fields: id, description, done, priority, due_date.
- **Reason**: Consistent output makes tests reliable and user expectations predictable.
- **Rules out**: Optional fields, abbreviated output, fields varying by flag.

## Sort order
- **Decision**: list always shows tasks in creation order (by id ascending). No sort by priority, due date, or status.
- **Reason**: Predictable ordering makes manual verification easier.
- **Rules out**: Any automatic sorting.

## Date format
- **Decision**: All dates use YYYY-MM-DD. Invalid format prints error, exits non-zero.
- **Reason**: Single format, no ambiguity between MM/DD and DD/MM.
- **Rules out**: Other date formats, locale-specific parsing.

## Search behavior
- **Decision**: search is always case-insensitive. No flag.
- **Reason**: Users should not need to think about case to find their own tasks.
- **Rules out**: Case-sensitive search mode; --case-sensitive flag.
```

---

Create this file yourself — not by prompting the agent, but by hand. Use your editor or `touch decisions.md`, paste the content above, and save it.

This took about ten minutes to write. The benefit is not just the document itself — it is the act of writing it. Reviewing six chapters of decisions reveals which ones you would forget to mention in a prompt and which ones would surprise a new AI session if it had to guess.

---

## The Success Path: Format with Context

Start a fresh Claude Code session. This time, give the agent your decisions.md as part of the context. You do not need to paste the entire file — pull out the decisions relevant to this feature (error behavior and output format). The prompt below shows exactly what to include:

```
I have a Python CLI task manager in tasks.py with 12 passing tests.
Current commands: add (--priority, --due), list, done, delete, overdue, search.
tasks.json schema: {"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}

Project decisions (from decisions.md):
- Invalid input prints an error and exits non-zero. Does not silently default.
- JSON output includes all task fields: id, description, done, priority, due_date.
- list always shows all fields; no optional or abbreviated output.

Add a --format flag to the list command:

Input:
- python tasks.py list — unchanged text output
- python tasks.py list --format json — outputs tasks as a JSON array

Output (json format):
- A JSON array of task objects, one per line, all fields included
- Example: [{"id": 1, "description": "Buy groceries", "done": false, "priority": "medium", "due_date": null}]
- If no tasks: []

Edge cases:
- python tasks.py list --format csv or any unsupported format: print error
  "Error: unsupported format 'csv'. Supported formats: json" and exit non-zero.

Add exactly 1 new test:
- list --format json outputs valid JSON containing all task fields

All 12 existing tests must still pass.
```

> **What the Agent Will Do:** The agent will add the `--format` flag and implement JSON output. Because the decision log explicitly stated that invalid input must error and exit non-zero, the agent will implement the error case correctly — it has a clear constraint.

> **Watch For:** The invalid format test — run this after the agent finishes:

```bash
python tasks.py list --format csv
```

Expected: `Error: unsupported format 'csv'. Supported formats: json` and a non-zero exit code. If you see this, the decision was respected. If the command silently outputs text, the agent missed the constraint.

Verify:

```bash
pytest tests/ -v
```

> **Watch For:** 13 tests passing. Then manually verify JSON output:

```bash
python tasks.py add "Buy groceries" --priority medium
python tasks.py add "Fix critical bug" --priority high --due 2026-04-01
python tasks.py list --format json
# Expected: JSON array with both tasks, all fields present including due_date
```

> **Watch For:** Every field present — `id`, `description`, `done`, `priority`, `due_date`. If `due_date` is missing from the JSON, the agent did not follow the "all fields" decision. Issue a targeted correction referencing the decision log.

---

## Debrief

Compare the two sessions. In the first, the agent made its own call on invalid format — plausibly, but inconsistently with your established behavior. In the second, the agent had the decision log and implemented correctly on the first try.

The decision log did not add complexity. It removed ambiguity. The agent did not have to guess what you wanted for invalid input because you had already decided that, six chapters ago, and written it down.

**A decision log is insurance against your own forgetfulness as much as the AI's amnesia.** Midway through a long project, you will not remember why you chose YYYY-MM-DD over other formats, or why search has no case-sensitive flag. The log is the record. The AI is just the most obvious beneficiary.

The discipline generalizes to collaborators — human and AI alike. If another developer joins this project, the code tells them what exists. The decisions.md tells them what constraints those choices were made under. One file, one purpose: preserving intent across time.

You have now built a task manager through seven chapters of deliberate practice: planning, requirements, testing, review, iteration, scope, and decision tracking. Each discipline compounds. The requirements from Chapter 2 informed the test cases in Chapter 3. The tests from Chapter 3 caught the scope drift in Chapter 6. The scope decisions from Chapter 6 are now in the decision log you will carry into Part 2.

```
Plan (Ch 1) ──────────► Requirements (Ch 2)
     ▲                           │
     │                       Tests (Ch 3)
     │                           │
Document                     Review (Ch 4)
Decisions (Ch 7)                 │
     ▲                       Iterate (Ch 5)
     │                           │
     └─────── Scope (Ch 6) ◄─────┘
```

*Each new feature enters at Plan, informed by documented decisions from the previous feature. The loop is the practice.*

In Part 2, decisions.md becomes the seed of a larger artifact — the project context file that makes multi-session AI development tractable at scale. You built the habit here. Part 2 gives it a formal structure.

---

*The AI forgets everything when the session ends. decisions.md doesn't.*
