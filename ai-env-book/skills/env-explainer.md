# Skill: Env Explainer

Use this skill when a chapter or brief needs to explain an environment concept
to a new developer. The goal is not to turn the reader into an operator. The
goal is to help them recognize what kind of problem they are looking at, follow
what the AI is doing, and avoid undoing the fix.

## The Required Sequence

Environment explanations in this book follow the same order every time:

1. Show the exact wall first
2. Name the thing the reader is actually looking at
3. Give one mental model that makes it legible
4. Show what the AI checks or changes
5. Tell the reader what success or failure looks like

Do not invert this. New developers usually do not need a definition first.
They need relief first: "Yes, this is the thing that produced that error."

If the scenario thread already defines the error message, show it verbatim. Do
not paraphrase it into cleaner prose. Recognition depends on matching what the
reader will actually see in the terminal.

## Error First, Then Meaning

Start with the real output, confusion, or failure state. After the error block,
add one plain-language sentence that answers: "What does this mean?"

Examples:

- `ModuleNotFoundError: No module named 'flask'` means the backend is running
  without the package installed in the Python environment it is currently using.
- `zsh: command not found: node` means the shell cannot find a `node`
  executable at all, not that the app code is wrong.
- `npm ERR! code EBADENGINE` means Node exists, but it is the wrong version for
  what this project declared.

Only after that should you explain the concept behind the failure.

## Mental Models That Work

Pick one analogy and stay with it long enough for the reader to use it.
Avoid stacking metaphors or switching vocabulary mid-explanation.

- Python environment: a project-specific room. The interpreter and packages in
  that room belong to this project, not every project on the machine.
- `pyproject.toml` or `requirements.txt`: the project's packing list. These
  files describe what the backend expects before the AI installs anything.
- Node version managers such as `nvm`: a version switchboard. Node is not just
  "installed" or "missing"; the machine can have multiple versions, and the AI
  may need to switch to the one this project expects.
- `package.json`: the frontend's manifest. It names the app, scripts, and
  dependencies. `node_modules` is the local copy of what the manifest asked for.
- `PATH`: the shell's search list. When the shell says "command not found," it
  is often saying, "I do not know where to look for that program."
- A busy port: a parking space already occupied. The app can be correct and
  still fail because another process is already using port `3000`.

These analogies are good because they help the reader identify the class of
problem without forcing them to memorize system internals.

## Recognition, Not Mastery

Aim for the depth where the reader can answer these questions:

- What kind of thing failed here?
- What is the AI trying to inspect or change?
- What output tells me the fix worked?

That is enough. Do not drift into operator training, man-page tours, or
complete package manager theory. The reader does not need every flag on
`python`, `uv`, `npm`, or `nvm`. They need to know why the AI used the tool and
what changed as a result.

A useful test: if the AI fixed the problem while the reader watched, could the
reader explain the shape of the fix in one or two sentences? If yes, the depth
is right.

## Show What the AI Does

When the AI acts, narrate the action in this order:

1. What the AI is checking or changing
2. The command, file read, or configuration change
3. The output or file diff the reader sees
4. One sentence on why that output matters

This keeps the reader oriented. It also prevents command memorization mode.
The command is evidence of the operation, not the lesson itself.

Prefer explanations like:

- "The AI checks which Python is active before installing packages."
- "The AI reads `backend/pyproject.toml` to confirm the required Python range."
- "The AI switches Node versions before retrying `npm install`."

Avoid explanations like:

- "Run this exact command every time."
- "Memorize these flags because you will need them later."

## What to Avoid

- Do not define a concept before the reader has seen the problem it solves.
- Do not treat environment failures as code failures when the code is not the
  issue.
- Do not bury the success signal. Name the line or behavior that confirms the
  fix worked.
- Do not assume the reader knows what "interpreter," "process," "shell
  config," or "PATH" means; define the term inline the first time it matters.
- Do not expand beyond the scenario. Use the canonical repo, files, branches,
  and errors from `skills/scenario-thread.md`.

The book's job is to make the machine legible enough that the reader can work
with an AI on purpose instead of treating every environment problem like magic.
