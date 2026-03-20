# Chapter 11: Multi-Agent Coordination

Until now you have used a single Claude Code session at a time. That is the right default. It keeps the loop tight and the context manageable.

Claude Code also supports subagents with fresh, separate context windows. They are the right tool when you want parallel work without dumping every branch of the task into one conversation. You have not used it yet because you did not need to. After ten chapters, the task manager is feature-complete and you have a mature context file. Now the conditions are right.

To use subagents, either ask Claude directly to delegate part of the work to a subagent, or use `/agents` to create a reusable specialist first. Each subagent runs with fresh context and returns a summary to the main session.

Claude Code subagents are useful for exactly one situation: **genuinely independent work**. If Agent A and Agent B have no overlapping file writes, they can run in parallel without coordinating. Agent A's session does not know what Agent B is doing — which means they cannot negotiate, they cannot wait for each other, and they cannot merge their own changes. That is the human's job.

The discipline from Chapter 6 (explicit scope) is what makes parallelism safe. Without it, two agents working on the same project without shared context about who owns which file will produce conflicts — not immediately visible, but present in the merged result.

---

## When Parallelism Is Safe

The safety rule for multi-agent work is a single constraint:

**No two agents should write to the same file in the same session.**

Reading the same file is safe. Both agents can read `context.md` and `decisions.md` simultaneously without conflict — they are not modifying the files, just consuming them. Writing is different. If both agents write to `tasks.py`, the second agent's write overwrites or ignores the first, depending on timing and Claude Code's file handling. You will not see an error. You will see one agent's changes missing from the final result.

The way you enforce this rule is the same way you have been preventing scope creep since Chapter 6: explicit "Does NOT" statements in each agent's prompt. "Agent A modifies only tasks.py and test_tasks.py. Agent B creates only COMMANDS.md." Each agent knows its boundary. Neither wanders.

Two additional conditions make parallel work tractable:
- **Independent requirements**: Each task is specifiable without reference to the other. If Agent B needs to know what Agent A built before it can start, they are not independent.
- **Shared context**: Both agents read from the same context.md. They may not know what the other is doing, but they know the same project state and constraints.

When these conditions hold, parallel agents are an efficiency gain. When they do not, serialization is safer.

---

## The Failure Path: Unscoped Parallel Agents

Stay in your main Claude Code session and explicitly delegate to two subagents with non-overlapping write scopes. Tell one subagent it owns the code change. Tell the other it owns the documentation change.

Send each agent the same vague prompt:

**Subagent 1:**
```
Update the task manager to add filtering to the list command.
```

**Subagent 2:**
```
Update the task manager to improve its output formatting.
```

> **What the Agents Will Do:** Both agents will read `tasks.py`. Both will make changes. Agent 1 may add a `--filter` flag. Agent 2 may reformat the `list` output. Both changes touch the same function. When Agent 2 writes its changes to `tasks.py`, it may overwrite Agent 1's filter flag — or Agent 1 may not have finished yet, writing on top of Agent 2.

> **Watch For:** Open `tasks.py` after both agents indicate they are done. Check whether both changes are present. One or both may be missing. Run:

```bash
pytest tests/ -v
```

> **Watch For:** Unexpected test failures. The file may be in a state that neither agent intended — one agent's output plus a fragment of the other's.

Stop here. This is the conflict that scope discipline prevents.

---

## The Success Path: Scoped Parallel Agents

Two tasks, genuinely independent:
- **Agent A**: Add `--priority` filter to `list` (e.g., `list --priority high` shows only high-priority tasks). Modifies `tasks.py` and `test_tasks.py`.
- **Agent B**: Create `COMMANDS.md` — a reference document of all commands with usage and examples. Creates a new file only.

Stay in the main session and create two subagent tasks.

**Send Agent A this prompt:**

```
[paste your full context.md here]

Task for Agent A: Add --priority filter to list command.

SCOPE: Modify ONLY tasks.py and test_tasks.py. Do not create or modify any other files.

Feature: --priority filter on list
Input: python tasks.py list --priority high (or medium or low)
Output: Only tasks matching that priority, same format as regular list.
Default (no --priority flag): unchanged — shows all tasks.

Edge cases:
- Invalid priority value: print error, exit non-zero (consistent with add command)
- --priority can be combined with --format json
- If no tasks match the filter: No tasks with priority 'high'.

Add exactly 1 new test:
- list --priority high shows only high-priority tasks

All 15 existing tests must still pass.
```

