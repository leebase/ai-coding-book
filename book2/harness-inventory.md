# Harness Inventory: Coding with Agent Teams

> **Purpose**: Catalogues every `> **Antigravity:**` callout in the book as a swap point for spin-off editions. Each entry shows chapter, context, and what the harness step does — so a spin-off editor can replace it with tool-specific instructions without touching the concept prose.

---

## Swap Point Structure

Each swap point contains:
- **Location**: chapter and section
- **Concept action**: what the reader needs to accomplish (tool-agnostic)
- **Antigravity instruction**: the current harness text

The concept prose surrounding each callout must remain unchanged in spin-offs. Only the callout content changes.

---

## Part 1: Content Pipeline

### Chapter 1: Run the Prompt

**Swap 1.1** — Open a new agent session
**Concept action**: Start a fresh AI agent session with no prior context. Send the article prompt. Do not interrupt.
**Antigravity instruction**: Open Antigravity. Click **New Session** (the **+** icon near your session list) to start a fresh conversation. Type or paste the prompt into the input field and press Enter. Do not send follow-up messages.

**Swap 1.2** — Save article as `article-v1.md` with comment block
**Concept action**: Copy the article output. Create a new file named `article-v1.md`. Paste the article, add the comment block at the top, fill in the four impressions, save.
**Antigravity instruction**: Copy the full article text from the agent response. In the Explorer pane (left sidebar), right-click your project directory and choose **New File**. Name it `article-v1.md`. Paste the article text, then add the comment block above it. Fill in your impressions and save (Cmd+S or Ctrl+S).

---

### Chapter 2: The Grounding Problem

**Swap 2.1** — Run the verification test
**Concept action**: Open a fresh agent session. Send the five-examples prompt. Read the output.
**Antigravity instruction**: Click **New Session** to open a fresh conversation. Paste the prompt and send it. Read the five examples the agent produces.

**Swap 2.2** — Create `agents/researcher.md`
**Concept action**: Create a new file at `agents/researcher.md`. Paste the role definition. Save it.
**Antigravity instruction**: In the Explorer pane, right-click your project directory, choose **New File**, name it `agents/researcher.md`. Paste the role definition above. Save it.

**Swap 2.3** — Run the researcher role
**Concept action**: Open a fresh agent session. Load the researcher role by pasting its contents first. Add the topic and question. Send it. Save output as `research-notes.md`.
**Antigravity instruction**: Start a **New Session**. In the input field, paste the full text of `agents/researcher.md`, then add a blank line, then add the topic and question above. Send it. The agent will produce structured research notes rather than article prose.

---

### Chapter 3: The Reader Problem

**Swap 3.1** — Write draft from research notes
**Concept action**: Open a fresh agent session. Paste the research notes and the draft instruction. Send it. Save output as `draft.md`.
**Antigravity instruction**: Start a **New Session**. Paste the full contents of `research-notes.md` first, then add a blank line, then add the instruction above. Send it.

**Swap 3.2** — Create `agents/adversarial-reader.md`
**Concept action**: Create a new file at `agents/adversarial-reader.md`. Paste the role definition. Save it.
**Antigravity instruction**: Create `agents/adversarial-reader.md` in your project directory. Paste the role definition above. Save it.

**Swap 3.3** — Run the adversarial reader role
**Concept action**: Open a fresh agent session. Paste the adversarial reader role, then the draft. Send it. Save output as `reader-notes.md`.
**Antigravity instruction**: Start a **New Session**. Paste the full text of `agents/adversarial-reader.md`, then a blank line with `---`, then the full text of `draft.md`. Send it.

**Swap 3.4** — Address gaps in `draft.md`
**Concept action**: Open `draft.md`. Make targeted fixes for each item in `reader-notes.md`. Save.
**Antigravity instruction**: Open `draft.md`. For each item in `reader-notes.md`, make the specific, minimal change that closes the gap. Save the updated file.

---

### Chapter 4: Voice and Sequence

**Swap 4.1** — Create `skills/voice.md`
**Concept action**: Create a new file at `skills/voice.md`. Paste the voice definition. Adjust the reader description. Save.
**Antigravity instruction**: Create `skills/voice.md` in your project directory. Paste the definition above, adjust the reader description to match your intended audience, and save it.

**Swap 4.2** — Create `skills/article-pipeline.md`
**Concept action**: Create a new file at `skills/article-pipeline.md`. Paste the coordinator. Save.
**Antigravity instruction**: Create `skills/article-pipeline.md`. Paste the coordinator above. Save it.

**Swap 4.3** — Create `agents/writer.md`
**Concept action**: Create a new file at `agents/writer.md`. Paste the role definition. Save.
**Antigravity instruction**: Create `agents/writer.md` with the role definition above. Save it.

---

### Chapter 5: Run the Pipeline

**Swap 5.1** — Load the coordinator and run the full pipeline
**Concept action**: Open a fresh agent session. Load the article pipeline coordinator. Add the topic and target reader. Follow the stages. Use the optional Stage 1 gate before proceeding to Stage 2.
**Antigravity instruction**: Start a **New Session**. Paste the full contents of `skills/article-pipeline.md` at the start, then add the topic and target reader above. The agent will walk through the stages. At Stage 1, read `research-notes.md` before confirming it should proceed to Stage 2.

