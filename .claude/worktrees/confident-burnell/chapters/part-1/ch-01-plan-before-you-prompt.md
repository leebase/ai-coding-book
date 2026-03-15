# Chapter 1: Plan Before You Prompt

You have used AI coding tools. You have described what you want, watched the AI generate something, looked at it, and thought: *that's not quite right*. So you described it again, differently. The AI generated something else. Closer, maybe. Or maybe not.

This is the most common frustration in AI-assisted development, and it has a simple cause: you did not have a plan before you opened the tool.

This chapter is about fixing that. Not with a complicated framework. With five questions you answer before you type your first prompt.

---

## Why "Just Describe It" Doesn't Work

Before AI, writing code yourself was slow. That slowness was secretly useful. When you had to write every line, you had to think about every line. Bad assumptions surfaced during implementation, because you ran into them. You adjusted. The friction of the work kept you honest.

AI removes that friction. You describe something, and thirty seconds later you have code. The speed feels like productivity. It often isn't.

Here is what actually happens: the agent makes assumptions. It has to — you did not give it enough information to do otherwise. It produces something that compiles, runs, and looks reasonable. You think it is mostly right. You move on.

Three prompts later, you realize the foundation is wrong. The AI built a task manager with SQLite persistence and a full CLI argument parser, and you just wanted a simple JSON file and four commands. Now you are either fighting the existing structure or starting over.

The AI did not fail you. It did exactly what a capable colleague would do when handed a vague request: it made reasonable assumptions and built something. The assumptions just were not yours.

**The problem is not the AI's ability to generate code. It is your failure to specify what code to generate.**

This gets worse with AI than with human developers for one specific reason: speed. A human colleague who receives a vague brief will ask clarifying questions before starting. An AI agent starts immediately. The faster the execution, the faster the wrong assumption becomes load-bearing architecture.

---

## The Project You'll Build

Across Part 1 of this book, you will build a personal task manager CLI. Every chapter adds something to it — a feature, a test suite, a code review, a documentation pass. By Part 1's end, you will have a real, working tool and seven chapters of SE discipline applied to it.

Here is what "done" looks like at the end of this chapter:

- `add` — adds a task by description
- `list` — shows all tasks
- `done` — marks a task complete by ID
- `delete` — removes a task by ID

Tasks are stored in a JSON file. The whole thing runs with `python tasks.py`. No database. No external services. One command to run it.

If you want to use your own project instead, that is fine — see the appendix for the criteria it needs to meet. Everything in this chapter applies regardless of what you are building.

---

## The Failure Path: Prompting Without a Plan

Let's start by doing it wrong. Not to be perverse — because you need to feel what goes wrong before the fix makes sense.

