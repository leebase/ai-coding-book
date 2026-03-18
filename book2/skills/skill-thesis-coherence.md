# Skill: Thesis Coherence

## Goal

Ensure every chapter advances the book's central argument — that the solution to the single-agent quality ceiling is a team — and that the book's structure makes this argument by demonstration, not assertion.

## Directives

### 1. Per-Chapter Thesis Statement

- For each chapter, extract the single sentence that states the thesis claim it advances.
- If you cannot state it in one sentence, the chapter is documenting a procedure rather than making an argument. Flag it.
- Example of an argument chapter: "The researcher and the writer are separate because research and writing are different cognitive tasks — doing them simultaneously compromises both."
- Example of a documentation chapter: "Here is how to create `agents/researcher.md`." Flag this.

### 2. "Key Takeaway" Audit

- Read all Key Takeaway callouts in sequence, as if they were the only text in the book.
- Do they build a cumulative argument? Or are they disconnected principles?
- The sequence should trace the arc: ceiling → role separation → handoff contracts → coordination → limits → translation → coding team → full sprint.

### 3. Part 1 → Part 2 Translation Quality

- Chapter 7 is the translation chapter. Audit its mapping claims:
  - Content role → coding role: is each analogy tight or strained?
  - What changes (domain, output format, error stakes): is this named explicitly?
  - What does not change (role isolation, handoff contracts, gate discipline): is this stated directly?
- A mechanical translation ("researcher becomes planner") fails. An earned translation explains why the design decision is the same even though the domain is different.

### 4. Introduction Promise Audit

- Extract every promise the introduction makes to the reader.
- For each promise, identify the chapter that delivers it.
- Flag any promise without a delivery. Flag any delivery without a corresponding promise.

### 5. Chapter Ending Check

- Each chapter must end with one sentence: the principle demonstrated + door to next.
- A summary ending ("In this chapter, you built X and Y and Z") is a documentation ending. Flag it.
- A thesis ending ("Now that you have separated the researcher from the writer, you need someone who reads the result the way your reader will") advances the argument. Verify these are present.
