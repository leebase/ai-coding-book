# business-growth-playbook Result Review

> **Running log of completed work.** Newest entries at the top.

---

## 2026-03-28 — Conclusion Drafted

Drafted
[conclusion-dont-cut-your-way-to-the-future.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/conclusion-dont-cut-your-way-to-the-future.md).

What this chapter now does:

- restates the wrong-win trap without re-deriving the entire manuscript
- restates the brighter future in compact form
- gathers the major failure modes into one closing logic
- ends in a clear leadership choice rather than a vague inspirational close

Why it matters:

- The manuscript now has a full first-draft ending, not just an unfinished
  final arc.
- The book closes as a handbook with a choice, not as a manifesto with a fade.

## 2026-03-28 — Final Book Outputs Built

Built the combined manuscript and publication files:

- [the-business-growth-playbook.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.md)
- [the-business-growth-playbook.epub](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.epub)
- [the-business-growth-playbook.docx](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.docx)
- [the-business-growth-playbook.pdf](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.pdf)

Also added the local builder:

- [build_outputs.py](/Users/lee/projects/ai-coding-book/business-growth-playbook/build_outputs.py)

What this now does:

- assembles the full manuscript from introduction through conclusion in the
  correct order
- uses `BusinessGrowthPlaybook.png` as the cover for EPUB, DOCX, and PDF
- builds bookstore-style publication outputs locally and reproducibly
- leaves the project with a one-command regeneration path for future revision
  passes

How to verify:

1. Rebuild the outputs:
   - `uv run --no-project --with markdown --with python-docx --with reportlab python3 business-growth-playbook/build_outputs.py`
2. Confirm the files exist:
   - [the-business-growth-playbook.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.md)
   - [the-business-growth-playbook.epub](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.epub)
   - [the-business-growth-playbook.docx](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.docx)
   - [the-business-growth-playbook.pdf](/Users/lee/projects/ai-coding-book/business-growth-playbook/the-business-growth-playbook.pdf)
3. Inspect EPUB nav:
   - `unzip -p business-growth-playbook/the-business-growth-playbook.epub EPUB/nav.xhtml`
4. Inspect DOCX core metadata:
   - `unzip -p business-growth-playbook/the-business-growth-playbook.docx docProps/core.xml`
5. Confirm the PDF is valid:
   - `file business-growth-playbook/the-business-growth-playbook.pdf`

## 2026-03-28 — Chapter 11 Drafted

Drafted
[chapter-11-the-leadership-conversation.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-11-the-leadership-conversation.md).

What this chapter now does:

- gives the reader practical language for boards, CFOs, peer executives, and
  outside partners
- defines the twin mandate of efficiency plus empowerment as a leadership
  position rather than a slogan
- reframes the CFO discussion as a capital-allocation conversation, not a
  soft plea against savings
- adds an explicit buyer's framework for evaluating outside partners
- gives the reader a Monday-morning leadership prep instead of another abstract
  framework

Why it matters:

- The manuscript now has a defense-and-alignment chapter, not just a strategy
  and execution system.
- The book is better able to survive real organizational pressure because it
  now tells the reader how to hold the surrounding conversations, not only how
  to think privately.

## 2026-03-28 — Chapter 12 Drafted

Drafted
[chapter-12-the-amplified-enterprise.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-12-the-amplified-enterprise.md).

What this chapter now does:

- shows the future organization in practical terms instead of ending only in
  warning
- elevates smaller, higher-trust teams with disproportionate reach as an
  organizational pattern
- makes amplified people, faster learning, lower fragility, and more credible
  growth part of one coherent future-state picture
- treats Lewis and Clark as an organization-design signal without overstating
  it as already-deployed proof
- gives the reader a Monday-morning future-state review rather than a vague
  aspirational close

Why it matters:

- The manuscript now has a true synthesis chapter rather than only a set of
  adjacent tools.
- The book can now end by showing what the stronger enterprise looks like when
  the system starts becoming normal.

## 2026-03-28 — Companion Book Workspace and Core Package Created

Created the new standalone companion-book workspace at
[business-growth-playbook/](/Users/lee/projects/ai-coding-book/business-growth-playbook).

The initial concept package now exists:

- [author-flow.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/author-flow.md)
- [book-concept.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/book-concept.md)
- [chapter-migration-map.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapter-migration-map.md)
- [story-bank.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/story-bank.md)
- [positioning.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/positioning.md)
- [audience-review.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/audience-review.md)

What this package locked:

- the title
- the paired-book relationship with `growth-consulting-playbook/`
- `Don't Eat Your Seed Corn` as doctrine
- `Capacity Investor` as the identity shift
- `capacity misallocation` as the named invisible failure
- Lewis and Clark / five high performers as the primary structural anchor

Why it matters:

- The book now has a real conceptual center rather than only a discussion trail.
- The demand-side companion is clearly differentiated from the consulting-leader
  manuscript without losing the shared prescription.

## 2026-03-28 — Enterprise-Side Reviewer Set Added

Added three new reviewer agents for this book:

- [enterprise-transformation-reviewer.md](/Users/lee/projects/ai-coding-book/agents/enterprise-transformation-reviewer.md)
- [business-unit-leader-reviewer.md](/Users/lee/projects/ai-coding-book/agents/business-unit-leader-reviewer.md)
- [cfo-reviewer.md](/Users/lee/projects/ai-coding-book/agents/cfo-reviewer.md)

Why it matters:

- The consulting-audience reviewers were not sufficient for a book whose
  protagonist is now an enterprise transformation or operations leader.
- The new review lenses make it easier to catch three different risks:
  enterprise-program vagueness, weak growth relevance, and soft economic logic.

## 2026-03-28 — Local Book Scaffold Added

Added the local continuity and execution files:

- [context.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/context.md)
- [result-review.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/result-review.md)
- [sprint-plan.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/sprint-plan.md)
- [chapter-outline.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapter-outline.md)

Why it matters:

- The book is now set up like a real standalone project, not just a concept
  folder.
- The authoring process is now visible enough to support later tutorial or
  process-writing work.

## 2026-03-28 — Proof Discipline Added and Introduction Drafted

Added two new drafting-control artifacts:

- [doctrine-sheet.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/doctrine-sheet.md)
- [proof-map.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/proof-map.md)

These were created to keep the manuscript from drifting into elegant slogans by
locking:

- exact doctrine definitions
- proof obligations for key terms
- chapter-by-chapter belief shifts
- story-to-proof mappings

Also tightened [chapter-outline.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapter-outline.md)
to reduce repetition in Part I, sharpen the load-bearing middle chapters, and
make the partner-evaluation and Lewis-and-Clark commitments more explicit.

Then drafted the new opening chapter at
[chapters/introduction-the-wrong-win.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/introduction-the-wrong-win.md).

What the introduction now does:

- opens from the enterprise-leader side rather than the consulting-firm side
- establishes `capacity` as the real leadership variable
- makes `Don't Eat Your Seed Corn` immediate and memorable
- frames AI as a question of amplified humans rather than AI abundance alone
- uses Lewis and Clark as an amplification pattern, not just a story

Why it matters:

- The project has moved from planning into actual manuscript drafting.
- The prose now tests whether the doctrine can coexist naturally on the page in
  the language of the intended reader.

## 2026-03-28 — Credibility Strategy Locked

Added [credibility-strategy.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/credibility-strategy.md)
to define how this book earns the right to make a contrarian argument to
enterprise leaders.

The key decision:

- use pattern authority and trusted-advisor authority rather than borrowed
  executive authority

This means the book will speak as someone who has spent decades close to the
decisions, execution, and aftermath across multiple organizations, rather than
pretending to have held every final enterprise leadership title the reader may
hold.

The introduction was also updated to state this stance explicitly once, early,
and then move on.

## 2026-03-28 — Chapter 1 Drafted

Drafted
[chapter-1-the-efficiency-story-everybody-understands.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-1-the-efficiency-story-everybody-understands.md).

What this chapter now does:

- explains why reduction-first AI strategy feels rational, legible, and
  institutionally rewarded
- distinguishes good reduction, necessary reduction, and dangerous reduction
- shows how boards, CFOs, and vendor narratives all reinforce the same narrow
  definition of success
- introduces `capacity misallocation` as the failure mode where real gains are
  harvested without a larger allocation strategy

Why it matters:

- The manuscript now moves beyond introduction-level doctrine into the first
  real argument chapter.
- The opening sequence can now be tested for pacing and repetition risk against
  Chapter 2 rather than only in theory.

## 2026-03-28 — Chapter 2 Drafted

Drafted
[chapter-2-what-gets-lost-when-you-cut-too-deep.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-2-what-gets-lost-when-you-cut-too-deep.md).

What this chapter now does:

- makes invisible loss concrete and person-shaped rather than abstract
- establishes `Knowledge Carriers` in enterprise-side language
- uses the Don story as the main proof that visible diagnosis can hide the real
  value at risk
- argues that continuity is not only defensive, but a growth asset
- begins the logic of a business-side `Do Not Cut List`

Why it matters:

- The opening sequence now has a real escalation:
  - Introduction = wrong win
  - Chapter 1 = why smart leaders choose it
  - Chapter 2 = what that choice actually removes
- The manuscript now has enough opening material to test for pace, repetition,
  and proof strength before the reframe section begins.

## 2026-03-28 — Chapter 3 Drafted

Drafted
[chapter-3-the-multiplier-model.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-3-the-multiplier-model.md).

What this chapter now does:

- introduces the book's central strategic fork for enterprise leaders
- contrasts the extraction path with the investment path
- makes `Efficiency Extractor` versus `Capacity Investor` the leadership mirror
- uses the Rach 2 proof point to show that amplification changes range, not
  just speed
- turns the book from warning into a concrete choice about what AI becomes
  inside the business

Why it matters:

- The manuscript now has its first true reframe chapter.
- The book is no longer only diagnosing the trap; it is starting to define the
  better path with enough specificity to support the rest of the playbook.

## 2026-03-28 — Chapter 4 Drafted

Drafted
[chapter-4-who-ai-replaces-who-it-multiplies.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-4-who-ai-replaces-who-it-multiplies.md).

What this chapter now does:

- turns the reframe into a more explicit handbook chapter
- distinguishes compressed work from multiplied people
- shows why AI often compresses effort before it replaces judgment
- gives leaders a practical classification test for identifying investment
  candidates
- bridges naturally into the underused-talent argument of Chapter 5

Why it matters:

- The manuscript is now moving from doctrine into reusable operating guidance.
- The book's promise as a handbook is becoming visible in the prose, not just
  in the outline.

## 2026-03-28 — Research Backbone Added

Added two new research-control artifacts:

- [research-support.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/research-support.md)
- [reference-ledger.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/reference-ledger.md)

What these now do:

- curate a small, primary-source-heavy support set for the book's strongest
  doctrines
- distinguish direct empirical support from the book's own managerial
  inferences
- log exact findings and safe manuscript uses for each source
- create a hard rule that no study, number, or quote enters the manuscript
  unless it is verified in the reference ledger

Why it matters:

- The book can now gain authority from research without becoming a study-review
  book.
- The sourcing discipline reduces hallucination risk and makes later citation
  passes much safer.

## 2026-03-28 — Early Research Insertion Pass Applied

Added light, verified research reinforcement to the opening manuscript:

- [introduction-the-wrong-win.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/introduction-the-wrong-win.md)
- [chapter-1-the-efficiency-story-everybody-understands.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-1-the-efficiency-story-everybody-understands.md)
- [chapter-2-what-gets-lost-when-you-cut-too-deep.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-2-what-gets-lost-when-you-cut-too-deep.md)
- [chapter-3-the-multiplier-model.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-3-the-multiplier-model.md)
- [chapter-4-who-ai-replaces-who-it-multiplies.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-4-who-ai-replaces-who-it-multiplies.md)

What changed:

- added adoption-speed context from Bick, Blandin, and Deming
- added incentive-bias framing from Acemoglu, Autor, and Johnson
- added augmentation / heterogeneous-gain support from Brynjolfsson, Li, and
  Raymond, Dell'Acqua et al., and the software-developer field experiments
- added tacit-knowledge and forgetting support in the chapter on invisible loss

Why it matters:

- The manuscript now carries a light authority layer without changing its
  handbook voice.
- The book is still led by doctrine and lived proof, but the strongest early
  claims are no longer standing alone.

