# Chapter 4: Branches and Worktrees

You asked your AI to add a theme switcher to `neighborhood-meals`. It ran some commands and then you noticed your terminal prompt changed — it now shows `feat/theme-switcher` where it used to show `main`. Or maybe you ran `git status` yourself and saw:

```
On branch feat/theme-switcher
nothing to commit, working tree clean
```

Nobody asked it to create a branch. It just did. And now you're not on `main` anymore.

Or you looked at your filesystem and found a second copy of the project:

```
~/code/neighborhood-meals/
~/code/neighborhood-meals-theme-switcher/
```

Two project folders. The AI created one you didn't ask for, and you're not sure if it's a duplicate, a backup, or something that matters.

Both of these things are intentional. They're how the AI protects your work.

---

## What a Branch Actually Is

The word "branch" suggests a copy — a diverging path of code. That's the intuition, but it's not how git implements it.

A branch is a label. It's a pointer to a specific commit in your snapshot history. That's all. When you create a new branch, you're not copying any files. You're creating a new label that points to the commit you're currently on.

When the AI created `feat/theme-switcher`, it did something equivalent to putting a sticky note on the current snapshot that says "this is where theme-switcher work starts." Then it moved to that label and began committing. Each new commit on `feat/theme-switcher` advances that label forward, while `main` stays pointing at the last commit before the branch was created.

The practical result: `main` doesn't change while the AI works on `feat/theme-switcher`. When the feature is ready and reviewed, the AI merges the branch — bringing those commits into `main`'s history. Until then, `main` is clean.

You can see all branches with:

```
git branch
```

The output will look like:

```
* feat/theme-switcher
  main
```

The `*` marks the branch you're currently on.

---

## Why the AI Uses Branches

The AI creates a branch for feature work because `main` is supposed to be stable. In most projects, `main` represents code that works — code that could be deployed or shared right now. If the AI commits in-progress, experimental, or broken code directly to `main`, it corrupts that baseline.

On `feat/theme-switcher`, the AI can make commits freely, break things, fix them, make five commits and undo three of them, without `main` ever seeing any of it. When the work is done and confirmed to work, merging it into `main` is one clean operation.

This also means if the theme switcher approach doesn't pan out — if you decide to scrap it — you delete the branch and `main` is exactly where it was. No cleanup needed.

> **What the AI Does:** Before starting any significant feature, the AI will typically run `git checkout -b feat/feature-name` (or `git switch -c feat/feature-name` on newer git). This creates the branch and moves to it in one step. It will tell you what branch it's on before it starts writing code.

---

## What a Worktree Is

A worktree is a second checked-out copy of the same repository, in a different folder.

When you have `neighborhood-meals-theme-switcher` appearing next to `neighborhood-meals`, that's a worktree. Both folders share the same `.git` database — there's only one copy of the project history. But each folder has a different branch checked out, so the files on disk are different.

The AI uses worktrees when it needs to work on two things at once without switching back and forth. Maybe it's building the theme switcher in one worktree while the main project is open and running in the other. Switching branches in a single checkout would interrupt whatever is running. With worktrees, it doesn't have to.

To see all worktrees, the AI can run:

```
git worktree list
```

The output shows both locations:

```
/Users/you/code/neighborhood-meals              abc1234 [main]
/Users/you/code/neighborhood-meals-theme-switcher  def5678 [feat/theme-switcher]
```

The first column is the path on disk. The second is the current commit ID in that worktree. The third is the branch name in brackets.

> **Key Takeaway:** A worktree is not a duplicate project. It's the same project, same history, second folder. The `.git` folder in `neighborhood-meals` is shared. The `neighborhood-meals-theme-switcher` folder exists because the AI needed to work on `feat/theme-switcher` separately. You can treat it as a window into that branch.

---

## The Worktree Wall

If you try to check out `feat/theme-switcher` in your main `neighborhood-meals` folder while a worktree already has it checked out, git will stop you:

```
fatal: 'feat/theme-switcher' is already checked out at '/Users/you/code/neighborhood-meals'
```

Wait — that error message says it's checked out at `/Users/you/code/neighborhood-meals`, but that's the main folder, not the worktree. The error message in older versions of git can be confusing. What git is actually telling you is: this branch is already in use somewhere — it can't be in two places at once.

A branch can only be checked out in one worktree at a time. If `feat/theme-switcher` is in the `neighborhood-meals-theme-switcher` worktree, you can't also check it out in `neighborhood-meals`. Git protects you from this because two checked-out copies of the same branch would diverge immediately and create a conflict.

> **What the AI Does:** When it hits this error, the AI will check `git worktree list`, find the worktree that has the branch, and either switch to working in that directory or remove the worktree if it's no longer needed. It won't try to force the checkout.

> **Watch For:** If the AI runs `git worktree remove ../neighborhood-meals-theme-switcher`, it's cleaning up a worktree that's done. The folder will disappear from your filesystem. That's expected. The branch and its commits still exist in `.git` — the worktree was just the window into it.

---

## The Dirty Working Tree During a Branch Switch

There's a related wall that comes up around branches — not specific to worktrees, but common enough to cover here.

You edited `frontend/src/App.jsx`. Then the AI tried to switch branches and got stopped:

```
error: Your local changes to the following files would be overwritten by checkout:
	frontend/src/App.jsx
Please commit your changes or stash them before you switch branches.
Aborting
```

Git is not being difficult. It's protecting you. The file on disk has changes that haven't been committed. If git switches to a different branch — where `App.jsx` looks different — it would overwrite your edits and they'd be gone. Git refuses to do that without explicit instruction.

The options are: commit the changes first (make them a permanent snapshot), or stash them (save them temporarily in a git-managed holding area, switch branches, then restore them afterward). The AI will usually commit if the changes are meaningful, or stash if they're scratchwork.

This error isn't a sign that something went wrong with your setup. It's git working as designed.

---

## What You Don't Need to Manage

The AI creates branches. The AI creates worktrees. The AI merges, deletes, and cleans up. You don't need to know the commands to do any of this from scratch.

What you need is the recognition layer: if you see a second folder appear, it's a worktree and it's not a mistake. If you see a branch name you didn't create, the AI made it intentionally. If you see the worktree wall error, you know what it means and can tell the AI "there's a worktree conflict — you'll need to sort out which copy to use."

The model is: branch = label on a snapshot, worktree = second folder looking at a different label. Everything else follows from those two definitions.

---

Branches protect `main`, but they can't protect you from making changes you didn't mean to — and that's where git's safety mechanisms become visible.
