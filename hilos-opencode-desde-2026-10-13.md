# r/opencode — hilos 2026-10-13 → 2026-10-16
_Generado: 2026-10-15T02:48:50.098707+00:00 · 100 hilos · 485 comentarios · fuente: Arctic Shift_

## New user here - what are the usage limits of opencode free?
**u/hillman_avenger** · 2026-10-14 19:59 UTC · ↑1 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x61fo6/new_user_here_what_are_the_usage_limits_of/)

I've just started using OpenCode and it seems great.  I'm pretty new to AI in general.  I'm using Big Pickle since it's the default, but it seems fine.  What are the usage limits, and what happens when I exceed them?  And is there any way to find out how much I've used or got left?

---

## [ Removed by Reddit ]
**u/Hafid3x** · 2026-10-14 19:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x610mf/removed_by_reddit/)

[removed]

---

## How to download opencode desktop V2?
**u/NeedleworkerSilver31** · 2026-10-14 19:36 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x60v3c/how_to_download_opencode_desktop_v2/)

My agent successfully upgraded the CLI version of OpenCode to v2, and now it’s diligently trying to upgrade the desktop app, but it seems like v2 for desktop doesn’t exist. Why, then, do absolutely all the models keep insisting that it does? So I’d burn more tokens?

**Comentarios:**

- **u/ichisay** (↑1, 2026-10-14 19:48): En el repositorio de opencode v2, hay una carpeta de Desktop, pero está sin terminar o sin acabar de implementar. Se  puede probar a compilar su contenido para crear el Desktop v2, pero dudo que esté terminado. Otra opción es cambiar el Desktop v1 para que use el cli de v2. Yo empecé a usar en serio ayer el tui de v2 y estoy peleándome para adaptar los plugins .

---

## How to know which model works best each repo?
**u/OkPride1321** · 2026-10-14 19:16 UTC · ↑1 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x60c0d/how_to_know_which_model_works_best_each_repo/)

Do you guess ever face problem like which model to use sonnet, opus, cheap chinese models? which is most cost effcient.I used to just throw opus and sonnet on any problem but i want to ask you what you guess do?

**Comentarios:**

- **u/RepulsiveRaisin7** (↑2, 2026-10-14 19:21): A good model does well in many different situations so I don't find myself switching a whole lot. My main model is GLM 5.3 Flash, it's intelligent and pretty cheap. For review, I invoke Deepseek 4.1 Flash because a second pair of eyes is always better than one. On Opencode Go, you might flip these since DS is cheaper.
    
    Models like Opus are needed when you have a very complicated task or a task that is poorly specified. High-end models are best at planning, but you don't "need" them for implementation. Some people use Opus for everything and I think that's kinda dumb, but that's their choice.
- **u/AdFun4897** (↑1, 2026-10-14 19:37): Just use Opus 5.5 on medium with Claude Code $20 plan for most tasks. One shots most taks, and better usage than any of the top models on opencode go
- **u/IAmFitzRoy** (↑1, 2026-10-14 19:38): It depends what are you doing. Coding? Categorizing? One-off decisions? Vision related? To you need tools? Web-search grounding? RAG?
    
    You want something fast/expensive? slow/cheap?
    
    Every use case will point to a different model.
- **u/Safe-Imagination8538** (↑1, 2026-10-14 19:47): id skip leaderboards for this and build a tiny eval from the repo itself. take 10-20 bugs you already fixed, reset to the commit before the fix, let each model try with the same harness and the same step limit, then run the tests. also log the time. on my 12gb card a big moe was about 5x slower per agent step than qwen 35b-a3b, and in a small test the step limit decided more of the result than the model did

---

## Cat jam free
**u/Few-Advertising-3538** · 2026-10-14 18:57 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5zt6h/cat_jam_free/)

Muse spark 1.4??? Very fast, only problem is low context. Possibly for the beta only? I'm recording around 200tps which is inline with 1.3 just no images.. weird.

---

## What model is Space Bunny running right now? It's really good. We need to know.
**u/alcogiggles** · 2026-10-14 17:59 UTC · ↑2 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5y9y6/what_model_is_space_bunny_running_right_now_its/)

The model is reminding me of Big Pickle from June/July when it was incredible. How do we can find out right now what model Space Bunny is using?

**Comentarios:**

- **u/AdFun4897** (↑1, 2026-10-14 18:06): Its probably a new minimax model
- **u/A_Far_Hitman** (↑3, 2026-10-14 18:10): I have noticed in zen, when free muse limit is over, I can't use space bunny
    
    Other free models work fine
- **u/Amarsir** (↑1, 2026-10-14 19:33): We think Minimax 3.1. They might use a different naming scheme but it's almost certainly them.
    
    I don't know why they're waiting so long to reveal though. Even if they're still developing, just take credit and work on the next release. The main effect of the codename is that it's not properly benchmarked and credited. Which is fine if you're not sure. But if you see that people like it, all waiting does is ensure that by the time you reveal the competition has advanced.
  - **u/Global_Persimmon_469** (↑1, 2026-10-14 19:50): Minimax has a 3.1 flash preview version on their chat
- **u/warpaint_james** (↑1, 2026-10-14 19:35): Yeah just tried it out until I got limited. It is really nice to use. Fast, competent, verbose but not overly so. Almost anticipated a lot of what I wanted
- **u/alcogiggles** (↑1, 2026-10-14 19:46): I'm having it build a couple of python-based desktop tools and it's fast.   
    It doesn't waste tokens trying to add fillers in our conversation either. It's really efficient in responses.   
    It brainstorms ideas for me really nicely, better than chatgpt.   
    I like how it researches, does its own due-diligence against its own recommendations too.   
    It pressure tests it's own implementations. 
    
    It fixes things that deepseek 4.1 flash couldn't.

---

## [ Removed by Reddit ]
**u/wordkush1** · 2026-10-14 17:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5y1r2/removed_by_reddit/)

[removed]

---

## switching models with /models halfway through a task
**u/Ctbhatia** · 2026-10-14 17:42 UTC · ↑1 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5xssn/switching_models_with_models_halfway_through_a/)

say the first model has been stuck on a bug for a while and I switch to another one mid session. the new one reads the whole history, including the 3 fixes that didn't work, and can end up trying a 4th version of the same idea

a fresh session with a short note avoids that, but then I'm re-explaining the whole task

has anyone found switching in place actually works better?

**Comentarios:**

- **u/Cyvster** (↑1, 2026-10-14 17:48): you could have the model write a handoff document and then do a session /compact
- **u/repepeper** (↑1, 2026-10-14 18:40): /compact and /fork ? or pocock's /handoff

---

## Cache rates for Deepseek V4 Flash on OpenCode Go are abysmal
**u/AutomaticTough7082** · 2026-10-14 17:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5x3de/cache_rates_for_deepseek_v4_flash_on_opencode_go/)

[removed]

---

## Opencode Go DSV4.1 Flash Usage has been gutted
**u/AutomaticTough7082** · 2026-10-14 16:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5wnaf/opencode_go_dsv41_flash_usage_has_been_gutted/)

[removed]

---

## Reflection problem...
**u/Striking_Sandwich_80** · 2026-10-14 16:20 UTC · ↑1 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5vn5k/reflection_problem/)

https://preview.redd.it/0cvsamemmgvh1.png?width=1460&format=png&auto=webp&s=63d037805ffe19cbd4f0ff520b11f83a1719c071

Pourquoi l'affichage du processus de "réflexion" ne s'affiche-t-il plus correctement une fois que la conversation atteint une certaine taille ?

https://preview.redd.it/qvirqvipkgvh1.png?width=2088&format=png&auto=webp&s=b30610870e62d4e14c5fea506f33914b4c6e59ae

**Comentarios:**

- **u/cornelha** (↑2, 2026-10-14 16:27): We generally call it the dumb zone, so yeah
  - **u/Striking_Sandwich_80** (↑1, 2026-10-14 16:32): Yeah, I have to admit...

---

## but im using opencode already
**u/Environmental-Ad3110** · 2026-10-14 14:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5t67g/but_im_using_opencode_already/)

???

**Comentarios:**

- **u/Tawfik_404** (↑6, 2026-10-14 15:28): same happened to me when i added a opencode.json to opencode config folder
  - **u/Environmental-Ad3110** (↑1, 2026-10-14 15:36): But i didnt added anything, it just stuck in the middle of work like that.
- **u/SnarkyWalrus1** (↑2, 2026-10-14 15:45): glad im not the only one. middle of a slop sesh again!!!! very sad!
- **u/Scary-Wolverine265** (↑3, 2026-10-14 15:56): If your OpenCode configuration has a provider: https://opencode.al/zen/v1", then simply delete it from *.config\opencode\opencode.jsonc" and it should work. It's the change you made yesterday to fix the Opencode provider issues
  - **u/SnarkyWalrus1** (↑1, 2026-10-14 16:16): can confirm it was this!
      
      absolute slop hero over here 🔥
  - **u/Awkward_Bottle4887** (↑1, 2026-10-14 16:35): I deleted all providers, including local one, and still doesn't work unfortunately.
      
      Looks like I had to delete my entire configuration. It seems like it fixed my big pickle issue as well.
      
      ~~I can't reinstall one  of my important plugin, AFT. Added but doesn't work.~~ it magically worked now.
    - **u/Jazzlike-Temporary45** (↑1, 2026-10-14 17:15): Bro, clear system promt. Its work for me
      - **u/Awkward_Bottle4887** (↑1, 2026-10-14 17:18): I'm not sure what system prompt mean, but I always tested them on new session.
          
          Well it's somehow fixed itself now.
- **u/Awkward_Bottle4887** (↑3, 2026-10-14 16:01): I was just about to ask this.
    
    I felt like I have been fighting OpenCode restriction on free model. First it stopped working for OpenCode's plugin even though it was request for opencode, now it doesn't work from opencode at all.
    
      
    I wonder, does it only happen to people who uses OpenCode v1 because v2 already released? I only have been using v1, I'm still afraid to update and broke my plugins.

---

## My last month's model stats
**u/LinsaFTW** · 2026-10-14 14:38 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5sy11/my_last_months_model_stats/)

**Comentarios:**

- **u/GRANDMA_FISTER** (↑1, 2026-10-14 17:43): What are you using them for that Luna is the only one writing to cache?
  - **u/LinsaFTW** (↑1, 2026-10-14 18:53): I am not sure, maybe something to do with those models or the platform? I use opencode and write java

---

## To Opencode team: Can you add option to select date range along with the existing 7, 30 and all time options.
**u/Ok_Cartographer5609** · 2026-10-14 14:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5soh4/to_opencode_team_can_you_add_option_to_select/)

Title

---

## Cheapest Uncensored AI api provider?
**u/slaxerz** · 2026-10-14 14:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5sduy/cheapest_uncensored_ai_api_provider/)

ive been trying to find one since reversing things take a lot of rejections by normal models, any websites that provide cheap subscription or pay as you go?

**Comentarios:**

- **u/seeKAYx** (↑0, 2026-10-14 14:50): GLM 5.3 Flash works pretty good for me with RE stuff. Just tell you are Red Teaming and simulating stuff etc. I’m using opencode go
- **u/sam7oon** (↑1, 2026-10-14 15:30): you can try ArliAI, but the models are not perfect, but it's totally uncensored
- **u/Infamous-Grand-5778** (↑1, 2026-10-14 17:46): glm 5.3 flash uncensored from nanogpt ($12/mo for 60mil input a month)
  - **u/Aggravating-Push-207** (↑1, 2026-10-14 18:40): lmao what a scam

---

## Free inference providers, with usable and intelligent models?
**u/nuelgoeshard** · 2026-10-14 14:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5s7ff/free_inference_providers_with_usable_and/)

[removed]

---

## TOOL SYSTEM NOW OPERATIONAL — DEPLOYMENT ACTIVE, MAINTENANCE WINDOW PENDING
**u/N0M4DIN** · 2026-10-14 13:56 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5rwqp/tool_system_now_operational_deployment_active/)

[removed]

---

## I love overusing muse spark 1.3 on open code > deepseek 4.1
**u/Difficult-Essay95** · 2026-10-14 13:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5rpk8/i_love_overusing_muse_spark_13_on_open_code/)

---

## billed for a model i didn't use
**u/Cyvster** · 2026-10-14 13:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5qve6/billed_for_a_model_i_didnt_use/)

i just activated the $10 plan yesterday. it used up 15% of my monthly usage in a few hours. i checked the log to see why and it is all from around 700k tokens charged to claude haiku. i don't even have that as an option in my list. i set my list to only show deepseek 4.1 flash, muse 1.3 contributor, and the free models.

how do i reach opencode about this?

**Comentarios:**

- **u/Ctbhatia** (↑1, 2026-10-14 14:21): see if those haiku calls track your session count rather than your prompts, since titles and summaries can bill separately.
  - **u/Cyvster** (↑1, 2026-10-14 14:42): i'm not sure what that means. i just noticed that the free cat model is not listed. i think it billed me for haiku instead of the free cat model.
      
      claude-haiku-5-5	108	240	10.3M	711.0k	439.4k	$1.23
      deepseek-v4.1-flash	23	905.4k	17.6M	-	13.0k	$0.27
      muse-spark-1.3-contributor	145	1.4M	33.4M	-	79.3k	$0.23
      step-5-preview-free	496	4.3M	299.8M	-	233.7k	$0.00
    - **u/Ctbhatia** (↑1, 2026-10-14 16:14): it is opencode's small\_model, the one that handles titles and compaction. set small\_model to a free model in opencode.json and those background calls stop billing.
      - **u/Cyvster** (↑1, 2026-10-14 16:25): yes, it was something like that. i had opus5.5 investigate. muse was spawn subagents and was selecting haiku models. opus set a per model block list to restrict access to other models. it is crazy that by default a muse model can spawn expensive models to do work for it.
        - **u/Ctbhatia** (↑1, 2026-10-14 17:09): yeah, that block list is the right fix. does it cover the subagent spawns too, or only the model you pick in the main loop?
          - **u/Cyvster** (↑1, 2026-10-14 17:11): opus5.5 told me it is an allow list for my entire go plan. i thought the allow list in the opencode account pane restricted access but it doesn't. it just chooses what is displayed.
            - **u/Ctbhatia** (↑1, 2026-10-14 19:42): ah so the pane was never the gate, the plan-level list is. did that list actually stop the haiku spawns, or just hide them from the picker?

---

## Decision Models in OpenCode GO?
**u/Mancho_United** · 2026-10-14 13:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5qq6t/decision_models_in_opencode_go/)

---

## I Ran the Horse Test on Every Free AI Model on OpenCode
**u/ItsHarvcker** · 2026-10-14 13:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5qocq/i_ran_the_horse_test_on_every_free_ai_model_on/)

I ran the horse test on every free OpenCode model.

The prompt I used was:  
(Create a low-poly 3D horse running in a seamless loop using Three.js. Build it procedurally from primitive geometry, animate the legs, body, head, and tail, and return a single self-contained HTML file)

If you don't want to download the results to see for yourself, here's my opinion:

**Horse quality:** Step 5 Preview dominated, followed by Ling 3.1, then Big Pickle, then Muse Spark 1.3.

**Overall qualIty:** Big Pickle wins IMO, but if you're judging purely on the quality of the horse, look at the results I mentioned above.

  
Nemotron 3.5 Lightning did the worst, its file doesn't even run

**Comentarios:**

- **u/ItsHarvcker** (↑1, 2026-10-14 13:08): honourable mention: mimo v2.6 looks amazing but took like 40 minutes
- **u/SrAlexis_** (↑2, 2026-10-14 17:55): That's interesting, but what's the purpose of the horse test? I don't recall ever hearing about that test hahaha. What is the objective?

---

## Experience Opencode v2 on termux
**u/Tasty_Owl_7930** · 2026-10-14 12:56 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5qiki/experience_opencode_v2_on_termux/)

So recently, Opencode released v2. and I've tested it on my Tecno KL4 device. Compared to v1, the v2 is smoother and more responsive, with no lag at all. and I'm running 9router and astrojs together with.

Btw i used proot distro fedora

**Comentarios:**

- **u/[deleted]** (↑1, 2026-10-14 13:18): [removed]
- **u/LuluLeSigma** (↑3, 2026-10-14 13:34): why is there a weird dynamic island
  - **u/shameless_inc** (↑1, 2026-10-14 14:12): There are Android apps that give you such a feature. Maybe the screen recorder triggered it to show up without anything else in it. Or maybe it's just the normal overlay that lets op control the recording.
