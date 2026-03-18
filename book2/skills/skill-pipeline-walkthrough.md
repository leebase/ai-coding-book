# Skill: Pipeline Walkthrough

## Goal

Execute every pipeline step mentally as a reader following exact instructions. Find gaps, ambiguities, and missing success criteria.

## Directives

### 1. Step Completeness Audit

- For every instruction, ask: could a reader execute this with only what appears on the page?
- Flag any step that requires inferring the file path, session state, or prior step outcome.
- Flag any step that says "paste the role definition" without specifying where the definition is.

### 2. Gate Quality Check

- Every gate must have: (a) what the reader checks, (b) what a passing output looks like, (c) what a failing output looks like.
- A gate that only says "review before proceeding" has no success criteria. Flag it.
- The mandatory gate after Stage 1 in the feature sprint is the most critical — audit it with extra rigor.

### 3. Comparison Exercise Verification

- Track `article-v1.md` from Chapter 1 through Chapter 5. Is the reader instructed not to modify it? Is it preserved?
- In Chapter 5: are the differences between `article-v1.md` and `article-v2.md` named specifically? (Voice, examples, misconceptions addressed — not just "better.")
- If the differences are described as "not subtle," the text must make them nameable.

### 4. Parallel Session Readiness

- Identify the first chapter that requires Manager View or simultaneous sessions.
- Is Manager View explained before it is required?
- Does the reader have enough information to manage two concurrent sessions without losing state?

### 5. File State Tracking

- Build a chapter-by-chapter file inventory: what files are created, modified, or referenced?
- Flag any chapter that references a file before it was created.
- Flag any filename inconsistency across chapters.
