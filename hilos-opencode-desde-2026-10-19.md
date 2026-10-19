# r/opencode — hilos 2026-10-19 → 2026-10-20
_Generado: 2026-10-19T18:05:26.652994+00:00 · 64 hilos · 280 comentarios · fuente: Arctic Shift_

## Can I use opencode API on Deepseek harness and use the free models?
**u/Top-Royal5255** · 2026-10-19 18:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa43vb/can_i_use_opencode_api_on_deepseek_harness_and/)

I did what is said in the title. Made an API key and added it to deepseek harness and was added and I can filter tot he free models.

  
I chose one and send a prompt and get different error code on all free models.

  
Anyone that can help me.

---

## I let MiniMax M3.1 free control my 3D printer and I'm genuinely impressed with it's judgement
**u/BotSympathiser** · 2026-10-19 17:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa41al/i_let_minimax_m31_free_control_my_3d_printer_and/)

[removed]

---

## OpenCode got me banned from github... any tips?
**u/AlfieLionel** · 2026-10-19 17:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa3q5y/opencode_got_me_banned_from_github_any_tips/)

As title says. I told my OpenCode agent to scrape all of the URLs in my DB and gave it a VPS. It then proceeded to scrape those 4,000,000 URLs using several sharded GitHub Actions, completely breaking ToS and getting my account (with all of my personal and professional projects!) promptly suspended. Any advice? 

https://i.redd.it/vezsbectogwh1.png

---

## Reran the Space Bunny horse prompt on released M3.1 Flash, max variant
**u/No-Log9919** · 2026-10-19 16:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa1y6t/reran_the_space_bunny_horse_prompt_on_released/)

Space Bunny got confirmed today as an earlier version of MiniMax-M3.1-Flash. I saw the announcement and reran the horse prompt from that thread a few weeks back on the released model, max variant. One prompt, no follow-ups, no manual edits.

turns 183  
input (uncached) 52,536  
output 72,280  
thinking 102,356  
cache read 27,620,499  
total 27,847,671  
tool calls 184  
wall time 36 min 56 s

At the API price that's about fifty cents.

    Create a low-poly 3D horse running in a seamless loop using Three.js. Build it procedurally from primitive geometry, animate the legs, body, head, and tail, and return a single self-contained HTML file.
    
    Do your best, you are being rated against other AI models.
    

It pixel-diffed the first and last frame of a stride to verify the loop is seamless. The trick is it keeps the horse in place and slides the ground past at the speed of the planted hooves.

Result is a chestnut horse with a saddle pad, bridle, and one white sock galloping in place. Dust kicks up at the hooves, dry plain with grass tufts and rocks, hazy mountains in the distance, camera slowly orbiting. On-screen hints for drag, zoom, pause, camera cycle.

If you ran this same prompt on the earlier version a few weeks back, how did yours turn out?

---

## 🔥 DeepSeek V4.1 Flash updated to 1017 in OpenCode Go and Free
**u/afanasenka** · 2026-10-19 16:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa1qy7/deepseek_v41_flash_updated_to_1017_in_opencode_go/)

---

## lo trovo già MiniMax-M3.1-Flash ?
**u/Wise_Shame_2853** · 2026-10-19 16:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa1dki/lo_trovo_già_minimaxm31flash/)

---

## Token Usage in OpenCode with External Provider
**u/boiref** · 2026-10-19 15:45 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa0euk/token_usage_in_opencode_with_external_provider/)

Hey guys, a bit newbie in this agentic stuff.

If I subs for GPT or Claude (their usual monthly subs) and then connect it with OpenCode (so that I can flip easily + use their free/Go subs), will it be more expensive in terms of token usage vs their own native CLI/desktop app?

For ex: For same prompt, will it be more expensive to talk through GPT 6 or Opus 5.5 from OpenCode vs Codex/Claude Code?

**Comentarios:**

- **u/Rick_C135** (↑1, 2026-10-19 16:10): No, OpenCode isn't inherently more expensive in terms of tokens, but it can consume your subscription limits faster depending on how you use it.
    
    There are two important distinctions:
    
    1. ChatGPT Plus/Pro → OpenCode
    
    OpenCode officially supports signing in with your ChatGPT subscription. You don't need to pay separately for API tokens.
    
    * OpenCode and Codex draw from your subscription's usage allowance.
    * The same prompt can consume different amounts of usage because each tool has its own system prompts, context management, tool calls, and agent workflows.
    * OpenCode isn't automatically less efficient, but plugins, subagents, and repeated tool calls can increase consumption.
    
    So you're not paying extra just because you're using OpenCode.
    
    OpenCode
    
    \+1
    
    
    
    2. Claude Pro/Max → OpenCode
    
    This is where things get tricky.
    
    Anthropic no longer officially supports using Claude Pro/Max subscription authentication directly in OpenCode. OpenCode removed its built-in integration, and third-party OAuth workarounds carry account risks.
    
    You can still use Claude models through an Anthropic API key, but that's billed separately based on token usage.
    
    OpenCode
    
    \+1
    
    
    
    3. Which one is more token-efficient?
    
    For an identical coding task, neither Codex nor OpenCode is guaranteed to use fewer tokens.
    
    The biggest differences come from:
    
    * How much conversation and repository context gets sent.
    * Prompt caching efficiency.
    * How many tool calls and retries the agent makes.
    * Whether you're running additional agents or plugins.
    
    My recommendation: If you want one interface for switching between models, OpenCode is a solid choice. Use your ChatGPT subscription directly, connect Claude through an API if needed, and use free models for simpler tasks.
    
    Just remember: a $20 subscription doesn't give you $20 of unrestricted API usage, and subscription limits aren't necessarily measured the same way as API tokens.
- **u/lincolnthalles** (↑1, 2026-10-19 16:25): You shouldn't connect a Claude Code sub to OpenCode or any other harness. Their ToS doesn't allow it, and they monitor the system prompt, meaning you can be banned. 
    
    Google does a similar thing with Antigravity.
    
    The only way to use their models outside their harness is via direct API or to use a sub from another provider that includes their models.
    
    On the other hand, you can use an OpenAI sub with no issues on any harness. They allow it, and you are likely to save a few tokens, as OpenCode V2 utilizes a minimal system prompt. Note that this will also make OpenAI models behave differently than when running inside Codex.
    
    T3 Code is the closest thing that allows you to mix a Claude sub, as it still uses Claude Code/Codex/OpenCode/Muse Code/Gemini under the hood. It auto-handoffs when you switch the provider. The main issue is that it's not practical to customize anything harness-specific with this workflow. You can only seamlessly share skills and the global AGENTS.md file between harnesses.

---

## What would make M3.1-Flash your default OpenCode model?
**u/Temporary-Tie-8734** · 2026-10-19 15:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa05mq/what_would_make_m31flash_your_default_opencode/)

M3.1-Flash is already showing up pretty high in OpenCode usage, but I’m less interested in the ranking than whether the release version is actually good enough to become someone’s everyday model.

For coding, “fast” isn’t enough by itself.

I’d care more about fewer retries, clean repo edits, following constraints, not wandering once the context gets long, reliable tool use, and the total cost of getting a task finished.

Space Bunny gave people an early look at the model, but it was an early version, so I wouldn’t treat those results as identical to M3.1-Flash today.

I’d like to rerun some of the same OpenCode tasks on the release version and see what actually changed.

Anyone tried both yet? What difference are you noticing between M3.1-Flash and Space Bunny?

**Comentarios:**

- **u/xRebellion_** (↑1, 2026-10-19 16:24): If it's more expensive than deepseek and/or not fill a specific niche I don't see myself using it. Will probably use it for personal benchmarking on my tool set but nothing else

---

## "AI will take over human j*bs", meanwhile Al-
**u/Friday_99** · 2026-10-19 15:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xa02y7/ai_will_take_over_human_jbs_meanwhile_al/)

So, I asked my agent to create a demo replay so that I can test how the frontend animations are working out without actually running the whole application. I mentioned in the instructions to create a button labelled "demo" too

It wrote the script and made a few more changes, but did not add the button to the frontend. I questioned it about the button and it started tweaking out hard.

I used the GLM-5.3-flash model under the go subscription for this.

**Comentarios:**

- **u/acakaacaka** (↑2, 2026-10-19 15:35): Lol AI is now protesting the cost of living
- **u/reybrujo** (↑1, 2026-10-19 15:37): Happens from time to time. Still AI gets in a loop such at that less times than a human goes to the bathroom during the day, so they might still take your job.
- **u/Technocratix902** (↑1, 2026-10-19 15:46): Do not use max reasoning. Only go upto high or Xhigh - no more.
- **u/Cute_Obligation2944** (↑1, 2026-10-19 15:50): Demo
- **u/migsperez** (↑1, 2026-10-19 16:04): Could this be an indicator of low quantization?

---

## Bring muse-spark 1.3 back
**u/Secure-Turnip6589** · 2026-10-19 15:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9ztgg/bring_musespark_13_back/)

---

## Bring muse-spark 1.3 back
**u/Secure-Turnip6589** · 2026-10-19 15:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9ztax/bring_musespark_13_back/)

Like many of you, I'm completely gutted that Muse Spark 1.3 was removed from OpenCode due to hosting costs and API errors. It was easily my favorite model to use.

Instead of just complaining, we should push the developers to add a **BYOK (Bring Your Own Key)** gateway for it. That way, OpenCode doesn't have to foot the server bills, and those of us who love the model can just plug in our own API keys to keep talking to it.

If you want to organize a coordinated feature request for this, I am setting up a dedicated Discord server so we can get the devs' attention peacefully and effectively. Drop a comment if you want in, and let's get Muse Spark back!

**Comentarios:**

- **u/Soifon99** (↑9, 2026-10-19 15:28): it's not gone? it's in GO, but you have to PAY for it.   the saying a beggars can't be  chooser does not work for people who are freeloading off off good models.
  - **u/Secure-Turnip6589** (↑-7, 2026-10-19 15:29): Proof?
    - **u/Soifon99** (↑4, 2026-10-19 15:32): i'm looking at it in opencode. with a go key.   they only removed the free one.  ok BUT, i see it's limited region.  so maybe you are not in the right region..   check the website on opencode.  and see if it's in the model list for you.
- **u/Professional_Price89** (↑2, 2026-10-19 15:31): If you think about byok why not connect directly with Meta API?
- **u/ArC3488** (↑3, 2026-10-19 15:34): You can literally do that right now. Better yet, get OpenRouter and use muse 1.3 spark from there. Might want to check and make sure you're using the cheapest possible provider
- **u/acakaacaka** (↑1, 2026-10-19 15:35): It's there in the go model?
- **u/Secure-Turnip6589** (↑0, 2026-10-19 15:38): "Using OpenRouter or the Meta API directly is definitely the best workaround right now. But the whole reason a lot of us love OpenCode is having our workspace, benchmarks, and extensions in one clean hub. If OpenCode implements a native BYOK gateway, we get the best of both worlds: our favorite UI plus custom cost management. Let's push the devs for official BYOK integration!"
     [
    1, 
    2]
  - **u/FZRP2** (↑1, 2026-10-19 15:58): you can vibe code the thing yourself its an open source software
