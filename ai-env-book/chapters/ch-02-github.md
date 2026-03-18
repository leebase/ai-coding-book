# Chapter 2: GitHub — Where Your Code Lives

You asked your AI to push some changes. It ran a command and referenced something called `origin`. Or maybe it told you the push succeeded, and you went to look for your code on GitHub and couldn't find it — different repository, different account, not where you expected it. Or the AI mentioned fetching from `origin/main` and you're not sure if that's the same `main` you're looking at in your project folder.

`origin` is not magic. It's a name. But understanding what it names changes how you read everything the AI does with GitHub.

---

## Git Is Local First

This is the thing that trips people up most. Git doesn't require a network connection. Git doesn't require GitHub. When you commit code, it goes into the `.git` folder on your machine. That's it. Nothing leaves your computer unless you explicitly push it somewhere.

GitHub is a separate thing. It's a hosting service — a computer somewhere that stores a copy of your `.git` database and gives it a web interface. When the AI clones `neighborhood-meals`, git copies that `.git` database from GitHub's servers to your machine. From that moment on, you have a complete, independent copy of the project history. You can commit, branch, and review history without ever touching GitHub again.

The connection between your local copy and GitHub exists only when you push or pull. And that connection has a name: `origin`.

---

## What `origin` Is

When you clone a repository, git automatically creates a shorthand name for where you cloned it from. That shorthand is `origin` by default. It points to the URL of the source repository.

For this book's companion repo, the canonical GitHub URL is:

```
https://github.com/leebase/neighborhood-meals.git
```

Depending on how the machine is set up, `origin` may use that HTTPS form directly or the SSH form of the same repository. The important point is not the transport. It's that `origin` names the remote copy of this repo.

To see what `origin` is in `neighborhood-meals`, the AI can run:

```
git remote -v
```

The output looks something like this:

```
origin	git@github.com:leebase/neighborhood-meals.git (fetch)
origin	git@github.com:leebase/neighborhood-meals.git (push)
```

That's it. `origin` is an alias for a URL. When the AI says `git push origin main`, it means: "push the commits on my local `main` branch to the URL called `origin`, into the branch called `main` on that remote."

> **Key Takeaway:** `origin` is not a place — it's a name for a place. It points to a specific URL on GitHub. The AI uses it so you don't have to read the full URL every time.

Nothing about `origin` is automatic after the initial clone. If someone sends you a project folder that wasn't cloned from GitHub — just copied — there might be no `origin` set up at all. If you try to push, you'll get an error saying there's no remote configured. The AI will add one, but it's worth knowing why it's needed.

---

## Local vs. Remote: They Are Not the Same

Your local copy of `neighborhood-meals` and the copy on GitHub are separate databases that happen to share history. Changes you make locally do not appear on GitHub until you push. Changes someone else pushes to GitHub do not appear on your machine until you pull.

This is not a bug. It's the design. Git was built for offline work and distributed teams. The local-remote split is intentional.

The practical effect: if you commit something locally and then look at the GitHub repository, you won't see it. The AI knows this. When it runs `git push origin main`, it's explicitly sending your local commits to GitHub. When it runs `git pull` or `git fetch`, it's bringing GitHub's commits down to your machine.

> **Watch For:** After a successful push, the AI may confirm with output like this:
> ```
> To git@github.com:yourname/neighborhood-meals.git
>    abc1234..def5678  main -> main
> ```
> That's git confirming it sent commits from your local `main` to the remote's `main`. The two hex strings are commit IDs — where the remote branch was, and where it is now.

If the AI pushed and you don't see this output — or if you see an error — that means nothing was sent, regardless of what the local commits look like.

---

## Public vs. Private Repositories

Every GitHub repository is either public or private. Public means anyone on the internet can view the code. Private means only people you've explicitly given access can see it.

This distinction matters in two places.

The first is obvious: if your project has credentials, API keys, or any secrets hardcoded into files, a public repository exposes them to everyone. The `.gitignore` file in `neighborhood-meals` exists partly for this reason — it lists files that should never be committed. The AI knows to check `.gitignore` before committing, but you should know why it matters.

The second is less obvious: when you share context with an AI tool, you're often pasting code, error messages, or file contents into a conversation window. That conversation may not be private depending on your service settings. Knowing whether your repository is public or private helps you calibrate how careful to be with what you paste.

For `neighborhood-meals`, the repository is private. The AI doesn't need to know your GitHub credentials to work with a private repository — but your machine does, and that's what the next chapter covers.

One more detail matters for this repo specifically: `main` is the book-facing branch, not the "everything is already smooth" branch. If you need to sanity-check whether a failure is environmental or whether the app itself is broken, the known-good branch is `reference-working`. The AI handles the branch switch. You just need to know why that branch exists.

---

## What a Fork Is

You'll see this word eventually, usually when you're working on a project you don't own.

A fork is a personal copy of someone else's repository on GitHub. When you fork a project, GitHub creates a new repository under your account that starts as an identical copy of the original. From that point, it's yours to modify. The original stays untouched.

Forks are common in open-source work: someone publishes a project, you fork it, make changes, then propose those changes back to the original through a pull request.

For `neighborhood-meals`, you probably cloned directly from a repository you own or have write access to. No fork involved. But if you ever see the AI reference an `upstream` remote in addition to `origin`, that means the project was forked — `upstream` points to the original, `origin` points to your fork.

You don't need to manage this. The AI handles it. But when you see `upstream` in a git command, you'll know what it means.

---

## What the README Does

The `README.md` in `neighborhood-meals` is not decoration. It's the front door of the project.

When an AI coding tool starts working on a project, one of the first things it reads — if it has file access — is the README. The README tells it what the project does, how to set it up, what the main commands are, and often what the expected environment looks like. A well-written README gives the AI enough context to make reasonable decisions about what to change and what to leave alone.

For you, the README is orientation. When you can't remember what the backend entry point is, or how to run the tests, or what environment variable you need to set — the README usually has it. The AI will often refer to it. When it does, that's not a stall. That's the AI using available context.

> **Don't Do This:** Don't ignore the README because you're having the AI set things up. The README describes the intended state of the environment. If the AI's setup diverges from the README — installs a different version, skips a step — that's worth noticing. The README is your reference for "what this project is supposed to look like."

---

## Why the Remote Matters for AI-Assisted Work

Your AI coding tool runs commands on your machine. It edits local files, commits to your local git history. But collaboration — getting changes to a teammate, opening a pull request, deploying — requires GitHub. That means pushing to `origin`.

If `origin` isn't configured, or if the machine isn't authorized to push to it, the AI hits a wall. It can keep working locally, but nothing reaches GitHub. That's a limited loop: the AI does work, nothing ships.

When the AI encounters a push failure, it will usually tell you what's wrong — `remote: Repository not found` if the URL is incorrect, or the permission denied error if authentication isn't set up. Those are fixable problems, but they require your machine to be set up correctly. The AI can diagnose them. It can't fix them without your help on the auth side.

> **What the AI Does:** When the AI needs to push and the remote isn't configured, it will run `git remote add origin <url>` with the correct GitHub URL. Once the remote is set, it pushes. If authentication fails after that, you'll see an error — and that's the subject of the next chapter.

---

## What You Own Here

You don't need to manage `origin` manually. The AI handles it. What you need to own is the distinction: when you see changes locally, they are not on GitHub until something pushes them. If you're looking at `neighborhood-meals` on GitHub and not seeing a recent change your AI made, the question isn't "why didn't it save" — it's "did we push."

Ask the AI. It'll check.

---

Before the AI can push to that remote, your machine needs permission — and that's what the next chapter is about.
