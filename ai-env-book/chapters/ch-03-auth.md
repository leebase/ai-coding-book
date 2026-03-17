# Chapter 3: Getting Your Computer Authorized

The AI tried to push your changes to `neighborhood-meals` and got this:

```
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Nothing was pushed. GitHub rejected the connection before it even started.

This isn't a git problem. Git did everything right — it built the commit, it connected to the right URL, it tried to authenticate. GitHub looked at your machine and said no.

---

## Why GitHub Requires Proof

GitHub doesn't recognize your machine by address. Anyone can make a TCP connection to GitHub's servers. What GitHub needs is proof that the machine making requests is actually allowed to access this repository.

For a long time, that proof was a username and password. You'd push, GitHub would ask who you are, you'd type your credentials. GitHub stopped accepting account passwords for git operations in 2021. The reason: passwords can be phished, reused across sites, guessed. GitHub moved to credential models designed for machine-to-machine communication: SSH keys and personal access tokens.

Your AI coding tool is a machine making requests on your behalf. It needs one of these credential models set up on your machine, or it can't push.

---

## SSH Keys: The Mental Model

SSH stands for Secure Shell — a protocol for encrypted communication between machines. The authentication works like a matched lock and key.

When you generate an SSH key pair, you get two files: a private key and a public key. The private key stays on your machine and never leaves. The public key is a string you give to GitHub. When your machine connects to GitHub, GitHub sends a challenge. Your machine uses the private key to answer it. GitHub checks the answer against the public key it has stored. If they match, you're in.

No username. No password. No prompts.

The private key is usually stored at `~/.ssh/id_ed25519` (or `~/.ssh/id_rsa` for older keys). The public key is the corresponding `.pub` file. You give GitHub the contents of the `.pub` file — not the private key. Never the private key.

The practical upshot: once the public key is on GitHub and the private key is on your machine, every git operation over SSH just works. The exchange happens invisibly. The AI pushes, GitHub checks, the handshake completes.

> **Don't Do This:** Do not regenerate your SSH key pair after setting it up unless you have a specific reason. Regenerating creates a new key pair, which means the old public key on GitHub no longer matches. Every push will fail until you update GitHub with the new public key. The AI may regenerate keys if you ask it to "fix" auth by starting over — confirm this is what you want before it does.

---

## HTTPS Tokens: The Alternative

The other option is HTTPS with a personal access token (PAT). You'll notice this if the project's remote URL looks like:

```
https://github.com/yourname/neighborhood-meals.git
```

rather than:

```
git@github.com:yourname/neighborhood-meals.git
```

The `git@` prefix means SSH. The `https://` prefix means HTTPS.

With HTTPS, git needs a username and a token instead of a password. A personal access token is a long string of characters you generate on GitHub — think of it as a purpose-built application credential. It has specific permissions (read-only, write, etc.) and can be revoked without changing your account password.

On macOS, git can store HTTPS tokens in the system keychain so you don't have to paste them every time. The AI may set this up for you with `git credential-helper osxkeychain` or similar. Once configured, it behaves the same as SSH — the credential exchange happens invisibly.

SSH is more common for developer machines. HTTPS tokens are common in CI systems and automated environments. For `neighborhood-meals` running locally, SSH is the default setup you'll likely see.

---

## How to Check If Auth Is Set Up

Before the AI tries to push and fails, it can verify auth with one command:

```
ssh -T git@github.com
```

This sends a test connection to GitHub using SSH. If auth is working, GitHub responds with:

```
Hi yourname! You've successfully authenticated, but GitHub does not provide shell access.
```

That message looks odd but it's correct. GitHub is confirming who you are and reminding you that SSH access to GitHub is for git operations only — not for interactive shell sessions.

If auth is not working, you get the same error as the push failure:

```
git@github.com: Permission denied (publickey).
```

> **What the AI Does:** The AI will run `ssh -T git@github.com` as a diagnostic step when it suspects an auth problem. If the test fails, it will walk you through generating an SSH key pair and adding the public key to GitHub. The steps involve: running `ssh-keygen` to create the key pair, copying the public key with `cat ~/.ssh/id_ed25519.pub`, and going to GitHub's SSH key settings page to paste it in.

> **Watch For:** After you add the public key to GitHub and rerun `ssh -T git@github.com`, you should see the "Hi yourname!" confirmation. That's the signal that auth is fixed. The AI can then push without needing anything else.

---

## Walking Through the Setup

If you hit the permission denied error and need to set up SSH from scratch, the AI will run something like this sequence:

First, check if any SSH keys already exist:

```
ls ~/.ssh
```

If you see `id_ed25519` and `id_ed25519.pub` already, the key pair exists. The issue might be that the public key isn't on GitHub yet — or that you're using a different account than you think.

If there are no keys, the AI will generate them:

```
ssh-keygen -t ed25519 -C "your@email.com"
```

This creates the key pair at `~/.ssh/id_ed25519`. It will ask for a passphrase — you can leave it empty for local development use, or set one for extra security. The AI will handle the prompts.

Then it reads the public key:

```
cat ~/.ssh/id_ed25519.pub
```

The output is a long string starting with `ssh-ed25519`. That entire string gets added to GitHub at: Settings → SSH and GPG keys → New SSH key.

After you paste it in and save, the `ssh -T git@github.com` test should succeed.

---

## One-Time Setup

This is a one-time configuration per machine. Once SSH is working on your laptop, you don't touch it again. The AI won't ask you to redo it. If you get a new machine, you do it again — either transfer the key or generate a new one and add it to GitHub.

The frustrating thing about auth errors is that they feel like code problems because they happen while you're doing code work. They're not. They're infrastructure configuration, and they have clean binary outcomes: either the key is set up and pushes work, or it isn't and pushes fail. There's no partial state to diagnose.

---

## What You Own

Two things.

First, following the setup steps. The AI will guide you through them, but it can't add the public key to GitHub on your behalf. That requires you to be logged into GitHub in a browser. The AI will tell you exactly what to paste and where.

Second, not undoing the setup. The two ways auth breaks after being correctly set up: regenerating the key pair (new private key, old public key on GitHub no longer matches), or changing the remote URL from `git@github.com:...` (SSH) to `https://github.com/...` (HTTPS) without configuring the HTTPS credential helper. Either change breaks auth silently — git will try to connect and fail, and the error will look the same as if nothing was ever set up.

If the AI suggests changing the remote URL for some reason, ask why. That's not a routine operation.

> **Key Takeaway:** SSH auth is a matched key pair: the private key on your machine, the public key on GitHub. The test command is `ssh -T git@github.com`. Success looks like "Hi yourname!" — that line confirms the handshake worked. Setup is one-time per machine.

---

Now that the machine is authorized, the next thing you'll notice is that the AI rarely works directly on `main` — it creates branches, and sometimes something called a worktree.
