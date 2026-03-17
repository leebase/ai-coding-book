# Book 3 Lessons Learned — Agents Within Claude Code

> Running log of observations from writing ai-env-book using Claude Code agents.
> These lessons inform Book 3: using agents within Claude Code/Codex before
> reaching for external orchestration.

---

## The Symphony Experiment (What Not To Do First)

**What happened:** Set up Symphony + Linear for fully automated overnight book writing.
Consumed 1.17M tokens. Produced zero chapter artifacts.

**Root cause:** CON-38 (the first issue) failed on attempt 1 with a runtime error and
retried until exhausted. Symphony had no fallback, no human-readable error surface,
and no way to recover. The entire pipeline stopped at issue 1.

**Lesson:** External orchestration adds a failure mode at every layer of the stack
(agent runner, issue tracker, workspace sync, completion guard). When any layer fails,
the whole system stops. For a new project, the operational cost of that stack is not
worth it until you have verified that the underlying agent work is reliable.

**Book 3 angle:** Start with what Claude Code already gives you. The Agent tool,
worktrees, and task decomposition are built in and do not require a separate
orchestration system to run.

---

## Skill Files As Context Injection

**Observation:** The five skill files (scenario-thread, book-voice, env-explainer,
new-dev-validator, warp-expert) replaced what Symphony would have injected via the
issue body. Putting them in the repo meant any agent — in any session, in any tool —
could load them by reading the file.

**Lesson:** Good skill files are portable. They are not tied to a specific orchestrator.
Claude Code agents, Symphony agents, and manual sessions all load the same files.

**Book 3 angle:** Write skill files before writing agents. The skill file is the
reusable unit. The agent just reads it.

---

## Parallelization Within Claude Code

**Observation:** Claude Code's Agent tool allows parallel subagent calls in a single
message. Chapters within a part share narrative state, but chapters across parts
(Git vs Python vs Node vs Warp) are largely independent once the scenario-thread is
locked.

**Pattern used:**
- Introduction: foreground (must complete before parallelizing — sets the frame)
- Part 1 (Ch 1-5) + Part 2 (Ch 6-8): parallel background agents
- Part 3 (Ch 9-11): parallel background agents
- Part 4 (Ch 12-15): parallel background agents
- Conclusion: foreground (needs all chapters done to summarize)

**Lesson:** The right unit for parallelization is not "every chapter" — it is
"chapters that share no narrative state." The scenario-thread file makes this
explicit: each part's state is defined independently.

**Book 3 angle:** Identify the dependencies first. Write a dependency map before
spawning agents. Unconstrained parallelism produces inconsistent output.

---

## Self-Review Pass Within the Agent

**Observation:** Rather than separate Symphony issues for review (editor-and-qa agent),
baking a new-dev-validator self-check into the writing agent's prompt produces a
tighter loop with less orchestration overhead.

**Trade-off:** A single agent reviewing its own work catches the obvious issues
but may miss blind spots a truly separate agent would catch. For a solo project at
this quality level, the trade-off is acceptable.

**Lesson:** Two-agent review (writer + editor) adds quality but multiplies the
issue count and orchestration complexity. For most projects, a single agent with an
explicit review checklist in the prompt is enough until you have evidence you need
more.

**Book 3 angle:** Show the single-agent-with-checklist pattern first. Introduce the
separate reviewer agent as a "when to level up" step, not the default.

---

## Prompt Size vs. Agent Reliability

**Observation:** Each chapter-writing agent received a large prompt (4,000–6,000 tokens)
containing all relevant skill file content inline. Agents completed their assigned chapters
reliably with no failures — contrast with Symphony's CON-38 which failed immediately.

**Why it worked:** The agent had everything it needed in a single context. No workspace
sync, no external state, no completion guard, no issue tracker integration. Read prompt,
write files, done.

**Trade-off:** Large prompts cost more per run and can't be cached as effectively. For
a book project, this is fine. For a high-volume production pipeline, it would matter.

**Book 3 angle:** Inline context injection is the beginner pattern. Skill files in the
repo are the intermediate pattern. External orchestration is the advanced pattern —
and it adds real overhead. Show the progression, don't jump to the end.

---

## Word Count Variance Across Agents

**Observation:** Chapters targeting 1,500–2,500 words came in at 1,274–1,630 words.
Parallel agents produced consistently shorter chapters than the upper target.

**Pattern:** Agents tend toward the minimum viable response. When the spec says
"1,500–2,500 words," agents aim for ~1,400–1,600. The lower bound anchors more
than the upper bound.

**Mitigation:** Set the lower bound explicitly ("at least 1,500 words of prose,
not counting code blocks") or add a word count check with instruction to expand
before saving.

**Book 3 angle:** Agent outputs cluster toward the minimum of any range you give.
If quality requires a floor, enforce it explicitly — don't rely on the agent
to self-expand.

---

## Parallelization Results

**What ran in parallel:**
- Part 1 (Ch 1–5) and Part 2 (Ch 6–8) launched simultaneously
- Part 3 (Ch 9–11) launched after Part 2 completed (no real dependency, could have been parallel)
- Part 4 (Ch 12–15) launched as soon as Part 4's domain was unblocked

**Result:** 15 body chapters written across ~4 parallel agent runs. Introduction and
Conclusion ran foreground serially. Total wall time significantly less than serial would
have been.

**No conflicts:** Each agent wrote to distinct files. No race conditions, no merge
conflicts, no coordination overhead.

**Book 3 angle:** File-level parallelism within Claude Code is safe and easy. The unit
of parallelism is the file (or set of files). Define non-overlapping output files and
agents can run fully independently.

---

*Updated as writing progresses. Add new entries above this line.*
