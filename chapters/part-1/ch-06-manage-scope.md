# Chapter 6: Manage Scope

Every feature you ask an AI to build creates an opportunity. Not just for that feature — for all the features adjacent to it that the AI thinks you probably also want.

Search is a good example. If you ask an AI to add search to the task manager, it will implement search. It will also likely add a `--case-sensitive` flag, a filter for completed tasks, output highlighting for matched terms, and possibly a `--limit` flag for capping results. All useful. None of what you asked for.

This is gold-plating — the AI adding polish and adjacent features beyond what was specified. It is not malicious. It is the AI being helpful based on what search usually means in a real application. The problem is that each addition is untested, undocumented, and potentially in conflict with what you actually wanted. You specified nothing, so the AI filled in.

**Gold-plated features are liability, not value.** They cost more to verify than to skip. They introduce surface area for bugs you did not write requirements for. They expand your mental model of a codebase you are trying to keep small.

The fix is the same as the fix for bad requirements: make the scope explicit before you prompt. Not just what the feature does — what it does not do.

---

## The Gold-Plating Problem

Your task manager now has eleven passing tests and a growing feature set: add with priority and due date, list with formatted output, done, delete, and overdue. A reasonable next feature: search. Users want to find tasks by description text.

Before you write the requirement, do the failure path. Open Antigravity and start a new agent session (new conversation icon at the top of the agent sidebar). Type:

```
Add a search command to the task manager.
```

> **What the Agent Will Do:** The agent will read `tasks.py` and add a `search` command. It will also make decisions you did not make — about case sensitivity, about whether to search completed tasks, about how matches are displayed, and possibly about result limits. Watch how many of these decisions it makes without being asked.

> **Watch For:** The agent adding flags or options you did not request. Specifically: `--case-sensitive`, `--include-done` or similar filter, color or bracket highlighting of matched terms, or a `--limit` flag.

When the agent finishes, run a quick manual test in the terminal panel:

```bash
python tasks.py search "buy"
```

Look at the output. If the agent added highlighting, you will see markers around the matched text. If it added flags, the help text may show them. Now run the tests:

```bash
pytest tests/ -v
```

> **Watch For:** Failing tests. The agent may have changed the `list` output format to add match highlighting — which breaks tests that check output format. Or it may have added flags that conflict with how the argument parser handles existing commands.

> **Free Tier Note:** You are now in a debugging session you did not plan for. Each correction is another prompt. The corrections may fix one test and surface another issue. You are untangling decisions the agent made without a specification.

Stop here. Note what the agent added that you did not ask for. Then start over with a requirement.

---

## Scope as Part of the Requirement

The fix is to treat scope as a first-class part of every requirement — not an afterthought.

In Chapter 2, you saw the scope boundary as one of the four required properties: what is explicitly *not* part of this feature. You used it to tell the agent not to sort by priority, not to allow editing priority, not to filter by priority. Those constraints prevented three plausible features the agent might have added.

For search, the scope boundary does more work. Search is a feature with obvious extensions — case options, filters, highlighting, sorting by relevance. Each one is adjacent enough that an agent building a real application would consider it in scope. You need to be explicit that you are not building those yet.

A scope boundary works because it gives the agent a constraint it cannot argue with. Without it, the agent defaults to *what would a complete search feature look like?* With it, the agent defaults to *what exactly did the user specify?*

Here is the requirement for search with an explicit scope boundary:

---

*Feature:* Search command

*Specific input:*
- `python tasks.py search "text"` — case-insensitive substring match against task descriptions

*Specific output:*
- Matching tasks displayed in the same format as `list`: `[ID] [priority] description [due: date]`
- If no tasks match: `No tasks match "text".`

*Edge cases:*
- Search is always case-insensitive — no flag needed or allowed
- Completed tasks are included in results
- Tasks with no description match are excluded

