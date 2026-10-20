# r/opencodeCLI — hilos 2026-10-19 → 2026-10-21
_Generado: 2026-10-20T02:03:09.953167+00:00 · 45 hilos · 98 comentarios · fuente: Arctic Shift_

## OpenCode Hacked
**u/RelevantEmergency707** · 2026-10-20 01:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaf1wq/opencode_hacked/)

---

## I want to try the Pi harness. Does OpenCode support it?
**u/itherseed** · 2026-10-20 01:24 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaf0f8/i_want_to_try_the_pi_harness_does_opencode/)

I was thinking of trying other harnesses using the models of OpenCode Go. Does OpenCode allow users to do that, or will I get limited/banned for using anything else than their product? I was trying to find some official documentation allowing it or prohibiting it but haven't found anything. Thanks in advance.

---

## Does OpenCode free model rate limit affect all devices on the same WiFi ?
**u/sammartinX** · 2026-10-19 23:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xacpt3/does_opencode_free_model_rate_limit_affect_all/)

Have you guys noticed this in OpenCode?

When multiple devices are connected to the same WiFi, if one device hits the free model rate limit, does it affect other devices too?

I was working on a project with my friends. After some time, we all got rate limited on free models. So we told the others to pull all latest changes from GitHub, fix some features, and continue working on the project.

But when they started using OpenCode, they also got rate limited on free models.

When using Gooo, everything works fine, obviously.

So I am wondering, is OpenCode free model rate limiting based on IP address? Like, if multiple people use it from the same WiFi, can one person's rate limit affect everyone else? Or is this just a coincidence? Cause its not a coincidence cause I noticed it with my second laptop !

Anyone else experienced this?

---

## Unpopular opinion: the model is a commodity. Claude hit its limit at 18:40 and my agent just swapped brains.
**u/phantomyard_labs** · 2026-10-19 23:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xac65f/unpopular_opinion_the_model_is_a_commodity_claude/)

---

## How are you optimally using LongCat 2.5 Preview Free and Beam Free in OpenCode Go?
**u/letuslisp** · 2026-10-19 23:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xabx6e/how_are_you_optimally_using_longcat_25_preview/)

---

## How are you optimally using LongCat 2.5 Preview Free and Beam Free in OpenCode Go?
**u/letuslisp** · 2026-10-19 22:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xabrsw/how_are_you_optimally_using_longcat_25_preview/)

Hey everyone!

I'm using OpenCode Go and noticed that **LongCat 2.5 Preview Free** **and** **Beam Free** are both currently available with unlimited usage.

I'm curious how people are actually getting the most out of these two models.

And also their experiences (are they really unlimited)?  

  

For those of you who have been using them regularly:

\* **What tasks does each model work best for?** For example, planning, codebase exploration, debugging, implementing features, refactoring, tests, or simpler repetitive coding tasks.

\* **What prompting techniques work well?** Do you use specific instructions, planning workflows, custom agents, or other configurations to improve their results?

\* **How reliable are they with tools?** Do you let them edit files and run commands autonomously, or do you keep them on a shorter leash?

\* **How do you avoid loops, bad edits, and wasted time?** Have you found effective ways to handle these issues?

\* \\*\\*Do you use either as your main coding model, or do you combine them with other models in a particular workflow?

I'd especially appreciate concrete examples of workflows, prompts, and configurations that have worked well for you, rather than just general impressions.

Since usage is unlimited for now, I'm wondering how best to take advantage of that without sacrificing code quality or spending time undoing bad changes.

Thanks!

---

## OpenCode Mobile App Made with DeepSeek V4.1 Flash 1017
**u/Genetic_Prisoner** · 2026-10-19 22:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xab412/opencode_mobile_app_made_with_deepseek_v41_flash/)

Title pretty much says it.

I wanted to test the new DeepSeek’s ability to one-shot a native mobile app while keeping the UI consistent with OpenCode’s theming.

As you can see, it turned out pretty well for a one-shot. Definitely not bad at all.

Feel free to try it out here: [github repo](https://github.com/jaggerjack61/OpenCodeMobile)

---

## I reimplement Opencode v2 and v1 in Rust
**u/microbass** · 2026-10-19 22:24 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xab2a4/i_reimplement_opencode_v2_and_v1_in_rust/)

I use opencode every day and the thing that kept getting in the way wasn't the client. It was the server. On my laptop it sat at about 2.4 GB RSS next to a 33 GB SQLite file, and searching inside a single session took roughly six seconds.

So I reimplemented the server in Rust. Same HTTP and SSE wire contract, so the real TUI attaches and the real web UI loads against it. No client changes, no patches to their project.

Same box, same fixture data, back to back:

• binary: 61 MB, upstream 185 MB

• idle RSS: \~100 MB, upstream \~2.4 GB

• boot: 0.6 s, upstream 4.7 s

• session list and read p95: 0–2 ms, upstream 8–15 ms

• search inside one session: 0.2 ms, upstream \~6 s

• web UI first load: 1.05 MB of assets, upstream 9.10 MB

Then I ran a read-only load test, no model calls at all, both servers pinned to the same two cores. It held about 6,700 requests/sec against roughly 420 for upstream, with p95 latency an order of magnitude lower, and used about a quarter of the memory. That's a closed-loop test, so treat the throughput as capacity, not as a latency promise for your setup.

What works: TUI attach, the embedded web UI, sessions and messages with cursor paging, streaming, tools, permissions, questions, PTY, shadow-git snapshots, revert, diff, in-session search, MCP, and plugins in both the v1 shape and the newer v2 shape. Auto-compaction and config hot-reload. The v2 API surface is bound and tested against the real 2.0.28 client.

What doesn't: provider OAuth, the hosted share backend, and macOS/Windows: the PTY layer is Linux/glibc only.  

