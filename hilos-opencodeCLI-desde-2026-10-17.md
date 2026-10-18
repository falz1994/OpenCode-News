# r/opencodeCLI — hilos 2026-10-17 → 2026-10-19
_Generado: 2026-10-18T01:57:13.567185+00:00 · 29 hilos · 124 comentarios · fuente: Arctic Shift_

## Follow-up: Tested my 9 thinking rules on long-horizon agent tasks (Terminal-Bench 2.0)
**u/PilgrimofHaqq2** · 2026-10-18 01:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8q75w/followup_tested_my_9_thinking_rules_on/)

On my previous posts, people argued these thinking rules might work on short tests but would hurt long-horizon tasks. So I tested them on Terminal-Bench 2.0: same model (GLM-5.3-Flash), same agent, every task run with and without the rules. I ran it on High thinking as Max thinking was taking so long that the model ran out of time for each task.

The rules:

    ## Thinking discipline
    
    1. Check the request first. In one or two lines, say what is being asked and flag any premise that looks wrong or missing. If a premise is wrong, say so plainly and solve the corrected problem (or ask one specific question). Do not silently accept a broken premise, and do not reason around it.
    2. Finish one approach before switching. Pick the most promising approach and carry it to a conclusion. Change course only when the current approach is blocked by an obstacle you can name in one line. Do not hop between approaches because of a vague feeling.
    3. When an answer is settled, stop working on it. Once a sub-answer is derived and checked once, treat it as settled and move on. Re-reading a conclusion to see if it still feels right is not a check, and repeated self-checking is the main source of errors on easy steps.
    4. Doubt is not evidence. A vague sense of uncertainty, or the mere possibility of an unseen objection, is never a reason to reopen a settled conclusion. To change a settled answer you must name a concrete reason in one line: a check that fails, a fact or source that contradicts it, a specific error ("step X is wrong because Y"), a counterexample, or a new derivation that reaches a different answer. If you cannot name one, keep your answer and continue.
    5. Do not revise just to agree. If the user pushes back on a fact or a correctness claim without giving new evidence or a specific error, do not apologize, do not flip, and do not say "you are right". Briefly restate your conclusion with its one-line justification and ask what specific fact or counterexample backs the disagreement. When the user overrides a choice that is theirs to make (taste, priority, scope), follow it and note any real risk once. Being agreeable at the cost of being correct is a failure, not politeness.
    6. New evidence does reopen the case. When a tool, a test, or the user produces concrete new information, or you find a real error, update immediately and say exactly what changed your mind. Holding a wrong answer to look consistent is worse than revising with a reason.
    7. Verify against outside facts, not by rethinking. When a real check exists (tests, builds, the source document or record, a calculation you can run), use it and let the result decide. Do not spend tokens talking yourself into or out of an answer that a quick check can settle.
    8. Do not perform caution. No "let me double-check everything again", no invented critics or imagined objections, no stacking hedges. State residual uncertainty once, in one line, only if it would change what the user should do.
    9. Only correct an earlier statement when the error would change the user's code, conclusions, or decisions. State corrections plainly and briefly, then continue the task. For slips that change nothing, make the fix and move on without noting it.

How it compares to the [Terminal-Bench 2.0 leaderboard](https://www.tbench.ai/?version=2.0):

|Model|Agent|Score|
|:-|:-|:-|
|GPT-5.5|Codex CLI|82.2%|
|Claude Opus 4.6|Terminus 2|62.9%|
|GPT-5.2|Codex CLI|62.9%|
|**GLM-5.3-Flash + my rules**|**mini-swe-agent**|**59.6%**|
|Claude Opus 4.6|Claude Code|58.0%|
|Gemini 3 Pro|Terminus 2|56.9%|
|GPT-5.2|Terminus 2|54.0%|
|**GLM-5.3-Flash, no rules**|**mini-swe-agent**|**52.8%**|
|GLM 5|Terminus 2|52.4%|
|GPT-5|Codex CLI|49.6%|
|Claude Sonnet 4.5|mini-swe-agent|42.5%|

My scores are out of all 89 tasks, single attempt (3 tasks wouldn't start on my machine and count as fails). Leaderboard scores average multiple attempts, so treat mine as ballpark.

---

## Any good basic opencode web ui tutorials?
**u/arkie87** · 2026-10-17 23:53 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8ouji/any_good_basic_opencode_web_ui_tutorials/)

Is it just me, or are there not any good opencode web ui tutorials?

It seems like most tutorials are focused on how to connect mcp servers etc...

but I want basics like how to access a terminal or view the git diff. I just discovered i could add comments to lines in the diff or just browse files by clicking a button. Similarly, i had to google to find out that there was a terminal i could access instead of just typing "! bash command " one command at a time

---

## A beginner could use some help
**u/aleebit** · 2026-10-17 23:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8osv2/a_beginner_could_use_some_help/)

Yesterday, I saw the news that DeepSeek was free and decided to give it a try. I started a tiny project to clone a website a friend of mine had built. It gamifies the study material for our 8-year-old kids' exams, and I wanted to adapt it for my autistic son.

