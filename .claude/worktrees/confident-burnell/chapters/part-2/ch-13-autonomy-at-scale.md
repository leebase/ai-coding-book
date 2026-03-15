# Chapter 13: Autonomy at Scale

Mode 1, Mode 2, Mode 3. You have the options. The question Chapter 9 left open is: how do you choose?

The temptation is to pick one mode and stick with it. Always Mode 1 if you are cautious. Always Mode 3 if you are optimistic. Neither is right. The correct mode is a function of the task — specifically, of three factors that change from task to task and from project to project.

**Factor 1: Task definition.** How well-specified is the requirement? A flag with explicit behavior, exact output format, and a "Does NOT" list is tightly defined. A schema change that touches stored data and backward compatibility is inherently riskier — even with a good requirement, the implementation has more ways to go wrong.

**Factor 2: Context maturity.** Is context.md current? Is decisions.md complete? Does the agent have everything it needs to make correct choices without asking? A mature context means the agent starts informed. A stale or thin context means the agent fills gaps with guesses.

**Factor 3: Test coverage.** If the agent makes a mistake, will the tests catch it? A high-coverage test suite is a safety net for high-autonomy sessions. If tests only cover happy paths, Mode 3 will eventually produce an error that passes all tests and ships to users.

All three factors high → Mode 3 is appropriate. Any one low → dial back. This is the calibration, not a rule.

---

## The Calibration Heuristic

Before each session, answer three questions:

| Factor | High | Low |
|--------|------|-----|
| Task definition | Tight requirement, existing pattern | Schema change, new behavior, unclear edge cases |
| Context maturity | context.md current, decisions.md complete | Stale state, gaps in decision log |
| Test coverage | Tests cover the error cases this task might produce | Happy-path coverage only |

Map the result to a mode:
- **All three high** → Mode 3 (full loop, human reviews output)
- **Two of three high** → Mode 2 (implement + verify auto, human reviews diff)
- **Any one low** → Mode 1 (human at every stage)
- **Multiple low** → Mode 1 with extra care; consider breaking the task into smaller pieces first

This is a heuristic, not an algorithm. A schema change almost always pushes toward Mode 1 regardless of the other factors, because the cost of a bad schema migration is high and tests rarely cover the full migration edge case space.

---

## Mode 2 in Practice: --done Filter

**Task**: Add `--done` filter to `list`. Shows only completed tasks. One new test. 19 tests total.

**Calibration:**
- Task definition: tight. Existing `--priority` filter is the exact pattern; same output format.
- Context maturity: context.md is current (18 tests, all commands listed).
- Test coverage: the `--priority` filter test covers the filter pattern; this is the same logic.

**Verdict**: Mode 2. Let the agent implement and run tests. Review the diff at Stage 4.

Open a new agent session (new conversation icon at the top of the agent sidebar). Paste your context.md and add the requirement:

```
[paste your full context.md here]

Mode: Implement and verify. Run tests after implementing. I will review the diff.

Feature: --done filter on list
Input: python tasks.py list --done (shows only done=true tasks)
Output: Same format as list; only completed tasks shown.
        If no completed tasks: No completed tasks.

Edge cases:
- --done can combine with --priority and --format flags
- --done with --priority: show completed tasks with that priority
- Invalid combination still respects error behavior

Does NOT:
- Change default list behavior
- Add any other filter flags

Add exactly 1 new test:
- list --done shows only completed tasks

All 18 existing tests must still pass.
```

> **What the Agent Will Do:** Because you specified "Implement and verify," the agent will interpret this as an instruction to proceed through Stages 2 and 3 without pausing — it will build the feature, run the test suite, and report back the results without stopping for confirmation.

> **Watch For:** The agent's test report. It should show 19 tests passing. If it reports failures, it will describe them — issue a targeted correction.

When the agent reports success, run the tests yourself to confirm:

```bash
pytest tests/ -v
```

> **Watch For:** 19 tests passing. Then Stage 4 — read the diff. Open `tasks.py` and find the `--done` filter implementation. Is it the same pattern as `--priority`? Are there any extra flags or conditions you did not specify?

Update context.md: `Tests: 19 passing`.

---

## Mode 1 in Practice: Tag Field

**Task**: Add optional `tag` field to tasks. Tasks can be tagged with a string (e.g., "work", "personal"). Schema change.

**Calibration:**
- Task definition: reasonably tight, but it is a schema change. The backward compatibility requirement (existing tasks with no `tag` field should display without tag — same as missing `priority` from Ch 3) adds implementation complexity.
- Context maturity: good.
- Test coverage: the missing-field default test from Ch 3 covers the pattern, but a schema change expands the test surface.

**Verdict**: Mode 1. Human present at every stage. Review the schema change before proceeding.

### Stage 1: Start and Requirement

Write the requirement before opening a session:

---

*Feature:* Tag field

*Input:*
- `add "description" --tag work` stores tag
- `add "description"` (no flag) stores `"tag": null`

