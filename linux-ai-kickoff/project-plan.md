# Project Plan: Teach Yourself Anything

> Strategic roadmap for the book. For current execution status, see
> `sprint-plan.md`.

---

## Mission

Build a book that helps a motivated young person become more inspired,
motivated, and empowered by learning how to use Linux, AI, manuals, and real
projects to teach themselves.

The real outcome is not Linux literacy. The real outcome is self-direction.

---

## Foundation Decisions

| Decision | Rationale | Status |
|----------|-----------|--------|
| Title: `Teach Yourself Anything` | Names the promise, not the setup | Locked |
| Linux and AI are tools, not the subject | Keeps the book centered on agency | Locked |
| Omarchy manual is the primary technical source | Supports the RTFM habit directly | Locked |
| AI is framed as tutor, coach, and force multiplier | Avoids the vending-machine model | Locked |
| Reader outcomes are inspired, motivated, empowered | Editorial north star for all decisions | Locked |

---

## Core Frameworks

### The Team-Captain Model

The reader learns to direct AI like a team:

1. Pick the right hero
2. Give them the backstory
3. Give them a mission
4. Stay in charge

### The Horse-Not-Car Model

AI is powerful and useful, but not deterministic in the way a machine like a
car is. The reader must learn guidance, supervision, and correction.

### Manual-First Learning

The reader uses official manuals and primary sources first, then uses AI to
interpret, clarify, and apply what they found.

---

## Planned Book Shape

See `architecture.md` for the concrete chapter map, mission ladder, and manual
coverage map.

### Part 1 - You're Not Stuck

Goal: Give the reader dignity, possibility, and a reason to believe they can
build a path.

### Part 2 - Meet Your Machine

Goal: Make the Omarchy machine legible and usable without turning this into a
system-administration manual.

### Part 3 - Meet Your Teacher

Goal: Teach the reader how to use AI effectively by directing it, correcting
it, and learning from it.

### Part 4 - Do Things That Matter

Goal: Turn confidence into momentum through practical missions and real output.

### Part 5 - Now You Choose

Goal: Help the reader choose a direction and keep going without the book.

### Working Manuscript Size

- 1 introduction
- 17 core chapters across five parts
- 1 conclusion

Total: **19 manuscript files**

---

## Phases

### Phase 0 - Foundation

- Create the local project document stack
- Lock the product definition and thesis language
- Create the custom agent roles
- Decide which reusable skills from `ai-env-book/` carry forward
- Define the chapter architecture for all five parts

**Done when:** The book has a stable planning spine and the writing workflow is
clear enough to begin chapter design.

### Phase 1 - Architecture and Chapter Map

- Decide chapter count and chapter-level outcomes
- Define the mission ladder across the book
- Identify the minimum Omarchy-manual sections each part depends on
- Choose the first concrete project thread for Part 4
 - Record the architecture in `architecture.md`

**Done when:** Every chapter has a one-sentence purpose, outcome, and place in
the reader journey.

### Phase 2 - Part 1 Drafting

- Write and refine all Part 1 chapters
- Protect the dignity and possibility framing
- Establish the core mental models early

**Done when:** The reader is oriented, hopeful, and ready to act.

### Phase 3 - Part 2 Drafting

- Write and refine all Part 2 chapters
- Ground Omarchy usage in the official manual
- Teach navigation, terminal use, and practical recovery habits

**Done when:** The reader can use the machine with basic confidence and knows
where to look when stuck.

### Phase 4 - Part 3 Drafting

- Write and refine all Part 3 chapters
- Teach AI as tutor, coach, and collaborator
- Introduce the Team-Captain and Horse-Not-Car models directly

**Done when:** The reader can get useful help from AI without surrendering
judgment.

### Phase 5 - Part 4 Drafting

- Write and refine all Part 4 chapters
- Build small, real, visible projects
- Use missions that create momentum and proof of capability

**Done when:** The reader has multiple completed wins and a stronger sense of
agency.

### Phase 6 - Part 5 Drafting

- Write and refine all Part 5 chapters
- Help the reader choose a direction
- Show how the same tools open multiple futures

**Done when:** The ending points outward, not just backward.

### Phase 7 - Continuity, Copyedit, and Publication

- Continuity pass across the full book
- Voice pass against `lee-voice.md`
- Accuracy pass against the Omarchy manual and any linked primary docs
- Copyedit and publication builds

**Done when:** The full manuscript is coherent, grounded, and publication-ready.

---

## Content Design Rules

Every chapter must:

- include a concrete mission
- produce a visible outcome
- teach one empowering habit, not just one topic
- show where to look next when the reader gets stuck
- avoid treating AI output as automatically correct

Every technical section must answer:

- What is the reader trying to do?
- What official source should they check?
- What is AI helping with here?
- What does success look like?

---

## Agent Stack

### Custom agents in this workspace

| Agent | Responsibility |
|-------|----------------|
| `pathfinder` | Protects the book's larger promise: agency, possibility, and direction |
| `confidence-auditor` | Checks whether the draft makes the reader feel capable rather than small |
| `manual-guide` | Ensures manuals and primary docs are used well and taught explicitly |
| `mission-designer` | Turns concepts into small missions with visible wins |

### Reused agents from the repo

| Agent | Source | Use |
|-------|--------|-----|
| `confused-beginner` | root `agents/` | Reader confusion attack |
| `continuity-editor` | root `agents/` | Track narrative and project continuity |
| `command-skeptic` | `ai-env-book/agents/` | Command and environment landmine review |
| `fresh-install` | `ai-env-book/agents/` | Beginner-friction review |

---

## Skill Stack

### Planned new skills

- `manual-first`
- `ai-as-tutor`
- `mission-ladder`
- `possibility-framing`
- `lee-voice` as an operational writing skill

### Likely reused skills

- `ai-env-book/skills/env-explainer.md`
- `ai-env-book/skills/new-dev-validator.md`
- `ai-env-book/skills/skill-command-safety.md`

New skills should be created only if they add real workflow value and not just
more vocabulary.

---

## Risks

| Risk | Mitigation |
|------|------------|
| The book collapses into a Linux how-to | Keep every chapter tied to agency and real-life direction |
| The book drifts into AI hype | Reassert that the future belongs to humans who use AI effectively |
| The reader feels judged or behind | Use the confidence-auditor role on major drafts |
| The technical material becomes second-hand or fuzzy | Ground Omarchy sections in the official manual |
| Motivation becomes abstract instead of practical | Require visible outcomes and short missions in every chapter |

---

## Source Anchors

- Omarchy manual: [The Omarchy Manual](https://learn.omacom.io/2/the-omarchy-manual)
- Local voice guide: `lee-voice.md`
- Local product definition: `product-definition.md`
- Local structure decisions: `architecture.md`
