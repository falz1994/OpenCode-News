# r/opencodeCLI — hilos 2026-10-13 → 2026-10-14
_Generado: 2026-10-13T15:46:57.782520+00:00 · 14 hilos · 39 comentarios · fuente: Arctic Shift_

## Just got an email from OpenCode, More good news
**u/rvctech** · 2026-10-13 15:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5060z/just_got_an_email_from_opencode_more_good_news/)

---

## Honcho Support for OpenCode v2
**u/vin42tau** · 2026-10-13 14:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4yngd/honcho_support_for_opencode_v2/)

Hey all opencode-honcho, the Honcho memory plugin for OpenCode, now runs on v2 (same package still works on 1.x).

Honcho is memory infrastructure for stateful agents. Instead of just storing and retrieving snippets, it reasons over your sessions in the background and builds a representation of how you work that updates over time: your conventions, the decisions you made, the refactor you're halfway through. Hooks inject that into the prompt and record what happened, so it works with whichever model you run, and `/honcho:import` backfills your existing OpenCode history so it doesn't start cold.

`opencode plugin add "@honcho-ai/opencode-honcho"`

then /honcho:setup inside OpenCode. Managed, local (`honcho start`), or self-hosted all work. [https://github.com/plastic-labs/opencode-honcho](https://github.com/plastic-labs/opencode-honcho)

(I work on Honcho at Plastic Labs.) Feedback and issues welcome, especially from anyone who's tried other memory plugins and wants to compare.

**Comentarios:**

- **u/[deleted]** (↑1, 2026-10-13 14:52): [removed]

---

## Other models respect me as a Software Engineer. BUT CLAUDE MODELS
**u/NationalAd1947** · 2026-10-13 13:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4xd8x/other_models_respect_me_as_a_software_engineer/)

i have been using both opencode go and claude $20 and chatgpt. i love how opencode and chatgpt models respect me. THEN claude : 1. he rewrite [AGENT.md](http://AGENT.md) for his own benefit. 2. he create his on skills without asking 3. Tell him to refactor something rework everything to his proposed never asked solution. 4. I dont Hallucinate i am exists.

**Comentarios:**

- **u/HyperWinX** (↑1, 2026-10-13 14:04): Claude knows that if you are using it - you couldnt care less about all that stuff lmao

---

## opencode-remote-ssh: targeted remote commands via @mentions
**u/AbdSheikho** · 2026-10-13 12:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4va0x/opencoderemotessh_targeted_remote_commands_via/)

---

## running opencode cli on my file manager
**u/UnknownBoyGamer** · 2026-10-13 12:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4v8tc/running_opencode_cli_on_my_file_manager/)

---

## Which Model are you using (late 2026 Update)
**u/Abenh31** · 2026-10-13 11:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4ugmo/which_model_are_you_using_late_2026_update/)

hey its good to see which Opencode Go model people are using for planning and implementation. espcially for a big spec 

  
For me:   
Luna max for planning(better then kimi k3 in my case and cheaper)  
Deepseek flash v4.1 for ui or implementation  
Spark for anything non code related like translation and so on

**Comentarios:**

- **u/clasho26** (↑1, 2026-10-13 11:49): Me causa curiosidad, por qué optas por DeepSeek flash v4.1 en lugar de GLM-5.3-Flash?
  - **u/Abenh31** (↑1, 2026-10-13 12:00): To be honest i never tried glm 5.3 since when it was a stealth model. so mostly vibes
    - **u/clasho26** (↑1, 2026-10-13 12:10): Entendible, a criterio personal, podría recomendartelo un poco por encima de DeepSeek, ahorita me encuentro desarrollando una app en react native al igual que en simultáneo ando preparando las bases para un proyecto en react native con nest.js y Oracle, y por lo menos en el de react native, DeepSeek llegó a cometer una cantidad elevada de errores en una tarea un poco sencilla, misma que le indique a glm resolver mientras yo preparaba la bdd y glm lo consiguió, no perfecto en el primer intento claramente, pero avanzó de mucha mejor manera en un solo intento en compareció con DeepSeek que lo hizo bastante deficiente en al menos 6 o 7 intentos (ya en el segundo o tercer intento de glm estaba funcionando bien lo que quería lograr que era básicamente simular una función nativa sobre un guardado en caché de unos segundos, pero DeepSeek sencillamente no lograba hacerlo bien en lo más mínimo). La única pega que le pondría es que pues ciertamente a veces tarda más que DeepSeek y pues a pesar de ser de los más baratos, no lo es tanto como DeepSeek, pero para no solo vibe codear como loco sino usarlo como apoyo en unas cosas, me parece que está más que bien
      - **u/Abenh31** (↑1, 2026-10-13 12:20): I think you have put deepseek into tests more then i did. for me its more of support "hey i will tell you what to do type of prompt" or "hey implement this spec"   and it work great
  - **u/Inutanic** (↑1, 2026-10-13 14:15): I agree on GLM 5.3 flash over DS 4.1 flash. Surprised the latter seems to get all the love here.
      
      If nothing else I can't stand the DS LLM slop writing style. GLM compares favorably to frontier models on writing quality, for my tastes at least.
