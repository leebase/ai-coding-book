# Teach Yourself Anything - Result Review

> Running log of completed work. Newest entries at the top.

---

## 2026-03-25 - Paragraph Shape Pass Applied And Outputs Rebuilt

Applied a dedicated prose-shape pass after a fresh human read surfaced that too
many adjacent standalone sentences were acting like chopped-up paragraphs. This
was not a thesis or voice rewrite. It was a page-texture pass: merging obvious
sentence clusters into fuller paragraphs while keeping isolated one-line beats
only where they still earned emphasis.

The highest-impact files revised in this pass were:

- `chapters/introduction.md`
- `chapters/part-1/ch-01-youre-not-stuck.md`
- `chapters/part-1/ch-02-what-this-machine-gives-you.md`
- `chapters/part-1/ch-03-learning-without-permission.md`
- `chapters/part-2/ch-04-meet-the-machine.md`
- `chapters/part-2/ch-06-the-terminal-is-not-a-wall.md`
- `chapters/part-2/ch-07-read-the-manual-then-make-it-yours.md`
- `chapters/part-3/ch-10-the-horse-not-the-car.md`
- `chapters/conclusion.md`

After the source edits, rebuilt:

- `teach-yourself-anything.md`
- `teach-yourself-anything.epub`
- `teach-yourself-anything.docx`
- `teach-yourself-anything.pdf`

### How to Verify

1. Rebuild the outputs:

```bash
python3 linux-ai-kickoff/build-manuscript.py
python3 linux-ai-kickoff/build-epub.py
python3 linux-ai-kickoff/build-docx.py
python3 linux-ai-kickoff/build-pdf.py
```

2. Spot-check the revised chapters in source:

```bash
sed -n '1,120p' linux-ai-kickoff/chapters/introduction.md
sed -n '1,120p' linux-ai-kickoff/chapters/part-1/ch-01-youre-not-stuck.md
sed -n '1,120p' linux-ai-kickoff/chapters/conclusion.md
```

3. Confirm the rebuilt artifacts exist and are fresh:

```bash
ls -lh linux-ai-kickoff/teach-yourself-anything.{md,epub,docx,pdf}
```

4. Open the exported files and check that explanatory sections now read in
fuller paragraphs while key emphasis lines still stand alone where warranted.

---

## 2026-03-25 - EPUB XML Parse Error Fixed

Fixed the EPUB exporter after a reader hit this XML error:
`PCDATA invalid Char value 12`.

The root cause was a literal form-feed character getting carried into the EPUB
XHTML from the shared cover/title-page export markdown. The fix was to make
`build-epub.py` export from the assembled manuscript directly while still using
the EPUB cover metadata path. That removes the invalid character and also
cleans up the duplicated title entries at the top of the EPUB TOC.

### How to Verify

1. Rebuild the EPUB:

```bash
python3 linux-ai-kickoff/build-epub.py
```

2. Confirm no XHTML or package file contains a form-feed character:

```bash
python3 - <<'PY'
from pathlib import Path
import zipfile
path = Path('linux-ai-kickoff/teach-yourself-anything.epub')
with zipfile.ZipFile(path) as zf:
    found = [
        name for name in zf.namelist()
        if name.endswith(('.xhtml', '.html', '.opf', '.ncx')) and b'\\x0c' in zf.read(name)
    ]
print(found or 'no-form-feed')
PY
```

3. Inspect the EPUB nav and confirm it starts at the actual book body instead
   of duplicate title-page entries:

```bash
unzip -p linux-ai-kickoff/teach-yourself-anything.epub EPUB/nav.xhtml | sed -n '1,40p'
```

---

## 2026-03-25 - Review Polish Pass Applied And Outputs Rebuilt

Applied the first external review as a targeted polish pass instead of a
rewrite. The main changes were:

- consolidating the `Super` explanation into Chapter 4
- adding a new appendix,
  `chapters/appendices/appendix-translate-this-book-to-your-machine.md`, so
  non-Omarchy readers can translate one concrete step at a time with AI
- pointing Chapter 4 to that appendix at the start of Part 2
- adding an explicit "do the mission over finishing the next chapter" rule in
  Chapter 12
