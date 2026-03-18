# Chapter 7: Translating the Pattern

You built a pipeline that takes a topic and produces a finished article. Researcher, Writer, Adversarial Reader, Coordinator. The pipeline works because each role does one thing, each stage hands off a structured output, and the coordinator enforces the sequence.

Now you are going to build the same thing for code.

Not the same roles. Not the same files. The same design: specialized roles, explicit handoff contracts, a coordinator that sequences them, and a gate where you look before you commit. The pattern translates directly. What changes is what each role is protecting against — and code has failure modes that prose does not.

---

## What Carries Over

Everything structural carries over unchanged.

**Roles over prompts.** The coding pipeline has a Planner, an Implementer, a Reviewer, a Tester, and a Documenter. Each one receives a specific input, produces a specific output, and operates within explicit scope constraints. You will write role definition files for each of them, exactly as you wrote `agents/researcher.md` and `agents/adversarial-reader.md`. Code needs two roles prose did not: a Tester, because code has an objective pass/fail signal, and a Documenter, because the implementation and test report together can define the tool's real boundary.

**Handoff contracts.** The Planner produces a plan that the Implementer consumes. The Implementer produces code that the Reviewer and Tester consume. The Tester produces a report that the Documenter uses to describe what the tool does and what it doesn't. Each stage is designed with the next stage's input in mind.

**A coordinator.** `skills/feature-sprint.md` will do what `skills/article-pipeline.md` does: sequence the roles, define what each stage receives and produces, and hold the optional gates.

**Shared memory.** `requirement.md` is the equivalent of the topic and research question you gave the article pipeline — the fixed input that every stage reads from without changing. In Part 1 that was a few lines of text. In Part 2 it is an explicit document, because code requires more decisions than prose does, and those decisions need to be traceable. It does not change between stages. If the requirement changes mid-sprint, the sprint stops and restarts.

---

## What Changes

**Code has a pass/fail signal that prose does not.** Tests either pass or they do not. This changes what the Tester role does compared to the Adversarial Reader — instead of simulating a reader without context, the Tester generates and runs objective checks. When tests fail, the failure is unambiguous. The Implementer did not meet the requirement, or the requirement was underspecified, or the test was wrong. You know something is wrong; you may not know which.

**The Reviewer's job is different from the Adversarial Reader's.** The Adversarial Reader simulates not having context. The Reviewer has full context — they read the code knowing what it is supposed to do — and asks different questions: Is this implementation correct? Is it the simplest implementation that satisfies the requirement? Does it handle the cases the requirement did not specify? Are there things this code does that the requirement did not ask for?

**Scope discipline is sharper.** In Part 1, the voice constraint and the research notes kept the writer from wandering. In Part 2, the requirement document keeps the Implementer from adding features that were not asked for. This is a harder constraint to enforce in code: the Implementer will see obvious improvements and want to make them. That is not its job. Its job is to implement the requirement as written. Improvements go on a backlog.

**The order of stages matters more.** In the article pipeline, a weak research notes file produces a weaker article — bad, but recoverable. In the coding pipeline, an underspecified plan produces an implementation that does not match what the Reviewer and Tester are checking against. The Planner stage is where the most important gate lives.

---

## The Project: `git-summary`

Across Part 2, you will build `git-summary` — a small CLI tool that takes a repository path and produces a human-readable summary of recent activity: commits in the last week, files changed most frequently, and the most recent commit message for each active file.

```
$ python git_summary.py /path/to/repo

Repository: my-project
Period: last 7 days
Commits: 12

Most active files:
  src/main.py       — 4 commits  — "fix: handle empty input edge case"
  tests/test_main.py — 3 commits — "test: add edge case coverage"
  README.md          — 1 commit  — "docs: update usage examples"
```

This tool has enough surface area to demonstrate all five roles without requiring infrastructure. It has no external dependencies beyond the `git` command and Python's standard library. It is testable: the output for a known repository with known commits is deterministic. It has a clear requirement that can be underspecified in interesting ways — "recent activity" is vague enough that the Planner will need to make decisions, and those decisions will matter to the Tester.

You will build it across Chapters 8 through 11, one role and one pipeline stage per chapter.

---

## The Requirement Document

Before the pipeline starts, the requirement document exists. This is the input every stage reads from. Create `requirement.md` now:

```markdown
# Requirement: git-summary

## What it does
A CLI tool that accepts a local repository path and prints a
human-readable summary of recent git activity.

## Inputs
- A path to a local git repository (required)
- Optional: number of days to look back (default: 7)

## Output format
Printed to stdout. Sections:
1. Repository name and period covered
2. Total commit count for the period
3. Top 5 most-modified files, with: filename, commit count,
   most recent commit message for that file

## Constraints
- Python standard library only (no pip installs)
- Must run on macOS and Linux
- If the path is not a valid git repository, print a clear
  error message and exit with code 1
- Output is plain text, no color codes

## Out of scope
- Remote repositories
- Branch filtering
- Commit author breakdown
- Output formats other than plain text
```

> **Antigravity:** Create a new folder for Part 2 in your workspace root. Name it `git-summary-project`. Then create `requirement.md` inside that folder, paste the requirement above, and save it. This file does not change during the sprint — if you find that the requirement is underspecified while building, you add a new version after the sprint, not during it.
>
> **Watch For:** `requirement.md` exists in `git-summary-project` with all five sections present: What it does, Inputs, Output format, Constraints, and Out of scope. Verify the Out of scope section is there before you proceed — it is the first scope boundary in the coding pipeline.

Read the requirement once. Notice what it specifies and what it leaves open. "Top 5 most-modified files" — what if there are fewer than 5? "Most recent commit message for that file" — what if the file has no commits in the period? These are the questions the Planner will answer. They are in the requirement as gaps on purpose — real requirements always have them.

---

> **Key Takeaway:** The pipeline pattern translates directly from content to code. What changes is what each role is protecting against — and code's pass/fail signal makes some failures unambiguous in a way that prose never is.
