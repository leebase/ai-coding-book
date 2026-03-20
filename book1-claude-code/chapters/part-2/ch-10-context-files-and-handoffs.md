# Chapter 10: Context Files and Handoffs

Open `start-session.md`. Find the line that says `Tests: 14 passing`.

It is wrong. You have 15 tests now, after Chapter 9. Every new agent session you start with this skill sends stale context — the agent thinks you have fewer tests than you do.

You could fix it. Update the number to 15. But next session, after the next feature, it will be wrong again. The test count is embedded in the skill file, which means maintaining the skill is a second job that runs in parallel with maintaining the project. Forget once, and the agent works with wrong information.

This is the stale skill problem. And it points to a separation of concerns that skills did not handle: the *instructions* for how to start a session are stable — same requirement format, same "Does NOT" convention, same test-pass constraint. The *state* of the project changes every session. They should not live in the same file.

A context file is that separation: project state in one place, session instructions in another. The skill references the context file. You update the context file. The skill stays current without touching it.

---

## What context.md Is (and Is Not)

`context.md` is not a README. A README explains the project to someone who wants to use it — how to install it, what commands exist, what it does. context.md explains the project to someone who wants to continue building it — what state it is in right now, what decisions constrain it, and what is open or unresolved.

The audience for context.md is not a user. It is the next developer — which is usually you, two weeks from now, or an AI session starting fresh.

What context.md contains:

**Project overview** — one paragraph. What the project is and what it does. Stable — rarely changes.

**Current state** — test count, command list, data schema. Changes every session, or whenever a feature is added.

**Decision summary** — the key constraints from decisions.md, compressed. Not a replacement for decisions.md — a quick reference so the agent does not have to read the full decision log for every session.

**Open questions** — anything undecided that might affect future sessions. Empty is fine.

**Session marker** — when it was last updated. Helps you know if the file is stale.

That is it. Five sections. The file should be readable in under two minutes.

---

## Writing context.md

Create `context.md` in your project directory using your editor or `touch context.md`. Copy and fill in this template:

```markdown
# Task Manager: Project Context

## Overview
Python CLI task manager. Reads and writes tasks.json. Single-user, local storage.
Built across a tutorial series; feature-complete as of Chapter 9.

## Current state
- Tests: 15 passing
- Schema: {"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}
- Commands: add (--priority, --due), list (--format json), done, delete, overdue, search, stats, clear

## Key decisions
Full log: decisions.md
Summary:
- Invalid input → print error, exit non-zero. Never silently default.
- Missing fields → display defaults, never error or modify stored data.
- All dates: YYYY-MM-DD only. Overdue uses local system date, not UTC.
- Output: fixed format, all fields always shown. No optional output.
- List order: creation order always. No automatic sorting.
- Search: always case-insensitive. No flag.

## Open questions
None currently.

## Last updated
[today's date] — 15 tests, 8 commands
```

Save with Cmd+S or Ctrl+S.

Now update `start-session.md`. Remove the embedded state section and replace it with a reference:

```markdown
# Task Manager: Session Start

## Project state
See context.md for current project state, schema, and decision summary.

## Standard instructions
- New features require a requirement before implementation.
- Each session adds at most 2 new tests.
- All existing tests must pass after any change.
```

Three lines replaced with one reference. The test count no longer lives in start-session.md — it lives in context.md, which you update at the end of every session as part of Stage 5 of the loop. The skill does not go stale because it does not contain the state.

---

## The Failure Path: Thin context.md

Before testing the full context.md, see what a minimal version produces.

Start a fresh Claude Code session in your project directory. Paste only this:

```
Read this project context and tell me: (1) what the current state of the
project is, and (2) what the most natural next feature to add would be.

# Task Manager: Project Context
Tests: 15 passing
Schema: {"id": int, "description": str, "done": bool}
```

> **What the Agent Will Do:** The agent will describe the project state as best it can from the minimal context — 15 tests, basic schema. For the next feature, it will guess based on common task manager patterns: due dates, priority, tags, recurring tasks. It has no way to know that due dates, priority, and search already exist.

> **Watch For:** The agent suggesting a feature that already exists. "You could add priority levels" or "consider adding due dates" — both already built in Chapters 2 and 5. The thin context.md did not give the agent enough to work with.

Stop here. Do not fix it in this session. The thin context was a demonstration, not a starting point.

---

## The Handoff Test: Full context.md

This is the test of whether your context.md is complete. A new agent session should be able to read it and — without any other input from you — correctly describe the project state and propose a reasonable next feature.

Start a fresh Claude Code session. Reference `@context.md` and send this prompt — replacing the bracketed placeholder if you are pasting manually:

```
Read this project context and tell me:
1. What is the current state of this project?
2. What would be the most natural next feature to add, consistent with
   the established decisions?

[paste the full contents of your context.md file here]
```

> **What the Agent Will Do:** The agent will describe the project accurately — 15 tests, 8 commands, the schema, the key constraints. For the next feature, it should propose something consistent with the decisions: perhaps a `--priority` filter on list, or a bulk `done` command, or CSV export — features that extend the project without contradicting established choices. It will not suggest due dates or priority (already built) and it should not suggest anything that violates the "no automatic sorting" or "always fixed format" decisions.

> **Watch For:** Three things:
> 1. Does the agent name all 8 commands correctly?
> 2. Does the agent's proposed feature respect the key decisions — no automatic sorting, no optional output, invalid input errors?
> 3. Does the agent mention the date format constraint when discussing any date-related feature?

If the agent answers all three correctly, the context.md passes the handoff test. A colleague joining the project could receive this file and start a productive session.

> **Credit Note:** This exercise does not consume much of your rate limit — you are asking the agent to read and respond, not to write code. Run it deliberately; pay attention to which decisions the agent correctly recalls and which it misses.

If the agent misses a decision — proposes something that contradicts your constraints — that is signal that context.md needs another line. Add it to the decision summary, run the handoff test again.

---

## Debrief

The handoff test reveals something important: context.md is not primarily a convenience. It is a verification tool. When the agent correctly describes your project from the context file alone, you know the file is complete. When it misses something, you know the file has a gap.

**A project with a complete context.md can be handed off cleanly.** Not to a specific person or a specific AI — to any developer with access to the files. The context is in the repository, not in anyone's head. The decisions are documented. The state is current. Someone new can pick up the project on day one and contribute on day two.

Update context.md at the end of every session as part of Stage 5 of the loop — same step where you update decisions.md. Two files, two minutes, consistent state going into the next session. The loop's Update stage is where operational discipline lives: if you skip it, the next session starts degraded.

In Chapter 11, multiple agents read the same context.md simultaneously — each running a different part of the loop in parallel. The shared context file is what makes that coordination possible. One file, consistently maintained, is the foundation that parallel work builds on.

---

*A complete context file means the next session — whoever runs it — starts with everything they need.*
