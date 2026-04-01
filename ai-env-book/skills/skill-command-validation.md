# Skill: Command Validation

## Goal
Ensure 100% technical accuracy and robustness across all platforms and tool versions.

## Directives

### 1. Adversarial Testing
- Assume the reader has the "wrong" version of everything.
- Flag commands that break if there's a space in the directory name or an unusual shell configuration.

### 2. Cross-Platform Parity
- Verify that every Bash command has an equivalent (or a warning) for Windows users (PowerShell/CMD) if they aren't using a terminal like Warp.
- Ensure version checks (e.g., `python --version`) are included before version-sensitive operations.

### 3. The "Red Zone" Audit
- Identify any command that could cause data loss or system instability if misconfigured.
- Ensure these "Red Zone" commands are preceded by a "Warning" callout and a "How to Undo" instruction.

### 4. Shell Awareness
- Audit for Zsh-specific syntax that might fail in Bash (or vice-versa).
- Ensure shell profile loading (e.g., `source ~/.zshrc`) is explained when environment variables are changed.
