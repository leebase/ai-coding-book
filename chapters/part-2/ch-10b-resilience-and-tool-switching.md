# Chapter: When Credits Run Out — Resilience and Tool Portability

> *Note for continuity pass: insert as Ch 11, renumber current Ch 11–14 → Ch 12–15.*

You are halfway through implementing a feature. The agent is mid-run, editing files, running tests. Then: rate limit. Or the browser crashes. Or you realize you burned through this month's Antigravity credits faster than expected, and the next 24 hours are going to be slow.

In a normal AI-assisted workflow, this is where you lose momentum — sometimes the thread entirely. You wait for the limit to reset, or you open a new session and spend the first fifteen minutes reconstructing context that existed perfectly well before the interruption. You paste fragments from memory. You re-explain decisions you made two weeks ago. Sometimes you just start fresh and accept the cost.

In an AgentFlow workflow, this is a five-minute problem. You open a different tool, paste two files, run the handoff test, and continue. The agent changes. The project state does not.

This chapter is about why that works, what the tool landscape actually looks like at different price points, and how to structure your workflow so that no single tool's credit limit, rate cap, or outage can stop you.

---

## The Hidden Assumption

Most developers who use AI coding tools make one assumption implicitly: this tool is the tool. The session history, the in-context understanding, the workflow — it all lives in one place. When that place becomes unavailable, the work stops.

AgentFlow challenges that assumption at the architectural level. Everything the AI needs to continue your work is in files: `context.md` holds the project state. `decisions.md` holds the constraints. `sprint-plan.md` holds the scope. Skill files hold your working conventions. These are plain markdown files in your repository. They are not inside any AI tool. They belong to you.

This means the AI session is interchangeable. Any agent that can read these files and understand markdown can pick up where the last one left off. The agent is an executor, not a memory. The memory is in the files.

**You are not locked into any tool. You are locked into your methodology.** And the methodology runs anywhere.

---

## The Failure Path: A Crash Without Context

Open Antigravity and start a session without context.md in place. Implement two or three exchanges — maybe you are adding a new command, maybe you are debugging something. The session is going well.

Now imagine the tab crashes. Or the rate limit fires. Or you come back tomorrow and open a new session.

Type:

```
What is the current state of the task manager? How many tests are passing?
What was the last thing we were working on?
```

> **What the Agent Will Do:** It will apologize. It has no memory of the previous session. It cannot answer any of those questions. If you had a test count in your head, you are the backup. If you remembered the last decision, good. If not, you are either guessing or reading through the codebase to reconstruct what you already knew.

This is not a hypothetical failure. It is the default behavior of every AI coding tool in existence. Sessions are stateless. The agent's working memory ends when the session ends.

> **Watch For:** How long it takes to reconstruct a productive starting state. Count the exchanges. Count the minutes. This is the cost you are paying every time you do not maintain context.md.

---

## The Recovery Protocol

When a session ends unexpectedly — crash, rate limit, credits exhausted — do this:

**Step 1: Commit what exists.**
Before switching tools, make sure the current state of the code is committed to git. A half-implemented feature is fine — commit it with a descriptive message: `WIP: add export command, tests failing, see context.md`. The commit is a checkpoint.

**Step 2: Update context.md.**
If you were mid-session, context.md may be slightly stale. Spend sixty seconds updating the "Current Work" section: what was in progress, where it stopped, what the next step is. If the agent was in the middle of something when the session ended, note it.

**Step 3: Open the new tool.**
Start a new session in the replacement tool — whether that is a different AI product, a different account on the same product, or the same tool after the rate limit resets.

**Step 4: Run the handoff prompt.**
Paste the contents of `context.md` and `decisions.md` into the new session, then ask:

```
Read these two files. Then tell me:
1. What is the current state of the project?
2. How many tests are passing?
3. What are we working on right now?
4. What constraints apply to this work?
```

> **Watch For:** The agent answering correctly from the files alone, without you adding anything. If it answers all four correctly, you are ready to continue. If it misses something, your context.md has a gap — add the missing information before proceeding.

**Step 5: Continue.**
Issue the next prompt — the same requirement or increment you were working on when the session ended. Reference the WIP commit if relevant. Proceed.

Five steps. Most of them take less than a minute. The handoff test (Step 4) is the only one that requires attention, and it doubles as verification that your context files are complete.

---

## The AI Tool Landscape

Understanding where to switch requires understanding what you are switching to. At any given moment in 2024–2026, there are three major platforms worth knowing at the free and ~$20/month tier: Claude, ChatGPT, and Gemini. Each has different credit generosity, different strengths, and different features that matter for different kinds of work.

### Free Tiers

Every platform offers a free tier. None of them are unlimited. All of them are more useful than nothing, and all of them are substantially more productive when you bring your own context.

Free tiers are best used for:
- Running the handoff test when you need to verify context
- Short, targeted prompts — fixing a specific bug, reviewing a small function
- Experimenting with a new tool before committing credits to it

Free tiers are not suited for:
- Long implementation sessions
- Multi-step agent runs that require sustained context
- Anything that requires the agent to hold a large working context across many exchanges