- **u/ai_ton** (↑1, 2026-10-19 15:42): o muse spark 1.3 me ajudou bastante no free  
    vou assinar o GO mais por ele
- **u/mmeister86** (↑0, 2026-10-19 15:45): Man, just pay for it if you love it so much. The API is dirt cheap, and even their coding plans are really good (right now). I'm on the $50 plan and it seems virtually unlimited
  - **u/Secure-Turnip6589** (↑1, 2026-10-19 15:49): Cheap? Are you kidding? 2,2k 
      hryvnias is 50 dollars this is not dirty cheap in Ukraine man
    - **u/VegeterianMeatEater** (↑1, 2026-10-19 16:05): Wat? Go is $10
    - **u/mmeister86** (↑1, 2026-10-19 16:12): Compared to Claude or OpenAI it's dirt cheap, yes.
    - **u/mmeister86** (↑1, 2026-10-19 16:13): Also the $50 is literally their most expensive one, they got a $5 plan available
- **u/FZRP2** (↑1, 2026-10-19 15:55): opencode is open source you literally can vibe code the thing yourself and ask the agent to combine and compile it. 
    
    magic of open source :)
- **u/Hades720g** (↑1, 2026-10-19 16:31): use the contributor mode directly from Meta its only .10 c  million tokens

---

## OpenCode is great in the terminal — but it goes invisible the moment you run more than one agent. So I built a desktop cockpit for it.
**u/Marcot3ssar1** · 2026-10-19 15:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9zma9/opencode_is_great_in_the_terminal_but_it_goes/)

[removed]

---

## “Free limit exceeded” on OpenCode without even using the free models?
**u/SammyTDS** · 2026-10-19 15:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9zlvg/free_limit_exceeded_on_opencode_without_even/)

Hi everyone

I usually use OpenAI models through opencode's connector, but after hitting my usage limit, I decided to try some of the free models instead.

And opencode hit me with the “Your free limit has been exceeded”

Is anyone else experiencing this? Any solutions would be appreciated.

---

## How much usage will I get on the 10$ plan?
**u/Facci_** · 2026-10-19 14:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9yov3/how_much_usage_will_i_get_on_the_10_plan/)

Thinking of having a third subscription, I am eyeing on GLM5.3, Deepseek V4.1, and Muse. I have a Claude and Codex subscription, though Codex has pretty bad limits (though they do keep giving resets all the time) and Claude gives a lot for 20$, I'd like to dive on these models for my suite. Any anecdotals notes on how much you fellow Go subscription users get? How much it is relative to the other subscriptions?

**Comentarios:**

- **u/Mixermachine** (↑3, 2026-10-19 14:48): With the recent changes you again get a lot out of Deepseek v4.1.  
    80$ API usage seemingly -> [https://opencode.ai/de/go#:\~:text=120%C2%A0%24-,DeepSeek%20V4.1%20Flash,-34.670](https://opencode.ai/de/go#:~:text=120%C2%A0%24-,DeepSeek%20V4.1%20Flash,-34.670)
    
    If you stay on that you will have a hard time filling the limits (if you don't fire all day).
    
      
    I use Qwen3.8-Flash and GLM5.3-Flash mainly.  
    Works pretty well for me.  
    I would recommend just giving it a try.
- **u/SpookyKipper** (↑3, 2026-10-19 14:48): [https://opencode.ai/v2/docs/console/go/#usage-limits](https://opencode.ai/v2/docs/console/go/#usage-limits)
    
    DeepSeek v4.1 flash is practically unlimited for me.
- **u/ShallotMotor2551** (↑1, 2026-10-19 14:56): The models you selected should give you plenty of usage. Just don't use the top tier models like Kimi K3, then it is gone quite fast, of course. Check [https://opencode.ai/v2/docs/console/go/#usage-limits](https://opencode.ai/v2/docs/console/go/#usage-limits) for limits.
- **u/Lap202pro** (↑1, 2026-10-19 15:05): I went through 25% of my usage with 5 hours of Gemini 4 Argon. Have been using Mimo-v2.6-pro and have gotten a ton of stuff done the past 3 days for like 16% usage. Deepseek I believe has great limits if you aren’t trying to run it 24 hours a day.
    
    Just look at the models and watch your usage. I’ll likely switch from mimo around 60% of my monthly and run on deepseek till it refreshes, but mimo has been great
- **u/IndividualPlus2011** (↑2, 2026-10-19 15:19): You can look at the second table I made here [https://www.reddit.com/r/codex/s/by5S7ouPlE](https://www.reddit.com/r/codex/s/by5S7ouPlE)
- **u/ollm-tux** (↑4, 2026-10-19 15:27): https://reddit.com/link/phpni9z/video/22yhh94uzfwh1/player
  - **u/eachDayIWakeUp** (↑1, 2026-10-19 15:54): wtf is this theme hahahahhaha
    - **u/ollm-tux** (↑2, 2026-10-19 16:17): :) xp coz I m nostalgic and very very old, first my pc was zx spectrum
- **u/AdAlternative5694** (↑1, 2026-10-19 15:55): My usage is 97% now. The number of tokens used is 8B tokens, mostly on DeepSeek. This number can vary and can be 10B i assume after deepseek limit increase and usage of free models

---

## 🚀 Built an open-source Notion alternative in 4 days using AI coding tools!
**u/Register_Defiant** · 2026-10-19 14:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9yomd/built_an_opensource_notion_alternative_in_4_days/)

I recently worked on **Noema**, an open-source, self-hosted productivity workspace designed to bring notes, documents, databases, and project management together in one place.

The idea is to create a flexible workspace where users can manage their work while maintaining control over their own data.

🔥 **Some of its main features:**

* 📝 Rich-text document editing with blocks, tables, equations, and more
* 🗃️ Databases with 7 views: Table, Board, List, Gallery, Calendar, Timeline, and Chart
* 📊 Project management with tickets, milestones, and sprint tracking
* 🤖 AI-powered writing, summarization, and workspace Q&A
* 🤝 Collaboration features, including comments, sharing, and permissions
* 🖥️ Web app and installable Windows desktop app
* 🔐 Self-hosting for greater control over your data

🛠️ **Tech stack:** Next.js, React, TypeScript, Tailwind CSS, Prisma, PostgreSQL, TipTap, and Tauri.

The project is open source under the MIT license, and it was built in just **4 days with the help of AI-assisted development using OpenCode**.

🔗 GitHub: [https://github.com/Guembri01/noema](https://github.com/Guembri01/noema)

This was an interesting experiment in rapid development and exploring how AI coding tools can help bring a project to life.

I'm sharing it here to get some honest feedback from the community.

**What do you think about building full-featured applications with AI coding tools? And what would you build in 4 days?**

I'd love to hear your thoughts! 🚀

---

## I use Claude Code to build the system and cheap OpenCode models to do the work
**u/root0ps** · 2026-10-19 14:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9yjsw/i_use_claude_code_to_build_the_system_and_cheap/)

I’ve been running two agents in one repo for a few weeks, and splitting their roles has helped more than picking better models.

**The split**

Claude Code owns the system: rules, templates, check scripts, agent configs. It never makes a deliverable itself.

OpenCode (Go subscription) does the production work from a written brief, runs the checks until they pass, and commits its own files.

I review everything before it ships.

**Defects become checks**

When something slips past the checks, I don’t fix it by hand. It goes on a backlog, and Claude Code turns it into a new check or template rule so it can’t happen again. Then the cheap model re-runs the piece. Over time the checks get stricter and the cheap models have fewer ways to fail.

**What helped**

One AGENTS.md that every tool reads, so switching agents is painless.

A fixed brief format. The cheap model only chooses wording. Bad output usually means a thin brief.

A second model reviews, and a pre-commit hook runs the checks.

Work in batches, because every cold start reloads the whole project context.

**Next**

Letting Claude Code hand out the work too: it writes the brief, runs opencode run and reads only the check results. I’m also trying a few models on the same brief to see which one passes fastest.

If you run a setup like this, how do you handle the handoff? Plain scripts, an orchestration tool, something else? Is there a tool you’d add to this setup?

---

## How are you optimally using LongCat 2.5 Preview Free and Beam Free in OpenCode Go?
**u/letuslisp** · 2026-10-19 13:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9x8yt/how_are_you_optimally_using_longcat_25_preview/)

Hey everyone!

I'm using OpenCode Go and noticed that **LongCat 2.5 Preview Free** and **Beam Free** are both currently available with unlimited usage.

I'm curious how people are actually getting the most out of these two models.

And also their experiences (are they really unlimited)?  
  
For those of you who have been using them regularly:

* **What tasks does each model work best for?** For example, planning, codebase exploration, debugging, implementing features, refactoring, tests, or simpler repetitive coding tasks.
* **What prompting techniques work well?** Do you use specific instructions, planning workflows, custom agents, or other configurations to improve their results?
* **How reliable are they with tools?** Do you let them edit files and run commands autonomously, or do you keep them on a shorter leash?
* **How do you avoid loops, bad edits, and wasted time?** Have you found effective ways to handle these issues?
* \*\*Do you use either as your main coding model, or do you combine them with other models in a particular workflow?

I'd especially appreciate concrete examples of workflows, prompts, and configurations that have worked well for you, rather than just general impressions.

Since usage is unlimited for now, I'm wondering how best to take advantage of that without sacrificing code quality or spending time undoing bad changes.

Thanks!

**Comentarios:**

- **u/absurdother** (↑2, 2026-10-19 13:48): Beam: very quick, multi-file and folder management, work on text files/mds fast, earn context, organize.  
    LongCat: context compaction, fast review; I go for it when other models stream fail or are already maxed out.
    
    Both ok at reasoning on basic tasks

---

## What is going on???
**u/Mental_Mousse_7143** · 2026-10-19 13:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9x3yd/what_is_going_on/)

I asked GLM-5.3-flash free to implementing a feature in my code and then this shown up suddenly??? I didn't ask it to write a story!!!!:

https://i.redd.it/fxwd5q42gfwh1.png

**Comentarios:**

- **u/Mental_Mousse_7143** (↑1, 2026-10-19 13:39): and now I cannot work with it anymore, it only care about the story!!!
- **u/dumbasPL** (↑6, 2026-10-19 13:56): Did you just get prompt injected by a repo that doesn't like AI "contributions" LMAO. If this is not your repo, you should probably check agents.md and stop if they don't like slop.
  - **u/Soifon99** (↑2, 2026-10-19 14:06): this would be funny if it's true.
  - **u/Mental_Mousse_7143** (↑1, 2026-10-19 14:28): it is my repo, and everything went ok a few week ago until this story. I changed the model to deepseek 4.1 flash to continue and it works now.
- **u/Defiant_Nerve_5042** (↑1, 2026-10-19 13:57): How i do to have access GLM-5.3-flash free ?
- **u/power10010** (↑1, 2026-10-19 14:01): Lol
- **u/diaracing** (↑1, 2026-10-19 14:09): Please, hand it over to me. It was printed at your public TUI by mistake.
- **u/hillman_avenger** (↑1, 2026-10-19 14:23): Is it in your agents.md or something?
  - **u/Mental_Mousse_7143** (↑1, 2026-10-19 14:29): No, it seems like it was answering another guy after a few api call errors.
