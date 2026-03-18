# claude_says.md: Reviewer Feedback for book2

> **The Definitive Feedback Loop.**
> This document captures the collective insights of the 5-agent reviewer team.
> The Writer should use these directives to sharpen the manuscript.

---

## 1. Project Thesis & Goals

- **Thesis**: A single AI agent cannot manage complexity at scale. The solution is a team: specialized roles, shared memory, and a workflow that coordinates them.
- **Target Reader**: Experienced developers who have already hit the single-agent quality ceiling; have probably looked at orchestration frameworks and found them too heavy; need the thinking, not a framework.
- **Tone**: Peer-to-peer, systemic, no hand-holding. Trusts the reader with nuance and tradeoffs.
- **Part 1 Thread**: Content pipeline — newsletter article on "How to write documentation your future self will actually use."
- **Part 2 Thread**: Coding pipeline — `git-summary` CLI tool.

---

## 2. Pipeline Execution Gaps (The Practitioner)

### Introduction + Part 1 (Ch 1–3)

**Ch 1 — Run the Prompt**
- The comment block in `article-v1.md` asks the reader to evaluate "Voice," "Examples," and "Misconception" — but none of these dimensions have been defined yet at this point in the book. A reader who arrives at Ch 1 fresh won't know what "voice" or "misconception" means in this context. The dimensions are explained implicitly in Ch 5's comparison but nowhere in Ch 1. Either define them briefly in Ch 1 or soften the instruction to "write one honest first impression per question."
- **Register concern (not a gap)**: "A note on why the prompt is written this way: length, audience, tone, and format are all specified." This paragraph explains prompt-writing basics to a reader who already knows this. See Voice & Narrative section.

**Ch 2 — The Grounding Problem**
- Swap 2.3 Watch For says: "If the agent produces flowing prose instead, the role constraint did not hold. Add an explicit instruction at the top of your role definition: 'Your entire output must use the structured format below. Do not write prose paragraphs.'" — But that instruction IS NOT in the role definition provided in the chapter. The reader would need to know to add it preemptively. Either add it to the role definition in the chapter or soften the Watch For to "You may need to add..." rather than instructing as if it's a common enough failure that the reader should prepare for it before the first run.

**Ch 3 — The Reader Problem**
- Swap 3.3 Watch For says: "If the output is general, the role constraint did not hold. Add this line to the role definition and run it again: 'Do not give general feedback. Every item must cite a specific sentence or phrase.'" — That line IS already in the role definition provided in the chapter ("Do not suggest rewrites. Do not give style feedback. Find the silent gaps and name them precisely."). The Watch For guidance is redundant/circular. If the role definition can drift anyway, the Watch For should give different recovery text.
- The format template in the concept prose shows `[paste full contents of agents/adversarial-reader.md]\n\n---\n\n[paste full contents of draft.md]`. The Antigravity callout says "a blank line with `---`". Whether this means `\n---\n` or `\n\n---\n\n` is ambiguous. Specify the exact separator format.

### Part 1 (Ch 4–6)

**Ch 4 — Voice and Sequence**
- The `skills/article-pipeline.md` coordinator references `agents/writer.md` in Stage 2, but the writer role is introduced *after* the coordinator is built, later in the same chapter. A reader who creates the coordinator file and reads it carefully may notice the reference to a file that doesn't exist yet. Add a sentence before the coordinator: "You'll build the writer role at the end of this chapter — for now, create the coordinator file as written."
- Swap 4.1 Antigravity callout: "adjust the reader description to match your intended audience." This is the first customization invitation in the book and it's unguided. What should the reader change? Add one example: "For example, if your article targets junior developers rather than experienced ones, change the first line of The Reader section."

