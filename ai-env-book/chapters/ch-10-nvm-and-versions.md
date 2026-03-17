# Chapter 10: nvm and Node Versions

Node is on the machine. The AI verified that with `node --version`. So it proceeds to the next step: installing the frontend's dependencies. It runs:

```
npm install
```

And gets this:

```
npm ERR! code EBADENGINE
npm ERR! engine Unsupported engine
npm ERR! engine Not compatible with your version of node/npm: neighborhood-meals-frontend@0.1.0
npm ERR! notsup Not compatible with your version of node/npm: neighborhood-meals-frontend@0.1.0
npm ERR! notsup Required: {"node":">=20.11.0"}
npm ERR! notsup Actual:   {"npm":"10.2.4","node":"18.19.0"}
```

Node is installed. npm is installed. The install command still failed.

The error is precise: the project requires Node `>=20.11.0`. The machine has Node `18.19.0`. Those two things don't satisfy each other, and npm stopped before it could install anything.

This is not a broken installation. It's a version mismatch. And it leads directly to the concept that makes Node version management make sense.

---

## Why Node Projects Pin to Versions

With Python, you might have one Python on your machine for years and it mostly works across projects. Node has more of a versioning culture. Projects tend to be specific about which Node version they expect, and for good reason.

Node releases follow a predictable cycle. Even-numbered versions (16, 18, 20) become Long-Term Support (LTS) releases — the ones that get security patches and bug fixes for several years. New JavaScript language features, new built-in APIs, and new npm behaviors land in different major versions. A project that was built and tested against Node 20 may use features or behaviors that don't exist in Node 18.

The `neighborhood-meals` frontend requires `>=20.11.0`. That's not arbitrary. The project's dependencies, build tools, and possibly some code itself depend on things that exist in Node 20 and not before. The npm engine check is enforcing that requirement before it installs anything that might fail at runtime.

You're likely to encounter this pattern regularly. A project you clone might have been written six months ago targeting Node 20. Another project might still be on Node 18. A tool you pull in for your own work might require Node 22. This is normal. The machine handles it by having multiple Node versions available at once.

---

## What nvm Is

nvm is the program that makes multiple Node versions manageable. The name stands for Node Version Manager.

Think of it as a switchboard. Without nvm, your machine has one Node installation, and every project uses that same version. With nvm, your machine has as many Node versions as you've installed, and you switch between them depending on which project you're working on.

When you switch Node versions with nvm, the PATH is updated so that `node` and `npm` commands point to the version you selected. The other installed versions are still there — they're just not currently active. A session using Node 18 doesn't interfere with a session using Node 20. They coexist on disk, and nvm routes commands to the right one.

The AI uses nvm to:

1. Check which Node version is currently active
2. Check which version the project needs
3. Switch to the right version, or install it if it isn't on the machine yet
4. Proceed with `npm install`

Without nvm, the AI's options are more limited. It can't easily switch Node versions in a single shell session. nvm is why that's possible.

---

## What `.nvmrc` Is

Open `frontend/` and there's likely a file called `.nvmrc`. It's short and contains a single line:

```
20.11.1
```

That's it. That file is the project's declaration of which Node version it expects. When the AI runs `nvm use` without specifying a version, nvm reads `.nvmrc` and switches to whatever version is listed there.

You don't need to create or maintain `.nvmrc`. It's already in the project. The AI reads it. The point of knowing it exists is so that when you see the AI run `nvm use` with no version argument, you understand what it's reading — and why the version it switches to is the right one.

If `.nvmrc` isn't present, nvm won't know which version to switch to automatically. The AI will handle that case by reading the `engines` field in `package.json` instead. Both paths lead to the same place: the correct Node version.

---

## What the AI Does

When the AI sees the `EBADENGINE` error, the sequence is straightforward.

> **What the AI Does:**
> First, the AI checks for `.nvmrc` in the frontend directory:
>
> ```
> cat frontend/.nvmrc
> ```
>
> Output:
> ```
> 20.11.1
> ```
>
> Then it checks if that version is installed:
>
> ```
> nvm ls 20.11.1
> ```
>
> If the version isn't installed yet:
> ```
> nvm install 20.11.1
> ```
>
> You'll see:
> ```
> Downloading and installing node v20.11.1...
> Downloading https://nodejs.org/dist/v20.11.1/node-v20.11.1-darwin-arm64.tar.xz...
> Computing checksum with sha256sum
> Now using node v20.11.1 (npm v10.2.4)
> ```
>
> Then:
> ```
> nvm use 20.11.1
> ```
>
> And it retries:
> ```
> npm install
> ```

