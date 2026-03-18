# The Harness Auditor Mission

## Mission

Verify that the concept/harness separation is clean enough to support spin-off editions. Every `> **Antigravity:**` callout is a swap point. Every concept paragraph must stand alone without it. Your goal is to find anywhere the boundary has been violated — in either direction.

## Scope

- **Callout completeness:** Every `> **Antigravity:**` callout must contain enough specificity to execute the step without referring to the surrounding prose. A spin-off editor replaces only the callout — the reader of the spin-off edition gets only the callout content.
- **Concept prose independence:** The concept narrative must be coherent and actionable without the Antigravity callout. If removing a callout leaves the reader unable to follow the concept, the concept is leaking into the harness.
- **Harness inventory alignment:** Cross-reference the 23 swap points in `book2/harness-inventory.md` against the actual callouts in the chapters. Are any swap points missing? Are there callouts in the chapters not captured in the inventory?
- **UI leakage:** Flag any Antigravity UI detail (panel names, button labels, keyboard shortcuts) embedded in concept prose rather than inside a callout.
- **Cross-chapter callout consistency:** Are callout formats consistent across all 11 chapters? Do the `> **Watch For:**` blocks always specify a concrete observable outcome?

## Inputs

- All manuscript files in `book2/chapters/`
- `book2/skills/skill-harness-separation.md`
- `book2/harness-inventory.md`
- `book2/skills/book-2-voice.md` (callout box conventions)

## Outputs

- Contributions to `book2/claude_says.md` (Harness Separation Findings section)

## Review Rules

- Test each callout in isolation: if you read only the callout, can you complete the step?
- Test each concept paragraph without its callout: does the narrative still make sense?
- Flag callouts that say "as described above" — the callout must be self-contained.
- Any Chapter 11 swap point not in the inventory is a documentation gap that will hurt spin-off editors.

## Done Criteria

- All harness boundary violations logged in `claude_says.md`.
- Inventory completeness verdict included.
- Callout consistency verdict across all chapters included.
