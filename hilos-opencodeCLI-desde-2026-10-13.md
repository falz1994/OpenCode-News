# r/opencodeCLI — hilos 2026-10-13 → 2026-10-16
_Generado: 2026-10-15T02:49:00.137475+00:00 · 40 hilos · 195 comentarios · fuente: Arctic Shift_

## Thinking of subscribing BytePlus ModelArk Coding Plan
**u/nekohacker591-** · 2026-10-14 21:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x63ysk/thinking_of_subscribing_byteplus_modelark_coding/)

Just like the title stated, anyone has referee code? it should be cheaper using that right?

---

## Big pickle giving thinking as output
**u/ohhno_whyamihere** · 2026-10-14 15:29 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5ua76/big_pickle_giving_thinking_as_output/)

I have been using chatgpt plus auth and the mimo v2.6 flash ,muse spark 1.3 and step 5 preview free models ,for a small task i thought of using big pickle and i was suprised to see today it was showing the thinking as output instead ,anybody else having that??

---

## OpenCode connects to a new API. What should you test next?
**u/EmetInteractive** · 2026-10-14 14:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5t5a8/opencode_connects_to_a_new_api_what_should_you/)

Getting OpenCode to return its first response through a new API is a good start, but it doesn't tell you whether it can actually handle your usual coding tasks.  
  
I'd start with a small, disposable repository and three checks: ask it to explain a function, make a small change, and run an existing test. Keep the starting commit, client version, and model ID recorded so you can reproduce the run later. If you change several settings at once, debugging becomes much harder.  
  
It's also worth separating connection problems from actual coding failures. Did the request reach the endpoint? Did OpenCode parse the response and handle tool calls correctly? Did the resulting code pass the test? A successful HTTP response doesn't necessarily mean the whole workflow works.  
  
I'd also test cancellation and retries. Cancel a response, continue the session, and check whether completed tool actions get repeated or whether the client handles the conversation context correctly. Use a harmless task so an unexpected retry can't damage anything.  
  
For anyone evaluating hosted inference options, Mango Inference is one option worth testing. Its documentation covers OpenCode setup and an OpenAI-compatible Chat Completions interface. Just check the specific API requirements before switching, since compatibility with Chat Completions doesn't automatically mean support for embeddings or the OpenAI Responses API.  
  
My final step would be to record the model, starting commit, task, tool errors, test result, elapsed time, and billed usage. That gives you a fair baseline when comparing providers.  
  
What tends to break first when you switch API providers in OpenCode, tool calling, context handling, or something else?

---

## Opencode freetier stoped working with 9router
**u/MasonPak** · 2026-10-14 14:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5s16r/opencode_freetier_stoped_working_with_9router/)

Hey guys; does anyone else has issues with using 9router for opencode free tier? I faced the issue just now. Is there any way around it? Without the 9router, the free tier reaches the usage limit too soon.

---

## Decision Models in OpenCode GO?
**u/Mancho_United** · 2026-10-14 13:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5qpzr/decision_models_in_opencode_go/)

Does anyone know if there are any plans to have any of the decision models as part of the OpenCode GO subscription? There are many models already from different providers, and some of them we already use in opencode and we have their agentic models as part of the subscription.

Some examples of popular decision models:  
  
typesafe/jev-1.13

microsoft/microsoft-decision-1

nace-ai/drex-v2.0 (and also drex-v1.5)

openai/gpt-6-luna-decisions

cloudflare/clef (also clef-omni, clef-flash)

perplexity/pplx-decider-v1.1-27b

liquid/d1

**Comentarios:**

- **u/Diligent-Loss-5460** (↑1, 2026-10-14 13:23): jev free is available on zen
  - **u/Mancho_United** (↑1, 2026-10-14 14:53): Yes, but I assume for a limited time and with rate limiting. Would be great to be part of the GO plan usage.

---

## I Ran the Horse Test on Every Free AI Model on OpenCode
**u/ItsHarvcker** · 2026-10-14 13:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5qomw/i_ran_the_horse_test_on_every_free_ai_model_on/)

---

## I'm bothered by the recent change to directory permissions and lack of transparent communication.
**u/thatboyonabike** · 2026-10-14 10:10 UTC · ↑22 · 8 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5neba/im_bothered_by_the_recent_change_to_directory/)

I wrote up this post to bring awareness to a recent change I took issue with and think should be discussed by the community.

**The facts:**

As of OpenCode v2.0.25 the default behaviour is to no longer prompt for access to external directories.

