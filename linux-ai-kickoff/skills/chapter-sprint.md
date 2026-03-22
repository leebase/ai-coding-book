# Skill: Chapter Sprint

Use this skill when planning, drafting, reviewing, and closing a chapter sprint
for Teach Yourself Anything.

This is the local writing-loop adaptation of AgentFlow for this book.

## Required Inputs

- the chapter's place in `architecture.md`
- the current status in `context.md` and `sprint-plan.md`
- the relevant local skills for this chapter
- the relevant primary sources if the chapter is technical

## Default Skill Stack

- `skills/mission-ladder.md`
- `skills/possibility-framing.md`
- `skills/ai-as-tutor.md`
- `skills/lee-voice.md`

For technical chapters also use:

- `skills/manual-first.md`
- `ai-env-book/skills/env-explainer.md`
- `ai-env-book/skills/new-dev-validator.md`
- `ai-env-book/skills/skill-command-safety.md` when commands can bite

## Agent Sequence

1. `mission-designer`
2. `pathfinder`
3. `manual-guide` for technical chapters
4. `confidence-auditor`
5. `continuity-editor`
6. `confused-beginner` or a beginner-friction review when needed

## Sprint Loop

### Stage 1 - Lock the mission

Use `mission-ladder` and `possibility-framing`.

Produce:

- chapter mission
- why it matters
- visible outcome
- next door it opens

### Stage 2 - Map the sources

Use `manual-first` when the chapter depends on technical truth.

Produce:

- exact source sections
- why each source matters
- what should stay out of the chapter

### Stage 3 - Draft the chapter

Use `lee-voice` and `ai-as-tutor`.

Write for a smart reader who needs orientation, not hand-holding.

### Stage 4 - Run review

Run the agent sequence in order.

Do not skip `manual-guide` on technical chapters or `confidence-auditor` on any
chapter.

### Stage 5 - Revise

Fix clarity, drift, confidence problems, and source-accuracy issues before
calling the sprint done.

### Stage 6 - Close the sprint

Update:

- `context.md`
- `result-review.md`
- `sprint-plan.md`

Commit and push the sprint on the working branch.

## Hands-Off Mode

Lee has explicitly asked for hands-off execution. That means the agent may
continue through the full chapter sprint once the mission is coherent, instead
of pausing for a human outline gate.

Do not use that freedom as an excuse to skip review discipline.
