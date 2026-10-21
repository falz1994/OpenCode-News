# r/opencode — hilos 2026-10-21 → 2026-10-22
_Generado: 2026-10-21T23:35:56.663550+00:00 · 63 hilos · 335 comentarios · fuente: Arctic Shift_

## help guys! OpenCode's free tier can only be used from within OpenCode. Download it at https://opencode.ai and keep building.
**u/RP2BACKUP2** · 2026-10-21 22:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xc13th/help_guys_opencodes_free_tier_can_only_be_used/)

OpenCode's free tier can only be used from within OpenCode. Download it at [https://opencode.ai](https://opencode.ai) and keep building.

i pawned my laptop for a month to help my mom out with some money, i got it back today and it responds with this on every free model i try, i tried a few things clearing cache, uninstalling and reinstalling. nothing seems to work , has anyone else ran into this?

---

## Is the $40 plan or additional credits on Go worth it?
**u/plurTM** · 2026-10-21 22:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xc0w9e/is_the_40_plan_or_additional_credits_on_go_worth/)

I have a temporary need to do about 4-5 trillion tokens as cheaply and quickly as possible. It is paralellisable work in that I can run a thousand subagents at a time as long as they all can continue so I don't need high TPS per session (it is not interactive coding or chat). DeepSeek Flash or GLM Flash both work fine, not picky. Unfortunately not something a Jev-style model can do. Screenshots and image recognition is mandatory -- no image generation, just being able to describe where UI is.

Would you do multiple Go accounts, multiple $40 Go accounts, API rates (more expensive than Go from measuring a week's worth of traffic), DS directly (far more expensive than Go), or any other options? I've noticed the $40 Go doesn't seem to be 4x of the $10 Go either, oddly

---

## I built an open-source Android dictation app using OpenCode + Termux — looking for testers
**u/bhairava0** · 2026-10-21 21:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xc0160/i_built_an_opensource_android_dictation_app_using/)

Hey everyone!

I've been building Wahtuh Pho, an open-source, offline-first dictation app for Android.

The unusual part? I don't have a dedicated workstation. I've been building with OpenCode, Termux on Android, and Azure/cloud compute when available.

I wanted to experiment with a different approach to voice dictation: a floating bubble that lets you speak and insert text into other apps, with on-device transcription by default and optional cloud providers if you want to bring your own API key.

What's in the project so far:

\- On-device speech recognition with the Whistle model.

\- A floating dictation bubble and accessibility-based text insertion.

\- Snippets, a personal dictionary, writing styles, and text-editing commands.

\- Optional Groq, Gemini, OpenAI, and Deepgram integrations.

\- A Rust workspace for experimenting with the underlying audio and transcription pipeline.

It's still early software. Local Telugu recognition isn't supported yet, and I need more real-device testing. I'm especially interested in bugs, battery usage, transcription accuracy, accessibility issues, and feedback from people who dictate code or mix languages while speaking.

Try it / inspect the code:

GitHub: https://github.com/desukab/wahtuh-pho

I'm building in public because I want to learn, experiment with new ideas, and make useful tools available to more people.

One personal challenge: without a workstation, progress depends on access to devices and cloud compute. If you'd like to support future open-source experiments, I've shared the details and wallet address here: https://github.com/desukab/wahtuh-pho/blob/main/SUPPORT.md

Solana support address: "2EJyURV4HhJNFas4V3cJtB1BqvMnDaPhqcxu5yiSkAxG"

No pressure at all. Testing feedback, bug reports, stars, and contributions are just as welcome as financial support.

If you try it, please tell me what worked, what broke, and what you'd want me to build next.

---

## I brought OpenCode Go & Zen to Visual Studio 2026 (not VS Code)
**u/Archeone** · 2026-10-21 21:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbzt2g/i_brought_opencode_go_zen_to_visual_studio_2026/)

I've been building [**iolys**](https://getiolys.com), an AI coding assistant that lives inside **Visual Studio 2026**, specifically for C# and .NET developers.

I wanted to work with OpenCode's model services while staying in the full Visual Studio IDE, with my solution, files and development tools close at hand. So I added dedicated connections for [**OpenCode Go**](https://getiolys.com/providers/opencode-go) and [**OpenCode Zen**](https://getiolys.com/providers/opencode-zen).

# OpenCode Go: bring your subscription

With [OpenCode Go / Go Plus in iolys](https://getiolys.com/providers/opencode-go), you can connect your subscription API key, choose which models appear in your chat picker, adjust reasoning effort where supported, and inspect your account's 5-hour, weekly and monthly usage windows and reset times without leaving Visual Studio.



![img](xy6vmhguzvwh1 "OpenCode Go model selection")

  
You can see directly in Visual Studio your usage:

![img](47x551o70wwh1 "OpenCode go usage")




# OpenCode Zen

The separate [OpenCode Zen integration](https://getiolys.com/providers/opencode-zen) lets you use your Zen API key and select models through the same Visual Studio workflow, with usage and cost information where available.

![img](w1hx72bzzvwh1 "OpenCode Zen")

  


![img](cukqzh8f0wwh1 "You can manage the reasoning level")

  
  



# More than a chat window

The point isn't to recreate the OpenCode CLI. These are **Go and Zen API integrations**, and neither requires installing the CLI. You can work from your C#/.NET solution and use iolys' workspace tools, MCP integrations, model selection and supported image inputs.

I'm the developer of iolys. It's currently **free for personal and commercial use**; OpenCode subscriptions and API usage are handled separately by OpenCode.

You can [install iolys from the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=iolys.iolys-visual-studio).

I'd love feedback from people using OpenCode with C# and .NET: **what would make a native Visual Studio workflow genuinely useful to you?**

---

## Meet Archestra 1.4 "Arpa": Remote Agents
**u/motakuk** · 2026-10-21 21:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbzrdt/meet_archestra_14_arpa_remote_agents/)

---

## How do I structure my monorepo and workflow to keep Claude Code consistent as a project grows?
**u/alatmaca** · 2026-10-21 20:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbyyho/how_do_i_structure_my_monorepo_and_workflow_to/)

---

## Experimenting with live task tracking at a glance on the sidepanel
**u/Rovax** · 2026-10-21 20:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbywx5/experimenting_with_live_task_tracking_at_a_glance/)

I have been experimenting with having a side panel integration for my yet-another-task-tracker tool, and it feels really nice to be able to keep track of what tasks my agent mentions, as well as what he is actually working on in the current session

---

## Should I stick with OpenCode or switch to DS?
**u/GervolkS** · 2026-10-21 19:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbwzha/should_i_stick_with_opencode_or_switch_to_ds/)

Hello,  
I am not a heavy AI user, but I have encountered some issues while using DS 4.1 on Opencode Go. I am wondering if it would be better to switch directly to the DS API or to GLM (which would likely also save me -or not- a couple bucks).   
  
Given that my usage quota has reset today, should I make the switch based on my consumption from last month?

https://i.redd.it/mhtjloksgvwh1.png

https://i.redd.it/o3t08x7ygvwh1.png

Thanks in advance!!

**Comentarios:**

- **u/AdFun4897** (↑2, 2026-10-21 19:41): I dont think your nintedo can handle an llm

---

## Need help for my first videogame
**u/Local-Item-2241** · 2026-10-21 19:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbwzf8/need_help_for_my_first_videogame/)

Hi! As I mentioned in the group, I’m trying to make a strategy game (the gameplay clip attached is what I’ve come up with in one week using OpenCode and Claude for the code), and I want to keep working on it.

I’m thinking about buying a Claude Pro subscription to start working on more specific things like 3D modeling, but I’m not sure if that’s the best option. I’m looking for something more polished in terms of interfaces, UI, and animations, so I’m not sure if Claude Pro would be the right choice or stick with OpenCode.

---

## V4 Flash API Connection Issues With Opencode
**u/LionFluid6548** · 2026-10-21 19:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbwyiu/v4_flash_api_connection_issues_with_opencode/)

---

## guys i used use vpn when i hit the limit of Free usage to have extra usage ,but now that doesnt work ,do you anything could help
**u/One_Grapefruit_2948** · 2026-10-21 19:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbwg7w/guys_i_used_use_vpn_when_i_hit_the_limit_of_free/)

[removed]

---

## I got tired of hitting my Opencode Go limit by surprise, so I built a live usage meter right in the TUI sidebar
**u/sitozhad** · 2026-10-21 18:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbw2el/i_got_tired_of_hitting_my_opencode_go_limit_by/)

You're deep in a session, the agent is cooking, and then... you hit the limit. No warning. Just a wall.

I kept alt-tabbing to the Console to check my OpenCode Go usage, so I built a plugin that puts it **permanently in the TUI sidebar**:

```
Go usage
5h  ──────────────── 0%   ↻ 4h 56m
7d  ──────────────── 3%   ↻ 6d 4h
30d ━━────────────── 10%  ↻ 25d 16h
```

## What you get

- All three windows: rolling (5h), weekly and monthly, the same numbers the Console shows
- Time until each window resets
- Bars turn **yellow at 75%** and **red at 90%**, so you see it coming
- Polls every 60s, countdown refreshes every 30s

## Setup (30 seconds)

Add it to `~/.config/opencode/opencode.jsonc`:

```
{
  "$schema": "https://opencode.ai/config.json",
  "plugins": ["opencode-go-usage-meter"]
}
```

Restart OpenCode and it shows up in the sidebar footer.

## Privacy (because I'd ask too)

- Read-only: never sends prompts, never writes credentials
- Your key only goes to `opencode.ai/zen/go/v1/usage` (the official endpoint)
- No telemetry, no logging
- MIT licensed

**Requirements:** OpenCode v2 + a Go / Go Plus subscription.



---

It's brand new, so bugs are likely. If something breaks or you want another view (per-model breakdown? alerts at X%?), tell me and I'll build it.

**Comentarios:**

- **u/Halsandr** (↑1, 2026-10-21 20:46): Looks pretty similar to slkiser/opencode-quota, are you trying to solve a subtlety different problem?
  - **u/sitozhad** (↑1, 2026-10-21 20:56): Actually, no I didn’t know it existed until you mentioned it. I’d been looking for something like this for days, but since I couldn’t find anything, I just built it myself. It solves my problem, which was simply wanting to see how much of my Go! subscription I’ve used so far.

---

## guys i used use vpn when i hit the limit of Free usage to have extra usage ,but now that doesnt work ,do you anything could help
**u/One_Grapefruit_2948** · 2026-10-21 18:53 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbvwpu/guys_i_used_use_vpn_when_i_hit_the_limit_of_free/)

[removed]

---

## Limits Opencode Go 10$ vs. Claude Code 20$
**u/Commercial_Guard_448** · 2026-10-21 18:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbvj6c/limits_opencode_go_10_vs_claude_code_20/)

How do the limits of the OpenCode Go $10 plan compare to the ClaudeCode $20 plan when using Claude models in OpenCode? And what are the advantages of OpenCode Go regarding free models? Are they worth it?

**Comentarios:**

- **u/ApprehensiveDelay238** (↑0, 2026-10-21 18:41): Edit: you're getting a 50% benefit from Claude/ChatGPT on go compared to PAYG. But you're likely getting more out of a Claude subscription compared to PAYG.
  - **u/Equivalent_Stop_4735** (↑2, 2026-10-21 18:42): Yes it does.
    - **u/Decent_Gap1067** (↑0, 2026-10-21 18:42): 3 prompt and you're done lol
    - **u/ApprehensiveDelay238** (↑1, 2026-10-21 18:43): You're right. Must be a newer thing.
  - **u/retardhari** (↑2, 2026-10-21 19:17): whats Payg?
    - **u/ApprehensiveDelay238** (↑1, 2026-10-21 19:23): Pay as you go.
      - **u/retardhari** (↑1, 2026-10-21 19:25): oh i didnt know abt 50% benefit on claude/gpt via go tho like are they subsidizing a bit on those models?
        - **u/excellentforcongress** (↑0, 2026-10-21 19:33): they lost 80 billion the first half of this year. they are a non-business and are just trying to get data/pump user numbers to try to dump the business on other investors in an ipo
- **u/Christosconst** (↑8, 2026-10-21 18:50): I have both subscriptions, use opus 5.5 on the $20 plan and havent hit a limit yet. But my usage is low, maybe 30-40 prompts a day
  - **u/diaracing** (↑1, 2026-10-21 18:52): What is your daily average token consumption?
  - **u/l0rd_raiden** (↑3, 2026-10-21 18:53): Coding prompts via oauth or just chat?
    - **u/Christosconst** (↑3, 2026-10-21 18:54): All coding, I’m a senior dev
      - **u/No_Committee8392** (↑-1, 2026-10-21 19:18): You’re a senior dev with a $20 subscription? And you don’t hit the limits? I find that surprising… Or maybe you’ve embraced agentic development less than some of the people here (including myself)  
          Or you just ship less probably
        - **u/Christosconst** (↑3, 2026-10-21 19:19): I’m actually a tech lead so not as hands on as i used to be
          - **u/No_Committee8392** (↑1, 2026-10-21 19:23): Ahhhh okay that would explain it
        - **u/excellentforcongress** (↑0, 2026-10-21 19:32): they are trying to give more inference to get more data before their final push to ipo and monetize. they have probably cooked up some scheme/plan to ban open source right after american companies go public, because otherwise none of the math makes sense. they lost 80 billion dollars... in the first HALF OF THIS YEAR
  - **u/OldWorldKestrell** (↑1, 2026-10-21 20:13): Same here, working 20/80 claude vs opencode, except when it's close to Claude's session reset, then I push Claude to do more.
