# Skill: Thesis Coherence Audit

## Goal

Verify that every chapter advances the book's central argument — "You don't need to be a sysadmin. You need to recognize what you're looking at." — and that the book proves this by demonstration, not assertion.

## Directives

### 1. Per-Chapter Thesis Extraction

For each chapter, extract the single sentence that states the argument it makes. Format:
- **Chapter N:** [one-sentence thesis]
- **Flag:** if you cannot state it in one sentence — the chapter is documenting, not arguing

The arc should trace: snapshot model → remote coordination → auth → isolation → recovery → environment invisibility → tool selection → dependency management → runtime understanding → version management → module system → machine state gap → AI-augmented terminal → environment management → AI division of labor.

### 2. "Recognition" Language Audit

The thesis is about recognition, not memorization. Flag:
- Any passage that says "you must remember" instead of "you'll recognize"
- Any command list presented as things to memorize
- Any chapter that ends with "you now know X" rather than "you can now see X"

### 3. Key Insight Callout Arc

Read all Key Insight / Key Takeaway callouts in sequence, in isolation from the prose. Ask:
- Do they build a cumulative argument?
- Does each callout advance from the previous?
- Or are they isolated tips that could be reordered without loss?

A coherent arc is a PASS. Isolated tips are a FAIL.

### 4. Introduction Promise Audit

Extract every promise the Introduction makes. Map each to a chapter:

| Promise | Delivery Chapter |
|---------|-----------------|
| ? | ? |

Flag any promise without a delivery. Flag any major chapter delivery without a corresponding introduction promise.

### 5. Chapter Ending Quality

Each chapter should end with: the principle demonstrated + door to the next chapter. Test each chapter ending:
- **PASS:** ends with the argument made + setup for the next argument
- **FAIL:** ends with a list of "what you learned" (summary ending)
- **FAIL:** ends abruptly without transition

### 6. Part Structure Argument

The book has 4 parts. Verify each Part opener argues why this group of topics belongs together:
- Part 1 (Git + GitHub): version control as the foundation of all state management
- Part 2 (Python env): the invisible environment problem
- Part 3 (Node): the second invisible environment problem
- Part 4 (Warp): the AI layer that makes all of this more powerful

Flag any Part opener that just lists chapters rather than making an argument.