- **u/Unlikely-Places** (↑0, 2026-10-19 14:37): You are vibe coding too much, take a break and go hug a tree

---

## Slow cheapseek
**u/InstructionFar3749** · 2026-10-19 13:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9x14d/slow_cheapseek/)

any other provider i can use with better TPS?

**Comentarios:**

- **u/IISomeOneII** (↑1, 2026-10-19 13:51): yes, official deepseek 😹
- **u/Academic-Sentence-34** (↑2, 2026-10-19 14:08): Openrouter was providing me with approximately 400TPS earlier today. Ollama, on the other hand, offers around 240TPS, but its performance drops to 130TPS during peak hours.
  - **u/eachDayIWakeUp** (↑1, 2026-10-19 15:57): and here I am, happy with an average of \~40TPS using Longcat 2.5 😄
- **u/Adventurous_Re** (↑1, 2026-10-19 14:29): You can use the official harness of minimax and qwen they give free token usage aswell
    
    In your current project you have to setup handoff after major works so even if your projects are shared between harness or models it will work flawlessly

---

## do you work in parallel on once repo or sequantial?
**u/RoofTall6762** · 2026-10-19 13:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9x0qp/do_you_work_in_parallel_on_once_repo_or_sequantial/)

[removed]

---

## I created this page to keep up with the pace of changing AI, so please look at how it is and let me know your feedback. ainews-smel.vercel.app
**u/Silcord_Gaming** · 2026-10-19 13:14 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9wl0l/i_created_this_page_to_keep_up_with_the_pace_of/)

---

## Multi LLM Subscription - Hermes and Opencode
**u/lawfulcrispy** · 2026-10-19 13:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9wctk/multi_llm_subscription_hermes_and_opencode/)

I'm looking for real user experiences with these 4 providers:

\-OpenCode Go  
\-Deeprelay (Base or Plus)  
\-Command Code GOAT  
\-OpenDesign Go

I want to use them with both OpenCode and Hermes Agent.   
How is the experience in practice? Any issues with setup, stability, or model quality?   
Also, how is the actual usage limit? Is the quota enough for daily use, or do you hit limits quickly?Which one would you recommend, and why?

---

## Opencode Setup help
**u/Dry-Smell436** · 2026-10-19 12:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9vvdr/opencode_setup_help/)

I am building a product, i have claude pro , but that doesn't seem sufficient, thought of using opencode to use some free models to reduce workload, help me for the setup and how can i efficiently use it, .

Please help me

**Comentarios:**

- **u/Complete_Comb_2167** (↑1, 2026-10-19 12:58): I’ve tried creating a skill to be able to leverage opencode’s cli.  
    Instruct claude to build it for itself to use it as an implementation agent in a way that it can monitor and nudge to get the implementation right.  
    Typically my workflow is creating a spec and implementation plan using claude and then asking it to hand it off to opencode agents to get it implemented. Claude reviews it at the end.
    
    If you’re able to somehow get your hands on gemini pro. You can try using antigravity similarly as well. As long as any service has cli it can be triggered and be used from claude code.
    
    If you’re serious about the product i’d suggest you to get opencode go for 10$. Its value for money. its got muse 1.3 - absolute bang for the buck (as long as you’re ready to sacrifice your data)

---

## Is the new Space Bunny gone?
**u/JackFrost0c** · 2026-10-19 12:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9vovt/is_the_new_space_bunny_gone/)

**Comentarios:**

- **u/migsperez** (↑3, 2026-10-19 12:41): [https://x.com/MiniMax\_AI/status/2112150867868541221](https://x.com/MiniMax_AI/status/2112150867868541221)
- **u/Xiaomin4114** (↑3, 2026-10-19 12:41): Revealed to be Minimax M3.1 flash, which wasn't very surprising. a lot of people already guessed.
- **u/LinkiooN** (↑2, 2026-10-19 13:13): there's a free M3.1 Flash model, so I think it's the replacement

---

## Tokless: 30-second all-in-one toolkit for OpenCode — Zero setup, minimal MCPs, token-efficient tools (CodeGraph, Context-Mode, Project Memory, Headroom, RTK, Caveman, Ponytail)
**u/Strict_Grocery9693** · 2026-10-19 12:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9vk6t/tokless_30second_allinone_toolkit_for_opencode/)

[removed]

---

## 🔥 MiniMax M3.1 Flash (Space Bunny) is FREE on OpenCode for 3 days
**u/afanasenka** · 2026-10-19 12:20 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9vegj/minimax_m31_flash_space_bunny_is_free_on_opencode/)

**Comentarios:**

- **u/Interesting-Movie452** (↑3, 2026-10-19 12:25): is it better than ds 4.1
  - **u/OnderGok** (↑5, 2026-10-19 12:26): Even better than 1017?
    - **u/kabir_sharma_sans** (↑0, 2026-10-19 12:53): yes
      - **u/No_Committee8392** (↑1, 2026-10-19 14:41): Arguable
          
          M3.1 flash is a good model though no argument but I wouldn’t call it better than dsv4.1f
  - **u/xRebellion_** (↑4, 2026-10-19 12:53): Space bunny was good for me, but not ds 4.1 level imo. Don't know whether they have improved it or not.
  - **u/MLGSW4G** (↑1, 2026-10-19 13:36): For me, DeepSeek V4.1 Flash was noticeably better for writing a Bevy game, likely depends on specific task
  - **u/YoRt3m** (↑1, 2026-10-19 15:29): No
- **u/viitorfermier** (↑6, 2026-10-19 12:39): I use daily minimax m3 and it's super good. I'm curious about M3.1 if it's even better :)
  - **u/davienzs** (↑4, 2026-10-19 12:43): This is 3.1 flash not 3.1
    - **u/viitorfermier** (↑1, 2026-10-19 13:23): aa ok
  - **u/Unusual-Customer713** (↑2, 2026-10-19 13:58): better than M3 alot a lot imo
- **u/DreamProgramming** (↑1, 2026-10-19 16:36): Rocket nice

---

## MiniMax M3.1 Flash (Space Bunny 🚀) benchmarks... 😁
**u/afanasenka** · 2026-10-19 11:55 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9uuxq/minimax_m31_flash_space_bunny_benchmarks/)

Cowork (Automation-Bench: 62%; ALE: 30%)

Coding (DeepSWE: 74%)

Visual Understanding (BabyVision: 91%), at 1/3 the cost of M3 and 3x the speed.

**Comentarios:**

- **u/RepulsiveRaisin7** (↑64, 2026-10-19 12:00): It's time to retire benchmarks. This thing is worse than GLM Flash
  - **u/No_Gold_4554** (↑6, 2026-10-19 12:04): agreed
  - **u/ApprehensiveDelay238** (↑13, 2026-10-19 12:24): Benchmarks is the best thing we have for objective measures. It's not perfect and it doesn't capture everything that goes in training an LLM but it does quantify important metrics of agentic performance.
  - **u/Eyelbee** (↑5, 2026-10-19 12:24): Maybe that was the alpha version?
  - **u/Writer00100** (↑3, 2026-10-19 12:28): Agreed
  - **u/Yayman123** (↑3, 2026-10-19 12:51): They said on Twitter that Space Bunny was "an early version". Maybe it's better than it looks?
  - **u/Kaan-M** (↑1, 2026-10-19 13:18): I think so.
  - **u/Sovairon** (↑2, 2026-10-19 13:35): I have both minimax and glm subscriptions, I have been using the preview for a while already. from what I experienced so far on my use cases minimax flash does better than glm flash.
    - **u/RepulsiveRaisin7** (↑1, 2026-10-19 13:39): Have you used Space Bunny too? Maybe they served at worse quant on the free endpoints. I'm skeptical but I might give it another shot.
      - **u/Sovairon** (↑1, 2026-10-19 14:24): The only model I tried is 3.1 Flash Preview provided by minimax
  - **u/zyxciss** (↑1, 2026-10-19 15:46): This model was **WAY too lazy, even at Max effort** Benchmarks don’t tell the whole story
      
      I tested Muse Spark side by side with other models on a real project it took 48 mins which was just out of the 30 mins mark : completing a partial LRU cache implementation. I also ended up writing the implementation myself so I could compare the results and see whether AI models could genuinely replace my work.
      
      Here’s how it went:
      
      * **Claude Opus 5.5, Sol 6.1, and Argon 4:** All finished in under 30 minutes.
      * **Gemini 3.8 Flash:** Took 3 hours.
      * **Space Bunny (M3.1 Flash) :** Still hasn’t completed the task after 15 days.
      * **Me, as a human:** Finished it in 1.5 days, writing around 2,800 lines of code.
      
      This is why I think real-world coding tasks matter more than benchmarks alone. A model can look impressive on paper, but how well does it actually perform when given a real engineering problem
      
      Also Deepseek v4.1 Flash , GLM 5.3 Flash weren't able to do it too , looking forward for the new DeepSeek endpoint i got hopes :) Actually no open model pulled it off
    - **u/RepulsiveRaisin7** (↑1, 2026-10-19 15:57): You do have to keep in mind model size, these are Luna/Terra tier. And the gap has shrunk, but it still exists. Try the regular GLM 5.3, you might be surprised (or not).
        
        A bad model is never going to solve a hard task, no matter how much time you give it.
- **u/LazyLoser006** (↑3, 2026-10-19 12:05): WTF
- **u/GCP_Biryani** (↑19, 2026-10-19 12:06): BenchMAXXED
- **u/diaracing** (↑14, 2026-10-19 12:08): I can fabricate any benchmarks measures because nobody was there when I tested any piece of crap.
- **u/ivej** (↑3, 2026-10-19 12:09): Brother what??
- **u/honglac3579** (↑10, 2026-10-19 12:09): I think space bunny is good, but not that good though
- **u/YogurtExternal7923** (↑2, 2026-10-19 12:15): The benchmaxxing overlords nobody cares bru
- **u/andrewlvd** (↑4, 2026-10-19 12:25): All that dev just to be below 1017 lol
- **u/cypherbits** (↑3, 2026-10-19 12:27): Space bunny is worst than the first version of deepseek v4
- **u/WOLF_FOSSIL** (↑2, 2026-10-19 12:28): Zero people care.
- **u/siotong2798** (↑7, 2026-10-19 12:28): lol they are tripping, its not that good
- **u/ConsistentGent** (↑3, 2026-10-19 12:37): Yeah right 😂
- **u/AcrobaticToaster1329** (↑5, 2026-10-19 12:44): Yay distillated benchmaxxing
- **u/totoer008** (↑5, 2026-10-19 12:46): I am sorry I use a lot of free models. Step 5 on work buddy is good. DeepSeek on work buddy is good. DeepSeek on open code is good but context is trash. This one, is trash on freebuff and open code. It created so many errors. Worse one is nematron 3.5 light but man come on
- **u/PhotographIcy7588** (↑3, 2026-10-19 12:47): BenchMiniMaxxed
  - **u/Kaan-M** (↑2, 2026-10-19 13:17): lol
