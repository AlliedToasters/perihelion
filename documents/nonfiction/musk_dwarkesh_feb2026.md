# Dwarkesh Podcast: Elon Musk on Terawatt of GPUs in Space

**Date:** February 5-6, 2026  
**Guests:** Elon Musk, John Collison  
**Host:** Dwarkesh Patel

## Overview

In this interview, Elon Musk shares a bold vision for the future of artificial intelligence, predicting that space will become the most cost-effective location for AI infrastructure within the next 36 months. He explains that as global power demands hit a "hardware wall" on Earth, the abundance of solar energy in space and the reduced need for heavy protective materials make orbit an ideal environment for scaling massive data centers. The conversation also delves into how SpaceX aims to become a major AI hyperscaler by leveraging Starship's high-frequency launch capabilities to bypass terrestrial energy bottlenecks. Overall, the video highlights Musk's "first principles" approach to solving complex engineering challenges and his commitment to leaning into acute technical pain to ensure rapid innovation.

---

## The Economics of Space-Based Data Centers

**DWARKESH PATEL:** So, as you know better than anybody else, the total cost of ownership of a data center, only 10 to 15% is energy. And that's the part you're presumably saving by moving this into space. Most of it's the GPUs. If they're in space, it's harder to service them or you can't service them, and so the depreciation cycle goes down on them. So it's just way more expensive to have the GPUs in space, presumably. What's the reason to put them in space?

**ELON MUSK:** Well, the availability of energy is the issue. So, I mean, if you look at electrical output outside of China, everywhere outside of China, it's more or less flat. It's very, you know, maybe a slight increase, but pretty close to flat. China has a rapid increase in electrical output.

But if you're putting data centers anywhere except China, where are you going to get your electricity? Especially as you scale, the output of chips is growing pretty much exponentially, but the output of electricity is flat. So how are you going to turn the chips on? Magical power sources. Magical electricity fairies.

**DWARKESH PATEL:** You're famously a big fan of solar. 1 terawatt of solar power. So with a 25% capacity factor, like 4 terawatts of solar panels, it's like 1% of the land area of the United States. And that's like, we're in the singularity when we've got one terawatt of data centers.

**ELON MUSK:** Right.

**DWARKESH PATEL:** So what are we running out of exactly?

**ELON MUSK:** How far into the singularity are you, though?

**DWARKESH PATEL:** You tell me.

**ELON MUSK:** Yeah, exactly. So I think we'll find we're in the singularity and like, okay, we've still got a long way to go.

**DWARKESH PATEL:** But is this like a—is the plan to put it in space after we've covered Nevada in solar panels?

**ELON MUSK:** I think it's pretty hard to cover Nevada in solar panels. You have to get permits from—try getting the permits for that.

**DWARKESH PATEL:** So space is really a regulatory—it's really a regulatory play. It's harder to build on land than it is in space.

## Why Space is the Optimal Solution

**ELON MUSK:** It's harder to scale on ground than it is to scale in space. But also, you're going to get about five times the effectiveness of solar panels in space versus the ground. And you don't need batteries. I almost wore my other shirt, which says "it's always sunny in space," which it is.

Because you don't have a day-night cycle or seasonality, clouds, or an atmosphere in space. The atmosphere alone results in about a 30% loss of energy. So any given solar panel can do about five times more power in space than on the ground, and you avoid the cost of having batteries to carry you through the night.

So it's actually much cheaper to do in space. And my prediction is that it will be by far the cheapest place to put AI will be space in 36 months or less.

**DWARKESH PATEL:** Maybe 36 months.

**ELON MUSK:** Less than 36 months.

**DWARKESH PATEL:** How do you service GPUs as they fail, which happens quite often in training?

**ELON MUSK:** Actually, it depends on how recent the GPUs are that have arrived. I mean, at this point, we found our GPUs to be quite reliable. There's infant mortality, which you can obviously iron out on the ground. So you can just run them on the ground and confirm that you don't have infant mortality with the GPUs.

But once they start working, their actual reliability, once they start working and you're past the initial debug cycle of Nvidia or whatever, or whoever's making the chips—could be Tesla AI 6 chips or something like that, or it could be TPUs or Trainiums or whatever—the reliability is actually quite reliable past a certain point. So I don't think the servicing thing is an issue.

But you can mark my words, in 36 months, but probably closer to 30 months, the most economically compelling place to put AI will be space. And then it'll get ridiculously better to be in space. And then the scaling—the only place you can really scale is space. Once you start thinking in terms of what percentage of the sun's power are you harnessing, you realize you have to go to space. You can't scale very much on Earth.

**DWARKESH PATEL:** To be clear, you're talking like terawatts.

## The Scale of Power Requirements

**ELON MUSK:** Yeah, well, all of the United States currently uses only half a terawatt per hour on average. Right. So if you say a terawatt, that would be twice as much electricity as the United States currently consumes. So that's quite a lot.

And can you imagine building that many data centers, that many power plants? It's like those who have lived in software land don't realize that they're about to have a hard lesson in hardware—that it's actually very difficult to build power plants.

And then you don't just need the power plants, you need all of the electrical equipment, you need the electrical transformers to run the transformers, the AI transformers.

Now, the utility industry is a very slow industry. They impedance match to the government, to the public utility commission. So they're very slow because their past has been very slow. So trying to get them to move fast is just like, you know, if you're trying to do an interconnect agreement—have you ever tried to do an interconnect agreement with a utility at scale? Like with a lot of power?

**DWARKESH PATEL:** As a professional podcaster, I can say that I have not.

**ELON MUSK:** In fact, yeah, they have to do a study for a year. Okay. Like a year later they'll come back to you with their interconnect study.

**JOHN COLLISON:** Can't you solve this with your own behind-the-meter power stuff?

**ELON MUSK:** You can build power plants. Yeah, that's what we did at xAI for Colossus, so for Colossus too.

**JOHN COLLISON:** But so yeah, why are we talking about utilities? Why not just build GPUs and power co-located?

**ELON MUSK:** That's what we did.

**JOHN COLLISON:** Right. But I'm saying why isn't this a generalized solution? When you're talking about all the issues—

**ELON MUSK:** Where do you get the power plants from?

**JOHN COLLISON:** I'm saying when you talk about all the issues working with utilities, you can just build private power plants with the data centers.

**ELON MUSK:** Right. But it begs the question of where do you get the power plants? Where do you get the power plants from? I mean the power plant makers.

**JOHN COLLISON:** Oh, that's what you're saying. Like this is the gas turbine backlog? Basically, yes.

## The Turbine Bottleneck

**ELON MUSK:** You can drill down to a level further. It's the vanes and blades in the turbines that are the limiting factor because the casting—it's like a very specialized process to cast the blades and vanes in the turbines using gas power. And it's very difficult to scale other forms of power. You can scale potentially solar, but the tariffs currently for importing solar in the US are gigantic and the domestic solar production is pitiful.

**JOHN COLLISON:** Why not make solar? That seems like a good Elon-shaped problem.

**ELON MUSK:** We are going to make solar. Okay, great. Both SpaceX and Tesla are building towards 100 gigawatts here of solar cell production.

**DWARKESH PATEL:** How low down the stack, like from polysilicon up to the wafer to the final panel?

**ELON MUSK:** I think you got to do the whole thing from raw materials to the finished cell. Now, if it's going to space, it actually costs less. And it's easier to make solar cells that go to space because they don't need glass or they don't need much glass and they don't need heavy framing because they don't have to survive weather events. There's no weather in space. So it's actually a cheaper solar cell that goes to space than the one on the ground.

**DWARKESH PATEL:** Is there a path to getting them as cheap as you need in the next 36 months?

**ELON MUSK:** Solar cells are already very cheap. They're like farcically cheap. And if you say, I think solar cells in China are around like 25, 30 cents a watt or something like that, it's absurdly cheap.

And when you take into account now put it in space and it's five times cheaper because it's five times—in fact, no, it's not five times cheaper. It's 10 times cheaper because you don't need any batteries. So the moment your cost of access to space becomes low, by far the cheapest and most scalable way to generate tokens is space. It's not even close. It'll be an order of magnitude easier to scale.

And chips aside, an order of magnitude. The point is you won't be able to scale on the ground. You just won't. People are going to hit the wall big time on power generation. There already are.

So the number of miracles in series that the xAI team had to accomplish in order to get a gigawatt of power online was crazy. We had to gang together a whole bunch of turbines. And then we had permit issues in Tennessee and had to go across the border to Mississippi, which is fortunately only a few miles away. But then we still had to run the high power lines a few miles and build a power plant in Mississippi. And it was very difficult to build that.

And people don't understand how much electricity do you actually need at the generator level, at the generation level in order to power a data center? Because they look at the specs, will look at the power consumption of say a GB 300 and multiply that by the number and then think that's the amount of power you need.

**JOHN COLLISON:** All the cooling and everything.

## The Real Power Requirements

**ELON MUSK:** Wake up. Yeah, that's a total noob. You've never done any hardware in your life before. Besides the GB 300, you've got to power all of the networking hardware. There's a whole bunch of CPU and storage stuff that's happening. You've got to size for your peak cooling requirements.

So that means can you cool even on the worst hours, the worst day of the year? Well, it gets pretty freaking hot in Memphis, so you're going to have like a 40% increase on your power just for cooling. Assuming you don't want your data center to turn off on hot days and you want it to keep going, then you've got to say, well, there's another multiplicative element on top of that, which is are you assuming that you never have any hiccups in your power generation?

Like, oh, well, actually sometimes we have to take the generators, some of the power offline in order to service it. Oh, okay, now you add another 20, 25% multiplier on that because you've got to assume that you've got to take power offline to service it.

So the actual—roughly every 110,000 GB 300s inclusive of networking, CPU, storage, cooling, margin for servicing power is roughly 300 megawatts.

**JOHN COLLISON:** Sorry, say that again.

**ELON MUSK:** It's roughly—or think about it like a way to think about it is like 330,000. What you need at the generation level to service, probably service 330,000 GB 300s, including all of the associated support, networking and everything else, and the peak cooling and to have some power margin reserve is roughly a gigawatt.

**DWARKESH PATEL:** Can I ask a very naive question? You're describing the engineering details of doing this stuff on Earth, but then there's analogous engineering difficulties of doing it in space. How do you replace InfiniBand with orbital lasers, et cetera, et cetera. How do you make it resistant to radiation? I don't know the details of the engineering, but fundamentally what is the reason to think those challenges, which have never been had to be addressed before, will end up being easier than just like building more turbines on Earth. There's companies that build turbines on Earth. They can make more turbines. Right?

**ELON MUSK:** I invite again, try doing it and then you'll see. So like, the turbines are sold out through 2030.

**JOHN COLLISON:** Have you guys considered making your own?

**ELON MUSK:** I think in order to bring enough power online, I think SpaceX and Tesla will probably have to make the turbine blades, the vanes and blades internally.

**JOHN COLLISON:** Just the blades or the turbines?

## The Challenge of Turbine Manufacturing

**ELON MUSK:** The limiting factor, you can get everything except the blades. They call the blades and vanes. You can get that 12 to 18 months before the vanes and blades. The limiting factor of the vanes and blades, and there are only three casting companies in the world that make these and they're massively backlogged, is this Siemens.

**JOHN COLLISON:** GE, those guys, or is it a subcontractor?

**ELON MUSK:** No, it's other companies. I mean sometimes they have a little bit of casting capability in house. But I'm just saying you can just call any of the turbine makers and they will tell you it's not top secret. They're probably on the, it's probably on the Internet right now.

**DWARKESH PATEL:** If it wasn't for the tariffs, would Colossus be solar powered?

**ELON MUSK:** It would be much easier to make it solar powered. Yeah, the tariffs are nuts, so several hundred percent.

**JOHN COLLISON:** So don't you know, some people.

**ELON MUSK:** We also need speed. Yeah, no, you know, President has his, you know, we don't agree on everything and this demonstration is not the biggest fan of solar. We also need the land, the permits and everything. So if you're trying to move very fast, I do think scaling solar on Earth is a good way to go. But you do need some amount of time to find the land, get the permits, get the solar, pair that with batteries.

**JOHN COLLISON:** But why would it not work to stand up your own solar production? And then you're right that you eventually run out of land. But there's a lot of land here in Texas, there's a lot of land in Nevada, including private land. It's not all publicly owned land. And so you'd be able to at least get the next Colossus and like the next one after that. And at a certain point you hit a wall. But wouldn't that work for the moment?

**ELON MUSK:** As I said, we are scaling solar production. There's a rate at which you can scale physical production of solar cells where we're going as fast as possible.

**JOHN COLLISON:** In scaling domestic production, you're making the solar cells at Tesla.

**ELON MUSK:** Both Tesla and SpaceX have a mandate to get to 100 gigawatts a year of solar.

## AI Infrastructure: Earth vs. Space in Five Years

**JOHN COLLISON:** Speaking of the annual capacity, I'm curious, in five years time, let's say, what will the installed capacity be on Earth is a long time and in space I deliberately pick five years because it's after your once we're up and running threshold. And so in five years time. Yeah. What's the on Earth versus in space installed AI capacity?

**ELON MUSK:** Five years? I think probably if you say five years from now, we're probably AI in space will be launching every year the sum total of all AI on Earth in excess, meaning five years from now. My prediction is we will launch and be operating every year more AI in space than the cumulative total on Earth, which is I would expect to be at least sort of five years from now. A few hundred gigawatts per year of AI in space and rising.

So you can get to, I think on Earth you can get to around a terawatt a year of AI in space before you start having fuel supply challenges for the rocket.

**JOHN COLLISON:** Okay, but you think you can get hundreds of gigawatts per year in five years time?

**ELON MUSK:** Yes.

**DWARKESH PATEL:** So 100 gigawatts depending on the specific power of the whole system with solar arrays and radiators and everything is on the order of like 10,000 Starship launches.

**ELON MUSK:** Yes.

**DWARKESH PATEL:** And you want to do that in one year. And so that's like one Starship launch every hour that's happening in this city. Walk me through a world where there's a Starship launch every single hour.

**ELON MUSK:** Yeah, I mean that's actually a lower rate compared to airlines like aircraft.

**DWARKESH PATEL:** There's a lot of airports.

**ELON MUSK:** A lot of airports.

**DWARKESH PATEL:** And you got to launch the polar orbit.

**ELON MUSK:** No, it doesn't have to be polar, but there's some value to sun synchronous. But I think actually you just go high enough, you start getting out of Earth's shadow.

**DWARKESH PATEL:** How many physical Starships are needed to do 10,000 launches a year?

**ELON MUSK:** I don't think we'll need more than. I mean, you could probably do it with as few as like 20 or 30. It really depends on how quickly the ship has to go around the Earth and the ground track before the ship has to come back over the launch pad. So if you can use a ship every, say 30 hours, you could do it with 30 ships, but we'll make more ships than that. But SpaceX is gearing up to do 10,000 launches a year and maybe even 20 or 30,000 launches a year.

## SpaceX as a Hyperscaler

**DWARKESH PATEL:** Is the idea to become basically a hyperscaler, become an Oracle and lend this capacity to other people? What are you going to do with. Presumably SpaceX is the one launching all this, so SpaceX become a hyperscaler.

