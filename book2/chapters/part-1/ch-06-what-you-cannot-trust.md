# Chapter 6: What You Cannot Trust

The pipeline works. You have evidence of it in `final.md`. The comparison with `article-v1.md` showed specific, traceable improvements — not "better in general" but better in the ways the design intended.

Now for the part the pipeline does not advertise.

Run the pipeline again on a new topic. Read the output. Is it as good as the first run? Maybe. Maybe not. Run it a third time on the same topic as the first run. Is it identical? It isn't. Different claims in the research notes, different examples in the draft, different gaps found by the adversarial reader. The coordinator ran the same stages in the same order with the same roles. The output is different.

This is not a bug. It is a property of how language models work. And it has practical consequences for how much you can trust the pipeline to produce consistent quality without your attention.

---

## What Can Go Wrong

**Stage collapse.** The coordinator instructs the agent to run Stage 1, produce research notes, then stop. Sometimes it runs Stages 1 and 2 together — research notes and draft in the same response — because the agent anticipates what comes next and does not wait for a boundary you defined in the skill file. The stages blend, the handoff contract is skipped, and the writer's output is not constrained by the research notes in the way you intended. This happens more often in long sessions where the coordinator has already explained the full pipeline.

**Role drift.** The researcher produces three Grounded claims and then, in the same response, starts writing article prose because it can see where the research is going. The adversarial reader gives general style feedback alongside the located gaps because it has opinions about the prose and cannot fully suppress them. The roles you defined are constraints, not walls. The base model is still there, underneath, and it will surface when the role constraints are underspecified or when the task is long enough that the agent loses track of which stage it is on.

**Output variance.** The same researcher role, same topic, run twice, produces different Grounded claims. Not because one run is wrong — both may be accurate — but because the model's sampling process is not deterministic. Some runs will be more thorough than others. Some adversarial readers will find three gaps; others will find six. You do not control which run you get.

**Context accumulation.** A full pipeline run is a long session. By Stage 4, the agent is working in a context that contains the full coordinator skill, the research notes, the draft, the adversarial reader's feedback, and whatever stage instructions preceded the current one. Later stages are influenced by earlier stages in ways you did not design. The adversarial reader in Stage 3 may be gentler because it has seen the effort that went into the draft. The revising writer in Stage 4 may be more conservative because it has seen what the adversarial reader flagged.

---

## The Gate Is Your Main Instrument

Every one of these failure modes has the same mitigation: read the output before proceeding to the next stage.

The Stage 1 gate — before writing begins — is the most valuable stopping point because it is the cheapest. If the research notes have drifted into prose, or the Grounded section is thin, catching it before the writer runs saves a full draft. The gate after Stage 3 is the second-most valuable: if the adversarial reader produced style feedback instead of located gaps, address it before the revision runs, or the revision will be fixing the wrong things.

Whether to stop at each gate depends on how well you know the topic, how mature your roles are, and how much your last run looked like your previous one. For a pipeline you have run many times on familiar topics, running straight through is reasonable. For a new topic or a role you just wrote, use the gates.

The gate works only if you know what good output looks like at each stage. A research notes file that is all Plausible claims and no Grounded ones is a signal. An adversarial reader report that runs to ten items for a 900-word article probably caught some noise alongside the signal. A draft that introduces examples not present in the research notes means the writer stepped outside its constraint. These are the things to check. The gate is useless if you confirm it without looking.

---

## What an External Orchestrator Solves

The failure modes above have a common structure: they happen because the AI is also the executor. The coordinator skill is read by the same model that runs the stages. The role constraints are instructions to the model, not walls around it. When the model loses track of a stage boundary or surfaces its base behavior through a role constraint, there is no independent layer to catch it.

An external orchestrator is that independent layer. Instead of a skill file that the AI reads and follows, it is code that programmatically routes work between stages — calling an AI for Stage 1, collecting the structured output, validating it against the expected format, then calling an AI for Stage 2 with that output as input. Each stage runs in an independent context: no accumulated session, no model anticipating what comes next, no role drift across a long conversation. The output of each stage is validated before it becomes the input of the next.

This solves stage collapse (the router controls when stages transition), role drift (each stage is a fresh context with a single role), output variance (you can validate the format before proceeding), and context accumulation (there is no accumulated context to affect later stages).

It also requires building something. The orchestrator is code — not a skill file, not a role definition. It has dependencies, it has failure modes of its own, and it is more work to build than what you have spent the last five chapters creating.

Whether that tradeoff is worth it depends on what you are building. For a content pipeline that produces articles, the document-driven approach you have now is probably enough — the failure modes are tolerable and the gate catches most of them. For a pipeline that produces code that gets deployed, or runs in production without human review, the tradeoff shifts significantly.

That is the next level. It is not in this book. Where to find it is at the end of this chapter.

---

## What You Have

You have a working pipeline, an honest picture of its limits, and a clear view of what comes after it.

The pipeline is useful. It produces consistent improvement over single-agent output in the specific ways it was designed to. The improvement is traceable — you can see which stage produced which quality. That traceability is what lets you improve the pipeline: if the adversarial reader is finding too much noise, tighten the role definition. If the researcher is not producing enough Grounded claims, change the research question. The design is visible.

The limits are real but manageable at this stage. The gate is your main instrument. Use it when you need it, skip it when you don't, and know the difference.

Part 2 takes everything you just built and applies it to a software development workflow. The roles change. The files change. The coordinator changes. The design decisions — why you separate stages, what the handoff contracts look like, how the gate works — do not change at all.

---

> **Key Takeaway:** The pipeline works because the design is visible. It fails in predictable ways for the same reason. Know the failure modes, use the gate, and you have a system you can trust — within the limits you now understand.

---

## For the Next Level

External orchestration frameworks provide the programmatic routing layer described above. This is one of the fastest-moving areas in software right now — frameworks that were experimental a year ago are production-ready today, and the landscape will continue to shift. Treat this list as a starting point, not a permanent reference.

As of writing, the main options worth knowing:

- **LangGraph** — graph-based workflow with explicit state management and checkpointing; strongest story for complex, stateful pipelines
- **CrewAI** — role-based multi-agent coordination with structured handoffs; the fastest path to multi-agent prototyping; broad protocol support
- **OpenAI Agents SDK** — OpenAI's production-ready orchestration layer (replaced the earlier experimental Swarm framework in 2025); simplest onramp if you are already using OpenAI models
- **OpenAI Symphony** — released March 2026; monitors a project board (currently Linear), creates an isolated workspace per issue, and spawns autonomous coding agents through each stage of the ticket lifecycle; built on Elixir/BEAM for fault-tolerant agent supervision; the closest existing thing to what this book describes — a system where you move tickets on a board instead of prompting agents directly
- **Microsoft Agent Framework** — merged AutoGen and Semantic Kernel into a single framework; natural fit for Azure-based teams; reached release candidate in early 2026

Each of these trades the simplicity of document-driven coordination for the reliability of programmatic control. If what you built in Part 1 is working for you, you do not need them yet. If the failure modes are costing you more than the infrastructure would, you do now. Search for current comparisons before committing — the relative strengths of these frameworks are changing faster than most books can track.