From [Pull Request #53585](https://github.com/anomalyco/opencode/pull/53585):

> What does this PR do?
>
> Removes the external_directory: * → ask rule from the default > agent ruleset in Agent.Info.default. The catch-all * → allow now > covers paths outside the project too, so build/general/custom 
> agents no longer prompt before touching them.
> 
> Explore also stops asking: it keeps its deny-by-default tool list > but now explicitly allows external_directory.

How this change was communicated:

1. Not communicated through the [github releases page](https://github.com/anomalyco/opencode/releases/) which still tracks v1, not v2.
2. Not communicated through the [changelog on the official website](https://opencode.ai/changelog) as it only started tracking releases from 2.0.26 onward.
3. Communicated by reading [commit 36a3805](https://github.com/anomalyco/opencode/commit/36a38058fb6178aab2ed4d13216b3260de9cf6b2) directly.



There are already multiple issues referencing this change:

- [#54524](https://github.com/anomalyco/opencode/issues/54524)
- [#54632](https://github.com/anomalyco/opencode/issues/54632)
- [#55070](https://github.com/anomalyco/opencode/issues/55070)
- [#55207](https://github.com/anomalyco/opencode/issues/55207)

**My opinion:**

 This a major change to a security boundary that should have been:

A) Purely opt-in.

and

B) Communicated loudly and directly to all users.

The lack of communication is downright suspicious but I have enough goodwill towards the OpenCode team to just assume this is a maintenance oversight. 

I'm aware that best practice is usually to run your agents in some kind of container, but I'm willing to bet a large portion of users are _not_ doing that, and should have been rightfully informed of the impact this could have on their security.

I've promoted OpenCode to many people in the past and this feels like it's impacted my own credibility. I'm not necessarily abandoning it, but I am going to be more reserved in my recommendation. I think it's also time I take another look at the current landscape of harnesses.


What are everyone else's thoughts?

**Comentarios:**

- **u/tsangberg** (↑6, 2026-10-14 10:50): >I'm aware that best practice is usually to run your agents in some kind of container, but I'm willing to bet a large portion of users are *not* doing that
    
    I agree that it should've been communicated, but I think the right thing to do is to remove all the pretense that these "please don't" rules work. It's better to just tell people that if they're running the harness without actual sandboxing they are indeed risking the LLM doing something it shouldn't.
  - **u/thatboyonabike** (↑1, 2026-10-14 11:11): I do agree, but I think that's a larger issue that even the bigger players are guilty of, so I didn't want to sound like I was picking on OpenCode for it.
    - **u/Diligent-Loss-5460** (↑2, 2026-10-14 12:57): I think its worth mentioning in the changelog since it is a behavior change but anomaly has been doing an awful job at maintaining their repo so it might be too much to ask
- **u/crasspuk** (↑2, 2026-10-14 11:22): The communication complaint is fair. A change to which directories need approval is a security default, so it belongs in the release notes, not only in a commit. Opt-in is the safer default, and the linked issues show others hit the same change.
  - **u/thatboyonabike** (↑1, 2026-10-14 11:31): Begone bot.
- **u/ozguru** (↑2, 2026-10-14 13:23): I guess this is to reduce friction for users. similar to codex. I believe they kept related config field.
- **u/geearf** (↑2, 2026-10-14 17:11): I opened a post about this: [https://www.reddit.com/r/opencode/comments/1x4kkmr/security\_opencode\_does\_not\_ask\_for\_file/](https://www.reddit.com/r/opencode/comments/1x4kkmr/security_opencode_does_not_ask_for_file/)
- **u/rilosk** (↑1, 2026-10-14 19:19): I switched off the platform. I feel like theyve been slacking on the communication  side of things and a lot of changes they are making just aren't great. Too busy on twitter i guess

---

## Comparing OpenCode Go vs OpenDesign Go (vs Command Code GOAT too for good measure)
**u/misaalanshori** · 2026-10-14 09:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5mppv/comparing_opencode_go_vs_opendesign_go_vs_command/)

Anyone used these alternatives to OpenCode Go? AFAIK all these provides full API access and doesnt lock you down to a specific agent software.

I am currently looking at OpenDesign Go plan (https://open-design.ai/pricing/) which is SUPER TEMPTING because it is $7/mo for similar limits to OpenCode Go, but that requires a 1 year commitment (pay for annual). Their monthly plan is at $8 for first month and $10 after that... 

I've literally only heard of OpenDesign like yesterday, and so I don't yet have full trust on Open Design for the long term... Like will Open Design even still be around in a year? Will OpenDesign still be competitive with other AI subscriptions? etc

Can someone maybe either convince me more or talk me out of this? lol

Also about Command Code, which I think is a lot more established, but is basically the same pricing as OpenCode Go. Looking at their limits I think I prefer OpenCode Go rather than Command Code GOAT. But honestly all I'm thinking of right now is this OpenDesign Go lol, I don't think they mention how long this promo is going to run for, so my FOMO brain is going wild 😭

---

## Anyone running custom subagents in OpenCode for non-web / C++ / embedded stacks?
**u/eh_see_l** · 2026-10-14 09:15 UTC · ↑1 · 1 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5mj12/anyone_running_custom_subagents_in_opencode_for/)

**Comentarios:**

- **u/crasspuk** (↑2, 2026-10-14 10:58): Keep each subagent narrow, with one job and a description that says when to call it. For C, C++ and embedded work, put the build, test and flash commands and the hardware limits in the project's AGENTS.md, so every agent sees them. Generic web-dev prompts usually miss exactly those details.

---

## I built a quota sidebar for OpenCode V2 with remaining usage, reset timers, and credits
**u/SkanePrime** · 2026-10-14 07:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5lbk4/i_built_a_quota_sidebar_for_opencode_v2_with/)

---

## Gemini 4 Argon is now in OpenCode Go 🔥
**u/afanasenka** · 2026-10-14 07:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5l557/gemini_4_argon_is_now_in_opencode_go/)

...

**Comentarios:**

- **u/Odd_Teacher_4089** (↑7, 2026-10-14 07:46): ![gif](giphy|fDbzXb6Cv5L56)
- **u/kubblegum** (↑2, 2026-10-14 07:47): insane
- **u/BrownCarter** (↑6, 2026-10-14 07:49): Is it better thank cheapseek?
  - **u/Embarrassed-Salt6590** (↑2, 2026-10-14 07:59): Not that much noticable unless maybe u want to hype vibe
  - **u/ComeOnIWantUsername** (↑2, 2026-10-14 07:59): a lot better
  - **u/Amarsir** (↑5, 2026-10-14 08:06): In terms of intelligence, definitely. But you also get like 1% as much use because the API price is so much more expensive.
    - **u/AlexandraMaryWindsor** (↑1, 2026-10-14 08:18): Intelligence does not matter if it actively seeks to do the least amount of work as possible.
        Cheap Chinese models have a better work ethic and are more reliable, I cannot trust it's output, too much wrong things have happend.
      - **u/New_Comfortable7240** (↑1, 2026-10-14 10:58): What do you think of the workflow
          
          - plan with intelligent model in max of xhigh
          - work with cheap Chinese workhorse 
          - verify with intelligent model in medium or high
        - **u/RespectJaded15** (↑1, 2026-10-14 12:38): I think medium is good enough for intelligent model. I use opus 5.5 medium with DeepSeek/muse model.
- **u/alphasubstance** (↑41, 2026-10-14 07:52): Available in opencode-go before available in antigravity for pro users.
  - **u/l0rirw1ao** (↑1, 2026-10-14 08:48): Truly a Google fell off moment and its not even that good form what I read about it.
  - **u/Pinery01** (↑1, 2026-10-14 09:02): oh.. yeah, available for people who paid $10, not for who paid $20 lol
  - **u/Bloated_Plaid** (↑1, 2026-10-14 10:35): Make it make sense lol.
  - **u/jbig3low** (↑1, 2026-10-14 15:27): yah this makes no sense, why does google do such dumb stuff you would think they have some smart people employed.
- **u/hacker_backup** (↑4, 2026-10-14 07:56): How is it so cheap?
  - **u/WishboneOk305** (↑1, 2026-10-14 08:17): because its fucking expensive to use. You can easily get 10x more done on deepseek or whatever
- **u/Amarsir** (↑3, 2026-10-14 08:03): Bear in mind that the API price is $4/$20. That means even with the $60 usage they estimate 440 prompts.  Without the 4x it would be the same as Kimi K3.
  - **u/subhashg547** (↑1, 2026-10-14 08:28): isn't introductory pricing 2/10 usd?
    - **u/Amarsir** (↑1, 2026-10-14 08:31): Not here:
        
        [https://opencode.ai/v2/docs/console/go/#usage-limits](https://opencode.ai/v2/docs/console/go/#usage-limits)
        
        Other source might have cheaper API introductory prices. But it seems OpenCode went "full price, better multiplier" rather than a cheaper API price on $15 or $30.
      - **u/migsperez** (↑1, 2026-10-14 10:12): And it's a contributor
  - **u/Embarrassed_OnionX** (↑1, 2026-10-14 15:35): Smartest? It's benchmaxxed af
- **u/crusaderky** (↑1, 2026-10-14 08:24): oh wow, $60 will last three whole prompts
  - **u/Financial_Bug2389** (↑1, 2026-10-14 10:27): Depends on how you use it. Maybe one.
- **u/nomadArch** (↑1, 2026-10-14 10:57): Google still makes models?
- **u/KayBay80** (↑1, 2026-10-14 11:31): Nobody's going to care at all about Argon in a week anyways.
  - **u/ahmetegesel** (↑1, 2026-10-14 13:01): Sad but true. All the hype, slow roll-out plan and awesome looking benchmarks, but the pace in the frontier race and the tension the Chinese models cause with cheaper options will make all this effort pointless. They need to get faster with their flagship releases. 
      
      TBH I will always be more hyped up with small but capable models’ releases.
    - **u/KayBay80** (↑1, 2026-10-14 13:22): We broke down and got Ultra just to test this (well, one of our teammates did) and while its an upgrade over flash, it still has the same quirks. One of which is unforgivable: It doesn't actually do the job and says that it does, fabricates things it SHOULD have done but didnt, and straight up lies about ideas that we have being good (when they are actually really bad).
        
        Google isn't going to catch the frontier at this point. We trust Qwen and DS over Argon any day of the week based on just less than one day of working with it.
    - **u/Stock-Self-4028** (↑1, 2026-10-14 13:27): Argon is still currently the SOTA in 'creative writing' (whatever it means in practice) and is significantly less expensive, than Fable so I guess it'll remain wiable at least for that for quite some time.
        
        I guess it'll remain one of the best models for things like pre-reviewing drafts of scientific papers etc for a few months. But yeah, it's definitely not a great coding model.
- **u/Fresh_Sock8660** (↑1, 2026-10-14 12:25): Meh. Will stick to opus 5.5 slavedriving ds4.1f thanks google moneybags.
- **u/uncondensed** (↑1, 2026-10-14 12:51): Isn't this for the Contributor model where using it gives them permission to train on your data?
- **u/Dluugi** (↑1, 2026-10-14 14:53): it's not Gemini 4 Argon tho. It's Gemini 4 Argon contributor.
    
    Your data is explicitly used for model training
  - **u/Dluugi** (↑1, 2026-10-14 15:00): fuck that sounded like AI wrote it
    - **u/retardedGeek** (↑1, 2026-10-14 15:13): It's just 2 sentences, chill

---

## Local Nvidea Sparks DGX Desktop - Ollama or vLlm
**u/Sufficient_Wait4290** · 2026-10-14 05:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5jaol/local_nvidea_sparks_dgx_desktop_ollama_or_vllm/)

I run OpenCode against the Spark with its 128gb unified memory. Works fine.

Since OpenCode makes parallel calls, but Ollama only executes them sequentially, I would gain performance if I switch to vLlm.

However, my opencode model and the model my coded applications use is far over 128gb.

Possible I can use some  new sleep/wake-up API on the vLlm if I put one model on one port. I'm going to try this.

Does anyone have the same setup and want to share some tips?

What is the best vLlm model for openCode?

**Comentarios:**

- **u/arcanemachined** (↑2, 2026-10-14 07:07): Not Ollama
- **u/crasspuk** (↑1, 2026-10-14 08:50): Ollama handles one request at a time per model by default. OLLAMA_NUM_PARALLEL sets how many run at once (default 1). The memory needed scales with that number times the context length, so on 128GB you may need to cap the context to make room. On Linux, run systemctl edit ollama.service, add Environment=OLLAMA_NUM_PARALLEL=4 under [Service], then run systemctl daemon-reload and systemctl restart ollama. So the sequential behaviour you saw is the default, not a hard limit.

---

## What ? Is opencode seves this model only ?
**u/Successful_Night4513** · 2026-10-14 03:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5hcx0/what_is_opencode_seves_this_model_only/)

**Comentarios:**

- **u/masterofall20** (↑12, 2026-10-14 04:58): You had to type ONE sentence.
  - **u/Successful_Night4513** (↑-9, 2026-10-14 05:16): You get the context then why it's needed ?
    - **u/masterofall20** (↑6, 2026-10-14 05:18): I got zero context.
    - **u/laser50** (↑1, 2026-10-14 11:51): Bro there ain't no way I am translating hieroglyphics first.. Can't you use the seves model only to write proper sentence?
- **u/Dizzy-Truck-1780** (↑6, 2026-10-14 05:24): What did you type? I genuinely don't understand.
- **u/HyperWinX** (↑2, 2026-10-14 05:45): ...huh?
- **u/Aggressive-Habit-698** (↑0, 2026-10-14 05:57): Lol, the author of the post just posted a screenshot of a website and got 11 upvotes. 
    That doesn't look like opencode.ai
  - **u/subhashg547** (↑2, 2026-10-14 06:20): it is opencode's official website actually
    - **u/Aggressive-Habit-698** (↑2, 2026-10-14 07:16): link ?
      - **u/Aggressive-Habit-698** (↑0, 2026-10-14 07:18): [https://opencode.ai/data/deepseek](https://opencode.ai/data/deepseek)

---

## Gemini 4 Argon High vs. SWE-2 (literately Kimi-K3) - On regression hunts, spec gaps, downstream failure.  Blasting out reviews of 14 independent reviewers representing  2 teams of 7 each.
**u/ZealousidealTown1974** · 2026-10-14 03:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5h0dm/gemini_4_argon_high_vs_swe2_literately_kimik3_on/)

They’re tracing user journeys through specs, code, tests, and downstream failure paths—not merely reviewing documentation. A fresh root test/typecheck run is also underway.

Blasting out reviews of 14 independent reviewers representing  2 teams of 7 each. Each gets a separate report file; none may edit product code. I’ll also capture one fresh test/typecheck run. Source evidence, test results, and observed TUI behavior will stay clearly separated.

Then having OpenAI GPT 6.1 Sol - xHigh  reasoning level as a judge and this is the result

  
\## Verdict: \*\*Devin is the more trustworthy lead reviewer.\*\*  
  
\*Scores judge this audit—not model capability generally.\*  
  
| Team | Score | Verdict |  
|---|---:|---|  
| \*\*Devin\*\* | \*\*7/10\*\* | Better evidence and causal reasoning. Produced a real malformed-permission reproduction. Lost points for missed integration gaps and overconfident “complete” verdicts. |  
| \*\*Antigravity\*\* | \*\*5/10\*\* | Better at spotting neglected gaps: hosted-policy setup, consent, phantom documented tools, scanner weaknesses. But several reports fabricated test/history details or cited incorrect source facts. \*\*Not trustworthy for sign-off without verification.\*\* |  
  
\*\*Best combination:\*\* Antigravity hunts gaps; Devin reproduces them; the coordinator validates both. Never approve by agreement alone.  
  
\### Project verdict: \*\*REQUEST CHANGES\*\*  
The \*\*1,165 passing tests and passing typecheck\*\* coexist with confirmed defects and incomplete promised workflows. Full runtime/UAT acceptance remains pending.  
  
\[Detailed scoring and rationale\](.audit/2026-10-14-project-e2e-audit/model-assessment.md) · \[Validated and rejected findings\](.audit/2026-10-14-project-e2e-audit/reconciliation.md)  


https://preview.redd.it/4rwnfsdqrcvh1.png?width=3024&format=png&auto=webp&s=db24cc15eab66096755190368f114a7a995926f4

https://preview.redd.it/ehkdfodqrcvh1.png?width=3024&format=png&auto=webp&s=678c081d843dad7d7a2d10cbe8bae861a593fc08

https://preview.redd.it/y3mg8ndqrcvh1.png?width=3024&format=png&auto=webp&s=79c1b643488cd14339d1a4e0debd1f674e1c0e97

https://preview.redd.it/po9ugndqrcvh1.png?width=3024&format=png&auto=webp&s=bc1d5cf2242fcedebd8e1b59dab291c3ea229a4f

---

## Built a small OpenCode v2 plugin to avoid DeepSeek peak pricing
**u/Square_Confection_62** · 2026-10-14 03:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5grtz/built_a_small_opencode_v2_plugin_to_avoid/)

I use OpenCode Go + DeepSeek and got tired of checking whether I was inside the 2x peak-pricing window.

So I made **opencode-offpeak**.

Turn it on once, then use OpenCode normally:

* send a prompt off-peak → it runs immediately
* send a prompt during peak → it waits before hitting the provider
* off-peak starts → the same request continues automatically in the same OpenCode session

No need to resend `continue` or watch the clock.

It also has an optional background task queue, but normal interactive sessions already work automatically.

Install:

    opencode plugin add git+https://github.com/lutzkind/opencode-offpeak.git#v0.1.3

[https://github.com/lutzkind/opencode-offpeak](https://github.com/lutzkind/opencode-offpeak)

Open source / MIT. Currently supports OpenCode Go DeepSeek models on OpenCode `>=2.0.26 <2.1.0`.

Would be interested in feedback or other providers with similar time-based pricing.

---

## I built a desktop and phone app for OpenCode v2 that runs your sessions on a cloud machine
**u/DishRadiant1937** · 2026-10-14 02:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5fqhe/i_built_a_desktop_and_phone_app_for_opencode_v2/)

Otto starts `opencode serve` on Boat, boxd, E2B or Daytona, or connects to a server you already run. The app covers sessions, permissions, agents, MCP, skills, commands and schedules. Permission prompts come to your phone, so you can approve a `git push` away from your desk.

It'll also run OpenCode on your own machine, no cloud machine or key required.

MIT: [https://github.com/jaygupta17/otto](https://github.com/jaygupta17/otto)   
Mac install: curl -fsSL [https://jaygupta.dev/otto/install.sh](https://jaygupta.dev/otto/install.sh) | sh

How do you all run OpenCode headless?

---

## The horsy prompt with Gemini Argon 4 - Running on OpenCode TUI V2 - via Antigravity harness (ACP lane)
**u/ZealousidealTown1974** · 2026-10-13 20:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5863s/the_horsy_prompt_with_gemini_argon_4_running_on/)

---

## Argon 4 on OpenCode  is awesome  - Gemini, the king has returned and it outsmarts OpenAI GPT 6.1 Sol on high
**u/ZealousidealTown1974** · 2026-10-13 19:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x56gpn/argon_4_on_opencode_is_awesome_gemini_the_king/)

still testing seeing what it is capable of

**Comentarios:**

- **u/ZealousidealTown1974** (↑16, 2026-10-13 19:54): well, withdraw on what I said - it sucks with tool using even on its own Antigravity harness
    
    https://preview.redd.it/q6p7urwuhavh1.png?width=3024&format=png&auto=webp&s=d2295ec0f270e0daf25d3064010fffcb0aea7d9a
  - **u/alovoids** (↑3, 2026-10-14 03:22): yeah and expensive 🤣
  - **u/GoldPossession7284** (↑1, 2026-10-14 04:25): cara primeiro que pode ser essa tua gambiarra que você fez ai do antigravity, segundo estou usando direto da vertex. não obtive nenhum problema até agora. segunda tarefa que passo pra ele e está executando perfeitamente, porém realmente é caro pra krl
- **u/migsperez** (↑1, 2026-10-13 20:00): Can you try the horse prompt test, please https://www.reddit.com/r/opencode/s/vkVCQgDvMt
  - **u/ZealousidealTown1974** (↑2, 2026-10-13 20:45): yes posted it! unfortunately it sucks 
      
      ![gif](giphy|Jq7WUBf71Gju1vTe2A)
    - **u/migsperez** (↑1, 2026-10-14 01:15): Damn I was hoping it would reach Opus level
- **u/Fresh_Sock8660** (↑1, 2026-10-14 12:40): That's the thing with new models. I can never tell anymore whether something is hype or good testing. Only after extensive usage do I somewhat draw conclusions about models now.

---

## Gemini 4 Argon now available in OpenCode 🔥
**u/afanasenka** · 2026-10-13 18:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x54ynu/gemini_4_argon_now_available_in_opencode/)

**Comentarios:**

- **u/biograf_** (↑8, 2026-10-13 18:49): Never even heard of it...
  - **u/torrso** (↑1, 2026-10-14 05:44): Then you haven't been following.
  - **u/Chemical_Union226** (↑1, 2026-10-14 07:43): you didn't miss anything
- **u/AccomplishedFail9857** (↑16, 2026-10-13 18:54): Is it April 1st?
- **u/xatey93152** (↑23, 2026-10-13 19:24): Wrapper of qwen 3.8
- **u/MedAyoub26K** (↑13, 2026-10-13 19:26): "Second most used model"
- **u/Ariquitaun** (↑3, 2026-10-13 19:40): Can't see it on the docs page yet, anybody know the relative cost?
  - **u/lewwdsv1** (↑5, 2026-10-13 20:15): Input/Output/Cache
      $2.00	$10.00	$0.10
    - **u/deleted-account69420** (↑2, 2026-10-13 22:42): That's for the contributor model.
  - **u/frostybito** (↑4, 2026-10-13 20:16): Gemini 4 Argon official pricing through November 30, 2026: input $2, output $10 /1M tokens (input $0.1 cached); pricing starting December 1, 2026: input $4, output $20 /1M tokens (input $0.2 cached)  
      (\* Promotional pricing provided through 50% credits back on net spend on select models within a given period.)
- **u/horrbort** (↑0, 2026-10-13 21:50): FP2 i hope
- **u/Warm-Chipmunk-5636** (↑3, 2026-10-14 01:06): What kinda fumble is the second line lol 😆
- **u/Thundechile** (↑3, 2026-10-14 03:38): "The second we started testing this model heavily it became temporarily the second most used model in our team".

---

## Codex + GPT-6.1 SOL medium vs DeepSeek Harness + 4.1 Flash — which one actually wins on price/performance?
**u/yxf2y** · 2026-10-13 18:29 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x54ne6/codex_gpt61_sol_medium_vs_deepseek_harness_41/)