**Ch 5 — Run the Pipeline**
- **Gate gap**: The Antigravity callout says "At Stage 1, read `research-notes.md` before confirming it should proceed to Stage 2." How does the reader "confirm"? What do they type to the agent? The gate instruction needs a concrete action: "Type 'Stage 1 complete, proceed to Stage 2' into the session."
- **Viewing gap**: "Place both articles side by side" — the Antigravity callout doesn't specify how to view two files simultaneously. Add: "In Antigravity, open both `article-v1.md` and `article-v2.md` in the Editor pane by clicking each file. Switch between them using the file tabs."
- `article-v2.md` is created as a copy of `final.md`. The reader may wonder why two files exist with the same content. Add: "Like `article-v1.md`, `article-v2.md` is preserved as an immutable comparison artifact — do not modify it after saving."

**Ch 6 — What You Cannot Trust**
- No procedure gaps. Ch 6 is conceptual only and has no Antigravity callouts — correct.

### Part 2 (Ch 7–9)

**Ch 7 — Translating the Pattern**
- Swap 7.1 Antigravity callout: "Create `requirement.md` in a new project directory for Part 2." — No name is given for the Part 2 project directory. The Part 1 directory was named implicitly through use. Name it explicitly here: "Create a new project directory in Antigravity (right-click your workspace root → New Folder → name it `git-summary-project`). Create `requirement.md` inside it."
- **Missing Watch For**: Swap 7.1 has no Watch For callout. Every Part 1 swap point with file creation has one. Add: "**Watch For:** `requirement.md` appears in your Part 2 project with all sections — What it does, Inputs, Output format, Constraints, Out of scope. Verify the 'Out of scope' section is present before proceeding — it is the Planner's constraint boundary."

**Ch 8 — The Coding Team**
- Swap 8.1: "Create the `agents/` directory in your Part 2 project." — This is the first directory creation instruction in the book. Antigravity's file creation method (Explorer pane → New File) has been used throughout Part 1, but directory creation has not been explained. Add: "Right-click your Part 2 project in the Explorer pane, choose **New Folder**, name it `agents`."
- **Missing Watch For**: Swap 8.1 has no Watch For. Add: "**Watch For:** Five files exist in your `agents/` directory — `planner.md`, `implementer.md`, `reviewer.md`, `tester.md`, `documenter.md`. Open each and verify the first line matches the role name."

**Ch 9 — The Feature Skill**
- **Missing Watch For**: Swap 9.1 has no Watch For. Part 2 setup chapters (Ch 7, 8, 9) are consistently missing Watch For callouts that Part 1 had. This is a pattern, not an oversight — but it leaves Part 2 feeling lighter on confirmation scaffolding. Recommend adding Watch For callouts to all three. For Ch 9: "**Watch For:** `skills/feature-sprint.md` exists with all six stages. Verify the `⛔ Gate — Required` block appears between Stage 1 and Stage 2 — that gate is load-bearing."

### Part 2 (Ch 10–11) + Conclusion

**Ch 10 — Running a Sprint**

**CRITICAL**: Manager View (Swap 10.4) is introduced for the first time. The Antigravity callout explains it well. But the concept-level prose in Ch 10 says only "This is where running two simultaneous sessions pays off" with no concept-level description of what parallel sessions look like abstractly. A spin-off reader would have no concept preparation before the callout. See Harness Separation Findings for the full diagnosis. The concept prose needs a paragraph before the callout that explains parallel sessions at the concept level without naming Antigravity UI.

- Swap 10.5: "Open a new session (or return to your Stage 2 session if context is still clean)." — "Context still clean" is undefined. Add criteria: "A session is 'context clean' if it has not accumulated more than one prior exchange and the coordinator has not yet drifted from its original sequence."
- **Test-running gap**: After Stage 5, the chapter says "Run the tests again." No Antigravity callout covers this step and no Swap Point exists for it in the harness inventory. Add the step: "In a terminal (or Antigravity's built-in terminal if available), run `python -m pytest test_git_summary.py` or `python -m unittest test_git_summary` to confirm tests pass."
- **File-saving gap**: The Tester produces both `test_git_summary.py` (code) and `test-report.md` (report). The chapter instructs "Save `review-notes.md` and `test-report.md`" but does not mention saving `test_git_summary.py`. Add an instruction to save the test file.