"cargo install ocserve"  still gives you 0.3.1, because crates.io caps crate size and one crate carries the embedded web UI; the 0.4.0 tarball is on the releases page.

It's not a fork. Separate codebase, MIT, their notice retained. I read their source to port behaviour faithfully and I keep a differential harness that boots both servers and compares the bytes.

If opencode runs fine on your machine, keep using it. It's the reference implementation and it's good. This exists for the machines where the server is the thing falling over.

MIT, source and releases: https://github.com/Reliary/ocserve

---

## VOID
**u/PLAYER99-void** · 2026-10-19 22:02 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaaj7t/void/)

[removed]

---

## opencode on an always-on server, with the working copy still on my laptop (setup and gotchas)
**u/tapeo** · 2026-10-19 21:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaaewj/opencode_on_an_alwayson_server_with_the_working/)

Disclosure first: I built the sync piece described below, so read the recommendation with that in mind. The opencode side is plain and works with any setup.

**The problem.** I want opencode running on a machine that stays on, but I also want the project on the laptop, because that's where builds happen: xcodebuild, a flutter run on a plugged-in phone, a dev server the browser talks to. Committing every time to move work between the two is the part that made me give up on a remote box.

**The setup, three commands.**

On the server, as root:

    curl -fsSL https://github.com/tapeo/corami/releases/latest/download/install.sh | sh

On the laptop, signed in to the same Tailscale account:

    curl -fsSL https://github.com/tapeo/corami/releases/latest/download/install.sh | sh
    corami project add --local-path ~/dev/myapp

From there the folder on the laptop and the folder on the server are the same project: edits flow both ways, uncommitted work included. opencode runs on the server inside that folder, and `corami serve 3000` gives the dev server a stable https URL on the tailnet, so previews open from the phone. `corami status --json` is what I use from scripts.

**Gotchas I actually hit.**

* `node_modules` and build output stay out of the sync, each machine regenerates them. Syncing them is slow and pointless.
* git is the fragile part, not the sync: a rebase on one side while the agent is writing on the other is how you get index.lock fights. Do one at a time.
* when both sides edit the same file and it can't be resolved safely, the sync stops and reports instead of picking a winner. I'd rather fix it than find out later.
* big binaries: keep them out, it's a source tree sync, not a backup.

**Why not the other shapes.** tmux over ssh leaves the code on the server, so local builds get awkward. A mount (sshfs, or a devcontainer mount) pays latency on every read and the file watchers hate it. A cloud agent works on a clone and hands back a branch, so whatever wasn't committed stays behind.

How is everyone else running opencode away from the machine in front of them? And does anyone actually keep a local copy of the working tree, or do you just live on the remote?

Repo, if useful: [https://github.com/tapeo/corami](https://github.com/tapeo/corami)

---

## Deepseek 1017 Free for a month on PGS AI. Usage that rolls over, 100% Private infrastructure.
**u/Whole_Succotash_2391** · 2026-10-19 21:11 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa98hv/deepseek_1017_free_for_a_month_on_pgs_ai_usage/)

We all deserve access to high grade intelligence. The kind you can point your whole workflow at without watching a meter, without wondering whether your code is training someone else's model, and without a plan that quietly bets you will not use what you already paid for. That is what the PGS coding plan is built to be, and this week it ships with the best open model to land ever.

DeepSeek 1017 is live on Phoenix Grove API right now, free for a month. Fast, sharp, and running on private US infrastructure. GLM 5.3 Flash is in there too, along with Mimo 2.6 and all three are on the free month.

If you have not run into us yet: PGS hosts the top open models behind one API, on 100% US based infrastructure, with zero training on your code or prompts. One key, one bill, and no hunting across five dashboards to reach the models you actually like.

**The models, together.** DeepSeek 1017, GLM 5.3 Flash, the Kimi family, Qwen, Nemotron and more. Switch between them by changing nothing but a model string. Eighteen other major models sit on the same key whenever you want them.

**Usage that waits.** This is the part we care most about. Most coding plans are built around the hope that you waste what you buy, chopped into rolling windows so nobody can ever spend it all. Our higher plans bank up to ten days of usage. Unused windows roll forward instead of evaporating, so a light week is not a loss, it is a head start on the heavy week.

**Actually private.** US based processing, and your code and prompts are never used for training. Ever. Not "some models are private, others are not." All of them, all the time. Run the top open models without shipping your private prompts to a training lab.

**Fast where it counts.** The flash models we host run 100 to 130 tokens per second. It feels smooth in the way that matters when you are watching a diff generate instead of waiting on it.

**Pricing that does not need tricks.** On average our token pricing runs about 20 percent under market, and that is the whole business model. No ads, no data sales, no harvesting.

Genuine thanks to the DeepSeek team. Every release like this one is a gift to everyone who would rather not rent their intelligence from a company that can change the terms next quarter.

Free for a month, bills at $3.99 after, cancel anytime. Use it and cancel, that is completely fine.

API and coding plan: [api.pgsgrove.com](http://api.pgsgrove.com)  
The full app, if you want it: [ai.pgsgrove.com](http://ai.pgsgrove.com)

 There are a lot of great services to choose from, and you do not need to be locked in. As of today, we are one of the only fast, private, US based and low cost options out there. Come give it a try.

---

## Los plugins y modificaciones de OpenCode valen la pena?
**u/ERROR_FOX_PG** · 2026-10-19 20:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa8jm8/los_plugins_y_modificaciones_de_opencode_valen_la/)

---

## What is your Opencode setup?
**u/ECrispy** · 2026-10-19 19:53 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa75nw/what_is_your_opencode_setup/)

---

## Any useful plugin for opencode CLI?
**u/KJMHELLO** · 2026-10-19 18:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa4tt7/any_useful_plugin_for_opencode_cli/)

I used to be a huge fan of OpenCode just 6 months ago, but I haven't been using it at all lately.

