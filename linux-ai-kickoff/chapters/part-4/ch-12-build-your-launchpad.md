# Build Your Launchpad

Up to this point, a lot of the work in this book has been training.

Important training.

Useful training.

But still training.

Now we start keeping things.

That shift matters.

Confidence grows faster when the work leaves evidence behind.

Not just better thoughts.

A real folder.

A real note.

A real place on your machine where your direction starts taking shape.

That is what this chapter is for.

By the end of it, you should have one launchpad folder for one real goal, plus
one plain-language mission note inside it.

## Why A Launchpad Matters

Most people who want to change their life keep everything in their head.

A half-plan.

A vague intention.

A bunch of tabs.

A burst of motivation that disappears by Thursday.

That is not a system.

It is a fog.

A launchpad is just a place where one real direction gets a home.

Not your whole future.

Not every possible interest.

Just one direction you care enough about to give a folder, a note, and a next
step.

That is a small move.

It is also a serious move.

Because now the idea has somewhere to live.

## Pick One Goal Worth Giving A Home

Do not pick five.

Pick one.

Something real enough that you would like your machine to help you move on it.

If the `starter note` from Part 1 still feels true, use that same door here.

You are giving it a home now, not starting your life over.

Examples:

- build a tiny portfolio site
- organize your freelance admin better
- learn enough Python to automate one annoying task
- start a notes system for a topic you actually care about

This is not the moment to choose your forever identity.

This is the moment to choose one direction worth giving a home.

If you still feel fuzzy, use AI like a coach, not like a decider.

Try:

`Be a practical project coach. I want to pick one goal to build a small launchpad for. Help me choose something small, real, and worth keeping. Ask me two questions, then help me name one direction.`

That is a good use of AI.

Not "tell me who to become."

Just "help me narrow this into one real thing."

## Shrink It Into A Folder And A Mission

Once you have the direction, shrink it.

You need two things:

1. a short folder name
2. a plain-language mission sentence

If your goal is too big, ask AI to compress it.

Try:

`Be a practical project coach. My direction is: [your real goal]. Help me turn that into a short folder name and a one-sentence mission I can actually work from. Keep it plain and small.`

Examples:

- direction: `learn Python well enough to automate one repeated task`
- folder name: `python-automation`
- mission sentence: `Use this space to learn just enough Python to automate one annoying repeated task on my computer.`

- direction: `start a portfolio site for my work`
- folder name: `portfolio-site`
- mission sentence: `Use this space to build and ship a simple site that shows my work clearly.`

That is enough.

You do not need a ten-page plan.

You need a place and a sentence.

## Build The Launchpad

Now make it real.

Do this chapter the book's way:

1. read the `Terminal` and `Shell Tools` sections of [The Omarchy Manual](https://learn.omacom.io/2/the-omarchy-manual)
2. ask AI to clarify anything about `mkdir`, `cd`, or `pwd` that still
   feels fuzzy
3. then run the smallest real steps

Keep the manual open while you do the exercise.

Open your terminal.

Then create your launchpad folder and your goal folder inside it:

```bash
mkdir -p ~/launchpad
cd ~/launchpad
mkdir your-folder-name
cd your-folder-name
pwd
touch mission.md
ls
```

Run those in the terminal, not in the AI chat.

Replace `your-folder-name` with the short name you picked.

If `pwd` ends with `/launchpad/your-folder-name`, you are in the right place.

You will probably see a full path like
`/home/yourname/launchpad/your-folder-name`.

That is your first kept artifact.

If `~/launchpad` already exists, that is fine. `mkdir -p` will leave it alone.

If something does not work, do not guess.

Use the Chapter 11 loop:

- ask what to do
- refine anything you do not understand
- test the smallest real step
- repeat using the exact result

For example:

`Be a patient Linux teacher. I already made ~/launchpad, but I am not sure whether I am inside the right folder yet. Help me verify it in the smallest possible way.`

That is the loop on something real, not just a classroom drill.

If the terminal shows an error, re-check the relevant part of the manual first,
then paste the exact command and exact error back into AI and ask for the next
smallest fix.

## Add A Mission Note

Now give the folder a purpose.

If you ran the commands above, the `touch mission.md` line already created the
file.

Now open `mission.md` in whatever editor you already have available.

If you do not already have an editor open, use the application launcher
(`Super + Space`) and open the editor you have on this machine, then open
`mission.md` there. If you need the launcher shortcut again, check the
`Navigation` and `Hotkeys` sections of [The Omarchy Manual](https://learn.omacom.io/2/the-omarchy-manual).

Do not turn this into an editor debate.

The point is the note, not the tool.

Make the first line your actual mission sentence.

Then, if it helps, add two more short lines:

1. why it matters
2. the next smallest step

The mission sentence is the required part.

The other two lines are there to help you keep momentum.

Here is a simple example:

```md
Use this space to learn enough Python to automate one annoying repeated task.
Why it matters: I want to stop wasting time on boring repeat work.
The next smallest step: Pick one task and describe exactly how I do it now.
```

If you run `ls` in the folder and see `mission.md`, the file is there and real.

That is enough to start.

It does not need to look impressive.

It needs to be real.

## Keep It Small Enough To Keep

This chapter works only if the launchpad stays small enough to keep alive.

Do not build a life operating system tonight.

Do not create twelve folders and a productivity religion.

Do not confuse complexity with seriousness.

The serious move is this:

you picked one direction, gave it a home, and wrote down what it is for.

That is how real projects begin.

With a place to start.

## Do It Now

Pick one real goal.

Shrink it into a folder name and one mission sentence.

Create:

- `~/launchpad`
- one goal folder inside it
- one `mission.md` note

Then check two things:

1. does the folder exist in the place you expect?
2. does the mission note say what this space is for in plain English?

If yes, you did the work of this chapter.

And now your machine contains evidence that you are no longer just thinking
about changing something.

You started.

## What This Opens

Now you have somewhere real to work.

That changes the feeling of everything that comes next.

In the next chapter, we are going to stay in this same launchpad, keep the same
goal folder and `mission.md`, and make the setup more useful by adding a small
alias or helper you actually use.

That is where the machine starts paying you back for the effort you put into
it.
