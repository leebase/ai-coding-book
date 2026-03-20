# Chapter 12: The Sprint Cadence

You have been running sprints without calling them that.

Look at how this book is structured. Each chapter is a unit of work with a goal, a scenario, a definition of done, and a commit at the end. You planned chapters before writing them. You reviewed them before committing. You updated the sprint plan after each one. That is a sprint cadence — a recurring cycle of plan, execute, review, repeat.

Now apply it to software. A session is one loop: Start, Implement, Verify, Review, Update. A sprint is several sessions grouped around a coherent goal. The sprint cadence is the rhythm that governs which sessions run, in what order, and when the sprint is done.

**Without a cadence, you optimize sessions but not the project.** Each session is locally fine — good requirement, clean implementation, tests passing. But there is no global view: features accumulate without a theme, decisions that should have been made together get made in isolation, and the backlog grows unchecked because nothing ever closes.

The sprint cadence closes things. Plan the sprint, execute the sprint, review the sprint, update context. Then plan the next one.

---

## What Sprint Planning Produces

A sprint plan is not a Gantt chart. It is a one-page analysis that answers five questions before you open Claude Code:

**1. What is the sprint goal?**
One sentence. Not a list of features — the reason this set of features belongs together. "Export capabilities" is a goal. "Add --format csv, export command, and fix the priority filter bug" is a task list, not a goal.

**2. What features are in scope?**
List the specific features. Each one maps to a requirement you will write before implementing. Anything not on the list is out of scope for this sprint — it goes to the backlog.

**3. What are the dependencies?**
Which features depend on other features being done first? A `--format csv` flag on `list` depends on nothing. An `export` command that produces the same format as `--format csv` depends on the CSV format decision being made first — but not necessarily on `--format csv` being fully built.

**4. Which tasks can run in parallel?**
If two features have no shared file writes and no dependency between them, they are parallelism candidates. Identify them explicitly. This is the sprint planning analysis that makes Chapter 11's Claude Code subagents useful at scale.

**5. What is "done" for this sprint?**
State the exit criteria before starting. Not "it feels finished" — a specific count of tests, a specific set of commands, a specific update to context.md. If you cannot state done before starting, the sprint scope is not clear enough.

---

## The Failure Path: No Plan

The task manager needs export capabilities. Two features: `--format csv` on `list`, and an `export` command that writes tasks to a CSV file.

Jump straight in. Ask Claude to use two subagents immediately, giving each only a rough description:

**Agent A:**
```
Add CSV output to the task manager.
```

**Agent B:**
```
Add an export command to the task manager.
```

> **What the Agents Will Do:** Agent A may add `--format csv` to `list`. It will choose a CSV format — fields, order, header row. Agent B will add an `export` command. It will also choose a CSV format. They will almost certainly choose differently, because neither agent knows what the other decided.

> **Watch For:** After both agents finish, compare their CSV output formats. Run:

```bash
python tasks.py list --format csv
python tasks.py export tasks.csv && cat tasks.csv
```

> **Watch For:** Different field orders, different header rows, or different handling of null fields (`due_date: null` becomes an empty string? The word "null"? Omitted?). Two agents, two CSV formats, one broken sprint.

Stop here. The conflict is in the format decision — which should have been made once, in the sprint plan, before either agent started.

---

## Writing the Sprint Plan

Before opening Claude Code, write a `sprint-plan.md` in your project using your editor or `touch sprint-plan.md`. Use this structure:

```markdown
# Sprint: Export Capabilities

## Goal
Give users two ways to get task data out of the system in a consistent format.

## Features
| Feature | Description | Test count |
|---------|-------------|------------|
| --format csv | Add CSV option to list command | +1 (total: 17) |
| export command | Write all tasks to a named CSV file | +1 (total: 18) |

## Dependency analysis
- CSV format (fields, header, null handling) must be decided before either feature is built.
- --format csv and export are otherwise independent — no shared file writes.
- Both can run in parallel after the format decision is made.

## CSV format decision
- Header row: id,description,done,priority,due_date
- Fields: all fields, always (consistent with JSON format decision)
- Null due_date: empty string in CSV
- Invalid format value: print error, exit non-zero (consistent with existing --format behavior)

## Parallelism plan
- Agent A: --format csv on list. Modifies tasks.py and test_tasks.py only.
- Agent B: export command. Modifies tasks.py and test_tasks.py only.
- Note: both agents modify the same files. Run sequentially, not in parallel.
  (The format decision is shared; same-file writes require serialization.)

## Definition of done
- 18 tests passing
- list --format csv and export produce identical CSV format
- context.md updated
- decisions.md updated with CSV format decision
```