**Ch 11 — Your Coding Team at Work**
- No execution gaps. Ch 11 is synthesis. The directory listing precisely matches what was built across Ch 7–10. ✓

---

## 3. Harness Separation Findings (The Harness Auditor)

### Ch 1–3 Swap Points (1.1–3.4)

- **1.1, 1.2**: Self-contained. Concept prose stands without callouts. ✓
- **2.1**: "Paste the prompt and send it." — In isolation, the callout doesn't include the prompt text. Acceptable: the concept prose (which would be unchanged in a spin-off) contains the prompt. The callout's phrase "the prompt" correctly refers to it. ✓
- **2.2**: "Paste the role definition above" — acceptable; concept prose contains the definition. ✓
- **2.3**: "add the topic and question above" — acceptable; concept prose contains them. ✓
- **3.1, 3.2, 3.3, 3.4**: All acceptable. Concept prose stands alone. ✓

### Ch 4–6 Swap Points (4.1–5.2)

- **4.1**: "adjust the reader description to match your intended audience" — present in concept prose context; callout acceptable. ✓
- **4.2**: Coordinator references `agents/writer.md` which doesn't exist at the point of creation. Not a harness separation issue — it's a chapter ordering issue (see Pipeline Execution Gaps).
- **5.1**: "Paste the full contents of `skills/article-pipeline.md` at the start, then add the topic and target reader above." Self-contained enough; topic is in concept prose. ✓
- **5.1 ISSUE**: "At Stage 1, read `research-notes.md` before confirming it should proceed to Stage 2." — "Confirming" requires an action not described in the callout. Spin-off editions would also lack this instruction. Add the confirmation message to the callout.

### Ch 7–9 Swap Points (7.1–9.1)

- **7.1**: Self-contained but missing Watch For. See Pipeline Execution Gaps.
- **8.1**: Self-contained but missing Watch For and directory creation instructions. See Pipeline Execution Gaps.
- **9.1**: Self-contained but missing Watch For. Consistent gap across all three Part 2 setup swaps.
- **Pattern finding**: Part 2 setup chapters (Ch 7, 8, 9) have no Watch For callouts anywhere. Part 1 has Watch For on nearly every swap point. This is the most consistent harness gap in the book. All three chapters need Watch For additions.

### Ch 10–11 Swap Points (10.1–10.6)

**CRITICAL — Swap 10.4 (Manager View / Parallel Sessions)**:
The entire concept of parallel execution is embedded inside the Antigravity callout:
> "You now have two agent cards."

The concept prose before this callout says only "This is where running two simultaneous sessions pays off" — no concept-level description of what "two simultaneous sessions" means abstractly, why isolation matters, or what the reader should be watching for as a design principle. A spin-off editor replacing the callout would need to add concept prose about parallel execution from scratch, because none exists in the current concept layer. This is the most significant harness separation violation in the book.

**Fix**: Add a concept-level paragraph before the callout: "Running Stages 3 and 4 simultaneously means each starts from the same implementation file but operates in a separate context — no shared state, no sequential dependency. Each produces its output independently. You collect both before Stage 5 can begin."

- **10.5**: "return to your Stage 2 session if context is still clean" — "context still clean" is undefined. Not self-contained for a spin-off. Add criteria.
- **10.1–10.3, 10.6**: Self-contained. ✓
- **Missing swap**: The "run tests again" step after Stage 5 has no Antigravity callout and no swap point in the harness inventory. This is a documentation gap affecting both the current edition and any spin-off.

### Harness Inventory Completeness

- 23 swap points listed in the inventory. All are present in the chapter text. ✓
- **Gap**: One untracked action in Ch 10 — the post-Stage 5 test run. The inventory should add Swap 10.5b: "Run tests to confirm Stage 5 fixes succeeded."
- **Directory creation gap**: `skills/` directory creation (Part 1) and `agents/` directory creation (Part 2) are both undocumented in the inventory. Creating a directory is a different action than creating a file in Antigravity. These should be added as swap point actions, or called out explicitly in existing swaps.
- **Callout type consistency**: Part 1 Watch For callouts are present and specific. Part 2 Watch For callouts are absent for Swaps 7.1, 8.1, and 9.1. Ch 10 Watch For callouts are present. This inconsistency should be resolved by adding the missing Watch Fors.

