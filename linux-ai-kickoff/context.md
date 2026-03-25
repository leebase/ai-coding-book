# Teach Yourself Anything - Session Context

> Working memory for session continuity. Read this first, then `sprint-plan.md`.

---

## Snapshot

| Attribute | Value |
|-----------|-------|
| **Title** | Teach Yourself Anything |
| **Phase** | Review and Packaging |
| **Mode** | 2 (Collaborative) |
| **Last Updated** | 2026-03-25 |

### Sprint Status

| Sprint | Status | Completion |
|--------|--------|------------|
| Sprint 0 - Foundation | Complete | 100% |
| Sprint 1 - Chapter architecture | Complete | 100% |
| Sprint 2 - Skill stack and writing workflow | Complete | 100% |
| Sprint 3 - Introduction | Complete | 100% |
| Sprint 4 - Part 1 Chapter 1 | Complete | 100% |
| Sprint 5 - Part 1 Chapter 2 | Complete | 100% |
| Sprint 6 - Part 1 Chapter 3 | Complete | 100% |
| Sprint 7 - Part 2 Chapter 1 | Complete | 100% |
| Sprint 8 - Part 2 Chapter 2 | Complete | 100% |
| Sprint 9 - Part 2 Chapter 3 | Complete | 100% |
| Sprint 10 - Part 2 Chapter 4 | Complete | 100% |
| Sprint 11 - Part 3 Chapter 1 | Complete | 100% |
| Sprint 12 - Part 3 Chapter 2 | Complete | 100% |
| Sprint 13 - Part 3 Chapter 3 | Complete | 100% |
| Sprint 14 - Part 3 Chapter 4 | Complete | 100% |
| Sprint 15 - Part 4 Chapter 1 | Complete | 100% |
| Sprint 16 - Part 4 Chapter 2 | Complete | 100% |
| Sprint 17 - Part 4 Chapter 3 | Complete | 100% |
| Sprint 18 - Part 4 Chapter 4 | Complete | 100% |
| Sprint 19 - Part 5 Chapter 1 | Complete | 100% |
| Sprint 20 - Part 5 Chapter 2 | Complete | 100% |
| Sprint 21 - Part 5 Chapter 3 | Complete | 100% |
| Sprint 22 - Conclusion | Complete | 100% |
| Sprint 23 - Full continuity pass | Complete | 100% |
| Sprint 24 - Technical accuracy and source pass | Complete | 100% |
| Sprint 25 - Copyedit and voice pass | Complete | 100% |
| Post-production review follow-up | Complete | 100% |

---

## What's Happening Now

This book has moved well past concept setup and into sustained drafting. Part 1
and Part 2 are complete, Part 3 is complete, Part 4 is complete, and Part 5 is
now complete, and the conclusion is drafted and reviewed. The manuscript now
has a full closing artifact chain in the same workspace: `direction.md`,
`curriculum.md`, `next-three-moves.md`, and a conclusion that points outward
from proof instead of promise.

All planned production sprints in `sprint-plan.md` are now complete on the
working branch. The manuscript has been drafted, continuity-reviewed,
source-checked against the live Omarchy manual, and copyedited for voice.

The book now also has a local export/build pipeline inside `linux-ai-kickoff/`.
`teach-yourself-anything.md`, `teach-yourself-anything.epub`,
`teach-yourself-anything.docx`, and `teach-yourself-anything.pdf` are built in
place, with `TeachYourselfAnything.png` embedded as the cover in all three
publication formats. The PDF path uses a PDF-specific raw LaTeX cover page so
the cover leads the document correctly.

The first external review has now been applied as a targeted polish pass. Part
2 now explains `Super` once and trusts the reader after that, Chapter 4 now
points non-Omarchy readers to a new appendix for machine translation, Chapter
12 explicitly tells the reader to do the mission instead of just finishing the
book if they have to choose, Chapter 15 has more hands-on real-life examples,
and the conclusion now names the Apple IIe origin story directly.

The current focus is human review of both the manuscript and the exported
artifacts and, after approval, merge.

---

## Decisions Locked

| Decision | Rationale | Date |
|----------|-----------|------|
| Title: `Teach Yourself Anything` | Stronger promise than `linux-ai-kickoff` | 2026-03-22 |
| Linux and AI are tools, not the true subject | Keeps the book centered on agency | 2026-03-22 |
| Reader priorities are inspired, motivated, empowered | Editorial north star | 2026-03-22 |
| Omarchy manual is the primary technical companion source | RTFM is part of the method | 2026-03-22 |
| AI is framed as tutor and leverage, not destiny | Avoids hype and passivity | 2026-03-22 |
| GenAI is taught as horse-not-car | Explains why guidance and supervision matter | 2026-03-22 |
| Working manuscript shape: 19 files | Enough room for transformation without turning into a reference tome | 2026-03-22 |
| Part 4 project thread: personal launchpad | Keeps the practical work real, small, and broadly accessible | 2026-03-22 |
| Local export pipeline lives in `linux-ai-kickoff/` | Keeps this book's build path self-contained and dependency-light | 2026-03-25 |
| External review follow-up should be targeted, not a rewrite | Preserve the book's strengths while taking obvious polish wins | 2026-03-25 |

---

## Open Questions

1. What is the final subtitle?
2. Do any of the working chapter titles need stronger wording before publication?
3. Do any of the Part 3 chapter titles need stronger wording before the part is
   refined as a whole?
4. Do any final chapter titles or the subtitle want one last tightening before
   merge?

---

## Next Actions Queue

| Rank | Action | Owner | Done When |
|------|--------|-------|-----------|
| 1 | Human review of the exported EPUB, DOCX, and PDF | Lee | Artifacts feel publication-ready |
| 2 | Decide whether the new appendix and conclusion note are exactly right | Lee + AI | Cross-platform and autobiographical framing feel final |
| 3 | Human review of the working branch | Lee | Approval path is clear before merge |
| 4 | Revisit the subtitle against the finished manuscript | Lee + AI | Subtitle matches the actual tone of the book |
| 5 | Merge `codex/teach-yourself-anything` after approval | Lee + AI | Finished manuscript lands on the main line cleanly |

---

## Local Inventory

| File | Purpose | Status |
|------|---------|--------|
| `AGENTS.md` | Local operating guide | Done |
| `skills/` | Local chapter-writing skill stack | Done |
| `product-definition.md` | Book vision and thesis | Done |
| `project-plan.md` | Strategic roadmap | Done |
| `architecture.md` | Chapter map and structural decisions | Done |
| `chapters/` | Live manuscript source | In progress |
| `build-*.py` | Local publication/export scripts | Done |
| `teach-yourself-anything.md` | Assembled manuscript | Done |
| `teach-yourself-anything.epub/.docx/.pdf` | Built export artifacts | Done |
| `chapters/appendices/` | Cross-platform support appendix | Done |
| `context.md` | This file | Done |
| `sprint-plan.md` | Tactical execution | Done |
| `result-review.md` | Running log of completed setup work | Done |
| `lee-voice.md` | Voice and register guide | Done |
| `agents/` | Custom role files | Done |

---

## Working Convention

### Start of session

1. Read `AGENTS.md`
2. Read this file
3. Read `result-review.md`
4. Read `sprint-plan.md`

### End of session

1. Update `context.md`
2. Update `result-review.md`
3. Update `sprint-plan.md`