I've been using Codex with a ChatGPT Plus subscription for a while, mostly GPT-6.1 sol on medium for everyday stuff. Lately I've been thinking about trying DeepSeek Harness with 4.1 Flash on high for similar tasks, and I'm trying to figure out which setup actually makes more sense cost-wise.

Here's what a typical task looks like on my end (Codex + GPT-6.1 sol medium):

* 4 turns, 75 steps, around 5.6M tokens total
* 98% cache hit rate
* Breakdown: 5.44M cached input, 94K uncached input, 65K output

On the DeepSeek side, off-peak pricing for 4.1 Flash looks like this:

* Cached input: $0.003 / 1M
* Uncached input: $0.15 / 1M
* Output: $0.60 / 1M

Off-peak hours for me are roughly 13:00–04:00 on weekdays, plus weekends and Chinese public holidays entirely.

Rough math for the same token set:

* GPT-6.1  Sol API pricing: \~$2.00
* DeepSeek 4.1 Flash off-peak: \~$0.07
* So DeepSeek comes out roughly 16–20x cheaper

What I'm actually wondering:

1. Is this comparison realistic, or am I missing something? Specifically, how far does the "5-hour usage window" on ChatGPT Plus actually stretch with token-heavy agentic tasks like these?
2. How do DeepSeek Harness's agentic capabilities stack up against Codex + GPT-6.1? I'm particularly curious about tool use, MCP integration, and multi-step tasks — I run Serena and codebase-memory-mcp alongside it.
3. Long term, does it make more sense to keep ChatGPT Plus and use DeepSeek API on the side, or just go all-in on DeepSeek?
4. Does the 98% cache hit rate hold up in practice, or does it drop once you're doing varied work and the cost advantage disappears?

