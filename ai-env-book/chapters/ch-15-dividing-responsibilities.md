# Chapter 15: Dividing Responsibilities

Something broke. You're staring at an error message. The first question is: do I ask my AI coding tool, or do I open Warp?

You face this constantly once you're building real things. And for the first few weeks, you'll probably pick wrong sometimes. Not disastrously — the wrong tool will just tell you it can't help, and you'll switch — but there's friction in the detour. The goal of this chapter is to make the right call on the first try.

---

## The Decision Model

Two questions. Ask them in order.

**Is the problem in a file?**

If you can open a file and see the problem — a syntax error, a missing import, a misconfigured value — it's a file problem. File problems go to the AI coding tool. It can read the file, trace the issue, and write the fix. That's its terrain.

**Is the problem in the machine's running state?**

If the problem is about what's executing right now, what the shell can find, what's listening on a port, or what an environment variable is set to — that's machine state. Machine state lives outside the project files. It lives in the OS. It goes to Warp.

The heuristic in one sentence: if the AI coding tool can read it in a file, it owns the problem. If it lives in the machine's running state, Warp owns it.

---

## Walking Through the Decision

Abstractions are only useful when they connect to real errors. Here are the errors from this book, with the right call for each one.

---

### `ModuleNotFoundError: No module named 'flask'`

**AI coding tool.**

This error means Python can't find the Flask package in the current environment. The fix is installing the package — `pip install flask` inside the active virtual environment, or better, making sure the project's dependencies are installed with `pip install -r requirements.txt` or `uv sync`.

That's a project-level operation. The AI coding tool knows the project structure, knows where `requirements.txt` lives, and knows how to install into the right environment. This is what it's for.

It's tempting to call this a "machine-state problem" because it involves an environment. But the virtual environment is part of the project — it's described in project files, managed by project tools, and the AI coding tool knows how to work with it. The problem is in the project layer, not in the raw OS.

---

### `Error: listen EADDRINUSE: address already in use :::3000`

**Warp.**

A process is occupying port 3000. That process exists in the OS's list of running processes. It's not in any file. The AI coding tool can tell you what kind of problem this is and what the fix probably looks like, but it can't check which process is there or kill it.

Open Warp: `# what is on port 3000`. Get the PID. `# kill that process`. Check again. Start the server.

---

### `zsh: command not found: node`

**Depends.**

This one straddles the line, and it's worth being precise about why.

If Node isn't installed on your machine at all, that's a machine-state problem. Warp can help you install it or diagnose why it's not being found.

If nvm is set up and you just need to switch to the right Node version, that's a project-level operation. The AI coding tool handles version management through nvm — it reads `.nvmrc`, runs `nvm use`, and gets the right version active. It knows the project's requirements. That's not machine state; that's project configuration.

The signal: does the AI coding tool have what it needs to fix this? If nvm is in place and the version is just wrong, yes. If the runtime itself is missing, no — Warp.

---

### `zsh: command not found: gh` (after installing)

**Warp.**

The `gh` binary is on disk, but the shell can't find it because the directory it's in isn't on PATH. The AI coding tool can explain PATH, but it can't look at your current PATH, find the missing directory, and write the fix to your `~/.zshrc` from inside your project files.

This is a shell configuration problem. Open Warp: `# gh command not found but I just installed it`. Follow the diagnostic. If the PATH is missing a directory, `# add [directory] to my PATH permanently`.

---

### `export OPENAI_API_KEY=abc123` disappears after terminal restart

**Warp.**

Shell configuration — not code. The value needs to live in `~/.zshrc` (or the equivalent for your shell), not just in the current session. The AI coding tool can tell you what to write to the file, but Warp is already in a live terminal session and can write it directly.

`# set OPENAI_API_KEY permanently so it survives terminal restarts`. Done.

---

### A syntax error in `backend/app.py`

**AI coding tool.**

It's in a file. The AI coding tool can see it, explain it, and fix it. This is the simplest case.

---

## When You Pick the Wrong Tool

Usually nothing bad happens. You just slow down.