- **u/Amarsir** (↑1, 2026-10-19 13:19): They took their time to announce what we all knew. 
    
    I've been saying it's "in the zone" and I stand by that. Depends on pricing if it's worth using or not.
- **u/archerallstars** (↑1, 2026-10-19 13:20): It's probably worse than the respectable (but dated) M3 model. M3 has a very low hallucination rate, usually the leader in this aspect. Now M3.1 Flash is only 2nd behind DeepSeek to which has always been the most hallucinated model in the market.
    
    [https://artificialanalysis.ai/models/comparisons?compare=minimax-m3-1-flash%2Cgrok-4-7%2Cmimo-v2-6-pro%2Cmimo-v2-6-flash&omniscience=omniscience-hallucination-rate](https://artificialanalysis.ai/models/comparisons?compare=minimax-m3-1-flash%2Cgrok-4-7%2Cmimo-v2-6-pro%2Cmimo-v2-6-flash&omniscience=omniscience-hallucination-rate)
    
    Worse yet, it's a verbose model, burning context like hell like DeepSeek, hence actually more expensive per task than MiMo... API pricing alone doesn't tell the whole story.
- **u/Master_Border_2913** (↑1, 2026-10-19 13:55): benchmax 3.1 flash
- **u/arielif1** (↑1, 2026-10-19 13:58): sorry, this model is not as good as v4.1f release, let alone 1017, or glm 5.3. It's good, don't get me wrong, but currently minimax is far behind the whale and zhipu.
- **u/Candid_Historian2961** (↑3, 2026-10-19 14:10): Space Bunny was high (as in on something, high). Now, they just cheated to achieve high scores. That model was puking while thinking with lots and lots of gibberish into debug, no way it is sane, and no way it as good as those numbers showing, at least the free one they put into opencode. I used it with more ~2-3B usage tokens but it couldn't even build a simple SSO part of an application, even with just LDAP/Kerberos.
- **u/Money-String4165** (↑1, 2026-10-19 14:38): I have found it to be really strong when you tell it exactly what to do.  It definitely hallucinates and struggles at times.  I find it to a good cheap work horse while opencode/code command bring 4.1 flash 1017 online for cheap.
- **u/FUSCHiA15** (↑2, 2026-10-19 14:39): Space bunny is good for fast iterations, but I noticed that it doesn't really hold context really well. It sometimes decide on it's own when even specifically said to only present a plan, forgets that it's supposed to this and the like.
- **u/Sadlyf68** (↑2, 2026-10-19 14:45): Space bunny was actually really good
- **u/LarDark** (↑2, 2026-10-19 15:12): I tried Space Bunny last night and it broke a whole project deleting the main files out of nowhere... so yes, deepseekv4.1 1017 it is for me
- **u/lordcohliani** (↑3, 2026-10-19 15:34): Benchmaxed to the extreme. This thing is nowhere near as good as DeepSeek
- **u/Saderius** (↑1, 2026-10-19 16:11): That thing was unusably stupid

---

## I made opencode v2 read my plan quota and type what I                                                       say
**u/LeonVeganMan** · 2026-10-19 11:36 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9uhoc/i_made_opencode_v2_read_my_plan_quota_and_type/)

# Two opencode v2 TUI plugins: a plan/context meter and Groq dictation

I use opencode v2 all day and ended up writing two small TUI plugins. Both MIT, both on npm, no config entry needed.

**opencode-go-meter** — your session context usage and your OpenCode Go plan windows in the sidebar, plus a forecast of where the current pace lands by each reset. Rows are clickable: the title opens a settings dialog where you can turn the panel and the footer on or off. It replaces the built-in context/footer blocks, so disable those in `cli.json` (`"disabled": ["-opencode.sidebar.context", "-opencode.prompt.footer"]`) or you'll see the numbers twice.

**opencode-groq-dictate** — press `alt+v`, speak, press `alt+v` again. The take goes to Groq's `whisper-large-v3-turbo` and the transcript is pasted into the prompt at the cursor, ready to edit. `esc` throws a take away without uploading it. The panel shows state, model, language, today's spend and requests left: RPM is tracked locally (20/min), the daily number comes straight from Groq's response headers, so checking the quota doesn't cost a request. A free Groq key is enough.

Install — clone into the plugins folder and restart the TUI:

```bash
git clone https://github.com/LeonVeganMan/opencode-go-meter \
  ~/.config/opencode/plugins/opencode-go-meter

git clone https://github.com/LeonVeganMan/opencode-groq-dictate \
  ~/.config/opencode/plugins/opencode-groq-dictate
```

Plugins are discovered from `~/.config/opencode/plugins/<name>/`; there is no hot reload, so restart opencode after cloning.

- go-meter: https://github.com/LeonVeganMan/opencode-go-meter · https://www.npmjs.com/package/opencode-go-meter
- groq-dictate: https://github.com/LeonVeganMan/opencode-groq-dictate · https://www.npmjs.com/package/opencode-groq-dictate

Both target **opencode v2** (`@opencode/plugin/tui`: slots, dialogs, keymap layers). The v1 plugin API is a different generation and these won't load there.

Two honest limits: dictation only exists inside the TUI — `Super+V` never reaches it because VTE strips the modifier, hence `alt+v` — and it needs `parec` plus `xclip`. If you try them, tell me what breaks; the issue tracker is open.

Ciao.
L.

**Comentarios:**

