# Chapter 9: What Node Is (and Why It's on Your Machine)

The backend is running. The Python environment is set up, `backend/.venv` exists, and the AI was able to start the Flask server without complaint. Now you want to run the frontend.

You ask the AI to start it. It tries to check the environment first, and this comes back:

```
zsh: command not found: node
```

The AI was looking for Node before it could do anything with the frontend. The shell doesn't know what Node is. Or more precisely: the shell can't find a program called `node` anywhere it knows to look.

This is not a code problem. It's a runtime problem. And understanding what Node is — and why it needs to exist on your machine — is what makes the rest of Part 3 make sense.

---

## What Node Actually Is

Node is a JavaScript runtime. That's the precise description, and it's worth knowing what it means.

JavaScript was originally designed to run inside web browsers. A browser can open a `.js` file and execute it — that's been true since the late 1990s. But JavaScript couldn't run on its own, outside a browser, on your machine. You couldn't run a JavaScript file from the command line the same way you can run `python script.py`.

Node changed that. Released in 2009, it took the JavaScript engine from Google's Chrome browser and made it available as a standalone program. Now JavaScript can run on your machine, directly, without a browser in the middle. That's what a runtime is: the program that executes code. Python is a runtime for Python code. Node is a runtime for JavaScript code.

The `neighborhood-meals` frontend is a JavaScript application. It uses a framework called React, written in JavaScript and JSX (JavaScript with HTML-like syntax mixed in). Running that app — even just for local development — requires a JavaScript runtime. That runtime is Node.

When you ask the AI to start the frontend dev server, it needs Node to exist on your machine. When the shell says `command not found: node`, it means that requirement isn't met.

---

## Why Node Lives on Developer Machines

You might expect that a frontend app runs in the browser, so why would you need Node on your development machine at all? The browser handles JavaScript — shouldn't that be enough?

It's enough for running the finished app. It's not enough for building and developing it.

Modern frontend development involves a build step. Your source files — the `.jsx` files in `frontend/src/` — get processed, bundled, and transformed before the browser sees them. Tools do that processing. Those tools are JavaScript programs. They need Node to run.

The development server — the program that lets you open `localhost:3000` in your browser and see the app — is also a JavaScript program. Same situation.

This is why Node ends up on machines that have nothing to do with writing JavaScript. A Python developer building a full-stack app still needs Node for the frontend build pipeline. A data scientist publishing a documentation site may need it for the static site generator. The JavaScript tooling ecosystem runs on Node, and that ecosystem has become part of how a lot of development infrastructure works.

For you, working on `neighborhood-meals`, the requirement is direct: the frontend tooling runs on Node, so Node has to be there.

---

## What "Command Not Found" Actually Means

When the shell says `command not found: node`, it's being specific about the problem. It's not saying Node is broken. It's saying the shell can't locate it.

The shell finds programs by looking through a list of directories called the PATH. When you type `node`, the shell checks each directory in that list for a file named `node`. If it finds one, it runs it. If it doesn't find one in any of the listed directories, you get `command not found`.

This means there are two possible situations:

**Node isn't installed.** There's no `node` binary anywhere on the machine. This is the clean case — the AI knows exactly what to do.

**Node is installed, but the shell can't see it.** Node exists in a directory that isn't in the PATH. This happens more than you'd expect. Some Node installation methods put the binary in a non-standard location, or the PATH entry that points to it hasn't been added to the shell configuration. The AI checks both possibilities.

Either way, the AI's starting point is the same: verify whether Node is present at all.

> **What the AI Does:**
> The AI runs `node --version` to check whether Node is available and, if so, which version is active.
>
> ```
> node --version
> ```
>
> If Node is missing entirely, the response is:
> ```
> zsh: command not found: node
> ```
>
> That confirms the situation. The AI will proceed to install Node using nvm (Node Version Manager).

---

## Node and npm Are Different Things

Before going further, this distinction matters: Node and npm are not the same program, even though they're installed together.

**Node** is the JavaScript runtime. It executes JavaScript code.

**npm** is the package manager for JavaScript. It handles downloading and managing libraries — the same role that pip plays for Python. npm stands for Node Package Manager, and it ships bundled with Node. When you install Node, you get npm too.

You'll see both names in the AI's output. You'll see `node --version` checks and `npm install` commands in the same session. They're related tools, but they do different things. Node runs code. npm manages the libraries that code depends on.

The analogy to Python is close: Node is to JavaScript as Python is to Python code. npm is to JavaScript libraries as pip is to Python packages. The tools are parallel in concept, different in detail.

---

## How the AI Installs Node

When Node is missing, the AI doesn't install it the way you might install most software — by downloading an installer, running it, and hoping for the best. It uses nvm.

nvm stands for Node Version Manager. Chapter 10 covers it in depth. For now, what matters is that nvm is the standard tool for managing Node installations, and using it rather than a direct installer is intentional. Projects often require specific Node versions. nvm makes it possible to install multiple versions and switch between them. If the AI installs Node directly without nvm, version management becomes harder later.

> **What the AI Does:**
> If nvm is already installed on the machine, the AI checks the project's Node version requirement and installs the right version:
>
> ```
> nvm install 20.11.1
> nvm use 20.11.1
> ```
>
> You'll see output like:
> ```
> Downloading and installing node v20.11.1...
> Now using node v20.11.1 (npm v10.2.4)
> ```
>
> If nvm itself is not installed, the AI will install it first before installing Node. That's a longer process, but the output is still readable: you'll see nvm's install script complete, then the Node install.

> **Watch For:**
> After the install, `node --version` should return `v20.11.1`. That confirms the runtime is present and the PATH is configured correctly. If you see a version number, Node is ready.

---

## Why This Is the Frontend's Version of the Python Problem

You saw something similar in Part 2. The Python error — `ModuleNotFoundError: No module named 'flask'` — wasn't about Python being missing. It was about the right environment not being set up.

The Node situation has the same shape. The shell returned `command not found: node` not because JavaScript doesn't work, but because the runtime that JavaScript needs for local development wasn't in place.

The fix is the same kind of fix: establish the runtime, then proceed. In Python, that meant creating a virtual environment with the right interpreter. In Node, it means getting the right version of Node active on the machine.

What's slightly different is the version layer. With Python, the machine often had some Python installed — just the wrong version. With Node, the machine might have nothing at all. Both cases look like "command not found" from the outside. The AI distinguishes between them by checking what's installed before deciding what to do.

---

## What You Own

The AI handles the install. You own knowing what you're looking at when the error happens again.

If you open a new terminal and try to do something with the frontend and see `command not found: node`, your first question should not be "did I break something?" It should be: "is Node active in this terminal?" There are reasons it might not be, and Chapter 10 explains the main one.

> **Don't Do This:** Do not install Node by downloading the package from nodejs.org and running it directly, even if it looks like the easiest path. That method can work, but it puts Node in a location that conflicts with nvm's version management. Once the AI switches to nvm-managed Node, you can end up with two Node installations that fight for the PATH. Let the AI choose the installation method.

> **Key Takeaway:** `zsh: command not found: node` is a runtime missing problem, not a code problem. Node is the JavaScript runtime the frontend tooling needs. The AI installs it via nvm. Once `node --version` returns a version number, that wall is down.

---

Node exists on the machine now — but the version the project requires might not be the version currently active, and that's what the next chapter is about.