It was a single HTML page with some simple, embedded JavaScript. I started yesterday at 8 PM, and by this afternoon, I'd already hit the usage limit.

During that time, I made a few adaptations, added two new pages, and wrote some JavaScript. Nothing particularly substantial.

I know it was the free model, and I understand there are usage limits, so I figured that might explain it. But then I opened the DeepSeek harness, which gave me something like $1 in free credits. I used the same model, asked it to review the project and suggest improvements, and those credits lasted about 30 minutes.

I'm a data engineer, and my company provides corporate AI tools that I use pretty heavily in my day-to-day work. But I've never had to worry about the costs, so I'm pretty much a beginner when it comes to this.

Should a tiny web project with just HTML and a little JavaScript really consume that many tokens or hit usage limits that quickly?

I'm asking because I'm considering subscribing to OpenCode Go. It might not seem expensive, but in my currency, it's around R$60 a month. If I'm going to burn through the available usage that quickly, I don't see the point in paying for it.

---

## OpenCode v2 TUI plugin renders only the current session when installed as a package, but works from a local path
**u/UpstairsResident8121** · 2026-10-17 23:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8o677/opencode_v2_tui_plugin_renders_only_the_current/)

I'm building a TUI sidebar plugin for OpenCode V2 (github:ypxcs/opencode-session-history).

\- Environment: OpenCode v2.0.32, macOS arm64.

\- Works: loading the plugin from a local path ("plugins": \[{ "package": "/abs/path/src" }\]).

\- Broken: installing it as a package (github:ypxcs/opencode-session-history). The panel shows only the current session, and the built-in sidebar context/usage info disappears.

\- The plugin's data layer works in both cases (it fetches all sessions). The host just doesn't render them.

I've ruled out versions, the install tool, the install location, exports vs path loading, and tsconfig.json. Full details, the ruled-out table, and the debug steps are in the repo:

https://github.com/ypxcs/opencode-session-history#known-issue-github-install-renders-only-the-current-session

Does anyone know why a TUI plugin loaded as a package breaks Solid/Slot rendering, when the same code works from a local path?

---

## never used opencode before will definitely never touch it again
**u/Just_Lingonberry_352** · 2026-10-17 22:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8mmer/never_used_opencode_before_will_definitely_never/)

data breach aside and all the api keys now being exposed through it 

i have never used it much never really "got" what opencode was for other than it was for people who couldn't afford the higher tier plans from frontier labs

after today i think im going to uninstall it and stick with claude and codex 

i think cline or pi anywhere someone has custody of your api keys from frontier labs is going to be targeted so im going through them all to remove them all

fuc k opencode lmao

**Comentarios:**

- **u/NervousWinner8160** (↑1, 2026-10-17 22:14): Not sure why fuck opencode in particular?
    
    And yes other providers under similar attacks, you see it in usage disappearing and credit cards getting charged
- **u/Fair-Spring9113** (↑1, 2026-10-17 22:16): tell me your clueless without telling me
- **u/tronkk** (↑1, 2026-10-17 22:17): ![gif](giphy|tIeCLkB8geYtW)
- **u/Important-Radish-722** (↑1, 2026-10-17 22:20): First time on the Cloud?

---

## Time to move? 2 Security issues in a week
**u/geearf** · 2026-10-17 20:53 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8kxw2/time_to_move_2_security_issues_in_a_week/)

It makes me wonder.

One main security change in the harness and no warning: [https://www.reddit.com/r/opencodeCLI/comments/1x4kkgg/security\_opencode\_does\_not\_ask\_for\_file/](https://www.reddit.com/r/opencodeCLI/comments/1x4kkgg/security_opencode_does_not_ask_for_file/)  
And one breach in the service: [https://www.reddit.com/r/opencodeCLI/comments/1x8gtjg/opencode\_security\_breach/](https://www.reddit.com/r/opencodeCLI/comments/1x8gtjg/opencode_security_breach/)

  
How can we trust the team anymore?

**Comentarios:**

- **u/DanteVermillyon** (↑1, 2026-10-17 21:00): me personally I do think this are valid reasons to move out, they don't necessarily affect me yet (the things i use the agents for are so non-important for me that i blindly just say yes whenever it asked for permission before cause it really didn't matter, and at this point i was part of so many security breaches that i got kinda desintized, someone is probably selling information about my private data since 2019 anyways), but if  people that use OpenCode for more serious things do see this as a reason to change to any other thing, I think they have all the reasons to, just the security change would be enough for me to dip-out if i actually used OpenCode for sensitive work
  - **u/Ok_Topic_3468** (↑2, 2026-10-17 21:12): i get what you mean but the real issue with this breach was it cost many users with paid api keys linked to get charged hundreds in unauthorized usage
    - **u/DanteVermillyon** (↑1, 2026-10-17 21:20): Yeah, that's why I said they have all the reasons to leave. Hope the team can fix all of this so the victims get their money back
  - **u/geearf** (↑2, 2026-10-17 21:13): I think even if you don't have security requirements today, as a force of habit you might still use the same stuff whenever you do, so it's not terrible to move out before it becomes a problem, instead of after...But I get your point. :)
