# Introduction

You cloned the project. You asked your AI coding tool to get it running. It wrote a setup script, installed some packages, maybe even edited a config file. You ran the command it gave you.

And then something broke. An error message you've never seen before. Something about a Python version, or a missing module, or a port that's already in use. You asked the AI to fix it. It gave you another command. You ran that one too. Now there are two error messages.

This is the wall. Not the code — you can write code. The wall is the layer underneath the code: the environment your code runs in. And when that layer breaks, your AI coding tool gets quieter, more circular, or more confidently wrong.

This book is about that layer.

---

## What You're Actually Looking At

The project you cloned lives in a folder on your machine. But it also depends on things that aren't in that folder: a specific version of Python, a collection of JavaScript packages, a set of access credentials for GitHub, a terminal shell with the right paths configured. When the project runs, it's not just running your code. It's running your code inside a specific environment. That environment either matches what the project expects, or it doesn't.

When it doesn't match, you get errors that have nothing to do with your code. Errors that say things like `command not found` or `module 'xyz' not found` or `ENOENT: no such file or directory`. These aren't bugs. They're mismatches. And the fix isn't writing better code — it's understanding what the environment is supposed to look like.

That's the thesis of this book: you don't need to be a sysadmin. You need to recognize what you're looking at.

Your AI coding tool is good at writing code. It can generate a function, refactor a class, write a test suite. What it wasn't designed to do — not alone, anyway — is understand your specific machine, your shell configuration, your credential store, the Python version you installed three months ago and forgot about. That context lives on your computer, not in the AI's context window. When something in the environment breaks, the AI can guess at it. But you're the one who knows what's actually there.

This book gives you the mental models to understand what's actually there.

---

## The Project

Throughout this book, you'll be working through a single scenario. You've cloned a project called `neighborhood-meals` — a small full-stack web app for managing community meal pickups. It has a Python backend and a JavaScript frontend.

```
neighborhood-meals/
  README.md
  backend/
    app.py
    pyproject.toml
    requirements.txt
  frontend/
    package.json
    src/
      App.jsx
```

The project doesn't run cleanly on the first try. That's intentional. The errors you hit in this scenario are the same category of errors you'll hit on real projects. Each part of the book is a wall: first git gets confusing, then the Python environment is wrong, then Node throws a version mismatch, then there's a system-level problem that requires a different tool entirely.

You're not memorizing solutions to these specific errors. You're building the mental map that lets you recognize what kind of problem you're looking at — and tell your AI what it actually needs to know to help.

---

## What Your AI Handles vs. What You Need to Own

Your AI coding tool is a code tool. It thinks in functions, files, and syntax. When you say "add a search feature" or "fix this bug," it knows what to do. That's its terrain.

The environment is different terrain. The environment is the operating system's concern, the shell's concern, the package manager's concern. It involves things like which version of a language runtime is active, how authentication tokens are stored, which directory your shell is currently pointed at. These are not code problems. They're infrastructure problems.

Your AI can often fix infrastructure problems when you describe them accurately. But here's the catch: to describe them accurately, you need to understand what you're looking at. If you just paste an error message and say "fix this," the AI is working blind. It might get lucky. It might send you down a path that fixes the symptom and breaks something else.

The division of responsibility in this book is: the AI runs the commands, but you know what the commands are doing. Not memorized — understood. There's a difference.

---

## What the Four Parts Cover

**Part 1: Git and GitHub**

Git is version control — it tracks changes to your code. GitHub is a hosting service where git repositories (folders tracked by git) live online. They're related but different, and the distinction matters when your AI is pushing changes, managing branches, or running into authentication errors.

Part 1 covers what git is tracking, what the common states of confusion look like, and how GitHub authentication works when your AI coding tool is doing the pushing. You'll hit this wall first with `neighborhood-meals`, before you even get the project running.

**Part 2: Python Environments**

Python has a problem: different projects often need different versions of Python or different sets of packages, and they can't all share the same installation without stepping on each other. The solution is isolated environments — separate containers of packages per project.

When your AI sets up a Python project, it's usually creating one of these environments. Part 2 explains what it's creating, why, and what goes wrong when the environment isn't active or isn't the right version.

**Part 3: Node and npm**

Node is a JavaScript runtime. npm is its package manager. The `frontend/` directory in `neighborhood-meals` runs on Node, and like Python, Node has a version problem: projects specify which version they expect, and if your machine has a different one, things break in confusing ways.

Part 3 covers how Node versions work, what npm is actually doing when it installs packages, and how to read the errors that come out of a Node version mismatch.

**Part 4: Warp for System-Level Problems**

There's a category of problem that sits below your AI coding tool's reach: things wrong with the shell configuration, the file system, running processes, or system permissions. Your AI coding tool can tell you what command to run. It can't always see what your system is doing.

Warp is a terminal designed for this kind of diagnostic work. Part 4 covers what Warp does that a standard terminal doesn't, and how to use it when your AI coding tool says "it should work" but it doesn't.

---

## What You Need Before You Start

You need a machine with Git, Python, and Node installed. You need an AI coding tool — Claude, Codex, Cursor, or similar. You don't need to know how to use any of them deeply. You don't need prior experience with virtual environments, package managers, or shell configuration.

If you can open a terminal and run a command when someone tells you what it is, you're ready.

---

## A Note on Commands

This book shows terminal commands. You are not expected to memorize them. When a command appears, the point is to understand what it's doing — not to write it down for later. Your AI will write the commands. Your job is to know whether the result is what you expected.

When something looks wrong, you'll know what question to ask. That's the skill.

---

Part 1 starts with the thing that confuses almost everyone who's new to working with an AI coding tool on a real project: git state, and what it means when the AI starts talking about branches and commits before you've even gotten the project running.