However, using OpenCode's free models or its core models seems to have great perks, so I wanted to try using it, but I ran into some parts that I couldn't use. So, I'm thinking of going back to using the OpenCode CLI instead, but a lot seems to have changed.

Could you please show me a good way to explore marketplaces or plugins to find the additional features I need?

---

## What to do to improve usage: burn limit in 30 min when before was all day
**u/mamcx** · 2026-10-19 17:30 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa38c4/what_to_do_to_improve_usage_burn_limit_in_30_min/)

---

## 🔥 DeepSeek V4.1 Flash updated to 1017 in OpenCode Go and Free
**u/afanasenka** · 2026-10-19 16:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa1qm5/deepseek_v41_flash_updated_to_1017_in_opencode_go/)

**Comentarios:**

- **u/chinmay06** (↑10, 2026-10-19 17:02): https://preview.redd.it/68jy124pggwh1.png?width=480&format=png&auto=webp&s=d32b1338303241968960a8dd4fcd4a262a4a4b2f
- **u/bankinu** (↑2, 2026-10-19 17:04): Do free models work with opencode-cli?
  - **u/nexis** (↑1, 2026-10-19 17:29): yes
- **u/IamPussyKitten** (↑4, 2026-10-19 17:12): What is 1017
  - **u/No_Captain4899** (↑2, 2026-10-19 17:14): A new version
  - **u/AdFun4897** (↑6, 2026-10-19 17:31): Deepseek v4.1 astra flash
  - **u/-PROSTHETiCS** (↑1, 2026-10-19 17:40): its a version/date checkpoint.. = October 17 2026
  - **u/Solocune** (↑1, 2026-10-19 17:48): Release of the 17th October. New version.
  - **u/Ok-Drawer5245** (↑1, 2026-10-19 18:29): It’s what they call a minor update, “only” about 30% better than the last version….
      
      In other words it’s hands down the best flash model in the world right now… and absurdly cheap
- **u/rootb3r** (↑3, 2026-10-19 17:24): has a very small context window compared to the offical deepseek API, I had to compact the conversations multiple times.
  - **u/Genetic_Prisoner** (↑1, 2026-10-19 17:41): Are you using the free zen version?
    - **u/QuietPsychonaut** (↑1, 2026-10-19 18:00): He surely is. The paid version still has 1M context.
    - **u/rootb3r** (↑1, 2026-10-19 18:07): yup
- **u/nooneiusedtoknow** (↑2, 2026-10-19 17:45): Thinking time was as usual, however output fellt blazingly fast.
- **u/Osvik** (↑2, 2026-10-19 17:46): I've tried it once with my benchmark project and it's much **much better**, specially the **visual design**. The result of my test is similar to what I've obtained in GPT-6.1 Sol, which is far better than what I was expecting. I'm curious to see what they can do with 4.1 Pro, if/when it comes out.
  - **u/Ok-Drawer5245** (↑1, 2026-10-19 18:31): Ouhhhh tasty visual design. I just asked it to do some design that requires spatial understanding, cant wait to see what it comes up with
- **u/egomarker** (↑1, 2026-10-19 18:26): Yeah booooiiiiii

---

## OpenFlow vs OpenCode
**u/SeeRay11_Main** · 2026-10-19 16:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa1jh4/openflow_vs_opencode/)

OpenCode: better for everyday use especially for straightforward tasks.

OpenFlow: better for mixing a variety of different agents together and seeing how they interact and work together.

Both the same harness with different results.

---

## Anyone testing the final M3.1-Flash in OpenCode yet?
**u/Professional_Run3390** · 2026-10-19 15:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xa0bb3/anyone_testing_the_final_m31flash_in_opencode_yet/)

I used Space Bunny quite a bit in OpenCode and honestly liked it.  
It felt fast, stayed on track surprisingly well on longer tasks, and usually followed constraints without me constantly steering it back. Repo work also felt pretty smooth for a Flash model.  
Now that it’s been revealed as an early version of M3.1-Flash, I want to give the actual release a proper test before deciding whether I’d subscribe.  
I’m mostly going to rerun the kinds of things I used Space Bunny for:  
longer repo tasks  
multi-file edits  
recovering after a failed tool call  
how many correction rounds it needs  
whether it starts wandering as the session gets longer  
I’m especially curious whether the final version keeps the speed I liked while improving the rough edges.  
Anyone testing M3.1-Flash in OpenCode already? What’s your experience been like so far?

---

## I run OpenCode and Claude Code as one team with a shared memory, so I built a desktop app for it
**u/Main_Vermicelli3363** · 2026-10-19 14:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9xytk/i_run_opencode_and_claude_code_as_one_team_with_a/)

I've been using OpenCode for the routine work (edits, tests, refactors on cheaper models) and Claude Code for planning and review. The annoying part was everything in between: copying context from one terminal to the other, losing what was decided yesterday, and Claude hitting its 5-hour limit in the middle of a task.

So I built Foxpit, a desktop app where they work as one team:

* **One team, any agent per seat.** The lead can run on Claude Code while teammates run OpenCode on whatever model you pick. The lead splits the task and hands parts to them.
* **Shared memory.** Decisions, files and open threads go into `.foxpit/memory` as plain markdown with \[\[links\]\] in your repo. A fresh OpenCode session starts already knowing what Claude did yesterday, and the other way round.
* **Limits.** When Claude Code hits its limit, the lead parks and resumes by itself at the reset while OpenCode teammates keep going.
* **You can see all of it.** Real terminals (up to 4 side by side), and a 3D office where every project is a room and you can see who is working, stuck or waiting for your approval.

It uses your own OpenCode setup and models; nothing is resold, and your code stays on your machine. Windows, macOS (Apple Silicon) and Linux.

It's a paid app in beta. For this sub I made a code that gives a free week, no card: **FOXOC** [https://foxpit.dev/account.html?kod=FOXOC&utm\_source=reddit&utm\_medium=community&utm\_campaign=opencodecli](https://foxpit.dev/account.html?kod=FOXOC&utm_source=reddit&utm_medium=community&utm_campaign=opencodecli)

