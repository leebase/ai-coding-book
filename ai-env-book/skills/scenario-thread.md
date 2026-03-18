# Skill: Scenario Thread

This file is the canonical source of truth for the book's running scenario.
Every brief, draft, and review must match it. Do not invent a different repo,
different filenames, different branches, or different error messages unless this
file is updated first and the change is called out explicitly.

## Reader and Project

The reader is an unnamed "you" in second person. You are a new developer who
has finished tutorials, has started using an AI coding tool, and has just
cloned a real project that does not run cleanly on the first try.

The project is `neighborhood-meals`, a small full-stack web app for managing
community meal pickups. It is simple enough to explain, but real enough to
create Git, Python, Node, and system-level environment problems.

It is a real companion repository for this book, not an invented folder name
used only in prose. The canonical GitHub repository is:
`https://github.com/leebase/neighborhood-meals.git`

The repo name is always `neighborhood-meals`. The default branch is always
`main`. The remote is always `origin`.

Branch roles are fixed:

- `main` is the book-facing branch. It preserves intentional setup and workflow
  friction while keeping the core app behavior correct.
- `reference-working` is the known-good runnable baseline. It exists so a
  reader can compare "environment problem" against "application problem."
- `feat/theme-switcher` is the workflow-support branch used for branch and
  worktree examples.

## Canonical Repo Layout

Use this structure when chapters need to name files or directories:

```text
neighborhood-meals/
  README.md
  .gitignore
  backend/
    app.py
    pyproject.toml
    requirements.txt
    neighborhood_meals/
      __init__.py
      routes.py
  frontend/
    package.json
    package-lock.json
    src/
      App.jsx
      main.jsx
```

Important conventions:

- Python work happens in `backend/`
- Node work happens in `frontend/`
- The Python virtual environment directory is `backend/.venv`
- The frontend dev server runs on port `3000`
- The backend dev server runs on port `8000`
- The feature branch used in branch/worktree examples is `feat/theme-switcher`
- The known-good comparison branch is `reference-working`
- The extra worktree path is `../neighborhood-meals-theme-switcher`
- The shell config file is `~/.zshrc`

`backend/requirements.txt` and `backend/pyproject.toml` both exist on purpose.
The repo is in a transition period: older setup notes still mention
`requirements.txt`, while the newer dependency declaration lives in
`pyproject.toml`. Chapter 8 explains this instead of treating it as a mistake.

## Environment and Versions

Assume a Mac-like developer environment unless a chapter explicitly says
otherwise. Linux readers are still in scope, but the canonical shell and file
paths are macOS-style.

- OS: macOS with `zsh`
- Git: 2.43+
- Python: 3.11.8
- `uv`: 0.5.x
- Node: 20.11.1
- npm: 10.2.4
- `nvm`: 0.39.x
- Warp: current release with blocks, AI Command via `#`, Warp Drive, and Agent
  Mode available

Do not write chapters that depend on a specific IDE, package manager UI, or
Warp build number. The stable part is the mental model and the terminal output.

## Canonical Walls and Exact Error Messages

These are the walls the reader hits across the book. When a chapter needs a
verbatim error message, use these strings.

### Part 1: Git and GitHub

The reader has cloned `neighborhood-meals` and is already confused about what
Git is tracking, what lives on GitHub, and why the AI keeps talking about
branches, remotes, and worktrees.

Wrong directory wall:

```text
fatal: not a git repository (or any of the parent directories): .git
```

GitHub auth wall:

```text
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

Worktree wall:

```text
fatal: 'feat/theme-switcher' is already checked out at '/Users/you/code/neighborhood-meals'
```

Dirty working tree wall:

```text
error: Your local changes to the following files would be overwritten by checkout:
	frontend/src/App.jsx
Please commit your changes or stash them before you switch branches.
Aborting
```

### Part 2: Python Environments

The backend does not run on the first try. The reader learns that "Python is
installed" is not the same as "this project is running in the right Python
environment."

Missing dependency wall:

```text
Traceback (most recent call last):
  File "/Users/you/code/neighborhood-meals/backend/app.py", line 1, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
```

Wrong interpreter wall:

```text
ERROR: Package 'neighborhood-meals-backend' requires a different Python: 3.9.6 not in '>=3.11'
```

Chapter 8 is the "read the metadata" moment. The AI opens `backend/pyproject.toml`
and `backend/requirements.txt` to understand what the project expects before it
installs or upgrades anything.

### Part 3: Node and npm

The frontend compounds the confusion. Even after Python is fixed, the browser
app still needs the right runtime, the right version, and a populated
`node_modules` directory.

Node missing wall:

```text
zsh: command not found: node
```

Wrong Node version wall:

```text
npm ERR! code EBADENGINE
npm ERR! engine Unsupported engine
npm ERR! engine Not compatible with your version of node/npm: neighborhood-meals-frontend@0.1.0
npm ERR! notsup Not compatible with your version of node/npm: neighborhood-meals-frontend@0.1.0
npm ERR! notsup Required: {"node":">=20.11.0"}
npm ERR! notsup Actual:   {"npm":"10.2.4","node":"18.19.0"}
```

Missing local packages wall:

```text
> neighborhood-meals-frontend@0.1.0 dev
> vite

