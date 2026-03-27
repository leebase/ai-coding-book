# Skill: Thought Leadership Book

This skill coordinates planning and drafting for a thesis-driven nonfiction or
business book.

Do not jump into prose because the idea feels exciting. Lock the argument first.

## The Team

Each stage adopts a specific role. Load the agent file to take on that role's
constraints.

| Role | Agent File | Responsibility |
|------|------------|----------------|
| thesis-architect | `agents/thesis-architect.md` | Sharpens the central claim and reader shift |
| research-synthesizer | `agents/research-synthesizer.md` | Grounds the argument in credible sources and gaps |
| story-miner | `agents/story-miner.md` | Extracts lived stories into reusable proof and application |
| framework-designer | `agents/thesis-architect.md` | Creates named models, diagnostics, and decision tools |
| positioning-editor | `agents/positioning-editor.md` | Clarifies title, audience, promise, and differentiation |
| argument-writer | `agents/argument-writer.md` | Drafts the prose once the thinking is locked |

## Stage 1: Frame the Thesis

**Role**: thesis-architect
**Load**: `agents/thesis-architect.md`
**Produce**: Thesis Brief

- What is the claim?
- What tempting but wrong move is the reader making?
- What is the central tension?
- What shift should the reader make?

## Stage 2: Synthesize Research

**Role**: research-synthesizer
**Load**: `agents/research-synthesizer.md`
**Produce**: Research Support Memo

- What is well supported?
- What is only partially supported?
- What is original here?
- What claims still need stronger evidence or interviews?

## Stage 3: Mine the Stories

**Role**: story-miner
**Load**: `agents/story-miner.md`
**Produce**: Story Bank

- Which lived stories prove the thesis?
- Which stories humanize it?
- Which are vivid but non-essential?
- What is transferable to the reader?

## Stage 4: Design the Frameworks

**Role**: thesis-architect
**Load**: `agents/thesis-architect.md`
**Produce**: Framework Notes

- What named concepts or diagrams belong in this section?
- What decisions do they help the reader make?
- Are they clear enough to survive outside the manuscript?

## Stage 5: Position the Chapter or Book

**Role**: positioning-editor
**Load**: `agents/positioning-editor.md`
**Produce**: Positioning Notes

- Who is this for?
- Why now?
- What promise is being made?
- What makes it different from adjacent books?

## Gate — Human Approval Required

Stop here for major book or chapter planning work.

Present the Thesis Brief, Research Support Memo, Story Bank, Framework Notes,
and Positioning Notes. Revise the thinking before drafting prose.

## Stage 6: Draft the Argument

**Role**: argument-writer
**Load**: `agents/argument-writer.md`
**Produce**: Draft

Write only after the argument is sharp enough to survive summary.

## Stage 7: Refine

**Role**: argument-writer
**Load**: `agents/argument-writer.md`
**Produce**: Final Draft

Tighten language, remove drift, and make sure every section still serves the
claim rather than the note pile.