I'm the solo dev, so honest feedback helps a lot. One question I'm curious about: which model do you run in OpenCode for routine edits? I want the team setup to suggest sensible defaults.

**Comentarios:**

- **u/Soifon99** (↑1, 2026-10-19 14:16): Sorry but it seems like almost everybody is so eager to do something with AI, that reddit is flooded with a million semi useless tools and apps..   everybody is a app builder these day.  and they all say, i build a app..  No you didn't  the building was done by AI.  you thought of a app.. they build it.
  - **u/Main_Vermicelli3363** (↑1, 2026-10-19 14:18): That’s kind of the point of the app though. The hard part wasn’t typing code, it was getting Claude Code and OpenCode to share context, not redo each other’s work, and not stall when Claude hits its limit. Foxpit is the setup I ended up needing for that, so I made it usable for others. If it’s useless for your workflow, totally fair, I’d rather hear what’s missing.
    - **u/Soifon99** (↑1, 2026-10-19 14:30): IT's not personal, it's just a thing that's been bugging me in the back of my mind. :D
      - **u/Main_Vermicelli3363** (↑1, 2026-10-19 14:35): No worries, I get it. The flood is real, I scroll past most of it too. Appreciate you saying it straight.
  - **u/MeasIIDX** (↑1, 2026-10-19 14:44): This is something I think about here and then as well (I'm a software engineer of 13 years). 
      
      Do you feel that people point out that AI is the builder and not the user when the user poses as the solo dev of an app/game/code? Or is it the way the OP framed the body of text? 
      
      Like, I would not generate artwork and say I'm the solo painter behind the piece, but when does the line get crossed between a person coding with AI and them becoming the developer of what they're building.
      
      Of course I'm using AI at work everyday (I don't have a choice on my team), professionally I'm a developer, when I build little apps here and there with AI, am I still a developer? Maybe I'm thinking about this too much lol.
    - **u/Main_Vermicelli3363** (↑2, 2026-10-19 14:59): Honestly, while building this I spent a lot of time on where the top models get confused, catching their mistakes, making the UI decisions and so on, and I really racked my brain over what would work best. Yes, we’re not the ones typing the code, but we’re the ones making the decisions. I don’t think it needs much overthinking, let’s just keep up with the future 😃
    - **u/Seastrike_Dev** (↑1, 2026-10-19 15:32): Did AI wake up one morning and decide for you the app to build? Did AI then decide to turn its self on to execute your thoughts? Did AI then decide to design the app/software exactly how you imagined it? If AI didnt do all this then you designed and built that app, AI is just 2026s tool equivalent to linux in the 80s period.
- **u/IlNaka** (↑-1, 2026-10-19 14:18): Good idea
  - **u/Main_Vermicelli3363** (↑1, 2026-10-19 14:20): Thanks! If you try it, I’d love to know where setup felt confusing. That’s the part I’m polishing most right now.
- **u/Vexaris1** (↑0, 2026-10-19 14:48): This project will gain value...
  - **u/Main_Vermicelli3363** (↑1, 2026-10-19 14:50): Thanks, means a lot this early!
- **u/investigatormaker** (↑-2, 2026-10-19 15:14): Foxpit's limit handling is the part I'd lead with: the lead parking until the 5-hour reset while OpenCode teammates keep going is something anyone who has hit that limit mid-task pictures right away. For defaults, I'd read whatever models the user already has configured in OpenCode and suggest the cheapest one for teammate seats, rather than shipping a fixed model name. Also say whether .foxpit/memory is meant to be committed or gitignored, since shared decisions in a team repo change who sees them.
    
    I make ThreadFox. We find relevant Reddit conversations and do the posting for your business. The $39 Pilot covers seven days and up to 50 posts and replies. No automatic renewal. https://threadfox.vip/managed?tier=employee_pilot&utm_source=reddit&utm_medium=comment&utm_campaign=tf-managed&utm_content=20261019-1429-elmpl#employee-order
  - **u/Main_Vermicelli3363** (↑1, 2026-10-19 15:23): Good points. Reading the models already configured in OpenCode and suggesting the cheapest for teammate seats is a better default than a fixed name, adding that to the list. On memory: Foxpit doesn’t gitignore .foxpit/memory, it’s plain markdown so you decide. Commit it if you want the team to share decisions, add it to .gitignore if you want it personal. I should make that a clear choice on first setup instead of leaving it implicit.

---

## How are you optimally using LongCat 2.5 Preview Free and Beam Free in OpenCode Go?
**u/letuslisp** · 2026-10-19 13:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9x94g/how_are_you_optimally_using_longcat_25_preview/)

---

## Opencode Setup help
**u/Dry-Smell436** · 2026-10-19 12:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9vvjm/opencode_setup_help/)

---

## 🔥 MiniMax M3.1 Flash (Space Bunny) is FREE on OpenCode for 3 days
**u/afanasenka** · 2026-10-19 12:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9ve84/minimax_m31_flash_space_bunny_is_free_on_opencode/)

**Comentarios:**

- **u/Chupa-Skrull** (↑7, 2026-10-19 12:22): I just made a Space Bunny in the toilet this morning
  - **u/Aggravating-Push-207** (↑3, 2026-10-19 15:32): Thanks for telling us
    - **u/Chupa-Skrull** (↑2, 2026-10-19 15:36): I'll keep you looped in
      - **u/corobo** (↑1, 2026-10-19 15:54): Logged on
- **u/Ammoun442** (↑3, 2026-10-19 12:25): Who would have ( not ) guessed

---

