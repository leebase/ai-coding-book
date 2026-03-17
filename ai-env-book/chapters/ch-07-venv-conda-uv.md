# Chapter 7: venv, conda, uv — Which One and Why

The AI created the virtual environment using a tool called `uv`. But you've also seen tutorials that show `python -m venv`. Someone on your team mentioned conda. A blog post you found recommended virtualenv. Are all of these the same thing? Do they produce different results? Can you mix them?

The short answer: they solve the same problem in different ways. You don't need to choose between them for `neighborhood-meals` — the AI already made that call. But you do need to know enough to recognize what you're looking at when the environment comes up in conversation, in documentation, or in a teammate's message.

---

## There Are Several Tools, and They All Create Rooms

The problem from Chapter 6 — each project needs its own isolated Python with its own packages — has been around since Python's early days. Several tools were built to solve it. They all create that private room, but they differ in how much they do, how fast they are, and what kinds of projects they're built for.

Here are the three you'll encounter most often.

---

## python -m venv

`python -m venv` is built into Python. Starting with Python 3.3, every Python installation includes it. You don't install it separately; it comes along for the ride.

When you run `python -m venv .venv`, it creates a `.venv` folder with a self-contained Python interpreter and an empty library shelf. Nothing else. It doesn't read your `pyproject.toml`. It doesn't know what packages you need. It just creates the room. You then install packages separately with `pip`.

This minimalism is its strength and its limitation. It's predictable, well-documented, and works anywhere Python is installed. It's also slower and more manual than newer alternatives. You're doing two steps — create the environment, then install packages — and you manage Python versions separately.

You'll see this tool in older tutorials and many official Python documentation pages. If you're reading something that shows `python -m venv`, that's this tool.

---

## conda

`conda` comes from the Anaconda distribution, which was built for data science and scientific computing. It's different from the others in an important way: it manages Python versions directly, not just packages.

With `python -m venv` and `uv`, you need to have the right Python version installed on your machine before creating the environment. `conda` can fetch and install different Python versions as part of creating an environment. It also manages packages that aren't Python packages at all — system-level libraries that scientific tools sometimes depend on.

This makes `conda` powerful and popular in machine learning and data analysis work, where projects often depend on tools like NumPy, CUDA, or TensorFlow that have complicated non-Python dependencies. For a web backend like `neighborhood-meals`, that extra machinery isn't needed.

`conda` environments are also not typically placed inside the project folder as `.venv`. They live in a central location managed by Anaconda, and you switch between them by name rather than by directory. If a teammate says "activate the base environment" or mentions `conda activate`, this is the tool they're using.

---

## uv

`uv` is newer than both of the above. It was released in 2024 and written in Rust, which is partly why it's fast — environment creation and package installation that takes seconds in `pip` can happen in milliseconds in `uv`.

More importantly for a project like `neighborhood-meals`: `uv` is project-aware. When you run `uv venv .venv` and then `uv pip install -e .`, it reads the project's `pyproject.toml` to understand what packages are needed and what Python version is required. It also creates the environment inside the project folder as `.venv`, which keeps everything local and self-contained.

`uv` is what modern Python projects are moving toward. It's faster, it handles both environment creation and package installation in a unified workflow, and it natively reads the `pyproject.toml` format that newer projects use to declare their dependencies.

---

## Why the AI Used uv for neighborhood-meals

The backend has a `pyproject.toml` that declares its dependencies and Python version requirement. `uv` reads that file natively. Creating the environment and installing the right packages is a single coherent workflow.

Using `python -m venv` would have required the AI to create the environment first, then separately figure out what to install and run `pip install` for each dependency. Using `conda` would have been heavier than the project needs and would have placed the environment outside the project folder, making it harder to keep the project self-contained.

`uv` is the right fit for a web backend with a `pyproject.toml`. That's the call the AI made.

> **Key Takeaway:** The tool used to create the environment doesn't change what a virtual environment is. All three tools make a private room for the project. They differ in speed, scope, and how much they handle automatically. For `neighborhood-meals`, `uv` is the right choice because the project already has a `pyproject.toml` and doesn't need the data-science machinery that `conda` brings.

---

## How to Tell Whether the Environment Is Active

Once the virtual environment is set up, you need to know whether it's actually being used when you run a command. The signal for this is in the terminal prompt itself.

When a virtual environment is active, your prompt changes. Where it previously showed something like:

```
you@machine neighborhood-meals %
```

It now shows:

```
(.venv) you@machine neighborhood-meals %
```

That `(.venv)` prefix is confirmation. It means the terminal is currently pointing at the Python and packages inside `backend/.venv`. When you — or the AI — runs a Python command, it uses that environment.

The name in parentheses matches the name of the environment directory. If the virtual environment had been named `backend` instead of `.venv`, the prefix would say `(backend)`. The prefix is just the folder name.

> **Watch For:**
> When the AI activates the environment, it runs:
> ```
> source backend/.venv/bin/activate
> ```
> The prefix appearing in the prompt is how you confirm activation worked. No prefix means the environment is not active.

---

## What "Activated" Actually Means

The prefix isn't cosmetic. When a virtual environment is activated, the terminal rewires one specific thing: which Python binary it uses.

Your machine has a Python installed somewhere in a system folder. Your terminal finds it by looking through a list of directories — your PATH — until it finds a program named `python`. Normally that's the system Python.

Activation inserts the environment's directory at the front of that list. Now when the terminal looks for `python`, it finds the one inside `.venv` first, before it ever gets to the system Python. Everything you run in that terminal session — every Python command, every package — goes through the environment's Python until you close the session or explicitly deactivate.

You don't need to manage this list yourself. You just need to know that the prefix tells you whether the rewiring happened.

---

## The Environment Doesn't Survive a New Terminal

This is where people get caught. The virtual environment is activated for a session — one terminal window, one shell session. When you close that terminal and open a new one, the activation is gone. The new terminal starts fresh with the system Python.

If the backend was working yesterday and today `ModuleNotFoundError` is back, this is probably why. Nothing broke. The environment still exists on disk. It just isn't active in the new terminal.

> **Don't Do This:** Do not reinstall the entire environment because the error came back. Check whether the prefix is visible in your prompt first. If it isn't, the fix is reactivation, not rebuilding from scratch.

---

## What You Own

The AI handles which tool to use and how to activate the environment. You own one thing: noticing whether the prefix is there.

If you open a new terminal and start working, check the prompt before you ask the AI to run the backend. If `(.venv)` is missing, tell the AI. It will activate the environment before running anything. That takes a second and prevents a cascade of errors.

If the prefix disappears mid-session — which can happen if something resets the shell — the same applies. Mention it. The AI will re-activate.

The rest of the environment management is not your job. The AI knows which commands to run, which tool to use for this project, and how to recover if something is broken. Your job is to report what you see.

---

The AI knows which tool to use — but it also needs to know what to install, and that's recorded in two files the backend carries around.
