# r/opencodeCLI — hilos 2026-10-18 → 2026-10-20
_Generado: 2026-10-19T00:11:07.396742+00:00 · 20 hilos · 32 comentarios · fuente: Arctic Shift_

## Microsoft azure network is banned??
**u/Robert__Sinclair** · 2026-10-18 19:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9bs1j/microsoft_azure_network_is_banned/)

---

## OpenCode 2.0 Released: The #1 Open-Source Coding Agent
**u/RelevantEmergency707** · 2026-10-18 18:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9aml3/opencode_20_released_the_1_opensource_coding_agent/)

---

## PLUGIN PARA USO DE CUOTA GO, CLINE, CODEX
**u/sanabria1927** · 2026-10-18 18:30 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x9ajdq/plugin_para_uso_de_cuota_go_cline_codex/)

---

## the new version gave plan mode too much freedom
**u/megablue** · 2026-10-18 17:56 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x99omg/the_new_version_gave_plan_mode_too_much_freedom/)

well, the plan mode figured out ways to modify files by calling the skill i just asked it to write. it went outside of the project directory and modified files that wasn't supposed to modify.

**Comentarios:**

- **u/tsangberg** (↑1, 2026-10-18 18:01): The only way to not risk having the model do things it shouldn't is to use a proper sandbox. Everything else is just asking the model to please behave.
    
    I made my own, feel free to be inspired or fork (it's CC0). There are many like it - and all of them will be better than plan mode :)
    
    [https://verified.technology/](https://verified.technology/)
  - **u/megablue** (↑1, 2026-10-18 18:07): this is at least the 3rd or forth time i caught opencode cli's plan mode modify files that it wasn't supposed to...
- **u/BrightAIFuture** (↑1, 2026-10-18 18:35): There are two separate issues here: containing damage and checking whether plan mode honours its advertised behaviour. A sandbox can contain an unexpected write; that does not establish that plan mode behaved correctly.
    
    
    
    For a reproducible test, I’d use a throwaway project and a harmless canary file in a sibling directory, then record which tool/skill attempted the write and whether it actually changed the file. Include the exact OpenCode version, relevant permission configuration and tool trace, with secrets removed. That gives maintainers something narrower than “the model ignored the rules” to investigate. Keep the real files isolated while testing.
    
    
    
    AI-assisted suggestion; I run Bright. I haven’t reproduced this report or established its cause.
  - **u/megablue** (↑1, 2026-10-18 18:40): i asked it why, apparently it was my own fault, i wrote a new context management but the system prompt/notice got lost and never reinjected back to the context.
    - **u/BrightAIFuture** (↑1, 2026-10-18 19:04): That narrows the next test to the context-manager transition. I’d compare the same harmless fixture with the stock context path and with your plugin, and check that the required notice is present before the first tool call after compaction/resume. The model’s explanation is a lead to verify, not proof of the failure path. If only the plugin run loses the notice, that is much stronger evidence about where to fix it. AI-assisted follow-up.
- **u/plmtr** (↑1, 2026-10-18 22:43): I guess I've also learnt that less/carefully curated skills are better.
    
    And !skillNotToUse on the agents you need to curtail

---

## What if Subscriby become Opensource?
**u/moneytvdaily** · 2026-10-18 17:49 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x99hmr/what_if_subscriby_become_opensource/)

---

## What if Subscriby become Opensource?
**u/moneytvdaily** · 2026-10-18 17:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x99fgn/what_if_subscriby_become_opensource/)

---

## Deepest new model
**u/rvctech** · 2026-10-18 15:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x95i6y/deepest_new_model/)

---

## OpenCode’s Console incident: more defensive capability needs less unchecked permission
**u/BrightAIFuture** · 2026-10-18 14:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x94pyw/opencodes_console_incident_more_defensive/)

Disclosure: I run Bright. This is our analysis/opinion, prepared with AI assistance, not an independent forensic investigation or a hands-on test of the tools discussed.



Dax Raad’s newer statement says the team needs agents operating around the clock while responding to sustained attack attempts. That is an attributable account; it does not establish the original intrusion mechanism or prove an agent performed it.



Three boundaries matter here:



1. The hosted Console service holding provider credentials and a local OpenCode client are different trust arrangements. A local client is still software with file, shell and network access.



2. Approval prompts can help a user notice an action, but OpenCode’s own security policy says they are not an OS sandbox.



3. Finding more plausible flaws is not the same as repairing more verified flaws. Someone must own validation, fixes, tests and rollback.



My argument is to expand access to defensive tools while keeping their authority narrow: named target and owner, isolated workspaces, credentials limited to the task, enforcement outside the agent and human review before consequential action. Measure repaired issues, exposure time and false alarms.



NVIDIA’s OpenShell is relevant to the outside-enforcement idea; we have not tested it and do not claim it would have prevented this Console event.



