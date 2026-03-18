# Feedback Log

> **AI Review Workflow**: One AI codes, another reviews and documents feedback here.
> 
> Structure: Most recent feedback at top. Each entry includes reviewer, status, and actionable items.

---

## Feedback Entries (Newest First)

### 2026-03-17 — Review by Lee

**Status**: 🟡 Pending

**Scope**: `book2/` publication quality and reader-facing prose choices

**Findings**:

1. **[UX] EPUB code examples cut off horizontally**
   - **Location**: `book2/coding-with-agent-teams.epub` code/preformatted blocks
   - **Issue**: Long example blocks in EPUB do not wrap cleanly, which makes role-file examples difficult to read on-device.
   - **Recommendation**: Strengthen EPUB `pre` wrapping rules and rebuild the EPUB.
   - **Priority**: 🔴 High

2. **[DOCS] Antigravity callouts feel repetitive**
   - **Location**: Book 2 chapter callouts, especially `> **Antigravity:**` immediately following prose that already states the action
   - **Issue**: The harness layer is clear, but some callouts restate the preceding paragraph instead of adding only the UI-specific step.
   - **Recommendation**: Trim callouts so the surrounding prose carries the concept and the callout carries only the tool-specific action.
   - **Priority**: 🟡 Medium

3. **[STYLE] “Confabulation” is harder than the concept needs to be**
   - **Location**: `book2/chapters/part-1/ch-02-the-grounding-problem.md` and mirrored combined-manuscript passages
   - **Issue**: The term adds cognitive load in a chapter that is trying to sharpen recognition of made-up examples.
   - **Recommendation**: Replace with plainer language such as “invented example” or “made-up example” where possible.
   - **Priority**: 🟡 Medium

**Action Items**:
- [x] Strengthen EPUB code-block wrapping and rebuild Book 2 EPUB (completed by: @ai)
- [x] Replace “confabulation” terminology in reader-facing Book 2 prose (completed by: @ai)
- [ ] Run a focused callout-trimming pass on Book 2 harness callouts (assigned to: @ai)

**Context/Notes**:
Feedback came from human EPUB reading review. The wrapping issue is a production bug; the callout note is still an editorial follow-up. EPUB was first rebuilt with stronger `pre` wrapping rules after pandoc became available, then the worst long-line code examples were manually hard-wrapped in the manuscript and the EPUB was rebuilt again so the fix would survive EPUB readers that ignore `pre` wrapping CSS.

### 2026-03-18 — Review by Claude

**Status**: 🟢 Actioned

**Scope**: `book2/` execution completeness, harness separation, and chapter-to-callout alignment

**Findings**:

1. **[DOCS] Gate and execution steps were underspecified in a few load-bearing places**
   - **Location**: `book2/chapters/part-1/ch-05-run-the-pipeline.md`, `book2/chapters/part-2/ch-10-running-a-sprint.md`
   - **Issue**: The book told the reader to confirm a gate or re-run tests without always saying exactly what to type or run next.
   - **Recommendation**: Add explicit transition wording and concrete test commands.
   - **Priority**: 🔴 High

2. **[DOCS] Part 2 setup chapters had weaker confirmation scaffolding than Part 1**
   - **Location**: `book2/chapters/part-2/ch-07-translating-the-pattern.md`, `book2/chapters/part-2/ch-08-the-coding-team.md`, `book2/chapters/part-2/ch-09-the-feature-skill.md`
   - **Issue**: Part 2 setup had fewer `Watch For` confirmations, which made the harness feel less grounded than the earlier chapters.
   - **Recommendation**: Add targeted `Watch For` callouts for the requirement, role files, and feature-sprint skill.
   - **Priority**: 🟡 Medium

