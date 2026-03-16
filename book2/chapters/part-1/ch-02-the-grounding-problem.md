# Chapter 2: The Grounding Problem

The article you saved in Chapter 1 has examples in it. Read them again.

They sound specific. There may be a named tool, a named situation, a reference to something a developer would recognize. Now ask yourself: how do you know those examples are real?

You probably cannot check without effort. And you probably did not try — because the prose read with confidence, and confident prose does not usually flag itself as potentially invented. The AI wrote specific-sounding examples because you asked for specific examples, and it has no reliable way to distinguish between "I know this" and "this sounds right." Neither mode produces a different signal in the text.

That is the grounding problem. It is not unique to AI — human writers conflate memory and confabulation too — but AI does it at a scale and fluency that makes it invisible. This chapter shows you how to design around it.

---

## What One Agent Does When It Writes and Researches at Once

Ask any AI agent to write a practical article and it will blend what it knows with what it fills in, because writing and research are the same action when no one separates them. The agent does not have a research phase — it has a generation phase, and generation produces text, whether that text is grounded in something specific or assembled from plausible-sounding components.

This is not a model problem. It is an architecture problem. One agent doing everything has no moment where it commits to what it knows before it starts constructing. You can add "use specific examples" to your prompt and the agent will produce specific-sounding examples. Whether they are specific in the way you meant depends on whether it actually knows them.

---

## The Confabulation Test

Before you build anything, do this: open a fresh agent session — no context from Chapter 1 — and send this prompt:

```
Give me five specific, real examples of documentation
that failed its author. For each one: name the project
or context, describe what the documentation said, and
explain what the author needed six months later that
the documentation did not provide.
```

> **Antigravity:** Click **New Session** to open a fresh conversation. Paste the prompt and send it. Read the five examples the agent produces.

Read what you get. Each example will be specific — named projects, specific situations, plausible failures. Now pick two of them and try to verify them. Search for the project, the context, the specific incident described.

You do not need to prove they are false. You only need to notice how much effort it takes to find out whether they are real. That effort is the gap the grounding problem lives in.

> **Watch For:** At least one example that you cannot verify with a quick search, where the agent's prose gave you no indication of uncertainty. That is a confabulated example written with the same fluency as a real one.

You are not going to fix this by asking the agent to "only use real examples." That instruction does not change what the agent has access to. It changes how it presents what it generates.

---

## What a Researcher Role Does Differently

A role is not a prompt. A prompt tells the agent what to produce. A role defines what the agent *is* during this task — its perspective, its constraints, and its output format. Those three things change what gets produced.

The researcher role does one thing: it commits to what it knows before writing starts. It does this by separating two outputs that one-agent generation blends together:

- Claims the agent can ground — things it knows are real, with enough specificity to verify
- Claims the agent is uncertain about — things it believes are plausible but cannot confirm

That separation is the design. The agent can still produce both kinds of claims in the researcher role. But it has to label them. And the act of labeling forces a kind of honesty that generation alone does not.

The researcher produces `research-notes.md`. Not an article. Not a list of ideas. A structured set of claims, each tagged with its confidence level, ready for a writer who will build something on top of them.

---

## Building `agents/researcher.md`

Create a new file: `agents/researcher.md`. This is your researcher role definition. It should contain:

**What the researcher receives:**
A topic and a question. In this case: the topic is "documentation your future self will actually use" and the question is "what do developers actually get wrong, and what evidence supports that?"

**What the researcher produces:**
`research-notes.md` — a structured document with this format:

```markdown
# Research Notes: [topic]

## Grounded Claims
Claims I can support with specific, verifiable examples.
- [claim] — [specific example or source]

## Plausible Claims
Claims I believe are likely true but cannot ground specifically.
- [claim] — [why I believe this; what would confirm it]

## Uncertain Claims
Things I've seen stated but cannot evaluate.
- [claim] — [why this is uncertain]
```

**The researcher's constraint:**
Do not write prose. Do not draft article sections. Produce only the structured notes above. If you do not have a grounded example for a claim, it goes in Plausible, not Grounded.

Here is what `agents/researcher.md` should say:

```markdown
# Agent: Researcher

You receive a topic and a research question.
You produce research-notes.md — structured notes in the
format provided, with explicit confidence markers.

You do not write prose. You do not draft the article.
Your job is to commit to what you know before writing begins.

Rules:
- Grounded claims require a specific, verifiable example
- Plausible claims require a reason for the belief
- Uncertain claims require an honest flag
- If you cannot ground a claim, it does not go in Grounded
```

> **Antigravity:** Create a new file: in the Explorer pane, right-click your project directory, choose **New File**, name it `agents/researcher.md`. Paste the role definition above. Save it.

---

## Running It

Open a new agent session. Load the researcher role by pasting the full contents of `agents/researcher.md` at the start of the conversation, then follow it with:

```
Topic: How to write documentation your future self will actually use
Question: What do developers actually get wrong about documentation,
and what evidence supports that?
```

> **Antigravity:** Start a **New Session**. In the input field, paste the full text of `agents/researcher.md`, then add a blank line, then add the topic and question above. Send it. The agent will produce structured research notes rather than article prose.
>
> **Watch For:** Output organized into the three sections — Grounded, Plausible, Uncertain. If the agent produces flowing prose instead, the role constraint did not hold. Add an explicit instruction at the top of your role definition: "Your entire output must use the structured format below. Do not write prose paragraphs."

When the output arrives, save it as `research-notes.md`.

Now read it and answer this honestly: which claims in the Grounded section could you verify right now? Pick two and try. Compare this to what you found in the confabulation test.

---

## The Handoff Contract

`research-notes.md` is not just the researcher's output. It is the input for the next stage — the writer who will build the article on top of it. The format you defined matters because of what comes next.

This is a handoff contract: the output of one role is the input specification of the next. The researcher produces something structured because the writer needs to consume something structured. If the researcher produced free-form notes, the writer would have to interpret them, and interpretation introduces the same blending problem you just designed around.

Every role in your pipeline will have a handoff contract. You will design them deliberately, starting now.

---

> **Key Takeaway:** The researcher's job is not to write — it is to commit. Separating that commitment from the writing changes what the writing can trust.