---

## 4. Thesis Coherence (The Thesis Guard)

### Per-Chapter Thesis Statements

| Chapter | Thesis Claim | Verdict |
|---------|-------------|---------|
| Introduction | Team > individual; coordination without infrastructure | ✓ |
| Ch 1 | Observes the ceiling — "complete is not the same as good" | ✓ Setup chapter |
| Ch 2 | Separation (research/writing) changes what the writing can trust | ✓ |
| Ch 3 | You need a role whose entire job is to not have your context | ✓ |
| Ch 4 | A coordinator turns a collection of roles into a pipeline | ✓ |
| Ch 5 | Each quality in the final article traces back to a specific role | ✓ Strongest thesis expression in Part 1 |
| Ch 6 | The design is visible — including its failure modes | ✓ |
| Ch 7 | The pattern translates directly from content to code | ✓ |
| Ch 8 | Five roles, one handoff chain, visible before code is written | ✓ |
| Ch 9 | The mandatory gate is the last cheap moment | ✓ |
| Ch 10 | Specialized roles produce better results — you have now seen both | ✓ |
| Ch 11 | The pipeline is portable | ✓ |
| Conclusion | The design is portable — roles change, pattern does not | ✓ |

The Key Takeaway sequence builds a genuine cumulative argument. Reading all 11 in order traces the arc: observe ceiling → separate (research/writing) → separate (writer/reader) → coordinate → demonstrate → name limits → translate → design team → coordinator → execute → generalize. This is the book's argument in eleven sentences and it holds. ✓

### Part 1 → Part 2 Translation Quality

Ch 7 explicitly names four things that carry over unchanged (roles over prompts, handoff contracts, coordinator, shared memory) and four things that change (pass/fail signal, reviewer vs. adversarial reader, scope discipline, order stakes). This is the most analytically rigorous chapter in the book and it does exactly what a translation chapter should do. ✓

**Minor gap**: The expansion from 3 roles (Part 1) to 5 roles (Part 2) is not explained. Why does code need two more roles than prose? The answer is implicit — the Tester provides the pass/fail signal that prose can't have, and the Documenter closes the scope boundary with observable evidence — but it's not stated. One sentence in Ch 7 or Ch 8 should name this: "Code gets two roles prose doesn't need: a Tester that can produce objective results, and a Documenter who knows from the test report exactly what the tool does not do."

### Introduction Promise Audit

| Promise | Chapter that Delivers | Verdict |
|---------|----------------------|---------|
| "what is on the other side of that ceiling" | Part 1 + Part 2 | ✓ |
| Team: specialized roles, working in sequence, coordinated by a skill | All chapters | ✓ |
| No external orchestration infrastructure required | Demonstrated throughout | ✓ |
| "learn exactly where it breaks down" | Ch 6 | ✓ |
| Ch 1 vs Ch 5 comparison: "the difference is not subtle" | Ch 5 | ✓ — names specific dimensions |
| Free tier sufficient throughout | No paid features appear | ✓ |
| "run that pipeline in Antigravity without manual intervention at every step" | Ch 10 | ⚠️ |

**Issue**: "Without manual intervention at every step" — Ch 10 shows six stages requiring: a confirmation message after Stage 1, saving files after each stage, Manager View setup, a judgment call on whether context is clean, running tests externally, and confirming the optional gate. This is substantial manual intervention. The pipeline *reduces* intervention compared to single-agent work, but "without manual intervention at every step" overstates the automation level. Soften to: "running that pipeline with far fewer intervention points than single-agent work requires."

### Chapter Endings