- **u/migsperez** (↑1, 2026-10-19 12:49): [https://github.com/LeonVeganMan/opencode-go-meter](https://github.com/LeonVeganMan/opencode-go-meter)
    
    I like this one and would want to use it.  Can you create an NPM package, please.  It makes it easier to install and use.  
    
    Take the workflow from my plugin [https://github.com/8perezm/esuyo-opencode-session/blob/main/.github/workflows/publish.yml](https://github.com/8perezm/esuyo-opencode-session/blob/main/.github/workflows/publish.yml) and customise it for your needs.  Github Actions is free for open source public projects.
  - **u/LeonVeganMan** (↑2, 2026-10-19 14:05): Done. Now you can install with:
      
          opencode plugin add opencode-go-meter
      
      Ciao.
      
      L.
    - **u/migsperez** (↑1, 2026-10-19 15:20): You're great!!  Nice thanks :)
    - **u/migsperez** (↑1, 2026-10-19 15:48): Feedback:
        
        \- Showing "plan n/a"  - I do have a subscription and i'm use a Go model  
        \- the settings, when i click on footer it doesn't seem to do anything.. I wanted to turn the footer off.  - the settings, when i click on any of the rows the option isn't changed on the second column.  I can see some are doing something below the popup.
      - **u/LeonVeganMan** (↑1, 2026-10-19 16:10): Hi, 
          
          API key is stored in \~/.local/share/opencode/auth.json → \["opencode-go"\].key: check it. Any way now an error message instead of n/a.
          
          Fix click on options.
          
          Update plugin (1.0.6)
          
          Ciao.
          
          L.
- **u/migsperez** (↑1, 2026-10-19 12:50): For dictation I normally use [https://handy.computer/](https://handy.computer/)  
    
    But kudos for creating something unique.
  - **u/LeonVeganMan** (↑1, 2026-10-19 14:06): Try in local, but very very slow on my machine. Groq is very fast instead.
      
      Ciao.
      
      L.

---

## I made opencode v2 read my plan quota and type what I                                                       say
**u/LeonVeganMan** · 2026-10-19 11:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9ufy2/i_made_opencode_v2_read_my_plan_quota_and_type/)

\# Two opencode v2 TUI plugins: a plan/context meter and Groq dictation

I use opencode v2 all day and ended up writing two small TUI plugins. Both MIT, both on npm, no config entry needed.



\*\*opencode-go-meter\*\* — your session context usage and your OpenCode Go plan windows in the sidebar, plus a forecast of where the current pace lands by each reset. Rows are clickable: the title opens a settings dialog where you can turn the panel and the footer on or off. It replaces the built-in context/footer blocks, so disable those in \`cli.json\` (\`"disabled": \["-opencode.sidebar.context", "-opencode.prompt.footer"\]\`) or you'll see the numbers twice.



\*\*opencode-groq-dictate\*\* — press \`alt+v\`, speak, press \`alt+v\` again. The take goes to Groq's \`whisper-large-v3-turbo\` and the transcript is pasted into the prompt at the cursor, ready to edit. \`esc\` throws a take away without uploading it. The panel shows state, model, language, today's spend and requests left: RPM is tracked locally (20/min), the daily number comes straight from Groq's response headers, so checking the quota doesn't cost a request. A free Groq key is enough.



Install — clone into the plugins folder and restart the TUI:



\`\`\`bash

git clone [https://github.com/LeonVeganMan/opencode-go-meter](https://github.com/LeonVeganMan/opencode-go-meter) \\

  \~/.config/opencode/plugins/opencode-go-meter



git clone [https://github.com/LeonVeganMan/opencode-groq-dictate](https://github.com/LeonVeganMan/opencode-groq-dictate) \\

  \~/.config/opencode/plugins/opencode-groq-dictate

\`\`\`



Plugins are discovered from \`\~/.config/opencode/plugins/<name>/\`; there is no hot reload, so restart opencode after cloning.



\- go-meter: https://github.com/LeonVeganMan/opencode-go-meter · https://www.npmjs.com/package/opencode-go-meter

  
\- groq-dictate: https://github.com/LeonVeganMan/opencode-groq-dictate · https://www.npmjs.com/package/opencode-groq-dictate



Both target \*\*opencode v2\*\* (\`@opencode/plugin/tui\`: slots, dialogs, keymap layers). The v1 plugin API is a different generation and these won't load there.

Two honest limits: dictation only exists inside the TUI — \`Super+V\` never reaches it because VTE strips the modifier, hence \`alt+v\` — and it needs \`parec\` plus \`xclip\`. If you try them, tell me what breaks; the issue tracker is open.

**Comentarios:**

- **u/Natethegreat9999** (↑1, 2026-10-19 12:59): I'm building Oruk, and the large-v3 cost estimate looks low: the meter applies Turbo's cheaper rate.
  - **u/LeonVeganMan** (↑1, 2026-10-19 14:11): Hi, you are right. Fixed it.
      
      Ciao.
      
      L.

---

## Anyone else tired of reading long AI responses while vibe coding?
**u/Vast-Tutor-9942** · 2026-10-19 11:13 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9u1qv/anyone_else_tired_of_reading_long_ai_responses/)

[removed]

---

## How do I know my deepseek model
**u/johndoe1985** · 2026-10-19 11:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9u0ud/how_do_i_know_my_deepseek_model/)

I'm using the OpenCode Go subscription. 

How do I know which version of DeepSeek 4.1 Flash I'm using? Is it the latest version that came out this week?

Thanks!

**Comentarios:**

- **u/Leather-Cod2129** (↑8, 2026-10-19 11:31): Ask it! It'll tell you which version of Claude it is
  - **u/johndoe1985** (↑-3, 2026-10-19 11:32): Talking deepseek buddy
    - **u/Conscious-Doctor-585** (↑4, 2026-10-19 11:40): He was trying to make a joke of it.
      - **u/johndoe1985** (↑-2, 2026-10-19 12:29): What’s the joke
        - **u/Leather-Cod2129** (↑3, 2026-10-19 12:29): That’s the joke Claude
- **u/Queasy_Fondant_9295** (↑2, 2026-10-19 11:44): opencode clearly mentioned it's deepseek 4.1 flash, not deepseek v4.1 flash 1017. so it's not the latest deepseek version yet
  - **u/johndoe1985** (↑2, 2026-10-19 12:21): When did they say that.  And when will they change ?
    - **u/Queasy_Fondant_9295** (↑2, 2026-10-19 13:21): [https://x.com/opencode/status/2110635747648909472](https://x.com/opencode/status/2110635747648909472) no information so far for 1017
- **u/Plastic_Love3352** (↑1, 2026-10-19 13:37): not yet, [https://www.reddit.com/r/opencodeCLI/comments/1x9oydj/deepseek\_v41\_flash\_1017\_in\_opencode\_yay/](https://www.reddit.com/r/opencodeCLI/comments/1x9oydj/deepseek_v41_flash_1017_in_opencode_yay/)

---

## So Space Bunny was M3.1-Flash
**u/Rocky885533** · 2026-10-19 11:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9txys/so_space_bunny_was_m31flash/)

---

## Space Bunny Revealed
**u/CoffeeTea021** · 2026-10-19 10:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9ti3o/space_bunny_revealed/)

**Comentarios:**

- **u/mubaidr** (↑13, 2026-10-19 10:47): And its pretty good!!! Let's see how the pricing is.
  - **u/MMORPGDev** (↑1, 2026-10-19 10:55): But is it really good?
    - **u/RepulsiveRaisin7** (↑1, 2026-10-19 10:58): No
    - **u/mubaidr** (↑6, 2026-10-19 11:00): Not comparable to frontier models but its good.
    - **u/Fun_Squirrel5446** (↑1, 2026-10-19 13:45): I tested it out for a full day before I gave up on it. It's pretty bad.
  - **u/Odd_Abrocoma_8421** (↑1, 2026-10-19 16:14): Well a dissapointment, expensive than deepseek and mimo while being less intelligent
- **u/Odd_Abrocoma_8421** (↑12, 2026-10-19 10:47): Everyone knew from the starting.
  - **u/mubaidr** (↑1, 2026-10-19 10:56): Yeah pretty much!
  - **u/DagothUrLovesGroza** (↑2, 2026-10-19 11:02): This
- **u/migsperez** (↑3, 2026-10-19 10:47): https://www.reddit.com/r/opencode/s/bcyL8l537q
  - **u/Gunnarz699** (↑1, 2026-10-19 12:45): Nightmare fuel.
- **u/totoer008** (↑0, 2026-10-19 11:08): I tested it. It is not good. Step 5 and DeepSeek found a lot of issues. I would not say it is a good model.
- **u/PhaseTemporary** (↑2, 2026-10-19 12:13): i was doing something with space bunny and it just disappeared, and had to choose glm
- **u/Soifon99** (↑2, 2026-10-19 13:15): somehow muse spark 1.3 understood the problems it was presented better, it was not about coding. but mostly front end design(and the little bit of coding),  spark you could explain in human language what i did not like and say how i do want it and it understood,  space bunny, not so much.
- **u/Vexaris1** (↑1, 2026-10-19 13:37): It was obvious he would come out of it, it wasn't a surprise.
- **u/Serious_Ship7011** (↑1, 2026-10-19 15:39): Space Bunny work was so inconsistent, did some very good job when presented a blank project, but then failed to understand it properly next session.

---

## getting "rate limit exceeded" on dsv4.1f after waiting like 10 min
**u/GoonigUnc** · 2026-10-19 10:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9tfr5/getting_rate_limit_exceeded_on_dsv41f_after/)

[removed]

---

## I cannot lie opencode is so much better than Claude code
**u/multyfora** · 2026-10-19 10:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9szh8/i_cannot_lie_opencode_is_so_much_better_than/)

after using Claude code tui for the first time I can't believe how bad it is compared to opencode, like obviously the models are better, but the UI is so bad oh my god, how is this even possible

**Comentarios:**

- **u/Sea-Dimension-1097** (↑5, 2026-10-19 10:19): Yea the UI of claude code is worser than Opencode, but if you look at the task execution and don't think about the UI , then its just better, yea opencode is more effecient, but sometimes corners are cut in opencode task execution which leads to multiple rounds of prompting just to get a few bugs corrected, but other than that its all good. 
    
    If you have been able to use opencode models in claude code then create a proxy to where your claude cli will connect to and send requests to opencode, then if you have a proxy like that then you can use developer mode in the claude desktop app and create your inference and use your own models in the claude code desktop app if UI is an issue.
  - **u/Anurag_baral** (↑1, 2026-10-19 11:03): Unrelated,   
      "Worser" - I'm reading that for the first time, May i ask which writer made this non-standard word famous ?
    - **u/Sea-Dimension-1097** (↑1, 2026-10-19 12:30): Talking about knowing English yet doesn't know if a letter after a comma needs to be capitalized and when should the letter 'i' should be capitalized.
      - **u/Anurag_baral** (↑0, 2026-10-19 13:11): Sorry, I'm learning english and wanted to learn which writer or a human made that non-standard word famous, i used it a lot aswell, I edited my mistake thanks.
- **u/vqt907** (↑1, 2026-10-19 10:57): I don't think OpenCode is the best, but it fit me:
    
    * It has just enough tools - not as bloated as Claude Code, but not as primitive as Pi
    * not too much system prompt
    * TUI is pleasant to use
    * openchamber provides very good web, mobile, and desktop apps, along with VS Code integration, though I still use TUI 50% of the time
    * most third-party AI tools support it
  - **u/KubeGuyDe** (↑1, 2026-10-19 11:31): What do you use for vscode integration?
    - **u/vqt907** (↑1, 2026-10-19 12:15): openchamber, basically I only use plain opencode in TUI, on other platforms I always openchamber
- **u/csgeek-coder** (↑1, 2026-10-19 13:52): Not sure how the models are better, the part I strongly dislikes about CC is that it's a bit too free with the permissions and what it grants itself access. I'm sure I can tone that down but I really LOVE that opencode lets me control the access and control a lot better.
- **u/skillmaker** (↑1, 2026-10-19 16:06): In terms of UI and cost, OpenCode with DeepSeek 4.1 flash or GLM 5.3 flash is best; however, Codex with Sol 6.1 or Claude Code with Claude Opus 5.5 are better in everything else. I used Codex and OpenCode Go, Sol 6.1 reviews find more issues and defects when using DeepSeek 4.1 flash max as an implementer compared to using Luna xhigh or Sol low for implementation. I haven't tried Claude Code yet.
    
    For simple codebases and logic, maybe, but not for complex stuff intended for production, you might find yourself wasting more tokens by going back and forth correcting the model.

---

## Context issue
**u/illusion-xo** · 2026-10-19 10:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9svh4/context_issue/)

I was using glm 5.3 which is currently made free. im working on this project and every time it gives it a prompt it context usage skyrockets and by the time its finished it has compacted the session like 3-4 times. This mid working compacts would obviously be impacting its performence. So i was wondering should i let it be or use some other 1m context model, if so which is the best one?

**Comentarios:**

- **u/simpleuss** (↑1, 2026-10-19 10:12): I have seen people say you can force 1000000 context window by changing opencode.json(c)
  - **u/KKTheLightWolfKK** (↑1, 2026-10-19 10:37): i dont think it works anymore. I did that thing with deepseek but it auto compacts now. at 200-300k
- **u/AbdullahHavinFun** (↑1, 2026-10-19 10:39): I use this and my context doesnt go over 100k [https://github.com/Tarquinen/opencode-dynamic-context-pruning](https://github.com/Tarquinen/opencode-dynamic-context-pruning)
  - **u/illusion-xo** (↑1, 2026-10-19 16:18): it isnt helping man
- **u/illusion-xo** (↑1, 2026-10-19 16:19): lowkey someone help, now its a never ending loop of just compacting

---

## Thousands of people are pooling spare AI tokens to remake paid software
**u/Numerous-Campaign844** · 2026-10-19 09:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9sfu3/thousands_of_people_are_pooling_spare_ai_tokens/)

**Comentarios:**

- **u/Numerous-Campaign844** (↑1, 2026-10-19 09:41): And you know what's the coolest part? You can join the swarm. Any model, any agentic IDE, your spare tokens. [PdfCraft](https://github.com/storytold/pdfcraft) is the best one to start with: pick an [issue](https://github.com/storytold/pdfcraft/issues), let your agent fix it, and PR. Open source powered by everyone’s leftover AI budget. What a time 🫡

---

## 🚀 MiniMax-M3.1-Flash is coming..
**u/afanasenka** · 2026-10-19 09:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9sda3/minimaxm31flash_is_coming/)

Space Bunny?!

[https://x.com/MiniMax\_AI/status/2112111925975032241](https://x.com/MiniMax_AI/status/2112111925975032241)

**Comentarios:**

- **u/aliencreature12** (↑-1, 2026-10-19 09:36): it was a shit model any way
  - **u/LuluLeSigma** (↑1, 2026-10-19 09:38): yeah it barely talk english
    - **u/truecrisis** (↑1, 2026-10-19 11:09): They do that deliberately, to optimize reasoning since LLMs don't need full sentences to reason.
        
        Its a legit strategy. How well it works, I've no idea.
- **u/MMORPGDev** (↑2, 2026-10-19 10:37): It's terrible

---

## Suddenly, I Can’t Use OpenCode’s Free Models Anymore
**u/aliencreature12** · 2026-10-19 09:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9sd5g/suddenly_i_cant_use_opencodes_free_models_anymore/)

https://i.redd.it/w1b5tn868ewh1.png

All of a sudden, I can’t use OpenCode’s free models anymore. I’m getting a new error. I don’t use a VPN, and the free models worked fine before. But after they got hacked, it seems like they started limiting users. By the way, I’m on Go, but I want to use the free Zen models at the same time.

**Comentarios:**

- **u/nazmulpcc** (↑1, 2026-10-19 09:39): they're going through something, just wait a few days
- **u/Super-Veterinarian22** (↑1, 2026-10-19 13:29): Try Cloudflare WARP. It helped me get rid of the same error.

---

## Workspaces access restricted since few days
**u/Klakocik** · 2026-10-19 09:29 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9saeu/workspaces_access_restricted_since_few_days/)

https://i.redd.it/snl5xjro7ewh1.png

I'm my own administrator.  
Tried contacting me - didn't help.  
Tried contacting opencode support - also didn't help.  
What do i do?

---

## What are some of the cool projects you have built on opencode?
**u/automax** · 2026-10-19 09:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9s496/what_are_some_of_the_cool_projects_you_have_built/)

Please only post projects that are free to open on either web or mobile.  
If you have used a mixture of opencode/claude/chatgpt thats fine also.

  
I'm interested to see what everyone's been building.

**Comentarios:**

- **u/MrBansal** (↑1, 2026-10-19 09:27): Trading bot
  - **u/automax** (↑1, 2026-10-19 09:34): whats the url
  - **u/Severe_Can_6620** (↑1, 2026-10-19 11:49): share with us please
- **u/arvernester** (↑5, 2026-10-19 11:03): Building a service status aggregator from official status pages with an alerts feature. Built using DeepSeek Flash Go/Free.
    
    URL: [https://downradar.info](https://downradar.info)
- **u/drunkmasterflex** (↑1, 2026-10-19 11:07): Sportsbook simulator that runs on real sports schedules and real Vegas odds with a built in bookie/loan shark that gets meaner the more you owe. https://www.jaystakes.com
- **u/Lonely-Session-7643** (↑3, 2026-10-19 11:09): * [https://github.com/onebuckapp/whatever](https://github.com/onebuckapp/whatever) \- browser with built-in ad blocker, password manager and many customization buttons. Made with Nim + Swift (macos only for now)
    * [https://github.com/openpeeps/tim](https://github.com/openpeeps/tim), a front-end engine DSL written in Nim. CLI, Source-to-source transpilation (optimized with OC)
    * [https://github.com/openpeeps/powpow](https://github.com/openpeeps/powpow) \- an event notification library (UDP, TCP, HTTP/1.1, H/2 alternative to libuv and libevent)
    * [https://github.com/openpeeps/bowdy](https://github.com/openpeeps/bowdy) \- a fast CSS preprocessor alternative to SassC and DartSass
    * [https://github.com/openpeeps/openparser](https://github.com/openpeeps/openparser) \- a shameless collection of tiny parsers and serializers for JSON, CSV, TOML, YAML, BSON, Regex, SQL, Gettext and more (mostly SIMD-accelerated + zero-copy/efficient parsing) \~ also available as NodeJS/Bun addon
    * [https://github.com/openpeeps/vancode](https://github.com/openpeeps/vancode) \- a macro-based AST, codegen, VM and JIT compiler for Nim (used by tim, bowdy)
    * many other nim packages, bindings and so on
  - **u/migsperez** (↑1, 2026-10-19 12:20): [https://github.com/onebuckapp/whatever](https://github.com/onebuckapp/whatever) the about section in the readme, needs to be at the top.  I almost left without knowing what the project was.
      
      Really interesting projects.  How do you think models do, with less known programming languages like Nim?  Are there certain models which have a deeper understanding of Nim than others?
    - **u/Lonely-Session-7643** (↑1, 2026-10-19 12:31): Thanks for that! I will update the README.
        
        I'm using DS v4 Flash and Muse Spark 1.3, both are pretty good! Usually, Nim's syntax is not a problem (except in meta-programming, some macro-based DSLs are pretty abstract and LLMs need some extra hints), also Nim's compiler is statically typed, very strict, and can catch most bugs at compile-time, so this is free info for the Agent
  - **u/Minimum-Avocado-8015** (↑1, 2026-10-19 16:24): Nim.That's the first thing that caught my attention. The last time that happened was with Rust.
- **u/Important_Copy_6011** (↑2, 2026-10-19 11:31): https://glimdocs.com/
- **u/Other_Bicycle_5421** (↑2, 2026-10-19 11:32): Basketball online manager www.baxball.com
  - **u/migsperez** (↑1, 2026-10-19 12:09): This looks fun.  Which models did you use?  I most often use Muse 1.3
- **u/AdImportant9459** (↑2, 2026-10-19 11:47): Yo me he desarrollado una imitación personal de Strava para ciclismo, con algunas características que no incluye Strava. Tanto aplicación móvil como aplicación web.
    El último añadido que le he hecho ha sido, con el MCP Rea, una funcionalidad para que lea las rutas directamente del ciclocomputador por bluetooth, sin necesidad de la aplicación propia del ciclocomputador
  - **u/migsperez** (↑2, 2026-10-19 12:11): That's cool.  There's a lot of complex computational work it needs to do.  Pushing models to their limits, nice.
- **u/migsperez** (↑1, 2026-10-19 12:05): Recent fun:  
      
    [https://github.com/8perezm/esuyo-coding-container](https://github.com/8perezm/esuyo-coding-container) \- A system for creating coding based containers in K8S, to be able to develop off the laptop with Opencode. 
    
    [https://rafscoots.esuyo.com/](https://rafscoots.esuyo.com/) \- A fake ecommerce website for my kid who's interested in scooters.  Wanted to see what a model could achieve. 
    
    [https://github.com/8perezm/esuyo-esp32-agent](https://github.com/8perezm/esuyo-esp32-agent) \- Chat with your ESP32 in a browser. Controls pins, sensors, memory and web via AI tools, with OTA updates.  Meant to be a starting point for creators.
- **u/Purple_Poetry9198** (↑1, 2026-10-19 12:07): [Bourloto Game](http://bourloto.com/app)
- **u/Wise_Choice7014** (↑1, 2026-10-19 12:14): I built AI CostGuard⁠, an open-source Node.js library that estimates AI call costs before supported SDK methods execute and blocks calls that exceed configured budget limits. 
    It runs locally without a dashboard or proxy. Feedback from developers using OpenCode and other coding agents would be especially useful.
    Guys please i need your feedback: https://github.com/salimassili62-afk/ai-costguard
- **u/pppodong** (↑2, 2026-10-19 12:19): I reverse engineered some apps using Rea that have license trials to find the binary and use open code cli with jailbreak to remove it and build a native one same as the og app with no license or a patcher app for some . Another thing I did is removed the time limit swither from the proton app windows in free mode.
  - **u/Maximum-Country-2409** (↑1, 2026-10-19 15:22): can you explain how to access opencode jailbreak?
      I want to use rea, but I have no idea where to start
- **u/RoofTall6762** (↑1, 2026-10-19 12:20): content creator subscription platform on the blockchain.
    
    you can find it on google "kaskama"
- **u/data_in_void** (↑1, 2026-10-19 12:51): 1. an AI skill (with MCP, choose one to use) I can call my own :shrug:
    
    https://github.com/bladeacer/lccst
    
    > it's not as flashy and more unix esque (compared to the popular AI skills out there) with a semi decent playground for benchmarking how models actually provide improved output (in terms of code quality) and how much more tokens it requires them to do so.
    
    2. Ada/SPARK formal verification and compliance tool chain
    
    https://github.com/bladeacer/adacovex
    
    > basically I wanted a sane CLI/web dashboard/interface over gnatprove (what one uses to verify the contracts written for the SPARK dialect of the Ada programming language). Has some neat features but there's a fair bit to list (and that's what the docs are for)
    
    I alternate between opencode kilo and freebuff, depending on my needs for each project
- **u/Silcord_Gaming** (↑1, 2026-10-19 13:12): I got frustrated trying to keep up with the pace of AI, so I created this to stay updated; it is still in progress, but if you check my page, please provide feedback if you have any 
    
    [signal-Ai compnaion ](http://ainews-smel.vercel.app)
- **u/wikipowdergroup** (↑1, 2026-10-19 13:24): We have built our entire project using OpenCode [www.wikipowder.com](http://www.wikipowder.com) 😄 Mainly to avoid being tied to a specific model or ecosystem. Glad we made the switch a while ago... Claude's pricing has increased significantly
- **u/Ok_Cricket9353** (↑2, 2026-10-19 13:28): A couple of free web projects I recently put together:
    
    * [**Docset**](https://docset.in)– A clean tool/documentation hub for quickly referencing and organizing technical resources.
    * [**Crokinole Web**](https://crokinole.pages.dev)– A browser-based simulation of the classic board game Crokinole, focusing on smooth physics and lightweight mechanics.
    
    Both built with assistance from AI coding workflows to handle the initial scaffolding and physics/logic tuning.
- **u/Miserable_Season_610** (↑1, 2026-10-19 13:38): Used adb to make my superslow 5 year old TCL android tv lightening fast!!!! I know people could have done it using adb directly and don't need an agent for something so trivial, but I loved it and fuckin proud of it. Not a techie!
- **u/DuckDatum** (↑1, 2026-10-19 13:46): Ephemeral airflow with asset and task based workflows, builtin Blueprint, rust. It’s about half way through the first release.
    
    Also had a project that let you read/write to DuckLake from iceberg clients. Got it to POC then stopped. :/
- **u/immersive-matthew** (↑1, 2026-10-19 14:17): 5 years the old fashion way, then the past year with OpenCode assisting. https://www.meta.com/en-gb/experiences/theme-park-dark-rides-games/4212005182188732/
- **u/Minimum-Avocado-8015** (↑1, 2026-10-19 16:25): why not Jira, Zendesk remake guys? Not fun?

---

## GitHub copilot diff
**u/RoofTall6762** · 2026-10-19 08:44 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9rkcq/github_copilot_diff/)

[removed]

---

## I built brushrouter so any coding agent can generate images using the ChatGPT/Gemini logins
**u/MrStevenOFC** · 2026-10-19 08:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9rh7g/i_built_brushrouter_so_any_coding_agent_can/)

brushrouter is an open-source CLI and MCP server. Any agent(because i use multiple tools) that speaks MCP or can run a shell command gets a single image tool, which I route through Codex CLI and Gemini smartly. OpenRouter, fal, or a custom endpoint come next. OpenRouter is disabled by default, so nothing gets billed unless you enable it.

The part I spent the most time on is credentials. The native routes spawn the CLI, so brushrouter never sees your token, and everything it prints goes through a redactor. I also added a prompt library with 27 layouts and 137 styles that the agent searches before generating.

Work on ChatGPT **Free, Go, Plus and Pro** accounts

Inspired from opencode-gpt-imagegen - You can checkout that also, its a great project.

[https://github.com/avinaxhroy/brushrouter](https://github.com/avinaxhroy/brushrouter)

Meaningful Contributions are welcome.

---

## Does DeepSeek V4.1 Flash slow down after 200k tokens of context?
**u/CognitiveAuthor** · 2026-10-19 07:51 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9qqeh/does_deepseek_v41_flash_slow_down_after_200k/)

[removed]

---

## OpenAI using deepseek v4.1
**u/Maleficent-Volume-81** · 2026-10-19 07:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9qqas/openai_using_deepseek_v41/)

**Comentarios:**

- **u/sinanpostaci** (↑1, 2026-10-19 07:57): I am having the same issue since yesterday.
- **u/ReoTempo** (↑5, 2026-10-19 08:07): Most likely, Deepseek uses OpenAI protocol, the message is just telling that the stream (in the form of OpenAI Chat) was interrupted without a reason.
- **u/Any_Ad9815** (↑1, 2026-10-19 08:31): same

---

## Payment Decline opencode
**u/akuma-st0ic** · 2026-10-19 07:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9qoe9/payment_decline_opencode/)

Go subscription Payment card Declined any help would be appreciated

**Comentarios:**

- **u/Strict-Prune-879** (↑0, 2026-10-19 07:50): quel pays?
  - **u/akuma-st0ic** (↑1, 2026-10-19 07:54): Quel pays? what is it?
    - **u/Strict-Prune-879** (↑1, 2026-10-19 09:57): what is your country?
- **u/Electronixen** (↑1, 2026-10-19 08:02): Yep. Has happened to me, can't pay for the subscription at all, and nobody seems to be able to fix it.
  - **u/akuma-st0ic** (↑1, 2026-10-19 08:08): Do you have Idea when we'll be able to subscribe
    - **u/Electronixen** (↑1, 2026-10-19 11:14): No idea, hasn’t worked for two months now.
- **u/dumbasPL** (↑2, 2026-10-19 08:39): Contact support not reddit?
- **u/y_dem** (↑1, 2026-10-19 12:59): Switching browsers worked for me. I was using Brave, but it denied the authorization. I then tried Firefox, and the purchase went through successfully.

---

## Is it normal to have so much context tokens?
**u/AdNecessary8217** · 2026-10-19 07:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9qjjv/is_it_normal_to_have_so_much_context_tokens/)

I saw 100k+ tokens very frequently, sometimes even 150k+.

Any solutions or is this harmless?

**Comentarios:**

- **u/Maglcite** (↑12, 2026-10-19 07:40): very normal.
- **u/Rick_C135** (↑4, 2026-10-19 07:42): normal
- **u/AlexandraMaryWindsor** (↑5, 2026-10-19 07:43): I have auto compact at 400k
- **u/swg0101** (↑2, 2026-10-19 07:58): Most likely caused by your MCP tools - camofox itself has a lot of tools within and each of them occupy context so even if you send a single "hi" message, a lot of the context is already preoccupied by all of your tools.
- **u/Effective_Union7326** (↑2, 2026-10-19 08:05): For casual chatting, 100K is plenty, just start a new session for a different topic. However, for coding, 100K is very small (you won't need to worry until 300K or 400K). Since your current model maxes out at 200K, it can't handle long tasks, and you'll waste a lot of tokens on autocompact.
- **u/bender_fut** (↑0, 2026-10-19 08:45): Even more. Yesterday I got > 800k.
- **u/ScientistStrict9850** (↑0, 2026-10-19 09:05): I try to reduce context cuz it's quite wasteful. Mine sits at around 40K on first turn prompt
- **u/JoeyredditSMP** (↑2, 2026-10-19 09:31): yes its normal for first message like saying hi it should be at most 30k if it was working for some time thats normal
- **u/static_soul87** (↑1, 2026-10-19 10:38): Yes it is completely normal in fact it compacts it after a certain range

---

## which one is opencode best model ?
**u/OrangeLimp9572** · 2026-10-19 07:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9qh5t/which_one_is_opencode_best_model/)

**Comentarios:**

- **u/Strict-Prune-879** (↑2, 2026-10-19 07:40): deepseek v4.1 flash il est polyvalent et pas cher
  - **u/OrangeLimp9572** (↑2, 2026-10-19 07:41): thank you for your suggestion !
- **u/NinjaAlaska** (↑3, 2026-10-19 07:46): deepseek v4.1 flash then muse v1.3 contributor.  
    good pair. others costly all good too but price matters
  - **u/Sudden-Dog-8084** (↑1, 2026-10-19 10:20): What are some good ways of using both, do you use one for planning one for building or is it just refactoring type pairing?
    - **u/NinjaAlaska** (↑2, 2026-10-19 10:29): i use OMP or deep seek harness  
        i use deep seek v4.1 as orchestrator or plan tasks  
        for sub tasks muse aka coder n etc
- **u/AgitatedUse4032** (↑2, 2026-10-19 07:47): I like Muse spark 1.3 because it's really fast and reliable. Deepseek is another option but it burns tokens like crazy.
- **u/power10010** (↑0, 2026-10-19 08:08): Deepseek 1017
- **u/Takeoded** (↑1, 2026-10-19 08:18): You need to be more specific. OpenCode Free, OpenCode Go, or OpenCode Zen? 
    
    Free: probably `deepseek-v4.1-flash-free`
    
    Go: probably `deepseek-v4.1-flash` (maybe `muse-spark-1.3` , they're both really good)
    
    Zen: definitely `claude-fable-5-1`
- **u/alex9001** (↑1, 2026-10-19 08:22): deepseek v4.1 is very best and costs very less
- **u/Vexaris1** (↑1, 2026-10-19 14:43): My favorite opencode model was Muse Spark 1.3. Currently, models like GLM 5.3 Flash, Deepseek v4 Flash, and M3.1 Flash are quite good free models.
- **u/look** (↑1, 2026-10-19 14:48): As of today, best mix is probably: Mimo 2.6 Pro + latest Deepseek 4.1 + a bit of GLM 5.3

---

## [Release] opencode-models-discovery v2.0.0: Native OpenCode V2 support, host storage, and live model overrides now GA
**u/yu_hp** · 2026-10-19 07:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9pzcc/release_opencodemodelsdiscovery_v200_native/)

---

## Does opencode v2 lack LSP?
**u/wentallout** · 2026-10-19 06:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9pou1/does_opencode_v2_lack_lsp/)

https://i.redd.it/1tcld5jledwh1.png

I remember having something like this but v2 just never mention it. Do you guys know what happened

---

## Deepseek V4.1 Flash 1017 in OpenCode! Yay!
**u/abhijithwarrier** · 2026-10-19 05:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9oyi0/deepseek_v41_flash_1017_in_opencode_yay/)

**Comentarios:**

- **u/AppealSame4367** (↑2, 2026-10-19 06:25): "Where 1017 on go???"
    
    Seriously, can't wait. I'm grilling dollars away like nothing on openrouter right now
  - **u/abhijithwarrier** (↑3, 2026-10-19 06:34): Usually the model appears within 24hrs of their listing in the data page. Seems like they are a bit busy now due to the whole data breach situation.
  - **u/Ameldur93** (↑1, 2026-10-19 12:51): Same herr can't wait lol
- **u/Dazzling-Toe9614** (↑1, 2026-10-19 13:10): I have access to it after updating to opencode version 2 and I must say, I am impressed
  - **u/abhijithwarrier** (↑1, 2026-10-19 13:11): What? Where? How?
      
      Send a screenshot!

---

## Opencode Go in LibreChat
**u/Different-Monk5916** · 2026-10-19 05:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9o9b2/opencode_go_in_librechat/)

Has anyone tried adding API key from Opencode go for local chats with LibreChat?

I am getting 400 with below message

`The model provider could not complete this request (status 400).`

`400 Request is missing x-opencode-session and cannot be routed efficiently. Please see` [`https://opencode.ai/docs/go/#where-can-i-use-it`](https://opencode.ai/docs/go/#where-can-i-use-it)

**Comentarios:**

- **u/cornelha** (↑1, 2026-10-19 05:27): Librechat would need to add those headers

---

## OpenCode on my phone now answers my messages when a notification comes in (free models work)
**u/3amae404** · 2026-10-19 05:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9o0yy/opencode_on_my_phone_now_answers_my_messages_when/)

Buddy is an open-source Android app where OpenCode (or Claude Code, or Codex) uses your phone from a floating bubble, running in a small Linux inside the app, no PC. I just added notification rules.

You pick an app (optionally who it's from or a word it has to contain), pick the agent and model, and write what to do: "reply in my style", "tell me in one line what it says". When a matching notification comes in, the agent gets it in its own chat for that conversation and replies through the notification's Reply field, even with the phone locked. Before sending, it asks you or shows a countdown you can tap to cancel, after a second model checks the reply against your rule.

A stranger's message is now driving an agent on my phone, so these runs get less: OpenCode's bash, edits and web fetch are set to "ask" with nobody there to approve, no app installs, and links need my OK.

OpenCode needs no sign-in, so its free models are enough to try it. Apache 2.0: https://github.com/ghorbelhamdi/buddy-android

(The run in the video uses Claude Code and a demo chat app, so I don't show my own chats. Picking OpenCode is one tap in the rule.)

---

## Ugh, Opencode has been such a total mess since the hack! First it kept complaining I wasn't using a opencode client, then hit me with http 500 errors, and now this. Anyone know what's even going on?
**u/FHSenpai** · 2026-10-19 04:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9noql/ugh_opencode_has_been_such_a_total_mess_since_the/)

https://i.redd.it/10b1u0oiscwh1.png

**Comentarios:**

- **u/Primary-Meal-2264** (↑2, 2026-10-19 04:59): You probably got banned, try to use another network. I had same issue and fixed it by switching from WiFi to mobile network.
  - **u/FHSenpai** (↑1, 2026-10-19 06:59): using vpn right now
- **u/Super-Veterinarian22** (↑3, 2026-10-19 06:09): Same issue here. If you’ve modified the config to increase the context window for free models, that’s likely the cause. The block is probably temporary. You can use WARP to bypass it.
  - **u/FHSenpai** (↑3, 2026-10-19 07:03): I honestly didn't do anything special, I just kept working on my project like normal and then this happened! I had no idea you could actually make the context windows bigger for these models, especially since I haven't even maxed out the one they gave me yet.
    - **u/Super-Veterinarian22** (↑1, 2026-10-19 07:30): This is just my own theory, as it’s the only thing I did that was followed by the exact same issues. Furthermore, tech support claimed that I had repeatedly abused the free models on the day I tested a configuration with a modified model context size. In any case, this doesn't seem like how things should work. Regardless, my advice is to use CloudFlare WARP. It at least resolved the error for me.
- **u/ByteNomadOne** (↑3, 2026-10-19 06:15): Unfortunately, OpenCode was a mess before. I'm used to occasional errors by now.
  - **u/FHSenpai** (↑2, 2026-10-19 07:05): you are not wrong.

---

## Can somebody explain why we need platforms like opencode, cursor, antigravity etc. When we get all the ai chatbots for free online?
**u/jhalmuri_aur_gud** · 2026-10-19 04:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9njy2/can_somebody_explain_why_we_need_platforms_like/)

[removed]

---

## Day 8 of Daily Morph!
**u/2tacchi** · 2026-10-19 03:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9mqms/day_8_of_daily_morph/)

