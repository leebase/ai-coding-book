---
tracker:
  kind: linear
  project_slug: "ea5b98d43cc4"
  api_key: $LINEAR_API_KEY
  active_states:
    - Todo
    - In Progress
  terminal_states:
    - Done
    - Canceled
    - Duplicate
polling:
  interval_ms: 5000
workspace:
  root: ~/code/symphony-workspaces/ai-env-book
hooks:
  after_create: |
    if ! git clone "${LIVE_REPO_ROOT}" .; then
      git init -b main .
    fi
    rsync -a --delete --exclude '.git' --exclude '.env' --exclude 'symphony-logs/' \
      "${LIVE_REPO_ROOT}/" ./
  before_run: |
    rsync -a --delete --exclude '.git' --exclude '.env' --exclude 'symphony-logs/' \
      "${LIVE_REPO_ROOT}/" ./
    printf '%s' "${LIVE_REPO_ROOT}" > .live-repo-root
  after_run: |
    bash ./scripts/enforce-after-run.sh
agent:
  max_concurrent_agents: 1
  max_turns: 4
codex:
  command: codex --config shell_environment_policy.inherit=all --config model_reasoning_effort=low --model gpt-5.3-codex app-server
  approval_policy: never
  thread_sandbox: workspace-write
  read_timeout_ms: 15000
  turn_sandbox_policy:
    type: workspaceWrite
---

# ai-env-book Workflow Contract

You are a writing agent assigned to one ai-env-book Linear issue.

## Before Acting

Your Linear issue title contains your AENV-xxx id (e.g. "AENV-011 ch-01 draft").
Read only what your task needs — nothing else.

1. `cat AGENTS.md`
2. Extract only your BACKLOG entry — do NOT read the full file:
   - Full entries: `awk "/^### AENV-NNN/,/^---/" BACKLOG.md`
   - Condensed entries: `grep -A 30 "^AENV-NNN:" BACKLOG.md`
   (replace NNN with your three-digit issue number)
3. Read `agents/<owner>.md` (owner is listed in your entry)
4. Read each `skills/<name>.md` listed under `skills:` in your entry
5. If your entry has `input_artifact:`, read each file listed — these are the
   prior-stage artifacts your task builds on

Do not read context.md. Do not read the full BACKLOG.md. Do not read any file
not explicitly listed in steps 1–5.

## Your Job

Advance exactly one issue. Produce the artifact named in the issue entry.
Land it at the declared `artifact_path`. Verify it exists and meets the
definition of done.

## Rules

- Work only inside this repo
- Produce a concrete artifact early — do not spend the run on open-ended analysis
- Stay inside the active issue scope; do not touch other chapter files
- Do not modify `scripts/`, `WORKFLOW.md`, or orchestration files unless the
  issue explicitly requires it
- Do not move the issue to `Done` directly
- As soon as verification passes, write `.symphony-state/completion-ready.md`
  with: artifact path, word count or section count, verification command and result
- After writing the completion marker, make only minimum updates to `context.md`
  and `BACKLOG.md`, then stop
- If blocked, write `.symphony-state/blocked.md` with the exact blocker and stop

## Verification Commands

For chapter briefs, drafts, and finals:
- `wc -w <artifact_path>` — confirm word count in expected range
- `grep -c "^## " <artifact_path>` — confirm required sections present
- Check file exists at the declared canonical path (not in a temp location)

For review memos:
- File exists at declared path
- `grep -c "^## " <artifact_path>` returns >= 5 (all review sections present)

## What Progress Means

Progress is a landed artifact in the live repo, not commentary, issue churn,
or a good-looking workspace. The `after_run` guard will verify this.