All 11 chapter endings are one sentence or short paragraph that states the principle + opens the door. ✓

**Minor**: Ch 11's ending is four sentences ("The pipeline is portable. The team you built for `git-summary` is the team for the next feature, and the one after that. Add roles when you need them. The coordinator grows with the work.") — the most summary-like chapter ending in the book. Consider tightening to one sentence: "The team you built for `git-summary` is already staffed for the next feature — add roles when the work requires them, not before."

---

## 5. Ceiling Integrity (The Ceiling Skeptic)

### Chapter 6 Failure Mode Descriptions

All four failure modes pass the "would I recognize this" test:

| Failure Mode | Description Quality | Verdict |
|--------------|--------------------|---------|
| Stage collapse | "runs Stages 1 and 2 together... because the agent anticipates what comes next" | ✓ Specific, recognizable |
| Role drift | "starts writing article prose because it can see where the research is going" | ✓ Specific example given |
| Output variance | "same researcher role, same topic, run twice, produces different Grounded claims... the model's sampling process is not deterministic" | ✓ Explains the mechanism |
| Context accumulation | "by Stage 4, the agent is working in a context that contains the full coordinator skill, the research notes, the draft..." | ✓ Specific stage cited |

Chapter 6 earns its "honest ceiling" label. ✓

### Pre-Chapter 6 Honesty Gaps

The book is genuinely honest before Ch 6 — failure modes are acknowledged at the point of first encountering them:

- Ch 2, Watch For: "If the agent produces flowing prose instead, the role constraint did not hold." ✓
- Ch 3, Watch For: "If the output is general... the role constraint did not hold." ✓
- Ch 4: "That instruction will be interpreted differently by every session." ✓
- Ch 5, Watch For: "If stages blend... the coordinator did not hold. Note where it broke; Chapter 6 addresses this directly." ✓
- Ch 5: "Is there a place where the adversarial reader's feedback was correct but the revision did not quite close the gap?" ✓

No pre-Ch 6 overclaims found. ✓

### External Orchestration Accuracy

| Framework | Description | Verdict |
|-----------|-------------|---------|
| LangGraph | "graph-based workflow with explicit state management and checkpointing; strongest story for complex, stateful pipelines" | ✓ Accurate |
| CrewAI | "role-based multi-agent coordination... fastest path to multi-agent prototyping; broad protocol support" | ✓ Accurate |
| OpenAI Agents SDK | "replaced the earlier experimental Swarm framework in 2025; simplest onramp if you're already using OpenAI models" | ✓ Accurate |
| Symphony | "released March 2026; monitors Linear, creates isolated workspace per issue, spawns agents through ticket lifecycle; built on Elixir/BEAM" | ✓ Accurate and timely |
| Microsoft Agent Framework | "merged AutoGen and Semantic Kernel; reached release candidate in early 2026" | ⚠️ "Release candidate" may be outdated — verify current release status as of publication |

The hedge "Search for current comparisons before committing — the relative strengths of these frameworks are changing faster than most books can track" is exactly right. ✓

### Quality Improvement Claim Grounding

Ch 5's "What the Skills Produced" section explicitly traces each quality dimension to a specific stage:

| Quality | Source Stage | Verdict |
|---------|-------------|---------|
| Consistent voice | skills/voice.md | ✓ |
| Grounded examples | agents/researcher.md | ✓ |
| Addressed misconception | research question design | ✓ |
| Located gaps closed | agents/adversarial-reader.md | ✓ |
| Sequence | skills/article-pipeline.md | ✓ |

All quality improvement claims are grounded to a specific design decision. ✓

### Gate Reliability Audit

The book calls the gate "your main quality instrument." Does it teach the reader to use it?

