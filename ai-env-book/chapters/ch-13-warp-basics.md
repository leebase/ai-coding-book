# Chapter 13: Warp Basics

You have Warp open. It looks like a terminal. There's a prompt, probably a blinking cursor, and if you type a command and press Enter it runs — just like any other terminal.

The difference isn't in how it looks. It's in two things: how output is organized, and what happens when you type `#`.

---

## Blocks

In a traditional terminal, output streams past. You run a command, get ten lines of output, run another command, get thirty more lines. Everything accumulates from top to bottom, and if you want to find something from three commands ago, you scroll up and hunt for it in an undifferentiated wall of text.

Warp organizes output differently. Every command you run produces a **block** — the command you typed and the output it produced are grouped together, with a visual indicator showing whether the command succeeded or failed. Green indicator: it exited cleanly. Red indicator: something went wrong.

Blocks are self-contained. You can navigate between them with keyboard shortcuts instead of scrolling. You can copy just the output of a specific command. You can search within a single block's output using Cmd+F (macOS) or Ctrl+F (Linux/Windows). You can collapse blocks you're done with.

When you're diagnosing a problem, this matters. You're going to run a diagnostic command, read the output, run a fix command, and check the result. In a traditional terminal, those four outputs are interleaved. In Warp, each one is its own unit. You can see exactly what each command produced.

---

## `#` — AI Command Search

This is the feature that changes how you use the terminal.

At the prompt, type `#`. Don't press Enter yet — just `#`. The prompt will shift into a description field.

Now type what you want in plain English. Not a command — a description of what you're trying to do, or a problem you're looking at. Warp processes your description and generates the command. You review it. Then you run it.

A few things this means:

**You are not memorizing syntax.** The syntax for checking which process is using a port is `lsof -i :3000`. You don't need to know that. You describe the situation, and Warp produces the command. The next time you need it, you describe it again.

**You review before you run.** Warp generates the command and shows it to you. You can read it, understand what it does, and decide whether to execute it. This is not a "just trust the AI" workflow. You own the final decision on every command, especially commands that modify system files.

**Specificity matters.** "Something is broken" is too vague for Warp to do much with. "Port 3000 is already in use and I need to find what's using it" is specific enough. The more accurately you describe the situation, the more useful the generated command will be. You'll develop a feel for this after a few uses.

---

## Pattern 2: Port Conflict

Here's how this plays out in practice, starting from the wall.

You tried to start the frontend dev server and got:

```
Error: listen EADDRINUSE: address already in use :::3000
```

Open Warp. At the prompt, type `#` and then describe what you need:

```
# what is on port 3000
```

Warp generates:

```
lsof -i :3000
```

`lsof` lists open files and network connections. The `-i :3000` flag filters to connections on port 3000. You don't need to remember the flag. You just need to know that this command will tell you what's there.

Run it. The output looks something like this:

```
COMMAND   PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node    12345   you   24u  IPv6 0x...         0t0  TCP *:3000 (LISTEN)
```

There it is. A Node process, PID 12345, listening on port 3000. This is the previous dev server session — it didn't stop cleanly when you closed that terminal window. The process is still running. The port is still occupied.

Now type `#` again:

```
# kill that process
```

Or if you want to be more specific:

```
# kill PID 12345
```

Warp generates:

```
kill -9 12345
```

`kill` sends a signal to a process. `-9` is the SIGKILL signal — it terminates the process immediately, no cleanup. The `12345` is the PID from the output you just read.

> **Watch For:** After running `kill -9 12345`, run `lsof -i :3000` again. If the output is empty, the port is clear. If the same process is still there, you may need to run the kill command again.

Now start your dev server. The `EADDRINUSE` error is gone.

> **Don't Do This:** Don't run `kill -9` without checking the PID first. The number in your output will be different from the one in this example — it changes every time a process starts. Read the `lsof` output, find the PID column, and use that specific number. Running `kill -9` on the wrong PID terminates a different process.

---

## Pattern 3: PATH Problem

The other wall from Chapter 12. You (or the AI) just installed `gh` and now:

```
zsh: command not found: gh
```

Open Warp. Type:

```
# gh command not found but I just installed it
```

Warp will suggest checking where the binary is and whether that location is on your PATH:

```
which gh
```

`which` searches your PATH and prints the location of the command if it finds it. If `gh` isn't on your PATH at all, `which gh` returns nothing — or a message like `gh not found`. If it finds it, it returns the path, like `/usr/local/bin/gh`.

Run `which gh`. Two possibilities:

**It returns a path:** The binary exists and the shell can find it — which means something else is going on. You might be running the wrong shell, or there might be a version conflict. Describe what you see to Warp and continue diagnosing.

**It returns nothing:** The binary is installed somewhere that isn't on your PATH. Now you need to figure out where it actually is and add that location to PATH.

Type `#` again:

```
# add /usr/local/bin to my PATH permanently
```

Warp generates:

```
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

This is worth reading before you run it.

`echo 'export PATH="/usr/local/bin:$PATH"'` produces a line of text. `>> ~/.zshrc` appends that line to the end of your `~/.zshrc` file — your shell configuration file, which runs every time a new terminal session starts. `&&` means "if the first command succeeded, run the next one." `source ~/.zshrc` reloads the configuration file in the current session, so the change takes effect immediately without you needing to close and reopen the terminal.

> **Don't Do This:** Do not use `>` instead of `>>`. A single `>` overwrites the file. A double `>>` appends to it. If you accidentally overwrite your `~/.zshrc`, you'll wipe out all your existing shell configuration. Warp generates the correct `>>` — this is just something to understand when you read the command before running it.

After running it, confirm:

```
gh --version
```

If it prints a version number, the PATH fix worked. If it still says `command not found`, the binary isn't in `/usr/local/bin` — it's somewhere else. Type `#` again and describe what you're seeing; Warp will help narrow it down.

> **Watch For:** `gh --version` should return something like `gh version 2.x.x`. If you see that, you're done.

---

## Describing Problems Well

The quality of what Warp generates depends on how specifically you describe what you're looking at. Some examples of the difference:

| Too vague | Specific enough |
|-----------|-----------------|
| `# npm is broken` | `# npm says missing script dev` |
| `# the server won't start` | `# server fails with EADDRINUSE on port 3000` |
| `# command not found` | `# gh command not found but I just installed it` |
| `# fix my PATH` | `# add /usr/local/bin to my PATH permanently` |

The pattern: name the error or symptom you actually see, not just the outcome you want. Warp needs to understand what the current state is before it can suggest a path forward.

You'll get faster at this. After the first few times, you start to know instinctively how much detail Warp needs.

---

## What You Own

Warp generates the command. You run it. That division is straightforward for read-only commands like `lsof` — there's no risk in checking what's on a port. It matters more for commands that change things.

Two categories to be careful about:

**Commands that modify shell configuration files.** When Warp generates a command that writes to `~/.zshrc`, read it before running it. Check whether it's appending (`>>`) or overwriting (`>`). Check that the value being written is what you intend. These changes persist across every future terminal session.

**Commands that kill processes.** Confirm the PID is what you expect before running `kill -9`. The `lsof` output tells you the command name (`node`, `python`, etc.) — that's a sanity check. If the PID in your output belongs to something other than a dev server, stop and look more carefully.

Warp is a tool for working faster, not for running commands without reading them. The AI generates; you decide.

---

These two patterns — killing a stuck process and fixing a broken PATH — cover the most common machine-state problems you'll hit while running `neighborhood-meals`, but they're just the beginning of what Warp can do when you have a few more worked examples.