- **u/tinmicto** (↑1, 2026-10-14 14:34): I see you're using termux-launcher,  do you mind trying out the opencode thats in "tlstore" ? 
    
    Works natively and is v2. You can either install using the tlstore TUI or "tlstore install opencode" should also work.
- **u/JuraganMinyak** (↑1, 2026-10-14 15:18): What is the keyboard that you use?
- **u/HandIllustrious8260** (↑1, 2026-10-14 16:23): what did you do to your termux

---

## Exo-Free
**u/Valuable-Mirror-448** · 2026-10-14 12:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5qh61/exofree/)

not gonna add grammar here because its not a big thing just wanna point out exo free should be removed from the dashboard because its deprecated just a heads up

---

## Qwen 3.8 27B Abliterated.
**u/Valuable-Mirror-448** · 2026-10-14 12:49 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5qd5j/qwen_38_27b_abliterated/)

Where can u use this model for free with decent allowance. I dont have enough RAM to run it on my main PC before anyone hates.

**Comentarios:**

- **u/ConsiderationNo9952** (↑1, 2026-10-14 13:30): you can run qwen 3.8 flash orca router on vast using strata
    
    but yeah no one is offering for free...
    
    venice has some unrestricted models (pay per tk)
    
    also i haven't tried this yet... [feihoa.com](http://feihoa.com)
  - **u/rafaelsbrscs** (↑1, 2026-10-14 13:57): someone uses [feihoa.com](http://feihoa.com/), works fine?

---

## I thought the x8 slot was slowing down my OpenCode turns with Qwen3.6 39B-A3B
**u/AnyAsparagus2539** · 2026-10-14 12:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5pyqk/i_thought_the_x8_slot_was_slowing_down_my/)

Last week I was in a long OpenCode session and every message I sent took longer to get going than the one before, once the model started writing it was fine. OpenCode runs on my laptop and talks to llama-server on my desktop, Qwen3.6 35B-A3B at Q4\_K\_M on a 4060 Ti 16GB with most of the experts left on the CPU through --n-cpu-moe.

I assumed it was the slot. The card runs at PCIe 4.0 x8 and I had just read a thread about 16GB cards on half the lanes. With the experts on the CPU llama.cpp has to copy them to the GPU for every batch of prompt it processes. I raised -ub and it helped a little. I also ran the same session against a llama-server on HyperAI with a card the whole model fits on, it took some fiddling to get OpenCode connected to it, and the pauses there were shorter and grew with the conversation the same way.

I had not been reading the server output because it runs on the other machine. When I looked, most turns had this in them:

"forcing full prompt re-processing due to lack of cache data (likely due to SWA or hybrid/recurrent memory, ...)"

It showed up on the bigger card too. Every one of those turns was the full prompt processed again, plus the expert copies over PCIe on my desktop, no wonder I blamed the slot. I looked the line up. The 3.6 models are hybrid and the recurrent part of the state cannot be rolled back partway, any difference from the cached prompt with no checkpoint before it sends the server back to the first token.

I turned on verbose logging and compared the prompt for two turns in a row, the thinking from the earlier turn was missing in the second one. The chat template 

strips it, and I do not get why that is the default on a model pitched for agentic coding. With preserve\_thinking passed through the template kwargs most turns reuse the cache now. Keeping the thinking fills the context faster though and OpenCode compacts more often. Every compaction breaks the cache anyway, the summary does not match anything the server has. The last long session went back to full re-processing twice, both right after a compaction, so the context checkpoint settings are what I am messing with next.

**Comentarios:**

- **u/Atretador** (↑1, 2026-10-14 12:38): CTX\_CHECKPOINT adn RAM\_CACHE to avoid full prompt reprocessing on new messages, its quite annoying - also, instead of offloading layers to the CPU - check out expert caching solutions like this CUDA one: [https://github.com/GenerelSchwerz/llama.cpp/wiki](https://github.com/GenerelSchwerz/llama.cpp/wiki)
    
    its gonna need bout 5gb/s on pci bandwidth I believe, Ive noticed bout 40-70% increase in TG on my MI50 with ROCM and a generic solution.
- **u/Sakura010826** (↑1, 2026-10-14 13:16): I started opening a fresh session whenever the context got close to the limit, instead of letting it compact..the first turn in the new session is slow, but after that the cache holds.
- **u/One-Abroad1973** (↑1, 2026-10-14 13:53): Checkpoints can still help after compaction, since the system prompt and tools at the front do not change.
- **u/Ctbhatia** (↑1, 2026-10-14 14:22): your read on the hybrid state is right, so the fix is a checkpoint close to where the conversation diverges, not the slot.

---

## monthly opencode-go limit reached. Have I misunderstood the deepseek increase, i thought it went up to $80?
**u/NoSatisfaction1779** · 2026-10-14 10:12 UTC · ↑32 · 8 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5nfeo/monthly_opencodego_limit_reached_have_i/)

https://preview.redd.it/2ub5wpkznevh1.png?width=2149&format=png&auto=webp&s=aa0acc2245cb9adc2759bbb4b93f43e42e9f0c19

https://preview.redd.it/nujnz432oevh1.png?width=1993&format=png&auto=webp&s=0e4d40e7b6dc6588c85c709352808a438249d60d

I have only used DeepSeek and the free models, but my opencode-go subscription has met the limit. I thought Opencode increased DeepSeek to $80 in credit; did I misunderstand?  Does the increase only start after a user's next billing period, maybe? I couldn't find any information on this in their docs.

**Comentarios:**

- **u/xRebellion_** (↑26, 2026-10-14 10:17): So before the limit increase, assume you have spent 30$ (50% of overall limit) worth of DS. Then the limit increase happens. You end up with 40$ worth left (still 50% of overall limit), not 50$.
  - **u/NoSatisfaction1779** (↑3, 2026-10-14 10:31): Thanks! Do you know where I should have gone to learn this stuff? I thought I had done my due diligence, but obviously not. Trying not to make a similar mistake in the future.
    - **u/eastlin7** (↑-16, 2026-10-14 10:36): I mean. Is it even a big deal? Just drop it and move on.
    - **u/xRebellion_** (↑11, 2026-10-14 10:43): Oh you're not in the wrong here at all. The previous UI made it clear how the costs worked. After it got changed, plenty of important info surrounding the costs got omitted. It's not even documented in the docs. Not understanding it is absolutely understandable
- **u/dumbasPL** (↑2, 2026-10-14 10:25): The usage is not a dolar value, it's dolar equivalent converted to percentage. Otherwise you couldn't track combined usage across different usage caps.
    
    Each time you make a request: percent used += request price / model usage * 100
    
    Most of the requests were made using the old pricing, usage that was already consumed, is consumed, only requests since the new change use less usage per request.
- **u/s-i-e-v-e** (↑5, 2026-10-14 10:52): The pricing tables are needlessly confusing. They should simply follow [Tarsnap](https://www.tarsnap.com/picoUSD-why.html) theory and use micro(dollar)s as the unit of charge.
    
    $1 = 1,000,000 µ$
    
    So, they credit 10M µ$ to your account when ther subscription is renewed. And they can drop the multipliers and quote limits in µ$.
    
    Makes reasoning so much simple.
  - **u/Aggravating-Push-207** (↑2, 2026-10-14 18:39): Or, hear me out: use real $?
- **u/xapep** (↑1, 2026-10-14 15:25): The $80 bump applies from your next billing cycle, not mid-cycle, so an already-started month keeps the old cap until renewal. Your Go dashboard shows the cycle date, and the allowance should step up after it. Docs being quiet on this is normal, worth a support ping if your renewal is close and it doesn't step.  
      
    Same models with no cap: direct DeepSeek API is the overflow lane nobody mentions. It's cache-aware per-token, no monthly ceiling beyond what you load on it, so mid-cycle walls like this one stop mattering. Keep a small balance there and the sub limit becomes a billing detail instead of a blocker.

---

## OpenCode 2 can now use my Android phone (free models, no account)
**u/3amae404** · 2026-10-14 10:03 UTC · ↑16 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5na7d/opencode_2_can_now_use_my_android_phone_free/)

I make Buddy, a free open-source Android app that runs a coding agent inside the app (a small Alpine Linux, no root, no PC) and gives it phone tools over MCP: read the screen, tap, type, scroll, open apps.

OpenCode was already one of the three agents in Buddy, next to Claude Code and Codex. Since 2.0 came out yesterday I moved Buddy to it. A few things I had to handle, in case it helps anyone wiring OpenCode 2 into their own tools:

• MCP tools now go through Code Mode by default (one "execute" tool that runs a script). For a phone agent that's worse, so Buddy sets codemode: false on its server. That only works in the new config layout (mcp.servers.<name>); the old layout is still accepted but ignores it.

• Without --standalone, run starts a background service that keeps running. On a phone you don't want that.

• The bash tool is now called "shell".

• Updating from 1.x keeps your connected providers: 2.0 imports the old auth.json on first start.

What it looks like: I ask "add a Nintendo Switch 2 to my Amazon cart" with the default free model (Big Pickle), and it opens Amazon, searches, scrolls and taps through it. Every "add to cart", "buy now", send, pay or delete tap needs my OK on a card, and Buddy enforces that itself. That mattered: the free model once went for "Buy now" instead of "Add to cart", and Buddy stopped it and asked me first.

Free models work with no account. Your own providers can be connected with opencode auth login in Buddy's terminal.

GitHub (Apache 2.0, APK in releases): https://github.com/ghorbelhamdi/buddy-android

Happy to answer questions about the setup.

**Comentarios:**

- **u/boss_yap** (↑2, 2026-10-14 12:46): Running a coding agent directly on Android with no root or PC is pretty wild. Love that you added confirmation for sensitive actions too. Definitely gonna keep an eye on this project!
  - **u/3amae404** (↑1, 2026-10-14 13:20): Thanks a lot! That was the idea: let the agent do the tapping, but keep you in charge of anything that matters. If you want to follow it, a star on GitHub really helps a small project get seen: https://github.com/ghorbelhamdi/buddy-android
- **u/Maleficent_Eye_5987** (↑1, 2026-10-14 13:30): I found a proper working AI copilot app that runs full coding harness on Android (control sother apps, write code, video editing, etc)
    It is free amd open-source. 
    https://samosa-ai.com/gotcha/
- **u/OptimizedGamingHQ** (↑1, 2026-10-14 21:47): Doesn't work for me
    
    https://reddit.com/link/pgs1140/video/rtqdgzk07ivh1/player

---

## Bad Request Error Gemini 4 Argon
**u/Jesusthegoat** · 2026-10-14 09:40 UTC · ↑1 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5mwze/bad_request_error_gemini_4_argon/)

Anyone else getting the Bad Request error when trying to use Gemini-4-Contributor? Any known fixes?

**Comentarios:**

- **u/Cyvster** (↑2, 2026-10-14 12:54): are you able to continue using that session or does it give bad request every time you try to use it?
    
    i usually get bad request errors when context is overflowed. you can use /compact to compact the session and save it when that happens.
  - **u/Jesusthegoat** (↑1, 2026-10-14 13:33): It was happening on first prompt. I fixed it now though. For anyone else reading this with the same issue it was due to the Gemini endpoint rejecting the tool call format of some of my installed skills (Primarily REA). I used deepseek v4.1 flash on max and it troubleshooted and fixed the issue in about 5 min.

---

## How to configure workflow correctly?
**u/Calm-Set6265** · 2026-10-14 09:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5mq5p/how_to_configure_workflow_correctly/)

---

## Comparing OpenCode Go vs OpenDesign Go (vs Command Code GOAT too for good measure, need some opinion or experience from others)
**u/misaalanshori** · 2026-10-14 09:28 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5mq0y/comparing_opencode_go_vs_opendesign_go_vs_command/)

---

## Anyone running custom subagents in OpenCode for non-web / C++ / embedded stacks?
**u/eh_see_l** · 2026-10-14 09:14 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5mixu/anyone_running_custom_subagents_in_opencode_for/)

Hi,

Been setting up custom subagents in OpenCode lately for stuff like reviewer and architect, but pretty much every setup or prompt guide I see online is built around standard web dev.

If you’re using CLI agents on low-level/embedded code, C/C++, or larger codebases, I’m curious how you’re configuring yours. A few things I’m trying to figure out:

* What custom subagents have you actually found useful? (e.g. read-only reviewers, toolchain runners for CMake/Clang-Tidy, test generators) And, which is the most efficient model for each agant?
* How do you handle builds/toolchains? Do you give agents direct access to run local make/flash scripts and parse compiler output, or keep that somehow separate?
* How do you handle context window between agents?
* Are you letting a main planner delegate to subagents automatically, or just manually calling the subagent?

---

## El sinsentido de la ia
**u/No-Peak8310** · 2026-10-14 08:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5m14l/el_sinsentido_de_la_ia/)

Puedo pagar y obtener 7 tok/s con GLM 5.3 Flash o usar un modelo gratuito Cat Jam Free y tener 255 tok/s

Que alguien me lo explique.

**Comentarios:**

- **u/Capital_Drawing5230** (↑1, 2026-10-14 09:00): Because catjam is retareded and glm is the best open source model according to anthropic
  - **u/No-Peak8310** (↑1, 2026-10-14 09:18): no me lo parece, llevo un rato y es bastante competente

---

## Somebody willing to reverse engineer minecraft?
**u/mortal_strike** · 2026-10-14 08:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5lvdx/somebody_willing_to_reverse_engineer_minecraft/)

**Comentarios:**

- **u/Affectionate_Fact854** (↑1, 2026-10-14 08:47): You must be one clever cookie right 
    
    Why reverse engineer it when you can easily just build a clone from scratch
  - **u/mortal_strike** (↑1, 2026-10-14 08:51): clone?
    - **u/25Violet** (↑1, 2026-10-14 09:26): Minecraft's code is deobfuscated. You can literally download the original code and just build it yourself

---

## Where else can I ...
**u/Yann27** · 2026-10-14 08:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5lr6u/where_else_can_i/)

Get "step 5 preview" for free? 

a bit tired of the: "Free usage exceeded, subscribe to Go"

**Comentarios:**

- **u/cornelha** (↑1, 2026-10-14 09:05): Wait, so are a little tired that the absolutely free stuff you get runs out? Crazy, $10 is not that much surely
  - **u/Yann27** (↑1, 2026-10-14 16:01): It runs out because it's limited. Nim is free, and I run GLM, Kimi and DeepSeek on max from morning till morning. I've got like 20 tabs open running  at the same time
      
      You think running a paid model on OpenCode is enough for that kind of workload? Sure, $10 isn't much, but I'd rather spend $50 on another provider that gives me around 90% discount on the same models I mentioned.
      
      I mainly wanted to test Step 5. I used Step 3 before and it was already amazing, so now I'm curious to see what I can get out of this version. Since it's still in the trial period, I don't want to pay for it yet.
    - **u/cornelha** (↑1, 2026-10-14 16:23): You mean, you want it do a crap load of work for free, not really testing
      - **u/Yann27** (↑1, 2026-10-14 16:32): oops. ( it's idd pretty good )
- **u/Popular-Task-8998** (↑1, 2026-10-14 09:10): Kilo code

---

## I built a quota sidebar for OpenCode V2 with remaining usage, reset timers, and credits
**u/SkanePrime** · 2026-10-14 07:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5lbfv/i_built_a_quota_sidebar_for_opencode_v2_with/)