If you paste `EADDRINUSE` into the AI coding tool, it will explain what it means, probably suggest a command, and note that it can't run the command itself. That's a couple of exchanges before you end up in Warp anyway.

If you describe a syntax error to Warp, it will generate a command to open the file or search it — something like `grep -n "def " backend/app.py`. Not useless, but also not what your AI coding tool would do with the same information.

The boundary isn't a trap. It's a guide. Both tools will usually point you toward the right place if you're using the wrong one. The cost is a few extra steps.

---

## The Grey Zone

Some problems genuinely straddle the line. Version management is the main one.

nvm and uv are project-aware tools — they read project files to determine which version to use, and the AI coding tool is designed to work with them. So when nvm needs to switch Node versions for `neighborhood-meals`, that's an AI coding tool operation. When the Python virtual environment needs to be created or activated, that's the AI coding tool.

But when nvm itself is broken — misconfigured, not installed, or invisible to the shell — that's a Warp problem. When uv can't be found because it isn't on PATH, that's a Warp problem. The tool that manages your version managers is a machine-state concern.

The pattern: if the problem is about the state of a project tool, the AI coding tool handles it. If the problem is about whether the tool exists on your machine and your shell can find it, Warp handles it.

---

## Agent Mode

One more thing worth knowing before you close this part.

Warp rebranded as an "Agentic Development Environment" in June 2025 and added a feature called Agent Mode, activated with `Cmd+I` on macOS or `Ctrl+I` on Linux and Windows.

Where `#` generates a single command from a description, Agent Mode takes a multi-step task. You describe the goal — "find what's on port 3000 and kill it" — and Warp runs a sequence of commands to get there, showing you each step.

For the patterns you've built in this book, `#` is the right entry point. Each problem has a clear first command, and you want to see and understand each step. Agent Mode is useful when the task is genuinely multi-step and you trust Warp to sequence it — or when you want to hand it a task rather than a question.

This is the same distinction you saw with your AI coding tool: there's a difference between asking for a specific change and asking for a goal. As you get more experienced, you'll know when to hand Warp a task rather than a command. `#` gets you there first.

---

## A Final Word on Whether You Need This

Warp is optional. The author uses it and finds it worth the subscription — not for coding, but as an on-demand systems administrator for the things an AI coding tool wasn't designed to touch. When something is wrong at the machine level, Warp is faster than switching to a browser, searching for the right command, and then coming back to the terminal.

If you're already comfortable at the command line and don't mind looking things up the old way, you don't need Warp to work effectively with an AI coding tool. The decision model in this chapter — code layer vs. machine layer — applies regardless of which terminal you're using.

What you do need is the mental model. That's what this part of the book was actually about.

---

## The Map

You started this book without a map. You had code that ran sometimes, error messages that didn't mean anything, and an AI tool that was confidently guessing about things it couldn't see.

Here's what the map looks like now.

**Git and GitHub** are version control and remote hosting. Git tracks snapshots. GitHub hosts them. Authentication problems at the GitHub layer — not git problems, not code problems — belong to the auth tooling.

**Python environments** are isolated containers of packages, one per project. When the environment isn't active or the wrong version is active, you get import errors that aren't import problems. The AI coding tool manages the environment. You know what "activate" means.

**Node and npm** follow the same logic as Python, with version management via nvm. The `.nvmrc` file declares which version the project expects. The AI reads it. Version mismatches are not broken code.

**Machine state** is the layer underneath all of it: running processes, PATH, shell configuration, environment variables. The AI coding tool works in the file layer. Warp works in the machine layer. Both are open. You switch based on what you're looking at.

The lines will blur as both tools evolve. Warp will get better at understanding code. AI coding tools will get better at understanding machines. But the underlying distinction — code versus environment — isn't going away. It's not a Warp feature or a Claude feature. It's how operating systems work.

> **Key Takeaway:** Code problems go to the AI coding tool. Machine-state problems go to Warp. When you're not sure which you have, ask: is this in a file, or in the running state of the machine?

---

You don't need to know every command — you need to recognize what kind of problem you're looking at, and now you do.
