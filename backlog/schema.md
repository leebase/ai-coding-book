# ai-coding-book Backlog Item Schema

> **The Contract**: AI (scout) → Human (curator) → Builder (factory)

This schema defines the YAML frontmatter format for all backlog items. It unifies:
- Sprint-plan operational focus
- Research mining detail (risks, mitigations, effort)
- Factory consumption requirements

---

## File Location

```
backlog/
├── candidates/       # AI writes here (read-only for AI after write)
├── approved/         # Human moves items here when approved
├── parked/           # Human moves items here (deferred, needs more info)
├── implemented/      # Builder moves items here when complete
└── schema.md         # This file
```

**File naming**: `backlog/{candidates,approved,parked,implemented}/BI-NNN-{kebab-title}.md`

---

## Schema Definition

```yaml
---
# REQUIRED: Identity
id: BI-001                          # Backlog Item ID (BI-NNN)
title: Example Feature              # Human-readable title

# REQUIRED: Source
source: research/primitive          # Which work inspired this
source_insight: >                   # One sentence insight
  Key insight from research goes here.

# REQUIRED: Rationale (why this matters)
opportunity: >                      # What capability is gained
  Describe what the project gains if this is implemented.

why_now: >                          # Tie to current phase/mission
  Why this matters now. Connect to current phase or blockers.

# REQUIRED: Implementation (what to build)
minimal_impl: >                     # Smallest version that works (TinyClaw)
  Describe the smallest implementation that actually works.

definition_of_done:                 # Concrete, measurable outcomes
  - First verifiable outcome
  - Second verifiable outcome

# REQUIRED: Planning metadata
effort: M                          # S (hours) | M (days) | L (weeks)
build_recipe: builder_safe         # planner_only | builder_safe | operator_blocked
  # planner_only = research/ideation only, no code execution
  # builder_safe = code generation allowed, human review required
  # operator_blocked = never auto-execute, human must run

# REQUIRED: Priority
priority: now                       # now | next | someday

# OPTIONAL: Dependencies
dependencies:                       # Required components or prerequisites
  - BI-002
  - External: Some requirement

# OPTIONAL: Risk assessment
risks: >                           # Security, complexity, or distraction risks
  What could go wrong?

mitigations: >                      # How to reduce risks
  How to reduce risks?

# OPTIONAL: Tags for filtering
tags:                              # Free-form tags
  - feature
  - security
  - phase-1

# RUNTIME FIELDS (populated by AI)
status: candidate                  # candidate | approved | parked | implemented
created_at: 2026-03-15T12:00:00Z    # ISO8601 timestamp
created_by: AI-Run-XXX            # Identifier of the run that created this
token_cost: 0                     # Tokens consumed to generate

# CURATOR FIELDS (populated by human)
approved_at: ~                    # ISO8601 timestamp (null if not approved)
approved_by: ~                    # Human who approved
notes: ~                          # Human curator notes

# BUILDER FIELDS (populated by factory)
implemented_at: ~                 # ISO8601 timestamp
implemented_by: ~                 # Builder run identifier
pr_url: ~                         # Link to implementation PR
---

# Body (free-form markdown)

Additional context, discussion, research notes, etc.
```

---

## Field Reference

### Identity Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✅ | Format: `BI-NNN` (e.g., `BI-001`) |
| `title` | string | ✅ | Human-readable, max 80 chars |

### Source Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `source` | string | ✅ | What inspired this |
| `source_insight` | string | ✅ | One-sentence key insight |

### Rationale Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `opportunity` | text | ✅ | What capability is gained |
| `why_now` | text | ✅ | Why this matters now |

### Implementation Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `minimal_impl` | text | ✅ | TinyClaw interpretation |
| `definition_of_done` | list | ✅ | Checklist of measurable outcomes |

### Planning Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `effort` | enum | ✅ | `S` (hours), `M` (days), `L` (weeks) |
| `build_recipe` | enum | ✅ | Execution permission level |
| `priority` | enum | ✅ | `now`, `next`, `someday` |
| `dependencies` | list | ❌ | Prerequisite items or requirements |
| `risks` | text | ❌ | What could go wrong |
| `mitigations` | text | ❌ | How to reduce risks |
| `tags` | list | ❌ | Free-form tags |

---

## Build Recipe Explained

| Recipe | Meaning | Use Case |
|--------|---------|----------|
| `planner_only` | No code execution allowed | Research, architecture docs |
| `builder_safe` | Code generation allowed, human review required | Most implementations |
| `operator_blocked` | Never auto-execute, human must run | Security-critical ops |

---

## Workflow

```
┌─────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   AI    │────▶│Candidates│────▶│ Approved │────▶│Implemented│
│generates│     │(awaiting │     │(ready for│     │(complete) │
│         │     │ review)  │     │ factory) │     │          │
└─────────┘     └──────────┘     └──────────┘     └──────────┘
                       │                ▲
                       ▼                │
                ┌──────────┐           │
                │  Parked  │───────────┘
                │(deferred)│  (revivable)
                └──────────┘
```

---

## Version

Schema Version: 1.0.0
Last Updated: 2026-03-15
