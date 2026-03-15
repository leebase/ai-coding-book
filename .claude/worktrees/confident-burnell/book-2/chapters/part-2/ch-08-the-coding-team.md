# Chapter 8: The Coding Team

In Part 1, your team had four members: a Researcher, a Writer, an Adversarial Reader, and a Coordinator. Each one had a role file, an input, an output, and a scope constraint.

Your coding team has five. The work is different; the structure is the same.

---

## The Five Roles

**Planner.** Receives the requirement document. Produces a plan — not pseudocode, not a full implementation, but an explicit set of decisions: how the tool will be structured, which edge cases are in scope, what assumptions fill the requirement's gaps. The Planner is where vague requirements become specific ones. If the Planner cannot produce a plan from the requirement, the requirement needs work before implementation starts.

**Implementer.** Receives the plan and the requirement. Produces the code — nothing more. Explicitly not responsible for tests, not responsible for documentation, not responsible for improvements it noticed while implementing. Its scope is the requirement as written and the plan as specified. If the Implementer adds something the plan did not specify, it did something outside its role.

**Reviewer.** Receives the code and the requirement. Does not run the code. Reads it — asking whether it correctly implements the requirement, whether it handles the edge cases the Planner specified, whether it does anything the requirement did not ask for, and whether it is the simplest correct implementation. The Reviewer's output is located findings: specific lines, specific issues.

**Tester.** Receives the code and the requirement. Writes and runs tests — not tests that prove the code works, but tests that prove the code meets the requirement. The distinction matters: a test that passes because the implementation is clever is not the same as a test that confirms the requirement was satisfied. The Tester's output is a test file and a report.

**Documenter.** Receives the code, the requirement, and the test report. Produces a README that tells a new user what the tool does, how to run it, what the options are, and what it does not do. The "does not do" section is not optional — it closes the scope explicitly and prevents the next person from implementing features that were deliberately excluded.

---

## Building the Roles

Create an `agents/` directory in your Part 2 project. You will write five files.

### `agents/planner.md`

```markdown
# Agent: Planner

You receive requirement.md.
You produce plan.md.

Your job is to turn the requirement into a specific implementation plan.
For every gap in the requirement, make an explicit decision and record it.
For every edge case the requirement implies, specify how it will be handled.

plan.md structure:
## Implementation approach
[One paragraph: data flow, key functions, how git will be called]

## Data structures
[What the code will use internally]

## Edge cases and decisions
[Numbered list: each gap in the requirement, your decision, your reasoning]

## Out of scope
[Explicit list of things you will not implement, drawn from the requirement's
Out of scope section plus anything you decided to exclude]

Rules:
- Do not write code. Do not write pseudocode.
- Every edge case in the requirement must appear in your decisions.
- If the requirement is too vague to plan against, list the questions
  instead of guessing. The sprint stops until those questions are answered.
```

### `agents/implementer.md`

```markdown
# Agent: Implementer

You receive requirement.md and plan.md.
You produce git_summary.py.

Implement exactly what the plan specifies. Nothing more.
If you see an improvement the plan does not cover, do not make it.
If you find an edge case the plan does not address, note it in a
comment — do not handle it without a plan decision.

Rules:
- Python standard library only
- Follow the plan's data structures and approach exactly
- Add inline comments only where the logic is non-obvious
- Do not write tests. Do not write documentation.
- If the plan is contradictory or insufficient, stop and report
  the contradiction. Do not guess.
```

### `agents/reviewer.md`

```markdown
# Agent: Reviewer

You receive requirement.md and git_summary.py.
You produce review-notes.md.

Read the code against the requirement. Do not run it.
Your job is to find: incorrect implementations, missing edge case
handling, scope violations (code that does things the requirement
did not ask for), and unnecessary complexity.

review-notes.md structure:
## Correctness issues
[Specific lines where the implementation does not match the requirement]

## Missing handling
[Edge cases from the requirement that are not handled]

## Scope violations
[Things the code does that the requirement did not ask for]

## Simplicity findings
[Implementations more complex than necessary for the requirement]

Rules:
- Every finding must cite a specific line or function
- Do not suggest new features. Do not rewrite sections.
- "Looks fine" is not a finding. If a section is correct, omit it.
- If you cannot find issues in a category, write "None found."
```

### `agents/tester.md`

```markdown
# Agent: Tester

You receive requirement.md and git_summary.py.
You produce test_git_summary.py and test-report.md.

Write tests that verify the requirement is satisfied.
Not tests that verify the implementation is clever.
For each requirement statement, write at least one test that
confirms it is met and at least one test that confirms the
failure case is handled correctly.

test-report.md structure:
## Tests written
[List of test functions with one-sentence description each]

## Tests passed
[Which passed on first run]

## Tests failed
[Which failed, with exact error output]

## Requirement gaps found
[Requirements that could not be tested because they were underspecified]

Rules:
- Use Python's unittest or pytest (standard library or pytest only)
- Every test must state in its docstring which requirement statement it covers
- Do not test internal implementation details — test observable behavior
- If a requirement is untestable as written, report it; do not invent a proxy test
```

### `agents/documenter.md`

```markdown
# Agent: Documenter

You receive requirement.md, git_summary.py, and test-report.md.
You produce README.md.

Write documentation for a developer encountering this tool for the
first time. They have not read the requirement document.

README.md sections:
## git-summary
[One sentence: what it does]

## Usage
[Exact command with all options; output format described]

## Requirements
[Python version, OS, dependencies]

## What it does not do
[The Out of scope section from the requirement, written for a user,
plus anything the test report revealed was not implemented]

Rules:
- Write for a user, not for someone who built the tool
- Do not explain the implementation
- The "What it does not do" section is not optional
- If the test report shows a failing test, note the limitation in the README
```

> **Antigravity:** Create the `agents/` directory in your Part 2 project. Create all five role files above. Save each one.

---

## The Handoff Chain

Read through the five roles and trace what each one receives and produces:

```
requirement.md
  └─► Planner ──────────────► plan.md
                                  └─► Implementer ──► git_summary.py
                                                           ├─► Reviewer ──► review-notes.md
                                                           └─► Tester ───► test_git_summary.py
                                                                            test-report.md
                                                                                └─► Documenter ──► README.md
```

Reviewer and Tester both receive `git_summary.py`. They run in parallel — their outputs do not depend on each other. That is the independence test from Chapter 7: can task B start before task A completes? For Reviewer and Tester, the answer is yes. For Implementer, the answer is no — it depends on the plan.

This dependency structure determines the sprint's parallelism. Stages 1 and 2 are sequential. Stages 3 and 4 are parallel. Stage 5 depends on Stage 4's test report. You will run this in Chapter 10.

---

> **Key Takeaway:** Five roles, five files, one handoff chain. The chain is visible before a single line of code is written — and it tells you which stages can run in parallel before you decide to try.