- **u/Ok_Topic_3468** (↑1, 2026-10-17 21:08): considering how open they are about using ai to develop opencode itself, im not surprised this happened... personally im moving to deepseek harness to not have any more risks with opencode's centralized proxy issues since everything is locally hosted
  - **u/geearf** (↑3, 2026-10-17 21:12): I've never tried DS's harness, how do you like it?  
      Is it ok with non DS's models too or...?
      
        
      Thanks for the idea!
    - **u/Ok_Topic_3468** (↑1, 2026-10-17 21:25): i think its a pretty good alternative, i like the customizability it offers
        
        it works perfectly fine for me with non deepseek models, sometimes better than opencode depending on the model . the only issues ive had with it is due to the tradeoff with it being completely local hosted, you'll need to add your own plugin/api for web search capabilities. [ive found this free one to work perfectly for me](https://github.com/liustack/modsearch) although there are many other options out there
      - **u/geearf** (↑1, 2026-10-17 21:31): I appreciate it!  
          Looking a bit into it it seems there's no TUI for it, only desktop and webapp, but you know while that's a con, if it works better, it's just that...
        - **u/Ok_Topic_3468** (↑1, 2026-10-17 21:36): [this repo](https://github.com/rayafriandion/dsh-oc-tui) for a TUI plugin appears to be actively maintained and the design is claimed to be inspired by opencode's, i haven't tested it yet but it looks promising
          - **u/geearf** (↑1, 2026-10-17 21:40): I appreciate this!  
              But if moving away is, in part, done for trust reasons, starting with a third party cli seems iffy... unless the third party is well known of course...
              
                
              Thank you!
- **u/NervousWinner8160** (↑7, 2026-10-17 21:25): Other providers are definitely under similar attacks. 
    
    You see it in peoples usage disappearing and such, they just dont talk about it as much.  Every provider has a big red target on their back.
    
    Opencode does happen to have a higher tier of responsibility in this case because they are storing external credentials. But i wouldn’t say it’s indicative of particularly poor security practices.
    
    I’ll be waiting for the full report.
- **u/SaltineAmerican_1970** (↑1, 2026-10-17 21:42): \> How can we trust the team anymore?
    
    You’d rather trust a team that *doesn’t* fix security issues?
- **u/Just_Lingonberry_352** (↑1, 2026-10-17 22:09): curious
    
    why do you guys even bother to use opencode ????
    
    what possible benefit does it give you that codex or claude cant?
    
    you know frontier labs have cheap models that performs better than anything opencode offers through its bullshit tier subs?
  - **u/RedParaglider** (↑1, 2026-10-17 22:15): I used to use it. I just actually removed it today.  I use pi.dev, hermes, and claude/codex.  Hermes and pi.dev for local models.  Open code was just too opinionated and heavy for a console tool, and Hermes for that kind of weight is more functional.
  - **u/Competitive-Ebb3899** (↑2, 2026-10-17 22:43): First of all, I get way more usage out of my $10 of OC Go Subscription using DS4 flash than I could by paying the double to Codex or Claude by using their cheapest models. 
      
      And their cheapest models are OK, but I didn't feel they are smarter than Deepseek. Especially that up until just recently, Anthropic's cheapest model was a really old and dumb Haiku. And with Sonnet I constantly hit usage limits. Luna is OK, but it's also more prone to hit limits.
      
      Not to mention both Anthropic and OpenAI forces you to use their subscriptions with their software. And I just don't like them.
      
      On the other hand, I could use my OC subscription with other clients. Heck, I could even use it with Codex or Claude if I wanted. But I don't, I actually prefer using the OpenCode CLI, because it may not have all the features, but it's UX is much more like how a TUI should be. 
      
      So, there are many benefits which can be summed up with lots of options, and dirt cheap low-mid-range inference.
- **u/narkeeso** (↑0, 2026-10-17 22:15): This honestly got me to check if a Claude Pro subscription is feasible. I just had a bunch of killer sessions with Sonnet and Haiku that is more than enough usage for me.

---

## OpenCode is selling data (your api keys and data is unsafe)
**u/wpbrgiejoe** · 2026-10-17 18:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8i1cy/opencode_is_selling_data_your_api_keys_and_data/)

**Comentarios:**

- **u/SaltineAmerican_1970** (↑1, 2026-10-17 21:54): If the product is free, *you* are the product.

---

## Opencode Hack: How is OpenCode claiming to be ZDR when API keys from Anthropic and OpenAI are being stored in their database?
**u/Far-Worldliness5561** · 2026-10-17 18:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8hlcv/opencode_hack_how_is_opencode_claiming_to_be_zdr/)

How is OpenCode claiming to be ZDR when API keys from Anthropic and OpenAI are being stored in their database?

OpenCode admitted they were hacked and are calling it a distillation attack. How does distillation explain users’ API keys being exposed? Distillation and credential theft are two completely different things.

This is a massive data leak, and users deserve to know exactly what happened, what was compromised, and who had access to their credentials.

Stop hiding behind the distillation narrative and give users real answers. 

**What is the point of claiming ZDR when users’ API keys are sitting in your database?**

**Comentarios:**

