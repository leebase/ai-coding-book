# Chapter 1: Run the Prompt

You have done this before. You opened an AI agent, described what you wanted, and got back something usable. Maybe you iterated once or twice. Maybe the first output was good enough. Either way, you got the thing done.

That pattern — one agent, one context, one output — is how most developers use AI tools. It works on tasks with clear scope and modest complexity: write this function, summarize this document, generate a test for this class. The agent does it, you check it, you move on.

This chapter asks you to use that pattern on something harder. Not because it will fail spectacularly — it won't. Because the output you get is the most useful thing in this book.

You are going to write an article on a topic that matters: how to write documentation your future self will actually use. It is the kind of task where quality is obvious when it is there and invisible when it is not. You will save what you get, and you will come back to it in Chapter 5. By then you will have built something to compare it to. The difference will be specific and nameable.

For now: run the prompt.

---

## The Task

Documentation is a solved problem in theory and a persistent failure in practice. Every developer knows they should document decisions. Most documentation is either missing, outdated, or present but useless — accurate enough that someone wrote it, not specific enough that anyone reads it twice.

That gap — between documentation that exists and documentation that works — is exactly the kind of problem that looks straightforward to an AI agent. The topic is clear, the audience is defined, the format is familiar. You will get a complete article.

Keep that observation in mind when you read what comes back.

---

## The Prompt

Open a new agent session with a clean context — no prior conversation, no previously loaded files. Then give the agent this prompt, word for word:

```
Write a 1000-word article titled "How to write documentation
your future self will actually use." Write it for developers.
Be practical and direct. Include specific techniques and at
least two concrete examples. Do not use a listicle format —
write in paragraphs.
```

> **Antigravity:** Open Antigravity. Click **New Session** (the **+** icon near your session list) to start a fresh conversation — you should see an empty input field with no prior context. Type or paste the prompt above into the input field and press Enter. Let the agent complete the article without interruption. Do not send follow-up messages.
>
> **Watch For:** A complete article — introduction, several body sections, conclusion — in a single response. If the agent asks a clarifying question instead of writing, reply "just write it" and let it continue. If it produces a bulleted list despite the instruction, note that; the instruction was clear, and a list anyway is itself information about what single-prompt output does with constraints it finds inconvenient.

A note on why the prompt is written this way: length, audience, tone, and format are all specified. A vague prompt produces a vague output, and a vague output is hard to compare to anything. You want something complete enough to be a real artifact. The "no listicle" instruction exists for the same reason — a list hides quality problems behind visual organization.

---

## Reading What You Got

Read the article once, straight through, without editing it.

Then create a new file called `article-v1.md`, paste the full text in, and add this comment block at the very top:

```markdown
<!--
First impressions — one sentence each:
  Voice:
    Does this sound like a specific person wrote it,
    or like anyone could have?
  Examples:
    Are they concrete enough to recognize,
    or generic enough to fit anything?
  Misconception:
    Does this address something developers get wrong,
    or just explain the topic?
  Send test:
    Would you send this to someone whose opinion
    you respect, unchanged?
-->
```

Write one honest sentence in response to each question. Not a critique — an impression. You are not deciding whether the article is good. You are noticing what you notice before you know what to look for.

> **Antigravity:** Copy the full article text from the agent response. In the Explorer pane (left sidebar), right-click your project directory and choose **New File**. Name it `article-v1.md`. Paste the article text, then add the comment block above it — at the very top of the file, before the article begins. Fill in your one-sentence impressions and save (Cmd+S or Ctrl+S).
>
> **Watch For:** `article-v1.md` appears in your file tree with the comment block at the top followed by the article text. Your four impressions are filled in. The file is saved.

One rule: do not iterate on this article. Do not ask the agent to improve it, tighten the tone, or add better examples. Every change reduces the comparison you will run in Chapter 5. The version you have right now — first output, unedited — is the artifact. Its value is in being exactly what one agent produces in one pass.

---

## What You Have

You have a complete article written by one agent in one session. It covers the topic. It has structure. It may have sections you find genuinely useful.

What you may have noticed — or not yet been able to name — is whether it has a voice. Whether the examples are grounded in something specific enough to recognize, or plausible enough to feel real without actually being real. Whether it addresses what developers actually get wrong about documentation, or whether it explains documentation the way documentation articles always explain documentation.

These are not small distinctions. They are the difference between an article someone reads once and an article someone sends to a colleague. You will be able to name them precisely in Chapter 5. Right now you have an impression, four sentences of it, and a file.

That is exactly what this chapter needed to produce.

---

> **Key Takeaway:** Complete is not the same as good. You have a complete article. Keep it exactly as it is — you will need it in five chapters.
