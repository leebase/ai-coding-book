---
# Backlog Item Template
# Copy this file to backlog/candidates/BI-NNN-{kebab-title}.md
# Then fill in all REQUIRED fields (marked with ✅)

id: BI-NNN                          # ✅ REQUIRED: Next sequential number
title: Human-Readable Title         # ✅ REQUIRED: Max 80 chars

source: research/primitive          # ✅ REQUIRED: What inspired this
source_insight: >                   # ✅ REQUIRED: One sentence key insight
  The key insight goes here.

opportunity: >                      # ✅ REQUIRED: What capability is gained
  Describe what the project gains if this is implemented.

why_now: >                          # ✅ REQUIRED: Why this matters now
  Connect to current phase, mission, or blocker.

minimal_impl: >                     # ✅ REQUIRED: TinyClaw version
  Smallest implementation that works. Be specific.

definition_of_done:                 # ✅ REQUIRED: Checklist of outcomes
  - First concrete, verifiable outcome
  - Second concrete, verifiable outcome
  - Third concrete, verifiable outcome

effort: M                          # ✅ REQUIRED: S (hours) | M (days) | L (weeks)
build_recipe: builder_safe         # ✅ REQUIRED: planner_only | builder_safe | operator_blocked
priority: now                       # ✅ REQUIRED: now | next | someday

# Optional but recommended
dependencies:                       # List of BI-NNN IDs or external requirements
  - BI-002
  - External: Some requirement

risks: >                           # What could go wrong?
  Describe security, complexity, or distraction risks.

mitigations: >                      # How to reduce risks?
  Describe specific mitigations.

tags:                              # Free-form tags
  - feature
  - security
  - phase-1

# RUNTIME FIELDS (AI populates these)
status: candidate                  # ✅ REQUIRED: candidate (don't change)
created_at: 2026-03-15T12:00:00Z    # ✅ REQUIRED: ISO8601 timestamp
created_by: AI-Run-XXX            # ✅ REQUIRED: Run identifier
token_cost: 0                     # ✅ REQUIRED: Tokens consumed

# CURATOR FIELDS (Human populates when approving)
approved_at: ~
approved_by: ~
notes: ~

# BUILDER FIELDS (Factory populates when implementing)
implemented_at: ~
implemented_by: ~
pr_url: ~
---

# Additional Context

Write free-form markdown here for:
- Background information
- Open questions
- Reference links
- Implementation notes