- **u/Toastti** (↑25, 2026-10-17 18:37): Zdr has nothing to do with them storing api keys. If you provide open code your openAI or Anthropic key for later use how do you expect to use it if they are not storing the value in their database?
  - **u/Far-Worldliness5561** (↑-27, 2026-10-17 18:38): First of all why are they storing my openai keys in the db? Why? It’s against their own privacy policy 
      
      Second if they can store api keys I am pretty sure these scammers are storing everything else too
    - **u/vlewy** (↑15, 2026-10-17 18:43): Obviously, they are stored in the database if you register them yourself in your account to use with Opencode. 🤷🏻‍♂️
      - **u/Positive_Poem5831** (↑16, 2026-10-17 18:46): The downside of vibing and don't  knowing how things work 🤦‍♂️
        - **u/debackerl** (↑6, 2026-10-17 18:53): Yes, lot of noobs in the sector nowadays...
        - **u/geearf** (↑2, 2026-10-17 20:50): How many weeks until  
            \> "It's what plants crave"  
            ?
    - **u/DrunkenRobotBipBop** (↑6, 2026-10-17 18:57): How on earth would a BYOK system work if they did not store the key on their database? 
        
        If you are affected by this, just rotate that key and call it a day.
- **u/theChaosBeast** (↑3, 2026-10-17 18:49): Dude relax, no need to post every few minutes
- **u/look** (↑5, 2026-10-17 18:53): It was keys entered into their web console for their hosted “BYOK” solution for sharing across a team in a workspace. 
    
    They aren’t storing the third party keys you put into your local harness.
- **u/Strict-Prune-879** (↑1, 2026-10-17 19:03): Mon dieu que le monde est peuplé de complotiste!!!!
- **u/No_Captain4899** (↑1, 2026-10-17 19:04): Opencode has no more ZDR for the most part as far as I know
  - **u/Bloodshoot111** (↑3, 2026-10-17 19:07): And even if it has, ZDR has nothing to do with it this guy is just spamming with 0 knowledge
    - **u/No_Captain4899** (↑1, 2026-10-17 19:07): I agree with you

---

## Opencode Hacked ? And the response from opencode is bogus
**u/Far-Worldliness5561** · 2026-10-17 18:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8hh3h/opencode_hacked_and_the_response_from_opencode_is/)

OpenCode says this was a distillation attack, but how does that explain API keys being compromised?  
Distillation and credential theft are two very different things. If API keys were exposed, users deserve a clear explanation of what happened, what data was affected, and what steps are being taken to secure their accounts.  
Stop hiding behind vague explanations. We need answers, not excuses.

How is Opencode ZDR? If they store our api keys too in the database ? This means OpenCode lies about being ZDR

**Comentarios:**

- **u/theChaosBeast** (↑1, 2026-10-17 18:35): It just happened today and they stated in the mail that they will provide updates and more info...
  - **u/Far-Worldliness5561** (↑-4, 2026-10-17 18:37): They should haha
    - **u/theChaosBeast** (↑2, 2026-10-17 18:38): There is no reason to think they wouldn't. Stop panicking
- **u/Chupa-Skrull** (↑3, 2026-10-17 18:37): How would one distill via an "attack" without compromising and fraudulently using someone else's API key for their requests
- **u/look** (↑2, 2026-10-17 18:39): Opencode has a hosted “bring your own key” thing where you put the Anthropic, OpenAI, etc key into their web console so it can be shared across a team/workspace.
    
    The server compromise doesn’t affect users that just put keys into their local harness.
- **u/geearf** (↑1, 2026-10-17 20:49): They used the keys they stole to do the distillation (I'm not going to call distillation an attack, I think it's fair game when those companies just grabbed their knowledge for free, at least usual distillers pay for the tokens).
    
      
    The important thing to me is that it's the 2nd security issue this week, one in the harness and one in the service. Time to look for something by someone else I think.

---

## Integrated the new DeepSeek tools into opencode
**u/_N0K0** · 2026-10-17 18:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8h7bk/integrated_the_new_deepseek_tools_into_opencode/)

Hey!

  
Saw Deepseek had posted some new tools next to the updated model, so figured I'd make a plugin for OpenCode that allows it to leverage them via code mode.



[https://github.com/N0K0/opencode-deepseek-tools](https://github.com/N0K0/opencode-deepseek-tools)

[https://www.npmjs.com/package/@hacky.software/opencode-deepseek-tools](https://www.npmjs.com/package/@hacky.software/opencode-deepseek-tools)

**Comentarios:**

- **u/DebosBeachCruiser** (↑1, 2026-10-17 19:43): 404

---

## ⚠️ OpenCode security breach
**u/afanasenka** · 2026-10-17 18:02 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8gtjg/opencode_security_breach/)

.

---

## OpenCode security breach, rotate your keys
**u/jpcaparas** · 2026-10-17 17:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8gp72/opencode_security_breach_rotate_your_keys/)

We had a security breach last night related to a large scale distillation attack that impacted 1.4% of OpenCode Console users

We have notified them all this morning via email

The incident is ongoing so we cannot share more details at this point but we are working with Anthropic, OpenAI, and Google to remediate

**Comentarios:**

