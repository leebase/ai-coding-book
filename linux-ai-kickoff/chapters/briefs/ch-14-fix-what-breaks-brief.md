# Chapter 14 Brief - Fix What Breaks

## Mission

- Mission: Teach recovery and troubleshooting through one real break inside the
  launchpad helper from Chapter 13.
- Why it matters: The reader now has a real workspace and a real helper. The
  next honest thing is friction. This chapter should teach that fixing one small
  break is part of the work, not evidence that they are failing.
- Success looks like: The reader identifies one real break, verifies what is
  actually wrong, fixes it, and re-runs the helper successfully.
- Next door it opens: Chapter 15 can finish Part 4 with a small working system
  that feels earned instead of lucky.

## Purpose

This chapter needs to:

1. make troubleshooting feel normal and non-dramatic
2. keep the break small, real, and recoverable
3. use the manual-first + AI-second loop under pressure
4. show the reader how to look at evidence instead of guessing
5. end with a repaired artifact they keep using

## Working Example Set

Primary break:

- `start-goal.sh` points to the wrong goal folder name
- terminal shows `cd: no such file or directory`

Core recovery moves:

1. read the error literally
2. inspect the real files/folders
3. correct one line
4. re-test

Keep out of chapter:

- catastrophic failures
- package installation problems
- abstract debugging theory
- multiple unrelated breakages
- turning the chapter into a general Bash manual

## Working Outline

1. Why breakage is part of real work
2. Read the error, do not dramatize it
3. Re-check the manual and inspect the real folder
4. Fix one line in `start-goal.sh`
5. Re-run the helper and close on competence