*Output:*
- `list` shows `[tag: tagname]` after description when tag present: `[1] [medium] Buy milk [tag: personal]`
- `list` shows nothing extra when `tag: null`
- Completed tasks: `[1] [medium] [done] Buy milk [tag: personal]`
- Due date + tag: `[1] [medium] Buy milk [due: 2026-04-01] [tag: personal]`

*Edge cases:*
- Existing tasks with no `tag` field: display without tag (no error, no migration)

*Scope boundary:*
- Does NOT filter by tag (not yet)
- Does NOT search by tag
- No tag editing after creation

---

### Stage 2: Implement

Open a new agent session (new conversation icon at the top of the agent sidebar). Paste context.md and the requirement. Add explicitly:

```
Mode: Stage by stage. After implementing, stop before running tests.
I will review the schema change before proceeding.
```

> **What the Agent Will Do:** The agent will add `--tag` to the `add` command, update the task object construction, and modify the `list` display. It will stop before running tests because you specified Mode 1.

> **Watch For:** The agent's proposed schema change. Before moving on, open `tasks.py` and answer:
> 1. Is `tag` stored as `null` when not provided (not as an empty string or omitted entirely)?
> 2. Does the `list` display use `.get("tag")` or equivalent — not `task["tag"]` — to handle missing fields safely?
> 3. Is the display order correct: description, then due date, then tag?

If all three are correct, send a follow-up message in the same session: "Everything looks good — please run the test suite now."

### Stage 3: Verify

Tell the agent to run the tests (or run them yourself):

```bash
pytest tests/ -v
```

> **Watch For:** 20 tests passing. Then manually verify backward compatibility:

```bash
# In the Antigravity file explorer, open tasks.json
# Find an existing task entry and remove the "tag" field entirely
# Save (Cmd+S or Ctrl+S), then:
python tasks.py list
# Expected: the task displays without any tag — no error, no "[tag: null]"
```

### Stage 4: Review

Read the diff. Specifically: does `list` handle `due_date` before `tag` in the output? Is the display consistent with the requirement's examples?

### Stage 5: Update

Add to decisions.md:

```markdown
## Tag field
- **Decision**: tag is stored as null when not provided; displayed as [tag: name] when present.
- **Reason**: Consistent with due_date and priority patterns — null = not set, display nothing.
- **Rules out**: Empty string for no tag, auto-migration of existing tasks.
```

Update context.md: `Tests: 20 passing`. Add `tag` to the schema line.

---

## Mode 3: When and Why

Mode 3 — the full loop, all five stages, minimal human checkpoints — is appropriate when all three calibration factors are high and the task is low-risk.

A documentation update is a good example. Ask the agent to update COMMANDS.md to include the `--done` filter and the `--tag` flag you just added.

Open a new agent session. Give it context.md and the instruction:

```
[paste your full context.md here]

Update COMMANDS.md to document two new options:
1. list --done: shows only completed tasks
2. add --tag <name>: optional tag for a task; list shows [tag: name] when set

Mode: Full loop. Complete the update, verify the file looks correct,
and report back when done.
```

> **What the Agent Will Do:** The agent will read COMMANDS.md, add the two new entries, review its own output for accuracy, and report completion. You review the final COMMANDS.md.

> **Watch For:** The entries matching your requirements exactly — correct syntax, correct output format shown. If any entry is wrong, issue a targeted correction. The bar for Mode 3 on documentation is that the output is reviewable in under two minutes.

**The Mode 3 constraint:** Documentation is safe for Mode 3 because no test can fail and no stored data changes. For code changes, Mode 3 requires test coverage that would catch any mistake the agent might make. If your test suite does not test the behavior the agent might break, Mode 3 shifts the risk to the user.

**Invisible drift** is the failure mode specific to Mode 3: the agent runs all five stages, all tests pass, and the implementation quietly violates a decision from decisions.md that no test enforces. This is why decisions.md must be in the context and why the calibration factors matter. Mode 3 is not "let the AI do whatever it wants." It is "I trust that the context, the tests, and the requirement are complete enough that the AI can run the loop safely."

---

## Debrief

Three tasks, three modes. The modes did not change the discipline — the requirement was still written before implementation, the tests still ran, the diff was still read. What changed was the distribution of work between human and AI across the five stages.

**Autonomy is earned, not granted.** The path to Mode 3 is:
1. Build complete context.md and decisions.md (Chapters 7 and 10)
2. Write requirements that leave no room for guessing (Chapter 2)
3. Build a test suite that covers error cases, not just happy paths (Chapter 3)
4. Run enough Mode 1 sessions to develop confidence in the agent's judgment on this project

When all four are in place, Mode 3 is safe for routine, well-understood tasks. It is not safe for schema changes, new commands, or anything that expands the project's decision surface.

Chapter 14 brings all of this together — not as a new technique, but as a synthesis. The task manager, the loop, the skills, the context files, the sprint cadence, the autonomy modes — one system, working as a whole.

---

*Autonomy is calibrated, not maximized. The right mode is the one that matches the task's risk to your safety net's coverage.*