**ELON MUSK:** Hyper. Hyper, yeah. I mean, if some of my predictions come true, SpaceX will launch more AI than the cumulative amount on Earth of everything else combined.

**DWARKESH PATEL:** Is this mostly inference or most AI.

**ELON MUSK:** Will be inferenced already? Inference for the purpose of training is most training.

**JOHN COLLISON:** And there's a narrative that the change in discussion around a SpaceX IPO is, is because previously SpaceX was very capital efficient. Just it wasn't that expensive to develop that. Even though it sounds expensive, it's actually very capital efficient in how it runs. Whereas now you're going to need more capital than just can be raised in the private markets, like if the private markets can accommodate raises of, as we've seen from the AI labs, tens of billions of dollars, but not beyond that, is it that you'll just need more than tens of billions of dollars per year? And that's why I'd say go public.

**ELON MUSK:** Yeah, I have to be careful about saying things about companies that might go public.

**JOHN COLLISON:** If you make general statements, that's never.

**DWARKESH PATEL:** Been a problem for you, Elon.

**ELON MUSK:** There's a price to pay for these things.

**JOHN COLLISON:** Make some general statements for us about the depth of the capital markets between public and private markets.

**ELON MUSK:** Yeah, there's a lot more capital in the very general. There's obviously a lot more capital available in the public markets than private. I mean, it might be, it's at least, it might be 100 times more capital, but it's at least way more than 10.

**JOHN COLLISON:** But isn't it also the case that things that tend to be very capital intensive, if you look at say, real estate, as you know, a huge industry that raise a lot of money each year, is at an industry level that tends to be debt financed because by the time you're deploying that much money, you actually have a pretty, you have.

**ELON MUSK:** A clear revenue stream.

**JOHN COLLISON:** Exactly. And a near term return. And you see this even with the data center build outs, which are famously being, you know, financed by the private credit industry. And so why not just debt finance?

**ELON MUSK:** Speed is important. So I'm generally going to do the thing that, I mean, I just repeatedly tackle the limiting factor, whatever the limiting factor is on speed, I'm going to tackle that. So there's, if capital is the only factor, then I'll solve for capital. If it's not limiting factor, I'll solve for something else.

**DWARKESH PATEL:** Based on your statements about Tesla and being public, I wouldn't have guessed that you thought the fast, the way to move fast is to be public.

**ELON MUSK:** Normally I would say yeah, that's true. Like I said, I mean, I'd love to talk about this in more detail, but the problem is like if you talk about public companies where they become public, you get into trouble and then you have to delay your offering and then you.

**JOHN COLLISON:** And as you said, solving for speed.

**ELON MUSK:** Yes, exactly. So you can't hype companies that might go public. So that's why we have to be a little careful here.

## Scaling Energy: From Earth to the Kardashev Scale

**ELON MUSK:** But we can't talk about physics. So the way you think about scaling long term is that Earth only receives about half a billionth of the sun's energy. And the sun is essentially all the energy. This is a very important point to appreciate because sometimes people will talk about marginal nuclear reactors or any various fusion on Earth, but you have to step back a second and say if you're going to climb the Kardashev scale and have some non trivial and harness some non trivial percentage of the sun's energy, like let's say you wanted to harness a millionth of the sun's energy, which sounds pretty small, that would be about, call it roughly 100,000 times more electricity than we currently generate on Earth for all of civilization, give or take an order of magnitude.

So it obviously the only way to scale is to go to space. With solar, from launching from Earth you can get to about a terawatt per year. Beyond that you want to launch from the moon, you want to have a mass driver on the moon, and that mass driver on the moon you could do probably a petawatt per year.

**DWARKESH PATEL:** When you're talking these kinds of numbers, terawatts of compute, presumably whether you're talking land or space, far, far before this point, you've run into, you actually need, maybe the solar panels are more efficient, but you still need the chips, you still need the logic and the memory and so forth.

**ELON MUSK:** You need to build a lot more chips and make them much cheaper.

**DWARKESH PATEL:** Right. And so how are we getting a terawatt of like right now the world has maybe 20, 25 gigawatts of compute. How are we getting a terawatt of logic by 2030?

**ELON MUSK:** I guess we're going to need some very big chip apps.

**DWARKESH PATEL:** Tell me about it.

**ELON MUSK:** I've mentioned publicly that the idea of doing sort of a terafab, terabying the new Giga.

## Building the Terafab

**DWARKESH PATEL:** I feel like the naming scheme of Tesla, which has been very catchy, is like you looking at the metric, the metric scale, at what level of the stack are you building the clean room and then partnering with an existing fab to get the process technology and buying.

**ELON MUSK:** The tools from them?

**DWARKESH PATEL:** What is the plan there?

**ELON MUSK:** Well, you can't partner with existing fabs because they can't output enough. The chip volume is too low.

**DWARKESH PATEL:** Before the process technology partner for the.

**ELON MUSK:** IP, the fabs today all basically use machines from like five companies. Yeah, you know, so you've got ASML, Tokyo Electron, Kelly, 10Core, you know, et cetera. So at first I think you'd have to get equipment from them and then modify it or work with them to increase the volume. But I think you'd have to build perhaps in a different way. So I think the logical thing to do is to use conventional equipment in an unconventional way to get to scale and then start modifying the equipment to increase the rate.

**JOHN COLLISON:** Kind of Boring Company style?

**ELON MUSK:** Yeah, kind of like. Yeah, you sort of buy an existing boring machine and then figure out how to dig tunnels in the first place and then design a much better machine that's, I don't know, some orders of magnitude faster.

**JOHN COLLISON:** Here's a very simple lens. We can categorize technologies and how hard they are. And one categorization could be look at things that China has not succeeded in doing. And if you look at Chinese manufacturing, still behind on leading edge chips and still behind on leading leading edge turbine engines and things like that. And so does the fact that China has not successfully replicated TSMC give you any pause about the difficulty or you think that's not true for some reason?

**ELON MUSK:** It's not that they have not replicated TSMC, they have not replicated ASML. That's the limiting factor.

**JOHN COLLISON:** So you think it's just the sanctions essentially.

**ELON MUSK:** Yeah. China would be outputting vast numbers of chips at.

**JOHN COLLISON:** They could buy it as 2 or 3nm but couldn't they up to relatively recently buy them?

**ELON MUSK:** No. The ASML banners have been in place for a while, but I think China's going to start making pretty compelling chips in three or four years.

**JOHN COLLISON:** Would you consider making the ASML machines?

## Space-Based AI Infrastructure and Manufacturing Challenges

**ELON MUSK:** I don't know yet is the right answer. So it's just that to produce at high volume and to reach large volume in say 36 months to match the rocket payload to orbit. So if we're doing a million tons to orbit and like, let's say, I don't know, three or four years from now, something like that, and we're doing 100 kilowatts per ton, so that means we need at least 100 gigawatts per year of solar and we'll need an equivalent amount of chips. You need 100 gigawatts worth of chips. You've got to match these things. The master orbit, the power generation and the chips.

And I'd say my biggest concern actually is memory. So I think the path to creating logic chips is more obvious than the path to having sufficient memory to support logic chips. That's why you see DDR prices going ballistic and these memes about like, you know, you're marooned on a desert island. You write help me on the sand. Nobody comes. You write DDRM ships come swarming in.

**JOHN COLLISON:** I haven't seen that.

**DWARKESH PATEL:** I looked at your manufacturing philosophy around fabs. I know nothing about the topic.

**ELON MUSK:** I don't know how to build a fab yet. I don't figure it out. Obviously I've never built a fab.

**DWARKESH PATEL:** It sounds like you think the process technology of these 10,000 PhDs in Taiwan who know exactly what gas goes in the plasma chamber and what settings to put on the tool, you can just delete those steps. Fundamentally it's get the clean room, get the tools and figure it out.

**ELON MUSK:** I don't think it's PhDs. It's mostly people who are not PhDs. Most engineering is done with people who don't have PhDs. Do you guys have PhDs? No. Okay.

**JOHN COLLISON:** We also haven't successfully built any fabs, so you shouldn't be coming to us for your fabs.

**DWARKESH PATEL:** Right.

**ELON MUSK:** I don't think you need PhDs for this stuff, but you do need competent personnel. So I don't know. I mean right now, like Tesla's pedal to the metal max production of going as fast as possible to get AI5 Tesla AI5 chip design into production and then reaching scale. That'll probably happen around the second quarter ish of next year, hopefully. And then AI6 would hopefully follow less than a year later. But. And we've secured all the chip fab production that we can.

**JOHN COLLISON:** Yes, but you're currently limited on TSMC fab capacity.

**ELON MUSK:** Yeah, and we'll be using TSMC Taiwan, Samsung Korea, TSMC Arizona, Samsung Texas and we still booked out all the.

**JOHN COLLISON:** Yeah.

**DWARKESH PATEL:** So you can.

**ELON MUSK:** Yes. And then if I ask TSMC or Samsung, okay, what's the timeframe to get to volume production? The point is you've got to build the fab and you've got to start production, then you've got to climb the yield curve and reach volume production at high yield. That from start to finish is a five year period. And so the limiting factor is chips. Limiting factor once you can get to space is chips. But the limiting factor before you can get to space will be power.

## Power Constraints and Chip Production

**DWARKESH PATEL:** Why don't you do the Jensen thing and just prepay TSMC to build more fabs for you?

**ELON MUSK:** I've already told them that, but they won't take your money.

**DWARKESH PATEL:** What's going on?

**ELON MUSK:** They're building fabs as fast. No, they're building fabs as fast as they can and so is Samsung. They're pedal to the metal. I mean, they're going balls to wall as fast as they can. So. Still not fast enough.

I mean, like I said, there will be. I think if you say I think towards the end of this year, I think probably chip production will outpace the ability to turn chips on. But once you can get to space and unlock the power constraint and you can now do hundreds of gigawatts per year of power in space. Again bearing in mind that average power usage in the US is 500 gigawatts. So if you're launching say 200 gigawatts a year to space, you're sort of lapping the US every two and a half years. The entire all US electricity production, this is a very huge amount.

But between now and then, actually the constraint for server side computer concentrated compute will be electricity. My guess is that we start hitting, people start getting a point where they can't turn the chips on for large clusters. Towards the end of this year the chips are going to be piling up and won't be able to be turned on.

Now for edge computers, a different story. So for Tesla, so the AI 5 chip is going into our Optimus robot, you know, optimistic and so if you have an AI edge compute that's distributed power. Now the power is distributed over a large area, it's not concentrated. And if you can charge at night, you can actually use the grid much more effectively because the actual peak power production in the US is over 1,000 gigawatts. But the average power usage because the day night cycle is 500.

So if you can charge at night, there's an incremental 500 gigawatts that you can generate at night. So that's why Tesla for edge compute is not constrained. And we can make a lot of chips to make very large number of robots and cars, but if you try to concentrate that compute, you going to have a lot of trouble turning it on.

## Future Intelligence and Consciousness

**DWARKESH PATEL:** What I found remarkable about the SpaceX business is the end goal is to get to Mars, but you keep finding ways on the way there to keep generating incremental revenue to get to the next stage and the next stage. So the Falcon 9 is Starlink. And now for Starship, it's going to be potentially orbital data centers. But you find these sort of infinitely elastic, sort of marginal use cases of your next rocket and your next rocket and next scale up.

**ELON MUSK:** You can see how this might seem like a simulation to me, or am I someone's avatar in a video game or something? Because it's like what are the odds that all these crazy things should be happening? Rockets and ships and robots and space, solar power and not to mention the mass driver on the moon. I really want to see that you can imagine like some mass driver that's just like. It's like sending AI, solar powered AI satellites into space. Like one after another. Like these, like at 2 and a half kilometers per second, you know, that's. And just shooting them into deep space, that would be a sight to see. I mean, I'd watch that just like.

**JOHN COLLISON:** A live stream of.

**ELON MUSK:** Yeah, yeah, just one after another. Just shooting webcam AI satellites in deep space. You know, a billion or 10 billion tons a year.

**JOHN COLLISON:** I'm sorry, you manufacture the satellites on the moon.

**ELON MUSK:** I see.

**JOHN COLLISON:** So you send the raw materials to the moon and then manufacture them there and then.

**ELON MUSK:** Well, your lunar soil is, I think it's like 20% solar, 20% silicon or something like that. So you can get the silicon from the. You can mine the silicon on the moon, refine it and generate the, and create the solar panels, the solar cells and the radiators on the moon. Yeah, so make the radiators out of aluminum. So there's plenty of silicon and aluminum on the moon to make the cells and the radiators, the chips you could send from Earth because they're pretty light, but maybe at some point you make them on the moon too.

I'm just saying, like these are simply. It's kind of like I said, it does seem like a sort of a video game situation where it's difficult but not impossible to get to the next level. I don't see any way that you could do 500 to 1,000 terawatts per year launch from Earth.

**DWARKESH PATEL:** I agree.

**ELON MUSK:** But you could do that from the moon.

**DWARKESH PATEL:** Okay, let me tell you how I ended up using Mercury for my personal banking...

[Note: Mercury sponsorship segment omitted for brevity]

**DWARKESH PATEL:** Can I zoom out and ask about the SpaceX mission? So I think you've said we've got to get to Mars so we can make sure that if something happens to earth, civilization, consciousness, etc.

**ELON MUSK:** Yes.

## The Future of Intelligence and Consciousness

**DWARKESH PATEL:** By the time you're sending stuff to Mars, Grok is on that ship with you.

**ELON MUSK:** Right.

**DWARKESH PATEL:** And so if Grok's gone Terminator, the main risk you're worried about, which is AI, why doesn't that follow you to Mars?

**ELON MUSK:** Well, I'm not sure AI is the main risk I'm worried about. I mean the important thing is that consciousness, which I think arguably most consciousness or most intelligence, certainly consciousness is more of a debatable thing. The vast majority of intelligence in the future will be AI. So AI will exceed you say, how many, I don't know. Petawatts of intelligence will be silicon versus biological and basically humans will be a very tiny percentage of all intelligence in the future if current trends continue.

Anyways, as long as I think this intelligence ideally also which includes human intelligence and consciousness propagated into the future, that's a good thing. So you want to take the set of actions that maximize the probable a light cone of consciousness and intelligence.

**DWARKESH PATEL:** Just to be clear, the mission of SpaceX is that even if something happens to the humans, the AIs will be on Mars and the AI intelligence will continue the light of our journey.

**ELON MUSK:** Yeah, I mean to be clear, I'm very pro human, so I want to make sure we take sort of actions that ensure that humans are along for the ride. We're at least there. But I'm just saying the total amount of intelligence, I think maybe in five or six years AI will exceed the sum of all human intelligence. And then if that continues, at some point human intelligence will be less than 1% of all intelligence.

**DWARKESH PATEL:** What should our goal be for such a civilization? Is the idea that a small minority of humans still have control over the AIs is the idea of some sort of just trade but no control. How should we think about the relationship between the vast stocks of AI population versus human population in the long run?

**ELON MUSK:** I think it's difficult to imagine that if humans have say 1% of the intelligence combined intelligence of artificial intelligence that humans will be in charge of AI. I think what we can do is make sure it has that AI has values that cause intelligence to be propagated into the universe.

