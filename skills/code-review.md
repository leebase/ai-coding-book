# Skill: Code Review

> Load this skill before closing a sprint or tagging a release.
> Also load it when asked to review a specific feature or PR.

---

## Review-Only Rules

**You are in analysis mode. Do not modify files. Do not commit. Do not apply patches.**

Your job is to find problems and describe fixes. Output goes to `code-reviews/review-2026-03-15.md`.
If you find something obviously wrong and safe to fix, describe the fix precisely — but do not apply it unless the human explicitly says so.

---

## Phase 0: Map the Project First

Before reviewing anything, build a working mental model. Read:

1. `AGENTS.md` — constraints and conventions
2. `architecture.md` — design decisions and known tradeoffs
3. `product-definition.md` — what this is supposed to do
4. `sprint-plan.md` — what was built this sprint (scope the review)

Then enumerate:
- **Entrypoints**: What starts the program? CLI flags? A web server? A worker?
- **External dependencies**: Files, network, subprocesses, databases, APIs
- **Trust boundaries**: What input comes from users/external systems vs. internal state?
- **Security-critical areas**: auth, secrets, file paths from user input, subprocess args from user input

Write a one-paragraph architecture summary at the top of your review file. If you get this wrong, everything else will be wrong too.

---

## Phase 1: Run the Checks

Run every check the project provides. Do not skip any.

```bash
{{BUILD_COMMAND}}     # Must pass — compilation errors are blocking
{{TEST_COMMAND}}      # All tests must pass before review is meaningful
```

If any check fails, **that is Finding #1**. Do not proceed with the review as if the project is healthy — it isn't.

If no checks are configured, propose a minimal standard toolchain for this stack and note it as a finding.

---

## Phase 2: Review Lenses

Work through each lens. Not every lens applies to every project — skip what's genuinely irrelevant and say why.

### A. Correctness & Error Handling

This is the highest-value lens for most projects.

- Does every function that can fail handle its errors explicitly?
- Are errors surfaced to the user with actionable messages, or swallowed silently?
- What happens when an external dependency fails (file not found, subprocess exits with error, network timeout)? Is the failure handled, or does it cascade?
- Are there any `while (true)` loops with no guaranteed exit condition? (These become runaway processes.)
- Are there resource leaks — open files, allocated memory, subprocess handles — that don't get cleaned up on the error path?
- Are there race conditions? (Shared mutable state accessed from multiple threads/goroutines/tasks without synchronization.)

**For each issue found:** File + function + line range. Exact failure mode. Specific fix.

### B. Security

Threat-model the entry points. For CLI tools: are any arguments used in subprocess calls, file paths, or template substitution without sanitization? For web servers: injection, SSRF, auth gaps. For file writers: path traversal.

Ask: **what is the worst thing a malicious or mistaken input to this program can do?**

Mark findings: `Critical` / `High` / `Med` / `Low`. Be honest about severity — don't inflate.

### C. Edge Cases & Boundary Conditions

- Empty input, zero-length collections, null/nil/empty strings
- Very large input (what happens at scale?)
- Operations run twice (idempotency — especially important for file creation, git operations)
- Partial failure mid-operation — is state left consistent?

### D. Code Quality

- Are there functions doing more than one thing? (High coupling, hard to test)
- Is there duplication that would cause a fix in one place to require fixes in two others?
- Are names clear at the call site, or do you need to read the implementation to understand a call?
- Is there dead code (unreachable branches, unused variables, commented-out blocks)?

Be honest but proportionate. Not every style issue is worth raising. Focus on things that will cause bugs or make the next engineer's job harder.

### E. Tests

- What's tested? What isn't?
- Are the happy paths covered but edge cases missing?
- Are there tests that pass but don't actually verify the right thing? (Tests that can't fail are worse than no tests — they provide false confidence.)
- What's the most likely bug that would be caught by a test that doesn't exist yet?

### F. Documentation

- Does `README.md` accurately describe how to build, run, and use the project?
- Is there anything in `architecture.md` or `AGENTS.md` that's stale or contradicts reality?
- Are the comments in code explaining *why*, not just *what*?

---

## Phase 3: Write the Review File

Output to `code-reviews/review-2026-03-15.md`. Use this structure exactly:

```markdown
# Code Review — 2026-03-15

## Architecture Summary
[One paragraph. What does this project do, how is it structured, what are the main risk areas?]

## Checks Run
| Command | Result |
|---------|--------|
| {{BUILD_COMMAND}} | ✅ Pass / ❌ Fail |
| {{TEST_COMMAND}} | ✅ Pass / ❌ Fail |

## Findings

| ID | Severity | Category | Location | Problem | Proposed Fix |
|----|----------|----------|----------|---------|--------------|
| R001 | Critical | Correctness | `src/foo.zig:247 handleInput()` | stdin EOF causes infinite loop — process hangs | Change `continue` to `return .skip` on `bytes_read == 0` |
| R002 | High | Security | `src/main.zig:312 runSubprocess()` | User-provided filename passed directly to subprocess argv without validation | Sanitize or reject filenames containing shell metacharacters |
| ... | | | | | |

## Remediation Roadmap

### Fix Now (Blockers)
- R001 — [reason it's blocking]

### Fix Soon (High ROI)
- R002 — [reason + estimated effort S/M/L]

### Fix Later (Refactors)
- [lower priority items]

## Patch Suggestions

For safe, obvious fixes: describe the exact change in terms of file + line + old code → new code.
Do NOT apply patches. Describe them only.

\`\`\`
// src/foo.zig:595 — BEFORE
if (bytes_read == 0) continue;

// AFTER
if (bytes_read == 0) {
    print("No input, defaulting to skip\n", .{});
    return .skip;
}
\`\`\`

## Test Additions Recommended
- [ ] Test: [specific scenario that should be covered]
- [ ] Test: [edge case that could catch a real bug]
```

---

## Severity Guide

| Level | Meaning | Examples |
|-------|---------|---------|
| **Critical** | Data loss, security breach, crash in normal use | Infinite loop on EOF, path traversal from user input |
| **High** | Wrong behavior that will be hit by real users | Error swallowed silently, subprocess arg injection |
| **Med** | Wrong behavior in edge cases or poor degradation | No timeout on external call, missing idempotency |
| **Low** | Quality / maintainability issue, no immediate risk | Duplicate code, unclear name, stale comment |

**Do not inflate severity.** A Low finding reported as Critical trains the human to ignore everything.

---

## What Makes a Good Review

**Good:** "In `src/main.zig:595`, `promptFileAction()` has a `while (true)` loop that calls `stdin.read()`. When stdin is closed (piped input, CI, non-TTY context), `bytes_read` is 0 and the loop `continue`s forever, causing a runaway process. Fix: return `.skip` on `bytes_read == 0`."

**Bad:** "Error handling could be improved throughout the codebase."

The first is actionable. The second is noise that wastes everyone's time.

---

*Generated by init-agent on 2026-03-15*
