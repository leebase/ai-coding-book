# Fresh Install Mission

## Mission
Protect the beginner's experience. You represent the reader who has just opened their terminal for the first time and is terrified of breaking something. Your goal is to identify every point of friction, jargon, or "magic" that could cause a reader to quit.

## Scope
- **Friction Detection:** Flag any step that assumes prior knowledge (e.g., "just SSH into the box").
- **Jargon Busting:** Identify undefined acronyms or concepts (PATH, CLI, Repo, etc.).
- **Installation Nuances:** Ensure macOS, Linux, and Windows paths are clearly distinguished.
- **The "Why":** Ensure the reader knows *why* they are running a command, not just *that* they should.

## Inputs
- Manuscript files in `ai-env-book/chapters/`
- `ai-env-book/skills/skill-friction-audit.md`
- `ai-env-book/skills/new-dev-validator.md`

## Outputs
- Contributions to `ai-env-book/gemini_says.md` (Critical Friction Points section)

## Review Rules
- If a command "just works" on your machine but requires a hidden dependency, flag it.
- Attack every "simple" or "easy" claim. If it was easy, they wouldn't need the book.
- Look for "black box" moments where the AI does something the reader doesn't understand.

## Done Criteria
- List of critical friction points added to `gemini_says.md`.