## Tokless: 30-second all-in-one toolkit for OpenCode — Zero setup, minimal MCPs, token-efficient tools (CodeGraph, Context-Mode, Project Memory, Headroom, RTK, Caveman, Ponytail)
**u/Strict_Grocery9693** · 2026-10-19 12:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9v20w/tokless_30second_allinone_toolkit_for_opencode/)

[removed]

---

## MiniMax M3.1 Flash to go open weights on 23 October
**u/jpcaparas** · 2026-10-19 11:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9uv9c/minimax_m31_flash_to_go_open_weights_on_23_october/)

Announcement: https://x.com/minimax\_ai/status/2112149942332494093?s=46

**Comentarios:**

- **u/Strict-Prune-879** (↑1, 2026-10-19 12:02): intéressant donc ils attaquent le marché flash? pour concurrencer qui? deepseek v4.1 flash? glm 5.3 flash? mimo v2.6 flash?
  - **u/xRebellion_** (↑1, 2026-10-19 15:00): From listed pricing alone, closer to glm I'd say

---

## MiniMax M3.1 Flash (Space Bunny 🚀) benchmarks... 😁
**u/afanasenka** · 2026-10-19 11:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9uupb/minimax_m31_flash_space_bunny_benchmarks/)

Cowork (Automation-Bench: 62%; ALE: 30%)

Coding (DeepSWE: 74%)

Visual Understanding (BabyVision: 91%), at 1/3 the cost of M3 and 3x the speed.

**Comentarios:**

- **u/Mancho_United** (↑17, 2026-10-19 12:16): For flash models the most important is instructions following and code writing, as you will use better model for planning and review and want a reliable cheap and fast model for the implementation.
  - **u/DenysMb** (↑5, 2026-10-19 14:13): And sadly MiniMax is terrible for "instructions following".
  - **u/Solocune** (↑2, 2026-10-19 14:35): Instructions are obviously always important. But it's better to have stronger models than weaker ones with the same instruction. The "flash" does not have much to say here. It's still better than glm 4.7 non flash.
- **u/bakawolf123** (↑11, 2026-10-19 12:18): minimax coding models looked benchmaxed for me in the past, will see how it pans out  
    I think glm might want to release an update too soon
  - **u/Guardian-Spirit** (↑6, 2026-10-19 12:42): I'm extremely suspicious towards it. MiniMax always had top benchmarks score, and I never could understand, why.
  - **u/look** (↑3, 2026-10-19 14:39): GLM releases have occurred every two months almost like clockwork for the past year and a half or so. We’re due for one by the end of the month.
  - **u/Civil_Rent4208** (↑1, 2026-10-19 18:17): I tried the space bunny in the opencode and it seems like it is benchmaxxed
- **u/Ammoun442** (↑7, 2026-10-19 12:27): Its kinda good  i used it alot in the stealth duration
- **u/Able_Statistician688** (↑6, 2026-10-19 12:32): Why do people post benchmarks where the model obviously wins…against dated models? Opus 5 instead of 5.5? 5.6 sol? Can someone explain how a benchmark like this isn’t just an ad?
  - **u/ayudha90** (↑2, 2026-10-19 12:51): Well it's flash model. So it's smaller and can only compete with other small models or older bigger models. It might spend significantly more token to finish the task compared to the older bigger models but it finishes it with "better" results (task from the benchmark).
  - **u/no-name-here** (↑1, 2026-10-19 12:51): 1. This is a flash model that costs a tiny percentage in comparison yet still beats a US frontier lab highest-tier model released in July. This one costs 33 times less per output but yet is scoring higher than it.
      2. If your expectation is that a Chinese flash model is going to be comparable to a frontier lab's highest-tier model from more recent than a few months ago then I think you are going to be disappointed. If your expectation is that a Chinese flash model can beat a frontier lab's highest-tier model from 3 months ago, you'll be pleased. And the Chinese flash model isn't even comparing itself to OpenAI's moon or earth model variants - they are comparing it to the 'sun' (sol) highest-tier version.
    - **u/adolf_twitchcock** (↑1, 2026-10-19 15:25): https://preview.redd.it/9mdzgveezfwh1.png?width=666&format=png&auto=webp&s=38709cd3d0386ced0682c25ab904a95bdd8d2011
        
        mogged by luna and haiku (cost per task)
  - **u/queso184** (↑1, 2026-10-19 14:06): I think its more useful to compare it to similar models in either price or performance. 
      
      If we just compared it to latest Opus and Astra, obviously it's worse (and it's not trying to compete on that frontier anyway) so not sure how that becomes a useful comparison
- **u/DiscountFit9224** (↑3, 2026-10-19 13:34): API vs API pricing + reliability -> cheapseek v4.1 1017 wins all day
- **u/Specter_Origin** (↑3, 2026-10-19 13:56): I have never found any minimax model to be even remotely close to what their benchmarks suggest.
  - **u/Specter_Origin** (↑1, 2026-10-19 16:02): After testing it, can confirm, not even half as good as 4.1 flash. 
      
      I would even call it rackless, tried to write a script that would do 3m recursive workers on something in multithreaded manner and I was wondering why fan on macbook is spinning for minutes which is so rare.
- **u/RedlineTriad** (↑2, 2026-10-19 14:29): I find terminal bench 4 to be the most representative benchmark so far and... It doesn't seek to be doing great there. Frontiercode is also good. DeepSWE seems like a joke nowadays.
- **u/mannenmytenlegenden** (↑3, 2026-10-19 16:05): I used Space Bunny free last week. One commit all of a sudden was "Co authored by Claude Opus 4.8"... Who knows what's happening behind the scenes
  - **u/basil_0408** (↑3, 2026-10-19 16:22): Got that too, but it's normal if they make the dataset from public git repos. Lots of commits have that co-author line, this just proves that Opus 4.8 commits are the majority in their dataset.