- strengthening the conclusion with a short Apple IIe autobiographical note
- widening Chapter 15's kept-artifact examples to include household and
  troubleshooting use cases

After those source edits, rebuilt:

- `teach-yourself-anything.md`
- `teach-yourself-anything.epub`
- `teach-yourself-anything.docx`
- `teach-yourself-anything.pdf`

### How to Verify

1. Confirm the source edits exist:

```bash
rg -n "Translate This Book To Your Machine|Apple IIe|household-schedule|troubleshooting-log" \
  linux-ai-kickoff/chapters \
  linux-ai-kickoff/teach-yourself-anything.md
```

2. Confirm Part 2 now explains `Super` once and then trusts it:

```bash
rg -n "From this point on, when the book says `Super`|If .*Super" \
  linux-ai-kickoff/chapters/part-2
```

3. Confirm the appendix made it into the EPUB nav:

```bash
unzip -p linux-ai-kickoff/teach-yourself-anything.epub EPUB/nav.xhtml | rg "Appendix: Translate This Book To Your Machine"
```

4. Confirm the rebuilt DOCX contains the new review-driven strings:

```bash
unzip -p linux-ai-kickoff/teach-yourself-anything.docx word/document.xml | \
  rg "Appendix: Translate This Book To Your Machine|household-schedule|Apple IIe"
```

---

## 2026-03-25 - Export Pipeline And Renamed Book Artifacts Built

Built a local publication/export pipeline for `Teach Yourself Anything` inside
`linux-ai-kickoff/`. The book now assembles into
`teach-yourself-anything.md` and exports to:

- `teach-yourself-anything.epub`
- `teach-yourself-anything.docx`
- `teach-yourself-anything.pdf`

The exported artifacts use `TeachYourselfAnything.png` as the embedded cover.
EPUB and DOCX build through local pandoc-based exporters, and PDF uses an
explicit raw LaTeX cover page so the cover becomes the real first page instead
of getting buried behind generated front matter.

### How to Verify

1. Run the local build scripts:

```bash
python3 linux-ai-kickoff/build-manuscript.py
python3 linux-ai-kickoff/build-epub.py
python3 linux-ai-kickoff/build-docx.py
python3 linux-ai-kickoff/build-pdf.py
```

2. Confirm the built files exist:

```bash
ls -lh linux-ai-kickoff/teach-yourself-anything.{md,epub,docx,pdf}
```

3. Confirm the archive formats contain the cover image:

```bash
unzip -l linux-ai-kickoff/teach-yourself-anything.epub | rg 'cover|png|media'
unzip -l linux-ai-kickoff/teach-yourself-anything.docx | rg 'media/|docProps/core.xml'
```

4. Confirm the PDF leads with the cover:

```bash
qlmanage -t -s 800 -o /tmp linux-ai-kickoff/teach-yourself-anything.pdf
open /tmp/teach-yourself-anything.pdf.png
```

---

## 2026-03-25 - Sprint 25 Copyedit and Voice Pass Applied

Ran the final polish pass across the manuscript. This pass focused on the
highest-value remaining soft spots after continuity and source truth were
already handled: repeated cadences, a few weak chapter endings, a couple of
slightly fuzzy artifact references, and the last places where the book's voice
was more patterned than invisible.

The main changes were tying Chapter 12 more explicitly back to the Part 1
`starter note`, tightening Chapter 17 and Chapter 18 to the same launchpad
goal folder wording, sharpening the endings of Chapter 5 and Chapter 8, varying
the Part 5 closing cadence, and softening the conclusion's repeated thesis
wording so the close lands more like ownership than slogan.

### How to Verify

1. Read `linux-ai-kickoff/chapters/reviews/copyedit-and-voice-pass-review.md`
2. Read `linux-ai-kickoff/chapters/part-4/ch-12-build-your-launchpad.md`, `linux-ai-kickoff/chapters/part-5/ch-17-build-your-own-curriculum.md`, and `linux-ai-kickoff/chapters/part-5/ch-18-keep-going-without-permission.md` and confirm the artifact wording is fully aligned
3. Read `linux-ai-kickoff/chapters/part-2/ch-05-move-through-it.md`, `linux-ai-kickoff/chapters/part-3/ch-08-ai-is-not-a-vending-machine.md`, and `linux-ai-kickoff/chapters/conclusion.md` and confirm the closing lines are tighter
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 25 complete