- **u/Amarsir** (↑3, 2026-10-21 19:17): If you want Claude models, get a Claude sub. It's no question.
    
    Haiku is pretty much unlimited. Opus you can get a lot of use out of, but if you use it exclusively you can hit the limit with enough work. But using what I consider a reasonable balance of Opus to write and Haiku to execute on plans, I don't come close. The only time I hit the 5 hour limit is when I had two instances going and communicating with each other.
    
    Opencode Go is fine if you only want to spend $10 and you can dabble across a range of different models. And the free option stops you from hitting a wall. But you're better off just getting the value from Claude sub.  It's like $400 minimum in API value for $20.
  - **u/look** (↑2, 2026-10-21 19:32): But that $400 value of Anthropic API for $20 costs about $10 on non-Anthropic model APIs…
    - **u/Amarsir** (↑2, 2026-10-21 20:01): Like I said you can get by with $10. But you're not getting anything Opus level and anything you're going to get lots of use of on Go is pretty comparable to Haiku.
        
        If DS 1017 was faster you could maybe make a case for that in-between spot, because it's smarter than Haiku max. But also more expensive per-task, and even if they were the same $80 is less than $400. As it stands now, the reason you'll never hit the limit on DS 1017 is because it's too slow to use your quota.
      - **u/look** (↑0, 2026-10-21 20:55): Oh, I don’t use Go. I use faster providers that also have better prices on the bigger models.
          
          I stopped bothering with Go after they went all in on the “Cheapseek” market. 1017 is finally a decent model, but it needs a faster provider, not cheaper one.
          
          But I was just objecting to your “$400 in value” comment. That’s a number Anthropic made up.  Outside of a very narrow set of tasks, that same “task value” can be had for a fraction of the price.
- **u/Pirateshack486** (↑3, 2026-10-21 20:27): For homelab admin tasks the 10$ opencode with deepseek is amazing, I just let my hermes get on... for coding work has claude code 20$ definitely better at that

---

## What's the best model for math research?
**u/No-War-6618** · 2026-10-21 18:30 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbv9lg/whats_the_best_model_for_math_research/)

As the title states, I'd like to know y'alls opinion on which ones are the best. 

I tried GLM and DeepSeek as they are well known, but they have a low context window, and compaction gets to the better of them. 

I'm looking for something that can handle logical work, and longer tasks.

**Comentarios:**

- **u/AdFun4897** (↑1, 2026-10-21 19:00): Get claude $20 subscription and use Opus 5.5.
    
    Check the AA intelligence index for model comparison. No open source model in Opencode compares to Opus 5.5 in reasoning and research

---

## What is a "Complex" task for AI When Judging models?
**u/rev_ex_id** · 2026-10-21 17:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbub20/what_is_a_complex_task_for_ai_when_judging_models/)

I see this a lot, and I'm having trouble myself identifying what is considered a "Complex" task. 

For example, when comparing Opencode Go to Claude, I often see the advice: "Claude has better models for more complex tasks, but for most people, Opencode Go is plenty of bang for the buck."

Even when choosing between models: "Your more complex tasks should be done with Deepseek V4 Pro or GLM 5.3, but your grunt work can be done with the flash models."

But this work is difficult for me to define in my head, and I often feel what is "complex" to one person isn't to another. 

A few example projects

* I have a mostly Typescript based web-app that is for recipe hosting. 
* I have a Display Manager application primarily built in QML and Python
* I have a (pretty rudimentary) game engine written primarily in C++

Would complexity be dependent on size and language? Does CI|CD portions matter?

I guess, when someone talks about complexity when discussing models, what is being referenced?

**Comentarios:**

- **u/migsperez** (↑2, 2026-10-21 18:07): [https://opencode.ai/data](https://opencode.ai/data) here you can see what most people use with Opencode.   I normally choose a budget like Deepseek, Muse or GLM model and stick with it for most of the day.  If I notice it's slow I may choose another.
    
    My tip is create your own benchmark in a repo, set the model loose, review it's changes using another smart independent model, get a score.   
      
    Create a few one shot prompts to see how well it does.   Here's one:
    
        Prompt 1:
        Build a Windows Tetris game with keyboard controls, scoring, increasing difficulty, and pause/restart. Deliver a standalone .exe that runs without installation.
        
        Prompt 2:
        Add local two-player mode with side-by-side boards and separate controls (WASD and arrow keys). The last player standing wins. Deliver the updated standalone .exe.
- **u/AdFun4897** (↑2, 2026-10-21 18:21): Migrating languages, refactoring code, handling db schemas = hard
    
    Everything else is subjective
- **u/sugarw0000kie** (↑1, 2026-10-21 19:43): The answer is that it really depends on the workload and is super subjective. Lots of free models come about on opencode so good time to try them out 
    
    Smaller models like DS flash, Luna, mimo 2.6 will do fine when they don’t need to reason deeply about how what they’re working on affects other things in the codebase. It’s not that they can’t do this, but the second their working on an area of code that creates a domino effect in other areas of the codebase, they’re going to struggle more and likely have a much longer chain of reasoning/trial and error getting there if they have to figure it out. The bigger “pro” models can usually see the big picture more clearly. It’s like small models have tunnel vision and can focus very well on a little area but degrade as the task requires them to keep more things in their “head”
    
    So big code base can be harder if not structured well. Keeping it modularized helps manage context limitations
    
    Typescript and python are some of the most popular languages, those two might be easier. But lots of variation on frontend, lots of people like Claude models for that reason. Some models are just better at different things so sometimes it’s worth it to use multiple. The c++ game engine could be harder, idk. Like I’ve found mimo models to handle rust very well in the past. I usually like the way GPT writes code, normally pretty understandable, where DS has given me spaghetti in the past. But if you’re not spending much time looking at code anymore maybe it doesn’t even matter lol.

---

## Je viens de commencer le vibe coding j'ai du mal pour codé des appli qui ne soit pas des applications web pour mon pc vous avez des conseils a me donner
**u/MIRROR9583** · 2026-10-21 17:53 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbu9l6/je_viens_de_commencer_le_vibe_coding_jai_du_mal/)

**Comentarios:**

- **u/bangsmackpow** (↑1, 2026-10-21 18:07): Need more information.  
    
    General rule of thumb, if you can't explain the problem and the desired outcome, it won't do what you want.
  - **u/MIRROR9583** (↑1, 2026-10-21 18:17): Par exemple j'ai codé une application de veille pour tester opencode je l'ai demandé un appli qui surveille la ram le CPU et le stockage et de me signaler quand la mémoire atteint une certaine limite mais le résultat était un terminal qui me rediriger vers un lien local host
    - **u/bangsmackpow** (↑1, 2026-10-21 18:27): Solo para aclarar: ¿quieres que una aplicación local devuelva un conjunto de datos a la terminal?
        
        
        
        ¿Mac, Windows o Linux?
      - **u/MIRROR9583** (↑1, 2026-10-21 18:41): Pas vraiment je l'ai juste demander de ce lancé en arrière plan
    - **u/awkard_guy_** (↑1, 2026-10-21 19:30): Make an exe file.
      - **u/MIRROR9583** (↑1, 2026-10-21 19:57): Je l'ai déjà fait mais ça rien changer juste un terminal noir avec un lien local host

---

## model preference
**u/Classic_Raspberry_60** · 2026-10-21 17:53 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbu8uv/model_preference/)

which model do you guys prefer for coding while being free i been using minimax m3.1 and i feel like it works a lot better than deepseek v4.1 flash and glm 5.3 flash and also doesn’t refuse basically at all am i the only one that prefers minimax m3.1 over deepseek and glm ?

**Comentarios:**

- **u/migsperez** (↑1, 2026-10-21 17:59): I've been giving Deepseek v4.1 a go again after many months.  I was using Muse 1.3 over the past month.
    
    Deepseek seems to have more imagination but makes more mistakes.  Muse is solid, it's output isn't excessive and it stays on target.  I think I'm going to use Deepseek for front end and idea exploration but use Muse for the rest.  We'll see it's still early in the eval.
    
    I used Space Bunny early on but I haven't touched Minimax m3.1 yet.  From the examples I've seen it seems the model is a noticeable improvement over Space Bunny and m3.0
  - **u/Classic_Raspberry_60** (↑2, 2026-10-21 18:05): yeah i was using muse 1.3 before it went away now i switched to minimax m3.1 has been very well for me and definitely think you should try it , deepseek at least for me always keeps going back and forth and just overthinking so bad not doing what i need it to do while taking forever and minimax will one shot it almost 98% of the time even when telling it to do an entire paragraph of stuff
    - **u/OptimizedGamingHQ** (↑2, 2026-10-21 18:07): DS on low doesn't overthink and the output is good
        
        DS High for planning big changes, low for small changes, and use build on low
      - **u/Classic_Raspberry_60** (↑1, 2026-10-21 18:09): oh i never really thought about that i always just put the model on max 😂 ill try that out though and see what happens
        - **u/OptimizedGamingHQ** (↑2, 2026-10-21 18:10): I benchmarked it
            
            - Muse Spark Contributor 1.3 Xhigh | 7m 25s
            - DeepSeek V4.1 Flash Low | 8m 36s
            - GLM v5.3 Flash Low | 17m 26s
            - DeepSeek V4.1 Flash Max | 33m 54s
            - GLM v5.3 Flash Max | 57m 42s
          - **u/migsperez** (↑1, 2026-10-21 18:41): Huge difference in the Deepseek thinking levels
- **u/jarvis123451254** (↑4, 2026-10-21 18:00): I used only free models till date for my personal scripts and such and minimax 3.1/space bunny works way better than other free ones as of now
  - **u/Classic_Raspberry_60** (↑2, 2026-10-21 18:05): yeah i think the same been loving it

---

## I had Claude build a small Wear OS app so I can dictate into my PC from my watch (works with Hex & Handy)
**u/hiddenpr0cess** · 2026-10-21 17:38 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbtuh9/i_had_claude_build_a_small_wear_os_app_so_i_can/)

I use Hex for local dictation on my PC and wanted to use it from my watch, so I asked Claude to build a small app for it. It's called Wristle: hold the button on your watch, talk, and the text appears on your PC wherever your cursor is. Transcription stays local in your dictation app. The watch only sends audio over your home Wi-Fi.

Tested on a Pixel Watch 4 with Hex on Windows. Other watches and Mac/Linux should work, but I haven't tested them. If you try it, let me know how it goes!

Free and open source: https://github.com/unknownprocess/wristle. A ⭐ helps if you find it useful!

---

## What does Cost mean on the summary page
**u/Guyserbun007** · 2026-10-21 17:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbtczk/what_does_cost_mean_on_the_summary_page/)

https://i.redd.it/fjawcfuntuwh1.png

I have subscribed to the OpenCode Go $10 per month plan. What does the Cost ($7.47) mean? Is it an additional cost I need to pay on top of the $10, or is it just tracking the "amount" of tokens used?

**Comentarios:**

- **u/borobinimbaba** (↑1, 2026-10-21 17:27): You should've used a big ass model to burn through 50% of your monthly quota with 40 million tokens
- **u/squirrelscrush** (↑1, 2026-10-21 17:32): It's the equivalent cost of the tokens used as if you were paying for it through API

---

## 🔥 Meta Muse Wonder is now available on OpenCode
**u/afanasenka** · 2026-10-21 17:00 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbsrta/meta_muse_wonder_is_now_available_on_opencode/)

...

**Comentarios:**

- **u/One_5549** (↑3, 2026-10-21 17:06): YES
- **u/breadnone** (↑11, 2026-10-21 17:16): was looking for the word \*free\*
  - **u/Expert-Couple-8639** (↑4, 2026-10-21 17:32): or contributer
    - **u/Wrekklol** (↑3, 2026-10-21 19:26): What is contributer?
      - **u/Metwalley** (↑1, 2026-10-21 19:37): You use the model for free in exchange of them training on your prompts
        - **u/Wrekklol** (↑1, 2026-10-21 20:17): Hmm I just get "Go usage limit exceeded" when trying to use models like "Gemini 4 Argon Contributor" and "Muse Spark 1.3 Contributor".
          - **u/bleakj** (↑1, 2026-10-21 20:53): They're heavily discounted, not free
- **u/Wise-Chain2427** (↑7, 2026-10-21 17:50): just miss "Contributor"
- **u/scottchiefbaker** (↑4, 2026-10-21 18:15): How is this different than Muse Spark?
  - **u/Cool-Service-8067** (↑7, 2026-10-21 18:33): suposadly better, also way more expensive, imo mid model, not worth it for any work most people are doing
  - **u/Amarsir** (↑3, 2026-10-21 19:30): Muse Spark is "Flash". Wonder is their attempt at "Pro". But like a lot of Pro versions it isn't worth the cost. And this is V1.0 so it's especially not too impressive.
- **u/Dorima_boy** (↑6, 2026-10-21 18:52): 20 usd output ☠️
- **u/packsolite** (↑3, 2026-10-21 19:24): Go or zen? Or both?
- **u/mitchins-au** (↑3, 2026-10-21 19:57): No contributor, no dice
- **u/kapsule_code** (↑2, 2026-10-21 20:53): Yo he probado durante unas semanas Muse Spark 1.3 y me encanta.

---

## 🔥 Meta Muse Wonder is now available on OpenCode
**u/afanasenka** · 2026-10-21 16:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbsrab/meta_muse_wonder_is_now_available_on_opencode/)

---

## Why is my Go API spend so low ($0.08 / $3.28) when my monthly limits are 99% used up
**u/Scared_Building_3127** · 2026-10-21 16:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbrqmz/why_is_my_go_api_spend_so_low_008_328_when_my/)

Hi all,

Need some help

I'm looking at my usage dashboard, and I'm a bit confused about how the billing/spend is calculated vs. my actual usage limits.

My monthly limit resets in about 6 days and says it is **99% used**, but my extra usage credits/spend totals seem incredibly low compared to how much I've actually been using the models.

Here is what my dashboard looks like right now:

Usage & Limits

* **Rolling:** 1% used *(Resets in 34m)*
* **Weekly:** 25% used *(Resets in 4d 8h)*
* **Monthly:** 99% used *(Resets in 6d 12h)*

  
If I read this right, opencode is aware that they have given me 3.30 of usage for the 10$ I paid them and... that's okay? 

  
I know the peak off peak pricing and token cost increases etc that come with extra context and whatnot but I'm fairly confident my workflows are not affected by that. What could this be?

  
Thanks for any help! 



Table attached:  
Model Cost Breakdown

|**Model**|**Requests**|**Input Tokens**|**Output Tokens**|**...**|**Total Tokens**|**Spend**|
|:-|:-|:-|:-|:-|:-|:-|
|**deepseek-v4.1-flash**|625|7.3M|28.6M|\-|785.4k|**$3.28**|
|**glm-5.3-flash**|375|267.4k|\-|\-|85.0k|**$0.08**|

**Comentarios:**

