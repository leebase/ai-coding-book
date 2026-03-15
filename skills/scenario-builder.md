# Skill: Scenario Builder

Design hands-on coding scenarios that teach SE principles through experience in the Google Antigravity app.

## The Rule of One

Each scenario teaches exactly one principle. If you find yourself teaching two things, split the scenario.

## Structure of Every Scenario

1. **Setup** — What state is the project in? What does the reader have in front of them?
2. **The prompt** — Exact wording to give the Antigravity agent, with the intent explained
3. **What the agent does** — What the reader should observe (autonomous actions, output, files changed)
4. **The success path** — What good looks like when the principle is applied
5. **The failure path** — What happens when the discipline breaks down (skip this, and the lesson is hollow)
6. **Debrief question** — One question the reader must answer before moving on

## Constraints

- Every scenario must be completable on the Antigravity free tier (Editor View or Manager View, Gemini models)
- Never design a scenario that requires paid features or elevated rate limits
- Ground every scenario in the book's ongoing project thread — readers build one project across Part 1, not a new toy each chapter
- Scenarios should be short enough to complete in a single Antigravity session

## The Failure Path Is Not Optional

Show what happens when discipline breaks down — skipping planning, ignoring test output, accepting the first AI output without review. The reader must feel the consequence, not just read about it.

## Keep Scenarios Observable

Antigravity agents work autonomously. Readers cannot follow the agent's internal reasoning. Design scenarios around outputs the reader can see: files created, tests run, terminal output, diffs shown in the editor.
