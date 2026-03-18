# Skill: Harness Separation

## Goal

Verify that concept prose and Antigravity harness instructions are cleanly separated, such that a spin-off editor can replace every `> **Antigravity:**` callout without touching the surrounding text.

## Directives

### 1. Callout Self-Containment Test

- Read each `> **Antigravity:**` callout in isolation, ignoring surrounding prose.
- Can the step be completed from the callout alone?
- Flag any callout that references "the prompt above," "the role definition above," or "as described" — the callout must contain or fully specify what it references.

### 2. Concept Prose Independence Test

- Remove each `> **Antigravity:**` callout mentally from its surrounding context.
- Does the concept narrative remain coherent? Can the reader understand what is happening and why, without the UI steps?
- Flag any concept paragraph that only makes sense if the reader has seen the callout.

### 3. Inventory Cross-Reference

- For each of the 23 swap points in `book2/harness-inventory.md`, verify the corresponding callout exists in the chapter text.
- For each `> **Antigravity:**` callout found in the chapters, verify it appears in the inventory.
- Any mismatch is a documentation gap — flag it with the chapter and section.

### 4. UI Detail Leakage Check

- Antigravity UI details (button labels, panel names, keyboard shortcuts, menu paths) belong only inside callouts.
- Flag any UI detail embedded in concept prose.
- Flag any callout that uses vague UI language ("click the button") instead of specific labels ("click **New Session**").

### 5. Callout Type Consistency

- `> **Antigravity:**` — tool-specific UI steps only
- `> **Watch For:**` — concrete observable outcome that confirms the step succeeded
- `> **What the Agent Will Do:**` — prediction before autonomous action
- `> **Key Takeaway:**` — one sentence; the principle the reader must leave with
- Flag any callout using the wrong type for its content.