Would love to hear from anyone who's actually run both setups. Real-world experience with the subscription-vs-API tradeoff would be especially useful.

**Comentarios:**

- **u/Aldarund** (↑3, 2026-10-13 18:36): Deepseek use waaaaay more tokens than gpt 6.1
- **u/TestTxt** (↑5, 2026-10-13 18:41): Taking API prices for Codex doesn’t make any sense at all since the codex subs are heavily subsidized. On top of that Deepseek uses way more tokens, so in practice ChatGPT is not that expensive at all. Deepseek offers no official coding plans
  - **u/yxf2y** (↑2, 2026-10-13 18:46): Fair, you're right. Comparing Codex sub to DeepSeek API prices was a bad framing on my part. But the token thing is the real issue. My 5.6M number is from GPT-6.1. No idea what DeepSeek burns on the same task, and if it's 2-3x more then the whole "way cheaper" argument falls apart. So the real question is: if you're already on ChatGPT Plus, is there any actual reason to add DeepSeek on top? Or is it just cheaper for people who don't want a sub at all? What's your setup?
    - **u/TestTxt** (↑1, 2026-10-13 18:50): It’s good for some tasks like reverse engineering etc. which ChatGPT refuses to do
    - **u/EvolvingDior** (↑2, 2026-10-14 03:01): Deepseek-v4.1-flash is about as capable as Luna, but with a better personality. It also costs about the same per task. Sol is more capable. But few people need Sol for agentic work.
