# Claude Review Sprint Plan: ai-env-book

> **Tactical execution for the Reviewer Team.**
> This plan follows the AgentFlow methodology: Research → Strategy → Execution (Plan → Act → Validate).
> The goal is to produce a comprehensive `claude_says.md` artifact to sharpen the `ai-env-book` manuscript.

---

## Sprint 0 — Environment & Setup (Research Phase)

**Goal**: Prepare the review environment and orient all agents to the book's structure and thesis.

| Task | Indicator of Done |
| :--- | :--- |
| **Research**: Audit all 17 files (Intro, Ch 1–15, Conclusion) and the combined manuscript. | A verified "Chapter Map" exists — title, part, key concept, thesis claim — for each chapter. |
| **Strategy**: Assign specific attack vectors for each chapter to the 5-agent team. | A "Review Matrix" maps each agent to specific chapters and focal points. |
| **Execution (Plan)**: Define the structure of `claude_says.md`. | `claude_says.md` exists with section placeholders for all 5 agents. |
| **Execution (Act)**: Initialize `claude_says.md` with current project thesis and audience. | `claude_says.md` committed with core thesis and reader profile. |
| **Execution (Validate)**: Confirm all 5 reviewer agents and 5 skills are accessible. | All agent and skill files verified present in `ai-env-book/agents/` and `ai-env-book/skills/`. |

---

## Sprint 1 — Part 1 Review: Git and GitHub (Chapters 1–5)

**Goal**: Audit the book's foundation — git fundamentals, GitHub coordination, SSH auth, branching, and error recovery.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Define the thesis arc for Ch 1–5. | The "snapshot model → recognition → recovery" arc is mapped. |
| **Execution (Act)**: **The Fresh Installer** audits Ch 1–5 for step completeness and prerequisite assumptions. | Git installation assumption, SSH key setup steps, and `git reset --hard` framing verified or flagged in `claude_says.md`. |
| **Execution (Act)**: **The Thesis Guard** audits Ch 1–5 for per-chapter argument quality and chapter endings. | Per-chapter thesis statements for Ch 1–5 added; chapter endings graded PASS/FAIL. |
| **Execution (Act)**: **The Safety Auditor** checks Ch 5 for `git reset --hard` framing and Ch 3 for SSH config completeness. | Destructive operation framing and SSH config safety assessed. |
| **Execution (Validate)**: **The Scenario Auditor** spot-checks `neighborhood-meals` state in Ch 1–5 for continuity. | Scenario state table for Part 1 verified. |

---

## Sprint 2 — Part 2 Review: Python Environments (Chapters 6–8)

**Goal**: Audit the Python environment problem definition, tool comparison, and dependency management.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Identify the critical audit points — environment invisibility concept, uv recommendation, pyproject.toml transition. | A "High Stakes List" for Part 2 is defined. |
| **Execution (Act)**: **The Thesis Guard** audits Ch 6 as the pivotal "problem definition" chapter. | Ch 6 thesis verdict (does it define the invisible environment problem clearly?) added to `claude_says.md`. |
| **Execution (Act)**: **The Fresh Installer** audits Ch 7 for the venv/conda/uv comparison and activation state assumptions. | Activation state assumptions, uv installation path, and tool comparison completeness verified. |
| **Execution (Act)**: **The Safety Auditor** audits Ch 7–8 for dotfile mutations and virtual environment idempotency. | Idempotency hazards in venv activation and requirements.txt patterns assessed. |
| **Execution (Validate)**: **The Scenario Auditor** verifies the `neighborhood-meals` Python backend scenario thread in Ch 6–8. | Scenario continuity and team composition consistency verified for Part 2. |

---

## Sprint 3 — Part 3 Review: Node and npm (Chapters 9–11)

**Goal**: Audit the Node runtime explanation, nvm version management, and package.json/node_modules coverage.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Map the Part 2 → Part 3 transition — same invisible environment problem, different runtime. | Translation quality from Python env to Node env assessed. |
| **Execution (Act)**: **The Thesis Guard** audits Ch 9–11 for "recognition" language vs. memorization framing. | Thesis coherence for Node section verified; "recognition vs. memorization" language assessed. |
| **Execution (Act)**: **The Fresh Installer** audits Ch 10 for nvm installation instructions — URL stability, `curl | bash` framing, shell reload. | nvm installer URL risk, shell reload requirement, and PATH update completeness verified. |
| **Execution (Act)**: **The Safety Auditor** audits Ch 10 for `echo >> ~/.zshrc` idempotency and dotfile safety. | Dotfile mutation safety for nvm PATH setup assessed. |
| **Execution (Validate)**: **The Scenario Auditor** verifies the `neighborhood-meals` React frontend thread in Ch 9–11. | Frontend scenario continuity verified; Node version problem illustration assessed. |

---

## Sprint 4 — Part 4 Review: Warp (Chapters 12–15)

**Goal**: Audit the Warp section for technical accuracy, safety of commands demonstrated, and thesis relevance.

| Task | Indicator of Done |
| :--- | :--- |
| **Execution (Plan)**: Identify the critical audit points — platform availability inconsistency, `kill -9` framing, `#` AI interface currency, Agent Mode key binding. | A "High Stakes List" for Part 4 is defined. |
| **Execution (Act)**: **The Warp Reviewer** audits Ch 12–15 for platform claims, feature accuracy, and YAML format validity. | Platform inconsistency, `#` interface currency, Agent Mode binding, and Workflow YAML verified or flagged. |
| **Execution (Act)**: **The Safety Auditor** audits Ch 13 for `kill -9` framing and Ch 14 for `>> ~/.zshrc` PATH mutation. | Kill -9 standard applied; dotfile append safety verified. |
| **Execution (Act)**: **The Thesis Guard** audits Ch 12's "machine state gap" as the thesis statement for all of Part 4. | Ch 12 thesis verdict (does it frame Warp's role in the thesis arc?) added. |
| **Execution (Validate)**: **The Scenario Auditor** verifies the Warp scenario arc in Ch 12–15 and Conclusion payoff. | Scenario closure and conclusion arc verified. |

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

- `claude_says.md` covers all 17 files (Intro, Ch 1–15, Conclusion).
- Every note is **actionable** — not descriptive. "This is unclear" is not a note.
- All 5 reviewer agent perspectives are represented.
- The Priority Heatmap distinguishes Critical (blocks reader) from Important (degrades quality) from Optional (polish).
- The `kill -9` framing verdict is explicit.
- The Warp platform availability inconsistency is resolved.
- The scenario thread has been assessed for continuity across all 15 chapters.
- The `#` AI command interface currency has been assessed.
