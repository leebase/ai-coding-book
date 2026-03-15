# ai-coding-book Session Context

> **Purpose**: Working memory for session continuity. Read this first, then `sprint-plan.md`.

---

## Snapshot

| Attribute | Value |
|-----------|-------|
| **Phase** | Phase 1 — Part 1 Writing |
| **Mode** | 2 (Collaborative) |
| **Last Updated** | 2026-03-14 |

### Sprint Status
| Sprint | Status | Completion |
|--------|--------|------------|
| Sprint 0 — Foundation | ✅ Complete | 100% |
| Sprint 1 — Chapter 1 | 🔄 Active | 0% |

---

## What's Happening Now

### Current Work Stream
Ready to begin writing Chapter 1: "Plan Before You Prompt."

One prerequisite decision needed before Sprint 1 can start: **What project does the reader build across Part 1?** This must be decided before the scenario-designer can work.

### Recently Completed
- ✅ AgentFlow scaffold (AGENTS.md, CLAUDE.md)
- ✅ Writing pipeline: ebook-writer coordinator (9 stages)
- ✅ Agent roles: se-educator, scenario-designer, antigravity-expert, confused-beginner, continuity-editor, agentflow-architect
- ✅ Supporting skills: scenario-builder, antigravity-guide, book-voice
- ✅ Tutorial-writer sub-skills (18 skills, ported from init-agent)
- ✅ product-definition.md
- ✅ project-plan.md (14 chapters across 2 parts)
- ✅ sprint-plan.md

### In Progress
- ⏳ Deciding the Part 1 project thread

---

## Decisions Locked

| Decision | Rationale | Date |
|----------|-----------|------|
| Working title: "The AI-Era Developer" | Captures the audience and thesis | 2026-03-14 |
| 14 chapters: 7 Part 1 (SE principles) + 7 Part 2 (AgentFlow) | Maps one AgentFlow mechanism to each Part 1 pain point | 2026-03-14 |
| Free tier only for Antigravity scenarios | Accessible to all readers; rate limits reinforce planning discipline | 2026-03-14 |
| One project thread across all of Part 1 | Continuity, realism, avoids toy examples | 2026-03-14 |
| book-voice skill: peer-to-peer, direct, no hype | Defines prose register for all chapters | 2026-03-14 |

---

## Open Questions

1. What project does the reader build in Part 1? (Blocker for Sprint 1)
2. What is the book's final title?
3. Target publication format (markdown → what)?

---

## Next Actions Queue

| Rank | Action | Owner | Done When |
|------|--------|-------|-----------|
| 1 | Decide Part 1 project (type, domain, complexity) | Human | Decision locked above |
| 2 | Begin Sprint 1 using `skills/ebook-writer.md` | AI | Chapter 1 outline approved |
| 3 | Create `chapters/` directory structure | AI | Directories exist |

---

## Document Inventory

| File | Purpose | Status |
|------|---------|--------|
| `product-definition.md` | Book vision, audience, thesis, constraints | ✅ Done |
| `project-plan.md` | 14-chapter roadmap, phases, risks | ✅ Done |
| `sprint-plan.md` | Sprint 0 complete, Sprint 1 active | ✅ Done |
| `AGENTS.md` | AgentFlow rules, skill triggers | ✅ Done |
| `CLAUDE.md` | Claude Code orientation | ✅ Done |
| `skills/ebook-writer.md` | Chapter writing coordinator (9 stages) | ✅ Done |
| `skills/book-voice.md` | Book tone and style guide | ✅ Done |
| `skills/scenario-builder.md` | Scenario design principles | ✅ Done |
| `skills/antigravity-guide.md` | Antigravity UI writing guide | ✅ Done |
| `agents/` | 10 agent roles (6 book-specific) | ✅ Done |

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
