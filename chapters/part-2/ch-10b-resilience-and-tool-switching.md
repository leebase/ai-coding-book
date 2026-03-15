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

Paste the contents of `context.md` and `decisions.md` into the new session. Then send this template exactly:

> **Handoff Prompt — copy this**
>
> *Paste context.md and decisions.md above, then send:*
>
> Read these two files. Then tell me:
> 1. What is the current state of the project?
> 2. How many tests are passing?
> 3. What are we working on right now?
> 4. What constraints apply to this work?

> **Watch For:** The agent answering correctly from the files alone, without you adding anything. If it answers all four correctly, you are ready to continue. If it misses something, your context.md has a gap — add the missing information before proceeding. This step doubles as a diagnostic: a passing handoff test means your context files are complete enough to sustain the session.

**Step 5: Continue.**
Issue the next prompt — the same requirement or increment you were working on when the session ended. Reference the WIP commit if relevant. Proceed.

Five steps. Most of them take less than a minute. The handoff test (Step 4) is the only one that requires attention, and it doubles as verification that your context files are complete.

---

## How to Evaluate AI Tools for Tool Switching

Understanding where to switch requires knowing what to evaluate. The specific tool landscape changes — prices shift, new products appear, credit policies update. What does not change are the properties that make a tool useful for a given type of work. Evaluating tools by their properties gives you a framework that ages better than any point-in-time comparison.

**Four criteria that matter when evaluating AI coding tools for AgentFlow compatibility:**

**Reasoning quality.** How carefully does the tool approach complex code? High-reasoning tools handle edge cases, produce clean variable names, and write error handling that makes sense on first read. They produce cleaner first drafts that require less correction after review. This matters most for sessions involving intricate logic, multi-step validation, or document-and-code work where both outputs need to be correct and clear.

**Session stamina.** How many exchanges can you sustain before credit limits fire? For an implementation sprint — agent running tests, editing multiple files, iterating on output — session stamina is the primary budget constraint at the $20/month tier. A tool with excellent reasoning and limited credits may be less useful as your primary workhorse than one with generous credits and solid (if not exceptional) reasoning.

**Ecosystem integration.** Does the tool connect to software you already use? For developers in Google Workspace, AI integration into Docs, Sheets, and Drive removes friction that other tools require workarounds for. For a developer who works entirely in the terminal, ecosystem integration is less relevant — what matters is what happens in the editor.

**Context handling.** When you paste a long context.md, decisions.md, and a skill file into the session, does the tool hold and respect those constraints throughout? Some tools drift from stated constraints as the session lengthens. You want the decisions you specified at the start of the session applied consistently at exchange thirty. The handoff test (Step 4 of the recovery protocol) is your practical diagnostic for this: if the agent answers all four questions correctly from your context files alone, it is handling context well enough for the task.

---

**How these criteria cash out at the free and ~$20/month tier:**

*On reasoning quality* — Claude Pro (approximately $20/month) stands out. For complex logic, data transformation, and anything that mixes writing with code (documentation, spec documents, decision logs), it tends to produce cleaner first drafts that are easier to review and maintain. Its document-collaborative capabilities make it unusually strong for any session where the output needs to be both technically correct and well-written. The trade-off: its coding credit budget is more conservative than the alternatives. Reserve it for the sessions where reasoning quality pays off most.

*On session stamina* — ChatGPT Plus ($20/month) leads. For extended implementation sprints, the credit budget goes further than comparable tiers. ChatGPT Plus also offers Codex Web — the ability to kick off agent tasks from a mobile device, start a PR review from your phone, and return to the result on your laptop. No other $20 tier offers async mobile-to-desktop workflow at this quality level. Use it as your primary workhorse for implementation sprints; use Codex Web for async work between meetings.

*On ecosystem integration* — Gemini Advanced (Google One AI Premium, approximately $20/month) leads — and leads substantially. The tier includes AI integration across Google Workspace (Docs, Sheets, Drive), NotebookLM for cross-document reasoning (ask questions across your spec files, decisions.md, and code simultaneously), and Antigravity for hands-on coding sessions — all running on the same underlying model. For teams already in the Google ecosystem, this integration removes friction that other tools cannot match at this price point.

*On context handling* — this varies by tool and task complexity. Run the handoff test every time you switch. A tool that passes it is ready for the session.

**The free tier.** Every platform offers one. None are unlimited, and none are suited for extended implementation sessions. Free tiers are most useful for running the handoff test when you need to verify your context files, short targeted prompts (a specific bug fix, a small function review), and evaluating a new tool before committing credits. If you are on a zero-budget constraint, AgentFlow's incremental structure — one requirement, one scoped session, one verified result — is naturally compatible with free tier limitations. Each session is bounded by design.

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

> **Handoff Prompt — copy this**
>
> *Paste context.md and decisions.md above, then send:*
>
> I'm switching AI tools mid-session due to a rate limit. Here are two files
> that describe my project — read them carefully before we continue.
>
> Tell me:
> 1. What are we building?
> 2. What is the current state of the implementation?
> 3. What is the next step?
> 4. What constraints apply to output format and error handling?

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