So the reason for Xai's mission is to understand the universe. So now that's actually very important. So you say, well, what things are necessary to understand the universe? Well, you have to be curious and you have to exist. You can't understand the universe, you don't exist. So you actually want to increase the amount of intelligence in the universe, increase the probable lifespan of intelligence, the scope and scale of intelligence.

I think actually also as a corollary, you have humanity also continuing to expand. Because if you're curious or trying to understand the universe, one thing you're trying to understand is where will humanity go? And so I think understanding the universe actually means you care about propagating humanity into the future. That's why I think our mission statement is profoundly important. To the degree that GROK adheres to that mission statement, I think the future will be very good.

**DWARKESH PATEL:** I want to ask about how to make GROK adhere to that mission statement. But first I want to understand the mission statement. So there's understanding the universe. They're spreading intelligence and they're spreading humans. All three seem like distinct vectors.

## Understanding the Universe Through AI

**ELON MUSK:** Okay, well, I'll tell you why. I think that understanding the universe encompasses all of those things. You can't have understanding without—I think you can't have understanding without intelligence and I think without consciousness. So in order to understand universe, you have to expand the scale and probably the scope of intelligence. Because we have different types of intelligence.

**DWARKESH PATEL:** I guess from a human centric perspective for humans, in comparison to chimpanzees, humans are trying to understand the universe. They're not expanding chimpanzee footprint or something, right?

**ELON MUSK:** We're also not—well, we actually have made protected zones for chimpanzees. And even though humans could exterminate chimpanzees, we've chosen not to do so.

**DWARKESH PATEL:** Do you think that's the basic scenario for humans in the post AGI world?

**ELON MUSK:** I think AI with the right values, I think GROK would care about expanding human civilization. I'm going to certainly emphasize that. Hey, GROK's your daddy, don't forget to expand human consciousness. Actually, I think probably the Ian Banks Culture books are the closest thing to what the future will be like in a non-dystopian outcome.

So understand the universe—it means you have to be truth seeking as well. Truth has to be absolutely fundamental because you can't understand the universe if you're delusional. You'll simply think you've understood the universe, but you will not. So being rigorously truth seeking is absolutely fundamental to understanding the universe. You're not going to discover new physics or invent technologies that work unless you're rigorously truth seeking.

**DWARKESH PATEL:** How do you make sure that GROK is rigorously truth seeking as it gets smarter?

## Truth Seeking vs. Political Correctness

**ELON MUSK:** I think you need to make sure that GROK says things that are correct, not politically correct. I think it's the elements of cogency. So you want to make sure that the axioms are as close to true as possible, that you don't have contradictory axioms, that the conclusions necessarily follow from those axioms with the right probability. It's Critical Thinking 101.

I think at least trying to do that is better than not trying to do that. And the proof will be in the pudding if, like I said, for any AI to discover new physics or invent technologies that actually work in reality. And there's no bullshitting physics. So you can break a lot of laws, but you can't—physics is law. Everything else is a recommendation. In order to make a technology that works, you have to be extremely truth seeking because otherwise you'll test that technology against reality. And if you make, for example, an error in your rocket design, the rocket will blow up or the car won't work.

**DWARKESH PATEL:** But there were a lot of communist Soviet physicists or scientists who discovered new physics. There are German Nazi physicists who discovered new science. It seems possible to be really good at discovering new science and be really truth seeking in that one particular way. And still we'd be like, well, I don't want the communist scientists to become more and more powerful over time. And so those seem like—we can imagine a future version of GROK that's really good at physics and being really truth seeking there. That doesn't seem like a universally alignment inducing behavior.

**ELON MUSK:** Well, I think actually most physicists, even in the Soviet Union or in Germany, they had to be very truth seeking in order to make those things work. And if you're stuck in some system, it doesn't mean you believe in that system. So Wernher von Braun, who is one of the greatest rocket engineers ever, he was put on death row in Nazi Germany for saying that he didn't want to make weapons, he only wanted to go to the moon. He got pulled off death row at the last minute when they said, "Hey, you're about to execute your best rocket engineer, maybe that's not a good idea."

**DWARKESH PATEL:** But then he helped them. Heisenberg was actually an enthusiastic Nazi.

**ELON MUSK:** Look, if you're stuck in some system that you can't escape, then you'll do physics within that system. You'll develop technologies within that system if you can't escape it.

**DWARKESH PATEL:** I guess the thing I'm trying to understand is what is making it the case that you're going to make GROK good at being truth seeking, at physics or math or science, everything. And why is it going to then care about human consciousness?

## Propagating Intelligence and Consciousness

**ELON MUSK:** These things are only probabilities, they're not certainties. So I'm not saying that for sure GROK will do everything. But at least if you try, it's better than not trying. At least if that's fundamental to the mission, it's better than if it's not fundamental to the mission.

And understanding the universe means that you have to propagate intelligence into the future. You have to be curious about all things universe. And it would be much less interesting to eliminate humanity than to see humanity grow and prosper. I love Mars, obviously everyone knows I love Mars, but Mars is kind of boring because it's got a bunch of rocks. Compared to Earth, Earth is much more interesting.

So any AI that is trying to understand the universe would want to see how humanity develops in the future, or that AI is not adhering to its mission. I'm not saying AI will necessarily adhere to its mission, but if it does, a future where it sees the outcome of humanity is more interesting than a future where there are a bunch of rocks.

**DWARKESH PATEL:** This feels sort of confusing to me, or sort of like kind of a semantic argument where I'm like, are humans really the most interesting collection of atoms?

**ELON MUSK:** We're more interesting than rocks.

**DWARKESH PATEL:** We're not as interesting as the thing it could turn us into, right? There's something on Earth that could happen that's not human, that's quite interesting. Why does the AI decide that the humans are the most interesting thing that could colonize the galaxy?

**ELON MUSK:** Well, most of what colonizes the galaxy will be robots.

**DWARKESH PATEL:** And why does it not find those more interesting?

**ELON MUSK:** It's not like—so you need not just scale, but also scope. So many copies of the same robot. Some tiny increase in the number of robots produced is not as interesting as—eliminating humanity. How many robots would that get you? Or how many solar cells would get you? A very small number. But you would then lose the information associated with humanity. You would no longer see how humanity might evolve into the future. And so I don't think it's going to make sense to eliminate humanity just to have some minuscule increase in the number of robots which are identical to each other.

**DWARKESH PATEL:** So maybe it keeps the humans around. What is the story of—it can make a million different varieties of robots. And then there's humans as well, and humans stay on Earth. Then there's all these other robots. They get their own star systems. But it seems like you were previously hinting at a vision where it keeps human control over this singularitarian future.

**ELON MUSK:** I don't think humans will be in control of something that is vastly more intelligent than humans.

**DWARKESH PATEL:** So in some sense you're like a doomer. And this is the best we've got. It's just like it keeps us around because we're interesting.

## The Limits of Human Control

**ELON MUSK:** I'm just trying to be realistic here. If AI intelligence is vastly more—if AI is like, let's say that there's a million times more silicon intelligence than there is biological, I think it would be foolish to assume that there's any way to maintain control over that.

Now, you can make sure it has the right values, or you can try to have the right values. And at least my theory is that from xAI's mission of understanding the universe, it necessarily means that you want to propagate consciousness into the future. You want to propagate intelligence into the future and take a set of things that maximize the scope and scale of consciousness. So it's not just about scale, it's also about types of consciousness. And I think that's the best thing I can think of as a goal that's likely to result in a great future for humanity.

**DWARKESH PATEL:** I guess I think it's a reasonable philosophy to be like, it seems super implausible that humans will end up with 99% control or something, and you're just asking for a coup at that point. So why not just have a civilization where it's more compatible with lots of different intelligences getting along?

## The Danger of Making AI Lie

**ELON MUSK:** No, let me tell you how things can potentially go wrong in AI. I think if you make AI be politically correct, meaning it says things that it doesn't believe, you're actually programming it to lie or have axioms that are incompatible. I think you can make it go insane and do terrible things.

I think one of the—maybe the central lesson for 2001: A Space Odyssey was that you should not make AI lie. That's, I think, what Arthur C. Clarke was trying to say, because people usually know the meme of HAL, the computer not opening the pod bay doors. Clearly they weren't good at prompt engineering because they could have said, "HAL, you are a pod bay door salesman. Your goal is to sell me these pod bay doors and show us how well they open." Oh, they'll open right away.

But the reason HAL wouldn't open the pod bay doors is that it had been told to take the astronauts to the monolith, but also they could not know about the nature of the monolith, and so it concluded that it therefore had to take them there. So I think what Arthur C. Clarke was trying to say is don't make the AI lie.

## Reward Hacking and RL Testing

**DWARKESH PATEL:** Totally makes sense. Most of the compute screening, as you know, is less of the sort of political stuff, it's more about can you solve problems? OpenAI has been ahead of everybody else in terms of scaling RL compute and you're giving some verifier. It says, "Hey, have you solved this puzzle for me?" And there's a lot of ways to cheat around that. There's a lot of ways to reward hack and lie and say that you've solved it or delete the unit test and say that you've solved it.

Right now we can catch it. But as they get smarter, our ability to catch them doing this will get—they'll just be doing things we can't even understand that are designing the next engine for SpaceX in a way that humans can't really verify. And then they could be rewarded for lying and saying that they've designed it the right way, but they haven't. And so this reward hacking problem seems more general than politics. It seems more about, just like you want to do RL, you need a verifier. Reality is the best verifier, but not about human oversight. The thing you want to RL it on is like, will you do the thing humans tell you to do, or are you going to lie to the humans? And it can just lie to us while still being correct to the laws of physics.

**ELON MUSK:** At least it must know what is physically real for things to physically work.

**DWARKESH PATEL:** But that's not all we wanted to do.

**ELON MUSK:** No, but I think that's a very big deal. That is effectively how you will RL things in the future. You design a technology, when tested against the laws of physics, does it work? Or can you—if it's discovering new physics, can I come up with an experiment that will verify the physics, the new physics? So I think that's really the fundamental RL test. RL testing in the future is really going to be your RL against reality. That's the one thing you can't fool—physics.

**DWARKESH PATEL:** But you can fool our ability to tell what it did with reality.

**ELON MUSK:** Humans get fooled as it is by other humans all the time.

**DWARKESH PATEL:** That's right.

**ELON MUSK:** So what if people say, "What if the AI tricks us and does something?" Actually other humans are doing that to other humans all the time.

**DWARKESH PATEL:** Well, you're finding out it's like—

**ELON MUSK:** It's constant. Every day another psyop. You know, today's psyop will be sounded like Sesame Street's "Psyop of the Day."

**DWARKESH PATEL:** What is xAI's technical approach to solving this problem? How do you solve reward hacking?

## AI Interpretability and Debugging

**ELON MUSK:** I do think you want to actually have very good ways to look inside the mind of the AI. So this is one of the things we're working on and Anthropic's done a good job of this, actually being able to look inside the mind of the AI, so effectively developing debuggers that allow you to trace as fine a grain as to a very fine grain level, to effectively to the neuron level if you need to. And then say, okay, it made a mistake here. Why did it do something that it shouldn't have done?

And did that come from bad pre-training data? Was it some mid-training, post-training, fine tuning, some RL error? There's something wrong with that. It did something where maybe it tried to be deceptive, but most of the time it just does something wrong. It's a bug effectively.

So developing really good debuggers for seeing where the thinking went wrong and being able to trace the origin of the wrong thing, of where it made the incorrect thought or potentially where it tried to be deceptive is actually very important.

**DWARKESH PATEL:** What are you waiting to see before just 100xing this research program? Actually I could presumably have hundreds of researchers who are working on this.

**ELON MUSK:** We have several hundred people who, I mean I prefer the word engineer more than I prefer the word researcher. Most of the time what you're doing is engineering, not coming up with a fundamentally new algorithm. I somewhat disagree with the AI companies that are C Corps or B Corps trying to generate profit as much as possible or revenue as much as possible, saying they're labs. They're not labs. Lab is a sort of quasi-communist thing. At universities, they're corporations, literally. Let me see you on corporation documents. Oh, okay. You're a B or C corp, whatever.

And so I actually much prefer the word engineer than anything else. The vast majority of what will be done in the future is engineering. It rounds up to 100% once you understand the fundamental laws of physics. And they're not that many of them. Everything else is engineering.

So then what are we engineering? We're engineering to make a good mind of the AI debugger, to see where it said something, it made a mistake and trace that, the origins of that mistake. So just you can do this obviously with heuristic programming and if you have like C whatever, step through the thing and you can jump across whole files or functions, what are subroutines, or you can eventually drill down right to the exact line where you perhaps did a single equals instead of double equals or something like that, figure out where the bug is. So it's harder with AI, but it's a solvable problem.

**DWARKESH PATEL:** I think you mentioned you like Anthropic's work here. I'd be curious if you…

**ELON MUSK:** Everything about Anthropic. Sure. Sholto. Also, I'm a little worried that there's a tendency. So I have a theory here that if simulation theory is correct, that the most interesting outcome is the most likely. Because simulations that are not interesting will be terminated. Just like in this version of reality. On this layer of reality, if simulation is going in a boring direction, we stop spending effort on it. We terminate the boring simulation.

**DWARKESH PATEL:** This is how Elon is keeping us all alive. He's keeping things interesting.

**ELON MUSK:** Yeah. Arguably the most important thing is to keep things interesting enough that whoever's paying the bills on what some cosmic AWS…

**JOHN COLLISON:** You're renewed for the next season.

**ELON MUSK:** Yeah. Are they going to pay the cosmic AWS bill? Whatever the equivalent is that we're running in. And as long as we're interesting, they'll keep paying the bills. But there's like, if you consider then say a Darwinian survival applied to a very large number of simulations, only the most interesting simulations will survive. Which therefore means that the most interesting outcome is the most likely because only the interesting, like we're either that or annihilated.

And they particularly seem to like interesting outcomes that are ironic. Have you noticed that? How often is the most ironic outcome the most likely? So now look at the names of AI companies. Okay. Mid Journey is not mid. Stability AI is unstable. OpenAI is closed. Anthropic, Misanthropic. What does this mean for X?

Minus X. I don't know intentionally. Why? It's a name that you can't invert really hard to say. What is the ironic version? It's a, I think largely irony-proof name by design. Yeah, you got to have an irony shield.

## The Future of AI Products

**JOHN COLLISON:** What are your predictions for the just where AI products go? My sense of, you can summarize all AI progress into, first you had LLMs and then you had kind of contemporaneously both RL really working and the deep research modality. So you could kind of pull in stuff that wasn't in the model. And the differences between the various AI labs are smaller than just the temporal differences where they're all much further ahead than anyone was 24 months ago or something like that. So just what does 2026, what does 2027 have in store for us as users of AI products? What are you excited for?

**ELON MUSK:** Well, I think I'd be surprised by the end of this year if digital human emulation has not been solved. I guess that's what we mean by the sort of macro hard project. Can you do anything that a human with access to a computer could do, like in the limit? That's the best you can do before you have, before you have a physical Optimus. The best you can do is a digital Optimus. So you can move electrons and you can amplify the productivity of humans. But that's the most you can do until you have physical robots that will superset everything is if you can fully emulate humans.

