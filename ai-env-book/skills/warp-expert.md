# Skill: Warp Expert

> This file is the canonical source of truth for all Warp-related content.
> Load it for chapters covering the Warp terminal (ch-09 through ch-11).
> Do not write Warp content from general knowledge — use only what is in here.

---

## What Warp Is

Warp is a terminal emulator built for developers who want to stop memorizing
shell commands and start describing what they want in plain English. It is not
a replacement for your AI coding tool — it fills the gap between "I need to
fix this code" (which Claude handles) and "I need to fix my environment"
(which is where most new developers get stuck).

Warp was originally Mac-only. As of 2025:
- **macOS**: fully supported (Intel and Apple Silicon, macOS 10.14+)
- **Linux**: available since February 2024 (x86_64 and ARM64)
- **Windows**: available since February 2025 (Windows 10 v1809+)

As of June 2025, Warp rebranded as an "Agentic Development Environment" —
a terminal plus editor plus AI agent in one tool. For the book's audience,
what matters most is the terminal + AI command features. Introduce the broader
rebranding only in ch-11 (where to go from here).

---

## Core Concept: Blocks

Every command you run in Warp produces a **block** — a self-contained unit
that groups the command, its output, and metadata (when it ran, how long it
took, whether it succeeded). Failed commands show a red indicator. You can
scroll back and navigate between blocks with the arrow keys.

Why this matters for new developers:
- You can see exactly what ran and what it produced, without output scrolling
  off the screen
- You can share a block (as a web link) to ask for help without copy-pasting
- You can search within a single block's output with `Cmd+F`

Do not anthropomorphize blocks. They are not "smart" — they are just better
output grouping than a traditional terminal.

---

## AI Features

### `#` — AI Command Search

Type `#` at the command prompt to open the AI Command Search box. Describe
what you want in plain English. Warp generates the command.

**Example interactions for the book:**

| What you type after `#` | What Warp suggests |
|-------------------------|-------------------|
| `what is using port 3000` | `lsof -i :3000` |
| `kill whatever is on port 3000` | `lsof -ti:3000 \| xargs kill -9` |
| `show me the last 50 lines of my npm install log` | `tail -n 50 npm-debug.log` |
| `add /usr/local/bin to my PATH permanently` | `echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc` |
| `what environment variable is NODE_ENV set to` | `echo $NODE_ENV` |

The `#` prefix cannot be disabled. If a reader reports that `#` is doing
something else, they are likely in a different shell (fish, for example, uses
`#` for comments in scripts but not in the interactive prompt).

### Agent Mode (`Cmd+I` / `Ctrl+I`)

Agent Mode is a fully shipped feature as of June 2025. The keyboard shortcut
is `Cmd+I` on Mac and `Ctrl+I` on Linux and Windows.

In Agent Mode, Warp can:
- Run a sequence of commands to complete a multi-step task
- Read the output of each command and adjust its next action
- Self-correct when a command fails

For the book's audience, introduce Agent Mode in ch-11 only. New developers
should build the mental model of "describe → get command → review → run"
before jumping to "let Warp do it all."

**Do not present Agent Mode as a reason to skip understanding commands.**
The book's thesis is recognition over recall — Agent Mode still produces
commands, and the reader needs to recognize whether those commands are safe.

### Models

Warp AI defaults to Claude 3.5 Sonnet. GPT-4o and Claude 3.5 Haiku are also
available. This is an implementation detail — do not lead with it. The reader
does not need to choose a model to use `#` effectively.

---

## Warp Drive

Warp Drive is a library of saved, shareable, reusable commands. Think of it
as a command cookbook that your team can all read from and write to.

### Workflows

A workflow is a parameterized command — a command with blanks you fill in.
Example: a workflow called "Kill port" might store `lsof -ti:{PORT} | xargs kill -9`
where `{PORT}` is the blank. When you run it, Warp prompts you to fill in the
value.

Workflows live in Warp Drive and sync in real time across teammates.

For the book: introduce workflows in ch-10 after the reader has already used
`#` to generate commands. The workflow concept lands better once the reader
has seen the underlying command form at least once.

### Notebooks

