# ai-env-book Project Plan

> **Strategic roadmap.** For task-level status, see Linear. For the staging runway, see `sprint-plan.md`.

---

## Mission

Teach new developers just enough about git, GitHub, Python environments, Node/npm, and Warp.dev that they can understand what their AI coding tool is doing — and direct it when something breaks.

---

## Phases

### Phase 0 — Scaffold (current)

**Goal:** Project infrastructure ready to produce chapters via Symphony + Linear.

| Artifact | Status |
|----------|--------|
| `product-description.md` | ✅ Done |
| `architecture.md` | ✅ Done |
| `project-plan.md` | ✅ Done |
| `sprint-plan.md` | ✅ Done |
| `AGENTS.md` | ✅ Done |
| `context.md` | ✅ Done |
| `BACKLOG.md` | ✅ Done |
| `WORKFLOW.md` | ✅ Done — needs Linear project_slug filled in |
| `agents/program-director.md` | ✅ Done |
| `agents/researcher.md` | ✅ Done |
| `agents/writer.md` | ✅ Done |
| `agents/editor-and-qa.md` | ✅ Done |
| `skills/book-voice.md` | ✅ Done |
| `skills/env-explainer.md` | ✅ Done |
| `skills/new-dev-validator.md` | ✅ Done |
| `skills/scenario-thread.md` | ⬜ Placeholder — AENV-001 must run via Symphony |
| `skills/warp-expert.md` | ⬜ On hold — requires Lee input or web research pass |
| `scripts/bootstrap-workspace.sh` | ✅ Done |
| `scripts/enforce-after-run.sh` | ✅ Done |
| `scripts/start-symphony.sh` | ✅ Done |

**Done when:** Symphony can pick up a Linear issue, run the writer agent against a chapter brief, and land a draft in the live repo.

---

### Phase 1 — Introduction and Scenario Establishment

**Goal:** Introduction chapter written and the running scenario locked. This is the foundation every subsequent chapter builds on.

| Artifact | Status |
|----------|--------|
| `chapters/briefs/introduction-brief.md` | ⬜ |
| `chapters/drafts/introduction.md` | ⬜ |
| `chapters/reviews/introduction-review.md` | ⬜ |
| `chapters/introduction.md` | ⬜ |

**Done when:** Introduction is final in live repo. Scenario is established and encoded in `skills/scenario-thread.md`.

---

### Phase 2 — Part 1: Git and GitHub (5 chapters)

**Goal:** All five git/GitHub chapters written and finalized.

| Chapter | Status |
|---------|--------|
| ch-01 — What Git Actually Is | ⬜ |
| ch-02 — GitHub: Where Your Code Lives | ⬜ |
| ch-03 — Getting Your Computer Authorized | ⬜ |
| ch-04 — Branches and Worktrees | ⬜ |
| ch-05 — When Git Goes Wrong | ⬜ |

Each chapter = 4 Linear issues (brief → draft → review → final). 20 issues total.

**Done when:** All 5 chapters finalized in `chapters/`.

---

### Phase 3 — Part 2: Python Environments (3 chapters)

**Goal:** All three Python environment chapters written and finalized.

| Chapter | Status |
|---------|--------|
| ch-06 — Why Python Has an Environment Problem | ⬜ |
| ch-07 — venv, conda, uv — Which One and Why | ⬜ |
| ch-08 — Reading requirements.txt and pyproject.toml | ⬜ |

12 issues total.

**Done when:** All 3 chapters finalized in `chapters/`.

---

### Phase 4 — Part 3: Node and npm (3 chapters)

**Goal:** All three Node/npm chapters written and finalized.

| Chapter | Status |
|---------|--------|
| ch-09 — What Node Is (and Why It's on Your Machine) | ⬜ |
| ch-10 — nvm and Node Versions | ⬜ |
| ch-11 — package.json and node_modules | ⬜ |

12 issues total.

**Done when:** All 3 chapters finalized in `chapters/`.

---

### Phase 5 — Part 4: Warp (4 chapters)

**Goal:** All four Warp chapters written and finalized. Requires `skills/warp-expert.md` to be complete before this phase begins.

| Chapter | Status |
|---------|--------|
| ch-12 — The Gap Warp Fills | ⬜ |
| ch-13 — Warp Basics | ⬜ |
| ch-14 — Warp Workflows for Developers | ⬜ |
| ch-15 — Dividing Responsibilities | ⬜ |

16 issues total.

**Done when:** All 4 chapters finalized in `chapters/`. `skills/warp-expert.md` must be locked before Phase 5 begins.

---

### Phase 6 — Conclusion

**Goal:** Conclusion chapter written and finalized.

| Artifact | Status |
|----------|--------|
| `chapters/conclusion.md` | ⬜ |

4 issues total.

**Done when:** Conclusion finalized in `chapters/`.

---

### Phase 7 — Continuity Pass

**Goal:** Read all chapters as one continuous work. Fix scenario drift, voice inconsistencies, cross-chapter references.

| Task | Status |
|------|--------|
| Read all chapters sequentially | ⬜ |
| Fix scenario thread drift | ⬜ |
| Verify voice consistency | ⬜ |
| Check "recognition over recall" frame held throughout | ⬜ |

**Done when:** All chapters read as coherent single work with no drift.

---

### Phase 8 — Copyedit

**Goal:** Line-level polish. Tighten prose, remove repetition, verify callout boxes.

**Done when:** Final read-through complete, all chapters at target word count.

---

### Phase 9 — Publication

**Goal:** Final output format decided and generated.

**Done when:** Distributable artifact exists (EPUB, PDF, or both).

---

## Total Issue Estimate

| Phase | Issues |
|-------|--------|
| Phase 0 — Scaffold | ~5 (infrastructure, skill files) |
| Phase 1 — Introduction | 4 |
| Phase 2 — Part 1 (5 chapters) | 20 |
| Phase 3 — Part 2 (3 chapters) | 12 |
| Phase 4 — Part 3 (3 chapters) | 12 |
| Phase 5 — Part 4 (4 chapters) | 16 |
| Phase 6 — Conclusion | 4 |
| Phase 7–9 — Polish + Publication | ~8 |
| **Total** | **~81** |

---

## Constraints

- `skills/scenario-thread.md` must be locked before Phase 1 begins
- `skills/warp-expert.md` must be locked before Phase 5 begins
- Phase 5 (Warp) depends on Lee's direct input or a web research pass — do not draft Warp chapters from general knowledge
- Parallel Symphony runs are not safe; all phases are strictly serial