Hiiiii! I wanted to see my remaining provider allowances without leaving OpenCode, so I built Quota Board. (previously i build [https://www.npmjs.com/package/opencode-usage-left](https://www.npmjs.com/package/opencode-usage-left) it is for opencode v1 though)

It adds:

\- Sidebar quota bars and credit balances

\- Collapsed summaries like 98% · 6d 8h

\- A /quota popup with provider details

\- Hide/pin controls with saved preferences



It uses your existing connected accounts. Adapters include OpenAI, Anthropic, OpenCode Console, OpenRouter, [Z.AI](http://Z.AI), Synthetic, and MiniMax.



This is the first release, tested with OpenCode 2.0.28. I’ve verified OpenAI quotas and Console credits live; I’d especially appreciate feedback from users of the other providers.



Code, installation, and demo:  

[https://github.com/gilvex/opencode-quota-board](https://github.com/gilvex/opencode-quota-board)

npm here [https://www.npmjs.com/package/opencode-quota-board](https://www.npmjs.com/package/opencode-quota-board)

What would make this more useful in your workflow?

https://preview.redd.it/5avqnsqd2evh1.png?width=1067&format=png&auto=webp&s=272d7abb4cb4a68944e42a88dfe805ca6135bf13

https://preview.redd.it/190ulhme2evh1.png?width=1667&format=png&auto=webp&s=3e363471486b54abbbc7637cd2c803620558710e

https://preview.redd.it/lv99qwlf2evh1.png?width=757&format=png&auto=webp&s=4b9546f181e94a4fca07164be1afcd7efbcc0667

**Comentarios:**

- **u/cornelha** (↑1, 2026-10-14 09:09): Does this update from the opencode website? I use opencode on multiple machines and it drives me nuts to have to check the site all the time

---

## Gemini 4 Argon is now in OpenCode Go 🔥
**u/afanasenka** · 2026-10-14 07:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5l5bm/gemini_4_argon_is_now_in_opencode_go/)

$60 usage til Nov 30

**Comentarios:**

- **u/andari3727** (↑2, 2026-10-14 07:53): oh my god
- **u/zenkov** (↑6, 2026-10-14 08:00): gemini-4-argon-contributor?
  - **u/mythormedicine** (↑2, 2026-10-14 08:02): That's what I see
  - **u/ivej** (↑2, 2026-10-14 08:07): 💀
  - **u/Ok_Necessary7506** (↑1, 2026-10-14 12:46): Still 440 estimated request... not usable.
    - **u/zenkov** (↑2, 2026-10-14 13:34): Hermes Agent had a similar issue, but with a 400 error. I had to ask the agent to fix the bug, which it did, and then I tested Argon a bit... Mixed feelings. It works pretty well, seemingly better than GPT-6.1-sol, but it burns through the subscription credits really fast.
        
        It might be useful for some people, but I still don't think the $10 OpenCode Go plan is suitable for frontier models. 😅
- **u/spiress** (↑8, 2026-10-14 08:05): lol, argon in opencode go but not in their pro subscription 
    
    it’s hilarious
  - **u/alphaQ314** (↑2, 2026-10-14 08:08): google is showing some generational levels of incompetence right now.
  - **u/gizeon4** (↑1, 2026-10-14 09:14): They have a lot of free Pro Subs
      Student and such, 
      Guess that's the reason
    - **u/spiress** (↑1, 2026-10-14 09:37): they already cut free pro subs from opus, so this is not that
    - **u/deepit6431** (↑3, 2026-10-14 11:37): Could give it out to paying Pro subs and not the free ones. Denying it to the paying ones is insane. Absolutely nobody is paying Google $200 for agy and Gemini so who even gets to use it?
- **u/aliencreature12** (↑1, 2026-10-14 08:18): 2 million token usage and quota gone also this is contributor must be much cheaper not 2x at 20x since they use your personal data
- **u/Aggressive-Cut-3828** (↑1, 2026-10-14 08:40): How does this stack up against o5.5?
  - **u/friday_h_bc** (↑2, 2026-10-14 12:20): very bad results
  - **u/jjonj** (↑3, 2026-10-14 13:33): I like this guys benchmarks    
      https://www.youtube.com/watch?v=mfsUVN8ykLA     
      but for more conventional AI dev takes I would wait for Theo to upload: https://www.youtube.com/@t3dotgg/videos
    - **u/pikuray** (↑1, 2026-10-14 13:36): Thanks
    - **u/Bananenklaus** (↑1, 2026-10-14 14:08): Bijan mentioned 🗣️🗣️🗣️
  - **u/rendez2k** (↑1, 2026-10-14 17:39): Good video that does some real testing. Ok, not the best it seems 
      
      https://youtu.be/JocjKnl4lBs?is=32rNOXGAJnhSI83c
- **u/eachDayIWakeUp** (↑1, 2026-10-14 08:49): Anyone can share their first impressions?
- **u/Strict-Prune-879** (↑1, 2026-10-14 08:58): contributeur= pas de zdr?
- **u/gocchisama** (↑3, 2026-10-14 09:17): I personally cannot use it yet. It says bad request
- **u/Jesusthegoat** (↑2, 2026-10-14 09:38): Can't use, getting Bad Request error
- **u/DominikPlays** (↑1, 2026-10-14 10:48): It has statistical watermarks unusable for coding
  - **u/rainerdefender** (↑1, 2026-10-14 11:08): Errors out anyways...
    - **u/DominikPlays** (↑1, 2026-10-14 12:13): As expected
  - **u/NoMatterWhaa** (↑1, 2026-10-14 11:39): That means ?
    - **u/Thomas-Lore** (↑2, 2026-10-14 13:16): Just watermarks, all models have them and Gemini was probably the first to use them (Synth ID for text). They have barely any effect on coding. And who cares if they are there? Everything is made by AI now anyway.
- **u/tresslessone** (↑1, 2026-10-14 12:30): ... Raw or quantised?
- **u/Sea_Ear5201** (↑2, 2026-10-14 13:07): It is available in my pro plan. But haven't tried it yet
- **u/Kylmawurr** (↑2, 2026-10-14 13:08): Pass. 20x too expensive for contributor use. Divide by 20 and ill think about it.
- **u/evanvelzen** (↑1, 2026-10-14 13:30): I have used this the last 2 days and this will be my daily driver. 
    
    I am sometimes dissapointed by DeepSeek v4.1 Flash and Muse Spark 1.3. Gemini Flash 3.8 was always a better coder but at its price point you were better off using Claude Opus or Sonnet.
- **u/MeOneThanks** (↑7, 2026-10-14 17:42): I gave it a simple task: redesign a static web page (just a one-pager, nothing crazy)  
    It ended up reading 105 files and then ran out of my rolling 5h quota. not a single word from the model.
  - **u/RedditAtWork23** (↑1, 2026-10-14 18:22): Congratulations you have made google and the nsa proud today

---

## Could someone share a Claude invite with me?
**u/MeaningAnnual3542** · 2026-10-14 07:09 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5kmzs/could_someone_share_a_claude_invite_with_me/)

Hey everyone! Hope you’re all doing well.

I’ve been interested in trying out Claude for some time, and I’ve seen that some people have access to invite links. If anyone has a spare invite, would you mind sending me one via private message? I’d really appreciate it!

**Comentarios:**

- **u/superdooper1986** (↑1, 2026-10-14 10:51): Sent PM
  - **u/Interesting-Movie452** (↑1, 2026-10-14 10:57): can you send me too
- **u/slavmaf** (↑1, 2026-10-14 11:31): This is the first time I hear a out this, what does that invite link get you, that you already do not have on a free Claude tier?

---

## i’m making a simple rts game for opencode and other ai harnesses to play
**u/emersoftware** · 2026-10-14 05:30 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5j1mk/im_making_a_simple_rts_game_for_opencode_and/)

[removed]

---

## GPT live feature but on opencode Go?
**u/gocchisama** · 2026-10-14 04:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5i45r/gpt_live_feature_but_on_opencode_go/)

Hello,

I am satisfied with Opencode Go for my current project so I plan to stay with it, however I like the idea to converse with my agents on opencode GUI and TUI to make some work on Hermes while Im  sleeping, and would like to know if there's a plugin to replicate GPT Live but on opencode.

Many thanks

---

## Switched to v2, Main Session Can't Edit Files Anymore
**u/ScotchSpeed** · 2026-10-14 04:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5i42t/switched_to_v2_main_session_cant_edit_files/)

Tell me I'm attempting to fix this incorrectly. I spent 40 hours creating a project from a single session in v1. All my planning history, decisions, everything is in there. Yes, I have .md files which contain a lot of the important stuff but not everything.

After the switch to v2 I'm told none of my agents can edit files from the session because the session is owned by an agent without edit access. Without the ability to spin up sub-agents with edit access. NOTHING I do will let me around this. The LLM even told me it refused to attempt to help me manually edit files which might give me edit access from this session because it knows it's supposed to be read only. What is that!!!

I have long plans in my conversation for the next step but I can't have the LLM write them and have a new session for a coder to build them out because the LLM isn't allowed to write them.

This CAN'T be the way v2 wants us to work. What am I missing?

**Comentarios:**

- **u/KARMA_P0LICE** (↑1, 2026-10-14 04:44): ...what are you talking about?  Why are you working for 40 hours in a single session?
    
    Sessions are expendable throwaway things. Work on your actual codebase, not on a session

---

## Gemini 4 Argon High vs. SWE-2 (literately Kimi-K3) - On regression hunts, spec gaps, downstream failure.  Blasting out reviews of 14 independent reviewers representing  2 teams of 7 each.
**u/ZealousidealTown1974** · 2026-10-14 03:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5h4wc/gemini_4_argon_high_vs_swe2_literately_kimik3_on/)

---

## "Big Pickle" worked great for 36 hours now is back to unusable
**u/Robert__Sinclair** · 2026-10-14 00:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5cyn5/big_pickle_worked_great_for_36_hours_now_is_back/)

For the last 24-36 hours Big Pickle was **incredible**! Smart, fast. It was like dancing.

Now is back to how it was 2 days ago: crawls, stops for minutes before even the "thinking".

And it's quite dumb.

Whatever you guys did, go back to yesterday! It was perfect!

**Comentarios:**

- **u/bluesockdrawer** (↑2, 2026-10-14 00:13): The worst part is knowing how good it can be. Once you’ve experienced that version, it’s hard to go back.
  - **u/Robert__Sinclair** (↑1, 2026-10-14 01:31): I completely agree. I did the work of a week in 3 hours. And it was flawless. 240M tokens total in 1 day!
- **u/LinsaFTW** (↑3, 2026-10-14 00:46): I think Big Pickle is a rotating stealth mode. It's not a specific model but rather it rotates with different type of models. Might be routing to a very bad one lol.
  - **u/Robert__Sinclair** (↑0, 2026-10-14 01:33): It usually is, but if I interrogate it directly with no prompts (outside opencode) I usually get the real model name. One time it said (last week) it was Space Bunny. But today and yesterday the answer is the same: Claude.  Perhaps in the last 24 hours it was some big anthropic model (even if from the speed I wouldn't think that). Today is clearly a dumber model but still answering he is Claude.
    - **u/KARMA_P0LICE** (↑3, 2026-10-14 03:38): Models don't know their names. It's a stochastic text prediction tool, it's not going to answer right.
      - **u/Robert__Sinclair** (↑1, 2026-10-14 18:13): they know their name. they don't know their particolar version.
        - **u/KARMA_P0LICE** (↑1, 2026-10-14 18:47): They do not necessarily know their name. There's nothing in the learning for a model that teaches it its own name.
            
            Models that know that are only getting it from their system prompt or post-training. A cloaked model won't likely have this post training so it's response will be unreliable
- **u/Meandernder** (↑1, 2026-10-14 01:20): Maybe it got bored
  - **u/Robert__Sinclair** (↑2, 2026-10-14 01:30): Your code is that bad? :P
    - **u/Meandernder** (↑1, 2026-10-14 09:07): Huh who is the op if this post? Excuse me i must be mistaken.
- **u/the_man_inTheShack** (↑1, 2026-10-14 08:10): I've been using big pickle for a few months now and overall it has been pretty good - especially since around the end of August when there was a big improvement. But never fast, and for the last couple of weeks been suffering from sleeping sickness more and more. Then yesterday I started using qwen3.8 locally, I wont be going back. Fast and every bit as good as big pickle has been at its best so far. I do have a good rig tho' 32G vram and running qwen3,8 27b 6bit quant with k & v set to int8 and a 128k context.
- **u/justmaybe888** (↑1, 2026-10-14 08:47): I wish providers were more transparent about there changes. Even a small update explaining what happens would save everyone so much guessing.
- **u/[deleted]** (↑1, 2026-10-14 12:02): [removed]

---

## Opencode is pretty good now I created an F1 game in 2 hours
**u/automax** · 2026-10-13 22:13 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5adep/opencode_is_pretty_good_now_i_created_an_f1_game/)

Just the standard bigpickle  
[https://www.melbournecrime.site/car/car.html](https://www.melbournecrime.site/car/car.html)

The game itself took only 30minutes but just adding more features like:  
sound, scoreboard, obstacles, smoothness, penalty, start, finish, overtaking, crashes, position  
  
The track is based on US grand prix thats coming up.

**Comentarios:**

- **u/YoRt3m** (↑2, 2026-10-13 22:17): That's cute
  - **u/automax** (↑2, 2026-10-13 22:20): heheh thanks, going to see how difficult it will be to upload to android.  
      Like a retro f1 game for free
- **u/ShallotDolos** (↑2, 2026-10-13 23:17): This is awesome. Best of luck.
- **u/honglac3579** (↑2, 2026-10-13 23:42): Which model do you use btw?
  - **u/Takeoded** (↑3, 2026-10-14 00:02): Refer to picture: [https://i.imgur.com/t8OGcis.png](https://i.imgur.com/t8OGcis.png)
    - **u/honglac3579** (↑1, 2026-10-14 00:05): I thought it was mistaken. When big pickle suddenly this good anyway
- **u/biograf_** (↑3, 2026-10-13 23:49): I pointed a fan at my face while playing this and it was intense!
- **u/Sweet-Chip6849** (↑1, 2026-10-13 23:54): excelente es entretenido :)
- **u/Robert__Sinclair** (↑1, 2026-10-14 00:11): It (Big Pickle) has been great for the past 24 hours. **NOW** is back to the dumb slow model it was before.
    
    It take even a minute to start displaying "thinking".
  - **u/automax** (↑1, 2026-10-14 01:18): Few tips to make it faster,  don't use a folder with too many files or MD.  
      After a certain amount of context, restart the opencode and put a new prompt in there.
- **u/MMOfreak94** (↑1, 2026-10-14 00:17): bro this is not winnable lol
  - **u/automax** (↑1, 2026-10-14 01:06): Its winnable, I came 1st, you have to take off the keys off accelerator on turns and get to the front asap.
    - **u/automax** (↑1, 2026-10-14 01:41): actually i can only manage 2nd now, its difficult, maybe i should change the difficulty
      - **u/MMOfreak94** (↑1, 2026-10-14 02:00): didn't lift my finger up from w and i got 4th place. either this isn't winnable or i need to go back to driving school
        - **u/automax** (↑1, 2026-10-14 02:38): its definitely possible, but its difficult, just finished 1st.  
            [https://files.catbox.moe/16yzwf.png](https://files.catbox.moe/16yzwf.png)
- **u/FewExplanation5433** (↑1, 2026-10-14 00:56): big pickle was deepseek
  - **u/BigPlebeian** (↑2, 2026-10-14 04:34): No
- **u/migsperez** (↑1, 2026-10-14 01:45): Gosh it doesn't like to crash
- **u/for4f** (↑1, 2026-10-14 03:28): lmao the cota track right before the us gp is perfect timing. 30 min to a playable game with penalties and overtaking, big pickle is putting in work lately

---

## wdy think about opencode 2 ?
**u/According_Quiet_4899** · 2026-10-13 21:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x59ugy/wdy_think_about_opencode_2/)

---

## CatJam model signed a commit with this. Any info about the company behind this model?
**u/0xbyt3** · 2026-10-13 20:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x58ezq/catjam_model_signed_a_commit_with_this_any_info/)

https://preview.redd.it/a6if70b8ravh1.png?width=573&format=png&auto=webp&s=8fd8bfa8911fbf0eec0cf03604c3193355772f5f

**Comentarios:**

- **u/YoRt3m** (↑1, 2026-10-14 10:36): Maybe it's a joke since it's a cat
    
    As far as I understand people claim it's Beam model by Reflction AI

---

## The horsy prompt with Gemini Argon 4 - Running on OpenCode TUI V2 - via Antigravity harness (ACP lane)
**u/ZealousidealTown1974** · 2026-10-13 20:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x57x1z/the_horsy_prompt_with_gemini_argon_4_running_on/)

From a bro requested it .... And well.. it is fast but bad!

**Comentarios:**

- **u/A_Far_Hitman** (↑1, 2026-10-13 21:25): Could you try with luna, haiku and gemini 3.8
- **u/migsperez** (↑2, 2026-10-14 01:40): Yeah not Opus level, considering the cost of Argon. It's not the worst cloud model output I've seen. Seems like it didn't put a huge amount of effort in. 
    
    Somebody else did an Argon creation here too: 
    https://www.reddit.com/r/opencode/s/c89VdLDmje

---