Hi again, its the 8th day of this little experiment. I made a [website ](https://dailymorph.app/)that



Bases its contents completely on the top comment of this reddit thread.

Everyday the comment gets put into an open code agent that than updates the website.

It runs on an isolated VPS with an persistent Opencode agent session so all past prompts and inputs are remembered. 

I kept my involvement minimal with an add on prompt saying do not ask follow up questions but other than that nothing to restrict it! 

I made a archive and context page so you can see past versions of the site and the context and builds the LLM went through in the past.

The LLM used is DeepSeek V4.1 Flash 1017



Yesterday's winner was EtsyCorn with  comment "Wooo hooo!!!

Ok let’s try again !! Keep the same website don’t replace or refresh it just make the changes stated below.  Make the checks for  safe, warm & gentle stronger & tighter. So weird stuff can't get thru.  Do not remove the flowers. Just double check each flower against the new stricter guidelines.

Redesign the watering can and make sure it looks like a watering can. Like double check everything. Oh and make sure every flower is clickable. Don't remove but move the existing to make sure all are clickable! 

Add an cute rainbow to the sky!

Add an very cute unicorn that pops in randomly and runs around the meadow. A bunny too. Make sure they look right double check triple check! I want too see the most magical unicorn and the cutest bunny ever!

If someone clicks on the unicorn magical sparkles should appear. Clicking the bunny should make it jump & once in a while show a carrot you can feed to bunny!"

---

## Looking For More Models With Unlimited Use For Free
**u/Kin_gjami47** · 2026-10-19 03:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9mnbl/looking_for_more_models_with_unlimited_use_for/)