---

## 2026-03-25 - Sprint 24 Technical Accuracy and Source Pass Applied

Ran a source-truth pass on the Omarchy-dependent material and re-checked the
book's core technical claims against the live Omarchy manual. The pass focused
on the manual sections the manuscript relies on most: Welcome, Navigation,
Hotkeys, Unified clipboard, Terminal, AI, Development Tools, and Shell Tools.

The good news is that the book's core Omarchy guidance still lines up with the
live manual. The only manuscript tweak needed was making Chapter 7's AI section
more specific by naming the current Omarchy AI tools directly: OpenCode, Claude
Code, and Voxtype.

### How to Verify

1. Read `linux-ai-kickoff/chapters/reviews/technical-accuracy-pass-review.md`
2. Read `linux-ai-kickoff/chapters/part-2/ch-07-read-the-manual-then-make-it-yours.md` and confirm the AI paragraph now names OpenCode, Claude Code, and Voxtype
3. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 24 complete

---

## 2026-03-25 - Sprint 23 Full Continuity Pass Applied

Ran a full-manuscript continuity pass and fixed the highest-value seams across
the draft. The main changes were stabilizing the early Part 1 note thread as a
named `starter note`, carrying that thread more explicitly through Chapters 1-3,
clarifying how `mission.md` and `direction.md` relate at the Part 4 -> Part 5
handoff, making the `curriculum.md` contract internally consistent, and paying
the full artifact chain off more explicitly in the conclusion.

The pass also cleaned up a few manuscript-level voice seams: several harsher
lines in the introduction and Part 1 were softened, the early examples widened
slightly so the book's broader "anything" promise appears sooner, and the
reusable Team-Captain prompt in Chapter 9 is now explicitly something the
reader keeps in their notes.

### How to Verify

1. Read `linux-ai-kickoff/chapters/reviews/full-continuity-pass-review.md`
2. Read `linux-ai-kickoff/chapters/introduction.md` and confirm the `starter note` is named as a persistent thread
3. Read `linux-ai-kickoff/chapters/part-1/ch-01-youre-not-stuck.md`, `linux-ai-kickoff/chapters/part-1/ch-02-what-this-machine-gives-you.md`, and `linux-ai-kickoff/chapters/part-1/ch-03-learning-without-permission.md` and confirm the same note is carried through Part 1
4. Read `linux-ai-kickoff/chapters/part-5/ch-16-pick-a-direction.md` and confirm `mission.md` and `direction.md` are explicitly related
5. Read `linux-ai-kickoff/chapters/part-5/ch-17-build-your-own-curriculum.md` and confirm the curriculum contract matches the template
6. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 23 complete

---

## 2026-03-25 - Sprint 22 Conclusion Drafted

Completed the conclusion, `You Can Keep Going`, with the full sprint artifact
set:

- `chapters/briefs/conclusion-brief.md`
- `chapters/reviews/conclusion-review.md`
- `chapters/conclusion.md`

The conclusion closes the book by restating the thesis through the reader's
proof rather than through recap. The review pass tightened the ending around
the real artifact chain, softened lines that risked sounding too slogan-like or
too dismissive of real constraints, and ended on `next-three-moves.md` so the
book points outward through a concrete next move.

### How to Verify