A Warp notebook is a runnable document — Markdown text mixed with embedded
shell commands. A notebook can document a procedure (say, "how to set up this
project from scratch") and let the reader run each step directly in Warp
without copy-pasting.

For the book: mention notebooks as a "what Warp Drive can grow into" idea in
ch-11. Do not make notebooks a primary teaching concept for new developers —
the `#` workflow is the right entry point.

---

## Five Patterns for the Scenario Thread

These are the five concrete sysadmin moments the scenario character
encounters. Use these as the basis for worked examples in chapters 9–11.

### Pattern 1: "Something is broken, I don't know why"

The reader's npm install failed (or Python virtualenv is broken, or `node`
is not found). They have an error message but do not know the right search
terms.

**Warp pattern:**
1. Type `#` to open AI Command Search
2. Paste or describe the error: `npm ERR! missing script: start`
3. Warp suggests the diagnostic command (`cat package.json | grep scripts`)
4. Reader runs it, sees the problem, types `#` again to fix it

**Key teaching point:** Describing the error in plain English is a skill.
"npm is broken" is too vague. "npm says missing script start" is specific
enough for Warp to help.

### Pattern 2: Kill a stuck process

The reader's dev server is running and they cannot start another one because
"port 3000 is already in use."

**Warp pattern:**
1. `# what is on port 3000`
2. Warp suggests `lsof -i :3000` — reader sees the process and its PID
3. `# kill that process` or `# kill PID 12345`
4. Warp suggests `kill -9 12345`

**Key teaching point:** The reader learns that a port conflict means a
process is alive somewhere. They do not need to memorize `lsof` — but after
seeing it twice they will recognize it.

### Pattern 3: Fix a PATH problem

A newly installed tool (`gh`, `poetry`, `node`) is "not found" even though
the install succeeded. The tool is on disk but not on PATH.

**Warp pattern:**
1. `# gh command not found but I just installed it`
2. Warp suggests checking `which gh` and examining `$PATH`
3. `# add /usr/local/bin to my PATH permanently`
4. Warp generates the right `echo >> ~/.zshrc` line and `source` command

**Key teaching point:** PATH errors look like the tool is broken. It is
usually not. Recognition: "command not found after install = PATH problem."

### Pattern 4: Set an environment variable permanently

The reader is following a tutorial that says `export MY_KEY=abc123` but the
variable disappears after they close the terminal.

**Warp pattern:**
1. `# set MY_API_KEY permanently so it survives terminal restarts`
2. Warp generates the `echo 'export MY_API_KEY=abc123' >> ~/.zshrc && source ~/.zshrc` command
3. Reader runs it, opens a new terminal, confirms with `echo $MY_API_KEY`

**Key teaching point:** `export` in the terminal sets a variable for the
session. Shell config files (`~/.zshrc`, `~/.bashrc`) persist across sessions.

### Pattern 5: Find what is using a port before starting a server

Preventive pattern — the reader has been burned before and wants to check
before starting their dev server.

**Warp pattern:**
1. `# is anything on port 3000 right now`
2. `lsof -i :3000` returns nothing — safe to start
3. Reader starts the server

**Key teaching point:** Checking first is faster than killing after. A single
`#` query adds five seconds to startup and prevents ten minutes of confusion.

---

## Authoring Rules for Warp Chapters

- All feature descriptions in this file are based on verified 2025 Warp
  behavior. Do not add features not listed here without re-researching.
- Warp 2.0 rebranded as "Agentic Development Environment" in June 2025.
  Use the term "Warp terminal" for the core product in ch-09 and ch-10.
  Acknowledge the broader Warp 2.0 positioning only in ch-11.
- Do not describe Warp as a replacement for Claude or an AI coding tool.
  Warp covers system-level tasks; Claude covers code-level tasks. They
  are complementary, not competitive.
- Windows users: Warp is available. Mention this early to avoid alienating
  readers — it was Mac-only until 2024 and the reputation lingers.
- `#` is the primary interaction pattern for new developers. Prioritize it
  over Agent Mode. A reader who gets comfortable with `#` is already
  dramatically more capable than a reader who types raw commands from memory.
- The recognition thesis applies here too: after seeing `lsof` twice in a
  Warp-generated suggestion, the reader should recognize it. They do not
  need to memorize its flags.
