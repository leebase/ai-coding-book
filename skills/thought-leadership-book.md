# Skill: Thought Leadership Book

This skill coordinates planning and drafting for a thesis-driven nonfiction or
business book.

This workflow is also referred to as **AuthorFlow**.

Do not jump into prose because the idea feels exciting. Lock the argument first.

Maintain an `author-flow.md` file in the active book directory so the method can
be studied and reused later.

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
| big-consulting-reviewer | `agents/big-consulting-reviewer.md` | Reviews for large-firm credibility and scale realism |
| mid-market-consulting-reviewer | `agents/mid-market-consulting-reviewer.md` | Reviews for mid-market practicality and economics |
| independent-consultant-reviewer | `agents/independent-consultant-reviewer.md` | Reviews for solo and small-shop relevance |

Every drafting stage should also load `skills/consulting-book-voice.md`.

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
The draft must sound human, reflective, and inviting rather than corporate or
slide-deck polished.

## Stage 7: Audience Review

**Roles**:
- big-consulting-reviewer
- mid-market-consulting-reviewer
- independent-consultant-reviewer

**Load**:
- `agents/big-consulting-reviewer.md`
- `agents/mid-market-consulting-reviewer.md`
- `agents/independent-consultant-reviewer.md`

**Produce**: Audience Review Notes

- What lands for Big Consulting?
- What lands for mid-market firms?
- What lands for the individual consultant?
- Where does the draft overfit one audience and lose the others?
- What scale assumptions need to be made explicit?

## Stage 8: Refine

**Role**: argument-writer
**Load**: `agents/argument-writer.md`
**Produce**: Final Draft

Tighten language, address audience-review findings, remove drift, and make sure
every section still serves the claim rather than the note pile.

Before marking prose done, run an explicit tone pass:

- remove consulting cliches
- replace abstract prestige language with observed language
- make sure the reader feels guided by a person rather than addressed by a firm