- **u/RepulsiveRaisin7** (↑3, 2026-10-21 16:28): Extra usage is not your Go usage
  - **u/Scared_Building_3127** (↑1, 2026-10-21 16:47): I'm confused. What do you mean by extra usage?
    - **u/Zoro-chi** (↑1, 2026-10-21 18:30): Extra usage is what you have in your opencode wallet (Not your $10 sub). This is used when you access models that are paid or not on the opencode go model offering like Anthropic models
- **u/xRebellion_** (↑1, 2026-10-21 17:17): That's weird. Have you checked the "Last 30 days/Last 7 days" record and see what is being used?
  - **u/Scared_Building_3127** (↑1, 2026-10-21 17:39): this is the issue. i never clicked all time. in my defense, it's far removed from the main UI and the stuff below doesnt make it clear that one button far above controls it. thanks for the help
    - **u/xRebellion_** (↑1, 2026-10-21 17:44): Filters are usually what I'd look for when numbers don't add up haha. Glad could help

---

## Used OpenCode to Import MacOs's Airpods Handling to Windows! (REA)
**u/Little_Marsupial9383** · 2026-10-21 16:09 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbrdts/used_opencode_to_import_macoss_airpods_handling/)

![video](pswa5o6wguwh1 "Connection PopUp")

So, I use Windows daily because of my work, but I wanted to be able to use my AirPods the same way they are handled around the Apple Ecosystem. The hardware is great; the software experience is not. So I spent a weekend reverse engineering the macOS AirPods connection handling, brought it to windows and now it works seamlessly.  
  
What it does:  
\- When I open the lid, a small dark card appears with the buds and case, battery levels, and connection status, I did not use apple's UI assets because It was not worth the extra work.  
\- Windows connects and switches the default audio output automatically.  
\- Closing the lid dismisses the card, and stops the connection automatically.  
\- It runs at login as a tiny background watcher. No tray icon, no telemetry, no network listener, lean, simple and imported directly from Apple's environment (Of course I had to do some workarounds, but It is essentially the same functionality, so I am very happy with it)  
\- ANC and Audio modes were also imported so I can control that as well.  
  
Whenever I want to switch them to my Iphone, just simply start listening to something there, audio transfers seamlessly as well.  
I know there are tools around for this, but I did not want to install any unknown 3rd party software or pay for something I could do myself.  
  
Not selling anything and not trying to turn this into a product. It’s just my daily driver. Curious if anyone else has gone down this rabbit hole.

**Comentarios:**

- **u/ayaanngandhi** (↑4, 2026-10-21 16:15): Hey! There's a pretty active community around this project called LibrePods, and the project itself is open source and about connecting AirPods and bringing full functionality to Android. I have contributed there once too. A windows client wasn't yet made, but was much needed. It would be a lot of help if you could upload your code to GitHub and open source it. Thanks!
  - **u/Little_Marsupial9383** (↑1, 2026-10-21 16:20): Of course, I will put that on my list!

---

## Thinking of getting opencode. Should I buy it or not?
**u/jackybacksy3636** · 2026-10-21 16:00 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbr469/thinking_of_getting_opencode_should_i_buy_it_or/)

Had recently purchased claude pro subscription and was working with it and the usage limit got used up pretty fast. The thing I am working on currently takes alot more than i expected it to take (working with n8n) - using claude as MCP. 

With recent hacking, idk how the scene is with open code. I'm on a budget as well. Need some thing for my n8n and later, vibe coding some tools. What do you guys suggest?

I'm a complete beginner in AI. I just read in gpt that with open code you can have multiple models running in one environment. I thought maybe I can use one main agent with gpt/DeepSeek and the rest, with their specific capability (sub-agents).

Please feel free to share your thoughts and how do you structure,plan,use repo etc so I can also try to learn the same.

**Comentarios:**

- **u/RepulsiveRaisin7** (↑2, 2026-10-21 16:11): It's free, just try it
  - **u/jackybacksy3636** (↑-1, 2026-10-21 16:13): Is it safe? 😭 
      How do you use it
    - **u/RepulsiveRaisin7** (↑3, 2026-10-21 16:15): Show some initiative holy fuck
      - **u/jackybacksy3636** (↑1, 2026-10-21 16:16): The ones who got hacked had external api keys in opencode? This was the only affected party?
- **u/Lazy-Lie2833** (↑2, 2026-10-21 16:14): You can create an opencode account/just download it and use their free models, there is limits but upgrading to go is fairly cheap and offers about $80 of api in Deepseek v4.1 flash - recomenend it highly to fill in gaps or let Claude usage go further
  - **u/jackybacksy3636** (↑1, 2026-10-21 16:18): Thanks broski. I wanted to know which platform do you guys use to run main agent and sub agents with different models at once?
    - **u/Lazy-Lie2833** (↑1, 2026-10-21 16:25): Ah gotcha - So I have made my own system. Claude Code with Opus 5.5 is the orchestrator, it delegates work to agent ( fresh context) via a tool called agentBus, just allows agents to speak and send work amongst each other. So essentially tell Claude what to do and they spin up opencode sessions with the correct model depending on the task. Made agentBus myself but it’s quite simple overall. I recomend finding something that just works for you as everyone has their owns ways of productivity. Lately I don’t touch the CLI I route all work requests through a Plane board and speak to agents on Zulip instead
      - **u/jackybacksy3636** (↑1, 2026-10-21 19:31): That sounds awesome broski
- **u/thezombieparade** (↑1, 2026-10-21 16:19): Can you give a rough example how much usage you got per session from Claude pro?
  - **u/jackybacksy3636** (↑1, 2026-10-21 16:21): 10% weekly limit and done one set of usage for current session and it's 39% again (2nd set).
      Idk how else to measure. (3-4 hrs chatting with claude)
- **u/xatey93152** (↑1, 2026-10-21 16:34): Before buy. Compare direct deepseek and opencode deepseek. You will notice there's so much differennce. I'm sure they did something fishy
  - **u/jackybacksy3636** (↑1, 2026-10-21 16:49): Read somewhere they limit the flow
- **u/torrso** (↑1, 2026-10-21 16:46): No. The current owners are fine.
  - **u/jackybacksy3636** (↑1, 2026-10-21 16:48): Ooh okay.
- **u/Amarsir** (↑1, 2026-10-21 19:28): You should be able to get pretty unlimited use of Haiku under the Claude sub so if you can balance there isn't a lot of benefit to adding an Opencode Go sub IMHO. You can and people do. I just think it's unnecessary.
    
    The Opencode harness is great, and after trying Claude Code for a few days I went back to it. I use the Oh-my-opencode-slim extension which makes subagent delegation very clever.
    
    https://github.com/alvinunreal/oh-my-opencode-slim
    
    You also need the opencode-claude extension to use your Claude sub with it. 
    
    In either harness use Opus medium or high for thinking stuff and Haiku high or extra high to execute. Sonnet is beaten in value by one or the other at every point except medium, and few things land in precisely that range.
  - **u/jackybacksy3636** (↑2, 2026-10-21 19:33): Thanks broski. Will do.

---

## Where is my Opencode storing its configurations, etc
**u/ProgrammusMaximus** · 2026-10-21 15:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbqwq3/where_is_my_opencode_storing_its_configurations/)

Greetings:

I am running opencode 2.1.2 in a docker container. I am concerned, because I am not seeing the various files that I am expecting to see for configuration, projects, or anything else.

My docker-compose file has the following volumes:

`volumes:`

`- ./workspace:/app`

`- ./opencode-config:/root/.config/opencode`

`- opencode-data:/root/.local/share/opencode`

Unfortunately, using opencode-web I created a project out of the app folder (which I didn't want to do) and did a session. I wanted to remove the project so that I could create some directories under /app (in order to be able to do multiple projects) since opencode web doesn't allow the user to actually edit configuration files or add directories. Unfortunately, looking at the directories pointed to in my docker-compose file, I am seeing empty directories. I am not even seeing anything under opencode-config!

So where is my opencode instance getting its configuration? Where is it storing my project information? And how do I remove the project so that I can start over again?

**Comentarios:**

- **u/Unhappy_Ad8103** (↑1, 2026-10-21 19:22): Hi, the config is in /root/.config/opencode/
    
    You did not tell how you are "looking at the directories pointed to in my", so we can't know why you see empty directories
    
    if you do  
    docker exec -it <container\_name> sh  
    you get a shell where you should be able to find the config
    
    however, if you do  
    docker debug <container\_name>  
    you won't, as / in debug is root of the debug environment, not your container, in my case the path to container root is  
    /proc/1/root/  
    meaning docker config is in   
    /proc/1/root/root/.config/opencode
  - **u/ProgrammusMaximus** (↑1, 2026-10-21 21:03): Thank you, Unhappy\_Ad8103, for your response.
      
        
      I am looking at the contents of the directory by ssh'ing over to the machine where I am running Opencode, cd'ing to the opencode directory where the docker compose file is, and doing an "ls -a" on the workspace, opencode-config, and opencode-data directories.  Since (for example) my docker-config directory maps to the /root/.config/opencode directory in the container, I should see the config file. 
      
        
      Except that I do not.
      
        
      I am familiar with the docker exec command (I have been using it for many years now). I did use it to do an ls -a of /root/.config/opencode from within the container, just in case I might have misdone the mapping. That directory is also empty.
      
        
      This is why I am here.
      
      As for the possibility that the config is actually in /proc/1/root/.config/opencode: no, there is no /proc directory in the container. There is a /root directory, though. Unfortunately, the /root directory does indeed have a .config/opencode directory in it.
      
      So: this is why I am wondering: where is my Opencode instance getting its configuration and its project information if the config file(s) are not where they are supposed to be?

---

## I got tired of paying for AI sub, so I built a website aggregating free AI models across providers
**u/zaCKoZAck1** · 2026-10-21 15:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbqnoi/i_got_tired_of_paying_for_ai_sub_so_i_built_a/)

**Comentarios:**

- **u/afanasenka** (↑0, 2026-10-21 15:59): I got tired of being free beta-tester for all these "free/stealth/flash gordon" models and providers, so I started paying for a normal AI sub... 😏
  - **u/YoRt3m** (↑1, 2026-10-21 17:30): >Free
      
      No, you get agents working for you for free. 
      
      Nobody is forcing you, but don't paint it in such an disingenuous way.
- **u/foreverleveling** (↑0, 2026-10-21 19:02): Thanks very usefull case of use for me!
- **u/Fun_Squirrel5446** (↑1, 2026-10-21 21:11): "I built" = I vibe coded, with a single prompt, no functional testing, and no security testing, please feed your personal data into my slop.

---

## Is it impossible to connect the Mistral Pro subscription to Opencode?
**u/Cool_Samoyed** · 2026-10-21 15:30 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbqaux/is_it_impossible_to_connect_the_mistral_pro/)

---

## How to use tokens right
**u/thevoidman_** · 2026-10-21 15:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbpzya/how_to_use_tokens_right/)

After muse spark is no longer available as free i switched to deep seek but i found that i have only 200k tokens so how can i use it Wisely and is there any free models that give me more tokens and still good? I remember muse spark gave me like 1 million free tokens so :/

**Comentarios:**

- **u/CurtissYT** (↑2, 2026-10-21 15:19): While you can, use minimax m3.1
- **u/reybrujo** (↑1, 2026-10-21 15:23): Are you talking about context?
  - **u/thevoidman_** (↑1, 2026-10-21 15:24): Ah yeah
    - **u/reybrujo** (↑2, 2026-10-21 15:28): DeepSeek 4.1 Flash has 1 million context. But even 200k is a lot, I worked for 4 hours before reaching the context limit in an enterprise software, yesterday I spent 14 hours until I neared the 1 million context size. I think you need to get good at prompting and not just go "do something", "make this better", "change all".
- **u/ayaanngandhi** (↑1, 2026-10-21 16:22): There's a skill called DCP compression (I think). Set it to auto compress at 200k tokens. Each turn shouldn't take more than that
  - **u/squirrelscrush** (↑1, 2026-10-21 17:41): It's a plugin

---

## New Deepseek Flash, when?
**u/Leather-Cod2129** · 2026-10-21 14:29 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbopdz/new_deepseek_flash_when/)

Hi,

Any info on when it'll land on GO?

Thanks

**Comentarios:**

- **u/theythinkitsallover** (↑9, 2026-10-21 14:30): She there already bud
- **u/Diligent-Loss-5460** (↑14, 2026-10-21 14:37): Let me teach you a valuable skill. [https://gprivate.com/6mdqe](https://gprivate.com/6mdqe)
  - **u/Killeramn-26** (↑1, 2026-10-21 14:44): I feel like I got rickrolled.
  - **u/honglac3579** (↑1, 2026-10-21 15:04): Bro do all of that just to troll
- **u/jarvis123451254** (↑5, 2026-10-21 14:37): already there
- **u/OrdinaryLemon731** (↑-2, 2026-10-21 14:39): Hopefully they add it soon. More model options are always welcome, especially affordable ones.
- **u/ConstantEmotion2211** (↑1, 2026-10-21 14:44): I feel like tasks a getting a lot more time? Is this due to the infrastructure or to the model?

---

## Can i learn coding with help from open code?
**u/Professional_Day4470** · 2026-10-21 14:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbolxt/can_i_learn_coding_with_help_from_open_code/)

So next year im gonna go to college and choose informatics, and im need assistance to help me start from scratch because I'm originally a visual and design person, soo if you guys Have you ever tried learning coding with open code? Please give me some tips. Thanks!

**Comentarios:**

- **u/robeybeswick** (↑1, 2026-10-21 14:29): I mean it’s easy to get it to bootstrap projects for you that you can then observe and learn from. But that is also a vice. If you really wanna learn fundamentals of coding. Which might not be relevant in a few years. I’d buy a book and start from hello world. Some object orientated programming etc. 
    
    I would probably learn more architectural concepts so you know how systems fit together
