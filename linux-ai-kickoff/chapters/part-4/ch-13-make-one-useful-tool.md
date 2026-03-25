# Make One Useful Tool

This is where the machine starts giving something back.

Not in a dramatic way.

Not with a startup.

Not with a giant automation system.

Just with one little piece of leverage.

That matters because a useful tool changes the feeling of work.

Instead of starting from scratch every time, you start with help you built.

That is a real shift.

By the end of this chapter, you should have one tiny helper script you can run
to get back into your launchpad and see your mission again.

## Why One Tiny Tool Matters

People hear "build a tool" and imagine something way too big.

A product.

An app.

A giant script with a logo and a README.

Forget all that.

For this chapter, a tool can be tiny.

If it removes one repeated annoyance, it counts.

If it helps you get back to the work faster, it counts.

If you actually use it again tomorrow, it definitely counts.

That is the bar.

## Keep The Same Launchpad

Do not start over in a new folder.

Stay in the same launchpad from Chapter 12.

Stay with the same goal folder.

Stay with the same `mission.md`.

That is important.

We are not collecting demos.

We are building a place that gets more useful each time you touch it.

## Read First, Then Decide

Do this chapter in the same order again:

1. read the `Shell Tools`, `Shell Functions`, and `Development Tools` sections
   of [The Omarchy Manual](https://learn.omacom.io/2/the-omarchy-manual)
2. ask AI to help you choose the smallest helpful move
3. build and test only that move

Keep the manual open while you work.

Those sections matter for different reasons.

`Shell Tools` reminds you that the shell can be improved in small ways.

`Shell Functions` shows that little command helpers are normal.

`Development Tools` is a reminder that real tools become more useful when they
live close to the work they support.

For this chapter, one clean first choice is a short helper script instead of a
permanent alias.

Why?

Because a short script gives you something real to keep without editing shell
startup files yet.

That keeps the win small.

## Ask AI For The Smallest Helpful Script

Now use AI like a coach and collaborator.

Try:

`Be a practical shell teacher. I have a launchpad folder at ~/launchpad and one goal folder inside it with a mission.md note. Help me write the smallest script I can source in my current shell so it takes me back into that goal folder and prints mission.md. Keep it simple and explain each line.`

That is a good ask.

It is specific.

It is grounded in a real folder.

And it asks for explanation, not just output.

You are still the one deciding whether the script makes sense.

## Build The Script

Use the same launchpad from Chapter 12.

Go to `~/launchpad` in the terminal.

Then create a file named `start-goal.sh`.

If you want a simple path, use your editor to create the file in `~/launchpad`.

If you want to stay in the terminal, you can run:

```bash
cd ~/launchpad
touch start-goal.sh
ls
```

If `ls` shows `start-goal.sh`, the file is there.

If you are not sure what your real goal folder is called, run `ls ~/launchpad`
and look for the folder you made in Chapter 12.

Now open `start-goal.sh`, paste in a small version like this, and save the
file. This file is meant to be sourced into your current shell, not run with
`bash`. Replace `your-folder-name` with your real goal folder:

```bash
cd ~/launchpad/your-folder-name || return 1
echo "Mission:"
cat mission.md
```

If you do not already have an editor open, use the application launcher
(`Super + Space`), open the editor you have on this machine, and open
`start-goal.sh` there.

You do not need to understand every detail on the first pass.

You do need to understand the shape:

- go to the goal folder
- print a label
- show the mission note

If any line feels fuzzy, stop and ask AI to explain that exact line in plain
English before you run anything else.

That is part of the method.

## Run It

Now test the helper.

Because this helper needs to change the folder of your current terminal, you
should `source` it instead of running it with `bash`.

In plain English: `source` runs the file inside your current shell, so the `cd`
line actually moves you where you want to go.

The smallest safe way is:

```bash
source ~/launchpad/start-goal.sh
```

Run that in the terminal, not in the AI chat.

If it works, you should see:

- the word `Mission:`
- the contents of your `mission.md` file
- and your terminal should now be sitting in that goal folder

That is your tool working.

It may be tiny.

It still counts.

It is also proof that you can make your machine remember useful things for you.

## If It Does Not Work

This chapter is not broken if the first run fails.

This chapter gets more real if the first run fails.

That is because now you have something concrete to fix.

Do not guess.

Re-check the relevant part of the manual.

Then bring the exact script line and exact terminal output back to AI.

Try:

`Be a patient shell teacher. I ran source ~/launchpad/start-goal.sh and got this output: [exact output]. Help me find the next smallest fix and explain why it failed.`

If you want a concrete example, an error like `cd: no such file or directory`
usually means the folder name in the script does not match the real folder yet.

And an error like `mission.md: No such file or directory` usually means you are
in the wrong folder or the mission note is missing there.

That is the same ask-refine-test-repeat loop from Chapter 11 on a real artifact
you care about.

## Why This Counts As Leverage

This helper is small.

Good.

Small is why you are likely to keep it.

And if you use it more than once, that means your machine is already paying you
back.

Not because it became magical.

Because you removed one little bit of friction.

That is how useful systems begin.

## Use It Tomorrow Too

Do not let this become a one-time exercise.

Tomorrow, run the helper again.

See your mission note.

Drop back into the work.

That is what makes it real.

A tool is not impressive because it is complicated.

A tool is impressive because it keeps helping.

## Do It Now

In the same `~/launchpad` from Chapter 12:

1. create `start-goal.sh`
2. point it at your real goal folder
3. make it print `mission.md`
4. run it with `source ~/launchpad/start-goal.sh`

If you see your mission note come back in the terminal, you did the work of
this chapter.

And now you have your first real helper.

## What This Opens

Once you have a real workspace and one real helper, the next thing that happens
is usually friction.

Something breaks.

Something points to the wrong place.

Something behaves differently than you expected.

Good.

That is where the next chapter begins.

We are going to fix one real break instead of pretending that useful work stays
neat.