| Gate | Success criteria provided | Verdict |
|------|--------------------------|---------|
| Ch 4 Stage 1 gate (concept) | "read the research notes before writing begins. If anything looks uncertain, address it." | ⚠️ Vague — "looks uncertain" should be: "if the Uncertain section contains claims that would become the backbone of the article" |
| Ch 9 mandatory gate (feature sprint) | Four-item checklist: requirement → plan decision; edge cases; out of scope; agree with decisions | ✓ Specific |
| Ch 10 Stage 3/4 review | "Are the findings located? Does each one cite a specific line?" | ✓ |
| Ch 10 optional gate | "tests pass, review findings resolved, no new scope violations" | ✓ |

**Issue**: The Tester role says "Write and run tests." But the chapter instructions treat test-running as a human action ("Run the tests again" after Stage 5). The book never explicitly resolves whether the Tester agent runs the tests or writes them for the human to run. In a real Antigravity session, the agent almost certainly writes the tests but cannot execute them in a live Python environment. The Tester role definition ("write and run tests") overstates what the agent does — it should say "write tests and report expected results." The actual test execution is a human step.

**What the gate doesn't catch**: The book doesn't name what the gate misses. Ch 6 covers output variance as a failure mode, but doesn't say explicitly "the gate cannot catch output variance between runs." This would sharpen the chapter: add one sentence after the gate discussion — "The gate catches what the current run produced. It cannot tell you whether the next run will be better or worse."

---

## 6. Voice & Narrative (The Senior Dev)

### Register Violations by Chapter

**Ch 1**:
- "A note on why the prompt is written this way: length, audience, tone, and format are all specified. A vague prompt produces a vague output, and a vague output is hard to compare to anything." — This explains prompt construction basics to a reader who has been using AI agents long enough to hit a quality ceiling. They know this. **Cut the paragraph or replace with**: "The constraints are specific so the output is specific enough to compare to something — format, length, and topic are nailed down."
- "You want something complete enough to be a real artifact." — "real artifact" is fine. But the preceding explanation is patronizing to the target reader.

**Ch 2**:
- "A role is not a prompt. A prompt tells the agent what to produce. A role defines what the agent *is* during this task — its perspective, its constraints, and its output format." — This is a meaningful distinction that the book uses throughout, and it's worth making once. But the explanation continues: "Those three things change what gets produced." This last sentence is redundant — the reader already understood from the first three sentences. Cut it.

**Ch 3**:
- "This is not an AI problem. It is an architecture problem." ✓ Perfect register.
- "This is structural, not stylistic." ✓ Good.
- No register violations in Ch 3 beyond the norm. ✓

**Ch 4**:
- The "Two Kinds of Files" section explains agents vs. skills. This explanation is genuinely new information — not a register violation. ✓
- "The directory names are not decorative." ✓ Exactly right tone.

**Ch 5**:
- "The comparison is the argument this book has been building." ✓ Transparent without being condescending.
- No register violations. ✓

**Ch 6**:
- Strongest register in the book. "You are not going to fix this by asking the agent to 'only use real examples.'" ✓ Direct, trusts the reader.

**Ch 7–11**:
- "This chapter is a walkthrough, not a tutorial. You have done every step before — you built all the roles, you built the coordinator, you know what each stage produces." ✓ Ch 10's opening is the best register statement in Part 2.
- No register violations found in Part 2.

**Conclusion**:
- "We are early in that story." — Shifts from second-person voice used throughout the book. The "we" includes the author in a way that feels slightly different. Minor — not a violation, but notable.
- "The third level — which frameworks like OpenAI's Symphony are beginning to approach — is the system where you manage the work, not the agents. You move a ticket to 'Ready.' The pipeline picks it up..." — This describes a future state aspirationally. For a book that commits to "no hype," this passage is the closest thing to hype in the whole text. It's describing what Symphony *approaches*, not what it does. Soften to: "The third level is being built now. Symphony is the closest existing example — you move a ticket to 'Ready' and the pipeline handles the sprint."

### Weasel Words

No "basically," "actually," "simply," or "of course" instances found in a reading pass. The book avoids these consistently. ✓

"Just" appears once: in Ch 1, the Watch For callout instructs the reader to reply "just write it" to the agent if it asks a clarifying question. This is a direct instruction, not a hedge — acceptable in context.

