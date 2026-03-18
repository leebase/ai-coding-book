# Code with Agent Teams — Session Context

> **Purpose**: Working memory for session continuity. Read this first, then `sprint-plan.md`.

---

## Snapshot

| Attribute | Value |
|-----------|-------|
| **Phase** | Post-publication review and revision |
| **Mode** | 2 (Collaborative) |
| **Last Updated** | 2026-03-18 |

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

---

## What's Happening Now

### Current Work Stream
Book 2 is published and rebuilt from the latest revised manuscript. Human EPUB review surfaced three follow-up items; the EPUB readability problem has now been addressed twice: first with stronger CSS wrapping rules, then with manual hard-wrapping of the worst long-line code examples in the manuscript itself. Simpler reader-facing wording than "confabulation" is also done. A later Claude review added a second round of high-signal fixes: clearer gate-confirmation steps, explicit directory creation, stronger Part 2 Watch For scaffolding, and a cleaner explanation of parallel stages in Chapter 10. The publication outputs have now been regenerated from that revised source set. One editorial pass remains: trimming repetitive Antigravity callouts.

### Recently Completed
- ✅ All 11 chapters (Sprints 1–11)
- ✅ Introduction and conclusion
- ✅ Chapter 6 updated with current orchestration frameworks (Symphony, Agents SDK, Microsoft Agent Framework)
- ✅ `book-2/skills/book-2-voice.md`
- ✅ Phase 3 complete: continuity pass (5 issues fixed), copyedit (voice + callout consistency), harness inventory, combined publication file
- ✅ Agent vs skill distinction added to Ch 4 ("Two Kinds of Files" section)
- ✅ Reader-facing "confabulation" wording replaced with plainer language
- ✅ Long-line EPUB code examples manually hard-wrapped in source and EPUB rebuilt
- ✅ High-signal Claude review fixes applied to execution flow and harness separation in Ch 1, 2, 4, 5, and 7-10
- ✅ EPUB, DOCX, and PDF rebuilt from the revised Book 2 manuscript
- ✅ DOCX builder updated to write correct title/author metadata

### In Progress
- Human-review follow-up pass for Antigravity callout trimming
- Optional follow-up on lower-priority Claude review notes (for example, conclusion tightening and future-framework phrasing)

---

## Decisions Locked

| Decision | Rationale | Date |
|----------|-----------|------|
| Working title: "Code with Agent Teams" | Positions the methodology (coding with teams) and the domain (coding) | 2026-03-15 |
| Chapter 1 comparison topic: "How to write documentation your future self will actually use" | Universal developer pain; one-prompt output is generic and exhaustive; pipeline output is specific and grounded; failure path is clear | 2026-03-15 |
| Standalone — does not require Book 1 | Broader audience; AgentFlow patterns present but not named | 2026-03-15 |
| Content pipeline as Part 1 project thread | Accessible; no dev environment friction; teaches coordination patterns without language/framework distractions | 2026-03-15 |
| Feature sprint pipeline as Part 2 project thread | Applies same pattern to coding; maps 1:1 to Part 1 structure | 2026-03-15 |
| 11 chapters (6 Part 1, 5 Part 2) | Scope appropriate to subject; Part 1 needs more room to build the foundation | 2026-03-15 |
| Chapter 1 vs Chapter 5 comparison exercise | Argument by demonstration; reader observes the difference rather than being told | 2026-03-15 |
| Chapter 6 honest ceiling — external orchestration named but not taught | Intellectual honesty; sets up next book/next part without overselling | 2026-03-15 |
| Two-layer harness separation (concept + Antigravity callouts) | Enables spin-off editions; Antigravity steps in `> **Antigravity:**` callouts only | 2026-03-15 |
| Antigravity free tier only | Accessible to all readers; constraint reinforces planning discipline | 2026-03-15 |
| Part 2 feature: `git-summary` CLI tool | Takes a repo path, outputs human-readable summary of recent changes; clear requirements, no external dependencies, demonstrates all five coding roles | 2026-03-15 |
| Shared infrastructure (skills/, agents/) with Book 1 | No duplication; Book 2 voice override in `book-2/skills/` | 2026-03-15 |

---

## Open Questions

1. How aggressive should the Book 2 callout-trimming pass be?
2. Do we want to apply the optional Claude review notes in the conclusion, or leave the current ending alone?

---

## Next Actions Queue

| Rank | Action | Owner | Done When |
|------|--------|-------|-----------|
| 1 | Trim repetitive `> **Antigravity:**` callouts | Lee + AI | Callouts carry only tool-specific UI/action detail |
| 2 | Spot-check rebuilt Book 2 outputs on-device | Lee | Human review confirms the latest EPUB/PDF/DOCX read cleanly in the target apps |
| 3 | Capture any additional Book 2 reader errata | Lee + AI | Feedback logged and categorized |

---

## Document Inventory

| File | Purpose | Status |
|------|---------|--------|
| `book-2/product-definition.md` | Book vision, audience, thesis, constraints | ✅ Done |
| `book-2/project-plan.md` | 11-chapter roadmap, project threads, risks | ✅ Done |
| `book-2/sprint-plan.md` | Sprint 0 active, Sprints 1–11 defined | ✅ Done |
| `book-2/context.md` | This file — session state | ✅ Done |
| `book-2/skills/book-2-voice.md` | Voice override for Book 2 | ✅ Done |

---

## Relationship to Book 1

Book 1 (`The AI-Era Developer`) is complete at 14 chapters and in Phase 3 (polish). Book 2 is independent — separate directory, separate planning docs, shared infrastructure.

Book 1 files are untouched. The two books share `/skills/`, `/agents/`, `AGENTS.md`, and `CLAUDE.md`. Book 2 adds overrides in `book-2/skills/` only when Book 1 defaults don't apply.

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
