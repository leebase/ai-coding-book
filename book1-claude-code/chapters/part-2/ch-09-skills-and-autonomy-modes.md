# Chapter 9: Skills and Autonomy Modes

Count how many times you have typed a variation of this at the start of an agent session:

```
I have a Python CLI task manager in tasks.py with N passing tests.
Current commands: add (--priority, --due), list, done, delete, overdue, search, stats.
tasks.json schema: {"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}
```

Seven times across Part 1. Plus the decisions. Plus the scope of the specific feature. Every session, reconstructed from memory.

This is the boilerplate problem. The context setup is identical across sessions — the same project, the same schema, the same decision constraints — but you write it from scratch each time. Small errors accumulate: a forgotten decision, a wrong test count, an outdated schema. The agent works with what you give it. If the context is incomplete, the implementation reflects the gap.

**A skill is the fix.** Write the context setup once, save it as a file, reference it instead of retyping. The agent reads the skill file and has everything it needs to start. The session begins at the feature, not at the boilerplate.

---

## What a Skill Is

A skill is a markdown file that encodes a repeatable prompt. It is not code. It is not documentation. It is a saved prompt template — the same thing you have been typing manually, written once and stored.

A skill for the Start stage of the AgentFlow loop would contain:
- The current project state (test count, commands, schema)
- A reference to decisions.md for the full decision list
- Any standard instructions that apply to every session (the requirement format, the "Does NOT" convention, the test count to preserve)

The format is simple:

```markdown
# Task Manager: Session Start

## Project state
- Tests: [CURRENT_COUNT] passing
- Commands: add (--priority, --due), list (--format json), done, delete, overdue, search, stats, clear
- tasks.json schema: {"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}

## Decisions
See decisions.md for the full decision log. Key constraints:
- Invalid input: print error, exit non-zero. Never silently default.
- Missing fields: display defaults, never error.
- Output format: fixed, all fields shown, no optional output.
- Date format: YYYY-MM-DD only. Overdue uses local system date, not UTC.
- Sort order: creation order always. No automatic sorting.

## Standard instructions
- New features require a requirement before implementation.
- Each session adds at most 2 new tests.
- All existing tests must pass after any change.
```

Three sections. The only part that changes session to session is the test count. Everything else is stable until the project changes significantly.

---

## Writing start-session.md

Create the skill file in your task manager project. Use your editor or `touch start-session.md`, then copy the template above and update `[CURRENT_COUNT]` to `14` (your current test count after Chapter 8).

Save with Cmd+S or Ctrl+S.

> **Note:** The skill file lives in your project directory alongside `tasks.py` and `decisions.md`. It is not a special Claude Code file type. It is a plain markdown file you can reference at the start of each session with `@start-session.md`, or copy into the prompt if you prefer.

Now see the failure path, to understand what the skill prevents.

---

## The Failure Path: Without the Skill

The next feature is `clear` — a command that removes all completed tasks from tasks.json. Simple feature, one new test. Add it without using the skill.

Start a fresh Claude Code session in your project directory. Type from memory:

```
I have a Python CLI task manager with 14 tests. Add a clear command that
removes done tasks. Also make sure the overdue count in stats is right.
```

> **What the Agent Will Do:** The agent will implement `clear`. It will also attempt to verify the `overdue` count in `stats`. But "overdue count is right" is ambiguous — the agent may use UTC rather than local system time, which is what your decisions.md specifies. You did not include that decision, so the agent guesses.

> **Watch For:** After the agent finishes, run:

```bash
python tasks.py stats
```

The count may look correct. But check the implementation — open `tasks.py` and find where `stats` computes overdue tasks. Does it use `datetime.now()` (local time) or `datetime.utcnow()` or `datetime.now(timezone.utc)`? If it uses UTC, it contradicts the decision you made in Chapter 8, and users in certain timezones will see wrong overdue counts.

You would not catch this from the test suite. The tests run on your machine, in your timezone. The inconsistency is invisible until a user in a different timezone files a bug report.

This is the cost of incomplete context: the agent filled the gap with a plausible assumption. The assumption was wrong.

> **Credit Note:** Run the tests anyway to see the count:

```bash
pytest tests/ -v
```

> **Watch For:** Tests passing, but the implementation containing a decision you did not specify. Stop here — do not fix it. You will use the skill in the success path.

---

## The Success Path: Clear with the Skill

Start a fresh Claude Code session. This time, reference `@start-session.md` at the top of your prompt, or paste its contents if you prefer. Then add the feature requirement below:

```
# Task Manager: Session Start

## Project state
- Tests: 14 passing
- Commands: add (--priority, --due), list (--format json), done, delete, overdue, search, stats
- tasks.json schema: {"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}

## Decisions
See decisions.md for the full decision log. Key constraints:
- Invalid input: print error, exit non-zero. Never silently default.
- Missing fields: display defaults, never error.
- Output format: fixed, all fields shown, no optional output.
- Date format: YYYY-MM-DD only. Overdue uses local system date, not UTC.
- Sort order: creation order always. No automatic sorting.

## Standard instructions
- New features require a requirement before implementation.
- Each session adds at most 2 new tests.
- All existing tests must pass after any change.

---

Feature: Clear completed tasks

Input: python tasks.py clear (no arguments)
Output:
- Cleared N completed tasks. (where N is the count removed)
- If no completed tasks: No completed tasks to clear.

Edge cases:
- Task IDs are NOT renumbered after clearing
- Tasks with done=false are not affected

Does NOT:
- Clear by priority, due date, or any other filter
- Ask for confirmation before clearing
- Support undoing the clear

Add exactly 1 new test:
- clear removes done tasks and prints the correct count

All 14 existing tests must still pass.
```

> **What the Agent Will Do:** The agent will implement `clear` with full knowledge of your decisions — it will not touch the overdue logic, it will not renumber IDs, and it will follow the established error pattern. The skill context prevents the gap the failure path exposed.

> **Watch For:** The agent not asking clarifying questions. Complete context means no guessing required.

Verify:

```bash
pytest tests/ -v
```

> **Watch For:** 15 tests passing. Then manually verify:

```bash
python tasks.py add "Buy groceries" --priority medium
python tasks.py add "Fix critical bug" --priority high
python tasks.py done 1

python tasks.py clear
# Expected: Cleared 1 completed tasks.

python tasks.py list
# Expected: Only task 2 remains. Task 1 is gone. IDs are not renumbered.

python tasks.py clear
# Expected: No completed tasks to clear.
```

Update decisions.md with a new entry for `clear`:

```markdown
## Clear behavior
- **Decision**: clear removes all done=true tasks permanently. IDs not renumbered. No confirmation.
- **Reason**: Matches delete behavior (no confirmation, no undo). Keeps ID sequence stable.
- **Rules out**: Confirmation prompt, undo capability, selective clear by filter.
```

Also update the test count in `start-session.md`: change `14` to `15`.

---

## Autonomy Modes

A skill makes the Start stage fast. Autonomy modes decide how much of the remaining loop the AI runs before pausing for human input.

**Mode 1: Stage-by-stage**
The AI completes one loop stage and stops. You review, then invoke the next stage explicitly. Maximum oversight — every implementation, verification, and review step has human eyes before proceeding. Appropriate when: the task is unfamiliar, the requirement is uncertain, or you want to build confidence in a new skill.

**Mode 2: Implement and verify**
The AI runs Implement and Verify automatically — it builds the feature and runs the tests. It stops before Review and Update, which remain human steps. Appropriate when: the requirement is tight, the test suite is comprehensive, and you trust the implementation quality. This is the mode you effectively used for most of Part 1 — you wrote the requirement, let the agent implement, then ran tests yourself.

**Mode 3: Full loop**
The AI runs all five stages — Start (using the skill), Implement, Verify, Review, and Update — and delivers a complete session artifact. You review the entire output at the end. Appropriate only when: your skills are mature, your context file is complete (Chapter 10), and the test suite is reliable enough to catch regressions. Mode 3 is fast and high-risk; save it for routine features on a well-established project.

For the `clear` command you just built, Mode 1 was appropriate — first time using a skill, first session with the new loop structure. As you build confidence in your skills and context file, you will naturally shift toward Mode 2 for routine features. Mode 3 is something to earn, not a default.

---

## Debrief

A skill is saved process. The context setup that took five minutes every session now takes thirty seconds — copy, paste, append the feature requirement, send. The overdue-uses-local-date decision travels with every session automatically, not just when you remember to include it.

**Skills reduce the cost of consistency.** The disciplines from Part 1 are only valuable if applied every session. Skills apply them without relying on memory.

The next chapter formalizes this further. Rather than embedding the project state directly in `start-session.md`, you will learn to maintain a dedicated context file — a single source of truth for current project state that your skills reference. When the test count changes, you update one file. All skills automatically reflect the new state.

---

*A skill is a discipline made repeatable. Write it once; apply it every session.*
