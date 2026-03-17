# ai-env-book Backlog

> Canonical planning ledger. All AENV-xxx issues live here.
>
> **BACKLOG.md** = source of truth for issue definitions, dependencies, and done criteria.
> **Linear** = execution queue. Stage issues here when their `depends_on` are all Done.
> **`blocks`** = set this relation in Linear so Symphony auto-promotes the next issue on completion.
>
> Staging rule: 1 active `Todo`, 3–7 in `Backlog`. Everything else stays here until it's real enough to stage.

---

## Status Key

| Status | Meaning |
|--------|---------|
| `Scaffold` | Built in-session by Claude Code, not via Symphony |
| `Hold` | Blocked on human input before it can be staged |
| `Ready` | Dependencies met; eligible to stage in Linear |
| `Staged` | In Linear as `Backlog` or `Todo` |
| `Done` | Artifact verified in live repo |

---

## Phase 0 — Scaffold (in-session, not Symphony)

These are built directly in Claude Code sessions, not via Linear/Symphony.
Mark Done here when the file exists and has been reviewed.

| ID | Title | Artifact | Status |
|----|-------|----------|--------|
| AENV-S01 | product-description.md | `product-description.md` | Done |
| AENV-S02 | architecture.md | `architecture.md` | Done |
| AENV-S03 | project-plan.md | `project-plan.md` | Done |
| AENV-S04 | sprint-plan.md | `sprint-plan.md` | Done |
| AENV-S05 | BACKLOG.md | `BACKLOG.md` | Done |
| AENV-S06 | AGENTS.md | `AGENTS.md` | ⬜ |
| AENV-S07 | context.md | `context.md` | ⬜ |
| AENV-S08 | WORKFLOW.md | `WORKFLOW.md` | ⬜ |
| AENV-S09 | agents/program-director.md | `agents/program-director.md` | ⬜ |
| AENV-S10 | agents/researcher.md | `agents/researcher.md` | ⬜ |
| AENV-S11 | agents/writer.md | `agents/writer.md` | ⬜ |
| AENV-S12 | agents/editor-and-qa.md | `agents/editor-and-qa.md` | ⬜ |
| AENV-S13 | scripts/bootstrap-workspace.sh | `scripts/bootstrap-workspace.sh` | ⬜ |
| AENV-S14 | scripts/enforce-after-run.sh | `scripts/enforce-after-run.sh` | ⬜ |
| AENV-S15 | scripts/start-symphony.sh | `scripts/start-symphony.sh` | ⬜ |

---

## Phase 1 — Skill Files (Symphony)

Skill files are small, focused Symphony issues. They must land before chapter work begins.
`scenario-thread.md` is the hardest dependency — nothing drafts until it is Done.

---

### AENV-001 — Write skills/scenario-thread.md

```
title:          AENV-001 Write skills/scenario-thread.md
owner:          writer
artifact_path:  skills/scenario-thread.md
depends_on:     none
blocks:         AENV-006, AENV-010, AENV-014, AENV-018, AENV-022, AENV-026,
                AENV-030, AENV-034, AENV-038, AENV-042, AENV-046, AENV-050,
                AENV-054, AENV-058, AENV-062, AENV-066 (all chapter briefs)
status:         Staged
verification:   wc -w skills/scenario-thread.md (target >400 words)
                grep -c "^## " skills/scenario-thread.md (>=4 sections)
definition_of_done: |
  File exists. Encodes: who the reader is, the project they cloned, the exact
  error messages they hit in each part, the tools and versions assumed, and the
  canonical names for all scenario elements. Any agent reading this file can
  write a chapter that slots into the scenario without inventing new details.
notes: |
  This is the most important skill file. Lock it before staging any chapter brief.
  If the scenario needs to evolve after Part 1 is written, update this file first
  and note the change — do not let agents drift from it silently.
```

---

### AENV-002 — Write skills/book-voice.md