1. Read `linux-ai-kickoff/chapters/conclusion.md`
2. Read `linux-ai-kickoff/chapters/briefs/conclusion-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/conclusion-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 22 complete

---

## 2026-03-25 - Sprint 21 Chapter 18 Drafted

Completed Part 5 Chapter 3, `Keep Going Without Permission`, with the full
sprint artifact set:

- `chapters/briefs/ch-18-keep-going-without-permission-brief.md`
- `chapters/reviews/ch-18-keep-going-without-permission-review.md`
- `chapters/part-5/ch-18-keep-going-without-permission.md`

This chapter closes Part 5 by turning `curriculum.md` into a near-term action
plan the reader can carry on their own. The review pass kept "without
permission" practical instead of dramatic, anchored the visible outcome to a
kept `next-three-moves.md` note, added a stall-recovery loop for when the
reader wobbles, and ended with Move 1 already started or scheduled so the part
lands on motion instead of reflection.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-5/ch-18-keep-going-without-permission.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-18-keep-going-without-permission-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-18-keep-going-without-permission-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 21 complete

---

## 2026-03-25 - Sprint 20 Chapter 17 Drafted

Completed Part 5 Chapter 2, `Build Your Own Curriculum`, with the full sprint
artifact set:

- `chapters/briefs/ch-17-build-your-own-curriculum-brief.md`
- `chapters/reviews/ch-17-build-your-own-curriculum-review.md`
- `chapters/part-5/ch-17-build-your-own-curriculum.md`

This chapter turns the reader's `direction.md` note into a kept
`curriculum.md` roadmap inside the same launchpad folder. The review pass
tightened the chapter so "curriculum" stays small and usable instead of
school-like, required each mission to point to a supporting doc, tool, and
done signal, widened the examples beyond tech-only paths, and ended with a
real start-now nudge so the chapter lands on motion instead of planning.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-5/ch-17-build-your-own-curriculum.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-17-build-your-own-curriculum-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-17-build-your-own-curriculum-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 20 complete

---

## 2026-03-25 - Sprint 19 Chapter 16 Drafted

Completed Part 5 Chapter 1, `Pick a Direction`, with the full sprint artifact
set:

- `chapters/briefs/ch-16-pick-a-direction-brief.md`
- `chapters/reviews/ch-16-pick-a-direction-review.md`
- `chapters/part-5/ch-16-pick-a-direction.md`

This chapter starts Part 5 by helping the reader step back from the Part 4
launchpad work and read real signals from what they actually built, fixed, and
kept. The review pass tightened the evidence-based framing, added a fallback
for readers with no obvious "most alive" signal yet, kept the AI step optional
and coach-like, and anchored the chapter's outcome to a kept `direction.md`
note in the existing launchpad folder so Chapter 17 has a real handoff object.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-5/ch-16-pick-a-direction.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-16-pick-a-direction-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-16-pick-a-direction-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 19 complete

---

## 2026-03-25 - Sprint 18 Chapter 15 Drafted

Completed Part 4 Chapter 4, `Ship a Small Win`, with the full sprint artifact
set:

- `chapters/briefs/ch-15-ship-a-small-win-brief.md`
- `chapters/reviews/ch-15-ship-a-small-win-review.md`
- `chapters/part-4/ch-15-ship-a-small-win.md`

This chapter closes Part 4 by turning the launchpad, helper, and recovery skill
into one real kept artifact. The reader starts with `start-goal.sh`, asks AI
for one 20-minute deliverable tied to the mission note, creates one real file,
and finishes it enough to keep. The review pass also tightened the scope rule,
made the fallback from a broken helper more concrete, and sharpened the final
proof check so the win is unmistakable.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-4/ch-15-ship-a-small-win.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-15-ship-a-small-win-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-15-ship-a-small-win-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 18 complete

---

## 2026-03-25 - Sprint 17 Chapter 14 Drafted

Completed Part 4 Chapter 3, `Fix What Breaks`, with the full sprint artifact
set:

- `chapters/briefs/ch-14-fix-what-breaks-brief.md`
- `chapters/reviews/ch-14-fix-what-breaks-review.md`
- `chapters/part-4/ch-14-fix-what-breaks.md`

This chapter turns recovery into a real skill instead of a scary interruption.
It uses the same `start-goal.sh` helper from Chapter 13, introduces one small
wrong-path failure, and walks the reader through reading the error literally,
checking the real files, asking AI with exact evidence, fixing one line, and
testing again. The review pass also made the exercise reliable by giving the
reader a safe intentional break if their real helper already works, and it kept
the Omarchy manual in the troubleshooting loop as a lookup aid.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-4/ch-14-fix-what-breaks.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-14-fix-what-breaks-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-14-fix-what-breaks-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 17 complete

---

## 2026-03-25 - Sprint 16 Chapter 13 Drafted

Completed Part 4 Chapter 2, `Make One Useful Tool`, with the full sprint
artifact set:

- `chapters/briefs/ch-13-make-one-useful-tool-brief.md`
- `chapters/reviews/ch-13-make-one-useful-tool-review.md`
- `chapters/part-4/ch-13-make-one-useful-tool.md`

This chapter turns the launchpad into leverage with one tiny helper the reader
can actually reuse. It keeps the same goal folder and `mission.md` from Chapter
12, uses the Omarchy manual before AI clarification, and builds a small sourced
helper that drops the reader into the goal folder and prints the mission note.
The review pass also fixed the shell-behavior mismatch between `bash` and
`source`, added a concrete edit/save path, and made the failure path more real
for beginners.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-4/ch-13-make-one-useful-tool.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-13-make-one-useful-tool-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-13-make-one-useful-tool-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 16 complete

---

## 2026-03-25 - Sprint 15 Chapter 12 Drafted

Completed Part 4 Chapter 1, `Build Your Launchpad`, with the full sprint
artifact set:

- `chapters/briefs/ch-12-build-your-launchpad-brief.md`
- `chapters/reviews/ch-12-build-your-launchpad-review.md`
- `chapters/part-4/ch-12-build-your-launchpad.md`

This chapter starts the practical half of the book with the first kept artifact
instead of another drill. The reader chooses one real direction, uses AI to
shrink it into a folder name and mission sentence, creates `~/launchpad` plus a
goal folder, and adds a `mission.md` note they can keep building from. The
review pass also restored the manual-first flow, made the file-creation path
concrete for beginners, and clarified that Chapter 13 will keep using the same
workspace instead of starting over.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-4/ch-12-build-your-launchpad.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-12-build-your-launchpad-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-12-build-your-launchpad-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 15 complete

---

## 2026-03-25 - Sprint 14 Chapter 11 Drafted

Completed Part 3 Chapter 4, `Ask, Refine, Test, Repeat`, with the full sprint
artifact set:

- `chapters/briefs/ch-11-ask-refine-test-repeat-brief.md`
- `chapters/reviews/ch-11-ask-refine-test-repeat-review.md`
- `chapters/part-3/ch-11-ask-refine-test-repeat.md`

This chapter turns Part 3's mental models into a practical working loop. It
shows one full ask-refine-test-repeat cycle on a small safe terminal task,
explains why testing is where reality enters the process, and keeps the reader
in charge of the work instead of waiting for one perfect AI answer. The review
pass also made the repeat step concrete, clarified beginner terms like `pwd`
and `~`, marked the example as a warm-up drill, and set up Part 4's launchpad
thread cleanly.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-3/ch-11-ask-refine-test-repeat.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-11-ask-refine-test-repeat-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-11-ask-refine-test-repeat-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 14 complete

---

## 2026-03-25 - Sprint 13 Chapter 10 Drafted

Completed Part 3 Chapter 3, `The Horse, Not the Car`, with the full sprint
artifact set:

- `chapters/briefs/ch-10-the-horse-not-the-car-brief.md`
- `chapters/reviews/ch-10-the-horse-not-the-car-review.md`
- `chapters/part-3/ch-10-the-horse-not-the-car.md`

This chapter turns the horse-not-car mental model into a practical reader tool.
It explains why AI drift is normal, names a few common forms of drift in plain
language, and teaches four clean redirect moves so the reader can steer the
interaction back toward usefulness. The review pass also tightened the agency
frame by making steering feel learnable, treating drift as useful information,
and keeping the full ask-refine-test-repeat loop reserved for Chapter 11.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-3/ch-10-the-horse-not-the-car.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-10-the-horse-not-the-car-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-10-the-horse-not-the-car-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 13 complete

---

## 2026-03-25 - Sprint 12 Chapter 9 Drafted

Completed Part 3 Chapter 2, `Pick the Right Hero`, with the full sprint
artifact set:

- `chapters/briefs/ch-09-pick-the-right-hero-brief.md`
- `chapters/reviews/ch-09-pick-the-right-hero-review.md`
- `chapters/part-3/ch-09-pick-the-right-hero.md`

This chapter turns the book's Team-Captain mental model into a practical reader
tool. It teaches four moves: pick the right helper role, give backstory, assign
the mission, and stay in charge. The review pass tightened the metaphor,
defined exactly what a Team-Captain prompt is, added a step-by-step built
example, and made the final visible outcome more explicit.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-3/ch-09-pick-the-right-hero.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-09-pick-the-right-hero-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-09-pick-the-right-hero-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 12 complete

---

## 2026-03-25 - Sprint 11 Chapter 8 Drafted

Completed Part 3 Chapter 1, `AI Is Not a Vending Machine`, with the full sprint
artifact set:

- `chapters/briefs/ch-08-ai-is-not-a-vending-machine-brief.md`
- `chapters/reviews/ch-08-ai-is-not-a-vending-machine-review.md`
- `chapters/part-3/ch-08-ai-is-not-a-vending-machine.md`

This chapter opens Part 3 by reframing AI as tutor, coach, and collaborator
instead of as an answer machine. It teaches a small rewrite pattern the reader
can use immediately: ground the situation, narrow the question, and ask for one
kind of help. The review pass also made the examples more beginner-safe by
swapping in self-contained scenarios, adding an annotated worked rewrite, and
making the visible win more explicit.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-3/ch-08-ai-is-not-a-vending-machine.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-08-ai-is-not-a-vending-machine-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-08-ai-is-not-a-vending-machine-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 11 complete

---

## 2026-03-25 - Sprint 10 Chapter 7 Drafted

Completed Part 2 Chapter 4, `Read the Manual, Then Make It Yours`, with the
full sprint artifact set:

- `chapters/briefs/ch-07-read-the-manual-then-make-it-yours-brief.md`
- `chapters/reviews/ch-07-read-the-manual-then-make-it-yours-review.md`
- `chapters/part-2/ch-07-read-the-manual-then-make-it-yours.md`

This chapter teaches the book's manual-first loop directly with one safe
Omarchy example: read the `Shell Tools` section, ask AI to explain the
difference between `ff`, `fd`, and `rg`, then try one small `ff` experiment and
observe what happens. The review pass tightened the beginner experience with a
safer browser-launch fallback, an exact `cd ~` setup step, plainer `ff`
language, and a stronger bridge into Part 3's AI chapters.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-2/ch-07-read-the-manual-then-make-it-yours.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-07-read-the-manual-then-make-it-yours-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-07-read-the-manual-then-make-it-yours-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 10 complete

---

## 2026-03-25 - Sprint 9 Chapter 6 Drafted

Completed Part 2 Chapter 3, `The Terminal Is Not a Wall`, with the full sprint
artifact set:

- `chapters/briefs/ch-06-the-terminal-is-not-a-wall-brief.md`
- `chapters/reviews/ch-06-the-terminal-is-not-a-wall-review.md`
- `chapters/part-2/ch-06-the-terminal-is-not-a-wall.md`

This chapter is grounded in the Omarchy manual's `Terminal`, `Shell Tools`,
and `Shell Functions` sections. It keeps the command set deliberately small and
safe: open the terminal, ask where you are, see what is there, move on purpose,
and reuse a prior command without memorizing it. The review pass also tightened
the beginner experience by defining `Super`, adding a fallback open path,
explaining what the prompt looks like, and making the `Ctrl + R` interaction
fully followable.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-2/ch-06-the-terminal-is-not-a-wall.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-06-the-terminal-is-not-a-wall-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-06-the-terminal-is-not-a-wall-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 9 complete

---

## 2026-03-25 - Sprint 8 Chapter 5 Drafted

Completed Part 2 Chapter 2, `Move Through It`, with the full sprint artifact
set:

- `chapters/briefs/ch-05-move-through-it-brief.md`
- `chapters/reviews/ch-05-move-through-it-review.md`
- `chapters/part-2/ch-05-move-through-it.md`

This chapter is grounded in the Omarchy manual's `Navigation`,
`Unified clipboard`, and `Hotkeys` sections. It teaches a small set of
confidence-building patterns instead of turning the chapter into a giant hotkey
list: workspace movement, close/fullscreen behavior, and the unified clipboard.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-2/ch-05-move-through-it.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-05-move-through-it-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-05-move-through-it-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 8 complete

---

## 2026-03-23 - Sprint 7 Chapter 4 Drafted

Completed Part 2 Chapter 1, `Meet the Machine`, with the full sprint artifact
set:

- `chapters/briefs/ch-04-meet-the-machine-brief.md`
- `chapters/reviews/ch-04-meet-the-machine-review.md`
- `chapters/part-2/ch-04-meet-the-machine.md`

This chapter is grounded in the Omarchy manual's `Welcome to Omarchy`,
`Navigation`, and `Hotkeys` sections. It teaches only the smallest useful set
of entry points: launcher, Omarchy menu, hotkey sheet, terminal, and browser.
That keeps the chapter usable and avoids turning the opening Part 2 chapter
into a system tour.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-2/ch-04-meet-the-machine.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-04-meet-the-machine-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-04-meet-the-machine-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 7 complete

---

## 2026-03-22 - Sprint 6 Chapter 3 Drafted

Completed Part 1 Chapter 3, `Learning Without Permission`, with the full sprint
artifact set:

- `chapters/briefs/ch-03-learning-without-permission-brief.md`
- `chapters/reviews/ch-03-learning-without-permission-review.md`
- `chapters/part-1/ch-03-learning-without-permission.md`

This chapter closes Part 1 by turning the reader's chosen door and leverage
list into one concrete mission with a why, success signal, and first move. That
gives Part 2 a clean handoff into teaching the machine in service of a live,
reader-owned goal.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-1/ch-03-learning-without-permission.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-03-learning-without-permission-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-03-learning-without-permission-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 6 complete

---

## 2026-03-22 - Sprint 5 Chapter 2 Drafted

Completed Part 1 Chapter 2, `What This Machine Really Gives You`, with the full
sprint artifact set:

- `chapters/briefs/ch-02-what-this-machine-gives-you-brief.md`
- `chapters/reviews/ch-02-what-this-machine-gives-you-review.md`
- `chapters/part-1/ch-02-what-this-machine-gives-you.md`

The chapter now reframes the machine as leverage instead of identity. It gives
the reader a practical exercise to turn their chosen door into a short
"this setup helps because it lets me..." list, which prepares the ground for
Chapter 3's focus on self-direction.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-1/ch-02-what-this-machine-gives-you.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-02-what-this-machine-gives-you-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-02-what-this-machine-gives-you-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 5 complete

---

## 2026-03-22 - Sprint 4 Chapter 1 Drafted

Completed Part 1 Chapter 1, `You're Not Stuck`, with the full sprint artifact
set:

- `chapters/briefs/ch-01-youre-not-stuck-brief.md`
- `chapters/reviews/ch-01-youre-not-stuck-review.md`
- `chapters/part-1/ch-01-youre-not-stuck.md`

The chapter now gives the reader a clear first move: stop treating "my whole
life" as the problem and pick one real door to move on. That keeps the promise
of the book practical and gives Chapter 2 a clean handoff into what the machine
actually gives the reader once they have a direction.

### How to Verify

1. Read `linux-ai-kickoff/chapters/part-1/ch-01-youre-not-stuck.md`
2. Read `linux-ai-kickoff/chapters/briefs/ch-01-youre-not-stuck-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/ch-01-youre-not-stuck-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 4 complete

---

## 2026-03-22 - Sprint 3 Introduction Drafted

Completed the introduction sprint with a full artifact set:

- `chapters/briefs/introduction-brief.md`
- `chapters/reviews/introduction-review.md`
- `chapters/introduction.md`

The introduction is now drafted at roughly 1,445 words and establishes:

- the reader-centered thesis of the book
- Linux and AI as tools rather than the true subject
- the line that the future belongs to humans who learn to use AI effectively
- the preview of the Team-Captain and Horse-Not-Car models
- the opening reader exercise around the doors they want to open

The draft was also checked against the local review roles and revised to keep
the tone grounded, dignified, and action-oriented.

### How to Verify

1. Read `linux-ai-kickoff/chapters/introduction.md`
2. Read `linux-ai-kickoff/chapters/briefs/introduction-brief.md`
3. Read `linux-ai-kickoff/chapters/reviews/introduction-review.md`
4. Confirm `linux-ai-kickoff/sprint-plan.md` marks Sprint 3 complete

---

## 2026-03-22 - Sprint 2 Skill Stack Created

Built the first local skill stack for Teach Yourself Anything under
`linux-ai-kickoff/skills/`.

This sprint added:

- `chapter-sprint.md`
- `manual-first.md`
- `ai-as-tutor.md`
- `mission-ladder.md`
- `possibility-framing.md`
- `lee-voice.md`

These skills turn the book's core ideas into a reusable workflow:

- manuals first, AI second
- AI as tutor instead of vending machine
- chapter missions with visible outcomes
- grounded possibility instead of hype
- a local chapter sprint loop that uses the custom agents in sequence

The local project docs now point to these skills as the active writing stack
for the book.

### How to Verify

1. Open the files in `linux-ai-kickoff/skills/`
2. Read `linux-ai-kickoff/skills/chapter-sprint.md`
3. Read `linux-ai-kickoff/AGENTS.md` and confirm the skills are listed there
4. Read `linux-ai-kickoff/project-plan.md` and confirm the skill stack is now active

---

## 2026-03-22 - Sprint 1 Architecture Locked

Completed the first real production sprint for the new book by creating
`linux-ai-kickoff/architecture.md` and locking the working manuscript
structure.

This sprint established:

- a 19-file manuscript shape
- exact working chapter slots across all five parts
- a purpose and visible outcome for every chapter
- the Part 4 "personal launchpad" project thread
- the placement of the core mental models
- the Omarchy-manual coverage map by chapter
- the review sequence to use during drafting

It also updated the local project docs so `AGENTS.md`, `project-plan.md`,
`context.md`, and `sprint-plan.md` all point to the new architecture as the
canonical chapter map.

### How to Verify

1. Read `linux-ai-kickoff/architecture.md`
2. Confirm it contains the chapter map, project thread, and manual coverage map
3. Read `linux-ai-kickoff/project-plan.md` and confirm it now references `architecture.md`
4. Read `linux-ai-kickoff/sprint-plan.md` and confirm Sprint 1 is marked done

---

## 2026-03-22 - Full Production Sprint Plan Added

Replaced the placeholder sprint plan with a full-book production runway in
`linux-ai-kickoff/sprint-plan.md`.

The new plan now covers:

- foundation and architecture
- skill-stack setup
- introduction
- all five parts of the book
- conclusion
- continuity pass
- technical/source accuracy pass
- copyedit
- manuscript assembly
- publication builds
- publication QA
- release readiness

The plan uses a concrete working manuscript shape so production is scoped all
the way through the end of the project instead of stopping at early drafting
milestones.

### How to Verify

1. Read `linux-ai-kickoff/sprint-plan.md`
2. Confirm it includes sprints through publication QA and release readiness
3. Confirm Sprint 0 now includes the full-book planning work

---

## 2026-03-22 - Foundation Workspace Created

Created the first real planning spine for the new book in
`linux-ai-kickoff/`. The concept now has a locked working title,
`Teach Yourself Anything`, a product definition, a project plan, a sprint plan,
a session context file, and a local operating guide.

Also reframed the book around the actual thesis:

- the future does not belong to AI
- it belongs to humans who learn to use AI effectively
- Linux and AI are tools, not the true subject
- the real subject is agency, self-direction, and confidence

Added four custom agents for the book's workflow:

- `pathfinder`
- `confidence-auditor`
- `manual-guide`
- `mission-designer`

The Omarchy manual is now explicitly named as the primary technical companion
source, which aligns with the goal of teaching the reader to read the manual
and use AI to interpret and apply it.

### How to Verify

1. Read `linux-ai-kickoff/product-definition.md`
2. Read `linux-ai-kickoff/project-plan.md`
3. Read `linux-ai-kickoff/context.md`
4. Read `linux-ai-kickoff/sprint-plan.md`
5. Open the files in `linux-ai-kickoff/agents/`