sh: vite: command not found
```

### Part 4: Warp and System-Level Problems

By this point the reader understands that some failures are not code failures.
They are machine-state failures: a port is occupied, PATH is wrong, or an
environment variable was only set for one shell session.

Port conflict wall:

```text
Error: listen EADDRINUSE: address already in use :::3000
```

PATH wall:

```text
zsh: command not found: gh
```

Persistence wall:

The reader sets an environment variable with `export` in the current terminal,
opens a new terminal, and it is gone. This is a "session vs shell config" wall,
not a code wall. Writers may show `echo $OPENAI_API_KEY` returning nothing after
a restart, but the core lesson is persistence, not the exact variable name.

## Chapter-by-Chapter Thread

Use this as the progression map.

1. Introduction: the reader clones `neighborhood-meals` and learns the thesis:
   the problem is not intelligence, it is missing environment context.
2. Chapter 1: the AI uses `git status`, the reader sees tracked vs untracked
   files, and learns what the `.git` directory is doing.
3. Chapter 2: local Git and hosted GitHub are separated clearly. GitHub is
   where the remote copy and pull requests live; Git is still local first.
4. Chapter 3: the push fails because the machine is not authorized to GitHub.
5. Chapter 4: the reader sees why the AI creates a branch and sometimes a
   second worktree instead of piling changes into one folder.
6. Chapter 5: the reader hits a dirty-tree problem and learns what Git is
   protecting them from.
7. Chapter 6: the backend fails because packages are not installed in an
   isolated environment yet.
8. Chapter 7: the reader learns to identify which Python is active and why the
   AI prefers `uv` plus a project-local `.venv`.
9. Chapter 8: the reader learns how the AI reads `requirements.txt` and
   `pyproject.toml` to know what the backend actually expects.
10. Chapter 9: the frontend cannot run because `node` is not available.
11. Chapter 10: Node exists, but the version is wrong, so `nvm` enters the
    story.
12. Chapter 11: `package.json` declares what is needed; `node_modules` is the
    downloaded local copy; `npm install` is how the AI fills that gap.
13. Chapter 12: the reader meets the class of problems that code AIs do not
    solve well: system diagnosis.
14. Chapter 13: Warp is introduced as the terminal tool for turning plain
    English into system commands the reader can inspect before running.
15. Chapter 14: Warp handles concrete workflows like finding a process on port
    3000, fixing PATH, and making an environment variable persistent.
16. Chapter 15: the reader learns the boundary line: code problems go to the
    AI coding tool; environment and machine-state problems go to Warp.
17. Conclusion: the reader leaves knowing how to recognize the shape of the
    problem before asking a tool to act.

## Canonical Names and Writing Rules

Use these names consistently:

- repo: `neighborhood-meals`
- backend package: `neighborhood_meals`
- frontend app: `neighborhood-meals-frontend`
- default branch: `main`
- feature branch: `feat/theme-switcher`
- remote: `origin`
- shell: `zsh`
- virtual environment folder: `backend/.venv`

Do not:

- rename the repo to a different example project
- switch between `master` and `main`
- switch between `frontend/` and `client/`
- invent Docker, PostgreSQL, Redis, CI, or deployment problems
- turn the scenario into a command-heavy tutorial

The book is about recognition. The AI coding tool usually performs the fix. The
reader's job is to recognize what class of problem they are looking at, notice
whether the output means success or failure, and avoid undoing the AI's work.

When useful, chapters may remind the reader that:

- `main` is for following the book's friction-facing workflow
- `reference-working` is the safety line for verifying whether a problem is
  environmental versus application-level

## Chapter State Log

State at the end of each phase:

- After Part 1: the reader understands local Git, GitHub, authorization,
  branches, worktrees, and how Git protects uncommitted changes.
- After Part 2: `backend/.venv` exists, Python 3.11 is active for the project,
  and the reader can recognize where dependency intent is declared.
- After Part 3: Node 20.11.1 is active, `frontend/node_modules` exists locally,
  and the frontend can start when the machine state is clean.
- After Part 4: the reader can separate code issues from system issues and can
  use Warp to diagnose ports, PATH, and shell persistence problems.

If a later issue needs the scenario to evolve, update this file first and note
the change explicitly in the run output. Silent drift is a bug.