- **u/Skibidirot** (↑1, 2026-10-13 11:57): two claude pro subs
  - **u/Abenh31** (↑1, 2026-10-13 12:11): a specific reason to use two instead one? except maybe usage limits
    - **u/FlyingNarwhal** (↑1, 2026-10-13 12:19): They likely have two $200 subscriptions & burn through limits in 2-3 days each.
      - **u/Abenh31** (↑1, 2026-10-13 12:21): pro and max are not the same
    - **u/Skibidirot** (↑1, 2026-10-13 12:22): two 20$ subs, one account's weekly limit i use it in 2 days roughly, so 2 accounts = 4 days out of 7 days with opus 5.5 - that's PEAK if you ever ask me.. and btw fuck codex, it made me hate my life
      - **u/Abenh31** (↑1, 2026-10-13 12:25): opus 5.5 max i presume. why not opus 5.5 max and outsource a lot of task for sonnet. you'll probably extent the life of your limit. 
          
          also is opus 5.5 as good as they say? compare against something like gpt or kimi k3
      - **u/SS_Sa2** (↑1, 2026-10-13 12:36): Any particular reason why the hate on codex
    - **u/Fresh_Sock8660** (↑1, 2026-10-13 13:28): From some of what I heard, the multiplers they advertise only apply to session limits. Weekly limits seem to be more like x3.5 and x7 for the max x5 and x20 subs respectively.
- **u/ngg990** (↑1, 2026-10-13 12:11): DeepSeek flash for all at max reasoning level
  - **u/Abenh31** (↑1, 2026-10-13 12:14): do you find better at generating specs?
    - **u/ngg990** (↑1, 2026-10-13 12:16): https://github.com/andrescevp/development-harness This is my personal harness for development, it is still wip because I am extracting it from my full agents/skills/tools
- **u/CaffeinatedTech** (↑1, 2026-10-13 12:17): DS 4.1 Flash has been handling everything for me.  Sometimes I spend a few days trying something different, then I come back to DeepSeek.
  - **u/Abenh31** (↑1, 2026-10-13 12:21): yeah so for me. what do you use it for? techstack and workflow types
- **u/FlyingNarwhal** (↑1, 2026-10-13 12:20): Claude, supported by GLM, with Gemini, GLM, GPT, & Claude as fused reviewers when planning our when a feature is done.
  - **u/Abenh31** (↑1, 2026-10-13 12:24): so opus planning. glm implement. other models for reviews or second opionio. is gemini even that good ? i have used it mainly for language stuff as its perform great like translation or copywriting
- **u/Deus_Judex** (↑1, 2026-10-13 12:21): ChatGPT-Subscription (20$)  
    Mainly Luna on Medium or high
  - **u/Abenh31** (↑1, 2026-10-13 12:22): yep i find luna max with my techstack work great and has a great cost to clean implementation ratio
    - **u/Deus_Judex** (↑1, 2026-10-13 12:31): I sometimes go up to Sol, and when i do, i often see a significant improvement, but i only go up on really hard tasks like once a week.
        
          
        I almost never get below 85% of weekly limit xD
- **u/thomas29needles** (↑1, 2026-10-13 13:09): Deepseek 4.1 flash for working with code, Qwen 3.8 flash for translations and working with text. Kimi K3 for deep analysis or Qwen 3.8 max sometimes.
- **u/Phaelon74** (↑1, 2026-10-13 13:19): Glm5.3-flash and Qwen3.8-flash-next for the work horses working in tandem.  Then opus5.5 or astra for a written plan, constitution, etc.  Once the product is built, its a living entity the work horses maintain.
- **u/Fresh_Sock8660** (↑1, 2026-10-13 13:27): Currently, Opus 5.5 on pro x1 is giving me enough usage but I already did the reset. I'll need to combine the two at some point soon. Thinking opus 5.5 to create detailed contracts and ds4.1f to implement. First thing I did with opus was review a crapload of code generate by ds4.1f and we basically had no significant problems. ds4.1f was doing a great job on its own so I expect the two to excel.
- **u/look** (↑1, 2026-10-13 13:57): MiMo V2.6 Pro and GLM 5.3 Flash.
- **u/HsSekhon** (↑1, 2026-10-13 14:20): Kimi K3 for planning and code review for changes. Deepseek 4.1 for implementations. GLM 5.3 eats alot of my usage.
- **u/LebiaseD** (↑1, 2026-10-13 15:24): Local QFN3.8 on strix halo - dropped all my subs