If you are on a zero-budget constraint, rotate across free tiers and keep your sessions short and targeted. AgentFlow's incremental structure (one requirement, one session, one verified result) is naturally compatible with free tier limitations — each session is bounded by design.

### Claude (~$20/month — Pro tier)

Claude's Pro tier is conservative with agentic coding credits compared to the others. If you are running extended Antigravity-style sessions, you will hit limits faster than you might expect. Budget accordingly — use Claude for the tasks where it adds the most unique value.

**Where Claude leads:**

*Reasoning quality.* Claude consistently produces code with careful attention to edge cases, clear variable naming, and sensible error handling. For complex logic — parsing, data transformation, multi-step validation — Claude tends to produce cleaner first drafts that require less cleanup.

*Document collaboration.* Claude's Projects feature and its document-collaborative capabilities make it unusually strong for any work that mixes writing with code. If you are producing documentation, spec documents, decision logs, or anything that requires well-structured prose alongside implementation work, Claude handles the cognitive switch between "write this explanation" and "implement this function" better than most. For this book, for example — Claude is the right tool.

*Long-context fidelity.* When you paste a long context.md plus a decisions.md plus a skill file into Claude, it tends to hold and respect those constraints across the full session. The decisions you specified in the context are the decisions the agent applies, consistently.

**How to use Claude efficiently at $20/month:** Reserve it for high-reasoning tasks — the sessions where you need careful implementation of complex logic, or where you are producing artifacts that need to be both technically correct and well-written. For straightforward CRUD-style feature work, use ChatGPT or Gemini where your credits will go further.

### ChatGPT Plus (~$20/month — Plus tier)

ChatGPT Plus is notably more generous with coding credits at the $20 tier. For extended implementation sessions — the kind where the agent is running tests, editing multiple files, and iterating — ChatGPT Plus lets you go further before hitting limits.

**Where ChatGPT leads:**

*Coding session stamina.* If you are in a deep implementation sprint, ChatGPT Plus is likely your most productive $20 spend. The credit budget is generous enough for sessions that would exhaust other tools' limits.

*Codex Web.* This is genuinely novel. OpenAI's Codex Web interface allows you to kick off agent tasks from a mobile device — review a pull request, start an implementation, trigger a test run — and return to it on desktop when it finishes. For a developer who has fifteen minutes between meetings, or wants to queue up work from their phone on the commute in, this is a material workflow advantage. You can start a PR review from your phone, have the agent produce a structured review with specific suggestions, and read the result on your laptop when you sit down. The work does not require you to be at a desk.

*Model options.* GPT-4o and the o-series reasoning models are available at Plus, giving you flexibility between speed (4o) and deep reasoning (o1/o3) depending on what the task requires.

**How to use ChatGPT efficiently at $20/month:** Use it as your primary workhorse for implementation sprints. When you hit a rate limit elsewhere, open ChatGPT. Use Codex Web for async work — kick off a task, do something else, return to the result.

### Gemini Advanced (~$20/month — Google One AI Premium)

Gemini's $20/month tier is actually a Google One AI Premium subscription, which bundles substantially more than just AI coding assistance. This is the platform with the broadest feature surface area at the $20 price point.

**Where Gemini leads:**

*Ecosystem integration.* If your work involves Google Workspace — Docs, Sheets, Drive, Gmail — Gemini integration at this tier connects AI assistance directly into those tools. Draft a spec in Google Docs with AI help, generate a summary of your project status in Sheets, ask questions about your codebase in a format that connects back to your Drive files. For teams already in the Google ecosystem, this integration removes friction that other tools require workarounds for.

*NotebookLM.* This is one of the most underrated tools in the AI landscape. NotebookLM allows you to create a research notebook from your documents — upload your spec files, your decisions.md, your chapter drafts, your code — and ask questions across all of them simultaneously. "What features have we explicitly decided not to implement, and why?" is a question NotebookLM can answer from your actual files rather than from the AI's training data. For long projects with a lot of accumulated context, NotebookLM is a powerful complement to the standard chat interface.

*Antigravity.* Antigravity is a Google DeepMind product, and at the Google One AI Premium tier you have access to the same Gemini models that power Antigravity's agent capabilities. This means your coding sessions in Antigravity and your chat sessions in Gemini Advanced are running on the same underlying model — the context you build in one is structurally compatible with how the other reasons.

*Raw model capacity.* Gemini's context window and multimodal capabilities (code, text, images, and increasingly structured data) give it flexibility for tasks that require processing large amounts of existing material.

**How to use Gemini efficiently at $20/month:** Use Antigravity for hands-on coding sessions. Use NotebookLM to reason across your accumulated project documents. Use Gemini chat for ecosystem-integrated tasks — anything touching Google Docs or your Drive. The three products, used together, cover more workflow surface area than any other $20 tier.

---

## The $200/Month Professional Tier

At $200/month, the math changes.

Claude Max, ChatGPT Pro, and comparable tiers at this price point offer substantially higher rate limits, priority access to the most capable models, and in some cases access to experimental features not available at the lower tier. The practical difference is not just quantity — it is the ability to run extended, uninterrupted sessions that would hit limits on the $20 tier.

