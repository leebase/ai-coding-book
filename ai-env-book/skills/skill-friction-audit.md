# Skill: Friction Audit

## Goal

Find every point where a reader executing the book's instructions would get stuck, confused, or produce an error — not because the reader is wrong, but because the text is incomplete.

## Directives

### 1. Step Completeness Test

For each chapter with executable instructions:
- List every command the reader must run
- Verify each command has: (a) a starting state defined, (b) an expected output shown or described, (c) a verification step or success indicator
- Flag any command that arrives without a defined starting state

### 2. Prerequisite Audit

The book assumes the reader has: a terminal, git installed, a GitHub account, Python installed, Node installed, and Warp (for Part 4). Verify these are stated at the appropriate point. Flag any chapter that introduces a new tool without verifying it is installed.

### 3. "It Just Works" Detection

- Flag any instruction that says "this will work" or "you'll see" without showing what "working" looks like
- Flag any "your output may vary" without specifying what variance is acceptable
- Flag any instruction that assumes a specific OS state (e.g., assumes zsh, not bash) without noting it

### 4. Forward Reference Check

If Chapter N requires knowledge or a file state from Chapter M, verify the forward reference is explicit. A reader who reads chapters out of order should know they're missing context.

### 5. URL and Installer Stability

- Identify any URLs shown in the text (installer URLs, GitHub links)
- Flag any URL that could rot (i.e., version-specific download links)
- Flag any `curl | bash` pattern without a "what this does" explanation

### 6. Error Recovery Coverage

For each chapter that introduces a new tool or operation, check: does the text describe what to do if the operation fails? A reader who gets an unexpected error should have a path forward.