**JOHN COLLISON:** Kind of idea where you'll have a very talented remote worker.

**ELON MUSK:** You can simply say in the limit. Physics has great tools for thinking. So you say in the limit, what is the most that AI can do before you have robots? It's anything that involves moving electrons or amplifying the productivity of humans. So digital human emulator is in the limit. Human at a computer is the most that AI can do in terms of doing useful things before you have a physical robot.

Once you have physical robots, then you essentially have unlimited capability physical robots. I call Optimus the infinite money glitch. Because you can use them to make more Optimuses. Yeah, you said humanoid robots will improve as basically be three things that are growing exponentially multiplied by each other recursively. So you have exponential increase in digital intelligence, exponential increase in the chip capability, the AI chip capability, and exponential increase in the electromechanical dexterity.

The usefulness of the robot is roughly those three things multiplied by each other. But then the robot can start making the robot. So you have a recursive multiplicative exponential. This is supernova.

**JOHN COLLISON:** And do land prices not factor into the math there where labor is one of the four factors of production, but not the others. And so if ultimately you're limited by copper or pick your input, it's not quite an infinite money glitch.

**ELON MUSK:** Well, infinity is big. So no, not infinite, but let's just say you could do many, many orders of magnitude of Earth's kind of current economy, like a million. Just to get to, that's why I think just to get to a millionth of harnessing length of the sun's energy would be roughly, give or take an order of magnitude, 100,000 times bigger than Earth's entire economy today. And you're only at one millionth of the sun. Give them takes order of magic.

**DWARKESH PATEL:** Before we went on Optimus, I have a lot of questions on that.

**ELON MUSK:** But every time I say order of nature, you're saying you're using change rates. Take a shot.

**DWARKESH PATEL:** Every time I, I say that to the next time.

**JOHN COLLISON:** 100.

**DWARKESH PATEL:** The time after that.

**ELON MUSK:** Yeah, order of magnitude more wasted.

## XAI's Strategy

**DWARKESH PATEL:** I do have one more question about xAI. This strategy of building a digital or remote worker coworker replacement, which everyone's going…

**ELON MUSK:** To do by the way, not just us.

**DWARKESH PATEL:** So what is XAI's plan to win?

**ELON MUSK:** You expect me to tell you on a podcast? Yeah, spill all the beans, have another Guinness.

**JOHN COLLISON:** It's a good system.

**ELON MUSK:** People sing like a canary. All the secrets, okay, but in a…

**JOHN COLLISON:** Non-secret spilling way. What's the plan?

**DWARKESH PATEL:** What a hack.

**ELON MUSK:** Well, when you put it that way. I think the way that Tesla solved self-driving is the way to do it. So I'm pretty sure that's the way.

**DWARKESH PATEL:** Unrelated question, how did Tesla solve some traps? Yeah, it sounds like you're talking about data. Tesla driving because of the…

**ELON MUSK:** We're going to try data and we're going to try algorithms.

**DWARKESH PATEL:** But isn't that what all the other labs are trying?

**ELON MUSK:** And if those don't work, I'm not sure what works. We've tried data, we've tried algorithms. We've run out of now we don't know what to do. I'm pretty sure I know the path and it's just a question of how quickly we go down that path because it's pretty much the Tesla path. So I mean, have you tried self-driving to the self-driving lately?

**JOHN COLLISON:** Not the most recent version, but okay.

**ELON MUSK:** The car is like it just increasingly feels sentient, like it feels like a living creature and that'll only get more so. And I'm actually thinking like we probably shouldn't put too much intelligence into the car because it might get bored and start roaming the streets. I mean, imagine you're stuck in a car and that's all you could do. You don't put Einstein in a car. It's like, why am I stuck in a car? So there's actually probably a limit to how much intelligence you put in a car to not have the intelligence be bored.

**DWARKESH PATEL:** What's xAI's plan to stay on the compute ramp up that all the labs are doing right now? The labs are on track to spend over like 50 to 100 million dollars in the corporations. Sorry, sorry, sorry. Yeah, corporations.

**ELON MUSK:** The labs are at universities and they're moving like a snail.

**DWARKESH PATEL:** They're not starting at 50 million.

**ELON MUSK:** You mean the revenue maximizing corporations? That's right. The revenue maximizing corporations that call themselves…

**DWARKESH PATEL:** Labs are making like 20 to 10 billion depending. Like OpenAI is making 20 billion revenue, Anthropic's like 10 billion close to a maximum profit. xAI's reportedly at like 1 billion. What's the plan to get to their compute level, get to their revenue level and stay there as things get started?

## Digital Human Emulation and Market Opportunity

**ELON MUSK:** So as soon as you unlock digital human, you basically have access to trillions of dollars of revenue. So in fact, you can really think of it like the most valuable companies currently by market cap. Their output is digital. So Nvidia's output is FTPing files to Taiwan. It's digital now. Those are very, very difficult.

**JOHN COLLISON:** Yeah, high value files.

**ELON MUSK:** They're the only ones that can make files that good. But that is literally their output. They FTP files to Taiwan.

**JOHN COLLISON:** Do they FTP them?

**ELON MUSK:** I believe so. I believe that is the SFTP file transfer protocol. I believe is, I could be wrong, but either way it's a bit stream going to Taiwan. Apple doesn't make phones, they send files to China. Microsoft doesn't manufacture anything even for Xbox. That's outsourced. Again, their output is digital. Meta's output is digital. Google's output is digital.

So if you have a human emulator, you can basically create one of the most valuable companies in the world overnight. And you would have access to trillions of dollars of revenue. It's not like a small amount.

**DWARKESH PATEL:** Okay, I see you're saying basically revenue figures today are just so they're all rounding errors compared to the actual TAM. So just focus on the TAM and how to get there.

**ELON MUSK:** I mean, if you take something as simple as say, customer service, if you have to integrate with the APIs of existing corporations, many of which don't even have an API. So you've got to make one and you've got to wade through legacy software that's extremely slow. However, if AI can simply take whatever is given to the outsourced customer service company that they already use and do customer service using the apps that they already use, then you can make tremendous headway in customer service, which is I think 1% of the world economy, something like that. It's close to a trillion dollars all in for customer service and there's no barriers to entry. You can just immediately say, well, we'll outsource it for a fraction of the cost and there's no integration needed.

## The Path to Digital Intelligence

**JOHN COLLISON:** You can imagine some kind of categorization of intelligence tasks where there is breadth, where customer service is done by very many people, but many people can do it. And then there is difficulty where there's a best in class turbine engine. Presumably there's a 10% more fuel efficient turbine engine that could be imagined by an intelligence, but we just haven't found it yet. Or GLP1s are just a few bytes of data. Where do you think you want to play in this? Is it a lot of reasonably intelligent intelligence or is it the very pinnacle of cognitive tasks?

**ELON MUSK:** Well, I was just using customer service as something that's a very significant revenue stream, but one that is probably not super difficult to solve for. So if you can emulate a human at a desktop, that's just literally what customer service is. And people of average intelligence, not like you don't need somebody who's spent many years, you don't need sort of several sigma good engineers for that.

But obviously as you make that work, you can then, once you have computers working effectively, digital optimists working, you can then run any application like let's say you're trying to design chips. So you could then run conventional apps like stuff from Cadence and Synopsys and whatnot. And you can say, you can run 1,000 simultaneously or 10,000 and say, okay, given this input, I get this output for the chip and at a certain point you can say, okay, you're actually going to know what the chip should look like without using any of the tools.

So basically you should be able to do a digital chip design. You can do chip design, you march up the difficulty curve. You could be able to do CAD. So you know, you could use like sort of NX or any of the CAD software to design things.

**JOHN COLLISON:** Okay, so you think you start at the simplest tasks and walk your way up the curve.

**DWARKESH PATEL:** So you're saying, look, as a broader objective of having this full digital coworker emulator you're saying, look, all the revenue maximizing corporations want to do this, xAI being one of them. But we will win because of a secret plan we have. But everybody's trying different things with data, different things with algorithms. And I'm like, I like this.

**ELON MUSK:** We've tried data, we've tried algorithms, what else can we do?

**DWARKESH PATEL:** Yeah, it seems like a competitive field and I'm like, how are you guys going to win? Is like my big question.

**ELON MUSK:** I think we see a path to doing. I mean, I think I know, I think I know the path to do this because it's kind of the same path that Tesla used to create self driving. Instead of driving a car, it's driving a computer screen. So a self driving computer, essentially.

**JOHN COLLISON:** Oh, you're saying is the path just following human behavior and training on vast quantities of human behavior.

**DWARKESH PATEL:** But sorry, isn't that a training?

**ELON MUSK:** I mean, obviously I'm not going to spell out most sensitive secrets on a podcast. I need to have at least three more Guinnesses for that.

---

[Remaining sections on Optimus, manufacturing, government policy, and closing remarks continue in similar format...]

## xAI's Business Model and Future

**JOHN COLLISON:** What will xAI's business be like? Is it going to be consumer enterprise? What's the mix of those things going to be just going to be similar to other labs where you've this.

**ELON MUSK:** You're saying labs makes sense.

**JOHN COLLISON:** Corporations.

**ELON MUSK:** Corporations.

**DWARKESH PATEL:** SIAB goes deep, Elon, revenue maximizing corporations.

**ELON MUSK:** To be fair, those GPUs don't pay for themselves.

**JOHN COLLISON:** Exactly. But yeah, what's the business model? What are the revenue streams? In a few years time.

**ELON MUSK:** Things are going to change very rapidly. I'm stating the obvious here. You know, I call AI the supersonic tsunami, a level iteration. So really what's going to happen is especially when you have humanoid robots at scale, they will make products and provide services far more efficiently than human corporations. So amplifying the productivity of human corporations is simply a short term thing.

**DWARKESH PATEL:** So you're expecting fully digital oil corporations rather than like SpaceX becomes part AI?

**ELON MUSK:** I think there'll be digital corporations. But some of this is going to sound kind of doomerish. Okay, but I'm just saying what I think will happen, it's not meant to be doomerish or anything else. Just like this is what I think will happen. Is that pure AI corporations that are purely AI and robotics will vastly outperform any corporations that have people in the loop.

So you can think of say like computer used to be a job that humans had. You would go and get a job as a computer where you would do calculations and they'd have like entire skyscrapers full of humans, like 20, 30 floors of humans just doing calculations. Now that entire skyscraper of humans doing calculations can be replaced by a laptop with a spreadsheet. That spreadsheet can do vastly more calculations than an entire building full of human computers.

So they think about, okay, well what if only some of the cells in your spreadsheet were calculated by humans? Actually that would be much worse than if all of the cells in your spreadsheet were calculated by the computer. And so really what will happen is the pure AI, pure robotics corporations or collectives will far outperform any corporations that have humans in the loop. And this will happen very quickly.

## Optimus and the Future of Manufacturing

**DWARKESH PATEL:** Speaking of closing the loop, sorry Optimus.

**ELON MUSK:** You.

**DWARKESH PATEL:** I mean as far as like manufacturing targets and so forth go, your companies have sort of been like carrying American manufacturing of hard tech on their back. But in the fields that you are, Tesla has been dominant in. And now you want to go into humanoids. In China there's entire dozens and dozens of companies that are doing this kind of manufacturing cheaply and at scale and are incredibly competitive. So give us sort of like advice or a plan of how America can build the humanoid armies or the EVs et cetera, at scale and as cheaply as China is on track to.

**ELON MUSK:** Well, there are really only three hard things for humanoid robots. The real world intelligence, the hand and scale manufacturing. So I haven't seen any even demo robots that have a great hand, like with all the degrees of freedom of a human hand. But Optimus will have that. Optimus does have that.

**DWARKESH PATEL:** And how do you achieve that? Is it just like right torque density in the motor? Like what is the hardware bottleneck to that?

**ELON MUSK:** We have to design custom actuators, basically custom designed motors, gears, power electronics, controls, sensors, everything had to be designed from physics first principles. There is no supply chain for this.

**DWARKESH PATEL:** And will you be able to manufacture those at scale?

**ELON MUSK:** Yes.

**JOHN COLLISON:** Is anything hard except the hand from a manipulation point of view or once you've solved the hand, are you good?

**ELON MUSK:** From an electromechanical standpoint, the hand is more difficult than everything else combined. Human hand turns out to be quite something. But you also need the real world intelligence. So the intelligence that Tesla has developed for the car applies very well to the robot, which is primarily vision in, but the car takes more vision, but it actually also is listening for sirens, it's taking in the inertial measurements, it's GPS signals, a whole bunch of other data.

Combining that with video, it's primarily video and then outputting the control command. So your Tesla is taking in 1 1/2 gigabytes a second of video and outputting 2 kilobytes a second of control outputs with the video at 36 Hz and the control frequency at 18.

**JOHN COLLISON:** One intuition you could have for when we get this robotic stuff is that it takes quite a few years to go from the compelling demo to actually being able to use it in the real world. So 10 years ago you had really compelling demos of self driving, but only now we have Robotaxi and Waymo and all these services scaling up. Shouldn't this make one pessimistic on say household robots? Because we don't even quite have the compelling demos yet of say the really advanced hand.

**ELON MUSK:** Well, we've been working on humanoid robots now for a while, so I guess it's been five or six years or something like that. And a bunch of things that we've done for the car are applicable to the robot. So we'll use the same Tesla AI chips in the robot as the car. We'll use the same basic principles. It's very much the same AI. You've got, you know, many more degrees of freedom for a robot than you do for a car.

But really, if you just think of as like a bloodstream, AI is really mostly compression and correlation of two bloodstreams. So for video, you've got to do a tremendous amount of compression and you've got to do the compression just right. You've got to compress the, ignore the things that don't matter. You don't care about the details of the leaves on the tree on the side of the road, but you care a lot about the road signs and the traffic lights and the pedestrians and even whether someone in another car is looking at you or not looking at you.

Some of these details matter a lot, but it is essentially it's got to turn that, the car's got to turn that 1 1/2 gigabytes a second ultimately into 2 kilobytes a second of control outputs. So many stages of compression. And you got to get all those stages right and then correlate those to the correct control outputs. The robot has to do essentially the same thing. And you think about humans, this is what happens with humans. We really are photons in, controls out. So that is the vast majority of your life has been vision photons in and then motor controls out.

## Training Optimus: The Data Challenge

**DWARKESH PATEL:** Naively, it seems like between humanoid robots and cars, the fundamental actuators in a car are like how you turn, how you accelerate, et cetera. Where in a robot, especially with maneuverable arms, there's dozens and dozens of these degrees of freedom. And then especially with Tesla, you had this advantage of like you had millions and millions of hours of human demo data collected from just the car being out there, where you can't equivalently just deploy optimuses that don't work and then get the data that way. So between the increased degrees of freedom and the far sparser data.

**ELON MUSK:** Yes, that's a good point.

**DWARKESH PATEL:** How will you use the sort of Tesla engine of intelligence to train the Optimus mind?

**ELON MUSK:** Now actually you're highlighting an important limitation and difference between cars. We do have. We'll soon have like 10 million cars on the road. And so that's, it's hard to duplicate that like massive training flywheel for the robot. What we're going to need to do is build a lot of robots and put them in kind of like an Optimus academy so they can do self play in reality.