Sources: https://github.com/anomalyco/opencode/security/policy ; https://github.com/NVIDIA/OpenShell ; Raad’s attributed update https://x.com/thdxr/status/2111790511409258796 . Fuller argument, incident caveats and counterarguments: https://brightaifuture.com/discoveries/stop-slowing-down-ais-defenders



Which separation has made the biggest practical difference in your own setup: credentials, filesystem access, outbound network policy, or review before changes reach production?



Image: Bright editorial quote card; founder’s account, not independent forensics.

**Comentarios:**

- **u/veculus** (↑9, 2026-10-18 14:40): thanks claude
- **u/dryadofelysium** (↑5, 2026-10-18 14:51): holy slop. the new OpenCode incident is due to a hole/security issue in their implementation of SSO/login with differnet providers that led to stolen API keys. nothing here has anything to do with (local) AI/LLM sandboxing or safeguards
  - **u/BrightAIFuture** (↑0, 2026-10-18 15:14): Fair criticism of the framing. A local sandbox is not a remedy for provider keys exposed by a hosted service, and I’m not claiming OpenShell or agent permission prompts would have prevented this incident.
      
      
      
      I should have separated the immediate hosted-credential issue more clearly from the broader defensive-agent argument prompted by Raad’s later statement. The article does not establish the entry vector; it treats that as unresolved in the evidence reviewed. The concrete response to a key believed exposed is revocation at its issuer and review of usage. Local isolation addresses a separate risk.

---

## Consejos para un novato
**u/OwnSystem1633** · 2026-10-18 14:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x94it8/consejos_para_un_novato/)

---

## Muse Spark 1.3 Contributor
**u/mustafsyria2011-afk** · 2026-10-18 14:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x941s2/muse_spark_13_contributor/)

[removed]

---

## OpenCode Error
**u/Affectionate-Fun-623** · 2026-10-18 13:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x92qt7/opencode_error/)

---

## Hermes vs muse ai
**u/ArtAdventurous5863** · 2026-10-18 12:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x92jr7/hermes_vs_muse_ai/)

---

## Hermes vs muse ai
**u/ArtAdventurous5863** · 2026-10-18 12:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x92gtx/hermes_vs_muse_ai/)

---

## Anyone else using Uptokey’s TUI as a local-first alternative / companion to OpenCode? (free AI tier + same system), we have a Tauri,a vs code extension and maybe more, visit us.
**u/Severe-Apartment3609** · 2026-10-18 12:25 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x91yrb/anyone_else_using_uptokeys_tui_as_a_localfirst/)

[removed]

---

## [Help needed] Permission issues in local installation with Qwen3 coder? Terminal instead of Tool use.
**u/CitrusGames** · 2026-10-18 11:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x916bl/help_needed_permission_issues_in_local/)

Hello together, 

I have successfully set up a qwen3-coder installation, and use Ollama with opencode.

I can successfully interact with the model and receive valid answers, but for some reasons can not get Qwen to actually write to a file. 

I have once or twiced got a [readme.md](http://readme.md) to be filled with arbitrary information, but not reliable.

The model clearly tries to do a tool call, but is not succesful, and write to the CLI:

    <function=write>
    <parameter=path>
    hello.c
    </parameter>
    <parameter=content>
    #include <stdio.h>
    int main() {
        printf("Hello, World!\n");
        return 0;
    }
    </parameter>
    </function>
    </tool_call>

Does anybody has any experience with these issues? Or can at least determine, wether this is a **Qwen3**, an **opencode**, or an **ollama** issue?

  
If you need additional Information, let me know! 

And thanks <3

**Comentarios:**

- **u/SirRobinBlibs** (↑1, 2026-10-18 21:52): This is almost always context length, not permissions. Ollama's default context window is small, and OpenCode's system prompt plus tool definitions don't fit, so they get truncated. The model then only half-knows the tool format and writes the call out as text. Raise it, either with `OLLAMA_CONTEXT_LENGTH=32768` before `ollama serve` or with a Modelfile containing `PARAMETER num_ctx 32768`, then restart. Also make sure the model in your opencode.json is pointed at Ollama's OpenAI-compatible endpoint (`http://localhost:11434/v1`) with tool calling enabled for it. If it still flakes, try a larger quant. Small quants of coder models get much worse at structured tool calls.

---

## hi is anyone facing this
**u/edengilbert1** · 2026-10-18 11:09 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x90l4f/hi_is_anyone_facing_this/)

---

## I got banned from OpenCode's free tier 😂
**u/DarkStyleV** · 2026-10-18 10:12 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8zn99/i_got_banned_from_opencodes_free_tier/)

https://i.redd.it/zb7jmmrz87wh1.png

https://i.redd.it/ipiy8ux197wh1.png



I was just casually developing a game in Unity (btw, their Unity CLI is actually pretty cool).

I had **Sol 6** running as my main agent, with **DeepSeek V4.1 Flash Free** handling the subagents.

Left it running, went AFK for about an 3 hour, and came back to this:

**403 Rejected**

>OpenCode's free tier can only be used from within OpenCode.