- **u/Difficult_Plantain89** (↑1, 2026-10-21 14:30): You could make lesson plans Opencode and have Opencode grade your work.
- **u/Monecreiff** (↑1, 2026-10-21 14:39): I feel like ai teaches like American teachers but better since you can learn at your own pace and learn things that are useful to yourself
- **u/Johell1NS** (↑3, 2026-10-21 14:42): I'll definitely be unpopular, but in my opinion, rather than using opencode to learn how to program, you'd be better off using opencode to learn how to use AI in the best possible way. AI moves very fast, and the things there are to know and learn are not trivial, if you want to learn to use it in a truly productive way compared to the masses. By now, knowing how to program is secondary; the things to learn are others, and sooner or later I'm sure the universities will understand that too.
  - **u/nonexistentnight** (↑0, 2026-10-21 17:02): That sounds misguided to me. "Using AI in the best possible way" means learning how to do the things you expect it to be doing so you can guide it better. The people who can most effectively use AI tools are the people who are most familiar with what they expect it to be doing for them. You may not need to know syntax or the the exact names of library functions or whatever. But having a basic understanding of programming concepts is essential if you want something better than slop.
      
      OP if you have a Mac, check out Swift Playground for a very basic intro. It feeds in to Apple's more advanced tutorials as well. There's probably other alternatives you could use as well. It doesn't matter much what system or language you learn on, the goal is to understand the concepts.
- **u/lordcohliani** (↑1, 2026-10-21 14:54): I think you missed the point
- **u/my_new_accoun1** (↑1, 2026-10-21 15:14): Not with OpenCode. That codes for you. Instead ask like ChatGPT on the website to help, that way it can teach you with test rather than writing code on your machine. Or [Obsidian](https://obsidian.c00l.site)
- **u/Opening_Act_2580** (↑1, 2026-10-21 15:39): No. However, if you do want to do this with any coding agent, turn off its ability to write any file, because once you are familiar with laziness you cannot recover.
- **u/GlitteringComputer52** (↑0, 2026-10-21 16:06): JUST FREAKING LEARN HOW TO CODE  
    READ THE FUCKING MANULE
  - **u/Professional_Day4470** (↑1, 2026-10-21 16:06): Im sorry, imma delete this post

---

## Best multi-agent OpenCode setup using ChatGPT Plus and free models?
**u/Negative_Macaroon_85** · 2026-10-21 13:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbncte/best_multiagent_opencode_setup_using_chatgpt_plus/)

I'm using OpenCode Desktop with ChatGPT Plus, mainly for Power Apps, Power Automate and other development projects. I'm trying to build a multi-agent workflow using strong free models for simpler tasks while reserving GPT models for complex work, without exhausting my usage limits. My current setup idea is:  
**Orchestrator (GPT-6 Luna):** Task coordination and agent management.  
**Luna (GPT-6 Luna):** Investigation, debugging and analysis.  
**Reviewer (Strong reasoning model):** Code review, security and regression checks.  
**Sol (GPT-6.1 Sol):** Coding, fixes and implementation.  
**Astra (GPT-6 Astra):** Architecture and complex refactoring.  
I'm also struggling with organizing [AGENTS.md](http://AGENTS.md), agent configurations, skills and Markdown reports without wasting context or creating redundant documentation. Has anyone built a similar setup? Which free models would you recommend for these roles, and how would you distribute tasks to get the most out of a ChatGPT Plus subscription? I'm open to changing the entire architecture if there's a better approach.

---

## We don't need to make AI with big brains, they can just use a map (AI Model Concept)
**u/FluidModeNetwork** · 2026-10-21 13:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbn21j/we_dont_need_to_make_ai_with_big_brains_they_can/)

Large parameter models are way too large. They are certainly capable models, astra, Claude, kimi, but what do they have in common. They primarily have all of the knowledge to complete tasks in there "brain", and we are seeing that there are smaller models showing capabilities of larger models that don't need billions of parameters.

There are two people who take a test, the nerd who's been studying all night and day, and will most likely ace the exam, and the ditz, the guy who's pretty care free but doesn't have much going on in their head, doesn't care about the exam at all. The professor sees the ditz and and feels bad for them, so he makes an exception, 1 sheet of paper of notes to use for the exam. Normally, the ditz would fail but with the cheat sheet their intelligence matters significantly less. No memorization needed, just a basic grasp on the fundamental concepts, right?

Lets say the professor didn't put a limit on the amount of notes used for the exam. After a certain point, how much could the ditz not need to know and just follow their notes? We are trying to make instead of a brain that knows everything, to a brain that knows how to navigate everything. The ditz of course couldn't write their own notes, but they instead could employ someone to make the "map" for them.

So here's my idea.

1. An rlm digs through a library or database to build a map
2. That map is then used by a small model trained for the tool calls to probe the map
3. The small model can then answer any questions about the information given by the map

Pros of this idea

1. Results are repeatable, because the model can change its weights as much as it needs, but the map stays the same, the avenues stay the same.
2. The map **does not need to sit in vram or ram, but in storage.**
3. The model needs to know significantly less than it needs to be trained for, and can "cheat" complete comprehension in whatever the maps contents are
4. With a complete map, we'd have an almost exact way to train an llm to be fluent in any language, coding or spoken. Subject and skills too.

Cons:

1. We are trading ram with storage, so however large the map is would take up space
2. Trying to map a library/subject might take new concepts of conceptual organization to solve
3. Probably more, but cant think of any.

Excited to hear some responses.

**Comentarios:**

- **u/megablue** (↑1, 2026-10-21 13:32): I've already built something like or at least something at the bare minimum scale 
    
    [megablue/opencode-feature-map: Makes an OpenCode agent read your project's feature map before it reads your source.](https://github.com/megablue/opencode-feature-map)

---

## If you are not Experimenting with Open weight. You should be. Especially if it's 18 times cheaper.
**u/robeybeswick** · 2026-10-21 11:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbl0yd/if_you_are_not_experimenting_with_open_weight_you/)

---

## is deepseek expensive?
**u/Previous_Spread5920** · 2026-10-21 11:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbkupm/is_deepseek_expensive/)

[removed]

---

## i can't find "muse-spark-1.3-contributor-free" now
**u/National-Night3116** · 2026-10-21 10:44 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbjshe/i_cant_find_musespark13contributorfree_now/)

**Comentarios:**

- **u/acakaacaka** (↑2, 2026-10-21 10:46): As far as I know, they dont offer it for free anymore. They have other free models
- **u/100xReasonable** (↑1, 2026-10-21 10:47): It's not there
- **u/Tough-Obligation7386** (↑1, 2026-10-21 11:26): I gone bro, is gone... its a sad day to be alive
- **u/reybrujo** (↑1, 2026-10-21 12:56): Gotta pay the subscription.

---

## The math behind running Meta’s 816B Muse Spark Open locally: 4x M5 Ultra Mac Studios (1.2 TB/s, TB5 RDMA) vs. 2x Nvidia DGX Spark, KV cache limits, and the 3.5-year OpenRouter break-even
**u/Capatain_CV** · 2026-10-21 09:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbivu9/the_math_behind_running_metas_816b_muse_spark/)

With Apple and Meta showcasing the **816B parameter Muse Spark Open** (42B active MoE) running across M5 Ultra Mac Studios at ~37 tok/s, I put together a full numbers breakdown looking at the actual memory math, how Apple's Thunderbolt 5 RDMA tensor parallelism compares to Nvidia's DGX Spark, and whether a $21K–$43K Mac Studio cluster ever breaks even against cloud API pricing.



### Key Numbers & Hardware Breakdown (TL;DW):

**1. The Memory Wall (Weights + 1M Context KV Cache)**
* **Full Precision vs. 4-Bit:** Full weights require **~1.6 TB** of VRAM. Apple’s 4-bit MLX quantization brings the weights down to **~493 GB** (requiring either the upcoming 2x 512 GB Mac Studio config or 4x 256 GB machines at an illustrative ~$10,799/each = **~$43,196**).
* **The Context Trap:** While Spark Open supports a 1M token context window, an uncompressed 1M token cache across all layers baselines around **~266 GB** (less with Spark Open's hybrid attention, but still massive). Even a heavily compressed 2-bit weight download (~225–226 GB) on a 256 GB machine leaves barely ~30 GB before macOS overhead—meaning a "1M context model" is strictly limited by remaining unified memory.

**2. Apple M5 Ultra (MLX + TB5 RDMA) vs. 2x Nvidia DGX Spark**
* **M5 Ultra Cluster:** Each M5 Ultra delivers **1.2 TB/s** of memory bandwidth. Using MLX over **Thunderbolt 5 with RDMA**, switching from Pipeline Mode to Tensor Parallelism jumps 2-node speed (at 8K context) from **~16 tok/s to ~25 tok/s**, and **4x M5 Ultra Macs hit ~37 tok/s**.
* **2x Nvidia DGX Spark Constraints:** Each DGX Spark has **273 GB/s** bandwidth (>4x slower than M5 Ultra) and **128 GB RAM** (~242 GB usable across a pair). In testing, two DGX Sparks ran a 2-bit build at 8K context, choked at 32K context, and had to drop to a **~1-bit quantization** (which took 10m 48s to load over the network and generated at **~7 tok/s**).

**3. Coding Benchmarks (Does it beat GLM 5.3 & Kimi K3?)**
* **Intelligence Index (Artificial Analysis):** Spark Open scores **39** (compared to **45** for Meta's closed Spark 1.3).
* **Tool Use vs. Terminal Coding:** Spark Open wins on **MCP Atlas (89.2 vs. GLM 5.3's 84.2)**, but trails on **Terminal Bench 2.1 (76.4)** behind **GLM 5.3 (83.9)** and **Kimi K3 (85.0)**.

**4. The $43,000 Cloud ROI Math (3.5 Years to Break Even)**
* OpenRouter lists Spark Open at **$1.25/1M input** and **$4.25/1M output** (~$1.75/1M blended at a 5:1 input-to-output ratio).
* A $43,000 hardware budget buys **~25 billion cloud tokens** (>4 billion output tokens).
* At Apple's reported ~37 tok/s single-stream speed, generating 4+ billion output tokens takes **~3.5 years of 24/7 continuous generation** (before accounting for prompt prefill time or electricity).
* **Bottom Line:** Unless you are batching multi-user concurrency or have strict air-gapped IP/compliance requirements, you aren't buying a 4-Mac cluster to save money on API tokens—and single-machine users are likely better off looking at **Muse Glimmer (30B)** (<20 GB quantized, easily fitting on a 24GB/32GB Mac).

For those running multi-node local setups or eyeing the 512GB M5 Ultra config later this month: is anyone seriously considering multi-Mac TB5 RDMA over cloud APIs for coding agents, or is the 30B class still the local sweet spot?

---

## Best practices for moving a website from local to vps.
**u/katana1096** · 2026-10-21 09:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbiodx/best_practices_for_moving_a_website_from_local_to/)

Hello. I am using opencode to develop a website for a friend, as of now I am doing the front end (design and features) locally and the plan is to move it to the vps and use opencode to develop the backend and the structuring the database. But I am wondering is it enough to ask opencode to do this on the vps or it should learn something from the local opencode? I mean the local writes a guide in .MD file to clear things up for the opencode in vps.

I am taking the idea of hermes that it learns over time and perhaps something similar do exisits or helps in my case. 

Does this makes sense or I am  over thinking things? 

Thanks,

**Comentarios:**

- **u/sparex-controller** (↑1, 2026-10-21 09:42): Honestly, Git is probably the biggest thing here. Keep the project in a repo, commit your changes, and let the VPS work from the same codebase. The documentation fills in the context, you don’t need to transfer the local agent’s memory.
- **u/rdndds** (↑1, 2026-10-21 09:44): Told opencode to setup docker for the project and ask it how to deploy in the vps.
- **u/iam_a_human2** (↑1, 2026-10-21 14:02): tell opencode to setup Devenv + gh actions, its the easiest way to not deal with the dependency shit and have it work across machines

---

## Is the paid subscription deepseek flash faster than the free flash?
**u/RiskNumerous3860** · 2026-10-21 09:24 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbig9b/is_the_paid_subscription_deepseek_flash_faster/)

I've been using the free flash in the opencode OS standalone console and it is very very slow compared to using the flash api directly through vscode copilot harness.  

  
Is there any speed difference in the flash included in the cheap-seek metered flash with the opencode go paid subscription?

**Comentarios:**

- **u/OrdinaryLemon731** (↑4, 2026-10-21 09:32): I’ve seen reports of Go’s Flash endpoint being slower than the direct API too. I’d test both with the same prompt and context before paying just for speed.
  - **u/Fresh_Sock8660** (↑2, 2026-10-21 09:37): Wouldn't surprise me. Pay as you go is faster in every provider I've tried. Like, try codex vs gpt models through azure, it's a push bike vs a sports car. Not sure why people expect opencode go to be different, goes to show the cheaper the service the more people demand, because this is such a common complaint in the opencode subs.
  - **u/TripleMellowed** (↑2, 2026-10-21 11:27): Flash on Go is like 50-70% slower than direct API.
- **u/Standard_Ear_84** (↑3, 2026-10-21 09:34): Paid is much faster and better. Obviously just gut feel, but the free version got stuck trying to fix a simple bug and I eventually got sick of it and switched to paid, got it fixed next try which cost 10c.
  - **u/julieinpink** (↑1, 2026-10-21 13:55): Ten cents to fix a big instead of spending another hour fighting it? Sounds Iike a pretty good deal to me.
    - **u/Standard_Ear_84** (↑1, 2026-10-21 20:07): It's a fantastic deal. I wonder how much it cost DS.
- **u/Nenad1979** (↑2, 2026-10-21 10:22): In my expirinace they are the same
  - **u/RiskNumerous3860** (↑2, 2026-10-21 10:30): that's interesting, and do they seem slow to you?  just checking it's not something on my end.  When i use direct byok pay as you go deepseek in copilot it is fantastic.  if i ever run out of tokens and try to do some follow up in opencode free flash it is like 20x slower, almost unusable.
    - **u/Nenad1979** (↑2, 2026-10-21 12:48): They vary MASSIVELY troighout the day, so I can't rly give u a definite answer, but with muse spark going away, and ds41f newest version dropping for free i would expect them to slow af rn
- **u/Alanboooo** (↑1, 2026-10-21 10:30): I use it on deepseek harness, i fot 200++ tps stable
  - **u/buxA_** (↑2, 2026-10-21 12:00): harness for me refuses prompt which pass in opencode for some reason
- **u/gerald222** (↑1, 2026-10-21 11:01): Is the GO 4.1 Flash the 1017 variant does anyone know?
  - **u/Takeoded** (↑2, 2026-10-21 11:30): Yes it is.
- **u/Amarsir** (↑1, 2026-10-21 13:42): Not subbed to Go at the moment so I can't answer first-hand.
    
    I can say logically it probably comes down to whether it's worth them setting up a different provider for free. My gut is no - same provider but with cutoff and context window imposed. So you'd get the same speed. (And same quant, if that's a factor.)

---

## OpenCode with Deep Infra
**u/editemup** · 2026-10-21 09:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbi30p/opencode_with_deep_infra/)

Idea is to use open source models hosted on deep infra with open code, wanted to get a sense of the budget you plan for such a use case, also general feedback on quality of artifacts produced

---

## Why do people use open code instead of unsloth studio ?
**u/sly3x** · 2026-10-21 08:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbi0qv/why_do_people_use_open_code_instead_of_unsloth/)

