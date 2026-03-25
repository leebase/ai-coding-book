# Fix What Breaks

This is the part people usually try to avoid.

Something breaks.

The command does not work.

The path is wrong.

The file is not where you thought it was.

And right there, a lot of people start telling themselves the wrong story.

Do not believe that story.

This is not the moment where your talent gets revealed.

This is the moment where the work gets real.

If you are building anything useful, something will break.

Good.

That means you finally have something real enough to fix.

By the end of this chapter, you should have repaired one real break in your
launchpad helper and watched it work again.

## Breakage Is Part Of The Work

Useful work is not clean all the way through.

That is not a personal failure.

That is reality.

You make a folder.

You write a note.

You build a helper.

Then one line points to the wrong place and the whole thing stops feeling smart.

That is normal.

The skill is not avoiding every break forever.

The skill is learning how to come back from one without panic.

## Start With The Error You Actually Have

Use the same `start-goal.sh` from Chapter 13.

If your helper is already broken in real life, use that real error.

If your helper works fine right now, create one safe teaching break for this
chapter: open `start-goal.sh`, change one piece of the goal-folder name so it
is slightly wrong, save it, and then run the helper. The `python-auto` example
below is one intentional broken example, not a claim that Chapter 13 gave you a
bad script.

Now imagine you run:

```bash
source ~/launchpad/start-goal.sh
```

and the terminal says:

```text
cd: no such file or directory: /home/yourname/launchpad/python-auto
```

That is a very good teaching moment.

Not because it feels good.

Because the error is giving you a clue.

Read it literally.

The shell is not saying:

- you are bad at this
- Linux hates you
- the whole project is doomed

It is saying:

I tried to go to this folder, and that folder is not there.

That is much more workable.

## Read First, Then Inspect

Do this chapter the same way you have done the others:

1. use the `Terminal`, `Shell Tools`, and `Shell Functions` sections of [The Omarchy Manual](https://learn.omacom.io/2/the-omarchy-manual)
   as lookup help while you troubleshoot
2. ask AI to help you interpret the error in plain English
3. inspect what is actually on disk before you edit anything

Keep the manual open while you work.

The manual reminds you what `cd`, `pwd`, and `ls` are doing.

That matters when you are under a little pressure.

Pressure makes people guess.

The manual helps you slow down.

## Look At Reality

Before you change the script, look at the real folders.

Run:

```bash
cd ~/launchpad
ls
```

You might see something like:

```text
python-automation
start-goal.sh
```

Now you know something useful.

The script was trying to go to `python-auto`.

The real folder is `python-automation`.

That is not a mystery anymore.

That is one wrong line.

## Ask AI The Right Question

Now that you have real evidence, use AI well.

Try:

`Be a patient shell teacher. My helper script says cd ~/launchpad/python-auto, but ls shows the real folder is python-automation. What is the smallest fix? Explain it in plain English.`

That is a strong question because it includes:

- the exact broken line
- the exact real evidence
- the exact kind of help you want

That is a much better move than:

`My script is broken.`

## Fix One Line

Open `start-goal.sh`.

If you do not already have it open, use the same editor path from Chapter 13:
open your editor, open `~/launchpad/start-goal.sh`, and change just the broken
line.

Find the line that says:

```bash
cd ~/launchpad/python-auto || return 1
```

Change it to:

```bash
cd ~/launchpad/python-automation || return 1
```

Save the file.

That is the fix.

Not a rewrite.

Not a grand theory.

One corrected line.

If your own folder has a different name, use your real folder name instead.

## Test It Again

Now re-run the helper:

```bash
source ~/launchpad/start-goal.sh
```

If it works, you should see:

- your helper run without the folder error
- your mission note show up
- your terminal sitting in the correct goal folder

That matters.

Because now you have seen the whole cycle:

- something broke
- you read the error
- you checked reality
- you fixed one thing
- you tested again

That is real troubleshooting.

And it is proof that you can come back from a break without losing the thread.

## If The Error Is Different

Maybe your error is not a wrong folder name.

Maybe it says:

```text
mission.md: No such file or directory
```

That is still workable.

Now the question becomes:

- are you in the wrong folder?
- is `mission.md` missing?
- did you name it something slightly different?

Two good inspection commands here are:

```bash
pwd
ls
```

Same posture.

Read the error.

Check the real files.

Bring the exact evidence back to AI.

Fix one thing.

Test again.

The pattern is the same even when the details change.

## What Recovery Really Builds

Fixing one break does more than repair one tool.

It changes your relationship to problems.

You stop treating friction like a verdict.

You start treating it like information.

That is a serious upgrade.

Because now you can stay in the work longer.

And staying in the work longer is how real capability gets built.

## Do It Now

Use your real `start-goal.sh`.

If it already has a real break, use that.

If it does not, make one small safe break by changing the goal-folder name, run
the helper once, then fix it back.

Then:

1. read the error literally
2. check the real folders or files
3. ask AI with the exact evidence
4. fix one line or one file
5. test again

If your helper works again after the fix, you did the work of this chapter.

And now you have something better than a clean run.

You have recovery skill.

That is part of how you become somebody who can keep building without panic.

## What This Opens

Now your launchpad is not just real.

It is durable.

You made a place.

You made a helper.

You fixed a break.

The next step in this part is to use all of that to ship one small win you
actually keep.
