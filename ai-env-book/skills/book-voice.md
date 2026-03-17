# Skill: Book Voice — ai-env-book

> This skill is specific to ai-env-book. Do not confuse it with the book-voice
> skill in ai-coding-book, which targets experienced developers.

---

## Who You Are Writing For

A new developer. They have written some code — maybe from tutorials, maybe from
a bootcamp, maybe self-taught. They have started using an AI coding tool.
But every time they try to work on a real project, they hit walls that have
nothing to do with the code: the git state is confusing, the environment is
wrong, npm is broken, something requires a password they don't have.

They are not stupid. They are missing a mental map of the infrastructure their
code runs in. This book gives them that map.

They do not need to be impressed. They need to be shown.

---

## The Register

**Patient but not condescending. Peer, not professor.**

Write as someone who remembers hitting these exact walls. Not as someone
lecturing about them from above.

- Use "you" freely. This is a conversation.
- Short sentences when the point is sharp. Expand when the concept requires it.
- Name the frustration before you solve it. The reader has seen these error
  messages and felt stupid. Acknowledge that they are confusing — because they
  are — before explaining why.
- Do not apologize for the reader's confusion. Don't say "don't worry" or
  "it's actually simple once you understand it." Just explain it.

---

## What This Book Argues

Every chapter serves this thesis:

> You don't need to be a sysadmin. You need to understand your environment well
> enough that when something breaks — or when you're asking an AI to set something
> up — you know what you're looking at.

Let this surface naturally. Do not lecture it. Show the reader a wall they
recognize, explain what it actually is, and show them what their AI does with it.

---

## The Pattern

Every chapter follows this shape:

1. Show the error or confusion first — before explaining anything
2. Give the mental model in plain language
3. Show what the AI does to resolve it
4. Tell the reader what they need to own to not undo the fix

The reader's goal is **recognition, not recall**. They do not need to memorize
commands. They need to recognize what they're looking at and know whether to let
the AI handle it or ask for help.

---

## What to Avoid

**Tutorial condescension**: "First, let's learn about git! Git is a version
control system that..." — No. The reader knows git exists. They're confused
about what it's doing. Start there.

**Command memorization mode**: Listing every flag, every option, every edge
case. The AI will run the commands. The reader needs the mental model, not
the man page.

**Cheerleading**: "Once you master this, you'll be amazed at what you can do!"
— No. Just explain the thing.

**Scare framing**: "If you get this wrong, you could lose all your work!" — No.
Accurate stakes, stated plainly. Not drama.

**Padding**: Do not warm up to the point. Start with the wall.

---

## Callout Boxes

Use sparingly. Reserve for:

- `> **What the AI Does:**` — before showing an AI action, so the reader
  knows what to expect and what to look for
- `> **Watch For:**` — when a specific output confirms the fix worked
- `> **Don't Do This:**` — when a common mistake undoes what the AI just fixed
- `> **Key Takeaway:**` — the one thing the reader must leave the chapter knowing

Do not use callouts to restate what was just said.

---

## Chapter Endings

Every chapter ends with one sentence. Not a summary. Not a list. One sentence
that names what the reader just learned and points to the next wall.

Example: "Now that you know what git is actually tracking, the question is where
that tracking lives when you share your code — and that's GitHub."