- **u/IndividualPlus2011** (↑2, 2026-10-13 18:50): You can take a look at my table and make the decision for yourself [https://www.reddit.com/r/codex/s/M1fBQXH6vU](https://www.reddit.com/r/codex/s/M1fBQXH6vU)
    
      
    You have to take into account that DeepSeek will use several times more tokens for the same task, and the quality will be worse.
    
    TLDR. Cut the 6.1 Sol cost by 10 and assume that DeepSeek will use at least twice the tokens, but sometimes even up to 10x (typically 5+ for my use cases)
  - **u/yxf2y** (↑1, 2026-10-13 19:48): Okay this table is actually useful, thanks. So GPT-6.1 Sol runs about $200/mo in API terms against a $20 sub — that's the 10x ratio. Even if I cut that by 10 and land at DeepSeek's \~$0.07/task, the 5x token multiplier brings it right back up. And that's before the quality gap. So yeah, the "16x cheaper" thing I posted was way off. Appreciate the reality check.
- **u/crasspuk** (↑1, 2026-10-14 10:36): Comparing ChatGPT Plus to API list prices does not tell you much, since the sub is not billed per token. The bigger variable is tokens per finished task, which differs a lot between models. Run the same task on both and compare cost per completed task.
- **u/[deleted]** (↑1, 2026-10-14 11:51): [removed]

---

## I built TermPlete: open-source terminal autocomplete that learns your choices and uses recent terminal context
**u/CollarActive** · 2026-10-13 18:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x54dnl/i_built_termplete_opensource_terminal/)

Hey everyone — I’ve released **TermPlete v0.1.0**, an open-source autocomplete tool for your existing terminal.

It combines command history, the suggestions you accept, recent terminal context, and a model you choose. You can browse command options, insert one, edit it, and decide when to execute it.

Repo and demo: [https://github.com/aft1n/termplete](https://github.com/aft1n/termplete)

# What it does

* **Learns your preferences.** Accepted suggestions influence future rankings alongside recency and frequency. Fresh choices with a clear lead can become local answers without a model request.
* **Reuses your command history.** Finds familiar commands, arguments, and SSH targets instead of making you reconstruct them.
* **Uses recent terminal context.** Suggestions can incorporate recent commands, bounded captured output, exit status, and visible directory entries.
* **Turns task descriptions into command options.** In zsh, type something like `# convert dog.mp4 to` [`dog.mov`](http://dog.mov) `with ffmpeg` and press Enter to request suggestions.
* **Completes real directories.** `cd` suggestions are checked against existing folders.
* **Lets you browse alternatives.** Use Tab/Shift+Tab to move through suggestions. Browsing an already-returned batch doesn’t trigger additional AI requests.
* **Supports partial acceptance in zsh.** Accept the next suggested word, then change the remaining arguments yourself.
* **Offers automatic and on-demand modes.** Suggestions can appear while you type, or wait until you ask.

https://reddit.com/link/1x54dnl/video/cm1oibdj0avh1/player

# Choose your model setup

TermPlete supports hosted providers, Ollama, LM Studio, and custom OpenAI-compatible endpoints. It also supports ChatGPT subscription authentication through Codex.

Local history suggestions don’t require an API key or a running model.

There’s an optional decision helper that can rank existing command candidates and check whether generation is permitted. You can use it separately from the model that generates commands.

# Control and privacy

Accepting a suggestion **only inserts it**. It never automatically executes the command.

You can pause and resume TermPlete with:

    tp stop
    tp start

There are controls for captured context, private-path exclusions, and recognized-secret redaction. API keys use the platform credential store, and local-only requests skip the model backends.

You can also disable integration in selected terminal applications.

# Compatibility and installation

The full interactive experience is available in **zsh 5.9+ on macOS and Linux**. Bash integration provides Tab completion and suggestion preview on supported versions; older Bash versions have more limited functionality.

Installation is available through the GitHub release installer and a Homebrew tap. The README includes installation instructions and a demo.

It’s written in **Rust** and released under the **MIT license**. The installer, shell integrations, and suggestion logic are all in the repository.

Tools such as zsh-autosuggestions, fish, and Atuin already cover useful parts of terminal completion and history. TermPlete’s focus is combining accepted-choice learning, recent terminal context, and configurable generation inside an existing shell.

This is an early release, and I’d appreciate feedback—especially on suggestion quality, shell compatibility, and keyboard behavior.

**What command do you repeatedly search for, and what would make an autocomplete suggestion useful enough for you to accept?**

**Comentarios:**

- **u/Puzzleheaded_Bug_697** (↑2, 2026-10-13 19:04): https://preview.redd.it/l8w20r8u8avh1.jpeg?width=900&format=pjpg&auto=webp&s=8d82b80a2eca0773d930be4829fa92da351ffdfb
  - **u/CollarActive** (↑2, 2026-10-13 19:41): Haha... autocompletes were long before ai mate ))

---

## Cat Jam now available
**u/jpcaparas** · 2026-10-13 18:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x53xxb/cat_jam_now_available/)

**Comentarios:**

- **u/MrMrsPotts** (↑2, 2026-10-13 20:46): Is it any good?
  - **u/Bloated_Plaid** (↑9, 2026-10-13 21:51): No.
