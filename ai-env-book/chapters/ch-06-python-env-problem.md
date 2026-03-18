# Chapter 6: Why Python Has an Environment Problem

You cloned `neighborhood-meals`. Git is sorted. Now you want to run the backend. You ask the AI to start it, and it tries `python backend/app.py`. This comes back immediately:

```
Traceback (most recent call last):
  File "/Users/you/code/neighborhood-meals/backend/app.py", line 1, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
```

Python is installed on your machine. You can run `python --version` and get an answer. So why doesn't it work?

The error isn't telling you Python is missing. It's telling you that Flask — the library the backend is built on — isn't available to the Python that just ran. Those are two different things.

---

## Python Is Installed, But That's Not Enough

When you install Python on your machine, you get a Python interpreter. That's the program that reads and runs Python code. It comes with a small set of built-in tools. It does not come with Flask, or SQLAlchemy, or any of the libraries that `neighborhood-meals` needs to function.

Libraries get installed separately. When you install a library, it gets placed somewhere on your machine — a folder that the Python interpreter looks in when your code says `from flask import Flask`. If Flask isn't in that folder, you get the error above.

Here's the part that trips people up: Python can be installed in multiple places on the same machine, and each installation has its own separate folder of libraries. Running `python backend/app.py` uses whichever Python your terminal found first. That search list is part of your PATH — the list of places your shell checks when you type a command. That Python might not be the one with Flask installed. Or more precisely, it probably isn't — because Flask hasn't been installed anywhere yet for this project.

That's the problem. Not that Python is missing. Not that Flask doesn't exist. It's that this project's libraries haven't been installed into an isolated space that this project uses.

---

## The Mental Model: Rooms

Think of each Python environment as a room. The room has its own Python interpreter and its own set of packages on the shelves. When your code runs, it runs inside one specific room. If Flask isn't on the shelves in that room, the code can't find it — even if Flask is sitting in a completely different room down the hall.

Right now, `neighborhood-meals` doesn't have a room. When the AI tried to run `backend/app.py`, Python went looking for Flask in whatever generic room the terminal happened to be using. Flask wasn't there. Hence the error.

The fix isn't to install Flask globally — that is, into the default room every Python program shares. That approach breaks eventually. If one project needs Flask 2.x and another needs Flask 3.x, they can't share the same room. They'll conflict.

The fix is to build `neighborhood-meals` its own room. In Python, that room is called a virtual environment.

---

## Why Projects Need Their Own Rooms

Picture two projects on the same machine. Project A is an older app that depends on Flask 2.3. Project B is `neighborhood-meals`, which needs Flask 3.0. If you install both into the global Python, one overwrites the other. Both can't be the current version simultaneously.

Virtual environments solve this by giving each project a private folder — usually named `.venv` — that contains its own copy of an interpreter and its own library shelves. Project A's `.venv` has Flask 2.3. Project B's `.venv` has Flask 3.0. They don't know about each other. They can't conflict.

This is the reason Python environments exist. Not because someone wanted to make things complicated, but because real projects live on machines with real constraints and real version disagreements.

---

## What the AI Does

When the AI sees that `ModuleNotFoundError`, it doesn't just try to install Flask. It first checks whether the project has a virtual environment set up at all.

> **What the AI Does:**
> The AI checks for `backend/.venv`. That directory doesn't exist yet. So it creates the virtual environment first, then installs the project's dependencies into it.
>
> The commands look like this:
> ```
> cd backend
> uv venv .venv
> uv pip install -e .
> ```
>
> You'll see output like:
> ```
> Using Python 3.11.8
> Creating virtual environment at: .venv
> Resolved 12 packages in 0.4s
> Installed 12 packages in 1.2s
>  + flask==3.0.3
>  + werkzeug==3.0.2
>  ...
> ```

The `uv venv .venv` command creates the room. The `uv pip install -e .` command reads the project's package list and puts the right libraries on the shelves. After this, `backend/.venv` exists on disk, and Flask is inside it.

The next time you run the backend, Python will use that room. The error will be gone.

> **Watch For:**
> The line `Creating virtual environment at: .venv` confirms the room was built. The list of installed packages confirms the shelves were stocked. If you see those, the setup succeeded.

---

## What "Activation" Actually Changes

You'll often see one more step after the environment is created:

```
source .venv/bin/activate
```

This is the part that feels abstract until someone names it plainly. Activating the environment changes which Python your current shell reaches for by default. Before activation, typing `python` might mean the system Python, or a Homebrew Python, or whatever interpreter your shell finds first on PATH. After activation, typing `python` means the interpreter inside `backend/.venv`.

Nothing magical happened to Python itself. Your shell just changed which room it walks into first.

That's why activation is session-scoped. Open a new terminal and the shell starts over with its normal PATH. The environment isn't "broken" — it's just no longer the default for that new session until the AI activates it again. Once you see activation as a shell-state change rather than a Python concept, the behavior stops feeling random.

---

## The Other Wall: Wrong Python Version

Sometimes the error isn't about a missing library. Sometimes the AI runs the install step and you get this instead:

```
ERROR: Package 'neighborhood-meals-backend' requires a different Python: 3.9.6 not in '>=3.11'
```

This is a different problem. The library isn't missing — the Python version itself is wrong. The project was written for Python 3.11 or newer, and the machine's default Python is 3.9.6.

This happens because macOS ships with an older Python. Your terminal found that one first. You're not in the right room — you're not even using the right building.

The AI will look for Python 3.11 on the machine. If it's installed somewhere (via Homebrew, pyenv, or similar), it will use that. If it isn't, it will prompt you to install it. Either way, the virtual environment needs to be built with the correct Python version before any packages get installed.

> **Watch For:**
> Once this is resolved, the setup output will say `Using Python 3.11.x` rather than `3.9.x`. That's the confirmation that the right Python is running.

---

## What You Own

The AI created `backend/.venv`. You don't need to understand its internals, and you shouldn't need to touch it. But there are two things that will break the setup if you do them:

**Don't delete `backend/.venv`.** It's a generated folder — nothing in it was handwritten, and nothing irreplaceable lives there. But deleting it means the next time you run the backend, Python goes back to the wrong room. The AI can recreate it, but only if you ask, and only if you know that's what broke.

**Don't run Python commands from outside the project's virtual environment accidentally.** If you open a new terminal window and run a Python command without the environment active, you're back in the generic room. The error returns. You'll know this happened if the `ModuleNotFoundError` shows up again on a project that was previously working.

There's a subtle version of this mistake that's worth naming. You see the backend running correctly in one terminal, open another terminal to test something, run `python backend/app.py`, and assume it should work the same way because it's the same project on the same machine. But shells don't share state. The first terminal had the environment active. The second one doesn't. Same repo, different room.

> **Don't Do This:** Do not install Flask or any other library globally with `pip install flask` to make the error go away faster. A global install can mask the problem temporarily, but it doesn't set up the project correctly. The next time someone else clones the project, or you set up a new machine, the install step will fail in the same way.

The reason the global install feels tempting is that it can appear to work immediately. The import error disappears, which makes it feel like the diagnosis was correct. But what you actually did was put Flask on the generic shelf instead of the project shelf. The backend might start, but you've taught yourself the wrong lesson about what the project needs. The next project with different dependencies collides with it, and now the machine feels inconsistent again.

> **Key Takeaway:** "Python is installed" and "this project's packages are installed" are two different conditions. A virtual environment is what connects them — it's the private room where this project's dependencies live.

---

Now you know what a virtual environment is — but you may have noticed there are several tools that create them, and the AI chose one called `uv`. That choice matters.
