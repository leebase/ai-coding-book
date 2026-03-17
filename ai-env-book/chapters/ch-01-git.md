# Chapter 1: What Git Actually Is

You just cloned `neighborhood-meals` and asked your AI to check the project state. It ran a command and handed you this:

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be staged)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   frontend/src/App.jsx

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	frontend/src/styles.css

no changes added to commit (use "git add" and/or "git commit -a")
```

If you don't know what you're looking at, this is noise. Words like "staged," "untracked," and "working directory" have specific meanings here, and without them the output tells you nothing. Or maybe you didn't even get that far — maybe you opened the terminal in the wrong folder and got this instead:

```
fatal: not a git repository (or any of the parent directories): .git
```

That one stops everything. The AI can't do git work from outside the project folder. Before anything else works, you need to know what git is, where it lives, and what it's actually tracking.

---

## Git Is a Snapshot Machine

Most people come to git thinking of it as something like a backup system or a change tracker — a record of what got edited and when. That's close, but it's not right, and the gap between that model and the actual one causes real confusion.

Git is a snapshot machine. Every time you commit, git takes a complete picture of your files at that moment and saves it. Not a record of what changed — a full snapshot. If you look at the history of a project, you're not looking at a list of diffs. You're looking at a stack of complete states of the project, each one labeled with a message, a timestamp, and a unique ID.

The practical implication: you can go back to any of those states exactly. Not reconstruct it — go back to it. The snapshot is there.

This is why the error message `fatal: not a git repository` is specific about what's missing. Git's snapshot history lives in a folder called `.git` inside your project. No `.git` folder means git has nowhere to read from or write to. It can't operate.

When you ran `git clone` to get `neighborhood-meals`, git created that `.git` folder automatically. It's hidden by default in most file browsers, but it's there, at `neighborhood-meals/.git`. That folder is the database. Every commit you've made, every branch, every piece of the project's history — it's in there.

> **Don't Do This:** Do not delete the `.git` folder. There's no reason to, but sometimes people do it when cleaning up a project or troubleshooting. If you delete it, you lose all history. The AI knows not to touch `.git`. You should too.

---

## The Three Places Your Code Lives

At any moment, the files in your project exist in one of three places. Understanding these three places is what makes git's output legible.

**The working directory** is your filesystem. The files you open in your editor, the files you can see and change. When you edit `frontend/src/App.jsx`, that change exists only here. Git hasn't heard about it yet.

**The staging area** is a holding zone. When the AI runs `git add`, it moves changes from the working directory into staging. Think of it as a preparation table: you're assembling what you want the next snapshot to contain. A file can be partially staged — some of its changes going in, some not — but practically speaking, you'll usually see the AI add whole files.

**The committed history** is the snapshot stack. When the AI runs `git commit`, it takes everything in staging and locks it into a new snapshot. That snapshot goes into `.git`. It's permanent — or as close to permanent as digital things get.

The output from `git status` is a report on where your files are. That's all it is. The "Changes not staged for commit" section is telling you what's in the working directory but not in staging. The "Untracked files" section is telling you what files git has never seen — they're not even in staging consideration yet.

A clean `git status` looks like this:

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

That last line is the signal. "Working tree clean" means nothing is in the working directory that isn't also reflected in the last snapshot. No uncommitted edits, no untracked files.

A dirty `git status` means something is in the working directory that hasn't been committed. It's not an error. It's a report.

---

## The Five Commands You'll Watch the AI Use

Your AI is going to run these five commands constantly. You don't need to memorize them — you need to know what each one is doing when you see it.

**`git status`** — Checks the current state. What's modified, what's staged, what's untracked. The AI runs this before almost every other git operation to understand what it's working with.

**`git add`** — Moves changes from the working directory into staging. `git add frontend/src/App.jsx` stages one file. `git add .` stages everything in the current directory. The AI will usually be specific about what it adds.

**`git commit`** — Takes everything in staging and saves it as a new snapshot. Always comes with a message describing what changed: `git commit -m "update app styles"`. Without a message, git refuses.

**`git log`** — Shows the snapshot history. Each entry has a commit ID (a long string of letters and numbers), an author, a timestamp, and the message. The AI reads this to understand where the project came from and to reference specific commits.

**`git diff`** — Compares states. With no arguments, it shows the difference between the working directory and staging. With commit IDs, it compares two snapshots. The AI uses this to understand what changed before deciding what to commit.

None of these commands change anything on GitHub. They're all local. Your working directory, your staging area, your committed history — all of it lives on your machine. GitHub is separate.

---

## What the Wrong-Directory Error Is Actually Saying

Back to that error:

```
fatal: not a git repository (or any of the parent directories): .git
```

Git looked for a `.git` folder in your current directory, then in every parent directory above it. It found nothing. The project's git database doesn't exist at this location.

This usually happens one of two ways. Either you're in the wrong directory — maybe you're in your home folder or in `Desktop` instead of `neighborhood-meals` — or you're in a subdirectory of the project that git is treating as unrelated. Running `git status` from inside `neighborhood-meals/backend/` works fine. But if you opened a new terminal window and forgot to navigate back into the project, you'll get this.

> **What the AI Does:** When the AI sees this error, it checks your current directory, finds the correct project path, and re-runs the command from there. It may run `cd neighborhood-meals` first, or it may note the path in its next command. If it can't find the project, it will ask you where it is.

> **Watch For:** After the AI navigates to the correct folder, the next `git status` should return output about your project — branch name, file states — instead of the `fatal:` error.

The fix is not a git fix. It's a navigation fix. That's worth naming, because a lot of git errors are actually shell errors in disguise.

---

## The Reader's One Job

The AI handles the commands. It decides when to add, when to commit, when to check status. What you need to own is one piece of awareness: is `git status` showing a clean working tree or a dirty one?

Clean means the AI is working from a stable baseline — the last committed snapshot reflects what's on disk. Dirty means there's uncommitted work somewhere, and the AI needs to account for it before doing things like switching branches or pulling from GitHub.

You don't need to know what to do about it. You need to notice it. If your AI is about to do something and you see untracked or modified files in the status output, that's the moment to say: "there are uncommitted changes here — should we commit or discard them first?" The AI will take it from there.

> **Key Takeaway:** Git saves snapshots of your project, not diffs. The `.git` folder is the database. The three areas — working directory, staging, committed history — are where your files live at any moment. A clean working tree means git's snapshot matches your disk. A dirty one means it doesn't yet.

---

Now that you know what git is tracking, the question is where that tracking lives when you share your code.