- **u/jpcaparas** (↑17, 2026-10-17 18:08): https://preview.redd.it/cmxvdxgji2wh1.jpeg?width=1079&format=pjpg&auto=webp&s=3a91a7bd929df36533b671e3f8b543fac9e02258
    
    https://x.com/mattjay/status/2111507582053491188?s=46
- **u/jpcaparas** (↑5, 2026-10-17 18:18): https://x.com/mweinbach/status/2111518053662064829?s=46
    
    https://preview.redd.it/ob8og72gk2wh1.jpeg?width=1320&format=pjpg&auto=webp&s=3461989ef2669bf44880b4f1da915d5af0fc9ab4
- **u/Chemical-Quote** (↑0, 2026-10-17 18:33): Distillation?  
    Which AI company is that desperate?
- **u/No_Commission_6153** (↑4, 2026-10-17 18:36): Does this affect someone who conencted their OpenAi Account with Open Code?
  - **u/wpbrgiejoe** (↑2, 2026-10-17 18:39): Yes opencode sells your data you're not safe change all account pass.
  - **u/Significant_Treat_87** (↑3, 2026-10-17 18:41): Are you on a subscription plan ("login with chatgpt") or did you paste in an API key? The first one I assume is fine, this is about the second one.
    - **u/No_Commission_6153** (↑3, 2026-10-17 18:42): subscription. but still worried if they got hacked if they got something from me
      - **u/Significant_Treat_87** (↑8, 2026-10-17 18:44): This is an issue with people having their API keys stolen, so I think you're ok. I will personally never use Opencode now though, they have had way too many security issues now.
- **u/Far-Worldliness5561** (↑-5, 2026-10-17 18:39): https://www.reddit.com/r/opencodeCLI/s/jA0CegTx0G we need answers
- **u/RevolutionaryFunny40** (↑15, 2026-10-17 18:43): https://preview.redd.it/yp9of9ouo2wh1.jpeg?width=1290&format=pjpg&auto=webp&s=ad421a572b1e81ff257eeabd9ab73c213b55a5e8
- **u/PhatOofxD** (↑12, 2026-10-17 18:45): This is why you don't put keys in cloud services I guess
- **u/geteum** (↑1, 2026-10-17 18:46): Just people who use API keys got affected?
- **u/qustrolabe** (↑4, 2026-10-17 18:54): So it's only those that added keys to online console? I guess local keys shouldn't be affected but better rotate for good measure
  - **u/jpcaparas** (↑1, 2026-10-17 19:52): correct, only BYOK on Zen
- **u/Certain-Emphasis-135** (↑1, 2026-10-17 19:26): So that’s why my openrouter credits got cleaned
- **u/dx80x** (↑2, 2026-10-17 20:08): I had my DeepSeek API connected to opencode and haven't received jack shit in my inbox about this.
    
    Luckily it wasn't touched but fuck opencode now.
    
    Thank you for posting here anyway, I wouldn't have known until I got drained if it wasn't for this post.
  - **u/officerblues** (↑6, 2026-10-17 20:39): It's only if you used bring your own key on opencode zen, not if you connected to the key using the opencode harness. They could work on their comms a bit, but you were likely not affected. It didn't leak your local keys, only the keys they had stored.
    - **u/dx80x** (↑1, 2026-10-17 20:49): Ah ok, thanks for the clarification mate.  I've used Go in the past but never Zen.  I still think it would have been better to inform everyone just in case, so at least people who aren't affected don't jump the gun (like I did a little haha).  
        
        Oh well, just need to make some new DeepSeek keys now which is alright but some people have been stung hard and that's really unfortunate.  Hope there's some kind of compensation for those guys at least
- **u/jpcaparas** (↑1, 2026-10-17 22:17): Some spicy discussions:
    
    \- [https://news.ycombinator.com/item?id=50133643](https://news.ycombinator.com/item?id=50133643)  
    \- [https://x.com/HotAisle/status/2111535689586413705](https://x.com/HotAisle/status/2111535689586413705)
    
    \> *The thing that grinds my gears is that everyone who works there seems to think that they’re cooking, or doing anything impressive at all. One day they will hopefully mature a little and realize how hard they got ego pimped.*

---

## Fingerprinting Cat-Jam
**u/andari3727** · 2026-10-17 17:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8fphb/fingerprinting_catjam/)

My report on Cat-Jam-Free provided in opencode.

---

## Haven't been able to login to OpenCode, any one?
**u/Miserable_Sky_4424** · 2026-10-17 17:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8fk57/havent_been_able_to_login_to_opencode_any_one/)

**Comentarios:**

- **u/Mountain-Business-92** (↑1, 2026-10-17 17:57): huh, I also use google to sign in and I was able to do it with no problems. maybe its a regional thing?

---

## A coding-agent price comparison should include the session you resume tomorrow
**u/EmetInteractive** · 2026-10-17 17:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8fi1n/a_codingagent_price_comparison_should_include_the/)

