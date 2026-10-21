# r/opencode — hilos 2026-10-21 → 2026-10-22
_Generado: 2026-10-21T13:42:06.203012+00:00 · 32 hilos · 7 comentarios · fuente: Arctic Shift_

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

---

## Is the paid subscription deepseek flash faster than the free flash?
**u/RiskNumerous3860** · 2026-10-21 09:24 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbig9b/is_the_paid_subscription_deepseek_flash_faster/)

I've been using the free flash in the opencode OS standalone console and it is very very slow compared to using the flash api directly through vscode copilot harness.  

  
Is there any speed difference in the flash included in the cheap-seek metered flash with the opencode go paid subscription?

---

## OpenCode with Deep Infra
**u/editemup** · 2026-10-21 09:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbi30p/opencode_with_deep_infra/)

Idea is to use open source models hosted on deep infra with open code, wanted to get a sense of the budget you plan for such a use case, also general feedback on quality of artifacts produced

---

## Why do people use open code instead of unsloth studio ?
**u/sly3x** · 2026-10-21 08:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbi0qv/why_do_people_use_open_code_instead_of_unsloth/)

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

---

## MiniMax 3.1 is unusable in its current state
**u/Lordddddddy** · 2026-10-21 07:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbh3k8/minimax_31_is_unusable_in_its_current_state/)

https://i.redd.it/vfbv817i1swh1.png

Been getting for 2 days straight infinite loops, with massive thinking boxes even though I'm using medium or high, I never in my life got a model to 900k context and this one got to it for a simple bugfix, this is ridiculous, it's happening to someone else or is this just something related to me?

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

---

## GLM 5.3-flash and DeepSeek v4.1 Performance
**u/rizaldywirawan** · 2026-10-21 07:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbgian/glm_53flash_and_deepseek_v41_performance/)

How is the model performance? is it slow?

I use another local router in my country, and when i tried to use GLM-5.3-flash, the performance is pretty slow, and there are lots of timeout.

---

## Does OpenCode prioritize paid users over free users?
**u/Equux** · 2026-10-21 07:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbggkf/does_opencode_prioritize_paid_users_over_free/)

Ever since making all of these models free, I'm getting rate limiting issues left and right. I understand that opencode is a business, and the "free tier" is how they find their prospects, but it does feel like paid users don't get much more for paying OC money. I'm getting rate limited at every turn, and I can only imagine it's because they made so many of these models free.

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

- **u/CalamityMetal** (↑6, 2026-10-21 06:42): Yeah we need transparency on this
- **u/GoldenX86** (↑2, 2026-10-21 06:47): I wonder which one is it, if opencode is quantizing the model or the kv cache, or if deepseek saves a better model version for themselves
- **u/Amarsir** (↑2, 2026-10-21 06:48): We don't know, and it might not even be one. They might switch and load balance between multiple.
    
    (I haven't seen this claimed about 1017 yet, but sometimes people report very low cache hit rates and that's almost certainly because of a provider reroute.)
- **u/DocumentFun9077** (↑2, 2026-10-21 07:01): OC mostly uses OrcaRouter from what I know
- **u/sukazu** (↑2, 2026-10-21 07:04): If they used the same full quality checkpoint than DeepSeek, you can be sure they would advertise it.   
    
    Either they don't, or they mix it up.
- **u/appsettings** (↑2, 2026-10-21 07:22): It's a disquise prank. If you know how to check you will understand most of their model gets redirected to cheaper one

---

## OpenCode keeps getting stuck in an infinite shell-command loop. Anyone else experiencing this?
**u/Clear_Expert_7669** · 2026-10-21 06:22 UTC · ↑2 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbfjxi/opencode_keeps_getting_stuck_in_an_infinite/)

Hey everyone, I’m using OpenCode to develop a large software project, and sometimes it gets stuck repeatedly generating or executing shell commands without making any progress.

This happens across multiple models and providers, so I’m not sure whether it’s an OpenCode bug, a tool execution issue, or something in my setup.

Has anyone experienced this? What was the root cause, and what fixed it for you?

Any help would be appreciated!

**Comentarios:**

- **u/Amarsir** (↑1, 2026-10-21 06:41): Trace back to the first command in the loop, or the last before the loop. Did a tool call fail and that's why it's trying to find something that works? I find this is the case at least a fair amount of the time. So I address it by fixing what failed or adding instructions like "if this doesn't work as expected, stop and discuss with the user instead of finding a workaround."

---

## Is it me or Deepseek 4.1 is super slow? Its taking an absurd amount of time for a simple task. Should I change to another model?
**u/FutureLynx_** · 2026-10-21 05:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbenld/is_it_me_or_deepseek_41_is_super_slow_its_taking/)

Big Pickler and Muse 1.3 wasn't this slow.

---

## Is buy opencode go is more worth it than buy api from official website?
**u/Professional_Day4470** · 2026-10-21 05:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbeidn/is_buy_opencode_go_is_more_worth_it_than_buy_api/)

hello everyone, im new to open code and curious about this, should i buy the api from the official or just buy opencode go? Im gonna using deepseek flash for my main

---

## Do i download the CLI or desktop app
**u/AnOrdinaryCrayon725** · 2026-10-21 05:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbeat7/do_i_download_the_cli_or_desktop_app/)

I’m not sure what to use both look very good

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

---

## Is Deepseek 4.1 flash 1017 better than glm 5.3 flash?
**u/Upset_Disaster_1427** · 2026-10-21 02:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbbfkn/is_deepseek_41_flash_1017_better_than_glm_53_flash/)

---

## is there way deal with doom loops?
**u/qustrolabe** · 2026-10-21 02:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbb5f1/is_there_way_deal_with_doom_loops/)

https://i.redd.it/pztzd8zpcqwh1.png

also is there way to collapse thinking traces without scrolling all the way app, it's so annoying

---

## Came back to opencode. Was 🙂 now 🙁
**u/Melodic-Mud-1116** · 2026-10-21 02:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xbauzx/came_back_to_opencode_was_now/)

In the latest updated I don't know if it's. Me or what but I have been noticing it's running shell commands way too much and also the performance kind of seems bad is it only me or what. And any tips on it.

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

---

## Cursor to OpenCode Advice
**u/Prudent-Promotion512** · 2026-10-21 00:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1xb8mlo/cursor_to_opencode_advice/)

I just switched to OpenCode from Cursor and I have been impressed by many aspect of it and very excited to be free of the Cursor cache token tax but I have found my agents are using way more tokens in general.   

I think Cursor’s internal harness was helping to make my guidance more efficient but I can’t quite figure it out.  

Qualitatively the agents in OpenCode follow their guidance much more closely which I wanted but they are not as pragmatic and get bogged down in minor details more.

Anyone else experience this or have advice?

---