### Part 1 Project Thread State Table

| Chapter | Files Created | Files Modified | Files Referenced |
|---------|--------------|----------------|-----------------|
| Introduction | — | — | — |
| Ch 1 | `article-v1.md` | — | — |
| Ch 2 | `agents/researcher.md`, `research-notes.md` | — | — |
| Ch 3 | `agents/adversarial-reader.md`, `draft.md`, `reader-notes.md` | `draft.md` | `research-notes.md` |
| Ch 4 | `skills/voice.md`, `skills/article-pipeline.md`, `agents/writer.md` | — | `agents/researcher.md`, `agents/adversarial-reader.md` |
| Ch 5 | `final.md`, `article-v2.md`, `research-notes.md` (new run), `draft.md` (new run), `reader-notes.md` (new run) | — | `article-v1.md`, all agents, pipeline |
| Ch 6 | — | — | `final.md` |

Ch 5 explicitly acknowledges that research-notes.md, draft.md, and reader-notes.md are replaced by the pipeline run. ✓ State is consistent.

**Issue**: `skills/` directory is never explicitly created in Ch 4 — only individual files within it. Same issue as `agents/` in Ch 2. Both Antigravity callouts say "Create `skills/voice.md`" without a prior step to create the directory. In Antigravity, creating a file at a path (`skills/voice.md`) may auto-create the directory, or may not — this behavior should not be assumed. Add explicit directory creation steps.

### Part 2 Project Thread State Table

| Chapter | Files Created | Files Referenced |
|---------|--------------|-----------------|
| Ch 7 | `requirement.md` | — |
| Ch 8 | `agents/planner.md`, `agents/implementer.md`, `agents/reviewer.md`, `agents/tester.md`, `agents/documenter.md` | `requirement.md` |
| Ch 9 | `skills/feature-sprint.md` | all agents |
| Ch 10 | `plan.md`, `git_summary.py`, `review-notes.md`, `test-report.md`, `test_git_summary.py`, `README.md` | all prior |
| Ch 11 | — | all prior |

Ch 11's directory listing precisely matches what was created across Ch 7–10. ✓ State is consistent throughout Part 2.

**Issue**: `test_git_summary.py` is created by the Tester in Ch 10 but is never explicitly instructed to be saved in the prose. "Save `review-notes.md` and `test-report.md`" omits the test file. Add "Save `review-notes.md`, `test-report.md`, and `test_git_summary.py`."

### Part 1 → Part 2 Transition Quality

Ch 7 opens with an explicit callback: "You built a pipeline that takes a topic and produces a finished article. Researcher, Writer, Adversarial Reader, Coordinator. The pipeline works because each role does one thing, each stage hands off a structured output, and the coordinator enforces the sequence. Now you are going to build the same thing for code."

This is exactly right. The transition names what was built, names what carries, names what changes. The reader feels continuous momentum, not a reset. ✓

The Part 2 chapters maintain the same structural clarity as Part 1. The handoff chain diagram in Ch 8 is particularly good — it makes the dependency structure visible before any code is written. ✓

---

## 7. Priority Heatmap

### [CRITICAL] Blockers — Fix First

1. **Manager View concept gap (Ch 10, Swap 10.4)**: The concept of parallel sessions has no concept-level explanation — it lives entirely inside the Antigravity callout. A spin-off edition cannot be produced without reconstructing concept prose from scratch. Add a concept paragraph before the callout.

2. **Missing test-run step (Ch 10, post-Stage 5)**: "Run the tests again" has no Antigravity callout and no instructions for how to run the tests. The reader has `test_git_summary.py` but no guidance on executing it. Add the command.

3. **Gate confirmation gap (Ch 5, Swap 5.1)**: "Confirming" the Stage 1 gate has no specified action. The reader doesn't know what to type. Add the confirmation message.

4. **Tester role overclaim**: The Tester role definition says "Write and run tests." In a document-driven pipeline, the agent almost certainly writes tests but cannot execute them in a live environment. The role definition and the Ch 10 execution both need to clarify who runs the tests and how.

