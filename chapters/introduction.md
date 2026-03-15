# Introduction

You have described what you want. The AI built something. It was close — but not quite right. So you described it again, differently. The AI built something else. Closer, maybe. You kept going. Three prompts in, you realized the foundation was wrong, and you were either going to fight it or start over.

This is not a failure of the AI. The AI did exactly what a capable colleague does when handed a vague request: it made reasonable assumptions and produced something that compiles, runs, and looks reasonable. The problem is that the assumptions were not yours. And because AI builds so fast, those assumptions became structural before you had a chance to question them.

The faster the execution, the more expensive the unclear thinking. This is the central challenge of AI-assisted development, and it does not get easier as the tools improve. It gets harder. Every speed increase in AI output raises the cost of not knowing what you want before you start.

---

## The Discipline Problem

Software development has always required clarity of thought. Before AI, the writing of code was slow enough that bad assumptions surfaced during implementation — you ran into them, you adjusted, the friction kept you honest. AI removes that friction. The cost of starting is nearly zero. The cost of being wrong does not change.

What changes is when you pay it.

In a pre-AI workflow, unclear requirements showed up as slow progress, lots of dead ends, and gradual course-correction. In an AI-assisted workflow, unclear requirements show up as a codebase full of someone else's decisions — the AI's reasonable interpretations of what you probably meant — that you now have to maintain and extend.

The software engineering disciplines that address this are not new. Plan before you build. Define requirements precisely. Test against what you specified, not against what was implemented. Review code as if you have to own it forever. Iterate in controlled increments. Manage scope explicitly. Document the decisions that are not in the code.

These disciplines predate AI coding tools by decades. They are not more important now than they were before. But the consequences of skipping them have changed. The penalty for skipping planning used to be a slow start. The penalty now is thirty seconds of confident execution in the wrong direction.

**Software engineering discipline does not disappear in the AI era. It moves up a level.** The AI writes the code. You are responsible for everything the code is supposed to do — and that responsibility requires the same clarity, precision, and rigor it always did. More, in fact, because the AI will not push back on a bad idea. It will implement it.

---

## This Book

This book teaches you to apply seven foundational SE disciplines in an AI-assisted workflow, then shows you how to make those disciplines systematic through a methodology called AgentFlow.

**Part 1** covers the disciplines through hands-on practice. You will plan before you prompt. You will write verifiable requirements before you build. You will design test cases from your requirements — not from the implementation. You will review AI-generated code as if you are approving a pull request. You will iterate in explicit, verified increments. You will manage scope by naming what you are not building. You will maintain a decision log so that every new session — and every new agent — starts with context instead of guesswork.

**Part 2** shows you how these disciplines scale. AgentFlow is a documentation-driven methodology for human-AI collaboration. It formalizes the practices from Part 1 into a system that works across sessions, tools, and — when you are ready — parallel AI agents. You will learn to build skills that encode your working style, context files that survive session resets, sprint plans that coordinate work across multiple AI runs, and autonomy calibration so you know how much to delegate and when to stay in the loop.

The two parts are designed to be read in order. Part 1 establishes the practice. Part 2 builds the system. You cannot build a reliable system around practices you have not internalized.

---

## The Project Thread

Every chapter in this book is grounded in a single running project: a personal task manager CLI written in Python.

You will not start with a finished product. You will build it from scratch in Chapter 1 and add to it in every chapter that follows. By the time you reach Chapter 14, the task manager will have grown from four commands and zero tests to more than ten commands and twenty tests — and you will have applied every discipline in this book to real, running code.

Here is what you start with at the end of Chapter 1:

- `python tasks.py add "Buy groceries"` — adds a task
- `python tasks.py list` — shows all tasks
- `python tasks.py done 1` — marks task 1 complete
- `python tasks.py delete 1` — removes task 1

That is it. Simple enough that the structure is obvious. Complex enough that all seven disciplines have real work to do on it.

Each chapter adds a feature or applies a discipline to the existing code. The project thread is continuous — what you build in Chapter 3 is what you test in Chapter 4 and review in Chapter 5. By Part 2, the same codebase is the vehicle for multi-session AgentFlow sprints.

If you want to substitute your own project, it needs to be a CLI tool you can build incrementally, with testable behavior and a growing feature set. Everything in the book applies regardless of what you are building.

---

## How Part 1 Works

Each chapter in Part 1 introduces one discipline through a failure path and a success path.

The failure path shows what happens when the discipline is absent. You will do it — not read about it. You will make the vague prompt, watch the AI make assumptions, and feel the consequence. These are not constructed cautionary tales. They are the actual workflow most developers default to. Experiencing the failure is what makes the discipline legible.

The success path shows the same scenario with the discipline applied. Same feature, same tool, completely different outcome — because you changed what you did before opening the tool.

Each chapter ends with a debrief. The debrief names the discipline you just practiced, explains why it worked, and connects forward to the next chapter. Part 1 chapters build on each other. The requirements you write in Chapter 2 are the source of the tests you design in Chapter 3. The tests you write in Chapter 3 catch the scope drift you will see in Chapter 6. Each discipline compounds.

---

## How Part 2 Works

Part 2 assumes you can apply the Part 1 disciplines. It does not re-teach them. It shows you how to make them systematic.

AgentFlow introduces five core components: a skill system that encodes your working style into reusable prompts, context files that preserve project state across sessions, a sprint cadence for planning and executing work in coordinated increments, a multi-agent coordination model for parallel work, and an autonomy calibration framework for deciding how much to delegate.

Each Part 2 chapter introduces one component through the same task manager project thread. By Chapter 14, you will run a complete AgentFlow sprint from scratch — using every component you learned — on a feature you choose from the backlog you built across Part 1.

Part 2 is where the practice becomes a system. If Part 1 is the discipline, Part 2 is the infrastructure that makes the discipline automatic.

---

## Before You Begin

**What you need:**

- **Python 3.10 or later.** The task manager is pure Python with no external libraries. Any modern Python installation works.
- **Antigravity installed.** Antigravity is Google DeepMind's free-tier AI coding IDE. Visit [antigravity.google](https://antigravity.google) to download it. Installation is straightforward — follow the current guide on the site rather than any screenshots here, as the UI evolves. The free tier is sufficient for every exercise in this book.
- **A terminal you are comfortable with.** You will run Python commands from the terminal throughout. macOS Terminal, Windows PowerShell, or any Linux shell all work.
- **2–10 years of development experience.** This book is not for beginners. It assumes you know what a function is, you have written tests before, and you have shipped code in a production environment at least once. The disciplines here are not novel theory — they are practices you probably know exist and have not applied rigorously because the workflow was slow enough to get away with it. It is no longer slow enough.

**What you do not need:**

- Prior experience with AI coding tools. This book starts from scratch with Antigravity.
- Experience with AgentFlow, AgentFlow-adjacent tools, or any specific AI methodology. AgentFlow is introduced in Part 2 and built up from first principles.
- Python expertise. The task manager code is deliberately simple — under 200 lines by Part 1's end. Understanding it requires reading, not fluency.

---

## Let's Start

Chapter 1 opens with the failure path. You will open Antigravity, describe what you want, and watch what happens. By the time you finish that chapter, you will understand exactly why the experience felt familiar — and what to do instead.

---

*The AI is fast. What it builds is only as good as what you specified. This book is about the specifying.*
