# Chapter 6 Brief - The Terminal Is Not a Wall

## Mission

- Mission: Make the terminal feel usable and non-mystical by teaching a very
  small set of safe, repeatable terminal actions.
- Why it matters: If the terminal still feels like a hostile black box, the
  machine does not yet feel like leverage.
- Success looks like: The reader can open a terminal, tell where they are,
  see what is in front of them, move to a familiar place, and reuse a previous
  command without panic.
- Next door it opens: Chapter 7 can teach manual-first problem solving from a
  stronger base of terminal confidence.

## Purpose

This chapter needs to:

1. lower the emotional barrier around the terminal
2. teach purpose before commands
3. keep the command set small and safe
4. show that Omarchy already makes terminal work friendlier
5. point the reader back to the manual instead of pretending this chapter is
   the whole map

## Source Notes

Primary manual sections:

- `Terminal`
- `Shell Tools`
- `Shell Functions`

Technical anchors to ground:

- open terminal with `Super + Return`
- terminal choice lives under `Install > Terminal` in the Omarchy menu
- `ls` is backed by the richer `eza` tool in Omarchy
- `cd` is helped by Zoxide once the reader has visited a directory before
- `Ctrl + R` uses `fzf` to search command history
- Omarchy includes shell functions such as `compress` and `decompress`, which
  reinforce that the shell can be shaped around useful human tasks

Keep out of chapter:

- Tmux layouts and advanced session management
- terminal splits, tabs, and pane resizing
- remote port forwarding
- drive-formatting helpers and any risky system mutation
- full tours of `rg`, `fd`, or other tool manuals

## Working Outline

1. The terminal feels worse than it is
2. Open one terminal and explain what the prompt is
3. Teach the three core questions: where am I, what is here, how do I move
4. Show one memory-saving habit with command-history search
5. Reframe shell tools and shell functions as evidence that the terminal can be
   made friendlier
6. End with a short, safe terminal drill
