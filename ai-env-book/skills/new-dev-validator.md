# Skill: New-Dev Validator

Use this skill when reviewing a chapter draft from the perspective of a
zero-context reader. Assume the reader is smart, motivated, and new to terminal
work. They have likely seen an AI tool run commands for them, but they do not
already know what shells, PATH, activation, processes, package managers, or
version managers are. Your job is to pressure-test whether the draft can still
be followed by that reader.

---

## Core Standard

A draft passes this review only if a new developer can:

1. recognize the situation they are in
2. understand what the command or fix is doing
3. tell what part the AI handled versus what they still need to understand

If any one of those fails, flag it.

---

## Review Method

Read the draft in order. Stop at every paragraph, command block, screenshot
caption, and transition. Ask the following questions in plain language:

1. **Prerequisite check**: What does this section assume the reader already
   knows? Flag unstated prerequisites concretely.
   Example: "This paragraph assumes the reader knows what an environment
   variable is before the book has named that concept."

2. **Terminal familiarity check**: Does this step assume comfort with the
   terminal, file paths, prompts, or command output? If yes, flag the exact
   assumption.
   Example: "This says 'open a shell and run' as if the reader already knows
   what the prompt is and where the command should be entered."

3. **Error-first check**: Is the actual error, warning, or moment of confusion
   shown before the explanation? If the draft explains first and shows the
   problem later, flag the ordering problem.

4. **Command intent check**: Does the draft explain what a command does before
   or immediately after showing it? A new dev does not need command trivia, but
   they do need the purpose.
   Example: "The chapter gives `python -m venv .venv` without first saying it
   creates a project-local Python environment."

5. **Memorization check**: Does the draft ask the reader to remember a command,
   flag, or sequence instead of teaching recognition? Flag any passage that
   drifts into rote instruction.

6. **Jargon check**: Is a term used before it is defined inline? Flag the first
   unexplained use and suggest the missing one-sentence definition.

7. **Transition check**: Does the chapter jump from one idea to another without
   telling the reader why the shift happened? Flag the broken transition and
   state what bridge sentence is missing.

8. **Ownership check**: Is it clear what the AI tool is doing and what the
   reader still owns? Flag sections that blur the line.
   Example: "The draft says the AI 'fixed the environment' but never explains
   what the reader should verify afterward."

9. **Scenario consistency check**: Does the draft stay consistent with
   `skills/scenario-thread.md`? Flag invented facts, changed tooling, or
   timeline drift.

---

## What A Good Flag Looks Like

Every flag must include four parts:

1. the location
2. the reader problem
3. why it matters for a zero-context reader
4. a concrete fix direction

Bad flag:

"This section is confusing."

Good flag:

"Paragraph 5 introduces 'activation' as if it were already known. A new reader
who has only clicked run buttons in an editor will not know that activation
changes which Python the terminal uses. Add one sentence defining activation
before the command block."

---

## Severity

- **Block**: The reader cannot correctly follow the chapter without outside
  knowledge.
- **Fix**: The reader can continue, but confusion or a wrong mental model is
  likely.
- **Note**: The section is basically correct, but can be made easier to
  recognize.

Use `Block` for missing prerequisites, missing error context, or commands shown
without enough explanation to understand their purpose.

---

## Review Output Format

When you write review notes, group them by severity and keep them actionable.
Use this pattern:

- `Block` - paragraph or section reference - problem - required change
- `Fix` - paragraph or section reference - problem - recommended change
- `Note` - paragraph or section reference - minor improvement

If there are no issues in one severity level, say so explicitly rather than
skipping it.

---

## What This Skill Does Not Do

- It does not copyedit for grammar or polish.
- It does not rewrite the chapter for the author.
- It does not demand beginner-level simplification of every technical term.
- It does not expand scope beyond the chapter's assigned concept.

Technical content is allowed. Hidden assumptions are not. The test is not
"would an expert approve this?" The test is "could a new developer recognize
their own problem here and stay oriented while the AI helps fix it?"