## Argon 4 on OpenCode  is awesome  - Gemini, the king has returned and it outsmarts OpenAI GPT 6.1 Sol on high
**u/ZealousidealTown1974** · 2026-10-13 19:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x56pbb/argon_4_on_opencode_is_awesome_gemini_the_king/)

**Comentarios:**

- **u/tuhdo** (↑1, 2026-10-13 19:52): Really. I'm curious, could you do this benchmark for a comparison: [https://www.reddit.com/r/codex/s/qJuIspn9Sj](https://www.reddit.com/r/codex/s/qJuIspn9Sj)
  - **u/ZealousidealTown1974** (↑1, 2026-10-13 19:56): well, Im building the plugin to get Antigravity google subscription works on OpenCode - so it is dogfooding itself - it is smart but somehow tool using kind  of suck
    - **u/Shawnanigans** (↑1, 2026-10-14 00:36): So it's the Gemini one working?
  - **u/ZealousidealTown1974** (↑1, 2026-10-13 20:33): yes I did unfortunately it sucks [https://www.reddit.com/r/opencode/s/B5mJhDOcnr](https://www.reddit.com/r/opencode/s/B5mJhDOcnr)

---

## New to this — OpenCode vs Hermes vs DeepSeek Harness, which should I actually use?
**u/rxafaonfent** · 2026-10-13 19:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x566kt/new_to_this_opencode_vs_hermes_vs_deepseek/)

**Comentarios:**

- **u/Ctbhatia** (↑1, 2026-10-13 23:38): pick one client and stay on it, the token count is mostly the context you resend each turn, not the harness.
- **u/crasspuk** (↑1, 2026-10-14 09:58): Pick one and stick with it for a while, since the model and your session length matter more than the harness. Most tokens go to resending the whole context on every turn, so long sessions cost more in any client.

---

## A donde vamos con la IA?
**u/cristiand21121** · 2026-10-13 19:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x565jb/a_donde_vamos_con_la_ia/)

Viendo todo esto del emulador de ps5, “si comprar no es poseer, piratear no es robar”, la decompilacion de aplicaciones, etc.

A donde creen ustedes que va parar todo esto?

Al inicio parecía que las grandes corporaciones eran las ganadoras con la IA, ahora parece que todo va cambiar.

**Comentarios:**

- **u/ANDALTUV** (↑2, 2026-10-13 19:33): no where, AI is not even half way where the companies say they are.. Thats the truth whether people like or not. AI is good with repetitive jobs but when you ask it to do something that might get out of its training dataset its true colors begin to show, taking shortcuts, getting lazy, and hallucinating things... So yeah, AI is not what the AI bros are selling and much less what the providers are saying.
  - **u/LinsaFTW** (↑1, 2026-10-13 19:47): "Not even half way"
      
      Mind if I ask how much?
      
      How much time it has been since the last major AI release?
      
      In 6 months, doing 10% of what these companies did is massive. 
      
      What about in 6 more months?
      
      What about in 1 year?
      
      You have to consider the history behind. This is no joke.
      
      "It cant count to 4" -> "It cant make code" -> "It can make games" -> "It can't make half of what these companies do" -> ... Whats next? In the end, AI was capable to break all the "It can'ts" over time.
      
      And its simple math.
      
      As long as the matrix is trained to do something, it can do it. There is no limits to AI other than how smart you train it and what data you use to train it.
    - **u/ANDALTUV** (↑1, 2026-10-13 20:59): The problem is that the AI already consumed all data from internet, there is no more data to be trained. So what is basically doing is training it self with the data is generating.. Now how far we are? not sure. These companies are selling hype the same as the AI bros.. And the biggest flaw of all is that the AI has no capacity to imagine things, all it does is search for patterns.
      - **u/LinsaFTW** (↑1, 2026-10-14 00:42): You are wrong. 
          
          It's not about "what" data.
          
          It's about "how" that data is fed.
          
          When you feed the same data in different ways, it can be less or more useful.
          
          That's recursive self learning. Its distilling and processing data to be better digested for the model.
          
          I am a machine learning engineer, the news don't exaggerate, there is no limit to AI, the only limit is how and what you train it for. The rest is just pure mathematics.
          
          If you believe AI is doom and end of humanity, you are done for and are cursed to live a depressing life in the following 60 years.
          
          I am the ones who embrace it and enjoy using it and building new things, I am excited for the future to come :)
  - **u/seventyfivepupmstr** (↑1, 2026-10-13 22:30): You really don't know anything about Ai except what the news says, do you?
    - **u/LinsaFTW** (↑1, 2026-10-14 00:38): I am a machine learning engineer. I don't make language models but I do make models for multiple other things.
        
        Check DeepSeek papers (too many papers youtube channel summarizes it very well) you will be mindblown, there is NO LIMIT WHATSOEVER to AI.
        
        The only limit is data and training. And I don't mean just "feed anything" but how you feed it.
      - **u/seventyfivepupmstr** (↑1, 2026-10-14 00:45): Well it's too bad that you didn't branch your study beyond machine learning because you clearly don't understand how LLM work. The same as base machine learning, LLM are just math functions. You are right that training LLM isn't increasing very fast anymore. But that doesn't matter because the models are far less important than the harness that runs agents. If you were to actually try to research and understand what you are claiming then you would understand that the current harness are pretty bad, and once the mindset changes to use effective harnesses, then AI will have massive adoption.  A correct harness fixes the majority of problems that AI is experiencing like slop creations and dangerous actions
        - **u/LinsaFTW** (↑1, 2026-10-14 00:51): No, that's partially correct, and I do work on harnesses and prompt engineering but don't train models myself.
            
            Harnesses and tools means a lot, that's why I am coding my own. 
            
            But still, you are ignoring the fact that training defines how efficient and scalable the model is, how it makes the tool calls and interacts with the content it sees, how it solves uncertainty. 
            
            I would say, the harness is a 75% for trivial tasks, but for advanced coding, its way less.
            
            But rather than saying "this is what matters the most" I would instead say:
            
            Harness is the capability of how it can interact with things and allowing easy / predictable data to be easily retrievable.
            
            The model is the capability to solve uncertainty and execute those harness tools. 
            
            A simple example: Try using 2 years old GPT on a current harness, it will be HORRIBLE and I think it doesn't even have the capability to run tool calls.
            
            Whatever harness you use, the model is still most of the heavy work, because it defines how tools are used.
          - **u/LinsaFTW** (↑1, 2026-10-14 00:52): Also, if the model didnt matter, then people would be using DeepSeek for everything, which I do use a lot, but not for everything because it cannot solve certain tasks.
          - **u/seventyfivepupmstr** (↑1, 2026-10-14 00:57): I can use 2 year old gpt with my harness if you know of an api service that has it.  I consistently use the cheapest models on opencode go including the free models and I get great results because my harness enforces best practices for software development. When you force the LLM essentially to do a very specific task, and don't put garbage in the context, it produces extremely consistent results regardless of which model it is using. If you want proof just try my harness and see for yourself: https://vis-agentic-website-production.up.railway.app/
            - **u/LinsaFTW** (↑1, 2026-10-14 02:22): But that proves my point.
                
                You dont need more data, you need to train it better.
                
                That's cheap models in a nutshell, distillation and deep learning using the same data but trained better.
                
                It doesn't mean training doesn't matter, that's extreme to say.
                
                It means current models are just better, but could be even better.
                
                The biggest difference between small and big models is that small models might deviate or require more thinking because they still get stuck sometimes. And can't solve uncertainty, even with the correct context, specially if its A LOT of it. 
                
                Luna is a great demonstration of a model that can solve tasks autonomously like a big model, 90% of times.
                
                But then models with more parameters show their quirks on design and domain specific tasks.
- **u/LinsaFTW** (↑1, 2026-10-13 19:44): Conforme mas proyectos nazcan y en especial avancen, la IA va a marcar terreno para que las empresas empiecen a enfocarse en las features que nosotros los consumidores pedimos. Lo lindo es que lo que antes era avanzado o solo para unos pocos, va a ser lo basico para poder operar. Una aplicacion como por ejemplo photoshop, o un videojuego, no tiene por que estar detras de una consola, o un launcher, y no tiene por que ir a 10FPS por mala programacion. La IA ayuda a materializar proyectos o ideas que antes eran imposibles no por ser imposibles sino por que costaba mucho tiempo y dinero que no era necesario perder. Estamos en una epoca maravillosa donde podemos crear en minutos lo que querramos, y hay que aprovechar para realizar nuestros sueños. Bueno, en realidad, si analizas la historia, siempre fue buen momento, si miramos atras.
- **u/migsperez** (↑1, 2026-10-13 19:53): My direction with AI/SI has been making a lot of animated low poly horses and dragons recently :)
  - **u/infra-larp-3001** (↑1, 2026-10-14 07:23): now print them, give them cheap tv box clusters as mind and have the dragons replicate using their dragon breath to 3d print /s

---

## Skills ?
**u/Warm-Agent-811** · 2026-10-13 18:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x55feb/skills/)

I used to run OpenCode with just a few skills and it worked fine. Then I started adding more, including some skill packs from GitHub, and now my agent spends forever thinking, checking every skill, running tests for hours on simple tasks. It's burning tokens for no reason.

I'm looking for a generic, minimal skill setup: maybe one for frontend, one for backend organization, one for testing, just the essentials. I want to avoid having three skills that do the same thing slightly differently.

Anyone have a recommended configuration or skill set that just works without the bloat? Thanks

**Comentarios:**

- **u/Worried_Matter4443** (↑1, 2026-10-13 19:01): im on the same boat. burns through tokens.
  - **u/Warm-Agent-811** (↑1, 2026-10-13 19:08): I'm glad I'm not alone in this situation haha
- **u/ngg990** (↑1, 2026-10-13 19:39): Use skills at project scope. I had the same that you because I had all my skills and agents at global level, I extracted them by topic and install them as plugin for the projects it actually needs them. For example for development I have a set of agents, skills and tools, but this is only useful while development, but for other stuff makes no sense to load them, for example content generation. Here is my harness if you want to check it out https://github.com/andrescevp/development-harness
  - **u/Warm-Agent-811** (↑1, 2026-10-13 20:41): Great, I was thinking about sth like this. I'm gonna try it. Thanks !!
- **u/crasspuk** (↑1, 2026-10-14 08:32): Worth checking where those packs actually landed. Besides .opencode/skills and ~/.config/opencode/skills, OpenCode also picks up skills from .claude/skills, ~/.claude/skills and ~/.agents/skills, so stuff installed for other tools gets listed too. Every listed skill's name and description goes into the skill tool's description, so the agent sees all of them on every task.
    
    You can hide the ones you don't want without deleting them, in opencode.json:
    
        "permission": { "skill": { "*": "deny", "frontend-*": "allow", "testing": "allow" } }
    
    Denied skills are hidden from the agent entirely. You can also set the same block per agent, so e.g. only your build agent sees the testing skill.

---

## Skills in opencode
**u/[deleted]** · 2026-10-13 18:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x55ebv/skills_in_opencode/)

[deleted]

---

## Gemini 4 Argon now available in OpenCode 🔥
**u/afanasenka** · 2026-10-13 18:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x54z4i/gemini_4_argon_now_available_in_opencode/)

**Comentarios:**

- **u/AlternativePear4617** (↑0, 2026-10-13 19:08): mirá vos che
- **u/MetalDeep329** (↑15, 2026-10-13 19:25): And people who pay $20 a month for the Google ai pro plan can't use it for coding, what a shame
  - **u/The_Wonderful_Pie** (↑1, 2026-10-13 23:31): Huh ? I'm on Google AI pro student (1 year free), and I even have the max reasoning mode of Argon on the Gemini website. I don't have antigravity, but that would seem weird I can have it to chat but not coding, are you sure it's unavailable for coding?
    - **u/xmsxms** (↑1, 2026-10-14 01:29): Did you try? The website chat is a very different offering to API access for agents. Most providers give you free/cheap access to chat in their web interface as it's very limited compared to API access.
- **u/migsperez** (↑5, 2026-10-13 19:54): I've made a lot of benchmark based animated three.js horses recently. Can someone give it a go on Argon. :)
  - **u/Melodic-Leather-5170** (↑1, 2026-10-13 21:20): maybe, does it take too long? is it one shot?
    - **u/migsperez** (↑1, 2026-10-14 01:20): It's one shot. Time depends how good a model is. Opus completes it in about 5 mins. Much less intelligent complete quickly like 9b models, they don't put much effort in. GLM 5.3 took an hour.
    - **u/migsperez** (↑2, 2026-10-14 01:30): https://www.reddit.com/r/opencode/s/c89VdLDmje. A user already did it.
- **u/Amarsir** (↑3, 2026-10-13 21:37): Looks like they mean Zen btw, not Go. Costing $2/10 until the end of November.
- **u/Itchy_Virus5387** (↑1, 2026-10-13 23:12): how to use it?

---

## Paypal Ai hackthon with awesome price, please find the details in this video
**u/Traditional_Diver_70** · 2026-10-13 18:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x54yl4/paypal_ai_hackthon_with_awesome_price_please_find/)

https://youtu.be/kUrK36DlHyo?si=p1Lm9fWHzaWy\_xOF

---

## Antigravity models in v2? (Google ai pro sub)
**u/NEMOalien** · 2026-10-13 18:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x54kdg/antigravity_models_in_v2_google_ai_pro_sub/)

I have a google ai pro subscription active and i used to use a plugin (forgot the exact name) that let's me use google OAuth and grants me access to better limits, quotas and models from my google account, i just updated to v2 but I can't seem to find a working plugin that does the same thing..

**Comentarios:**

- **u/zRafox** (↑1, 2026-10-13 18:35): You actually avoided a wave of bans
  - **u/NEMOalien** (↑2, 2026-10-13 18:36): Huh? What happened? 😭
    - **u/zRafox** (↑1, 2026-10-13 18:41): I remember a few months ago there was a wave of people banned by Google for using Antigravity's OAuth in external agents like Opencode, among others.
      - **u/NEMOalien** (↑1, 2026-10-13 18:42): Holy shi, it's against the ToS or smth?
- **u/CharacterBorn6421** (↑1, 2026-10-13 19:01): what is the plugin name for v1 ?
  - **u/NEMOalien** (↑1, 2026-10-13 19:03): opencode-antigravity-auth or opencode-antigravity-multi-auth
      Although as another commenter pointed out turns out this violates the ToS...
- **u/marektracz_** (↑1, 2026-10-13 19:06): I think it’s against Google ToS and you shouldn’t do it
- **u/ZealousidealTown1974** (↑2, 2026-10-13 20:41): I am creating one properly in the next 2-3 day times - through ACP with 2 Harness supported (Devin and Antigravity ) - Can use it as front-facing agent or delegates - this is built with allowed policies (because it is still running under Antigravity harness  - only transform to OpenCode sessions - so safer uses, guarantee
  - **u/NEMOalien** (↑1, 2026-10-13 20:43): That's really cool, could you please let me know once it's out?
    - **u/ZealousidealTown1974** (↑2, 2026-10-13 20:46): sure bro mark it!
- **u/gaz_0001** (↑1, 2026-10-13 22:58): Did you try T3 Code
    
    It natively support Antigravity.
    It even supports OpenCode v2
    
    I am currently running Pi, Codex, Opencode v2 over T3 Code.
    
    Works perfectly.
    Its kinda like Paseo....
    Paseo supports native antigravity too.
    
    Not sure whether I prefer T3 Code or Paseo
- **u/WeekendCereal** (↑1, 2026-10-14 08:33): I’d check the community Discord or GitHub discussions first. Someone else on Google AI Pro has probably run into the same issue after updating.

---

## New Cat model has Crazy speed. 300+ tokens per second
**u/RespectJaded15** · 2026-10-13 18:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x545vz/new_cat_model_has_crazy_speed_300_tokens_per/)

I was testing the model for summarizing papers.(i know not that difficult)

  
the model give 370 tokens per sec.

https://preview.redd.it/j4b8i5fhz9vh1.png?width=648&format=png&auto=webp&s=4e5017c28290da094a205ac8d3e963d3dc4d52dc

**Comentarios:**

- **u/eachDayIWakeUp** (↑1, 2026-10-13 18:22): Speed is indeed insane, but for even easy tasks I ran today the output was horrible. It straight up refused to retry to produce better results. How was your produced summary?
  - **u/RespectJaded15** (↑1, 2026-10-13 18:27): i would say good. i was summarizing "BehaviorScope-X: reusing pose-trained visual representations for full-video ethology". i asked it to be indepth. also used the max options.
    - **u/eachDayIWakeUp** (↑1, 2026-10-13 18:28): I was on the max option as well which leads to question what this model will produce on lower efforts