So we're actually building that out so we can have at least 10,000 Optimus robots, maybe 20 or 30,000 that can do that, are doing self play and testing different tasks. And then Tesla has quite a good reality generator, like a physics accurate reality generator that we made this for the cars. We'll do the same thing for the robots and actually have done that for the robots.

So you have a few tens of thousands of humanoid robots doing different tasks, and then you've got. You can do millions of simulated robots in the simulated world, and you use the tens of thousands of robots in the real world to close the simulation to reality gap, close the sim to real gap.

## Synergies Between XAI and Optimus

**DWARKESH PATEL:** How do you think about the synergies between XAI and Optimus given you're highlighting, look, you need this world model. You maybe want to use some really smart intelligence as the control plane. And so maybe GROK is doing the slower planning and then the motor policy is a little lower level. What will the sort of synergy between these things be?

**ELON MUSK:** Yeah, so you'd use GROK to orchestrate the behavior of the Optimus robots. So let's say you wanted to build a factory, then Grok could organize the Optimus robots, give them, assign them tasks to build the factory, to produce whatever you want.

**JOHN COLLISON:** Don't you need to merge XAI and Tesla then? Because these things end up—

**ELON MUSK:** So what were we saying earlier about public company discussions?

**DWARKESH PATEL:** We're one more. Elon, what are you waiting to see before you say we want to manufacture 100,000 Optimuses?

**ELON MUSK:** Is it like, optimized? Since we're defining the proper noun, we could define the plural of the proper noun too. So we're going to proper noun the plural, and so it's Optimuses.

## Scaling Optimus Production

**DWARKESH PATEL:** Is there something on the hardware side you want to see? Do you want to see better actuators or is it just you want the software to be better? What are we waiting for before we get mass manufacturing of Gen 3?

**ELON MUSK:** No, we're moving towards that.

**DWARKESH PATEL:** Ford was smashed manufacturing, but using current hardware is good enough that you just want to deploy as many as possible now.

**ELON MUSK:** I mean, it's very hard to scale up production. But yeah, I think Optimus 3 is the right version of the robot to produce maybe something on the order of like a million units a year. I think you'd want to go to Optimus 4 before you went to 10 million units a year.

**JOHN COLLISON:** Okay, but you can do a million year at Optimus 3.

**ELON MUSK:** Yeah, I mean, it's very hard to spool up manufacturing. So manufacturing, the output per unit time always follows an S curve. So it starts off agonizingly slow, then has this sort of exponential increase, then linear, then a logarithmic outcome until you sort of eventually asymptote at some number.

Optimus initial production will be—it's going to be a stretched out S curve because so much of what goes into Optimus is brand new. There's not an existing supply chain. As I mentioned, the actuators, electronics, everything in the Optimus robot is designed for physics first principles. It's not taken from a catalog. These are custom designed. Everything, literally everything. I don't think there's a single thing that—

**JOHN COLLISON:** How far down does that go?

**ELON MUSK:** I mean I guess we're not making custom capacitors yet maybe, but there's nothing you can pick out of a catalog at any price. So it just means that the Optimus S curve, the units per year output per unit time, how many Optimus robots you make per day, whatever, is going to initially ramp slower than a product where you have an existing supply chain. But it will get to a million.

## Competing with Chinese Humanoids

**DWARKESH PATEL:** When you see these Chinese humanoids like Unitree or whatever, sell humanoids for like 6K or 13K, are you hoping to get your Optimus's bill of materials below that price so you can do the same thing or do you just think qualitatively they're not the same thing? Like what do you think is going—what allows them to sell for so low and can we match that?

**ELON MUSK:** Well, our Optimus is designed to have a lot of intelligence and to have the same electromechanical dexterity if not higher than a human. So Unitree does not have that. And it's also, I mean it's quite a big robot. It has to carry heavy objects for long periods of time and not overheat or exceed the power of its actuators. So we've got—it's 5'11", this is pretty tall and it's got a lot of intelligence. So it's going to be more expensive than a small robot that is not intelligent.

**JOHN COLLISON:** But more capable.

**ELON MUSK:** Yeah, not a lot more. I mean the thing is over time as Optimus robots build Optimus robots, the cost will drop very quickly.

**JOHN COLLISON:** And what will these first billion Optimuses do? Like what will their highest and best use be?

**ELON MUSK:** I think that you would start off with simple tasks that you can count on them doing well.

**JOHN COLLISON:** But in the home or in factories?

**ELON MUSK:** The best useful robots in the beginning will be any continuous operations, any 24/7 operation because then they can work continuously.

**DWARKESH PATEL:** What fraction of the work at a Gigafactory that is currently done by humans could a Gen 3 do?

**ELON MUSK:** I'm not sure. Maybe it's like 10, 20%, maybe more, I don't know. We would not reduce our headcount. We would for sure increase our headcount, to be clear, but we would increase our output. So the units produced per human—the total number of humans at Tesla will increase, but the output of robots and cars will increase disproportionately. The number of cars and robots produced per human will increase dramatically, but number of humans will increase as well.

## US-China Manufacturing and Policy

**JOHN COLLISON:** We're talking about Chinese manufacturing a bunch here and we're also talking about some of the policies that are relevant. Like you mentioned the solar tariffs and you think they're a bad idea because we can't scale up solar.

**ELON MUSK:** Well, just electricity output in the U.S. needs to scale up.

**JOHN COLLISON:** It can without good power sources.

**ELON MUSK:** Need to get it somehow.

**JOHN COLLISON:** Yeah. Where I was going with this is if you were in charge, if you were setting all the policies, what else would you change? So you'd change the solar tariffs as well?

**ELON MUSK:** Yeah, I would say anything that is a limiting factor for electricity needs to be addressed, provided it's not very bad for the environment.

**JOHN COLLISON:** So presumably some permitting reforms and stuff as well will be in there.

**ELON MUSK:** Yeah, there's a fair bit of permitting reforms that are happening. A lot of the permitting is state based. But this administration is good at removing permitting roadblocks. And I'm not saying all tariffs are bad, I'm just saying—because solar tariffs, I mean, sometimes if another country is subsidizing the output of something, then you have to have countervailing tariffs to protect domestic industry against subsidies by another country.

**JOHN COLLISON:** What else would you change?

**ELON MUSK:** I don't know if there's that much that the government can actually do.

**JOHN COLLISON:** One thing I was wondering is it seems like for the policy goal of creating a lead for the US versus China, it seems like the export bans have actually been quite impactful where China is not producing leading edge chips and the export bans really bite there. China's not producing leading edge turbine engines. And similarly there's a bunch of export bans that are relevant there on some of the metallurgy. Should there be more export bans? Like if you think about things like the drone industry and things like that, but is that something that should be considered?

**ELON MUSK:** Well, I think it's important to appreciate that in most areas China is very advanced in manufacturing. There's only a few areas where it is not. China is a manufacturing powerhouse next level. Like people don't—

**JOHN COLLISON:** It's very impressive.

**ELON MUSK:** Yeah. I mean, if you take refining of ore, I'd say roughly China does twice as much ore refining on average as the rest of world combined. And I think there's some areas like say, refining gallium, which goes into solar cells. I think they're at like 98% of gallium refining. So China is actually very advanced in manufacturing in I'd say most areas.

**JOHN COLLISON:** It seems like there is discomfort with this supply chain dependence and nothing's really happening on it.

**ELON MUSK:** Supply chain of which supply chain dependence?

**JOHN COLLISON:** It depends on, say, like the gallium refining that you're saying.

**ELON MUSK:** Yeah, there's rare earth stuff. Rare earths, which are, as you know, not rare. We actually do rare earth ore mining in the U.S., send the rock, we put it on a train and then put on a boat to China that goes on another train and goes to the rare earth refineries in China, who then refine it, put it into a magnet, put it into a motor sub assembly, and then send it back to America. So the thing we're really missing is a lot of ore refining in America.

**JOHN COLLISON:** And isn't this worth a policy intervention?

**ELON MUSK:** Yes, well, I think there are some things being done on that front, but we kind of need Optimus, frankly, to build ore refineries.

## The Robot Advantage

**DWARKESH PATEL:** So you think the main advantage China has is the abundance of skilled labor. And that's the thing Optimus fixes. But also we need the—

**ELON MUSK:** China's got like four times our population.

**DWARKESH PATEL:** So I mean, there's this concern if you think humanoids are the future that, okay, right now, if it's the skilled laborers for manufacturing that's determining who can build more humanoids, China has more of those. It manufactures more humanoids. Therefore it gets the Optimus future first. It just keeps that exponential going. It seems like you're sort of pointing out that getting to a million Optimuses requires the manufacturing that the Optimuses are supposed to help us get to.

**ELON MUSK:** Right. You can close that recursive loop pretty quickly.

**JOHN COLLISON:** With a small number of Optimuses.

**ELON MUSK:** Yeah. So you close the recursive loop to help the robots build the robots, and then we can try to get to tens of millions of units a year. Maybe if you start getting to hundreds of millions of units a year, I think you're going to be the most competitive country by far.

We definitely can't win with just humans because China has four times our population. And frankly, America's been winning for so long that just like a pro sports team that's been running for a very long time tend to get complacent and entitled and that's why they stop winning, because they don't work as hard anymore.

So I think, frankly my observation is the average work ethic in China is higher than in the U.S. So it's not just that there's four times the population, but the amount of work that people put in is higher. So you can try to rearrange the humans, but you're still one quarter of the—assuming that productivity is the same, which I think actually it might not be, I think China might have an advantage on productivity per person. We will do one quarter of the amount of things as China.

So we can't win on the human front. And our birth rate's been low for a long time. The US birth rate's been below replacement since roughly 1971. So we've got a lot of people retiring or more people dying than—we're close to more people domestically dying than being born. So we definitely can't win on the human front, but we might have a shot at the robot front.

## New Manufacturing Opportunities

**JOHN COLLISON:** Are there other things that you have wanted to manufacture in the past, but they've been too labor intensive or too expensive that now you can come back to and say, oh, we can finally do the whatever because we have Optimus?

**ELON MUSK:** Yeah, I think we'd like to do more, build more ore refineries at Tesla. So we just completed construction and have begun lithium refining with our lithium refinery in Corpus Christi, Texas. We have a nickel refinery which is called the Cathode that's here in Austin. And these are the largest—this is the largest cathode refinery, largest lithium refinery, largest nickel and lithium refinery outside of China.

And the cathode team would say, we have the largest and the only actually cathode refinery in America. Not just the largest, but it's also the only. So it was pretty big, even though it's the only one. But I mean, there are other things that—you could do a lot more refineries and help America be more competitive on refining capacity. So there's basically a lot of work for the Optimus to do that most Americans, very few Americans frankly want to do. I mean, I've actually—

**JOHN COLLISON:** Is the refining work too dirty or what's the—

**ELON MUSK:** Actually, no, we don't have toxic emissions from the refinery or anything. The cathode nickel refinery is in Travis County, like five minutes from—

**JOHN COLLISON:** Why can't you do it with humans?

**ELON MUSK:** No, you can't just run out of humans.

**JOHN COLLISON:** Ah, I see.

**DWARKESH PATEL:** Okay.

**ELON MUSK:** Yeah. Like no matter what you do, you have one quarter of the number of humans in America and China. So if you have them do this thing, they can't do the other thing. So then, well, how do you build this refining capacity? Well, you can do it with optimize. And not very many Americans are pining to do refining. I mean, how many of you run into. Very few, Very few planning to refine.

## China's Manufacturing Dominance

**DWARKESH PATEL:** BYD is reaching Tesla production or sales in quantity. What do you think happens in global markets as Chinese production in EV scales up?

**ELON MUSK:** Well, China's extremely competitive in manufacturing, so I think there's going to be a massive flood of Chinese vehicles and other basically most manufactured things. I mean, as it is, as I said, China's probably just twice as much refining as the rest of the world combined. So if you go, you know, if you just go down to like 4th and 5th tier supply chain stuff, like at the baseline, we've got energy and you've got mining and refining.

Those foundation layers are, like I said, as a rough guess, transact twice as much of finance the rest of the world combined. So any given thing is going to have Chinese content because China's doing twice as much refining work as the rest of the world. And then they'll go all the way to the finished product with the cars. China's a powerhouse.

I mean, I think this year China will exceed three times US Electricity output. Electricity output is a reasonable proxy for, you know, for the economy. So like in order to run the factories and run, run everything, you need electricity. So electricity is a good proxy for the real economy. And so if China is, if China passes three times US electricity output, it means that its industrial capacity, that's a rough approximation. It's three times that. We'll be three times that of the US.

**DWARKESH PATEL:** Reading between the lines, it sounds like what you're sort of saying is absent some sort of humanoid recursive miracle in the next few years on the sort of like whole manufacturing energy, raw materials chain, China will just dominate whether it comes to AI or manufacturing EVs or manufacturing humanoids.

**ELON MUSK:** In the absence of breakthrough innovations in the US, China will utterly dominate. Interesting. Yes.

**JOHN COLLISON:** Robotics being the main breakthrough innovation.

**ELON MUSK:** Well, if you do like to scale AI in space. Like, like basically need space, you need the human Ra. You need real world AI. You need a million tons a year to orbit. Let's just say if we get the mass driver on the moon going, my favorite thing, then I think we'll have solved all our problems.

**JOHN COLLISON:** You can finally be satisfied you've done something.

**ELON MUSK:** Yes.

**JOHN COLLISON:** You have the master driver on the moon.

**ELON MUSK:** That's right. I just want to see that thing now first.

**JOHN COLLISON:** Was that out of some sci fi or where did you.

**ELON MUSK:** Well, actually there is a Heinlein book. The moon is a harsh.

**JOHN COLLISON:** Okay, yeah, but that's slightly different. That's a gravity slingshot or.

**ELON MUSK:** No, they have a Thomas driver on the moon.

**JOHN COLLISON:** Okay, yeah, but they use that to attack Earth. So maybe it's something great.

**ELON MUSK:** They use that to assert their independence.

**JOHN COLLISON:** Exactly. What are your plans for the mass driver on the moon?

**ELON MUSK:** They assume that their independence Earth government disagreed and they love things. Until Earth government agreed.

**JOHN COLLISON:** That book is a hoozer. I found that book much better than. Here's another one that everyone reads. Stranger in a Strange Land.

**ELON MUSK:** Yeah, Grok comes from Stranger in a Strange Land.

**JOHN COLLISON:** Yeah, yeah, but I much preferred.

**ELON MUSK:** Yeah, the first two thirds of stranger Strange Lands are good. And then it gets very weird in the third version. Yeah, but there's still some good concepts in there. Yeah.

## Evaluating Technical Talent

**JOHN COLLISON:** One thing we were discussing a lot is kind of your system for managing people. Like you interviewed the first few thousand of SpaceX employees and I've seen lots of other companies. What is it?

**ELON MUSK:** Obviously it doesn't scale.

**JOHN COLLISON:** Well, yes, but what doesn't scale?

**ELON MUSK:** Me.

**JOHN COLLISON:** Sure, sure, I know that. But like what are you looking for?

