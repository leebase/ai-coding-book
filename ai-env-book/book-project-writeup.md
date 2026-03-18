# neighborhood-meals Book Project Write-Up

Repository URL: `https://github.com/leebase/neighborhood-meals.git`

## What This Project Is

`neighborhood-meals` is the companion repository for Lee Harrington's book *Your Dev Environment: A Guide for AI-Assisted Developers*.

It is a deliberately small full-stack web app for managing community meal pickups:

- Neighbors can post available meals.
- Other neighbors can claim those meals for pickup.
- The app is simple on purpose so the book can focus on environment setup, tooling, workflow, and debugging instead of product complexity.

This repository is not just an example app. It is also a teaching tool. Some parts of the setup experience are intentionally left rough on the book-facing branch so readers encounter realistic development problems and learn how to resolve them.

## Repository URL and Branch Model

Canonical remote:

- `origin` -> `https://github.com/leebase/neighborhood-meals.git`

Canonical branches:

- `main`: the book-facing branch. It preserves intentional setup and workflow friction while keeping the underlying application logic correct.
- `reference-working`: the known-good runnable baseline. Use this branch when the goal is to confirm the app works end to end without wondering whether the current state is intentionally unfinished.
- `feat/theme-switcher`: the workflow-support branch used for branch and worktree examples in the book.

Canonical worktree example:

- sibling path: `../neighborhood-meals-theme-switcher`

## What the Books Should Explain Clearly

The books should make these points explicit:

- This repo contains a real backend and frontend, not a toy single-file example.
- The app logic is intended to be correct once the environment is configured properly.
- Some failures on `main` are deliberate teaching moments, not accidental defects.
- `reference-working` exists as the safety line when a reader needs to compare against a known-good baseline.
- The friction belongs in environment setup, dependency management, Git workflow, and machine state, not in the core app behavior.

The books should also tell the reader when to use each branch:

- Use `main` when following the book's workflow and learning from setup/debugging friction.
- Use `reference-working` when verifying whether a problem is environmental versus application-level.

## Application Shape

The app is a minimal full-stack system:

- Backend: Flask API in `backend/`
- Frontend: React/Vite app in `frontend/`
- Root: documentation, project memory, planning artifacts, and lightweight repo metadata

The root should not be described as the primary runtime surface. The real runtime entrypoints are:

- backend server: `backend/app.py`
- frontend scripts: `frontend/package.json`

## Core User Story

The books should describe the product simply:

- Someone in the neighborhood has extra food.
- They post a meal with a title.
- Another neighbor sees it and claims it.

That is enough functionality to justify a real stack without hiding the learning objective behind domain complexity.

## Canonical Tech Stack

- Python 3.11+
- Flask 3.x
- `flask-cors`
- Node 20.11+
- React 18
- Vite 5
- Python package management with `uv`
- Node package management with `npm`
- Canonical shell context: `zsh` on macOS

## Canonical Repo Layout

```text
neighborhood-meals/
  README.md
  .gitignore
  AGENTS.md
  architecture.md
  backend/
    app.py
    pyproject.toml
    requirements.txt
    neighborhood_meals/
      __init__.py
      routes.py
  frontend/
    index.html
    package.json
    package-lock.json
    vite.config.mjs
    src/
      App.jsx
      main.jsx
      styles.css
  src/
    neighborhood-meals/
      __init__.py
      main.py
  tests/
    test_backend.py
```

## Non-Negotiable Conventions

The books should call these out because examples depend on them:

- Python package name: `neighborhood_meals`
- Frontend package name: `neighborhood-meals-frontend`
- Backend virtual environment location: `backend/.venv`
- Backend port: `8000`
- Frontend port: `3000`
- Remote name: `origin`
- Default branch: `main`
- Workflow example branch: `feat/theme-switcher`

The books should also note what must not be committed:

- `backend/.venv/`
- `frontend/node_modules/`
- generated caches and local machine artifacts

## Backend Behavior

The backend is intentionally small and in-memory. No database is required.

Primary API surface:

- `GET /health`
- `GET /api/meals`
- `POST /api/meals`
- `POST /api/meals/<id>/claim`

Canonical meal shape:

```python
{
  "id": 1,
  "title": "Chicken soup - 4 servings",
  "posted_by": "Apartment 4B",
  "claimed": False
}
```

Important implementation notes for the books:

- data is stored in a module-level list
- the point is to prove the backend can run and respond
- persistence is intentionally out of scope

## Frontend Behavior

The frontend is a single-page React app.

It should:

- fetch meals from the backend
- show the list of available meals
- let a user post a new meal title
- let a user claim a meal

The books should emphasize what it does not need:

- no routing library
- no global state library
- no backend auth
- no database UI complexity

The goal is a minimal but real browser app that exercises the frontend toolchain and talks to a live API.

## Setup Instructions the Books Should Give

### Backend

```bash
cd backend
uv venv --python 3.11 .venv
uv pip install -e .
./.venv/bin/python app.py
```

Expected backend URL:

- `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Expected frontend URL:

- `http://localhost:3000`

## Intentional Friction the Books Should Teach

The books should explain that `main` is designed to naturally produce certain setup and workflow failures.

### Git and workflow friction

Examples the books can rely on:

- `fatal: not a git repository` when commands are run outside the repo
- GitHub authentication or SSH setup failures on a new machine
- worktree and branch conflicts around `feat/theme-switcher`
- checkout failures caused by local changes

These are mostly machine-state or workflow problems, not code problems.

### Python environment friction

Examples the books should cover:

- `ModuleNotFoundError: No module named 'flask'` if the user runs the backend before installing dependencies
- Python version mismatch when the user is on Python 3.9 instead of 3.11+

Load-bearing repo expectation:

- `backend/.venv/` must stay uncommitted

### Node and npm friction

Examples the books should cover:

- `zsh: command not found: node`
- unsupported engine errors if the machine is on an older Node release
- `vite` missing before `npm install`

Load-bearing repo expectation:

- `frontend/node_modules/` must stay uncommitted

### System-level friction

Examples the books can discuss:

- port conflicts on `3000`
- missing CLI tools on `PATH`
- shell configuration changes that do not persist across sessions

## Why Both `pyproject.toml` and `requirements.txt` Exist

The books should explain this directly instead of treating it as a mistake.

- `backend/pyproject.toml` is the authoritative modern dependency declaration.
- `backend/requirements.txt` remains intentionally present as a legacy artifact the book can discuss during toolchain transition examples.

The reader should not be told to delete `requirements.txt` casually, because its presence is part of the teaching material.

## What Must Stay Stable for the Books

If the repo changes, the books should either be updated or these details should stay fixed:

- branch names
- port numbers
- endpoint names
- package names
- directory names
- the existence of both backend and frontend
- the existence of `reference-working`
- the existence of `feat/theme-switcher`
- the intentional non-commit of `.venv` and `node_modules`

## Verification the Books Can Reference

At a minimum, the books should describe these verification points:

- backend tests pass from `tests/test_backend.py`
- the backend returns `{"status": "ok"}` from `/health`
- the frontend production build succeeds
- the meal post/list/claim flow works

## Current Practical Status

As of 2026-03-17, the repository has been verified locally to the extent possible in the current environment:

- backend tests pass
- frontend build succeeds
- Git metadata and checkout health have been repaired on the current machine
- the Flask API behavior has been verified through the Flask test client

If a book mentions the current validated state, it should present `reference-working` as the clean runnable baseline and `main` as the teaching branch with intentional friction.

## Recommended Book Framing

A concise way for the books to frame this project:

> `neighborhood-meals` is a deliberately small full-stack teaching application. Its job is not to impress with product scope. Its job is to create a realistic development environment in which an AI-assisted developer must handle Git, Python, Node, shells, ports, package managers, and branch workflow correctly. The app should work once the environment is correct, and the repository gives the reader both a friction-facing branch (`main`) and a known-good baseline (`reference-working`) so they can learn without losing their footing.
