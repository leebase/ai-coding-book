# Pick the Right Hero

Once you stop treating AI like a vending machine, the next question is:

what kind of helper do you actually need right now?

Last chapter, you chose the kind of help.

Now you are choosing the kind of helper.

That matters more than people think.

Because "the AI" is too vague.

Sometimes you need a patient teacher.

Sometimes you need a coach.

Sometimes you need a careful explainer.

Sometimes you need somebody to compare options.

If you ask the same machine for all of those things in the same blurry way, you
will get blurry help back.

This is where the Team-Captain model comes in.

You are not standing in front of one magic robot.

You are assembling the right helper for the job.

Here, `hero` just means the helper role you want the AI to play for this task.

By the end of this chapter, you should have one reusable Team-Captain prompt for
a real task you care about.

## Same Machine, Different Heroes

Imagine you are stuck on a small Linux question.

You saw `cd ~` in the terminal and you do not understand what it means.

If you ask:

`Help me with Linux`

you might get anything.

A history lesson.

A giant overview.

A list of commands.

Something too broad to be useful.

But if you ask for the right kind of helper, the answer shape changes.

Try this:

`Be a patient Linux teacher. I'm new to the terminal. Explain what cd ~ means in plain English and give me one example.`

That is already much better.

Not because you found a magic sentence.

Because you picked the right hero.

You asked for a teacher, not a generic machine.

And `cd ~` is a good beginner-sized mission because it is small, specific, and
easy to judge.

## The Team-Captain Model

This is the model:

1. Pick the right hero
2. Give them the backstory
3. Give them a specific mission
4. Stay in charge

That is it.

It is simple.

It is also a lot more powerful than just saying "help me."

A Team-Captain prompt is one short prompt with four parts: role, backstory,
mission, and steering.

Think of it like assembling the right person for the moment.

Not forever.

Just for this task.

## 1. Pick The Right Hero

Start with the role.

Not "AI, do something."

What kind of helper would actually help here?

Examples:

- `Be a patient Linux teacher`
- `Be a practical project coach`
- `Be a careful explainer`
- `Be a tough-but-clear editor`

The role matters because it changes the shape of the answer.

A teacher explains.

A coach helps you move.

An editor tightens.

An explainer translates.

When the role is wrong, the answer often feels wrong even if the facts are not.

## 2. Give The Backstory

Now tell the helper what world they are walking into.

What are you doing?

What do you already know?

What did you already try?

What machine or project are you in?

This does not need to be long.

It just needs to be real.

Examples:

- `I'm new to the terminal and I just saw cd ~ in a command.`
- `I'm trying to build one useful tool, not a full app.`
- `I already read the manual section, but I still don't get the difference.`

Backstory reduces guessing.

That is the point.

## 3. Give A Specific Mission

Now assign the actual task.

This is where many people stay too vague.

Do not say:

`Teach me Linux`

Say something like:

- `Explain what cd ~ means in plain English.`
- `Compare these two options and tell me the tradeoff.`
- `Give me the next smallest step I can do today.`
- `Quiz me once so I know I actually understand it.`

The mission should be small enough to finish.

That keeps the interaction useful and keeps you moving.

## 4. Stay In Charge

This is the part many people forget under pressure.

You are still the captain.

If the answer is too broad, say so.

If it is too technical, ask for simpler language.

If it gives five steps and you only want one, push it back down.

If it missed your point, redirect it.

That is not being rude.

That is using the tool correctly.

The role, the backstory, and the mission all matter.

But they only really work if somebody is still steering.

That somebody is you.

## Build It Step By Step

Start weak:

`Help me learn Linux`

Now build it up.

Step 1, pick the hero:

`Be a patient Linux teacher.`

Step 2, add the backstory:

`Be a patient Linux teacher. I'm new to the terminal and I just saw cd ~.`

Step 3, add the mission:

`Be a patient Linux teacher. I'm new to the terminal and I just saw cd ~. Explain what it means in plain English and give me one example.`

Step 4, add the steering:

`Be a patient Linux teacher. I'm new to the terminal and I just saw cd ~. Explain what it means in plain English and give me one example. If your answer gets too technical, simplify it.`

That is the full prompt.

Same machine.

Much better direction.

The exact wording is not magic.

Clear role, context, mission, and steering are what make this work.

## Watch A Weak Prompt Turn Into A Directed One

Weak:

`Help me learn Linux`

Better:

`Be a patient Linux teacher. I'm new to the terminal and I just saw cd ~. Explain what it means in plain English and give me one example. If your answer gets too technical, simplify it.`

Look at what changed:

- hero: `patient Linux teacher`
- backstory: `I'm new to the terminal and I just saw cd ~`
- mission: `Explain what it means in plain English and give me one example`
- stay in charge: `If your answer gets too technical, simplify it`

That is the whole model in one prompt.

And that is a prompt you could actually use.

## Build One You Can Keep

Now build one role prompt for a real task you actually care about.

Use this pattern:

`Be a [right hero]. I'm [real backstory]. Help me [specific mission]. If you drift, [how I want to redirect you].`

If you want examples:

`Be a practical project coach. I'm trying to automate one repeated task on my computer, and I do not want a giant project plan. Help me find the next smallest step. If you start going too big, bring it back down.`

`Be a careful explainer. I already read the manual, but I still do not understand one command. Help me understand it in plain English. If you use jargon, define it right away.`

`Be a tough-but-clear editor. I wrote a rough plan for my learning project. Help me tighten it into something I can actually do this week. If you start rewriting my whole life, stop and keep it small.`

Pick one.

Rewrite it so it matches your real situation.

Keep it.

That is your first real Team-Captain prompt.

If you can point to the hero, backstory, mission, and redirect sentence, it is
ready to use.

And if you can save one prompt you could paste into AI right now for a real
task, you have finished the work of this chapter.

## What This Opens

You do not need one perfect master prompt for all of life.

You need the ability to choose the right helper for the moment.

That is a much more human skill.

And it is a much more useful one.

You can now turn a fuzzy need into a reusable prompt that gets better help
faster.

In the next chapter, we are going to talk about why even a well-chosen helper
still drifts, improvises, and needs correction.

That is not a flaw in your character.

It is part of the nature of the tool.