Notice what the dependency analysis revealed: both agents would modify `tasks.py` and `test_tasks.py`. They cannot run in parallel. The sprint plan caught a would-be conflict before any code was written. Run Agent A first; then Agent B reads the completed implementation as context. Because both tasks write to the same files, use one Claude Code session at a time rather than parallel subagents for this sprint.

Save `sprint-plan.md` with Cmd+S or Ctrl+S.

---

## Executing the Sprint

### Session 1: --format csv (Agent A)

Start a fresh Claude Code session. Give the agent context and the requirement:

```
[paste your full context.md here]

Sprint context: Adding CSV export capabilities. See sprint-plan.md for the format decision.

Feature: --format csv on list
Input: python tasks.py list --format csv
Output: CSV with header: id,description,done,priority,due_date
        One row per task; null due_date = empty string; done = true/false

Does NOT:
- Sort output
- Filter output
- Change the default (no --format flag) behavior

Add exactly 1 new test:
- list --format csv produces correct CSV output with header row

All 16 existing tests must still pass.
```

> **What the Agent Will Do:** The agent will add CSV to the `--format` flag handler in the `list` command. It will format the output consistently with the JSON format: all fields, all tasks, no filtering.

Verify:

```bash
pytest tests/ -v
```

> **Watch For:** 17 tests passing. Then manually verify:

```bash
python tasks.py add "Buy groceries" --priority medium
python tasks.py add "Fix bug" --priority high --due 2026-04-01
python tasks.py list --format csv
# Expected:
# id,description,done,priority,due_date
# 1,Buy groceries,false,medium,
# 2,Fix bug,false,high,2026-04-01
```

### Session 2: export command (Agent B)

Start a fresh Claude Code session. Agent B runs after Agent A is verified:

```
[paste your full context.md here]

Sprint context: --format csv is already implemented and produces CSV with
header: id,description,done,priority,due_date. Null due_date = empty string.

Feature: export command
Input: python tasks.py export <filename>
Output:
- Writes all tasks to the specified file in the same CSV format as list --format csv
- Prints: Exported N tasks to <filename>.
- If no tasks: No tasks to export.
- If file already exists: overwrite without warning

Does NOT:
- Filter by priority, done status, or due date
- Ask for confirmation
- Support different output formats

Add exactly 1 new test:
- export writes correct CSV file with expected content

All 17 existing tests must still pass.
```

> **What the Agent Will Do:** The agent will add an `export` command that reuses the CSV formatting logic from `list --format csv`. Because the sprint plan defined the format explicitly and Agent A already implemented it, Agent B has a concrete reference for the exact output format.

Verify:

```bash
pytest tests/ -v
```

> **Watch For:** 18 tests passing. Then manually verify consistency:

```bash
python tasks.py export tasks-export.csv
cat tasks-export.csv
# Expected: same format as list --format csv — same header, same fields, same null handling
# (Or open tasks-export.csv in your editor to view the contents)
```

> **Watch For:** `list --format csv` and `export tasks.csv` producing identical format for the same task data. If they differ, the sprint goal is not achieved — two formats is the exact problem the sprint plan was written to prevent.

---

## Sprint Review

The sprint is done when:
- 18 tests pass ✅
- `list --format csv` and `export` produce identical CSV format ✅
- context.md is updated ✅
- decisions.md has a new CSV format entry ✅
- sprint-plan.md is marked complete or archived ✅

Update context.md:

```
- Tests: 18 passing
- Commands: add (--priority, --due), list (--format json/csv, --priority), done, delete, overdue, search, stats, clear, export
```

Add to decisions.md:

```markdown
## CSV format
- **Decision**: CSV header is id,description,done,priority,due_date. Null due_date = empty string.
- **Reason**: Consistent with JSON format (all fields, always). Matches --format csv and export.
- **Rules out**: Optional fields, different field order, null as "null" string.
```

Look at the backlog — features excluded from this sprint that were named and parked. What is the most coherent next sprint goal? That is the starting question for sprint planning, next cycle.

---

## Debrief

The sprint plan took fifteen minutes. It prevented a format conflict that would have taken longer than fifteen minutes to untangle. It also caught the parallelism trap — two agents that looked independent but were not, because they shared output files.

**Sprint planning is not overhead. It is front-loaded problem discovery.** The dependency analysis and format decision happened on paper, not in the middle of a debugging session. The definition of done made the sprint review a five-minute check rather than an open-ended question.

The cadence scales. A solo developer running one sprint per week accumulates coherent features, a living context.md, and a backlog that reflects deliberate deferral rather than forgotten ideas. A small team can run the same cycle — one shared context file, shared sprint plan, parallel agents when scopes are clean.

In Chapter 13, the cadence runs with reduced human involvement — higher autonomy modes, mature skills, complete context files. The discipline does not change. What changes is how much of each loop stage the AI runs versus the human.

---

*A sprint is the unit of coherence. Plan before you execute. Review before you close.*
