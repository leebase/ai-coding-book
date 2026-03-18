# Skill: Scenario Coherence Audit

## Goal

Verify that the `neighborhood-meals` scenario thread is a self-consistent narrative throughout the book. The scenario must feel like a real project with a real history, not a device that appears and disappears to serve individual chapters.

## Directives

### 1. Scenario State Table

Build a table tracking the scenario state at each chapter:

| Chapter | Team Composition | Current Problem | Files/State | Scenario Role |
|---------|-----------------|-----------------|-------------|---------------|
| Intro | ? | ? | ? | Frame |
| Ch 1 | ? | ? | ? | ? |
| ... | | | | |

"Scenario Role" is one of: **Frame** (sets up why this matters), **Illustrative** (demonstrates the chapter's concept), **Decorative** (mentioned but doesn't carry argument).

Flag any Decorative usage.

### 2. Team Composition Consistency

Track when "teammates" are introduced. If Ch 6 says "a teammate encounters a Python environment error," verify that teammates were established in an earlier chapter. Flag any team composition that changes without explanation.

### 3. Perspective Consistency

The book addresses "you" — a single developer building `neighborhood-meals`. Flag any passage that:
- Shifts to "developers" (generic third person)
- Suddenly adds teammates without prior establishment
- Uses first person ("we built")

### 4. File and Directory Path Consistency

Track any specific file paths mentioned in the scenario:
- `neighborhood-meals/` (root)
- `neighborhood-meals/backend/` (Python)
- `neighborhood-meals/frontend/` (React/Node)

Flag any inconsistency in path naming or directory structure across chapters.

### 5. Problem-to-Chapter Alignment

Each scenario problem must clearly illustrate the chapter's core concept. Test: could the reader state, in one sentence, what the scenario problem demonstrates about the chapter's topic? Flag scenario appearances where this connection is unclear.

### 6. Conclusion Payoff

Verify the Conclusion closes the scenario arc: the reader has built `neighborhood-meals`, managed its environment, and knows what to do when things break. A conclusion that abandons the scenario for abstract reflection fails this test.
