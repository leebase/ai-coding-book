# Symphony + Linear Book Workflow Primer

This primer is for another AI working on Connie Book with Symphony and Linear
in a manual, human-directed mode.

It is not for autonomous planning.
It is not for an hourly heartbeat.
It is not for queue self-management.

The intended mode is simple:

1. read the repo-owned project docs
2. understand the next book-writing or tutorial task
3. stage tasks in Linear effectively
4. let Symphony execute one issue at a time
5. land artifacts in the live repo
6. close the issue honestly

## What This Project Is

Connie Book is a daughter-first writing and AI-learning project.

The mission is to help Connie:

- write a book
- learn AI tools while writing it
- build portfolio evidence and operating habits

This repo is also a practical Symphony sandbox, but the runtime exists to
serve the writing mission, not the other way around.

The source of truth for mission and operating rules is:

- [PROJECT_BRIEF.md](/Users/leeharrington/projects/connie-book/PROJECT_BRIEF.md)
- [BACKLOG.md](/Users/leeharrington/projects/connie-book/BACKLOG.md)
- [WORKFLOW.md](/Users/leeharrington/projects/connie-book/WORKFLOW.md)
- [RUN_LOG.md](/Users/leeharrington/projects/connie-book/RUN_LOG.md)
- [AGENTS.md](/Users/leeharrington/projects/connie-book/AGENTS.md)
- [context.md](/Users/leeharrington/projects/connie-book/context.md)

## Current Live Setup

Use these concrete paths and identifiers:

- live repo root: `/Users/leeharrington/projects/connie-book`
- Symphony workflow file: `/Users/leeharrington/projects/connie-book/WORKFLOW.md`
- workspace root: `~/code/symphony-workspaces/connie-book`
- secrets file: `/Users/leeharrington/projects/connie-book/.env`
- manual Symphony launcher: `/Users/leeharrington/projects/connie-book/scripts/start-symphony.sh`
- Linear project URL:
  `https://linear.app/connie-book/project/connie-book-5960e2522285`
- Linear `project_slug` in workflow front matter: `5960e2522285`

Current tracker conventions in this repo:

- local `Ready` maps to Linear `Todo`
- local `Blocked` maps to Linear `Backlog`
- local `Done` maps to Linear `Done`
- terminal states are `Done`, `Canceled`, and `Duplicate`

## The Right Operating Mode

Do this manually and intentionally:

1. Use `BACKLOG.md` as the planning ledger.
2. Use Linear as the execution queue.
3. Keep exactly one active issue in `Todo` unless the human explicitly wants
   concurrency.
4. Stage future issues in `Backlog`.
5. Let Symphony execute the active issue.
6. Verify the artifact landed in the live repo.
7. Only then move the issue to `Done` and promote the next one.

Ignore the hourly automation unless you are explicitly debugging it.

Relevant repo-owned automation files exist under:

- [hourly-automation/](/Users/leeharrington/projects/connie-book/hourly-automation)
- [HOURLY_ORCHESTRATION.md](/Users/leeharrington/projects/connie-book/HOURLY_ORCHESTRATION.md)

Those are not the primary mode for this primer.

## What Another AI Should Read First

Before touching Linear or Symphony, read in this order:

1. [AGENTS.md](/Users/leeharrington/projects/connie-book/AGENTS.md)
2. [context.md](/Users/leeharrington/projects/connie-book/context.md)
3. [result-review.md](/Users/leeharrington/projects/connie-book/result-review.md)
4. [sprint-plan.md](/Users/leeharrington/projects/connie-book/sprint-plan.md)
5. [PROJECT_BRIEF.md](/Users/leeharrington/projects/connie-book/PROJECT_BRIEF.md)
6. [WORKFLOW.md](/Users/leeharrington/projects/connie-book/WORKFLOW.md)
7. the relevant mission files in [agents/](/Users/leeharrington/projects/connie-book/agents)

This repo uses AgentFlow. Shared memory matters here.

## Agent Roles

Use the existing mission files instead of inventing new roles:

- Program Director:
  [agents/program-director.md](/Users/leeharrington/projects/connie-book/agents/program-director.md)
- Curriculum Architect:
  [agents/curriculum-architect.md](/Users/leeharrington/projects/connie-book/agents/curriculum-architect.md)
- Writing Coach:
  [agents/writing-coach.md](/Users/leeharrington/projects/connie-book/agents/writing-coach.md)
- AI Tools Coach:
  [agents/ai-tools-coach.md](/Users/leeharrington/projects/connie-book/agents/ai-tools-coach.md)
- Research and Reference Agent:
  [agents/research-and-reference-agent.md](/Users/leeharrington/projects/connie-book/agents/research-and-reference-agent.md)
- Editor and QA Agent:
  [agents/editor-and-qa-agent.md](/Users/leeharrington/projects/connie-book/agents/editor-and-qa-agent.md)

Default pattern:

- Program Director frames the item
- one or two specialist agents do the actual work
- Editor and QA Agent reviews before `Done`

## How To Load Tasks Into Linear Effectively

Use this pattern, not a giant undifferentiated queue.

### 1. Define the task in `BACKLOG.md` first

Every task should have:

- a stable `CBOOK-xxx` id
- a clear title
- one owner agent
- explicit dependencies
- a concrete `definition_of_done`
- a concrete `artifact_path`

Good task:

- `CBOOK-040 Draft tutorial module 4: revision pass`
- done when one file exists and is reviewable

Bad task:

- `Improve the book`

### 2. Keep task size artifact-sized

A good Symphony issue for this repo usually produces one main artifact:

- one guide
- one outline
- one module
- one checklist
- one review memo

Do not load broad or fuzzy tasks that require many independent outputs.

### 3. Stage only a short runway in Linear