**Send Agent B this prompt:**

```
[paste your full context.md here]

Task for Agent B: Create COMMANDS.md reference documentation.

SCOPE: Create ONLY a new file named COMMANDS.md. Do not modify tasks.py, test_tasks.py, or any existing file.

Write a concise command reference for the task manager covering all 8 commands:
add, list, done, delete, overdue, search, stats, clear

For each command include:
- Command name and usage syntax
- Brief description (one sentence)
- Example with expected output

Format: markdown, one section per command. Keep it short — this is a reference, not a tutorial.
```

> **What the Agents Will Do:** Agent A will add the `--priority` flag to the argument parser, add a filter step to the `list` handler, and write one new test. Agent B will write COMMANDS.md from scratch, reading context.md to get the command list and schema. Neither agent touches the other's files.

> **Watch For:** Both subagents running in parallel. You do not need to alternate between them; let them run, then review the summaries and changed files.

When both agents indicate completion, verify each independently.

**Verify Agent A:**

First confirm Agent A stayed in scope — open `tasks.py` and check that the formatting of existing functions is unchanged from what you expect. Agent B was not supposed to touch this file, but a quick sanity check takes ten seconds.

```bash
pytest tests/ -v
```

> **Watch For:** 16 tests passing. Then manually:

```bash
python tasks.py add "Buy groceries" --priority medium
python tasks.py add "Fix critical bug" --priority high
python tasks.py list --priority high
# Expected: Only [2] [high] Fix critical bug

python tasks.py list --priority urgent
# Expected: Error message, non-zero exit
```

**Verify Agent B:**

Open `COMMANDS.md` in your editor. Read it. Check:
- All 8 commands covered?
- Usage syntax matches actual commands?
- Examples are realistic?
- Nothing in the document contradicts a decision in decisions.md?

---

## The Merge Review

Both agents produced correct output independently. Now you review them as a pair before the session is complete.

The merge review has one question that single-agent review does not: **do the two outputs conflict?**

In this case they should not — one modified code, one created documentation. But check:
- Does COMMANDS.md document the `--priority` filter on `list`? It should, since Agent B had context.md and the filter now exists in the project. If Agent B finished before Agent A and did not know about the filter, the documentation is already incomplete. Note this for the Stage 5 update.
- Do the tests Agent A wrote conflict with anything in the existing test suite? Run the full suite one more time to confirm.

Update context.md to reflect the new state:

```
- Tests: 16 passing
- Commands: add (--priority, --due), list (--format json, --priority), done, delete, overdue, search, stats, clear
```

Add a decisions.md entry:

```markdown
## Priority filter
- **Decision**: list --priority filters by exact value; invalid priority errors.
- **Reason**: Consistent with add --priority validation (Ch 2 decision).
- **Rules out**: Fuzzy match, multiple priority values, silent filtering.
```

If COMMANDS.md did not include the `--priority` filter, return to a single Claude Code session and issue a targeted correction:

```
Add --priority to the list command's entry in COMMANDS.md.
Usage: python tasks.py list --priority high|medium|low
Description: Filter tasks by priority. Invalid value prints error.
```

---

## Debrief

Two agents, two tasks, one session. The throughput advantage is real — both tasks completed in the time one would have taken. The coordination cost is also real: you had to specify scope explicitly for each agent, monitor both sessions, and review both outputs as a pair before updating context.md.

**Parallel agents multiply throughput when scopes are clean. They multiply problems when they are not.** The discipline that makes this work is not multi-agent-specific — it is the same scope discipline from Chapter 6 and the same review discipline from Chapter 4. The only thing that changes at scale is that you apply those disciplines to two agents at once instead of one.

Claude Code subagents become useful when you have a backlog of independent tasks. In Chapter 12, you will see how to identify those tasks systematically — which is what sprint planning is for. A sprint is not just a time box. It is an analysis of what work is truly independent, so you know which tasks can run in parallel and which must serialize.

---

*Parallelism is a throughput multiplier, not a coordination shortcut. The discipline still runs once per agent.*
