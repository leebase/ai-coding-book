# ai-coding-book Session Context

> **Purpose**: Working memory for session continuity. Read this first, then `sprint-plan.md`.
> **Note**: This file tracks the series roadmap centered on Book 1. Book 2 context is in `book2/context.md`. The standalone environment primer has its own context in `ai-env-book/context.md`.

---

## Snapshot

| Attribute | Value |
|-----------|-------|
| **Series** | Main arc: 3 books. Standalone environment primer tracked separately. |
| **Phase** | Book 1: Complete. Book 2: Complete. Standalone environment primer: Complete and rebuilt from final revised sources. Main-arc Book 3: Planned. |
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
Book 1 and Book 2 are complete and published. The standalone environment primer is also complete and rebuilt from its revised source set. The main-arc Book 3 is still ahead of us.

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
- ✅ Post-publication review fixes applied and outputs rebuilt in `book2/`

### Standalone Primer — Your Dev Environment (complete)
- ✅ All 17 chapters written (~25,000 words) using Claude Code subagents
- ✅ Final revision complete: thin chapters expanded, continuity and copyedit passes applied
- ✅ Rebuilt: EPUB (8.9MB), DOCX (8.9MB), PDF (10.0MB) in `ai-env-book/`
- ✅ Structural publication QA complete, including EPUB TOC verification

### Planned Book 3 — Independent and Autonomous Agents
- ⏳ Intentionally deferred until more firsthand experience is gathered
- ⏳ Scope, structure, and thesis not yet locked

### Next Up
See `ai-env-book/context.md` for the standalone primer finish state and optional post-release follow-up.

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
3. Main-arc Book 3 topic, structure, and scope

---

## Next Actions Queue

| Rank | Action | Owner | Done When |
|------|--------|-------|-----------|
| 1 | Book 2 spin-off: Claude Code edition | AI | Harness swaps applied from `book2/harness-inventory.md` |
| 2 | Explore thesis and boundaries for main-arc Book 3 on independent/autonomous agents | Lee + AI | Enough real-world lessons collected to lock scope |
| 3 | Optional environment-book visual proof pass before external upload | Lee + AI | Outputs spot-checked in reader apps if needed |

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
