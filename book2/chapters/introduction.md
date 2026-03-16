# Introduction

You have been using AI agents for a while. You know how to write a prompt. You know what a good response looks like and what a bad one looks like. You have gotten real work done with these tools.

And at some point you hit a wall.

Not a dramatic failure — nothing crashed, nothing was obviously wrong. The output just started coming back flat. Generic. Almost right but not quite. You asked for something complex, you got something complete, and you knew the difference even if you could not name it. You tried better prompts. Longer prompts. More specific prompts. The ceiling stayed where it was.

This book is about what is on the other side of that ceiling.

---

## The Problem With One Agent

A single agent session has one context, one perspective, and one job: produce the output you asked for. On simple tasks — write this function, summarize this document, answer this question — that is enough. The task fits in the context. The agent does it. You move on.

Complex tasks do not fit in a single context. Not because the model lacks capability, but because complex work has structural properties that one agent cannot satisfy. Research and writing are different cognitive tasks — when they happen simultaneously, the research gets compromised. Editing and authorship require different perspectives — the writer cannot be the adversarial reader of their own work. Planning and implementing have a hard dependency — a plan must be complete before implementation begins, or the implementation is built on guesses.

You can write longer prompts to try to simulate all of this. It does not work reliably. The same model that produces brilliant output on a focused task blends concerns, loses constraints, and drifts when asked to be everything at once.

The solution is not a better prompt. It is a team.

---

## What This Book Teaches

This book teaches you to build and run teams of AI agents — specialized roles, working in sequence, passing structured output between them, coordinated by a skill file you design.

You do not need external orchestration infrastructure to do this. You do not need to write a routing layer or manage API calls between agents. Everything in this book runs in Antigravity, using documents and skill files as the coordination layer. The human — you — runs the coordinator and confirms the gates.

That is both the power and the limit of what this book teaches. You will build something genuinely useful. You will also learn exactly where it breaks down and what the next level looks like when you are ready for it.

**Part 1** builds a content pipeline: a team that takes a topic and produces a finished article. You start by running a single prompt and saving the output. Over five chapters you build the team that does the same task properly. In Chapter 5, you compare both outputs. The difference is not subtle.

**Part 2** applies the same pattern to software development. You build a coding team — Planner, Implementer, Reviewer, Tester, Documenter — with a coordinator skill that sequences them through a full feature sprint. The project is a CLI tool called `git-summary`. By Chapter 11, you run the complete pipeline from requirement to documented, tested code.

---

## What You Need

A Google Antigravity account (free tier is sufficient throughout — no paid features are required). Some familiarity with using AI agents for development tasks. And a complex task you have been avoiding because you suspected one agent was not going to cut it.

That last one is the most important. The system in this book is not a demonstration — it is a working method. The best way to learn it is to use it on something real.

---

## One More Thing

This book was written using the system it teaches.

The chapters you are about to read were produced by a pipeline of specialized agent roles: one that defined the principle to be taught, one that designed the hands-on scenario, one that reviewed the Antigravity instructions for accuracy, one that read each draft as a confused first-time reader to find the gaps, one that checked continuity across chapters. A coordinator skill sequenced all of them. The gate ran before every chapter draft was written.

The pipeline did not run perfectly every time. Stages collapsed occasionally. Roles drifted. Some runs were better than others. The gate caught most of what needed catching.

That is an accurate description of what you are about to build. Not a perfect system — a visible one, where the failures are predictable and the improvements are traceable. That is the point.

Let's build it.
