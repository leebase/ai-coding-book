# Product Description — Your Dev Environment: A Guide for AI-Assisted Developers

---

## 1. What does it do?

Teaches new developers just enough about git, GitHub, Python environments, Node/npm, and Warp.dev that they can understand what their AI coding tool is doing — and direct it when something breaks.

---

## 2. What does it NOT do?

- Does not teach git mastery, advanced branching strategy, or rebasing workflows
- Does not teach Python or JavaScript programming
- Does not cover Docker, CI/CD, cloud infrastructure, or deployment
- Does not cover package publishing, monorepos, or advanced npm/pip workflows
- Does not teach Warp.dev as a replacement for a terminal — only as a sysadmin tool for the gaps AI coding tools leave
- Does not belong to the 3-book series (Books 1 and 2); it is a standalone primer
- Does not assume the reader will memorize commands — the goal is recognition, not recall
- Does not cover Windows environments; assumes macOS or Linux

---

## 3. How does the user interact with it?

The reader reads the book linearly. There are no exercises that require running commands independently. Every scenario shows the reader what the AI is doing and why — not what the reader must type.

**Chapter structure per topic:**
- Open with a concrete failure state (the error the reader has seen or will see)
- Explain the mental model in plain language
- Show what the AI does to fix or manage it
- Tell the reader what they need to understand to not undo the fix

**Warp chapters follow a different pattern:**
- Open with the gap (what Antigravity, Codex, or Claude Code cannot do)
- Show a real Warp workflow: describe the problem in plain English, let Warp diagnose
- Close with the division of responsibility: system problems go to Warp, code problems go to the AI coding tool

**The scenario thread:**
A new developer has just cloned a project and is trying to get it running. Each part of the book is a wall they hit in sequence: git confusion → wrong Python env → Node version mismatch → system-level problem that needs Warp. This thread unifies the primer without requiring a separate tutorial project.

---

## 4. What does the data look like?

**Book source files** — all Markdown:

```
ai-env-book/
  product-description.md        # this file
  WORKFLOW.md                   # Symphony contract
  AGENTS.md                     # agent orientation
  context.md                    # session state
  BACKLOG.md                    # issue ledger with AENV-xxx IDs
  agents/
    program-director.md
    researcher.md
    writer.md
    editor-and-qa.md
  skills/
    book-voice.md
    env-explainer.md             # show the error first, then explain why
    warp-expert.md
  scripts/
    bootstrap-workspace.sh
    enforce-after-run.sh
    start-symphony.sh
  chapters/
    briefs/                      # AENV-xxx research brief per chapter
    drafts/                      # AENV-xxx draft per chapter
    reviews/                     # AENV-xxx review memo per chapter
    introduction.md
    ch-01-git.md
    ch-02-github.md
    ch-03-auth.md
    ch-04-branches-and-worktrees.md
    ch-05-when-git-goes-wrong.md
    ch-06-python-env-problem.md
    ch-07-venv-conda-uv.md
    ch-08-requirements-and-pyproject.md
    ch-09-what-node-is.md
    ch-10-nvm-and-versions.md
    ch-11-package-json-and-modules.md
    ch-12-the-gap-warp-fills.md
    ch-13-warp-basics.md
    ch-14-warp-workflows.md
    ch-15-dividing-responsibilities.md
    conclusion.md
```

**BACKLOG.md entry format:**

```
## AENV-001
title: Research brief — ch-01-git
status: Ready
owner: researcher
artifact_path: chapters/briefs/ch-01-git-brief.md
definition_of_done: File exists, >300 words, covers core confusion points and mental model
depends_on: none
```

**Linear issue body format:**

```
Source of truth: BACKLOG.md entry AENV-xxx
Workflow contract: WORKFLOW.md
Artifact: chapters/briefs/ch-01-git-brief.md
Agent: agents/researcher.md + skills/env-explainer.md
Done when: artifact exists in live repo and meets word count and section requirements
```

---

## 5. What does "done" mean for this session?

This product description is written and committed. Planning is complete enough to build the project scaffold — `WORKFLOW.md`, `AGENTS.md`, `BACKLOG.md`, agent files, skill files, and scripts — in the next session.