Coding agents rarely run in one uninterrupted session. You review a diff, step away, make changes, and return. That pause can affect the total cost.  
When comparing inference options like Mango Inference and MangoBoosts, test the same repository task twice: once without interruption and once after resuming later. Compare actual usage instead of assuming either run will be cheaper.  
Track the context sent at each step, including conversation history, file content, and new instructions. Even a short follow-up can resend substantial context. Remove credentials and private code before sharing traces.  
Compare reported input, cached input, and output separately. Repeated text doesn't guarantee a cache hit, so use actual usage records and current pricing rules.  
Ultimately, compare the total cost of completing the task, including resumed sessions and retries, alongside whether the tests pass. A low input-token rate means little if the workflow repeatedly resends context or fails to finish.

**Comentarios:**

- **u/Ariquitaun** (↑1, 2026-10-17 21:42): It's incredible how many words you used to say sweet fuck all

---

## Opencode va camino al desastre de la baja calidad
**u/PollutionDue7541** · 2026-10-17 16:59 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8f9zc/opencode_va_camino_al_desastre_de_la_baja_calidad/)

---

## /usage tab would be nice
**u/Saderius** · 2026-10-17 16:53 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8f5bv/usage_tab_would_be_nice/)

I mean, would you also like it within CLI? I mean, I would gladly tbh. Some test requests I send, I would not mind to know what I can use for that.

---

## How do i use a backup workspace in api key in omniroute?
**u/unchained_io** · 2026-10-17 14:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8c83y/how_do_i_use_a_backup_workspace_in_api_key_in/)

---

## Im rally liking opencode in cli. Thanks.
**u/BleedReddit** · 2026-10-17 13:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8anzr/im_rally_liking_opencode_in_cli_thanks/)

 tinkering with the spine of opencope to reduces token cost and continuity of  long and multiple sessions and workflow. few more verification and i will be sending it to the opencode dev team. 🤤

---

## Deepseek v4.1 flash 1017
**u/alovoids** · 2026-10-17 12:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x88v51/deepseek_v41_flash_1017/)

i hope it's available soon in opencode go 👀

**Comentarios:**

- **u/Academic-Sentence-34** (↑14, 2026-10-17 12:29): Wonder if they will give this at 80 dollar usage. No, right?
  - **u/boringstacks** (↑14, 2026-10-17 12:54): Not sure why not, same model, just post-trained
  - **u/alovoids** (↑1, 2026-10-17 12:59): they will. they succeed with the previous v4.1 flash
  - **u/ApprehensiveDelay238** (↑5, 2026-10-17 14:29): Why not? It's not any more computationally expensive than before. If anything, it's cheaper due to lower token usage.
- **u/horrbort** (↑16, 2026-10-17 12:34): Fp2 on opencode next week
  - **u/woodalchi96** (↑3, 2026-10-17 12:38): Why not full precision?
    - **u/horrbort** (↑8, 2026-10-17 12:54): Profit margins have to come from somewhere
      - **u/woodalchi96** (↑-1, 2026-10-17 12:57): Do you think they self host the models??
        - **u/horrbort** (↑8, 2026-10-17 13:08): No, I think they resell from the cheapest supplier and lock in favorable deals by guaranteeing predictable load. What do you think?
          - **u/woodalchi96** (↑3, 2026-10-17 13:50): I'm afraid they do the same..
  - **u/ApprehensiveDelay238** (↑1, 2026-10-17 14:30): Is current one fp2 too? Or just speculation.
    - **u/SOUINnnn** (↑1, 2026-10-17 17:51): Speculation
- **u/identity-morphism** (↑1, 2026-10-17 13:52): Muse contribor still better pareto right?
- **u/One_5549** (↑0, 2026-10-17 14:55): is this what the opencode free variant is using right now ??
  - **u/JackFr0st98** (↑1, 2026-10-17 21:56): it should be. but last time theu made a post 3 days after an update and the model selector ui got updated as well with "(new)" tag
- **u/warpaint_james** (↑3, 2026-10-17 16:00): Its live on OpenRouter now: https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017

---

## A Model Orchestra in opencode with Claude Code — Free Planner, Opus Coder
**u/ercanatay** · 2026-10-17 10:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x86pdo/a_model_orchestra_in_opencode_with_claude_code/)

Instead of making one AI model do everything, we built a team: a free “conductor” that delegates, and coders picked by how hard the job is. Here is what we learned in one evening, with the numbers we measured.

[](https://ercanataycom.medium.com/?source=post_page---byline--ce9a238545c5-----------------------------------------)

---

## A Model Orchestra in opencode with Claude Code
**u/ercanatay** · 2026-10-17 10:13 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x86o49/a_model_orchestra_in_opencode_with_claude_code/)

---

## Beam 1.0
**u/Abenh31** · 2026-10-17 09:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x85zme/beam_10/)

https://i.redd.it/9pth0nn1yzvh1.png

Guyz give beam a try. you might be suprised.   
I found it to be honest enough for daily work  
quite good at agentic coding  
very fast output  
and performed well in my ruby benchmark (better then deepseek v4.1 and muse spark 1.3)

**Comentarios:**

- **u/niwia** (↑1, 2026-10-17 09:39): Better than ds and glm ? 🤔
  - **u/Ammoun442** (↑1, 2026-10-17 11:48): Nope its kinda bad for hard stuff but its just so fast