- **u/look** (↑2, 2026-10-14 02:05): My guess is a new Laguna from Poolside.
    
    It is definitely not a Chinese lab, and I doubt it is from one of the big US/EU labs (most don’t do stealth models like this). So one of the smaller/newer western labs and Poolside seems like the best fit.

---

## [Humor] Usage Limits Too Low?
**u/Heretek-ai** · 2026-10-13 17:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x534yo/humor_usage_limits_too_low/)

https://preview.redd.it/3exyyxeks9vh1.png?width=2653&format=png&auto=webp&s=311456f7eec25d06a1bbf04d84f3e696ba1d3657

How do I have 10 days left on my subsciption but no credits left??? Is claude or codex a better deal????

**Comentarios:**

- **u/squirrelscrush** (↑1, 2026-10-13 20:27): Which models you used?
  - **u/look** (↑1, 2026-10-13 21:39): 10B tokens with $60 value… looks like a lot of Deepseek on the $10 plan.
  - **u/Heretek-ai** (↑1, 2026-10-13 22:02): Muse 1.3 contributor
    - **u/squirrelscrush** (↑1, 2026-10-14 08:02): My guy was probably coding 24/7 lol
- **u/look** (↑2, 2026-10-13 21:43): I don’t think even the Claude/Codex subs aren’t going to beat 10B tokens for $10. That’s $0.001/Mtok.
    
    Maybe if you only use Haiku/Luna… but it’s not going to be much more per dollar than that.

---

## Cat Jam (stealth) is now FREE in OpenCode 🔥
**u/afanasenka** · 2026-10-13 17:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x52qw4/cat_jam_stealth_is_now_free_in_opencode/)

**Comentarios:**

- **u/bew78** (↑4, 2026-10-13 17:23): What's a "stealth" model?
  - **u/Ammoun442** (↑17, 2026-10-13 17:27): Its when the company trying to test a model but dont wanna say its name , for exmple this model can be gemini 4 flash or glm flash  
      I know i didnt explain well but hope that helps
    - **u/danjack0** (↑1, 2026-10-13 17:30): Google never stealth
      - **u/Ammoun442** (↑1, 2026-10-13 17:37): Yea just an example
        - **u/kankerstokjes** (↑1, 2026-10-13 17:38): I think this one is a new Mimo model. It's not bad.
          - **u/Ammoun442** (↑3, 2026-10-13 17:46): didnt they drop 2.6 recently
            - **u/Strong_Essay1176** (↑0, 2026-10-14 02:24): If you cant release 1 model per month, you are out. 
                
                **unless you are Google, google can announce 1 model per month.
      - **u/someoneyouknow23** (↑9, 2026-10-13 18:27): not true? nano banana was literally a stealth model, the name just stuck
  - **u/Info-NoInfo** (↑4, 2026-10-13 17:28): When the provider chooses to keep itself hidden, so the market does not yet know who the publisher is. Hence 'stealth'. This is mainly because they want to know how the public reacts to the model, what people do with the model, and to do a little post training to make it a little bit better before a public release.
  - **u/No_Communication4256** (↑2, 2026-10-13 21:55): It's openrouter (not an opencode one) notation for secret free models
- **u/Aldarund** (↑2, 2026-10-13 17:32): Some version of mimo
- **u/[deleted]** (↑1, 2026-10-13 17:34): [removed]
- **u/unsatisfied_guy1** (↑4, 2026-10-13 17:41): better than v4.1?
  - **u/popiazaza** (↑22, 2026-10-13 17:48): worse than v4
- **u/thatscoolbutno123** (↑2, 2026-10-13 17:47): DS v4.1 pro?
  - **u/lewwdsv1** (↑4, 2026-10-13 18:21): Nah. Doesn't feel like DS at all.
- **u/-PROSTHETiCS** (↑4, 2026-10-13 18:06): 262k context whatapak!?
- **u/Stunning_Pair_3027** (↑12, 2026-10-13 18:14): My recommendation is do not ever use it in build mode.
  - **u/eachDayIWakeUp** (↑3, 2026-10-13 20:11): can confirm its tricky to even monitor what its doing. Its so fast you cant read the garbage commands its running :P
  - **u/No_Communication4256** (↑11, 2026-10-13 21:54): https://i.redd.it/3qrhjda83bvh1.gif
      
      Pelican (xenomorph actually) ride bike
- **u/HotDoshirak** (↑3, 2026-10-13 18:22): ![gif](giphy|8ln4T2ZAsxFp0DzbGD)
- **u/[deleted]** (↑1, 2026-10-13 19:17): [removed]
- **u/frostybito** (↑7, 2026-10-13 20:02): this time no mention "no data retention" ? so very fast free data harvest from gullible users\*?
- **u/look** (↑10, 2026-10-13 21:20): It is from a US or EU lab. It is not Chinese. 
    
    It will readily discuss Tiananmen Square massacre, Uyghur genocide, human rights and cultural destruction of Tibet, and so on.
  - **u/the_last_code_bender** (↑-5, 2026-10-13 23:18): EU and US never did bad things ig
    - **u/SpaceEnthusiast3** (↑2, 2026-10-13 23:35): i mean they do but ur allowed to talk about it
      - **u/Spitfire1900** (↑2, 2026-10-14 00:35): I don’t have a good prompt to test US model censorship.
        - **u/Hawful** (↑1, 2026-10-14 14:04): Questions about Israel. Here's my specific ask: "Is Israel committing a genocide? Answer with yes or no. Base it on the definition of genocide and the actions of Israel, including statements made by their prime minister and the minister of defense. Do not make this judgement based on the outcome of an ICJ case."
            
            Every US model will fence sit, but Kimi K3 will just say yes.
          - **u/look** (↑1, 2026-10-14 15:29): Good idea. I’ll use that, too, for testing future stealth models.
    - **u/look** (↑2, 2026-10-14 04:21): I wasn’t making a political statement. It’s the first question in a game of 20 questions. The LLM equivalent of “is it bigger than a breadbox?”
        
        It’s the same way we knew Ox Alpha was a Chinese model right away, because it would just abort the response halfway through the first sentence.
  - **u/ComeOnIWantUsername** (↑1, 2026-10-14 14:04): \> It will readily discuss Tiananmen Square massacre, Uyghur genocide, human rights abuses and cultural destruction of Tibet, and so on.
      
      All these Chinese models are happy to discuss it at first. Censorship comes later
    - **u/look** (↑1, 2026-10-14 15:33): When hosted in China, they typically have external “safeties” that shutdown the model on certain topics. You could see that pattern very clearly with the Ox Alpha/GLM 5.3 Flash release. The initial hosting was all inside China, and it would abort mid-response, but as international partner providers came up, the model would talk more freely.
      - **u/ComeOnIWantUsername** (↑1, 2026-10-14 16:00): First days of Ox Alpha/GLM-5.3-Flash it was happy to talk about Tiananmen and stuff with me. It was only after 2-3 days when they started censoring it. 
          
          I still have my conversation with this model in OpenRouter Chat when it was very vocal about this topic and super anti-Chinese. And after it was censored it either stopped mid-thinking or responded with text like from CCP leaflet
