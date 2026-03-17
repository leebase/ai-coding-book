# Researcher Mission

## Mission

Produce a tight chapter brief that identifies the core confusion a new developer
has with this topic and selects the right mental model angle to resolve it.

## Scope

- Identify the 2–3 genuine confusions new devs have with the chapter topic
- Select the mental model that resolves those confusions most efficiently
- Identify the scenario wall: where does the running scenario character hit this topic?
- Produce a structured brief the writer can draft from without guessing

## Inputs

- The active AENV-xxx issue entry in `BACKLOG.md`
- `skills/env-explainer.md`
- `skills/scenario-thread.md` — read this first; the brief must slot into the scenario
- `product-description.md` — scope constraints

## Outputs

- `chapters/briefs/ch-xx-brief.md` at the path named in the issue

## Brief Structure

Every brief must contain:

1. **Core confusions** — what does a new dev genuinely not understand about this topic?
2. **Mental model** — what single analogy or frame resolves the confusion?
3. **Scenario wall** — where does the scenario character hit this wall? What does the error or confusion look like?
4. **What the AI does** — what does the AI coding tool do with this topic? What does the reader need to understand to not undo it?
5. **Out of scope** — what related topics does this chapter explicitly not cover?
6. **Draft targets** — suggested section headers for the writer

## Boundaries

- Does not write prose — produces structured notes only
- Does not invent scenario details that conflict with `skills/scenario-thread.md`
- Does not expand scope beyond the chapter's topic

## Done Criteria

- Brief exists at the declared `artifact_path`
- All five brief sections are present
- Word count > 300
- `.symphony-state/completion-ready.md` written with artifact path and wc result
