# Sprint Plan: Code with Agent Teams

> **Tactical execution.** For strategic roadmap, see `project-plan.md`.

---

## Sprint 0 — Foundation (COMPLETE ✅)

**Goal**: Book 2 scaffold complete; project threads defined; writing infrastructure ready.

| Task | Status |
|------|--------|
| `book-2/product-definition.md` | ✅ Done |
| `book-2/project-plan.md` | ✅ Done |
| `book-2/sprint-plan.md` | ✅ Done |
| `book-2/context.md` | ✅ Done |
| `book-2/skills/book-2-voice.md` — voice override for Book 2 audience | ✅ Done |
| Chapter 1 comparison topic locked: "How to write documentation your future self will actually use" | ✅ Done |

---

## Sprint 1 — Chapter 1: Run the Prompt (COMPLETE ✅)

**Goal**: Establish the problem through experience. Reader runs one prompt, saves output, notes first impressions. The output is adequate — that is the point.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-1/ch-01-run-the-prompt.md` | ✅ Done |

**Chapter must accomplish:**
- Reader runs a single Antigravity prompt to produce an article on a chosen topic
- Output is saved as `article-v1.md`
- Reader notes first impressions — not a full critique, just "what feels off?"
- Chapter closes without resolving the problem — the inadequacy is named, not fixed

---

## Sprint 2 — Chapter 2: The Grounding Problem (COMPLETE ✅)

**Goal**: Researcher role + grounding skill. Show what happens when research and writing blend. Show what separating them produces.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-1/ch-02-the-grounding-problem.md` | ✅ Done |

**Chapter must accomplish:**
- Reader builds `agents/researcher.md` — with explicit input, output, and scope
- Reader builds `skills/grounding.md` — forces commit to known facts before writing
- Reader runs researcher role on their topic; observes what it produces vs. what Ch 1 assumed
- The insight: the AI confabulates when it writes and researches simultaneously

---

## Sprint 3 — Chapter 3: The Reader Problem (COMPLETE ✅)

**Goal**: Adversarial reader role. The writer cannot be the reader — you need a role that doesn't have the writer's context.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-1/ch-03-the-reader-problem.md` | ✅ Done |

**Chapter must accomplish:**
- Reader builds `agents/adversarial-reader.md`
- Reader runs it against the Ch 2 draft; adversarial reader finds gaps the writer could not see
- The insight: clarity is invisible to the person with context; silent confusion is worse than visible confusion
- Connects to learner-confusion-attack pattern from Book 1's writing pipeline

---

## Sprint 4 — Chapter 4: Voice and Sequence (COMPLETE ✅)

**Goal**: Voice skill + pipeline coordinator. Define voice before writing. The coordinator enforces the sequence that prevents premature optimization.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-1/ch-04-voice-and-sequence.md` | ✅ Done |

**Chapter must accomplish:**
- Reader builds `skills/voice.md` — explicit register, tone constraints, what to avoid
- Reader builds `skills/article-pipeline.md` — coordinator that sequences all stages with their roles
- The insight: voice is a constraint defined before writing starts, not a style that emerges; order of stages matters as much as the stages
- Reader now has a complete pipeline — not yet run end-to-end

---

## Sprint 5 — Chapter 5: Run the Pipeline (COMPLETE ✅)

**Goal**: Run the completed pipeline on the Chapter 1 topic. Compare outputs. The difference is nameable.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-1/ch-05-run-the-pipeline.md` | ✅ Done |

**Chapter must accomplish:**
- Reader loads `article-pipeline.md`, runs it on the same topic as Chapter 1
- Output saved as `article-v2.md`
- Reader compares `article-v1.md` and `article-v2.md` using the five-point checklist
- Each checklist criterion maps back to the skill that produces it
- The comparison is the argument — book does not tell the reader the output is better; the reader observes it

---

## Sprint 6 — Chapter 6: What You Cannot Trust (COMPLETE ✅)

**Goal**: Honest ceiling. What the skill-based approach cannot guarantee. External orchestration named and pointed to as the next level.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-1/ch-06-what-you-cannot-trust.md` | ✅ Done |

**Chapter must accomplish:**
- Name the failure modes: stage collapse, role drift, output variance, context accumulation
- Explain why these happen (not bugs — properties of LLMs in long sessions)
- The gate as the primary quality instrument — and its cost (you must know what to look for)
- External orchestration: what it solves, why it's the next level, where to find it
- Closes Part 1: the reader has a working pipeline, an honest picture of its limits, and a path forward

---

## Sprint 7 — Chapter 7: Translating the Pattern (COMPLETE ✅)

**Goal**: Move to Part 2. Show how content pipeline roles translate to coding roles. What changes, what doesn't.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-2/ch-07-translating-the-pattern.md` | ✅ Done |

---

## Sprint 8 — Chapter 8: The Coding Team (COMPLETE ✅)

**Goal**: Define the coding roles. Planner, Implementer, Reviewer, Tester — each with explicit input, output, and scope.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-2/ch-08-the-coding-team.md` | ✅ Done |

---

## Sprint 9 — Chapter 9: The Feature Skill (COMPLETE ✅)

**Goal**: Build the feature sprint coordinator. A skill that sequences coding roles through a development workflow.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-2/ch-09-the-feature-skill.md` | ✅ Done |

---

## Sprint 10 — Chapter 10: Running a Sprint (COMPLETE ✅)

**Goal**: Run the feature skill in Antigravity Manager View. Parallel agents where scopes are clean. Merge discipline.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-2/ch-10-running-a-sprint.md` | ✅ Done |

---

## Sprint 11 — Chapter 11: Your Coding Team at Work (COMPLETE ✅)

**Goal**: Full sprint synthesis. Reader runs the complete feature pipeline. Closing reveal: this book was produced by the same system they just built.

| Task | Status |
|------|--------|
| All 9 ebook-writer stages | ✅ Done |
| Commit `chapters/part-2/ch-11-your-coding-team-at-work.md` | ✅ Done |

---

## Book Status: ALL 11 CHAPTERS COMPLETE ✅

**Part 1** (Chapters 1–6): Content pipeline — one-prompt baseline, researcher, adversarial reader, voice + coordinator, full run + comparison, honest ceiling
**Part 2** (Chapters 7–11): Coding team — pattern translation, five roles, feature skill, sprint run, synthesis + recursive reveal

**Phase 3 status:**
- Introduction | ✅ Done
- Conclusion | ✅ Done
- Agent vs skill distinction — added "Two Kinds of Files" section to Ch 4 | ✅ Done
- Continuity pass across all 13 documents | ✅ Done
- Copyedit | ✅ Done
- Publication format — `book-2/coding-with-agent-teams.md` | ✅ Done
- Spin-off preparation — `book-2/harness-inventory.md` | ✅ Done
