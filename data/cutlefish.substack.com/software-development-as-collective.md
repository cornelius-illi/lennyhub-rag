Back in late February, Tom Kerwin and I wrote a post titled [How Capable Leaders Navigate Uncertainty and Ambiguity](https://cutlefish.substack.com/p/tbm-274-how-capable-leaders-navigate). The post listed 18 competencies—things like Accept We are Part of the Problem and Blend Diverse Perspectives—along with sample questions you could ask yourself or someone else to reflect on each competency.

A couple of days later, Hazel Weakly shared [a deeply introspective post](https://hazelweakly.me/blog/observations-of-leadership-part-one/) in which she used our post as the basis for a personal retrospective. I, like many others on LinkedIn, was completely blown away by the depth and thoughtfulness of the post. 

In this episode, we talk about Hazel’s journey from individual force multiplier to focusing on collaborative learning and scaling that up. We talk about emergence and systems, developer productivity, architecture as a catalyst for coherent autonomy, migrations, being Done, Done Done, Done Done Done, and how being explicit about values, culture, and collaboration enables more graceful and continuous change. We end by discussing how leaders can’t wait for outcomes to introspect and get feedback (hence Hazel doing that deep dive personal retrospective).

Hazel is currently a Principal Platform Architect at Datavent, serves as a Director on the board of the Haskell Foundation, and is [known as the Infrastructure Witch of Hachyderm](https://hachyderm.io/@hazelweakly) (a popular Mastodon instance).

Hope you enjoy the episode, and thanks for your patience as I become a better podcast host.

**Podcast RSS:**

Subscribe to The Beautiful Mess Podcast in your favorite podcast platform using this RSS URL: [https://api.substack.com/feed/podcast/24711.rss](https://api.substack.com/feed/podcast/24711.rss)

**Will Larsen’s post on migrations**  
[https://lethain.com/migrations/](https://lethain.com/migrations/)

**More info on Stripe’s migration to TypeScript**  
[https://stripe.com/blog/migrating-to-typescript](https://stripe.com/blog/migrating-to-typescript)

**Cat Hicks (and team)’s Developers Thriving work**

[https://www.pluralsight.com/resource-center/guides/developer-thriving-research-paper](https://www.pluralsight.com/resource-center/guides/developer-thriving-research-paper)

**Hazel’s retrospective post**

[https://hazelweakly.me/blog/observations-of-leadership-part-one/](https://hazelweakly.me/blog/observations-of-leadership-part-one/)

**Hazel Weakly’s contacts info:**

**LinkedIn:** [https://www.linkedin.com/in/hazelweakly/](https://www.linkedin.com/in/hazelweakly/)

**Mastodon**: [https://hachyderm.io/@hazelweakly](https://hachyderm.io/@hazelweakly)

**Website**: [https://hazelweakly.me/blog/](https://hazelweakly.me/blog/)

Transcript

==========

[00:01:35] Hi, Hazel. Thanks for joining me on the podcast.

[00:01:37] **Hazel Weakly:** Glad to be here.

[00:01:39] **John Cutler:** I think I can put a finger on some of the threads in your recent posts on LinkedIn, but I'm not sure I would be right. I want to hear it in your words. What is that thread?

[00:01:49] **Hazel Weakly:** So the common thread, is something that I've been trying to think about and articulate throughout my career of what is it that really drives me and motivates me. The way it has manifested externally doesn't make a lot of sense. It doesn't really have this coherent narrative. But, it made sense to me.

[00:02:10] The way I explain it now, is how do I take this idea of learning and scale it up. Because I think about this collective learning and collective knowledge and the development of it as being essentially what you do in software development.

[00:02:29] Previously I would have considered the explanation of my career as being about how do I be a force multiplier? And how do I multiply the efforts of things? But it turns out that being a force multiplier or having this effectiveness or this productivity or things like that is not really the point. The point is actually a lot more about this collective learning and about how do you work together in this very, very collaborative way.

[00:02:57] That's my current iteration of the common thread. When I think about everything I do—everything I think about from platform engineering to infrastructure to the state of the world, to my ramblings about how broken things are, to developer experience and front end development and back end development— all these sorts of things, product development. How do we, as a society, actually understand and figure out, not just how to work together, not just how to be effective and win capitalism or whatever. But actually how do we take this learning thing and then do it better at scale?

[00:03:31] **John Cutler:** What was the moment like when you started to question the idea of the individual force multiplier? And started thinking more about collaborative learning?

[00:03:41] **Hazel Weakly:** It was when I started thinking more and more about emergent behavior and systems. If I think about myself as being an individual multiplier or a change agent, you're not really thinking about the emergent behavior of a system. You are the emergent behavior.

[00:03:58] There's this individualistic, I can change the world kind of philosophy that's happening there. That goes pretty far. It goes really, really far, especially if you get really good at change agency, you can single handedly influence an organization of hundreds of people, maybe even thousands of people.

[00:04:17] The thing that I find is that your presence is the multiplier not the outputs of what you did. And so you end up with these people who become very effective change agents, like me. And then they leave, the change agency stops happening. And that is unsatisfying to me, because what's the point of developing something and building up an improvement in the system when the system doesn't improve if you step away from it. That's not actually building something that works to me.

[00:04:49] You can't emergently develop this emergent behavior from a single person. It's the interactions that make more sense and have more impact and are more rewarding than any individual action in the system.

[00:05:01] **John Cutler:** When you were doing your whole force multiplying thing, if you could coach yourself now, if you could go back in time --you're now Hazel and you're coaching force multiplier hero, Hazel--what would you have told yourself?

[00:05:14] **Hazel Weakly:** When you take people and you don't necessarily improve their autonomy, but you improve their ability to do things and ability to execute, you're a massive force multiplier, but you're not building a system that people can interact with and collaborate with and develop with in a way that actually works.

[00:05:32] So what I would have told, you know previous self, I would have told her "What you need to do and what you need to think about is not can I build things that enable people to do more, to be faster, to whatever, but can I build ways of thinking, ways of doing, ways of collaboration, ways of peopling that make it so that local decisions have the emergent behavior of being globally coherent."

[00:05:58] That local architectural choices, local product development choices, local experimentation, local knowledge gathering, bubbles up, becomes coherent, and moves everything forward in the right direction. It's not even, can I make this person's output twice as fast or twice as better or twice as whatever, it's can I give them the ability to make decisions that I don't even have to check in with them? They don't have to check in with me. We're going to collaborate together. We're going to check in together naturally as a very intentional process of building those check in mechanisms. Not in local small choices that they make in the day to day. The local small things that they do in the day to day are globally coherent. That is true multiplication of not just the force, but of the system's synergy.

[00:06:47] **John Cutler:** Which is funny because people talk about developer productivity as some kind of end goal, but it would seem from what you're saying that that's not quite it. What are your thoughts when people go on about developer productivity?

[00:07:00] **Hazel Weakly:** So developer productivity is a fascinating topic to me in a lot of different avenues. So when you think about developer productivity, you have to take a step back. It's not about the developers. And it's actually a really unfortunate naming of developer productivity or developer experience or developer, throw the word developer out. Please just do that. It's knowledge work.

[00:07:22] And it's not how do I make knowledge work more productive. Because you can't really do that in a way that makes sense. So I like to actually think about it in terms of like artistry. If you take an artist and you tell the artist, "Hey, I would like you to, you know, Do more paintings per hour." Not only is that a concept that literally doesn't make sense, but it's going to ruin all of the art over time, it's going to burn them out, it's going to, essentially they're going to quit art and they're going to go, screw it, I'll do something more creative like accounting or taxes.

[00:07:57] And the thing that is fascinating about that is you get two very different splits in the industry for research of how to do this. get one split that is focusing very much on sort of business oriented outcomes and how to move the lever for like developers specifically. And then you have one other bent of the research that really focuses on the cognitive science background of things. And they end up with often complementary but very different ways of thinking about it and approaching it and measuring it and reconciling with it. So, I like the cognitive science side, because that's the interesting one to me.

[00:08:39] And it turns out that for developer productivity, quote unquote, for knowledge work. Knowledge work is fruitful not, you know, productive, not, you know, effective. It's fruitful when you create the right conditions for success and you feel it and you tend it like a garden. So if the people in knowledge work feel like their work is valued, they feel like they have autonomy in measuring what value means, they feel like they have this ability to share what they learn and share what they know, and they have the ability to make experiments and take risks and just go off forth and learn. That is seen by the collective and seen by leadership and recognized and validated.

[00:09:28] Those are the conditions of fruitful knowledge work. And that comes from Cat Hicks' Developer Thriving paper. But you see that not just in developers. You see that in product management. You see it in basically every aspect of the business where you have this, " Oh, this is actually kind of creative after all," element. You need that exploratory, collaborative learning thing. And that's where my huge sort of interest in collaborative learning and scaling that really comes from and really keeps showing up over and over.

[00:10:00] **John Cutler:** What's the role of architecture in all this? If someone self identifies as an architect or has that in their title what role do they have in collaborative learning?

[00:10:09] **Hazel Weakly:** There's a part of learning that only happens from doing. And if you think about software development as you need to implement a functionality and implement this, you know, feature, implement this, you know, how things work and glue it all together in a way that works.

[00:10:25] The process of figuring out how you glue things together, how you build that infrastructure, how you go about developing these things and how you build these structures of the structures of the structures that allow you to continue to learn and develop and iterate. And have this management of change rather than making change easy to do, make it easy to handle. And this adaptive capacity and all these tenets of good design, of good thinking, of good whatever. That ends up a lot of times being called architecture.

[00:11:00] And so when I think of my role as an architect, it is not just sitting down and drawing a cloud diagram or figuring things out. It is very fundamentally, how do I help build the ways of doing, the ways of working, the ways of collaborating that make the local decisions and the local architectural choices and local software development have an emergent property of aligning with the business goals and the business needs. So making it a natural emergent property of the software development process is the role, to me, of an architect, and that's a complementary role and a peer role to that of people leadership.

[00:11:41] People leadership is how do I get people working together? How do I build that culture? How do I build that ways of operating in the company? Have I built the company in a way that they have this environment where that works? And then when it comes down to the doing the side of it, they have to be synergetic. That's where the socio technical part comes from. They're both socio technical. One has a bit more focus in social. One has a bit more focus in technical. But they're both having to interlock together.

[00:12:08] **John Cutler:** What's an example of something that will tend to get an architect a raise and a promotion, but will be dangerous and harmful to a company in the long run?

[00:12:18] **Hazel Weakly:** So the snarky answer would be like, you know, adopting a popular technology stack. And just going, "Oh, yeah, we need to do this sort of refactoring and we need to migrate to new technology stack. We need to do all these sorts of things." And that often has buy in as once you get the buy in, you're committed to a very large migration project.

[00:12:39] And nobody likes to fail a migration or, you know, stop at halfway through. So you end up using the sunken cost fallacy as a weapon to your advantage to push through a very large change in an organization. But changing an organization, they're very fragile structures, and ripping out their support structures and their embedded ways of doing things through a large scale migration, if it doesn't fail, it'll probably end up settling and mapping back into, "This didn't really change anything."

[00:13:11] And you see that all the time, where people go, "Oh, we develop in this way, and we do this, and we have all these problems, and now we need to move to Kubernetes, and that'll solve all our problems.

[00:13:21] And you have a four year migration to Kubernetes, same problems twice the cloud bill. And they're like, did this fix anything? Ehhh, the architects got a raise for sure. They got a promotion, they got a whole bunch of things. But did it solve the problem of the company, when the problem maybe was You know, a company just refuses to talk to their users.

[00:13:42] **John Cutler:** Is there a safer approach?

[00:13:45] It seems like that momentum that's built up by this pitching it and getting everyone excited about it. Some would argue that's the only thing you can do to nudge the thing into being and get the ball rolling. Is there a better way to try to make something like that possible?

[00:14:02] **Hazel Weakly:** It comes down to, I think, two or three different things. One is that you need to think of migrations in a different way. A lot of people think of migrations as essentially you see a problem, you have the solution that will fix the problem, we need to migrate to a new solution. But the problem with that is they're solving a multifaceted problem with a single faceted technical solution.

[00:14:30] So that in and of itself is just not going to really work. And the second thing that often runs into with migrations. is people think of migrations like the word migration. Kind of implies to us a one time, one shot thing. And when you look at migrations in nature, migrations in the wild, migrations are not migration, it's a migratory pattern.

[00:14:56] And that is the mindset shift you need until the migration is, how do we make change easy to handle? And as an artifact of doing that, be willing to do change and that's migrations. So you want a migratory approach to, you know, software development, or, you know, business thinking, or like, you know, product development, like pivoting in business is a migration, we don't call it that.

[00:15:25] And it's fine to pivot a bunch of times, but you can't migrate your code based architecture multiple times, are you serious? But like, pivoting is safe, pivoting is fine, you can pivot four times a quarter, it's totally cool, it's totally cool. The migrations are like pivots, and you want to actually be able to pivot, it's a feature, not a bug.

[00:15:44] An effective business is one that can pivot. An effective software code base and architecture and way of development is one that can do migrations. And one of the core competencies to develop technically is the ability to do migrations.

[00:15:59] Will Larson has a blog post on essentially how to do migrations and pretty much everybody has this sort of same three step process.

[00:16:09] Database migrations, code base based migrations, technical migrations, everything comes into the same three phases of you de risk the migration by making sure that it actually works for the corner cases, the weird cases, the people. That's where you find like a small team. You figure it out, you work with it, you do that, and you, you prove it out before committing.Try before you buy, essentially.

[00:16:33] You do that. Product development, same thing. You reach out to your users, you reach out to people, and you go, "Oh, hey, we're thinking of this idea. Are we going to spend nine months building it? Who knows yet? We're going to show you a mockup." Like, right? Like, you know, build the feature, you test it out first. You prove it out a little bit. Not all the way, but a little bit.

[00:16:53] And then there's the enabling phase of the migration, and that is, you need to automate essentially 90 percent of it before really doing it. That is where you take the migration from essentially an impossible slog to something that can be done.

[00:17:10] And one of the most amazing examples of that in software development is actually a code base migration that Stripe did and they wrote about how they did it. They migrated four million lines of JavaScript code to TypeScript in one weekend. Plus six months of enablement work, but one weekend of actual execution. And what they did was they built essentially a compiler that took their code and took their annotations and their commenting style and their JavaScript types and their flow types and all these other things. And then they would run it over the whole code base every day until they had tweaked this compiler transformer thing to work.

[00:17:51] Then they ran it. Did the last 200 or 400 fixes manually. Shipped it, boom, done

[00:17:57] But then there's the third phase. Last mile, and that's the finishing part. That's where you need that burn down chart, that's where you need that one by one whack a mole. Because you have done, and you have done done, and you have done done done, and you have this is so done, it's never gonna need to be touched again or thought about. Those are all extremely distinct levels of doneness.

[00:18:20] A lot of people stop at the first one. I need to get to at least done done. Done done done is great. That's where it's so done that everyone thinks it's done. Not, it's actually done, everyone thinks it's done. That's, that's the three dones. The, it's so done you never have to think about it again. Most people never get there, but that one is sort of the cultural collective knowledge of how it was before has been internalized, and now we understand why we did this migration. And we never ever really have to think about it again, and everyone in the company who is involved with this understands essentially the migration and can instantly answer any question about why is your current state this instead of this? And that is so done, we've internalized knowledge, we've learned from it collectively. Most people never get that.

[00:19:11] But if you can get to Done Done and if you can get really, really good at getting to Done Done you're going to get somewhere. And if you build that into your methodology and your ways of doing --a code based architecture that actually makes it easy to get to Done Done --then migrations, if they become a way of life, stop being viewed as churn, and start being viewed similar to pivots. It's not a failure. It's a pivot. Migrations don't mean you failed previously. And so doing them over and over and over doesn't mean you suck at software.

[00:19:41] **John Cutler:** One thing that stands out about that is taking that same approach to thinking about changing ways of working or retrospectives. I mean, I think everyone can relate to going into retrospectives. Everyone's talking about communications hard, this is hard, this is hard, but nothing seems to happen. It's just sort of a gripe cycle, which I think is okay in some sense, but it turns into that.

[00:20:03] And I'm trying to think about the analogy you just gave in comparing that to teams that almost rehearse changes as part of their daily work and just get good at change versus, you know, big bang reorgs or other things. I haven't been able to put a finger on what differentiates organizations that can take one approach or another. There's some words that seem to only be able to get something done and change when it's this huge disruptive thing. And there's some that seem to be able to it change effortlessly and one commonality there may be that they rehearse change a lot. They practice it. Any thoughts on that?

[00:20:37] **Hazel Weakly:** I don't even necessarily think it's practicing change a whole lot. I think it's how you view the structure of the organization and how you view what you do with it.

[00:20:48] When you have this concrete culture and concrete ways of working and concrete, we sit down and we're very intentional about talking about how we learn, talking about how we work together, our values are the most important things to talk about, our ways of working are the most important things to talk about. How we develop and grow and learn, that becomes the explicitly laid down, demarcated, talked about, intentionally built up, crafted structure of the company. You don't need a bunch of structure elsewhere anymore. So then, you get this wibbly wobbly org chart and you get this wibbly wobbly software architecture.

[00:21:25] And that gives a company an appearance of massive flexibility and mobility. Because the thing they chose to ossify was that we're going to work together well, and we're going to rethink how we do it. Those are the two things that you set in stone. A surprising amount of inflexible things become re-imaginable.

[00:21:45] When we set in stone we're Java shop. And you set in stone, we have this org chart, we have directors, we have VPs, we have, you know, engineering managers, then the things that aren't set in stone, like the software architecture and all these other things, they have to carve into the stone in order to make change. And so the only way to make change is to reinvent it, or rebuild it, or scrap and start over, or change the work chart.

[00:22:10] **John Cutler:** I was really blown away when you built a manager retrospective or a leadership retrospective based on some of these patterns I wrote about for navigating uncertainty. I guess one question would be how, how often should managers or leaders dig that deep in terms of introspection? Because you went so deep. And you kind of ripped yourself apart. And so one, what was that like, uh, two you know, what would you suggest to other people in terms of thinking about how they work and how they tackle uncertainty and when is it too much, uh, to dig that deep?

[00:22:45] **Hazel Weakly:** So, that one's a really fun question. So for me, I dig that deep because that's like just how I am. I've always been very, very deeply introspective. And that's a fascinating blend of childhood trauma and how my brain works and just like how I survived everything. I like to dig very, very, very deep in this introspective behavior. And that's how I learn and think about things and develop stuff. And it's also kind of, to me, the only way to make meaningful progress when nobody has answers anymore. And you become in this, you know, awkward stage of, "Oh, I want a real adult, or I want, you know, a real expert." And you are the adult and you are the expert so that introspection really becomes required. In terms of how often people should do that, I think it really comes down to how are you reflecting on and learning about what you're doing and the results and outcomes of what you're doing? Are you looking for that? Are you able to even see that? What's going on there?

[00:23:51] And for leaders your feedback times become unreasonable. They become ineffective. You can't actually learn how to be a better director or how to be a better Manager sometimes because the manager feedback loops are like three to six months. The director feedback loops are one to three years. And by the time you get to a CTO, you're at like a five to ten year feedback loop time. Which means you are only going to learn two lessons from what you do by waiting for the results in your entire fucking career. You cannot be an effective executive if you only learn from seeing the results of your outcomes.

[00:24:30] You have to find other ways to get that feedback and get that response and develop and articulate ways of improving yourself that go far beyond "I'm gonna do this and see what happens."

[00:24:40] So for me it was am I effective in learning at the pace that I can be. And since I learned so quickly and so rapidly, I need to spend consequently a lot more time digging deep and a lot more time digging into the sort of feedback loops and finding ways to learn and reflect and introspect and improve and think about and rationalize and operate at a much shorter time scale than the results of my actions actually come from. And that's why I needed so much introspection and then that often ends up giving me a fun result of it makes it much much easier to see the multiple different manifestations of the actual outcomes.

[00:25:26] There's not just, here's the outcome. There's like one big outcome. Yes. But there's like 20 smaller outcomes. And those add smaller smaller outcomes. And you see this splintering ripple effect from the decisions that you make in leadership. And unless you've done a lot of reflecting and thinking about things before those small ripples start to happen, you're not really going to see them happening in real time in a way that lets you go "Okay this was part of what I did" and that's where a lot of the value has come for me.

[00:25:57] **John Cutler:** Gets me thinking, should do a better job. Okay. Get it together. Well, I think that's a great place to stop. I get the feeling that you like collaborating with other people and learning and watching people learn. What's the best way for people to do that with you? How could they connect with you? How can they learn alongside you?

[00:26:21] **Hazel Weakly:** I'm, very terminally online and very findable on the internet. If you reach out to me on LinkedIn I'll probably respond. If you just send me a connection request with no context it's a little harder. But if there's context in there, yeah, i'm happy to work with you happy to respond to you If you have questions, if you want to find me in one of the many different Slack groups I'm in, or one of some of the Discord groups that I'm in, or some of the other places, yeah, absolutely.

[00:26:49] I'm also mostly on Mastodon. That's my main social media network. You can also find me there and chat with me. I'm really, really happy to work with people and learn with them and do these sorts of experimentations even if I don't have a lot of concrete time to spend doing things. I'm really happy to talk about them and work together with people like that.

[00:27:12] **John Cutler:** Great. Thank you so much. Hazel.

[00:27:14] **Hazel Weakly:** Thank you, this was a lot of fun.