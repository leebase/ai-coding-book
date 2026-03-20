# Chapter 8: The AgentFlow Loop

Look back at what you did in Part 1.

Before each feature, you wrote a requirement. Before you opened a new session, you read your code. After each change, you ran the tests. When something went wrong, you issued a targeted correction. When you finished, you updated decisions.md.

You were not following a random set of tips. You were running a loop.

Every session had the same structure: establish what you know, specify what you want, implement with a scoped agent, verify the result, review what changed, record what was decided. Seven disciplines, one sequence. **AgentFlow is the name for that sequence made explicit** — a repeatable structure that puts the disciplines in order so you do not have to remember when to apply them.

Part 2 is about running that loop deliberately, at scale, across a project that grows over weeks. This chapter introduces the loop. The chapters that follow introduce the tools that make it faster.

---

## The Five Stages

The AgentFlow Development Loop has five stages. You have run all of them. Here they are with their names:

**Stage 1: Start**
Load the context for this session. What is the current state of the project? How many tests are passing? What schema does the data have? What decisions have been made? This is where decisions.md earns its keep — instead of reconstructing context from memory, you read the file.

Then write the requirement for this session's work. Specific input, specific output, edge cases, explicit scope boundary. Nothing new here — this is Chapter 2.

**Stage 2: Implement**
Open a new agent session. Give the agent the context (state) and the requirement. Let it build. Do not interrupt unless it asks a question or does something visibly wrong.

This is one session, one requirement, one increment — Chapter 5.

**Stage 3: Verify**
Run the test suite. Read the output. If tests fail, issue a targeted correction. If tests pass, run the manual checks from your requirement's verification section.

The tests come from your requirements, not from the agent's interpretation of its own code — Chapter 3.

**Stage 4: Review**
Read the diff. Not to find bugs — to transfer understanding. Can you explain every function that changed? Are the variable names readable? Is there anything you would not want to explain to a colleague?

This is Chapter 4, applied after every implementation sprint rather than once at the end.

**Stage 5: Update**
Record what changed. Add a new entry to decisions.md for any new decisions made during this session. Note the end state: how many tests pass, what commands exist, what the schema looks like. This is the Start material for the next session.

Then close the agent session. The next session begins at Stage 1.

---

The loop is not bureaucracy. Each stage takes a fraction of the time the implementation takes. The overhead is the requirement (ten minutes), the test run (seconds), the diff read (two minutes), the decisions.md update (two minutes). The total is fifteen minutes of structure per hour of implementation. The payoff is a project you can pick up in two weeks and know exactly where it stands.

---

## The Failure Path: Skipping the Loop

Your task manager has thirteen passing tests and a decisions.md. A reasonable next feature: a `stats` command that shows a quick summary — total tasks, how many are done, how many are overdue.

Skip the loop. Start a fresh Claude Code session in your project directory. Type:

```
Add a stats command to the task manager.
```

> **What the Agent Will Do:** The agent will add a `stats` command that counts tasks. It will make choices you have not specified: what to count, what format to display, what to show when tasks.json is empty, and how to count "overdue" — does it use the same logic as the `overdue` command, or its own?

> **Watch For:** The agent's output format. Run it after the agent finishes:

```bash
python tasks.py stats
```

Note the format. Is it one line? Multiple lines? Does it show counts as numbers or percentages? Does it mention overdue? Now run the tests:

```bash
pytest tests/ -v
```

> **Watch For:** The test count. If the agent wrote a test for stats, it wrote it against its own implementation — not against a requirement you specified. And the session left no trace: no updated decisions.md, no documented output format, no note of what was added.

Stop here. The feature may work. But if you close this session and open a new one tomorrow, you cannot answer: what does `stats` output when there are no tasks? The agent decided. You do not know its reasoning. It is gone.

This is what the loop prevents — not bad code, but undocumented decisions.

---

## Running the Loop: Stats

Start over. Close the agent session. Now run the loop explicitly.

### Stage 1: Start

Before opening a new agent session, establish context and write the requirement.

**Current state:**
- 13 passing tests
- Commands: add (--priority, --due), list (--format json), done, delete, overdue, search
- tasks.json schema: `{"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}`
- decisions.md: error behavior, missing fields, output format, sort order, date format, search behavior

**Requirement:**

---

*Feature:* Stats command

*Specific input:*
- `python tasks.py stats` — no arguments

*Specific output:*
- One-line summary: `Total: N tasks (X done, Y overdue)`
- If tasks.json is empty or does not exist: `No tasks.`

*Edge cases:*
- Overdue count uses the same logic as the `overdue` command: due_date before today AND done=false
- Done count: tasks where `done` is true, regardless of due date

