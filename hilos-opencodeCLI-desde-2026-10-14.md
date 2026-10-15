# r/opencodeCLI — hilos 2026-10-14 → 2026-10-16
_Generado: 2026-10-15T15:22:53.080882+00:00 · 17 hilos · 70 comentarios · fuente: Arctic Shift_

## DeepSeek V4.1 Flash is FREE in OpenCode 🔥
**u/afanasenka** · 2026-10-15 07:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x6fj3h/deepseek_v41_flash_is_free_in_opencode/)

---

## Thinking of subscribing BytePlus ModelArk Coding Plan
**u/nekohacker591-** · 2026-10-14 21:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x63ysk/thinking_of_subscribing_byteplus_modelark_coding/)

Just like the title stated, anyone has referee code? it should be cheaper using that right?

**Comentarios:**

- **u/AdditionImmediate510** (↑2, 2026-10-15 03:35): Just don't. Stay with Opencode Go

---

## Big pickle giving thinking as output
**u/ohhno_whyamihere** · 2026-10-14 15:29 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5ua76/big_pickle_giving_thinking_as_output/)

I have been using chatgpt plus auth and the mimo v2.6 flash ,muse spark 1.3 and step 5 preview free models ,for a small task i thought of using big pickle and i was suprised to see today it was showing the thinking as output instead ,anybody else having that??

**Comentarios:**

- **u/Individual-Quote-958** (↑2, 2026-10-14 17:54): Yeah I've hit this with a couple of the free/Plus-routed models. What usually happened for me was the "thinking" channel getting dumped into the visible reply instead of staying collapsed, especially on short prompts. Try the same tiny task on a different free model in the same session; if only Big Pickle does it, it's that model path. Also check whether you have any thinking/reasoning display toggle on for that model, and retry with a one-line instruction like "reply with the final answer only, no scratchpad."

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

**Comentarios:**

- **u/Ctbhatia** (↑1, 2026-10-15 00:29): the check people skip is how the API behaves when a stream is cancelled or comes back empty, since a client that waits for a final usage chunk can just hang there.

---

## Opencode freetier stoped working with 9router
**u/MasonPak** · 2026-10-14 14:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x5s16r/opencode_freetier_stoped_working_with_9router/)

Hey guys; does anyone else has issues with using 9router for opencode free tier? I faced the issue just now. Is there any way around it? Without the 9router, the free tier reaches the usage limit too soon.

**Comentarios:**

- **u/william341** (↑1, 2026-10-15 02:45): You're probably getting caught by abuse prevention for abusing the free tier.
  - **u/Ordinary_Giraffe_825** (↑1, 2026-10-15 04:55): no. i just install on separate vps. it's same problem. opencode hasn't support 9router. must use from opencode CLI.

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

- **u/Diligent-Loss-5460** (↑6, 2026-10-14 13:23): jev free is available on zen
  - **u/Mancho_United** (↑3, 2026-10-14 14:53): Yes, but I assume for a limited time and with rate limiting. Would be great to be part of the GO plan usage.
  - **u/Tech-Sapien18** (↑2, 2026-10-14 16:26): Is it? It is not visible
- **u/squirrelscrush** (↑2, 2026-10-15 02:37): You can probably get a free decision model from openrouter, but I remember Jev is there on Zen

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

- **u/tsangberg** (↑5, 2026-10-14 10:50): >I'm aware that best practice is usually to run your agents in some kind of container, but I'm willing to bet a large portion of users are *not* doing that
    
    I agree that it should've been communicated, but I think the right thing to do is to remove all the pretense that these "please don't" rules work. It's better to just tell people that if they're running the harness without actual sandboxing they are indeed risking the LLM doing something it shouldn't.
  - **u/thatboyonabike** (↑0, 2026-10-14 11:11): I do agree, but I think that's a larger issue that even the bigger players are guilty of, so I didn't want to sound like I was picking on OpenCode for it.
    - **u/Diligent-Loss-5460** (↑2, 2026-10-14 12:57): I think its worth mentioning in the changelog since it is a behavior change but anomaly has been doing an awful job at maintaining their repo so it might be too much to ask
