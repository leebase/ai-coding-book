# Chapter 5: When Git Goes Wrong

You edited `frontend/src/App.jsx` directly — you were experimenting with a color change, just looking at it. Then the AI tried to switch to a different branch and git stopped everything:

```
error: Your local changes to the following files would be overwritten by checkout:
	frontend/src/App.jsx
Please commit your changes or stash them before you switch branches.
Aborting
```

Nothing broke. No data was lost. Git saw the unsaved edit and refused to proceed. But the AI is stuck now, and you need to understand what happened before deciding how to proceed.

Git has a small set of error states that come up repeatedly. Each one has a distinct message, a clear cause, and a specific resolution. Once you've seen them once, you'll recognize them on sight.

---

## Error State 1: Dirty Working Tree

This is the error shown above. You have uncommitted changes in the working directory, and git is refusing to do something that would overwrite them.

**What git is protecting:** Your edits. The file on disk contains changes that don't exist anywhere in git's snapshot history. If git proceeds with the branch switch, it would replace your version of the file with the version from the other branch. Those edits disappear. Git won't do that silently.

**What the AI does:** The AI has two options. If the changes are worth keeping — if they're meaningful work, even incomplete — it commits them first:

```
git add frontend/src/App.jsx
git commit -m "wip: color experiment"
```

Now the changes are in a snapshot. The branch switch proceeds.

If the changes are not worth keeping — you were poking at something and don't need the result — the AI discards them:

```
git restore frontend/src/App.jsx
```

This brings the file back to the last committed state. The edits are gone. The branch switch proceeds.

A third option is stashing: `git stash` saves the changes in a temporary holding area outside your commit history, lets the branch switch happen, and you can retrieve them later with `git stash pop`. The AI uses this when the changes matter but you're not ready to commit them.

> **Watch For:** After the AI commits, stashes, or restores, it will run the branch switch again. This time it should succeed silently — no output except the confirmation that you're on the new branch. A clean switch means the dirty working tree is resolved.

---

## Error State 2: Detached HEAD

You run `git status` and see:

```
HEAD detached at abc1234
nothing to commit, working tree clean
```

Or maybe the AI mentioned it was in detached HEAD state and you don't know what that means.

**What git is telling you:** You're not on a branch. You're floating on a specific commit.

Normally, when you're on a branch, your position is tied to a label. When you commit, that label advances — `main` or `feat/theme-switcher` moves forward with you. In detached HEAD state, there's no label attached to your position. If you commit here, those commits are not connected to any branch. They exist in the `.git` database temporarily, but git can't easily find them and will eventually discard them during cleanup.

This usually happens when the AI checks out a specific commit by its ID rather than by branch name. It's useful for inspecting history but risky if you start working.

**What the AI does:** If it needs to do work from a detached HEAD, it creates a branch at that position:

```
git checkout -b recovery-branch
```

This attaches a label to where you are now. Any commits you make from here are saved under that branch name. Nothing gets lost.

> **Watch For:** After the AI creates a branch, `git status` should show `On branch recovery-branch` (or whatever name it chose) instead of `HEAD detached at...`. That means you're anchored. Commits are now safe.

> **Don't Do This:** Do not commit in detached HEAD state without asking the AI to anchor you first. It looks like it works — the commit goes through — but if you switch branches after, those commits become orphaned. They're hard to find and will eventually be garbage-collected by git.

---

## Error State 3: Merge Conflict

Two people (or the AI on two branches) edited the same part of the same file. Now git is trying to combine them and doesn't know which version to use:

```
CONFLICT (content): Merge conflict in frontend/src/App.jsx
Automatic merge failed; fix conflicts and then commit the result.
```

If you open `frontend/src/App.jsx`, you'll see this inside it:

```
<<<<<<< HEAD
  background-color: #ffffff;
=======
  background-color: #1a1a2e;
>>>>>>> feat/theme-switcher
```

**What git is telling you:** The section between `<<<<<<< HEAD` and `=======` is the version from the branch you're merging into. The section between `=======` and `>>>>>>> feat/theme-switcher` is the version from the branch you're merging in. Git doesn't know which one is right, or whether you want to combine them somehow.

**What the AI does:** The AI reads both versions, understands what each one is doing, and resolves the conflict — either by choosing one version, or by writing a third version that incorporates both intentions. It then removes the conflict markers, saves the file, and runs:

```
git add frontend/src/App.jsx
git commit
```

That commit finalizes the merge.

> **Watch For:** After the AI resolves conflicts and commits, run `git status`. It should show `nothing to commit, working tree clean` with no mention of conflicts. If any file still shows `UU` (unmerged) in the status output, there are unresolved conflicts remaining.

> **Don't Do This:** Don't edit a conflict-marked file manually unless you know exactly what you're doing. The conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) are git's syntax. If you accidentally delete one marker but not the others, git's merge state gets corrupted and the resolution process fails.

---

## Error State 4: Rejected Push (Non-Fast-Forward)

The AI tried to push to GitHub and got:

```
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'git@github.com:yourname/neighborhood-meals.git'
hint: Updates were rejected because the remote contains work that you do not have locally.
hint: Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
```

**What git is telling you:** Someone else pushed commits to `main` on GitHub after you last pulled. Your local `main` and the remote `main` have diverged. Git won't push because that would overwrite the other person's work.

This happens in team contexts — or if you pushed from another machine and forgot to pull on this one. The remote has commits your local copy doesn't have. Before your commits can go up, you need to bring those commits down first.

**What the AI does:** It pulls first:

```
git pull origin main
```

or, more precisely, it fetches and then rebases or merges. `git pull --rebase origin main` is a common pattern — it brings down the remote commits, then replays your local commits on top of them. The result is a clean linear history.

After the pull succeeds, the push goes through.

> **Watch For:** After a successful pull and push, the output should include a line like:
> ```
> To git@github.com:yourname/neighborhood-meals.git
>    abc1234..def5678  main -> main
> ```
> If the push still fails after a pull, something else is wrong — possibly a force-push restriction on the branch (common on `main` in team repositories). The AI will tell you if that's the case.

> **Don't Do This:** Do not run `git push --force` unless the AI explicitly tells you to and explains why. Force-pushing rewrites the remote's history. If anyone else pulled that branch, their copy is now out of sync in a way that's hard to recover from. It's occasionally necessary, but it's not a default fix for a rejected push.

---

## The Pattern Across All Four

Every one of these errors follows the same structure. Git encountered something it couldn't proceed past safely, and it stopped and told you exactly what it found.

Git doesn't silently overwrite your work. It doesn't guess. It doesn't proceed when things are ambiguous. The errors are not failures — they're reports. The AI reads them, identifies what git is protecting or what state it found, and takes the appropriate action.

Your part in this is the same as it's been throughout Part 1: recognize which error you're looking at. When you can name the state — dirty working tree, detached HEAD, merge conflict, rejected push — you can tell the AI what it's dealing with. That's faster and more accurate than pasting the full error and asking "what does this mean."

These four states cover most of what you'll see. There are edge cases beyond them, but the pattern is consistent: git tells you exactly what it found, in words you can read. The message is not obscure. It's precise.

> **Key Takeaway:** Git stops rather than overwrites. Every error state in this chapter is git protecting something — your uncommitted edits, the integrity of the history, someone else's pushed work. When the AI resolves one of these states, it's not fighting git. It's working with the information git gave it.

---

Git is the foundation, but once the code is in the right place, the next wall is usually not about the code at all — it's about whether the right Python is running it.