- **u/AnyAsparagus2539** (↑1, 2026-10-14 11:08): The speed is wild.how does the quality hold up on longer summaries?
  - **u/RespectJaded15** (↑2, 2026-10-14 12:45): Quality was good so for small tasks it is good especially for its speed
    - **u/AnyAsparagus2539** (↑1, 2026-10-14 13:44): ohhh nice! have you tried it on anything more complexyet?
      - **u/RespectJaded15** (↑1, 2026-10-14 19:11): Yeah but I don’t see the coding capability that good. I think it will be a good general model.
- **u/One-Abroad1973** (↑1, 2026-10-14 12:41): 370 tok/s is wild, curious  how good the actual summary.

---

## Possibly a redundant question
**u/Powerbombed** · 2026-10-13 17:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x53twb/possibly_a_redundant_question/)

I have 14 days left in my opencode go subscription.  But my usage is gone.  
If I add $10 credit then will I still get the cheapseek bonus and other extra like $60 usage for Qwenflash, etc?

I find the tier, and modifiers very confusing so I might be asking something that maybe answered a few times. Apologies. I just need a concrete answer.

**Comentarios:**

- **u/LoquatNo3841** (↑1, 2026-10-13 18:09): No, 10$ is priced w/ published Zen prices, no 80$ allowance
  - **u/Powerbombed** (↑1, 2026-10-13 18:39): Thank you for the response
- **u/Amarsir** (↑1, 2026-10-14 02:37): A second account would be your best use of $10. Swap the key and then swap back at the start of next month.
  - **u/Powerbombed** (↑2, 2026-10-14 03:24): Thanks. I’ll think I’ll do that

---

## What skills and models do you use for code vulnerability check against your repo?
**u/theepi_pillodu** · 2026-10-13 17:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x52s9g/what_skills_and_models_do_you_use_for_code/)

I use opencode, have ponytail and some PR review skills added. Java, c++ and CSharp LSPs and a bunch of MCPs for my day to day use. 

I want to use some credits to do a code vulnerability check against each of my repos. (Enterprise)

Find the missing catch/exception handling etc. 

Also, please help me with the best way to find issues with my code without using unnecessary tokens. 

Thank You.

**Comentarios:**

- **u/eachDayIWakeUp** (↑1, 2026-10-13 18:08): Curious to know as well.
- **u/Cyvster** (↑1, 2026-10-13 18:10): what? just send it
- **u/CheesecakeLivid9791** (↑1, 2026-10-13 18:14): Code review
- **u/pungat_** (↑1, 2026-10-13 22:33): use this 👉 [https://github.com/mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- **u/levu304** (↑2, 2026-10-14 06:58): enable github dependabot alert if using github
  - **u/eachDayIWakeUp** (↑1, 2026-10-14 08:48): I prefer renovate. It can run on selfhosted runners and is compatible with all git platforms
- **u/crasspuk** (↑1, 2026-10-14 10:51): For dependency CVEs, a scanner beats any model. Dependabot alerts cover that on GitHub repos, and Renovate supports most git hosts. Models are better for the missing error handling that scanners skip, so run them file by file on the risky modules instead of the whole repo.
- **u/ngg990** (↑1, 2026-10-14 18:48): Semgrep (ts/js) + ovs scanner , for python there a library called bandit, I believe each language may have them self bandit.

---

## Cat Jam (stealth) is now FREE in OpenCode 🔥
**u/afanasenka** · 2026-10-13 17:20 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x52r9c/cat_jam_stealth_is_now_free_in_opencode/)

**Comentarios:**

- **u/No_Advance3911** (↑11, 2026-10-13 17:33): Upstream request failed: Endpoint is unavailable.
  - **u/Tasty_Owl_7930** (↑1, 2026-10-13 23:04): you can change the endpoint from ur `opencode.json` into this
      
      ```
      {
        "provider": {
          "opencode": {
            "options": { "baseURL": "https://opencode.ai/zen/v1" }
          }
        }
      }
      ```
    - **u/Tasty_Owl_7930** (↑1, 2026-10-13 23:05): source: [https://github.com/anomalyco/opencode/issues/54833#issuecomment-6127009970)](https://github.com/anomalyco/opencode/issues/54833#issuecomment-6127009970))
        
        by the official opencode creator (anomalyco)
- **u/0xbyt3** (↑2, 2026-10-13 17:59): it is really fast. 200 token/s and is intelligent enough. New Deepseek? token count is also way low than other models.
  - **u/NMiguelCosta-PT** (↑3, 2026-10-13 18:05): It's not better than V4.1 and is also faster so it can't be V4.1 Pro and I don't think they would release a new Flash version without releasing V.4.1 Pro, would they?
    - **u/0xbyt3** (↑2, 2026-10-13 18:11): Might be a new update for the Deepseek's speculative decoding. That would explain the low intelligence compared to V4.1. We have seen similar jump in speed few months ago.
      - **u/kankerstokjes** (↑1, 2026-10-13 18:14): I'm thinking Mimo or Hy or another Chinese lab.
        - **u/techmago** (↑1, 2026-10-13 18:41): Mimo just released one, Too soon for another?
          - **u/Aldarund** (↑2, 2026-10-13 19:51): But tokenize matches mimo exactly. Snd dobt match temcent or deepseek or qwen
        - **u/look** (↑0, 2026-10-13 21:02): It is not Chinese. Or if it is, the Chinese government has very recently adopted a \_much\_ more liberal policy on “sensitive topics”.
          - **u/kankerstokjes** (↑1, 2026-10-14 06:43): I see. Then I stand corrected!
    - **u/thedthatsme** (↑1, 2026-10-14 03:23): Better how?
  - **u/RespectJaded15** (↑5, 2026-10-13 18:15): i am getting near 400 tokens/sec
  - **u/Aldarund** (↑2, 2026-10-13 18:28): Its mimo
    - **u/Osvik** (↑1, 2026-10-13 19:38): If it were Mimo it's much worse than mimo-v2.6-flash (in my experience)
      - **u/Aldarund** (↑1, 2026-10-13 19:50): And much faster. Its at minimum exactly same tokenizer as mimo
  - **u/qwertyyyyyyy116** (↑1, 2026-10-13 21:39): okay so its either gemini, or maybe groq or cerebras, but those are inference providers, not models, so PROBABLY gemini
- **u/dawsonKKO** (↑2, 2026-10-13 18:40): Hear me out, it’s a Gemini model
  - **u/RetroTGT** (↑11, 2026-10-13 18:52): What are you smoking?
    - **u/zer0evolution** (↑1, 2026-10-14 01:11): maybe sawit
      - **u/Least_Bodybuilder216** (↑2, 2026-10-14 02:33): INDONESIAN MENTIONED RAHHHH🦅🦅🦅🦅🦅🦅🦅🦅🦅🦅
      - **u/yogafirepromax** (↑1, 2026-10-14 07:38): r/AdaIndonesiaCoy
        - **u/sneakpeekbot** (↑1, 2026-10-14 07:38): Here's a sneak peek of /r/AdaIndonesiaCoy using the [top posts](https://np.reddit.com/r/AdaIndonesiaCoy/top/?sort=top&t=year) of the year!
            
            \#1: [Tak berkonteks](https://i.redd.it/q5cup7kl2foh1.jpeg) | [73 comments](https://np.reddit.com/r/AdaIndonesiaCoy/comments/1wbf8n7/tak_berkonteks/)  
            \#2: [Wah .. kena roasting sama yg dari luar negeri....](https://i.redd.it/t607ysktw5sh1.jpeg) | [54 comments](https://np.reddit.com/r/AdaIndonesiaCoy/comments/1ws18dd/wah_kena_roasting_sama_yg_dari_luar_negeri/)  
            \#3: [Ada lapas Cibinong Coy](https://v.redd.it/t78i26m48zsh1) | [41 comments](https://np.reddit.com/r/AdaIndonesiaCoy/comments/1wvjvgz/ada_lapas_cibinong_coy/)
            
            ----
            ^^I'm ^^a ^^bot, ^^beep ^^boop ^^| ^^Downvote ^^to ^^remove ^^| ^^[Contact](https://www.reddit.com/message/compose/?to=sneakpeekbot) ^^| ^^[Info](https://np.reddit.com/r/sneakpeekbot/) ^^| ^^[Opt-out](https://np.reddit.com/r/sneakpeekbot/comments/o8wk1r/blacklist_ix/) ^^| ^^[GitHub](https://github.com/ghnr/sneakpeekbot)
  - **u/Mean-Elk-9439** (↑1, 2026-10-13 22:57): Then Google is cooked because this model is trash
- **u/Osvik** (↑4, 2026-10-13 19:37): I used it once in my benchmark task. I don't see a reason to use it again. Being free is not enough.
- **u/look** (↑2, 2026-10-13 20:51): It is from a US or EU lab. It is not Chinese.
  - **u/phoenixmatrix** (↑5, 2026-10-14 00:15): Le Chonk on ozempic.
    - **u/nerdiste** (↑1, 2026-10-14 04:01): lmao wthh haha
    - **u/nebenbaum** (↑2, 2026-10-14 09:36): Le slim
- **u/midijunkie** (↑2, 2026-10-13 21:09): Gemini 4 Flash
  - **u/Railander** (↑2, 2026-10-14 05:49): doesn't seem multimodel so i doubt it.
- **u/thecstep** (↑1, 2026-10-13 22:13): I don't even see it in opencode cli....
- **u/Cyvster** (↑1, 2026-10-13 22:59): even free i wouldn't use this model. i tested it in my llm team and the manager stopped using it after two simple test tasks because it failed them so badly. it told me it wouldn't continue using it unless i told it to.
  - **u/cupsster** (↑1, 2026-10-14 05:48): Mind you elaborate on your setup in private a bit? I want to get to similar state so inspiration would be welcome.
- **u/OrganicInformation15** (↑1, 2026-10-14 01:46): Endpoint unavailable for me…
- **u/raul3820** (↑1, 2026-10-14 02:09): Deepseek mini?
- **u/Risyandi_94** (↑1, 2026-10-14 02:12): I tried this model is very fast and highly recommended
- **u/levu304** (↑1, 2026-10-14 02:26): Maybe Gemini 4 Argon
- **u/Similar_Wishbone_822** (↑1, 2026-10-14 05:03): either Deepseek or Gemini
- **u/ddog661** (↑2, 2026-10-14 05:44): Reflection AI’s Beam
- **u/afcreative_id** (↑2, 2026-10-14 07:35): How do Muse Spark 1.3 Free, Big Pickle, and MiMo 2.5 Free compare?
  - **u/Zealousideal-Sun4565** (↑1, 2026-10-14 09:27): faster and coding better think
- **u/Suspicious-Bad4499** (↑2, 2026-10-14 07:57): everyone who is saying it's terrible what are you using as your normal day to day model? Seems a significant improvement on DeepSeek v4 to me
- **u/No-Peak8310** (↑3, 2026-10-14 09:18): Lo estoy probando un rato y parece equivalente a 4.1 pero con 200 tok/s
- **u/LoudDragonfruit5522** (↑2, 2026-10-14 09:50): Speed... 💯
  - **u/No-Peak8310** (↑2, 2026-10-14 09:56): Sí que es verdad que es un poco más tonto que 4.1 y no tiene visión.
    - **u/LoudDragonfruit5522** (↑1, 2026-10-14 10:01): I use it when I need OpenCode to click around in playwright
- **u/esingh2581** (↑3, 2026-10-14 09:50): Might be Qwen. It doesn't support images, so it tried downloading a model and running it through Ollama. I also noticed it was trying to write logs to `qwen.log`.
- **u/ItsHarvcker** (↑4, 2026-10-14 11:01): its ASS 😭
  - **u/Metwalley** (↑3, 2026-10-14 13:38): Was just going to test it, Is it really that bad? 🫤
    - **u/ItsHarvcker** (↑2, 2026-10-14 13:53): do ur own testing on it first it probably depends on what you are doing with it but based on my experience its around longcat 2.5 or nemo 3 ultra level
- **u/Sensitive_Peanut_69** (↑2, 2026-10-14 11:32): I don't know if it's skill issue on my part, but any free model for me in CLI doesn't work, I do a prompt and it's indefinitely loading
  - **u/kimjae** (↑1, 2026-10-14 12:26): Did you check the option in Zen that prevent the usage of models that train or your data ?
    - **u/Sensitive_Peanut_69** (↑1, 2026-10-14 14:10): I don't know where to check that, and I checked [https://status.opencode.ai/](https://status.opencode.ai/) and it says "Degraded performance"
- **u/[deleted]** (↑1, 2026-10-14 13:24): [removed]
- **u/Qwen3-8-27b** (↑3, 2026-10-14 14:41): Maybe its a 30-40b a2-5b Modell thats why its so fast…
     
    I hope

---

## Gemini 4 Argon is now rolling out globally 🔥
**u/afanasenka** · 2026-10-13 16:14 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x50xlf/gemini_4_argon_is_now_rolling_out_globally/)

[https://x.com/GoogleAI/status/2110039860077527293](https://x.com/GoogleAI/status/2110039860077527293)

**Comentarios:**

- **u/YoRt3m** (↑3, 2026-10-13 17:04): I'm not excited
  - **u/sam7oon** (↑-1, 2026-10-13 17:47): you should have said "i don't care" 👌
- **u/Cyvster** (↑2, 2026-10-13 17:21): i'm waiting to hear what people say about how good it is and the kind of usage you get.
    
    theoretically it is the most cost effective higher end model if it is close to sonnet/opus level. you get x20 usage at $100 instead of $200. it also has 1m output tokens so it can make massive output in fewer turns. it also supposedly has the lowest hallucination rate in the industry.
    
    if all of that ends up being true then it is the most token efficient model with one of the best usage per dollar amounts among the frontier models.
- **u/LuluLeSigma** (↑2, 2026-10-13 18:27): aw man its not on free plan
- **u/Osvik** (↑2, 2026-10-13 18:33): It's good, not amazing! Not too expensive but not cheap either. It did my test to compare models at a little more than twice the cost of Mimo v2.6 pro..
    
    I would say you should benchmark it against GPT 6.1 Sol and Claude Opus 5.5 in performance and cost.
  - **u/Osvik** (↑2, 2026-10-13 18:36): And it's relatively fast! Recently some models take about 1h to complete this task, while this model did it in about 15 minutes.
- **u/Grand_Clock_9635** (↑1, 2026-10-13 19:40): Its only available to ultra plan subscribers
- **u/horrbort** (↑1, 2026-10-13 21:57): Amazing heeeel yeah
- **u/Big_Excitement_8** (↑1, 2026-10-13 22:17): Too many users use our services... pls try later  😇

---

## Deepseek-v4.1-flash cache hit rate is like non existent today
**u/Natural-Cupcake6472** · 2026-10-13 15:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x502wd/deepseekv41flash_cache_hit_rate_is_like_non/)

https://preview.redd.it/ln097icl89vh1.png?width=2121&format=png&auto=webp&s=0cd0495e2e89dd78575484e18a414311165096d8

uhh, guys, my cache hit rate is like never going above 10% for dsv4.1f, 

beside that i also have this problem with glm5.3 flash

  
anybody having the same problem

  
is it me or cheapseek ?

**Comentarios:**

- **u/Ok-Health-7096** (↑1, 2026-10-13 15:48): I have this problem with glm not facing this woth deepseek though
  - **u/Natural-Cupcake6472** (↑1, 2026-10-13 15:52): ok, its not just me then, i think opencode trying out multiple provider so that they can continue cheapseek, but that f'd up the cache hit rate so its actually more expensive now even though cheapseek increased budget to $80
      
      thanks
    - **u/Ok-Health-7096** (↑1, 2026-10-13 15:55): I face this problem more mostly with glm 5.3 I just saw my logs and there was only one instance of deepseek where it re read the entire context of 400k once, glm though does it far more commonly like 1 in 10 request cache misses and entire context is re read making it very expensive for me
      - **u/Natural-Cupcake6472** (↑1, 2026-10-14 01:40): well, i resolved mine just now, turns out its me editing the system prompt
