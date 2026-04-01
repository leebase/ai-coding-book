# Skill: O'Reilly Rigor

## Goal
Enforce professional technical publishing standards, ensuring the book is authoritative, consistent, and logically structured.

## Directives

### 1. Structural Logic
- Every chapter must start with a "What You Will Learn" list and end with a "Summary" and "Next Steps."
- Concepts must flow from "Definition" to "Application" to "AI-Assisted Context."
- Use Mermaid diagrams for any process with more than 3 steps.

### 2. Technical Precision
- Audit for "weasel words" (e.g., "basically," "actually," "just," "simply").
- Ensure all technical terms are defined upon first use.
- Maintain a consistent "Peer-to-Peer" register (senior engineer explaining to a junior colleague).

### 3. Formatting Standards
- **Note:** Use for side-bar context that isn't essential to the main thread.
- **Tip:** Use for AI-specific "power moves" or environment shortcuts.
- **Warning:** Use for destructive operations (e.g., `rm -rf`, `git reset --hard`).

### 4. Visual Hierarchy
- Use H1 for chapter titles, H2 for main sections, H3 for sub-sections.
- Code blocks must include a comment line indicating the shell or file name (e.g., `# bash` or `// package.json`).
