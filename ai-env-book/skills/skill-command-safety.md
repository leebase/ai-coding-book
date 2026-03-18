# Skill: Command Safety Audit

## Goal

Verify that every potentially destructive command in the book is adequately framed. A reader who runs commands verbatim without understanding consequences must not be able to damage their system or lose data.

## Directives

### 1. Destructive Command Inventory

Build a table of every command in the book that can cause data loss or system state corruption:

| Command | Chapter | Risk | Current Framing | Verdict |
|---------|---------|------|-----------------|---------|
| `kill -9 <pid>` | Ch 13 | Terminates process without cleanup | ? | ? |
| `git reset --hard` | Ch 5 | Discards uncommitted work | ? | ? |
| `echo "..." >> ~/.zshrc` | Ch 10, 14 | Dotfile mutation (duplicates on re-run) | ? | ? |
| `source ~/.zshrc` | Ch 10, 14 | Reloads shell config (may hide errors) | ? | ? |
| `curl -o- URL \| bash` | Ch 10 | Executes remote code | ? | ? |

Verify the "Current Framing" for each entry. A command has adequate framing if: (a) the risk is named, (b) the recovery path is named (or stated to not exist).

### 2. `kill -9` Standard

- Verdict: PASS if the text calls `kill -9` a last resort or nuclear option, names that processes may not clean up after themselves, and provides a non-kill alternative (e.g., closing the terminal tab, restarting the service)
- Verdict: FAIL if `kill -9` is presented as the standard way to stop a process

### 3. Dotfile Idempotency

For every `echo >> ~/.zshrc` pattern:
- Does the text warn the reader that running this twice produces duplicate entries?
- Does the text show how to verify the current state of the file before appending?
- Is there an `if not exists` pattern or equivalent guidance?

### 4. SSH Configuration Safety

For `~/.ssh/config` modifications:
- Is the `Host`, `HostName`, `User`, and `IdentityFile` structure fully explained?
- Does the text warn that incorrect entries can break other SSH connections?
- Is there a verification step (`ssh -T git@github.com`)?

### 5. Git Destructive Operations

For `git reset --hard`:
- Is uncommitted work loss explicitly named?
- Is `git stash` offered as an alternative?
- Is the command shown only in a context where the reader has been warned?