Recommended:

- `1` issue in `Todo`
- `3-7` issues in `Backlog`
- everything else stays in `BACKLOG.md` until it is real enough to stage

This avoids queue theater and keeps issue descriptions current.

### 4. Use a consistent issue title

Use:

- `CBOOK-032 Add reprioritization rules for autonomy-added items`

Do not drop the `CBOOK-xxx` prefix. The repo tooling depends on it.

### 5. Put the real execution contract in the issue body

Issue bodies should say:

- source of truth is `BACKLOG.md`
- workflow contract is `WORKFLOW.md`
- required artifact path
- relevant agent roles
- any special validation or closeout notes

### 6. Promote one item at a time

When the current issue is done and verified:

1. move it to `Done`
2. promote the next staged issue from `Backlog` to `Todo`
3. let Symphony pick it up

Do not front-load many active issues.

## What Symphony Should Actually Do

When Symphony works an issue, it should:

1. read the repo docs
2. read the specific `CBOOK-xxx` entry in `BACKLOG.md`
3. read the relevant agent mission files
4. produce the artifact
5. update repo memory files if the item materially changed project state
6. verify the artifact exists in the live repo
7. only then move the issue toward `Done`

The most important rule is this:

Progress is not commentary.
Progress is a landed artifact in the live source-of-truth tree.

## What To Avoid

Do not ask another AI to:

- run the hourly loop
- invent new backlog items continuously
- keep reprioritizing without human direction
- hold many active issues in Linear
- call an item done because the workspace looks good while the live repo is
  still missing the artifact
- use generic “write the book” prompts

Avoid queue churn. Avoid autonomy theater.

## The Manual Symphony Flow

Use this straight-through sequence.

### Step 1: Orient

Read:

- [AGENTS.md](/Users/leeharrington/projects/connie-book/AGENTS.md)
- [context.md](/Users/leeharrington/projects/connie-book/context.md)
- [WORKFLOW.md](/Users/leeharrington/projects/connie-book/WORKFLOW.md)
- [BACKLOG.md](/Users/leeharrington/projects/connie-book/BACKLOG.md)

### Step 2: Choose the next real task

Pick the highest-value `Ready` item with:

- dependencies already `Done`
- one clear artifact
- clear done criteria

### Step 3: Stage it in Linear

Create or update the Linear issue:

- title starts with the `CBOOK-xxx` id
- issue is in the Connie Book project
- state is `Todo`
- future issues remain in `Backlog`

### Step 4: Start Symphony manually

Use:

```bash
cd /Users/leeharrington/projects/connie-book
./scripts/start-symphony.sh
```

This matters because it loads `.env` correctly before evaluating the workflow.

### Step 5: Let the issue run

Symphony should work inside the correct workspace root:

- `~/code/symphony-workspaces/connie-book`

The workflow will clone and overlay the live repo into the issue workspace.

### Step 6: Verify the artifact in the live repo

Check the declared `artifact_path` in the real repo, not only in the workspace.

### Step 7: Close honestly

Only move the issue to `Done` when:

- the artifact exists in the live repo
- the item meets its definition of done
- the repo memory is updated if needed

## Recommended Task Shapes For Book Work

Strong examples:

- reader profile
- positioning memo
- comparable-books research sheet
- working outline
- section scene map
- one opening-section draft
- one tutorial module
- one revision checklist
- one weekly writing packet

Weak examples:

- “improve all docs”
- “make the book better”
- “do planning”
- “clean up the repo”

## Current State As Of 2026-03-16

The current setup already has:

- live Symphony
- live Linear integration
- repo-owned workflow and hooks
- repo-owned backlog
- repo-owned agent mission files
- book-framing artifacts already landed
- tutorial pipeline already bootstrapped

Current live issue state from [context.md](/Users/leeharrington/projects/connie-book/context.md):

- `CON-36` is `Done`
- `CON-37` is the current active `Todo` issue
- `CBOOK-032` is the current closeout target

This may change, so another AI should always re-read `context.md` before
acting.

## Pasteable Primer For Another AI

Use this prompt:

```text
You are working in /Users/leeharrington/projects/connie-book.

Operate Connie Book in manual Symphony + Linear mode.

Do not use the hourly heartbeat.
Do not do autonomous queue management.
Do not reprioritize broadly unless asked.

Your job is to move one book-writing or tutorial artifact at a time from
BACKLOG.md into Linear, let Symphony execute it, verify the artifact lands in
the live repo, and then close the issue honestly.

Read these first:
1. AGENTS.md
2. context.md
3. result-review.md
4. sprint-plan.md
5. PROJECT_BRIEF.md
6. WORKFLOW.md
7. BACKLOG.md
8. the relevant file(s) in agents/

Use these concrete settings:
- live repo root: /Users/leeharrington/projects/connie-book
- workflow file: /Users/leeharrington/projects/connie-book/WORKFLOW.md
- workspace root: ~/code/symphony-workspaces/connie-book
- Linear project slug: 5960e2522285
- start command: ./scripts/start-symphony.sh

Operating rules:
- BACKLOG.md is the canonical planning ledger
- Linear is the execution queue
- keep exactly one active Todo issue unless explicitly told otherwise
- stage future work in Backlog
- use CBOOK-xxx prefixes in issue titles
- only work items with one clear artifact and a concrete definition of done
- never mark an item Done until the artifact exists in the live repo

Progress means landed work product, not commentary or issue churn.
```

## Final Guidance

If another AI is going to use this setup well, the most important mindset is:

- treat Linear as a queue, not as strategy
- treat Symphony as an execution engine, not as a planner
- treat `BACKLOG.md` and `WORKFLOW.md` as the real contract
- keep tasks small, artifact-first, and reviewable
- close issues only on live repo evidence