For a developer working with AI tools daily on a professional project — not for an hour a week but for several hours a day — $200/month is often the right answer. The productivity gain from uninterrupted sessions, combined with access to the best models, typically pays for itself quickly in reduced friction and higher-quality output.

That said, even at $200/month, the portability principles apply. You still want context.md maintained. You still want to be able to switch if a tool has an outage. You still want your methodology to be the constant, not your vendor.

The difference at $200/month is that the credit pressure largely disappears, and the tool rotation strategy becomes a choice rather than a necessity.

---

## The Weekend Warrior Strategy

If you are a hobbyist, an open-source contributor, or someone building side projects on a limited budget, the free and $20/month tiers are entirely viable — with the right workflow.

The key insight: AI credits are not scarce if you are disciplined about what you do with them. The failure mode that burns credits fastest is undirected exploration — vague prompts, iterative correction, context reconstruction. AgentFlow's structure — one requirement, one scoped session, one verified result — is inherently credit-efficient. Every prompt has a purpose. Every session ends with committed, tested code.

A practical weekend warrior setup:
- **Primary tool**: Antigravity (Gemini, free tier or $20/month) for hands-on coding sessions
- **Backup tool**: ChatGPT Plus ($20/month) for when Antigravity's rate limit fires — especially for longer implementation runs where ChatGPT's credit budget goes further
- **Reasoning tasks**: Claude ($20/month) for complex logic, document work, and anything that benefits from careful analysis
- **Total monthly spend**: $40 for two $20 subscriptions, or $20 for one and free tier on the other

With AgentFlow's context files in place, the tool rotation is invisible to the project. Monday you are in Antigravity. Tuesday the rate limit fires and you switch to ChatGPT. Wednesday you come back to Antigravity. The project has no idea. The context.md knows exactly where you are.

---

## A Full Tool-Switch Walkthrough

Here is the scenario in concrete terms.

You are in Antigravity. You are halfway through implementing the `export` command — Increment 2 of 3, adding CSV output. The agent has modified `tasks.py` and is mid-run on the tests when Antigravity hits your rate limit for the day.

**Step 1:** Open your terminal. Commit what exists:

```bash
git add tasks.py tests/test_tasks.py
git commit -m "WIP: export CSV mid-implementation, tests failing on csv format — see context.md"
```

**Step 2:** Update context.md — add one line to "Current Work":

```
WIP: Increment 2 of export command (CSV output). tasks.py modified,
tests/test_tasks.py has new tests. Tests failing — csv format not yet
matching expected output. Next: fix output format in export_csv() function.
```

**Step 3:** Open ChatGPT (or Claude, or whichever tool you are rotating to). Start a new conversation.

**Step 4:** Run the handoff prompt:

```
I'm switching AI tools mid-session due to a rate limit. Here are two files
that describe my project — read them carefully before we continue.

[paste context.md contents]

[paste decisions.md contents]

Tell me:
1. What are we building?
2. What is the current state of the implementation?
3. What is the next step?
4. What constraints apply to output format and error handling?
```

> **Watch For:** The agent correctly identifying the WIP state, the failing tests, the export command context, and the key decisions (error behavior, output format consistency). If it gets these right from the files, you are ready.

**Step 5:** Continue with the increment:

```
We're mid-implementation on the export command, Increment 2: CSV output.
tasks.py has been modified. tests/test_tasks.py has new tests that are
currently failing because the CSV format doesn't match the expected output.

The current tasks.json schema is:
{"id": int, "description": str, "done": bool, "priority": str, "due_date": str|null}

Fix the export_csv() function in tasks.py so the CSV output format is:
id,description,done,priority,due_date
1,Buy groceries,False,medium,
2,Fix bug,False,high,2026-04-01

Run the tests and confirm they pass.
```

The new agent picks up exactly where Antigravity left off. It has the project context, the constraint history, and the specific current task. The rate limit interruption cost you less than ten minutes.

---

## Debrief

The tool landscape at $0–$20/month is genuinely capable. The gap between free-tier AI coding and professional-tier AI coding is not primarily about model quality — it is about credit volume and feature breadth. The models at the $20 tier are good. The question is how many sessions you get before the limit fires.

AgentFlow changes the calculation in two ways. First, it makes every session more efficient — fewer wasted prompts, cleaner context, less reconstruction overhead. Second, it makes tool switching seamless — because the project state lives in files, not in any agent's memory.

**The practice is the constant. The tool is the variable.** Any developer who ties their workflow to a single AI tool has a single point of failure — credit limits, outages, model degradation, pricing changes. Any developer who ties their workflow to a methodology has none of those problems. The methodology runs anywhere.

This is the full value of context.md, decisions.md, and the Update stage of the loop. Not just continuity between your own sessions — continuity across tools, across devices, across collaborators, and across whatever the AI tool landscape looks like twelve months from now.

In Chapter 11, you will use this same portability to run two agents in parallel — one in Antigravity, one potentially in a different tool — with a shared context file coordinating their work. The tool-agnostic architecture that enables crash recovery also enables multi-agent coordination. Same principle, different scale.

---

*Your context file is more durable than any AI tool's memory. Build accordingly.*
