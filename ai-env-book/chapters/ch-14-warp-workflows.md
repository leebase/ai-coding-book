# Chapter 14: Warp Workflows for Developers

You've used `#` to kill a stuck process and to fix a broken PATH. The pattern is familiar now: describe the problem, get the command, review it, run it.

This chapter adds two more patterns and introduces something that happens naturally once you're comfortable with those patterns.

---

## Pattern 4: Environment Variables That Disappear

You're connecting the `neighborhood-meals` backend to an external API. The AI coding tool told you to set an API key as an environment variable, so you did:

```
export OPENAI_API_KEY=abc123
```

The backend can read it. Everything works. You stop for the day, close the terminal, and come back the next morning.

New terminal. You check the value:

```
echo $OPENAI_API_KEY
```

Nothing. The variable is gone.

This is the persistence wall from Chapter 12 in practice. `export` sets a variable for the current shell session. When the session ends — when you close the terminal — the variable disappears. The OS doesn't write it anywhere permanent. The next terminal session starts fresh.

If you want an environment variable to be there every time you open a terminal, it has to live in a shell configuration file. On macOS and Linux with zsh (the default shell on modern macOS), that file is `~/.zshrc`. Every time a new terminal session starts, your shell reads `~/.zshrc` and runs everything in it. If your `export` statement is in there, the variable gets set automatically on every startup.

Open Warp and describe what you need:

```
# set OPENAI_API_KEY permanently so it survives terminal restarts
```

Warp generates:

```
echo 'export OPENAI_API_KEY=abc123' >> ~/.zshrc && source ~/.zshrc
```

The logic is the same as the PATH fix from Chapter 13: append the export statement to `~/.zshrc`, then reload the file in the current session so the change takes effect immediately.

> **Don't Do This:** Do not put the actual value of a sensitive API key in a public repository. The command above writes the key to `~/.zshrc`, which is a local file on your machine and is not tracked by git (as long as you haven't explicitly added it to the project). But if you ever commit `~/.zshrc` itself, or copy its contents somewhere version-controlled, the key is exposed. Keep `~/.zshrc` off of git.

Run the command. To confirm it worked, open a new terminal — not just a new tab, a genuinely new session — and check:

```
echo $OPENAI_API_KEY
```

> **Watch For:** The value you set should print to the terminal. If it returns an empty line, the command didn't write to `~/.zshrc` correctly — check whether you're running zsh (the default shell on modern macOS) or bash. If you're running bash, the file you want is `~/.bash_profile` or `~/.bashrc`, not `~/.zshrc`. Describe this to Warp: `# I'm using bash and I need to set an environment variable permanently` — Warp will generate the right command for your shell.

---

## Pattern 5: Check Before You Start

The port conflict in Chapter 13 happened after the fact: you tried to start the server, it failed, you diagnosed. There's a faster approach.

Before starting the dev server, check whether the port is already in use:

```
# is anything on port 3000 right now
```

Warp generates:

```
lsof -i :3000
```

You've seen this command before. You don't need to memorize what `lsof` or `-i` mean — but you're starting to recognize it. Run it.

**If the output is empty:** Nothing is on port 3000. Safe to start the server.

**If you see a process:** Something is already there. You know what to do: `# kill that process`, get the PID from the output, run `kill -9 <PID>`. Then check again before starting.

The lesson here is about sequence, not commands. Starting a dev server without checking first means you might get an `EADDRINUSE` error, go through the diagnosis, kill the process, and then start the server. That's three steps. Checking first collapses it to one.

There's a deeper pattern here too: Warp is often most useful before the failure, not just after it. Once you know the common walls on your machine, you can ask preventative questions. Is the port free? Is the binary on PATH? Is the variable still set? These are boring checks, and boring checks are good. They turn "debugging" into "verifying the machine state before you depend on it."

---

## Why `lsof` Keeps Appearing

You've now seen `lsof -i :3000` come up twice — once when diagnosing a port conflict, and once as a pre-check. This is not a coincidence, and it's not asking you to memorize anything.

What's happening is recognition. You described two different situations to Warp ("what is on port 3000" and "is anything on port 3000 right now"), and both times it gave you the same command. That's because `lsof -i :3000` is the right tool for both questions — it checks which processes have a network connection on that port.

After seeing it twice, you know what it does. You don't need the flags memorized. You don't need to know how to spell it. But the next time you see `lsof` in Warp output, you'll recognize it as "the command that tells me what's using a port." That recognition is the point. It's the difference between output that means something and output that's just noise.

The same thing will happen with other commands you encounter repeatedly. Each time Warp generates the same tool for similar situations, the tool becomes slightly more legible.

---

## Warp Drive

Once you've been using `#` for a while, you'll start to notice a pattern: some descriptions come up over and over. "What is on port 3000." "What is on port 8000." "Is anything on port 3000 right now." You're asking the same question in slightly different forms.

Warp Drive is a library of saved, shareable commands. A **workflow** is a command with named blanks — like a template. You might save a workflow called "Check port" that runs `lsof -i :{PORT}`, where `PORT` is a placeholder. When you use the workflow, Warp asks you for the port number and fills it in.

For a solo developer, Warp Drive is a personal cookbook. You save the patterns you use often so you don't have to retype the description from scratch each time.

For a team, it's a shared resource. If everyone on the team saves the same diagnostic workflows, you're all using the same commands when you're debugging the same server. The senior developer who knows what `lsof` is can save it once, and everyone else can use it without needing to know the syntax.

That matters more than it might seem. A shared workflow doesn't just save time. It standardizes what "check the port" means on your team. Instead of one person using `lsof`, another using `netstat`, and a third searching the web every time, everyone reaches for the same known-good diagnostic. For a new developer, that consistency removes a lot of ambient doubt.

You don't need Warp Drive to use the patterns in this book. The `#` workflow gets you there every time. But if you find yourself describing the same situation repeatedly, Warp Drive is where you turn that repetition into a saved shortcut.

To get to it: look for the Warp Drive icon in the Warp sidebar, or search for it in Warp's command palette. You can browse workflows others have published, save your own, and share them with a team.

---

## All Five Patterns Together

At this point you have five diagnostic patterns:

| Situation | What you type |
|-----------|---------------|
| Something is broken, you don't know why | `# describe the error in plain English` |
| Port conflict | `# what is on port 3000` → see PID → `# kill that process` |
| PATH problem | `# [command] not found but I just installed it` → `# add [path] to my PATH permanently` |
| Environment variable disappears | `# set [VARIABLE] permanently so it survives terminal restarts` |
| Check before starting | `# is anything on port 3000 right now` |

None of these require memorizing commands. Each one starts with describing a situation. Warp handles the syntax.

What you're building is not a list of commands — it's a habit of reaching for the right tool when you see a particular shape of problem. Port occupied: Warp. Command not found: Warp. Variable disappeared overnight: Warp. Syntax error in `backend/app.py`: AI coding tool.

And by this point, another habit has started to form too: you review the generated command before you run it. That's important. Warp is helping with translation, not replacing judgment. You still glance at the command, make sure it matches what you asked for, then run it. That's the same pattern you've been building with the AI coding tool throughout the book: let the tool do the syntax, keep ownership of the intent.

> **Key Takeaway:** The `#` pattern in Warp handles machine-state problems the same way every time: describe what you see, review the generated command, run it, confirm it worked. Warp Drive extends this with saved, shareable workflows — useful once you're running the same patterns often enough to want shortcuts.

---

You now have a working toolkit for the gap between code problems and machine problems — the last chapter draws the line between them.
