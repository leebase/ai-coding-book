# Chapter 11: Your Coding Team at Work

You have a working pipeline for `git-summary`. A requirement document, a plan, an implementation, a test suite, review notes, and a README — produced by five specialized roles in a defined sequence, with a mandatory gate at the most expensive decision point.

Before you extend it, there is something you should know about where this system came from.

---

## The Reveal

This book was written using the same system you just built.

Not metaphorically. The chapters you read were produced by a pipeline with specialized agent roles: one that defined the principle to be taught, one that designed the hands-on scenario, one that reviewed Antigravity instructions for accuracy, one that read the draft as a confused first-time reader, one that checked continuity across chapters, one that connected Part 1 principles to Part 2 mechanisms. A coordinator skill — `skills/ebook-writer.md` — sequenced all of them, defined what each stage received and produced, and held a gate before prose was written.

The coordinator did not always follow the stages faithfully. Roles drifted. Stages collapsed. Some runs produced better output than others. The gate caught most of the problems before they propagated.

Sound familiar?

The system that wrote this book is the system the book teaches. The failure modes in Chapter 6 are the failure modes the pipeline ran into. The mandatory gate in Chapter 9 is the gate that prevented the most expensive rework. You were not being taught an abstract methodology — you were watching it operate on itself.

---

## What You Now Have

Look at your Part 2 project directory:

```
requirement.md          — the spec that every stage read from
plan.md                 — the Planner's decisions, filling the gaps
git_summary.py          — the implementation
test_git_summary.py     — tests that verify the requirement, not the code
test-report.md          — what passed, what failed, what was missing
review-notes.md         — located findings from someone
                          who read without running
README.md               — documentation for someone who was not in the room
agents/
  planner.md
  implementer.md
  reviewer.md
  tester.md
  documenter.md
skills/
  feature-sprint.md
```

This is a team. Not a team that meets, not a team that negotiates, not a team that requires coordination tooling. A team defined in files, sequenced by a coordinator, executable by you with a session and a skill file.

The system is portable. Take it to a different feature, a different codebase, a different language. Change the requirement document. Change the plan's edge case decisions. Run the pipeline again. The roles do not change. The coordinator does not change. The handoff contracts do not change. The team is already built.

---

## Extending the Team

The five roles you built are sufficient for `git-summary`. They are not exhaustive for every feature you will ever build. Some features need roles these five do not cover.

A **Security Reviewer** receives the code and looks specifically for security implications the general Reviewer may have deprioritized: input validation, command injection risk, file path traversal, credential handling. `git-summary` runs a git command with a user-provided path — a Security Reviewer would flag that `subprocess.run` with shell=True would be dangerous here (use shell=False with a list), and check that the path is validated before being passed to git.

A **Dependency Auditor** receives the requirement and checks whether the standard library constraint is met, and whether any third-party library would make the implementation significantly simpler or safer — and whether that tradeoff is worth revisiting the constraint.

A **Compatibility Checker** runs the code in an environment different from the one the Implementer produced it in. macOS and Linux have different git output formats. The Tester may not have caught that.

These are roles you add when you need them. They follow the same structure: input, output, constraints. They slot into the coordinator as additional stages. The pipeline grows with the requirements.

---

## The Next Feature

Pick one from the natural extensions of `git-summary`:

**Option A: `--author` filter** — show only commits by a specified author. Low risk. New flag, existing data flow. The Planner's main decision: what happens when the author has no commits in the period?

**Option B: `--format json`** — output the summary as JSON instead of plain text. Medium risk. New output format, same data. The Documenter will need to describe the JSON structure.

**Option C: `--since` date flag** — instead of days, accept an ISO date string. Medium risk. New argument type, date parsing, edge cases around timezone handling.

Write the requirement for whichever you choose. Run the pipeline. The team is already staffed.

---

## Where the Path Continues

You have the document-driven coordination layer. You know its limits from Chapter 6. The next level — programmatic orchestration, independent contexts, validated handoffs — is the subject of a future volume.

That path is worth taking when the failure modes from Chapter 6 cost more than the infrastructure would. When you are running pipelines in production without human review. When output variance is a product defect, not an inconvenience. When you need the team to run without you.

For now, you have a system you can run, a team you understand, and an honest picture of where it stops. That is a complete starting point.

---

> **Key Takeaway:** The pipeline is portable. The team you built for `git-summary` is the team for the next feature, and the one after that. Add roles when you need them. The coordinator grows with the work.
