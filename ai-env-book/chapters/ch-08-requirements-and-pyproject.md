# Chapter 8: Reading requirements.txt and pyproject.toml

Before the AI installs anything into the virtual environment, it opens two files: `backend/requirements.txt` and `backend/pyproject.toml`. It reads them first. It doesn't just run `pip install flask` and call it done.

If you've watched the AI work, you may have seen it open these files without explanation and then move straight into the install step. This chapter explains what those files say, why they both exist in the same project, and what can go wrong if you edit them without understanding what they declare.

---

## The Packing List

Before a project can run, someone has to tell the installer what to install. These two files do that. Think of them as a packing list: before the AI stocks the shelves in the virtual environment, it checks the list to know what belongs there.

Without these files, the AI would have to guess — or you would have to tell it every package by hand each time. Neither is sustainable. The packing list is how the project carries its own requirements, so that anyone who clones it (you, a teammate, a deployment server) can set up the same environment.

---

## requirements.txt

`requirements.txt` is the older of the two formats. It's been the default way to list Python dependencies for over a decade. You'll find it in almost every Python project that predates 2022 or so, and still in many that are more recent.

The format is a flat list. Each line is a package name, usually with a version constraint:

```
flask==3.0.0
sqlalchemy>=2.0.0
python-dotenv>=1.0.0
```

The `==` operator means exactly this version. `flask==3.0.0` tells the installer to get Flask 3.0.0 specifically — not 3.0.1, not 3.1.0. This is useful for production projects where you want to make sure every machine installs the exact same version.

The `>=` operator means this version or newer. `sqlalchemy>=2.0.0` tells the installer to get SQLAlchemy 2.0.0 or any later release that satisfies the constraint. This gives more flexibility but less precision.

`requirements.txt` is readable without any special tools. You can open it in any text editor and see exactly what the project needs. That's part of why it became so widely used — it's simple, flat, and self-explanatory.

Its limitation is equally simple: it only knows about packages. It doesn't know what Python version the project needs. It doesn't declare the project's name, its version, or how to build it. It's a list of packages and nothing more.

---

## pyproject.toml

`pyproject.toml` is the newer standard, introduced to replace the patchwork of older configuration formats that Python projects accumulated over the years. It's richer than `requirements.txt` because it holds more than just the package list.