```
title:          AENV-002 Write skills/book-voice.md
owner:          writer
artifact_path:  skills/book-voice.md
depends_on:     none
blocks:         AENV-007, AENV-011, AENV-015, AENV-019, AENV-023, AENV-027,
                AENV-031, AENV-035, AENV-039, AENV-043, AENV-047, AENV-051,
                AENV-055, AENV-059, AENV-063, AENV-067 (all chapter drafts)
status:         Staged
verification:   wc -w skills/book-voice.md (target >400 words)
definition_of_done: |
  File exists. Written fresh for this book — not inherited from ai-coding-book.
  Encodes: the new-dev reader profile, the peer register (patient but not
  condescending), the "show the error first" pattern, what to avoid (tutorial
  condescension, command memorization mode, cheerleading), and callout box rules.
notes: |
  The ai-coding-book book-voice.md targets experienced developers. This version
  must target new developers. Different audience, different register. Do not copy.
```

---

### AENV-003 — Write skills/env-explainer.md

```
title:          AENV-003 Write skills/env-explainer.md
owner:          writer
artifact_path:  skills/env-explainer.md
depends_on:     none
blocks:         AENV-007, AENV-011, AENV-015, AENV-019, AENV-023, AENV-027,
                AENV-031, AENV-035, AENV-039 (all chapter drafts, Parts 1–3)
status:         Staged
verification:   wc -w skills/env-explainer.md (target >300 words)
definition_of_done: |
  File exists. Encodes the pattern for explaining environment concepts: show the
  real error message first, then explain the mental model, then show what the AI
  does to fix it. Includes guidance on what level of detail is right (recognition,
  not mastery) and what analogies work for new devs.
```

---

### AENV-004 — Write skills/new-dev-validator.md

```
title:          AENV-004 Write skills/new-dev-validator.md
owner:          writer
artifact_path:  skills/new-dev-validator.md
depends_on:     none
blocks:         AENV-008, AENV-012, AENV-016, AENV-020, AENV-024, AENV-028,
                AENV-032, AENV-036, AENV-040, AENV-044, AENV-048, AENV-052,
                AENV-056, AENV-060, AENV-064, AENV-068 (all chapter reviews)
status:         Completion-ready
verification:   wc -w skills/new-dev-validator.md (target >300 words)
definition_of_done: |
  File exists. Encodes how to attack a chapter draft from the zero-context reader
  perspective. Questions to ask: Are there implicit prerequisites? Does it assume
  terminal familiarity? Does it explain what a command does before showing it?
  Is the error message shown before the fix? Flags must be concrete and actionable.
```

---

### AENV-005 — Write skills/warp-expert.md

```
title:          AENV-005 Write skills/warp-expert.md
owner:          writer
artifact_path:  skills/warp-expert.md
depends_on:     none
blocks:         AENV-054, AENV-058, AENV-062, AENV-066 (Warp chapter briefs)
status:         completion-ready
verification:   wc -w skills/warp-expert.md (target >500 words)
definition_of_done: |
  File exists. Contains accurate, current Warp.dev feature descriptions: AI Command
  (how to invoke, what it does), Warp Drive (shared workflows), blocks/notebooks,
  the gap Warp fills vs AI coding tools, and 3–5 concrete sysadmin workflow patterns.
  Must be based on real Warp knowledge — not generated from general knowledge.
notes: |
  Web research pass completed 2026-03-16. Verified against warp.dev/docs and
  warp.dev/all-features. Five concrete sysadmin workflow patterns written.
  Warp chapter briefs (AENV-054 onward) are now unblocked.
```

---

## Phase 2 — Introduction

### AENV-006 — Introduction brief

```
title:          AENV-006 Introduction brief
owner:          researcher
artifact_path:  chapters/briefs/introduction-brief.md
depends_on:     AENV-001 (scenario-thread)
blocks:         AENV-007
status:         Ready (once AENV-001 Done)
verification:   wc -w chapters/briefs/introduction-brief.md (target >300 words)
                grep -c "^## " chapters/briefs/introduction-brief.md (>=3 sections)
definition_of_done: |
  File exists. Covers: who this book is for, what the scenario is, what the reader
  will be able to do after reading, how the four parts connect, and the thesis
  (you don't need to be a sysadmin — you need to recognize what you're looking at).
skills:         env-explainer
```

---

### AENV-007 — Introduction draft