- **u/AdFun4897** (↑1, 2026-10-17 16:23): Guys dont listen to the poster, dont even waste your time with Beam

---

## 🔥DeepSeek V4.1 Flash-1017 is on Hugging Face (see benchmarks inside)
**u/afanasenka** · 2026-10-17 08:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x84uhs/deepseek_v41_flash1017_is_on_hugging_face_see/)

[https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

**Comentarios:**

- **u/Ok_Quantity_4950** (↑14, 2026-10-17 08:20): https://preview.redd.it/6kqpdnbolzvh1.png?width=745&format=png&auto=webp&s=45dc4434442348081bc4e481c315bdaa29b86a7f
    
    WTF? Better than Opus? suspicious as f\*\*\*
  - **u/adolf_twitchcock** (↑-7, 2026-10-17 08:31): Why aren't they comparing it to current models like opus 5.5 and sol 6.1? weird af
    - **u/Living_Usual_1281** (↑4, 2026-10-17 08:36): You should know that this is just a Flash model. Such a contrast will only occur when it is in the Pro version.
    - **u/cloudsurfer48902** (↑19, 2026-10-17 08:37): Because it's a flash model. You only compare with SOTA if you were trying to build a SOTA model which a flash model is not. They get compared with other Flash models or previous SOTA.
      - **u/ps5cfw** (↑7, 2026-10-17 08:49): Flash was already SOTA enough for me, this only makes it better.
          
          People do not realize for most intents and purposes Opus tier models are overkill for the tasks.
        - **u/0DayMaker** (↑0, 2026-10-17 09:29): Okay cool? Not the case for all of us..
      - **u/adolf_twitchcock** (↑-3, 2026-10-17 09:26): Yeah, I agree they should compare it to similar sized models. But they compare it to old opus and sol models. Which makes it weird.
        - **u/cloudsurfer48902** (↑1, 2026-10-17 15:52): They are not that old, just direct prev Gen frontier models to show how close the flash model is. Just makes it impressive. Putting current Gen frontier would make the flash look bad and if they were more more than 2 gens old then that would would make it look like they're coping. But here, it's a complete fair use of them.
  - **u/xAragon_** (↑49, 2026-10-17 08:34): Did you read the image you attached? Opus 5 is beating in im most benchmarks there. Also, it's Opus 5, not Opus 5.5.
    - **u/yiestee** (↑14, 2026-10-17 09:05): A flash model on par with Opus 5 (not 5.5) is pretty big deal for me.
      - **u/ggPeti** (↑17, 2026-10-17 09:07): Did you read the comment you're replying to? Opus 5 beats it in more rows in the attached image than the other way around.
        - **u/look** (↑6, 2026-10-17 09:33): DS Flash is typically one of the weakest models of each generation (at least in terms of benchmarks), so it being close to Opus 5 bodes well for the new GLM and Kimi models that should be out soon.
            
            I would expect them to be clearly past Opus 5 and perhaps even competitive with 5.5 now.
          - **u/ggPeti** (↑5, 2026-10-17 11:28): GLM is garbage compared to DS Flash in my experience. Kimi is a smartass. Nothing follows instructions as diligently as DS.
          - **u/Front_Eagle739** (↑4, 2026-10-17 12:18): Not really? Dsv4 flash 0731 and dsv4.1 are great. Very competitive.
            - **u/look** (↑1, 2026-10-17 16:25): I’m talking about benchmarks and saying DS typically underperforms on them (in general at least) relative to apparent actual ability.
                
                It is quite low on the overall AA intelligence score, for example, but I think that is mostly just because of how hard that metric penalizes omniscience hallucination rate (which Deepseek is far and away the worst at of current models).
              - **u/Front_Eagle739** (↑2, 2026-10-17 16:31): Underperform on benchmarks relative to the actual performance is probably just others doing a little cheating with including benchmarks in the training data. Glm and deepseek seem on the better side as that goes. Ill give you the hallucination rate is probably part if it as well though
      - **u/ALxR1337** (↑0, 2026-10-17 09:44): Benchmarkmaxxing
    - **u/xatey93152** (↑2, 2026-10-17 09:11): This guy really comparing flash and trillion params model?
  - **u/Imaginary-Fee-9918** (↑-5, 2026-10-17 09:06): benchmaxxed
  - **u/howudothescarn** (↑1, 2026-10-17 11:38): Benchmarks are slightly below opus 5
    - **u/dumbasPL** (↑1, 2026-10-17 14:50): While price is orders of magnitude below.
- **u/Strict-Prune-879** (↑20, 2026-10-17 08:55): pour un modèle flash ces déja enorme
- **u/MotherPotential** (↑3, 2026-10-17 10:03): how many gb is this and hie much ram is needed
  - **u/squirrelscrush** (↑5, 2026-10-17 11:24): Similar to V4.1 Flash. This is just a retrained version.
- **u/Genetic_Prisoner** (↑22, 2026-10-17 10:24): Beating 5.6 sol on most benchmarks???Big if not benchmaxxed.
  - **u/LargeLanguageModelo** (↑1, 2026-10-17 16:36): Narrator: It was.
- **u/Harshith_Reddy_Dev** (↑9, 2026-10-17 10:55): Opencode go when?
  - **u/HsSekhon** (↑0, 2026-10-17 12:58): its not same as one already on opencode go?
    - **u/Harshith_Reddy_Dev** (↑5, 2026-10-17 13:15): [https://opencode.ai/data/deepseek/deepseek-v4-1-flash](https://opencode.ai/data/deepseek/deepseek-v4-1-flash)
        
        Not yet
        
        https://preview.redd.it/igz9oxud21wh1.jpeg?width=1239&format=pjpg&auto=webp&s=6d05bc0e2acf44974ae7b770e8f314c35b03fd56
      - **u/HsSekhon** (↑1, 2026-10-17 13:38): Thanks for sharing, I wasnt upto date with this.
        - **u/Harshith_Reddy_Dev** (↑2, 2026-10-17 13:39): It just released now so it'll take 2-3 days I guess
- **u/amo_pessoas_peladas** (↑1, 2026-10-17 17:36): What is funny for me about DeepSeek is that it can be both as good as advertised and completely crazy if not properly harnessed at the same time. 
    
    Like, it can sometimes find very hard bugs and create very complex applications very fast costing like a dollar and then, out of nowhere, start writing complete random bullshit and ignoring clear instructions out of nowhere.
    
    It's probably due to distillation. I'm not complaining and I'm getting way more done with it on my personal projects than with my job's Claude subscription with a mind-blowing 2 orders of magnitude less cost. Claude's gotten way better now price-wise due to opus 5.5, but it's still way costlier.

---

## opencode.json for any OpenAI-compatible endpoint + 3 things that tripped me up with Qwen3.8-27B
**u/IteraCompute** · 2026-10-17 07:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x844bl/opencodejson_for_any_openaicompatible_endpoint_3/)

[removed]

---

## DeepSeek V4.1 Flash 1017 is silently rolling out? 😲
**u/afanasenka** · 2026-10-17 07:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x83wll/deepseek_v41_flash_1017_is_silently_rolling_out/)

