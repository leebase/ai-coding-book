# Chapter 2: Define Requirements Before You Build

In Chapter 1, you wrote a planning brief that answered: *what are we building?* Now you need to add a feature, and that question has an answer — the task manager exists. The question changes: *what must this specific feature do?*

That is a requirement. It is not the same thing as a plan.

---

## A Plan and a Requirement Are Different Things

A plan tells the AI what to build. A requirement tells the AI how to verify that it built it correctly.

Without a requirement, "working" is undefined. The AI will implement something that runs and looks reasonable. You look at the result and think: *that is not quite what I meant*. But you cannot articulate why, because you never articulated what you did mean.

The mistake is not the AI's implementation. The mistake is evaluating the output against a mental model you never made explicit. You cannot test a requirement you never wrote.

**A requirement is a statement you can test as true or false.**

Non-verifiable: "Users should be able to set task priority." You cannot test this. There are a dozen ways to implement it, and any of them satisfies the statement.

Verifiable: "Running `python tasks.py add "Buy groceries" --priority high` adds a task and `list` displays it as `[high] Buy groceries`." Either it does or it does not. No interpretation required.

---

## The Failure Path: Adding Priority Without a Requirement

Your task manager from Chapter 1 has four commands. A reasonable next feature: let users mark tasks as high, medium, or low priority.

Open Antigravity and open your task manager project from Chapter 1. In the agent sidebar, type:

```
Add priority levels to tasks.
```

> **What the Agent Will Do:** The agent will modify `tasks.py` and update `tasks.json` handling. It will make a series of decisions you did not make: whether priority is set at creation or edited later, what the valid values are, what the default is, how priority appears in the list output, whether the list sorts by priority, and how existing tasks without priority are handled.

> **Watch For:** How the agent chose to implement the `add` command. Does it use a flag? A positional argument? A prompt? Look at the `list` output format — what does priority look like? Open `tasks.json` and look at the schema it chose.

When the agent finishes, run a few commands and examine what you got:

```bash
python tasks.py add "Buy groceries"
python tasks.py add "Fix critical bug"
python tasks.py list
```

The agent probably built something functional. But look carefully at the decisions embedded in that implementation:

- Did it use `--priority` as a flag, or something else?
- What is the default priority for a task added without specifying one?
- How are existing tasks (from before priority was added) handled?
- Does `list` sort by priority, or just display it?
- What happens if you pass an invalid priority value?

You did not make any of these decisions. The agent did. You will only discover the mismatches later, when the feature does not behave as you expected.

> **Free Tier Note:** At this point you might be tempted to issue corrections — "actually, use a flag," "sort the list by priority." Each correction is another prompt, another rate limit draw, and another opportunity for the agent to introduce new assumptions. You are debugging a mental model you never wrote down.

Stop here. Do not fix it. You are going to start over with a requirement.

---

## What Makes a Requirement Verifiable

A verifiable requirement has four properties:

**1. Specific input.** What exactly does the user type or provide? Not "the user sets a priority" — `python tasks.py add "description" --priority high`. Exact syntax.

**2. Specific output.** What exactly does the user see? Not "priority is displayed" — `[high] Buy groceries` as the list format. Exact format.

**3. Defined edge cases.** What happens at the boundaries? What if no priority is specified? What happens with an invalid value? What about tasks created before this feature existed?

**4. Defined scope boundary.** What is explicitly *not* part of this feature? This prevents the AI from adding related things you did not ask for.

A requirement that has all four properties is testable before the agent writes a single line. You can read it and answer: "If the agent implements exactly this, will I be satisfied?" If yes, it is a good requirement. If you are still unsure, the requirement is not specific enough yet.

---

## Writing the Priority Requirement

Apply the four properties to the priority feature:

---

*Feature:* Task priority levels

*Specific input:*
- `python tasks.py add "description" --priority high` sets priority to high
- `python tasks.py add "description" --priority medium` sets priority to medium
- `python tasks.py add "description" --priority low` sets priority to low
- `python tasks.py add "description"` (no flag) sets priority to medium by default
- Any value other than `high`, `medium`, or `low` prints an error and exits without adding the task

*Specific output:*
- `list` displays each task as: `[ID] [priority] description` — for example: `[1] [high] Buy groceries`
- Completed tasks display as: `[1] [high] [done] Buy groceries`

*Edge cases:*
- Tasks in `tasks.json` that have no `priority` field (created before this feature) display as `[medium]` without modifying the stored data