Open `backend/pyproject.toml` and you'll see something like this:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "neighborhood-meals-backend"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "flask>=3.0.0",
    "sqlalchemy>=2.0.0",
    "python-dotenv>=1.0.0",
]
```

The `[project]` section is where the core information lives. The `name` and `version` fields identify the project. The `requires-python` field is critical — it declares the minimum Python version the project was designed for. The `dependencies` list is the equivalent of what lives in `requirements.txt`.

That `requires-python = ">=3.11"` line is not advisory. It's a constraint the installer checks before it installs anything. If the virtual environment was built with Python 3.9, the installer sees that `3.9.6 not in '>=3.11'` and stops. That's the exact error from Chapter 6. The constraint is what triggers it.

`pyproject.toml` also carries configuration for development tools — linters, formatters, test runners — in additional sections. It's the single file modern Python projects use for project-level configuration. `uv` reads it natively, which is one reason the AI prefers `uv` for projects that have it.

---

## Why This Project Has Both

If you look at the `backend/` folder, you'll find both files sitting there. That might seem redundant. It isn't a mistake.

`neighborhood-meals` is in transition. It started with `requirements.txt` as its dependency list, which is how almost all Python projects started. At some point the project added `pyproject.toml` to adopt the newer standard and to declare the Python version requirement. But the `requirements.txt` was left in place because older documentation, scripts, and notes still referenced it.

This coexistence is common. It happens on real projects when teams migrate from one tooling convention to another. Both files are valid. They describe similar things in different formats. The authoritative source for what to install is now `pyproject.toml`, but `requirements.txt` hasn't been deleted because removing it would break any process that still reads it.

When the AI runs the install step, it uses `uv pip install -e .`, which tells `uv` to read `pyproject.toml` as the source of truth. If something reads `requirements.txt` instead — an older script, a teammate's manual install command — it will install from that list. The two files should stay in sync. In `neighborhood-meals`, they do.

> **Key Takeaway:** Having both files isn't a problem to fix. It's the project in the middle of a migration. The AI knows to read `pyproject.toml` with `uv`. If you see documentation that shows `pip install -r requirements.txt`, that's the older approach working from the older file. Both work; they just serve different toolchains.

---

## What Version Constraints Actually Enforce

The version constraints in these files aren't just documentation. They're instructions the installer checks before it acts.

`flask>=3.0.0` tells the installer: any version of Flask from 3.0.0 onward is acceptable. If Flask 3.1.0 is the latest release when you install, that's what you'll get. This is useful for libraries that follow good release practices — newer patch and minor versions are generally safe.

`flask==3.0.0` pins the version precisely. You'll get exactly 3.0.0 regardless of what newer versions are available. This is useful when you want full reproducibility — every developer and every server installs the exact same thing.

`requires-python = ">=3.11"` is the version constraint for Python itself. The project was written for Python 3.11 and relies on language features or library behaviors that exist in 3.11 but not in older versions. A machine running Python 3.9 doesn't meet that constraint. The installer stops and tells you so.

This is where the wrong-interpreter error comes from. When the system Python is too old, the install fails before any packages get added, because the constraint check happens first.

---

## What the AI Does With These Files

The AI doesn't guess at dependencies. Before it installs anything, it reads these files to understand what the backend actually expects.

> **What the AI Does:**
> After creating the virtual environment, the AI runs:
> ```
> uv pip install -e .
> ```
> This tells `uv` to install the current project in editable mode. `uv` reads `pyproject.toml`, checks the `requires-python` constraint against the environment's Python version, then resolves and installs every package in the `dependencies` list.
>
> You'll see output like:
> ```
> Resolved 12 packages in 0.3s
> Installed 12 packages in 0.9s
>  + flask==3.0.3
>  + sqlalchemy==2.0.29
>  + python-dotenv==1.0.1
>  ...
> ```

The packages listed in the output correspond to what `pyproject.toml` declared. If the constraint check passes and all packages resolve, the environment is ready. The AI is not improvising — it's executing the packing list.

> **Watch For:**
> The line `Resolved N packages in X.Xs` tells you `uv` successfully read the dependency declarations and found a compatible set. `Installed N packages` tells you they were placed in the virtual environment. Both lines appearing without errors means the install succeeded.

---

## What You Own

The AI manages the install. You own the files the AI reads.

`requirements.txt` and `pyproject.toml` are the source of truth for what the project needs. If you add a new package to `pyproject.toml` correctly, the AI will install it on the next setup. If you add it incorrectly — wrong field name, broken TOML syntax, incompatible version constraint — the install step fails.

> **Don't Do This:** Do not add a package to `pyproject.toml` by guessing at the format. If you need to add a dependency, ask the AI to do it. It knows the correct section (`[project.dependencies]`), the correct syntax, and whether the package name you have in mind is what's actually published on PyPI.

> **Don't Do This:** Do not edit `requirements.txt` to add a package you installed manually with `pip install` without also updating `pyproject.toml`. The two files should describe the same set of dependencies. A package in one but not the other creates drift — the project behaves differently depending on which file the installer reads.

The other thing you own is context. You know, now, that this project has both files for historical reasons. If a teammate tells you to run `pip install -r requirements.txt` and you do that from outside the virtual environment, you'll install packages into the wrong room. The mental model from Chapter 6 applies here: the right packing list, installed into the right room.

---

With the backend dependencies installed and the right Python running, the frontend is next — and it has its own runtime, its own version problem, and its own package list.
