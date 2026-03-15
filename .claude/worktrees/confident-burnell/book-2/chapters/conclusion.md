# Conclusion

You built two pipelines. One produces articles. One produces code. They use different roles, different file names, different handoff contracts. They use the same design.

That is the thing worth keeping: the design is portable. Specialized roles. Explicit inputs and outputs. A coordinator that enforces the sequence. A gate at the most expensive decision point. Shared memory that every stage reads from.

You can take that design to any complex, repeatable task you do regularly. The roles change. The coordinator changes. The pattern does not.

---

## What You Have

After Part 1:

A content pipeline with four roles — Researcher, Writer, Adversarial Reader, Coordinator — and the understanding of why each one exists. Not just what it does, but what breaks when it is absent. The researcher prevents confabulation. The adversarial reader finds the gaps the writer cannot see. The voice constraint prevents drift across sessions. The coordinator enforces the sequence that makes all of it work together.

And `article-v1.md` and `article-v2.md` side by side — the argument the book did not make, but let you observe.

After Part 2:

A coding team with five roles — Planner, Implementer, Reviewer, Tester, Documenter — and a coordinator that runs them through a full feature sprint. A working `git-summary` tool, a test suite that verifies the requirement, and a README that describes what the tool does not do. The mandatory gate after the Planner, which you now understand costs nothing to take and potentially saves a full implementation run.

---

## What the System Cannot Do

Chapter 6 named these, but they are worth restating as you close the book.

The coordinator runs inside the same context it is coordinating. Stages collapse. Roles drift. Output varies between runs. The gate is your primary quality instrument, which means quality depends on you knowing what good looks like at each stage.

This is not a reason to put the book down. It is a reason to use the gates seriously and calibrate your trust against actual results, not against what the pipeline is supposed to produce.

When these failure modes cost more than the infrastructure of a proper orchestration layer, you will know. The frameworks in Chapter 6 are there for that moment. They are not the starting point — this book is.

---

## The Next Feature

The most common question after finishing a book like this is: what do I build next?

The answer is whatever you have been avoiding because it was too complex for one agent.

You know the structure now. Write the requirement. Identify the roles the work actually needs. Write the handoff contracts. Build the coordinator. Run the mandatory gate. The team is built the same way every time — the domain is the only thing that changes.

The roles in this book are a starting point, not a complete set. A Security Reviewer. A Compatibility Checker. A Dependency Auditor. An API Contract Validator. Every team you build will need a slightly different roster. What stays constant is the structure of each member: what they receive, what they produce, what they are not allowed to do.

---

## Where the Path Goes

This book teaches the first level: document-driven coordination, human-executed, with Antigravity as the runtime. It is useful at this level and honest about its ceiling.

The second level is programmatic orchestration — code that routes work between agents, validates outputs against schemas, runs stages in independent contexts, and does not require your attention at every gate. That is the work of the frameworks named in Chapter 6, and of a future volume.

The third level — which frameworks like OpenAI's Symphony are beginning to approach — is the system where you manage the work, not the agents. You move a ticket to "Ready." The pipeline picks it up, plans it, implements it, tests it, reviews it, and opens a pull request. You review the PR. That is the loop.

We are early in that story. The infrastructure is being built now. The teams that get there first will be the ones who already understand what the pipeline needs to do — because they built one by hand.

That is what you just did.

---

## A Note on This Book

This book was written by a team of agents coordinated by a skill file. The roles are named in `skills/ebook-writer.md`. The coordinator ran nine stages per chapter, with a mandatory gate after the outline and before prose was written. The pipeline ran on itself — the book that teaches agent teams was produced by one.

That is not a disclaimer. It is evidence. The system works well enough to produce something you just read from cover to cover. It also ran into every failure mode described in Chapter 6, and the gates caught most of them.

Build the team. Run the gates. Keep the output.

---

*The companion volume, covering programmatic orchestration and autonomous pipeline execution, is in progress.*