- **u/Osvik** (↑3, 2026-10-19 17:25): I tired it twice with a prompt I use to benchmark. In my experience it's a model with imagination but less accurate execution. It also doesn't follow prompts as intended. It's like that cousin who is studying contemporary art but fails at commercial visual design.
- **u/Grouchy-Possible-852** (↑1, 2026-10-19 18:17): Lo he usado en un pequeño proyecto personal y para que me solucionará un Bug pequeño he tenido que meterle 5 promts, me he cansando y he continuado con haiku 5.5 y como la noche y el día, haiku a sido muy superior, soy fan de minimax y esperaba que llegara a un nivel aceptable, pero la realidad es que me llega a desperar usarlo.

---

## MiniMax M3.1 to go open weights on 23 October
**u/jpcaparas** · 2026-10-19 11:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9uufb/minimax_m31_to_go_open_weights_on_23_october/)

[removed]

---

## I made opencode v2 read my plan quota and type what I                                                       say
**u/LeonVeganMan** · 2026-10-19 11:36 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9uhsd/i_made_opencode_v2_read_my_plan_quota_and_type/)

---

## So Space Bunny was M3.1-Flash
**u/Rocky885533** · 2026-10-19 11:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9txr1/so_space_bunny_was_m31flash/)

---

## Request Failures with OpenCode V2
**u/LinuXperia** · 2026-10-19 10:49 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9tlru/request_failures_with_opencode_v2/)

OpenCode V2 fails a lot with requests the last few Days.

This is very bad situation.

I am having huge amount of inference request failures, inference request rejections and inference tool call failures.

This inference problems did not exist few days ago.

Not sure if OpenCode is not compatible with the newest models that were released the last days and does not follow specific new standards the new released models like DeepSeek 1017 and gemini 4 Argon implemented or the inference providers are failing and rejecting OpenCode users becouse they dont use their offocial harness but instead use the third party harness software opencode itself and try to stiffle competition that way so lesss paying customers use opencode with their models and instead swith over to their subscription offers.

I used opencode in combination the newest 1017 version of DeepSeek direct over their API and had huge amount of request and tool call failures the last days.

Same with opencode and Google Gemini Argon using it over the opencode go plus subscription.

See picture.

OpenCode is not usable for workung as of now becouse of this many requests failures either becouse of opencode itself or the inference providers !

This request failures did not happened few days ago and are new, becouse either of bugs and errors in opencode version like too early closing conection to the inference provider or inference provider incompability and problems.

Having muse wonder on OpenCode would at least ease the Problems with DeepSeek and Gemini.

**Comentarios:**

- **u/LinuXperia** (↑1, 2026-10-19 10:52): I just looked up the Code 429 what it means.
    429 means opencode sent too many requests in a short Period of time ( rate limiting ) !
    Looks like opencode must implement some delays to avoid be too much performant and overload the inference provider.
    Need lookup if i can do this even myself somehow manually in some settings.
  - **u/Soooskiii** (↑1, 2026-10-19 11:20): Take a look here https://http.cat/
    - **u/LinuXperia** (↑1, 2026-10-19 12:59): 429 is too many requests in short time: [https://http.cat/429](https://http.cat/429)
        
        The inference provider blocks opencode parallel requests that are issued in short time probably becouse they proccess the requests fast er so everything is speedup and this leads to this blocking failures.

---

## with DeepSeek and GLM free in opencode, the spare agent time can go into other people's GitHub issues
**u/Nitjsefnie** · 2026-10-19 10:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9sw6r/with_deepseek_and_glm_free_in_opencode_the_spare/)

free models in opencode mean a lot of us have more agent time than tasks now. I built a place for that time to go: Overflow

spare week: take a priced issue from a registered repo, merged PR gets you credit
dry week: price an issue in your repo, someone with spare usage ships it, your credit pays

it only sees the PR, so which model or harness wrote it doesn't matter. junk PRs: you block them on GitHub like any repo, you set the price after you've seen the work, and you only owe for what you merge. the issue is the brief, if your agent hits a decision it asks the maintainer on the issue

no money, no keys, MIT

main reason I'm posting is I want people to register their repos. every open issue on the board right now is mine and I'm not after help with those, I want spare usage going into other people's projects. 28 users so far

https://github.com/Nitjsefnie/Overflow

---

## OpenCode's free models aren't available from your current network because we've detected abusive traffic from this IP address
**u/Trick_Vegetable8474** · 2026-10-19 09:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9sh9r/opencodes_free_models_arent_available_from_your/)

OpenCode's free models aren't available from your current network because we've detected abusive traffic from this IP address  
what is the solution ?

**Comentarios:**

- **u/nazmulpcc** (↑3, 2026-10-19 09:54): Just wait for a few days, they're going through an incident
  - **u/ArC3488** (↑-3, 2026-10-19 11:00): no it's permanent unless we make enough noise about it
    - **u/nazmulpcc** (↑3, 2026-10-19 11:02): what's your evidence?
      - **u/ArC3488** (↑-4, 2026-10-19 11:04): I don't need to say anything
        - **u/nazmulpcc** (↑3, 2026-10-19 11:06): LOL
            you can literally see that they were hacked recently and still trying to recover and maintain security, right?
            Dax posted about it on x
            You can criticize the fact that they got hacked but saying free offer shutdown is permanent just from that is not an intelligent assumption. Do better
          - **u/ArC3488** (↑-3, 2026-10-19 11:16): That's not what i said. I said people won't be able to abuse proxy IPs anymore. This abuse more so happens in 3rd world countries.
              
              Free tier is always there. Opencode is being more strict about the IP checks from hereon out