*Scope boundary:*
- `list` does NOT sort by priority — tasks appear in creation order
- No command to change a task's priority after creation
- No filtering tasks by priority

---

That requirement took about ten minutes to write. Every decision the agent made for you in the failure path is now made by you in writing. The agent's job is to implement this — not to interpret it.

Notice also the edge case: existing tasks must display as medium priority without rewriting their stored data. That is a backward compatibility requirement. If you do not specify it, the agent will handle it some way. Maybe correctly. Maybe not. Now you control the outcome.

---

## The Success Path: Building to a Requirement

Stay in the same project folder — your `tasks.py` and `tasks.json` from Chapter 1 should still be there. Start a new agent session by clicking the new conversation icon at the top of the agent sidebar (it looks like a compose or plus icon). This keeps the existing code but gives the agent a clean context with no memory of the failure path session.

> **Free Tier Note:** Starting a new agent session resets the agent's context. This is intentional — you are giving the agent a complete requirement, so it does not need the history of the failure path session.

Your prompt is the requirement, prefaced with context. Copy this exactly — the precision is the point:

```
I have an existing Python CLI task manager in tasks.py. The current schema in
tasks.json is: {"id": 1, "description": "Buy groceries", "done": false}

Add priority levels to this existing implementation with the following
specification exactly:

Feature: Task priority levels

Input:
- python tasks.py add "description" --priority high/medium/low
- Default priority when flag is omitted: medium
- Invalid priority values print an error and exit without adding the task

Output:
- list displays: [ID] [priority] description
  Example: [1] [high] Buy groceries
- Completed tasks: [1] [high] [done] Buy groceries

Edge cases:
- Existing tasks.json entries with no priority field display as [medium]
  without modifying the stored data

Out of scope:
- No sorting by priority
- No changing priority after creation
- No filtering by priority
```

> **What the Agent Will Do:** The agent will read `tasks.py`, understand the existing structure, and modify it to add the `--priority` flag to the `add` command and update the `list` display. It should not restructure the file or change other commands.

> **Watch For:** The agent asking clarifying questions — if your requirement is complete, it should not need to. An agent that asks no questions on a well-specified requirement is confirmation that the requirement was specific enough.

When the agent finishes, verify each property of your requirement:

```bash
# Test default priority
python tasks.py add "Buy groceries"
python tasks.py list
# Expected: [1] [medium] Buy groceries

# Test explicit priorities
python tasks.py add "Fix critical bug" --priority high
python tasks.py add "Update README" --priority low
python tasks.py list
# Expected: three tasks with correct priority labels, creation order

# Test invalid value
python tasks.py add "Test task" --priority urgent
# Expected: error message, task not added

# Test done display
python tasks.py done 1
python tasks.py list
# Expected: [1] [medium] [done] Buy groceries

# Test backward compatibility
# In Antigravity's file explorer (left panel), click tasks.json to open it.
# Remove the "priority" field from one task entry so it looks like the
# original Chapter 1 format: {"id": 1, "description": "Buy groceries", "done": false}
# Save the file (Cmd+S / Ctrl+S), then:
python tasks.py list
# Expected: that entry displays as [medium] without you having added priority to it
```

> **Watch For:** Each test matching the requirement exactly. If something does not match, you now have a specific, testable mismatch — not a vague "it seems off." Go back to the requirement, find the property that failed, and issue a targeted correction quoting the requirement and the observed behavior.

---

## Debrief

Look at what just happened. You made a product decision — priority is set at creation, not editable after; list is unsorted; invalid values error — and the AI implemented your decision. In the failure path, the AI made those same decisions. You just did not know what they were until you looked.

This is the shift that requirements create. Without them, you are a tester discovering someone else's design decisions after they are already built. With them, you are the product owner verifying your own decisions were implemented correctly.

**A requirement is not documentation. It is specification.** You are not writing it to record what was built. You are writing it to define what will be built — before the agent writes a line.

Every feature you add to this task manager from here will follow this pattern: write the requirement first, then prompt. Not as bureaucracy. As precision.

In Part 2, you will see how requirements connect to a larger document system that persists across sessions and lets any AI — or any collaborator — pick up exactly where you left off. The requirement you just wrote is a backlog item in everything but name. The reason AgentFlow works across tools and sessions is that the decisions live in files, not in your head or the AI's memory. You have already started doing this — you just did not have a name for it yet.

---

*The AI executes. You decide what done means. A requirement is how you make that decision stick.*