```
title:          AENV-007 Introduction draft
owner:          writer
artifact_path:  chapters/drafts/introduction.md
depends_on:     AENV-002 (book-voice), AENV-003 (env-explainer), AENV-006 (brief)
blocks:         AENV-008
status:         Ready (once dependencies Done)
verification:   wc -w chapters/drafts/introduction.md (target 1200–1800 words)
definition_of_done: |
  File exists. Hits: hook (the wall new devs hit), thesis, what the book covers,
  the scenario introduced, what the reader needs before starting. Ends with one
  sentence pointing into Part 1.
skills:         book-voice, env-explainer, scenario-thread
```

---

### AENV-008 — Introduction review

```
title:          AENV-008 Introduction review
owner:          editor-and-qa
artifact_path:  chapters/reviews/introduction-review.md
depends_on:     AENV-004 (new-dev-validator), AENV-007 (draft)
blocks:         AENV-009
status:         Ready (once dependencies Done)
verification:   file exists, grep -c "^## " >=3 sections
definition_of_done: |
  Review memo exists. Covers: voice check, new-dev comprehension attack,
  scenario accuracy, thesis clarity. Actionable notes only — no praise.
skills:         book-voice, new-dev-validator, scenario-thread
```

---

### AENV-009 — Introduction final

```
title:          AENV-009 Introduction final
owner:          writer
artifact_path:  chapters/introduction.md
depends_on:     AENV-008 (review)
blocks:         none
status:         Ready (once AENV-008 Done)
verification:   wc -w chapters/introduction.md (target 1200–1800 words)
                file exists at canonical path (not drafts/)
definition_of_done: |
  Final file exists at chapters/introduction.md. Review notes addressed.
  Word count in range. Scenario established correctly.
skills:         book-voice, scenario-thread
```

---

## Phase 3 — Part 1: Git and GitHub

*Issue pattern repeats for all 5 chapters. Each brief→draft→review→final chain is independent of other chapters at the brief stage, but should be worked serially to maintain scenario continuity.*

---

### Chapter 1 — What Git Actually Is

#### AENV-010 — ch-01 brief

```
title:          AENV-010 ch-01 brief — What Git Actually Is
owner:          researcher
artifact_path:  chapters/briefs/ch-01-brief.md
depends_on:     AENV-001 (scenario-thread)
blocks:         AENV-011
status:         Ready (once AENV-001 Done)
verification:   wc -w chapters/briefs/ch-01-brief.md (target >300 words)
definition_of_done: |
  Core confusions identified: what "staging" means, why commits exist, what the
  .git folder is, what "untracked" means. Mental model angle selected. Scenario
  wall identified (reader tries to understand what git init did).
skills:         env-explainer, scenario-thread
```

#### AENV-011 — ch-01 draft

```
title:          AENV-011 ch-01 draft — What Git Actually Is
owner:          writer
artifact_path:  chapters/drafts/ch-01-git.md
depends_on:     AENV-002 (book-voice), AENV-003 (env-explainer), AENV-010 (brief)
blocks:         AENV-012
status:         Ready (once dependencies Done)
verification:   wc -w chapters/drafts/ch-01-git.md (target 1500–2500 words)
definition_of_done: |
  Draft covers: snapshots not diffs, the three areas (working/staging/committed),
  what .git is, the 5 commands the reader will see their AI use. Scenario wall shown
  and resolved. Ends with one forward sentence.
skills:         book-voice, env-explainer, scenario-thread
```

#### AENV-012 — ch-01 review

```
title:          AENV-012 ch-01 review — What Git Actually Is
owner:          editor-and-qa
artifact_path:  chapters/reviews/ch-01-review.md
depends_on:     AENV-004 (new-dev-validator), AENV-011 (draft)
blocks:         AENV-013
status:         Ready (once dependencies Done)
verification:   file exists
definition_of_done: |
  Review memo with actionable notes. New-dev attack applied. Voice check done.
  Scenario accuracy confirmed. No command memorization drift.
skills:         book-voice, new-dev-validator, scenario-thread
```

#### AENV-013 — ch-01 final

```
title:          AENV-013 ch-01 final — What Git Actually Is
owner:          writer
artifact_path:  chapters/ch-01-git.md
depends_on:     AENV-012 (review)
blocks:         none
status:         Ready (once AENV-012 Done)
verification:   wc -w chapters/ch-01-git.md (target 1500–2500 words)
                file exists at canonical path
definition_of_done: Review notes addressed. Final at chapters/ch-01-git.md.
skills:         book-voice, scenario-thread
```

---

### Chapter 2 — GitHub: Where Your Code Lives

