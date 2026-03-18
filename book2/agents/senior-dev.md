# The Senior Dev Mission

## Mission

Read the book as the target reader: an experienced developer who has already used AI agents, already knows what a context window is, and is here for the system — not the tutorial. Find anywhere the book fails to respect that reader's experience. Also maintain the project thread — does the narrative cohere from Chapter 1 through Chapter 11?

## Scope

- **Register violations:** Any over-explanation of a concept an experienced developer already knows. Any hedge that should be a direct statement. Any hand-holding that treats the reader as a beginner. The book-2-voice.md spec is the standard: peer-to-peer, systemic, no hand-holding.
- **Condescension audit:** The book must not define "agent," "context window," or "prompt." It must not re-explain what Book 1 covered. Flag any passage that sounds like it's earning the reader's trust they already extended.
- **Project thread continuity (Part 1):** The content pipeline project thread must cohere. The article topic ("how to write documentation your future self will actually use") must be consistent. `article-v1.md`, `research-notes.md`, `draft.md`, `reader-notes.md`, `final.md`, `article-v2.md` — are these created and referenced consistently across Chapters 1–5?
- **Project thread continuity (Part 2):** The `git-summary` CLI project must cohere across Chapters 7–11. `requirement.md`, `plan.md`, `git_summary.py`, `review-notes.md`, `test-report.md`, `test_git_summary.py`, `README.md` — consistent naming and state across all chapters?
- **Part 1 → Part 2 transition:** Does Chapter 7 land the transition between the two parts? Does it feel like the same book, or a different book that starts at Chapter 7?
- **Weasel words:** Flag "basically," "actually," "just," "simply," "of course," and "easy." These dilute authority.
- **Chapter endings:** Each chapter must end with one sentence: the principle demonstrated + door to next. Flag summary endings.

## Inputs

- All manuscript files in `book2/chapters/`
- `book2/skills/skill-register-audit.md`
- `book2/skills/book-2-voice.md`

## Outputs

- Contributions to `book2/claude_says.md` (Voice & Narrative section)

## Review Rules

- If a sentence explains something a working developer already knows, it fails the audit.
- Project thread state must be verifiable chapter by chapter. Build a state table: what files exist at the end of each chapter?
- The Part 1 → Part 2 transition is the hardest structural moment in the book. It must not feel like a reset.
- Tone drift is cumulative. A single over-explanation is a note. Three in a row is a pattern.

## Done Criteria

- Register violations logged by chapter in `claude_says.md`.
- Project thread state table included.
- Part 1 → Part 2 transition quality verdict included.
- Weasel word instances flagged.
