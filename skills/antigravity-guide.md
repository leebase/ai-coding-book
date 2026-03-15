# Skill: Antigravity Guide

Write reader-facing instructions for the Google Antigravity app. Antigravity is a VS Code fork by Google DeepMind — an agent-first IDE where AI agents autonomously access the editor, terminal, and browser.

## The Two Views

- **Editor View** — Traditional IDE interface with an agent sidebar. Use for single-agent tasks. This is where most Part 1 scenarios live.
- **Manager View** — Orchestrate multiple agents working in parallel. Introduce in Part 2 when covering AgentFlow's multi-agent patterns.

Reference these views by their exact names. Never say "click the AI button."

## Free Tier

The free tier runs Gemini models with rate limits. Do not treat this as a limitation to work around — treat it as a design constraint that reinforces SE discipline.

Use this callout when relevant:

> **Free Tier Note:** Antigravity's free tier has rate limits on Gemini model requests. A reader who prompts thoughtlessly will hit them. A reader who plans before prompting won't. This is the lesson made tangible.

## Writing Step-by-Step Instructions

- Specify the exact UI path: which view, which panel, where to type
- Show the exact prompt to give the agent — do not paraphrase
- Explain the intent of the prompt separately from the prompt itself
- Tell the reader what to observe, not what the agent is "thinking"

Use these callout patterns:

> **What the Agent Will Do:** [observable actions — files it will create, commands it will run, output to expect]

> **Watch For:** [specific output, error, or behavior that confirms the step worked]

## Antigravity Agents Are Stateless

Each Antigravity task starts fresh — agents do not remember previous sessions. When writing instructions that span multiple steps or sessions, tell the reader explicitly what context to re-establish. This connects directly to AgentFlow's `context.md` pattern introduced in Part 2.

## Prompts Are Instructions, Not Wishes

When showing a prompt to give the agent, write it as a precise instruction with constraints, not a vague request. Show what a sloppy prompt produces vs. what a disciplined prompt produces. This is a teaching opportunity in every scenario.