**Swap 5.2** — Save `final.md` as `article-v2.md`
**Concept action**: Copy the content of `final.md`. Create a new file named `article-v2.md`. Save.
**Antigravity instruction**: Copy the content of `final.md`. Create a new file in your project directory named `article-v2.md`. Paste the content and save.

---

## Part 2: Coding Team

### Chapter 7: Translating the Pattern

**Swap 7.1** — Create `requirement.md`
**Concept action**: Create a new file at `requirement.md` in a new project directory for Part 2. Paste the requirement. Save. Do not change this file during the sprint.
**Antigravity instruction**: Create `requirement.md` in a new project directory for Part 2. Paste the requirement above. Save it. This file does not change during the sprint.

---

### Chapter 8: The Coding Team

**Swap 8.1** — Create all five agent role files
**Concept action**: Create an `agents/` directory. Create `agents/planner.md`, `agents/implementer.md`, `agents/reviewer.md`, `agents/tester.md`, and `agents/documenter.md` with the role definitions above. Save each.
**Antigravity instruction**: Create the `agents/` directory in your Part 2 project. Create all five role files above. Save each one.

---

### Chapter 9: The Feature Skill

**Swap 9.1** — Create `skills/feature-sprint.md`
**Concept action**: Create a new file at `skills/feature-sprint.md`. Paste the coordinator. Save.
**Antigravity instruction**: Create `skills/feature-sprint.md`. Paste the coordinator above. Save it.

---

### Chapter 10: Running a Sprint

**Swap 10.1** — Start Stage 1 (Planner)
**Concept action**: Open a fresh agent session. Load the feature sprint coordinator. Add the topic. The agent will load the Planner role and produce `plan.md`.
**Antigravity instruction**: Start a **New Session**. Paste the full contents of `skills/feature-sprint.md`, then a blank line, then "Ready to begin Stage 1. Topic: git-summary". The agent will load the Planner role and begin producing `plan.md`.

**Swap 10.2** — Save `plan.md` and confirm the gate
**Concept action**: Save the Planner's output as `plan.md`. Read it. Add or adjust decisions. Confirm the gate.
**Antigravity instruction**: Save the Planner's output as `plan.md`. Read it thoroughly. Add or adjust any decisions before proceeding. The plan is the spec from here.

**Swap 10.3** — Run Stage 2 (Implementer)
**Concept action**: In the same session, provide `requirement.md` and `plan.md`. Instruct the agent to proceed to Stage 2.
**Antigravity instruction**: In the same session, paste the full contents of `requirement.md` and `plan.md`, then instruct the agent to proceed to Stage 2.

**Swap 10.4** — Run Stages 3 and 4 in parallel (Reviewer + Tester)
**Concept action**: Open two simultaneous agent sessions. In the first, load the Reviewer role and provide `requirement.md` and `git_summary.py`. In the second, load the Tester role and provide the same inputs. Run both.
**Antigravity instruction**: Click the grid icon (upper right) to open **Manager View**. Create a second agent card. In Card 1, load `agents/reviewer.md` and paste `requirement.md` and `git_summary.py`. In Card 2, load `agents/tester.md` and paste `requirement.md` and `git_summary.py`. Send both.

**Swap 10.5** — Run Stage 5 (Implementer addressing findings)
**Concept action**: Open a fresh agent session. Load the Implementer role. Provide the current implementation, the review notes, and the test report. Instruct it to fix correctness issues and failing tests.
**Antigravity instruction**: Open a new session (or return to your Stage 2 session if context is still clean). Load `agents/implementer.md`. Paste `git_summary.py`, `review-notes.md`, and `test-report.md`. Instruct the agent to fix the correctness issues and failing tests.

**Swap 10.6** — Run Stage 6 (Documenter)
**Concept action**: Open a fresh agent session. Load the Documenter role. Provide `requirement.md`, the final implementation, and the test report. Let it produce `README.md`.
**Antigravity instruction**: Open a new session. Load `agents/documenter.md`. Paste `requirement.md`, the final `git_summary.py`, and `test-report.md`. Let the Documenter produce `README.md`.

---

## Summary: Swap Point Count

| Chapter | Swap Points | Primary action type |
|---------|-------------|---------------------|
| Ch 1 | 2 | New session; file creation |
| Ch 2 | 3 | New session; file creation |
| Ch 3 | 4 | New session; file creation; file editing |
| Ch 4 | 3 | File creation |
| Ch 5 | 2 | New session; file creation |
| Ch 7 | 1 | File creation |
| Ch 8 | 1 | Directory + file creation |
| Ch 9 | 1 | File creation |
| Ch 10 | 6 | New session; parallel sessions; file operations |
| **Total** | **23** | |

---

## Action Type Categories for Spin-Off Mapping

When building a spin-off edition, each action type maps to the tool's equivalent:

| Action type | Antigravity | Claude Code equivalent | Cursor equivalent |
|-------------|-------------|----------------------|-------------------|
| New session | **New Session** button | New conversation / `/clear` | New chat window |
| Load role | Paste role file contents at top | Load file via `@` reference | Paste in system prompt area |
| File creation | Explorer pane → New File | `Write` or `touch` + editor | File explorer → New File |
| Parallel sessions | Manager View (two cards) | Two terminal windows | Two chat panels |
| Save output | Copy → paste into file | `Write` tool / redirect | Copy → paste into file |

---

*Maintained by the book team. Update when chapters are revised.*