Aside from the GLM 5.3 flash, which other AI models can be used for free without paying for any subscriptions or limits that can serve as an unlimited use. 

I use GLM 5.3 flash a little and yeah it's good. Can build apps tho slow. Trying to use others like DeepSeek. I need more good coding models.

**Comentarios:**

- **u/AdFun4897** (↑8, 2026-10-19 03:52): Nothing is free in this life man.
    
    Get a Dgx spark and run your own llm (you will pay electricty and infrastructure costs)
    
    Or get a monthly subscription.
    
    You will get rate limited with the free models and they will use your data for training
  - **u/menjav** (↑1, 2026-10-19 05:43): With a DGX you also need to pay for the machine and also the performance is pretty bad. Cannot run the really good models.
    - **u/ntn8888** (↑0, 2026-10-19 07:44): yep purely from a cost perspective, local is waste of money, better go subscription
      - **u/adeshpreet_singh** (↑1, 2026-10-19 10:32): DGX isnt a bad investment i guess. It can run qwen 3.8 flash next.  
          I’m currently using the same model on RTX 3090 with 64gb ram. Getting like 50-70 tokens per second speed on average. And the data goes nowhere, stays locally. Clients really like that secure part.  
          Going for deepseek 4.1 flash subscription seems like a really good choice tho. Incase if one dont want to spend so much money and dont care much about data (everything’s online already).
  - **u/Cor3nd** (↑1, 2026-10-19 06:07): You really think that the the ones you paid are not using your data? 😂
