# Chapter 4: Review AI Output Like a PR

You have been running `tasks.py` for three chapters. You have verified its behavior. The tests pass. The commands work.

Here is a question: can you explain how the code assigns IDs to new tasks?

Not what it does — how. Open `tasks.py` right now and find the ID assignment logic. Read it. Could you explain it to a colleague in thirty seconds without looking at the file?

If you hesitated, you have an understanding gap. The code works. You do not fully understand it. And the next time you add a feature — which is next chapter — you will be building on a foundation you cannot fully explain.

This is the problem that code review solves. Not finding bugs. Not enforcing style. **Transferring understanding from the implementation to you**, so that you — not the AI — own the code going forward.

---

## The Understanding Gap

When you write code yourself, review happens continuously. You make a decision, you write the code, you read it back, you adjust. By the time you are done, you understand the code because you built it incrementally.

AI-generated code arrives complete. You read it once to verify it runs. Then you move on. Three chapters in, you may have read `tasks.py` in fragments — checking one function when something seemed off, looking up one variable name — but probably not end-to-end with the goal of understanding the whole thing.

The gap between "verified behavior" and "understood implementation" matters for one specific reason: **you are the permanent maintainer**. The AI that generated this code has no memory of it. Next session, it will read the file fresh, just like you will. The difference is that you are responsible for what it contains and what it does going forward. The AI is not.

Code review is how you take that responsibility seriously. Not as a formality — as a transfer of ownership.

---

## The Failure Path: Running Without Reading

Open `tasks.py` right now. Not to check something specific — to read it, top to bottom, as if a colleague had submitted it as a pull request and you had to approve or reject it.

Read slowly. When you finish each function, ask: *could I write this from scratch without looking at the file?*

Most readers at this point find at least one of the following:

**A function that does more than one thing.** The `add` command handler might parse the command-line arguments, validate them, construct the task object, and write to the file — all in one block. That is four responsibilities in one place.

**Variable names that are not descriptive.** The AI often uses single-letter variables (`t` for task, `d` for data, `f` for file handle) in loops and comprehensions. The code runs. The intent is not immediately clear.

**Missing error handling for invalid input.** What happens when you run `python tasks.py done 99` and task 99 does not exist? Try it now. Does the code print a clear error message and exit cleanly? Or does it crash with a Python traceback?

You probably found at least one of these. Possibly all three. None of them caused a test failure — the tests cover your requirements, which did not specify internal structure. But all of them will slow you down when you modify this code next chapter.

---

## The PR Review Checklist

Pull request review has standard questions. If you have done code review before, this is the same process applied to a different author. If you have not, here is the checklist:

**1. Can you explain what every function does in one sentence?**
If not, the function probably does too many things, or its name does not match its behavior.

**2. Does each function do one thing?**
A function that parses input *and* writes to disk *and* handles errors is three functions that happen to share a name. The AI defaults to this pattern because it produces working code faster. You have to decide if it is acceptable to maintain.

**3. Are variable and function names descriptive?**
`task` is better than `t`. `task_data` is better than `d`. `tasks_file_path` is better than `fp`. You will read this code again. Make it readable.

**4. Are error cases handled explicitly?**
Every command that takes an ID (`done`, `delete`) can receive an ID that does not exist. Every function that reads a file can receive a file that is malformed. If these cases are not handled explicitly, the user gets a Python traceback instead of a useful error message.

**5. Is there anything you would not want to explain to a colleague?**
This is the gut-check question. If there is a section of code you find yourself hoping no one looks at too closely, that section needs attention.

Go through the checklist on `tasks.py`. Write down every finding — even minor ones. Then prioritize: what must be fixed before you add another feature?

---

## Three Findings, Three Fixes

Here are three findings that commonly appear in the task manager after three chapters of AI generation. Yours may differ; apply the same approach.

### Finding 1: A Function Doing Two Things

The `add` command handler likely does argument parsing, task construction, and file writing in one place. This makes it harder to test the business logic independently and harder to read.

Open the agent sidebar and start a new session (new conversation icon at the top of the sidebar). Issue this targeted prompt:

```
In tasks.py, the function that handles the "add" command mixes argument parsing
with task creation and file writing. Refactor it into two parts:
- A pure function add_task(tasks, description, priority) that creates and
  appends a task to the list and returns the updated list
- The CLI handler that calls add_task and handles file I/O

Do not change any behavior. All existing tests must still pass.
```

> **What the Agent Will Do:** The agent will extract the business logic into a separate function and update the CLI handler to call it. The interface to the user — the command syntax and output — will not change.

> **Watch For:** The agent creating a function named `add_task` (or similar) that takes only data parameters and returns data — no file I/O inside it. Then run:

```bash
pytest tests/ -v
```

> **Watch For:** All nine tests still passing. If any fail, the refactor changed behavior — issue a targeted correction identifying the specific test that failed and what it expected.

### Finding 2: Unclear Variable Names

Find any single-letter or abbreviated variable names in `tasks.py`. Common examples: `t` in a loop over tasks, `d` used for a dict, `f` for a file handle.

Issue a targeted rename prompt — do not ask the agent to "improve readability" (too vague):

```
In tasks.py, rename these variables for clarity:
- Any loop variable named "t" that iterates over tasks → rename to "task"
- Any variable named "d" used for task data → rename to "task_data"
- Any file handle variable named "f" → rename to "file"

Do not change any logic. Run the tests to confirm nothing broke.
```

> **What the Agent Will Do:** The agent will perform the renames throughout the file. This is a mechanical change — it should not affect any behavior.

> **Watch For:** The agent completing quickly (this is a simple change). The agent may run the tests itself — but run them yourself in the terminal panel to confirm:

```bash
pytest tests/ -v
```

### Finding 3: Missing Guard on Nonexistent ID

Run this in the Antigravity terminal panel (not the agent sidebar):

```bash
python tasks.py done 99
```

If the output is a Python traceback (`IndexError`, `KeyError`, or similar) rather than a clean error message, the error case is not handled.

Write the requirement for the error behavior, then issue the fix prompt:

```
In tasks.py, the "done" and "delete" commands crash with a Python exception
when given an ID that does not exist in tasks.json.

Fix both commands to instead print a clear error message and exit with a
non-zero exit code when the given ID is not found. Example error message:
"Error: task 99 not found."

Do not change behavior for valid IDs. Run the tests to confirm nothing broke.
```

> **What the Agent Will Do:** The agent will add a guard at the start of each command handler that checks whether the given ID exists before proceeding. If not found, it prints the error message and exits.

> **Watch For:** Running `python tasks.py done 99` now prints `Error: task 99 not found.` instead of a traceback. Then run the full test suite:

```bash
pytest tests/ -v
```

> **Watch For:** All nine tests still passing. Optionally, add a tenth test for the nonexistent-ID case — you now have a requirement for this behavior.

---

## Debrief

Three findings. Three targeted prompts. Nine tests still passing after each fix.

Notice what the process was not: it was not "rewrite this to be cleaner." Vague improvement requests produce unpredictable changes. Each finding was specific, each prompt was specific, and the test suite confirmed that the behavior was preserved throughout.

This is the difference between code review as a discipline and code review as an editorial opinion. Discipline means: find a specific problem, specify the fix, verify the behavior did not change.

**The AI is a fast implementer. You are the permanent maintainer.** Those roles have different incentives. The AI's incentive is to produce working code quickly. Your incentive is to produce maintainable code you can understand, explain, and modify for the next six chapters. Review is where you enforce your incentive on the AI's output.

One more thing worth noting: you just did what a senior developer does when reviewing a junior developer's pull request. You did not rewrite it. You did not take it over. You asked targeted questions, identified specific issues, requested specific changes, and verified the result. The skill is identical — the colleague is just a different kind of intelligence.

In Part 2, the code review skill formalizes this checklist into a repeatable step in the Development Loop, run automatically after every implementation sprint. The autonomy modes you will learn about also reflect this ownership question: how much trust you extend to the AI, and when you pull the work back for human review. You have been calibrating that instinctively. Part 2 makes it explicit.

---

*Understanding the code is not optional — you are the one who has to change it next.*