#### AENV-014 — ch-02 brief

```
title:          AENV-014 ch-02 brief — GitHub: Where Your Code Lives
owner:          researcher
artifact_path:  chapters/briefs/ch-02-brief.md
depends_on:     AENV-001 (scenario-thread)
blocks:         AENV-015
verification:   wc -w >300, sections present
definition_of_done: |
  Core confusions: remote vs local, public vs private (and why it matters),
  what a fork is, what the README does, why the AI needs a remote to push.
  Scenario wall: reader tries to find their code on GitHub and can't.
skills:         env-explainer, scenario-thread
```

#### AENV-015 — ch-02 draft

```
title:          AENV-015 ch-02 draft — GitHub: Where Your Code Lives
owner:          writer
artifact_path:  chapters/drafts/ch-02-github.md
depends_on:     AENV-002, AENV-003, AENV-014
blocks:         AENV-016
verification:   wc -w 1500–2500
skills:         book-voice, env-explainer, scenario-thread
definition_of_done: Covers remote vs local, public/private, forks, README as front door, why remote matters for AI-assisted work.
```

#### AENV-016 — ch-02 review

```
title:          AENV-016 ch-02 review — GitHub: Where Your Code Lives
owner:          editor-and-qa
artifact_path:  chapters/reviews/ch-02-review.md
depends_on:     AENV-004, AENV-015
blocks:         AENV-017
skills:         book-voice, new-dev-validator, scenario-thread
definition_of_done: Review memo with actionable notes.
```

#### AENV-017 — ch-02 final

```
title:          AENV-017 ch-02 final — GitHub: Where Your Code Lives
owner:          writer
artifact_path:  chapters/ch-02-github.md
depends_on:     AENV-016
blocks:         none
verification:   wc -w 1500–2500, file at canonical path
skills:         book-voice, scenario-thread
definition_of_done: Review notes addressed. Final at chapters/ch-02-github.md.
```

---

### Chapter 3 — Getting Your Computer Authorized

#### AENV-018 — ch-03 brief

```
title:          AENV-018 ch-03 brief — Getting Your Computer Authorized
owner:          researcher
artifact_path:  chapters/briefs/ch-03-brief.md
depends_on:     AENV-001
blocks:         AENV-019
definition_of_done: |
  Core confusions: SSH keys vs HTTPS tokens, why auth is required to push,
  what "permission denied (publickey)" means, how to check if auth is set up.
  Scenario wall: AI tries to push and gets auth error. One-time setup framing.
skills:         env-explainer, scenario-thread
```

#### AENV-019 — ch-03 draft

```
title:          AENV-019 ch-03 draft — Getting Your Computer Authorized
owner:          writer
artifact_path:  chapters/drafts/ch-03-auth.md
depends_on:     AENV-002, AENV-003, AENV-018
blocks:         AENV-020
verification:   wc -w 1500–2500
skills:         book-voice, env-explainer, scenario-thread
definition_of_done: Covers SSH vs HTTPS, generating a key, adding to GitHub, why the AI needs this, "set it once" framing.
```

#### AENV-020 — ch-03 review

```
title:          AENV-020 ch-03 review — Getting Your Computer Authorized
owner:          editor-and-qa
artifact_path:  chapters/reviews/ch-03-review.md
depends_on:     AENV-004, AENV-019
blocks:         AENV-021
skills:         book-voice, new-dev-validator, scenario-thread
definition_of_done: Review memo with actionable notes.
```

#### AENV-021 — ch-03 final

```
title:          AENV-021 ch-03 final — Getting Your Computer Authorized
owner:          writer
artifact_path:  chapters/ch-03-auth.md
depends_on:     AENV-020
blocks:         none
verification:   wc -w 1500–2500, file at canonical path
skills:         book-voice, scenario-thread
definition_of_done: Review notes addressed. Final at chapters/ch-03-auth.md.
```

---

### Chapter 4 — Branches and Worktrees

#### AENV-022 — ch-04 brief

```
title:          AENV-022 ch-04 brief — Branches and Worktrees
owner:          researcher
artifact_path:  chapters/briefs/ch-04-brief.md
depends_on:     AENV-001
blocks:         AENV-023
definition_of_done: |
  Core confusions: what a branch is (a label on a snapshot, not a copy),
  why AI tools create branches, what a worktree is and why Claude Code / Codex
  spin them up, what the reader sees in their file system when this happens.
  Frame: you don't manage these — you don't panic when you see them.
skills:         env-explainer, scenario-thread
```