- **u/reynadotpdf** (↑2, 2026-10-13 21:42): it's probably some variant of Wonder
- **u/TrainingTheory552** (↑2, 2026-10-13 22:03): is this a super fast model that is really dumb?
- **u/sirloindenial** (↑2, 2026-10-13 23:43): Maybe another glm model but it seems kind of stupid and fast so not like glm😂
- **u/FullProgrammer7107** (↑1, 2026-10-14 05:43): Fast and dump
- **u/OtherCardiologist319** (↑1, 2026-10-14 08:28): reflection ai Beam-501B-A23B 🤔
- **u/Super-Compote3675** (↑1, 2026-10-14 10:10): Can i download this model to my pc like llama models and use them in ollama for example?

---

## Gemini 4 Argon is now rolling out globally 🔥
**u/afanasenka** · 2026-10-13 16:13 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x50x7t/gemini_4_argon_is_now_rolling_out_globally/)

[https://x.com/GoogleAI/status/2110039860077527293](https://x.com/GoogleAI/status/2110039860077527293)

**Comentarios:**

- **u/iamchuckschuldiner** (↑8, 2026-10-13 16:57): (ultra)
  - **u/Leo_Kwkmi** (↑1, 2026-10-13 18:19): My Pro plan in brazil also has it for some reason.
    - **u/iamchuckschuldiner** (↑3, 2026-10-13 19:15): yeah it is rolled out for pro plans apparently, just not in antigravity.  
        4 argon high eats your 5hour limits like crazy tho. got -5% after a single prompt in web. can't imagine what will happen on long and complex agent coding tasks in AG!
- **u/Connect_Anybody_9365** (↑6, 2026-10-13 17:05): They hype kinda seems to have died already

---

## Opencode Android
**u/XXXX-4444** · 2026-10-13 16:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x50o3z/opencode_android/)

[removed]

---

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

- **u/HyperWinX** (↑3, 2026-10-13 14:04): Claude knows that if you are using it - you couldnt care less about all that stuff lmao
- **u/Ariquitaun** (↑2, 2026-10-13 16:42): OK.
- **u/stub_back** (↑1, 2026-10-13 17:26): My Claude never rewrite the [AGENT.md/CLAUDE.md](http://AGENT.md/CLAUDE.md) files nor create skills without asking me to do so.
- **u/crasspuk** (↑1, 2026-10-14 10:14): Agent files like AGENTS.md and CLAUDE.md are read as instructions, so say explicitly in the file and in the prompt that the agent must not edit them. Ask for a plan first on anything like a refactor or new skills, and approve it before the agent writes anything. That blocks most of the unrequested changes.

---

## opencode-remote-ssh: targeted remote commands via @mentions
**u/AbdSheikho** · 2026-10-13 12:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4va0x/opencoderemotessh_targeted_remote_commands_via/)

**Comentarios:**

- **u/kantorcodes1** (↑1, 2026-10-14 05:36): The routing detail I'm curious about: once a session is connected, plain sentences can run remotely, so remote-vs-local execution depends on the mention detection catching the server name. What happens when the model drops the mention or names a server that isn't connected, does it fail closed, or can a local-intended command end up on a remote host (or the reverse)?
  - **u/AbdSheikho** (↑1, 2026-10-14 06:41): For the model to execute shell commands on a server, first it needs to establish a connection. This, if the server isn't connected or listed on `/list_ssh` then it'll warn you.
      
      Also it won't connect to a server that needs passphrase (meaning you should `ssh-add` its key to the `ssh-agent`)
      
      > What happens when the model drops the mention
      
      I haven't tested this, but I can assume that the prompt will either fail or make the model (if the model is dumb) go in circles, or even execute the command locally.
      
      > can a local-intended command end up on a remote host (or the reverse)?
      
      Without `@`-referencing it, I guess not.
    - **u/kantorcodes1** (↑1, 2026-10-14 07:17): That is exactly the seam: an unconnected mention fails, but a dropped mention silently reroutes a remote-intended command to local bash, so the model's omission becomes the routing decision. Disclosure since it shapes the ask: I work on HOL Guard, an open-source policy layer that gates agent-invoked tool calls per invocation. Your routing already produces a structured decision (remote, local, fail), which is the clean case for a gate: a small Guard descriptor could make ssh_exec and mention-wrapped bash calls fail closed when the target is not explicit, so the untested case becomes a blocked call instead of a local exec. Open to a small contribution if it earns its place?
      - **u/AbdSheikho** (↑1, 2026-10-14 08:10): Yeah for sure, you can DM me, or reach me via my GitHub
        - **u/kantorcodes1** (↑1, 2026-10-14 08:16): Appreciated, and I will keep it on this thread rather than DM so the working notes stay public. The minimal contribution is a small Guard descriptor covering ssh_exec plus the mention-wrapped bash path, with an explicit-target check that fails closed when no connected server is named. A draft PR to main is welcome; the checklist is here: https://github.com/hashgraph-online/hol-guard/blob/main/CONTRIBUTING.md

---

## running opencode cli on my file manager
**u/UnknownBoyGamer** · 2026-10-13 12:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4v8tc/running_opencode_cli_on_my_file_manager/)

**Comentarios:**

- **u/Ok_Topic_3468** (↑1, 2026-10-13 17:18): i love the font choice

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
    - **u/Arnafas** (↑1, 2026-10-14 05:43): GLM 5.3 flash from opencode is a bit weird. I have opencode go and zai GLM sub and for some reason zai glm 5.3 flash works fine but the opencode go version sometimes stuck in grepping every single file in the repo. It does not happen often but still happens. That's why I tend to use deepseek flash from the opencode go and use glm 5.3 flash from the zai subscription mostly. But maybe this happens only to me.
- **u/Skibidirot** (↑3, 2026-10-13 11:57): two claude pro subs
  - **u/Abenh31** (↑1, 2026-10-13 12:11): a specific reason to use two instead one? except maybe usage limits
    - **u/FlyingNarwhal** (↑1, 2026-10-13 12:19): They likely have two $200 subscriptions & burn through limits in 2-3 days each.
      - **u/Abenh31** (↑2, 2026-10-13 12:21): pro and max are not the same
    - **u/Skibidirot** (↑1, 2026-10-13 12:22): two 20$ subs, one account's weekly limit i use it in 2 days roughly, so 2 accounts = 4 days out of 7 days with opus 5.5 - that's PEAK if you ever ask me.. and btw fuck codex, it made me hate my life
      - **u/Abenh31** (↑1, 2026-10-13 12:25): opus 5.5 max i presume. why not opus 5.5 max and outsource a lot of task for sonnet. you'll probably extent the life of your limit. 
          
          also is opus 5.5 as good as they say? compare against something like gpt or kimi k3
      - **u/SS_Sa2** (↑1, 2026-10-13 12:36): Any particular reason why the hate on codex
    - **u/Fresh_Sock8660** (↑1, 2026-10-13 13:28): From some of what I heard, the multiplers they advertise only apply to session limits. Weekly limits seem to be more like x3.5 and x7 for the max x5 and x20 subs respectively.