3. **[DOCS] Some file-system actions were too implicit**
   - **Location**: `book2/chapters/part-1/ch-02-the-grounding-problem.md`, `book2/chapters/part-1/ch-04-voice-and-sequence.md`, `book2/chapters/part-2/ch-08-the-coding-team.md`, `book2/chapters/part-2/ch-09-the-feature-skill.md`
   - **Issue**: The book assumed `agents/` and `skills/` directories into existence instead of always instructing the reader to create them.
   - **Recommendation**: Make directory creation explicit where it first matters.
   - **Priority**: 🟡 Medium

**Action Items**:
- [x] Add explicit gate-confirmation wording and concrete test rerun commands (completed by: @ai)
- [x] Add missing Part 2 `Watch For` callouts (completed by: @ai)
- [x] Make `agents/` and `skills/` directory creation explicit in the relevant chapters (completed by: @ai)

**Context/Notes**:
The full Claude review memo lives in `book2/claude_says.md`. Only the high-signal execution and harness-separation points were applied. Lower-priority stylistic notes were intentionally left alone unless they helped a real reader action.
Book 2 publication outputs were then rebuilt from the revised manuscript, and the DOCX builder was updated to write the correct title/author metadata.

### 2026-02-17 — Review by {REVIEWER_NAME}

**Status**: 🟡 Pending / 🟢 Actioned / 🔴 Declined

**Scope**: [Specific files, features, or decisions reviewed]

**Findings**:

1. **[CATEGORY] Brief description of issue**
   - **Location**: `path/to/file:line` or "Architecture decision"
   - **Issue**: What was found
   - **Recommendation**: What should change
   - **Priority**: 🔴 High / 🟡 Medium / 🟢 Low

2. **[CATEGORY] Another finding**
   - **Location**: ...
   - **Issue**: ...
   - **Recommendation**: ...
   - **Priority**: ...

**Action Items**:
- [ ] Item 1 (assigned to: @handler)
- [ ] Item 2 (assigned to: @handler)

**Context/Notes**:
[Any additional context, alternatives considered, or rationale]

---

### 2026-02-17 — Review by PreviousReviewer

**Status**: 🟢 Actioned

**Scope**: Initial architecture review

**Findings**:

1. **[ARCHITECTURE] Template embedding approach**
   - **Location**: `src/main.zig`
   - **Issue**: Runtime template reading adds file dependencies
   - **Recommendation**: Use @embedFile for compile-time embedding
   - **Priority**: 🔴 High

**Action Items**:
- [x] Migrated to @embedFile (completed by: @coder)

**Context/Notes**:
This eliminates runtime dependencies and makes the binary truly portable.

---

## Feedback Categories

Use these prefixes for consistent organization:

- **[ARCHITECTURE]** — Structural decisions, patterns, abstractions
- **[CODE]** — Implementation details, logic, algorithms
- **[API]** — Interface design, CLI arguments, public functions
- **[DOCS]** — Documentation, comments, README
- **[TEST]** — Test coverage, test quality, edge cases
- **[PERF]** — Performance, efficiency, resource usage
- **[SEC]** — Security considerations
- **[UX]** — User experience, error messages, workflow
- **[STYLE]** — Code style, formatting, naming

## Status Legend

- 🟡 **Pending** — Feedback received, action not yet taken
- 🟢 **Actioned** — Changes implemented and verified
- 🔴 **Declined** — Intentionally not addressed (include rationale)
- ⚪ **Superseded** — Overtaken by later decisions (link to new feedback)

## How to Use This File

### As a Reviewer:
1. Copy the template section
2. Fill in your findings with specific locations
3. Set status to 🟡 Pending
4. Assign action items if known

### As a Coder:
1. Read feedback from top (most recent)
2. Address high priority items first
3. Update checkboxes as you complete items
4. Change status to 🟢 Actioned when complete
5. Add brief note about what was done

### When to Decline:
If you disagree with feedback:
1. Change status to 🔴 Declined
2. Add your rationale under Context/Notes
3. Tag the original reviewer for discussion

---

*This file is a living document. Keep feedback actionable, specific, and kind.*
