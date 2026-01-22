![](attachments/80f556ed204f05f69b0c583203624f78.png)

[A recent study (run by Atlassian and DX)](https://www.linkedin.com/pulse/state-developer-experience-2024-abi-noda-gdlfc/) surfaced the following findings:

* 69% of developers lose 8 or more hours each week to inefficiencies.

* Developers lose at least a full day per week due to inefficiencies.

* 2 out of 3 developers are still losing 8+ hours a week to inefficiencies in their roles.

I have no affiliation with Atlassian or DX.

Something has been nagging me about this study for a couple of days now, and I couldn't exactly pinpoint the issue until now.

Take two non-software development examples of teams losing a day a week. Imagine:

* A group of roofers discovers that one of five roofing tacks is defective. They lose 20% of their day fumbling with defective nails. This inefficiency would be intolerable on a construction site.

* The cast of Cirque du Soleil is practicing for a big debut. Randomly, the rehearsal stage goes dark (for a total of 20% time per week). No practice. You have a bunch of performers sitting around waiting. Would that ever fly? I doubt it. The problem would get fixed, or the troupe would decamp to another rehearsal space.

So what's going on? Why—assuming that developers are losing that much time (one full day per week)—aren't there grand mutinies and immediate efforts to address these issues? Imagine knowing, or believing, that 20% of your developer salaries disappear into the ether.

---

*Like the newsletter? Support TBM by upgrading your subscription. Get an invite to a Slack group where I answer questions. In the next couple days, I will be sending out information to TBM supporters about two events in September.*

[Support the newsletter](https://cutlefish.substack.com/subscribe)

---

A couple of thoughts (with the help of some friends):

For the roofers and performers, the waste is extremely tangible. In knowledge work, we typically pivot to another task and take a less tangible context-switching hit. It is possible to be/feel 1) extremely busy AND 2) like you're losing 20% of your week to inefficiencies. Workarounds and task switching become habitual.

"If you smear the pain to all five people [on the team] but at different stages of the day, they don't all get the same annoyance," observed Chris Combe (TeamForm, UBS). "So it's an async distributed pain in the butt vs CICD being down for everyone, in which case you'd probably see action. It's also a function of people in a team working independently vs people working together. If you pair or work together, you can notice this stuff and get feedback that it is not okay and that we should fix it." Contrast this with the Cirque example, where everyone has to stop working.

"Developers complain about DevEx a lot. But it is very expensive to fix, and attempts to fix it often fail or are effective only for a limited period," notes Yaniv Bernstein (Google, Airtasker, IBM). Defective roofing tacks and stage lights are not expensive to fix, and fixing them is seen as "returning to normal." 

On some level, teams get accustomed to "running in degraded mode." "It is part of the job, and pretty much how it has been at all of my jobs" (Developer Friend). "And it is also part of being a manager to remind people that things are never ideal and have them grumble."

Go back to our roofing example. One roofer is struggling with the nail gun. Another roofer is pontificating about a new roofing technology. Another roofer believes the team should implement their fix immediately. The roofers are blaming a shared tack-supplying team for screwing up yet again. Before you know it, the situation has devolved into a mix of technical debates, shaming less experienced team members, and blame. In short, solutions aren't always clear-cut, and complaining about debt and developer experience can take on a life of its own.

Consider all the other waste teams typically put up with—high work in progress, work spending endless time in queues, architectural review theatrics, flippant shifts in strategy, shipping things that fail to move the needle (but must be maintained), throwing people at problems, rushed and ineffective hiring (and supporting new team members), acquisitions that don't pay off, non-value-add administrative overhead, telephone games, etc. As scary as it sounds, losing a day of a week might be a blip in the grand scheme of things. Getting eight more hours of "quality work" might not make any difference whatsoever.

The study notes:

>
>
> "For an organization with 500 developers, losing 8 hours per week costs roughly $6.9 million over the course of a year." 
>
>

The real question is how much revenue those developers could generate with 4,000 hours. I guess that with a sufficiently informed strategy and customer insights, it would be more than $6.9 million. Of course, without the strategy and insights and with lots of WIP, the other 32 hours in the week will take a big hit in terms of ROI. 

Which brings me to a thought.

I'm happy the study is surfacing these insights, but in almost every larger organization I have been in, people were *already giving this feedback.* It wasn't for lack of awareness but more for figuring out *how to talk about it and process what people were saying*. Most teams address local issues within their immediate influence. When it comes to anything more global, they typically face a lot of pushback and second-guessing.

And in the current climate, the conversations often look like this (paraphrasing a discussion with a friend at a large B2C product company):

>
>
> X: "I'd say we're burning around 50% of our time wading through debt, too many priorities, administrative tasks, and trying to muddle through..."
>
>
>
> Me: "My god. That is a lot, especially considering the recent layoffs. It makes any cost savings seem like a drop in the bucket—like saving 10% on gas for a car with terrible gas mileage."
>
>
>
> X: "I know, I know. We all know. But no one is willing to say it out loud."
>
>
>
> Me: "Why?"
>
>
>
> X: "There are a couple of reasons. First, the outspoken people aren't around anymore. There's a lot of pressure to be positive and upbeat. And frankly, by the time we're asked to prove it, and by the time there's no response... what's the use, anyway?"
>
>
>
> Me: "That's tough..."
>
>
>
> X: "I'm not even bitter. It is like everyone has come to a certain peace about the situation. The job market isn't great. Everyone is in wait-and-see mode."
>
>
>
> Me: "But it must make you....frustrated? To wade through that much muck?"
>
>
>
> X: "It used to, but I have gotten a lot better at finding ways to stay busy in moderately interesting ways."
>
>
>
> Me: "Putting yourself in the shoes of leadership, what do they see?"
>
>
>
> X: "Can you imagine how hard it would be to walk into a meeting with investors, whoever, and say, 'um, you thought you had a 30mpg car, and it is a 15mpg car?"
>
>
>
> Me: "Damn, that would be hard."
>
>
>
> X: "Yeah. It wouldn't matter how well-meaning everyone was; you'd probably get fired in two seconds. That's the puzzle, and it flows down layers of management. Everyone is caught in a version of the dynamic."
>
>
>
> Me: "Wow, right. And it escalates and escalates. What could you see fixing this?"
>
>
>
> X: "We'd need the freedom to call it like it is without fearing getting personally blamed or for our managers and their managers to get blamed."
>
>
>
> Me: "Which almost gets harder and harder due to the escalation..."
>
>
>
> X: "Yeah. Impossible, I'd say. But I still wish it was possible."
>
>
>
> Me: "Well, good luck. Stay hopeful, I guess...."
>
>

This is all to say that estimates of time losses are important. However, for companies to truly address the challenge, they must figure out how to remove the layers of fear, blame, and apathy. The study recommends "Feedback loops that allow for continuous improvement through learning and adjustments." This advice is all good, but the path forward requires a deep cultural shift in many companies—not just running retros, incrementally better measurement, and better voice of developer efforts, etc.

These days, people in companies wants to be "efficient" and wants developers to be "productive", but few are willing to make the sacrifices required to achieve operational excellence and foster a culture of continuous improvement. It’s good we have some numbers around this, but the problem (and opportunity) has been out in the open for a long time—it is the talking about it that has been hard.

---

*Like the newsletter? Support TBM by upgrading your subscription. Get an invite to a Slack group where I answer questions. In the next couple days, I will be sending out information to TBM supporters about two events in September.*

[Support the newsletter](https://cutlefish.substack.com/subscribe)

---