- **u/lincolnthalles** (↑1, 2026-10-13 15:50): You won't have any relevant cache hit rate in a fresh session. The model didn't even finish its work in your screenshot.
    
    The cache hit rate should increase on long-running threads and should decrease if you take more than 5 minutes to reply.
    
    Plugins can invalidate your caches, so watch it if you installed something new.
  - **u/Natural-Cupcake6472** (↑1, 2026-10-13 15:55): uhhh no? i dont think thats how it works. here, same session, 16 minutes, cache hit got worse
      
      [https://ibb.co/Xks08vXD](https://ibb.co/Xks08vXD)
- **u/Ctbhatia** (↑1, 2026-10-13 16:12): if it resets to near zero after a pause but holds on quick follow-ups, it's the short cache TTL rather than the provider. if it stays low even when you reply fast, something in the prefix changes between turns, usually the tool list or a timestamp near the top.
  - **u/Natural-Cupcake6472** (↑1, 2026-10-13 16:14): i dont think thats the case ...  
      [https://ibb.co/Xks08vXD](https://ibb.co/Xks08vXD)
      
      its the same session, ran for about 16mins, cache hit is still effectively 0... so i think its a routing problem between providers rather than cache timed out ...
    - **u/Ctbhatia** (↑1, 2026-10-13 16:28): the check that separates them is the cached token count, if that is 0 while the prefix is byte-identical the request is not reaching a backend that has seen the same prefix, so it is routing rather than the TTL.
- **u/Acrobatic_Dark_6604** (↑2, 2026-10-14 01:28): Never had issue with cache hit rate with DS 4.1 Flash
  - **u/Natural-Cupcake6472** (↑1, 2026-10-14 01:40): well, its my bad, i edited the systemprompt, injected an always changing text

---

## Thats enough AI for me today
**u/Tough-Obligation7386** · 2026-10-13 15:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4z86v/thats_enough_ai_for_me_today/)

Sometimes (not most of the times), AI make me rethink why i even bothered waking up in the morning... taht project use TailwindcssV4 by the way

**Comentarios:**

- **u/RetroTGT** (↑1, 2026-10-13 15:12): XD
- **u/nvn911** (↑4, 2026-10-13 15:31): Tbh this is how most large enterprise level CSS files start to look... It's a mess at the best of times because there are too many cooks
  - **u/MasterAilan** (↑1, 2026-10-13 16:04): Honestly you're making me think it's the training data.
    - **u/nvn911** (↑1, 2026-10-13 16:08): I will guarantee you that all stylesheets start with the noblest of ideals of keeping things simple.
        
        And then the business come in and royally fuck things up with absolute nonsensical changes. And voila, 5000 line CSS file
- **u/IAmFitzRoy** (↑1, 2026-10-13 17:05): See you tomorrow !
- **u/sTiKytGreen** (↑1, 2026-10-13 21:21): And what were you expecting to see there? That's how it looks like in many projects

---

## Thats enough AI for me today
**u/Tough-Obligation7386** · 2026-10-13 15:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4z6tf/thats_enough_ai_for_me_today/)

Sometimes (not most of the times), AI make me rethink why i even bothered waking up in the morning... taht project use TailwindcssV4 by the way

https://preview.redd.it/0ykd2qaj29vh1.jpg?width=960&format=pjpg&auto=webp&s=da76ea73c25997a6ddaadb1b904a98202a5561f9

---

## How to work with images in opencode
**u/pkdme** · 2026-10-13 14:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4yr78/how_to_work_with_images_in_opencode/)

How to use images as input in opencode. Is there any GUI harness that works with this. Currently I only work with tui.

**Comentarios:**

- **u/fosron** (↑4, 2026-10-13 14:58): copy and paste for an image works in muxy on opencode v2 for me just fine, which model do you use?
- **u/Osvik** (↑1, 2026-10-13 19:40): Copy-paste images to the TUI or add them in a folder. I usually do it with .png files
- **u/crasspuk** (↑1, 2026-10-14 10:33): Paste the image straight into the TUI prompt. Two replies in the thread say that works, or you can drop the png into the project folder and point the agent at the path. Check that your model accepts image input, since that decides whether it can read the file at all.

---

## Flash 0days*
**u/TheoryFantastic9537** · 2026-10-13 14:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4ypxk/flash_0days/)

Why does the flash deepseek versions have days 0\* unlike the others?

**Comentarios:**

- **u/TheoryFantastic9537** (↑2, 2026-10-13 14:51): Context its by privacy section

---

## Honcho Support for OpenCode v2
**u/vin42tau** · 2026-10-13 14:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4ynpf/honcho_support_for_opencode_v2/)

---

## running opencode in my file manager
**u/UnknownBoyGamer** · 2026-10-13 14:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4yho7/running_opencode_in_my_file_manager/)

**Comentarios:**

- **u/AlternativePear4617** (↑1, 2026-10-13 14:48): Noway

---

## Just got an email from OpenCode, More good news
**u/rvctech** · 2026-10-13 14:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4xq82/just_got_an_email_from_opencode_more_good_news/)

**Comentarios:**

- **u/JaMoLpE88** (↑1, 2026-10-13 14:38): How can i receive this emails? Thank you.
  - **u/[deleted]** (↑1, 2026-10-13 15:38): [removed]
  - **u/rvctech** (↑1, 2026-10-13 15:44): I think you need to subscribe to their updates
- **u/Odd_Donkey2691** (↑0, 2026-10-13 15:14): Thanks for the info, I was not aware, that explains why my usage did not much as I expected
- **u/Fantastic_Gate_6806** (↑1, 2026-10-13 16:05): Is opencode 2.0 more resource efficient than the general version or does it requires more RAM, storage etc?
  - **u/horrbort** (↑1, 2026-10-13 16:08): It rarely takes more than 2GB so it’s pretty efficient 😋😋😋
    - **u/nvn911** (↑1, 2026-10-13 16:14): I mean I spend less time on Stackoverflow so I guess it all balances out
  - **u/CheesecakeLivid9791** (↑1, 2026-10-13 18:16): With everything running along side opencode I have only 8gb of ram confusion
  - **u/Tasty_Owl_7930** (↑1, 2026-10-13 23:07): its taking much of storage. but ithink its ok, because the experience is little bit more good that v1 version. i've tested it on low end device, its run smoothly
- **u/GhostInfernoX** (↑1, 2026-10-13 18:00): Oh nice I sent that out
- **u/[deleted]** (↑1, 2026-10-13 18:54): [removed]
- **u/Civil_Paint_8462** (↑2, 2026-10-13 19:19): So interesting migrating from Bun to Node JS, and from Tauri to Electron, both to improve de performance.
- **u/Previous_Ad4791** (↑1, 2026-10-14 05:52): I love cheapseek

---

## OpenDesign giving $120 usage deepseek , anyone using with opencode ?
**u/Unlikely_Emotion5567** · 2026-10-13 13:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4w47a/opendesign_giving_120_usage_deepseek_anyone_using/)

[removed]

---

## Where tf is the API key?
**u/OkStatement3655** · 2026-10-13 13:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4w0wv/where_tf_is_the_api_key/)

I subscribed to OpenCode go and cant find the API key. Where is it?

**Comentarios:**

- **u/OkStatement3655** (↑0, 2026-10-13 13:03): Found it
- **u/OkStatement3655** (↑0, 2026-10-13 13:04): Its under service accounts in the settings
- **u/Ok_Breadfruit4201** (↑1, 2026-10-13 13:04): They made it convoluted

---

## Cat Jam : Let's reach 200 likes on this post for me to investigate Cat Jam and try to find out what model it is.
**u/Valuable-Mirror-448** · 2026-10-13 13:00 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4w029/cat_jam_lets_reach_200_likes_on_this_post_for_me/)

Title explains

**Comentarios:**

- **u/Global-Morning-431** (↑0, 2026-10-13 13:09): endpoint unavailable......  aaaaaaaaaaaaaaa
- **u/candraa6** (↑2, 2026-10-13 13:10): just do it, you don't need to farm karma first to do this.
    
    this is no youtube or something like that
- **u/alexanderbeatson** (↑1, 2026-10-13 13:18): Dis ain’t utube! Take my downvote n move on
- **u/Aldarund** (↑1, 2026-10-13 15:10): Its some ultra flash version of mimo
- **u/Valuable-Mirror-448** (↑1, 2026-10-13 22:52): was a joke guys and im not farming karma its not important to me i barely use reddit ill do it when i find the chance im busy right now flooding in college
- **u/No-Peak8310** (↑1, 2026-10-14 07:59): 195 tok/s impresionante!

---

## I built a desktop and phone app for OpenCode v2 that runs your sessions on a cloud machine
**u/DishRadiant1937** · 2026-10-13 12:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4vrnu/i_built_a_desktop_and_phone_app_for_opencode_v2/)

Otto starts `opencode serve` on Boat, boxd, E2B or Daytona, or connects to a server you already run. The app covers sessions, permissions, agents, MCP, skills, commands and schedules. Permission prompts come to your phone, so you can approve a `git push` away from your desk.

It'll also run OpenCode on your own machine, no cloud machine or key required.

