# ai-env-book Architecture

## Primary Architecture

This project is documentation-first and workflow-first.

The core system is:

1. repo-owned planning artifacts
2. a structured backlog (AENV-xxx IDs)
3. agent mission files keyed to writing stages
4. a Symphony-compatible `WORKFLOW.md`
5. Linear as execution queue, advanced one issue at a time

There is no hourly automation, no autonomous queue selection, and no heartbeat.
A human stages work in Linear. Symphony executes it. Artifacts land in the live repo.

---

## Major Components

### Planning Layer

- `product-description.md` — scope, constraints, chapter map, definition of done
- `architecture.md` — this file; structure and decisions
- `context.md` — session state and handoff notes
- `BACKLOG.md` — canonical ledger of all AENV-xxx issues
- `sprint-plan.md` — active sprint tracking

### Agent Layer

- `agents/program-director.md` — frames issues, sets scope before Symphony runs
- `agents/researcher.md` — produces the chapter brief; owns the "what's the core confusion?" question
- `agents/writer.md` — drafts the chapter from the brief; reads `skills/book-voice.md`
- `agents/editor-and-qa.md` — reviews draft against voice, scope, and accuracy; produces review memo

### Skills Layer

- `skills/book-voice.md` — voice for a new dev reader: patient but not condescending, peer register, show the error first. **Not the Books 1–2 version** — that file targets experienced devs. This one must be written fresh.
- `skills/env-explainer.md` — how to explain environment concepts to new devs; mental model first, commands second; show the real error message before explaining why
- `skills/new-dev-validator.md` — attack each draft from the zero-context reader perspective; ask "what does someone who doesn't know what PATH is do here?"; flag missing prerequisites, implicit setup, and unexplained transitions
- `skills/scenario-thread.md` — canonical state of the running scenario (who the reader is, what project they cloned, what errors they've hit, what has been fixed so far); loaded by every writer and reviewer run to prevent drift across 15 chapters written in separate Symphony runs
- `skills/warp-expert.md` — Warp.dev patterns: AI Command, Warp Drive, system-level debugging workflows. **Requires real Warp knowledge as input** — must be authored by Lee or built from a web research pass before first use; do not generate from general knowledge

### Orchestration Layer

- `WORKFLOW.md` — Symphony contract; hooks for before_run, after_run; agent startup protocol
- `scripts/bootstrap-workspace.sh` — clones and overlays live repo into Symphony workspace
- `scripts/enforce-after-run.sh` — validates artifact landed in live repo before allowing Done
- `scripts/start-symphony.sh` — manual launcher; loads .env before evaluating WORKFLOW.md

---

## Writing Pipeline Design

Each chapter is a chain of four Linear issues, each blocking the next via Linear `blocks` relations.

```
AENV-xxx  Research brief   →  chapters/briefs/ch-xx.md
AENV-xxx  Draft            →  chapters/drafts/ch-xx.md
AENV-xxx  Review           →  chapters/reviews/ch-xx-review.md
AENV-xxx  Revise + final   →  chapters/ch-xx.md
```

### Issue sizing rule

One issue = one artifact. If the issue description contains more than one meaningful
"and", it is too broad for Symphony.

### Verification rule

Every issue must name one verification command. For writing issues:

- `wc -w <artifact_path>` — word count in expected range
- `grep -c "^## " <artifact_path>` — required sections present
- file existence check — artifact landed at the declared path

### Agent assignment per stage

| Stage | Agent | Skills loaded |
|-------|-------|---------------|
| Research brief | researcher | env-explainer |
| Draft | writer | book-voice, env-explainer |
| Review | editor-and-qa | book-voice |
| Revise + final | writer | book-voice, review memo from prior stage |

---

## Runtime Design

- Human reads `BACKLOG.md`, selects the next ready item, stages it in Linear as `Todo`
- All future items remain in `Backlog` state in Linear
- Human starts Symphony manually via `scripts/start-symphony.sh`
- Symphony clones the live repo into the workspace, runs the agent, syncs back
- `enforce-after-run.sh` checks that the declared artifact exists in the live repo
- Human verifies artifact, moves issue to `Done`, promotes the next item
- One active `Todo` at all times unless explicitly running two independent items

Progress is a landed artifact in the live repo, not commentary, not issue churn.

---

## Book Structure Decisions

### 2026-03-16 — Standalone primer, not part of the 3-book series

**Decision:** ai-env-book is a standalone product. It is not Book 0, not a companion,
not a prerequisite gate for Books 1 and 2.

**Rationale:** Books 1 and 2 form a coherent arc for developers who are already
functional. This primer serves a different reader — someone earlier in their journey —
and should not be coupled to that arc in either direction.

**Alternatives rejected:** Positioning it as Book 0 would imply a reading order that
doesn't serve either audience well. A companion label would subordinate it.

**Consequences:** Marketing, framing, and distribution are independent. The book
stands alone on its own value proposition.

---

### 2026-03-16 — 15 chapters across 4 parts plus intro and conclusion

**Decision:** The chapter map is: Introduction, Part 1 (Git + GitHub, 5 chapters),
Part 2 (Python Environments, 3 chapters), Part 3 (Node/npm, 3 chapters),
Part 4 (Warp, 4 chapters), Conclusion.

**Rationale:** Each part covers one environment domain. Warp gets more chapters
than any single technical topic because it is the novel recommendation — readers
need to understand why the gap exists, not just how to use the tool.

**Alternatives rejected:** Combining git and GitHub into one chapter loses the
important distinction between local version control and the hosted platform, and
the authorization setup needed for AI-managed pushes.

**Consequences:** The four-issue chain per chapter produces 60+ Linear issues total.
Stage them in short runways (1 active, 3–7 in Backlog) to keep issue descriptions
current.

---

### 2026-03-16 — Scenario thread as structural spine

**Decision:** A single scenario runs through the entire book — a new developer
cloning a project and trying to get it running. Each part is a wall they hit in
sequence.

**Rationale:** This turns five isolated reference topics into one coherent experience.
It also gives the researcher and writer agents a consistent grounding situation to
write from, rather than inventing new scenarios per chapter.

**Alternatives rejected:** Per-chapter scenarios would be more varied but would
require each chapter to re-establish context. The single thread is simpler to write
and simpler to read.

**Consequences:** The scenario must be established clearly in the introduction and
maintained consistently across agents and runs. The program-director role is
responsible for keeping the thread coherent across the four-issue chain.

---

### 2026-03-16 — Recognition over recall as the reader goal

**Decision:** The book does not teach command memorization. It teaches readers to
recognize what they're looking at so they can direct their AI correctly.

**Rationale:** The reader's AI will run the commands. The reader needs to understand
enough to know when something is wrong, what to tell the AI, and what not to undo.
Memorizing `git rebase -i` is out of scope. Recognizing "detached HEAD" is in scope.

**Alternatives rejected:** A more hands-on, command-by-command approach would
produce a conventional tutorial, which already exists and is not the gap this book fills.

**Consequences:** Every chapter must be written from the "understand it, don't
memorize it" frame. The book-voice skill and env-explainer skill must reinforce this.
The editor-and-qa agent must flag any drift toward command memorization mode.

---

### 2026-03-16 — book-voice.md must be written fresh, not inherited from Books 1–2

**Decision:** The `skills/book-voice.md` from Books 1–2 is not reused. A new version is written for ai-env-book.

**Rationale:** The existing book-voice explicitly targets "a working developer who has shipped code — not a beginner." That reader doesn't exist in this book. Using the inherited skill would cause every writer run to produce prose that talks over the reader's head — the most damaging possible failure mode for a primer.

**Alternatives rejected:** Adapting the existing file in place would risk contaminating the Books 1–2 asset and still might not produce the right register shift.

**Consequences:** `skills/book-voice.md` in this repo is a standalone file. The first Symphony issue for any chapter must load this version, not the one from the parent repo.

---

### 2026-03-16 — scenario-thread.md required to prevent drift across runs

**Decision:** A dedicated skill file encodes the canonical scenario state and is loaded by every writer and reviewer run.

**Rationale:** Symphony runs have no shared memory. Without a canonical scenario file, 15 separate Codex runs will invent inconsistent versions of the same scenario — different project names, different error messages, different tool versions. The scenario thread is what makes the book coherent; if it drifts, the whole book breaks.

**Alternatives rejected:** Embedding the scenario in each issue description would require maintaining it in 60+ places. Putting it in AGENTS.md or context.md buries it where writer agents may not load it. A dedicated skill file is the right scope.

**Consequences:** `skills/scenario-thread.md` must be written and locked before any chapter is drafted. It is the first skill file that needs to exist.