- **u/DiscountFit9224** (↑6, 2026-10-19 04:01): bro do you think they spent billions and just host it for free? This is more than AI psychosis
- **u/Mammoth_Fox_8051** (↑16, 2026-10-19 04:09): You can't ask for more when you're broke. Enjoy the free stuff while they last.
  - **u/moutazdarwesh** (↑3, 2026-10-19 11:41): 😂
- **u/Eastern_Spite335** (↑2, 2026-10-19 04:32): Si, anche io vorrei una Ferrari, due prostitute e una villa alla Scarface, gratis, adesso.
- **u/Alternative-Keyz** (↑1, 2026-10-19 04:33): [ Removed by Reddit ]
- **u/raw-power** (↑1, 2026-10-19 04:50): I read that as male models and wondered what kind of sub I was looking at. Been coding too much, need to sleep
  - **u/YoRt3m** (↑3, 2026-10-19 06:47): I thought that coding too much will cause you to think in terms of coding, not the opposite.
    - **u/raw-power** (↑3, 2026-10-19 06:48): lol yes, more the lack of sleep so not paying attention as much as usual
  - **u/stylist-trend** (↑1, 2026-10-19 11:44): [But why male models](https://youtu.be/WHrn_pHW2so)
- **u/Linkpharm2** (↑1, 2026-10-19 05:09): have $1? Command code is good value
  - **u/Jolly-Chef5241** (↑-1, 2026-10-19 05:38): $1 is not for free 🫨
- **u/Worried_Corner_8541** (↑3, 2026-10-19 05:38): Never underestimate the greed of indians that want absolutely unlimited inference.
  - **u/PlantainDry5705** (↑1, 2026-10-19 09:11): Lol true 😭
- **u/acakaacaka** (↑1, 2026-10-19 05:46): 10$ a month. You get billions of tokens.
  - **u/handsomedevildevil** (↑2, 2026-10-19 11:08): For which?
- **u/Leather-Cod2129** (↑1, 2026-10-19 05:47): Is GLM free training on our data?
- **u/TripleMellowed** (↑-2, 2026-10-19 06:23): Broke ass bitches want free stuff then complain because the free stuff isn’t good enough for them.
  - **u/Worried_Corner_8541** (↑1, 2026-10-19 09:26): Man and it's always fuckimg indians doing it. They flooded everything with ai slop and now they cry when inference isn't free.
    - **u/TripleMellowed** (↑0, 2026-10-19 10:26): I know. Building their AI slop with free models so it’s even worse apps then using paid for models.
- **u/ngcheck03** (↑2, 2026-10-19 06:35): actually, you can easily find good resources if you in Chinese community.
  - **u/Cup-Impressive** (↑1, 2026-10-19 07:10): are you in chinese community?
    - **u/Melodic-Mud-1116** (↑1, 2026-10-19 07:35): Gimme too 🙃
  - **u/Axiescholar3ph** (↑1, 2026-10-19 07:28): how to enter chinese community
    - **u/VibeCoder6000** (↑1, 2026-10-19 14:31): go to china
- **u/InsideTraditional187** (↑0, 2026-10-19 06:51): try freebuff
- **u/nikitaluger** (↑1, 2026-10-19 07:25): Get an nvidia api key and you can use nemotron 3.5 for free. I don't know what's the limit but I guess you're like me keeping lists of fallback models when my primary gets rate limited.
  - **u/Melodic-Mud-1116** (↑1, 2026-10-19 07:36): It's good but it's slow as hell.
    - **u/nikitaluger** (↑2, 2026-10-19 07:46): Free is free, we are beggars so we can't be choosers.
        
        I just started vibe coding last week and the game mashups made me decide to try coding with llm without prior programing knowledge. You pickup a lot and you learn fast but it's not worth spending money to get tokens. I learn faster due to jank that free models come with and you come up with good practices along the way. Debugging is tedious but you pick things up quick. Burn tokens for free so you can get good and save tokens for when you start paying.
      - **u/Melodic-Mud-1116** (↑1, 2026-10-19 08:47): It is what it is
- **u/Odd_Radio_5411** (↑1, 2026-10-19 10:17): Pay the really cheap api cost for the data retention version of muse spark 1.3. You can do a lot for pennies.
- **u/Salt-Ad-848** (↑1, 2026-10-19 12:35): You forgot to mention they must be frontier level!
- **u/aleemii** (↑1, 2026-10-19 13:33): WTF you'd even do with Free Unlimited Ai. if you can't even use to make money?

---

## Has the new DeepSeek V4.1 Flash model been updated in OpenCode?
**u/oylehesap11** · 2026-10-19 03:29 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9mbtx/has_the_new_deepseek_v41_flash_model_been_updated/)

I couldnt find any definitive information at the sub. I ran a few tests, and they seemed the same to me. Any clear inf?

**Comentarios:**

- **u/diegocraft2626** (↑1, 2026-10-19 03:30): no
- **u/AdFun4897** (↑20, 2026-10-19 03:33): No, tommorrow they will announce it. If they dont, read this again
  - **u/thanatos-class** (↑1, 2026-10-19 03:34): Xd
  - **u/cleversmoke** (↑3, 2026-10-19 04:38): Chat, remind me in tomorrow days
- **u/oylehesap11** (↑0, 2026-10-19 03:34): Okay i have 2 questions too. 1-why? 2-when?
  - **u/thanatos-class** (↑1, 2026-10-19 03:35): Tomorrow maybe
  - **u/TimChr78** (↑1, 2026-10-19 04:09): Because they don’t use Deepseek directly and the other providers need a bit of time to get the new weights up and running on their infrastructure.
      
      Probably later today or tomorrow.

---

## Is the referral still works/available?
**u/CYCLONOUS_69** · 2026-10-19 03:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9m4ke/is_the_referral_still_worksavailable/)

I'm thinking of buying OpenCode Go sub and I'm on very tight budget. If anyone has any referrals, please help me out.

**Comentarios:**

- **u/arcanemachined** (↑1, 2026-10-19 03:20): Nope, party's over.
  - **u/CYCLONOUS_69** (↑1, 2026-10-19 03:55): Damn.

---

## I’m building an AI chat that brings multiple models into one place — looking for honest feedback
**u/AdmirableAd7666** · 2026-10-19 03:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9m0n8/im_building_an_ai_chat_that_brings_multiple/)

[removed]

---

## plugin - session history in sidebar, click to resume in new tab
**u/UpstairsResident8121** · 2026-10-19 02:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9l63v/plugin_session_history_in_sidebar_click_to_resume/)

github - [https://github.com/ypxcs/opencode-session-history](https://github.com/ypxcs/opencode-session-history)

npm - `opencode plugin add opencode-session-history`

don't know how useful this is to anyone, but feedback is appreciated :)

**Comentarios:**

- **u/Natural-Cupcake6472** (↑1, 2026-10-19 02:56): you should try openchamber, honest opinion. i think yours is good, but someone already built a whole  new frontend for opencode,   
    that frontend is openchamber, and in my opinion, its very robust already, it even support tree view (for subagents)
  - **u/UpstairsResident8121** (↑1, 2026-10-19 03:12): wow, didn't know that. def trying it
- **u/nian2326076** (↑1, 2026-10-19 08:59): The session history plugin you linked might be helpful for developers who need to keep track of work across multiple tabs. It looks like a useful tool for managing session data. If you're looking for jobs in tech or other fields, [LandOffer.ai](https://landoffer.ai/?utm_source=reddit&utm_medium=community&utm_campaign=landoffer) can help you find job openings by role and location.
  - **u/porest** (↑1, 2026-10-19 09:26): nice bot

---

## Don't know how useful this is to anyone but made a session history plugin
**u/UpstairsResident8121** · 2026-10-19 02:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9kyx8/dont_know_how_useful_this_is_to_anyone_but_made_a/)

I built(vibecoded) a sidebar panel that lists your past OpenCode sessions and resumes them on click

**requirement -**

`opencode v2`

[](https://github.com/ypxcs/opencode-session-history#requirements)

For "open in new tab" behavior, enable session tabs:

    // ~/.config/opencode/cli.json
    { "tabs": { "mode": "on" } }

**npm install -** `opencode plugin add opencode-session-history`

more info. on github - [https://github.com/ypxcs/opencode-session-history](https://github.com/ypxcs/opencode-session-history) 

note - github install does not work, please read before you use it.

open to suggestions :)

---

## Launchpad: project commands in your OpenCode sidebar
**u/giannisCKS** · 2026-10-19 00:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9jakq/launchpad_project_commands_in_your_opencode/)

https://i.redd.it/z81041a9nbwh1.png



I built Launchpad, an OpenCode plugin that turns package scripts and Cargo commands into clickable sidebar buttons.

You can add custom buttons, edit names and commands, hide what you don’t need, and view logs or stop running tasks. Nothing runs automatically.

GitHub: [https://github.com/giannisCKS/opencode-launchpad](https://github.com/giannisCKS/opencode-launchpad)  

npm: [https://www.npmjs.com/package/opencode-launchpad](https://www.npmjs.com/package/opencode-launchpad)

Would love feedback, especially from people using Rust projects or monorepos.

---

## spaceeatingcode
**u/trashcoder999** · 2026-10-19 00:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x9ikrw/spaceeatingcode/)

I noticed that my "opencode.db" file in Termux on my smartphone has grown to 69 GB. How can I safely clean it up without deleting any data from sessions that have been active within the last 30 days?

**Comentarios:**

- **u/candraa6** (↑1, 2026-10-19 01:18): back it up and ask your agent to prune it

---