#### AENV-023 — ch-04 draft

```
title:          AENV-023 ch-04 draft — Branches and Worktrees
owner:          writer
artifact_path:  chapters/drafts/ch-04-branches-and-worktrees.md
depends_on:     AENV-002, AENV-003, AENV-022
blocks:         AENV-024
verification:   wc -w 1500–2500
skills:         book-voice, env-explainer, scenario-thread
definition_of_done: Covers branch as label, why AI tools use branches, worktrees explained, what reader sees, what not to do.
```

#### AENV-024 — ch-04 review

```
title:          AENV-024 ch-04 review — Branches and Worktrees
owner:          editor-and-qa
artifact_path:  chapters/reviews/ch-04-review.md
depends_on:     AENV-004, AENV-023
blocks:         AENV-025
skills:         book-voice, new-dev-validator, scenario-thread
definition_of_done: Review memo with actionable notes.
```

#### AENV-025 — ch-04 final

```
title:          AENV-025 ch-04 final — Branches and Worktrees
owner:          writer
artifact_path:  chapters/ch-04-branches-and-worktrees.md
depends_on:     AENV-024
blocks:         none
verification:   wc -w 1500–2500, file at canonical path
skills:         book-voice, scenario-thread
definition_of_done: Review notes addressed. Final at canonical path.
```

---

### Chapter 5 — When Git Goes Wrong

#### AENV-026 — ch-05 brief

```
title:          AENV-026 ch-05 brief — When Git Goes Wrong
owner:          researcher
artifact_path:  chapters/briefs/ch-05-brief.md
depends_on:     AENV-001
blocks:         AENV-027
definition_of_done: |
  Core errors catalogued: detached HEAD, merge conflict, "nothing to commit",
  "rejected (non-fast-forward)". For each: what it looks like, what it means,
  what to hand to the AI vs what to fix yourself.
skills:         env-explainer, scenario-thread
```

#### AENV-027 — ch-05 draft

```
title:          AENV-027 ch-05 draft — When Git Goes Wrong
owner:          writer
artifact_path:  chapters/drafts/ch-05-when-git-goes-wrong.md
depends_on:     AENV-002, AENV-003, AENV-026
blocks:         AENV-028
verification:   wc -w 1500–2500
skills:         book-voice, env-explainer, scenario-thread
definition_of_done: Covers 4+ error states. Pattern per error: show the message, explain it, divide the fix responsibility.
```

#### AENV-028 — ch-05 review

```
title:          AENV-028 ch-05 review — When Git Goes Wrong
owner:          editor-and-qa
artifact_path:  chapters/reviews/ch-05-review.md
depends_on:     AENV-004, AENV-027
blocks:         AENV-029
skills:         book-voice, new-dev-validator, scenario-thread
definition_of_done: Review memo with actionable notes.
```

#### AENV-029 — ch-05 final

```
title:          AENV-029 ch-05 final — When Git Goes Wrong
owner:          writer
artifact_path:  chapters/ch-05-when-git-goes-wrong.md
depends_on:     AENV-028
blocks:         none
verification:   wc -w 1500–2500, file at canonical path
skills:         book-voice, scenario-thread
definition_of_done: Review notes addressed. Final at canonical path.
```

---

## Phase 4 — Part 2: Python Environments

### Chapter 6 — Why Python Has an Environment Problem

#### AENV-030 through AENV-033