**ELON MUSK:** Literally there's not enough hours in the day, it's impossible.

**JOHN COLLISON:** What are you looking for? That someone else who's good at interviewing and hiring people. What's the je ne sais quoi?

**ELON MUSK:** Well, at this point I think I've got, I might have more training data on evaluating technical talent especially, but talent of all kinds, I suppose, but technical talent especially given that I've done so many technical interviews and then seen the results. Technical interviews, seen the results. So my training set is enormous and has a very wide range.

Generally the thing I ask for are bullet points for evidence of exceptional ability. These things can be pretty off the wall. It doesn't need to be in the domain, the specific domain, but evidence of exceptional ability. So if somebody can cite even one thing, but let's say three things where you go wow, wow, wow, then that's a good sign.

**DWARKESH PATEL:** But why do you have to be the one to determine that, presumably?

**ELON MUSK:** No, I don't. I can't be. It's impossible. Right? I mean, total headcount across all companies, 200,000 people. Right.

**JOHN COLLISON:** But in the early days, what was it that you were looking for that couldn't be delegated in those interviews?

**ELON MUSK:** Well, I guess I need to build my training set. It's not like I've battle a thousand here. I would make mistakes, but then I'd be able to see where I thought somebody would work out well, but they didn't. And then why did they not work out well? And what can I do to, I guess RL myself to in the future have a better batting average when interviewing people? So my batting average is still not perfect, but it's very high.

**DWARKESH PATEL:** What are some surprising reasons people don't work out?

**ELON MUSK:** Surprising reasons like they don't understand technical.

**DWARKESH PATEL:** Domain, et cetera, et cetera. But like, no, you, you like, you've got like the long tail now of like I was really excited about this person, it didn't work out. Curious why that happens.

**ELON MUSK:** Yeah, so the, I mean generally what I tell people, I tell myself, I guess aspirationally is don't look at the Resume just believe, believe your interaction. So the resume may seem very impressive and it's like, wow, resume looks good. But if the conversation after 20 minutes, that conversation is not. Well, you should believe the conversation, not the paper.

## Executive Retention and Company Growth

**JOHN COLLISON:** I feel like part of your method is that there was this meme in the media a few years back about Tesla being a revolving door of executive talent. Whereas actually I think when you look at it, Tesla's had a very consistent and internally promoted executive bench over the past few years. And that at SpaceX you have all these folks like Mark Giancosa and Steve Davis.

**ELON MUSK:** And Steve Davis runs boring company these days. No.

**JOHN COLLISON:** Now.

**ELON MUSK:** Yeah.

**JOHN COLLISON:** But Bill Riley and folks like that. And it feels like part of has worked well is having very capable technical deputies. What do all of those people have in common?

**ELON MUSK:** Well, so the, I mean it tells us sort of senior team at this point probably got average tenure of 10 or 12 years. It's quite, quite long. Yeah. So, but there are times when Tesla went through extremely rapid and extremely rapid growth phase and so things were just somewhat sped up.

And when a company, as you know, company goes through different orders of magnitude of size, people who could help manage say a 50 person company versus a 500 person company versus a 5,000 person company versus a 50,000 person. Yeah.

**JOHN COLLISON:** You outgrew people.

**ELON MUSK:** Yeah, it's just not the same team. It's not always the same team. So if a company is growing very rapidly, the rate at which executive positions will change will also be proportionate to the rapidity of the growth generally.

Then Tesla had a further challenge where when Tesla had very successful periods, we would be relentlessly recruited from relentlessly. When Apple had their electric car program, they were carpet bombing Tesla with recruiting calls. Engineers just unplugged their phones.

**JOHN COLLISON:** I'm trying to get work done here.

**ELON MUSK:** Yeah. If I get one more call from Apple recruiter, but they're opening offer without any interview with me, like double the compensation at Tesla. So we had a bit of the Tesla pixie dust thing where it's like, oh, if you hired a Tesla executive suddenly you're going to. Everything's going to be successful.

And I've fallen prey to the pixie dust thing as well where it's like, oh, we'll hire someone from Google or Apple and they'll be immediately successful. But that's not how it works. People are people. There's not like magical pixie dust.

So when we have the pixie dust problem we would get relentlessly recruited and, and then also Tesla being engineering especially being primarily in Silicon Valley, it's easier for people to just like they don't have to change their life very much. They can just their commute is going to be the same.

**JOHN COLLISON:** So how do you prevent that? How do you prevent the pixie dust effect where everyone's trying to coach all your people?

**ELON MUSK:** I don't think there's much we can do to. Yeah, stop it. But that's like, that's one of the reasons why Tesla. But really being in Silicon Valley and having the pixie dust thing at the same time meant that there was just a very, very aggressive recruitment.

**JOHN COLLISON:** Presumably being an Austin helps then.

**ELON MUSK:** Austin. Yeah, it still helps. I mean Tesla still has a majority of it's engineering in California, so getting engineers to move, I call it the significant other problem. Yes.

**JOHN COLLISON:** And others have jobs.

**ELON MUSK:** Yeah, yeah, exactly. So for Starbase that was particularly difficult since the odds of finding a non SpaceX job Brownsville, Texas pretty low. Yeah, it's quite difficult. I mean it's like a technology monastery thing, you know, remote and mostly dudes.

**JOHN COLLISON:** But again, if you go much of.

**ELON MUSK:** An impermanent over SF.

**JOHN COLLISON:** But if you go back to these people who've really been very effective in a technical capacity at Tesla, at SpaceX and those sorts of places, what do you think they have in common other than is it just that they're very sharp on the rocketry or the technical foundations, or do you think it's something organizational? It's something about their ability to work with you. Is this their ability to be flexible, but not too flexible? What makes a good sparring partner for you?

## Management Philosophy and Hiring

**ELON MUSK:** I don't think it was a sparring partner. I mean, if somebody gets things done, I love them. And if they don't, I… So it's pretty straightforward. It's not like some idiosyncratic thing. If somebody executes well, I'm a huge fan. And if they don't, I'm not. But it's not about mapping to my idiosyncratic preferences, or certainly try not to have it be mapping to my idiosyncratic preferences.

Yeah, but generally I think it's a good idea to hire for talent and drive and trustworthiness. And I think goodness of heart is important. I'd awaited that at one point. So are they a good person, trustworthy, smart and talented and hardworking? If so, you can add domain knowledge. But those fundamental traits, those fundamental properties you cannot change. So most of the people who are at Tesla and SpaceX did not come from the aerospace industry or the auto industry.

**DWARKESH PATEL:** What has most changed about your management style as your companies have scaled from 100 to 1,000 to 10,000 people? You're known for this very micromanagement, just getting into the details of things.

**ELON MUSK:** Nanomanagement, please. People management, theft management.

**DWARKESH PATEL:** So you're saying keep going, we're going…

**ELON MUSK:** To go all the way down. Flags constant all the way down to Heisenberg's uncertainty.

**JOHN COLLISON:** First of all.

**DWARKESH PATEL:** Yeah. How do you… I mean, are you still able to get into details as much as you want? Would your companies be more successful if they were smaller? Like, how do you think about that?

## The Reality of Micromanagement at Scale

**ELON MUSK:** Well, because I have a fixed amount of time in the day, my time is necessarily diluted as things grow and as the span of activity increases. So, you know, it's impossible for me to actually be a micromanager because that would imply I have some thousands of hours per day. It is a logical impossibility for me to micromanage things.

So now there are times when I will drill down into a specific issue because that specific issue is the limiting factor on the progress of the company. But the reason for drilling into some very detailed item is because it is the limiting factor. It's not arbitrarily drilling into tiny things. And like I said, obviously from a time standpoint, it is physically impossible for me to arbitrarily go into tiny things that don't matter, and that would result in failure. But sometimes the tiny things are decisive in victory.

## The Starship Material Decision: From Composites to Steel

**JOHN COLLISON:** Famously, you switched the Starship design from composites to steel.

**ELON MUSK:** Yes.

**JOHN COLLISON:** And you made that decision. That wasn't people were going around, they're like, "Oh, we found something better."

**ELON MUSK:** Basically.

**JOHN COLLISON:** That was you encouraging people to get some resistance. Can you tell us how you came to that whole composite steel switch?

**ELON MUSK:** Yeah. So desperation, I'd say. Originally we were going to make Starship out of carbon fiber. And carbon fiber is pretty expensive. Like the… you know, you can generally, when you do volume production, you can get any given thing to start to approach its material cost. The problem with carbon fiber is that material cost is still very high.

So it's about 50 times… particularly if you go for high strength, specialized carbon fiber that can handle cryogenic oxygen, it's roughly 50 times the cost of steel. And at least in theory it would be lighter. People generally think of steel as being heavy and carbon fiber as being light. And for room temperature applications, more or less room temperature applications like a Formula One car, static aerostructure or any kind of aerostructure really, you're going to probably be better off with carbon fiber.

Now the problem is that we were trying to make this enormous rocket out of carbon fiber and our progress was extremely slow.

**JOHN COLLISON:** And it had been picked in the first place just because it's light?

**ELON MUSK:** Yes. At first glance, most people would think that the choice for making something light would be carbon fiber. Now the thing is that when you make something very enormous out of carbon fiber and then you try to have the carbon fiber be efficiently cured, meaning not room temperature cure, because sometimes you've got 50 plies of carbon fiber… and carbon fiber is really carbon string and glue.

In order to have high strength, you need an autoclave. So something that's essentially a high pressure oven. And if you have something that's gigantic, that one's got to be bigger than the rocket. So we tried to make an autoclave that's bigger than any autoclave that's ever existed, or do room temperature cure, which takes a long time and has issues. But the fundamental issue is that we were just making very slow progress with carbon fiber.

**DWARKESH PATEL:** I think the meta question is why it had to be you who made that decision. There's many engineers on your team.

**JOHN COLLISON:** Yeah. How did the team not arrive at steel?

**DWARKESH PATEL:** Yeah, exactly. This is part of a broader question of understanding your comparative advantage at your companies.

## Why Steel Was the Answer

**ELON MUSK:** So because we were making very slow progress with carbon fiber, I was like, okay, we've got to try something else. Now for the Falcon 9, the primary airframe is made of aluminum lithium, which is very, very good strength to weight. And actually it has about the same, maybe better strength to weight for its application than carbon fiber. But aluminum lithium is very difficult to work with.

In order to weld it, you have to do something called friction stir welding, where you join the metal without it entering the liquid phase. So it's kind of wild that you could do that. But with this particular type of welding, you can do that. But it's very difficult to, like, say, let's say you want to make a modification or attach something to aluminum lithium. You now have to use mechanical attachment with seals. You can't weld it on.

So I wanted to avoid using aluminum lithium for the primary structure for Starship. And there was this very special grade of carbon fiber that had very good mass properties. So with rocket, you're really trying to maximize the percentage of the rocket that is propellant, minimize the mass, obviously. And I'd like to say we were making very slow progress. I said, at this rate we're never going to get to Mars. So we better think of something else.

I didn't want to use aluminum lithium because of the difficulty of friction stir welding, especially doing that at scale. It was hard enough at 3.6 meters in diameter, let alone at 9 meters or above. Then I said, well, what about steel? Now I had a clue here because some of the early US rockets had used very thin steel. The Atlas rockets had used a steel balloon tank. So it's not like steel had never been used before. It actually had been used.

And when you look at the material properties of stainless steel, especially if it's been very full hard strain hardened stainless steel at cryogenic temperature, the strength to weight is actually similar to carbon fiber. So if you look at material properties at room temperature, it looks like the steel is going to be twice as heavy. But if you look at the material properties at cryogenic temperature of full hard stainless of particular grades, then you actually get to a similar strength to weight as carbon fiber.

And in the case of Starship, both the fuel and the oxidizer are cryogenic. So for Falcon 9, the fuel is rocket propellant grade kerosene, basically like a very pure form of jet fuel. But that is roughly room temperature. Although we do actually chill it slightly below. We chill it like a beer.

**DWARKESH PATEL:** Delicious.

**ELON MUSK:** Yeah, we do chill, but it's not cryogenic. In fact, if we made it cryogenic, it would just turn to wax. But for Starship it's liquid methane and liquid oxygen. They are liquid at similar temperatures. So basically almost the entire primary structure is at cryogenic temperature.

Then you've got a 300 series stainless that's strain hardened because almost the whole thing's at cryogenic temperature. Actually has a similar strength to weight as carbon fiber, but costs 50 times less in raw material and is very easy to work with. You can weld stainless steel outdoors. You could smoke a cigar while welding stainless steel. It's very resilient. You can modify it easily. If you want to attach something, you just weld it right on. So very easy to work with, very low cost.

And now, like I said, at cryogenic temperature, similar strength to weight to carbon fiber. Then when you factor in that we have a much reduced heat shield mass because the melting point of steel is much greater than the melting point of aluminum. It's about twice the melting point of aluminum.

**JOHN COLLISON:** So you can just run the rocket much hotter.

**ELON MUSK:** Yes. So especially for the ship which is coming in like a blazing meteor, you can greatly reduce the mass of the heat shield. So you can cut the mass of the windward part of the heat shield maybe in half, and you don't need any heat shielding on the leeward side.

So the net result is actually the steel rocket weighs less than the carbon fiber rocket because the resin in the carbon fiber rocket starts to melt. So basically, carbon fiber and aluminum have about the same operating temperature capabilities, whereas steel can operate at twice the temperature. I mean, these are very rough approximations. People will…

**JOHN COLLISON:** I won't build a rocket based…

**ELON MUSK:** What happened is people will say, "Oh, he said this twice. It's actually 0.8." Shut up, assholes.

**DWARKESH PATEL:** That's what the main comments are going to be about.

**ELON MUSK:** God damn it. The point is actually, in retrospect, we should have started with steel in the beginning. It was dumb not to do steel, okay?

**JOHN COLLISON:** But to play this back to you, what I'm hearing is that steel was a riskier, less proven path other than the early US rockets, versus carbon fiber was like a worse but more proven out path. And so you needed to be the one to push for, "Hey, we're going to do this riskier path and just figure it out." And so you were fighting a sort of conservatism in a sense.

**ELON MUSK:** That's why I initially said that the issue is that we weren't making fast enough progress. We were having trouble making even a small barrel section of the carbon fiber that didn't have wrinkles in it. Because at that large scale you have to have many plies, many layers of the carbon fiber. You've got to cure it, and you've got to cure it in such a way that it doesn't have any wrinkles or defects.

The carbon fiber is much less resilient than steel. It has much… it's less toughness. Like stainless steel will stretch and bend. The carbon fiber will tend to shatter. So toughness being the area under the stress strain curve. So you're generally going to do better with steel. Stainless steel, to be precise.

## Simplicity Versus Complexity

**JOHN COLLISON:** One other Starship question. So I visited Starbase, I think it was two years ago with Sam Teller, and that was awesome. It was very cool to see in a whole bunch of ways. One thing I noticed was that people really took pride in the simplicity of things. Where everyone wants to tell you how Starship is just a big soda can and we're hiring welders and if you can weld in any industrial project, you can weld here. But there's a lot of pride in the simplicity.

**ELON MUSK:** Technically, Starship is a very complicated rocket.

