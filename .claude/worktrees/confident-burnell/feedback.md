# Feedback Log

> **AI Review Workflow**: One AI codes, another reviews and documents feedback here.
> 
> Structure: Most recent feedback at top. Each entry includes reviewer, status, and actionable items.

---

## Feedback Entries (Newest First)

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