*Scope boundary:*
- Does NOT show individual tasks
- Does NOT break down by priority
- Does NOT show percentages

---

### Stage 2: Implement

Start a fresh Claude Code session. Give the agent context and the requirement:

```
I have a Python CLI task manager in tasks.py with 13 passing tests.
Current commands: add (--priority, --due), list (--format json), done, delete, overdue, search.
tasks.json schema: {"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}

Project decisions (from decisions.md):
- Invalid input prints an error and exits non-zero. Does not silently default.
- Output format: fixed, one-line per summary. No optional fields.
- Overdue logic: due_date before today's local date AND done=false.

Add a stats command with the following specification:

Feature: Stats command
Input: python tasks.py stats (no arguments)
Output:
- Total: N tasks (X done, Y overdue)
- If no tasks or tasks.json missing: No tasks.

Edge cases:
- Overdue count: same logic as overdue command (due_date before today AND done=false)
- Done count: tasks where done=true, any due date

Does NOT:
- Show individual tasks
- Break down by priority
- Show percentages

Add exactly 1 new test:
- stats shows correct total, done, and overdue counts

All 13 existing tests must still pass.
```

> **What the Agent Will Do:** The agent will add a `stats` command that reads tasks.json and computes the three counts. It will reuse the date comparison logic from the `overdue` command. One new test.

> **Watch For:** The agent completing without clarifying questions. A well-specified requirement should not require agent questions. If it asks something, the answer is in the requirement — point to the relevant line.

### Stage 3: Verify

```bash
pytest tests/ -v
```

> **Watch For:** 14 tests passing. Then verify manually:

```bash
# Add test tasks if needed
python tasks.py add "Buy groceries" --priority medium
python tasks.py add "Fix critical bug" --priority high --due 2024-01-01
python tasks.py add "Future task" --priority low --due 2099-12-31
python tasks.py done 1

python tasks.py stats
# Expected: Total: 3 tasks (1 done, 1 overdue)

# Verify with no tasks
# Open tasks.json in your editor and replace its contents
# with an empty array: []
# Save (Cmd+S or Ctrl+S), then:
python tasks.py stats
# Expected: No tasks.
```

> **Watch For:** Both cases matching the requirement exactly. If the overdue count is wrong, check whether the agent used today's local date (correct) or UTC (which may differ by timezone).

### Stage 4: Review

Open `tasks.py` and find the `stats` command handler. Read it. Can you answer:
- How does it compute the overdue count? Is it the same logic as `overdue`?
- What does it do when tasks.json does not exist?
- Is the output format constructed correctly for singular vs. plural? (This edge case is easy to miss: "1 tasks" instead of "1 task".)

If the singular/plural case is wrong — `Total: 1 tasks` instead of `Total: 1 task` — issue a targeted correction now, before moving to Stage 5.

> **Watch For:** Any code path the agent added that you cannot explain in one sentence. If found, ask the agent to explain it in a follow-up message before moving on.

### Stage 5: Update

Add a new entry to decisions.md. Open `decisions.md` in your editor and add:

```markdown
## Stats format
- **Decision**: stats output is one line: "Total: N tasks (X done, Y overdue)". Empty: "No tasks."
- **Reason**: Matches the one-line summary pattern established for other commands.
- **Rules out**: Multi-line breakdown, percentage display, priority breakdown.
```

Also note the new end state at the bottom of decisions.md:

```
## Session end state
Tests: 14 passing
Commands: add, list, done, delete, overdue, search, stats
```

Close the agent session. The loop is complete.

---

## Debrief

You just ran a named, documented session. In thirty years, when you open this project after a long break, you will know exactly where it stands — not because you have a good memory, but because the loop left a trail.

**The loop is the discipline container.** Without it, the seven disciplines from Part 1 are habits that fire when you remember them. With the loop, they fire because the loop has stages and the stages have names: Start requires a requirement (Chapter 2), Verify requires tests (Chapter 3), Review requires a diff read (Chapter 4), Update requires decisions.md (Chapter 7). The loop does not add discipline — it schedules it.

The next three chapters introduce the tools that make the loop faster. Chapter 9 covers skills — prompts that automate specific stages, so you do not have to write the same context setup from scratch each session. Chapter 10 covers context files — the formalized version of decisions.md that makes Stage 1 nearly instantaneous. Chapter 11 covers multi-agent coordination — running multiple loop sessions in parallel, which is how Claude Code subagents become useful.

All of that builds on what you just did: one loop, five stages, one feature, fourteen tests, decisions documented.

---

*The loop does not make you faster. It makes you traceable — which is what lets you go faster for longer.*