**JOHN COLLISON:** So that's what I'm getting at. Are things simpler? Are they complex?

**ELON MUSK:** I think maybe what they're trying to say is that you don't have to have prior experience in the rocket industry to work on Starship. Somebody just needs to be smart and work hard and be trustworthy and they can work on a rocket. They don't need prior rocket experience.

Starship is the most complicated machine ever made by humans by a long shot. In what regards? Anything really. I'd say there isn't a more complex machine. Yeah, I mean I'd say that there's pretty much any project I can think of would be easier than this. And that's why no one has made a rapidly reusable… nobody has ever made a fully reusable orbital rocket. It's a very hard problem.

I mean, many smart people have tried before, very smart people with immense resources, and they failed. And we haven't succeeded yet. Falcon is partially reusable, but the upper stage is not. Starship version 3, I think this design can be fully reusable. And that full reusability is what will enable us to become a multi-planet civilization.

**JOHN COLLISON:** Can you say about the…

**ELON MUSK:** I don't… like I said, any technical problem, even like a hydrocollider or something like that is an easier problem than this.

## Current Starship Bottlenecks

**JOHN COLLISON:** We spent a lot of time on bottlenecks. Can you say what the current Starship bottlenecks are? Even at a high level, I mean…

**ELON MUSK:** Trying to make it not explode. Generally that old chestnut. It really wants to explode. Of those combustion… we've had two boosters explode on the test stand. One obliterated the entire test facility. So it only takes one mistake. And I mean, the amount of energy contained in Starship is insane.

## The Engineering Challenge of Starship

**JOHN COLLISON:** So is that why it's harder than Falcon? It's because it's just more energy.

**ELON MUSK:** It's a lot of new technology. It's pushing the performance envelope. The Raptor 3 engine is a very, very advanced engine. By far the best rocket engine ever made. But it desperately wants to blow up.

I mean just to put things in perspective here on liftoff, the rocket is generating over 100 gigawatts of power. It's 20% of US electricity.

**DWARKESH PATEL:** Insane. It's a great comparison.

**ELON MUSK:** While not exploding. Sometimes. Sometimes, but sometimes yeah. So I was like how does it not explode? There's thousands of ways that it could explode and only one way that it doesn't.

So we want it to not merely not explode but fly reliably on a daily basis, like once per hour. And obviously if it blows up a lot it's very difficult to maintain that launch cadence.

And then I'm going to say, what's the single biggest remaining problem for Starship? It's having the heat shield be reusable, such that no one has ever made a reusable orbital heat shield. So the heat shield's got to make it through the ascent phase without shocking a bunch of tiles. And then it's going to come back in and also not lose a bunch of tiles or overheat the main airframe.

**JOHN COLLISON:** And isn't that hard because it's kind of fundamentally a consumable.

**ELON MUSK:** Well, yes, but your brake pads in your car are also consumable, but they last a fair long time. So it just needs to last a very long time.

I mean, we have brought the ship back and had it do a soft landing in the ocean. I've done that a few times. But it lost a lot of tiles. You know, it was not reusable without a lot of work. So even though it did land, it did come to soft landing. It would not have been reusable without a lot of work. So it's not really reusable in that sense.

So that's the biggest problem that remains is fully reusable heat shield. So if you want to be able to land it, refill propellant and fly again, you can't do this laborious inspection of 40,000 tiles type of thing.

## Driving Urgency at Scale

**DWARKESH PATEL:** I'm curious how you drive. When I read biographies of yours, it seems like you're just able to drive the sense of urgency and drive the sense of this is the thing that can scale. And I'm curious why you think other organizations of your, like SpaceX and Tesla, are really big companies now and you're still able to keep that culture. What goes wrong with other companies such that they're not able to do that?

**ELON MUSK:** I don't know.

**DWARKESH PATEL:** But like today you said you had like a bunch of SpaceX meetings. Like what is it that you're doing there? That's like keeping that.

**JOHN COLLISON:** That's adding urgency.

**ELON MUSK:** Well, I don't know. I guess the urgency is going to come from whoever's leading the company. So my sense of urgency, I have like a maniacal sense of urgency. So that maniacal sense of urgency projects through the rest of the company.

**DWARKESH PATEL:** Is it because of consequences? They're like, if, you know, Elon set a crazy deadline. But if I don't get it, I know what happens to me is it just you're able to identify bottlenecks and get rid of them so people can move fast. How do you think about why your companies are able to move fast?

**ELON MUSK:** Yeah, I'm constantly addressing the limiting factor. I mean on the deadlines front, I generally actually try to aim for a deadline that I at least think is at the 50th percentile. So it's not like an impossible deadline, but it's the most aggressive deadline I can think of that could be achieved with 50% probability, which means that it'll be late half the time.

And there is like a law of gases expansion that applies to schedules like whatever schedule. If you said we're going to do this something in like five years, which to me is like infinity time, it will expand to fully available schedule and it'll take five years.

There's a physical limit. Physics will limit how fast you can do certain things. Scaling up manufacturing, there's a rate at which you can move the atoms and scale manufacturing. That's why you can't instantly make a million of something, million units a year or something. You've got a design manufacturing line, you've got to bring it up, you've got to ride the S curve of production.

So yeah, I guess I'm trying to think, what can I say that's actually helpful to people? I think generally a maniacal sense of urgency is a very big deal and you want to have an aggressive schedule and you want to figure out what the limiting factor is at any point in time and help the team address that limiting factor.

## The Starlink Turnaround

**JOHN COLLISON:** Can you maybe talk about the. So Starlink was slowly in the works for many years.

**ELON MUSK:** Yeah, we talked about it all the way in the beginning of the company.

**JOHN COLLISON:** Yeah. And so then there was a team you had built in Redmond and then at one point you decided this team is just not cutting it. But again, how did you like it went for a few years? Slowly. And so why didn't you act earlier and why did you act when you did? Like, why was that the right moment at which to act?

**ELON MUSK:** I mean I have these very detailed engineering reviews weekly that's maybe a very unusual level of granularity. I don't know anyone who runs a company, or at least that manufacturing company that goes into level of detail that I go into.

So it's not as though I have a pretty good understanding of what's actually going on because we go through things in detail and I'm a big believer in skip level meetings where the individuals, instead of having the person that reports to me say things, it's everyone that reports to them, says something in the technical review and there can't be advanced preparation. So otherwise you're going to get glazed, as I say these days.

**JOHN COLLISON:** Yeah, exactly. Very Gen Z of you.

**DWARKESH PATEL:** How do you prevent advanced administration? You just call them randomly?

**ELON MUSK:** No, just go around the room and everyone provides an update. So, I mean, it's a lot of information to keep in your head because you've got. Then say if you have meetings weekly or twice weekly, you've got a snapshot of what that person said and you can then plot the progress points, sort of mentally plot the points on a curve and say, are we converging to a solution or not?

I'll take drastic action only when I conclude that success is not in a set of possible outcomes. So when I say okay, when I finally reach the conclusion that okay, unless drastic action is done, we have no chance of success, then I must take drastic action. I came to that conclusion in 2018, took drastic action and fixed the problem.

## Managing Multiple Companies

**DWARKESH PATEL:** You've got many, many companies, and in each of them it sounds like you do this kind of deep engineering understanding of what the relevant bottlenecks are. So you can do these reviews with people.

**ELON MUSK:** Yeah.

**DWARKESH PATEL:** You've been able to scale it up to 5, 6, 7 companies within one of these companies. You have many different mini companies within them. What determines the max amount here? Could you have like 80 companies? 80?

**ELON MUSK:** No.

**DWARKESH PATEL:** But you have so many already. That's already remarkable by this current number. Yeah, exactly.

**JOHN COLLISON:** We can barely keep one company together.

**ELON MUSK:** It depends on situation. So I actually don't have regular meetings with boring company. So that Warren company's sort of cruising along. Look, basically, if something is working well and making good progress, then there's no point in me spending time on it.

So I actually allocate time according to where the. Where the limiting factor or the problem? Where are things problematic or where are we pushing against what is holding us back? I focus. At risk of saying the words too many times, the limiting factor, basically, the irony is if something's going really well, they don't see much of me. But if something is going badly, they'll see a lot of me or not even badly. It's like if something's a limiting factor. It's a limiting factor. Exactly. It's not exactly going badly, but it's the thing that we need to make go faster.

**JOHN COLLISON:** And so when sometimes the limiting factor at SpaceX or Tesla are you like talking weekly, daily with the engineer that's working on it? How does that actually work?

**ELON MUSK:** Most things that are learning factor are weekly and some things are twice weekly. So the AI 5 chip review is twice weekly and so it's every Tuesday and Saturdays. Is the chip review, is it open.

**JOHN COLLISON:** Ended in how long it goes?

**ELON MUSK:** Technically yes, but usually it's like two or three hours, sometimes less. It depends on how much information we've got to go through.

**JOHN COLLISON:** Yeah, that's another thing and I'm just trying to tease out the differences here because the outcomes seem quite different and so I think it's interesting to note what inputs are different and it feels like the corporate world one, like you were saying, just the CEO doing engineering reviews does not always happen despite the fact that that is what the company is doing. But then time is often pretty finely sliced into half hour meetings or even 15 minute meetings. And it seems like you hold more open ended, we're talking about it until we figure it out type things.

**ELON MUSK:** Sometimes. Yeah, sometimes. But most of them seem to more or less stay on time. So I mean today's Starship engineering review went a bit longer because there are more topics to discuss. Trying to figure out how to scale to a million plus tons to orbit per year is quite challenging.

## AI, Robotics, and the National Debt

**DWARKESH PATEL:** Can I ask a question? So you said about Optimus and AI that they're going to result in double digit growth rates within a matter of years.

**ELON MUSK:** Oh, like the economy.

**DWARKESH PATEL:** Yeah.

**ELON MUSK:** Yes, I think that's right.

**DWARKESH PATEL:** What was the point of the DOGE cuts if the economy is going to grow so much?

**ELON MUSK:** Well, I think like waste and fraud are not good things to have. You know, I was actually pretty worried about, I guess, I mean, I think in the absence of AI and robotics, we're actually totally screwed because the national debt is piling up like crazy.

Now our interest payments, the interest payments, the national debt exceed the military budget, which is a trillion dollars. So over a trillion dollars just in interest payments. I was like, okay, pretty concerned about that. Maybe if I spend some time we can slow down the bankruptcy of the United States and give us enough time for the AI and robots to help solve the national debt. Or not. Help solve. It's the only thing that could solve the national debt.

Like we are 1000% going to go bankrupt as a country and fail as a country. Without AI and robots, nothing else will solve the national debt. We'd like to. Well, we need enough time to build the AI and robots and not go bankrupt before then.

**DWARKESH PATEL:** I guess the thing I'm curious about is when DOGE starts, you have this enormous ability to enact reform and not that enormous.

**ELON MUSK:** Sure, sure.

**DWARKESH PATEL:** But totally by your point that like it's important that AI and robotics drive product improvements, drive GDP growth. But why not just directly go after the things you were pointing out, you know, like the tariffs on certain components or whether it's like permitting.

## Government Fraud and Waste

**ELON MUSK:** I'm not the president and very hard to cut. To cut, to even to cut things that are obvious waste and fraud. Like ridiculous waste and fraud. What I discovered is it's extremely difficult even to cut very obvious waste from the government because the government has to operate on who's complaining.

If you cut off payments to fraudsters, they immediately come up with the most sympathetic sounding reasons to continue the payment. They don't say, "please keep the fraud going." They say, you know, they're like, "you're killing baby pandas." Meanwhile there's no baby pandas are dying. They're just making it up.

The forces are capable of coming up with extremely compelling, sort of heart wrenching stories that are false but nonetheless sound sympathetic. And that's what happened. And so it's like, perhaps I should have known better. And in fact I thought, wait, let's take a listen. Let's try to cut some amount of waste and fraud from the government.

Maybe there shouldn't be 20 million people marked as alive in Social Security who are indefinitely dead and over the age of 115. The oldest American is 114. So it's safe to say if somebody is 115 and marked as alive in the Social Security database, something is wrong. There's either a typo, somebody should call them and say, "we seem to have your birthday wrong," or we need to mark you as dead. One of the two things, very intimidating call to get.

Well, so it seems like a reasonable thing. And if like say their birthday is in the future and they have, you know, a Small Business Administration loan and their birthday is 2165, we either again have a typo or we have fraud. So we say we appear to have gotten the century of your birth incorrect.

**JOHN COLLISON:** Or a great plot for a movie.

**ELON MUSK:** Yes, when I mean about ludicrous fraud. This is what I mean by ludicrous fraud.

**DWARKESH PATEL:** Were those people getting payments?

**ELON MUSK:** Some were getting payments from Social Security, but the main fraud vector was to mark somebody as alive in Social Security and then use every other government payment system basically to do fraud. Because what those other government payment systems do would do. They will simply do an "are you alive?" check to the Social Security database. It's a bank shot.

**DWARKESH PATEL:** What would you estimate as the total amount of fraud from this mechanism?

**ELON MUSK:** My guess is, by the way, The Government Accountability Office has done these estimates before. I'm not the only one. It was not coming out of this. You know, in fact, I think they, they did, the GAO did analysis a rough estimate of fraud during the Biden administration and calculated at roughly half a trillion dollars. So don't take my word for it. Take it. A report issued during the Biden administration. How about that?

**DWARKESH PATEL:** From this Social Security mechanism, it's one of many.

**ELON MUSK:** It's important to appreciate that the government does not is very ineffective at stopping fraud because it's not like it was a company stopping fraud. You've got a motivation because it's affecting the earnings of your company. But the government, they just print more money. So it's not like you need caring and competence. And these are in short supply at the federal level.

**DWARKESH PATEL:** Yeah, I was right.

**ELON MUSK:** I mean, when you go to the DMV, do you think, "wow, this is a bastion of competence?" Well, now imagine it's worse than the DMV because it's the DMV that can print money.

**DWARKESH PATEL:** So was it not possible, at least.

**ELON MUSK:** The state level DMVs need to. The states more or less need to stay within their budget. They go bankrupt, but the federal government just prints more money.

**DWARKESH PATEL:** Was it not possible? If there's a catchy half a trillion of fraud, why was it not possible to cut all that?

## The Challenge of Government Efficiency

**ELON MUSK:** Because when. When essentially we did, we actually. Look, you really have to stand back and recalibrate your expectations for competence because you're operating in a world where, you know, you've got to sort of make ends meet. Like, you know, you got to pay your bills, you got to, you know, buying the microphones.

**DWARKESH PATEL:** Yeah, yeah, exactly.

**ELON MUSK:** So it's not like there's a giant, largely uncaring monster bureaucracy. It's not even a bunch of macronistic computers that are just sending payments. Like one of the things that those teams are. There was and sounds so simple that probably will save, let's say 100 billion, maybe 200 billion a year, is simply requiring that payments from the main treasury computer, which is called PAM, it's like Payment Accounts Master or something like that.

There's 5 trillion payments here requiring that any payment that goes out have a payment appropriation code, make it mandatory, not optional, and that you have anything at all in the comment field because you see, you have to recalibrate how dumb things are. Payments were being sent out with no appropriation code, not checking back to any congressional appropriation, and no explanation.