## 2026-03-28 — Chapter 5 Drafted

Drafted
[chapter-5-the-people-you-didnt-know-you-had.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-5-the-people-you-didnt-know-you-had.md).

What this chapter now does:

- turns the latent-talent claim into a practical talent-diagnostic chapter
- defines five signals of an underused high-ceiling person
- adds a five-question multiplier-candidate test for leaders
- emphasizes coaching, permission, and wider lanes rather than tool access
  alone
- gives the reader a Monday-morning talent scan to run inside one function

Why it matters:

- The hopeful side of the book is now becoming operational rather than merely
  aspirational.
- The manuscript is behaving more clearly like a handbook for leaders, not just
  an argument about what they should believe.

## 2026-03-28 — Chapter 6 Drafted

Drafted
[chapter-6-every-ai-program-needs-a-growth-thesis.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-6-every-ai-program-needs-a-growth-thesis.md).

What this chapter now does:

- forces the book's central allocation question:
  where does the capacity actually go
- uses the MicroStrategy table-smack story shape to show that the first
  question is business value, not available data or technical motion
- defines what a real growth thesis contains and what a savings-only thesis
  looks like
- makes the structured economic case for harvest / strengthen / build instead
  of immediate extraction alone
- adds a handbook test and a Monday-morning capacity review

Why it matters:

- The manuscript has now crossed into the economic center of the book.
- The reader is no longer only being asked to see people differently; they are
  being asked to allocate gains differently.

## 2026-03-28 — Chapter 7 Drafted

Drafted
[chapter-7-stop-funding-the-wrong-work.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-7-stop-funding-the-wrong-work.md).

What this chapter now does:

- turns the growth thesis into a portfolio filter
- defines several forms of AI theater and wrong-work funding patterns
- adds a three-level portfolio test around thesis fit, internal capability, and
  reusable leverage
- distinguishes useful work from strategic work
- gives leaders a Monday-morning portfolio review to sort work into keep,
  redesign, or stop

Why it matters:

- The playbook now moves from thesis and allocation into real funding choices.
- The manuscript is helping leaders not just imagine a better future, but stop
  financing the wrong one.

## 2026-03-28 — Chapter 8 Drafted

Drafted
[chapter-8-build-the-capacity-portfolio.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-8-build-the-capacity-portfolio.md).

What this chapter now does:

- defines the main destination categories for reinvested capacity:
  growth, capability, resilience, and new value
- distinguishes Chapter 8 clearly from Chapter 6 by focusing on destination
  categories rather than thesis logic
- adds practical selection logic for choosing among destinations
- ties the Rach 2 "range" insight to portfolio-level decisions
- gives leaders a Monday-morning capacity portfolio session

Why it matters:

- The book now has a positive answer to the portfolio question, not just a
  negative filter.
- Chapters 6-8 now form a usable operating system: thesis, filter, portfolio.

## 2026-03-28 — Chapter 9 Drafted

Drafted
[chapter-9-redesign-the-program.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-9-redesign-the-program.md).

What this chapter now does:

- turns the Lewis and Clark pattern into a concrete execution model
- explains why broad early rollouts underperform
- defines who should be chosen for the first expedition
- defines what protection, mission, and coaching structure the expedition needs
- explains how learning transfers back into the institution and why that beats
  committee-scale rollout

Why it matters:

- The manuscript now has a distinctive execution chapter, not just a strategy
  chapter.
- The book is increasingly reading like a leadership operating system for real
  AI programs, not just a diagnosis and allocation framework.

## 2026-03-28 — Chapter 10 Drafted

Drafted
[chapter-10-talent-and-operating-model.md](/Users/lee/projects/ai-coding-book/business-growth-playbook/chapters/chapter-10-talent-and-operating-model.md).

What this chapter now does:

- explains why heroics do not scale
- turns coaching, apprenticeship, and transfer into part of the economic case
- uses GPLee as a cultural-spread proof point
- connects Lewis and Clark transfer logic to COE-building logic
- uses AgentFlow as a personal-COE analogue for how systems preserve learning

Why it matters:

- The manuscript now has a systems chapter that explains how amplified work
  compounds instead of staying isolated.
- The book's operating-system claim is now visible not only in the allocation
  model but in the capability model too.