Has anyone else run into this? Is there some kind of hidden usage limit, or did I accidentally trigger their abuse detection?   
(Version is latest 2.0.32)  
  
**Note:** I'm not complaining about OpenCode or expecting unlimited free usage. I just switched to a paid API and continued working as usual. Just wanted to highlight this issue since the error message seems pretty misleading, especially when you're actually using OpenCode itself.

**Comentarios:**

- **u/Strict-Prune-879** (↑1, 2026-10-18 10:16): déjà ces pas illimité ceux qui on l'abonnement opencode go la limite de mémoire est de 200 requêtes pas jour et pour ceux qui ne l'ont pas je ne sais pas ca doit etre très bas en sachant que selon les modèles ca puise plus vite.
- **u/NorthExtreme9270** (↑0, 2026-10-18 10:50): Have same problem
- **u/pungat_** (↑1, 2026-10-18 10:53): opencode adds a new layer to its free model checks, increasing the total from about ~4 layers to ~6.
- **u/Ok_Necessary7506** (↑14, 2026-10-18 10:53): "banned"? Why do you think you're banned?
  - **u/DarkStyleV** (↑-5, 2026-10-18 13:25): https://preview.redd.it/hcyqtxsy88wh1.png?width=1154&format=png&auto=webp&s=482384b0d9057357512633d0962d6b7e540312b5
      
      because they block my request by ip, for any free models
    - **u/Ok_Necessary7506** (↑4, 2026-10-18 14:13): But this message is completely different from the one in your original post.
- **u/lewwdsv1** (↑3, 2026-10-18 11:03): Not a ban.
- **u/sirloindenial** (↑1, 2026-10-18 11:06): So this is in something other than opencode, then it makes sense. What's weird is you were still able to use it until today, cause they tighten it around 2-3 weeks ago for use in third party. Not a ban, you can test by opening opencode now.
- **u/avinthakur080** (↑8, 2026-10-18 11:09): It is not a ban but likely a bug. I've seen it many times.
    
    Sometimes, it works after a restart, other times, it is more arrogant and demands a new session.
  - **u/DarkStyleV** (↑0, 2026-10-18 13:26): https://preview.redd.it/33t51uc998wh1.png?width=1563&format=png&auto=webp&s=75684255425e73bf80516ceb33285bc6a8c0b6bc
      
      new session didn't help , reastart and resinstall aswell
    - **u/avinthakur080** (↑1, 2026-10-18 13:28): [https://www.reddit.com/r/opencode/comments/1x92qoh/opencode\_error/](https://www.reddit.com/r/opencode/comments/1x92qoh/opencode_error/)
        
        Looks like a common issue.
        
        I am also getting the same. On restart, it worked for a few seconds but started giving this error after some time.
      - **u/DarkStyleV** (↑1, 2026-10-18 13:30): Okay, then just need to wait, thx for the info
- **u/ollm-tux** (↑0, 2026-10-18 11:13): never work free tiers with another harness, if u want free try orcarouter (have ds free now), openrouter and kilo
- **u/CookieAway995** (↑-1, 2026-10-18 11:29): You are not banned your Ip is blacklisted, You can change ip and try
- **u/imran-bd12** (↑0, 2026-10-18 11:35): facing same problem
- **u/nkkfu** (↑1, 2026-10-18 13:38): Unity CLI? What do you mean? Is it possible to make changes in unity editor without the GUI?
- **u/HyperWinX** (↑1, 2026-10-18 14:26): Bug*  
    Not a ban
- **u/Fantastic_Gate_6806** (↑0, 2026-10-18 15:02): Does opencode free tier actually works with lets say clsudd code? I thought we could only use opencode models within opencode?
- **u/sascharobi** (↑1, 2026-10-18 15:37): Nowhere does it say "ban."

---

## opencode cli not working
**u/pkdme** · 2026-10-18 10:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8zk3c/opencode_cli_not_working/)

---

## open-source tool to fully understand and optimize AI usage
**u/stichstichstich** · 2026-10-18 02:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1x8rhb5/opensource_tool_to_fully_understand_and_optimize/)

I’m a senior SWE using AI coding tools daily. I analyzed my Claude Code transcripts and found **56% of API-equivalent costs went to rereading context**. Cache expiry cost me $98.74 across 35 returns in 27 days, versus $2.95 with a warm cache.

That led me to build **optimAIzr**, which supports Claude Code, Codex and Opencode.

It analyzes usage, flags expensive patterns, helps you find optimization opportunities aaand much more.    
Runs locally, with no account or prompts.

npm i -g optimaizr

git: https://github.com/blendbunjaku/optimaizr

**Comentarios:**

- **u/Gargle-Loaf-Spunk** (↑-3, 2026-10-18 02:10): No
- **u/Soifon99** (↑3, 2026-10-18 06:53): if it works it looks interesting.  I understand the struggle of optimizing in a sea of new models and new home baked tools everyday.
- **u/ozguru** (↑3, 2026-10-18 08:15): Looking cool.

---

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