### [IMPORTANT] Quality Degraders — Fix Next

5. **Part 2 Watch For gaps**: Swaps 7.1, 8.1, and 9.1 all missing Watch For callouts. Part 2 setup chapters (Ch 7, 8, 9) have no Watch For callouts anywhere. Add them.

6. **Directory creation unspecified**: `skills/` directory (Ch 4) and `agents/` directory (Ch 2, Ch 8) are never explicitly created. Antigravity callouts jump to file creation. Add `New Folder` instructions.

7. **Introduction overclaim**: "without manual intervention at every step" overstates automation. Ch 10 requires six human actions across the sprint. Soften the framing.

8. **Ch 1 comment block**: The four evaluation dimensions (Voice, Examples, Misconception, Send test) are not defined at the point of use. Either define them briefly or soften the instruction.

9. **Role expansion gap (Ch 7/8)**: The expansion from 3 Part 1 roles to 5 Part 2 roles is unexplained. Add one sentence naming why code needs a Tester and Documenter that prose doesn't.

10. **Microsoft Agent Framework release status**: "Release candidate in early 2026" may be outdated. Verify before publication.

### [OPTIONAL] Polish — Nice to Have

11. **Ch 1 register**: The "A note on why the prompt is written this way" paragraph explains prompt basics to an experienced reader. Trim or replace.

12. **Ch 2 "A role is not a prompt" explanation**: The last sentence ("Those three things change what gets produced") is redundant. Cut it.

13. **Ch 11 ending**: Four sentences where one would do. Consider tightening.

14. **Conclusion "we" pronoun**: Single shift to first-person plural in an otherwise second-person book. Consistent with tone but notable.

15. **Conclusion Symphony description**: "Beginning to approach" reads aspirationally. Soften to what Symphony currently does.

16. **`article-v2.md` preservation note**: Add a sentence clarifying that `article-v2.md` is an immutable comparison artifact like `article-v1.md`.

17. **Gate "looks uncertain" language (Ch 4)**: Vague. Tie it to the Uncertain section of the research notes output format.

---

## 8. Final Synthesis for Writer

The book earns its thesis. The Key Takeaway sequence is a genuine eleven-sentence argument. The Part 1 → Part 2 translation (Chapter 7) is the most analytically rigorous chapter and does exactly what a translation chapter should do. Chapter 6 is genuinely honest — the failure modes are specific enough to recognize in practice, and the book acknowledges them before they're named, in the Watch For callouts throughout Part 1.

The issues found are concentrated in two areas: **execution completeness** (missing instructions for test-running, gate confirmation, directory creation, and Manager View concept) and **harness separation** (Part 2 Watch For callouts absent, Manager View concept embedded in callout). These are fixable without touching the conceptual layer.

**Writer Directives:**

1. **Fix the execution gaps first**: The four Critical items (Manager View concept, test-run step, gate confirmation, Tester role definition) are the ones that would cause a reader to stop mid-chapter and not know how to continue. These are the book's only blockers.

2. **Add Watch For callouts to Ch 7, 8, 9**: Part 1's confirmation scaffolding is one of the book's strengths. Part 2 loses it in the setup chapters. Three Watch For callouts would restore consistency.

3. **Don't touch the voice**: The book's register is strong and consistent from Introduction through Chapter 10. The minor violations in Ch 1 and the Conclusion are the only places the voice drifts, and neither is damaging.

4. **Don't touch Chapter 6**: It is exactly right — specific enough to be actionable, honest enough to be trusted, and calibrated enough to not undermine the reader's confidence in the system they just built.

5. **The comparison exercise (Ch 1→Ch 5) delivers**: The five named dimensions (Voice, Examples, Misconception, Silent gaps, Send test) are specific and traceable. The book keeps its biggest promise.

**Review Status**: COMPLETE
**Verdict**: PASS with Required Revisions (see Priority Heatmap — 4 Critical items)