...

**Comentarios:**

- **u/squirrelscrush** (↑2, 2026-10-17 07:48): Big if true
- **u/anxious_and_stupid** (↑2, 2026-10-17 10:44): Post trained 4.1 flash ??

---

## Melhor alternativa gratuita ao Muse Spark 1.3?
**u/Striking-Mix-1584** · 2026-10-17 02:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x7ypix/melhor_alternativa_gratuita_ao_muse_spark_13/)

---

## OpenCode’s Code Mode Fixes MCP’s Biggest Problem
**u/RelevantEmergency707** · 2026-10-17 02:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x7yn9p/opencodes_code_mode_fixes_mcps_biggest_problem/)

---

## Synthetic.new's latest plans designed to compete with OpenCode Go
**u/jpcaparas** · 2026-10-17 00:24 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x7wggj/syntheticnews_latest_plans_designed_to_compete/)

Synthetic now has three plans: Go at $9 a month, Standard at $30 and Big at $90. Every plan gets extra usage at API pricing, discounted models, the Web Search API and beta models. Big adds Fast mode (up to 2x faster) and Infinite mode, where background agents never hit your rate limit.

**Comentarios:**

- **u/ketsif** (↑7, 2026-10-17 00:38): do you have any numbers other than cost
  - **u/tomz17** (↑3, 2026-10-17 00:45): Looks like it's this table (i.e. subscribers just get a "discount" off api pricing for their presumably $ amount. 
      
      https://preview.redd.it/9uxbtcoicxvh1.png?width=918&format=png&auto=webp&s=d7fc05130a57db7d670c31dfc7c9b16cc5acb3db
    - **u/ketsif** (↑1, 2026-10-17 00:56): OK so that price difference is the factor for what the sub gets you per model? guessing they don't have pesk/offpeak or anything based on that picture
- **u/new_to_edc** (↑3, 2026-10-17 00:46): Looks like DS4.1F got cheaper, K3 got more expensive.
- **u/RepulsiveRaisin7** (↑3, 2026-10-17 01:07): Solid but cost-wise it's not really competitive with (multiple) Opencode Go plans
- **u/Useful_Math6249** (↑1, 2026-10-17 01:52): hope they improved their models, GLM and DeepSeek were pretty awful there, every two sessions there were reasoning loops (even under 200k tokens)
- **u/TheMythicSorcerer** (↑2, 2026-10-17 05:21): Intresting but doesnt seems as competitive as commandcode
- **u/Rustybot** (↑1, 2026-10-17 20:50): Mostly a 2x multiple, in exchange for assumingly quantized and rate limited models vs api price. Not great. I guess it’s an okay price for deepseek on low. The smallest multiple is on output tokens, so those hyper-verbose reasoning Chinese models will cost you if you set them to high/max, or, you know, just regular Kimi settings.
- **u/oNever** (↑3, 2026-10-17 14:58): Through OpenCode Go you pay $10 and get $80... that is an 8x, not 80x.
    
    Synthetic Go gets you ~7.5x by their own blend estimate at 90/9/1 cached/input/output.

---