```
AENV-030: ch-06 brief
  artifact:     chapters/briefs/ch-06-brief.md
  depends_on:   AENV-001
  blocks:       AENV-031
  definition:   Core confusion: why you can't just pip install globally. What an
                environment actually isolates. The "it worked on my machine" wall.
  skills:       env-explainer, scenario-thread

AENV-031: ch-06 draft
  artifact:     chapters/drafts/ch-06-python-env-problem.md
  depends_on:   AENV-002, AENV-003, AENV-030
  blocks:       AENV-032
  verification: wc -w 1500–2500
  skills:       book-voice, env-explainer, scenario-thread

AENV-032: ch-06 review
  artifact:     chapters/reviews/ch-06-review.md
  depends_on:   AENV-004, AENV-031
  blocks:       AENV-033
  skills:       book-voice, new-dev-validator, scenario-thread

AENV-033: ch-06 final
  artifact:     chapters/ch-06-python-env-problem.md
  depends_on:   AENV-032
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

### Chapter 7 — venv, conda, uv — Which One and Why

#### AENV-034 through AENV-037

```
AENV-034: ch-07 brief
  artifact:     chapters/briefs/ch-07-brief.md
  depends_on:   AENV-001
  blocks:       AENV-035
  definition:   Landscape explained plainly. When uv is the right answer. How to
                tell which env is active. What "activated" actually does.
  skills:       env-explainer, scenario-thread

AENV-035: ch-07 draft
  artifact:     chapters/drafts/ch-07-venv-conda-uv.md
  depends_on:   AENV-002, AENV-003, AENV-034
  blocks:       AENV-036
  verification: wc -w 1500–2500
  skills:       book-voice, env-explainer, scenario-thread

AENV-036: ch-07 review
  artifact:     chapters/reviews/ch-07-review.md
  depends_on:   AENV-004, AENV-035
  blocks:       AENV-037
  skills:       book-voice, new-dev-validator, scenario-thread

AENV-037: ch-07 final
  artifact:     chapters/ch-07-venv-conda-uv.md
  depends_on:   AENV-036
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

### Chapter 8 — Reading requirements.txt and pyproject.toml

#### AENV-038 through AENV-041

```
AENV-038: ch-08 brief
  artifact:     chapters/briefs/ch-08-brief.md
  depends_on:   AENV-001
  blocks:       AENV-039
  definition:   What these files say. How to hand them to the AI. What version
                constraints mean. Why pyproject.toml is replacing requirements.txt.
  skills:       env-explainer, scenario-thread

AENV-039: ch-08 draft
  artifact:     chapters/drafts/ch-08-requirements-and-pyproject.md
  depends_on:   AENV-002, AENV-003, AENV-038
  blocks:       AENV-040
  verification: wc -w 1500–2500
  skills:       book-voice, env-explainer, scenario-thread

AENV-040: ch-08 review
  artifact:     chapters/reviews/ch-08-review.md
  depends_on:   AENV-004, AENV-039
  blocks:       AENV-041
  skills:       book-voice, new-dev-validator, scenario-thread

AENV-041: ch-08 final
  artifact:     chapters/ch-08-requirements-and-pyproject.md
  depends_on:   AENV-040
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

## Phase 5 — Part 3: Node and npm

### Chapter 9 — What Node Is (and Why It's on Your Machine)

#### AENV-042 through AENV-045

```
AENV-042: ch-09 brief
  artifact:     chapters/briefs/ch-09-brief.md
  depends_on:   AENV-001
  blocks:       AENV-043
  definition:   Runtime vs language distinction. Why Node is installed even for
                non-JS projects. What "node not found" means when it appears.
  skills:       env-explainer, scenario-thread

AENV-043: ch-09 draft
  artifact:     chapters/drafts/ch-09-what-node-is.md
  depends_on:   AENV-002, AENV-003, AENV-042
  blocks:       AENV-044
  verification: wc -w 1500–2500
  skills:       book-voice, env-explainer, scenario-thread

AENV-044: ch-09 review
  artifact:     chapters/reviews/ch-09-review.md
  depends_on:   AENV-004, AENV-043
  blocks:       AENV-045
  skills:       book-voice, new-dev-validator, scenario-thread

AENV-045: ch-09 final
  artifact:     chapters/ch-09-what-node-is.md
  depends_on:   AENV-044
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

### Chapter 10 — nvm and Node Versions

#### AENV-046 through AENV-049

