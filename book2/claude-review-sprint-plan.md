# Claude Review Sprint Plan: book2

> **Tactical execution for the Reviewer Team.**
> This plan follows the AgentFlow methodology: Research → Strategy → Execution (Plan → Act → Validate).
> The goal is to produce a comprehensive `claude_says.md` artifact to sharpen the `book2` manuscript.

---

## Sprint 0 — Environment & Setup (Research Phase)

**Goal**: Prepare the review environment and orient all agents to the book's structure and thesis.

| Task | Indicator of Done |
| :--- | :--- |
| **Research**: Audit all 13 files (Intro, Ch 1–11, Conclusion) and the combined manuscript in `book2/`. | A verified "Chapter Map" exists — title, word count, key artifact, thesis claim — for each chapter. |
| **Strategy**: Assign specific attack vectors for each chapter to the 5-agent team. | A "Review Matrix" maps each agent to specific chapters and focal points. |
| **Execution (Plan)**: Define the structure of the `claude_says.md` template. | `claude_says.md` exists with section placeholders for all 5 agents. |
| **Execution (Act)**: Initialize `claude_says.md` with current project thesis and audience. | `claude_says.md` committed with core thesis and reader profile. |
| **Execution (Validate)**: Confirm all 5 reviewer agents and 5 skills are loaded and accessible. | All agent and skill files verified present in `book2/agents/` and `book2/skills/`. |

---

## Sprint 1 — Introduction + Part 1 Review: Chapters 1–3

**Goal**: Audit the book's opening and the first three chapters of the content pipeline.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Define the thesis arc for Introduction + Chapters 1–3. | The "one-agent ceiling" → "researcher role" → "adversarial reader" arc is mapped. |
| **Execution (Act)**: **The Practitioner** audits Chapters 1–3 for step completeness and gate quality. | Chapter 1 comparison exercise instructions, Chapter 2 researcher setup, and Chapter 3 adversarial reader steps are verified or flagged in `claude_says.md`. |
| **Execution (Act)**: **The Thesis Guard** audits Introduction and Chapters 1–3 for thesis coherence. | Introduction promise audit and per-chapter thesis statements for Ch 1–3 added to `claude_says.md`. |
| **Execution (Act)**: **The Senior Dev** checks Introduction and Chapters 1–3 for register violations and project thread state. | Voice violations and Part 1 thread state (article-v1.md through draft.md) verified in `claude_says.md`. |
| **Execution (Validate)**: **The Harness Auditor** spot-checks Swap Points 1.1–3.4 for concept/harness separation. | Callout self-containment and concept independence for Ch 1–3 verified or flagged. |

---

## Sprint 2 — Part 1 Review: Chapters 4–6

**Goal**: Audit the coordinator, the comparison exercise, and the honest ceiling.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Identify the critical audit points in Ch 4–6 — coordinator design, Chapter 5 comparison, Chapter 6 failure modes. | A "High Stakes List" for Part 1 Ch 4–6 is defined. |
| **Execution (Act)**: **The Practitioner** runs the Chapter 5 pipeline and comparison exercise mentally. | Comparison exercise verdict (nameable differences, article-v1.md preservation, gate quality) added to `claude_says.md`. |
| **Execution (Act)**: **The Ceiling Skeptic** attacks Chapter 6 — failure mode descriptions, external orchestration accuracy, gate reliability claims. | Chapter 6 integrity verdict and pre-Chapter 6 honesty gaps added to `claude_says.md`. |
| **Execution (Act)**: **The Harness Auditor** audits Swap Points 4.1–5.2 and Chapter 4's coordinator skill text. | Callout separation for the coordinator and pipeline run steps verified. |
| **Execution (Validate)**: **The Thesis Guard** checks that Chapter 5 comparison and Chapter 6 ceiling serve the thesis. | Part 1 thesis arc closure verdict added to `claude_says.md`. |

---

## Sprint 3 — Part 2 Review: Chapters 7–9

**Goal**: Audit the pattern translation and coding team setup.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Map the Part 1 → Part 2 translation — content roles to coding roles, article pipeline to feature sprint. | A "Translation Map" showing what changes and what stays the same is established. |
| **Execution (Act)**: **The Thesis Guard** audits Chapter 7's translation quality — are role analogies earned or mechanical? | Chapter 7 translation verdict added to `claude_says.md`. |
| **Execution (Act)**: **The Practitioner** audits Chapters 8–9 for coding team role definitions and feature sprint coordinator completeness. | Role definition gaps and feature sprint coordinator review added to `claude_says.md`. |
| **Execution (Act)**: **The Senior Dev** audits Chapter 7 for the Part 1 → Part 2 transition quality and register. | Transition verdict and any register violations for Ch 7–9 added to `claude_says.md`. |
| **Execution (Validate)**: **The Harness Auditor** verifies Swap Points 7.1–9.1 for concept/harness separation. | Callout separation for Part 2 setup chapters verified. |

---

## Sprint 4 — Part 2 Review: Chapters 10–11 + Conclusion

**Goal**: Audit the full sprint execution, synthesis chapter, and close.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Identify the critical audit points — parallel sessions, merge discipline, full sprint synthesis. | A "High Stakes List" for Part 2 Ch 10–11 is defined. |
| **Execution (Act)**: **The Practitioner** audits Chapter 10's parallel session instructions (Swap Points 10.4) and full sprint gate sequence. | Manager View introduction timing, parallel session readiness, and gate sequence verdict added to `claude_says.md`. |
| **Execution (Act)**: **The Ceiling Skeptic** audits Chapters 10–11 for pre-Chapter 6 failure mode acknowledgments. | Any implicit reliability overclaims in the sprint execution chapters flagged in `claude_says.md`. |
| **Execution (Act)**: **The Senior Dev** builds the complete Part 2 project thread state table and checks Conclusion for register and thesis closure. | Part 2 thread state table and Conclusion verdict added to `claude_says.md`. |
| **Execution (Validate)**: **The Harness Auditor** verifies all remaining swap points (10.1–10.6) and checks harness inventory completeness. | Final inventory cross-reference completed; all discrepancies logged. |

---

## Sprint 5 — Final Synthesis & Handoff

**Goal**: Prepare the final `claude_says.md` for the Writer to consume.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Compile and prioritize all agent notes into a single actionable heatmap. | A "Priority Heatmap" (Critical / Important / Optional) is added to `claude_says.md`. |
| **Execution (Act)**: Format `claude_says.md` for maximum usability — clear headers, bulleted directives, actionable notes only. | `claude_says.md` is structured with section headers matching the 5 agents plus the heatmap and synthesis. |
| **Execution (Validate)**: Human review of `claude_says.md` for accuracy and completeness. | Human approval documented; any corrections applied. |

---

## Exit Criteria

- `claude_says.md` covers all 13 files (Intro, Ch 1–11, Conclusion).
- Every note is **actionable** — not descriptive. "This is unclear" is not a note.
- All 5 reviewer agent perspectives are represented.
- The Priority Heatmap distinguishes Critical (blocks reader) from Important (degrades quality) from Optional (polish).
- The harness inventory is verified complete against the chapter text.
- The Chapter 5 comparison exercise has a specific verdict.
- The Chapter 6 ceiling has an integrity verdict.
