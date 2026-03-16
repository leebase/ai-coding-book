# Project Plan: Code with Agent Teams

> **Strategic roadmap.** For tactical execution, see `sprint-plan.md`.

---

## Phases

### Phase 0 — Foundation (ACTIVE)
- Book 2 scaffold: product-definition, project-plan, sprint-plan, context
- Adapt existing shared skills (ebook-writer, book-voice) for Book 2 context
- Define Part 1 project thread in detail (content pipeline spec)
- Define Part 2 project thread in detail (feature sprint pipeline spec)

### Phase 1 — Part 1: Build a Content Team

Six chapters. One project thread: a newsletter article pipeline. The reader builds it component by component, runs it at the end of Part 1, and compares the output to Chapter 1's single-prompt attempt.

| Chapter | Focus | Skill/Role Introduced | Status |
|---------|-------|----------------------|--------|
| 1 | Run the prompt | None — single Antigravity prompt | ⬜ Not started |
| 2 | The grounding problem | Researcher role + grounding skill | ⬜ Not started |
| 3 | The reader problem | Adversarial-reader role | ⬜ Not started |
| 4 | Voice and sequence | Voice skill + pipeline coordinator | ⬜ Not started |
| 5 | Run the pipeline | Full pipeline; Ch 1 comparison | ⬜ Not started |
| 6 | What you cannot trust | Honest ceiling; external orchestration named | ⬜ Not started |

**Phase 1 milestone:** Content pipeline complete and runnable. Chapter 1 vs Chapter 5 comparison works. Chapter 6 ceiling statement accurate and fair.

### Phase 2 — Part 2: Code with Agent Teams

Five chapters. One project thread: a feature sprint pipeline. Same coordination pattern applied to software development. Each chapter maps to its Part 1 counterpart.

| Chapter | Focus | Maps to Part 1 | Status |
|---------|-------|---------------|--------|
| 7 | Translating the pattern | Ch 2 — roles, different domain | ⬜ Not started |
| 8 | The coding team | Ch 3 — adversarial roles for code | ⬜ Not started |
| 9 | The feature skill | Ch 4 — coordinator for development | ⬜ Not started |
| 10 | Running a sprint | Ch 5 — full pipeline run | ⬜ Not started |
| 11 | Your coding team at work | Ch 6 — synthesis; recursive reveal | ⬜ Not started |

**Phase 2 milestone:** Feature sprint pipeline complete and runnable. Part 1 → Part 2 pattern transfer is visible and explicit. Chapter 11 closing reveal works.

### Phase 3 — Polish & Publication Prep
- Introduction and conclusion
- Continuity pass across all 11 chapters
- Copyedit
- Format for publication
- Spin-off preparation: identify all harness sections for Antigravity; document swap points for future tool editions

---

## Project Threads

### Part 1: The Content Pipeline

The reader builds a pipeline that takes a topic brief and produces a newsletter article. Built incrementally — each chapter adds one component. Runnable at the end of Chapter 5.

**Pipeline structure:**
```
brief.md
  └─► Researcher ──► research-notes.md
                         └─► Writer ──► draft.md
                                           └─► Editor + Adversarial Reader ──► final.md
```

**Files the reader creates across Part 1:**
- `brief.md` — topic, audience, goal (Chapter 1, used throughout)
- `agents/researcher.md` — researcher role definition (Chapter 2)
- `skills/grounding.md` — research discipline (Chapter 2)
- `agents/adversarial-reader.md` — adversarial reader role (Chapter 3)
- `skills/voice.md` — voice and register constraint (Chapter 4)
- `skills/article-pipeline.md` — coordinator skill, all stages (Chapter 4)

**Chapter 1 artifact:** `article-v1.md` — the single-prompt output. Kept for comparison.

**Chapter 5 artifact:** `article-v2.md` — the pipeline output on the same topic. Placed beside `article-v1.md`.

### Part 2: The Feature Sprint Pipeline

The reader builds a pipeline that takes a feature requirement and produces a reviewed, tested implementation. Same structural pattern as Part 1.

**Pipeline structure:**
```
requirement.md
  └─► Planner ──► plan.md
                      └─► Implementer ──► code + tests
                                              └─► Reviewer ──► review-notes.md
                                                                   └─► Tester ──► test-report.md
```

