# Chapter 3: Test What the AI Produces

You have a task manager that runs. You have verified that the main commands work — you ran them manually after each chapter and checked the output. That is not testing.

Testing is systematic verification of every behavior you specified. There is a meaningful difference between "it worked when I tried it" and "it works for every case it is supposed to handle."

That difference matters more with AI-generated code than with code you wrote yourself. When you write code, you understand it — you made the decisions, you know the edge cases you considered and the ones you skipped. AI-generated code has no such intuition attached to it. The code exists. It does things. What those things are, precisely, requires verification.

This chapter is about building that verification systematically — and about why you should design your tests from your requirements, not from your implementation.

---

## The Trust Problem

Here is a question worth sitting with: how confident are you that your task manager handles every case in the requirements you wrote in Chapter 2?

Specifically:
- What happens when you pass `--priority urgent` (an invalid value)?
- What happens if `tasks.json` gets a task entry without a `priority` field?
- What happens if you run `python tasks.py done 99` when task 99 does not exist?

If you are not certain, you have not tested it — you have assumed. Assumptions about AI-generated code are exactly as reliable as assumptions about a colleague's code you have never read: sometimes fine, sometimes not, always unverified.

The common response at this point is: "I'll just ask Antigravity to write the tests." That seems efficient. It is not — for a specific reason.

---

## The Failure Path: Letting the AI Write Its Own Tests

Open Antigravity and your task manager project. Start a new agent session. Type:

```
Write a test suite for tasks.py using pytest.
```

> **What the Agent Will Do:** The agent will read `tasks.py`, understand its structure, and write tests based on what the code does. It will create a `tests/` directory and a `test_tasks.py` file. The tests will likely cover the main commands with typical inputs.

> **Watch For:** Which cases the agent tests. Specifically, look for whether it tests: invalid priority values, missing priority fields in existing JSON entries, commands with IDs that do not exist.

When the agent finishes, open the Antigravity terminal panel (View → Terminal, or the terminal tab at the bottom of the window). Install pytest if you have not already, then run the suite:

```bash
pip install pytest
pytest tests/ -v
```

> **Watch For:** All tests passing. Pytest's verbose output lists each test by name with `PASSED` or `FAILED` next to it. A fully green run ends with a summary line like `9 passed in 0.12s`. That is what you are looking for — or not looking for, in this case.

The tests probably pass. Congratulations — you have a false sense of security.

Open `test_tasks.py` and read what the agent wrote. You will likely find:

- Tests that add a task and check it was stored
- Tests that list tasks and check the output format
- Tests that mark tasks done and delete them
- Happy path coverage for the priority flag

What you will probably not find:

- A test for `--priority urgent` (invalid value)
- A test for a `tasks.json` entry with no `priority` field
- A test for `done 99` when task 99 does not exist

The agent tested what it implemented. It did not test what you required. Those are different things. The edge cases in your requirement — the ones that make the behavior predictable — are exactly the cases the agent's tests skip, because the agent derived its tests from the implementation, not the specification.

> **Free Tier Note:** If you followed the failure path and the agent's tests pass, resist the urge to move on. A green suite that does not cover your requirements is not a safety net — it is a false floor.

---

## Tests Derived From Requirements, Not Implementations

The correct approach is to write tests from the requirement before the agent writes a line of test code.

Not the implementation — the requirement. The requirement is what you specified the code should do. The tests are verification that it does those things. The implementation is irrelevant to the test design — it is what you are testing, not where you get your test cases.

This distinction matters because of how AI-generated code fails. It rarely fails at the happy path. It fails at boundaries, edge cases, and behaviors you specified but did not manually exercise. Those are the cases your requirement covers. Those are the cases your tests must cover.

The process:

1. Read your requirement
2. For each property of the requirement, write one or more test cases
3. Give those test cases to Antigravity along with the requirement
4. Let the agent implement the test code — not design it

You design the test cases. The agent writes the test code. This mirrors the same division from earlier chapters: you define what is correct, the AI executes.

---

## The Test Plan

Here is the test plan for the task manager, covering both Chapter 1 and Chapter 2 requirements. Write this before opening Antigravity.

**From Chapter 1 requirements:**

| # | Test case | Input | Expected |
|---|-----------|-------|----------|
| 1 | Add creates a task | `add "Buy groceries"` | JSON contains id=1, description="Buy groceries", done=false |
| 2 | List shows all tasks | Two tasks added, then `list` | Both tasks shown in creation order |
| 3 | Done marks correct task | `add`, then `done 1`, then `list` | Task 1 shows as done, task 2 unchanged |
| 4 | Delete removes task | `add`, `add`, then `delete 1`, then `list` | Only task 2 remains |
| 5 | JSON created on first run | No `tasks.json` exists, then `add` | `tasks.json` created with one entry |