*Scope boundary:*
- Does NOT highlight or mark matched text in output
- Does NOT filter by priority, done status, or due date
- Does NOT sort results by relevance
- Does NOT support regex — substring match only

---

Four explicit "Does NOT" statements. Each one closes off an extension the agent might otherwise add.

Notice the format is the same as Chapter 2: specific input, specific output, explicit edge cases, explicit scope. The scope section grew because search has more natural extensions than priority did. The work you do in the scope boundary is proportional to how tempting the feature is to over-engineer.

---

## The Success Path: Scoped Search

Start a new agent session (new conversation icon at the top of the agent sidebar). Give the agent the full state and the scoped requirement:

```
I have a Python CLI task manager in tasks.py with 11 passing tests.
Current commands: add (--priority, --due), list, done, delete, overdue.
tasks.json schema: {"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}

Add a search command with the following specification:

Feature: Search tasks by description
Input:
- python tasks.py search "text" — case-insensitive substring match against description

Output:
- Matching tasks in the same format as list: [ID] [priority] description [due: date]
- If no matches: No tasks match "text".

Edge cases:
- Always case-insensitive (no flag)
- Completed tasks included in results
- Non-matching tasks excluded

Does NOT:
- Highlight matched text in output
- Filter by priority, done status, or due date
- Sort results by relevance
- Support regex — substring match only

Add exactly 1 new test:
- search returns matching tasks in list format, case-insensitive

All 11 existing tests must still pass.
```

> **What the Agent Will Do:** The agent will add a `search` command that filters tasks by substring match and formats output identically to `list`. The explicit scope boundary should prevent it from adding flags or altering the output format.

> **Watch For:** The agent's implementation after it finishes — open `tasks.py` and look at the `search` command. If it added `--case-sensitive` or any other optional flag despite the scope boundary, the implementation drifted from the requirement. Issue a targeted correction quoting the "Does NOT" line before moving on.

Verify:

```bash
pytest tests/ -v
```

> **Watch For:** 12 tests passing. Then manually verify the command:

```bash
# Add tasks if tasks.json was cleared
python tasks.py add "Buy groceries" --priority medium
python tasks.py add "Fix critical bug" --priority high
python tasks.py add "Update the readme" --priority low

# Test basic search
python tasks.py search "readme"
# Expected: [3] [low] Update the readme

# Test case insensitivity
python tasks.py search "BUY"
# Expected: [1] [medium] Buy groceries

# Test no match
python tasks.py search "xyz"
# Expected: No tasks match "xyz".

# Test that completed tasks appear in results
python tasks.py done 1
python tasks.py search "groceries"
# Expected: [1] [medium] [done] Buy groceries
```

> **Watch For:** Output format matching `list` exactly — same brackets, same priority label, same `[done]` indicator. If anything differs, the agent added its own formatting. Issue a targeted correction with the exact expected output.

---

## Debrief

One command. One new test. Twelve total. The agent stayed in scope because the scope was specified.

Compare this to the failure path, where the agent's interpretation of "search" included features you did not ask for. None of those were wrong — they were reasonable decisions about what a complete search feature should do. They just were not your decisions. The agent made them in the absence of explicit guidance.

**Scope is a product decision, not a cleanup task.** Every "Does NOT" statement in a requirement is a decision you made before the agent could make it for you. The agent cannot know which adjacent features you want and which you do not — unless you tell it.

The discipline generalizes. Every feature you add from here has a natural set of extensions — the next obvious steps an agent would consider if you left scope undefined. Your job before each prompt is to identify those extensions and explicitly exclude the ones you are not building yet.

Notice what happened to the features you excluded: they did not disappear. Relevance sorting, regex support, done-status filtering — those are all potential future features, now named and parked. In Part 2, that list of parked features becomes a formal backlog. The scope boundary is not a way to kill features. It is a way to defer them on your terms instead of building them without planning.

---

*Specify what you are not building. The AI will build it anyway if you don't.*