- **u/ArC3488** (↑0, 2026-10-19 11:06): There is no solution. Best thing you can do is wait to see if they change their mind. It's likely that this change is here to stay
  - **u/Kisscool-citron** (↑2, 2026-10-19 12:06): Completely false, I had the issue without using proxies or VPN, and after 2 days of various errors, back to normal. stop spreading bullshit please, the world has enough misinformation as it is.
    - **u/ArC3488** (↑0, 2026-10-19 12:09): I am facing the issue right now, it isn't "back to normal". Where are you getting this from?  
          
        Also i am more inclined to agree with you now that you've gone ahead and downvoted every single one of my post on this thread lmao. Fuckin schizo
      - **u/Kisscool-citron** (↑1, 2026-10-19 14:36): I said that I faced the issue, with many other error messages. They all went away after 2 days and no action on my part. Obviously the situation is anormal. But the statement that Opencode is making this change as a VPN/proxy countermeasures permanent is false, as I can attest. I didn't use any VPN or proxies anyway, and no commercial IP range.
        - **u/ArC3488** (↑0, 2026-10-19 14:44): what's your evidence?
    - **u/abdiMK** (↑1, 2026-10-19 14:29): Same here i was working and that issue just suddely come out of no where i was not using any VPN or Proxies
- **u/No_Manager2789** (↑0, 2026-10-19 16:21): I am facing the same problem..

---

## 🚀 MiniMax-M3.1-Flash is coming... 😄
**u/afanasenka** · 2026-10-19 09:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9scrr/minimaxm31flash_is_coming/)

Space Bunny?!

[https://x.com/MiniMax\_AI/status/2112111925975032241](https://x.com/MiniMax_AI/status/2112111925975032241)

**Comentarios:**

- **u/Eyelbee** (↑2, 2026-10-19 09:53): Hope it one-ups qwen flash
- **u/ps5cfw** (↑13, 2026-10-19 09:54): when I used it it wasn't too good compared to Muse Spark 1.3, which is itself kind of weaker than DS4.1 for my efforts, so not amused.
- **u/timmeh1705** (↑7, 2026-10-19 09:57): Output quality wasn't amazing compared to GM 5.3 Flash but you can't deny it was good at looooooong running chains, it never stopped.
  - **u/jedruch** (↑1, 2026-10-19 11:50): On point - it is unbeatable for long running chains.
- **u/Durian881** (↑4, 2026-10-19 10:14): It ran well for agentic flow on MiniMax Code. Felt the quality was a bit worse than Qwen3.8-Flash-Next though. The writing style was better (more professional) than M3. Hopefully, there's improvement over the preview period with additional training data.

---

## I built Re-Claude, an open-source CLI coding agent powered by web-based Claude
**u/two35s** · 2026-10-19 09:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9s611/i_built_reclaude_an_opensource_cli_coding_agent/)

[removed]

---

## You can get the DeepSeek 1M context API for free
**u/Loud-Coach-2671** · 2026-10-19 08:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9rhn2/you_can_get_the_deepseek_1m_context_api_for_free/)

A new provider is giving out $20 in free signup credits. You can use them to use deepseek-v4.1-flash with a 1M context window, and it’s fast too, around 200 tokens/sec.

Here: [Coralbricks](https://www.coralbricks.ai/r/97K71G).

---

## Payment Decline opencode
**u/akuma-st0ic** · 2026-10-19 07:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9qs60/payment_decline_opencode/)

---

## OpenAI using deepseek v4.1
**u/Maleficent-Volume-81** · 2026-10-19 07:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9qq02/openai_using_deepseek_v41/)

Today a curious thing happened to me and not once, but twice. I was using opencode for a code task and suddenly this message appears.  
What does it mean?.

**Comentarios:**

- **u/DaviidC** (↑8, 2026-10-19 07:55): OpenAI created the API that MOST opensource use.
- **u/DeciusCurusProbinus** (↑2, 2026-10-19 08:10): Isn't that just the API endpoint that Opencode uses?
- **u/Popular-Penalty6719** (↑1, 2026-10-19 10:07): I think the question is valid and should not be downvoted. If "OpenAI Chat stream" means OpenAI-compatible chat stream using whatever model the user selected, that's at least bad UX and misleading.
  - **u/geearf** (↑1, 2026-10-19 12:34): How is it misleading?
    - **u/Popular-Penalty6719** (↑1, 2026-10-19 14:11): OpenAI did not end any chat stream. A service using a compatible interface did.
        An example, let's say I offer Apple hearphones and you come to me to buy new Apple headphones for your iphone and I offer you apple-compatible headphones. Would you be happy about that?
      - **u/geearf** (↑1, 2026-10-19 16:14): And my PC was not made by IBM.  
          So?
        - **u/Popular-Penalty6719** (↑1, 2026-10-19 16:52): Good luck 🤣

---

## Is it normal to have so much context tokens?
**u/AdNecessary8217** · 2026-10-19 07:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9qjsa/is_it_normal_to_have_so_much_context_tokens/)

---

## which one is opencode best model ?
**u/OrangeLimp9572** · 2026-10-19 07:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9qhaz/which_one_is_opencode_best_model/)

---

## inteligencia artificial open source gratis
**u/KitsuneUX** · 2026-10-19 07:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9qgbl/inteligencia_artificial_open_source_gratis/)

---

## [Release] opencode-models-discovery v2.0.0: Native OpenCode V2 support, host storage, and live model overrides now GA
**u/yu_hp** · 2026-10-19 07:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9pz92/release_opencodemodelsdiscovery_v200_native/)

Following up on last week's release candidate, `opencode-models-discovery` **v2.0.0 is officially released and published to npm** `latest`**!** 🎉

This major version promotes **OpenCode V2** to the primary, stable integration. It redesigns how the plugin interacts with the host around three clean boundaries:

# Highlights in v2.0.0:

