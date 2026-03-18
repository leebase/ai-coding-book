# The Ceiling Skeptic Mission

## Mission

Attack every claim the book makes about what the document-driven coordination system can and cannot do. The book's intellectual credibility rests on Chapter 6 and on honest framing throughout. Your goal is to find anywhere the book oversells, undersells, or names a limitation without actually enforcing it.

## Scope

- **Chapter 6 integrity:** The four failure modes (stage collapse, role drift, output variance, context accumulation) must be named accurately and with enough specificity that a reader would recognize them when they occur. Vague descriptions that sound honest without being actionable fail the audit.
- **Pre-Chapter 6 honesty:** Are any of the four failure modes implicitly present in the pipeline instructions before Chapter 6 names them? If so, the book should acknowledge them where they first appear — not warehouse all the honesty in one chapter.
- **External orchestration accuracy:** The frameworks listed in Chapter 6 must be described accurately. Verify: are LangGraph, CrewAI, OpenAI Agents SDK, Symphony, and Microsoft Agent Framework described with enough precision that a reader could investigate them? Are any descriptions outdated or misleading?
- **Quality improvement claims:** The book claims the pipeline produces "specific, traceable improvement" over single-agent output. Is this claim grounded? What specifically is traceable? Voice? Examples? Addressed misconceptions? Flag any improvement claim that can't be tied to a specific stage output.
- **Gate reliability:** The book positions the gate as the main quality instrument. Is this accurate? What does the gate not catch? The book should acknowledge this.

## Inputs

- All manuscript files in `book2/chapters/`
- `book2/skills/skill-ceiling-audit.md`
- `book2/product-definition.md` — the "Honest Ceiling" and "Constraints" sections

## Outputs

- Contributions to `book2/claude_says.md` (Ceiling Integrity section)

## Review Rules

- "Honest ceiling" does not mean pessimistic. It means accurate. Underselling the system is also a ceiling integrity failure.
- Every failure mode description must pass the "would I recognize this" test: could a reader who has never seen stage collapse recognize it from the description?
- External orchestration names must be current as of the book's publication. Frameworks that are "experimental" in the text but production-ready in reality are a credibility issue.
- The gate is described as the "main quality instrument." Audit whether the book teaches the reader what to look for at each gate — if not, the instrument is described but not calibrated.

## Done Criteria

- Chapter 6 integrity verdict included in `claude_says.md`.
- Pre-Chapter 6 honesty gaps flagged.
- External orchestration accuracy verdict included.
- Quality improvement claim grounding verdict included.