- **u/crasspuk** (↑1, 2026-10-14 11:22): The communication complaint is fair. A change to which directories need approval is a security default, so it belongs in the release notes, not only in a commit. Opt-in is the safer default, and the linked issues show others hit the same change.
  - **u/thatboyonabike** (↑1, 2026-10-14 11:31): Begone bot.
- **u/ozguru** (↑1, 2026-10-14 13:23): I guess this is to reduce friction for users. similar to codex. I believe they kept related config field.
- **u/geearf** (↑2, 2026-10-14 17:11): I opened a post about this: [https://www.reddit.com/r/opencode/comments/1x4kkmr/security\_opencode\_does\_not\_ask\_for\_file/](https://www.reddit.com/r/opencode/comments/1x4kkmr/security_opencode_does_not_ask_for_file/)
- **u/rilosk** (↑1, 2026-10-14 19:19): I switched off the platform. I feel like theyve been slacking on the communication  side of things and a lot of changes they are making just aren't great. Too busy on twitter i guess
  - **u/OlegPRO991** (↑1, 2026-10-15 05:44): What did you switch opencode for?

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

- **u/Odd_Teacher_4089** (↑11, 2026-10-14 07:46): ![gif](giphy|fDbzXb6Cv5L56)
- **u/kubblegum** (↑2, 2026-10-14 07:47): insane
- **u/BrownCarter** (↑9, 2026-10-14 07:49): Is it better thank cheapseek?
  - **u/Embarrassed-Salt6590** (↑4, 2026-10-14 07:59): Not that much noticable unless maybe u want to hype vibe
  - **u/ComeOnIWantUsername** (↑2, 2026-10-14 07:59): a lot better
  - **u/Amarsir** (↑14, 2026-10-14 08:06): In terms of intelligence, definitely. But you also get like 1% as much use because the API price is so much more expensive.
    - **u/AlexandraMaryWindsor** (↑-1, 2026-10-14 08:18): Intelligence does not matter if it actively seeks to do the least amount of work as possible.
        Cheap Chinese models have a better work ethic and are more reliable, I cannot trust it's output, too much wrong things have happend.
      - **u/New_Comfortable7240** (↑2, 2026-10-14 10:58): What do you think of the workflow
          
          - plan with intelligent model in max of xhigh
          - work with cheap Chinese workhorse 
          - verify with intelligent model in medium or high
        - **u/RespectJaded15** (↑2, 2026-10-14 12:38): I think medium is good enough for intelligent model. I use opus 5.5 medium with DeepSeek/muse model.
- **u/alphasubstance** (↑101, 2026-10-14 07:52): Available in opencode-go before available in antigravity for pro users.
  - **u/l0rirw1ao** (↑14, 2026-10-14 08:48): Truly a Google fell off moment and its not even that good form what I read about it.
  - **u/Pinery01** (↑19, 2026-10-14 09:02): oh.. yeah, available for people who paid $10, not for who paid $20 lol
  - **u/Bloated_Plaid** (↑2, 2026-10-14 10:35): Make it make sense lol.
  - **u/jbig3low** (↑3, 2026-10-14 15:27): yah this makes no sense, why does google do such dumb stuff you would think they have some smart people employed.
- **u/hacker_backup** (↑5, 2026-10-14 07:56): How is it so cheap?
  - **u/WishboneOk305** (↑5, 2026-10-14 08:17): because its fucking expensive to use. You can easily get 10x more done on deepseek or whatever
- **u/Amarsir** (↑19, 2026-10-14 08:03): Bear in mind that the API price is $4/$20. That means even with the $60 usage they estimate 440 prompts.  Without the 4x it would be the same as Kimi K3.
  - **u/subhashg547** (↑2, 2026-10-14 08:28): isn't introductory pricing 2/10 usd?
    - **u/Amarsir** (↑7, 2026-10-14 08:31): Not here:
        
        [https://opencode.ai/v2/docs/console/go/#usage-limits](https://opencode.ai/v2/docs/console/go/#usage-limits)
        
        Other source might have cheaper API introductory prices. But it seems OpenCode went "full price, better multiplier" rather than a cheaper API price on $15 or $30.
      - **u/migsperez** (↑6, 2026-10-14 10:12): And it's a contributor
  - **u/Embarrassed_OnionX** (↑3, 2026-10-14 15:35): Smartest? It's benchmaxxed af
- **u/crusaderky** (↑3, 2026-10-14 08:24): oh wow, $60 will last three whole prompts
  - **u/Financial_Bug2389** (↑3, 2026-10-14 10:27): Depends on how you use it. Maybe one.
- **u/nomadArch** (↑2, 2026-10-14 10:57): Google still makes models?
- **u/KayBay80** (↑10, 2026-10-14 11:31): Nobody's going to care at all about Argon in a week anyways.
  - **u/ahmetegesel** (↑5, 2026-10-14 13:01): Sad but true. All the hype, slow roll-out plan and awesome looking benchmarks, but the pace in the frontier race and the tension the Chinese models cause with cheaper options will make all this effort pointless. They need to get faster with their flagship releases. 
      
      TBH I will always be more hyped up with small but capable models’ releases.
    - **u/KayBay80** (↑1, 2026-10-14 13:22): We broke down and got Ultra just to test this (well, one of our teammates did) and while its an upgrade over flash, it still has the same quirks. One of which is unforgivable: It doesn't actually do the job and says that it does, fabricates things it SHOULD have done but didnt, and straight up lies about ideas that we have being good (when they are actually really bad).
        
        Google isn't going to catch the frontier at this point. We trust Qwen and DS over Argon any day of the week based on just less than one day of working with it.
    - **u/Stock-Self-4028** (↑1, 2026-10-14 13:27): Argon is still currently the SOTA in 'creative writing' (whatever it means in practice) and is significantly less expensive, than Fable so I guess it'll remain wiable at least for that for quite some time.
        
        I guess it'll remain one of the best models for things like pre-reviewing drafts of scientific papers etc for a few months. But yeah, it's definitely not a great coding model.
      - **u/KayBay80** (↑1, 2026-10-14 16:39): I don't doubt that its good at creative writing. It should be, after all, considering Google has literally every ounce of data available on the interwebs. But that's a different discussion for a different subreddit.
  - **u/lumos_ai** (↑1, 2026-10-14 16:33): Please talk for yourself. Nothing comes close to Gemini model for translation tasks and creative writing for me. If you are American or Chineese every model is almoat enough these days for coding. But LLM are not made only for coding.
    - **u/KayBay80** (↑2, 2026-10-14 16:37): You are literally in a coding subreddit... you do realize that right? Or did Argon fail to translate that for you..
- **u/Fresh_Sock8660** (↑5, 2026-10-14 12:25): Meh. Will stick to opus 5.5 slavedriving ds4.1f thanks google moneybags.
- **u/uncondensed** (↑3, 2026-10-14 12:51): Isn't this for the Contributor model where using it gives them permission to train on your data?
- **u/Dluugi** (↑6, 2026-10-14 14:53): it's not Gemini 4 Argon tho. It's Gemini 4 Argon contributor.
    
    Your data is explicitly used for model training
  - **u/Dluugi** (↑2, 2026-10-14 15:00): fuck that sounded like AI wrote it
    - **u/retardedGeek** (↑3, 2026-10-14 15:13): It's just 2 sentences, chill
- **u/GroundbreakingNote71** (↑2, 2026-10-14 18:53): Google showing its colors

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
  - **u/Sufficient_Wait4290** (↑1, 2026-10-15 05:32): I turned on parallel=4 and debug, did a task in OpenCode, pasted the log in Gemini (because I'm lazy) and was told everything did run sequentially.
      So I need to turn on something in OpenCode or my assumption about OpenCode running parallel was wrong.
- **u/ngg990** (↑1, 2026-10-14 17:53): Compile llamacpp and setup properly the concurrent connections x context window

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