**Files the reader creates across Part 2:**
- `agents/planner.md` — planner role (Chapter 7)
- `agents/implementer.md` — implementer role (Chapter 7)
- `agents/reviewer.md` — reviewer role (Chapter 8)
- `agents/tester.md` — tester role (Chapter 8)
- `skills/feature-sprint.md` — coordinator skill (Chapter 9)

---

## The Comparison Exercise

Chapter 1: Reader prompts Antigravity with one request on a chosen topic. Saves output as `article-v1.md`. Does not evaluate it yet — just notes first impressions.

Chapter 5: Reader runs `article-pipeline.md` on the same topic. Saves output as `article-v2.md`. Compares both side by side using a specific checklist:
- Voice: consistent register throughout?
- Examples: specific and grounded, or generic and plausible-sounding?
- Misconceptions: does the article address a reader's wrong assumption, or just explain the topic?
- Failure path: does the article include what goes wrong, or only what goes right?
- Structure: does it build an experience, or list points?

The checklist maps each criterion back to the skill that produces it.

---

## Skill and Role Inventory

Skills and roles the reader builds during Part 1 and Part 2. These live in the reader's project directory, not in the book repo.

| Artifact | Type | Part | Chapter |
|----------|------|------|---------|
| `agents/researcher.md` | Role | 1 | 2 |
| `skills/grounding.md` | Skill | 1 | 2 |
| `agents/adversarial-reader.md` | Role | 1 | 3 |
| `skills/voice.md` | Skill | 1 | 4 |
| `skills/article-pipeline.md` | Coordinator skill | 1 | 4 |
| `agents/planner.md` | Role | 2 | 7 |
| `agents/implementer.md` | Role | 2 | 7 |
| `agents/reviewer.md` | Role | 2 | 8 |
| `agents/tester.md` | Role | 2 | 8 |
| `skills/feature-sprint.md` | Coordinator skill | 2 | 9 |

---

## Content Directory

```
book-2/
└── chapters/
    ├── part-1/
    │   ├── ch-01-run-the-prompt.md
    │   ├── ch-02-the-grounding-problem.md
    │   ├── ch-03-the-reader-problem.md
    │   ├── ch-04-voice-and-sequence.md
    │   ├── ch-05-run-the-pipeline.md
    │   └── ch-06-what-you-cannot-trust.md
    └── part-2/
        ├── ch-07-translating-the-pattern.md
        ├── ch-08-the-coding-team.md
        ├── ch-09-the-feature-skill.md
        ├── ch-10-running-a-sprint.md
        └── ch-11-your-coding-team-at-work.md
```

---

## Shared Infrastructure

Book 2 uses the same shared skills and agents as Book 1. No duplication.

| Resource | Location | Used by |
|----------|----------|---------|
| `skills/ebook-writer.md` | `/skills/` | Both books — chapter writing pipeline |
| `skills/book-voice.md` | `/skills/` | Both books — adapted voice for Book 2 audience |
| `skills/scenario-builder.md` | `/skills/` | Both books — scenario design |
| `agents/` | `/agents/` | Both books — all roles available |
| `AGENTS.md` | `/` | Both books |

Book 2 voice differs from Book 1 voice. A `book-2/skills/book-2-voice.md` override will be created at sprint start to capture the differences without modifying the shared file.

---

## Sprint Rhythm

Same as Book 1: one chapter per sprint, nine-stage ebook-writer pipeline, human gate after outline, commit on completion.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Part 1 pipeline too simple to demonstrate value | Comparison exercise makes the difference concrete — choose a topic rich enough that quality differences show |
| Part 2 feels like repetition of Part 1 | Explicit Part 1 mapping in each chapter; new failure modes unique to code (tests, merge conflicts, scope drift) |
| Chapter 6 honest ceiling discourages the reader | Frame as empowerment: you know what it can do, you know its limits, you know the next level — that's a complete picture |
| Harness sections embed too deeply in concept prose | Review every Antigravity reference before committing — if it can't be moved to a callout, restructure the paragraph |
| Spin-off confusion: readers pick up a tool-specific spin-off expecting the full book | Each spin-off edition notes clearly what it contains and what the canonical version is |