**Comentarios:**

- **u/DarkJoney** (↑5, 2026-10-21 09:02): They are two different things.
  - **u/sly3x** (↑0, 2026-10-21 09:37): I mean, except interface what functionnalities would lead you to used open code ?
    - **u/DarkJoney** (↑2, 2026-10-21 11:36): I use opencode because it’s a coding agent, Unsloth is a chat, training and interference platform… Unsloth can be used as a provider in the opencode. It’s two different tools.
      - **u/sly3x** (↑1, 2026-10-21 11:37): but unsloth can act like a coding agent aswell, i mostly use it for that btw. what's the difference ?
- **u/mofu1224** (↑0, 2026-10-21 09:13): その2つは用途もできる事も全部違う  
    用途によって最適なのを選んでるだけ
  - **u/sly3x** (↑3, 2026-10-21 09:35): arigato
- **u/Angeloooo_16** (↑1, 2026-10-21 09:14): I think it comes down to flexibility and workflow. Some people just prefer having more control over their setup
- **u/Correct_Cancel_9359** (↑1, 2026-10-21 14:23): Why do you care lol. Let ppl use what fits their needs. I hear there are better hobbies than this outdoors

---

## I built a plugin that gives OpenCode access to Gmail, Calendar, Slack, GitHub, Notion, Linear and more via Composio
**u/DishRadiant1937** · 2026-10-21 08:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbhsm5/i_built_a_plugin_that_gives_opencode_access_to/)

Sup guys!! built a plugin that gives OpenCode access to your apps through Composio: Gmail, Google Calendar, Slack, GitHub, Notion, Linear and more.

Needs OpenCode 2.1+. Setup is a keyFile + one plugin entry in your config.

It's early, so feedback, issues and PRs are very welcome.

[https://github.com/jaygupta17/opencode-composio](https://github.com/jaygupta17/opencode-composio)

---

## wow, ds 4.1 just goes blah blah compared to others
**u/Deep_Imagination_811** · 2026-10-21 08:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbhp2i/wow_ds_41_just_goes_blah_blah_compared_to_others/)

I haven't used DS4.1 for a long time, dropping it because a simple yes/no question churned so many tokens of it going in loops and rabbit holes that don't matter. 

I tested it again today. Wow, Deepseek have a nice little earner there churning though tokens unnecessarily!

**Comentarios:**

- **u/Slow-Set-2856** (↑5, 2026-10-21 08:41): Ye it's overengineering things like crazy for me
- **u/CaffeinatedTech** (↑3, 2026-10-21 09:22): It works well for me.  If I want it to be more terse, I tell it.
- **u/Ribcage84** (↑5, 2026-10-21 09:59): One thing i noticed in the new 1017 update is its become way way way better at reverse engineering it probably trained on opus 5.5 for that but the results are amazing.stuff it couldnt do previously it now one shots them its very good
  - **u/EdOfO** (↑2, 2026-10-21 12:33): Do you use it with a reverse engineering MCP? I wouldn't rely on a model alone if that's something you do a lot.
    - **u/Ribcage84** (↑3, 2026-10-21 12:58): Nah i just mod emulated games no skill or mcp hes reading the code through python
      - **u/EdOfO** (↑2, 2026-10-21 13:28): Emulated?
        - **u/Ribcage84** (↑5, 2026-10-21 13:29): Yeah like a mouse cam mod for mgs 1 played through duckstation ps1 emulator
- **u/Chromiell** (↑8, 2026-10-21 10:46): It's so dirt cheap it doesn't even matter tbh. Plus you can always tell it to be brief or use a low reasoning variant if you see it overengineering solutions.
- **u/Dizzy-Truck-1780** (↑4, 2026-10-21 11:56): The price is so dirt cheap it feels like I'm stealing anyway.
- **u/No_Gold_4554** (↑0, 2026-10-21 12:06): copilot has free tier and $10 tier
    
    it automatically picks luna most of the time and it seems fine mostly
- **u/EdOfO** (↑2, 2026-10-21 12:35): Have you tried turning down the reasoning strength? More reasoning doesn't always mean smarter or better for the task. Vague instructions are also a common cause of this problem.
- **u/reybrujo** (↑2, 2026-10-21 12:55): All cached, I spent 14 hours in the last 4 days (noticed I haven't used the Go subscription so I had like 8 days to go before the month reset) and barely reach 7% of the monthly cap.
- **u/Diligent-Loss-5460** (↑1, 2026-10-21 14:19): American propaganda against DS has ramped up past two days. Guess anthropic is shitting their pants.
  - **u/Deep_Imagination_811** (↑1, 2026-10-21 14:45): not american, not propaganda, not your friend, buddy.
- **u/Acrobatic_Dark_6604** (↑2, 2026-10-21 15:04): I actually like the detail/terseness.

---

## MiniMax 3.1 is unusable in its current state
**u/Lordddddddy** · 2026-10-21 07:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbh3k8/minimax_31_is_unusable_in_its_current_state/)

https://i.redd.it/vfbv817i1swh1.png

Been getting for 2 days straight infinite loops, with massive thinking boxes even though I'm using medium or high, I never in my life got a model to 900k context and this one got to it for a simple bugfix, this is ridiculous, it's happening to someone else or is this just something related to me?

**Comentarios:**

- **u/Unusual-Customer713** (↑1, 2026-10-21 08:05): maybe just the providers problem,  like when temperature too low or its just a quantized model. i use minimax m3.1flash through mininax coding plan it works fine for me.
  - **u/Administraciones** (↑1, 2026-10-21 15:09): Working fine for me also.
- **u/Live_Raspberry_4059** (↑1, 2026-10-21 20:19): i also have infinity thinking for 1 single file

---

## Got IP banned, how to fix
**u/vinknow4O4** · 2026-10-21 07:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbh1cy/got_ip_banned_how_to_fix/)

Hi.



First of all I'd like to appreciate what OpenCode has been doing for me. It has helped me a lot - has good models for my level of work, extremely generous quotas with daily resets, etc etc. Thank you for everyone who's had a hand in making this possible.



That being said, I used a desktop client and everything was okay until the other day when I got hit with an IP ban and couldn't use it anymore on my home WiFi.



Is there a way to fix this?

https://i.redd.it/1zdx9kwj0swh1.png

I keep getting this when I try to use it from my home WiFi.

But it is working on other networks.

**Comentarios:**

- **u/xatey93152** (↑1, 2026-10-21 08:34): Wait
  - **u/vinknow4O4** (↑1, 2026-10-21 08:39): For how long?, and if you had the issue before did waiting resolve it?
- **u/joegithinji** (↑0, 2026-10-21 11:47): Use a VPN for a while. Your IP will be unbanned after some time, worked for me.
  - **u/Soifon99** (↑1, 2026-10-21 14:03): great idea, you do understand that the free stuff will go away all together if you people keep abusing the fair use, and then circumventing it via vpn.
    - **u/joegithinji** (↑1, 2026-10-21 14:08): It's not abuse really, the IP ban comes out of nowhere. But I get what you're saying.
  - **u/vinknow4O4** (↑1, 2026-10-21 15:19): Thanks, I will definitely try this
- **u/Soifon99** (↑1, 2026-10-21 14:02): Stop abusing free stuff, you will ruin it for others.
  - **u/vinknow4O4** (↑1, 2026-10-21 15:17): how do you think  I abused and how can I avoid it?
    - **u/Soifon99** (↑1, 2026-10-21 15:48): I dont know , but opencode seems to think you are abusing them.  I don't know what see as abuse. Maybe try and find it on their site.

---

## Tokless: 30-second all-in-one toolkit — Zero setup, minimal MCPs, token-efficient tools
**u/ElectricalBet3264** · 2026-10-21 07:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbh158/tokless_30second_allinone_toolkit_zero_setup/)

Hello everyone,

I believe for most users, setting up popular AI coding packages is too technical and time-consuming. There are plenty of great tools out there to make agents straight to the point, less hallucinated, and token-efficient, but configuring them properly without conflicts is the real pain point.

