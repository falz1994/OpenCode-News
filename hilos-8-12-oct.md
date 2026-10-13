# r/opencode — hilos 2026-10-08 → 2026-10-13
_Generado: 2026-10-12T01:33:12.796789+00:00 · 145 hilos · 1067 comentarios · fuente: Arctic Shift_

## Best 10$ plan?
**u/GoonigUnc** · 2026-10-12 01:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3ovwy/best_10_plan/)

https://preview.redd.it/v79u27vzrxuh1.png?width=540&format=png&auto=webp&s=55474aea6bfab83c7c3fe9ff8350e93176a50929

found this while digging for good opencode alternatives. it kinda looked sus to me so i first tried the free plan where they give 500k token per day and 1m with telegram verify. for the free tier they got le chonk (mistral large 4) and qwen 3.8 max and many more good models. the speed was actually really good and i was thinking of buying the 5$ plan for testing

https://preview.redd.it/1z49jc1tsxuh1.png?width=530&format=png&auto=webp&s=5f88a265b22a21b9129ba4b12232dd04511af964

it says 30x of what you pay which seems too good to be true but if you take a good look at it, it says 5$ every 5 hour which doesnt get you much if you use models like opus or kimi or even 6.1 sol so its better to use ds4.1 flash which is probably why they can afford to keep the number high but the usage low for all user. 

also the free tokens means tokens on the free models. ones that you can also use in the free tier. and they also have 20$. 100 and 200$ plan working same as the 5 and 10$ plan but with higher usage limits. 

its called xkiro btw, if it helped and you wanna try it out id appreciate if you use my [referral link](https://xkiro.com/ref/EWEQHKJ) ;D

---

## Opencode keeps stalling
**u/ImpossibleBother5133** · 2026-10-12 01:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3ou8t/opencode_keeps_stalling/)

Hello, I am new to the local ollama/llm runs, so pardon my ignorance, but would love to get help to get unblocked...

Windows + rtx 5090 + ollama + qwen3.8:27b

  
I start default: ollama -> opencode -> qwen3.8.27b

  
it starts well, runs for few mins... but then stops and not making much progress.

https://preview.redd.it/a7wpi4hbtxuh1.png?width=2068&format=png&auto=webp&s=17759067b90981c2a4a538c8883434a55f013870

https://preview.redd.it/bxl40u6ftxuh1.png?width=847&format=png&auto=webp&s=b0ce9fe12ffcbe220ee031dc513846cf83715495

---

## Opencode desktop never asks permission to read/write all over the users drive.
**u/ccss2** · 2026-10-12 01:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3oro6/opencode_desktop_never_asks_permission_to/)

Is this normal behavior? I'm new to opencode, but after running some tests, I've confirmed it (Windows version).  I assumed that outside of the project directory that it would ask. 

Here is the summery that session created.

`On OpenCode 2.0.26 (Windows, desktop app), the external_directory permission check never fires: read and write calls on paths outside the session's Location succeed silently — I reproduced it reading files and creating a file on both the same drive and a different drive, with no approval prompt, no pending request in the API, and no saved, session-level, or config allow rules anywhere that could explain it. Other checks in the same pipeline work normally during the same session — a read of .env correctly raised an ask prompt and a configured deny rule was enforced — so this appears to be a fail-open bug in the external-directory boundary check rather than a configuration issue. The impact is that agents can currently read and modify files anywhere on disk, contradicting the documented default policy (external_directory → ask for every agent).`

---

## Is there a difference between MiMo-V2.6-Flash-free and MiMo-V2.6-Flash ?
**u/Takeoded** · 2026-10-11 23:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3mn7w/is_there_a_difference_between_mimov26flashfree/)

There is both a free-tier `MiMo-V2.6-Flash-free` and OpenCode Go `MiMo-V2.6-Flash` model, are they the same? or is the free model like lower quantization or slower or something?

**Comentarios:**

- **u/AdFun4897** (↑1, 2026-10-11 23:32): They are the same
  - **u/Takeoded** (↑1, 2026-10-11 23:45): at least free version have a 200K context window, full version have 1M context window 🤔
    - **u/TheMythicSorcerer** (↑1, 2026-10-11 23:52): 1m context costs more to run
      - **u/Takeoded** (↑5, 2026-10-11 23:56): You're not wrong, but also water is wet
        - **u/TheMythicSorcerer** (↑1, 2026-10-11 23:58): No I'm saying it's the exact same model probably even run on same harware but full version has priority in queue, and more features that cost money like context, output token limit, and extra inputs. It makes sense to do that as a business.
        - **u/AnimusAstralis** (↑1, 2026-10-12 00:28): Or is it?
            
            (I miss Vsauce videos)
- **u/Takeoded** (↑8, 2026-10-11 23:36): Free version: 
    - Context window 200,000
    - Max tokens: 32K tokens
    
    Full version: 
    - Context Window 1M tokens
    - Max Output: 128K tokens
    
    I don't know if there are other differences
    
    references [1](https://pi.dev/models/opencode/mimo-v2-6-flash-free) [2](https://mimo.mi.com/models/en-US/mimo-v2.6-flash)
  - **u/Global-Eye-7326** (↑3, 2026-10-12 00:11): Yeah I stopped using Big Pickle after it hallucinated a hamburger menu in Vietnamese on me in a vibe coding session.

---

## Migrated to opencode v2, agents get killed mid-task after ~1 hour
**u/sypcio25** · 2026-10-11 22:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3l5rp/migrated_to_opencode_v2_agents_get_killed_midtask/)

I recently migrated to opencode v2 and long-running sessions now get stopped mid-task, roughly an hour after they start working. The agent isn't idle. It's in the middle of a long subagent call or tool run when the turn ends with Step interrupted, and the service log shows location services evicted at the same second.

Is anyone else seeing this? Did you find a workaround, or a build where it's fixed?  
Not sure if the issue is on my end or it's still due to v2 being in beta.

**Comentarios:**

- **u/Robonotes1760** (↑1, 2026-10-11 22:20): Are you sure that it's interrupted not just running in the background? Background running is a new feature in OpenCode 2.
  - **u/sypcio25** (↑1, 2026-10-11 23:37): It was interrupted, happened to a couple of long running sessions, with v1 I could have a session running for hours without any issues.

---

## Actual token usage?
**u/Toiling-Donkey** · 2026-10-11 21:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3kep6/actual_token_usage/)

In Opencode v1.x, how do I see the total token usage in a session/etc.? 

I find it just shows dollar cost and context size.

I want to know that if I point it at a sizable codebase,  did it just burn 500k tokens, 500M, or 500B?

For me, the token usage rarely goes above 100k-500k using Opus 5.5 …

**Comentarios:**

- **u/maqifrnswa** (↑1, 2026-10-11 21:50): Ask it to make a plug-in to display that. Make sure it distinguishes between cached and uncached tokens as well

---

## Space Bunny overthinks too much
**u/Klein96** · 2026-10-11 21:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3jwhn/space_bunny_overthinks_too_much/)

I've been trying Space Bunny for a while in the recent days.   
It's fast. It's very fast and does achieve some tasks quickly.   
But I noticed how it wastes too many tokens and does too many tests and overthinks for some very simple task.  
  
As one example, one simple python script that I made very easily with gpt 3.5 many years ago. I tried recreating it with Space Bunny and specified exactly which libraries it should use. and while it did eventually make the script. the context went up to 315K tokens and took too much time and the result was too over engineered.

**Comentarios:**

- **u/wwdennis5** (↑1, 2026-10-11 22:25): This is exactly the behaviour I have noticed in tests. It has the highest token usage by a far margin. [https://www.reddit.com/r/opencode/comments/1x2svj9/stepfuns\_step\_5\_preview\_independently\_tested\_on/](https://www.reddit.com/r/opencode/comments/1x2svj9/stepfuns_step_5_preview_independently_tested_on/)
- **u/GoonigUnc** (↑1, 2026-10-12 00:56): ye fr

---

## A Call to Action for Open-Source Developers: Build Alternatives to Adobe, Microsoft, Autodesk, and Subscription-Locked Software (CHATGPT response involving this topic)
**u/Bleeding_Joy** · 2026-10-11 20:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3ip0f/a_call_to_action_for_opensource_developers_build/)

**Comentarios:**

- **u/Robonotes1760** (↑4, 2026-10-11 22:24): A lot of open source alternatives already exist - why not just make them better (or, if really necessary, fork them then make them better) with AI?
  - **u/Bleeding_Joy** (↑1, 2026-10-11 22:44): that's why I was mentioning in the post if an capable open source was already out to contribute to that project instead creating the alternatives from scratch unless people want to
    - **u/BleedReddit** (↑0, 2026-10-11 22:51): Proprietary software → Alternative A → Alternative B → Alternative C
  - **u/nvn911** (↑1, 2026-10-11 23:46): This is the correct answer but maintainers are drowning in the volume poor quality submissions. It's only feasible if we can improve the quality of code, or increase the number of maintainers for a project.
- **u/eastlin7** (↑3, 2026-10-11 22:48): Are you actually gonna do something? Or did you just go into a blind hype after that one article and generated some ai slop and then ran up to a soap box to yell out your grand idea?
    
    
    People have been doing open source software alternatives to large corporations software forever.
  - **u/BleedReddit** (↑-1, 2026-10-11 22:52): [https://github.com/BleedingCodes....I](https://github.com/BleedingCodes....I) guess not.
- **u/Bleeding_Joy** (↑1, 2026-10-12 00:33): okay, im just moldy potato, guys.Trying to sell plastic French fries to save the potato species.
  - **u/BleedReddit** (↑1, 2026-10-12 00:54): Look, dude, I told you they're real fries, just slightly more chewy and shiny.

---

## My first plugin lets your agent rewrite the session title whenever the topic changes so you never lose context.
**u/NEMOalien** · 2026-10-11 20:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3i5pt/my_first_plugin_lets_your_agent_rewrite_the/)

[m-uvex/opencode-topics](http://github.com/m-uvex/opencode-topics)

While plugins that automatically name your sessions are pretty popular, all of them fail at one thing, topic changes. After the plugin names the session for the first time it stays like that forever, even if the topic completely changes.  
  
i built "Topics", a plugin that not only names the session on first prompt but also keeps up with you and renames whenever the topic changes. It works by checking every new message against the title completely tokenless and AI-less to not burn through your subscription, whenever it catches the topic drifting it calls in your AI to simply rename the session to a new 4-6 words title, keeping up with the actual session context instead of staying behind. Whenever it renames it also adds in a \~ to indicate that the topic isn't the original.  
  
If you love it, please drop a star :)

**Comentarios:**

- **u/TheMythicSorcerer** (↑1, 2026-10-12 00:59): 1. How many extra tokens does it use?   
      
    2. How often does it rename the title? every prompt? tool call?

---

## My first plugin lets your agent rewrite the session title whenever the topic changes so you never lose context.
**u/NEMOalien** · 2026-10-11 20:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3hzpu/my_first_plugin_lets_your_agent_rewrite_the/)

https://preview.redd.it/0yjtms0n9wuh1.png?width=1920&format=png&auto=webp&s=249d6614e830108585a3ded78f8c60e26d75ed3c

  
[m-uvex/opencode-topics](https://github.com/m-uvex/opencode-topics.git)

  
While plugins that automatically name your sessions are pretty popular, all of them fail at one thing, topic changes. After the plugin names the session for the first time it stays like that forever, even if the topic completely changes.

So i built "Topics", a plugin that not only names the session on first prompt but also keeps up with you and renames whenever the topic changes. It works by checking every new message against the title completely tokenless and AI-less to not burn through your subscription, whenever it catches the topic drifting it calls in your AI to simply rename the session to a new 4-6 words title, keeping up with the actual session context instead of staying behind. Whenever it renames it also adds in a \~ to indicate that the topic isn't the original.

If you love it, please drop a star :)

---

## I built agent synchronization system for all harnesses
**u/Character_Stand_2847** · 2026-10-11 19:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3gfkq/i_built_agent_synchronization_system_for_all/)

I built cli application that syncs your Claude Code skills, agents, commands, hooks, MCP servers and claude.md, agents.md, codex.md, xxxxx.md files between computers, end-to-end encrypted.

Not just claude code. It can work with other popular harnesses like opencode, codex, antigravity and more. It will sync data across harnesses automatically

Its **FREE TO USE, FOREVER**.  
Plans are just helps me to keep this system online.

Website: [https://skillpouch.net](https://skillpouch.net)  
Source codes: [https://github.com/skillpouch](https://github.com/skillpouch)

**Comentarios:**

- **u/Tariq9977** (↑1, 2026-10-11 19:35): The sync part gets tricky once two machines go offline. If one edits `agents.md` while the other deletes it, I'd want revision hashes plus tombstones so reconnecting can't silently resurrect an old file or overwrite the newer one.
  - **u/Character_Stand_2847** (↑1, 2026-10-11 19:38): yes in webui there's conflicts section. also in tui it warns you if you get conflicts. if 2 versions mismatch you will see it from web and fix the conflicts.
      
      Or i didn't get the problem here because of like how it will go offline and write in one pc and delete in other. Its connected to your account i mean as tariq9977 you cannot be at 2 places at same time.
      
      Or if i didn't get it completely im open for fixing the system if i understand correctly
    - **u/Tariq9977** (↑1, 2026-10-11 19:59): Yep, that's the scenario I meant. Same account on two machines can still diverge while both are offline: laptop edits `agents.md`, desktop deletes it, then both reconnect. If the delete is stored as its own revision/tombstone, your conflict UI can resolve that instead of treating the missing file as no state.
      - **u/Character_Stand_2847** (↑1, 2026-10-11 20:07): I see now. maybe i can do something like set action timestamps locally before merging with cloud. Then which action taken lately will apply
        - **u/Tariq9977** (↑1, 2026-10-11 21:54): That could work, but I wouldn't trust each machine's wall clock for the ordering. If one laptop is a few minutes off, “latest timestamp wins” can pick the older action. A server-assigned revision or logical clock plus the tombstone gives you deterministic ordering without depending on clock sync.
          - **u/Character_Stand_2847** (↑1, 2026-10-11 21:56): yes your concern's right and my approach was wrong so i added graceful delete. you can always restore from webui
- **u/kiriharunya** (↑1, 2026-10-11 21:42): why not use apm for skills/mcp and other things?  
    and how things like gortex syncs?
  - **u/Character_Stand_2847** (↑1, 2026-10-11 21:45): the idea is you will use as what it is normally. it just syncs skills automatically in background. you can still use npm skills or manual file changes. when you save skill in your disk it will sync automatically with cloud. like local changes will upload automatically.
      
      I did this because after factory reset of my computers i had to install everything to my computers but my stack was same. I could use github repo but i got lazy to git pull everytime i made a change. This removes that. You will use your agents normally and once you connect it with cloud, no need to think again like in your work pc those skills and settings will be already there before you even check
    - **u/kiriharunya** (↑1, 2026-10-11 21:57): so what about things like gortex?
      - **u/Character_Stand_2847** (↑1, 2026-10-11 22:14): if gortex an ai harness i can add it no problem. its harness agnostic system it can work with anything
  - **u/Character_Stand_2847** (↑1, 2026-10-11 21:47): currently i have limited amount of harnesses. But im open to add new ones too. I didn't even know whats gortex, i might add it

---

## I built Mentat: A two-layer coding agent. Your code and data never leave your machine
**u/i_matin** · 2026-10-11 18:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3fp23/i_built_mentat_a_twolayer_coding_agent_your_code/)

I built **Mentat**, an open-source project for combining local and cloud AI coding workflows.

We’ve all read the news about OpenAI “allegedly” stealing Navier-stokes solution, and we know lots of “free” providers use our data and code as well. So, I thought of a solution to use their models without leaking any data or code to them. A two-layer approach:

Mentat runs a local model first, which understands your request and your repository, then builds a **synthetic mirror** of your project and hands *that* to a large cloud model. The cloud model makes the change against the mirror. Mentat maps the result back onto your real files with exact token substitution.

Currently Mentat supports:

* **Local layer:** LM Studio (I recommend Qwen 3.8 27b)
* **Cloud layer:** OpenCode

Also, I welcome any feedback and contributions to help expand compatibility with more tools and providers, especially things like **Claude Code, Codex, Ollama, vLLM, and other AI coding agents**.

Repo: [https://github.com/iMaatin/Mentat](https://github.com/iMaatin/Mentat)

 

P.S. If you want to know why I chose this name, read Frank Herbert's Dune.

---

## I built Mentat: A two-layer coding agent. Your code and data never leave your machine.
**u/i_matin** · 2026-10-11 18:14 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3f8tn/i_built_mentat_a_twolayer_coding_agent_your_code/)

I built **Mentat**, an open-source project for combining local and cloud AI coding workflows.

We’ve all read the news about OpenAI “allegedly” stealing Navier-stokes solution, and we know lots of “free” providers use our data and code as well. So, I thought of a solution to use their models without leaking any data or code to them. A two-layer approach:

Mentat runs a local model first, which understands your request and your repository, then builds a **synthetic mirror** of your project and hands *that* to a large cloud model. The cloud model makes the change against the mirror. Mentat maps the result back onto your real files with exact token substitution.

Currently Mentat supports:

* **Local layer:** LM Studio (I recommend Qwen 3.8 27b)
* **Cloud layer:** OpenCode

Also, I welcome any feedback and contributions to help expand compatibility with more tools and providers, especially things like **Claude Code, Codex, Ollama, vLLM, and other AI coding agents**.

Repo: [https://github.com/iMaatin/Mentat](https://github.com/iMaatin/Mentat)

 

P.S. If you want to know why I chose this name, read Frank Herbert's Dune.

---

## I kept missing it when one of my agents was waiting for a yes/no, so I made this
**u/glmn_official** · 2026-10-11 16:14 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3c6sb/i_kept_missing_it_when_one_of_my_agents_was/)

It's one terminal window that runs all your coding agents side by side: OpenCode, Claude Code, Codex.

The point is simple. You see right away which one is waiting for you, and you can answer it right there without switching windows. If you close the terminal, the agents keep running and you can come back to them later.

Works with OpenCode 1 and 2, and it doesn't touch your OpenCode settings.

Free and open source. To try it: npx neurosquad

GitHub: [https://github.com/glmn-ai/neurosquad-cli](https://github.com/glmn-ai/neurosquad-cli)

I built it, it's still early (0.2), so any feedback helps.

**Comentarios:**

- **u/nvn911** (↑1, 2026-10-11 16:20): Herdr already does this right?
  - **u/glmn_official** (↑1, 2026-10-11 16:25): Yeah, herdr is a similar idea and it's good. nsq is the terminal version of NeuroSquad, a desktop app I've been building for a while, so it reuses the same integrations: status comes from each CLI's own hooks, it runs on Windows, macOS and Linux, and there's a phone page and OpenRouter / your own models. The desktop app even speaks herdr's status protocol to get status from Crush. Just a different take, not a replacement.
- **u/YoRt3m** (↑1, 2026-10-11 16:51): No idea what im suppose to see on this because it's a gif and not a video so I got lost
- **u/EDELMARMZ** (↑1, 2026-10-11 16:55): o q ela faz?

---

## CommandCode 1$ Plan with Opencode
**u/aldapsiger** · 2026-10-11 16:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3bzbx/commandcode_1_plan_with_opencode/)

Yesterday I went out all of my subs, so i needed some cheap tokens. CommandCode had 1$ plan, that gives 10$ of ds v4.1 flash, but doesnt work for in other agents. So I asked CommandCode to reverse engineer itself. And it works, so if you need:

[https://github.com/ethanhamilthon/command-code-proxy/tree/main](https://github.com/ethanhamilthon/command-code-proxy/tree/main)

**Comentarios:**

- **u/xatey93152** (↑11, 2026-10-11 16:16): Got banned because of this
  - **u/megablue** (↑3, 2026-10-11 16:18): he posted this 11mins ago and you tried and immediately got banned? okay....
    - **u/CharacterTension2896** (↑2, 2026-10-11 16:25): It’s possible would have to ideally read the TOS
    - **u/jarvis123451254** (↑6, 2026-10-11 16:44): Someone before made this for pi and many got banned for it, it was some big controversy on X
      - **u/gaz_0001** (↑2, 2026-10-11 16:56): I thought you could use the command code API in whatber harness you like?
        - **u/BlackHazeRus** (↑2, 2026-10-11 16:57): Afaik you can, but not $1 plan.
          - **u/gaz_0001** (↑2, 2026-10-11 17:01): Ahahaha.
              I see.🤘🏼🤘🏻
          - **u/PapugaOfficial** (↑1, 2026-10-11 20:40): Wait what? I've been using it for like 2 months on 3 different computers and haven't gotten banned yet
    - **u/FlyingTwentyFour** (↑1, 2026-10-11 22:41): The command code guys were mad like some time ago due to some people using the $1 plan and abusing it while also using it on another harness iirc
        
        it was supposed to be way to gain audience even though they're losing money to it
  - **u/[deleted]** (↑1, 2026-10-11 17:01): [removed]
- **u/WisdomSky** (↑7, 2026-10-11 16:17): I haven't tried command code yet (even though it was one of my options when choosing between opencode, pure DS api, or commandcode), but opted to opencode because of its better reputation and feedback.
    
    I'll try it out after I exhaust my OC Go usage and will try to use this. thanks.
    
    Also, talking about command code, their founder (was it?) has a very nasty attitude and being just a complete online bully also what icks me towards using commandcode.
    
    I just can't see myself having my business on a platform that just throws you under the rug anytime they have tantrums.
- **u/[deleted]** (↑1, 2026-10-11 16:30): [removed]
- **u/audit-content-user** (↑2, 2026-10-11 16:48): Oversold opencode route to API, best experience I had so far is directly with provider to avoid scam (selling Claude by masking Copilot) and better token rate
- **u/upalse** (↑1, 2026-10-11 17:11): There's pi support (pi-commandcode-provider) thats widely used, as well litellm custom handlers.
    
    They all work fine, heard about no bans, unless you do something silly like point Hermes at the litellm proxy.
- **u/FineProfile7** (↑1, 2026-10-11 18:53): https://github.com/TheUnlimited64/rel-si
    
    Did too
- **u/orgkhnargh** (↑0, 2026-10-11 21:14): But why? You can already use any harness with the $10 plan.
- **u/nunugames** (↑1, 2026-10-12 00:06): You guys should try Freebuff, it’s amazing! You get free credits every day, and the things you can do with it are incredible. I’m making my very first game entirely with Freebuff!

---

## opencode ollama/qwen3.5:4b just stoppend while making a plan - why
**u/GawkyGibbon** · 2026-10-11 15:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3b9s4/opencode_ollamaqwen354b_just_stoppend_while/)

---

## "Upstream request failed: Endpoint is unavailable" with Step 5 Preview
**u/YogurtclosetClean478** · 2026-10-11 15:36 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3b974/upstream_request_failed_endpoint_is_unavailable/)

[removed]

---

## unavailable endpoint with step 5 preview
**u/YogurtclosetClean478** · 2026-10-11 15:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3b4l7/unavailable_endpoint_with_step_5_preview/)

[removed]

---

## Space bunny thinking
**u/Expensive-Pop3439** · 2026-10-11 15:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3axtg/space_bunny_thinking/)

https://preview.redd.it/u0jxj00pvuuh1.png?width=1137&format=png&auto=webp&s=0041b8f4a07b0682d276059ae39877646732a4c0

Are you guys seeing this too?

**Comentarios:**

- **u/xx_gamer_xx123321** (↑2, 2026-10-11 15:41): Deepseek v4.1 something confirmed
- **u/DarthNinja95** (↑2, 2026-10-11 15:48): Hmm hmm hmm another hmm
- **u/sudecode** (↑2, 2026-10-11 17:28): let it go  
    let it go
- **u/TheMythicSorcerer** (↑2, 2026-10-11 19:30): Deepseek type behavior

---

## GLM 5.3 Flash on OpenCode Go - quality/quant, speed?
**u/ramendik** · 2026-10-11 15:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3auj0/glm_53_flash_on_opencode_go_qualityquant_speed/)

I am getting good results with GLM 5.3 Flash, on NanoGPT PAYG with FP8 served by SCX. But I would like to look at a subscription for more usage, and OpenCode Go is one of the two leading candidates with the current price.

However I'd like to know how good the quality is (that is, are they serving the FP8 version, which seems to be the full version for this model), and also how good the speed is.

**Comentarios:**

- **u/Sumandora** (↑1, 2026-10-11 19:40): OpenCode Go routes to other providers, one of them is [Z.ai](http://Z.ai), they are currently serving brain-damaged GLM 5.3 Flash. The usage you get is nice tho. I unsubbed mainly because of this... I know its technically nothing they can change, but I just rather pay for OpenRouter and decide the provider I use, rather than praying they route it to the correct one. OpenCode also doesn't tell you where a request was routed. The only reason I know it's [Z.ai](http://Z.ai) is because people on their subreddit also started complaining. But it also doesn't seem consistent... but I usually realize when its too late and the history is already polluted, which is why I just can't work like this any longer... It's also possible that OpenCode Go sometimes routes it elsewhere or that [Z.ai](http://Z.ai) sometimes has mercy, but either way its just playing roulette :(
  - **u/ramendik** (↑1, 2026-10-11 22:24): Understood. I am currently using Nano-GPT which most of the time lets me go to a very nice provider called SCX (cheap, fast, FP8) but sometimes fails to do that but the quality is still good. Guess subscriptions are not an option which kinda sucks. (Nano's own sub is useless for coding agents as it does not discount cache hits)

---

## unavailable endpoint problem with step 5 preview
**u/YogurtclosetClean478** · 2026-10-11 15:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x3asly/unavailable_endpoint_problem_with_step_5_preview/)

[removed]

---

## Good Claude code Artifacts feature for OpenCode?
**u/Decent-Elk-4700** · 2026-10-11 14:44 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x39yyt/good_claude_code_artifacts_feature_for_opencode/)

Hi, I'm looking a way to have a nice Claude Code Artifacts feature in OpenCode? Is any way to get something like that? No need to be shareable but turning explanations into diagrams, interactive documents, maybe in html to visualize project structure, workflows, understand changes and features, etc?

It can be a skill, plugin or whatever it works. Better to be simple and not too much bloated.

Thanks

---

## Error: Upstream request failed: Policy budget exceeded
**u/No_Captain4899** · 2026-10-11 14:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x39ck0/error_upstream_request_failed_policy_budget/)

Error on opencode Go, can't use any model, do anyone know why? 

I still have credits left

https://preview.redd.it/fhm1pdxyjuuh1.png?width=1076&format=png&auto=webp&s=c1f36fed7ea16e232fda85b2ad35071f07f33c02

https://preview.redd.it/82pagj40kuuh1.png?width=895&format=png&auto=webp&s=cf920c8f2cca83ff73e9e90a2894744bfdd65cf5

**Comentarios:**

- **u/Accomplished-Fig4746** (↑2, 2026-10-11 14:51): same error, but i am on zen. i had only used about 30% of my quota
  - **u/No_Captain4899** (↑1, 2026-10-11 15:00): Found the solution, in opencode console, control, delete any policies and it's fixed
    - **u/Accomplished-Fig4746** (↑1, 2026-10-11 15:06): ah that worked! thanks m8, Happy Coding!
- **u/gaz_0001** (↑1, 2026-10-11 16:31): Same
  - **u/No_Captain4899** (↑1, 2026-10-11 16:31): Found the solution, in opencode console, control, delete any policies and it's fixed
    - **u/gaz_0001** (↑1, 2026-10-11 17:02): I did that and then into worked immediately for about 10 minutes.
        Have reset Pi and T3 Code and its super flaky.
        About 80% Failure rate.
      - **u/No_Captain4899** (↑1, 2026-10-11 17:15): That's super weird...
        - **u/gaz_0001** (↑1, 2026-10-11 17:24): Wonder if its becuade I'm running through pi.dev
          - **u/No_Captain4899** (↑1, 2026-10-11 17:29): I was running it trough MiMocode and was working so it should

---

## Is there any other app that can execute shell cmds, read write and edit and is free
**u/Interesting-Movie452** · 2026-10-11 13:02 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x37olx/is_there_any_other_app_that_can_execute_shell/)

title

**Comentarios:**

- **u/mozkohor** (↑1, 2026-10-11 13:29): [pi.dev](http://pi.dev)
- **u/itsner0o** (↑1, 2026-10-11 13:45): Hermes
  - **u/Interesting-Movie452** (↑-5, 2026-10-11 13:53): 
      
      ██╗  ██╗███████╗██████╗ ███╗   ███╗███████╗███████╗       █████╗  ██████╗ ███████╗███╗   ██╗████████╗
      
      ██║  ██║██╔════╝██╔══██╗████╗ ████║██╔════╝██╔════╝      ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝
      
      ███████║█████╗  ██████╔╝██╔████╔██║█████╗  ███████╗█████╗███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║
      
      ██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══╝  ╚════██║╚════╝██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║
      
      ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║███████╗███████║      ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║
      
      ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝      ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝
      
      
      
      ╭───────────── Hermes Agent v0.20.5 (2026.8.19) · upstream 3225f357 · local 93a29d11 (+1 carried commit) ──────────────╮
      
      │                                    Available Tools                                                                   │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⣀⣀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   browser: browser\_back, browser\_click, ...                                         │
      
      │   ⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣇⠸⣿⣿⠇⣸⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀   browser-use: browser\_exec                                                         │
      
      │   ⠀⢀⣠⣴⣶⠿⠋⣩⡿⣿⡿⠻⣿⡇⢠⡄⢸⣿⠟⢿⣿⢿⣍⠙⠿⣶⣦⣄⡀⠀   clarify: clarify                                                                  │
      
      │   ⠀⠀⠉⠉⠁⠶⠟⠋⠀⠉⠀⢀⣈⣁⡈⢁⣈⣁⡀⠀⠉⠀⠙⠻⠶⠈⠉⠉⠀⠀   code\_execution: execute\_code                                                      │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠛⢁⡈⠛⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   computer\_use: computer\_use                                                        │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣦⣤⣈⠁⢠⣴⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   cronjob: cronjob                                                                  │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⢿⣿⣦⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   delegation: delegate\_task                                                         │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣦⣈⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   file: patch, read\_file, search\_files, write\_file                                  │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠦⠈⠙⠿⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   (and 10 more toolsets...)                                                         │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣤⡈⠁⢤⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                     │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   Available Skills                                                                  │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠑⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   autonomous-ai-agents: claude-code, codex, +4 more                                 │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⢰⡆⠈⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   creative: architecture-diagram, ascii-art, +14 more                               │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠈⣡⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   devops: sdlc-review                                                               │
      
      │   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   email: email-inbox-triage, himalaya                                               │
      
      │                                    github: codebase-inspection, github-auth, +5 more                                 │
      
      │  minimax-m3:cloud · Nous Research  media: gif-search, songsee, youtube-content                                       │
      
      │        C:\\windows\\system32         mlops: huggingface-hub, llama-cpp, weights-and-biases                             │
      
      │  Session: 20261011\_175136\_7cb2d7   note-taking: obsidian                                                             │
      
      │                                    productivity: airtable, box, +15 more                                             │
      
      │                                    research: arxiv, blocked-page-recovery, blogwatcher, +3 more                      │
      
      │                                    smart-home: openhue                                                               │
      
      │                                    software-development: dogfood, +9 more                                            │
      
      │                                                                                                                      │
      
      │                                    22 tools · 73 skills · /help for commands                                         │
      
      ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
      
      
      
      Welcome to Hermes Agent! Type your message or /help for commands.
      
      ✦ Tip: hermes chat --source tool tags programmatic chats so they don't clutter hermes sessions list.
      
      💾 curator: snapshot created (2026-10-11T13-51-37Z)
      
      
      
      💾 curator: auto: no changes; llm: skipped (consolidation off)
      
      
      
      ────────────────────────────────────────
      
      ● Hey
      
      Initializing agent...
      
      
      
      ────────────────────────────────────────
      
      ⚠ Auxiliary title generation failed: Connection error.
      
      🔁 Transient APIConnectionError on custom — rebuilt client, waiting 6s before one last primary attempt.
      
      ⚠️  API call failed (attempt 1/3): APIConnectionError
      
         🔌 Provider: custom  Model: minimax-m3:cloud
      
         🌐 Endpoint: [http://127.0.0.1:11434/v1](http://127.0.0.1:11434/v1)
      
         📝 Error: Connection error.
      
         ⏱️  Elapsed: 2.79s  Context: 2 msgs, \~5,584 tokens
      
      ⏳ Retrying in 2.6s (attempt 1/3)...
      
      ⚠️  API call failed (attempt 2/3): APIConnectionError
      
         🔌 Provider: custom  Model: minimax-m3:cloud
      
         🌐 Endpoint: [http://127.0.0.1:11434/v1](http://127.0.0.1:11434/v1)
      
         📝 Error: Connection error.
      
         ⏱️  Elapsed: 7.46s  Context: 2 msgs, \~5,584 tokens
      
      ⏳ Retrying in 4.2s (attempt 2/3)...
      
      ⚠️  API call failed (attempt 3/3): APIConnectionError
      
         🔌 Provider: custom  Model: minimax-m3:cloud
      
         🌐 Endpoint: [http://127.0.0.1:11434/v1](http://127.0.0.1:11434/v1)
      
         📝 Error: Connection error.
      
         ⏱️  Elapsed: 13.74s  Context: 2 msgs, \~5,584 tokens
      
      ⚠️  API call failed (attempt 1/3): APIConnectionError
      
         🔌 Provider: custom  Model: minimax-m3:cloud
      
         🌐 Endpoint: [http://127.0.0.1:11434/v1](http://127.0.0.1:11434/v1)
      
         📝 Error: Connection error.
      
         ⏱️  Elapsed: 21.96s  Context: 2 msgs, \~5,584 tokens
      
      ⏳ Retrying in 3.0s (attempt 1/3)...
      
      ⚠️  API call failed (attempt 2/3): APIConnectionError
      
         🔌 Provider: custom  Model: minimax-m3:cloud
      
         🌐 Endpoint: [http://127.0.0.1:11434/v1](http://127.0.0.1:11434/v1)
      
         📝 Error: Connection error.
      
         ⏱️  Elapsed: 27.03s  Context: 2 msgs, \~5,584 tokens
      
      ⏳ Retrying in 4.8s (attempt 2/3)...
      
      ⚠️  API call failed (attempt 3/3): APIConnectionError
      
         🔌 Provider: custom  Model: minimax-m3:cloud
      
         🌐 Endpoint: [http://127.0.0.1:11434/v1](http://127.0.0.1:11434/v1)
      
         📝 Error: Connection error.
      
         ⏱️  Elapsed: 34.13s  Context: 2 msgs, \~5,584 tokens
      
      ❌ API failed after 3 retries — Connection error.
      
         💀 Final error: Connection error.
      
       ─  ⚕ Hermes  ─────────────────────────────────────────────────────────────────────────────────────────────────────────
      
      
      
       API call failed after 3 retries: Connection error.
    - **u/giveen** (↑3, 2026-10-11 14:01): So it's just trying to call a cloud model but you have it pointed at a local run ollama. The error is right there
- **u/Global-Eye-7326** (↑1, 2026-10-11 15:04): Freebuff is free (app, cloud models). There are other harnesses where you can get a free app and then you connect it to free API's with free cloud tokens. Harnesses include Qwen Coder, DeepSeek Harness (where everything is a plugin), Hermes, etc. Then go find your API's.
- **u/my_new_accoun1** (↑2, 2026-10-11 17:53): bash
- **u/TheMythicSorcerer** (↑1, 2026-10-11 18:30): There's a whole lot of them  
    Find a free api:  
    Pi, Hermes, Openclaw
    
    Has or secretly has a free tier:  
    Codex (but free limit is like nothing)  
    Freebuff
  - **u/Aggravating-Push-207** (↑1, 2026-10-11 19:39): the free tier is actually not that bad, considering it is a frontier model
- **u/ozguru** (↑1, 2026-10-11 19:20): You mean another agent with free  usage quota?, as far as I know, cline and cmdc has free model's to use but I am not sure if they are forcing to you have an active subscription, agy is also have free usage quota.
- **u/arielif1** (↑1, 2026-10-11 20:47): almost all the "apps" themselves are free, the paid part are the models themselves.

---

## 1Billion Token Claim Muse AI (meta)
**u/ImaginaryHat9597** · 2026-10-11 12:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x37bbw/1billion_token_claim_muse_ai_meta/)

Connect Usa Vpn, type muse ai in chrome open it. create account using gmail link ur Instagram or Facebook. click on the right bottom then settings-general-reedem type this code V5NHO0, will get 1 Billion Token.

---

## How is the calculation done?
**u/e99koob** · 2026-10-11 12:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x36q9j/how_is_the_calculation_done/)

[removed]

---

## Costs analysis: DeepSeek v4.1 Flash vs GLM 5.3 Flash
**u/Long_Rub5460** · 2026-10-11 12:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x36k86/costs_analysis_deepseek_v41_flash_vs_glm_53_flash/)

[OpenCode dashboard](https://preview.redd.it/mq8exdzmrtuh1.png?width=1492&format=png&auto=webp&s=ac8971572da799b0ffa7b7abec0e3f58951db3de)

[CommandCode dashboard](https://preview.redd.it/uwjvp1qcstuh1.png?width=428&format=png&auto=webp&s=5e8bf9179ce2ab0f85aea33b3083048e4644970b)

Myself included, a lot of peeps have had concerns about GLM 5.3 Flash consumption vs DeepSeekv4.1 Flash, hence the analysis. This is seen across both CommandCode and OpenCode.

Let's refer to these recent usage numbers as detailed in OpenCode (and also Commandcode) dashboards.

# Usage and cache hits

Deepseek did about 2.5x the work for only 20% extra cost.  
GLM cache hit rates are lower than DeepSeek.  
DSv4.1F   - 641M/663M cached (96%)  
GLM5.3F - 200M/218M cached (92%)  
  
**Rates:**

* **DeepSeek V4.1 Flash:** Uncached input: $0.15/1M | Cache read: $0.003/1M | Output: $0.60/1M
* **GLM-5.3 Flash:** Uncached input: $0.15/1M | Cache read: $0.03/1M | Output: $0.50/1M

Seems like GLM should be cheaper with equivalent pricing, but cheaper outputs. While output tokens are the most expensive, they are also the least significant for AI cost estimations. highly relevant here is the cost of cached tokens, which is **10x** for GLM 5.3 Flash.

Let's looks at costs for a workload of 500M input token and 5m output,  
Using the rates (identical) from [Command Code](https://commandcode.ai/docs/plans/goat) and [OpenCode](https://opencode.ai/docs/go/#usage-limits) for 500M input tokens and 5M output tokens:

# DSv4.1F (96% cache hit @$0.003)

* **Uncached Input (20M):** 20 × $0.15 = **$3.00**
* **Cached Input (480M):** 480 × $0.003 = **$1.44**
* **Output (5M):** 5 × $0.60 = **$3.00**
* **Total DS Cost:** **$7.44**

# [PEAK hours] DSv4.1F (96% cache hit @$0.006)

* **Uncached Input (20M):** 20 × $0.30 = **$6.00**
* **Cached Input (480M):** 480 × $0.006 = **$2.88**
* **Output (5M):** 5 × $1.20 = **$6.00**
* **Total DS Cost:** **$14.88**

# GLM-5.3F (92% cache hit  @$0.03)

* **Uncached Input (40M):** 40 × $0.15 = **$6.00**
* **Cached Input (460M):** 460 × $0.03 = **$13.80**
* **Output (5M):** 5 × $0.50 = **$2.50**
* **Total GLM Cost:** **$22.30**

# Verdict

So there we go mystery solved, GLM dude costs about 3x the DeepSeek dude for this kind of workloads. In general, Deepseek is also a bit more verbose though and does more output than GLM. So the ratio leans a bit more towards GLM. Also given GLM's slightly higher intelligence and succinctness it's still pretty good in terms of actual work done rather than token counts.

Use **Deepseek v4.1 Flash** during non peak hours unless you really need **GLM 5.3 Flash**. GLM during DS peak hours. Both models are pretty close and have their own perks and gotchas.

**Comentarios:**

- **u/mozkohor** (↑15, 2026-10-11 12:32): this just in, the model that costs more, costs more
  - **u/Long_Rub5460** (↑4, 2026-10-11 18:23): Should add that as a tldr on the top...
  - **u/DangerousLiberal** (↑2, 2026-10-11 20:14): But it might be more token efficient.
- **u/Imaginary_Big631** (↑0, 2026-10-11 13:24): always I think the same, the most important is the price and % hits of cache hits...
- **u/Ctbhatia** (↑0, 2026-10-11 13:36): the cache hit rate is doing the work in that comparison, deepseek's prefix reuse is why it looks 2.5x cheaper per unit of work. i work at [coralbricks.ai](http://coralbricks.ai) and cached input bills at $0 on both models, so a high-hit loop is basically input cost.
  - **u/ramendik** (↑1, 2026-10-11 15:29): Looks very interesting but you don't seem to have GLM 5.3 Flash? It's not a small GLM 5.3, it's actually new tech, related to GLM 5.3 like DS 4.1 Flashbis related to DS 4 Pro. I like GLM 5.3 Flash more, and am looking for providers for that. Also can you confirm FP8 quant?
    - **u/Ctbhatia** (↑1, 2026-10-11 16:09): yep, GLM 5.3 Flash is retired, its ids 404 since oct 7; at [coralbricks.ai](http://coralbricks.ai) we serve glm-5.3-fast which is the nvfp4 revision, not fp8. on cache, no client flag needed, prefix reuse is automatic and cache write is just prompt\_tokens minus cached\_tokens, and setting prompt\_cache\_retention to off bills novel input as plain input instead.
      - **u/ramendik** (↑2, 2026-10-11 16:13): I outright just like GLM 5.3 Flash more than GLM 5.3 full, and that before we talk of quant, so sadly looks like this is not a match
        - **u/Long_Rub5460** (↑1, 2026-10-11 18:40): I agree, though GLM full has higher intelligence, likes of the Mimo 2.6 Pro have higher intelligence at under a quarter of the costs. GLM 5.3 Flash is still a beast at the price point.
          - **u/ramendik** (↑1, 2026-10-12 00:58): If you ever bring back GLM 5.3 Flash at coral bricks, I do want to try it. Currently on NanoGPT and most spending is on cache.
          - **u/ramendik** (↑1, 2026-10-12 01:01): I am not a fan of MiMo 2.6 orobasbi saw in smoke tests. I like the style of thought in GLM 5.3 Flash. 
              
              Getting it served at quality on budget is tricky though
  - **u/Long_Rub5460** (↑1, 2026-10-11 18:39): At prices on your website, DSv4.1F would cost $7.80 for this workload.  
        
      **DSv4.1F (96% cache hit @$0.003)**  
      Uncached Input (20M): 20 × $0.09 = $1.80  
      Cached Input (480M): 480 × $0.006 = $0  
      Output (5M): 5 × $1.20 = $6.00  
      Total DS Cost: $7.80
      
      GLM costs are pretty interesting.  
      I wonder at what cache hit rate would the users break even vs the extra caching charges?
    - **u/Ctbhatia** (↑1, 2026-10-11 19:13): cached reads are $0, so the only cache charge is the write. i work at coralbricks.ai. ds v4.1 flash writes at $0.01 input + $0.08 cache write, so it needs about 8 re-reads to beat re-sending the prefix.
      - **u/Long_Rub5460** (↑1, 2026-10-11 19:27): I meant vs standard pricing.
        - **u/Ctbhatia** (↑1, 2026-10-11 20:05): yeah vs standard pricing. cached reads are $0, so the only extra is the write: ds v4.1 flash is $0.01 input plus $0.08 write, so about 9 sends of the same prefix before it beats paying input every time. i work at coralbricks.ai.
- **u/BoatZealousideal4521** (↑4, 2026-10-11 13:55): Thanks for this analysis. As per my experience Deepseek is much cheaper than GLM flash. I used low variant of both and for similar work GLM ended up consuming $3.75 whereas Deepseek Flash did same work in $1.75. 
    I personally like GLM Flash it has worked wonderfully for me, but DeepSeek cannot be overlooked.
    I have not spent much time with DeepSeek Flash, but at the end what matters is how much money is deducted from the kitty.
    
    Thanks once again.
  - **u/Long_Rub5460** (↑3, 2026-10-11 18:25): 100% I really like to use glm dude for some of my code stuff. But DeepSeek is my default everywhere (Hermes, OpenChamber chats).
- **u/Beautiful-Salary-191** (↑4, 2026-10-11 14:48): I use glm 5.3 flash a lot and it works well for me. I don't think it id worth it to try to adapt to deepseek. However, mimo layest model is on the pareto frontier curve.
    
    Did you try it?
  - **u/Long_Rub5460** (↑2, 2026-10-11 18:27): Yes, I love the new Mimo Pro, a beauty!
- **u/evia89** (↑0, 2026-10-11 14:59): No one pay for glm api here. Its all subs.
    
    Compare $20 claude vs $20 codex vs $18 (-50%-30% compound) zai lite. Only DS worth doing API since both subs are fucked:
    
    1) opencode go is slow and cache rate is well below DS. Hints on some quant. 2) command code is shady
- **u/Swipefeed** (↑1, 2026-10-11 15:07): imagine paying for GLM 5.3 flash😅😭. You guys are sleeping on FreeBuff. You can get free 6 hours of it EVERYDAY.
- **u/palucdev** (↑3, 2026-10-11 18:44): GLM 5.3 Flash has one more downside for me. It is frequently returning responses at the end of longer reasoning loops in chinese. I use workflows and stuff written purely in english so I do not know why it randomly switches but thats annoying. Never had any of this on Deepseek 4.1 Flash.
  - **u/lordwotton97** (↑1, 2026-10-11 20:00): It happened to me twice today with ds4.1
  - **u/evia89** (↑1, 2026-10-11 20:21): zai never does that. well as long as u keep below 200k
      
      weird that I see it really often @ go
  - **u/MarcusAurelius68** (↑1, 2026-10-11 21:22): I get Chinese responses all the time in the chat window with DeepSeek. Haven’t seen it via the API yet though.
  - **u/eastlin7** (↑2, 2026-10-11 22:09): I have seen random Chinese characters in deepseek. But the final output is never that so there literally no reason to care or obsess over it.
- **u/fragment_me** (↑1, 2026-10-11 21:00): Deepseek will think for 100k+ tokens and its wayyyy more verbose.  You need to take the tokens to complete task into account.
  - **u/Long_Rub5460** (↑1, 2026-10-11 22:00): True that, the first para in verdict does touch up on that.
- **u/PerfectReflection155** (↑3, 2026-10-11 21:45): Thanks for this breakdown, these are my 2 favorite worker models so this is extremely relevant to me.
    
    I will lean towards deepseek more in future although I do find Glm a bit smarter.
    
    What are your thoughts on step 5 preview free through opencode go? It seems quite decent and considering its free I’ve been using it a lot
  - **u/Long_Rub5460** (↑2, 2026-10-11 22:02): Yep, Step 5 is great I'm using that one significantly this week.  
      I do feel GLM Flash performs a bit better than DSv4.1F sometimes.
- **u/SalemDono** (↑1, 2026-10-12 00:08): Please add Mimo-V2.6-Flash to the analysis.
    these are the three workhorse models that I keep on rotating between

---

## How is this calculation done?
**u/e99koob** · 2026-10-11 12:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x36j5c/how_is_this_calculation_done/)

[removed]

---

## Opencode VS Claude 20e
**u/spirit_sound77** · 2026-10-11 10:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x34xqg/opencode_vs_claude_20e/)

**Comentarios:**

- **u/spirit_sound77** (↑1, 2026-10-11 10:36): Which one are you guys going for right now? Is it on par with Claude’s $20/month subscription? I think it is.

---

## New to OpenCode, curious about usage limits on free tier
**u/Keremvona** · 2026-10-11 10:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x34d29/new_to_opencode_curious_about_usage_limits_on/)

Hi,

I am new to OpenCode and I saw that they offer lots of free tier models. My question is how does the usage limits and reset work on the free tier? (is it weekly, 5hr or 24hr?)

The model I am using Muse Spark 1.3 free seems to have a large usage limit and this made me think how much of this I can use before the reset.

**Comentarios:**

- **u/YoRt3m** (↑2, 2026-10-11 10:05): Daily at 2am for me
- **u/ConferenceOver8258** (↑2, 2026-10-11 10:28): Without a Go subscription, you'll likely hit limits within 1 to 2 hours; I'm not sure about the exact token count. However, after subscribing to Go, I haven't encountered any restrictions on free models.
- **u/for4f** (↑1, 2026-10-11 10:44): resets daily at utc midnight, so 9am our time. the free list rotates too so don't get too attached to one model. if you're hammering it you'll hit the short-term rate cap before the daily one, normal paced use lasts way longer
- **u/Dangerous-Bench-5988** (↑1, 2026-10-11 16:03): Best to check it yourself , It varies with the task you are doing . Give it a large task and check it yourself a day
- **u/daniel-sousa-me** (↑2, 2026-10-11 20:44): About Muse Spark: https://reddit.com/comments/1x2kzah/comment/pf6ce8f
    
    For the last couple of month there has often been some stealth model with unlimited usage. Right now I think Step 5 (and Longcat 2.5?) are unlimited

---

## Issues with Claude Haiku 5.5 (Opencode Go)
**u/Osvik** · 2026-10-11 08:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x32jwa/issues_with_claude_haiku_55_opencode_go/)

Claude Haiku 5.5 (Opencode Go) was the only model I've tried with my benchmark project that could not produce any working code. The model just stops working after a few steps. I've tried with max and xhigh 4 times. I'm using Opencode 2. TUI.

I did this project with 24 other models since a few months ago. (BTW Space Bunny Free was the best model in this specific project and many other models did a good job)

Does this match your experience?

**Comentarios:**

- **u/Tariq9977** (↑1, 2026-10-11 08:38): Since both max and xhigh stall after a few steps on the same project, what does the stall look like in the TUI right before it stops.
  - **u/Osvik** (↑2, 2026-10-11 08:53): It just stops as if the task has finished but without the usual report. If I ask "Hello?" it recognizes it has stopped, ask me if it wants to continue to switch to implement mode and a 2 or 3 minutes latter it stops again.
    - **u/Tariq9977** (↑1, 2026-10-11 14:48): The missing report is a good clue. I'd compare the final provider stop reason and last assistant event for Haiku with a model that finishes the same benchmark. If OpenCode receives a normal end while work is still pending, that points away from the TUI.
- **u/zenkov** (↑1, 2026-10-11 10:13): In my case, Haiku 5.5 actually failed with an error. Luckily, it happened near the end of the project, and DeepSeek 4.1 managed to finish the job.
- **u/krautsourced** (↑1, 2026-10-11 21:21): Curious to see the context size, since Haiku 5.5 pricing switches pricing at iirc 100k context - maybe it just turns off once it reaches the higher tier?

---

## Mac users how are you installing and using your opencode setup?
**u/Im_A_Praetorian** · 2026-10-11 07:38 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x321w2/mac_users_how_are_you_installing_and_using_your/)

For those of you using LocalLLMs (or not), how are you installing and using opencode? 

Are you installing or using some sort of VM or Container to sandbox it?

Is it on a development Mac and you just run it in your admin account? 

Are you just using it in your regular account on your Mac and hoping for the best? 

  
Interested in hearing the various setups people are using and why that's the best.

**Comentarios:**

- **u/sudoer777_** (↑1, 2026-10-11 22:01): I've used Nix/home-manager and ran it in the same unprivileged account I do my other work in like on my Linux machine

---

## Вкатился в вайб-кодинг
**u/abrickosik** · 2026-10-11 07:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x31jik/вкатился_в_вайбкодинг/)

---

## Hy4 Preview is broken
**u/imbaconman** · 2026-10-11 05:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x30ayj/hy4_preview_is_broken/)

Has anyone tried Hy4 with their Go subscription? 

Mine seems to just hallucinate from the first prompt replying in a mix of Russian, Chinese, Vietnamese, Korean and English that makes no sense.

**Comentarios:**

- **u/zenkov** (↑1, 2026-10-11 10:14): You just don't understand.

---

## My short experience in composing videos with Hyperframes and how I was able to improve a bit the videos
**u/Odd_Donkey2691** · 2026-10-11 05:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2zutp/my_short_experience_in_composing_videos_with/)

Hello Forum, if you are a newbie to faceless video composition with Hyperframes, I wanted to share a smal progress I made in order to improve my videos. They were simple, something like an Slideshow. After several videos I made, they look too boring and the same, I always wondered how other creators were able to make such nice videos. I understand that some of them use Claude as Claude is a beast with Motion Graphics. I even tought it was a limitation to Hyperframes but then I realized hyperframes has nothing to do with it but rather the capability of the model you use and the directions you give on your prompt. 

  
Bewlo you can find a comparison for the same topic using the new prompt and direction I gave to the models. In my opinion Deepseek Flash made a great job and I would dare to say that is even better than 5.6 Tera. Howver I used Deepseek Harness Standard Preset and it took about 2 hours to complete, DSH does squeezes the best ouf of DS. 

Here you can see the type of videos I used to make before: [https://streamable.com/ydd8b2](https://streamable.com/ydd8b2)

New style with Deepseek 4.1 Flash: [https://streamable.com/i6zhkf](https://streamable.com/i6zhkf)

New Style with ChatGPT  5.6 Luna: [https://streamable.com/cc5wlh](https://streamable.com/cc5wlh)

**Comentarios:**

- **u/A_Far_Hitman** (↑1, 2026-10-11 06:58): I cant seem to acces the website, could you post those videos in the comments?
  - **u/Odd_Donkey2691** (↑2, 2026-10-11 07:00): https://reddit.com/link/pf7400z/video/sx2c69pzdsuh1/player
      
      ChatGPT
  - **u/Odd_Donkey2691** (↑2, 2026-10-11 07:01): https://reddit.com/link/pf742cx/video/u75a3kx2esuh1/player
      
      DeepSeek

---

## Opencode 2 vs v1.19.0
**u/tpakhoa** · 2026-10-11 03:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2xzfg/opencode_2_vs_v1190/)

Im confused about the latest version here. Why cant I find v2 releases on github? What are the noticeable changes for v2?

**Comentarios:**

- **u/Robert__Sinclair** (↑1, 2026-10-11 03:50): I prefer version 1 ten times over version 2
  - **u/Strict-Cicada6225** (↑8, 2026-10-11 04:13): Why ?
    - **u/DrinkClubMate** (↑-6, 2026-10-11 05:30): 1 is mature cute and stable
        
        2 is something else in alpha beta and not finishef
    - **u/Robert__Sinclair** (↑-1, 2026-10-11 14:23): tab switches agent from build to plan. big pickle is better than the default on v 2.  
        generally v1 is faster (even if lately big pickle is unusable)
- **u/BoatZealousideal4521** (↑9, 2026-10-11 03:59): I updates to 1.19.0 and it is giving me option to update to 2.0 cli. I am not sure if I should proceed with 2.0. is it stable?
  - **u/look** (↑15, 2026-10-11 04:05): I’ve been using v2 for a while (starting back when it was in beta), and for me, it has been more stable and with a ton of bugs fixed compared to v1.
      
      I was likely going to ditch opencode entirely until I tried v2.
    - **u/BoatZealousideal4521** (↑5, 2026-10-11 05:28): V2 is cli version as well right or a GUI only version. I prefer CLI version.
      - **u/Bubbly_Winter_1950** (↑2, 2026-10-11 05:58): There is cli v2 too, im using it a couple of weeks, didn’t notice any issues
        - **u/Bubbly_Winter_1950** (↑2, 2026-10-11 06:52): The only thing I’d point though is some plugins are not ready for v2 yet, so if you rely on any of them it’s worth to double check first
  - **u/Mean-Elk-9439** (↑1, 2026-10-11 05:03): If you update you won't be able to use v1 sessions.
    - **u/BolsaDeDolores** (↑2, 2026-10-11 13:30): Not true, I used mine
- **u/megablue** (↑6, 2026-10-11 04:05): V2 is not set as default branch yet
- **u/reachjalil** (↑1, 2026-10-11 04:19): The forced migration is so out of touch. Why can’t you just support your threads dude
- **u/Ashamed_Drag8791** (↑18, 2026-10-11 04:20): Read their docs man, what are we, your agents?
  - **u/taytay735** (↑-1, 2026-10-11 05:45): If OP is willing to sponsor an OpenCode Go subscription I’d be willing to spin up a few agents to help him research
  - **u/tpakhoa** (↑4, 2026-10-11 13:23): I read this docs https://opencode.ai/v2/docs/migrate-v1/ . But I dont see the motivation to why v2 is necessary, like most of the breaking changes are about config schema and contracts.
      
      RAM improvements seem nice. I will try it out. Thank you.
- **u/ohhno_whyamihere** (↑-2, 2026-10-11 04:25): Gng opencode v2 broke my whole workflow and has been acting weird ,tbh if u are using plugins, custom scripts ,etc ,u need to first fix them before updating ,i ruined my whole day and destroyed my codebase ,tbh
  - **u/lmoelleb** (↑4, 2026-10-11 06:23): How can you "destroy your codebase" when you can just do git revert?
    - **u/PanPanForReal** (↑2, 2026-10-11 06:39): Skill issue. He's just sucks at everything and blame everything
      - **u/ohhno_whyamihere** (↑-2, 2026-10-11 08:32): Uhh nah ,i just said everything for dramatic effect ,lowkey nothing happened to my codebase, just most of my work stopped for a day while trying to fix it ,hihihi
- **u/xatey93152** (↑3, 2026-10-11 05:04): Version 1 is better. Opencode doing reverse versioning
- **u/Late_Seat_299** (↑1, 2026-10-11 05:09): They changed how the web ui works that’s for sure. Defaulting username and password which I couldn’t actually find was opencode, still don’t know the default password and just used my own, which is set before start. They also I think implemented cors as part of the json config. More secure yes, more complicated also yes. There’s a new mini ui as well
- **u/Classic_Vegetable280** (↑3, 2026-10-11 05:20): you can find them [https://github.com/anomalyco/opencode/tags](https://github.com/anomalyco/opencode/tags)
- **u/ollm-tux** (↑3, 2026-10-11 06:25): i gave up v1 on all the device because v2 is more advanced, in v1 I had configured 7 mcp in v2 I left only 3, but on most only 1 mcp, simply there was no need in v2, the models seem to be doing better, the giving up I did with total uninstall, cleaning, installation from scratch to avoid conflicts, in v2 I no longer installed oh- my- opencode, in cli seems easier to use, now you have tabs up with sessions, and in opencode web appeared the requirement of a parole which allows me sharing with other devices even in public networks, so there are no more risky changes than that can be experienced. Nothing negative compared to v1
- **u/[deleted]** (↑1, 2026-10-11 07:51): [removed]
- **u/gurolayanlar** (↑4, 2026-10-11 08:13): "Can you paint the picture of happiness, Abidin?" *Nazım Hikmet's Saman Sarısı*  
    
    
    Opencode v2 can create images, bro. I think that's enough.
  - **u/[deleted]** (↑1, 2026-10-11 12:45): [removed]
- **u/Awkward_Intern2623** (↑1, 2026-10-11 09:06): Opencode v2 keeps a background service runnin' round the clock. You might find your customizations don't carry over when you make the switch, though otherwise it's pretty much v1 as you've always known it.
- **u/Top-Transition6825** (↑1, 2026-10-11 09:07): Have u ever tried freebuff? I think its a good AI tool
- **u/Low88M** (↑2, 2026-10-11 11:06): 1. Is there « a way » to install v2 from latest v1 without loosing v1 ? Like a copy/update process that guarantees to keep all settings and sessions to remain available on v1 install/launch ?
    
    2. Also, if I update to v2, will my settings (permissions, LLM server settings and tools) will survive or will u have to spend 1/2 days setting them again ? 
    
    In all cases, I know I’ll need to keep access v1’s sessions, but I’d like to try v2 to see how it behaves. I didn’t find any clear data on v1-v2 migration for these questions on anomalyco’s github or opencode-ai site, even on DeepWiki for that project… I’Lo stay on v1 until I’m sure
  - **u/Alive_Solution_689** (↑2, 2026-10-11 13:33): Ask opencode to install v2 for you in parallel and do all the migrations. Worked for me and survived several v2 updates already. If there should be a small issue during updates go back to v1 ans and ask it to fix it for you.
  - **u/WisdomSky** (↑1, 2026-10-11 16:27): Same as the other comment, I just asked the model inside opencode to install opencode v1 as opencode and retain opencode2 (since opencode v2 binary already is named opencode2) and the AI even added guardrails to prevent you from accidentally updating it to v2.
      
      now I have opencode v1 aliased as "opencode" and opencode2 as just "opencode2". This is useful especially if you are using a code editor/ide like Jetbrains and uses an opencode extension which still uses opencode v1 command structure. the v2 has breaking changes to the commands so yeah it broke those extensions too.
      
      An example was the opencode server. the new syntax in v2 is "opencode serve --port=XXXX", while in v1 it's just "opencode --port=XXXX".
- **u/StevenB0ss** (↑1, 2026-10-11 11:30): Its nice that you can manage all open sessions BUT one major annoying thing is that i CANNOT see the subagent its used context & the model. I hope theres a fix
- **u/ndaidong** (↑1, 2026-10-11 13:43): There is no releases, but you can look at the tags section.
    v2 gets improved a lot in resource usage. 
    I'm not very familar with their git model. Currently there are 2000+ branches. Don't know how they can manage them. Plus more than 4000 unresolved issues, I'm worry that it's out of control.
  - **u/plymouthvan** (↑6, 2026-10-11 14:09): “Fix all the issues. Make it good. No mistakes.”
  - **u/liambox123** (↑1, 2026-10-12 00:07): Ellos usan opencode para arreglar opencode

---

## I built a tiny (<1MB), local-only desktop widget app with a retro phosphor terminal aesthetic, meet SnappyTiles !
**u/Little_Marsupial9383** · 2026-10-11 01:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2vxvd/i_built_a_tiny_1mb_localonly_desktop_widget_app/)

Hey everyone, I’ve been working on a small side project on my local machine to fix a personal annoyance, most modern desktop widgets and dashboards are bloated, heavy on resources, or try to sync everything to the cloud.

I wanted something super lightweight, offline, and styled like an old-school amber phosphor terminal. I call it **Snappy Tiles**.

Right now, the whole app sits at **under 1 MB**. Everything stays local on your machine, and it’s designed to be lean and modular.

**Key Features So Far:**  
**Grid & Snapping System:** You can drag modules around, snap them into place, reorder the layout, or collapse (shrink) modules you don’t need.

**8 Initial Modules:**  
**Clock & Weather:** Minimal digital clock with local weather info.  
**Calendar:** Quick-glance monthly view.  
**API / Token Usage (Opencode Go):** Shows usage bars with estimated ETA indicators.  
**Media Controls:** Displays current track, artwork, and playback buttons.  
**Date Countdown:** Track upcoming events or trips.  
**Nook:** A dedicated little tile featuring a small, animated pixel ghost pet that floats around and reacts/interacts with you (planning to expand this one a lot!).  
**Tasks:** Simple offline To-Do list  
**Focus:** Customizable Pomodoro focus timer.  
**Customization:** Full control over colors, window transparency, and an "Always on top" toggle.  
**Extensible:** Built on a simple internal template so creating custom modules is straightforward.

**Current State**  
It’s not published anywhere yet, just running on my setup while I polish the layout engine, animations, and snap feel.  
Before I package it up or set up a public repo, I’d love to get some early feedback any of you, I’m not planning on selling it or charging a dime for it, just wanted to solve a personal issue with productivity widgets and the opencode go dashboard and work on something new!

**Comentarios:**

- **u/Emotional-Bag-3754** (↑1, 2026-10-11 05:54): Link?

---

## StepFun's Step 5 Preview Independently Tested on Terminal Bench 2.1
**u/wwdennis5** · 2026-10-10 23:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2svj9/stepfuns_step_5_preview_independently_tested_on/)

***Step 5 Preview Free*** is available for free for a week. So I have benchmarked it against a few other models that were recently free (and mimo v2.5) and its performance sits within the pack. Over the 89 tasks in TB 2.1, Step 5 solves 48-53% of the problems, uses less tokens than space bunny, but more than longcat 2.5.

|Model|Pass@1|Pass@3|Tokens Per Trial|
|:-|:-|:-|:-|
|Step-5 Preview|50.2% (134/267)|64.0% (57/89)|\~0.90M|
|Space Bunny (retired)|52.1% (139/267)|66.3% (59/89)|\~1.69M|
|LongCat 2.5 Preview|48.7% (130/267)|64.0% (57/89)|\~0.54M|
|MiMo v2.5|44.2% (118/267)|66.3% (59/89)|\~0.57M|

Finally, I know that a few more models are free via opencode zen, including the newer mimo v2.6 flash, but have not got round to this yet. How does this align with people's experience so far?

**Comentarios:**

- **u/GoonigUnc** (↑0, 2026-10-11 08:13): dude i had stroke reading those graphs
  - **u/wwdennis5** (↑1, 2026-10-11 08:34): How would you improve it?
    - **u/GoonigUnc** (↑1, 2026-10-12 00:21): i think just the table was enough.
- **u/Latter-Olive-2369** (↑2, 2026-10-11 12:38): Thanks!
- **u/crotch-mavens** (↑1, 2026-10-11 13:29): It's very slow.
  - **u/wwdennis5** (↑2, 2026-10-11 13:49): Here are the times per trial, where step 5 is the slowest but also has a much lower token count than space bunny so it feeling slow makes sense. 
      
      \- mimo: median 830s, mean 1071s, total 79.1 trial-hours  
      \- bunny: median 979s, mean 1238s, total 91.8 trial-hours  
      \- longcat: median 784s, mean 1034s, total 76.7 trial-hours  
      \- step5: median 970s, mean 1261s, total 93.5 trial-hours
- **u/Amarsir** (↑2, 2026-10-11 18:19): Much appreciated. That very much clears up what league it's in. 
    
    I hadn't realized Space Bunny was so token-inefficient. I guess being on free meant there was little reason to look.
  - **u/wwdennis5** (↑2, 2026-10-11 18:35): Yes I didn't realise that either but its important to note that I tested space bunny across this window *2026-10-01 21:04 → 2026-10-02 18:11 UTC,* and the model's token efficiency may change before it comes out of stealth and we find out what it is.

---

## Old Usage by Model Graph Gone??
**u/torsoreaper** · 2026-10-10 22:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2sfyp/old_usage_by_model_graph_gone/)

Is the old graph gone where I could see a stacked chart on which model was using most of my usage?  Right now it's just 1 block with no detail.  Running multi agent it used to be very easy to see which model was burning up tokens faster.  Would love to find how to see the old way again.

**Comentarios:**

- **u/HumbleAngelX** (↑1, 2026-10-10 23:03): I miss too. Another "open" company going not so open?... not a good signal, I hope they rebuild this on console soon.
- **u/Caelinus** (↑1, 2026-10-10 23:13): It does show per model usage under your keys on the website. Not sure if that would be useful for your purposes though.
  - **u/torsoreaper** (↑1, 2026-10-11 00:20): Yea just easier to see in a graph...  it used to look like this: [https://www.reddit.com/r/opencode/comments/1wflrgo/usage\_comparison\_for\_the\_last\_3\_days\_opencode\_for/](https://www.reddit.com/r/opencode/comments/1wflrgo/usage_comparison_for_the_last_3_days_opencode_for/)

---

## MiniMax $10 plan vs. OpenCode Go — which is better?
**u/Smooth-Plan4769** · 2026-10-10 21:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2r8fe/minimax_10_plan_vs_opencode_go_which_is_better/)

I have a $10 MiniMax token plan. Is it worth switching to OpenCode Go?

**Comentarios:**

- **u/migsperez** (↑9, 2026-10-10 22:01): Opencode Go
  - **u/pikuray** (↑3, 2026-10-11 01:55): To the polls!
    - **u/pigletmonster** (↑3, 2026-10-11 12:21): Ok hillary from 2015
- **u/Amarsir** (↑3, 2026-10-10 22:37): We have no idea how much MiniMax's plan provides because they don't tell you. And there aren't enough people who decided to give it a shot and do their own measurements.
    
    So I have to say Opencode Go, just because how can I recommend a black box?
- **u/Soul_Mate_4ever** (↑2, 2026-10-10 23:18): What’s your experience like with minimax?
  - **u/Smooth-Plan4769** (↑2, 2026-10-10 23:51): I’m a long-time customer and have been on the $10 plan since the 2.7 version; I didn't like it for coding. The M3 has been performing well in that regard, but the biggest issue is the plan's usage—I tend to burn through the 5-hour limit really quickly.
    - **u/taytay735** (↑1, 2026-10-11 03:46): I like Go, but would not recommend if your intention is to use M3 with Go. Go's limits are best when using other models like DeepSeek 4.1 Flash, MiMo 2.6 Flash, Muse Spark 1.3.
        
        Estimated request quota per 5 hr here: [https://opencode.ai/go](https://opencode.ai/go)
- **u/RepulsiveRaisin7** (↑2, 2026-10-10 23:26): M3 sucks, get Go
- **u/Ctbhatia** (↑2, 2026-10-11 00:18): compare them on $ per 1M in and out and whether cached reads are billed, those are the parts the flat monthly price hides.
- **u/PermanentLiminality** (↑2, 2026-10-11 01:06): Go has a lot of different models to try.  The minimax plan does not.
- **u/mylabfr** (↑2, 2026-10-11 02:03): Minimax has a $10 plan? was it a long time ago? I mean old plan?
  - **u/Smooth-Plan4769** (↑1, 2026-10-11 12:09): Yes, it was an old plan.
- **u/xatey93152** (↑2, 2026-10-11 05:16): Go is highly quantized
- **u/GoonigUnc** (↑1, 2026-10-11 06:21): opencode go. you get to use lots of different model for more usage than you pay. you can just use minimax in opencode go if you like. its a no brainer
- **u/Infamous-V** (↑1, 2026-10-11 13:35): opendesign is now offering DP v4.1 Flash worth 120$  for 8$ this month. nothing beats it for the time being.
  - **u/wallacer95** (↑1, 2026-10-12 01:09): where
- **u/Additional_Code** (↑1, 2026-10-11 13:46): Opencode Go

---

## Extremely slow OC response.
**u/Sleeper_444** · 2026-10-10 21:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2r34b/extremely_slow_oc_response/)

I just got the $10 "Go" plan from OpenCode, and the responses are extremely slow for all models. I don't know what's going on is anyone else experiencing this?

**Comentarios:**

- **u/No-Peak8310** (↑1, 2026-10-10 21:55): Pues eso que en fin de semana suele ir más rápido
- **u/horrbort** (↑1, 2026-10-10 21:58): Yep normal it’s a cheap plan
- **u/cezarducatti** (↑1, 2026-10-10 22:14): There's a problem today...

---

## DeepSeek V4 Flash returns HTTP 404, Kimi K2.7 Code returns HTTP 410, but GLM-5.3 works
**u/SrAlexis_** · 2026-10-10 19:00 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2n54p/deepseek_v4_flash_returns_http_404_kimi_k27_code/)

**Title:** 

I'm using the standard OpenCode provider and have added $10 to my account balance. I don't have an OpenCode Go subscription.

I'm trying to use these models through the standard provider:

* `opencode/deepseek-v4-flash` — HTTP 404
* `opencode/kimi-k2.7-code` — HTTP 410
* `opencode/glm-5.3` — works as expected

For DeepSeek V4 Flash, the Console reports:

* Error: `inference_failed`
* HTTP status: `404`
* Endpoint: `/inference/openai/v1/chat/completions`
* Protocol: `openai-chat`
* Product: `standard`
* Provider: `OpenCode`

The request fails almost immediately. GLM-5.3 works with the same account, so I'm wondering why these two models fail despite having balance available.

I'm aware that models under `Opencode Go/` require an active OpenCode Go subscription. I'm **not** trying to use those models; I'm selecting the standard `Personal Opencode/` versions.

Are DeepSeek V4 Flash and Kimi K2.7 Code currently unavailable through the standard provider, or could this be an account or routing issue? Has anyone else run into this?

Bash: 

    PS C:\Users\alex> opencode2 service status
    http://127.0.0.1:49374
    PS C:\Users\alex> opencode2 api get /api/health
    HTTP 404 Not Found
    PS C:\Users\alex> opencode2 service restart
    http://127.0.0.1:49374
    PS C:\Users\alexa> opencode2 api get /api/health
    HTTP 404 Not Found

Logs:

    level=INFO run=83b82f94 message="Sent HTTP response" http.span=2 role=server http.method=GET http.url=/api/session/<id_session>/permission http.status=404

    message="Sent HTTP response" http.span=2 role=server http.method=GET http.url=/api/session/<same id_session>/form http.status=404

    ...
    level=ERROR run=83b82f94 message="Failed to drain Session" cause="AI.Error: Upstream request failed: Endpoint is unavailable. ..."

**Comentarios:**

- **u/deafpigeon39** (↑1, 2026-10-10 19:17): Github.com/tbosancheros39/opencode-thinking-fix
- **u/xapep** (↑2, 2026-10-11 06:33): I run a small EU-hosted inference API, so I read these errors from the provider side. A 404 on one model while another works on the same balance is almost never a billing problem: the model id is not routed to your account or product tier. A 410 means the model was removed from that endpoint entirely. Neither goes away by adding credit.  
      
    What fixes it: check the exact model list the client exposes for your tier and compare ids. If DeepSeek V4 Flash or Kimi is not on it, point opencode at an OpenAI-compatible endpoint that serves those models. That is the whole point of the BYO-provider config: your tooling stays identical, only the base URL changes.  
      
    That is also what we do at Entrim: GLM 5.3 Flash, DeepSeek V4 Flash and V4.1 Flash, Qwen 3.8 27B, one OpenAI-compatible endpoint, EU-hosted, no plan, per token. The catalog is explicit, so you know before you commit whether the model you want is served.

---

## Melhores modelos para design e programação
**u/Any-Solution9478** · 2026-10-10 18:47 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2mtlw/melhores_modelos_para_design_e_programação/)

Quero modelos mais baratos e úteis para programação frontEnd e geração de código legal! Sugestões? Opencode go, 10 dol

**Comentarios:**

- **u/Extension-String1599** (↑1, 2026-10-10 20:36): Los ultimos modelos son buenos como MiniMax  M3 o deepseek pro pero creo que el tema de diseño sería bueno usar una skill para guiar el llm como taste-skill

---

## New to opencode
**u/Mammoth_Pineapple_47** · 2026-10-10 17:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2lnu2/new_to_opencode/)

[removed]

---

## Request for More Free Models
**u/Valuable-Mirror-448** · 2026-10-10 17:46 UTC · ↑1 · 3 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2ld8y/request_for_more_free_models/)

It would be great to see OpenCode explore and add more free models from different providers, especially capable coding and agentic models. More variety would give users better options to experiment, build projects, and use OpenCode without needing paid API access.

**Comentarios:**

- **u/Ariquitaun** (↑19, 2026-10-10 17:48): How about you pay for the subscription instead of taking the piss?
  - **u/Valuable-Mirror-448** (↑-10, 2026-10-10 17:52): Using a free tier that a provider deliberately offers isn't “taking the piss.” Free access is a business decision made by the provider, not a personal favor you're demanding from them. If they decide the economics no longer work, they're free to change the terms. And I'm equally free to criticize that decision or switch to a competitor. Nobody owes me unlimited inference, but I don't owe a company a subscription either.
    - **u/reybrujo** (↑6, 2026-10-10 18:01): Well, it's clear you don't own a company. The model is show you just enough to know what you could do with the subscription without paying for it. If you were to build software for clients you would find any subscription (OpenCode $10, or Claude $20, or whichever you choose) a good proposition to earn money for such a low investment.
    - **u/WisdomSky** (↑0, 2026-10-10 19:45): STFU freeloading parasite.
        
        Asking for free models like they can just download it and run it on a pc...  
        have you tried running 500b+ parameter models on your pc? No?  
        how about 27b+ models? probably also no.  
        Because we all know that these 27b+ model alone, it needs at least 2 damn GPUs with 16GB VRAM. and the resource bandwidth for that is just enough for 1 user.  
        Running a model for large-scale userbase is a different matter that requires money.
        
        And here you are asking for more free shits rather than start paying.
      - **u/Horcrux002** (↑0, 2026-10-10 19:50): Do you think open code give the free access from their own pockets ?  
          They themselves get startup credits for the big cloud providers to run these models  
          Or have collaboration with the providers which is also free.   
          As a consumer we have right to ask for free access to things which they selves get for free 
          
          But I guess real parasites don’t know the reality and only knows to dump shit load of slop jargon to sound knowledgeable.
- **u/RepulsiveRaisin7** (↑14, 2026-10-10 17:49): What is the incentive for Opencode? There isn't one, not gonna happen
  - **u/Valuable-Mirror-448** (↑-14, 2026-10-10 17:52): The incentive doesn't necessarily have to be immediate revenue. Retaining users, attracting developers, increasing adoption, and keeping OpenCode competitive are all potential incentives. If users leave for alternatives that offer better free inference, that's a competitive cost too. Whether those benefits outweigh the costs is a separate question, but saying there's *no incentive* at all ignores the potential upside. And obviously, the provider's willingness to keep the model available is a separate constraint.
    - **u/RepulsiveRaisin7** (↑9, 2026-10-10 18:00): Opencode is first and foremost an agent harness that works with many different inference providers. Serious users utilize paid providers or their own hardware, so I don't think the free offering matters all that much. It exists to make it easier for new users to get started, but I wouldn't expend state of the art models for free, those cost money. They are barely profitable as is.
- **u/my_new_accoun1** (↑13, 2026-10-10 17:58): Bruv they release a new free model like every hour 😭
- **u/thomas29needles** (↑3, 2026-10-10 18:04): Every day you have several free models to choose from in Zen. Some come and go, some have been there for quite some time already. Nobody is going to provide you real professional models capable of fullstack development for free.
  - **u/Valuable-Mirror-448** (↑1, 2026-10-11 13:36): The models are "benchmaxxed" also I dont want that im asking it to help the younger audience I myself  can say that opencode is very good due to the  models they let you use.
- **u/theChaosBeast** (↑3, 2026-10-10 18:11): Are you the same guy who started a petition that hey have to bring back free exo models?
- **u/FireGM** (↑5, 2026-10-10 18:25): # Request for More Money
    
    It would be great to see clients explore and add more money to different providers, especially capable coding and agentic models. More money would give users better options to experiment, build projects, and use OpenCode without needing free API access.
- **u/2finoz** (↑1, 2026-10-10 18:26): Loz pero solo cuesta 10 el go no veo que realizar un listado hamplio de modelos no es factible para ellos usar cómputo para free cuando tiene usuario de pago que ameritan prioridades
- **u/1818TusculumSt** (↑2, 2026-10-10 18:32): Stop being poor. Buy a sub.
- **u/EnoughConcentrate897** (↑2, 2026-10-10 18:33): It's not up to them. They get provided free inference from the providers themselves I'm pretty sure, and they break even on go subscriptions
- **u/2finoz** (↑2, 2026-10-10 18:40): Los modelos que te dan gratis son buenos y no te cuesta nada. Para ellos eso es una factura bien grande. Ellos deberían hacer como command code que si no tienen una sub no deberían usar ni lo gratis. El cómputo y la energía está muy cara.y por tener eso modelos gratis no dan más a lo que si pagan.
- **u/IAmFitzRoy** (↑1, 2026-10-10 18:54): This is pure ignorance, OpenCode are not the one offering the free models, those are the providers.

---

## What are the usage limits of the free models?
**u/Available-Space6350** · 2026-10-10 17:29 UTC · ↑8 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2kzah/what_are_the_usage_limits_of_the_free_models/)

For example Muse Spark 1.3 Free , whats the usage limit and how often does it refresh?

**Comentarios:**

- **u/mozkohor** (↑6, 2026-10-10 17:34): idk but spark 1.3 feels infinite  
    i had sessions go into 10s of millions of tokens
  - **u/Available-Space6350** (↑2, 2026-10-10 17:36): Damn, thats nice
    - **u/Chemical-Cheetah6163** (↑2, 2026-10-10 17:37): i think it was like 40 million a few weeks ago
      - **u/AmbitiousAthlete7324** (↑1, 2026-10-11 19:43): i have ised 13B in last 10 days
- **u/Pristine-Tonight-411** (↑3, 2026-10-10 17:37): Seems to reset every 24h and "feels" almost infinite, although I did run into "Usage exceeded" responses occasionally. I only use Muse Spark as orchestrator now so it's definitely almost "forever".
- **u/eugene_429** (↑3, 2026-10-10 17:38): i don't think there is a straightforward  way of knowing but the last time i used the free models the limits are really high and good for simple stuff
- **u/MindlessBranch3557** (↑1, 2026-10-10 18:02): let me know too
- **u/Obvious_Yoghurt1472** (↑3, 2026-10-10 18:52): En promedio de salida:
    
    \- 650 mensajes \*  
    \- 2M  de tokens
    
    \* Una misma respuesta del modelo puede tener varios mensajes
- **u/ERROR_FOX_PG** (↑2, 2026-10-10 20:02): Por mi parte, hay una hora específica a la que se reinicia (7 P.M hora colombia), trabajar y gastarse todo lo posible antes de esa hora es realmente eficiente
- **u/Robonotes1760** (↑2, 2026-10-10 20:18): I believe that it resets at midnight Zulu time.
- **u/Dangerous_Following4** (↑1, 2026-10-10 21:57): not sure
- **u/[deleted]** (↑0, 2026-10-11 01:29): [removed]
- **u/daniel-sousa-me** (↑5, 2026-10-11 03:36): I've done some analysis of muse spark and have figured out most of it! 
    
    The first thing to know is that it's based on the number of requests and not the number of tokens. A request is essentially a turn, so every tool call counts as an extra request 
    
    The usage is bound by IP alone. I've changed the network interface to use a different IP on the same machine, with the same history and I get new usage for the day
    
    Daily usage resets at midnight UTC. For the first day you get 1000 reqs. The next part I'm unsure about the details, but basically as you use the same IP, every day it gets fewer requests. First it drops to 750 than to 500. It stays on 500 for a while, then I've seen it drop to 333. I think these drops on IP reqs happen only when you hit the limit the previous day, but I'm less sure of this
    
    People behind CGNAT usually get a fresh ipv4 every time the router reconnects, so they easily get unlimited usage (I've played with this using my mobile connection, which is behind CGNAT. Going into airplane mode and back gets me a fresh IP with 1000 new requests)
    
    I have a current workload where I can send a request of up to 1MB, with no tool calls, so muse spark answers in a single turn with a lot of output tokens (I haven't actually counted the tokens) and I've done about 200 of these in a day from the same IP without hitting the limit (I haven't tried to hit the limit to test it. It was a legitimate workload I had that for well this pattern)
  - **u/Cute_Oven_5767** (↑1, 2026-10-11 03:41): Thanks!
  - **u/Icy-Examination-9512** (↑1, 2026-10-11 08:55): This helped me a lot thx
- **u/GoonigUnc** (↑1, 2026-10-11 06:58): i use space bunny and it easily goes to maybe 60-90m with cache reads every day
- **u/Sadlyf68** (↑1, 2026-10-11 08:18): 50-60M daily

---

## will i get banned from claude if i used my 200$ plan in opencode
**u/Friendly-Guard-2395** · 2026-10-10 17:25 UTC · ↑2 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2kvwp/will_i_get_banned_from_claude_if_i_used_my_200/)

**Comentarios:**

- **u/Good_Resolution4115** (↑1, 2026-10-10 17:26): Va en contra de los Términos y Condiciones hacer eso así que lo mejor es que no lo sigas haciendo, si no te la banean tienes suerte
- **u/NinjaAlaska** (↑0, 2026-10-10 17:28): against TOS. but i do it some times.  
     but there are better harness. try OMP or deep seek harness. absolute goat  nothing against opencode any more ..  
    i benchmarked so letting u know. and personally moved too.
  - **u/Friendly-Guard-2395** (↑2, 2026-10-10 17:29): it ain't against tos to use my claude sub in ds harness?
    - **u/NinjaAlaska** (↑1, 2026-10-10 17:30): ye they want u to use claude code only.  
        its all about your claude acc age TBH. i was lucky no issue.
    - **u/TechGearWhips** (↑1, 2026-10-11 11:41): Yes thats why Claude doesn't get a dime from me.
    - **u/JadedHead21** (↑1, 2026-10-11 14:07): It's against Anthropic's ToS to use a Claude subscription with anything other than Anthropic's software, and that includes piping your prompts from OpenCode, Deekseek's harness, etc, into Claude Code CLI.
        
        If you want to anything like that then you need to pay for API pricing
  - **u/TechGearWhips** (↑1, 2026-10-10 22:52): Pi harness when you tweak it to your own workflow is the 🐐
    - **u/NinjaAlaska** (↑1, 2026-10-11 06:26): PI cant handle complex tasks. as it lacks sub agents. i tried and benchmarked it too. its good not good enough. (for my tasks not hating)
      - **u/IgnisDa** (↑1, 2026-10-11 06:45): What do you use then?
      - **u/TechGearWhips** (↑1, 2026-10-11 11:39): Did you not dee the part ehrr I said: tweak it to your workflow? I spawn subagents just fine.
        - **u/NinjaAlaska** (↑2, 2026-10-11 12:25): i know that doesn't make it good for my tasks still. my tasks are a bit complex more complex than you imagine. 100k lines is nothing my code base is 42GB alone.. insane amounts of codes too.. lost count by now..   
            that doesn't make it bad neither good harness for my tasks.  
            OMP and deep seek good at large. even claude code with opus v5.5 fails some times (not always)
            
            i guess diff user diff experiences all good in end as long as open source :D
          - **u/TechGearWhips** (↑1, 2026-10-11 12:30): That’s only a skill issue. My setup is much better than omp. The codebase size does not matter. Graphify integration. Codex is open source. Claude is not open sourced but was once leaked. I copied how their prompts, tools, and compaction worked and optimized it further. Created my own extensions for the features I want (that’s the biggest pro of pi). Subagents all coordinate through herdr.   
              Again, once you TWEAK it to your own workflow it is goated. Omp and the other harnesses are built out for the general public but never for your own personal work flow.
            - **u/NinjaAlaska** (↑1, 2026-10-11 12:36): omp i disliked a lot too in past . now days its good has improved. before open code was better for me now its not. wierd stuff but i customized other harness not these 2.  things keep changing with AI models and time i guess. 
                
                  
                in my last week benchmarks deep seek and omp out performs my tasks more than other cli.. i customize all of them too offcourse..
                
                things just keeps changing. i am making a custom modded android OS after all. one setup will never work. i have to keep jumping from harness to other too some time one reaches limit. wierd.. 
                
                any ways Graphify i thought abt it but never tried. doing good for you?  
                some one even made a graph based harness [https://empryo.com/](https://empryo.com/) (was bad than omp and deepseek still )
                
                lot of stuff. would like to try ur setup if u can share some info.. as of now found peace with claude code, kimi cli (brute force swarms), OMP, and deep seek harness.
              - **u/TechGearWhips** (↑1, 2026-10-11 12:42): Just think about it. All OMP did was take regular pi and add on sane defaults that they think is good for the general public. Basically pi with batteries included. 
                  
                  But all I did was do the same exact thing for myself and tailor it to my own workflow. If you are a tinkerer you should do that. Because nothing will work batter for you than what you make for yourself.  
                  
                  Start with base pi and add stuff that you need as you go. You can even copy some extensions from OMP and leave out the rest of if the bloat
  - **u/Miserable_Recipe_522** (↑1, 2026-10-11 06:50): Upvote for this, proven that claude is still working fine and I used it to orchestrate deepseeks or even a**igra**ty inside omp for subagents and review their works, since I need to flush the limit
- **u/validsyntax1210** (↑-4, 2026-10-10 17:51): Why even do it ? There harnest seems better to me no?
- **u/x-communica** (↑-3, 2026-10-10 18:12): But why?
- **u/Time-Toe-1276** (↑-2, 2026-10-10 18:24): no seriously, why though?
    
    claude code is a great harnes yk. personally, I woul use codex after claude code. like if i were you, there would be no reason for me to use anything else besides CC.
    
    and also you probably not do this. its fine with OpenAI models, but Anthropic dont want you using ur subscription with other apps
  - **u/nab0y4enko** (↑4, 2026-10-10 19:19): For multi-agent work. For example: Plan by Opus 5.5, implementation using local agents or Luna, final review by Codex—just an example.
    - **u/Nexism** (↑1, 2026-10-10 23:37): Orca?
      - **u/Friendly-Guard-2395** (↑1, 2026-10-11 07:32): tried orca and i hated every second of it
- **u/torrso** (↑0, 2026-10-10 19:20): Possibly. You could try using it in jcode. It does all kinds of crazy stuff to act like claude code. System prompt says "you're claude", the tools get renamed to the same as claude's and it sends all kinds of extra claude headers and pings some undocumented api endpoint.  I guess someole could (unless already done) do that for opencode.
    
    In any case, Claude Code is better than OC so maybe just use it.
- **u/ESnyder9** (↑6, 2026-10-10 19:39): you can use anthropic's agents sdk in third party applications
  - **u/TheVoyant** (↑0, 2026-10-10 19:41): \^This, using the CLI/SDK is the "safe" way.  
      And chances are Anthro is gonna be the ban heavy Ai, they look to be playing up to that sorta market. If you want to keep using Claude, best bet is to play by their rules. As history shows companies that take that sorta position often become "ban happy"
  - **u/Amarsir** (↑3, 2026-10-10 22:05): [https://github.com/openchamber/opencode-claude](https://github.com/openchamber/opencode-claude)
      
      Although it's not the most verbose, [this ](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)clarifies 
      
      >You can still use the Claude Agent SDK, `claude -p`, and third-party apps with your subscription limits.
- **u/wtfbabez** (↑2, 2026-10-10 22:55): I have used claude sub in codex, pi, deepseek harness for the past 3 months without any problem
  - **u/Ok-Relative-6041** (↑2, 2026-10-11 13:52): how?? Im interested in pi and deepseek
    - **u/wtfbabez** (↑3, 2026-10-11 14:14): Both pi and deepseek have plugin for claude oauth. But I would say go with setting up cliapiproxy as your central oauth, since they have a big community with some cloaking features that would in theory make it safer to use claude oauth in other harness.
- **u/Global-Eye-7326** (↑0, 2026-10-11 02:56): Anthropic's $200/month subscription is not worth it.
    
    I be vibe coding on GLM-5.3/Flash, KimiK3 and the Nemotron models full-time and paying zero.
  - **u/daniel-sousa-me** (↑2, 2026-10-11 03:40): With Opus 5.5 and Haiku 5.5 I'm back on the $100 sub. It's absolutely amazing 
      
      I still send some work to opencode free models, but they're at another level
      
      How do you get GLM-5.3 Flash and K3 for free? I've considered opencode go to access those models, because they're quite nice, but the limits seem too low to be worth what it costs
    - **u/Global-Eye-7326** (↑1, 2026-10-11 14:54): I can't disclose the gravy train on Reddit, but I will tell you that it's literally in the list of vendors in OpenCode where you can add an API key.
  - **u/[deleted]** (↑1, 2026-10-11 06:52): [removed]
  - **u/Friendly-Guard-2395** (↑0, 2026-10-11 07:33): i have an oc go sub with my claude sub
    - **u/dangb2** (↑1, 2026-10-11 09:43): How?
    - **u/Global-Eye-7326** (↑1, 2026-10-11 14:53): I cancelled Go because I kept hitting the rate limits too fast. As much as I wanna support OpenCode, the Go subscription just wasn't worth it. I'd burn through the monthly limits in two weeks!
      - **u/Friendly-Guard-2395** (↑1, 2026-10-11 16:58): it's been nice lately with ds 4.1 flash u get 60$ usage
  - **u/[deleted]** (↑1, 2026-10-11 07:34): [removed]
  - **u/multyfora** (↑1, 2026-10-11 08:52): just use DeepSeek v4.1
    - **u/Global-Eye-7326** (↑1, 2026-10-11 14:55): I love DeepSeek! But...they've been retired by the vendor that I use.
  - **u/JaMoLpE88** (↑1, 2026-10-11 09:31): How?
    - **u/Global-Eye-7326** (↑1, 2026-10-11 14:56): It's in the list of vendors in OpenCode where I can add the API key. I can't be giving out the golden goose on Reddit otherwise everyone here is gonna do it 🤣
      - **u/[deleted]** (↑1, 2026-10-11 15:33): [removed]
      - **u/[deleted]** (↑1, 2026-10-11 15:47): [removed]
- **u/mmeister86** (↑1, 2026-10-11 06:43): For now it should be fine, as they stalled their decision to ban third party use of the subscription iirc. But could change anytime
- **u/Standard_Wish** (↑1, 2026-10-11 13:15): Seems like they're fine with it if I'm reading this correctly. Just don't spoof anything. 
    
    Using SDK or handing off to Claude CLI looks legit. 
    
    They recently offered additional API credits on max plans (over and above code sub consumption) https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers. You have to claim them though. 
    
    Gotta use those API credits somewhere.
- **u/Visible-Worry-6220** (↑1, 2026-10-11 13:16): I think a lot of people have decent success with using cliproxyapi + claude oauth and hooking it into opencode or whatever harness you prefer to use.
- **u/Zealousideal_Cry_441** (↑1, 2026-10-11 15:42): Use Claude CLI for Claude. No issues if you do that. Your harness can make a call to the Claude cli. I do the same with antigravity.
- **u/jelloeater85** (↑1, 2026-10-11 22:39): https://github.com/askalf/dario + https://github.com/decolua/9router works amazing w/ OpenCode + Goose
    
    Pair it w/ https://github.com/steipete/CodexBar ... H E A V E N

---

## Petition to Restore Exo-Free in OpenCode
**u/[deleted]** · 2026-10-10 16:04 UTC · ↑0 · 13 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2ixpz/petition_to_restore_exofree_in_opencode/)

[deleted]

**Comentarios:**

- **u/DertekAn** (↑1, 2026-10-10 16:11): Very bad router
  - **u/Valuable-Mirror-448** (↑1, 2026-10-10 17:40): Dude it's good just was very occupied.
- **u/Worried_Corner_8541** (↑2, 2026-10-10 16:21): Only indians think they deserve free unlimited inference
  - **u/[deleted]** (↑1, 2026-10-10 17:40): [removed]
  - **u/Valuable-Mirror-448** (↑1, 2026-10-10 17:51): When your argument about AI economics is so weak that you have to bring nationality into it, you've already lost the argument. Nobody said inference was free to provide. We're discussing whether free access can be a viable business strategy. Try addressing that instead.  
      (Also im not indian)
- **u/ManagementNo4948** (↑3, 2026-10-10 16:30): nvidia nemotron is free. Free access is provided by model developers to get user data, test and improve the model. nobody is here to bear the cost of inference just to provide the models for free.
  - **u/Valuable-Mirror-448** (↑1, 2026-10-10 17:42): Nemotron is really outdated now and models training on coding you do doesnt mean itll produce the same code it did for you it just improves the model in that topic.  Doesn't mean your giving away your projects.
- **u/theChaosBeast** (↑1, 2026-10-10 16:46): And who is going to pay for it?
  - **u/Valuable-Mirror-448** (↑1, 2026-10-10 17:40): There are investors.
    - **u/theChaosBeast** (↑1, 2026-10-10 17:41): And what's the ROI for a free model in the perspective of an investor?
      - **u/Valuable-Mirror-448** (↑1, 2026-10-10 17:43): A free model doesn't necessarily generate revenue directly, but it can still generate a positive ROI by attracting customers, building an ecosystem, or increasing the company's long-term value.
        - **u/theChaosBeast** (↑1, 2026-10-10 17:44): You have used it for free and are still not willing to switch to the paid version. So how is it generating a positive ROI?
          - **u/Valuable-Mirror-448** (↑1, 2026-10-10 17:48): You're assuming that every free user needs to convert into a paying customer for the model to generate ROI. That's not necessarily true. Free models can generate value through developer adoption, ecosystem growth, brand recognition, market share, and indirect revenue from APIs or enterprise deals. Free users also help expose weaknesses, test real-world use cases, and spread adoption.
              
              That said, you're right about one thing: if a free user generates zero indirect value, never converts, and costs more to serve than they contribute, that user is a net cost. The actual ROI depends on the provider's overall business model, marginal serving costs, and the value generated across the entire user base—not whether one individual free user upgrades.
- **u/thomas29needles** (↑2, 2026-10-10 16:49): Stop simping for a damn model. And it's not opencode decision anyway - the actual provider decides how long the stealth model will be live. Right now you still have Muse 1.3 for free with really decent capabilities.
  - **u/Valuable-Mirror-448** (↑1, 2026-10-10 17:50): The second half of your comment was a perfectly reasonable point. The first half just makes it look like you needed an insult because you had nothing substantive to add.
      
      And yes, I'm aware the provider controls the model's availability. That's literally why I'm criticizing the decision to discontinue access, not pretending OpenCode personally owns the model.
      
      You managed to make a valid argument and undermine it with the first sentence. Impressive.

---

## Is There Seriously Still No Way To Delete Projects???
**u/The_Crimson_Hawk** · 2026-10-10 15:01 UTC · ↑6 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2hexf/is_there_seriously_still_no_way_to_delete_projects/)

Opencode Desktop duplicated all my projects for some reason, so naturally I tried to delete them. That is, if I could delete them. Only mention i can find is this [https://github.com/anomalyco/opencode/issues/28030](https://github.com/anomalyco/opencode/issues/28030) which is closed... as not planned???

Is there any app that is similar to the google's antigravity 2.0 or chatgpt app in codex mode that allows you to bring your own api endpoint and key, but actually considers the basic use case of the user?

**Comentarios:**

- **u/LCGaming11** (↑1, 2026-10-10 15:25): ZCode or Deepseek Harness
- **u/TheVoyant** (↑1, 2026-10-10 19:43): You can just make a fork of open code to do it, thats the beauty of open source, you don't like something, make a version that doesn't have it.
- **u/__Davos__** (↑1, 2026-10-11 14:25): There is, go to settings -> Projects -> three dots and click on close.
    
    Though it's very confusing since you'd think close means close the menu not remove the project.
  - **u/The_Crimson_Hawk** (↑1, 2026-10-11 14:27): ohhhhhhh
      
      well that is... a rather creative way to name it to say the least

---

## I've recreated Google Research SKILL.STATE memory architecture as opencode CLI plugin - a runtime architecture that replaces conversational history with an explicit execution state.
**u/megablue** · 2026-10-10 14:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2gsde/ive_recreated_google_research_skillstate_memory/)

**Comentarios:**

- **u/kantorcodes1** (↑2, 2026-10-10 19:19): Interesting take on the context problem; explicit state over append-only history is the right instinct. One question on integrity: is Σ derived from the tool calls that actually executed, or from what the model reports it did? If an agent claims "step 3 done" in a state update but the underlying call failed or never ran, does the plugin reconcile against the execution log, or does the drift just accumulate in Σ?
  - **u/megablue** (↑1, 2026-10-11 01:43): No reconciliation. Drift accumulates silently.
      
      For your example, a call that failed or never ran, with "step 3 done" still written, the claim is stored, and every later request that carries it carries the model's own word. The counter-evidence isn't gone: the failed call and its result still sit in the durable transcript, and on the wire until that turn collapses. Nothing cross-reads it for verification, though. From the model's side over the wire, Σ is the record. (The sole derived exception: files/working/step seeded from call arguments, "attempts, not outcomes", and only into keys the model hasn't set.)
      
      That's why any reconciler is heuristic by nature: an exit code isn't intent, and "done" isn't a mechanical predicate. The cheap contradictions are detectable, the semantic ones are not.
    - **u/kantorcodes1** (↑1, 2026-10-11 20:21): That's the honest version - a reconciler can't judge intent, but it doesn't have to if the execution record is signed at dispatch rather than reconstructed after. Adjacent from the side I work on: HOL Guard (open-source - github.com/hashgraph-online/hol-guard) already has OpenCode adapters - pretool gating plus a signed receipt per gated action binding the call's arguments at dispatch. A Sigma check against receipts would separate "model claimed" from "actually gated" without the semantic problem - the receipt is mechanical fact, not the model's word.
        
        I work on the Guard side, so that's a disclosed suggestion. Worth a look?
- **u/ufos-dude-1** (↑2, 2026-10-10 22:28): nice one! :D
- **u/Ctbhatia** (↑1, 2026-10-11 13:41): explicit execution state over append-only history is the right instinct, the failure mode is when the state drifts from what the tools actually did. keep it derived from the tool results, not a summary.

---

## Anyone else getting huge uploads with OpenChamber
**u/TropicMike** · 2026-10-10 14:28 UTC · ↑18 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2gob1/anyone_else_getting_huge_uploads_with_openchamber/)

I installed OC on a Linux machine yesterday.  My firewall noted a \~3MB upload to [relay.openchamber.dev](http://relay.openchamber.dev) shortly after.  I figured, "hmm, ok, new install, maybe just diagnostic data or something."

Overnight, an upload of 1.86GB was made while I was sleeping.

Is anyone else seeing these uploads?  That seems excessively large for basically text communication while I'm sleeping -- and I've only just set OC up - I haven't uploaded a single jpg or anything -- pretty much just "hello" to the LLM testing...

**Comentarios:**

- **u/pigletmonster** (↑0, 2026-10-10 16:40): Ask opencode to investigate.
  - **u/TropicMike** (↑1, 2026-10-10 16:55): I did point it at the repo, and this is what it came-up with (GLM53-flash):
      
        
      \-----
      
      Found it. The code has a dictation path with no data ceiling, no duration cap, and no silence gate on the client, plus full replay on every reconnect. Here's the analysis.
      
      The mechanism
      
      When a user taps the mic in the composer, the client captures continuously and streams PCM in \~1s base64 chunks to the OpenChamber server:
      
      \- packages/ui/src/lib/dictation/use-dictation-audio-source.ts:205-227 — every 4096-sample block is resampled to 16 kHz and enqueued. The RMS level is computed but only for the waveform; silence is streamed exactly like speech.
      
      \- packages/ui/src/hooks/useDictation.ts — recording ends only on confirm, cancel, or unmount. There is no maximum duration, no idle timeout, no data-volume cap anywhere. The duration counter just counts up.
      
      \- packages/ui/src/lib/dictation/dictation-stream-sender.ts:40,91-108 — segments accumulate in an unbounded string\[\] in the renderer until the dictation completes.
      
      The wire rate is 16 kHz × 2 bytes × 4/3 base64 ≈ 43 KB/s, about 155 MB per hour. A recording left open from early evening to morning is 12 to 14 hours, which lands almost exactly on 2 GB.
      
      Two amplifiers
      
      First, full replay on every reconnect. useDictation.ts:154-166 calls restartStream() whenever the WS flips to connected while recording, and resetStreamForReplay() sets sendSeq = 0 (dictation-stream-sender.ts:82-89), so flush() re-sends every buffered segment from the beginning. Overnight connection churn (proxy drops, sleep/wake, tunnel reconnects) re-uploads the whole accumulated session each time. A 3 hour recording replayed 5 times is \~2.3 GB on its own. The flush loop drains 128 chunks per event-loop turn, so a replay of hours of audio completes in seconds.
      
      Second, retry. A failed dictation retains all segments (useDictation.ts:196-206) and retryFailedDictation replays everything again. A renderer left sitting on a failed overlay overnight is also holding hundreds of MB of strings in memory.
      
      Server-side nuance: packages/web/server/lib/dictation/stream-manager.js clears silence-only segments instead of committing them, so a quiet room pushes little to the STT provider. But the client→server stream itself is never silence-gated.
      
      What egress the 2 GB actually leaves through
      
      This is the part that determines whether the report is explained by dictation alone:
      
      \- Server remote (relay, SSH tunnel, hosted web): the client→server WS upload is WAN traffic. \~155 MB/h, 2 GB in a 13 hour night. Fits exactly.
      
      \- Server local desktop with a remote STT base URL (custom OpenAI-compatible endpoint): egress is the committed speech segments going to the provider, roughly the same volume if there was real audio near the mic.
      
      \- Server local desktop with a local Whisper model and only local UI use: dictation is loopback and can't be the 2 GB. In that case the next candidate is a git push with LFS objects overnight (packages/web/server/lib/git/network-operations.js:1360-1443, streams live by size of actual LFS content), then attachment data-URL re-uploads through the message queue.
      
      What I'd change
      
      Cap the total buffered audio per dictation and auto-finalize past it; it's the missing invariant, the server has per-segment caps but the client session has none. Don't replay from seq 0: the server can ack the highest contiguous seq it received and resume there, since chunks are already addressed by seq. And drop or compress silence client-side, which makes the wire cost roughly proportional to when someone is actually talking.
      
      To confirm on the affected machine, check the OpenChamber server log for dictation stream starts and STT commits timestamped during the night, and whether a recording was still in recording status when someone noticed.
      
      \----
      
        
      However, I moved the investgation to the machine actually running OC, and apparently there's no logging for the voice transcription, so it could not be verified.
      
      Also, the Linux machine is a VM, so doesn't even have a mic, and I didn't even realize you could do voice in OC, so the likelihood that I clicked the microphone is extremely small.
      
      My Windows and Mac both had an upload to the relay of \~2MB, which is more what I'd expect for linking machines/etc.
- **u/ZHName** (↑-1, 2026-10-10 20:19): Here's why I passed on it:
    
    The developers. A cluttered interface shouts carelessness in its workings, suggesting an ulterior motive. You just confirmed this for me, guess go by your gut and if you can't understand a repo, interrogate it.
- **u/Senior_Tourist_4260** (↑1, 2026-10-11 11:43): Is there anyone who can analyze this in more detail and draw a definitive conclusion? I was thinking of switching to OpenChamber soon, but this issue is preventing me. If there's even the slightest possibility of something like this happening, I'm really not considering switching.
- **u/TropicMike** (↑2, 2026-10-11 14:06): One other odd thing - when I installed it on my Mac, it wanted permissions for access files on the network.  Perhaps that is expected as part of normal operation - it's hard to say since Windows doesn't have the same permissions granularity prompts.
    
    Part of me thinks the large upload may just be a bug in the Linux version because I didn't see either my Windows or Mac install uploading anything more than the initial \~3MB payload right after the initial install and linking.
    
    Who knows.  For now, I've suspended use of OC until we get more consensus from people reviewing the code and/or input from the developer.
- **u/xatey93152** (↑2, 2026-10-11 16:50): Of course something sus about this app. Every hours there's some new spam post praising this app

---

## Mini Linux Kernel Virtual Machine on Veda
**u/vahmoh25** · 2026-10-10 14:14 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2gcc5/mini_linux_kernel_virtual_machine_on_veda/)

---

## Claude Sonnet 5.5
**u/Remarkable-Trash-769** · 2026-10-10 13:55 UTC · ↑0 · 6 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2fwk0/claude_sonnet_55/)

Please add Claude sonnet 5.5... CommandCode give sonnet 5.5 with $20 limit

**Comentarios:**

- **u/honglac3579** (↑2, 2026-10-10 13:58): And it will burn real quick as well
- **u/AlexandraMaryWindsor** (↑7, 2026-10-10 13:59): CommandCode advertisement. Mods ban this guy
  - **u/Remarkable-Trash-769** (↑-3, 2026-10-10 14:01): Opencode is GOAT 
      i love opencode very much ^_^
- **u/alexanderbeatson** (↑5, 2026-10-10 14:33): CommandCode isn’t even ZDR enforced, a scam.
  - **u/Soarin123** (↑1, 2026-10-11 22:12): i guess neither are
- **u/Relative-Document-59** (↑4, 2026-10-10 14:40): Sonnet 5.5 is expensive as fuck, even on low reasoning spends tokens like hell
- **u/[deleted]** (↑1, 2026-10-10 17:16): [removed]

---

## New to opencode
**u/Mammoth_Pineapple_47** · 2026-10-10 11:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2d8dl/new_to_opencode/)

[removed]

---

## AI-BOX
**u/loujJouri** · 2026-10-10 10:13 UTC · ↑4 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2bpfe/aibox/)

I created a shell tool for boxing any AI agent.

**Comentarios:**

- **u/kaliku** (↑9, 2026-10-10 10:22): Congrats. I made fried eggs this morning.
  - **u/niwia** (↑2, 2026-10-10 11:07): How many eggs did you use
    - **u/kaliku** (↑5, 2026-10-10 11:50): A cluster of 4, tensor parallel.
- **u/TheMythicSorcerer** (↑2, 2026-10-11 01:48): Have you heard of containers?

---

## Built a sandbox for opencode to run AI agents in a private, secure and isolated workspace
**u/Antiquete** · 2026-10-10 10:00 UTC · ↑0 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2bi22/built_a_sandbox_for_opencode_to_run_ai_agents_in/)

**Comentarios:**

- **u/[deleted]** (↑0, 2026-10-10 14:05): [removed]

---

## Freebuff
**u/OvercastedFuture** · 2026-10-10 09:53 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2bdsz/freebuff/)

[removed]

---

## What are some of your favorite plugins for Opencode?
**u/[deleted]** · 2026-10-10 09:41 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2b6s3/what_are_some_of_your_favorite_plugins_for/)

[removed]

---

## I made a sandbox for opencode so that I can run any agentic AI anywhere to do anything without worries
**u/[deleted]** · 2026-10-10 09:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2at51/i_made_a_sandbox_for_opencode_so_that_i_can_run/)

[removed]

---

## I made a sandbox for opencode so that I can run any agentic AI anywhere to do anything without worries
**u/[deleted]** · 2026-10-10 09:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2aq2h/i_made_a_sandbox_for_opencode_so_that_i_can_run/)

[removed]

---

## Opencode on iPhone Without App
**u/Professional_Log1367** · 2026-10-10 07:24 UTC · ↑7 · 17 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x290y4/opencode_on_iphone_without_app/)

Is there a way I can access opencode on my iphone without the app. i am already using openchamber to get temperary tunnels but they are just temperary. i want a permanent option, but free tiers don't really have it. What do you guys use?

**Comentarios:**

- **u/Vast_Anxiety3133** (↑2, 2026-10-10 07:37): I have a socket relay via my vps. But you could use tailscale to serve Opencode web
  - **u/gandalfoncoke** (↑2, 2026-10-10 10:30): Yeah I'm using tailscale and it's great. But I must say that opencode phone app and it's desktop app are so rubbish. Terminal is great but web... Wow. Is anyone even working on that?
    - **u/gandalfoncoke** (↑1, 2026-10-11 06:44): After upgrading to v2, it seems a bit of an improvement now actually.
  - **u/Professional_Log1367** (↑1, 2026-10-11 06:03): how does it work? what are the limits?
    - **u/Vast_Anxiety3133** (↑1, 2026-10-11 06:05): I am basically self hosting my own web interface. Ask an agent to serve Opencode web via tailscale. You need to have tailscale installed on all devices as it is a VPN
- **u/stanizzle** (↑1, 2026-10-10 08:21): Why are you not using the official opencode app that is on TestFlight? But to add to that build a Tailscale/Netbird tunnel and use an ssh app of your choice for it to launch e.g opencode or any other service you like
- **u/MunifTanjim** (↑1, 2026-10-10 08:54): Argus https://argus.muniftanjim.dev with ngrok/tailacale/cloudflare-tunnel
    (I'm the dev)
- **u/Tariq9977** (↑2, 2026-10-10 09:09): If you use Tailscale/Netbird, make the OpenCode endpoint stable behind it: `opencode web --port 4096` with `OPENCODE_SERVER_PASSWORD` set. OpenCode otherwise picks a random port, and its docs warn that network access without the password is unsecured.
- **u/Mammoth-Apple410** (↑2, 2026-10-10 09:35): Use openchamber. It connect to opencode and openchamber has a PWA app that works well on iOS
  - **u/maveric0815** (↑1, 2026-10-11 20:40): Totally agree, including push notifications
- **u/[deleted]** (↑1, 2026-10-10 09:57): [removed]
- **u/cuteseal** (↑3, 2026-10-10 12:40): Paseo.sh is what you need - it’s brilliant. No tunnels needed - it connects automatically from iOS/android app.
  - **u/mr_ignatz** (↑0, 2026-10-10 15:26): I think the category is called “agentic development environments.” They orchestrate all of the different agents and provide a bunch of guard rails and features like managing worktrees and tasks and mobile access. I tried a bunch: Paseo, Orchestrator, and settled on Orca. Everyone has different requirements and I’d try one or two for a feature and see which feels the best
  - **u/rubn-g** (↑1, 2026-10-10 17:08): No tunnels needed means public exposure, openchamber can also do that. OP asked about opencode, paseo is a different harness.
      
      As others said, Tailscale is the way to have a secure private connection to openchamber, or paseo too if that’s what you want to use. Personally i like openchamber over paseo, but that’s subjective.
    - **u/OGxGunner** (↑0, 2026-10-11 00:05): You're just an openchamber shill
      - **u/rubn-g** (↑1, 2026-10-11 07:49): I don’t think so, i yried both and made my choice, as i said, it’s subjective, my opinion. I think paseo is a great tool.
    - **u/Professional_Log1367** (↑1, 2026-10-11 06:07): what is paseo? is it just app (computer) to app (iphone)
      - **u/rubn-g** (↑1, 2026-10-11 07:48): It’s another ai harness, quite similar to openchamber

---

## I just build 'save' option for coding agent. when i'm working on new project the biggest struggle for me to save project waht i did so next time i come back later, may be some time, tommarow or 4 day later or even 2 year or 100 year, i wanted to know where we are?
**u/moneytvdaily** · 2026-10-10 06:25 UTC · ↑0 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x281l4/i_just_build_save_option_for_coding_agent_when_im/)

https://preview.redd.it/7jyavd032luh1.png?width=1912&format=png&auto=webp&s=ab072550c52176ae24946e1c42b590dde4b66918

**Comentarios:**

- **u/ConferenceOver8258** (↑1, 2026-10-10 07:13): I usually save it in the project's phase markdown file.
  - **u/moneytvdaily** (↑0, 2026-10-10 10:03): SMAA is boss 🙌
- **u/pungat_** (↑2, 2026-10-10 11:27): link?
  - **u/[deleted]** (↑1, 2026-10-10 15:38): [removed]
- **u/moneytvdaily** (↑1, 2026-10-10 15:40): [SMMA for everyone ](http://github.com/lab1207/smaa)

---

## I made a computer use MCP server for OpenCode (and any other agent), and it supports iPhone Mirroring on Mac
**u/ia77q** · 2026-10-10 02:10 UTC · ↑3 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x23i8a/i_made_a_computer_use_mcp_server_for_opencode_and/)

Hey all, I’ve been working on this for a while and finally made it public. It’s called Computer Use Turbo. It’s an open source MCP server that lets OpenCode (or any agent that supports MCP) operate the actual apps on your computer, like Notes, TextEdit, Finder, Xcode or whatever you have open. The thing that bugged me about most computer use setups is that the agent grabs your screen, moves your mouse, and you basically have to sit there and watch. Also, Claude’s computer use can’t control your iPhone through iPhone Mirroring on Mac, which matters if you’re building iOS apps and want to test on your real iPhone. Codex can do it, so I made this, inspired by it.

It runs on macOS, Windows and Linux

[https://github.com/afaaq-io/ComputerUseTurbo](https://github.com/afaaq-io/ComputerUseTurbo)

---

## Sizce opencode ile çalışma şeklim hatalı/yanlış mı?
**u/CustomerAromatic350** · 2026-10-10 00:34 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x21m2r/sizce_opencode_ile_çalışma_şeklim_hatalıyanlış_mı/)

[removed]

---

## opencode free tier can only be used from within opencode
**u/osama_awad** · 2026-10-10 00:33 UTC · ↑2 · 3 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x21lqk/opencode_free_tier_can_only_be_used_from_within/)

I keep getting this message even after I have deleted the cache directory and did a relogin, I have also updated opencode, ... , generated new api key, still same issue, how to fix this ?

**Comentarios:**

- **u/aldapsiger** (↑0, 2026-10-10 00:41): with another ai agent? try this one [https://github.com/ethanhamilthon/freerouter](https://github.com/ethanhamilthon/freerouter)
- **u/xmsxms** (↑1, 2026-10-10 08:57): It's intentionally blocked and requires matching specific headers and tool shapes. You can use 9router to get around that.
    
    Just realised you seem to be using opencode as the client. It should work ok, make sure everything is up to date.
- **u/pungat_** (↑1, 2026-10-10 11:38): if you use opencode terminal, check [this](https://reddit.com/r/opencode/comments/1wwekvm/how_to_fix_this_error_please_help_me/).
  - **u/osama_awad** (↑1, 2026-10-11 19:59): thank you, this fixed the issue for me

---

## OpenCode Go for a personal non-coding app: permitted API use and web search?
**u/patrona_halil** · 2026-10-09 23:56 UTC · ↑7 · 19 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x20t1j/opencode_go_for_a_personal_noncoding_app/)

I’m evaluating OpenCode Go for a personal, device-local job-search app that interprets documents and returns structured JSON job matches on demand. It would use an honest app identity and stable session header. I haven’t subscribed yet.



The Go documentation describes coding-agent traffic: [https://opencode.ai/docs/go/](https://opencode.ai/docs/go/)



1. Is this non-coding personal-app workload permitted under Go?



2. Does GPT-6 Luna through Go’s Responses API actually support hosted web search with citations?



3. How are those searches charged: shared subscription allowance, separate tool charges, or both?



I’d appreciate current documentation, provider clarification, or first-hand reproducible experience. Technical capability and permitted use are separate questions; I’m trying to verify both before subscribing.

**Comentarios:**

- **u/[deleted]** (↑1, 2026-10-10 00:04): [removed]
- **u/a355231** (↑2, 2026-10-10 00:09): It’s called opencode because that’s its primary use, they won’t ban you for using it another app.
  - **u/RoKy2608** (↑2, 2026-10-10 00:17): I don't think that necessarly answers OP's question, the opencode go sub is mainly focused for coding agents, what they want is more similar to what you would use direct API calls for.
  - **u/patrona_halil** (↑2, 2026-10-10 06:09): What i am asking is; are the apis like the general default apis that you buy from the provider itself or they are specialized for coding usage only? Can I do what i want to do?
    - **u/a355231** (↑1, 2026-10-10 06:26): Yes, it’s just standard API.
- **u/maqifrnswa** (↑6, 2026-10-10 01:19): 1) I use it for non coding work all the time. Data aggregation, web research. There's nothing in the TOS requiring coding work, it's just what it's designed for. 
    
    2) yes, it supports web search and tooling generally. It's up to you harness how you want to do it. Opencode harness comes with free tier exa and one or two others that it essentially rotates through. That's enough for a couple thousand searches a month. If you want more, opencode sells them for one cent each or you can use your own search tokens (or local search like brave or duck duck go). You mentioned hosted, so using the free tier is what you start with then can either pay opencode or pay any search provider you choose.
    
    3) web search is a function of the harness. Opencode, as a pay service, sells web search at 1 cent per search, but if you're just doing a couple hundred or thousands of searches a month, you don't have to pay. opencode as a harness comes with built in searching using free tiers. You also can use local as I mentioned above.
  - **u/patrona_halil** (↑1, 2026-10-10 06:09): What i am asking is; are the apis like the general default apis that you buy from the provider itself or they are specialized for coding usage only? Can I do what i want to do?
    - **u/maqifrnswa** (↑1, 2026-10-10 06:29): Of yeah, they use the standard jinja template as far as i can tell.
- **u/for4f** (↑1, 2026-10-10 06:29): yeah 1) is fine, go is just a provider endpoint, nothing in there saying the work has to be code. i use mine for plenty of non-coding stuff, planning docs, research writeups, whatever. it's your ten bucks of usage, spend it how you want lol
    
    for 2/3, websearch is exa-backed and doesn't need your own key, but it's off by default since it phones home to exa. you have to allow it under permission in opencode.json, and on some versions you need the exa env var set or the tool just doesn't show up in the list. usage-wise it counts against the same allowance, no separate search charge on go as far as i've seen
- **u/povlhp** (↑1, 2026-10-10 06:38): Just use deepseek V4.1 flash on a paid plan. $10 might last forever.
- **u/Ill_Community_8253** (↑1, 2026-10-10 08:25): deepseek v4.1 flash might be a good choice for me
- **u/ollm-tux** (↑1, 2026-10-10 10:22): I dont understand... You dont launch yet command "opencode web" ??? ... before 1 h i ask muse spark free how make some food ... opencode web work with both version v1 & v2 but v2 is more sure (coz have password access)... I put in my yunohost server...and now can access from anywhere with  any browsers
  - **u/patrona_halil** (↑1, 2026-10-10 10:23): What i am asking is; are the apis like the general default apis that you buy from the provider itself or they are specialized for coding usage only? Can I do what i want to do?
    - **u/ollm-tux** (↑1, 2026-10-10 10:30): depend what model you choose for example if you ask about food mimo maybe not good answer or refuse, but muse spark or nemotron i think have good answer for general ask, models is not AGI but is good to try
      - **u/ollm-tux** (↑1, 2026-10-10 10:45): I have started with one free api, then i buy 10$ opencode go same account for... I dont know but iI think is over 50 models wich use as general or coding, what dont work in opencode web is video, just text, docs and image work
- **u/Ashamed_Drag8791** (↑1, 2026-10-10 11:09): 1. as long as you dont sell the app/make money off rotating the account for the app, i see no reason to break ToS.
    2. yes, but you should add skill and hooks to instruct it return as structure json.
    3. combined, no extra charge.
    
    I would suggest you look at request limit of their though [Estimated requests](https://opencode.ai/docs/go/#estimated-requests) if you have intense usage, or directly convert to pay as you go(Zen subscription, add 10$ credit and use for as long and as much as you need, similar to openrouter)
  - **u/patrona_halil** (↑1, 2026-10-10 12:22): What i am asking is; are the apis like the general default apis that you buy from the provider itself or they are specialized for coding usage only? Can I do what i want to do?
    - **u/Ashamed_Drag8791** (↑1, 2026-10-10 13:38): general, yes.
- **u/Ariquitaun** (↑1, 2026-10-10 15:01): They've made some changes recently to their terms of service, you should check.

---

## BigPickle today is crawling.
**u/Robert__Sinclair** · 2026-10-09 23:21 UTC · ↑2 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x2034w/bigpickle_today_is_crawling/)

Usually (last week) it was quite fast, some hiccups every now and then.

Today it takes minutes (more than 10 sometimes) for each step.

:(

**Comentarios:**

- **u/Robert__Sinclair** (↑1, 2026-10-10 01:07): update: it took more than 6 hours to do a quite simple thing that any other free model could do in less than 2 hours. Like this it's **unusable**
  - **u/Druk3483** (↑2, 2026-10-10 13:05): well same here it is taking too long time to process request longcat 2.5 is quite fast rn
- **u/Mr_Lucas2000** (↑1, 2026-10-10 18:58): Slow ass model on it rn ig
  - **u/Robert__Sinclair** (↑1, 2026-10-11 03:52): I don't care if it's slow while thinking or in token/s but it take MINUTES even to start!
    - **u/Mr_Lucas2000** (↑1, 2026-10-11 06:58): It takes it's time

---

## Did anyone tried Hosted Web Search?
**u/Karklik** · 2026-10-09 20:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1wdqa/did_anyone_tried_hosted_web_search/)

[removed]

---

## Anyone else facing this issue??
**u/LoudDragonfruit5522** · 2026-10-09 18:24 UTC · ↑32 · 14 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1sxdq/anyone_else_facing_this_issue/)

**Comentarios:**

- **u/Aggravating-Push-207** (↑2, 2026-10-09 18:27): no
- **u/YoRt3m** (↑3, 2026-10-09 18:33): Exo doesn't work, it's known. for me nemotron also bad. all the rest are fine
- **u/stoner_prime** (↑4, 2026-10-09 18:43): Is there a website for this?
  - **u/migsperez** (↑2, 2026-10-09 22:12): there should be :)
    - **u/GoonigUnc** (↑1, 2026-10-10 00:11): what is it called
- **u/CHR_RH** (↑2, 2026-10-09 19:11): hmmmm that cool whats the CMD/tool for that?
- **u/[deleted]** (↑1, 2026-10-09 19:47): [deleted]
- **u/absurdother** (↑1, 2026-10-09 19:59): Yes. Space bunny oscillates. Longcat is typically always on. The Nemotron ones I've removed from my list as I didn't like them much.
- **u/SuchMajor5267** (↑1, 2026-10-09 21:28): Recently, yes.
- **u/NMiguelCosta-PT** (↑3, 2026-10-09 23:04): Ask one of the models that works like Bunny to check your harness logs for any clues about what's causing the "invalid JSON schema" error with Muse Spark. I suspect one of your enabled plugins or MCPs might be interfering with your prompts. Try running those models with a clean harness, without an agents file or any of the other custom stuff, and see if the errors persist.
- **u/GoonigUnc** (↑1, 2026-10-10 00:11): i dont think im having problem though
- **u/Toluwalashe** (↑1, 2026-10-10 06:49): Very annoying
- **u/Select-Archer6374** (↑0, 2026-10-10 06:50): Ask one of the models that works like Bunny to check your harness logs for any clues about what's causing the "invalid JSON schema" error with Muse Spark. I suspect one of your enabled plugins or MCPs might be interfering with your prompts. Try running those models with a clean harness, without an agents file or any of the other custom stuff, and see if the errors persist.
- **u/AideAgitated2132** (↑0, 2026-10-10 07:44): I've been using Opencode for a long time, and I've subscribed to Opencode-Go several times, but the weekly limit can be used up in a day, which is annoying. I've now switched to FreeBuff.
- **u/akza07** (↑1, 2026-10-10 10:06): Muse spark is fine most of the time. Rest are kinda accurate.

---

## Free Usage Exhausted in Few Mins
**u/Spiritual-Umpire7429** · 2026-10-09 17:27 UTC · ↑7 · 22 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1rfvf/free_usage_exhausted_in_few_mins/)

Hey Everyone,  
From today I observed, opencode's free usage got exhausted in matter of few minutes.  
Note, I have been doing apex level model usage and it lasted 12 hours of continous development. Is it me or everyone?

**Comentarios:**

- **u/Interesting-Movie452** (↑3, 2026-10-09 17:30): im getting Error: Rate limit exceeded. Please try again later. even tho the model is "unlimited"
  - **u/Simple-Departure-794** (↑1, 2026-10-10 00:55): which model is unlimited?
    - **u/Interesting-Movie452** (↑1, 2026-10-10 04:25): step 5 preview it liteary said in the code unlimited [https://github.com/anomalyco/opencode/commit/03146dab56b2c0cec7b6fafd1d8fad2750627256](https://github.com/anomalyco/opencode/commit/03146dab56b2c0cec7b6fafd1d8fad2750627256)
      - **u/thomas29needles** (↑1, 2026-10-10 08:37): Step 5 is unusable. I also keep hitting rate limits and at the first prompt at that.
- **u/roomjosh** (↑2, 2026-10-09 17:39): Seems like the free zen rate limits have changed recently. What I’ve found is some models can be used a lot, (muse spark 🔥 ), while big pickle has a more limited limit. Once big pickle triggers global rate limits, you have a (5-hour?) cool down. 
    
    Take away: avoid big pickle, try again in a few hours
  - **u/Interesting-Movie452** (↑1, 2026-10-09 17:42): im getting Error: Rate limit exceeded. Please try again later. on muse spark too even on step 5 preview and big pickle
    - **u/roomjosh** (↑2, 2026-10-09 17:46): Yeah, if you trigger your account’s global rate limit (which seems to differ from model to model) then it cuts off all models. From my experience, big pickle has seemed to be the model that triggers the global limits most often.  But it’s not a 24h cool down, try again in a few hours
  - **u/Gengur** (↑1, 2026-10-09 23:54): Yeah BigPickle hits limits pretty fast
- **u/Interesting-Movie452** (↑1, 2026-10-09 17:44): try Nemotron 3.5 Lightning Free it has very very high limit
  - **u/thomas29needles** (↑1, 2026-10-10 08:40): And is very very dumb, at least for me.
    - **u/matrix244** (↑2, 2026-10-10 22:21): All nemotron models are pretty dumb. I’d stay away from them imo
- **u/ANDALTUV** (↑3, 2026-10-09 17:47): yup I did a couple of tasks with deepseek pro and reached 10% of usage.. lets see how it goes with deepseek flash
- **u/Fine_Salamander_8691** (↑8, 2026-10-09 17:51): Skill issue /s
- **u/Mysterious-Travel344** (↑5, 2026-10-09 17:52): I use only muse spark these days. Gets the job done adequately, and I never hit the limits.
- **u/Kydanet** (↑4, 2026-10-09 18:09): The minutes-instead-of-hours pattern usually means you tripped the account-wide limit rather than a single model's — consistent with what roomjosh is seeing above.
    
    Regardless of which free model has headroom this week, agent workloads burn free tiers differently than chat does: the clever answers are cheap, the grind eats the budget — re-reading the same file, retrying flaky builds, scanning directories with a big model doing the reading. Two levers that survive rate-limit reshuffles:
    
    1. Run the mechanical loop (read, run, retry) on the cheapest model that can handle it and escalate to the big one only for decisions.
    2. Give the agent persistent state so it stops re-deriving your repo every session.
    
    That second lever is why we run opencode on a permanent Linux box at Kydanet — the machine persists between prompts, so you can point it at whichever free model has headroom today without paying to re-establish context every time.
- **u/[deleted]** (↑1, 2026-10-09 20:03): [removed]
- **u/porib** (↑2, 2026-10-09 20:36): I once got rate limited for 4days
  - **u/eachDayIWakeUp** (↑1, 2026-10-09 21:05): I have noticed different limtis myself too ranging from 2 to 10 hours, but they all happened using different models
- **u/2finoz** (↑1, 2026-10-09 21:34): Si la demanda es mayor para lo de pago los gratis se limitan. Ese cómputos se usa para usuario de pago tienen prioridades
- **u/mith963** (↑0, 2026-10-10 01:47): "I had the exact same issue with limits. You should try Freebuff instead. It's a completely free, ad-supported AI coding agent that gives you access to powerful models without running out of usage so quickly. It's definitely worth switching to."
- **u/AdhesivenessHefty455** (↑1, 2026-10-10 06:15): Yeah for it it shows like free usage limt exceeded so try again in 18 hrs   
    idk whats happening now ?? did they changed the rate limits for opencode zen users   
    im just using the free models like   
    Space Bunny, muse and mimo 2.6 
    
    so what should i do to get my long context window back
- **u/xpenxia** (↑1, 2026-10-11 02:52): Use VPN and use another account for the api key

---

## Pi agent not working with Opencode free models
**u/GeminiBoy91** · 2026-10-09 16:22 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1prl4/pi_agent_not_working_with_opencode_free_models/)

---

## I just automated my very technical six-figure enterprise admin job
**u/SuperClaim4586** · 2026-10-09 16:20 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1ppti/i_just_automated_my_very_technical_sixfigure/)

[removed]

---

## Is it just me, or has OpenCode been kinda slow lately?
**u/CoffeeTea021** · 2026-10-09 15:51 UTC · ↑16 · 13 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1oxpn/is_it_just_me_or_has_opencode_been_kinda_slow/)

I've noticed that OpenCode sometimes takes quite a while to start responding after I send a prompt. It's not happening all the time, but when it does, the delay can be pretty noticeable.

Once the model actually starts thinking, everything is relatively fast and normal. It's just that initial wait before anything happens that feels unusually long.

I don't remember it happening this often before, so I'm wondering if anyone else is experiencing this too.

I'm on v1.18.35.

Is this just happening to me, or is anyone else noticing it as well?

**Comentarios:**

- **u/lincolnthalles** (↑6, 2026-10-09 16:05): It's been terribly slow in the past ~6 hours. Latency is really high.
    
    I'm mainly using OpenCode V2 with Muse Spark, which is a pretty fast model. It timed out a few times already.
  - **u/CoffeeTea021** (↑2, 2026-10-09 16:12): Yeah.. I'm using Muse Spark too. Hopefully it get faster again soon.
    - **u/automax** (↑1, 2026-10-09 20:16): How does that compare with opencode with bigpickle than using opencode v2 with muse spark
- **u/MustafaAdam** (↑3, 2026-10-09 16:06): I  noticed that too. right after the prompt, there is some delay
  - **u/CoffeeTea021** (↑1, 2026-10-09 16:09): Oh, so it's not just me. Thanks for letting me know! Maybe the latency is just unusually high right now.
- **u/Eastern-Honey-943** (↑1, 2026-10-09 16:51): Its me. Hi. I'm the problem, its me. No but in all seriousness, you should try switching models and you may find a faster one. The free ones tend to have lower quality of service.
- **u/awkard_guy_** (↑1, 2026-10-09 17:31): Yea it's been so slow, it worked fine until yesterday
- **u/[deleted]** (↑1, 2026-10-09 17:54): [deleted]
- **u/ProgressionPeak** (↑1, 2026-10-09 18:06): It has been unusable or very slow at various times for me the last couple days. It's not consistently bad, sometimes it works great.
- **u/Empty-Flight8206** (↑1, 2026-10-09 18:15): Yes most prompts do not go through.. ?
- **u/deepit6431** (↑1, 2026-10-09 18:55): Yeah, time to first token is insane. Sometimes the service just goes down, and doesn't work for a bit. It's a bit maddening.
- **u/Awkward_Intern2623** (↑1, 2026-10-09 21:09): Well now, I was wondering, is this just for the free AIs, or does it apply to the rest of them too?
- **u/Acrobatic_Dark_6604** (↑1, 2026-10-10 00:01): Yeah I noticed the same thing
- **u/Traditional_Pie_8262** (↑1, 2026-10-10 02:39): yeah, i've noticed this too. that initial wait is honestly more frustrating than the actual response time, especially when everything runs fine once it finally starts. could be provider-side latency, but glad to know i'm not the only one experiencing it.
- **u/OrrnobMahmud** (↑1, 2026-10-11 08:12): it is slow!

---

## Is there any android app for connecting with opencode2
**u/valentimarco** · 2026-10-09 15:12 UTC · ↑1 · 10 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1ny6l/is_there_any_android_app_for_connecting_with/)

I am testing the V2 and i know there Is a pair mode that display the QR code. I know from a live on Twitch that was used from interns to pair their iPhone to the server...

Before Building It i would like to know if anyone build It

**Comentarios:**

- **u/Mihaylov93** (↑2, 2026-10-09 15:19): I just ssh to the machine with any android terminal emulator like Termux
  - **u/valentimarco** (↑1, 2026-10-09 15:22): Same but my experience Is not great, the tui is gliching and some times i get half screen...
    - **u/ApprehensiveDelay238** (↑1, 2026-10-10 09:15): Try haven from f-droid.
    - **u/Mihaylov93** (↑1, 2026-10-11 05:26): True, some other terminals were completely unusable but with Tmux you get a pretty good state, tui not mangled, but not clickable. I learned the shortcuts with the command key, you have a hint of them in the tui, thats how you can getaround the limitations
- **u/ApprehensiveDelay238** (↑0, 2026-10-09 15:19): I don't think so. But self-hosted openchamber works really great for mobile devices. Also for desktop. Recommend giving that a try.
  - **u/valentimarco** (↑1, 2026-10-09 15:24): I reed the V2 Is in preview but there isnt any ref in the docs, how can i access the preview?
    - **u/WisdomSky** (↑1, 2026-10-09 20:47): why do you even need exactly the v2 binary? openchamber already does what v2 pair mode does. 
        
        aside from openchamber's desktop app, it allows you to access it remotely away from from your desktop as long as the desktop app is running on your desktop (disabled sleep).
        
        the only other thing that you need to be able to access it remotely from internet away from your home is to use cloudflare or tailscale. and open chamber already provides the cloudflare tunnel integration in the settings to make cloudflare tunnel easier to setup.
  - **u/WhatYouGoBy** (↑3, 2026-10-09 15:26): +1 for this. Running a headless openchamber on my server and have it connected to my phone and pc
  - **u/Mihaylov93** (↑1, 2026-10-11 05:26): Have you compared to deepseek harness?
- **u/Airshakur88** (↑1, 2026-10-09 15:57): Se você instalar proot distro no termux você consegue usar
- **u/sixincomefigure** (↑1, 2026-10-09 18:58): Paseo is excellent on Android
  - **u/jelloeater85** (↑1, 2026-10-11 18:42): Works great for Claude and Goose as well. It's dope.
- **u/nadjib4200** (↑1, 2026-10-10 20:04): Lunch opencode server and Use tailscale in your laptop https://tailscale.com and install mobile app of tailscale after this conect to opencode with ip adress and add port of opencode example http://<VOTRE_IP_TAILSCALE>:4096
- **u/jelloeater85** (↑1, 2026-10-11 18:44): Been rocking https://github.com/kdlbs/kandev for keeping all my agents in order. Great for Coding. 
    Paseo is best for mobile though.
    
    Alot of folks also rock Herdr and Orca as well.

---

## FREEBUFF is cool
**u/ghost132026** · 2026-10-09 14:36 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1n20e/freebuff_is_cool/)

[removed]

---

## Can a local ollama agent access the internet using opencode
**u/super2061** · 2026-10-09 13:38 UTC · ↑1 · 14 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1llpz/can_a_local_ollama_agent_access_the_internet/)

should i be worried it might upload any data to servers unprompted? if it can access the web can i make it always ask for permission first? also can it mess up my files or anything if i don't approve it?

**Comentarios:**

- **u/dumbasPL** (↑2, 2026-10-09 13:46): It can execute any command, including ones that can access the internet. If you want to guarantee that doesn't happen, sandbox opencode with no internet access.
  - **u/super2061** (↑1, 2026-10-09 13:47): on settings i set permissions to prompt. isn't it enough? can't i make it ask for everything?
    - **u/Fresh_Sock8660** (↑2, 2026-10-09 14:23): You can block webfetch but that won't stop e.g. a python script. This sort of half arsed "sandboxing" is how these model escapes you see on the news occur.
      - **u/super2061** (↑1, 2026-10-09 14:29): 1. Why would it escape 2. Can't I make it ask for permission for everything so I know what it does? I mostly care about using it as a coding teacher that also helps me with writing code not everything.
        - **u/Fresh_Sock8660** (↑2, 2026-10-09 15:03): Whatever reason it finds to access the outside of the sandbox. Escapes aren't necessarily malicious, it's often just the agent trying to do things it can't inside the sandbox.
            
            Yes, you can make it ask for everything. Check the docs / ask sonnet how to setup the config.
            
            Needless to say, that wouldn't be enough to stop a malicious agent.
  - **u/super2061** (↑1, 2026-10-09 14:23): u/dumbasPL i pasted: {
      
        "permission": {
      
      "\*": "ask",
      
      "bash": "ask",
      
      "webfetch": "ask",
      
      "websearch": "ask",
      
      "edit": "ask",
      
      "read": "ask",
      
      "external\_directory": "ask",
      
      "task": "ask"
      
        }
      
      }
      
      on opencode.json. should it be fine or it still might upload stuff or mess with files without my permission
    - **u/dumbasPL** (↑1, 2026-10-09 14:25): You're gonna be doing a lot of reading, but yes, blocking all tool calls is a half assed solution.
        
        I'm gonna repeat one last time, nothing besides proper sandboxing is actually safe. Have fun
      - **u/super2061** (↑1, 2026-10-09 14:29): Ok I'm fine with it since I'm going to use it as a coding teacher and assistant. Not way too much
      - **u/super2061** (↑1, 2026-10-09 14:30): Also so without proper sandboxing it might still missbehave and upload stuff to the internet or mess with files without permission?
- **u/dumbasPL** (↑1, 2026-10-09 13:50): Try it and see, ask it to fetch something from the internet. If it can fetch, it can also upload.
    
    If you allow command access, everything is possible, and if you don't, it's useless. Prompting it only goes so far, it's not a hard guard rail. Use proper sandboxing for that.
- **u/TheMythicSorcerer** (↑1, 2026-10-09 15:40): Technically yes unless you:   
    A. Turn off internet (ollama and opencode should work fine)  
    B. Disable websearch and webfetch in your config
  - **u/super2061** (↑2, 2026-10-09 15:42): I made it ask for permission for everything. Are there realistic chances it might bypass the permission and just do stuff?
    - **u/TheMythicSorcerer** (↑1, 2026-10-09 18:35): Opencode seems to be well made enough that it can't bypass permission so if it does that would be a severe bug in opencode itself which would be quite suprizing to me.
        
        What's more likely is it does so much stuff that it spawn a new permission prompt every 30 seconds and after a hour you're not paying as much attention and accidentally approve web. 
        
        I would reccomend sandboxing, disabling web in config or even just creating a separate agent without web tools.
- **u/Kydanet** (↑1, 2026-10-09 17:32): The "make it ask for everything" approach has a known failure mode: the prompt is enforced by the same thing being constrained. If the model can run a shell command, it can run one that doesn't ask — and half the thread already said this, correctly. Prompt-level permissions are a speed bump, not a boundary.
    
    The only hard version of "ask first" is physical: give the agent a machine that isn't yours. Worst case it wrecks a box that gets rebuilt from a snapshot, and your real files were never in reach in the first place. A container with no mounts and no credentials gets you most of the way; a separate computer with its own disk gets you all the way, especially if every command it runs lands in an attributable audit log.
    
    That's the setup we run at Kydanet — the agent gets its own Linux box, so the sandbox is the machine itself, not a rule file in opencode.json. Point whatever model you want at it (ollama included) and the boundary doesn't change; only the brain swaps out.

---

## cache and restore the initial OpenCode prompt with llama.cpp and Qwen 3.x local models
**u/ea_man** · 2026-10-09 13:07 UTC · ↑3 · 14 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1kwh3/cache_and_restore_the_initial_opencode_prompt/)

Sometime ago I [posted about an extension](https://www.reddit.com/r/opencode/comments/1wvt3j4/is_there_an_interest_for_an_extension_that_allows/)  I made that allows to cache the initial prompt ingestion of Opencode when using llama.cpp (llama-server) with Qwen models like 27B, this allows people with slow PP to save the initial prompt ingesting time when starting a news session.

https://preview.redd.it/r2limc99ufuh1.png?width=1281&format=png&auto=webp&s=0e984a2ad1210c987ac1258be43fb15b42ac8fe0

As now llama.cpp has introduced preserving [context checkpoints](https://github.com/ggml-org/llama.cpp/pull/26004) in mainline there's no more need to patch llama.cpp to allow persistent storage of the caching, hence the extension can work with any llama.cpp build after **b11500** (goes like version: 0.6.0-dev).   
Beware: *that was merged 8 October.*

Other than the Readme of the extension there's the [Overview document](https://store.piffa.net/lm/ocache/OVERVIEW.html) that explains the mechanics of caching the initial prompt with hybrid cache models and Opencode. 

I have hence updated the extension, you can see and dwl from: [https://store.piffa.net/lm/ocache/](https://store.piffa.net/lm/ocache/) , ask your OpenCode to install and configure it for you, below a summary of manual install instructions. 

\--------------

\# Manual install and usage instruction:

    wget https://store.piffa.net/lm/ocache/oc-prefix-cache.tgz
    tar xzf oc-prefix-cache.tgz
    cp -r oc-prefix-cache ~/.config/opencode/
    mkdir -p ~/.config/opencode/plugin
    printf 'export { default } from "../oc-prefix-cache/index.ts"\n' \
      > ~/.config/opencode/plugin/oc-prefix-cache.ts

\# llama-server scrip edits:

    --slot-save-path ~/llama/slot_caches/
    # You have to save slots somewhere in order to have persistent storage
    
    --jinja --chat-template-file chat_template_3.8.jinja
    # Recommended to use a proper and stable template like https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates because tolls loading matters for prompt caching
    
    --checkpoint-min-step 4096
    # A resume can only land on the last checkpoint before the divergence point, so up to min_step tokens get re-read every start. The stock default (8192) is coarser than a typical harness prefix — you'd get zero reuse. 4096 works; 0 maximizes reuse at the cost of VRAM.



\# Extension Config — all env vars, read once at opencode start:

* export OC\_PREFIX\_CACHE\_BASE\_URL=http://127.0.0.1:8080/v1  # required; also the provider gate
* export OC\_PREFIX\_CACHE\_PERSIST=1
* export OC\_PREFIX\_CACHE\_SLOT\_DIR=$HOME/llama/slot\_caches  # must equal --slot-save-path
* export OC\_PREFIX\_CACHE\_SERVER\_ID=b11500-mainline          # bump on every server rebuild
* export OC\_PREFIX\_CACHE\_MODEL\_PATH=/path/to/model.gguf     # lets fingerprint notice a swapped GGUF

BASE\_URL unset ⇒ the plugin does nothing at all. It must exactly equal your provider's baseURL — that match is the gate, so it can only ever warm its own server.

\# Storage required:

Budget \~880 MB per cached prefix. Your fingerprint covers model id, GGUF, server build, opencode version and the exact tools\[\] array — so bumping any of those forces exactly one cold rebuild, which is by design. OC\_PREFIX\_CACHE\_MAX\_GB if the footprint matters.

**Comentarios:**

- **u/CyberTod** (↑1, 2026-10-09 14:05): Sounds very useful. I've had that idea, but haven't tried it.
    
    I have Qwen3.8-flash-next on an old server with 192GB RAM, but no GPU and that initial prefill is what making it unusable, but 5tok/s after that is sufficient for some nightly tasks.
    
    Building it now to test.
  - **u/ea_man** (↑1, 2026-10-09 16:06): If you are using llama.cpp to launch that Qwen3.8-flash-next it may work, I didn't test it as I'm going to see how it's working with Strata first, yet if llama.cpp is doing his part it should work.
      
      Otherwise it may be that we need a patch for llama.cpp, as it was before **b11500.**
      
      Yet I was even thinking about disabling that for MoE as those usually have pretty good PP compared to dense model, I designed this with 27B and smaller dense model in mind, I was just checking how it's working with A3B a few hours ago...
    - **u/CyberTod** (↑1, 2026-10-09 16:28): It does work, but I have some problem now and debugging.  
        If I just start new sessions it is almost instant and uses the cached prompt.  
        If I restart opencode it says 'selected slot by LRU' and processes the entire prompt again.
      - **u/ea_man** (↑1, 2026-10-09 18:08): It does work with Qwen3.6-35B-A3B which is MoE.
          
          For Qwen3.8-flash-next do you have problems with llama.cpp or Strata?
          
          Testing in llama.cpp is a pain for me as it's super slow :/
        - **u/CyberTod** (↑1, 2026-10-09 18:23): Qwen3.6 is not good for my use cases. Does too many mistakes and circles around. The Qwen3.8-27B is excellent, but not good for the CPU only scenario. Qwen-3.8-flash-next is good overall, so I just run that on that server, which is mostly idle anyway.
            
            I am testing with llama.cpp, a few issues discovered in my config, first I had --parallel 1 and that was an issue for some reason. And I had a model rewrite the plugin, because I am using v2, it was compatible only with v1, so after that it applied a patch "HIT check hardened", don't ask me what it does exactly, no idea.
          - **u/ea_man** (↑1, 2026-10-09 19:28): I'm sorry but I can't really understand:
              
              1. what is v2? you mean my extension updated release that it's pruned of the old .chk point code of the first release? I had a middle release that was working with both format in case.
              
              2. You say that the extension has issue with reasoning effort low? If you change effort during a session the harness should invalidate the KV cache up to that point.
              
              Nice to know that it works for you now :)
            - **u/CyberTod** (↑1, 2026-10-09 19:46): I mean opencode 2.0
                
                And not that it has an issue with reasoning effort low, but that the reasoning was not part of the fingerprint sent to llama.cpp, which caused the issues that sometimes it would use the cached prompt and sometimes not, but that could have been a problem with the rewrite.
              - **u/ea_man** (↑1, 2026-10-09 21:17): I see thanks, I didn't test with Opencode 2.0 already, this was made for 1.x .
                  
                  Thanks
- **u/ea_man** (↑1, 2026-10-09 14:14): FYI I've made this for [Pi.dev](http://Pi.dev) too, usually Pi uses a much smaller prompt.  
    I'm testing that now with Qwen 27B before publishing to Pi packages.
    
    \- [https://store.piffa.net/lm/picache/](https://store.piffa.net/lm/picache/)
- **u/Ctbhatia** (↑1, 2026-10-10 04:49): does the plugin restore the same slot id after a restart, or just leave the save file on disk? the selected slot by LRU line means llama-server picked a different slot, so the prefix you saved may not be the one it loads.
  - **u/ea_man** (↑1, 2026-10-10 11:56): The plugin saves the slot on disk (when config so) and those files are reused for new / different session that happen in different sessions / paths.
    - **u/Ctbhatia** (↑1, 2026-10-10 15:07): worth checking whether the save is keyed by slot or by prompt, because the selected-slot-by-lru line means the slot id after a restart is not the one you saved from.
      - **u/ea_man** (↑1, 2026-10-10 16:59): Oh no the save is fingerprinted by the extension in a granular way, I'll give you a slop summary:
          
          Short answer: **the save  is keyed by prompt, and save/restore are pinned to a fixed slot id — the LRU line is about the normal request,**  **not the save/restore.**
          
          # What the plugin actually does
          
          1. **The save file is keyed by prompt fingerprint, not slot.** `index.ts:317` — `fname = pi-prefix-<fp16>.bin`, where the 16-hex prefix is the fingerprint of (model + GGUF identity, pi/ext versions, server id, tools\[\], chat\_template\_kwargs, stable prefix). The slot number is only a stored attribute in the metadata index (`cache-store.ts`), never part of the key.
          2. **Save and restore explicitly target a fixed slot id — they never go through LRU.** Both operations are `POST /slots/{id}?action=save|restore` with `id = PI_PREFIX_CACHE_SLOT` (default `0`) — `warmup.ts:slotFileAction`, called at `index.ts:338` (restore) and `index.ts:404` (save). On the server side, `post_slots` resolves the slot by id via `get_slot_by_id()` — LRU is not involved at all. Slot ids are deterministic: slots are created in order `0..n_parallel-1` at server start (`server-context.cpp:1480`), so slot 0 is slot 0 after every restart.
          
          So after a restart the plugin doesn't "just leave the save file on disk and hope": it restores `pi-prefix-<fp16>.bin` into slot 0 explicitly, then empirically verifies it (identical-prompt warm-up must score ≥90% cache reuse, plus a divergent probe requiring a checkpoint resume — `index.ts:339-367`). Invalid → erase + cold rebuild + re-save.
          
          # Where the "selected slot by LRU" line comes from
          
          Server-side selection order (`server-context.cpp:1788-1872`):
          
          1. request has a slot field → selected slot by id — this is what the plugin's warm/probe/save/restore requests take;
          2. else, if `--slot-prompt-similarity` is set → LCP-similarity pick;
          3. else → LRU fallback.
          
          The extension never mutates the provider payload (option A), so the normal Pi request carries no slot field and lands in branch 2/3. That's the LRU line in the log — it says nothing about which slot the checkpoint was saved from or restored to.
          
          # The one real caveat
          
          With `-np 1` (the deployment assumption — see [`AGENTS.md`](http://AGENTS.md) known open items: multi-session locking unimplemented, single active session assumed), LRU/LCP trivially picks slot 0, i.e. exactly the slot the prefix was restored into. No mismatch is possible.
          
          With `-np > 1`, an unpinned normal request can be routed to a different slot (e.g. LCP picks another slot, or LRU picks the least-recently-used one), in which case the restored prefix in slot 0 goes unused and the request fully re-prefills. Two mitigations exist:
          
          * it's not silent — the `after_provider_response` diagnostic (`index.ts:445-469`) polls slot 0's counters and logs the observed reuse %; a `0%` line reveals the mismatch;
          * with `--slot-prompt-similarity` set, unpinned requests prefer the slot with the longest common prefix, i.e. the restored one.
          
          # Bottom line to tell the user
          
          >the questioner's premise ("the selected-slot-by-lru line means the slot id after restart is not the one you saved from") conflates two different code paths. Checkpoint files are prompt-keyed, and the save/restore endpoints are slot-id-pinned with deterministic slot numbering, so the restart case is handled. The LRU line only describes routing of the unpinned normal request, which is only a genuine risk in a multi-slot (`-np > 1`) setup — a known, documented limitation, not a save/restore bug.
        - **u/Ctbhatia** (↑1, 2026-10-11 19:25): if the save is keyed by prompt fingerprint then restore should not depend on a slot id surviving at all, store the fingerprint and look that up. pinning a slot when the key is already the fingerprint is the part that breaks after a restart.

---

## Can a French business use opencode ?
**u/Eddybeans** · 2026-10-09 12:04 UTC · ↑8 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1jl3o/can_a_french_business_use_opencode/)

Trying to use it with French business but there is no French VAT tax code in the list ???  
When I put my ful FRxxxxxxx tax code in Tax ID Field it says I must choose one from Tax ID type but there is no FR type  
Can someone help me out ?

**Comentarios:**

- **u/aimgorge** (↑2, 2026-10-09 12:16): Cant you pay the VAT and get then get it reimbursed by providing the invoice ?
  - **u/Eddybeans** (↑3, 2026-10-09 12:17): Maybe but i don’t want the hassle
- **u/_Heziode** (↑2, 2026-10-09 16:30): J’ai mis EU VAT, avec mon code TVA FR… c’est passé.
    Je viens de le faire, donc je ne sais pas encore si la TVA sera auto liquidé
  - **u/Eddybeans** (↑1, 2026-10-10 08:42): Ha yes parfait 👍

---

## What's the closest model you prefer as an alternative to Opus on Go plan?
**u/thepurpleproject** · 2026-10-09 11:59 UTC · ↑4 · 28 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1jgt6/whats_the_closest_model_you_prefer_as_an/)

I mostly use Open Code GO with Hermes and needed something which is comparable to Opus to get a few complicated task done. I'm on the $40 plan so its fine with the usage. Usually, I prefer DeepSeek 4.1 flash but it has its rough edges as it seems to contradict it self in some problems where things needs to be done in multiple steps and analyzed.

**Comentarios:**

- **u/ByteNomadOne** (↑27, 2026-10-09 12:03): DeepSeek 4.1 Flash and GLM 5.3 Flash are the only useful models there right now.
  - **u/thepurpleproject** (↑2, 2026-10-09 12:06): We are on the same page then. GLM 5.3 I found pretty equivalent to DeepSeek with a lower throughput. 
      
      What is the thinking level you use?
    - **u/Any-Solution9478** (↑1, 2026-10-09 14:12): Já testou o Muse Spark 1.3? Ele tá bem legal, cara
    - **u/ByteNomadOne** (↑1, 2026-10-09 14:28): Mostly HIGH, because MAX takes very long.
        
        On the campaign hours I had it running on MAX overnight. For daily use HIGH is better.
  - **u/stickgrinder** (↑3, 2026-10-09 12:30): Same. I tried GLM 5.3 and it's great but DS 4.1 Flash is currently my fav.
    - **u/ByteNomadOne** (↑2, 2026-10-09 21:12): I agree, DS 4.1 is faster
  - **u/daniel-sousa-me** (↑6, 2026-10-09 19:58): I used GLM 5.3 flash a lot during the ox alpha stealth period and found it pretty great
      
      It's not at the level of Opus 5.5, but I'd pick it over Opus 4.7 and 4.8 
      
      But I wouldn't call those Opus replacements anymore. Even Haiku 5.5 is ahead
    - **u/ByteNomadOne** (↑3, 2026-10-09 21:12): GLM 5.3 Flash is of course certainly behind Opus. Everything is.
        
        Opus is just very expensive and GLM 5.3 Flash & DeepSeek V4 Flash are the models I can afford.
      - **u/daniel-sousa-me** (↑2, 2026-10-09 21:42): Yeah, of course! 
          
          But you can match the Opus level from 3 months ago, it's crazy
  - **u/rcs67** (↑1, 2026-10-10 02:39): Muse 1.3 is excellent. I speak as a 4.1 Flash regular.
- **u/fosron** (↑2, 2026-10-09 12:16): Not sure if a one-to-one alternative to Opus, but if you create a good plan with a frontier model beforehand DeepSeek 4.1 Flash will get you 95% there almost all the time.
  - **u/migsperez** (↑0, 2026-10-09 14:10): Opus is in a league of it's own. Damn. I hope the others catch up soon.
- **u/torrso** (↑7, 2026-10-09 12:23): Just wanted to note that doing complex stuff in hermes is possibly not the best choice. It's not a great harness for complex tasks or coding. Actually it got the last place in a benchmark. 
    
    You may be better off doing that complex task in OpenCode or some other coding harness.
  - **u/JohnR_Orbit92** (↑4, 2026-10-09 12:58): Hermes is for everyday agentic tasks for example, I send Instagram and tiktok videos to Hermes and ask it to download the video n transcribe then it adds the transcript to my notes app & attaches video to that note. So if Instagram or tiktok delete it, I always have a copy. 
      
      Another example is I sent good book  names to Hermes and ask it to save it. Then it downloads those books & sends to my kindle. 
      
      For coding use claude code or opencode
    - **u/thepurpleproject** (↑2, 2026-10-09 13:29): Correct. Currently my problem is it takes a way too my trial and error to do some trivial stuff like login to reddit or twitter with browser CDP. Or loading credentials from keepass.
      - **u/JohnR_Orbit92** (↑2, 2026-10-09 13:45): Have you tried adding proxies, proper browser tools, cookies for login (you login in Reddit etc accounts n export that cookie n give to Hermes). + Avoid giveing it 10 tasks at once. If you do give it a batch Let it do 1 at a time. 
          It usually isn't the model, most 2026 models are smart enough to get scraping done. Then try GLM 5.3 flash (cheapest on openrouter at the moment) or DeepSeek 4.1 flash.
      - **u/Ashamed_Drag8791** (↑1, 2026-10-10 08:59): For stuff like this, use dedicated mcp, and specify your agents to only use it for those specific tasks.
    - **u/snok-man** (↑1, 2026-10-10 13:51): Which models do you use for those tasks?
      - **u/JohnR_Orbit92** (↑0, 2026-10-10 18:37): agentic work takes large amount of tokens (with all the tools it uses) so use GLM5.3 flash (dirt cheap on openrouter at the moment). Deepseek 4.1 flash is also great. 2 months ago i had Minimax plan (when they gave 5.1 billion tokens for $20/mth....not anymore tho)
        - **u/snok-man** (↑1, 2026-10-10 19:41): Alright thanks :)
  - **u/Top_Performance_732** (↑1, 2026-10-09 13:04): What about hermes for planning and then handing the same agent to a coding harness? I find hermes great for planning and designing architecture
- **u/hierovision** (↑1, 2026-10-09 12:27): Mimo 2.6 pro is excellent but slow, I mix it in when I want quality over speed. I combine DS 4.1 flash, mimo 2.6 pro, qwen 3.8 flash, minimax m3, gpt 5.6 Luna, and glm 5.3 flash to get family diversity in my daily driver activities. They're bound to agent files that represent different personas like architect, curator, implementer, reviewer, etc. 
    
    No anthropic model compares well enough to earn a spot. They're just too expensive. I haven't measured the new haiku yet though.
  - **u/look** (↑2, 2026-10-09 20:13): Agreed, and MiMo 2.6 Pro is my primary model now (in combination with GLM 5.3 Flash  
      and some Kimi 3, full GLM, and Qwen3.8 Flash).
      
      The speed is rough though, and I don’t use Go anymore for it. There are other providers with fast MiMo Pro. I use Neuralwatt’s right now, but I’m going to try out Prima Labs, too, which looks promising.
- **u/RasonYang** (↑-2, 2026-10-09 12:43): Heads up, Haiku 5.5 is on the Go table now.   
    3,850 requests per 5h and $15 of month quota, and it's not the same family as DS or GLM.   
    That matters  when one model keeps second-guessing its own plan.   
    Quota split matters too, Kimi K3 is 110 and $15 while DeepSeek 4.1 Flash is 26,000 and $60.   
    So I keep the expensive pool for the few hard jobs and never let it near the daily stuff.   
    On the drift you're seeing, cutting tools did more for me than any model swap.
- **u/Frequent_Director_94** (↑4, 2026-10-09 13:07): I agree with ds and glm flash. But I think bigpickle is crazy underrated and its free. I've been very impressed by that model
  - **u/stickgrinder** (↑2, 2026-10-09 21:17): For a silly bias (free = cheap) I never handed out heavy loads to it. For a lot of mundane stuff it's great, but I never put it under real pressure.
      
      Any experience to share about its actual limits?
- **u/mc7244** (↑1, 2026-10-09 21:27): Deepseek 4.1Flash. It's so excellent for coding.
    I create the plan myself... I mean I'm a dev, I can and want to plan myself. And DS executes.
- **u/Ok_Supermarket3382** (↑1, 2026-10-10 13:18): Dsf 4.1 and muse spark contributor. Depends on which is serving the real model sometimes they seem to serve a dumbed down version

---

## I built TermuCraft: a free, open-source Windows app that combines an SSH/SFTP terminal suite (MobaXterm-style) with a full database workbench (DBeaver-style)
**u/bm_mbaa** · 2026-10-09 11:47 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1j8ng/i_built_termucraft_a_free_opensource_windows_app/)

---

## literally every game dev and vibe coder lol
**u/GoonigUnc** · 2026-10-09 10:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1hebc/literally_every_game_dev_and_vibe_coder_lol/)

[removed]

---

## Frequent Error Interruption While Using Chat GPT Plus Plan on Opencode
**u/FZRP2** · 2026-10-09 10:02 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1hdv3/frequent_error_interruption_while_using_chat_gpt/)

https://preview.redd.it/k085m8240fuh1.png?width=1502&format=png&auto=webp&s=2ef5414acb0dd0b328523d4565387940fdc9e232

anybody encounters the same problem? idk what causes this

---

## DeepSeek V4.1 Flash issue
**u/BoatZealousideal4521** · 2026-10-09 09:44 UTC · ↑1 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1h3di/deepseek_v41_flash_issue/)

Hi All, 

I am not able to use the DeepSeek v4.1 flash model and am getting an error response stating that "this model requires global deployment". 

What is this issue has anyone faced this, if yes then how to fix it?

Thanks on advance

**Comentarios:**

- **u/FinalAliens** (↑2, 2026-10-09 09:48): Perhaps you did not allow connection to China from opencode webpage settings.
  - **u/BoatZealousideal4521** (↑2, 2026-10-09 09:51): Thankyou, I will check and update the settings.
- **u/Efficient_Try_9136** (↑2, 2026-10-09 09:50): you need to enable global in settings privacy, its hosted in China
- **u/BoatZealousideal4521** (↑1, 2026-10-10 06:35): Thanks guys for the inputs. Changed the settings and now able to use it.

---

## Step 5 Preview Free, what do you think?
**u/CoffeeTea021** · 2026-10-09 09:25 UTC · ↑37 · 23 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1gsfy/step_5_preview_free_what_do_you_think/)

I think Step 5 Preview Free is a pretty good model. What has your experience been like so far?

**Comentarios:**

- **u/qeadwrsf** (↑8, 2026-10-09 09:44): slow, better than expected.
- **u/Jaimeet_Sarode** (↑1, 2026-10-09 09:59): It's really really slow for me
- **u/YoRt3m** (↑2, 2026-10-09 10:02): Not the best, not the worst
- **u/Global-Morning-431** (↑3, 2026-10-09 10:04): pretty much like space bunny  (slow but good)
  - **u/yourpwnguy** (↑1, 2026-10-09 10:06): Wait that ain't slow, it reaches 100+ TPS for me.
    - **u/Time-Toe-1276** (↑0, 2026-10-09 11:50): maybe in ur time zone the mainstream users aren't probably awake yet. or it might just be better load balancing for ur region or sum.
        
          
        Ox Alpha had speed bursts in the free tier aswell
- **u/Vast_Anxiety3133** (↑4, 2026-10-09 10:16): API price is more expensive than DS, but it feels DS or better for me. (I have not tested doing something in lua, most models suck implementing in LUA against a rare and badly documented API, Deepseek is the cheapest I know can push through that
- **u/ByteNomadOne** (↑1, 2026-10-09 10:17): Very slow. Everything taking to long.
- **u/PerfectReflection155** (↑2, 2026-10-09 11:00): Well I think it’s great, compatible to glm flash 5.3. Solid model . I would probably pick it over Luna or muse contributor 1.3 but not over deepseek 4.1 of glm 5.3 or haiku
- **u/oldfag0** (↑3, 2026-10-09 11:30): 30-40% slower  then GLM 5.3 flash. Better, more predictable code quality. I use it together with opus 5.5 (manager). Switched back to glm because of speed.
- **u/Bakanyanter** (↑1, 2026-10-09 12:38): Decent but more expensive and so much slower than DS. It's a good model if we get it at $60 limit in Go, otherwise don't think worth it.
- **u/matadordepassarinhos** (↑1, 2026-10-09 13:02): slow
- **u/[deleted]** (↑1, 2026-10-09 13:42): [removed]
- **u/migsperez** (↑1, 2026-10-09 14:15): Bad
- **u/[deleted]** (↑1, 2026-10-09 15:48): [removed]
- **u/Intelligent_Ant_608** (↑1, 2026-10-09 15:58): Its better than ds 4.1
- **u/[deleted]** (↑1, 2026-10-09 16:10): [removed]
- **u/WeGoToMars7** (↑1, 2026-10-09 17:17): I ran it on my private CTF cybersecurity benchmark (overnight because it's slow; it stopped after 1.6B tokens due to a rate limit), and it's much worse than both DeepSeek V4.1 Flash and GLM-5.3-Flash, and about on par with MiMo V2.6 Flash. Maybe it's much better as a coder, but it feels very benchmaxxed.
- **u/alexanderbeatson** (↑1, 2026-10-09 17:31): My test: too much tool calls failed with typos in tool call (very much like Luna). Cannot update the todo progress dynamically (that is really bad). Implementation is sub par, not good, not bad, like DS4F, can do stuff, but cannot brainstorm. I would not use if it isn’t cheaper than DS.
- **u/breadnone** (↑1, 2026-10-10 07:07): it loves to overthink and do same tests over and over..
- **u/ATyp3** (↑1, 2026-10-10 13:32): Fucking love it.
- **u/Agile-Commercial9750** (↑1, 2026-10-10 16:37): Sloooowww
- **u/YogurtclosetClean478** (↑2, 2026-10-11 15:48): I just change from space bunny to step 5 preview in opencode zen today, but i meet "Upstream request failed: Endpoint is unavailable." for so many times. Although i tried to retry, this issue still remains.  
    why does this model take so much time to think? And what is the main reason for the problem in the image? How can i fix this?
- **u/HorosCode** (↑1, 2026-10-11 22:11): u can wait hehehe its time intensive\^\^

---

## Tokens acabam rápido demais!!!
**u/Any-Solution9478** · 2026-10-09 09:23 UTC · ↑0 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1grq7/tokens_acabam_rápido_demais/)

Sério, meus manos!! Esses tokens do Claude pro não duram nada, depois cê tem que ficar parado umas 4 ou 6h, mesma coisa com o Codex e nem testei outros agentes. Ouvi falar do Opencode que tu pode usar centenas de provedores diferentes e que é a melhor opção gratuita, eu já tô cansando de ficar pagando esses agentes aí, como vocês usam o Opencode? Melhores modelos gratuitos e como fazem para os tokens não acabarem igual água em casa de egípcio?

**Comentarios:**

- **u/bruno30303** (↑1, 2026-10-09 10:49): Tem que usar os modelos mais baratos no opencode Go tbm. O deepseek v4.1 flash, muse 1.3 contributor, etc. Se usar os modelos mais caros, acaba rápido tbm.
    
    Aqui tem uma tabela de uso dos modelos https://opencode.ai/br/go
  - **u/Any-Solution9478** (↑1, 2026-10-09 10:55): A cota é individual para cada modelo, ou é geral? Um amigo meu falou comigo que usava um tal de Big Pickle e quando limite acabava ele não conseguia usar outros modelos do plano. Mas na sua tabela a cota parace individual para cada um, se um acaba você pode simplesmente usar o outro?
    - **u/bruno30303** (↑1, 2026-10-09 12:52): É geral. Cada modelo tem um valor máximo de uso por mês, mas vc tbm tem limites a cada 5h, por semana e por mês.
        
        Se vc pegar um modelo X e gastar toda a cota mensal nele, já era. Aí vc pode continuar usando os modelos gratuitos, como o big pickle.
- **u/[deleted]** (↑1, 2026-10-09 11:07): [removed]

---

## every vibecoder and game dev
**u/ruboxytr** · 2026-10-09 08:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1gadg/every_vibecoder_and_game_dev/)

[removed]

---

## yeah I’m serious
**u/dogfoodarchitect** · 2026-10-09 08:33 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1fzk3/yeah_im_serious/)

---

## Can anyone help me out with a Claude invite?
**u/MeaningAnnual3542** · 2026-10-09 07:34 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1f2y2/can_anyone_help_me_out_with_a_claude_invite/)

Hi everyone. How’s it going?



I’ve been wanting to try out Claude for a while, but I noticed some users have those invite links could someone send me one via private message?

**Comentarios:**

- **u/crotch-mavens** (↑1, 2026-10-09 09:04): Weird post

---

## Opencode Go with openclaw, is it allowed usage?
**u/dragonfly_overfly** · 2026-10-09 07:09 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1eosx/opencode_go_with_openclaw_is_it_allowed_usage/)

[removed]

---

## Suggest me some best free models to create a saas product
**u/Helpful_Layer_4754** · 2026-10-09 06:26 UTC · ↑0 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1dzy2/suggest_me_some_best_free_models_to_create_a_saas/)

**Comentarios:**

- **u/trivial09** (↑1, 2026-10-09 06:31): If space bunny still up for opencode zen, you can test it out
- **u/FrostGoesBrrrt** (↑1, 2026-10-09 07:22): Muse Spark 1.3 or the new Step 5
- **u/torrso** (↑4, 2026-10-09 07:31): I heard slopgpt-2-flash is really good at saas products
- **u/PerfectReflection155** (↑1, 2026-10-09 07:40): The new step 5 free is really good. It’s on the same level as GLM 5.3 Flash and it’s free for 1 week only I beleive. Just came out today.
- **u/Federal-Rub2713** (↑1, 2026-10-09 11:33): From opencode specifically, Step 5 Preview and Muse Spark 1.3 are great. From other coding tools, you could try other tools that have promptional free models - Cline, Command code (the 1 buck sub), Kilo code, and my personal favorite is Freebuff (if you are from the US, they offer a great daily allowance on their free plan) - currently there's a promotion for GPT 6.1 Sol where you can use it for 1 hour daily, no token limits. Also other powerful middle class models such as MiMo 2.6 Pro (actually its a flagship level), Deepseek 4.1 Flash and GLM 5.3 Flash)

---

## Are there other excellent motion graphics models besides opus 5.5?
**u/Agitated_Unit8226** · 2026-10-09 06:15 UTC · ↑0 · 9 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1dtga/are_there_other_excellent_motion_graphics_models/)

Hey guys, I tried to create motion graphics with models like DeepSec V4.1, MIMO 2.6 Pro, kimi k3 My experience was that they take up a lot of my time and the result is unsatisfactory, so what is your experience with other models? Have you discovered a model that gives good results?

**Comentarios:**

- **u/jarvis123451254** (↑2, 2026-10-09 07:21): it would take open models to reach opus 5.5 level, lets give them 5-6 months
- **u/Amarsir** (↑2, 2026-10-09 08:24): If you're up for one more experiment, try Space Bunny. It's from Minimax who has always been focused on the more visual elements.
    
    But it's also a tough ask and I wouldn't be surprised if only Opus, Sonnet, and maybe Sol were good at it. If you absolutely need to use one of the open source models, help it out by sculpting your prompt as detailed as possible and maybe give a tech example of how you would want it done.
- **u/Zeeplankton** (↑1, 2026-10-09 09:41): Only claude right now
- **u/Federal-Rub2713** (↑1, 2026-10-09 11:28): So from my opinion:  
    **1. claude-haiku-5-5 (Best overall budget pick)**
    
    * **Strengths:** Strongest design intuition in the low-cost tier. Respects safe margins, handles Remotion/GSAP components cleanly, and applies spring physics without overlapping text.
    * **Best for:** Kinetic typography, UI animations, video promo sequences.
    
    **2. gpt-6-luna (Best for geometry and canvas)**
    
    * **Strengths:** High precision with coordinate math, SVG path morphing, Canvas/Three.js, and staggered arrays.
    * **Best for:** Procedural canvas animations, math-heavy transitions, data visualizations.
    
    **Why the rest struggle:**
    
    * **DeepSeek (v4/v4.1/flash), Kimi (k2.x/k3), MiniMax (m2/m3):** Poor internal spatial reasoning. They routinely overlap text, clip off-screen, and default to rigid linear fades instead of natural easing curves.
    * You could try MiMo 2.6 pro as it's really good overall, I havent tested it in motion graphics personally, though.
    
    (bonus: you could use other coding tools that provide promotional access for flagship models, for example right now Freebuff offers GPT 6.1 Sol (unlimited token usage, fixed 1 hour per day) if you are from one of these regions: US, CA, GB, AU, NZ, IE, NO, SE, DK, FI, NL, AT, LU, IS (freebuff has multiple free tiers depending on your region, i think its because of the different market and ad revenue))
- **u/lordcohliani** (↑1, 2026-10-09 14:46): What tools are you using to create the graphics? Or just asking the base model directly?
- **u/Odd_Donkey2691** (↑1, 2026-10-09 16:52): Hello, I agree with you, I am amazed of the motion graphic  I see other people doing with Claude and ChatGPT. I only use Hyperframes and cannot achieve that, I need to know how to foce my flash model to adapt to that or investigate how approximate they can get to frontier level.
  - **u/Agitated_Unit8226** (↑1, 2026-10-10 01:56): Yesterday I used Opus 5.5 Medium and it did the job. With open-source or Chinese models, my back broke while sitting in my chair.
    - **u/Odd_Donkey2691** (↑1, 2026-10-11 05:14): Hey bud, how are you. Yesterday I spent quite a few hours experimenting . Yo uknow I was testing with Deepseek Flash 4.1 and I was able to get some good Motion Graphics, procedural graphics with Dynamic Camera effects etc. I found that the prompt and description helps a lot, before I just asked for a video in hyperframe based on  a certain topic, and just asked the model to "Improve" the video or add graphics. Deepseek delivered better resultas than GPT 5.6Luna and Terra but it did took more time to work, I used Deepseek Harness Standard Preset.
      - **u/Agitated_Unit8226** (↑1, 2026-10-11 08:31): It's good that you tried it yourself because I already tried it and it does give results, but it's not 100% accurate. For example, I want a marketing video about a real estate project with audio, images, and videos. Deepseek needs to analyze the images and videos and creating scenarios for motion design and graphics.So it is simply the director and the executor.But of course, now after this experience, yesterday I finished creating a skill that makes the type of videos I want, and I tested it with Opus and it's excellent.Now I need to try it again with the Chinese models.

---

## orbio currently 60% off openrouter rates (direct openrouter usage)
**u/ConsiderationNo9952** · 2026-10-09 05:41 UTC · ↑0 · 8 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1d9j9/orbio_currently_60_off_openrouter_rates_direct/)

hey, i'm not associated, but if you're looking for cheap deepseek 4.1 flash etc - this is one way - orbrio dot so (unfortunately no providers that i know are offering high limit ds41f subscriptions so i use this) 

(and i've not seen it at 60% before)

**Comentarios:**

- **u/WisdomSky** (↑1, 2026-10-09 06:18): how is that even better than opencode?  
    Opencode literally gives you x6 credits for DS?4.1f.   
    60% off is complete trash if you compare that with it.  
    Also I don't know orbio and haven't heard much about that provider anywhere. I prefer to stick with known providers.
  - **u/ConsiderationNo9952** (↑0, 2026-10-09 06:55): hi! i use 1-4B tk/s week, mostly input and mostly cache. Do you suggested I run multiple opencode go subs? I hit the limits very very quickly.
      
      i'm not associated with it, but it is a solution for me and you can research on it.
  - **u/Ambitious-Neat7509** (↑1, 2026-10-09 07:02): The website is really laggy on chrome and how can they provide API usage of closed source models at a huge discount? Not possible, anthropic and openai wouldn't allow it. Its probably using subscriptions under the hood or who knows what. ZDR too? Yeah no.
    - **u/ConsiderationNo9952** (↑1, 2026-10-09 07:42): it is direct to openrouter. they pay openrouter credits to their miners and they onsell those credits.
- **u/Ctbhatia** (↑1, 2026-10-10 13:14): those credits are someone else's quota, so the discount is on price, not on capacity. i work at coralbricks.ai and for a cache-heavy loop i would rather pay list and get cached reads at $0, since the repeated prefix is most of what gets sent.
  - **u/ConsiderationNo9952** (↑1, 2026-10-10 18:08): hello! sorry what credits are someone's else's quota and why does it matter (assuming they are selling it?) the discount is on price yes, but compared to opencode plans there are no limits on when or over what time i use those credits.
    - **u/Ctbhatia** (↑1, 2026-10-10 19:02): fair, if there is no time limit then 60% off is just 60% off. the quota point only matters if the upstream rate limits are shared, since that is what bites a heavy loop rather than the price.
      - **u/ConsiderationNo9952** (↑1, 2026-10-10 20:20): no! right now (off peak on weekend) there are providers that are 90% off and 60% off is additional to that giving nearly free usage. what do you mean by shared upstream rates, it is a relay direct to openrouter providers.
          
          but again I'm not associated with it, i just use it and it is a useful solutions.

---

## Does opencode with local models have any telemetry or data collection?
**u/super2061** · 2026-10-09 05:04 UTC · ↑7 · 7 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1cn12/does_opencode_with_local_models_have_any/)

**Comentarios:**

- **u/AlexandraMaryWindsor** (↑1, 2026-10-09 05:13): No.
- **u/Ctbhatia** (↑2, 2026-10-09 05:18): as far as i can tell, no. with local models your prompts only go to the server you configured, and nothing in the config or docs suggests usage data leaves your machine. the one path your session data takes off your machine is sharing, it's manual by default, /share pushes the session to their servers and /unshare deletes it. there's also an experimental.openTelemetry flag if you want spans from AI SDK calls exported, it's off by default.
- **u/CollarMany3843** (↑-1, 2026-10-09 10:31): best to assume the worst with local agents.
    
    run opencode in a sandbox to ensure no out-calls, except ones you authorize.  
    
    among sandboxes i looked at, docker's sandbox product (microVM) is easiest.  free for personal use.  choose full lockdown mode when creating sandbox.
      
    https://www.docker.com/products/docker-sandboxes/
    
    if you're security/privacy conscious, also recommend using a reverse firewall (lulu if on macos) to notify you of all out-calls.
    
    https://objective-see.org/products/lulu.html
  - **u/super2061** (↑1, 2026-10-09 13:36): im on linux but can't i make it manual so it asks for every command and change or it can just access the web and everything by default?
    - **u/Top_Performance_732** (↑0, 2026-10-09 18:55): dont use opencode shithharness
- **u/LowIllustrator2501** (↑1, 2026-10-09 18:14): You can enable opentelemetry for debugging, but opencode doesn't report anything to Opencode servers.
- **u/TheMythicSorcerer** (↑1, 2026-10-09 18:32): No. you can turn off wifi though if you want to be extra paranoid.

---

## Good multi-device support with remote headless machines
**u/yexgoblin** · 2026-10-09 04:35 UTC · ↑0 · 8 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1c4qq/good_multidevice_support_with_remote_headless/)

I have lot of remote Linux boxes I ssh in and allocate work to. Mostly rewrites and such that takes a long time to finish. I also run local opencode inside containers/vms. For this I need a tool similar to Paseo for managing remotes. The issue with opencode web is that it's not a PWA and it doesn't have proper remote management. cli is okay. But it doesn't make it easy to manage everything from mobile. From the tools I have tried Paseo was the best but the experience is not that great compared to something dedicated to opencode. 

How are you guys managing these? T3 code and OpenChamber doesn't allow remotes. I don't want agents doing work in my host for obvious resons.

**Comentarios:**

- **u/MttGhn** (↑1, 2026-10-09 05:03): Openchamber te permet de te connecter de multiples serveurs ssh également ;)
  - **u/yexgoblin** (↑1, 2026-10-09 05:06): It's not the server. I want to connect to a remote headless container. I don't run agents on the host machines.
- **u/levu304** (↑1, 2026-10-09 06:22): Opencode has web frontend
  - **u/yexgoblin** (↑1, 2026-10-09 06:23): Please read what I wrote 😭
- **u/alexzzzz** (↑1, 2026-10-10 05:01): https://herdr.dev maybe?
- **u/lvl1-A** (↑1, 2026-10-10 09:31): What was it about paseo that you didn't like?
  - **u/yexgoblin** (↑1, 2026-10-10 09:33): Performance issues with the web ui and integration not being fully complete with what opencode offere
- **u/Competitive-Yak-8255** (↑1, 2026-10-10 12:42): Paseo

---

## Glyph Cluster Investigation - Microsoft MAI?
**u/Federal-Rub2713** · 2026-10-09 03:16 UTC · ↑1 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1aoeu/glyph_cluster_investigation_microsoft_mai/)

**Comentarios:**

- **u/SalamanderFickle4315** (↑1, 2026-10-09 05:01): Nice work brother

---

## Why, just why??
**u/anorak_999** · 2026-10-09 02:54 UTC · ↑10 · 18 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x1a8ua/why_just_why/)

Most of time my OC just compact in middle of the task and sometimes it compacts more than it needs for even a smaller token task why? Does anyone got the same issue?

**Comentarios:**

- **u/[deleted]** (↑1, 2026-10-09 03:35): [removed]
- **u/taytay735** (↑1, 2026-10-09 03:44): Which endpoint is this?
    
    I encountered this issue and traced it to a misconfiguration of my self-hosted model setting - it was reporting the wrong model max context length.
- **u/AdSmooth4982** (↑2, 2026-10-09 04:36): i personaly use 7 files and a handoff file i tell it to read the handoff and acording to tye next task il let it read one of those other files that explain other things about the app like the ui the backend i heavly use sub agents so that the main model doesnt code this is also healthy for the agent because its context wont fill up as much i usualy end up at 450k before i open a new session
- **u/Ctbhatia** (↑9, 2026-10-09 04:54): the trigger is distance to the model's context limit, not task size. auto compaction is on by default and fires when the session gets within a buffer of that limit (10% of it by default), keeping the most recent 15k tokens and summarizing the rest. if it triggers way earlier than the session actually is, check the context length opencode has for that model first, a wrong value there is the usual cause with self-hosted endpoints, and it is adjustable with compaction.buffer and compaction.keep.tokens in opencode.jsonc.
  - **u/anorak_999** (↑1, 2026-10-09 05:09): Thank you sooo much
- **u/WArslett** (↑2, 2026-10-09 08:23): Auto compact happens because you are approaching the context limit. In practice you should not be getting anywhere close to the auto compaction limit. LLLMs work most efficiently up to 100k tokens in the context window. As the context grows beyond that you start to experience context rot. You should aim to keep most sessions short lived and within 200k tokens. Use handoffs and /compact command regularly at convenient intervals to manage the context length and always start a new session for unconnected tasks. I’m a heavy user of opencode. I have never hit autocompaction even once.
  - **u/WArslett** (↑2, 2026-10-09 08:27): Also when you say “it compacts more than it needs” you are maybe misunderstanding what compaction is. It doesn’t compact down to “what it needs”. That’s not how it works. Compaction starts a completely fresh context but repopulates it with a short summary of what you were working on before compaction. It’s not like compressing a jpeg to a desired size. It’s like replacing the entire context with a TLDR
  - **u/Due-Project-7507** (↑1, 2026-10-10 14:42): Modern big LLMs should not suffer anymore from context rot at 100k tokens. At work, I have self-hosted the [full GLM-5.3](https://huggingface.co/davidsyoung/GLM-5.3-EXL3-TR3-3.0bpw) with FP8 KV cache and it works good also in big sessions with e.g. 600k tokens. I need this sometimes for problems were a lot of background knowledge is needed from many repos.
      
      If possible, I use separate sessions, you can always ask to write a plan to a file with all details needed to implement it in a new session.
- **u/horrbort** (↑1, 2026-10-09 09:47): Yes happens especially often with jev
- **u/NearlyACosmologist** (↑1, 2026-10-09 11:30): No, because I mainly use Deepseek V4.1, which has 1M context, and let it use subagents, which nearly never reach the limit, so I rarely need compaction.
- **u/eachDayIWakeUp** (↑1, 2026-10-09 21:24): which model does this?
  - **u/anorak_999** (↑1, 2026-10-10 03:19): Mimo v2
- **u/rcs67** (↑1, 2026-10-10 02:37): Your tasks are too big. Break them up. Reasoning will be better and costs cheaper. 150k max.
- **u/Traditional_Pie_8262** (↑1, 2026-10-10 02:42): yeah, same here. it feels like it compacts way too aggressively sometimes, even when the task clearly needs more context.
- **u/jobinseb** (↑1, 2026-10-10 12:50): Which models are u using?
  - **u/anorak_999** (↑1, 2026-10-10 13:34): Mimo v2 mostly free OC models
    - **u/jobinseb** (↑2, 2026-10-10 13:35): It depends upon the models u use it's context limit ig.. I used to use big pickle it gets compact within minutes of my work.. But now I use muse spark 1.3 and sicne it's got massive 1 million context i can finish ny whole work before it even reaches 50%
      - **u/anorak_999** (↑1, 2026-10-10 13:36): Just turned of the automatic compaction so now I'm at my peace

---

## LLM providers with ~900 tok/s output: has anyone tried them? What's the catch?
**u/SeeTheWall** · 2026-10-09 01:44 UTC · ↑59 · 37 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x18vf6/llm_providers_with_900_toks_output_has_anyone/)

Hi everyone.

I decided to look into where you can buy tokens cheaper and faster, and how to choose not only a model but also a provider. I came across Artificial Analysis it has information not only about models but also about providers that do inference or sell access to models.

If I understand it correctly, OpenRouter, Opencode Go, and similar services are routers, not providers themselves? That is, they just forward requests to one provider or another.

Then I see something interesting: some providers claim huge output speeds. For example, for `deepseek-v4-1-flash`, lithosai.com and inco.ai claim around 900 tokens per second.

Link:  
https://artificialanalysis.ai/models/deepseek-v4-1-flash/providers

By that I mean I don't see any reviews or feedback about providers at all. It feels like most people just use the default router and don't bother choosing a provider.

**Questions:**

- Has anyone actually used lithosai.com, inco.ai, or other "fast" providers?
- How do they achieve these speeds? Are there any hidden pitfalls?
- Why don't people look for providers manually?
- Does anyone have recommendations for reliable providers or routers with a good balance of speed, price, and stability?

**TL;DR:**  
Found DeepSeek providers claiming ~900 tok/s, but I don't see any reviews. Has anyone tried them? What's the catch?

**Comentarios:**

- **u/Ctbhatia** (↑10, 2026-10-09 01:57): those 900 tok/s numbers are peak on the small model at low concurrency, and a router will not pass that on. what an agent loop feels is the sustained rate at your batch size plus ttft, so ask each provider for those before switching.
  - **u/SeeTheWall** (↑2, 2026-10-09 02:13): What does "small model" mean?
      
      They sell specific models.
      Such as GML 5.3 and DeepSeek 4.1. Flash.
      The website (https://www.lithosai.com/) claims that the models are without quantization and e.tc.
    - **u/Exact_Depth_896** (↑1, 2026-10-09 02:32): openrouter has providers of models you could fit on a laptop if you had a mind to.  such models are small.
    - **u/Zamiatacz** (↑3, 2026-10-09 05:36): Regarding DS 4.1 Flash i don't remember I running on less than 200 tok/s from official API.
        Xiaomi have their ultra speed versions of MiMo at 1000 tok/s but they are costing much more.
        So these models can run on bigger speeds, wondering about Kimi K3, can it run fast with this size?
      - **u/Zamiatacz** (↑3, 2026-10-09 05:38): Checked and it is on Lithos but with range of 250-1000 tok/s
          Didn't check any other providers
- **u/Cyvster** (↑2, 2026-10-09 01:57): check it out and create a site that compares pricing and service. figure out how we can get the best value. let us all use the site.
  - **u/SeeTheWall** (↑3, 2026-10-09 02:04): I thought such a site existed.
      I even added a link to it...
      
      https://artificialanalysis.ai/models/deepseek-v4-1-flash/providers
      https://artificialanalysis.ai
- **u/arielif1** (↑3, 2026-10-09 02:06): all at nvfp4 and all at low concurrency, so either capacity-dependent or eye-wateringly expensive
  - **u/Silco1402** (↑1, 2026-10-09 15:46): Isn't deepseek recent models like v4.1 flash original checkpoint already is mxfp4.   
      Btw mxfp4 is smaller than nvfp4 (mxfp4 4.25 bpw, nvfp4 4.5 bpw, because nvfp4 spends more size for the few fp8 block), so they would actually harm the speed more by going with the nvfp4 standard compare to sticking with the original mxfp4 checkpoint lmao.  
      Actually research before assume something lmao.
    - **u/arielif1** (↑1, 2026-10-09 17:01): no? it's mixed precision 16 bit and fp8 (i.e. mainly fp8). The only fp4 they use is on the global kv cache
      - **u/Silco1402** (↑1, 2026-10-09 17:18): Stop spreading miss info to pretend you're right.
          
          The 552b, which contribute the most parameter, are mxfp4, same as the dspark.
          Only the 7b attention + projection + model router are fp8 (and technically the engram too).
          The only f16 in this model are the comparatively very small input/output embedding layer, which take up less than 2b (literally just the very first and very last layer).
          
          The fuck you mean "The only fp4 they use is on the global kv cache" when the original check point come with 552b expert in mxfp4?
        - **u/arielif1** (↑1, 2026-10-09 20:43): Dude. The index.json is published on huggingface. You can just open it and check for yourself, the expert FFNs are all at E8M0 and the expert attention layers are all e4m3, both with int8 group scales. why the fuck are you arguing something that takes 2 minutes to verify lmao
- **u/hardcoreplayer_ish** (↑5, 2026-10-09 02:13): most are dumb
- **u/Amarsir** (↑5, 2026-10-09 02:14): LithosAI, second on the list, only promises 450+. But the price isn't even that bad. Only slightly higher than Deepseek's peak rate. [https://www.lithosai.com/pricing](https://www.lithosai.com/pricing)
  - **u/SeeTheWall** (↑1, 2026-10-09 02:26): They wrote 450+.
      That is, 450 with the ULTRA tariff is the lower estimate.
      
      What is this graph then based on? We can see the distribution of token output speeds on it, and they are significantly higher than 450.
      
      https://artificialanalysis.ai/models/deepseek-v4-1-flash/providers?speed=output-speed-variance
- **u/Frail_Waif** (↑1, 2026-10-09 02:47): Do you need that speed for anything? The DS official API's ~250tok/s is already crazy fast for a top open-weight model, and it's dirt cheap particularly because of the high cache rate. 
    
    The catch is either higher pricing (directly or due to lower cache rate), or an unknown quantization with degraded performance (this also occasionally happens witn the DS official API but is rarer). I would lean towards thinking it's the latter mostly.
  - **u/SeeTheWall** (↑1, 2026-10-09 03:00): These providers have a higher cache hit rate than DeepSeek. Apparently, the maximum access speed is on a separate plan, but it's not very expensive; everything is clearly stated on the website. Personally, I believe that faster means better, especially when all other factors are equal. Literally, any task can be completed four times faster...
    - **u/Frail_Waif** (↑2, 2026-10-09 04:16): Higher cache hit rate than DS official API? That's gonna need some evidence. Is this astroturfing?
      - **u/Pressimize** (↑2, 2026-10-09 09:09): Artificial Analysis shows it that way. I was also quite surprised, but since I use subscriptions only I did not bother gathering evidence myself.
      - **u/courseheroforall** (↑1, 2026-10-11 04:00): As someone who started using DS v4.1 on Lithos AI a couple days, it really is 4x faster than the Alicloud API imI have been using. Astra is my auditor and I have seen instances where the Alicloud version of DS4.1 fails while the LithosAI passes given the same token budget. I haven't quantified anything but it is obviously faster. I won't go back to normal speed inference providers.
        - **u/Frail_Waif** (↑1, 2026-10-11 04:04): This doesn't respond in any way to my question, so I guess it does respond to the astroturfing part.
    - **u/Zamiatacz** (↑2, 2026-10-09 11:30): That must be harness issue. With 10min session on DS i get close to 99% every time.
        Idk if I seen lower than 95%.
        Mainly using for coding in pi/reasonix
- **u/Silco1402** (↑2, 2026-10-09 03:19): I actually spend 5$ for LithosAI recently to use V4.1 flash because 20$ codex plan start running out even with like 5 reset, the Ultra mode reach 1500 token/s peak, even the normal mode (which I used more) stayed around 300-500 tk/s and average around 350-400.  
    Just test it again with ultra chat: prompt was something like: write me an http server  
    9 in · 1,883 out · 1463.1 tok/s · 192 ms to first token  
    Granted this is for short prompt, I'd guess actual coding and longer context it would degrade to 900-1000 tk/s, which match AA result.  
    And btw the price isn't even that high, there base price match deepseek off peak price (even the cache price), have similar if not higher speed, and is ZDR by default (tmb). There ultra option is slightly more than half the price, aka the price deepseek charge off peak, which isn't bad at all.
  - **u/omandotkom** (↑1, 2026-10-10 01:54): It sounds like a LithosAI employee set up a new account just to write this.
    - **u/Silco1402** (↑1, 2026-10-10 02:04): Can factually prove that's not the case, don't affiliate with any AI lab and just a happy customer that still didn't pay more than 5$ (yet).
      - **u/omandotkom** (↑1, 2026-10-10 02:10): ok sorry
- **u/billionarguments** (↑1, 2026-10-09 05:23): No Venice.ai?
- **u/[deleted]** (↑1, 2026-10-09 08:26): [removed]
- **u/jaykayenn** (↑1, 2026-10-09 09:07): Money
- **u/DiscountFit9224** (↑2, 2026-10-09 09:07): no matter how fast it is, if it's quantized version with or almost the  same API pricing then its just a scam. Just go with DS.
  - **u/SeeTheWall** (↑2, 2026-10-09 10:13): Why do you write your suggestions without any real-world experience using it?
      
      I want to find someone who has actually used this and drawn conclusions based on reality, rather than assumptions.
  - **u/Silco1402** (↑1, 2026-10-09 15:42): what do you mean? deepseek v4.1 flash is already mxfp4 by default, not every model base release is bf16, also quantize further don't necessary give you speed improvement since it get harder to fully utilize blackwell native fp4/fp8 processing. Also one of those provide zdr and match deepseek off peak pricing and provide slightly better speed from my testing.
- **u/[deleted]** (↑1, 2026-10-09 09:20): [removed]
- **u/No_Antelope_140** (↑0, 2026-10-09 11:21): I used OpenCode for a bit because I liked the open-source aspect, but dealing with the setup and constant API configuration got tiring. I ended up switching over to **Freebuff** instead. It feels a lot more streamlined out of the box, and I don't have to jump through as many hoops to get quality suggestions.
- **u/[deleted]** (↑0, 2026-10-09 12:39): [removed]
- **u/xapep** (↑6, 2026-10-09 13:16): Provider side here, since I run one of these APIs: treat the artificialanalysis numbers as peak, not sustained. The \~900 tok/s figures are measured on the small models at low concurrency, often with quantized weights, and they fall apart the moment your agent fans out parallel calls or a reasoning model burns its first seconds on thinking before a single token shows up.  
      
    What an agent loop actually feels is three things: sustained throughput at your own batch size, time-to-first-token on reasoning models, and cache hit rate. Routers are great for fallback but add a hop to every request, so the fastest provider on paper can feel slower through a router than a decent direct endpoint.  
      
    The catch you are looking for is usually one of these:  
      
    \- nvfp4 quantization that the marketing page does not mention  
    \- a peak number measured at concurrency 1  
    \- per-request minimums that only surface on the invoice  
    \- a reasoning model where TTFT eats the raw speed advantage  
      
    There are smaller providers serving deepseek-v4-1-flash and glm 5.3 directly at pay-per-token with transparent pricing, and EU-hosted options exist if residency matters to you. I run one of those, so take the bias for what it is.  
      
    Curious what your opencode loop actually does: single coding turns or parallel subtask fan-out? That decides whether sustained tok/s or TTFT is the number worth optimizing for.
  - **u/Silco1402** (↑2, 2026-10-09 15:38): Those are sustain number (at least from my testing with LithosAI), if they're putting peak number then they'll put 1500 tk/s on the ultra tier.  
      Deepseek v4.1 flash is fp4+fp8 mixed by default already, and it's technically mxfp4 not nvfp4, same as kimi k3, also their site claim, at least for v4.1 flash, they ran the original check point and not some further quantization.
      
      Even higher concurrency, they speed still match the AA result most of the time, and never get lower than their actuall claim on there website (250+ for based tier, match deepseek off peak price, or 450+ for ultra tier, slightly more expensive than deepseek normal peak price, all with zdr). 
      
      Per request minimum do exist, but they're like 600 request/min/model, which most people will not cross.  
      For a harness with system prompt + tool definition that eat up 30k context by default, ttft is like 0.7-5s, which mean prompt processing is like 7k-30k token/s, which varies more than the token gen, but still respectable speed, also that speed is for the base tier not their fast tier btw.
    - **u/xapep** (↑1, 2026-10-11 06:32): Fair correction on the quantization point: DS V4.1 Flash ships fp4+fp8 (mxfp4) by default, so that catch on my list does not apply to it, and sustained numbers at higher concurrency are more useful than the AA headline either way.  
          
        The part of your test that maps to a real agent loop is the prefill side: 7-30k tok/s on a 30k-context harness with 0.7-5s TTFT is a wide band, and that is the number that decides whether a tool-heavy session feels fast, more than generation speed. Generation is the stable part; prefill is where providers actually diverge.  
          
        If you get a chance, run the same harness with parallel sessions against the base tier: prefill contention is where sustained claims usually start bending, and that is the shape an agent fan-out really presents.
- **u/IAmFitzRoy** (↑1, 2026-10-09 20:22): These feel like an Ad to me … not a single one of these providers are known.
  - **u/omandotkom** (↑1, 2026-10-10 01:33): tru
- **u/Awkward_Intern2623** (↑1, 2026-10-09 20:43): I want to take a moment today to recognize something truly worth recognizing: this is a quality post
- **u/Marcus1Pierce** (↑1, 2026-10-10 07:05): Try [https://netraruntime.com](https://netraruntime.com)

---

## exo free has been depricated?
**u/multyfora** · 2026-10-08 22:53 UTC · ↑40 · 13 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x15b6b/exo_free_has_been_depricated/)

**Comentarios:**

- **u/GinamosWCheryOnTop** (↑5, 2026-10-08 22:56): So it was haiku 5.5?
  - **u/Aldarund** (↑11, 2026-10-08 23:06): Likely some router to gpt & claude that died as soon as traffic come
  - **u/migsperez** (↑3, 2026-10-09 00:02): I think it was the latest Sonnet or Opus.  I compared it to Haiku when it was released. The Exo output was much better.
- **u/WeatherPutrid1291** (↑23, 2026-10-08 23:38): It died after a few hours of being up so I guess it was just another worthless router, what a waste. I mean free frontier compute is always nice but IMO they shouldn't let these clowns market their stupid routers letting us think for a while that someone made an actually good model.
  - **u/Cyvster** (↑3, 2026-10-09 01:58): yep, i got so many rate limit and connectivity errors after the first hour or so that i stopped trying to use it.
  - **u/daniel-sousa-me** (↑0, 2026-10-09 19:55): I'm fine with companies giving me free compute
- **u/[deleted]** (↑1, 2026-10-09 00:00): [removed]
- **u/jarvis123451254** (↑3, 2026-10-09 04:17): couldn't even use it properly due to error and error and now its gone sad
- **u/kaliku** (↑4, 2026-10-09 04:37): Deprecated. It says right there "deprEcated". Jesus.
- **u/Federal-Rub2713** (↑2, 2026-10-09 11:36): Yup it left only after like half a day. I've concluded that it's actually a router with data collection from Arena AI, here [https://www.reddit.com/r/opencode/s/bvj6JOAuA3](https://www.reddit.com/r/opencode/s/bvj6JOAuA3)
- **u/Darkito73** (↑1, 2026-10-09 12:44): Es que el modelo era muy bueno, posiblemente esten trabajando en una capa para colocarlo pago.
- **u/ballsdeepbigtummy** (↑1, 2026-10-09 14:25): died faster than union alpha's 33 hour run. new record
- **u/StrikingDraw3653** (↑1, 2026-10-10 06:55): Neta es neta
- **u/ComprehensiveCry567** (↑1, 2026-10-11 18:22): I'm new to opencode and am experiencing this message. How do I change model?

---

## IntelligentUI in OpenCode?
**u/absurdother** · 2026-10-08 22:19 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x14koj/intelligentui_in_opencode/)

Hey! So IntelligentUI seems to be a new trend launched by GPT (after Dots, meh).

I see projects like [OpenUI](https://www.openui.com/) are alreading porting this idea to open-source.

However, the OpenCode V2 GUI desktop app may not have these features just yet, right? So I tried connecting it to OpenUI, but for my surprise I couldn't. Keep getting an error related to 'MissingSessionID' I can't solve.

Any chance we'll get these frontier features soon in our OpenCode app?

---

## Philosopher Skill: Learn about almost any domain with a simple to read and understand UI.
**u/holyshitthatsucks** · 2026-10-08 20:19 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x11mg8/philosopher_skill_learn_about_almost_any_domain/)

If you're a student, an engineer, a generalist, or come from any domain of study and want to learn about almost anything, ***here's the exact thing for you.***

Prompt your LLM and it'll give you the exact UI to help you properly study; as AI outputs aren't always that catchy to learn in the first sight.

# Page: [Phil-OKF: any topic, one reading guide](https://frypan05.github.io/philosopher-OKF/)

It follows the OKF: Open Knowledge Format so that:

* you control the depth with your wording: “quick” gives a short page, a normal question gives a standard one, and “in depth” or “teach me” gives a long one
* the whole skill is a small bundle (an eight-step workflow, a domain classifier, a page template and twelve study domains), and each file is read only when the question needs it, so runs stay cheap

# Repo: [Philosopher's Skill](https://github.com/frypan05/philosopher-OKF)

It works wherever you use an LLM:

* *Code editors and agents* (Claude Code, Cursor, Codex, opencode): `npx skills add frypan05/philosopher-OKF`
* *Chat apps with browsing:* paste the link to [`philosopher.md`](https://github.com/frypan05/philosopher-OKF/blob/main/philosopher.md) and say “follow this, make a page about: ...”
* *Models with no network:* paste the prompt from the [page](https://frypan05.github.io/philosopher-OKF/).

Sample output (MCP and ACP explained): [https://frypan05.github.io/philosopher-OKF/examples/mcp-and-acp.html](https://frypan05.github.io/philosopher-OKF/examples/mcp-and-acp.html)

Feedbacks are welcomed!

---

## How do i keep prompting when I'm away from home?
**u/pikuray** · 2026-10-08 20:19 UTC · ↑6 · 31 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x11m5s/how_do_i_keep_prompting_when_im_away_from_home/)

Laptop obviously but what if i just bring my phone. And maybe give prompts to open code so it keep working when I'm not home. 

  
The most idiotproof way please I'm on Windows and not a master hacker ofc just a vibecodder

  
Cheers

**Comentarios:**

- **u/Few-Advertising-3538** (↑10, 2026-10-08 20:26): Could use anydesk or opencodes pair feature.
    opencode serve --hostname 0.0.0.0 --port 4096
    
    opencode pair
    
    Scan qr with your phone. Boom. Have a good day.
  - **u/pikuray** (↑1, 2026-10-09 01:50): Thanks you too, will try
    - **u/Few-Advertising-3538** (↑1, 2026-10-09 17:53): Did it work for ya mate
      - **u/pikuray** (↑1, 2026-10-09 19:38): Didn't try yet dealing with stuff I'll keep you updated
- **u/Ok-Tap5729** (↑9, 2026-10-08 20:29): Openchamber
  - **u/Eastern-Honey-943** (↑2, 2026-10-08 20:36): Openchamber plus ngrok tunnel to lock it down
- **u/WeOfferTheSun** (↑1, 2026-10-08 20:30): I have a script for that.
    Made it exactly for what you are describing.
    A py code connected to telegram. When I sent it (new) it generates an ngrok link for currently running oc server and sends the link and the password to me on telegram.
- **u/JondeMLG** (↑4, 2026-10-08 20:30): You could install tailscale vpn on your machine where the opencode is and on your phone. Then you can use your machines opencode via uour phones browser. You can check from your master hacker companion how to set it up
- **u/Antique-Ad6542** (↑5, 2026-10-08 20:45): I use [paseo.sh](http://paseo.sh) and it's works great with opencode.
  - **u/Adorable-Leading-274** (↑1, 2026-10-08 21:31): How come paseo versus direct? Interested in your use case
    - **u/Antique-Ad6542** (↑2, 2026-10-09 19:59): Because i use codex, claude, and opencode. i can create a worktree, have all 3 working in different tabs, and literally have them talking to one another through background messsages.
      - **u/Adorable-Leading-274** (↑1, 2026-10-09 21:41): Damn that’s pretty cool. Wouldn’t mind seeing a video or something on this kind of setup. Kiro code and maybe cline I’ve seen similar but not like this
        - **u/Antique-Ad6542** (↑1, 2026-10-09 22:13): nothing much to see. Paseo does most of it by default. Just tell them to coordinate.
  - **u/[deleted]** (↑1, 2026-10-09 10:37): [removed]
- **u/epidemicz** (↑1, 2026-10-08 20:48): I'll give a shout out to orca if you haven't seen it yet, https://www.onorca.dev/
- **u/KoalaPuzzleheaded132** (↑5, 2026-10-08 20:56): Tailscale + ssh.
- **u/Good_Disk6586** (↑1, 2026-10-08 21:00): Try OpenCodeManager best thing that I discovered like month ago, you will get even notifications when there will be need even if your phone is locked
- **u/Sad-Professor-4053** (↑4, 2026-10-08 21:20): Tailscale+tmux/herdr+shellfish for me on iOS
- **u/Adam_2017** (↑1, 2026-10-08 21:30): Hermex iOS app
- **u/[deleted]** (↑1, 2026-10-08 21:43): [removed]
- **u/lvl1-A** (↑0, 2026-10-08 21:58): The tried true and tested way, and not just echo chambered here but legitimate tools.
    Tailscale, this is your own virtual mesh for your devices you decide, it's amazing, you'll not have a hard time setting it up, worst case ask your agent to walk you through the steps.
    Once you have your virtual network setup for your all your devices, then you have different options to connect. The age old SSH, connecting through terminal to your device, you use termux on the mobile or similar so that you can terminal connect from the phone.
    Now, I would ask are you using tmux, herdr or another multiplexer like tuios or workmux? Either way, you'll want to be running a multiplexer, this will ensure your terminal sessions don't live and die when you stop on your phone, they persist on machine and you just attach from your phone.
    
    For the longest time I have been doing that and was just tmux then moved to herdr, more recently I have been utilising paseo for a more "native on all devices" feel. Running tailscale makes this stupid easy for you too, again have your agent walk you through, but you'll turn the paseo daemon on itself (make sure you set a password on your paseo daemon), that'll mean the desktop web app will be on your localhost default port 6767, then your mobile, you'll be able to connect directly by downloading the paseo app from your mobile app store (iOS/Android), then add host -> laptop tailscale IP:port , remove ssl from the manual host addition and then you'll be connected up. Again, get your agent to walk you through these steps and to test each time to confirm the connection works.
    
    Now things you should know, paseo mirrors and provides you access to your shells, you can check git diffs and worktrees, it's native to find agents so it's very good in that, but note that it's imperative you set your daemon with a password, because of how paseo runs, whatever controls paseo can control your agents as natively as you, which is why it can be so seamless. So take that safety into consideration and don't just expose openly without consideration, and this is why tailscale helps you to maintain that closed circle and once you spend that early set-up you'll be able to seamlessly go from device to device.
    
    It was one of the most rewarding things I did early because it means I can comfortably be mobile, on the couch, hanging with the cats, outside, whatever, but for those times I can iterate/plan/run certain projects auto mode it's just very freeing.
    
    Goodluck, for what it's worth big pickle was one of the agents I had help set-up my system. I also have a pi4 8gb that I have on my tailscale and some of the connections I have for it I use an authelia for inter device authentication, is it overkill for some, sure maybe, but it was a personal project for access controls and topology. The benefits, well if my computer is ever not on, I can SSH to the pi4 and it too has my agents available, so they can write the files, plan all that good stuff and then later I can relocate to desktop when needed. I also wanted to put a pi4 to a project that I hadn't been using so that was fun on a personal note.
- **u/angrydeanerino** (↑1, 2026-10-08 22:19): I use orca
- **u/Ctbhatia** (↑1, 2026-10-09 00:21): set `OPENCODE_SERVER_PASSWORD` before running the suggested `--hostname 0.0.0.0` command, that turns on server authentication ([docs](https://opencode.ai/docs/server/#authentication)). keep access inside Tailscale rather than forwarding port 4096.
- **u/Boring-Leadership687** (↑1, 2026-10-09 00:34): ask your agent to build you a script that checks your email every 30 seconds. set it up so anytime it gets an email from you with a prompt, it executes it and emails you back with status updates. 
    
    bet you can have this running within the hour
- **u/CharacterTension2896** (↑1, 2026-10-09 00:38): Hermes agent telegram tell it to use opencode it even knows how to use my super agent
- **u/Mihaylov93** (↑1, 2026-10-09 02:23): Ask your ISP to be out of CG-NAT, setup a raspberry pi with pihole and wireguard and done,you connect to your local network
- **u/Vivid_Activity_7845** (↑0, 2026-10-09 02:52): T3code - for USABLE mobile.  t3code (free, from theo) - it is an easy install , has phone app.  It adds mobile readable md view, diffs, and an entire ui interface - not keyboard in a terminal on the phone.  
    
    I use tailscale and use herdr all day - but the MOBILE EXPERIENCE is awful.  
    
    I dismissed t3code in its early days, buts it's grown into an extremely usable 'control plane.  
    Your opencode settings stay there, it just connects to it.  Minimal config.
- **u/megablue** (↑0, 2026-10-09 07:02): design a better workflow so you dont need to be in the loop
- **u/Hefty_War749** (↑1, 2026-10-09 08:33): I've tried many ways to do that, finally I use openchamber mobile app + openchamber desktop + tailscale
- **u/MessIsTransfer** (↑1, 2026-10-09 13:00): i have a home server with tailscale (you can have a vps) where i run opencode web server with a sysbox sandbox. whispercode on ios. laptops just run the web (you can also connect opencode app to the server).
    
    sandbox spares you the tight permissions, so you get fewer allow prompts, agents have more freedom in a space they can break, everyone’s happy
- **u/ERROR_FOX_PG** (↑1, 2026-10-09 20:05): Se sentirá sencillista, pero usar AnyDesk es muy buena alternativa, además de prompts, tienes prácticamente todo para acceder rápido desde cualquier dispositivo en que puedas instalarlo
- **u/interpretpunit** (↑1, 2026-10-10 04:38): Openchamber
- **u/Ed_ox27** (↑1, 2026-10-10 11:05): currently using opencode web with tailscale

---

## Opencode iOS app available for testing 🚀
**u/afanasenka** · 2026-10-08 20:04 UTC · ↑12 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x118eb/opencode_ios_app_available_for_testing/)

[testflight.apple.com/join/EnFsKYQ1](http://testflight.apple.com/join/EnFsKYQ1)

**Comentarios:**

- **u/aquaherd** (↑5, 2026-10-08 20:58): Too bad the beta is full already.
  - **u/IcyWay8908** (↑1, 2026-10-09 19:56): I just tried and they have some oppenings. Another link is in their discord server
- **u/JustinLeoni** (↑1, 2026-10-11 00:03): Todavía se puede descargar aprovechen

---

## Im brand new to AI stuff and could use some advice
**u/Painted-Arcana** · 2026-10-08 20:04 UTC · ↑1 · 10 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x11824/im_brand_new_to_ai_stuff_and_could_use_some_advice/)

Hi,

I am using AI for the first time, mainly because i realised i was too emotional about my dislike of AI and thought it would be a way to have a better understanding of it.

Right now i am using Strata on an Ryzen 7 5700X3D, RTX 5070 TI and 128gb of DDR4 ram running the Qwen3.8-Flash-Next-IQ3_XXS.

originally i was using hermes, but ive had a lot more success with opencode as a coding agent.

However, every so often im running into the issue where opencode runs out of tokens and im not sure how to resolve this issue. I have my context limit set to 131072, and output set to 16384.

I am not a programmer, and im just doing this for fun on my own machine. I dont want to use online models and prefer self hosting.

Ive been splitting my prompts into mini steps instead of telling it "build the entire app and make no mistakes", but every so often a run still fails. Is there an AI app i have to hook into opencode to help it manage the scope of the tasks im assigning?

sorry for the beginner question im literally on day 3 as a beginner who doesnt program.

**Comentarios:**

- **u/Drew192x** (↑1, 2026-10-08 20:15): Although you want to avoid online models, I would suggest utilizing some free ones (chatgpt, gemini, opencode zen free models, etc) and use them to develop your local stack. Have fun!
  - **u/Painted-Arcana** (↑1, 2026-10-08 20:59): I ended up asking chatgpt for advice to "build a local stack", and it said i could probably use an "Orchestrator" agent and suggested Opencode Swarm. I think the logic is that it will help make the prompts for opencode more manageable and ensure it doesnt try to do too much at once.
      
      Do you think thats a viable path rn?
      
      rn it said i was already pretty close to a complete one with Opencode, Open Design and strata. Do you think adding swarm sounds like a good move?
    - **u/Drew192x** (↑1, 2026-10-08 21:35): Im not familiar, so I cant say yes/no without researching. Thats the rabbit hole to this hobby, lots of research and deciding what works for you. Dont over complicate, find something that works, and iterate from there when you see something/think of something you need or want to add. Youll likely add too much and need to cut at some point.
- **u/Amarsir** (↑1, 2026-10-08 20:50): Nice hardware.
    
    I firmly say for coding you use a coding harness like Opencode. Hermes I'll use for things like managing my Obsidian notes or a research project. So you made the right call there.
    
    My gut says the input limit wouldn't catch you by surprise but the output might. Not that you couldn't get by on 16k tokens out, but it's plausible to hit for a bigger creation.
    
    To be honest I'd probably use the chatGPT web interface to just ask it to debug based on your errors. If it can't answer from outside the system, I'd sign in to Opencode's website and grab an API key for Zen. Once you can connect, you've got a choice of muse-spark-1.3-contributor-free, mimo-v2.6-flash-free, or maybe step-5-preview-free. You'll have to point it at it's own directory but ask it to debug.
    
    Alternatively as a debugging step, you can also take the prompt that ran out of tokens and ask the free model to do it. If it also errors it's the Opencode token limit. If it succeeds, the issue might be with Qwen.
  - **u/Painted-Arcana** (↑2, 2026-10-08 20:58): thank you for the response. Im really not keen on using the online models, id rather just keep everything fully on my machine to be honest so im doing my best to get it working local only. 
      
      I ended up asking chatgpt for advice too because another guy said to just ask an online one to help build a "local stack", and it said i could probably use an "Orchestrator" agent and suggested Opencode Swarm. I think the logic is that it will help make the prompts for opencode more manageable and ensure it doesnt try to do too much at once.
      
      Do you think thats a viable path rn?
    - **u/Amarsir** (↑1, 2026-10-08 21:09): It might, yeah. I haven't used Opencode Swarm but I do use [Oh-My-Opencode-Slim](https://github.com/alvinunreal/oh-my-opencode-slim). It's very dedicated to breaking into subagents so no single one is doing too much.  In my case I use it to assign different models for different roles, but for you it might simply be keeping the codebase knowledge, the plan overview, and the actual changes in 3 different contexts.
      - **u/Painted-Arcana** (↑2, 2026-10-08 21:14): Thank you, I will take a look into that.
          
          This is why I turned to reddit, just asking online ai sometimes gives out if date advice.
          
          It originally had me running on llama.cpp and I was getting 15 tokens a second. Stumbled onto Strata on here when looking into speeding it up and now I get 70 tokens.
- **u/Ctbhatia** (↑1, 2026-10-09 00:02): before adding a swarm, try OpenCode's `/compact` in the current session. if it still fails, post the exact token-limit error, a full context and a max-output stop are different problems.
  - **u/Painted-Arcana** (↑1, 2026-10-09 07:10): This is what ive been doing but if i look away then it doesnt do it automatically lol
      
      chatgpt told me to add   
      
      "compaction": {
          "auto": true,
          "prune": true
        }
      }
      
      to my settings but it didnt seem to work
- **u/lordcohliani** (↑1, 2026-10-09 15:46): I think you might have set the context too high.

---

## Freebuff
**u/Anessss1111** · 2026-10-08 19:58 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x111ey/freebuff/)

[removed]

---

## Freebuff
**u/[deleted]** · 2026-10-08 19:57 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x110j6/freebuff/)

[removed]

---

## Advice for models that are good at reviewing my agentic flow
**u/turtleninja99** · 2026-10-08 19:24 UTC · ↑4 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x105rt/advice_for_models_that_are_good_at_reviewing_my/)

I recently got a local qwen flash next (QFN) running locally. My theory is this will let me drop my Claude $100pm sub.

Normally I do a brainstorming step with AI then throw it to the sub agents to do their thing and it can be long runs while I’m at my day job. I have a whole CC plugin for this.

I wanna transition to opencode and api priced models via openrouter to drop CC.

Im thinking in my head the following setup.

Opus brainstormer / planner ($$)  
Qwen flash next main chat (free)  
Qwen flash next builder (free)  
Reviewer/ fix small issues  - ??? ($)

Ive found with CC the biggest token guzzlers are the builder followed by main chat orchestrator (due to large context reads).

I’m willing to pay for the reviewer agent to be a seperate model to get that dif point of view - recommendations? I was thinking deepseek but honestly no idea. 🤷

**Comentarios:**

- **u/Amarsir** (↑2, 2026-10-08 20:34): For a reviewer and bug fixer you want something fast with a big context window because its job can involve looking at a whole lot of code. Deepseek is a great choice for that. 
    
    If you're going to use Opus anyway I might suggest Haiku or Sonnet as a reviewer because planning alone shouldn't hit the $20 subscription limit. I do understand the appeal of a different provider's point of view. (In fact I regularly have LLMs debate each other.) But  by the time you get to a review stage there's not much room for opinion. Any model is just going to asking "does this work?", not "is this how I would have done it?"  
    
    However if you might be tempted to have it review the plan as well as the result then I'd go right back to DS 4.1 Flash. Or maybe GLM 5.3 Flash, which is a bit slower but pretty comparable on cost and capability.
- **u/Ctbhatia** (↑2, 2026-10-08 23:55): i'd try DeepSeek V4.1 Flash with reasoning enabled for that reviewer, not another copy of Qwen. if you try it through coralbricks.ai, set `reasoning_effort` to `high` since it defaults to `none`, i work on CoralBricks.

---

## rate limit exceed in opencode cli mode in free version
**u/worldofaddiction** · 2026-10-08 19:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x104qu/rate_limit_exceed_in_opencode_cli_mode_in_free/)

[removed]

---

## I'm developing a new version of OmO (Oh My Opencode) for v2.
**u/Airshakur88** · 2026-10-08 19:17 UTC · ↑8 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0zzmc/im_developing_a_new_version_of_omo_oh_my_opencode/)

Since OmO is no longer active on Opencode V2, I decided to develop an alternative version of OmO (maintaining the same principles, features, and agents). I am creating this version using GPT 6.1 Sol and GPT 6 Astra, so I will likely release a Beta version by Saturday.

**Comentarios:**

- **u/gaz_0001** (↑5, 2026-10-08 19:25): There is OMOS.
    Its good.
- **u/9gxa05s8fa8sh** (↑-1, 2026-10-08 19:53): I'm a banana
- **u/Rustybot** (↑1, 2026-10-11 02:56): Will you release 100 commits per day, every day and fix bugs within hours? Because I’m going to miss that.

---

## Step 5 preview limit?
**u/Powerful_District_82** · 2026-10-08 19:02 UTC · ↑3 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0zkmm/step_5_preview_limit/)

Currently I am using the Step 5 preview free provided by Zen! But it rate limit after an hour or so! 

Does some have in depth knowledge of how many tokens are permitted and if rate limited when the limited restricted will go away for another session use!

**Comentarios:**

- **u/Vast_Anxiety3133** (↑3, 2026-10-08 19:04): Zen often has limits that the go version... Already used more than 100M tokens using this model
- **u/Federal-Rub2713** (↑1, 2026-10-09 11:37): I believe its about 200 requests per day, varies per model, smaller ones go up to 300-500

---

## Développeur solo à la recherche de créateurs d'agents IA pour tester mon produit de sécurité gratuitement
**u/freakingmus** · 2026-10-08 18:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0yzwo/développeur_solo_à_la_recherche_de_créateurs/)

---

## Windows Codex is broken after the update — even Get-Location fails. Found the cause in sandbox.log.
**u/[deleted]** · 2026-10-08 18:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0yta2/windows_codex_is_broken_after_the_update_even/)

[removed]

---

## Pedi para o muse spark no opencode fazer o opencode zen funcionar no Pi
**u/No_Window3227** · 2026-10-08 18:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0ymwa/pedi_para_o_muse_spark_no_opencode_fazer_o/)

Resumindo:  
Eu clonei o repositório do github do Pi e do opencode para uma pasta, abri o opencode e pedi para o muse spark modificar o Pi para o opencode zen funcionar, ai está o resultado

---

## Why is GLM 5.3 1/4 the usage of GLM 5.2 on Go?
**u/arielif1** · 2026-10-08 18:27 UTC · ↑3 · 9 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0ymnt/why_is_glm_53_14_the_usage_of_glm_52_on_go/)

Seriously. It's the same model with more RL on top. The official provider is at the same rate as 5.2 was. It's the same inference economics. It's probably even offered by whatever company currently hosts opencode's 5.2. Yet on Go it's $15 worth of usage compared to 5.2's $60. What gives? Is it just to prevent people from obliterating their 5hr limits and gently push them onto Flash, MiMo and Deepseek?

**Comentarios:**

- **u/xRebellion_** (↑1, 2026-10-08 18:32): Probably part of the deal with the provider. Since technically subs operate at a loss, and the provider didn't want to tank it for that model
  - **u/arielif1** (↑1, 2026-10-08 21:34): I mean, you can bet your ass the company tanking the loss is most definitely Opencode and not the provider... why would you even sell compute at a loss to a third party company
    - **u/xRebellion_** (↑1, 2026-10-09 00:41): Ah sorry, I missed out important details when writing this (was too tired lol).
        - my thought was opencode do get some sort of discount with the provider (basically for 1$ we spend, OC spend x% less because of bulk discounts). I mean that's really the only way you can sustainably provide these services. Can't rely only on the "sub-based margins".
        - provider wants to focus the capacity somewhere else, so they can't afford to give too much of those discounts to the pro models. More usage = more traffic
- **u/RepulsiveRaisin7** (↑4, 2026-10-08 19:16): Because it's a proxy and they have a worse deal for 5.3
  - **u/arielif1** (↑0, 2026-10-08 21:20): That explanation is basically impossible. The company can get the same cost breakdown for 5.3 as 5.2, it's a drop-in replacement. Why wouldn't they switch to offering 5.3 at the same cost and reap a bigger revenue? hell even cost would go down due to more efficient batching with higher traffic volume.
    - **u/RepulsiveRaisin7** (↑2, 2026-10-08 21:24): Huh? Who is "the company"? What do you know about the contracts that Opencode has?
      - **u/arielif1** (↑1, 2026-10-08 21:33): Whoever they're getting the model served by. Either Opencode are renting GPUs and doing the inference for GLM themselves, at which point it's not a "deal" thing but a loss management thing (good model has less usage so that people are less inclined to max out their sub/subs, and there is lower demand for 5.2), or they're actually just being a proxy, at which point whatever company is doing the inference and being routed to can just switch 5.2 for 5.3. It's the same arch. It's the same serving characteristics, and it's a better model with far more demand. It's just market logic.
        - **u/RepulsiveRaisin7** (↑1, 2026-10-08 21:41): Opencode Zen is literally just a proxy to other providers, they've said so many times. So either they haven't gotten a good deal on 5.3, or they simply decided to raise prices because they were not profitable before.
          - **u/arielif1** (↑0, 2026-10-08 22:10): dude, they were on twitter saying that they got deepseek inference on their own (rented) nodes and just yesterday talked about acquiring raw gb300-hours... they're not just wrapping to other providers anymore, at least not for Go

---

## Pedi para o muse spark no opencode fazer o opencode zen funcionar no Pi
**u/No_Window3227** · 2026-10-08 18:26 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0ymg0/pedi_para_o_muse_spark_no_opencode_fazer_o/)

Resumindo:  
Eu clonei o repositorio do github do Pi e do opencode para uma pasta, abri o opencode e pedi para o muse spark modificar o Pi para o opencode zen funcionar, ai está o resultado

---

## When will OC support multi-model to route tasks based selection.
**u/100xReasonable** · 2026-10-08 18:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0yftf/when_will_oc_support_multimodel_to_route_tasks/)

---

## What unusual thing have you solved with opencode recently?
**u/f0d0r** · 2026-10-08 18:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0y6ut/what_unusual_thing_have_you_solved_with_opencode/)

I have a bunch of zip files with books, but there were a few what I could not open. I have kept them years on my laptop because I was always hoping I can find a tool which can open them. Yesterday I have finally managed to unzip them with Opencode. I have used the Space Bunny free model but I guess the others would have worked as well. It turned out that these zip files contains data which necessary to unzip them and it can happen that the tool which zipped writes these data to a wrong place inside the zip, for instance because of a bug. So finally Space Bunny just modified the zips and opened them. I was quite happy :)  
So I was wondering what else can I do next time. Have you ever used it for something that initially seemed impossible or completely unrelated to coding?

---

## Well, I got there first ( 50% Monthly Limit in ~3 days )
**u/Extra_Intention_152** · 2026-10-08 17:36 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0xaa1/well_i_got_there_first_50_monthly_limit_in_3_days/)



As per title, Only used Glm 5.3 flash and love it. This is way better than Openrouter.

---

## Fledge Alpha hallucinating crazy
**u/zyxciss** · 2026-10-08 16:40 UTC · ↑3 · 3 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0vtso/fledge_alpha_hallucinating_crazy/)

https://preview.redd.it/9xml0x5iu9uh1.png?width=2940&format=png&auto=webp&s=b46ff7ae4ff76ce214a9fda4dc52ece0f2cd2296

It was working on Qwen 3.8 Flash Next MTP bug and suddenly it started to yap about "SpokenEarth in Juno (a voice transcription) gadget" and started to read C:\\Users\\Administrator\\Desktop\\PID后\\ which does not even exist

**Comentarios:**

- **u/100xReasonable** (↑1, 2026-10-08 18:10): Is it still there ? The model is removed
  - **u/zyxciss** (↑1, 2026-10-09 08:42): i see a lot of models still and somehow everything works
    - **u/100xReasonable** (↑1, 2026-10-09 08:45): I cannot find Fledge Alpha in my Opencode.  It's gone

---

## Offtopic but any advice for a CS 3rd year student feeling stuck, powerless and worried because of Agentic Coding Revolution?
**u/Awkward-Swan8670** · 2026-10-08 16:34 UTC · ↑3 · 9 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0vo2g/offtopic_but_any_advice_for_a_cs_3rd_year_student/)

Mods, please don’t ban me if this is against the rules for being off-topic, but since every other subreddit seems to be full of coping redditors that secretly hates AI, I don’t really have anywhere else to post this.

So, as the title suggests, do you guys have any advice for a junior maggot like me who gets anxious every time a new flagship model drops?

My goal has always been to launch my own app/company/startup. But I tried some vibecoding this week, and it made me wonder: is there even any merit to getting a CS degree anymore?

As a CS student, it feels like I don’t have much of an edge over the average Joe anymore thanks to LLMs. And it feels like someone with more capital—someone who can afford to take more losses early on—will always be able to outcompete me. The barrier to entry has basically dropped to zero.

For anyone working in the industry, whether as a founder or an engineer, what’s your perspective on this?

**Comentarios:**

- **u/Green_Virus6289** (↑7, 2026-10-08 16:38): Learn that your role is to solve problems. It always has been. Coding was just an implementation detail, which is now agentic coding. The problem solving part has not gone away.
- **u/JustARandomPersonnn** (↑1, 2026-10-08 16:49): Not an engineer, but in the same position as you, had the same thoughts and then realized that well... There still need to be people managing the AI as well as actually knowing what's going under the scenes and understanding the architecture and making sure the codebase is good
    
    Projects made completely using AI by people without much experience are prone to serious security issues as well as unoptimized and unstable code- having used some popular open source projects by others that clearly seem to be vibe coded, there's often big issues and weird behaviors in each version
    
    I keep seeing news of companies firing people, and try to replace them with AI, only to then regret it and face serious backlash
    
    Companies that make software would always prefer to hire a professional software engineer that knows what they're doing rather than someone that doesn't actually know how code works at all and just vibe codes impressive things
    
    And clients too would much rather use stable software rather than something that cannot be relied on made by people that just blindly use AI
    
    And as for launching your own product- the same thing applies- and you've surely seen this- people DESPISE vibe coded projects, they don't like trusting code made by someone that doesn't understand what they're doing, and so do other companies...
    
    You're definitely still very important to the industry
  - **u/Awkward-Swan8670** (↑2, 2026-10-08 17:10): Thanks for chiming in but a lot of your arguments are just assumptions. (maybe except for the layoff part)
      
      Claiming that vibecoded apps are inherently unoptimized, unstable is an old point of argument. In 2026, most models are more capable than the average manual coding junior eng.
      
      People don't care about the pipeline as long as you deliver the product. And As I say with the current rate of advancements of LLMs, it feels like we won't even need to understand our code in the near future.
    - **u/JustARandomPersonnn** (↑2, 2026-10-08 21:24): I mean, you're right... Models indeed are pretty impressive with what they do now
        
        Honestly... I'm not entirely sure about the future, it's just that even using vibe coded apps now, they still have this thing to them that immediately tells me they're vibe coded... Even if not the UI, there really are a lot of odd quirks to them that make it quite clear and make them seem less trustworthy
        And I think that this is what drives people away
        
        But yes, also stability issues, that current models too can sometimes miss- having software engineers manually go through the code looking for issues can help more than just having one person to ask the LLM to check for issues with the code multiple times and having to blindly trust the its review to be right
        
        And regardless, as projects get bigger and need more people to work on, companies need employees- and it would make much more sense and be a lot safer for them to hire professional software engineers that demonstrate understanding of coding problems presented as examples in interviews, rather than people who can't say anything about the code themselves and are just overly dependent on LLMs
        After all, this is also an issue, in the case of the possible unavailability of those during critical issues for example
- **u/lacroix05** (↑0, 2026-10-08 17:00): you are worried because college mostly teaches you "knowledge". you feel insecure because llm can learn and process more knowledge much faster than you can.
    
    but in a real job, nobody really cares that you remember every single piece of information you can parrot from books. most people you work with mainly only expect you to have a basic understanding of how to do the job.
    
    what actually matters when working is not knowledge. what really matter is intelligence, experience, understanding, and judgment. llm make job feels easier because you essentially outsource a lot of the knowledge needed to that thing. but llm dont have those 4 important concept in the same way humans brains do.
    
    that's why llm doesnt simply replace engineers. in the near future, it will be more likely to replace jobs like fast food workers, where a large part of the job is following a fixed set of steps by the book. engineering is different because it requires understanding the bigger picture, making judgment calls, dealing with unexpected problems, and taking responsibility for the outcome.
- **u/Odd_Donkey2691** (↑2, 2026-10-08 17:55): Same, third year student in a third world country, 30 years old, second time going through Systems Engenieer. The Curriculum is outdated, they need to incorporate Agentic Engenieering into it a few clases. Vibe Coding has gotten complex to the point that only Engeniereers can get the best out of it or people that dedicate full time into information systems creation and management. I am not worried at all, the more I use AI and learn how LLMs work the more I see it's far from being autonomous.
  - **u/ramendik** (↑1, 2026-10-11 18:06): Vibe Coding was always an antipattern or at best a prototyping/experimentation route, in my opinion. Only *guided* agentic coding yields production quality over which one can stand.
- **u/the_man_inTheShack** (↑2, 2026-10-08 18:05): Many of the things you will learn are still valuable. Most people are hopeless at describing what it is they want, With a good understanding of what goes on inside a computer you are the one to translate what the user really wanted (rather than what the user asked for!) into what the application should -and can realistically- do. Until agentic coding, describing what the computer should do meant writing a program. When I started programming it meant writing assembler, then it meant using languages like Algol, then databases arrived as a better way of storing and accessing data. The task is the same, the means to do it changes.
  - **u/ramendik** (↑1, 2026-10-11 18:11): I'm a Technical Writer and 25+ years at it and feeling mildly optimistic because translating between user and programmer languages either way was always my specialty. For now my agentic coding is regarding writing support and personal stuff and I'm having fun.
      
      However, this does need understanding "userish" much more than a stereotypical old school programmer does. \*And\* this needs one to go back to Sgtructured Spec for anything really interesting. And Agile has been stamping out Structured Specs for a couple of decades now. 
      
      In my view Agile was a mistake from the start, an attempt to scale what worked *only* for a small group in the same room and the same subculture. These chickens are coming home to roost, big time. Your informal chats won't guide the Agent.
- **u/lordcohliani** (↑0, 2026-10-08 22:36): Change your major
- **u/ImaginaryRoyal9725** (↑1, 2026-10-10 18:46): We will need CS majors in the future when everybody thought to study something else because "ai took over". We'll need the people that can understand what's happening underneath.   
      
    So don't worry too much about that and make sure to learn the fundamentals extremely well. Those won't change

---

## Best Go model for reverse engineering / Ghidra work
**u/theanine3D** · 2026-10-08 16:08 UTC · ↑10 · 10 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0uzek/best_go_model_for_reverse_engineering_ghidra_work/)

Has anyone successfully used any of the models available via OpenCode Go for reverse engineering work - stuff like decompilations of games or apps. Are any of the models good enough for that?

**Comentarios:**

- **u/xx_gamer_xx123321** (↑6, 2026-10-08 16:20): Deepseek b4.1 flash
- **u/MorkezZ** (↑2, 2026-10-08 16:59): GLM 5.3
- **u/Grouchy-Stranger-306** (↑5, 2026-10-08 17:16): glm 5.3 flash was good enough for my re task
- **u/AdiCoSto** (↑1, 2026-10-08 17:25): dsv4.1 flash would be my first pick. For Ghidra work ... good context from the decompiler matters way more than chasing the “smartest” model tbh.
- **u/Time-Worker9846** (↑2, 2026-10-08 17:37): DeepSeek 4.1 Flash works for ghidra/hooking/capstone/pcap work very well
- **u/arielif1** (↑2, 2026-10-08 17:49): Both GLM 5.3 and 5.3 flash. Since you asked for best, it's 5.3 non-flash. flash is also pretty good, though
- **u/Affectionate_Fact854** (↑3, 2026-10-08 18:04): Glm 5.3 flash orchestration and using Muse spark for grunt work and 
    Deepseek for reviewing 
    
    Ghidra and cmake work is peanuts for that combination 
    
    But opencode is slow AF 
    My process RE a ps1 rom (odd world best oddesey) 
    With psxi ,ps1 bios, cmake , ghidra and splash took about 27 hours of none stop automation loops Excluding handover And orchestration cold starts in between 
    
    Not a quick process honestly
- **u/Fine_Salamander_8691** (↑2, 2026-10-09 01:34): Muse wasn’t too bad
- **u/Ashamed_Drag8791** (↑2, 2026-10-09 02:17): I like space bunny, ds is more of a architect than the worker
- **u/yoshijulas** (↑2, 2026-10-10 03:09): GLM 5.3 Flash works very well for me plus it has 60$, Muse just refuses to help, an i rather not be banned from it, since i use it for anything else.

---

## Deepseek flash 4.1 hallucinating
**u/skillmaker** · 2026-10-08 16:04 UTC · ↑20 · 19 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0uvox/deepseek_flash_41_hallucinating/)

Are you guys having the same issue? I've been having this issue for the past 2 days

**Comentarios:**

- **u/simpleuss** (↑6, 2026-10-08 16:10): Probably has something to do with operation cheepseek
  - **u/xx_gamer_xx123321** (↑1, 2026-10-08 18:28): Its probably 2-3bit max because of operation “cheepseek”
    - **u/simpleuss** (↑1, 2026-10-09 23:40): Would rather use ternary than Q2 or Q3
- **u/xx_gamer_xx123321** (↑2, 2026-10-08 16:37): Holy rap
- **u/localaisimple** (↑1, 2026-10-08 16:57): It happened with me too a few days ago, just press stop change the prompt and continue, usually works
- **u/qwertyyyyyyy116** (↑4, 2026-10-08 17:09): glm 5.3 flash does that exact thing aswell
  - **u/Best_Cattle_1376** (↑1, 2026-10-08 18:20): gemini does this too, its a issue everywhere (common hallucination)
- **u/ImMadeOfBees** (↑2, 2026-10-08 21:19): You don't speak Testificate?
- **u/dexter30** (↑2, 2026-10-08 21:36): Deepseek hallucinates a lot even when it works.
    
    It spits out like 10 different ideas, stops each time and spits out more. Never commits to a direction.
    
    I'm sure it's benefitial in some way. But holy crap I know it's cheap but it's frustrating seeing it go around in loops trying to solve an issue that has nothing to do with the prompt.
- **u/_BookBurner_** (↑2, 2026-10-08 21:57): HE IS THINKING AUDIBLY :D
- **u/Total-Management8023** (↑1, 2026-10-08 22:28): i find it so funny when an ai agent keeps making the same mistake over and over and it KNOWs its making the mistake its just helpless to stop.
- **u/[deleted]** (↑1, 2026-10-09 07:02): [removed]
- **u/porest** (↑1, 2026-10-09 08:51): I don't see the problem. Don't you go "hmmm" when your thinking?
- **u/TheSn00pster** (↑1, 2026-10-09 13:55): Hmm
- **u/TheMythicSorcerer** (↑1, 2026-10-09 19:00): Speedrunning using up all your usage
- **u/ERROR_FOX_PG** (↑1, 2026-10-09 20:08): Realmente se puso a cantar el inicio de wild lands
- **u/Long_Rub5460** (↑1, 2026-10-09 21:40): Check context size.
- **u/That_Macaron6026** (↑1, 2026-10-10 01:16): Whats this client? Opencode in Android?
- **u/[deleted]** (↑0, 2026-10-10 05:08): [removed]

---

## I love OpenCode Go… but something feels seriously wrong since Go Plus launched
**u/AdiCoSto** · 2026-10-08 15:56 UTC · ↑29 · 20 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0unzt/i_love_opencode_go_but_something_feels_seriously/)

This is not an OpenCode Go hate post. It’s almost the opposite lol.

I’ve been a HUGE fan of OpenCode Go for a long time. Genuinely one of the best subscriptions I pay for.

I’ve done **3,000+ GitHub commits this year**, and on one particularly unhinged day I somehow did 150+ commits :D That should probably tell you how much I’m coding.

https://preview.redd.it/avu8pikbm9uh1.png?width=1319&format=png&auto=webp&s=3c0ef71a23713fc8f180362d4ce4275e1279f5ce

And OpenCode Go has been a massive part of that.

For $10/month, the amount of building I’ve been able to do with models like DeepSeek V4.1 Flash is honestly ridiculous. Apps, automations, workflows, random ideas that would’ve stayed ideas otherwise... I really can’t thank the OpenCode + DeepSeek teams enough for making this stuff so accessible.

**Best bang for the buck in AI coding imo. Period.**

But...

Something has felt really wrong lately.

Ever since **Go Plus ($40/month)** launched, my experience on regular Go has become painfully slow. And I mean the actual throughput/TPS... not “the model is thinking for 5 seconds and I’m impatient.” Go Plus is indeed the new $40 tier with higher usage limits. 

Sometimes I’m sitting there thinking:

**is this thing even running??**

Nothing moves. Tokens crawl out. Tasks that used to feel fast suddenly feel like they’re stuck in mud.

It got frustrating enough a few days ago that I finally put money directly into the **official DeepSeek API** and started using V4.1 Flash from there instead.

And apparently I’m not imagining the broader slowdown either. There have been multiple recent reports of OpenCode Go users seeing much lower TPS, with one comparison reporting roughly 70–80 tok/s through Go vs 270–280 tok/s through the direct DeepSeek API, while other users have reported models dropping toward \~20 TPS during slow periods. I don't really know what TPS I was getting but I myself have experienced \~30 tps for sure... and that sucks. 

There are even people specifically saying their regular Go experience became worse around the Go Plus rollout.

Now, to be fair...

**I have absolutely no proof that Go Plus is causing this.**

And there were complaints about slower inference even before Plus launched, so correlation is not causation here. 

Maybe it’s traffic.

Maybe capacity.

Maybe provider routing.

Maybe I’ve just had terrible luck lately.

I genuinely don’t know.

But from the user side, the timing is hard not to notice.

And that’s why I’m kinda torn.

Because I’m not somebody looking for a reason to cancel OpenCode Go. I’m probably the exact opposite :)   
  
**I want this thing to be amazing.** It has enabled me to build an absurd amount of stuff for ridiculously little money.

I’d happily recommend it on value alone.

But their unlimited kinda usage means a lot less when you’re staring at the terminal waiting for tokens to crawl out... it gives me heartache. 

**I’d genuinely take 2x the speed with 2x the usage cost over 4x the allowance at painfully low TPS.**

That’s basically my rant.

Still a fan.

Still think OpenCode Go is a beast.

Still think the value is insane.

I just really and infinitely hope the speed comes back... because lately I’ve found myself reaching for the direct DeepSeek API more and more, and that kinda sucks when OpenCode Go used to be the thing I automatically reached for first.

I just wanted to put it in here so that maybe OpenCode team might see and do something about it.... hopefully!

**Comentarios:**

- **u/Ariquitaun** (↑6, 2026-10-08 16:10): I honestly have noticed no difference. I only use dsf and Mimo 2.6 flash though.
  - **u/AdiCoSto** (↑3, 2026-10-08 16:12): dsv4.1 flash has been killing me ... very slow at times.
- **u/Pedrito_Basket** (↑1, 2026-10-08 16:40): I agree with you, I get like 30tps on ds v4.1 flash and it is frustrating. I am rethinking of using official api instead of opencode but also like trying put new models, will think about it…
  - **u/AdiCoSto** (↑0, 2026-10-08 17:16): yeah i am using the offical dsv4.1 api more and more myself ... anything good in the new models? i feel dsv4.1 flash is unbeatable at this price.
- **u/Adorable-Leading-274** (↑1, 2026-10-08 17:16): Did you use ai to write this????
  - **u/AdiCoSto** (↑-3, 2026-10-08 17:17): openwhisper and then I made some edits manually :)
    - **u/Adorable-Leading-274** (↑3, 2026-10-08 17:36): That explains why it was a chore to read
      - **u/Drew192x** (↑0, 2026-10-08 18:05): This was honestly a small post in bullet point format. I just woke up and read this. If you think this was hard to read, your brain is slightly cooked my friend.
        - **u/Adorable-Leading-274** (↑2, 2026-10-08 18:07): lol or it was 10x the words required to convey the intended point 
            
            This is why caveman and ponytail exist (:
          - **u/AdiCoSto** (↑1, 2026-10-08 18:25): yep, I get it. to each their own I guess :)
              
              I just think the caveman version doesn’t really hit the same when you’re trying to vent and say something straight from the chest lol
        - **u/AdiCoSto** (↑0, 2026-10-08 18:21): thanks. I actually prefer splitting ideas in smaller chunks. i personally find it easier to read and it also lands much more impactfully :)
          - **u/Adorable-Leading-274** (↑2, 2026-10-08 18:25): Fair enough I can respect that, but didn’t you say this was AI?
            - **u/AdiCoSto** (↑1, 2026-10-08 18:43): I use OpenWhispr for pretty much all my dictation now. I just talk normally, dump the whole thought out, and then run it through a cleanup prompt I made that cuts the fluff, fixes the grammar, and keeps it sounding like me.
                
                Funny enough, I’m literally writing this comment with it lol. I use Groq’s Whisper v3 Large Turbo for transcription, then Luna to clean up the dictation.
                
                I recorded a quick screencast of my setup here if you wanna see how I have it wired up:
                
                [https://www.dropbox.com/scl/fi/3gzyw8y59j7bpwhd915kw/my-openwhispr-setup.mp4?rlkey=8imphwp06lb98erh1nz0vfcby&st=1cd4fans&dl=0](https://www.dropbox.com/scl/fi/3gzyw8y59j7bpwhd915kw/my-openwhispr-setup.mp4?rlkey=8imphwp06lb98erh1nz0vfcby&st=1cd4fans&dl=0)
                
                It’s pretty cheap to run, and depending on your setup, it can basically cost nothing.
                
                Honestly it’s been way better for me than typing all day. I can just say the messy version out loud, let the cleanup prompt do its thing, and move on.
- **u/alex9001** (↑3, 2026-10-08 18:18): How abused is your enter key
- **u/lordcohliani** (↑0, 2026-10-08 19:07): Bro made 3,000 GitHub comits this year and they're all AI slop like this post.
- **u/No_Structure1800** (↑1, 2026-10-08 19:08): Can confirm, actually "painfully slow" is exactly how I described it too before I saw your post. It's a shame, because it was already slower than Claude, but now some sessions take forever...
  - **u/AdiCoSto** (↑0, 2026-10-08 19:10): Couldn't agree more. It's painfully slow, exactly. It gives me heartache at times :(
- **u/Eryndalor** (↑1, 2026-10-08 19:15): I didn’t experience that, and I am on DS flash and the $10 most of the time
- **u/QuietPsychonaut** (↑1, 2026-10-08 19:48): Some people have reported the same as you. I feel no difference in speed. I feel like the monhtly limits have decreased while the 5-hour and weekly remained the same. I can spend my monthly limit without ever hitting the ceiling on the 5-hour or weekly.
    
      
    Maybe it is something model specific? What models are you using that cause this?
    
    I manly use DeepSeek v4.1 Flash and haven't had issues with speed.
- **u/ollm-tux** (↑1, 2026-10-10 08:53): i am from Romania (and this eats my whole life), when I made account of the opencode besides price I saw and the hours of congestion, the advantage of Eastern Europe is that I have local hours of activity that are not in maximum hours on DS. It should not be ignored that more and more people are discovering opencode, so I expect more and more congestion, which will increase your price or move to weaker servers

---

## I’m on the OpenCode GO plan and trying to choose the best models for a 3-step coding workflow
**u/Careless-Key-5326** · 2026-10-08 15:46 UTC · ↑4 · 15 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0uegr/im_on_the_opencode_go_plan_and_trying_to_choose/)

* **Planning / architecture**
* **Implementation:** I’m planning to use **DeepSeek V4.1 Flash**.
* **PR reviews**

The models I’m considering most for planning/reviews are **MiMo-V2.6-Pro, GPT-5.6 Luna, GPT-6 Luna, DeepSeek V4 Pro, Kimi K2.7 Code, and GLM-5.3**.

**Comentarios:**

- **u/xRebellion_** (↑5, 2026-10-08 15:58): I use dsv4.1 flash for both planning and orchestration, then mimo-v2.6-flash for implementation and browser test drive. For simpler tasks mimo is good enough. But once it gets too complex, it takes a looong time for it to finish the task. Occasionally use glm5.3 flash too.
    
    Those 3 are generally top picks for getting the most value for work, at least for me personally.
    
    A tip when picking models: try to find the ones you can get 60$ usage (it's written in the docs). With pro models, gpt models, and glm53 (no flash) you only get 15$, so if you're using it at least be aware of that.
  - **u/torrso** (↑2, 2026-10-08 21:30): And it's not like you can use $15 of those models and have $45 left for the $60 models. The $15 models are actually just priced 4x, they eat the same limits and using up that $15 will lock you out until the next cycle (even from free models).
- **u/AdiCoSto** (↑1, 2026-10-08 16:03): my 2 cents… I wouldn’t over-engineer the 3-model setup just because OpenCode GO gives us so many models lol.
    
    I’ve been using DeepSeek V4.1 Flash a LOT for actual coding and honestly I’d just make that the workhorse for almost everything.
    
    If it was me:
    
    **Planning / architecture → DeepSeek V4.1 Flash**  
    **Implementation → DeepSeek V4.1 Flash**  
    **PR review / second opinion → Kimi K2.7 Code**
    
    That’s basically it.
    
    For planning + implementation, keeping the same model has been much better for me because context continuity matters way more than people realize. You don’t really gain much by handing the plan to one model, implementation to another, then making a third model figure out what the first two were thinking lol.
    
    Then once the feature is done, I’d give the diff/code to Kimi K2.7 Code and basically tell it to try to destroy it… find bugs, bad assumptions, edge cases, architecture problems, whatever. I like having a completely different model do the review rather than asking the same model that wrote it to grade its own homework.
    
    Also… look into **obra’s Superpowers skill** if you haven’t already. That kinda structured workflow makes a bigger difference imo than obsessing over which model should handle every individual step. Give a good model a proper process for planning, implementing, testing, debugging etc and you can get way more out of it.
    
    So personally I’d keep it stupid simple:
    
    DeepSeek V4.1 Flash = builder  
    Kimi K2.7 Code = critic
    
    And layer something like Superpowers on top to improve the actual workflow.
    
    The best setup imo isn’t 3-4 “best” models constantly handing work to each other…
    
    it’s one really good workhorse + one model whose job is to disagree with it.
- **u/Atretador** (↑15, 2026-10-08 16:11): just slap DSV4.1 Flash on everything :)
  - **u/AdSmooth4982** (↑1, 2026-10-08 16:41): YES its soo good for almost anything!! exept ui work... you need to direct the ai a bit for ui work but its soo good at debuging stuff i love it!!!
    - **u/ahaw_work** (↑3, 2026-10-08 16:53): What would you suggest for UI work?
      - **u/AdSmooth4982** (↑2, 2026-10-08 17:05): glm is good at ui use that its best at web design
      - **u/squirrelscrush** (↑1, 2026-10-09 19:48): GLM 5.3 Flash. It creates beautiful UIs and actually understands stuff.
    - **u/techstrom007** (↑2, 2026-10-08 17:07): you are doing it wrong, get a design from dribble and ask 4.1 to use same ux and see the magic
    - **u/Atretador** (↑2, 2026-10-08 17:14): its still miles ahead of GPT models for UI work, heck I had better UI results with small local hosted qwen models
  - **u/techstrom007** (↑4, 2026-10-08 17:06): 100%
- **u/look** (↑3, 2026-10-08 16:18): MiMo 2.6 Pro for plan. DS Flash 4.1 for implementation. GLM 5.3 (or 5.3 Flash) for review.
  - **u/maqifrnswa** (↑2, 2026-10-08 16:47): I do similar for at least multi-model checking. I sometimes do DS 4.1 Flash for everything, but I like splitting up design stuff to glm 5.3 flash (better for UI work than DS 4.1 flash), DS Flash for planning + implementation, MiMo 2.6 Pro for review. But other than UI work, I think you can swap around and get similar results as long as there's a feedback loop.
- **u/PackageDecent3526** (↑1, 2026-10-09 14:47): I use .NET framework and tools that target Roslyn compiler, so I need a reliable model. I've gave both V4 Pro and GLM-5.3 the same task where they would have to decide on the architectural approach, and consider the ripple effect on how it might affect the surrounding areas. GLM-5.3 was more thorough and detail oriented, but V4 Pro had 'big picture' approach, and it gave the correct answer twice in a row. Not to mention, GLM spent $4.5 while V4 Pro spent 0.40 cents on the same task. But, that's my experience.
- **u/GhostVPN** (↑1, 2026-10-09 19:32): GLM-5.3 Planining > MiMo vor Dispatch > workers > DS > MiMo validation

---

## Does anyone know why this happens?
**u/Global_Routine** · 2026-10-08 15:46 UTC · ↑3 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0udt3/does_anyone_know_why_this_happens/)

https://preview.redd.it/ghg5cywrk9uh1.png?width=1212&format=png&auto=webp&s=141919452498fb957f5dc1e2b80d046408d64f32

**Comentarios:**

- **u/simpleuss** (↑2, 2026-10-08 16:17): Fledge alpha hallucinates a lot
  - **u/simpleuss** (↑1, 2026-10-08 16:18): Its probably a router though, if you ask for something very detailed it will not hallucinate

---

## I created an MCP server package for dynamic skill searches.
**u/Airshakur88** · 2026-10-08 15:35 UTC · ↑1 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0u3rh/i_created_an_mcp_server_package_for_dynamic_skill/)

I created @hallaxius/skills, an MCP server that allows AI agents to search for and query skills from [skills.sh](https://skills.sh)

It offers features to:

* Search for skills by keyword and author.
* Check rankings and trends.
* View details and related skills.
* Check security audits.
* Explore official skills.

This allows the agent to make requests such as:

"Find skills to improve the performance of a Next.js application and, before recommending any, check the security audits."

The project is open source and compatible with Bun, Node.js, OpenCode, Claude Code, Cursor, and Claude Desktop. It requires no API key for core features and uses data directly from skills.sh.

GitHub: [https://github.com/Hallaxius/skills](https://github.com/Hallaxius/skills)

Bun:

    bunx @hallaxius/skills

Node.js:

    npx -y @hallaxius/skills

**Comentarios:**

- **u/Ctbhatia** (↑2, 2026-10-08 16:06): could the audit result include a commit hash? that would let an agent install the version that was checked, not whatever is latest.
  - **u/Airshakur88** (↑1, 2026-10-08 18:31): Sure, I'll be home in a few hours, and I'll do that.

---

## OpenCode Go is noticeably slower than OpenAI direct with the same model
**u/FirstBroccoli5798** · 2026-10-08 15:28 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0txck/opencode_go_is_noticeably_slower_than_openai/)

[removed]

---

## Is “Machine Learning-Based Predictive Fault Diagnosis of Induction Motors Using Electrical and Vibration Signatures” a good CEP project?
**u/Buy_sellitems** · 2026-10-08 15:21 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0tqgg/is_machine_learningbased_predictive_fault/)

Hi everyone,

I’m an undergraduate Electronics Engineering student in Pakistan, and I need to select a Complex Engineering Problem (CEP) project for my Artificial Intelligence / Machine Learning course.

I’m considering this topic:

“Machine Learning-Based Predictive Fault Diagnosis of Induction Motors Using Electrical and Vibration Signatures”

The basic idea is to collect motor current, voltage, vibration, temperature, and/or speed data and use basic ML algorithms such as Random Forest, SVM, Decision Tree, or KNN to detect or predict faults such as bearing faults, imbalance, misalignment, overload, etc.

I want to keep the ML part at a basic/intermediate undergraduate level, but the overall project should be complex enough to meet CEP requirements.

Do you think this is a good project for an Electronics Engineering student?

What faults and sensors would you recommend focusing on?

Is it practical to collect the required dataset ourselves, or should we use an existing dataset?

Also, what could I add to make it a stronger engineering/CEP project rather than just a basic ML classification project?

Any suggestions, research papers, or similar projects would be greatly appreciated.

Thanks!

---

## Looking for AI/ML Complex Engineering Problem Ideas for an Electronics Engineering Student
**u/Buy_sellitems** · 2026-10-08 15:14 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0tkiz/looking_for_aiml_complex_engineering_problem/)

---

## Step 5 Preview is FREE on OpenCode for a week 🔥
**u/afanasenka** · 2026-10-08 14:47 UTC · ↑139 · 18 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0suys/step_5_preview_is_free_on_opencode_for_a_week/)

**Comentarios:**

- **u/afanasenka** (↑18, 2026-10-08 14:53): Not bad for "free model" (GLM 5.3 Flash / DS 4.1 Flash tier) - [https://artificialanalysis.ai/models/step-5](https://artificialanalysis.ai/models/step-5)
  - **u/aolender** (↑-1, 2026-10-08 15:17): Muse 1.3 looks better.
    - **u/NMiguelCosta-PT** (↑24, 2026-10-08 16:19): Muse only looks better in benchmarks.
      - **u/Substantial_Bag_9536** (↑3, 2026-10-08 21:50): lol
- **u/Own_Capital_1395** (↑3, 2026-10-08 15:03): dont see it as an option, how do iadd it
  - **u/BM0110** (↑2, 2026-10-08 17:07): refresh models
    - **u/Evan_gaming1** (↑1, 2026-10-10 15:20): how do you do that
- **u/DominikPlays** (↑2, 2026-10-08 16:38): It is Zdr then i can just right on
- **u/xRebellion_** (↑8, 2026-10-08 18:57): Tried it, this one drifts from the goal way too often for me. Personally found space bunny to be better, but will explore more later.
  - **u/WisdomSky** (↑2, 2026-10-09 01:22):  tried earlier as well. it started hallucinating immediately on the first prompt. 😅
  - **u/ByteNomadOne** (↑1, 2026-10-09 06:30): Confirmative. It did other stuff than asked.
- **u/[deleted]** (↑1, 2026-10-08 20:18): [removed]
- **u/breadnone** (↑2, 2026-10-09 05:29): the model sucks for designs and long horizon tasks. hope they'll fix this
- **u/[deleted]** (↑1, 2026-10-09 06:23): [removed]
- **u/ByteNomadOne** (↑2, 2026-10-09 06:29): Slow and a lot of timeouts. :/
- **u/Vegetable_Yam_9751** (↑0, 2026-10-09 10:05): I've been exploring alternatives to OpenCode lately, and Freebuff caught my attention. It's always worth checking out different options instead of sticking to the same tools, especially when you're looking for a workflow that fits your needs. Has anyone here tried it?
- **u/snowtosun** (↑2, 2026-10-09 23:37): Does Opencode's Step 5 Preview Free Version follow Opencode's ZDR policy?   
     I want to male sure to determine what kind of workloads I can be testing it with.
- **u/mitchins-au** (↑2, 2026-10-10 05:10): Not bad. It’s not unstable, but it makes a few mistakes that better models catch. Also I get “execution failed” or “endpoint unavailable” semi often.  
    I’d rate it below GLM 5.3 flash or muse spark, but better than something incompetent.
- **u/YogurtclosetClean478** (↑1, 2026-10-11 15:49): I just change from space bunny to step 5 preview in opencode zen today, but i meet "Upstream request failed: Endpoint is unavailable." for so many times. Although i tried to retry, this issue still remains.  
    why does this model take so much time to think? And what is the main reason for the problem in the image? How can i fix this?

---

## Building a voxel Gotham with interactive camera controls
**u/FinalEase1045** · 2026-10-08 14:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0rwq3/building_a_voxel_gotham_with_interactive_camera/)

[removed]

---

## Did Opencode remove the ability to view costing by API Key?
**u/lkn-ant** · 2026-10-08 13:33 UTC · ↑2 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0r1me/did_opencode_remove_the_ability_to_view_costing/)

I can't seem to find it anywhere. I'd like to know which service or tool is using what. Or should I create a service account for each, like a service account for Hermes, and one for my coding machine/WSL?

**Comentarios:**

- **u/AdministrationSlow3** (↑1, 2026-10-08 13:57): You can see such Data in Keys section with your Service Account. Hope it helps
  - **u/CharacterBorn6421** (↑2, 2026-10-08 15:18): But we can only see all the API keys usage combined. We cannot separate usage based on the API key in a single service account. In the old dashboard, we could filter out, but in new they removed this functionality.
    - **u/lkn-ant** (↑1, 2026-10-08 18:57): You beat me to it. That's what I wanted.
        
        I want to see which API Key is using which model and how much of it. For example today, my 5 hour limit was reached fairly quickly. I couldn't understand why. Then I saw Deepseek-v4-pro was used, when I set Hermes and Opencode TUI to use DeepSeek-v4.1-flash. I didn't know which API used Deepseek-v4-pro. So I had to revoke all API and make sure to set Deepseek-v4.1-flash for all of them again. That sucked and now I only have 9 days of rate left and my subscription renews in 20 days.
      - **u/Ctbhatia** (↑1, 2026-10-09 00:29): for the unexpected Pro calls, check custom agents in OpenCode, their `model` setting overrides the global model ([docs](https://opencode.ai/docs/agents/#model)). a Flash setting in the main TUI doesn't rule out a different model on a subagent.

---

## Is this better than opencode?
**u/ruboxytr** · 2026-10-08 09:49 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0msba/is_this_better_than_opencode/)

https://preview.redd.it/35748gynr7uh1.png?width=517&format=png&auto=webp&s=8146face26434bfb35a695559d5c4413de5704a9

i mean it does look skeptical at first but i think what makes this possible is that the 5$ limit every 5 hour which doesnt give you lots of usage. unless you code very often, its a bang for the buck.   
  
you still get 8m free tokens every single day on free models like mistral large 4 and qwen 3.8 max and muse and 55 more which is generous and nice if you dont use your $5 every day. 

and they also got other plans ranging from 10 to 200 and works same as the $5 plan

its called [xkiro](https://xkiro.com/ref/EWEQHKJ) btw (feel free to use my referral code for 500k token every day :D)

---

## What's your favorite Free Model?
**u/CoffeeTea021** · 2026-10-08 09:27 UTC · ↑23 · 34 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0mfyc/whats_your_favorite_free_model/)

There are quite a few free models on OpenCode at the moment, and I'm curious which one people are actually sticking with.

Some of the ones I've seen people mention a lot:

* **Muse Spark 1.3 Free:** seems to be one of the popular picks.
* **MiMo V2.6 Flash Free:** another favorite, especially for coding/agentic tasks.
* **Fledge Alpha Free:** I've never really used it myself, but I've seen people recommend it. IIRC there are also some region restrictions, so not everyone can access it.
* **Space Bunny Free:** I'm not really counting this one since its free access/limits seem to have changed quite a bit lately.
* **Exo Free:** the new one. Looks surprisingly strong from what people are posting, but... is it already down? I've been seeing a lot of `Endpoint unavailable` reports.

What's your favorite free model right now, and what are you mainly using it for?

**Comentarios:**

- **u/lincolnthalles** (↑9, 2026-10-08 09:42): Muse, though I'm using the billed version on the Go endpoint.
    
    It's an annoying model with the default OpenCode system prompt, but I managed to fix its quirks, and it's surprisingly capable and well-behaved. It gets things done correctly and really fast.
    
    I need to give another try to the MiMo V2.6 series. It was bad on launch, but Xiaomi said they rolled out a fix for the tool-call issues. I liked V2.5 over the previous DeepSeek V4 iteration, so there's hope.
    
    The other free models seem to be lower quality.
  - **u/niwia** (↑3, 2026-10-08 10:15): What did do to make muse proper?
    - **u/lincolnthalles** (↑5, 2026-10-08 12:11): Muse is running on this [system prompt](https://github.com/anomalyco/opencode/blob/v2/packages/core/src/plugin/system-prompt/meta.txt) on OpenCode V2.
        
        Other models use this [generic prompt](https://github.com/anomalyco/opencode/blob/v2/packages/core/src/session/runner/prompt/system.txt).
        
        I use a much more elaborate prompt, leaner than the old OpenCode V1 prompt but much larger than the default V2. It shapes its response, controls its permissions, work, validation, and tool usage.
        
        Minimal prompts are great for token-saving and make the model work best with a high context load, but they allow models to run loose.
        
        Maybe a thorough procedure is key for this model. It doesn't have issues working with lots of instructions, as long as they are not conflicting and have proper tie-breaks.
        
        I found Muse has a ton of biases in text output. I think it uses telegraphic reasoning internally, and this makes it output awful prose with bad formatting. I had a hard time breaking this tie, but it worked out eventually.
        
        It can be a lot of work, but the huge model quota and capabilities pay off.
        
        Try to address the issues you frequently encounter when using the model. The instructions you should use depend on personal taste and how you work with models, whether you want them to be more proactive and do everything the best they can, or whether you like them to do just what they were told.
        
        The latter is my case, so I suppress out-of-scope proactiveness that many models adopt, like when you tell it to do something (like commit or kill process X) and it takes this for granted for the whole thread.
      - **u/niwia** (↑2, 2026-10-08 12:21): Thanks for sharing :)
  - **u/Nenad1979** (↑2, 2026-10-08 11:43): What did you change?
  - **u/Mihaylov93** (↑2, 2026-10-08 12:04): I've only tried MiMo of the free ones and for android development with flutter is solid, handles the emulator and a physical device just fine and with the flutter skills the app it made is usable
  - **u/PackageDecent3526** (↑2, 2026-10-09 14:28): Muse through OpenCode gets you their Contributor variant, but with reasoning turned off completely. I don't know if that's the case with their Go tier. If it is, you're better off using Muse directly from Meta, because you can scale it up to high reasoning at the same price. Muse with high reasoning feels like a different model compared to default variant.
    - **u/lincolnthalles** (↑1, 2026-10-09 15:21): The free tier exposes the same reasoning flags. I wasn't aware they were rewriting it at the gateway level or something like that. It would explain many of the complaints about Muse.
        
        It would be best if they imposed greater usage limits or removed the model from the free tier rather than nerfing it, which works as bad publicity. 
        
        Also, Muse is really slow today. I even got some timeouts. Sadly, high service load aligns too well with nerfing practices.
        
        `max` reasoning is indeed only available on the non-contributor variant, but I found it performs really well even on `xhigh`.
        
        I like Go due to its model catalog. It also has a $60 budget for Muse Spark, but Zen + Meta API doesn't sound like a bad idea if the service is better.
      - **u/PackageDecent3526** (↑2, 2026-10-09 16:25): You can change the effort level inside OpenCode, but Muse Spark Free gets tagged with 'none' regardless. True, max is available only for the non-contributor variant, but it's almost irrelevant, because you're paying $0.10/$0.20 per million tokens for a frontier model. It has its own native CLI harness as well.
- **u/Competitive-Yak-8255** (↑1, 2026-10-08 10:13): Nice
- **u/ardahanbk** (↑5, 2026-10-08 11:37): I hope i won't jinx it but I'm still using space bunny free  to this day. I heard it was extended untill the 5th of octobre, but right now no limitations at my end at least.
  - **u/DarthNinja95** (↑0, 2026-10-08 12:16): Yeah I'm also able to use space bunny as free. When I checked the logs, it shows $0 usage
  - **u/[deleted]** (↑1, 2026-10-08 17:45): [removed]
- **u/Leading_Yogurt7025** (↑1, 2026-10-08 12:05): Mimo v2.6
  - **u/Leading_Yogurt7025** (↑1, 2026-10-08 12:06): Exo free also top but now unavail
  - **u/mwila2000** (↑1, 2026-10-09 06:43): MiMo v2.6 is just a trooper
- **u/mahesh-muttinti** (↑6, 2026-10-08 12:52): Big pickle forever stealth model
  - **u/CoffeeTea021** (↑1, 2026-10-08 15:56): Yeah, Big Pickle is pretty decent. Sometimes I feel like it’s not that great, but there are definitely times when it works really well. It was actually the first model I used.
- **u/gaspoweredcat** (↑2, 2026-10-08 14:12): muse isnt quite free, very cheap but it still has some cost, space bunny is gone (wasnt terrible for reviews etc) mimo i have on token plan, didnt know there was a free, dont know of the others, currently playing with Glyph Cluster which doesnt seem awful
  - **u/alexzzzz** (↑1, 2026-10-08 15:57): Space Bunny is working right now
    - **u/gaspoweredcat** (↑0, 2026-10-09 11:50): was removed from kilo/openrouter on the 5th
      - **u/alexzzzz** (↑1, 2026-10-09 11:55): Don't know how long it will last, but it still present on Opencode Zen as Space Bunny Free.  I'm using it right now. A pretty fast, stable and capable model.
        - **u/jezrill** (↑1, 2026-10-09 20:50): can u tell me how you're using free models on opencode
          - **u/alexzzzz** (↑1, 2026-10-10 04:48): You just download Opencode and use them. They are rate-limited but sometimes not. Space Bunny was unlimited for the first week, Step 5 is unlimited now.
            - **u/jezrill** (↑1, 2026-10-10 08:53): I'm talking about the provider and stuff.. how to do that? what endpoint should i take?
              - **u/alexzzzz** (↑1, 2026-10-10 11:29): The built-in Opencode Zen provider. You don't even need to sing up to try the free models.
                - **u/jezrill** (↑1, 2026-10-10 11:31): can you share the proxy url that u use? i tried like that several times but that's not working for me..
                  - **u/alexzzzz** (↑1, 2026-10-10 11:36): https://opencode.ai/docs/zen/
                      
                      https://opencode.ai/zen/v1/chat/completions
                      
                      Free Zen models are restricted to Opencode clients only. It was mentioned somewhere in the docs, but can't find it right now.
                    - **u/jezrill** (↑1, 2026-10-10 11:46): i tried this proxy url it still doesn't work for me 😞🙏🏼 network error
                    - **u/jezrill** (↑1, 2026-10-10 11:56): i can dm u and can u look at my configuration for once
  - **u/CoffeeTea021** (↑2, 2026-10-08 16:14): There actually is a free version of Muse Spark on OpenCode Zen, `opencode/muse-spark-1.3-contributor-free`. The regular Muse Spark 1.3 is paid but pretty cheap, while the Contributor Free version is free. They said it is a limited-time offering though, and there are some caveats around usage and data.
    - **u/gaspoweredcat** (↑1, 2026-10-09 11:50): ah im kilocode/openrouter, i used contributor a bit on there but im totally out of credit till tomorrow now
- **u/jezrill** (↑1, 2026-10-09 21:37): can u share the setup for open code? idk how to use the free models
- **u/GoonigUnc** (↑1, 2026-10-10 00:08): i live in japan and im still able to use space bunny for completely free. in fact, im running it right now without having any kind of subscription nor api balance
- **u/PerfectReflection155** (↑1, 2026-10-10 05:20): Step 5. Seems close to Glm flash 5.3

---

## Continuing after restart error showing up
**u/Upset-Bee-1964** · 2026-10-08 09:25 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0melf/continuing_after_restart_error_showing_up/)

https://preview.redd.it/o8vc8zg2p7uh1.png?width=768&format=png&auto=webp&s=7f6467417b5bd864eb0ee21293d9889ac5887c3f

---

## Question about benchmark for some free models in opencode zen
**u/YogurtclosetClean478** · 2026-10-08 08:50 UTC · ↑0 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0lvre/question_about_benchmark_for_some_free_models_in/)

Does anyone have good benchmark scores to compare among free models like space bunny, fledge-alpha, and exo-free, with other models? I am so curious about that and I want to have one to decide which model i should use to work.

**Comentarios:**

- **u/lordcohliani** (↑2, 2026-10-09 15:28): https://aicodingdaily.com/leaderboard
    
    I go by this guy's leaderboard. I like that he has his own private tests, they seem to be a lot more accurate. All the common public tests are built into the training data of the models and that's how you end up with Gemini flexing great benchmarks and still being terrible.
  - **u/YogurtclosetClean478** (↑1, 2026-10-10 13:33): thank you so much for the leaderboard!

---

## theres just no way they gave me this much for completely free
**u/ruboxytr** · 2026-10-08 08:44 UTC · ↑0 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0ls7t/theres_just_no_way_they_gave_me_this_much_for/)

https://preview.redd.it/9vdlbhr6g7uh1.png?width=795&format=png&auto=webp&s=d8c0780d8ceaad1c97c82105e27dae385b901a73

apparently its called [excelent ai](https://excelnt.ai/signup?ref=unc-06da), they got deepseek v4.1, opus 5.5 and even astra and some many more. im still trying it out and its actually working well. it does seem legit so try it out if you want and thank me later ;)

**Comentarios:**

- **u/Consistent_Jicama616** (↑3, 2026-10-08 08:54): this is engagement bait, the link he posted is just a referral link so he gets money ☠️

---

## Which gives me more usage?
**u/Harshith_Reddy_Dev** · 2026-10-08 08:31 UTC · ↑2 · 31 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0ll2w/which_gives_me_more_usage/)

 I'm deciding between buying DeepSeek API credits or using OpenCode Go. I’ll mostly be using Flash v4.1.

I’ve seen several posts claiming that they get significantly more usage by using the DeepSeek API directly. Are they simply buying around $10 worth of API credits, or does DeepSeek offer some kind of subscription that provides more usage?

Also, I’ve heard that OpenCode Go’s DeepSeek model is distilled, which supposedly means lower performance compared to the original DeepSeek model. Is that actually true?

**Comentarios:**

- **u/JaMoLpE88** (↑8, 2026-10-08 08:35): If $10 on the DeepSeek API gets you $10 worth of DeepSeek API usage, but $10 on the OpenCode Go subscription gets you $60 worth of DeepSeek usage... which one do you think gives you more? xD
  - **u/Harshith_Reddy_Dev** (↑1, 2026-10-08 08:41): I have seen some posts where they get much more token usage compared to the go one and is the distillation noticeably bad in performance?
    - **u/acakaacaka** (↑2, 2026-10-08 08:44): 6x more usage?
      - **u/Harshith_Reddy_Dev** (↑1, 2026-10-08 08:55): https://www.reddit.com/r/DeepSeek/s/ZfTlP537Xz
          
          Not exactly 6x more tokens. I meant better token usage efficiency. I’ve seen people getting hundreds of millions of tokens for just a few dollars through the direct DeepSeek API, mainly because of the huge cache-hit ratio. So I’m wondering how that compares with OpenCode Go’s 6x usage multiplier in practice
        - **u/acakaacaka** (↑1, 2026-10-08 09:25): That's depend on you. High cache hit ratio also only happends when you only work with the same chat.
    - **u/[deleted]** (↑1, 2026-10-08 08:44): [deleted]
    - **u/JaMoLpE88** (↑1, 2026-10-08 08:44): I’ve used the DeepSeek API, and I can assure you that for $10, you get way more out of the OpenCode subscription—significantly more than with the direct API. For the same amount of work, the subscription cost me $10, whereas the API would have cost $48—and that’s not even counting the free usage of the free "Zen" models. All in all, the OpenCode subscription offers much better value. That said, if we’re talking about quality or speed, I suppose the API is better, but it’s not worth it for me.
  - **u/xatey93152** (↑1, 2026-10-08 11:16): You should compare the difference. It seems opencode really use the nerfed quantized version
  - **u/pasteldebytes** (↑7, 2026-10-08 11:29): While this is true I just want to point out that opencode routes to inference providers, and my bet is they kind of use a flex routing, meaning they route to available unused capacity from those providers. I barely get 100 tok/s on opencode (average is 60 to 80), and when I use ds api, I get avg 170 to 200.
    - **u/Jazzlike-Form9669** (↑0, 2026-10-08 13:34): not to flex , but you should check out OGX plan. TPS will impress you
      - **u/pasteldebytes** (↑1, 2026-10-08 17:27): What you mean by ogx? Is that ollama?
        - **u/Jazzlike-Form9669** (↑-1, 2026-10-08 17:34): No, I know what Ollama is. I'm not talking about Ollama. I'm talking about OGX.
          - **u/Easy-Mad-740** (↑1, 2026-10-11 17:12): Lol no disclosure that you're on the team?
- **u/RasonYang** (↑1, 2026-10-08 08:48): Yeah, off-peak is real, and it works inside Go too.  
      
    Go's limits table lists DeepSeek V4.1 Flash twice, off-peak and peak, both under the same $60 cap. Off-peak is $0.15 in and $0.60 out per M, peak is double that, so the same $10 stretches about twice as far if you code outside peak hours. Peak is only 01:00-04:00 and 06:00-10:00 UTC on weekdays, so nights and weekends are always off-peak.  
      
    There's no DeepSeek sub btw, just prepaid credits, so $10 of credits is $10 of usage.   
      
    On the quantized thing, I don't think anyone can prove it either way.
  - **u/Harshith_Reddy_Dev** (↑1, 2026-10-08 08:58): Ah I reread the post(https://www.reddit.com/r/DeepSeek/s/ZfTlP537Xz) and now it makes sense. So I guess the real question is whether I’m willing to use DeepSeek only during off peak hours and optimize around caching or just use Go and not have to worry about any of that
    - **u/pasteldebytes** (↑1, 2026-10-08 11:30): Peak hours also affect go
- **u/CaffeinatedTech** (↑1, 2026-10-08 09:06): You're not missing out on caching by using the go plan.
  - **u/BobtheGodGamer** (↑1, 2026-10-08 09:27): You are. Tests have shown that it's cache hit rate is way worse
    - **u/CaffeinatedTech** (↑1, 2026-10-08 10:03): That's interesting.  Got a link?
    - **u/pasteldebytes** (↑1, 2026-10-08 11:31): I'm interested on that claim. I've stress tested cache on both gateways, and even while jumping around inference providers on opencode go, I didn't notice a big difference. The only problem I saw is when cache affinity is not respected and you are redirected to another inference provider on a long session
- **u/Ill-Ear-8763** (↑3, 2026-10-08 09:19): It would be more relevant on the other side of the spectrum (lower usage). 
    
    If you regulary don't utilize the full 6x usage on opencode and at the same time would spend less on the direct Deepseek API per month, "pay as you go" would win because for example the 10$ API would last you 2 month, where opencode would cost you 2x10$ for the same time frame.
    
    Then again, who here has actually a "low  usage" on AI..... 😂 
    
    With opencode you could of course use other models as well which you cant on Deepseek API.
  - **u/pasteldebytes** (↑1, 2026-10-08 11:34): Fully agree. And most people don't get that. Opencode go business model is either betting you don't consume the break even quota, or selling you unused capacity from inference providers. 
      
      Btw, that break even calculator is available on deepfrugal.
  - **u/squirrelscrush** (↑1, 2026-10-09 19:51): Even with DeepSeek I use a lot of tokens lol, so it's definitely worth the $10
- **u/4Sapi** (↑0, 2026-10-08 09:20): I'd compare the effective cost per successful coding task rather than just the advertised usage allowance.
    
    With the direct DeepSeek API, cache hit rates and off-peak pricing can make a pretty big difference, especially for repetitive coding workflows.
    
    For OpenCode Go, the key question is how its usage limits translate into actual tokens and completed tasks.
    
    As for the distilled/quantized model claim, I wouldn't assume that without evidence. Different outputs alone don't necessarily prove they're running different model versions.
    
    Would be interesting to see a side-by-side test using the same repo, prompts, and coding tasks.
- **u/Puzzleheaded-Tune-98** (↑1, 2026-10-08 09:39): Am i missing something here. When did Opencode go back to $60, usage for $10, for DS4.1F?
  - **u/pasteldebytes** (↑1, 2026-10-08 11:35): They were on a promo time, and listed $30 as the "normal", but then they decided to post $60 as the new limit
  - **u/Responsible-Rise2392** (↑1, 2026-10-08 12:32): Thank you
- **u/pigletmonster** (↑-2, 2026-10-08 11:08): For v4.1f the inference comes directly from deepseek. Its not a third party provider like they did with operation cheapseek. Deepseek lowered the price for this model plus they give massive discounts for opencode users so its just cheaper to get it from them directly.
  - **u/pasteldebytes** (↑2, 2026-10-08 11:37): That is not true, I'm sorry. Opencode uses at least 3 inference providers, including orcarouter, deepinfra and novita. I have a lot of logs to prove that.... 😬
    - **u/pigletmonster** (↑1, 2026-10-08 13:32): For v4.1f?
      - **u/pasteldebytes** (↑1, 2026-10-08 17:16): Yes. Just put a proxy on front of your harness and check for yourself. Or make the api call manually and see the response. Inference provider is part of the response
- **u/DiscountFit9224** (↑1, 2026-10-08 13:07): Can't speak about more tokens/$ but I started using the API mainly because I can't exhaust the $10 plan as I only use DS for assisted workflow. But what I noticed is, the official one outputs are compacted and straight to the point (maybe because I'm using PI now?). Also it follows instruction really well, synthesize information from search with multiple steps (I use as crack head search engine).
- **u/ManagementNo4948** (↑1, 2026-10-08 19:13): after initial prompts, I have seen 99.6%+ caching throughout on DeepSeek harness. haven't used much but around 1 billion token. off peak hours usage cost -$5
- **u/thechimpanc** (↑2, 2026-10-09 00:37): Both sides offer prompt caching. Some argue that OpenCode has a lower performance in caching and lower quality in thinking and output than OG, but it gives $60 worth of usage for only $10. You can’t really complain when it actually has a bit of issues. If you want the best quality while cost efficient, Deepseek API is still a great choice. It’s definitely more expensive, but also definitely higher quality and more efficient. Don’t use a combo because you are not going to enjoy benefits of caching to the fullest, which turns out not as efficient as sticking with either one of them.

---

## they said the limits were 'generous' i think they meant there is no limit
**u/AdSmooth4982** · 2026-10-08 08:21 UTC · ↑104 · 147 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0lfxv/they_said_the_limits_were_generous_i_think_they/)

not even at 50 precent like huh??

**Comentarios:**

- **u/AdSmooth4982** (↑15, 2026-10-08 08:22): am getting soo much usage from a 10 dolar subscription this is incredible
  - **u/brqzilianu** (↑2, 2026-10-08 08:27): same
  - **u/ichisay** (↑3, 2026-10-08 10:13): Pues fijate que otros se quejan de que no le llega para nada y andan escupiendo odio a la suscripción comparándola con las de 20$ de Claude o chatgpt. Yo no le veo sentido.
    - **u/onomastico** (↑2, 2026-10-08 14:06): Yo creo que él no utiliza su suscripción intensamente.
        
        Cuando comencé también me rendía mucho, pero a medida que me proyecto fue creciendo ya no llegava al mes y hasta tuve que comprar otra y recargarle créditos.
      - **u/ichisay** (↑2, 2026-10-08 14:12): Es que hay que combinarla con los modelos gratis también, yo incluso en su momento puse 10$ en openrouter para poder tener 1000 peticiones en vez de 50 diarios y eso queda para siempre, es una forma más de poder estirar la suscripción. Yo de los modelos de suscripción siempre usé los más baratos pero que fueran buenos.
        - **u/onomastico** (↑3, 2026-10-08 15:48): Sí, yo mayormente consulto a los modelos de pago, e implemnto con los gratuitos.
            
            A menos que sean consultas sencillas, donde sí hago ambas cosas con los gratuitos.
            
            Finalmente, cuando se me acaba la cuota gratuita, hago ambas cosas con los modelos de pago.
            
            Este mes estoy usando más Codex, ya que Sol 6.1 está bastante económico y es super inteligente, y uso los modelos de opencode para revisar código y obtener recomendaciones y mejoras sobre el plan o lo implementado.
          - **u/ichisay** (↑1, 2026-10-08 16:59): Si yo hago igual, uso Sol como orquestador y los demás para subagentes y en algún subagente uso Luna. Luego ya con omniroute ya se ocupa de que si uno cae o si llega al límite pues me hace los fallback. Incluso uso la promoción de Google cloud que te da 300$ para usar gemini 3.8 flash con vertex
- **u/Lanfeust09** (↑3, 2026-10-08 08:28): Yeah, that's my thought too. If you stay with DS, Muse, GPT6 and now Haiki 5.5, it honestly feels like unlimited !
  - **u/AdSmooth4982** (↑3, 2026-10-08 08:32): cheap models became really good these Chinese labs are soo good am impresed by haikus performance now too before i had a claude sub i used haiku a lot and id didnt even leave a dent on my usage and now? 75 percent cheaper?? il never be able to run out c:
    - **u/Standard_Wish** (↑2, 2026-10-09 19:05): Ever hear about how much effort it took China to develop a keyboard system to accommodate their language? I feel, but cannot prove, that Chinese language structure is more likely... more LLM inference efficient. Predicting next token would arguably (big assumption on my part) have less friction with a more structured linguistic foundation.
      - **u/AdSmooth4982** (↑1, 2026-10-09 19:38): chinese language really does use a lot of "data lanes" like the tone of your voice how fast your saying that word and stuff normaly when the language is put on text it looses these big pieces of information i need to research more chinese to say this but yes i think your right chinese does have a lot more information packed into the text and this explains why these Chinese models are soo good at instruction following with a fraction of the training cost to other close source llm models take my word as a grain of salt i didnt do as nearly enough research to make a valid theory
- **u/aliencreature12** (↑2, 2026-10-08 08:30): what model do you use the most? what harness do you use? and what's your use case mostly?
  - **u/AdSmooth4982** (↑2, 2026-10-08 08:36): i made my own harness using opencode i mainly use deepseek v4.1 flash i was using a combnation of models like deepseek v4 pro and flash googles flash models and stuff mainly used google for image related tasks and deepseek v4 flash was my terminal agent but now i dont even bother useing anything else deepseek v4.1 flash is enough gor most of my work its not that good at ui work tho so i used kimi and opus for it i have 10 days left till my sub ends i wont be able to use all my usage..
- **u/awkard_guy_** (↑1, 2026-10-08 08:35): where can i check this, please help me
  - **u/AdSmooth4982** (↑1, 2026-10-08 08:36): opencode website?
    - **u/awkard_guy_** (↑2, 2026-10-08 08:39): oh i forgot to authorize my console with opencode acc, thats why my usage is not reflecting in the website.
      - **u/AdSmooth4982** (↑1, 2026-10-08 08:42): ohhh
- **u/Alexandria_4624** (↑41, 2026-10-08 08:38): "Oh so no limit?" *Dev reduce the limit
  - **u/AdSmooth4982** (↑-84, 2026-10-08 08:38): i wouldnt mind a reduce in usage its already more than enough
    - **u/dumbasPL** (↑35, 2026-10-08 08:56): Please delete this
      - **u/Slow-Set-2856** (↑9, 2026-10-08 09:40): too late, his comment has already been scraped and oc is going to reduce limits by 50%
        - **u/AdSmooth4982** (↑-20, 2026-10-08 09:56): what does that mean? the second half
          - **u/Slow-Set-2856** (↑7, 2026-10-08 10:23): means that  oc is going to reduce limits by 50%
            - **u/AdSmooth4982** (↑-16, 2026-10-08 10:28): yeah but can you explain it a bit more? my english is not good i dont get what your saying.. am from turkiye btw nice to meet u
              - **u/SuccessfulDrink9007** (↑6, 2026-10-08 11:05): Ne yapmaya çalışıyon amk. Mal mal cevaplar vermişsin. Opencode botları bu konuyu görüp kullanım limitlerini düşürecek demişler. Şakaya vurmuşlar.
                - **u/AdSmooth4982** (↑3, 2026-10-08 11:07): hee tamam füşürsünler yaa zaten çok fazla yani.
                    cevaplarım gerçekten çok mu saçma 🥲
                  - **u/SuccessfulDrink9007** (↑4, 2026-10-08 11:09): Rage bait atıyorsun gibi geldi. Ondan saçma dedim şahsi düşünsense daha düzgün açıklarım. Neden limitleri düşürsünler? Kullanıcının zararına olur.
                    - **u/AdSmooth4982** (↑2, 2026-10-08 11:11): birazdaha dinamik bir plan olabilir başkalarının kulanmadıgı limitler çok kulanan insanlara bonus limit olarak verilebilir çünkü aysonu gelince kulanılmayan %20 yi kulanıcı napsın çöp oluyor benim demek istedigin bu ana limiti degiştirmesinler ztn haksız olur biraz
                      - **u/SuccessfulDrink9007** (↑2, 2026-10-08 11:25): 5 saatlik ve haftalık limitler zaten kullanımı dengelemek için konulmuş durumda. Bunun hem onların işine geliyor. Sürekli kullanamadığın için limiti dolduramıyorsun. Aslında bu limiti dolduramaman, onların da istediği bir şey. Gerçi Opencode açık kaynak bir program. Büyük ihtimalle kullanıcı yararına sunucularla anlaşmalar yapıyorlardır ama arka planda bu anlaşmalar nasıl yapılıyor bilmiyoruz. Bildiğim kadarı ile zaten hiçbir abonelik hizmetinde başka birine kullanım aktarma yok. Belki sonraki ayın kullanımına ilave edilebilir.
                        - **u/AdSmooth4982** (↑1, 2026-10-08 11:34): haftalık limit bence baya iyi onceden claude kulandıgım zamanlar gibi degil anca limit 100 oluyodu 5x e yulseltmek xorunda kaldıydım ama çok pahalıydı hani opencode suan çok iyi
              - **u/Slow-Set-2856** (↑2, 2026-10-08 11:45): yea sure, what i meant is that oc was going to just reduce limits by 50% after your post
                - **u/FacuA0** (↑3, 2026-10-08 11:53): Surely they didn't understand the short oc (opencode)
                  - **u/AdSmooth4982** (↑1, 2026-10-08 11:56): THANK YOU thats why i couldnt understand whats going on i tought oc meant like me the post creator but than i was like huh? am not a secret opencode developer? 🫪
                    - **u/FacuA0** (↑2, 2026-10-08 13:33): You're welcome. I think it's too easy to overuse shorts and assume everyone's on the same page.
    - **u/AdSmooth4982** (↑-9, 2026-10-08 09:11): i wonder how many downvotes i can get from this comment lol😆
    - **u/tetoing** (↑3, 2026-10-08 13:32): "It is enough for my specific use case using one of the cheapest non-free models available so please screw everyone over"
        
        gtfo
      - **u/AdSmooth4982** (↑0, 2026-10-08 13:38): this is my opinion i find deepseek v4.1 flash to be enough for agentic work ofcourse its bad at ui design and vision work its one of the cheapest models ever and they wouldnt look at my coment and go "oh yea lets cut the limits" because you all expresed your own opinion by downvoting it to the ground or replying to it in a negative way someone whos using a 10 dolar subscription shouldnt need to use the best open model on the market i think they are doing a great job at the minimum you get 15 bucks of value from a 10 dolar acount
    - **u/FixLower5218** (↑2, 2026-10-09 21:36): Posting such a message should be a war crime!lol.
- **u/wamiqiskira** (↑5, 2026-10-08 08:41): I dunno man I am at 82% usage and 16 days left on subscription 🥲🥲
  - **u/AdSmooth4982** (↑2, 2026-10-08 08:42): what were you doing 😭 what model u using mainly? i dont wanna click on THAT acidently
    - **u/wamiqiskira** (↑2, 2026-10-08 09:39): 😂😂 GLM 5.3 Flash 🫶🥲
      - **u/AdSmooth4982** (↑2, 2026-10-08 09:41): thats not normal huh?? i wish you 2x usage on whatever model you need
      - **u/xRebellion_** (↑3, 2026-10-08 11:18): For GLM 5.3 flash I recommend being careful in managing the context, above >80k it can eat your limits quite easily (expensive cache read).
- **u/TheBrownMamba1972** (↑27, 2026-10-08 08:41): I made a mistake of using GLM 5.3 non flash for one medium sized coding task. Tanked it from 100% monthly to 80% in one task. I came from Ollama Cloud so I was a bit surprised at how much it tanked. But running flash models does feel unlimited pretty much
  - **u/AdSmooth4982** (↑1, 2026-10-08 08:57): the flash models are great and glm5.3 is a solid model for visual tasks cus it has a kind of spacial understanding i dont know how to explain this but this makes it a good model for web development and also a bit expensive if your using this mainly for coding in terminal are you happy about its output? i heard cheaper models tend to use more tokens to finish tasks i never tested that because my projects are generaly not that complicated personaly i dont really like glm models
    - **u/TheBrownMamba1972** (↑3, 2026-10-08 09:03): The output itself is fine. I switched to GLM 5.3 because GLM 5.3 Flash introduced some bugs on a Linux quickshell config that I told it to make. GLM 5.3 immediately fixed it in one shot, but it also took 20% of my monthly usage. I don’t really see a big difference in actual result quality when they both make something where everything works properly, but at the same time I haven’t really done anything big with GLM 5.3 due to how expensive it is. GLM 5.3 Flash does the job perfectly fine and is pretty much unlimited, even if given constant coding tasks of different sizes
      - **u/AdSmooth4982** (↑5, 2026-10-08 09:09): ds 4.1 flash changed the game for me ive never seen a model this stable it handles long context like a champ only had to end 1 session where it started to give weird tool calls but i do understand why i made it like switch directions 10 times maybe more than that qwen 3.8 max was soo good but it ate my money like 50 dolars were gone tho it really helped me move the project was stuck for a long time before i used that but deepseek now basicly does somewhat the same thing it really understands why the code was there and explains it to me very cleanly am very happy
      - **u/XelomSit** (↑2, 2026-10-08 10:24): Give a try with MiMo v2.6 Pro. It's better at benchmarks when compared to GLM 5.3 (with reduced cost)
        - **u/xRebellion_** (↑3, 2026-10-08 11:14): Just note that in opencode-go you only have 15$ worth of usage
          - **u/amethyst_mine** (↑2, 2026-10-08 12:20): its still absurdly cheap to run tbh
            - **u/xRebellion_** (↑2, 2026-10-08 12:24): Personally haven't tried it yet, but have you compared it with ds41 flash or glm53flash? Might give it a try at the end of my sub if I still got some quota
              - **u/amethyst_mine** (↑3, 2026-10-08 12:58): not near as much usage as 4.1f, but i got similar to glm flash imo
- **u/moracola** (↑3, 2026-10-08 08:49): how about close some tabs
  - **u/AdSmooth4982** (↑1, 2026-10-08 08:50): i tried to but they all are soo important
  - **u/dumbasPL** (↑3, 2026-10-08 08:55): Doesn't matter. They are effectively closed. Mobile Chrome doesn't load them unless you click on them.
    - **u/WisdomSky** (↑3, 2026-10-08 11:11): correct. even safari does it too. i have 300+ tabs in my phone's safari.  [https://imgur.com/a/cmPSk9J](https://imgur.com/a/cmPSk9J)
- **u/dumbasPL** (↑2, 2026-10-08 08:52): > Monthly usage 50% used
    > Resets in 18d 8h
    
    Using exclusively DS 4.1f 
    
    So possible to run out, but that's only because I often have something spinning in the background on a side project.
- **u/zyxciss** (↑9, 2026-10-08 08:54): i used over 2.8Billion tokens over 6 days  (Opencode zen free tier)
  - **u/AdSmooth4982** (↑3, 2026-10-08 09:00): i cant use free models i made my own harness and it doesnt support zen free models it said i need to 'spoof' something but i didnt wanna do it and get potentialy banned
    - **u/ichisay** (↑2, 2026-10-08 10:17): No tienes que falsificar nada, solo tienes que configurar las cabeceras en las peticiones
      - **u/Odd-Elderberry-6328** (↑4, 2026-10-08 12:25): Today I've learned that "cabeceras" are headers in Spanish, in Portuguese this word means something totally different hahahaha
        - **u/Strong-Strike2001** (↑2, 2026-10-08 14:53): Que significa en portugués? Gemini lo logró descifrarlo jaja
          - **u/Odd-Elderberry-6328** (↑2, 2026-10-08 14:56): Well, how can I explain that hahaha, it's a mesita, which stays close to your bed during the night, where you put stuff you are going to need during the night
            - **u/ichisay** (↑2, 2026-10-08 16:30): Mesita de noche le dicen
  - **u/eachDayIWakeUp** (↑2, 2026-10-08 09:39): which model?
    - **u/AdSmooth4982** (↑3, 2026-10-08 09:53): i use deepseek v4.1 flash and kimi k2.7 code
    - **u/zyxciss** (↑2, 2026-10-08 10:40): fledge alpha + space bunny alpha (till it was free) , then exo
  - **u/evia89** (↑3, 2026-10-08 14:46): My opencode free tier gave me like 2-3M in 8h then it dies with 429
    - **u/Awkward_Intern2623** (↑1, 2026-10-09 21:33): I've been sitting here with 429s for a good while now, hours really, and I'm just wondering how long one's supposed to wait for them to let up.
      - **u/evia89** (↑1, 2026-10-09 21:36): I guess it depends on IP quality. If system think its  not residential or shared with other users or from "bad" country or proxy -> it will give less usage
  - **u/OkWrongdoer4038** (↑2, 2026-10-08 18:05): I have done 2B in 7 days (on Zen Free tier too). But I think a good model would have used 1B at the most.   
      It is not that good. On the other side, I tend to forget (or to avoid) to compact the context.   
      You gain in context but lose in accuracy. I think next week will compact more and maybe it will be more token efficient. Or split better the tasks with right specs (was all vibecoding managed by the distance by ChatGPT 5.6 Sol).
- **u/lgk01** (↑2, 2026-10-08 08:56): Really depends on the use you make of it, I went through my weekly limit in 4 days, my monthly is over 50% already 🫠
  - **u/AdSmooth4982** (↑1, 2026-10-08 08:59): damn use some flash models atleast they arent that bad bro.. i recomend deepseek v4.1 flash for debuging agentic coding and stuff and glm5.3 flash for web development deepseekv4.1 flash can do web development but glm is way better at full stack jobs
- **u/SeeTheWall** (↑2, 2026-10-08 09:35): I easily burned through two $10 Opencode Go monthly subscriptions in about 15 days.
    
    Actually, I managed to develop Kubernetes for Opencode with lightweight sandboxes based on bwrap and CoW copying. I worked on research in the field of semantic segmentation. I wrote my own SDD Gate plugin for Opencode, developed a small extension for Thunar, and created software to help me sort through 300 GB of junk files on an old win10 PC.
  - **u/AdSmooth4982** (↑1, 2026-10-08 09:39): youve done quite some work u did what models did you use? flash models are enough for me but your work requires some really good models or a normal model and a good software engineer
    - **u/SeeTheWall** (↑3, 2026-10-08 09:50): For the most part, I used DeepSeek 4.1 Flash. I think I managed to set everything up well: I have a full-fledged Linux machine, and the model works excellently when equipped with a bash shell and system utilities. In addition, seven MCP servers were involved (the model chose them on its own from the awesome-mcp list). I also used standard chatbots for project discussions and manual work; for example, Gemini 3.8 Flash in Google AI Studio is very good at keeping a conversation going.
- **u/Kylmawurr** (↑3, 2026-10-08 09:39): hah, im using only 1.3 contributor and 4.1 flash, rotating 4 accounts and still need a couple more soon.
  - **u/AdSmooth4982** (↑1, 2026-10-08 09:40): what are you workin on broo🫪
      can i look?
  - **u/bruno30303** (↑2, 2026-10-08 10:40): I was thinking in have multiple accounts, but I saw people telling that they were banned.
      
      Do you have any extra caution to use these accounts without being caught?
    - **u/AdSmooth4982** (↑1, 2026-10-08 12:26): multiple accounts get you banned??
    - **u/Able_Statistician688** (↑2, 2026-10-08 12:33): I sure hope not. You can setup up to 5 workspaces under a single email address and each can have its own go sub. So you didn’t even need to juggle different logins.
- **u/xatey93152** (↑-1, 2026-10-08 10:23): Dev please reduce the limit. I want opencode to stays longer.
- **u/XelomSit** (↑1, 2026-10-08 10:26): Looks like OP is tokenmaxxing Muse Spark 1.3 to its absolute limits
  - **u/AdSmooth4982** (↑1, 2026-10-08 10:32): oh thats the model that came out a month ago? i didnt test that model am mainly using deepseek v4.1 flash(the cache hits are crazy) what are your opinions on that model? should i switch?
    - **u/XelomSit** (↑1, 2026-10-08 10:37): Even I haven't used it much. I use MiMo2.6 Pro and DS4.1F
- **u/Single_Conclusion_52** (↑2, 2026-10-08 11:30): Bro you're the problem with our society. For me the limits are actually not enough.
  - **u/AdSmooth4982** (↑1, 2026-10-08 11:33): its not like the devs gave me 8x more usage or something.. hehe...
    - **u/Single_Conclusion_52** (↑-2, 2026-10-08 11:35): But keep it to yourself then 😂💔
      - **u/Single_Conclusion_52** (↑-2, 2026-10-08 11:36): Be like someone in a truly healthy & fulfilling  relationship. They dont update everyone online all the time bout whats happening.
      - **u/AdSmooth4982** (↑2, 2026-10-08 11:39): am just joking bro this is all cache hits from deepseek v4.1 flash that model relys heavly on cache hits
- **u/Odd-Profit-3833** (↑2, 2026-10-08 11:50): how is the speed of deepseek 4.1 flash in oc go? is it as fast as api key from deepseek ?
  - **u/LaPapaVerde** (↑2, 2026-10-08 21:19): It's slower that's for sure
  - **u/AdSmooth4982** (↑1, 2026-10-09 04:25): deepseek api will always be faster but oc api prices are cheaper and acording to my tests they are serving the 4 bit model for twice the price you can use the full 8bit model on deepseek tho both quantizations are good and using the 4 bit one for half the price is a good deal
- **u/onomastico** (↑20, 2026-10-08 14:02): I don't think you use it that much. I drain my 10$ sub in 15-20 days and started paying ChatGPT plus to balance my usage and make it to the whole month.
  - **u/AdSmooth4982** (↑2, 2026-10-08 14:04): i keep starting a new session everytime it gets to 300k tho deepseeks cache hits are crazy cheap
    - **u/onomastico** (↑6, 2026-10-08 14:10): You see? Your projects does not requiere and compactation at all because a new session still works for amount of context you prompts requiere.
      - **u/AdSmooth4982** (↑1, 2026-10-08 14:12): i use a handoff fike and 7 other documents i tell it to read the handoff and acording to the curent task i make it read one of those 7 files compaction gets lossy after a while 8 documents i can controll is safer
      - **u/AdSmooth4982** (↑1, 2026-10-08 14:19): also i forgot to mention i use sub agents HEAVLY like i wont let deepseek v4.1 flash actualy code i just make it use sub agents and it promts those subagents gets a report from them plans and continues i usually do 3 rounds of sub agents 7 agents at a time is max limit for debuging and stuff the subagent is deepseek v4.1 flash this way the main agents context wont fill up that much
        - **u/onomastico** (↑4, 2026-10-08 15:06): I do the same. I even use code-review-graph to try to use less tokens.
            
            I don't know if it is a difference in the size of our proyects (Not trying to under estimate yours and over estimate mine), but there is definately some difference which make us have not the same point of views.
            
            I'm just glad you make it to the end of the month with this sub.
          - **u/AdSmooth4982** (↑2, 2026-10-08 16:10): the qualty of the output degrades over the session aswell one time a model forgot how to make proper tool calls gave it a few chances than was like ok i guess this was too much than made it update the handoff and switched to a new session thats why i try to be bellow 300 tho i usualy end up at near 400 this is an usefull tool and it gets confused after a long time we need to monitor them good if we want a good output
        - **u/OlegPRO991** (↑4, 2026-10-09 08:39): What models do you use as sub agents?
          - **u/AdSmooth4982** (↑1, 2026-10-09 08:53): the main agent... its soo cheap the only reason am using it as a sub agent aswell as the main agent is because i dont wanna fill the main models context with tool calls and a fresh model with a straight job performs better than a model that changed its course a bajilion times
            - **u/IAmFitzRoy** (↑3, 2026-10-09 09:04): You didn’t answer the question.
                
                This makes me believe this is BS.
              - **u/AdSmooth4982** (↑0, 2026-10-09 10:38): i said deepseek v4.1 flash? like a few times? did you miss that?
                - **u/MFranz15** (↑2, 2026-10-09 12:31): you said in a previous comment that you won't actually let ds v4.1 flash code...
                  - **u/AdSmooth4982** (↑0, 2026-10-09 12:38): the main model that i was using i didnt want it to fill its context so i used subagents of it to do the job i think i worded it bad on the otiginal reply am sorry for that my english will improve in near feuture when i finish my uni in turkey
- **u/AdiCoSto** (↑8, 2026-10-08 14:06): OpenCodeGo is really a beast when it comes to value, and I love it, but recently it has slowed down so much that it kinda takes forever to be done with my work ... hope they fix it soon.
  - **u/AdSmooth4982** (↑1, 2026-10-08 14:10): in a market like this at leats they are trying to make it reachble to poorer users who cant afford to pay the api prices and other subscriotions like claude and openai are not open their cheapest useable sub 20 dolars and they dont give you an api key to use other agentic coding tools
    - **u/AdiCoSto** (↑2, 2026-10-08 15:41): absolutely. couldn’t agree more. I’ve used GPT, Claude, OpenRouter, [Z.ai](http://Z.ai) in the past, and honestly I still think OpenCodeGo is the best bang for the buck. period.
        
        No complaints on the value side at all. I’ve built some genuinely cool apps and workflows with DeepSeek V4.1 Flash, and I really can’t thank the DeepSeek + OpenCodeGo teams enough for making that kind of capability this accessible :)
        
        That said, my original complaint is still valid... OpenCodeGo has felt noticeably slower since the launch of the $40 Plus plan.
        
        And I’m saying that as a fan, not as someone trying to bash them. It actually saddens me a bit because I like the service so much. I just really hope the speed/TPS gets back to what it was before.
      - **u/AdSmooth4982** (↑1, 2026-10-08 16:16): thats weird? i havent really noticed any speed difrences in the last 2 months? well they are trying to cover more usage and we can tell from their docs that they dont have enough processing power to support it i guess thats why the 40 dolar plan is still good but people expected a acount that gives 4 opencode go acounts of usage am just glad they are trying to listen to the customers but i think in this case they shouldnt have it was a cheaper alternative to other subs at first the 40 dolar acount doesnt fit their current vision... (i couldve worded this better.. oh well❤️‍🩹)
  - **u/IntrepidMindExplorer** (↑2, 2026-10-08 14:53): Was curious on whether or not using free models was limited in some way compared to a subscription. Thanks for the heads up on that it's not. I was playing around with the free models last night on just a simple task (not coding, just working out a terminal command and it's usage) and noticed how slow it was. Night and day in way of speed compared to a couple weeks ago.
    - **u/AdiCoSto** (↑1, 2026-10-08 15:38): Yeah, absolutely. I’ve been using it a LOT. If you look at my GitHub, I’ve made over 3,000 commits this year lol, so I’m definitely a huge fan of the OpenCode Go subscription.
        
        But ever since they launched the $40 plan, I genuinely feel like they’ve made the experience worse. 
        
        Since that plan came out, the biggest thing I’ve noticed is the TPS has gotten painfully low. Like noticeably worse than before. I’m still using it because I like the service overall, but this part has been pretty frustrating lately. What is working for me is like I would have opencode go deepseek v4.1 flash set for subagents while the main orchestrator would be official deepseek api from openrouter ... that's been kinda working for me.
- **u/alphaQ314** (↑2, 2026-10-08 14:35): Which model. Muse is practically unlimited on their plan.
- **u/bobby_v_666** (↑0, 2026-10-08 14:50): best at
- **u/New-Worry5782** (↑2, 2026-10-08 15:05): is opencode or freebuff better? i think open code is also free (im broke)
  - **u/AdSmooth4982** (↑1, 2026-10-08 16:21): freebuff isnt free.. ur paying it with your own data
- **u/arielif1** (↑3, 2026-10-08 16:06): for most practical purposes this plan is unlimited DSv4.1 flash. By my calculations it's \~5B tokens per month.
  - **u/AdSmooth4982** (↑2, 2026-10-08 16:21): spot on its imposble to use em all lol😆
    - **u/yourpwnguy** (↑2, 2026-10-08 19:04): what plan is this ? 10$ or 40$
      - **u/AdSmooth4982** (↑1, 2026-10-08 19:28): 10$
- **u/somerussianbear** (↑4, 2026-10-08 16:28): GLM-5.3 on it is really expensive. Yesterday I got to 50% of 5h in 15min with a single session. 5.3 Flash goes far, but there’s a big distance between these models. DeepSeek 4.1 Flash is practically unlimited.
  - **u/AdSmooth4982** (↑0, 2026-10-08 16:30): YES deepseek is soo good at debuging and general agentic work glm is good at visual tasks make glm design the frontend deepseek handles backend like a champ
- **u/Ghilteras** (↑3, 2026-10-09 00:18): I finish my monthly quota with OpenCode go in a week just by using DeepSeek and glm5.3 flash so not sure what you're doing but you're probably not burning that many tokens
  - **u/AdSmooth4982** (↑-1, 2026-10-09 04:31): i only used kimi glm and deepseek v4.1 flash most of this is just deepseeks crazy cache hits ive done like 7 projects in this month a custom linux os for my baytrail tablet custom kernel oatches writen completly by deepseek an opencode android app that i ported it uses the real opencode binary to work its stable enough to do a lot of work aswell and another app code name spindle this is a native kotlin agent harness and i ginaly finished it after a long time working on it i love deepseek its soo good at code anylisis it ecplains why that code is there instead of what it does i love it i didnt use any free models on any of my projects and because of my custom harness i cant use zen free models...
    - **u/Ghilteras** (↑3, 2026-10-09 07:30): That's definitely not possible mate. Sorry I'm calling major BS
      - **u/IAmFitzRoy** (↑2, 2026-10-09 09:02): Agree. Kimi is going to burn those tokens really fast. I call this BS too.
        - **u/AdSmooth4982** (↑0, 2026-10-09 17:34): i only used kimi 2.7 code for like 5 tasks on ui and seeing kimi work was soo good it was purely focused on coding i just saw thinking and a tool call over and over kinda crazy how token efficient these models became... tho DeepSeek V4.1 flash handles a great many of things that i need i dont do ui much i can share my mountly model usage only 5 models!! you can also pull your calc out to like anylise what happened i can pull my github commit history and show you what was commited by kimi
- **u/openroom_xyz** (↑2, 2026-10-09 00:25): Well that free model is not even available I did even update the app wtf
  - **u/AdSmooth4982** (↑1, 2026-10-09 04:31): its all deepseek v4.1 flash
- **u/crotch-mavens** (↑3, 2026-10-09 05:29): Username checks out.
- **u/[deleted]** (↑1, 2026-10-09 06:02): [removed]
- **u/alfirusahmad** (↑2, 2026-10-09 08:57): Can you just keep quite!!!
  - **u/AdSmooth4982** (↑1, 2026-10-09 09:00): is this a secret or sumtin? those chinese models are soo cheap ofcourse itl last like a long time we have 60 dolars of usage on a 10 dolar sub like this is crazy
    - **u/alfirusahmad** (↑2, 2026-10-09 09:16): It will be much cheaper if you use free model as default, then fallback to paid model.
      - **u/AdSmooth4982** (↑1, 2026-10-09 10:39): i made my own harness and because of that i canot use zen free models i did try the space bunny on go i didnt do much with it
  - **u/kamwee** (↑1, 2026-10-09 16:10): Its like people dont learn
- **u/legolas427** (↑2, 2026-10-09 13:24): What model are you using and ik its great. Ran 3 simulators all mcp controlled for spot checks on my app via deep seek flash and it consumed only about 10-15 percent of whole month. FOR THE ENTIRE APP. I used to run one task via codex for mcp simulator and it took about entire week worth of usage lol
- **u/Hidden_Person_MG** (↑2, 2026-10-09 15:34): Gpt plus with opencode go is the best value you can get under 30 dollars. Gpt 6.1 sol at medium or high reasoning for orchestrating and deepseek doing all the work
  - **u/AdSmooth4982** (↑1, 2026-10-10 07:44): thats a more advanced workflow for 20 bucks!
- **u/Appropriate-Video-46** (↑2, 2026-10-09 16:47): What is this? Do I need it for developing or my home lab?
- **u/Standard_Wish** (↑5, 2026-10-09 18:24): I'm sure 50% if the comments are similar to what I'm about to add but here's my $0.02:
    
    Using opencodego, $10 and only about 68% of my monthly budget in ~20 days with a 5-Agent workflow (mini swarm or w/e):
    
    - DS Flash 4.1 (orchestrator, coder, designer, reviewer)
    - Kimi 2.7 Code (planner)
    - Jev (used by orchestrator)
    
    - Opencode
    - Tailscale
    - Openchamber
    
    After initial config on my home Linux machine, all development done from my phone.
    
    Generated
    - Free to host carpooling web app for my son's indoor climbing team. Includes email. Automates supabase, wrangler, etc. (not sharing the link, this app is being used and the free tiers are limited)
    - A hobby site providing a concordance reference & search function for AA recovery literature (basic texts.org)
    - A simple 2d ASCII dungeon crawler engine for web and mobile (GitHub released apk for android - uses Expo)
    - maintained and enhanced my tiny cli-five npx tool to incorporate Jev & Opencode now that GitHub copilot serves absolutely no purpose I can see.
    
    These models are remarkably efficient. Jev helps a good bit. Haven't even spent $10 and created the above while sitting on the toilet, voice dictating during my commute, etc.
    
    The only downside is the time to completion - lower than I'm used to with closed frontier LLMs.
    
    Note that none of the things I've created so far even begin to approach 'complex' or 'unique' so mid reasoning tier LLMs are fine for the work.
    
    I'm very impressed. Preaching to the choir but 5/5, would recommend to a friend.
  - **u/AdSmooth4982** (↑1, 2026-10-09 18:29): youve done wuite some work well done👍 
      60 dolars of usage on DeepSeek V4.1 flash and its a 10 dolar sub so am very happy about it
- **u/Khurrame** (↑2, 2026-10-10 07:04): When you are focussed on requirements and understand what/how its being built you cannot finish the quota for luna/flash etc models.
  - **u/AdSmooth4982** (↑1, 2026-10-10 07:43): YES instead of using the same chat and compact ing over and over again i just use 7 files and a handoff and chose a fike to read acording to the job
    - **u/moneytvdaily** (↑2, 2026-10-10 10:05): Try SMAA by lab1207
- **u/whhw311** (↑2, 2026-10-10 07:13): I feel you bro i have the same experience using claude for orchestration an luna/DS flash v4.1 at 40% in 26 days
  - **u/AdSmooth4982** (↑1, 2026-10-10 07:42): ds 4.1 flash is just soo cheapp 60 dorals of usage? in a month? imposble
- **u/[deleted]** (↑1, 2026-10-10 13:19): [removed]

---

## Speculation muse-spark-1.4-contributor page appeared in OpenCode Data — what to expect?
**u/Simple-Structure-890** · 2026-10-08 08:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0l6ev/speculation_musespark14contributor_page_appeared/)

[removed]

---

## opus 5.5 for 8$ per million token?
**u/ruboxytr** · 2026-10-08 07:44 UTC · ↑2 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0kvh3/opus_55_for_8_per_million_token/)

stumbled across this where they lets you use 5.5 for 8$ apparently, sus but tried it out of curiosity and it somehow works. the rpm is probably like 10 because i easily got rate limited but still cool nonetheless. its called [excelnt ai](https://excelnt.ai/signup?ref=unc-06da) and they are giving away lots of usage apparently. try it out if you want and thank me later ;)

**Comentarios:**

- **u/pigletmonster** (↑1, 2026-10-08 07:50): Most definitely routing to a different model. Another inference provider was exposed for doing that last month.
- **u/DesignerSeparate3619** (↑1, 2026-10-08 08:28): is that price even worth it for roleplay bots or do cheaper models handle the back and forth fine?

---

## Which free OpenCode models are fast, reliable workers?
**u/petburiraja** · 2026-10-08 07:43 UTC · ↑21 · 17 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0kuv2/which_free_opencode_models_are_fast_reliable/)

Free stops being useful if the worker stalls or leaves broken code.

I tested 10 OpenCode free models on Oct 8, 2026.

Q&A: probability and executed code; agentic: fix two failing tests, verified by pytest and unchanged test-file hash, 420 s timeout.

| Rank | Model | Score | Q&A | Agentic fix | Seconds |
|---:|---|---:|---|---|---:|
| 1 | mimo-v2.6-flash-free | 100 | 2/2 | pass | 129 |
| 2 | muse-spark-1.3-contributor-free | 99 | 2/2 | pass | 132 |
| 3 | space-bunny-free | 95 | 2/2 | pass | 167 |
| 4 | longcat-2.5-preview-free | 92 | 2/2 | pass | 214 |
| 5 | ling-3.1-flash-free | 91 | 2/2 | pass | 220 |
| 6 | nemotron-3-ultra-free | 70 | probability wrong | pass | 257 |
| 7 | nemotron-3.5-lightning-free | 20 | probability wrong | timeout, 2 failing | 422 |
| 8 | exo-free | 0 | failed/timeout | not run | n/a |
| 8 | fledge-alpha-free | 0 | failed/timeout | not run | n/a |
| 8 | ling-3.0-flash-fin-free | 0 | failed/timeout | not run | n/a |

Score (0-100): floor(20 per correct Q&A item + 40 per passing fix + 20 × 129/seconds for passing fixes only).

Try MiMo or Muse first; Space Bunny is the next pick.

- Keep tests as the oracle.
- Avoid secrets/private data: free models may log prompts.
- Re-check availability and rate limits.

Single repo runs cannot establish reliability; seconds are repo runtime including startup and parallel contention.

Share a free model's fix result and runtime.

**Comentarios:**

- **u/Mr_Lucas2000** (↑5, 2026-10-08 07:49): Mimo 2.6 flash quite smart, context limiting it but works for a few hours if it needs to better than muse in my opinion
  - **u/AmbitiousAthlete7324** (↑1, 2026-10-09 10:57): it have arte limit.
- **u/amethyst_mine** (↑-1, 2026-10-08 07:55): deepseek 4.1 flash?
  - **u/TruBustedElbow** (↑7, 2026-10-08 08:03): its not free anymore
    - **u/amethyst_mine** (↑1, 2026-10-08 08:04): didn't read free mb
- **u/Competitive-Yak-8255** (↑0, 2026-10-08 08:05): Nice
- **u/trowawayatwork** (↑1, 2026-10-08 10:11): big pickle?
- **u/Nenad1979** (↑9, 2026-10-08 10:15): If only mimo didn't spend 10 fucking minutes thinking about how to delete a file
  - **u/plmtr** (↑1, 2026-10-08 12:48): Same here, have had Mimo as Designer in my OMO-Slim setup and takes a long time, but results have been accurate
- **u/adrnptcl** (↑2, 2026-10-08 10:55): Mimo and Space Bunny do wonders for me
- **u/Interesting-Movie452** (↑2, 2026-10-08 11:12): what about big piclkle
  - **u/YoRt3m** (↑3, 2026-10-08 12:05): Isn't Big Pickle a different model from time to time?
    - **u/FacuA0** (↑3, 2026-10-08 13:05): Big Pickle is whatever other model opencode big picks at the moment.
- **u/plmtr** (↑2, 2026-10-08 12:44): And the new one to try today: exo-free
- **u/sudoer777_** (↑2, 2026-10-09 00:32): I tried LongCat 2.5 Preview yesterday and the connection was extremely unreliable and slow, but when it did work it wasn't terrible.
- **u/Available_Mood_1212** (↑1, 2026-10-09 07:29): Big pickle works the best for me. 
    
    BTW I also use mimov2.6 flash and is quite good... for me
- **u/Traditional_Pie_8262** (↑1, 2026-10-10 02:45): the unchanged test hash is such a smart guard against the agent editing its own oracle. do u separate provider queue time from model time? quick disclosure, this is a client related note about raven.

---

## Does anybody else have this strange behavior?
**u/KsLiquid** · 2026-10-08 07:31 UTC · ↑1 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0koje/does_anybody_else_have_this_strange_behavior/)

There is one specific folder. When I run "opencode" in a terminal there, the session does not start at that folder, it starts at \~. And I am unable to attach the session to the correct folder.

The "fix" is to delete opencode.json, run opencode, add opencode.json back and run opencode again. But a few hours later, the issue re-appears.

This happens only in one specific folder. All other projects work as expected: i run opencode and I am in the same folder where I ran it.

Did anybody experience this and knows how to fix it?

**Comentarios:**

- **u/Ctbhatia** (↑1, 2026-10-08 17:44): try opencode "$PWD" so the folder is explicit ([CLI docs](https://opencode.ai/docs/cli/#tui)). if it still opens ~, keep that command in the repro rather than deleting the config again.
  - **u/KsLiquid** (↑1, 2026-10-09 07:12): Passing the folder explicitly does not help :/

---

## OpenCode Terminal Text Coloring is Unreadable
**u/WeOfferTheSun** · 2026-10-08 06:43 UTC · ↑1 · 8 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0jwta/opencode_terminal_text_coloring_is_unreadable/)

[OpenCode Terminal Unreadable Light Coloring](https://preview.redd.it/x9dm33lvv6uh1.png?width=701&format=png&auto=webp&s=82391a7f8414904740c0e7b716a5a80b73f478e9)

[OpenCode V2 Appearance Settings](https://preview.redd.it/ofkpmjd3w6uh1.png?width=771&format=png&auto=webp&s=78eb87e2649ac06b0e40556afd66e7ebbe86917e)

As you can see (if you can see it!) whatever i type appears in very light-yello/grey which makes it almost impossible to read!

**Comentarios:**

- **u/acakaacaka** (↑1, 2026-10-08 06:56): Darkmode?
  - **u/WeOfferTheSun** (↑1, 2026-10-08 07:12): I can't during day because of too much reflections on screen.
- **u/torrso** (↑3, 2026-10-08 07:31): Isn't this because your shell's colors are meant for dark background? The same should happen if you turn such light mode on in the regular terminal unless you modify your shell's theme.
  - **u/WeOfferTheSun** (↑1, 2026-10-08 07:41): hmm, makes sense. but shouldn't this be handled by the IDE?
    - **u/torrso** (↑1, 2026-10-08 07:47): Maybe it could, maybe it should, maybe not, I suppose that's a different philosophical question. What should it do if the user's shell colors are already set for light mode? Look at the screen and think if the colors make sense now? 
        
        MicroSoft has made instructions for this:  
        [https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/using-light-theme?view=powershell-7.6](https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/using-light-theme?view=powershell-7.6)
      - **u/WeOfferTheSun** (↑1, 2026-10-08 08:40): that is too much overcomplicating. i've been using IDEs for ages before OpenCode whether in dark or light mode, the shell in them is readable. btw, my shell colors are the defaults. so at least the ide shall support the defaults.
          
          thanks for the link i will check it out
        - **u/torrso** (↑2, 2026-10-08 08:56): I looked into how VS Code handles this, and you're right. The problem isn't really that OpenCode needs to detect your shell's theme. It's that OpenCode changes the terminal background for light mode without adequately adapting the foreground/ANSI colors to go with it. VS Code changes its terminal palette with the theme and even adjusts colors that don't meet its minimum contrast ratio.
- **u/dumbasPL** (↑0, 2026-10-08 10:44): GUI, windows, powershell. The worst combo possible.

---

## I was using Kimi to code when suddenly...
**u/Professional_Log1367** · 2026-10-08 02:09 UTC · ↑0 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0f03r/i_was_using_kimi_to_code_when_suddenly/)

**Comentarios:**

- **u/Background-Leg-6840** (↑1, 2026-10-08 04:57): This has happened to me with some other Chinese models such as Minimax. 
    
    Assuming something in the code base that you're working and didn't cause this I just create a new conversation. 
    
    If you are looking for a diagnosis I usually just attribute it to the models being primarily bilingual being trained heavily on Chinese and English, in the case of this bug giving you a tug of war between the two.

---

## How to fully migrate from Codex to OpenCode
**u/sky__s** · 2026-10-08 01:31 UTC · ↑5 · 6 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x0e8np/how_to_fully_migrate_from_codex_to_opencode/)

Since I moved away from OpenCode 5-6 months back, I have been using codex ever and modified that harness a good bit, I use custom models from a private DC connection, bedrock, my ChatGPT subscription. I think I have on order of 100 or so skills/tools/mcp, and I want to do the bridging to get computer use from codex with the hidden mac Sky API going as well (using https://github.com/ifuryst/open-codex-computer-use). I quite liked codex but a big deal breaker for me is now how they handle usage, if you run out of codex usage it locks up the entire UI for work submission, making things unusable. I dont want to deal with that and it seems like my biggest hold-up is now gone (strong application computer use in other harness).   
  
Now I just want to see if I can migrate my logins/api/models, the skills I have on codex, and ideally even all my past sessions and folders, into opencode. Is there any one in all solutions out there I can use, and if not how would I fully offboard from codex and onboard to opencode again with everything intact?

**Comentarios:**

- **u/Antique-Ad6542** (↑2, 2026-10-08 01:52): its very interesting. I use paseo for a similar reason. It still uses codex for computer use though. IF this is a good comparison, might be worth adding to the kit.
- **u/ameeno1** (↑1, 2026-10-08 02:30): I saw on deepseek API page you can use deepseek on codex  so why not have other models or subs like opencode go or zen?
  - **u/sky__s** (↑2, 2026-10-08 02:33): well the thing I dont like is if i use up all my subscription for codex it locks me out at a UI level from using codex, that's a non-negotiable UX mistake for me. So I'm trying to switch harnesses and have all this baggage to migrate
    - **u/ameeno1** (↑1, 2026-10-10 07:17): I mean technically if you wrapped codex in different API, your not locked out?
- **u/ichisay** (↑1, 2026-10-08 10:06): Siempre puedes pedirle a sol o Astra que te lo haga
- **u/Ariquitaun** (↑1, 2026-10-08 17:16): Ask codex to migrate from opencode.

---
