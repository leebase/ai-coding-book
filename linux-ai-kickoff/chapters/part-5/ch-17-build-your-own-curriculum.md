# Build Your Own Curriculum

The word curriculum can make this sound more serious than it is.

Forget the school version.

You do not need a program.

You need a short path you can follow.

You do not need semesters.

You do not need a giant reading list.

You do not need a five-year plan.

You need a simple way to keep learning on purpose.

That is all this chapter is.

In Chapter 16, you wrote a `direction.md` note.

That note answered:

what kind of work do I want more of?

Now we are going to answer the next question:

what should I do next so that direction becomes real?

By the end of this chapter, you should have one small `curriculum.md` file in
the same launchpad goal folder with a few missions, a few docs, and a few
tools you can keep using.

## A Curriculum Is Just A Path You Can Follow

A good self-built curriculum is not a performance.

It is not there to impress anybody.

It is there to help you avoid waking up tomorrow and thinking:

I care about this, but I do not know what to do next.

That is what a curriculum solves.

It turns interest into sequence.

Not forever.

Just enough to keep moving.

## Start With The Direction You Already Chose

Do not build this from scratch.

Open the `direction.md` note from Chapter 16.

Read the sentence you wrote.

That sentence is the center of the curriculum.

If your direction was automation, the curriculum should help you automate more.

If your direction was writing and communication, the curriculum should help you
write, explain, and publish more.

If your direction was troubleshooting, the curriculum should put you in front
of more real problems to solve.

If your direction was a topic outside tech, the curriculum should use Linux and
AI in service of that topic.

The direction decides the shape.

Not the other way around.

## Keep It Small Enough To Use

Most people make two mistakes here.

The first mistake is making the plan too big.

The second mistake is making it too vague.

Too big sounds like:

`Learn Python.`

Too vague sounds like:

`Get better at this.`

What you want is smaller and more concrete.

More like:

`Write three tiny Python helpers that solve real annoyances.`

`Read the official docs for one tool and use one part of them on purpose.`

`Publish three short explanations of something I am learning.`

That is a real curriculum shape.

Small enough to act on.

Clear enough to follow.

## The Three-Part Shape

For this book, I want you to build your curriculum from three kinds of things:

1. missions
2. docs
3. tools

Three buckets are plenty.

Here is the plain-English version:

- a mission is something you do
- a doc is something you read, check, or keep nearby
- a tool is something you use repeatedly while doing the work

For your first version, keep it to:

- 3 missions
- about 2 docs you will keep reusing
- about 2 tools you will keep reusing

That is enough to begin.

You can revise it after you actually use it.

Those docs and tools can repeat across the three missions.

### Missions

Missions are the real work.

They are where confidence gets built.

Pick three missions that fit your direction and grow a little in difficulty.

Not ten.

Three.

That is enough to create momentum.

Good missions are:

- small enough to finish
- real enough to matter
- specific enough that you know when you are done

### Docs

Docs are how you stop depending on random summaries.

Pick two primary sources that belong to the direction you chose.

That might be:

- an official manual
- official documentation
- a well-maintained reference guide
- a README you keep coming back to
- a note you wrote because it contains the truth you keep needing

At least one of the two should be a real manual or official doc.

The second can be a README or a note you keep because it captures something you
already proved.

If your direction is still close to Linux, one of those might be the Omarchy
manual again.

If your direction is Python, it might be the official Python docs.

If your direction is writing on the web, it might be the official docs for the
tool you use to publish.

The point is the same:

learn where truth lives.

Then use AI to help you understand and apply it.

### Tools

Tools are the things you will keep touching while you learn.

Pick two.

Not every tool you might someday use.

Just two tools worth getting more comfortable with right now.

One might be the machine itself.

One might be a language, editor, note system, shell tool, or publishing tool.

Your tool list should support the missions.

If it does not support the missions, it is probably just a distraction.

As you build the list, keep one simple rule:

each mission should point to the doc that supports it, the tool that helps you
do it, and what done looks like when you finish.

## Use AI Like A Coach, Not A Scheduler

AI can help here.

But this is another place where you stay in charge.

Do not ask it to design your destiny.

Ask it to help you turn one direction into a workable next stretch.

Try:

`Be a practical learning coach. I have chosen this direction: [paste your direction note]. Help me build a small curriculum for the next few weeks. Give me three missions that get a little harder, two primary docs or manuals worth reading, and two tools worth practicing. Keep it practical and small.`

Then give it:

- what you have already built
- what kind of work felt alive
- what kind of work felt draining
- how much time you realistically have

That last one matters.

A curriculum that ignores your real life is not a good curriculum.

If the AI gives you something bloated, tell it to shrink it.

If it gives you something vague, tell it to make the missions concrete.

If it gives you a giant reading list, cut it down.

You are not trying to build the perfect plan.

You are trying to build one you will actually use.

## Write `curriculum.md`

Now create one more file in the same launchpad goal folder:

`curriculum.md`

Keep it simple.

The easiest way to do that is to make each mission carry its own support.

Use this shape:

```md
# Curriculum

## Direction
[paste your sentence from direction.md]

## Missions
1. [small real mission]
   - Doc: [manual, official doc, README, or note]
   - Tool: [tool]
   - Done looks like: [file, helper, fix, note, or published piece]
2. [slightly harder mission]
   - Doc: [manual, official doc, README, or note]
   - Tool: [tool]
   - Done looks like: [file, helper, fix, note, or published piece]
3. [small stretch mission]
   - Doc: [manual, official doc, README, or note]
   - Tool: [tool]
   - Done looks like: [file, helper, fix, note, or published piece]

## Start Here
[the first mission you will do next]
```

You do not need more structure than that.

A small curriculum you use is worth much more than a brilliant one you never
touch.

## One Worked Example

Start with a real direction note:

`A direction worth exploring next is automation, because building one tiny helper made my machine feel useful instead of passive.`

That can become a curriculum like this:

```md
# Curriculum

## Direction
A direction worth exploring next is automation, because building one tiny
helper made my machine feel useful instead of passive.

## Missions
1. Write one helper that creates a new notes file with today's date.
   - Doc: Omarchy manual section on shell tools
   - Tool: shell
   - Done looks like: one working helper file I can run again tomorrow
2. Write one helper that opens my launchpad folder and prints direction.md.
   - Doc: the man page for one command I keep reaching for
   - Tool: shell
   - Done looks like: one helper that saves me a real repeated step
3. Write one helper that chains two repeated actions I keep doing by hand.
   - Doc: the official docs for the command or shell feature I need
   - Tool: AI chat for explanation and iteration
   - Done looks like: one helper I actually keep because it saves time

## Start Here
Write the notes-file helper first.
```

Notice what happened there.

The curriculum did not try to solve a whole life.

It just turned one real signal into one short runway.

## A Few Quick Examples

If your direction is automation, your curriculum might look like this:

- Mission 1: make one helper for renaming files
  Doc: the `mv` or `find` man page
  Tool: shell
  Done looks like: a helper you run on a real folder
- Mission 2: make one helper for starting a repeated task
  Doc: Omarchy manual section on shell tools
  Tool: shell
  Done looks like: one command you stop typing by hand
- Mission 3: make one helper that chains two useful actions together
  Doc: the official docs for the shell feature you need
  Tool: AI chat as coach
  Done looks like: one kept helper that saves time

If your direction is writing and communication, your curriculum might look like
this:

- Mission 1: write one clear explanation of something you learned
  Doc: the Markdown reference or style guide you keep checking
  Tool: note system
  Done looks like: one note you would let another person read
- Mission 2: turn one explanation into a small post or page
  Doc: the official docs for the publishing tool you use
  Tool: publishing tool
  Done looks like: one page or post that exists outside your head
- Mission 3: collect three explanations into a small guide
  Doc: the docs for the editor or publishing system you picked
  Tool: note system
  Done looks like: one small guide with three sections

If your direction is troubleshooting, your curriculum might look like this:

- Mission 1: fix one repeatable small break on purpose
  Doc: the manual page for the command or tool that broke
  Tool: terminal
  Done looks like: the fix works twice in a row
- Mission 2: trace one error carefully from message to cause
  Doc: the official docs for the tool you are debugging
  Tool: AI chat for explanation and debugging
  Done looks like: one cause-and-fix note written in plain English
- Mission 3: write one short recovery note you could reuse
  Doc: your own proven note plus the original official source
  Tool: note system
  Done looks like: one saved recovery note you would trust later

If your direction is outside tech, your curriculum can still work the same way.

Say your direction is learning local history well enough to publish a small
guide for your town.

- Mission 1: collect and summarize three local sources into one note
  Doc: the archive, library, or project guide for the sources you are using
  Tool: note system
  Done looks like: one clear note with three usable source summaries
- Mission 2: write one short profile of a place or person
  Doc: your saved source note plus the style guide you are using
  Tool: AI chat for comparison and outlining help
  Done looks like: one short profile you could show another person
- Mission 3: turn three short profiles into one small guide or page
  Doc: the official docs for the writing or publishing tool you picked
  Tool: publishing tool
  Done looks like: one small guide or page you keep or publish

Notice what these examples have in common.

They are not giant.

They do not try to make you "job-ready" by next month.

They give you a runway.

That gives you room to move.

## Let The Curriculum Change

Your first self-built curriculum will not be perfect.

Good.

That means you are using it.

After Mission 1, you may learn that one doc matters much more than another.

After Mission 2, you may realize one tool is central and one is noise.

After Mission 3, you may even realize the direction needs to change a little.

That is not failure.

That is learning.

A self-built curriculum is alive.

You adjust it as reality teaches you.

## Do It Now

Open your launchpad goal folder.

Find `direction.md`.

Create `curriculum.md`.

Then fill in:

- three missions
- one doc, one tool, and one done signal for each mission
- one first move

If you keep it small, real, and tied to your actual direction, you did the
work of this chapter.

Then do one more thing:

start Mission 1 within the next day if you can, or schedule it now.

The curriculum matters most once it turns into motion.

## What This Opens

A direction is good.

A usable path is better.

In the next chapter, we are going to make that even more direct by talking
about how to keep moving without waiting for permission from a class, a boss,
or this book.
