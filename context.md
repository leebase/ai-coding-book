# ai-coding-book Session Context

> **Purpose**: Working memory for session continuity. Read this first, then `sprint-plan.md`.
> **Note**: This file tracks Book 1 (The AI-Era Developer). Book 2 context is in `book2/context.md`.

---

## Snapshot

| Attribute | Value |
|-----------|-------|
| **Series** | Three books — see README |
| **Phase** | Book 1: Complete. Book 2: Complete. Book 3: First draft + publication complete. |
| **Mode** | 2 (Collaborative) |
| **Last Updated** | 2026-03-17 |

### Sprint Status
| Sprint | Status | Completion |
|--------|--------|------------|
| Sprint 0 — Foundation | ✅ Complete | 100% |
| Sprint 1 — Chapter 1 | ✅ Complete | 100% |
| Sprint 2 — Chapter 2 | ✅ Complete | 100% |
| Sprint 3 — Chapter 3 | ✅ Complete | 100% |
| Sprint 4 — Chapter 4 | ✅ Complete | 100% |
| Sprint 5 — Chapter 5 | ✅ Complete | 100% |
| Sprint 6 — Chapter 6 | ✅ Complete | 100% |
| Sprint 7 — Chapter 7 | ✅ Complete | 100% |
| Sprint 8 — Chapter 8 | ✅ Complete | 100% |
| Sprint 9 — Chapter 9 | ✅ Complete | 100% |
| Sprint 10 — Chapter 10 | ✅ Complete | 100% |
| Sprint 11 — Chapter 11 | ✅ Complete | 100% |
| Sprint 12 — Chapter 12 | ✅ Complete | 100% |
| Sprint 13 — Chapter 13 | ✅ Complete | 100% |
| Sprint 14 — Chapter 14 | ✅ Complete | 100% |

---

## What's Happening Now

### Series Status
Both books are complete and published to main.

### Book 1 — The AI-Era Developer (complete)
- ✅ All 16 chapters (14 + Introduction + Conclusion)
- ✅ Project thread: task manager CLI built across Part 1
- ✅ AgentFlow scaffold, writing pipeline, agent roles, skills
- ✅ Continuity pass, copyedit
- ✅ Published: EPUB, DOCX, PDF in `chapters/`

### Book 2 — Coding with Agent Teams (complete)
- ✅ All 13 files (Introduction, Ch 1–11, Conclusion)
- ✅ Content pipeline (Part 1) + Coding pipeline (Part 2)
- ✅ Continuity pass, copyedit, harness inventory
- ✅ Published: EPUB, DOCX, PDF in `book2/`

### Book 3 — Your Dev Environment (first draft complete)
- ✅ All 17 chapters written (~25,000 words) using Claude Code subagents
- ✅ Published: EPUB (9.1MB), DOCX (72KB), PDF (222KB) in `ai-env-book/`
- ⏳ Thin chapters to expand: ch-04, ch-06, ch-14, conclusion
- ⏳ Continuity pass, copyedit, rebuild formats

### Next Up
See `ai-env-book/context.md` for Book 3 editing status and next actions.

---

## Decisions Locked

| Decision | Rationale | Date |
|----------|-----------|------|
| Working title: "The AI-Era Developer" | Captures the audience and thesis | 2026-03-14 |
| 14 chapters: 7 Part 1 (SE principles) + 7 Part 2 (AgentFlow) | Maps one AgentFlow mechanism to each Part 1 pain point | 2026-03-14 |
| Free tier only for Antigravity scenarios | Accessible to all readers; rate limits reinforce planning discipline | 2026-03-14 |
| One project thread across all of Part 1 (task manager CLI) | Continuity, realism, avoids toy examples | 2026-03-14 |
| book-voice skill: peer-to-peer, direct, no hype | Defines prose register for all chapters | 2026-03-14 |

---

## Open Questions

1. Tool-specific spin-offs for Book 2 (Claude Code, Cursor editions)
2. Distribution / reader feedback channel
3. Book 4 topic and scope

---

## Next Actions Queue

| Rank | Action | Owner | Done When |
|------|--------|-------|-----------|
| 1 | Book 3 editing passes (expand thin chapters, continuity, copyedit) | AI | All chapters ≥1,500w, drift resolved |
| 2 | Book 2 spin-off: Claude Code edition | AI | Harness swaps applied from `book2/harness-inventory.md` |

---

## Working Conventions

### Start of session
1. Read `AGENTS.md`
2. Read this file
3. Read `sprint-plan.md`
4. Load `skills/ebook-writer.md` when writing a chapter

### End of session
1. Update "Recently Completed" and "In Progress"
2. Update sprint-plan.md task statuses
3. Update "Next Actions Queue"
4. Update "Last Updated" timestamp