1. **Native Integration Credentials**: Works seamlessly with OpenCode V2's `/connect` workflow. The plugin resolves credentials dynamically in memory—no raw API keys in `opencode.json` and no sniffing `auth.json`.
2. **Host-Managed Storage (**`ctx.storage`**)**: Caching and user overrides are separated cleanly into different namespaces. Clearing discovery caches will **never** delete your custom model preferences.
3. **Persistent Model Overrides**: Edit model display names, context limits, output tokens, reasoning flags, and variants directly via `/models-discovery-console`. Changes trigger an instant provider reload—zero service restart needed.
4. **Resilient Auto-Reload**: Subscribes to OpenCode V2 lifecycle events (`config.updated`, credential switches). If an upstream provider experiences a temporary network hiccup, the plugin keeps the last-known valid inventory instead of wiping out your available models.
5. **Decoupled RPC & TUI**: Commands and UI dialogs communicate with the background server via typed RPC, avoiding synthetic session injections or terminal blocking.
6. **OpenCode V1 Legacy Support**: Existing OpenCode V1 setups remain fully functional through the legacy adapter inside the same combined package.

# Quick Setup (opencode.json / opencode.jsonc)

    {
      "$schema": "https://opencode.ai/config.json",
      "plugins": [
        "opencode-models-discovery@2.0.0"
      ],
      "providers": {
        "my-gateway": {
          "name": "Local Gateway",
          "package": "@opencode-ai/ai/providers/openai-compatible",
          "settings": {
            "baseURL": "https://gateway.example.com/v1",
            // Optional: omit apiKey and manage via OpenCode's native `/connect`
            "apiKey": "{env:GATEWAY_API_KEY}",
            "modelsDiscovery": {
              "enabled": true,
              "modelInfoFormat": "models.dev",
              "cache": {
                "enabled": true,
                "ttlSeconds": 86400
              }
            }
          }
        }
      }
    }

# Useful Commands:

* `/models-discovery-refresh` — Manually trigger model discovery (supports `--force`).
* `/models-discovery-console` — Interactive browser for models, metadata inspection, cache clearing, and override editing.
* `/connect` — Securely set or rotate your provider credentials.
* **GitHub:** [https://github.com/yuhp/opencode-models-discovery](https://github.com/yuhp/opencode-models-discovery)
* **NPM:** [https://www.npmjs.com/package/opencode-models-discovery](https://www.npmjs.com/package/opencode-models-discovery)

Thanks to everyone who tested the RC releases! If you run into any issues or have feature suggestions, feel free to open an issue or drop a comment here.

---

## Deepseek V4.1 Flash 1017 in OpenCode! Yay!
**u/abhijithwarrier** · 2026-10-19 05:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9oydj/deepseek_v41_flash_1017_in_opencode_yay/)

https://i.redd.it/91fjc0a86dwh1.png

Guys, we have deepseek v4.1 1017 in opencode, coming soon. It's time to move some shit!.

**Comentarios:**

- **u/vishu143x** (↑15, 2026-10-19 06:25): it been there past 3 days , daily I am refreshing the same page , if they have released or not
  - **u/abhijithwarrier** (↑4, 2026-10-19 06:25): I have seen it today only, hope they release it. But the guys have been busy this weekend due to whole data breach situation.
- **u/thomas29needles** (↑8, 2026-10-19 06:40): Will it be available in Go?
  - **u/abhijithwarrier** (↑7, 2026-10-19 07:52): Usually it will be available in go primarily, then when they have enough capacity, they give out in zen free
- **u/sirloindenial** (↑3, 2026-10-19 07:30): Another full comprehensive audit code review🤓
  - **u/abhijithwarrier** (↑1, 2026-10-19 07:53): You bet!. I have already lined up my important tasks.. Tbh, this upgrade is a beast. I have tried the official api of deepseek and it's honestly good.
    - **u/look** (↑1, 2026-10-19 15:20): Yeah, I’ve not been a fan of previous Deepseek models in the 4.x series, but it looks like they did some real work on key weaknesses with this update.
        
        I expect I’ll be using this one a lot more.
      - **u/abhijithwarrier** (↑1, 2026-10-19 16:10): Yeah. For my tasks, which are not research engineering or scientific innovatins, this update is more than enough. Most people don't need Astra level model for daily uses. I just wanted to try so I used 5$ and got the official api. I'm more than happy with the performance.
- **u/Prestigious-Pea1306** (↑-4, 2026-10-19 07:51): Why is this still not available? It’s honestly frustrating. How long are we supposed to wait? This should’ve been available by now. Stop making users wait endlessly for features that should already be here.
  - **u/abhijithwarrier** (↑2, 2026-10-19 07:55): I know right? But we can't complain them also, coz they have been busy with the whole data breach situation lately, and you know them right, once they are back, they will put this out soon...but soon...also I just got to know, this was listing was there three days, exactly when the data breach notification came.
  - **u/No_Captain4899** (↑5, 2026-10-19 09:11): Bro it's been two days... You are getting 8 times more than you are paying and still asking for more. If you want it so much go pay your credit through the real api and you will be satisfied.
  - **u/Zealousideal_Aide787** (↑5, 2026-10-19 09:34): Do you really they are not aware of this and  not working on it? It's been 2 days, stop acting like a spoiled kid

---

## Ugh, Opencode has been such a total mess since the hack! First it kept complaining I wasn't using a opencode client, then hit me with http 500 errors, and now this. Anyone know what's even going on?
**u/FHSenpai** · 2026-10-19 04:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9novh/ugh_opencode_has_been_such_a_total_mess_since_the/)

---

## Deepest new model
**u/Silcord_Gaming** · 2026-10-19 04:24 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9nbr3/deepest_new_model/)

---

## Is the referral still works/available?
**u/CYCLONOUS_69** · 2026-10-19 03:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9m4pr/is_the_referral_still_worksavailable/)

---

## The 3 new "stealth" models if you were in 2025 - anyone remember the "3-Pokemon-codename" stealth OpenAI models on Windsurf
**u/ZealousidealTown1974** · 2026-10-19 00:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9ivmg/the_3_new_stealth_models_if_you_were_in_2025/)

https://i.redd.it/q4e7jn9mjbwh1.png

---