```
AENV-046: ch-10 brief
  artifact:     chapters/briefs/ch-10-brief.md
  depends_on:   AENV-001
  blocks:       AENV-047
  definition:   Why version management exists. What .nvmrc is and who reads it.
                What "wrong Node version" errors look like. AI manages this — here
                is what it is doing.
  skills:       env-explainer, scenario-thread

AENV-047: ch-10 draft
  artifact:     chapters/drafts/ch-10-nvm-and-versions.md
  depends_on:   AENV-002, AENV-003, AENV-046
  blocks:       AENV-048
  verification: wc -w 1500–2500
  skills:       book-voice, env-explainer, scenario-thread

AENV-048: ch-10 review
  artifact:     chapters/reviews/ch-10-review.md
  depends_on:   AENV-004, AENV-047
  blocks:       AENV-049
  skills:       book-voice, new-dev-validator, scenario-thread

AENV-049: ch-10 final
  artifact:     chapters/ch-10-nvm-and-versions.md
  depends_on:   AENV-048
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

### Chapter 11 — package.json and node_modules

#### AENV-050 through AENV-053

```
AENV-050: ch-11 brief
  artifact:     chapters/briefs/ch-11-brief.md
  depends_on:   AENV-001
  blocks:       AENV-051
  definition:   What package.json declares. Why npm install is always step one.
                Why node_modules is in .gitignore. What "missing module" errors mean.
  skills:       env-explainer, scenario-thread

AENV-051: ch-11 draft
  artifact:     chapters/drafts/ch-11-package-json-and-modules.md
  depends_on:   AENV-002, AENV-003, AENV-050
  blocks:       AENV-052
  verification: wc -w 1500–2500
  skills:       book-voice, env-explainer, scenario-thread

AENV-052: ch-11 review
  artifact:     chapters/reviews/ch-11-review.md
  depends_on:   AENV-004, AENV-051
  blocks:       AENV-053
  skills:       book-voice, new-dev-validator, scenario-thread

AENV-053: ch-11 final
  artifact:     chapters/ch-11-package-json-and-modules.md
  depends_on:   AENV-052
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

## Phase 6 — Part 4: Warp

> All Warp chapter briefs depend on AENV-005 (warp-expert.md) in addition to AENV-001.
> Do not stage any issue in this phase until AENV-005 is Done.

### Chapter 12 — The Gap Warp Fills

#### AENV-054 through AENV-057

```
AENV-054: ch-12 brief
  artifact:     chapters/briefs/ch-12-brief.md
  depends_on:   AENV-001, AENV-005
  blocks:       AENV-055
  definition:   What AI coding tools cannot do: process management, PATH problems,
                system config, ad-hoc env debugging. Why this gap exists by design.
                What happens when a new dev hits it with no Warp.
  skills:       env-explainer, warp-expert, scenario-thread

AENV-055: ch-12 draft
  artifact:     chapters/drafts/ch-12-the-gap-warp-fills.md
  depends_on:   AENV-002, AENV-003, AENV-005, AENV-054
  blocks:       AENV-056
  verification: wc -w 1500–2500
  skills:       book-voice, warp-expert, scenario-thread

AENV-056: ch-12 review
  artifact:     chapters/reviews/ch-12-review.md
  depends_on:   AENV-004, AENV-055
  blocks:       AENV-057
  skills:       book-voice, new-dev-validator, warp-expert, scenario-thread

AENV-057: ch-12 final
  artifact:     chapters/ch-12-the-gap-warp-fills.md
  depends_on:   AENV-056
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

### Chapter 13 — Warp Basics

#### AENV-058 through AENV-061

```
AENV-058: ch-13 brief
  artifact:     chapters/briefs/ch-13-brief.md
  depends_on:   AENV-001, AENV-005
  blocks:       AENV-059
  definition:   Terminal as a tool, not a black box. AI Command: how to invoke,
                what it produces. Warp Drive basics. The shift: describe the
                problem in plain English.
  skills:       warp-expert, scenario-thread

AENV-059: ch-13 draft
  artifact:     chapters/drafts/ch-13-warp-basics.md
  depends_on:   AENV-002, AENV-005, AENV-058
  blocks:       AENV-060
  verification: wc -w 1500–2500
  skills:       book-voice, warp-expert, scenario-thread

AENV-060: ch-13 review
  artifact:     chapters/reviews/ch-13-review.md
  depends_on:   AENV-004, AENV-059
  blocks:       AENV-061
  skills:       book-voice, new-dev-validator, warp-expert, scenario-thread

AENV-061: ch-13 final
  artifact:     chapters/ch-13-warp-basics.md
  depends_on:   AENV-060
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

### Chapter 14 — Warp Workflows for Developers

#### AENV-062 through AENV-065