**Open Antigravity and create a new project folder.** If you have not installed Antigravity yet, visit [antigravity.google](https://antigravity.google) to download it. Installation instructions are on the site — they change occasionally as the product evolves, so follow the current guide rather than any screenshots in this book. It looks like VS Code because it is built on VS Code. Create a new folder for your project and open it.

**Open the agent sidebar.** In Editor View, find the agent sidebar — look for the chat or agent icon in the activity bar. This is where you will interact with the Antigravity agent. Click it to open the sidebar panel.

Now type this prompt — exactly this, nothing more:

```
Build me a task manager CLI in Python.
```

> **What the Agent Will Do:** The agent will begin working autonomously. You will see it creating files in your project explorer on the left, running commands in the terminal panel at the bottom, and occasionally pausing to report what it has done. Do not interrupt it. Let it finish.

> **Watch For:** How many files it creates. Look at the project structure that appears in the file explorer. Look at what it built — open `README.md` if it created one, or the main Python file.

Take a moment to look at what you got.

The agent probably built something that works. It might have a full argument parser. It might use SQLite for persistence. It might have categories, priorities, or due dates. It might have color output. It is probably more than you wanted, in a structure you did not choose, organized in a way that reflects the agent's assumptions, not yours.

Now try to correct it. Type something like:

```
Make it simpler — just a flat JSON file, four commands: add, list, done, delete.
```

> **What the Agent Will Do:** The agent will attempt to refactor what it built. You will see it editing existing files and possibly creating or deleting others.

> **Watch For:** Whether the result is actually simpler, or whether the agent made a different set of decisions that are also not quite what you wanted. Depending on how far the first version diverged from what you want, this may produce something close, or it may produce a different set of assumptions that are also not quite right.

> **Free Tier Note:** Each prompt to the agent consumes from your rate limit budget. If you have been iterating — trying to correct the first version — you may see a rate limit warning after three or four exchanges. This is the cost of planning failures made visible.

After two or three correction attempts, stop. Do not fix it further.

Notice what happened. You spent multiple prompts and have something that is approximately what you wanted. You do not fully understand its structure because you did not design it. And if you keep building on this foundation in later chapters, every chapter will inherit its unexamined assumptions.

This is the failure mode. Not a crash. Not an error message. A gradual accumulation of someone else's decisions about your project.

---

## The Planning Brief

Before you open Antigravity for any feature or project, answer five questions in writing. Not in your head — in writing, in a file. Vague thinking survives in your head. It does not survive contact with a blank document.

**The five questions:**

**1. What does it do?**
One sentence. Core function only. No features that are "nice to have."

**2. What does it NOT do?**
This is as important as question one. Constraints eliminate the AI's assumption space. Every constraint you leave unspecified is a choice the agent will make for you.

**3. How does the user interact with it?**
List the exact commands or interface elements. If it is a CLI, list every command and what it takes as input.

**4. What does the data look like?**
How is information stored? What format? What fields? If you do not specify this, the agent will choose — and its choice may not match your mental model.

**5. What does "done" mean for this session?**
Scope the work to what you actually want to accomplish right now. Not the full vision — this session's deliverable.

Here is the planning brief for Chapter 1's task manager:

---

*What it does:* A CLI tool to manage a personal to-do list from the terminal.

*What it does NOT do:* No categories, no priorities, no due dates, no colors, no database, no network requests, no configuration files.

*How the user interacts with it:*
- `python tasks.py add "Buy groceries"` — adds a task, prints the assigned ID
- `python tasks.py list` — prints all tasks with their IDs and completion status
- `python tasks.py done 1` — marks task 1 as complete
- `python tasks.py delete 1` — removes task 1

*What the data looks like:* A `tasks.json` file in the project directory. An array of task objects. After adding two tasks, the file should look like this:

```json
[
  {"id": 1, "description": "Buy groceries", "done": false},
  {"id": 2, "description": "Write chapter 1", "done": false}
]
```

IDs are sequential integers starting at 1.

*Done when:* All four commands work. `tasks.json` is created on first run if it does not exist. Running the commands in sequence produces the expected output.

---

That brief took five minutes to write. It eliminates every assumption the agent made in the failure path.

Notice what the brief actually is: a written record of your decisions, made before implementation started. In Part 2 of this book, you will see this idea formalized into a document system that persists across sessions, tools, and collaborators. For now, a text file is enough.

---

## The Success Path: Prompting From a Plan

Delete the project folder from the failure path — or simply create a new empty folder and open that in Antigravity instead. You want a clean slate with no files from the previous attempt.

Open the agent sidebar. This time, your prompt will be the planning brief, prefaced with a one-sentence instruction:

```
Build a Python CLI task manager matching this specification exactly.

What it does: A CLI tool to manage a personal to-do list from the terminal.

What it does NOT do: No categories, no priorities, no due dates, no colors,
no database, no network requests, no configuration files.

Commands:
- python tasks.py add "Buy groceries" — adds a task, prints the assigned ID
- python tasks.py list — prints all tasks with IDs and completion status
- python tasks.py done 1 — marks task 1 complete
- python tasks.py delete 1 — removes task 1

Storage: tasks.json in the project directory. Array of objects:
{"id": 1, "description": "Buy groceries", "done": false}
IDs are sequential integers. Create tasks.json on first run if missing.

Done when: All four commands work correctly in sequence.
```

> **What the Agent Will Do:** The agent will create `tasks.py` and likely a short `README.md`. It should not create additional files, a database layer, or a complex directory structure. The implementation should be direct — a single Python file under 100 lines.

> **Watch For:** The agent completing the task in one pass without asking clarifying questions. When a prompt is specific enough, the agent does not need to guess.

When the agent finishes, test it:

```bash
python tasks.py add "Buy groceries"
python tasks.py add "Write chapter 1"
python tasks.py list
python tasks.py done 1
python tasks.py list
python tasks.py delete 2
python tasks.py list
```

> **Watch For:** Each command producing exactly the output you specified. `list` showing IDs, descriptions, and completion status. `done` marking the correct task. `delete` removing the correct task. `tasks.json` appearing in your project folder and updating with each command.

If anything is off, do not issue a vague correction. Go back to the planning brief, identify the specific thing that is wrong, and issue a targeted correction.

Vague: *"The list command doesn't look right."*
Specific: *"The list command should print each task as `[1] Buy groceries` with a `[x]` prefix for completed tasks. Currently it prints the raw JSON object."*

One specific problem. One specific fix. This is the same discipline as the planning brief — specificity is what makes the agent useful.

> **Free Tier Note:** Notice how many prompts this approach took compared to the failure path. Planning before prompting is not just good practice — it is how you make your rate limit budget last.

---

## Debrief

Look at what you have. A working CLI tool, built in one focused Antigravity session, that does exactly what you specified — because you specified it.

The agent's job was execution. Your job was definition. When you handed the definition work to the agent in the failure path, the output reflected the agent's judgment, not yours. When you did the definition work yourself first, the output reflected your judgment.

**What you own: the plan. What the AI owns: the implementation.** Keep those roles clear and AI-assisted development becomes predictable. Blur them and you are debugging someone else's assumptions.

The task manager you just built is the foundation for the next six chapters. In Chapter 2, you will add a feature to it — but before you open Antigravity, you will define exactly what that feature is.

---

*Planning is not a speed bump between you and the AI. It is the thing that makes the AI fast.*