**From Chapter 2 requirements:**

| # | Test case | Input | Expected |
|---|-----------|-------|----------|
| 6 | Priority stored and displayed | `add "task" --priority high`, then `list` | Shows `[high] task` |
| 7 | Default priority is medium | `add "task"` (no flag), then `list` | Shows `[medium] task` |
| 8 | Invalid priority errors | `add "task" --priority urgent` | Error message, no task added, exit code non-zero |
| 9 | Missing priority field defaults to medium | `tasks.json` entry with no `priority` key, then `list` | Shows `[medium] description` |

Nine test cases. Each one maps to a specific property in your requirements. The test plan took about fifteen minutes to design.

---

## The Success Path: Requirement-Driven Tests

Start a new agent session in your task manager project by clicking the new conversation icon at the top of the agent sidebar. Your prompt gives the agent the requirement, the test plan, and the implementation context:

```
I have a Python CLI task manager in tasks.py with this behavior:

Core commands: add, list, done, delete
Storage: tasks.json — array of {"id": int, "description": str, "done": bool, "priority": str}
Priority values: high, medium, low. Default: medium.
Invalid priority: print error, exit non-zero, do not add task.
Missing priority field in tasks.json: display as medium without modifying stored data.

Write a pytest test suite in tests/test_tasks.py that covers exactly these
nine test cases (do not add others):

1. add creates a task with correct id, description, done=false, priority=medium
2. list shows all tasks in creation order
3. done marks the correct task as done, leaves others unchanged
4. delete removes the correct task, leaves others
5. tasks.json is created on first run if it does not exist
6. --priority high stores and displays [high]
7. add with no --priority flag displays [medium]
8. --priority urgent prints an error and does not add a task
9. a tasks.json entry with no priority field displays as [medium]

Use pytest. Each test must be independent — use a temporary directory for tasks.json
so tests do not affect each other.
```

> **What the Agent Will Do:** The agent will create `tests/test_tasks.py` with nine tests. It will use `tmp_path` to give each test a clean JSON file, avoiding test interdependencies. For CLI-level tests it may use `subprocess.run` to call `tasks.py` as a process.

> **Watch For:** The agent creating exactly nine tests, not more. If it adds extra "bonus" tests beyond your plan, note it — that is scope expansion, which is the subject of Chapter 6.

Run the suite in the terminal panel:

```bash
pytest tests/ -v
```

> **Watch For:** One test failing. Pytest will show `FAILED tests/test_tasks.py::test_missing_priority_defaults_to_medium` (or similar name) with a traceback beneath it. Specifically, test 9 — the missing priority field case — commonly surfaces a bug: the agent may have used `task["priority"]` (which raises `KeyError` on a missing field) instead of `task.get("priority", "medium")`. The test catches it. The implementation did not.

When you see the failure, do not guess at the fix. Open `tasks.py`, find the line that reads `priority`, and look at whether it handles a missing key. Then issue a targeted correction:

```
In tasks.py, the list command crashes with KeyError when a task in tasks.json
has no "priority" field. Fix it to default to "medium" when the field is absent.
Do not change any other behavior.
```

> **What the Agent Will Do:** The agent will locate the specific line and change `task["priority"]` to `task.get("priority", "medium")` (or equivalent). One line change.

Run the suite again:

```bash
pytest tests/ -v
```

> **Watch For:** All nine tests passing. The fix was targeted because the test was specific. The test was specific because the requirement was specific.

---

## Debrief

That failing test found a real bug. Not a hypothetical. A behavior your code had that violated your requirement — specifically the backward compatibility requirement you wrote in Chapter 2.

The agent's self-written tests missed it because the agent wrote tests that matched the implementation it produced, and the implementation had this bug. When the tests come from the requirement, they are independent of the implementation's blind spots.

This is why you design test cases and let the agent write test code. The test case design requires knowing what should be true — which is your job, derived from the requirement. The test code implementation is mechanical — which is the agent's job.

**A test suite that passes is not proof of correctness. It is proof of coverage.** The question is: coverage of what? If the tests come from the agent's interpretation of its own code, you are testing the agent's assumptions. If the tests come from your requirements, you are testing your decisions.

You now have a task manager with a requirement, an implementation, and a test suite that enforces the requirement against the implementation. Every feature you add in subsequent chapters gets the same treatment: requirement first, tests second (designed from the requirement), implementation third.

In Part 2, the Development Loop formalizes this sequence into an explicit structure that scales from solo sessions to teams of parallel agents. The same requirement-first, test-second discipline applies whether you are the only developer or coordinating multiple AIs. You have been following the pattern here — Part 2 gives it a name and a system.

---

*Passing tests tell you the code does what you tested. Requirements-derived tests tell you the code does what you specified.*