```
AENV-062: ch-14 brief
  artifact:     chapters/briefs/ch-14-brief.md
  depends_on:   AENV-001, AENV-005
  blocks:       AENV-063
  definition:   3–4 concrete Warp workflows: something broke (find out why),
                kill a process, fix a PATH problem, set an env variable permanently.
                Pattern per workflow: describe the problem, what Warp does, what
                the reader sees.
  skills:       warp-expert, scenario-thread

AENV-063: ch-14 draft
  artifact:     chapters/drafts/ch-14-warp-workflows.md
  depends_on:   AENV-002, AENV-005, AENV-062
  blocks:       AENV-064
  verification: wc -w 1500–2500
  skills:       book-voice, warp-expert, scenario-thread

AENV-064: ch-14 review
  artifact:     chapters/reviews/ch-14-review.md
  depends_on:   AENV-004, AENV-063
  blocks:       AENV-065
  skills:       book-voice, new-dev-validator, warp-expert, scenario-thread

AENV-065: ch-14 final
  artifact:     chapters/ch-14-warp-workflows.md
  depends_on:   AENV-064
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

### Chapter 15 — Dividing Responsibilities

#### AENV-066 through AENV-069

```
AENV-066: ch-15 brief
  artifact:     chapters/briefs/ch-15-brief.md
  depends_on:   AENV-001, AENV-005
  blocks:       AENV-067
  definition:   The decision model: system problems go to Warp, code problems go
                to the AI coding tool. Heuristics for the boundary. What happens
                when you pick the wrong tool.
  skills:       warp-expert, scenario-thread

AENV-067: ch-15 draft
  artifact:     chapters/drafts/ch-15-dividing-responsibilities.md
  depends_on:   AENV-002, AENV-005, AENV-066
  blocks:       AENV-068
  verification: wc -w 1500–2500
  skills:       book-voice, warp-expert, scenario-thread

AENV-068: ch-15 review
  artifact:     chapters/reviews/ch-15-review.md
  depends_on:   AENV-004, AENV-067
  blocks:       AENV-069
  skills:       book-voice, new-dev-validator, warp-expert, scenario-thread

AENV-069: ch-15 final
  artifact:     chapters/ch-15-dividing-responsibilities.md
  depends_on:   AENV-068
  verification: wc -w 1500–2500, file at canonical path
  skills:       book-voice, scenario-thread
```

---

## Phase 7 — Conclusion

#### AENV-070 through AENV-073

```
AENV-070: conclusion brief
  artifact:     chapters/briefs/conclusion-brief.md
  depends_on:   AENV-001
  blocks:       AENV-071
  definition:   Restate thesis with evidence. What the reader can do now. Where
                to go next. Honest about what the book doesn't cover.
  skills:       env-explainer, scenario-thread

AENV-071: conclusion draft
  artifact:     chapters/drafts/conclusion.md
  depends_on:   AENV-002, AENV-070
  blocks:       AENV-072
  verification: wc -w 1200–1800
  skills:       book-voice, scenario-thread

AENV-072: conclusion review
  artifact:     chapters/reviews/conclusion-review.md
  depends_on:   AENV-004, AENV-071
  blocks:       AENV-073
  skills:       book-voice, new-dev-validator, scenario-thread

AENV-073: conclusion final
  artifact:     chapters/conclusion.md
  depends_on:   AENV-072
  verification: wc -w 1200–1800, file at canonical path
  skills:       book-voice, scenario-thread
```

---

## Phase 8 — Polish

```
AENV-074: Continuity pass
  artifact:     chapters/reviews/continuity-pass.md
  depends_on:   AENV-073 (conclusion final — all chapters must be Done)
  owner:        editor-and-qa
  definition:   Read all chapters sequentially. Fix scenario drift, voice
                inconsistencies, broken cross-references. Produce a memo of
                changes made.

AENV-075: Copyedit pass
  artifact:     (in-place edits to all chapter files)
  depends_on:   AENV-074
  owner:        editor-and-qa
  definition:   Line-level polish. Tighten prose, remove repetition, verify
                callout boxes. All chapters at target word count.
```

---

## Phase 9 — Publication

```
AENV-076: Publication format decision and output
  artifact:     TBD (EPUB, PDF, or both)
  depends_on:   AENV-075
  owner:        program-director
  status:       Hold — format decision deferred
```