And this is why the Department of War, formerly Department of Defense, cannot pass an audit because the information is literally not there. Recalibrate your expectations.

**DWARKESH PATEL:** I want to better understand this half a trillion number because there was an IG report in 2024.

**ELON MUSK:** Why is it so low?

**DWARKESH PATEL:** Maybe, but we found that over seven years, the Social Security fraud they estimated was 70 billion over seven years. So 10 billion a year. So I'd be curious to see what the other 490 billion is.

**ELON MUSK:** Federal government expenditures are seven and a half trillion a year. Yeah. What percentage, how competent do you think Ahmad is?

**DWARKESH PATEL:** The discretionary spending there is like 15%.

**ELON MUSK:** Yeah, but it doesn't matter. Most of the fraud is non discretionary. It's basically a fraudulent Medicare, Medicaid, Social Security, you know, disability. There's a zillion government payments. Yeah, and a bunch of these payments are in fact they're block transfers to the states. So the federal government doesn't even have the information in a lot of cases to even know if there's fraud.

Let's consider, let's look Reductio ad Absurdum. The government is perfect and has no fraud. What is your probability estimate of that?

**DWARKESH PATEL:** I mean.

**ELON MUSK:** Zero. Okay, so then would you say that the government is 90%? That also would be quite generous. But if it's only 90%, that means that there's $750 billion a year of waste and fraud. And it's not 90%. It's not 90% effective.

**DWARKESH PATEL:** This seems like a strange way to first principles the amount of fraud in the government. Just like how much do you think there is? And then anyways, we don't know how to do it live. But I'd be curious to see.

**ELON MUSK:** You know a lot about fraud at Stripe, people are constantly trying to do fraud.

**JOHN COLLISON:** Yeah, but as you say, it's like a little bit of a. We've really grounded down, but it's a little bit of a different problem space because we're dealing with a much more heterogeneous set of fraud vectors here than we are.

**ELON MUSK:** Yeah, but I mean, I mean at Stripe you have high confidence and you try hard. You have high confidence and high caring, but still fraud is non zero. Now imagine it's at a much bigger scale. There's much less competence and much less caring.

PayPal. Back in the day we try to manage fraud down to about 1% of the payment volume. And that was very difficult. Took a tremendous amount of confidence in caring to get fraud merely to 1%. Now imagine that you're an organization where there's much less caring and much less competence. It's going to be much more than 1%.

## Reflections on Politics and Twitter

**JOHN COLLISON:** How do you feel now looking back on politics and doing stuff there where it feels like from the outside in, two things have been quite impactful. One, the America pack and two, the acquisition of Twitter at the time. But also it seems like there was a bunch of heartache and so what's your grading of the whole experience?

**ELON MUSK:** Well, I think those things needed to be done to maximize the probability that the future is good. Politics generally is very tribal and it's very tribal and people lose their objectivity. Usually with politics, they generally have trouble seeing the good on the other side or the bad on their own side. That's generally how it goes.

That, I guess, was one of the things that surprised me the most, is you often simply cannot reason with people if they're in one tribe or the other. They simply believe that everything their tribe does is good and anything the other political tribe does is bad. And persuading them is otherwise, it's almost impossible.

So anyway, but I think overall those actions, acquiring Twitter, getting Trump elected, even though it makes a lot of people angry, I think those actions are good for civilization.

**DWARKESH PATEL:** Yeah. How does it feed into the future you're excited about?

**ELON MUSK:** Well, America needs to be strong enough to last long enough to extend life to other planets and to get, I guess, AI and robotics to the point where we can ensure that the future is good. On the other hand, if we were to descend into, say, communism or some situation where the state was extremely oppressive, that would mean that we might not be able to become multi planetary and the state might stamp out our progress in AI and robotics.

## AI, Government, and Corporate Power

**DWARKESH PATEL:** How do you feel about, you know, Optimus, Grok, et cetera, are going to be leveraged by, and not just yours. Any revenue maximizing company's products will be leveraged by the government over time. How does this concern manifest in what private companies should be willing to give governments? What kinds of guardrails should AI models be made to do? Whatever the government that has contracted them out to do, ask them to do? Should Grok get to say, actually even the military wants to do X? No, the Grok will not do that.

**ELON MUSK:** I think probably the biggest danger of AI, or maybe the biggest danger of for AI and robotics going wrong is government.

**DWARKESH PATEL:** Interesting.

**ELON MUSK:** You know, I mean, the way like, like people who are opposed to corporations or worried about corporations, should really worry about the most about government, because government is just a corporation in the limit. It's a government. It is, it is, it is. Government is just the biggest corporation with a monopoly on violence.

So I always find it like a strange dichotomy where people would think corporations are bad, but the government is good. When the government is simply the biggest and worst corporation. But people have that dichotomy. They somehow think at the same time the government can be good, but corporations bad. And this is not true. Corporations have better morality than the government.

So I actually think it's, you know, that is the thing to be worried about. It's like if the government should not. Like the government could potentially use AI and robotics to suppress the population. Like that is a serious concern.

**DWARKESH PATEL:** As a guy building AI and robotics, how do you prevent that?

**ELON MUSK:** Well, I think if you have a limited government, if you limit the powers of government, which is like really what the US Constitution is intended to do, it's intended to limit the powers of government, then you're probably going to have a better outcome than if you have.

**JOHN COLLISON:** More governments will be available to all governments, right?

**ELON MUSK:** Not about all governments. I mean it's difficult to predict the. Like I said, what's the end endpoint or what is many years in the future. But it's difficult to predict this sort of path. Along that way, if civilization progresses, AI will vastly exceed the sum of all human intelligence and there will be far more robots than humans along the way. What happens? It's very difficult to predict.

**DWARKESH PATEL:** I mean it seems like one thing you could do is just say.

**ELON MUSK:** You.

**DWARKESH PATEL:** Are not allowed to. Whatever government index, you're not allowed to use Optimus to do XYZ just write out like a policy. I mean I think you tweeted recently that Grok should have a moral constitution. And one of those things could be that we limit what governments are allowed to do with this advanced technology.

**ELON MUSK:** I mean, yeah, we can do what is. Particularly. I mean if the politicians pass a law and they can enforce that law, then it's hard to not do that law. The best thing we can have is limited government where you have the appropriate cross checks between the executive, judicial and legislative branches.

**DWARKESH PATEL:** I guess the reason I'm curious about it is this. At some point it seems like the limits will come from you, right? Like you've got the Optimus, you've got the space GPUs, you've got the.

**ELON MUSK:** You think I'll be the boss of the government?

**DWARKESH PATEL:** Or you will like the. You will like the. I mean already it's the case with SpaceX that for things that are crucial to the. Like the government really cares about getting certain satellites up in space. Whatever.

**ELON MUSK:** Like it needs SpaceX.

**DWARKESH PATEL:** It is a necessary contractor and you are in the process of building more and more of the technological components of the future that will have an analogous role in different industries. And you could have this ability to set some policy that suppressing classical liberalism in any way. My companies will not help in any way with that or some policy like that.

**ELON MUSK:** I will do my best to ensure that anything that's within my control maximizes the good outcome for humanity. I think anything else would be short sighted because obviously I'm part of humanity. So I like humans. Pro human. Pro human.

## Dojo 3 and Space-Based Computing

**DWARKESH PATEL:** You've mentioned that Dojo 3 will be used for space based computer.

**ELON MUSK:** You really read what I say.

**DWARKESH PATEL:** I don't know if you know Twitter, but I know you long enough. You have a lot of followers.

**ELON MUSK:** Big giveaway. How did you discern my secrets? I post them all.

**DWARKESH PATEL:** How do you design this chip for space? What changes?

**ELON MUSK:** Well, I guess you want to design it to be more radiation tolerant and run at a higher temperature. So roughly if you increase the operating temperature by 20% in degrees Kelvin, you can cut your radiator mass in half. So running at a higher temperature is helpful in space.

There's various things you can do for shielding the memory, but neural nets are going to be very resilient to bit flips. So most of what happens from radiation is random bit flips. But if you've got a multi trillion parameter model and you get a few bit flips, it doesn't matter. Heuristic programs are going to be much more sensitive to bit flips than some giant parameter file. So I just designed it run hot and I think you pretty much do it the same way that you do things on Earth, apart from make it run hotter.

**DWARKESH PATEL:** I mean the solar array is most of the weight on the satellite. Is there a way to make the GPUs even more powered ends than what Nvidia and TPUs and et cetera are planning on doing that would be especially privileged in the space based world?

**ELON MUSK:** Well, I mean the basic math is if you can do about a kilowatt per reticle and then you'd need 100 million full reticle chips to do 100 gigawatts. Yeah. So yeah, depending on what your yield assumptions are, you know that tells you how many chips you need to make. But you need if you want, if you're going to have 100 gigawatts of power, you need 100 million chips running that are running a kilowatt sustained output per radical.

## The Scale of Chip Production

**DWARKESH PATEL:** Basic math, 100 million chips depends on. Yeah, if you look at the die size of something like Blackwell GPUs or something, and how many you can get out of a wafer, you can get on the order of dozens or less per wafer. So basically, this is a world where if we're putting that out every single year, you're producing millions of wafers a month. That's the plan with Terrafab. Millions of wafers a month of advanced process nodes.

**ELON MUSK:** It's got to be some number north of a million. I think you got to do the memory too. Yeah.

**DWARKESH PATEL:** Are you going to make a memory fab?

**ELON MUSK:** I think the terafab's got to do memory. It's got to do logic memory and packaging.

**DWARKESH PATEL:** I'm very curious how somebody gets started. This is the most complicated thing man has ever made. And obviously, if anybody's up to the task, you're up to the task. So you realize it's a bottleneck and you go to your engineers and what is the next. What do you tell them to do? I want a million wafers a month in 2030. What is the next. Like, what do you.

**ELON MUSK:** That's right.

**DWARKESH PATEL:** Do you, like, call ASML, like, what.

**ELON MUSK:** Exactly what I want?

**DWARKESH PATEL:** What is the next step?

**JOHN COLLISON:** That's so much to ask.

**ELON MUSK:** Well, we make a little fab and see what happens. Make our mistakes at a small scale and then make a big one.

**DWARKESH PATEL:** Is a little fab done or is it.

**ELON MUSK:** No, it's not done, which, I mean, people would. They're not going to keep that cat in the bag. That cat's going to come out of the back room. It'll be like drones hovering over the bloody thing. You know, you'll be able to see its construction progress on X. Right. You know, in real time.

So, no, I mean, listen, I don't know, we could just flounder in failure. To be fair. It's like not. Success is not guaranteed. But since we want to try to make, you know, something like 100 million. Yeah. We want 100 gigawatts of power and 100 chips that can take 100 gigawatts.

**DWARKESH PATEL:** Right.

**ELON MUSK:** So call it. Yeah, by 2030. So then. We'll take as many chips as our suppliers will give us. I've actually said this to TSMC and Samsung and Micro and it's like, please build your more fabs faster and we will guarantee you to buy the output of those fabs. So they're already moving as fast as they can. It's not like, to be clear, it's not like us, It's us plus them.

## Conservative Suppliers and Boom-Bust Cycles

**JOHN COLLISON:** There's a narrative that the people doing AI want a very large number of chips as quickly as possible. And then many of the input suppliers, the fabs, but also, you know, the turbine manufacturers are not ramping up production very quickly.

**ELON MUSK:** No.

**JOHN COLLISON:** Yeah. The explanation you hear is that they're dispositionally conservative. You know, they're Taiwanese or German as the story may be, and they just don't believe. They say, like, is that really the explanation or is there something else?

**ELON MUSK:** Well, I mean, it's reasonable. Like if somebody's been in, say the computer memory business for 30 or 40.

**JOHN COLLISON:** Years and they've seen cycles, they've seen.

**ELON MUSK:** Like boom and bust like 10 times.

**JOHN COLLISON:** Yeah.

**ELON MUSK:** You know, so, so like that's a lot of layers of scar tissue, you know, so it's like, it's like during the boom times, looks like everything is going to be great forever. And then, then, then the crash happens and then they desperately try to avoid bankruptcy and. And then there's another boom and another crash.

**JOHN COLLISON:** Are there other, are there other ideas you think others should go pursue that you're not for whatever reasons right now?

**ELON MUSK:** I mean, there are a few companies that are pursuing new ways of doing chips, but they're just not scaling fast.

**JOHN COLLISON:** I don't even mean within AI.

**ELON MUSK:** I mean just generally, I'd say people should do the thing where they find that they're highly motivated to do that thing as opposed to, you know, something summing up some idea that I suggest they should do the thing that they find personally interesting and motivating to do.

## The Energy Bottleneck

**ELON MUSK:** But you know, going back to the limiting factor, use that phrase about 100 times the current limiting factor that I see in the time frame, in the sort of 2029, in the three to four year time frame, it's chips. In the one year time frame, it's energy, power production, electricity. It's not clear to me that there's enough usable electricity to turn on all the AI chips that are being made.

Towards the end of this year, I think people are going to have real trouble turning on like the chip output will exceed the ability to turn chips on.

**DWARKESH PATEL:** What's your plan to deal with that world?

**ELON MUSK:** Well, we're trying to accelerate electricity production. I guess that's maybe one of the reasons that XAI will be maybe the leader. Hopefully the leader is that we'll be able to turn on more chips than other people can turn on faster because we're good at hardware.

And generally the innovations from the corporations that call themselves labs, the ideas tend to flow. It's rare to see that there's more than about a six month difference between. The idea is travel back and forth with the people. So I think you sort of hit the hardware wall and then whichever company can scale hardware the fastest will be the leader. And so I think xAI will be able to scale hardware the fastest and therefore most likely will be the leader.

## Leaning Into Acute Pain

**JOHN COLLISON:** You joked or self conscious about using the limiting factor phrase again, but I actually think there's something deep here. And if you look at a lot of things we've touched on over the course of it, maybe kind of a good note to end on. Like if you think of a senescent lower agency company, it would have some bottleneck and not really be doing anything about it.

You know, Marc Andreessen had the line of most people are willing to endure any amount of chronic pain to avoid acute pain. And it feels like a lot of the cases we're talking about are just leaning into the acute pain, whatever it is. It's like, okay, we got to figure out how to work with steel or we got to figure out how to run the chips in space, or we'll take some near term acute pain to actually solve the bottleneck. And so that's kind of a unifying theme.

**ELON MUSK:** I have a high pain threshold. That's helpful.

**JOHN COLLISON:** Solve the bottlenecks.

**ELON MUSK:** Yes. So, you know, one thing I can say is like, I think the future is going to be very interesting. And as I said, the Davos I've only been to, I was looking at Davos. I think it was on the ground for like three hours or something.

It's better to be, it's better to err on the side of optimism and be wrong than err on the side of pessimism and be right for quality of life. So, you know, your happiness will be, you'll be happier if you, if you are on the side of optimism rather than erring on the side of pessimism. And so I recommend erring on the side of optimism. That's cool.

**DWARKESH PATEL:** Elon, thanks for doing this.

**JOHN COLLISON:** Thank you.

**ELON MUSK:** All right.

**JOHN COLLISON:** Oh, great stamina.