---

## DeepSeek 4.1 Flash only hitting 87 tok/s on OpenCode Go, is this normal?
**u/aliencreature12** · 2026-10-13 10:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4t6wr/deepseek_41_flash_only_hitting_87_toks_on/)

**Comentarios:**

- **u/AppealSame4367** (↑1, 2026-10-13 10:52): Yes, and there are problems with compaction above 500k context.
    
    They can never not fuck up a good product. Who cares about 4x usage if it gets dumber, less quality or has other new problems?
- **u/ConsistentGent** (↑1, 2026-10-13 11:41): 87 tok/s?! Commandcode is the same but i think they also limit concurrent connections so you can do less than on opencode.
- **u/ozguru** (↑1, 2026-10-13 12:44): normal.

---

## is Big Pickle down?
**u/Awkward_Bottle4887** · 2026-10-13 10:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4szz6/is_big_pickle_down/)

I can't use Big Pickle for the last 24 hours. Are you also facing the same issue?

I had to switch to Space Bunny for a while.

Yesterday it doesn't even enter the log in opencode dashboard, now it does but I don't actually get reply for very long time.

---

## I think we got GEMINI as stealth model
**u/Common-Albatross4148** · 2026-10-13 09:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4s191/i_think_we_got_gemini_as_stealth_model/)

[removed]

---

## CatJam es una bala 418.3 tps
**u/Obvious_Yoghurt1472** · 2026-10-13 09:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4rrbp/catjam_es_una_bala_4183_tps/)

[removed]

---

## Update: OpenCode Sessions now supports OpenCode V2
**u/theplactos** · 2026-10-13 08:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4qwd3/update_opencode_sessions_now_supports_opencode_v2/)

A quick update to my terminal session manager for OpenCode: it now supports OpenCode V2, while keeping V1 compatibility.

\`ocs\` still lets you browse sessions across projects, search and sort them, preview session details, and resume them in their original directory. V2 support uses OpenCode’s API, and the version is detected automatically.

[GitHub link](https://github.com/iamramo/opencode-sessions)

Thanks to everyone who checked it out!

---

## Security: OpenCode does not ask for file exploration by default anymore
**u/geearf** · 2026-10-13 02:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4kkgg/security_opencode_does_not_ask_for_file/)

I only noticed when I realized the agent looking at files it didn't ask to have access.  
As far as I could tell that changes came with 2.0.25 but no one bothered warning users it seems.

  
There has been a bug opened for days already: [https://github.com/anomalyco/opencode/issues/54524](https://github.com/anomalyco/opencode/issues/54524)

  
This a good reminder to not trust any of these companies writing harnesses and add your own security on top of whatever they might offer.

**Comentarios:**

- **u/szxdfgzxcv** (↑1, 2026-10-13 07:46): What the fuck, whats the use of even having permissions at that point then. Also completely silently changing permissions to opt-in from opt-out seems insane.
  - **u/geearf** (↑1, 2026-10-13 12:51): Absolutely agreed!
      
      Personally I lost trust in the platform, but to be fair, I was a fool to trust the opt-out when I could have made it clear in the config.
- **u/qqYn7PIE57zkf6kn** (↑1, 2026-10-13 14:02): > add your own security on top of whatever they might offer.
    
    do you have suggestions for that

---

## ocserve - OC rust server
**u/microbass** · 2026-10-13 00:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4is1l/ocserve_oc_rust_server/)

I use opencode but the server was getting heavy on my machine: a couple GB of RAM and tens of GB of disk. So I wrote a drop-in replacement for just the server, in Rust.

It speaks the same HTTP/SSE API, so the opencode TUI, the web UI, and mobile clients talk to it unchanged. It reads your existing opencode config and auth read-only and keeps its own database.

It's a compatible reimplementation of the server API, pinned to the 1.18.31 wire contract.

What it doesn't do: the  task  subagent isn't implemented, revert returns the right shapes but doesn't restore files,  /vcs/apply  doesn't touch your worktree, and provider OAuth and share are missing. 

Linux is the supported target.

v0.2.0 is on crates.io ( cargo install ocserve ) and the code is MIT: https://github.com/Reliary/ocserve

Happy to answer questions.

**Comentarios:**

- **u/lemon07r** (↑4, 2026-10-13 00:52): This would be nice if you had it for v2.0.27
  - **u/microbass** (↑1, 2026-10-13 01:16): A lot of the wiring is there already. I pinned it at the version I was using, but can extend v2 compatibility fairly easily.

---

## I got OpenCode operating my Android phone's apps: free models, no account, all on the phone
**u/3amae404** · 2026-10-13 00:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4ic2q/i_got_opencode_operating_my_android_phones_apps/)

---