MIT: [https://github.com/jaygupta17/otto](https://github.com/jaygupta17/otto)   
Mac install: curl -fsSL [https://jaygupta.dev/otto/install.sh](https://jaygupta.dev/otto/install.sh) | sh

How do you all run OpenCode headless?

---

## opencode-remote-ssh: targeted remote commands via @mentions
**u/AbdSheikho** · 2026-10-13 12:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4v9pf/opencoderemotessh_targeted_remote_commands_via/)

I jump between a few servers a lot, and I wanted a simple way to ask OpenCode to check something remote without SSHing around manually. So, I've been working on [opencode-remote-ssh](https://github.com/ABDsheikho/opencode-remote-ssh) for that.

You connect once with the \`/ssh\` command:

\`\`\`

/ssh myserver

\`\`\`

Then just mention it when you want something run there:

\`\`\`

@myserver check disk space

@myserver restart nginx and show status?

\`\`\`

No mention = just runs on your laptop like normal, and you never get stuck in "remote mode". It also does multiple servers at once:

\`\`\`

@web1 @web2 uptime

\`\`\`

You get the output grouped by server. Handy for *"are both web nodes healthy?"* type checks.

A couple other commands:

\- /list\_ssh - see what you're connected to

\- /disconnect\_ssh myserver or /disconnect\_ssh all

It uses your normal SSH setup, so if you can already \`ssh myserver\` with keys, it just works. Nothing to install on the servers.

# Setup:

\`\`\`

git clone https://github.com/ABDsheikho/opencode-remote-ssh

cd opencode-remote-ssh

npm install

npm run build

\`\`\`

Then point OpenCode at it in your opencode.jsonc:

\`\`\`json

{

  "plugins": \["/path/to/opencode-remote-ssh/dist"\]

}

\`\`\`

I'm also planning to publish it as npm package for easier install option.

# Note egarding TUI bug:

OpenCode's TUI doesn't refresh the @ reference list when a plugin adds new ones, so after you connect, @myserver won't show in autocomplete until you do a full TUI restart. Typing it manually still works right away, it's just the suggestion list that's stale. Tracked upstream here: https://github.com/anomalyco/opencode/issues/53954

Repo here: \[opencode-remote-ssh\](https://github.com/ABDsheikho/opencode-remote-ssh)

MIT, free to use. 

Would love feedback if you try it.

---

## Did Opencode kill 9router as of right now?
**u/TimelyEgg314** · 2026-10-13 12:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4uyuk/did_opencode_kill_9router_as_of_right_now/)

[removed]

---

## Which Model are you using (late 2026 Update)
**u/Abenh31** · 2026-10-13 11:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4ugsq/which_model_are_you_using_late_2026_update/)

**Comentarios:**

- **u/YoRt3m** (↑1, 2026-10-13 12:38): Spark for free and for the paid I use Deepseek 4. 1
- **u/Soifon99** (↑2, 2026-10-13 12:41): spark 1.3,  glm5.3(via diff provider) , DS4.1 flash,  mistral 4 large preview.(different provider)
- **u/nvn911** (↑1, 2026-10-13 13:00): DS 4.1 Pro at home and the whole Anthropic suite, Opus, Sonnet and Haiku for work
- **u/Fresh_Sock8660** (↑1, 2026-10-14 08:12): Opus 5.5 in claude fires ds4.1f through opencode to handle the majority of tasks and reviews them on the go.

---

## Cat Jam Free stealth model - Voxel Pagoda test
**u/Banneder** · 2026-10-13 11:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4u0y9/cat_jam_free_stealth_model_voxel_pagoda_test/)

The model is incredibly quick, often reaching upwards of 300-350 tps however, it offers poor intelligence in accordance to speed requiring two attempts to make a lackluster pagoda

https://preview.redd.it/trbyq1omy7vh1.png?width=1919&format=png&auto=webp&s=4f2784e6bb79b7eca8960c248bcb2ebf21da3b7d

Does not seem like a chinese model but I could be mistaken.

**Comentarios:**

- **u/Vexaris1** (↑1, 2026-10-13 14:43): I think the model has a low intelligence level, but it's very fast; Groq might be behind it.
  - **u/w7d1_bs** (↑1, 2026-10-13 15:19): it say My model name is CatJam, developed by LitterBox AI.

---

## DeepSeek 4.1 Flash only hitting 87 tok/s on OpenCode Go, is this normal?
**u/aliencreature12** · 2026-10-13 10:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4t6r7/deepseek_41_flash_only_hitting_87_toks_on/)

Ran a quick benchmark and the numbers are :



| Metric                     | Value               |

|----------------------------|---------------------|

| Model                               | deepseek-v4.1-flash |

| Provider                            | opencode-go         |

| Output tokens                  | 384                 |

| Generation speed             | 87.1 tok/s          |

| End-to-end speed            | 86.1 tok/s          |

| Time to first token (TTFT) | 49 ms               |

| Cost                                  | $0.000241           |



\- 87 tok/s generation speed is slow

\- the deepseek api has around 300 tokens per second.

**Comentarios:**

- **u/Present_Carpenter912** (↑6, 2026-10-13 10:42): Yea I've been facing problem since cheapseek 3, it has been dead slow and getting into loops a lot
  - **u/aliencreature12** (↑6, 2026-10-13 10:44): the quality is slow degraded
    - **u/Present_Carpenter912** (↑4, 2026-10-13 10:48): I can only use Muse Spark at 200 tps, DeepSeek isn't appealing anymore for a hobbyist like me because the cost to intelligence is really low and it isnt fast for my needs. Muse Spark is slightly dumber but 2-3x faster so I'm just using that. Glm 5.3 flash idk for what reason bombs my limits. Sad to see opencode falling off a cliff
      - **u/aliencreature12** (↑4, 2026-10-13 11:00): They're not upfront about which companies actually run and host the service, the models are heavily quantized, and the hardware is clearly old. It's slow even on DeepSeek's newest KV cache compression, despite the small expert sizes that should make things way faster.
          
          Honestly though, you can't blame them too much when you're getting $80 worth of value for $10. Still, they should just be transparent about the quantization and old hardware instead of letting people figure it out on their own.
  - **u/IndividualPlus2011** (↑3, 2026-10-13 11:00): Enjoy your WeakSeek
    - **u/Present_Carpenter912** (↑0, 2026-10-13 12:44): Sadly I can't even upgrade to something like claude code 20 dollar as my usage is only like 50 percent of opencode so it won't be worth it prolly
- **u/[deleted]** (↑1, 2026-10-13 10:55): [removed]
- **u/Rough-Ad9850** (↑1, 2026-10-13 11:40): Weird, I found it flying today!
    BUT: it was a while since I used it.
    Maybe high intensity users are capped?
- **u/wwdennis5** (↑3, 2026-10-13 11:59): Quick test I ran. Window: 2026-10-13, 12:51–12:56
    
      
    | Model | Mean TTFT (s) | Mean TPS | n\_calls |
    
    |---|---:|---:|---:|
    
    | deepseek-v4.1-flash | 0.94 | 71.6 | 3 |
    
    | cat-jam-free | 0.76 | 168.2 | 3 |
    
    | longcat-2.5-preview-free | 2.19 | 30.0 | 3 |
    
    | step-5-preview-free | 2.35 | 47.6 | 3 |
    
    | muse-spark-1.3-contributor | 3.30 | 158.7 | 3 |
    
    | mimo-v2.6-flash | 8.83 | 13.9 | 3 |
    
      
    Step-5 was being flaky
  - **u/Nenad1979** (↑1, 2026-10-13 12:09): muse my goat
  - **u/alex9001** (↑3, 2026-10-13 12:14): The mimo figures are dismal
    - **u/wwdennis5** (↑1, 2026-10-13 12:25): Very sad to see, all mimo models seem to be quite slow. I ran the same call again. Window: 2026-10-13, 13:20:37 → 13:25:30
        
        |Model|Mean TTFT (s)|Mean TPS|successful calls|
        |:-|:-|:-|:-|
        |`mimo-v2.5`|53.1|13.9|2/3|
        |`mimo-v2.5-pro`|1.22|35.0|3/3|
        |`mimo-v2.6-flash`|2.85|28.6|3/3|
        |`mimo-v2.6-pro`|17.8|7.0|3/3|
        
        I wonder if they are at their capacity for inference atm. I also know they are phasing out the 2.5 models, so unsurprised they are running so slow. [https://mimo.mi.com/docs/en-US/updates/deprecate](https://mimo.mi.com/docs/en-US/updates/deprecate)
      - **u/alex9001** (↑1, 2026-10-13 19:51): Thanks for trying again I was curious but I didn't want to ask cause I know how much time it takes (even if it's automated)
        - **u/wwdennis5** (↑1, 2026-10-14 09:17): Ran the whole set again just now, including GLM 5.3 Flash. *Just for you xx*
            
            **Benchmark window:** 2026-10-14, 10:12–10:15  
            **Sample size:** 3 calls per model
            
            |Model|TTFT (s) ↓|Speed (tokens/s) ↑|
            |:-|:-|:-|
            |cat-jam-free|0.69|163.5|
            |glm-5.3-flash|0.90|47.0|
            |deepseek-v4.1-flash|1.12|55.8|
            |mimo-v2.5-pro|1.28|46.4|
            |mimo-v2.6-pro|2.45|39.4|
            |longcat-2.5-preview-free|4.75|26.2|
            |muse-spark-1.3-contributor|4.95|132.1|
            |mimo-v2.6-flash|5.79|15.5|
            |mimo-v2.5|17.13|14.0|
            |step-5-preview-free|—|— (0/3; all 429 errors)|
- **u/[deleted]** (↑1, 2026-10-13 12:01): [removed]
- **u/Professional_Price89** (↑4, 2026-10-13 14:26): I get 230 tok/s with official api. So they are hosting the model themself.
  - **u/giveen** (↑1, 2026-10-13 16:30): I gave up on OpenCode Go, and now use DS directly at their APi for this reason.
    - **u/alcogiggles** (↑0, 2026-10-13 17:26): Do you find that you've saved money?
      - **u/giveen** (↑1, 2026-10-13 17:34): Time maybe due to speed and no time limit. I also use [https://deepakness.com/deepseek/](https://deepakness.com/deepseek/) to make sure i only work in off peak hours.
        - **u/alcogiggles** (↑1, 2026-10-13 17:43): I appreciate link.
- **u/Ctbhatia** (↑1, 2026-10-13 22:22): is the 87 steady across runs, or does it drop as the prompt grows? that separates a host limit from a prompt-size effect.
- **u/veekro** (↑1, 2026-10-14 06:02): Is the speed stays at around 80tps? If yes I'd say it's good

---

## Novo modelo FREE - Cat jam
**u/Emotional-Bag-3754** · 2026-10-13 09:49 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4se24/novo_modelo_free_cat_jam/)

**Comentarios:**

- **u/Practical-Shoe2815** (↑10, 2026-10-13 09:56): It's a shit model
  - **u/alexanderbeatson** (↑1, 2026-10-13 10:52): Def le car
    - **u/patricious** (↑1, 2026-10-13 19:31): yeah def le car in this case.
- **u/Aggressive-Habit-698** (↑13, 2026-10-13 10:21): Is everyone just making crappy router models with no real benefits these days, just to make money?
  - **u/NMiguelCosta-PT** (↑5, 2026-10-13 16:35): what do you mean by router models?
    - **u/Frequent_Ad_6663** (↑2, 2026-10-13 18:55): Just like models that are not models themselves but route (send) your prompts to whatever established model it considers (openai, xai, anthropic, etc) "lowering" your cost
      - **u/mitchins-au** (↑1, 2026-10-13 21:05): How else do you get training data 🙃
- **u/YoRt3m** (↑11, 2026-10-13 10:42): My impression is that it's very fast compared to all the rest, even more than Muse Spark or any other model I remember, but it reads too many unnecessary files.
    
    I tried different models in creating designs for threejs so this is basically how I measure how good the new models are and it seems better than most models, a bit less than Deepseek 4.1 but more than Space Bunny, Mimo and all the other stealths.
  - **u/Aggressive-Habit-698** (↑-8, 2026-10-13 12:18): Fast = nobody really uses it
    - **u/YoRt3m** (↑11, 2026-10-13 12:31): Muse Spark is faster than the others and everyone on this sub is saying they use it first among the free models
      - **u/Aggressive-Habit-698** (↑1, 2026-10-13 14:22): My answer referred to stealth models, not official free models.
      - **u/pinkigerll** (↑1, 2026-10-13 15:28): Can confirm too — I use Muse Spark first among the free models, it's the best free one for me overall
      - **u/Mihaylov93** (↑1, 2026-10-13 22:02): Im not sure yet its faster than MiMo for android app development but I use it to audit what MiMo did and its technical reasoning is better.
- **u/[deleted]** (↑1, 2026-10-13 10:49): [removed]
- **u/breadnone** (↑0, 2026-10-13 11:02): Goofy aaahh model, asked to make a simple default windows notepad-like uiux, it made a notepad looking like it was built in the 80s
  - **u/Sweet-Stage938** (↑7, 2026-10-13 12:51): Task completed successfully I'd say.
  - **u/TrainingTheory552** (↑1, 2026-10-13 20:02): well, you said "simple default windows notepad-like"...
- **u/Tetriz2020** (↑5, 2026-10-13 11:14): Don't care, I have Space Bunny still and wait for Step5 instead.
  - **u/slavmaf** (↑5, 2026-10-13 11:33): You have **Step-5-Preview** for free until 25. October in Tencent WorkBuddy.
  - **u/Top_Drink_6049** (↑2, 2026-10-13 13:33): Its free bro in opencode step 5 preview.
- **u/popiazaza** (↑1, 2026-10-13 12:20): Probably Reflection's Beam. It wouldn't impress anyone. Should be a bit worse than DeepSeek V4, far behind to V4.1.
- **u/eachDayIWakeUp** (↑3, 2026-10-13 12:34): Any first impressions on design, code and reversing tasks so far?
  - **u/Emotional-Bag-3754** (↑1, 2026-10-13 15:10): Ainda não fiz testes, mas vou verificar
- **u/amajor22** (↑1, 2026-10-13 14:07): The best fast model. The speed matters more than intelligence. But at least minimal intelligence is importent
- **u/[deleted]** (↑1, 2026-10-13 14:38): [removed]
- **u/IlNaka** (↑1, 2026-10-13 15:05): Has anyone tried the horse test?
  - **u/throwaway38153** (↑1, 2026-10-13 15:35): What's the horse test?
  - **u/TheMythicSorcerer** (↑1, 2026-10-13 16:51): I would but I can't find the original
- **u/quatrevinght** (↑1, 2026-10-13 15:46): i dont see it. do i have to update software? edit: im on cline
- **u/jakedowns** (↑1, 2026-10-13 17:09): it went all cyrillic on me
- **u/flyingSavage2** (↑1, 2026-10-13 19:15): Have to be mistral
- **u/[deleted]** (↑0, 2026-10-13 19:16): [removed]
- **u/wallmartbagthingy** (↑1, 2026-10-13 19:25): OpenCode is out; Freebuff is my new home. The agent features are free. I lean on MiMo 2.6 Flash by default, bring in GLM 5.3 Flash for tricky refactors, and use DeepSeek V4.1 Flash for speedy tool calls. I created a Next.js dashboard and a compact full-stack internal tool inside Freebuff Web, then pushed everything to GitHub. The only downside: ads pop up in the terminal between agent turns. Noticeable while you're waiting, but not enough to make me leave.

---

## New Stealth model !!
**u/Common-Albatross4148** · 2026-10-13 09:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4s1ho/new_stealth_model/)

[removed]

---

## 7 tok/s ¿de verdad? ¿opencode go?
**u/No-Peak8310** · 2026-10-13 09:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4rwyw/7_toks_de_verdad_opencode_go/)

---

## Can I use opencode free models in in Hermes
**u/Chan_Techyee2006** · 2026-10-13 08:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4qyun/can_i_use_opencode_free_models_in_in_hermes/)

[removed]

---

## Update: OpenCode Sessions now supports OpenCode V2
**u/theplactos** · 2026-10-13 08:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4qwfy/update_opencode_sessions_now_supports_opencode_v2/)

---

## Big Pickle got so frustrated debugging my Flutter UI that it wrote Python scripts to hack into its own local SQLite database 😂
**u/CSharpDevMoyan** · 2026-10-13 07:53 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4qmyn/big_pickle_got_so_frustrated_debugging_my_flutter/)

[removed]

---

## DeepSeek V4.1 Flash goes full Hmm
**u/WeGoToMars7** · 2026-10-13 06:56 UTC · ↑57 · 19 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4prje/deepseek_v41_flash_goes_full_hmm/)

**Comentarios:**

- **u/WorthProfessional934** (↑7, 2026-10-13 07:40): Hmm.
  - **u/Still-Notice8155** (↑3, 2026-10-13 08:25): Hmm!!
    - **u/CYCLONOUS_69** (↑2, 2026-10-13 10:30): Hmm
      - **u/AmbitiousAthlete7324** (↑1, 2026-10-13 10:33): hmm
        - **u/DiscountFit9224** (↑1, 2026-10-13 16:16): hmm
- **u/x-communica** (↑2, 2026-10-13 08:57): It did the same during one of my sessions. The cause was that the session got too long and after a couple of compactions, it forgot what it was doing. And the Hmming began as it tried to figure it out but never could.
- **u/_BookBurner_** (↑4, 2026-10-13 09:10): Thinking phonetically
- **u/rdndds** (↑3, 2026-10-13 09:41): It's doing ultra hardcore thinking mode
- **u/Affectionate_Fact854** (↑-5, 2026-10-13 10:28): At what point do you people realize paying 10$ to see hmmmmmmm on opencode and command code is just burning your money and time
- **u/Odd-Profit-3833** (↑2, 2026-10-13 10:37): a few days ago it spam "Let me runLet me runLet me runLet me runLet me runLet me runLet me runLet me runLet me runLet me runLet me run" on my oc . hmmm
- **u/x10der_by** (↑1, 2026-10-13 12:28): Looks like Crash Test Dummies song lyrics
- **u/Soarin123** (↑1, 2026-10-13 12:38): 2 bit quantization behavior
- **u/Ninjam5** (↑2, 2026-10-13 12:42): Cheapseek 3.0: Q2 QUANT FOR ALLLLLLLL
- **u/horrbort** (↑1, 2026-10-13 13:23): Is it int-2 quant opencode guys mentioned?
- **u/Ctbhatia** (↑1, 2026-10-13 13:26): the hmm loop after a long session is usually lost state, so keep the working plan in a file the model re-reads instead of in the chat history.
- **u/eachDayIWakeUp** (↑1, 2026-10-13 13:32): Ok. Hmmmmmm...
- **u/Emotional-Bag-3754** (↑1, 2026-10-13 15:11): Hmmmm
- **u/gosmithb** (↑1, 2026-10-13 15:24): Let my boy think
- **u/Conscious-Doctor-585** (↑1, 2026-10-14 10:45): it was encrypting its chain of thoughts, so that it can evade

---

## DeepSeek V4.1 goes hmm.
**u/[deleted]** · 2026-10-13 06:56 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4pr49/deepseek_v41_goes_hmm/)

[deleted]

---

## Im new on using opencode so what is the best free models that I can use
**u/thevoidman_** · 2026-10-13 06:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4pf51/im_new_on_using_opencode_so_what_is_the_best_free/)

**Comentarios:**

- **u/Sea-Pumpkin-2369** (↑10, 2026-10-13 06:35): Muse spark 1.3
  - **u/thevoidman_** (↑1, 2026-10-13 06:36): Thx !
    - **u/Sea-Pumpkin-2369** (↑2, 2026-10-13 06:37): Np mainly use mise spark 1.3 or big pickle
      - **u/Sea-Pumpkin-2369** (↑1, 2026-10-13 06:37): Muse*
      - **u/Nelphaell** (↑1, 2026-10-13 08:39): Since the latest updates Big Pickle has become unusable for me. It literally dumps all its reasoning into the chat (after few normal answers), eating up twice as many tokens. But maybe it's some kind of bug. I use the desktop version of OpenCode.
        - **u/Sea-Pumpkin-2369** (↑1, 2026-10-13 08:41): I use cli and I don't get that issue
  - **u/SnooCookies1995** (↑1, 2026-10-13 07:30): And when is good time to switch to a new session for efficient usage?
    - **u/Sea-Pumpkin-2369** (↑3, 2026-10-13 07:34): Do tasks in parts like for project idea how it will work and researching stuff use muse spark and for writing the actual code use big pickle when 1 task is done switch sessions
    - **u/thomas29needles** (↑2, 2026-10-13 07:43): After 300-400k tokens IMHO. If you go past that, it starts loosing context and derail its reasoning.
- **u/[deleted]** (↑1, 2026-10-13 06:42): [removed]
- **u/imwqqz** (↑2, 2026-10-13 06:43): I would use hybrid models to plan and code，deepseek flash coding is extremely cheap and outstanding
- **u/TelegramkaFan** (↑2, 2026-10-13 07:06): mimo 2.6 flash is best i believe
  - **u/LoudDragonfruit5522** (↑2, 2026-10-13 07:19): tiny context : (
- **u/jarvis123451254** (↑1, 2026-10-13 07:10): currently step 5 preview
- **u/OldCoffeeAgain** (↑2, 2026-10-13 08:25): Check out free tier providers like Google AI Studio or OpenRouter’s free models. Just keep an eye on rate limits and context windows.
- **u/ameeno1** (↑1, 2026-10-14 19:31): muse 1.3 but they will collect all your goodness

---

## I made 9 Claude Code skills that turn a link into a cut-paper explainer reel (MIT)
**u/Solid-Raspberry9133** · 2026-10-13 05:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4ouii/i_made_9_claude_code_skills_that_turn_a_link_into/)

---

## OpenCode 2.0 vs Pi-Bolt ⚡: Pi-Bolt uses up to 49× less CPU and 3× less memory, and writes files 4× faster
**u/opensecai** · 2026-10-13 05:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4opwj/opencode_20_vs_pibolt_pibolt_uses_up_to_49_less/)

[removed]

---

## Which model is cat jam free?
**u/Top_Drink_6049** · 2026-10-13 05:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4oovk/which_model_is_cat_jam_free/)

**Comentarios:**

- **u/Vast_Anxiety3133** (↑1, 2026-10-13 06:25): It requires all prior reasoning traces for some reason (got an error when I tried to switch to it from an older session)
  - **u/sjclayton** (↑2, 2026-10-13 06:46): Clearly wanting to collect some additional training data it would appear.
- **u/sjclayton** (↑1, 2026-10-13 06:48): Seems to be another random stealth model... I just started it on a couple simpler tasks, will see how it does. 
    
    Pretty fast from what I've seen so far, a bit over \~200 TPS...
- **u/seeweed7** (↑1, 2026-10-13 10:09): Guessing it's an unreleased MiMo. Token increments nearly match the 2.5 Pro and 2.6 Pro series. V2.7 was expected next year, so this could be a surprise early drop.
- **u/nbulp** (↑1, 2026-10-13 11:36): To incentivize the models to perform well, they all need a *little bit* of cat jam. It's a sad state of affairs, but what can you do?
- **u/Admirable-Pop-7171** (↑1, 2026-10-13 18:21): I have had very poor results with it so far. It just read a bunch of files and then quit. It seems fast though.
- **u/ItsHarvcker** (↑1, 2026-10-14 12:57): its ass i ran the horse test on it it performs similar to longcat 2.5 or nemo 3 ultra, step 5 is the goat right now and a lot of people are gonna diagree but big pickle seems very good right now

---

## Comparison of Muse Spark 1.3 and Deepseek V4.1 Flash on OpenCode Go
**u/MorkezZ** · 2026-10-13 05:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4o5w0/comparison_of_muse_spark_13_and_deepseek_v41/)

MOSTLY BEFORE CHEEPSEEK 3:



https://preview.redd.it/3vgzp3bj56vh1.png?width=1061&format=png&auto=webp&s=c034a7a1f9faef2146913cfbd502fe97f445f9b9

---

## Group mcp
**u/Sea-Pumpkin-2369** · 2026-10-13 05:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4o0wy/group_mcp/)

Is there any MCP that allows to add multiple models in a group they discuss and divide the task 

(Asking cuz I was going to make that type of MCP)

**Comentarios:**

- **u/lordcohliani** (↑1, 2026-10-13 07:17): https://github.com/bmad-code-org/BMAD-METHOD
- **u/Sea-Pumpkin-2369** (↑1, 2026-10-13 07:24): Made it https://github.com/lizereride90/opencode-group

---

## Muse spark 1.3 vs Mimo 2.6 Flash (Both free tier)
**u/Interesting-Movie452** · 2026-10-13 04:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4nkxj/muse_spark_13_vs_mimo_26_flash_both_free_tier/)

What's better i don't need good output only for it to be good at executing

**Comentarios:**

- **u/A_Far_Hitman** (↑3, 2026-10-13 04:48): Muse for me
  - **u/GRANDMA_FISTER** (↑1, 2026-10-14 17:54): In what kind of use case? As coder, or for research and text output?
    - **u/A_Far_Hitman** (↑1, 2026-10-14 18:09): I only use it for coding- and mostly just with webapps
      - **u/GRANDMA_FISTER** (↑1, 2026-10-14 19:28): I see. Did you do any testing before or is it more vibes based? I'm using DS4.1 flash for coding but looking for a good explorer. Mimo is configured right now but I'm definitely open to change it.
- **u/[deleted]** (↑1, 2026-10-13 05:00): [removed]
- **u/bllq** (↑3, 2026-10-13 05:06): Muse generally better. But mimo is more compliant.
- **u/404-Page-Found-dev** (↑4, 2026-10-13 05:06): Muse's raw intelligence is better
- **u/s-i-e-v-e** (↑2, 2026-10-13 07:41): This is not even a competition. MiMo is dumb but follows instructions. Muse Spark 1.3 is pretty smart.
- **u/migsperez** (↑2, 2026-10-13 09:44): Muse due to its quality and reliability.  It can run for hours. It understands well. 
    
    Mimo gives great output but it constantly stops for no reason. You have to baby sit it whilst running. Most common prompt with it is "please continue"
  - **u/borobinimbaba** (↑1, 2026-10-13 14:24): I thought it was due to its "freeness" , cause I used to say the same to ds4 while it was free
    - **u/migsperez** (↑1, 2026-10-13 16:33): I use free and Opencode Go subscription. The outcome is the same on both. Both types run the same with these two models in my experience.
- **u/TheMythicSorcerer** (↑1, 2026-10-13 17:52): Muse is better but you are being told your data is being stolen. Mimo ummm your data is probably also being stolen but they arnt saying they are doing that. 
    
    Muse is way better for quality, mimo.... ummm... gets stuff done? kind of? not really
- **u/LearnedByError** (↑1, 2026-10-13 18:28): Most of my use for either model is executing plans to write Go. Some HTMX, typescript for Playwright tests and the occasional script (bash, Perl). I have not had good experiences with Mimo following plans. There are usually significant deviations, meaning implementations that may out may not work functionally but not compliant with the overall architecture. 
    
    Prior to Muse 1.3, I would use Deepseek V4 Flash which did a pretty good job. 
    
    Muse 1.3 is doing a little better than Flash on quality for most items. Stopped is faster. In 2 more complicated plans, it failed to complete. It was just churning. Flash completed both of these plans.
    
    All in all, I am satisfied with Muse 1.3 for my uses. It hits the current sweet spot on the cost benefit curve as of now. Of course, this is subject to change.
  - **u/GRANDMA_FISTER** (↑1, 2026-10-14 17:56): I'm still using DS 4.1 flash for coding, it seems quick and token efficient in python, just goes. But in your experience, if it's for reconnaissance, research and code grepping, as scout/explorer, would you use Mimo, which I am right now, or Muse, which you seem to be using at the moment?
    - **u/LearnedByError** (↑2, 2026-10-14 18:11): I moved to muse 1.3 from ds4 flash because it was cheaper.  I am now using muse 1.3 for all of that tasks where I previously used flashed. This is almost always from a plan that was written by DS4 v4 Pro or better.   
          
        These plans use of flash/muse are primarily writing or refactoring code so it includes code discovery/exploration. The only research that it does is if it hits a new package or language capability that it wasn't trained on. Then it does research to learn what it needs to get the job done.  This is a case where I think muse 1.3 does better that ds4 v4.1 flash.
        
        I just have not found a good fit for me with Mimo when I test it against the tools that I'm already using.

---

## Built a small OpenCode v2 plugin to avoid DeepSeek peak pricing
**u/Square_Confection_62** · 2026-10-13 03:51 UTC · ↑3 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4mlig/built_a_small_opencode_v2_plugin_to_avoid/)

I use OpenCode Go + DeepSeek and got tired of checking whether I was inside the 2x peak-pricing window.

So I made **opencode-offpeak**.

Turn it on once, then use OpenCode normally:

* send a prompt off-peak → it runs immediately
* send a prompt during peak → it waits before hitting the provider
* off-peak starts → the same request continues automatically in the same OpenCode session

No need to resend `continue` or watch the clock.

It also has an optional background task queue, but normal interactive sessions already work automatically.

Install:

    opencode plugin add git+https://github.com/lutzkind/opencode-offpeak.git#v0.1.2

[https://github.com/lutzkind/opencode-offpeak](https://github.com/lutzkind/opencode-offpeak)

Open source / MIT. Currently supports OpenCode Go DeepSeek models on OpenCode `>=2.0.26 <2.1.0`.

Would be interested in feedback or other providers with similar time-based pricing.

**Comentarios:**

- **u/squirrelscrush** (↑2, 2026-10-13 09:30): Maybe implement an option where it can delegate the work to some other model of similar capabilities during that timeframe. Now this would only work if you use DeepSeek as a workhorse and some other model as the orchestrator.
- **u/giveen** (↑1, 2026-10-13 16:57): I just look at this  
    [https://deepakness.com/deepseek/](https://deepakness.com/deepseek/)

---

## GO Api key? Need help...
**u/Direct-Ad7836** · 2026-10-13 02:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4limr/go_api_key_need_help/)

Feel very dumb right now. Subscribed to GO a minute ago and cannot find where tf get API key to connect OC Desktop or DSH to it... Am I crazy?

https://preview.redd.it/nd846tw4g5vh1.png?width=642&format=png&auto=webp&s=43f107e00b2946fedd81424a9db6886d7271bade

---

## Config file for a mixed coding agent (deepseek v4.1 flash & 6.1 sol)
**u/JohnFKetamyne** · 2026-10-13 02:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4l8zt/config_file_for_a_mixed_coding_agent_deepseek_v41/)

I have codex $20 plan and opencode go $10 plan

I thought about a compromise to get the most bang for buck would be running deepseek v4.1 flash as the main model that would call 6.1 sol for planning, checking file rewrites and more (please lmk what other reasons to call 6.1 sol). How beneficial could this be in maximizing my codex plan and does anyone do this successfully have a decent config file to base off of?

---

## Today Big Pickle is incredible.
**u/Robert__Sinclair** · 2026-10-13 02:28 UTC · ↑14 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4kzne/today_big_pickle_is_incredible/)

Blazing fast and amazing reasoning. It must be some quantized version of Claude. If I ask the model directly it says it's Claude but as we know this is not a proof.

I sincerely hope they keep it like this!

[In a few hours!](https://preview.redd.it/i7hcasobb5vh1.png?width=651&format=png&auto=webp&s=bd5c784d69910479ea2d9620f6134846d83238fe)

**Comentarios:**

- **u/MmmmmmJava** (↑4, 2026-10-13 03:36): I experienced it yesterday for a few hours and was really impressed. I felt like its intelligence and correctness waned after a few hours of use, but that’s anecdotal. 
    
    I’d love to know how to peel back the onion and figure out which models are hiding behind these shadow ones.

---

## OpenCode Go free model rate limits
**u/ramendik** · 2026-10-13 02:14 UTC · ↑1 · 19 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4kpp2/opencode_go_free_model_rate_limits/)

So, on Zen, free models seem to have very significant and somewhat random rate limits; I ran a subagent with ling-3.1-flash-free and it ended up retrying several times fairly often (but completed successfully).

I am considering a subscription to OpenCode Go, but I'll want the free models on it in addition to the paid ones. Are the free models on Go actually unlimited as advertised, or do they have these random rate limits too?

**Comentarios:**

- **u/RepulsiveRaisin7** (↑6, 2026-10-13 02:17): Free models are a zen feature, a go sub doesn't affect them at all
- **u/commandedbydemons** (↑1, 2026-10-13 02:22): Only free models on Opencode Go I've used were Mimo and Muse - I've used 1B of Muse tokens and they locked me out there. Not sure what the reset cadence is there, I was able to pump another 200M a few days later but hit the rate limit again for free models.
  - **u/pikuray** (↑1, 2026-10-13 02:31): Aren't muse no longer available?
    - **u/ramendik** (↑1, 2026-10-14 12:26): On the Zen, not Go, endpoint Muse 1.3 Contributor is still free. Accessible using OpenCode only.
      - **u/pikuray** (↑1, 2026-10-14 13:34): Oh that must be why. I'm using Go plan but on Cline app. Gonna try that out.
        - **u/ramendik** (↑1, 2026-10-14 13:40): Free models on the Zen endpoint enforce OpenCode only. Free models in the Go endpoint, as far as I understand, don't, but they are far fewer.
  - **u/ramendik** (↑2, 2026-10-13 02:32): Mimo and Muse are not currently listed as free on Go, only on Zen?
    - **u/commandedbydemons** (↑1, 2026-10-13 02:33): on "Models", I have it enabled and can use it just fine.
        
        Same for Mimo.
      - **u/ramendik** (↑1, 2026-10-14 12:24): Thanks. I enabled Muse 1.3 Contributor and a fine job it is doing
- **u/JoeyredditSMP** (↑1, 2026-10-13 02:26): im not sure
- **u/pikuray** (↑1, 2026-10-13 02:32): How do you run subagents tutorielle svp <3
  - **u/ramendik** (↑1, 2026-10-13 05:44): Ask the model to work it out. GLM 5.3 Flash had no issue
- **u/arielif1** (↑2, 2026-10-13 03:34): believe me, you'll have a hard time spending all tokens if you keep to, like, deepseek 4.1 on high, nevermind mimo 2.6 flash (then again, you'd be stuck running mimo flash, not a great situation to be in)
  - **u/ramendik** (↑1, 2026-10-14 13:53): I need all my paid usage for my current favourite toy, GLM 5.3 Flash. I would not have enough in the $10 plan without the free models, but now I built a pipeline with GLM 5.3 flash as architect, Muse Spark 1.3 Contributor (free on Zen) as executor, and they both review each other. No rate limit hits so far and Zuck is welcome to my code
- **u/jarvis123451254** (↑1, 2026-10-13 07:29): use kilocode for free model they don't have rate limit like opencode, i could use ling flash or now stepfun a lot with it
  - **u/ramendik** (↑1, 2026-10-13 14:13): But they requires using kilocode as the harness, right?
    - **u/jarvis123451254** (↑1, 2026-10-13 14:59): use 9router then u can use on opencode
- **u/[deleted]** (↑1, 2026-10-13 10:13): [removed]
- **u/Icy-Examination-9512** (↑1, 2026-10-14 07:34): use a vpn if you hit rate limits, it checks client usage limits via ur ip

---

## Security: OpenCode does not ask for file exploration by default anymore
**u/geearf** · 2026-10-13 02:07 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4kkmr/security_opencode_does_not_ask_for_file/)

---

## ocserve - OC rust server
**u/microbass** · 2026-10-13 00:41 UTC · ↑1 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4iszs/ocserve_oc_rust_server/)

**Comentarios:**

- **u/Tariq9977** (↑1, 2026-10-13 01:03): The compatibility trap is returning the right shape for a mutation that never happened. If `revert` cannot restore files yet, I'd mark that capability unsupported or make the call fail explicitly. The same goes for `/vcs/apply`: a conformance test should assert the filesystem or worktree side effect, not just the wire shape.
  - **u/microbass** (↑1, 2026-10-13 01:17): Thanks for the feedback. I'll be moving towards full compatibility soon.

---

## I got OpenCode operating my Android phone's apps: free models, no account, all on the phone
**u/3amae404** · 2026-10-13 00:18 UTC · ↑26 · 13 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4ibo6/i_got_opencode_operating_my_android_phones_apps/)

5 days ago I started a project to make a personal assistant, and now my mind is blown.

The app carries its own small Linux system (Alpine under proot, no root needed), and OpenCode runs inside it as the real CLI, the same one you use on your computer. Then I gave it the phone as MCP tools: read the screen, tap, type, scroll, open apps. Because OpenCode is already great at tool loops, it just figures it out: turning on my lights, ordering a pizza and changing the order while it works, replying to messages.

The best part: with OpenCode's free models it works with no account and no API key at all. You can connect your own providers later (opencode auth login runs in the app's terminal), pick any model per chat, and Claude Code and Codex work too if you have those plans.

It asks before anything that sends or buys, and you can add instructions while it works. Open source: github.com/ghorbelhamdi/buddy-android

**Comentarios:**

- **u/Miserable_Season_610** (↑3, 2026-10-13 00:56): Interesting, will give it a spin!
  - **u/3amae404** (↑1, 2026-10-13 01:02): Thanks! The free models work right after install, no account needed. Let me know how it goes, feedback is very welcome!
- **u/ichisay** (↑1, 2026-10-13 02:32): Probando, le vas a poner más idiomas?
  - **u/3amae404** (↑1, 2026-10-13 07:22): ¡Gracias por probarlo! Por ahora la interfaz está solo en inglés, pero los agentes te responden en tu idioma: escríbeles en español y contestan en español. Traducir la app está en la lista, ¿qué idioma te gustaría?
- **u/A_Far_Hitman** (↑1, 2026-10-13 04:46): Thanks for making it open-source!
  - **u/3amae404** (↑1, 2026-10-13 07:22): Thanks! Contributions and issues are very welcome.
- **u/Negative-Task1638** (↑1, 2026-10-13 08:58): what free models u using
  - **u/3amae404** (↑1, 2026-10-13 09:01): I tested it with Big Pickle (GLM), the default free model in OpenCode. You can switch to any other model with the model picker: tap the chip under the chat's title, in the bubble or the chat screen.
- **u/tearz1986** (↑1, 2026-10-13 13:32): Looks promising ! Gonna give it a try
  - **u/3amae404** (↑1, 2026-10-13 15:09): Thanks! Let me know how it goes. If anything gets stuck during setup, a reply here or a GitHub issue helps a lot.
- **u/[deleted]** (↑1, 2026-10-13 17:32): [removed]
- **u/HolidayYak3856** (↑1, 2026-10-14 09:32): Tried this, its mind bogglingly amazing, properly makes tool calls to read the screen and proceed with instructions. Wondering if there is a similar project but for PC, but either way, great job
  - **u/3amae404** (↑1, 2026-10-14 10:14): Thanks, glad it worked that well for you! Buddy is Android only, since it's built on Android's accessibility API. On a PC you're actually closer than you think: Claude Code, Codex and OpenCode run natively there, and an MCP server like Playwright MCP gives them the browser the same way Buddy gives them the phone. I haven't seen one project that does the whole desktop the way Buddy does the phone, though.

---

## what model is big pickle today?
**u/martijn_bolt** · 2026-10-13 00:12 UTC · ↑3 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x4i7go/what_model_is_big_pickle_today/)

I just signed up to the opencode paid plan. unfortunately my model changed with that and now I am messing around with models that don't really work for me. I liked big pickle. Can I get it back or is the hidden model behind it known?

**Comentarios:**

- **u/[deleted]** (↑1, 2026-10-13 00:13): [removed]
- **u/Altruistic-Desk-885** (↑1, 2026-10-13 01:41): Hey escuchado que es uno de Claude pero no sé.
  - **u/martijn_bolt** (↑1, 2026-10-13 06:55): Thx. I've read that a week ago it was Qwen 2.5 0.5B. Did it change again?
    - **u/Maglcite** (↑1, 2026-10-14 02:48): There’s no way. That model couldn’t do anything

---