To fix this, I built \[\*\*Tokless\*\*\](https://github.com/HoangP8/tokless). It wires the best tools together automatically with zero configuration, where each tool serves a distinct purpose:

\* \[\*\*CodeGraph\*\*\](https://github.com/colbymchenry/codegraph): Understands how your project fits together without reading every single file.  
\* \[\*\*Context-Mode\*\*\](https://github.com/mksglu/context-mode): Reads huge files and logs in the background so your chat history stays clean.  
\* \[\*\*Project Memory\*\*\](https://github.com/riponcm/projectmem): Remembers past bugs, decisions, and fixes so you never have to explain things twice.  
\* \[\*\*Headroom\*\*\](https://github.com/headroomlabs-ai/headroom): Automatically shrinks prompts behind the scenes to save tokens and costs.  
\* \[\*\*RTK\*\*\](https://github.com/rtk-ai/rtk): Cleans up noisy terminal outputs so only the important results reach the AI.  
\* \[\*\*Caveman\*\*\](https://github.com/JuliusBrussee/caveman): Cuts out conversational fluff and pleasantries to keep AI replies concise.  
\* \[\*\*Ponytail\*\*\](https://github.com/DietrichGebert/ponytail): Stops the AI from over-engineering solutions and writing unnecessary code.

\# 30-Second Setup (Zero Manual Config)

Tokless automatically detects OpenCode (both v1 and v2) and wires everything for you:

\*\*macOS / Linux:\*\*

curl -fsSL [https://raw.githubusercontent.com/HoangP8/tokless/main/scripts/install.sh](https://raw.githubusercontent.com/HoangP8/tokless/main/scripts/install.sh) | bash

\*\*Windows (PowerShell):\*\*

irm [https://raw.githubusercontent.com/HoangP8/tokless/main/scripts/install.ps1](https://raw.githubusercontent.com/HoangP8/tokless/main/scripts/install.ps1) | iex

Tokless is 100% free and open-source. Give it a try, and I would love to hear your feedback

---

## Got IP banned, how to fix
**u/rumzkurama** · 2026-10-21 07:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbgtpt/got_ip_banned_how_to_fix/)

[removed]

---

## Upgraded to the 'Go' tier for the first time after using the free version for several months.
**u/afcreative_id** · 2026-10-21 07:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbgkh7/upgraded_to_the_go_tier_for_the_first_time_after/)

I need an analogy to understand how the "Go" tier service compares to the "Free" tier I’ve been using. Previously, in the Free tier, I relied on a set of baseline models—MiMo 2.5, Muse Spark 1.3, and DeepSeek V4.1 Flash—to support my work. I’ve just subscribed to the "Go" tier on OpenCode. Since I’ve found Muse Spark 1.3 to be the most effective among the three (ranking it first), are there any models I should switch to—or consider as alternatives—that might offer better optimization or efficiency while maintaining a comparable level of performance? Please keep in mind that this is my first experience using AI agents, so I’m still quite limited in terms of both technical knowledge and broader insight. Thank you in advance.

**Comentarios:**

- **u/Railander** (↑22, 2026-10-21 07:40): currently 4.1 flash is the best and most efficient model, it received a huge upgrade like 2 days ago.
  - **u/outofindustry** (↑3, 2026-10-21 14:26): did opencode-go deploy the 1017 version? or did they proxy the og deepseek api?
    - **u/Railander** (↑2, 2026-10-21 14:59): they're using 1017, but no information of who/what they're using to deliver it.
      - **u/No_Committee8392** (↑1, 2026-10-21 19:05): Themselves (idk what on) and they report there serving it as is, presumably meaning not a lower quantization and not molested weights
- **u/Living_Morning94** (↑8, 2026-10-21 07:45): DS put out a new build a few days ago, many Benchmark put DS 4.1 Flash build 1017 as very, very good.
    
    The difference between the free and paid tier  
    1 million tokens context window vs 200k
    
    But everyone should just do their own evals : hard to make any conclusion since your codebase, how you prompt, etc could make huge difference.
- **u/EdOfO** (↑2, 2026-10-21 13:26): ### Happy to help
    You can DM me any time. 
      
    Subscriptions are the same as free tiers except with better models available and a lot more credits to use.  
      
    *As for choosing models*  
    I don't know why most don't do this, but the best way to evaluate any model, provider, or harness is to:
    1. Make your own benchmark test suite that is relevant to your work. Have a clear rubric. If don't know how to make these tests and rubric, any model can help you develop it.
    2. Test each model individually you are interested in on it. If you don't know if their answers are good or not, then use Gemini 4 Argon (current SOTA OpenCode model) to evaluate. If only need to do a couple times, it won't use up much of your monthly credits.
    3. Decide which model(s) are best for you. Some may be better for different work. Low or no reasoning may be sufficient for some work and use very few tokens.  
      
    *Efficiency and Agents*  
    If you want to maximize the use of your $10, you can keep using the free models for the easy stuff and have the top models check their work. If a new stealth model comes out, they are usually excellent. Any model doing a specific task on its own is an 'agent'. Agentic coding is assigning them a goal to work on till completion. Traditional AI conversations are not. It's not some complicated thing.  
    But many *way overcomplicate it* with Superpowers subagents. Ignore them. I use a Planner→Orchstrator/Manager (assign and whip workers to keep on task) →Researcher→ Executor→Reviewer → Fixer workflow same as any normal software development team. Sound complicated? Often this is only a Project Lead doing most of those things (top model like Opus or Sol) and Junior Dev (cheapest best like DeepSeek Flash) doing 2 to 3.  
      
    *The best thing you can do* is have a very clear and detailed idea of what you want to do and need done. Vague instructions waste time and tokens.   
      
    Good luck!
- **u/smartfon** (↑3, 2026-10-21 14:11): No. Muse Spark and DS V4.1 Flash are currently the most efficient performers for the price. If Muse works, you should continue to use it. There are more powerful models out there that will deplete your meter disproportionately faster.

---

## GLM 5.3-flash and DeepSeek v4.1 Performance
**u/rizaldywirawan** · 2026-10-21 07:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbgian/glm_53flash_and_deepseek_v41_performance/)

How is the model performance? is it slow?

I use another local router in my country, and when i tried to use GLM-5.3-flash, the performance is pretty slow, and there are lots of timeout.

**Comentarios:**

- **u/Railander** (↑1, 2026-10-21 07:50): it has good tks, but the latency between queries is not good. the more it needs to interact with the system, the slower it'll feel.
  - **u/rizaldywirawan** (↑1, 2026-10-21 09:22): ahhh i see ... is the timeout considered awful? like it will need more than 5 attempts to continue the process?
    - **u/Railander** (↑1, 2026-10-21 14:58): it rarely fails, you just need to wait a while for back and forth work.

---

## Does OpenCode prioritize paid users over free users?
**u/Equux** · 2026-10-21 07:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbggkf/does_opencode_prioritize_paid_users_over_free/)

Ever since making all of these models free, I'm getting rate limiting issues left and right. I understand that opencode is a business, and the "free tier" is how they find their prospects, but it does feel like paid users don't get much more for paying OC money. I'm getting rate limited at every turn, and I can only imagine it's because they made so many of these models free.

**Comentarios:**

- **u/appsettings** (↑3, 2026-10-21 07:20): What is the purpose of your post? You ask question and answer it yourself.
  - **u/Equux** (↑2, 2026-10-21 07:21): im a paid user if that wasn't clear.
    - **u/appsettings** (↑-1, 2026-10-21 07:26): OP already answered your question. He said freebies is just bait to get prospect. Now if user already become paid user then there is no purpose of the "freebies" anymore
- **u/Total-Management8023** (↑6, 2026-10-21 07:24): Patrick Jane over here
  - **u/outofindustry** (↑2, 2026-10-21 11:33): Sherlock, even
- **u/Old_Restaurant_2216** (↑3, 2026-10-21 07:29): >I'm a paid user, but getting rate limited at every turn
    
    Are you talking about the free tier models or paid models?
  - **u/Equux** (↑3, 2026-10-21 07:31): The opencode Go models, are they even different than the free ones
    - **u/Old_Restaurant_2216** (↑3, 2026-10-21 07:38): Yes they are separate. Paying for Go does not change your free-tier quota. Free models also have smaller context.
        
        Personally I've never been rate-limited on paid Go models, but I use deepseek only for small parts of my workflow, so what do I know.
      - **u/Equux** (↑1, 2026-10-21 07:39): Well I appreciate a real response in this thread, thank you
- **u/Unusual-Customer713** (↑2, 2026-10-21 07:30): recently rate limit alot so i have to go to deepseek offical api. i feel like when deepseek drops a better model or checkpoint, opencode go becomes unstable, just like using free models
- **u/TripleMellowed** (↑1, 2026-10-21 07:52): Never been throttled. Your work is probably too much for OC quotas so you need to up your subscription.
  - **u/Equux** (↑1, 2026-10-21 07:54): I assure you, it's not a workload issue. I daily with Claude, opencode covers extremely minor things in the background.
- **u/surgicalcoder** (↑3, 2026-10-21 07:57): There is no paid user for free models. No token gets sent to say "This guy over here pays, prioritise him"
  - **u/Equux** (↑1, 2026-10-21 07:58): Deepseek v4.1 is an option both on opencode go and for the free tier. My question is, are they the same on the backend or different
    - **u/KxrmaJunkie** (↑1, 2026-10-21 12:32): They are now a different backend, running with a different context level on the Api end
- **u/Flashy_Disaster9556** (↑2, 2026-10-21 08:11): Paid users and free users get routed to the same provider indeed so you're right in that every time they make a model free speeds gets lower and paid users suffer. Honestly since they made DSV4.1 and GLM5.3 Flash free, the business case for their paid tier makes very little sense to me.

---

## Which inference provider does OpenCode Go use for DeepSeek, and is the model quantized?
**u/ImpossibleConcert566** · 2026-10-21 06:39 UTC · ↑5 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbftih/which_inference_provider_does_opencode_go_use_for/)

I've been comparing DeepSeek through its API with the same model through my OpenCode Go subscription, primarily for coding and agentic tasks.

In my experience, the official DeepSeek API performs noticeably better at solving coding problems reliably. The difference is significant enough that I'm wondering whether the two services use different inference setups, even when the model name is the same.

I'd like to ask the OpenCode team and anyone familiar with its inference infrastructure a few questions:

\- Which inference provider serves DeepSeek models on OpenCode Go?

\- Is the model running at full precision, or does the provider use quantization?

\- Is the underlying checkpoint identical to the one used by DeepSeek's API?

\- Are there differences in reasoning budgets, sampling parameters, context limits, or output limits?

\- Does OpenCode Go apply additional prompt processing or context compaction that could affect coding performance?

I'm not assuming that quantization is necessarily the explanation. Different inference engines, model configurations, and agent integrations could all contribute to the difference.

I'm interested in a transparent technical explanation, especially from anyone who has compared the two services on identical coding tasks.

Has anyone identified the actual inference provider behind DeepSeek on OpenCode Go, or tested whether its outputs and coding reliability differ from the official API?

**Comentarios:**

- **u/CalamityMetal** (↑29, 2026-10-21 06:42): Yeah we need transparency on this
  - **u/Natural-Cupcake6472** (↑20, 2026-10-21 07:44): "any time we offer a model it's the exact same deployment as the official lab who made it  
      the worst we do is serve at lower TPS to handle more volume  
      but it is the same model, if we chop it up we release it under a different name"
      
      [https://x.com/thdxr/status/2111849415204065611](https://x.com/thdxr/status/2111849415204065611)
- **u/GoldenX86** (↑7, 2026-10-21 06:47): I wonder which one is it, if opencode is quantizing the model or the kv cache, or if deepseek saves a better model version for themselves
- **u/Amarsir** (↑3, 2026-10-21 06:48): We don't know, and it might not even be one. They might switch and load balance between multiple.
    
    (I haven't seen this claimed about 1017 yet, but sometimes people report very low cache hit rates and that's almost certainly because of a provider reroute.)
- **u/DocumentFun9077** (↑3, 2026-10-21 07:01): OC mostly uses OrcaRouter from what I know
- **u/sukazu** (↑6, 2026-10-21 07:04): If they used the same full quality checkpoint than DeepSeek, you can be sure they would advertise it.   
    
    Either they don't, or they mix it up.
- **u/appsettings** (↑0, 2026-10-21 07:22): It's a disquise prank. If you know how to check you will understand most of their model gets redirected to cheaper one
  - **u/rizaldywirawan** (↑0, 2026-10-21 09:24): is the "cheaper one" comes from other lab? like MiMo maybe?
- **u/Old_Restaurant_2216** (↑19, 2026-10-21 07:35): As per the [owner of opencode](https://x.com/thdxr/status/2111853153826021686), all models are "factory default" - no quantization, only lower TPS
- **u/WegoW** (↑4, 2026-10-21 07:42): Unfortunately, they removed the response headers a few days ago, which allowed us to get information about their upstream providers. I was able to monitor 1,5 days. The screenshot shows the distribution between orcarouter, manhattan-project, luminal, futurixai and deepinfra.
    
    [https://imgur.com/a/kwTD0VO](https://imgur.com/a/kwTD0VO)
    
    On X they claim the following:  
    *Any time we offer a model it's the exact same deployment as the official lab who made it. the worst we do is serve at lower TPS to handle more volume, but it is the same model, if we chop it up we release it under a different name.*
    
    [https://x.com/thdxr/status/2111853153826021686?s=46](https://x.com/thdxr/status/2111853153826021686?s=46)
- **u/wwdennis5** (↑2, 2026-10-21 09:07): Are you able to provide more details of your comparison? With the known difference being tps this definitely changes how the models feels for me and can effect task completion when im not patient.
- **u/dx80x** (↑3, 2026-10-21 11:57): I doubt they'll answer this

---

## OpenCode keeps getting stuck in an infinite shell-command loop. Anyone else experiencing this?
**u/Clear_Expert_7669** · 2026-10-21 06:22 UTC · ↑2 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbfjxi/opencode_keeps_getting_stuck_in_an_infinite/)

Hey everyone, I’m using OpenCode to develop a large software project, and sometimes it gets stuck repeatedly generating or executing shell commands without making any progress.

This happens across multiple models and providers, so I’m not sure whether it’s an OpenCode bug, a tool execution issue, or something in my setup.

Has anyone experienced this? What was the root cause, and what fixed it for you?

Any help would be appreciated!

**Comentarios:**

- **u/Amarsir** (↑1, 2026-10-21 06:41): Trace back to the first command in the loop, or the last before the loop. Did a tool call fail and that's why it's trying to find something that works? I find this is the case at least a fair amount of the time. So I address it by fixing what failed or adding instructions like "if this doesn't work as expected, stop and discuss with the user instead of finding a workaround."
- **u/Hatorate90** (↑1, 2026-10-21 14:32): delete the cache

---

## Is it me or Deepseek 4.1 is super slow? Its taking an absurd amount of time for a simple task. Should I change to another model?
**u/FutureLynx_** · 2026-10-21 05:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbenld/is_it_me_or_deepseek_41_is_super_slow_its_taking/)

Big Pickler and Muse 1.3 wasn't this slow.

**Comentarios:**

- **u/Comfortable_Eye_7736** (↑21, 2026-10-21 05:31): really slow right now, and it's not about TPS, it's about the endpoint itself, the communication between server and client, that's causing the bottleneck, the TPS is fast, but the processing speed is slow.
  - **u/Railander** (↑9, 2026-10-21 05:47): basically response latency is high. every time model has to run terminal commands back and forth, it takes an eternity.
    - **u/packsolite** (↑1, 2026-10-21 19:32): Prefill is slow
- **u/AgitatedUse4032** (↑8, 2026-10-21 05:34): It is slow and burns tokens like crazy compared to Muse.
- **u/Amarsir** (↑2, 2026-10-21 05:39): It's an inherently fast model but everyone wants it. Your requests are probably waiting in line.
- **u/lundrog** (↑5, 2026-10-21 05:43): Try it on a different provider
  - **u/FutureLynx_** (↑1, 2026-10-21 06:28): what provider do you recommend?
    - **u/lundrog** (↑1, 2026-10-21 10:45): neuralwatt.com , or synthetic.new  , dm for referrals but both offer fast, high quality models.
        
        Nw even has a speed lane option. 500 + tps.
      - **u/FutureLynx_** (↑1, 2026-10-21 10:50): I think i never chose a provider. Im with the free version of opencode using deepseek 4.1... Should i experiment with that? What is the default provider?
      - **u/FutureLynx_** (↑1, 2026-10-21 10:51): Ah seems the default provider is just opencode (OpenCode Zen)
        - **u/lundrog** (↑1, 2026-10-21 10:55): Correct. You get what you pay for to a point.
            
            Depends on how large your project is and if speed and results are important.
    - **u/Dear_Contract1865** (↑1, 2026-10-21 15:24): DeepSeek V4.1 Flash 1017 from Refuseless it seems pretty fast and cheaper.
- **u/justmaybe888** (↑2, 2026-10-21 05:54): Could be server load or the model taking its time reasoning. But honestly, speed matters too, especially for simple tasks. Use whichever gives you the best overall experience.
  - **u/Popular-Factor3553** (↑1, 2026-10-21 06:21): It could be because of the demand or response latency I don't think it's because of reasoning.
- **u/Different-Monk5916** (↑4, 2026-10-21 06:00): I am using both official and opencode. 
    
    If you are not concerned about the costs - which is pennies compared to ChatGPT or Claude on actual task completion, go for deepseek. There may not be any other well-rounded service.
    
    Opencode is fine, if the speed is not critical and wants to keep cost low via subs.
- **u/Anaeijon** (↑5, 2026-10-21 06:14): Not only that. I've also found, that it's output is terrible.
    
    It constantly does things I didn't ask it to do.
    It doesn't ask back for clarification.
    It overcomplicates things a lot.
  - **u/Huge_Business2428** (↑2, 2026-10-21 07:35): This is an issue that I've also experienced recently. I will give it the most straight forward prompt possible, even telling it explicitly not to do anything other than I say, and regardless it just goes ahead and makes up its own tasks, starts working on old tasks I gave it etc. Very annoying.
- **u/Callinectes-Lucidus** (↑2, 2026-10-21 06:33): Try to lower the reasoning effort to medium.
- **u/elonelon** (↑2, 2026-10-21 07:14): my free deepkseek get : "Upstream request failed: Endpoint is unavailable."
- **u/43848987815** (↑1, 2026-10-21 07:29): It’s been incredibly slow for me for the past 48hrs. On opencode go sub, I’ve stopped using it.
- **u/No_Structure1800** (↑1, 2026-10-21 08:27): Honestly, at this point I would prefer getting $40 usage for double the speed, than $80 at this speed. I only use opencode for Deepseek 4.1, and it's been getting slower and slower - now it's close to unusable. Wondering if it's worth the delays that it's causing me. I'm considering cancelling opencode go and moving to deepseek api.
  - **u/Zealousideal_Aide787** (↑1, 2026-10-21 09:19): Yea, this. What the point of having 80$ usage if the model is too slow to possibly use this limitation.
- **u/for4f** (↑1, 2026-10-21 08:36): yeah same here the last day or two, feels like endpoint load more than the model itself. ive been splitting it so claude does the planning and deepseek does the grunt work, way less painful when its slow lol
- **u/Leading_Yogurt7025** (↑1, 2026-10-21 10:43): No it's fine
- **u/Ok-Drawer5245** (↑0, 2026-10-21 12:40): It’s slow because the servers are overloaded i think (also speed varies over the time of day). Having said that, it is miles ahead in quality compared to glm 5.3 and the previous deepseek flash version. Im getting some REALLY incredible visual/graphical work out of it
    
    Honestly I don’t mind the speed that much the quality of the output I’m getting is fantastic. I don’t sit at my computer and wait for it anyways. Often I’m not even home and just talk to it over iMessage with Hermes
  - **u/FutureLynx_** (↑1, 2026-10-21 21:06): Awesome, thats what i need. And how do you see the results? Do you just make a list of prompts before you leave the house and just communicate it in order, or you have a way to see the results by sharing screen or something?
- **u/YoRt3m** (↑2, 2026-10-21 14:09): Yes, it's slow for me too. used to be much faster in the past.
- **u/BatNo7925** (↑1, 2026-10-21 14:42): Because it's not DeepSeek v4.1 but CheepSeek v4.1.
- **u/RainyDayFeel** (↑1, 2026-10-21 16:52): My OpenCode subscription ended today, so I signed up for the DeepSeek API. It was very fast (200 tok/s) with DeepSeek harness and maxed out. I think I will just go with that from now on because I've been getting errors constantly on OpenCode.
- **u/warpaint_james** (↑1, 2026-10-21 17:33): I had lots of stalls yesterday on it. Im considering putting $40 a month into OpenRouter instead because the availability is never compromised. The speed average is 269tok/s too. I dont think Ive ever seen OpenCode serve it that fast.
    
    Has anyone else done the math on this? Looking briefly, if you maxed out the "$160" of credit (peak, btw) on OpenCode just on v4.1, the same thing would cost you $39.41 on OpenRouter at the average price...
    
    Also, OpenRouter lets you pick a provider by lowest price. So you might be getting a quantized model, but the price can be up to 1/3 of the cost.

---

## Is buy opencode go is more worth it than buy api from official website?
**u/Professional_Day4470** · 2026-10-21 05:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbeidn/is_buy_opencode_go_is_more_worth_it_than_buy_api/)

hello everyone, im new to open code and curious about this, should i buy the api from the official or just buy opencode go? Im gonna using deepseek flash for my main

**Comentarios:**

- **u/rakotomandimby** (↑1, 2026-10-21 05:26): Opencode re-sell to you: they buy from upstream and re-sell to you. That is enough to make conclusion.
  - **u/YoRt3m** (↑1, 2026-10-21 05:34): But they resell to you a different product with less quality and more quantity so there's that to consider
- **u/mabuonomo** (↑1, 2026-10-21 05:29): Quando offrono api in promozione vincono loro
- **u/_janc_** (↑2, 2026-10-21 05:31): Quantized?
  - **u/CaffeinatedTech** (↑2, 2026-10-21 12:53): The base model is already FP8, but yeah, we have no way of knowing if the providers are running quantised versions.
- **u/Specialist-Leek-357** (↑3, 2026-10-21 05:37): the free tier is so generous, you should try it to do something and see if it's good enough.
    
    personally, it's the best AI agent i've use so far
  - **u/Professional_Day4470** (↑1, 2026-10-21 05:44): I've used it, the official and free from opencode, all good. but if the open code go worth more than $10 from official ill go for it
    - **u/Specialist-Leek-357** (↑4, 2026-10-21 05:46): opencode go $10 worth around $80 of deepseek official... at least that's what gemini told me.
      - **u/Professional_Day4470** (↑1, 2026-10-21 05:47): Okay thanks
- **u/Amarsir** (↑27, 2026-10-21 05:38): It's a buffet.
    
    You can eat more than your money's worth. ($80 for $10). If your tastes change you can switch instantly. But you'll be bumping elbows with crowds and occasionally wondering if the quality is as good as the same items purchased *a la carte*.
  - **u/Professional_Day4470** (↑5, 2026-10-21 05:44): Really? That's the reason im asking this
  - **u/IAmFitzRoy** (↑2, 2026-10-21 15:36): Tip: When the crab legs hit the floor, the crowds will leave alone the desserts for 5 minutes. That’s your chance.
  - **u/habibexpress** (↑1, 2026-10-21 20:27): Damn this is the best analogy
- **u/Tommaso_Ceoldo** (↑9, 2026-10-21 05:47): If you need quantity rather than quality, it's better
  - **u/Professional_Day4470** (↑1, 2026-10-21 05:47): Okay thanks
- **u/xatey93152** (↑1, 2026-10-21 06:13): They sell you different model. If you know how to test. It's open secret
  - **u/Professional_Day4470** (↑1, 2026-10-21 06:17): I see...
  - **u/squirrelscrush** (↑1, 2026-10-21 17:38): Source?
- **u/Slow-Set-2856** (↑2, 2026-10-21 06:23): I'm burning my opencode go limits like crazy lately but i guess still better than api (i only use flash models btw)
  - **u/Professional_Day4470** (↑2, 2026-10-21 06:25): Brah, thankss for ur information, i think imma try next month
- **u/cleversmoke** (↑3, 2026-10-21 08:01): When OpenCode Go was $60 usage for DeepSeek V4.1 Flash, I used 5 billion tokens per month. At $80 usage, it'll likely be around 7 billion tokens. 95% cache hit.
  - **u/cagycee** (↑1, 2026-10-21 13:42): Not to mention now that DeepSeek is also free now too (200k tokens) per session
- **u/Chromiell** (↑1, 2026-10-21 10:57): I use Opencode Go 10$ sub for my personal projects and I have Claude 20$ Teams subscription at work. I still do a lot of things manually but for my use case I think that for personal small to medium sized projects Opencode Go is the best value, you have access to a ton of models with various usage quotas: some are smarter, some are more useful for "manual labour" and some are extremely capable but quite costly (looking at Kimi K3 and Argon).
    
    DS 4.1 Flash is a great all rounder imo, it does all tasks relatively well and is as cheap as dirt, you'll never run out of usage when using DS 4.1 Flash. In my experience it's vastly superior to Luna.
    
    Comparing Opencode Go 10$ to what is basically Claude Pro 20$ I'd say Claude definitely has the better models, but unless you do extremely complex tasks they're not needed. Opus and Sonnet are great and you also get a ton of usage with Claude Pro (I usually end the week with just 10% of my quota spent) but you'll be paying double the price. It's up to you to choose the subscription that better fits your needs.
  - **u/squirrelscrush** (↑1, 2026-10-21 17:34): OpenCode Go + Claude Pro is the best combo tbh, you can make the Go to do the implementation work while Claude can do the planning, design, review.
  - **u/l0rd_raiden** (↑1, 2026-10-21 18:58): How do you use Claude? For coding tasks?
      
      I tried chatgpt go, I know is not comparable and I can bun the account with 3 prompts while coding
    - **u/Chromiell** (↑1, 2026-10-21 19:19): Yeah, at work we use Claude to work on the project, I personally use Claude Code and I'm by no means an expert, I still mostly prefer to code by hand but I use Claude to take care of boring or very time consuming tasks.
        
        GPT Go I think only allows you to use Luna which is a very unreliable model in my experience, I tried it when we still were using Copilot and it was very underwhelming, I pretty much only felt ok using it for writing documentation and nothing more. I briefly tried Terra when it first came out but it felt like a poor man's Claude Sonnet, and I've never tried Sol since it was priced stupidly high. At work right now I mostly use Sonnet (90% of the times) with Opus for very complex tasks and Haiku for documentation writing and implementing the test suite.
        
        At home, in my free time, I only use Opencode for the personal projects I have on GitHub: 90% of the times I use Deepseek v4.1 Flash and for complex tasks I have a custom setup with oh-my-opencode-slim (which I have on GitHub among my dotfiles already configured), it's mostly a mix of Deepseek models with Kimi, it works really well even for very complex tasks, it just takes a while since it a lot slower compared to Claude, but for 10$ a month I can certainly afford to wait.
- **u/GGsayan** (↑1, 2026-10-21 12:13): I'd personally recommend getting OpenCode Go instead. You can switch between different models depending on what you need, and it's more cost-effective than buying API credits separately.
    
    Since you're planning to use DeepSeek as your main model, Go is worth considering. For just $10, you get access to multiple models, and the DeepSeek V4.1 Flash usage you get through the subscription could be worth around $80 compared to paying for equivalent API usage directly.
    
    I'd go with Go, especially if you want the flexibility to try different models without constantly worrying about API costs.
- **u/Ameldur93** (↑1, 2026-10-21 12:53): Coming from Cursor Pro plan which used to least me whole month meanwhile opencode go lasted me 1 day full on deepseek 4.1 flash and 50% monthly usage used now i have to wait whole week for reset to use another day fully 50% so not worth
- **u/MrBeverly** (↑1, 2026-10-21 13:23): Another part of it is if you have your agents configured correctly you assign grunt work to models other than your primary, like for example leaving git management to a lightweight flash model and letting a more capable model handle the research and structural design. All of your usage is accounted for separately for each model so that way you don't waste your usage on the better stuff doing simple operations.
- **u/Minimum-Avocado-8015** (↑1, 2026-10-21 14:18): Go with Go. Pun not intended. But you will still face over-capacity problem sometimes where the Open Code app will have to retry few times. Small nuance for going cheap. DeepSeek4.1 flash is really good. Hop on faster mate!
- **u/squirrelscrush** (↑1, 2026-10-21 17:38): In my experience, the quality of output is similar to direct API (I was a DeepSeek API user before). Just that it's slower than API since the same hardware serves more users, but if you allow paid endpoints to train on prompts in the settings then it's not *that* slow.
    
    If your API usage will cross $10/month then it's worth it. I use DeepSeek V4.1 Flash and Muse Spark 1.3 Contributor on Go, and they're practically unlimited. DeepSeek does all the work, Muse verifies the DeepSeek work.
- **u/dellweb** (↑1, 2026-10-21 17:39): Well, I tested DeepSeek in opencode and through oficial API and what I noticed different was the tok/s with through the API is much faster compared to opencode. But overall quality is kind the same and o get more usage through Opencode then the API. So for me Opencode is better aiming the cost/usage you get.

---

## Do i download the CLI or desktop app
**u/AnOrdinaryCrayon725** · 2026-10-21 05:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbeat7/do_i_download_the_cli_or_desktop_app/)

I’m not sure what to use both look very good

**Comentarios:**

- **u/Sea-Dimension-1097** (↑1, 2026-10-21 05:12): Both are mostly the same, both can be used with a mouse as well, but the app has easier diff view, file tree, and commenting on specific files.
- **u/roomjosh** (↑2, 2026-10-21 05:14): OpenChamber is the best desktop ui, it will install the cli
- **u/Mr_Lucas2000** (↑1, 2026-10-21 05:17): Not sure about you but I like the v1 gui, cli quite nice too
- **u/lordcohliani** (↑1, 2026-10-21 05:48): The desktop app is horrendous. The CLI is okay. I use OpenChamber
- **u/Technocratix902** (↑1, 2026-10-21 05:50): Cli only. Use t3code with. Try

---

## OpenCode v2.1.2 dropped: No more wiped prompts on rate limits, hiding free models, and location timeout controls
**u/sltechpro** · 2026-10-21 04:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbdkiy/opencode_v212_dropped_no_more_wiped_prompts_on/)

OpenCode pushed v2.1.2 today. It's a quick minor bump, but it cleans up a few irritating terminal/desktop quirks.

The main practical takeaways:

1. Free limit handling actually works properly now. When you burn through your free message quota, Desktop and the TUI don't just vomit a generic failure anymore. They display the actual reset timer, keep your drafted prompt intact in the composer instead of wiping it, and provide inline `/connect` or `/models` actions to switch things up immediately.
2. You can hide free models completely. If you only want paid/private endpoints across defaults and fallbacks (or want to keep junior devs from accidentally routing to rate-limited free tiers), throw `OPENCODE_DISABLE_FREE_MODELS=1` into your environment to purge zero-cost models from OpenCode and Go catalogs.
3. Idle location services are configurable. Instead of dangling indefinitely, you can set `experimental.location_idle_timeout` (e.g. `"4 hours"` or `false`) to control when inactive workspaces/services spin down. They also fixed the bug that killed locations while long tool calls or background tasks were still running.
4. Clean installer setup and async writes. Fresh curl installs now create missing `~/.zshrc` or [`config.fish`](http://config.fish) files automatically and export to `PATH` cleanly. Also patched a nasty race in Code Mode where async jobs were interleaving mid-statement and dropping writes during concurrent runs.

Official references:

* [https://opencode.ai/changelog](https://opencode.ai/changelog)

**Comentarios:**

- **u/TheMythicSorcerer** (↑14, 2026-10-21 04:41): Cool. I had a really funny experience with it about 20 minutes ago I open opencode to type in a task it says "/upgrade for v2.1.1" I do that. I open it again it says "/upgrade for v2.1.2". 
    
    But the features are nice especially being able to see free usage reset timer.
  - **u/Amarsir** (↑8, 2026-10-21 04:47): I pretty much just wrote the exact same experience myself.
    - **u/TheMythicSorcerer** (↑5, 2026-10-21 04:49): Haha! I mean they both came out within these 2 days and if you didnt update yesterday then when you start working in the afternoon this comes out so its probably a likely occurence.
  - **u/Final_Bodybuilder490** (↑1, 2026-10-21 12:18): being able to see free usage reset timer.  
      //Agree on this cause before or maybe Im not aware, if I will be using free model, Im clueless if how much token/usage I left and when I can use it again.
- **u/Amarsir** (↑5, 2026-10-21 04:47): I got tired of seeing the reminder for 2.1.1. So I said "Argh, fine" and upgraded. Only to log in and instantly see a notice for 2.1.2. 😅
- **u/DEAD1nsane** (↑2, 2026-10-21 08:01): my https://github.com/DEAD1nsane/opencode2-termux-musl has a auto-update script and a check-update 
    
    ## Updating
    
    Updates are unattended: enable the periodic job once (Android fires it roughly every 6h — not at a fixed hour) and forget it.
    
    ```sh
    termux-job-scheduler --job-id 7802 --period-ms 21600000 \
      --network any --persisted true \
      -s "$HOME/GitHub/opencode2-termux-musl/scripts/auto-update.sh"
    ```
    
    The job (needs the Termux:API app — any network, survives reboot) checks the npm channel and re-runs `install.sh` only when behind; it never downgrades. You get a notification on success or failure (failures name the stuck version and retry automatically on the next run — nothing to do manually). Runs are logged to `~/.opencode-auto-update.log`, and the last outcome is always in `~/.opencode-update-status` (`./scripts/check-update.sh --status` shows status + job state + recent log).
    
    Rollback boundary: every update stages the new binary to `opencode-v2-musl.bin.new`, smoke-tests it there (`--version` must match the pinned release, `run --help` must exit 0), and only then promotes it — the previous binary is kept as `opencode-v2-musl.bin.last-good` with `VERSION`/`SHA256` sidecars. A bad upstream build therefore never overwrites your only working copy. The tarball SHA256 is logged and recorded each install, and enforced when `OPENCODE_EXPECTED_SHA256` is set. If you ever need to go back by hand:
    
    ```sh
    ./scripts/check-update.sh --rollback   # restore last-known-good binary
    ```
    
    so hardly do I ever see the /upgrade message inside the TUI, but If I do, I just jump into my repository, goto scripts, and ./auto-update.sh
- **u/alphaQ314** (↑1, 2026-10-21 10:37): What are the rate limits on the free Ds flash 1017
- **u/MrBeverly** (↑0, 2026-10-21 12:57): I swear they update this thing twice a day
- **u/Testaccount105** (↑1, 2026-10-21 15:06): can i see the limits in the web console?
- **u/Astral65** (↑1, 2026-10-21 16:01): I only see 1.19.3 version on github

---

## How small can you make an OpenCode agent failure and still reproduce it?
**u/Charlietest123** · 2026-10-21 04:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbdg0q/how_small_can_you_make_an_opencode_agent_failure/)

---

## Day 10! of Daily morph
**u/2tacchi** · 2026-10-21 03:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbd2dk/day_10_of_daily_morph/)

Hi again, its the 10th day of this little experiment. I made a [website ](https://dailymorph.app/)that

Bases its contents completely on the top comment of this reddit thread.

Everyday the comment gets put into an open code agent that than updates the website.

It runs on an isolated VPS with an persistent Opencode agent session so all past prompts and inputs are remembered.

I kept my involvement minimal with an add on prompt saying do not ask follow up questions but other than that nothing to restrict it!

I made a archive and context page so you can see past versions of the site and the context and builds the LLM went through in the past.

The LLM used is DeepSeek V4.1 Flash 1017

Yesterday was unfortunately a quiet day so the there were no new builds, please comment ideas to see it come to life tommorow!

**Comentarios:**

- **u/Mr_Lucas2000** (↑2, 2026-10-21 11:04): Hm make a realistically accurate prism meow
- **u/AccessIndependent795** (↑1, 2026-10-21 13:17): Make the site a porn site
- **u/cornelha** (↑1, 2026-10-21 14:14): You might want some better curation here, the shit that is being posted is crazy
  - **u/AccessIndependent795** (↑1, 2026-10-21 16:52): Im not even sure what this site is

---

## Is Deepseek 4.1 flash 1017 better than glm 5.3 flash?
**u/Upset_Disaster_1427** · 2026-10-21 02:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbbfkn/is_deepseek_41_flash_1017_better_than_glm_53_flash/)

**Comentarios:**

- **u/Previous-Fun4493** (↑36, 2026-10-21 02:36): hmmm... may....maybe... lets me think.. hmmnn... hm... maybe
  - **u/YogurtExternal7923** (↑8, 2026-10-21 03:05): Low blow 😂
  - **u/will_sm** (↑5, 2026-10-21 04:12): need think. Need to provide answer.
      
      I've only looked at it's low thinking which isn't that bad
  - **u/elonelon** (↑1, 2026-10-21 07:16): Big Pickle : what ? nah..you ask it, i gave the result, think later.
- **u/Least_Bodybuilder216** (↑9, 2026-10-21 02:36): yes, but in hallucination, not
- **u/wpdavid** (↑2, 2026-10-21 03:09): These are both really good models. Neither is as good as Opus 5.5. I am trying out 1017 this week and it is mostly doing good, reliable work, but also getting stuck on things I think Opus could figure out.
  - **u/Sufficient_Spite_349** (↑5, 2026-10-21 03:48): Nothing comes close to the frontier the gap has to be reduced by Harness and plugins
    - **u/amethyst_mine** (↑-1, 2026-10-21 05:20): deepseek has been better than 6.1 sol for me ☠️ less idiotic descisions
- **u/lordcohliani** (↑8, 2026-10-21 04:42): Yes no contest
- **u/AGIMaster911** (↑4, 2026-10-21 05:05): Sure way better
- **u/Ok-Drawer5245** (↑2, 2026-10-21 12:54): For me it is way better, its graphical / visual output is MILES ahead of glm 5.3 flash
- **u/horrbort** (↑2, 2026-10-21 13:19): Hmmm hmmm hmmmm hmmm you asked a question hmmm hmmm hmmm hmmm hmm I should answer hmmmm hmmmm…
- **u/EdOfO** (↑1, 2026-10-21 13:31): Make your own benchmark tests relevant to what you want to do and see yourself!
- **u/BatNo7925** (↑-1, 2026-10-21 14:11): Without a doubt, it’s made for getting things done quickly—its intelligence and speed have reached my fastest working pace.
- **u/Strong-Strike2001** (↑1, 2026-10-21 16:35): Hmmm hmmm hmmmm hmmm you asked a question hmmm hmmm hmmm hmmm hmm I should answer hmmmm hmmmm…
- **u/the_foreigner63** (↑1, 2026-10-21 19:35): Deepseek has always been a gamechanger. It might be worse than opus but if you have opencode go then its around unlimited to use. You can use opus to plan and validate results, ds4 flash will cover all other tasks
- **u/Iron-Over** (↑1, 2026-10-21 20:00): For code review of Python. In my tests, DeepSeek outperformed GLM Flash.  Both used MiaLabs recipes for 2 sparks.  
    
    
    This was across 3 runs reviewing code for planted bugs: Astra scored 9/9, Deepseek 1017 8/9, Opus 5.5 6/9, GLM API 4/9, Mimo 2.6 Flash 3/9, Qwen Flash Next 3.8 2/9, GLM 5.3 FLASH 1/9, Sonnet 5.5 0/9. 
    
    These are bugs I found in my code previously, and I need a good reviewer to catch them in the future.
  - **u/Miserable-Dare5090** (↑1, 2026-10-21 21:10): 2 sparks? for 4.1Flash?
    - **u/Iron-Over** (↑1, 2026-10-21 21:10): [https://github.com/MiaAI-Lab/DeepSeek-v4.1-Flash-1017-2x-DGX-Sparks](https://github.com/MiaAI-Lab/DeepSeek-v4.1-Flash-1017-2x-DGX-Sparks)
        
        [https://www.reddit.com/r/DGX\_Spark/s/CyoekOnTzQ](https://www.reddit.com/r/DGX_Spark/s/CyoekOnTzQ)
        
        It is nearly as good as api
- **u/Upset_Disaster_1427** (↑1, 2026-10-21 02:41): Do u know if it's also the case for 3d modeling and animating?
  - **u/LinsaFTW** (↑1, 2026-10-21 02:42): You are best off using opus friend
    - **u/Upset_Disaster_1427** (↑3, 2026-10-21 02:44): A little out of my budget lol, I'm considering it in the future tho, thank you!
      - **u/LinsaFTW** (↑2, 2026-10-21 04:00): The Claude sub is pretty cheap imo compared to what you get
  - **u/RasonYang** (↑2, 2026-10-21 03:39): No clue, man—I haven’t really touched 3D modeling or animation. I’m mostly doing Go, TypeScript, real-time voice, and AI call centers
  - **u/Amarsir** (↑2, 2026-10-21 04:27): It's more subjective than a full benchmark. But this youtuber runs the same prompts on new models and skews heavily toward 3d.
      
      [https://youtu.be/dk1OY5z08\_Y?is=xlBLmm\_w7dPWUDfw](https://youtu.be/dk1OY5z08_Y?is=xlBLmm_w7dPWUDfw)
      
      That video shows him being pretty happy with the new DS 1017. You can jump around some of his other videos for comparison.

---

## is there way deal with doom loops?
**u/qustrolabe** · 2026-10-21 02:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbb5f1/is_there_way_deal_with_doom_loops/)

https://i.redd.it/pztzd8zpcqwh1.png

also is there way to collapse thinking traces without scrolling all the way app, it's so annoying

**Comentarios:**

- **u/cornelha** (↑2, 2026-10-21 04:23): Choose another model and start over. Not all models are the same and if you are using git, the models can at least pick up what was changed if you tell it what you were busy with.
- **u/ichisay** (↑-1, 2026-10-21 11:20): Lo de ocultar razonamiento lo tienes en las opciones

---

## Came back to opencode. Was 🙂 now 🙁
**u/Melodic-Mud-1116** · 2026-10-21 02:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbauzx/came_back_to_opencode_was_now/)

In the latest updated I don't know if it's. Me or what but I have been noticing it's running shell commands way too much and also the performance kind of seems bad is it only me or what. And any tips on it.

**Comentarios:**

- **u/theotherartist_** (↑2, 2026-10-21 02:11): Try giving it the exact files to inspect, the expected outcome, and a clear stoping point. Otherwise , agents can get stuck in a loop of checking everything before doing anything.
  - **u/Melodic-Mud-1116** (↑1, 2026-10-21 03:19): Others agents I tried weren't this bad is it the free models only or what. And about the go plan are the models the full versions or lower performance ones.
    - **u/mondroyink** (↑1, 2026-10-21 07:29): What other agents are you comparing to?
      - **u/Melodic-Mud-1116** (↑1, 2026-10-21 07:47): Lately I was on zcode free and before that on cline and kilo code. Also was using open code too and I was good it's just now.
- **u/PanPanForReal** (↑1, 2026-10-21 05:25): Try changing to smarter models
  - **u/Melodic-Mud-1116** (↑1, 2026-10-21 05:49): On DeepSeek.
      And it's wasn't like this before.

---

## Need advice on which models should i use
**u/syakirx17** · 2026-10-21 02:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbatv1/need_advice_on_which_models_should_i_use/)

Hi guys, i'm new to open code, just subscribed to Go plan a few days ago.

i'm using it for   
\- moderate coding  
\- video editing (with a customized hyperframes skill, which originally built for claude)

so far, i have been using Muse Spark 1.3, which is ok for basic editing, but the generated ui animation effect is basic. i also try Deepseek 4.1 flash max, but it feel like its so slow (?)

from what i have seen how people edit video with AI, the best model for this use case is actually claude Opus 5.5. but i cant afford that, so i'm looking for alternative model in open code that close to it, but not really expensive on usage cost

i'm curious if anyone here also have the same video editing workflow.

thanks

**Comentarios:**

- **u/cheddarstatic** (↑1, 2026-10-21 02:08): I’d test two or three models on the exact same short animation task and compare the result, time, and quota used. Video workflows can vary a lot, so a small benchmark beats paying for a model based on hype.
  - **u/syakirx17** (↑1, 2026-10-21 02:11): thanks for the advice
- **u/lacroix05** (↑1, 2026-10-21 02:22): unfortunately for 3d work, there is no cheap model anywhere near claude 5.5 or gpt 6.1 right now. i always look at peoples benchmarks on x when a new model comes out, and somehow people on x mostly benchmark 3d stuff like creating models for rockets, houses, horses, etc.
    
    ds 1017 has some promise, but as you found, the generation result is slow. i saw some benchmarks where claude opus finished in 1 minute and deepseek took almost 5 minutes. so yeah, your waiting time will increase by 400-500% longer.
    
    if you really cannot afford claude but want similar results, ds 1017 is your only choice right now. though you need to wait more and probably make the prompt more detailed because in the end it is still ds and not claude.
  - **u/pikuray** (↑1, 2026-10-21 02:44): Hi. What are your thoughts on spark 3 contributor?
    - **u/Amarsir** (↑1, 2026-10-21 04:45): In general or for 3d work?
        
        Up through last week, I've been saying DS flash, GLM flash, Qwen Flash, Mimo Flash, Muse Spark contributor, Space Bunny (Minimax), Luna, and Haiku are all generally pretty comparable. Muse, Haiku, and Minimax being a little better at visual, Deepseek, Luna, and Mimo being a little better at code, GLM and Muse being better at language, Qwen and Mimo better at organizing. IMHO.
        
        Deepseek 4.1 1017 seems a genuine step above. If you loved one the other 7 it wouldn't be wrong to keep using it. And many people really like Muse. (Myself included, for the stuff I mentioned.) But if you're coming for a reco, I don't see anything that 1017 is weak enough in for me to not recommend it.
  - **u/syakirx17** (↑2, 2026-10-21 04:28): thanks, i'll just use ds 1017 now by running it in the background
    - **u/Amarsir** (↑1, 2026-10-21 04:38): You've probably got the best 2. If you want to experiment a little more, give Haiku, Mimo 2.6 Pro, and Minimax M3.1 a shot.  And sometimes if you have them rotate and improve each other's work you can get good results through combination. But of course that's slower and more tokens.
        
        There's a chance Argon would do well. But it's so expensive I'd suggest only pulling it out if there's a specific task that you're getting frustrated because other models fail.

---

## Cursor to OpenCode Advice
**u/Prudent-Promotion512** · 2026-10-21 00:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xb8mlo/cursor_to_opencode_advice/)

I just switched to OpenCode from Cursor and I have been impressed by many aspect of it and very excited to be free of the Cursor cache token tax but I have found my agents are using way more tokens in general.   

I think Cursor’s internal harness was helping to make my guidance more efficient but I can’t quite figure it out.  

Qualitatively the agents in OpenCode follow their guidance much more closely which I wanted but they are not as pragmatic and get bogged down in minor details more.

Anyone else experience this or have advice?

**Comentarios:**

- **u/oliviadventure** (↑1, 2026-10-21 00:52): I’d add explicit stopping criteria to your instructions. Something like “make the smallest change that satisfies the requirements, don’t refactor unrelated code” can prevent a lot of unnecessary work.
  - **u/Prudent-Promotion512** (↑1, 2026-10-21 15:14): Thanks - yes I think simple stuff like that is a great idea
- **u/Amarsir** (↑1, 2026-10-21 04:31): I haven't tried, but ask an agent to examine Cursor and pull out the built-in instructions so you can replicate what you like?
  - **u/Prudent-Promotion512** (↑1, 2026-10-21 15:14): I did a bit of this - feel like Cursor is smart enough to protect their IP and it didn’t give anything revolutionary out.

---