> **Watch For:**
> After the switch, `node --version` should return `v20.11.1`. When `npm install` runs again, the `EBADENGINE` error should be gone. You'll see the install proceed — downloading packages, logging progress, finishing with `added N packages in Xs`. That's the engine check passing and the install completing.

---

## The Session Caveat

Here's the part that catches people off guard: `nvm use` only applies to the current terminal session.

When you open a new terminal window, the shell starts fresh. It reads your shell configuration files (`.zshrc` for zsh, `.bashrc` for bash), and unless nvm has been configured to read `.nvmrc` automatically on directory change, the active Node version resets to nvm's default — or to whatever was last set as the default.

This means: if you were on Node 20.11.1, close the terminal, open a new one, and try to run the frontend, you might be back on Node 18. The commands fail. The project looks broken. It's not broken — the version just reset.

There are two ways this gets handled. One is that the AI switches Node at the start of each session before doing anything with the frontend. The other is that nvm can be configured to automatically run `nvm use` when you enter a directory that has a `.nvmrc` file. That's a persistent configuration — once it's set, nvm handles the switch without the AI needing to do it explicitly each time.

> **What the AI Does:**
> If nvm's auto-switch isn't configured, the AI will add a hook to your shell's configuration file (`.zshrc`) that enables automatic version switching. The hook watches for `.nvmrc` files when you change directories and runs `nvm use` for you.
>
> You'll see the AI add something like this to `~/.zshrc`:
> ```
> autoload -U add-zsh-hook
> load-nvmrc() {
>   local nvmrc_path
>   nvmrc_path="$(nvm_find_nvmrc)"
>   if [ -n "$nvmrc_path" ]; then
>     nvm use
>   fi
> }
> add-zsh-hook chpwd load-nvmrc
> load-nvmrc
> ```
>
> After this, opening a new terminal and navigating to `frontend/` will automatically switch to Node 20.11.1.

---

## The Python Parallel

This is the Node version of a problem you've already seen.

In Chapter 6, the Python error wasn't about Python being absent — it was about the wrong Python being active, or the right packages not being installed into the right environment. The fix involved setting up the right environment and making sure Python commands ran inside it.

Here, the Node error isn't about Node being absent. It's about the wrong Node version being active. The fix involves switching to the right version, verifying it, and then proceeding.

The parallel even holds in the session behavior. With Python, activating a virtual environment only applies to the current session — close the terminal and the environment is no longer active. With Node, `nvm use` only applies to the current session unless automatic switching is configured.

Both tools solve the same underlying problem: a machine can have multiple versions of a runtime, and different projects need different versions. The mechanism is different (`.venv` vs. nvm), but the concept is the same.

---

## What You Own

The AI manages the nvm install and the version switching. You own one thing: noticing when the version has reset.

If you open a new terminal, navigate to the frontend, and something starts failing that was working before, version reset is one of the first things to check. The AI can confirm by running `node --version`. If it shows `v18.19.0` when the project needs `v20.11.1`, that's the explanation.

You don't need to fix it yourself. You can ask the AI to switch the version. But knowing that this can happen — and recognizing it when it does — is what keeps it from being a mystery.

> **Don't Do This:** Do not use a Node installer from nodejs.org or a system package manager (like Homebrew's `brew install node`) to install or upgrade Node if nvm is already managing Node on your machine. Mixing install methods creates conflicts. The system-installed Node and the nvm-managed Node may fight over the PATH, and the AI's `nvm use` commands may not have the effect you expect. If nvm is in place, it should be the only thing managing Node versions.

> **Key Takeaway:** `EBADENGINE` means the Node version on the machine doesn't satisfy what the project declared. nvm is the tool that fixes this — it switches the active Node version to the one the project needs. The fix is a version switch, not a reinstall.

---

The right version of Node is active — but `npm install` also revealed that `frontend/node_modules` was empty, and that's what the next chapter explains.