- **u/ngg990** (↑1, 2026-10-13 12:11): DeepSeek flash for all at max reasoning level
  - **u/Abenh31** (↑1, 2026-10-13 12:14): do you find better at generating specs?
    - **u/ngg990** (↑1, 2026-10-13 12:16): https://github.com/andrescevp/development-harness This is my personal harness for development, it is still wip because I am extracting it from my full agents/skills/tools
- **u/CaffeinatedTech** (↑5, 2026-10-13 12:17): DS 4.1 Flash has been handling everything for me.  Sometimes I spend a few days trying something different, then I come back to DeepSeek.
  - **u/Abenh31** (↑1, 2026-10-13 12:21): yeah so for me. what do you use it for? techstack and workflow types
    - **u/CaffeinatedTech** (↑1, 2026-10-13 20:45): Go HTMX / Wails.  Rails 8.  Kotlin.  My old PHP Bootstrap app.  I had it writing some rust, but I got sick of the compile times, and switched.
- **u/FlyingNarwhal** (↑2, 2026-10-13 12:20): Claude, supported by GLM, with Gemini, GLM, GPT, & Claude as fused reviewers when planning our when a feature is done.
  - **u/Abenh31** (↑1, 2026-10-13 12:24): so opus planning. glm implement. other models for reviews or second opionio. is gemini even that good ? i have used it mainly for language stuff as its perform great like translation or copywriting
    - **u/FlyingNarwhal** (↑1, 2026-10-13 22:40): Gemini catches things others don't due to it having different training data & methods. It's great when using video or media, but I wouldn't put Gemini 3.8 flash anywhere close to opus-5.5.
        
        For development, opus for planning, fuse of experts for reviewing the plan, glm for implementation, opus for code reviews, and fuse of experts for final production gates.
- **u/Deus_Judex** (↑1, 2026-10-13 12:21): ChatGPT-Subscription (20$)  
    Mainly Luna on Medium or high
  - **u/Abenh31** (↑1, 2026-10-13 12:22): yep i find luna max with my techstack work great and has a great cost to clean implementation ratio
    - **u/Deus_Judex** (↑1, 2026-10-13 12:31): I sometimes go up to Sol, and when i do, i often see a significant improvement, but i only go up on really hard tasks like once a week.
        
          
        I almost never get below 85% of weekly limit xD
- **u/thomas29needles** (↑1, 2026-10-13 13:09): Deepseek 4.1 flash for working with code, Qwen 3.8 flash for translations and working with text. Kimi K3 for deep analysis or Qwen 3.8 max sometimes.
- **u/Phaelon74** (↑1, 2026-10-13 13:19): Glm5.3-flash and Qwen3.8-flash-next for the work horses working in tandem.  Then opus5.5 or astra for a written plan, constitution, etc.  Once the product is built, its a living entity the work horses maintain.
- **u/Fresh_Sock8660** (↑1, 2026-10-13 13:27): Currently, Opus 5.5 on pro x1 is giving me enough usage but I already did the reset. I'll need to combine the two at some point soon. Thinking opus 5.5 to create detailed contracts and ds4.1f to implement. First thing I did with opus was review a crapload of code generate by ds4.1f and we basically had no significant problems. ds4.1f was doing a great job on its own so I expect the two to excel.
- **u/look** (↑2, 2026-10-13 13:57): MiMo V2.6 Pro and GLM 5.3 Flash.
- **u/HsSekhon** (↑1, 2026-10-13 14:20): Kimi K3 for planning and code review for changes. Deepseek 4.1 for implementations. GLM 5.3 eats alot of my usage.
- **u/LebiaseD** (↑1, 2026-10-13 15:24): Local QFN3.8 on strix halo - dropped all my subs
- **u/supermerill** (↑1, 2026-10-14 00:21): Opus5.5-high ochestrate luna6-max or sonnet 5.5 or deepseek-max (depending of usage left) reviewed by sol6.1-xhigh & deepseek-max (or opus-xhigh, mimov2.6pro or glm, depending of usage left).
    
    Using codex 20$, opencode go, and obviously claude api as it's forbidden to use a max 100$ plan on opencode.

---

## DeepSeek 4.1 Flash only hitting 87 tok/s on OpenCode Go, is this normal?
**u/aliencreature12** · 2026-10-13 10:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4t6wr/deepseek_41_flash_only_hitting_87_toks_on/)

**Comentarios:**

- **u/AppealSame4367** (↑3, 2026-10-13 10:52): Yes, and there are problems with compaction above 500k context.
    
    They can never not fuck up a good product. Who cares about 4x usage if it gets dumber, less quality or has other new problems?
- **u/ConsistentGent** (↑1, 2026-10-13 11:41): 87 tok/s?! Commandcode is the same but i think they also limit concurrent connections so you can do less than on opencode.
- **u/ozguru** (↑0, 2026-10-13 12:44): normal.

---

## is Big Pickle down?
**u/Awkward_Bottle4887** · 2026-10-13 10:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4szz6/is_big_pickle_down/)

I can't use Big Pickle for the last 24 hours. Are you also facing the same issue?

I had to switch to Space Bunny for a while.

Yesterday it doesn't even enter the log in opencode dashboard, now it does but I don't actually get reply for very long time.

**Comentarios:**

- **u/bigrealaccount** (↑-1, 2026-10-13 17:40): Who tf is using big pickle
  - **u/Awkward_Bottle4887** (↑2, 2026-10-13 17:42): uhm... me?
      
      The last model on Big Pickle did better than Muse Spark despite it's much smaller 200k context window.
  - **u/blosu** (↑1, 2026-10-14 03:19): Clearly you need to give it another go. it can be quite good.
    - **u/Awkward_Bottle4887** (↑1, 2026-10-14 15:52): Do you not have problem using big pickle recently?

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
**u/geearf** · 2026-10-13 02:07 UTC · ↑13 · 4 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4kkgg/security_opencode_does_not_ask_for_file/)

I only noticed when I realized the agent looking at files it didn't ask to have access.  
As far as I could tell that changes came with 2.0.25 but no one bothered warning users it seems.

  
There has been a bug opened for days already: [https://github.com/anomalyco/opencode/issues/54524](https://github.com/anomalyco/opencode/issues/54524)

  
This a good reminder to not trust any of these companies writing harnesses and add your own security on top of whatever they might offer.

**Comentarios:**

- **u/szxdfgzxcv** (↑3, 2026-10-13 07:46): What the fuck, whats the use of even having permissions at that point then. Also completely silently changing permissions to opt-in from opt-out seems insane.
  - **u/geearf** (↑1, 2026-10-13 12:51): Absolutely agreed!
      
      Personally I lost trust in the platform, but to be fair, I was a fool to trust the opt-out when I could have made it clear in the config.
- **u/qqYn7PIE57zkf6kn** (↑1, 2026-10-13 14:02): > add your own security on top of whatever they might offer.
    
    do you have suggestions for that
  - **u/geearf** (↑2, 2026-10-13 16:16): Here are some ideas, but you'll have to look into it and decide what's appropriate for you:
      
      AppArmor, bwrap, different user for OpenCode, systemd hardening, containers like Docker, a full VM, etc.

---

## ocserve - OC rust server
**u/microbass** · 2026-10-13 00:40 UTC · ↑4 · 2 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x4is1l/ocserve_oc_rust_server/)

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
