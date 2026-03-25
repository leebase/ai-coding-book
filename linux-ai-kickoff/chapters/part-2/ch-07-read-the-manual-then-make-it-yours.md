# Read the Manual, Then Make It Yours

A lot of people hear "read the manual" and think punishment.

School.

Homework.

Somebody telling you to go figure it out alone.

That is not what I mean.

I mean this:

if you want to stop guessing, stop starting from guesses.

The manual is not where you go because AI failed you.

The manual is where you go so AI has something real to stand on.

That is a very different relationship.

The habit we want is simple:

read the source first, use AI to clarify it, try one small thing, then look at
what happened.

That loop will take you a long way.

By the end of this chapter, you should be able to read one relevant section,
ask AI one grounded question about it, try one safe experiment, and know what
to do next from the result.

This chapter is where we make it real.

## Start With A Small Question

The mistake most people make is trying to use the manual to answer a giant
question.

"How do I learn Linux?"

"How do I become technical?"

"How does Omarchy work?"

Those are bigger than one manual section can answer well.

A manual is much better at helping with something smaller.

For example:

"How do I find files faster without clicking around?"

That is a good manual question.

It is narrow.

It is practical.

And it gives you a clear way to tell whether the answer helped.

So that is the one we are going to use.

## Put The Manual Next To The Machine

The Omarchy manual's `Navigation` section reminds us that the browser opens
with:

`Super + Shift + Return`

and the terminal opens with:

`Super + Return`

If `Super` is unfamiliar, it usually means the key that feels like the Windows
key on many keyboards.

Open both.

Put them side by side.

If the browser shortcut is different on your machine or you forget it, open the
launcher with `Super + Space`, start the browser from there, and keep going.

This matters more than it sounds like it should.

You want the source and the machine visible at the same time.

Read.

Try.

Observe.

That rhythm is the whole skill.

It is also one reason keyboard-first systems get so powerful once they click.

You can move between reading and doing without turning it into a production.

## Read The Right Section First

Now open the Omarchy manual's `Shell Tools` section.

Do not read the whole manual.

Do not skim six chapters.

Read the part that matches the problem you actually have.

In this case, you are looking for ways to find things faster.

That section gives you several candidates:

- `ff` for fuzzy finding files in the current tree
- `fd` for finding files by name
- `rg` for searching text inside files

That is already useful.

It is also already a small win.

You stopped guessing and narrowed the problem.

Notice what just happened.

You stopped asking the whole world for an answer.

You narrowed the question and found the official section that speaks to it.

That is not glamorous.

It is powerful.

## Ask AI To Translate, Not Replace

Now that you have the source section in front of you, this is a great place to
use AI.

Not to replace the manual.

To translate it.

Try a prompt like this in a browser chat or another AI interface you already
know how to open:

`I'm reading the Omarchy manual's Shell Tools section. Explain the difference between ff, fd, and rg in plain English for a beginner. I want to solve one problem: finding things faster on my machine. Tell me which one I should try first and what I should expect to see.`

That is a much better AI question than:

`How do I use Linux better?`

Why?

Because now the AI is working from a real source and a real problem.

It is not inventing a starting point for you.

It is helping you interpret one.

That is how you keep AI in the role of tutor instead of oracle.

And this is also where the Omarchy manual's `AI` section quietly teaches a
bigger lesson. Even when Omarchy gives you AI tools, the manual still tells you
how to start them and where to be careful. The source gives the guardrails. AI
helps you understand and apply them.

That pattern matters.

## Try One Safe Thing

For this chapter, use `ff`.

The manual says it gives you fuzzy finding of files in the current tree with a
preview on the right.

That makes it a good first experiment because it is useful and low-risk.

First, in the terminal, run:

`cd ~`

Your home directory is your personal top-level folder.

The current tree just means whatever files and folders are underneath the place
you are standing right now.

Then type:

`ff`

`ff` opens a searchable file picker.

You do not type a full command after that.

You just start typing partial letters and the list filters live.

Start typing a few letters from a file name you think might be in that tree.

Watch what happens.

You should see the list narrow as you type.

If your setup shows a preview area on the right, good.

If it looks a little different, that is okay too.

Success here is simpler: `ff` opened, responded to your typing, and gave you an
interactive result instead of a blank wall.

Practical note, not a manual quote: if you only wanted to explore, `Esc` or
`Ctrl + C` will usually back out.

If you see `ff: command not found`, stop and re-check that you are in the
Omarchy terminal and in the `Shell Tools` section you just read. That is not
failure. That is a signal to verify your environment before guessing.

That is enough.

You do not need to master the tool today.

You just needed to prove that the loop works:

1. find the official section
2. ask AI to explain it in your language
3. try one small thing
4. observe what happened

That is the win.

## Make It Yours By Matching The Tool To The Question

Once you have seen `ff` once, the rest of the section makes more sense.

Now you can personalize the tool choice a little:

- if you only remember part of a file name and want to hunt visually, use `ff`
- if you want to search by file name more directly, look at `fd`
- if you want to search for words inside files, look at `rg`

This is what I mean by "make it yours."

Not endless customization.

Not tweaking colors for three hours.

Choosing the right tool for the problem in front of you.

That is a much deeper form of ownership.

## The Loop Scales Up

Today you used the loop on one small shell-tools question.

Later, you can use the same pattern on bigger things.

The Omarchy manual's `Development Tools` section is full of examples you do not
need yet but probably will later:

- choosing an editor under `Install > Editor`
- understanding how Omarchy manages programming environments
- using `gh auth login` when you need GitHub CLI

You do not need to do those things now.

You just need to see that the method scales.

Small tool today.

Bigger system choice later.

Same loop.

That matters because a lot of confidence comes from realizing you do not need a
different personality to tackle bigger problems.

You need the same habit applied to bigger questions.

## Read, Ask, Try, Observe

That is the pattern.

Read the source.

Ask AI to explain what is unclear.

Try one safe thing.

Observe what happened.

Then decide what to do next.

That is how you stop treating the machine like a mystery.

That is how you stop treating AI like magic.

And that is how reading the manual turns from something somebody assigned you
into something that gives you power.

Do one more tiny round before you leave this chapter.

Pick either `fd` or `rg` from the same `Shell Tools` section and ask AI one
clean question about it.

Not ten questions.

One.

Then try one small version of the answer.

That is enough.

Part 3 is where we are going to talk about AI more directly.

But now you have already seen the important part:

AI works better when it is standing on something real.

Next we will get more deliberate about how to ask AI for explanation,
comparison, and caution while keeping the human in charge.
