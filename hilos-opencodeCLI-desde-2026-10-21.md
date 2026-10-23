# r/opencodeCLI — hilos 2026-10-21 → 2026-10-24
_Generado: 2026-10-23T15:46:06.053363+00:00 · 40 hilos · 71 comentarios · fuente: Arctic Shift_

## OpenCode V2: How can I export a session from one repo and import it into another? Getting Session already exists
**u/sumit_654** · 2026-10-23 15:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xdh6jq/opencode_v2_how_can_i_export_a_session_from_one/)

Hey everyone!

I'm relatively new to OpenCode and still learning how its sessions and context management work, so apologies if I'm missing something obvious.

I'm using OpenCode V2 (`v2.1.2`), and I'm trying to figure out how to carry an existing conversation from one repository into another.

\----------------------------------------------------------------------------------------------------------------------------

**What I'm trying to achieve**

Suppose I'm working in **repo A** and have a long conversation with the coding agent about architectural decisions, code structure, trade-offs, and why we chose a particular approach.

Now, I want to work on **repo B** and continue that discussion using the previous conversation as context. For example, I'd like to ask the agent to inspect repo B and compare its architecture with the decisions we discussed for repo A.

I don't necessarily want to merge the repositories or permanently share context between all my projects. I just want to reuse a particular conversation when it's useful.

\----------------------------------------------------------------------------------------------------------------------------

**What I've tried**

I'm following the official OpenCode V2 CLI documentation:

[https://dev.opencode.ai/v2/docs/cli/commands/](https://dev.opencode.ai/v2/docs/cli/commands/)

The documentation describes exporting a session to JSON and importing it into a specific directory.

  
First, I exported my session:

    opencode session export SESSION_ID > dotfiles-context.jsonopencode session export SESSION_ID > dotfiles-context.json

Then, I tried importing it into the other repository:

    opencode session import \
      ~/Documents/Coding/open-source-repos/dotfiles/dotfiles-context.json \
      --directory ~/dotfilesopencode session import \
      ~/Documents/Coding/open-source-repos/dotfiles/dotfiles-context.json \
      --directory ~/dotfiles

However, OpenCode returns:

    Session already exists
    However, OpenCode returns:Session already exists

Both directories are different, so I initially expected the session to be imported into the destination repository.

I checked the CLI help, and my installed version supports these session subcommands:

* `list`
* `delete`
* `export`
* `import`

The import command also supports `--directory`, but I couldn't find a flag to import the conversation as a new session with a different ID.

\----------------------------------------------------------------------------------------------------------------------------

  
**What I understand so far**

My current understanding is that exporting a session saves its conversation history and associated session data as JSON. Importing it should make that history available in the destination project.

I understand that this doesn't automatically give the agent access to the source repository's files. It would still need to inspect the destination repository to compare the implementations.

I'm also aware that the session ID might be colliding with an existing session, even though the destination directory is different.

# My questions

1. Is there a supported way to import an exported session into another repository as a **new, independent session**, while preserving the original session?
2. Does OpenCode intentionally preserve the session ID during export/import, and is that what's causing this error?
3. Is there a recommended workflow for reusing a conversation's architectural context across repositories without manually copying the discussion into a new prompt?
4. If this isn't currently supported by the CLI, is there another supported approach in OpenCode V2?

I'm still a beginner with OpenCode, so I'd appreciate an explanation of the underlying behavior as well as a working solution. I'd prefer not to edit the session database or manually modify the exported JSON unless that's an officially supported approach.

(also used AI for the post to make it fast and to the point)

---

## Hmm... Hmm... Hmm...
**u/CYCLONOUS_69** · 2026-10-23 14:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xdforl/hmm_hmm_hmm/)

---

## Quota gone in 30 minutes? How to see what OpenCode is actually sending every turn
**u/SirRobinBlibs** · 2026-10-23 12:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xdczmd/quota_gone_in_30_minutes_how_to_see_what_opencode/)

There was a post here recently from someone whose quota used to last all day and now burns out in about 30 minutes, even after switching models. I've been auditing this across harnesses, and the cause is usually per-request overhead, not the task. Here's how to see it in OpenCode.

**Measure first:**

    opencode stats --days 7 --models     # input/output/cache totals and model breakdown
    opencode stats --project ""          # current project only
    opencode mcp list                    # what's connected
    npx ccusage@latest opencode weekly   # third-party, reads OpenCode's local data

If input and cache reads dwarf output, you're paying to re-send context, not to generate code.

**Things that surprised me:**

- **OpenCode reads your Claude Code setup by default.** It loads `~/.claude/CLAUDE.md` and `.claude/skills`. If you've built up a big Claude configuration, it follows you into every OpenCode session. `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1` and `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1` turn that off (`OPENCODE_DISABLE_CLAUDE_CODE=1` turns off both).
- **Every tool call re-sends the session.** One "small" turn with ten tool calls reads the full context about ten times. Long sessions with a few big file reads get expensive fast. A commenter on the original thread said a fresh session alone left their usage flat for an hour of small tweaks.
- **Caches expire.** On Anthropic models, the API's prompt cache lasts five minutes by default, and rebuilding a cold prefix costs many times more than reading a warm one (25x on Opus/Sonnet 5.5 with a 5-minute write). Coming back to a huge idle session is the expensive moment.
- **MCP servers and instruction files add weight to every request.** Trim AGENTS.md and disconnect servers you aren't using.

I wrote this up in more detail, mostly from the Claude Code side but with the OpenCode and Codex equivalents: https://medium.com/@r3dtuxedo/where-did-my-claude-usage-go-auditing-your-agents-hidden-token-tax-95d6ab17b8b6

(Disclosure: I wrote the article. Free to read, no referral links.)

---

## 👀 Kimi K3.1 is coming very soon (already teased by Moonshot AI)
**u/afanasenka** · 2026-10-23 07:27 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xd7dnk/kimi_k31_is_coming_very_soon_already_teased_by/)

Teaser video: [https://x.com/Kimi\_Moonshot/status/2113445757185606062](https://x.com/Kimi_Moonshot/status/2113445757185606062)

Screenshot from the video - [https://pbs.twimg.com/media/HVScyvya8AAY0iT?format=png](https://pbs.twimg.com/media/HVScyvya8AAY0iT?format=png)

**What we know so far:**

\- Kimi K3.1 is actively tested on LMArena under the codename "Kibitz;

\- Kimi K3.1 is very good at 3D, choosing colors, rendering reflections on water, and composition;

\- Kimi K3.1 is probably cheaper than Kimi K3, with better token efficiency.

Waiting for official release soon 😉

---

## Anyone finding DeepSeek V4.1 Flash through Go too slow between requests?
**u/squirrelscrush** · 2026-10-23 06:38 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xd6ke4/anyone_finding_deepseek_v41_flash_through_go_too/)

It's been the case for a few days. The actual output is quite fast. But it waits too long between requests like it's being timing out.

It usually happens in the morning where I live, so the non-peak between the first and second peak timings.

---

## devin fusion for opencode (and some other useful stuff for opencode)
**u/lemon07r** · 2026-10-23 06:00 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xd5xt0/devin_fusion_for_opencode_and_some_other_useful/)

I was taking a look at how some different fusion modes work, namely junie mix, openrouter's fusion, devin fusion and a few others. Devin's fusion mode was relatively one of the more simpler designs, but after testing all of them for a different project I was building (github actions for PR reviews, and selfhosted PR review github app like coderabbit, but built around my code-indexing tool vera, and sort of inspired by or a rust version of droid actions) devin's fusion mode was a combination of the fastest, cheapest and least amount of false positives. you can find the project and some of the testing results here [https://github.com/VeraTools/revera](https://github.com/VeraTools/revera)

I built my own version for opencode and have been iterating on it based on how it's worked over my past sessions for the last month or longer. So far it's working pretty well, and I thought I'd share if anyone else was interested. This was loosely built around how fusion mode works in devin cli (you can crack open the binary yourselves and take a look too; it's pretty interesting): [https://github.com/lemon07r/opencode-fusion-mode](https://github.com/lemon07r/opencode-fusion-mode)

My own setup after tweaking and trying a lot of things is just mostly vanilla opencode 2 with search provider pinned to exa (with fall back to parallel [https://github.com/lemon07r/opencode-exa-parallel](https://github.com/lemon07r/opencode-exa-parallel)) + vera ([https://github.com/VeraTools/vera](https://github.com/VeraTools/vera)) + my friends smart compaction tool ([https://github.com/shariqriazz/opencode-smart-compaction](https://github.com/shariqriazz/opencode-smart-compaction) which he built based on a lof other cli, and when I personally tested it, it had the best balance of accuracy and token usage compared to other compactions, with droid's following closely) and the devin fusion-like plugin I shared above. My setup is tuned around token efficiency and getting the best results for less. I think simpler setups work better, and always have in most of the evals I've run, which is why I avoid crap like omo. No MCP servers. I do use skills and CLI like Playwright CLI + skills, but most of them are project-scoped rather than global.

I do have a small discord community for discussing this sort of stuff, and a lot of us share tips and stuff there if anyone is interested in joining, although this wasn't the point of the post: [https://discord.gg/rXNQXCTWDt](https://discord.gg/rXNQXCTWDt)

---

## Brooo, where did MiniMax M3.1 Flash go? 💀
**u/AffectionateFuel4611** · 2026-10-23 04:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xd4trf/brooo_where_did_minimax_m31_flash_go/)

---

## Opencode deberia hacer esto?
**u/Ok-Committee1844** · 2026-10-23 04:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xd4mmu/opencode_deberia_hacer_esto/)

---

## Opencode go limit exhaustion : what have you built?
**u/anantshri** · 2026-10-23 02:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xd1idf/opencode_go_limit_exhaustion_what_have_you_built/)

---

## i built kimo so your coding agent can render a single frame to check its own edit - free open-source video editor you drive over mcp
**u/LieTop7965** · 2026-10-22 22:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcwnm8/i_built_kimo_so_your_coding_agent_can_render_a/)

hey - i built kimo, a free open-source (mit) video editor with no gui that your ai coding agent drives over mcp. the idea is simple: you tell your agent (opencode, codex, cursor, or any other mcp client) what to do and it drives the whole timeline as tool calls - cut, trim, keyframes, titles/captions, colour grade, particles, audio, export. a nice bit that makes this actually useful is that the agent can render a single frame back to itself to visually check its own edit before committing, so the loop is self-correcting instead of blind.

under the hood it's one ~15 mb cpu-only rust binary, no gpu, no containers - i run it on a 2 gb box and it just works. i'm naman, a college student, and i built it, so a few things are still rough: there is no ui (there's nothing to open, by design), some edge cases in tracking and captions are still janky, and a couple of export codecs need patience. i'd really rather hear what breaks than pretend it's polished, so if you point an agent at it and tell me where it trips, i'll fix it.

site: https://getkimo.tech
github: https://github.com/naman-sharma12345/kimo

---

## Seeing a new Flint 40B free model in my console
**u/warpaint_james** · 2026-10-22 18:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcqg56/seeing_a_new_flint_40b_free_model_in_my_console/)

---

## OpenCode V2 TUI sidebar file tree plugin
**u/FoundationOwn8281** · 2026-10-22 16:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcn6wt/opencode_v2_tui_sidebar_file_tree_plugin/)

Just published an OpenCode V2 plugin that adds a sidebar file tree. Features:

\- Tree of the current session's working directory

\- Click folders to expand/collapse; click files to preview first 200 lines

\- Right-click a folder → Set session working directory here to move the session

\- /tree-move-here moves the session to the last clicked folder (keyboard-friendly)

\- /tree-expand / /tree-collapse palette commands

\- Filter by name with /tree-filter <name>

\- Expand/collapse all from the header  


Install:

git clone [https://github.com/zemadeiran/opencode-file-tree-v2](https://github.com/zemadeiran/opencode-file-tree-v2) \~/.config/opencode/plugins/file-tree

Then add to opencode.json:

{"plugins": \["/Users/you/.config/opencode/plugins/file-tree"\]}

Note: opencode plugin add github:zemadeiran/opencode-file-tree-v2 currently fails with a JSX transform error (issue #33884). Use the local path install.

MIT license.

The plugin loads the session's working directory, supports expand/collapse, right-click move, and filter. Good for quick file navigation without leaving the terminal.

---

## Opencode 2 stable?
**u/Ace-_Ventura** · 2026-10-22 12:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcgor3/opencode_2_stable/)

I've seen posts and the official installer defaults to v2. However, github shows that v1 is still the version released, with v2 only shown in tags.

Since this is kinda contradictory, is v2 stable or not?

---

## Why I left OpenCode for Pi, then came back for v2
**u/rizal72** · 2026-10-22 12:02 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcgnpr/why_i_left_opencode_for_pi_then_came_back_for_v2/)

Long ago, when I started with **OpenCode v1**, I kept hitting the same wall: I wanted my own widgets — my provider stats, my prices, my layout — and there was no clean way to get them, without bloating things.

So I moved to **Pi**. Bare-bones was the feature: minimal surface, everything customizable, and I built exactly what I wanted on top of it: made it "my" Coding Assistant. That worked for a long time.

Then **OpenCode v2** shipped a real plugin API, and I realized the same job could be done there: panels, footer badges, sidebar blocks, custom commands, applied live while the TUI runs. I rebuilt my Pi setup: a context/usage block that changes color as the window fills, a git status block, a budget widget that reads the Go credit and the peak-hour tariff plus my other providers budgets, a plugin+widget that keeps the Mac awake while the agent works, a ponytail level indicator, a complete sub-agents delegation framework using just built-in tools, so no need for external plugins, and a **custom model picker**.

That last one is the one I'm proudest of: **/models-pro**. The native picker just lists models, this one lists prices, context windows, an intelligence index, the Go credit and each model's multiplier, sorts by what a request actually costs, and keeps favorites. It isn't a wrapper around the native dialog: it's the native function, extended.

**But the number that made my choice was another:** weight of the **first prompt** in a clean project. Same tools, same extensions, same widgets, all I need for my work, with Pi I never got it as low as I get it in OpenCode v2. To try to lower it I became a master of the *codemode:only* mode in Pi — but the trade was brutal: some tools get hidden and the model ends up using bash and Python scripts for everything. I switched between *codemode* "*on*" and "*only*" a lot and the minimum I got was 13k in mode "*only*" and 28k in mode "*on*".

On OpenCode v2, with all of the above installed, I sit around 11k. Lower, and nothing hidden. Everything works. Same tools, same widgets, plugins, extensions, all accessible. No compromises.

**So:** Pi's minimalism and extensibility, plus proper context/tools/token/cache handling out of the box: that's the combination I was after. v1 was heavy and rigid; v2 lets me do what Pi let me do, without giving up the rest. Even knowing that it is still an early release and I already had to modify my plugins a few times after new releases ;)  
That said, Pi remains the first choice for anything that needs the lightest and fastest Harness possible.

**Final note:**  
I'm deliberately not mentioning OpenCode's move about free models, available only through OpenCode, not to other agents: that's marketing, not engineering (and I get why).

*Two screenshots:* the TUI with my custom widgets annotated, and my custom model picker.

---

## DeepSeek V4.1 Flash 1017: OpenCode Zen vs OpenRouter — which is cheaper?
**u/vishu143x** · 2026-10-22 11:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcg81a/deepseek_v41_flash_1017_opencode_zen_vs/)

I’m planning to use only \*\*DeepSeek V4.1 Flash 1017\*\* with OpenCode for a couple of months.  

Which is cheaper in practice: \*\*OpenCode Zen or OpenRouter\*\*?

Open router :

In / Out Price

$0.07 / $0.50per 1M

Opencode :

\*\*$0.30  /$1.20\*\* per 1M

Deepseek API platform :

$0.15 input / $0.60 output (off-peak)

$0.3 input / $1.2 output (peak)

\*\*it seems like Opencode costly , Am i missing anything here ?\*\*

\*\*reference\*\*  

\[https://opencode.ai/data/deepseek/deepseek-v4-1-flash-1017\](https://opencode.ai/data/deepseek/deepseek-v4-1-flash-1017)

\[\*\*https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017\*\*\](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017)

\[\*\*https://api-docs.deepseek.com/quick\\\_start/pricing\*\*\](https://api-docs.deepseek.com/quick\_start/pricing)

---

## I use a VPN and have done for a very long time. I now can't use Opencode free because as soon as I open it, it tells me that the daily limit has been reached
**u/Deep_Imagination_811** · 2026-10-22 08:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcd8ld/i_use_a_vpn_and_have_done_for_a_very_long_time_i/)

I think the IP detection may be a bit over zealous?

**Comentarios:**

- **u/No_Captain4899** (↑2, 2026-10-22 09:03): Because other people are abusing of the freetier with their VPN as the free tier is based on your IP, so when people exausted their limit on their local IP, they activated their VPN to use the free tier and so on
  - **u/Deep_Imagination_811** (↑2, 2026-10-22 09:14): So: VPN and no opencode?
    - **u/No_Captain4899** (↑2, 2026-10-22 09:18): So VPN and you pay for opencode go or no VPN and you can use the free tier
      - **u/Deep_Imagination_811** (↑-3, 2026-10-22 09:24): why call it "free tier" when it's "free tier only for non-VPN users"
        - **u/Grouchy-Stranger-306** (↑2, 2026-10-22 09:27): how else do you want them to enforce limits? it's free with limits based on ip, it's not their problem that you use an ip that another person already abused limits on
        - **u/WalkAffectionate2683** (↑1, 2026-10-22 10:01): At worse just don't use the vpn on opencode and you are fine. You can exclude apps
- **u/Admirable-Cell-2658** (↑0, 2026-10-22 09:40): I use VPN to and works, just change to another server ip.

---

## SummonOS: an Omarchy-inspired macOS environment
**u/Comfortable_Cat_6207** · 2026-10-22 05:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xcajfk/summonos_an_omarchyinspired_macos_environment/)

---

## more performant coding agent
**u/Medium_Anxiety_8143** · 2026-10-21 23:37 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xc30wo/more_performant_coding_agent/)

---

## using different ip doesn't work anymore ?
**u/girlkiller1** · 2026-10-21 23:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xc2xr4/using_different_ip_doesnt_work_anymore/)

When i hit the free rate limit changing my ip doesn't reset the thing anymore..

---

## Qual a melhor configuração multiagente do OpenCode usando ChatGPT Plus e modelos gratuitos?
**u/Negative_Macaroon_85** · 2026-10-21 22:55 UTC · ↑1 · 2 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xc23d3/qual_a_melhor_configuração_multiagente_do/)

Estou usando o OpenCode Desktop com o ChatGPT Plus, principalmente para Power Apps, Power Automate e outros projetos de desenvolvimento. Estou tentando construir um fluxo de trabalho multiagente usando modelos livres robustos para tarefas mais simples, enquanto reservo os modelos GPT para trabalhos complexos, sem esgotar meus limites de uso. Minha ideia de configuração atual é:

\*\*Orchestrator (GPT-6 Luna):\*\* Coordenação de tarefas e gerenciamento de agentes.

\*\*Luna (GPT-6 Luna):\*\* Investigação, depuração e análise.

\*\*Reviewer (modelo de raciocínio robusto):\*\* Revisão de código, segurança e verificações de regressão.

\*\*Sol (GPT-6.1 Sol):\*\* Codificação, correções e implementação.

\*\*Astra (GPT-6 Astra):\*\* Arquitetura e refatoração complexa.

Também estou com dificuldades para organizar o arquivo \[AGENTS.md\](http://AGENTS.md), as configurações dos agentes, as habilidades e os relatórios em Markdown sem desperdiçar contexto ou criar documentação redundante. Alguém já criou uma configuração semelhante? Quais modelos gratuitos vocês recomendariam para essas funções e como distribuiriam as tarefas para aproveitar ao máximo uma assinatura ChatGPT Plus? Estou aberto a mudar toda a arquitetura se houver uma abordagem melhor.

**Comentarios:**

- **u/No-Mention-9653** (↑1, 2026-10-22 05:39): Plan machen mit sol in einer md file -> in Phasen unterteilen -> mit Luna Implementierung 
    
    Reicht meiner Meinung nach
- **u/mubaidr** (↑1, 2026-10-22 13:15): I use my own simple orchestrator based setup: https://github.com/mubaidr/gem-team
    
    Plan>implement>review

---

## Experimenting with a plugin to track my tasks on the sidepanel
**u/Rovax** · 2026-10-21 21:15 UTC · ↑14 · 2 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbzp3l/experimenting_with_a_plugin_to_track_my_tasks_on/)

Working on yet-another-task-tracker tool and I have been experimenting with having a side panel integration, and it feels really nice to be able to keep track of what tasks my agent mentions, as well as what he is actually working on in the current session

**Comentarios:**

- **u/Vast_Anxiety3133** (↑6, 2026-10-21 21:19): The Todo list is integrated in 2.1+
  - **u/Rovax** (↑2, 2026-10-21 21:42): yes, which is a per-session markdown for the agent to keep track of immediate work.
      
      this is for broader work management that is actually independent of opencode client, so other models and clients can collaborate on the same board and the panel keeps me up to date

---

## Remote OpenCode runs with Archestra 1.4. OpenCode could hand tasks to OpenCode on own Kubernetes cluster
**u/motakuk** · 2026-10-21 20:15 UTC · ↑2 · 4 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xby541/remote_opencode_runs_with_archestra_14_opencode/)

With the latest Archestra release, this workflow became possible: OpenCode on my laptop hands a task to OpenCode running in Archestra's runtime on my Kubernetes cluster, then pulls the patch back. OpenCode is both the local client and a built-in runtime agent, so both ends behave the same.  
  
How a handoff goes:  
\- Tell local OpenCode "hand this over to Archestra". The skill has it write a short handoff note first (the goal, what was decided, what remains, how you'll know it's done), then bundles the exact commit, a patch, and the untracked files you choose.  
\- Remote OpenCode picks it up in its own container, files persist, and you get a live terminal. Close the laptop, send follow-ups later.  
\- To pull it back, say "bring it back and continue here". What comes back is an incremental patch, and nothing gets applied until you have read it.  
  
Blog: [https://archestra.ai/blog/new-remote-agents](https://archestra.ai/blog/new-remote-agents)  
Repo: [https://github.com/archestra-ai/archestra](https://github.com/archestra-ai/archestra)

**Comentarios:**

- **u/poop_report** (↑3, 2026-10-21 20:20): welcome to last year
- **u/TheMythicSorcerer** (↑1, 2026-10-22 03:48): See... uhh codex has a built in cloud button and you just click it and it keeps running after you close your computer already no github repo needed. 
    
    And you also don't really need a paid VPS lots of AI subs (no not opencode because you need a server for that, but yes claude code and codex) lets you run tasks on their cloud compute...
  - **u/motakuk** (↑3, 2026-10-22 15:14): the idea is that sometimes you want to run them in your cloud, not theirs
    - **u/TheMythicSorcerer** (↑1, 2026-10-22 15:15): Technically still not your cloud if you use a VPS instead of self hosting.

---

## Need help for my first videogame
**u/Local-Item-2241** · 2026-10-21 19:40 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbx755/need_help_for_my_first_videogame/)

Hi! As I mentioned in the group, I’m trying to make a strategy game (the gameplay clip attached is what I’ve come up with in one week using OpenCode and Claude for the code), and I want to keep working on it.

I’m thinking about buying a Claude Pro subscription to start working on more specific things like 3D modeling, but I’m not sure if that’s the best option. I’m looking for something more polished in terms of interfaces, UI, and animations, so I’m not sure if Claude Pro would be the right choice or stick with OpenCode.

---

## Should I stick with OpenCode or switch to DS?
**u/GervolkS** · 2026-10-21 19:38 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbx58m/should_i_stick_with_opencode_or_switch_to_ds/)

---

## guys i used use vpn when i hit the limit of Free usage exceeded, subscribe to Go ,but now that doesnt work ,do you anything could help
**u/One_Grapefruit_2948** · 2026-10-21 17:59 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbufcr/guys_i_used_use_vpn_when_i_hit_the_limit_of_free/)

[removed]

---

## Best subscription in 10$?
**u/Nunu_Chus** · 2026-10-21 17:41 UTC · ↑2 · 20 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbtxj0/best_subscription_in_10/)

Is opencode go with ds 4.1 flash the best subscription in 10$? Or there are other options? I use pi.dev harness btw.

**Comentarios:**

- **u/Strict-Prune-879** (↑0, 2026-10-21 17:44): code command
  - **u/No_Committee8392** (↑3, 2026-10-21 17:49): I’ve seen this a lot what are the benefits over oc go? Can i use it elsewhere?
    - **u/Toad__Sage__** (↑3, 2026-10-21 17:58): I use both. I feel I can use models which don't have most usage without much thinking abt the usage. I really like mimo 2.6pro and it's actually cheap but most I can get from oc go is 15 dollars while on cc I can use 20 dollars worth of tokens and still have 50 dollars worth usage left for other models
      - **u/squirrelscrush** (↑1, 2026-10-21 19:19): If you use the whole quota of one model, you can't use other models. Since it's based on the usage percentage.
        - **u/Toad__Sage__** (↑1, 2026-10-21 19:50): Yeah ik. That was the part I told like cc more
          - **u/Odd_Abrocoma_8421** (↑1, 2026-10-22 09:48): So CC doesn't have that?
            - **u/Toad__Sage__** (↑1, 2026-10-22 10:33): no. it's on dollar usage and not % usage. You may complete usage of one model but if that was <70dollars, you still can you remaining amount on other models
- **u/squirrelscrush** (↑5, 2026-10-21 17:48): This is an OpenCode subreddit so it'll be biased towards the Go subscription lol. There are some others like Command Code and there are some I forgot the name...
    
    Although I use OpenCode Go and I find it satisfactory for what it is.
  - **u/Odd_Abrocoma_8421** (↑1, 2026-10-22 09:46): Opendesign
- **u/Odd-Elderberry-6328** (↑2, 2026-10-21 18:12): For 10 there is opencode and commandcode, both are good
    
    The devs behind opencode are open to feedback and sometimes answer the community, they don't fear criticism, the same cannot be told by the devs behind commandcode
    
    Also, opencode as a harness is much better then anything else on the market in my opinion, so I see go as a way to finance the development 
    
    Both options are really good, and if you don't mind the devs being less open to criticism, commandcode is slightly better, if you prefer a little more transparency (but don't expect much) opencode is better
  - **u/squirrelscrush** (↑1, 2026-10-21 19:20): In terms of DeepSeek Flash both are the same. OpenCode has insane Muse Spark 1.3 Contributor usage, while CC has better GLM 5.3 Flash usage.
- **u/dizvyz** (↑0, 2026-10-21 18:48): I tried ollama cloud and command code and decided that if anything they are NOT better than opencode so I might as well stick with that.
- **u/alexanderbeatson** (↑0, 2026-10-21 20:26): OpenCode is ZDR at least on paper.
    
    CommandCode isn’t ZDR by default. You have to enforce it and you will lose your credit like shit with ZDR-on
- **u/hernando1976** (↑1, 2026-10-21 20:35): Creque que estaba opencode desing qué te daba 120dls en ds 4.1 flash, creo, no se como este ahora
- **u/No-Condition5121** (↑1, 2026-10-22 08:09): Opencode Go or Command Code GOAT 
    Depends on which models you use
- **u/NigeriaBoi420** (↑1, 2026-10-21 21:37): Is that a scam cuz its too good to be true

---

## 🔥 Meta Muse Wonder is now available on OpenCode
**u/afanasenka** · 2026-10-21 16:59 UTC · ↑148 · 14 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbsr00/meta_muse_wonder_is_now_available_on_opencode/)

...

**Comentarios:**

- **u/Odd_Abrocoma_8421** (↑1, 2026-10-21 17:01): No contributors free edition??
  - **u/Psychological-Tell83** (↑6, 2026-10-21 18:48): Just take my data, mark zuckerberg
    - **u/sagiroth** (↑1, 2026-10-22 12:26): Your data is already harvested mate. It doesn't matter
  - **u/ApprehensiveEye7387** (↑1, 2026-10-22 01:48): i m a muse code user, there is a contributor mode for it. i tried it and it consumed 5hr limit (35% of weekly) in 2-3 prompts with not much better results than muse spark 1.3 max. for comparison i almost never ran out of usage with muse spark 1.3 max, don't what shit meta made of this new model.
- **u/OldWorldKestrell** (↑35, 2026-10-21 17:05): We still miss spark-1.3-contributor-free :D
  - **u/Shawnanigans** (↑14, 2026-10-21 17:08): It was so good for free.
    - **u/OldWorldKestrell** (↑4, 2026-10-21 17:12): Yeah, it had a nerving behavior to quickly one-shot everything, but as an orchestrated work that was a solid trait.
- **u/migsperez** (↑10, 2026-10-21 17:18): Jeez it ain't reasonably priced
  - **u/Amarsir** (↑2, 2026-10-22 00:10): Arguably a better deal than Grok, but Grok wasn't reasonably priced either.
      
      (To explain, it scores higher than Grok 4.7 in both [Benchmarks](https://artificialanalysis.ai/models/muse-wonder) and [Independent Measurements](https://www.bridgebench.ai/leaderboard). And the price is $4/$20^(\*)  for input/output but only $0.20 on a cache read. Grok charges $2/$6 on in/out but a massive $0.50 on a cache read. Anyone who has done this for a while knows how easy it is to have billions of cache read tokens. 
      
      *(\*) Which is paradoxically a very Elon thing to do.*
- **u/somerussianbear** (↑1, 2026-10-21 17:26): Price?
  - **u/Ok_Topic_3468** (↑6, 2026-10-21 20:31): $4 per mil input, $20 for output. probably one of the worst models you could ever use for the price, it is completely benchmaxxed.
    - **u/somerussianbear** (↑1, 2026-10-21 21:17): Insane price, Zuck again out of his mind
- **u/TheMythicSorcerer** (↑1, 2026-10-22 03:19): Wonder Full When?
- **u/CYCLONOUS_69** (↑1, 2026-10-22 20:58): I wonder how it will muse me...

---

## Running commands with the cli on remote server with opencode server running from hermes
**u/AizenSousuke92** · 2026-10-21 15:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbq73h/running_commands_with_the_cli_on_remote_server/)

---

## OpenCode keeps getting stuck in an infinite shell-command loop. Anyone else experiencing this?
**u/Clear_Expert_7669** · 2026-10-21 14:47 UTC · ↑8 · 19 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbp6ls/opencode_keeps_getting_stuck_in_an_infinite/)

Hey everyone, I’m using OpenCode to develop a large software project, and sometimes it gets stuck repeatedly generating or executing shell commands without making any progress.

This happens across multiple models and providers, so I’m not sure whether it’s an OpenCode bug, a tool execution issue, or something in my setup.

Has anyone experienced this? What was the root cause, and what fixed it for you?

Any help would be appreciated!

**Comentarios:**

- **u/megablue** (↑3, 2026-10-21 14:49): what are your context-window tokens usages?
  - **u/Clear_Expert_7669** (↑1, 2026-10-21 15:18): Mostly new sessions
    - **u/megablue** (↑1, 2026-10-21 18:33): what kind of plugins have you installed? do you have any context-management plugins installed?
- **u/Johell1NS** (↑1, 2026-10-21 14:50): In my opinion the problem isn't opencode, but the model you're using.
  - **u/Clear_Expert_7669** (↑1, 2026-10-21 15:19): Happened with multiple models   
      Deepseek flash  
      Kimi2.6  
      Mimimax M3.1 flash
    - **u/Low-Guarantee-3437** (↑1, 2026-10-21 21:45): on the other hand, I use opencode daily for hours in multiple sessions, and openai models and glm-5.3. Does not happen.
        
          
        the models you use are not proving to be very good at long running tasks.  
        I did have this happen once with kimi, which I then stopped using.
- **u/lincolnthalles** (↑2, 2026-10-21 14:53): DeepSeek? some models are more prone to this, especially in certain hours of the day.
  - **u/Clear_Expert_7669** (↑2, 2026-10-21 15:17): Just tested it right now it is working smoothly interesting
- **u/Outrageous-Story3325** (↑1, 2026-10-21 15:25): Try change harness, omp, pi, or something else, maybe try a system prompt to force it to avoid the behavior
- **u/alcogiggles** (↑-1, 2026-10-21 15:56): it's not opencode. It's the model.  
    Which one are you using? 
    
    DeepSeek 4.1 flash does that a lot.
  - **u/megablue** (↑1, 2026-10-21 18:39): >DeepSeek 4.1 flash does that a lot.
      
      nope, DS 4.1 Flash never did that.  I have 1.61B tokens spent on DS 4.1 Flash, never once it did that.
    - **u/alcogiggles** (↑0, 2026-10-21 19:51): If you look around this subreddit, you'll find is a common occurrence.   
        If it never happened to you, consider yourself lucky.
- **u/dizvyz** (↑4, 2026-10-21 16:16): While it's happening open another session and ask what the looping session is up to. THey have enough tools to diagnose.
  - **u/Low-Guarantee-3437** (↑3, 2026-10-21 21:47): this is a good tip. It is easy to get one opencode session to introspect another. I do this a lot when I am evaluating tweaks to [agents.md](http://agents.md), or skills, or working out why a task made a mistake. 
      
       Use a good model in high reasoning for the introspection (use a SOTA model if you have access, or a classy openweight model like glm-5.3 in max)
- **u/SirRobinBlibs** (↑1, 2026-10-21 17:51): If it happens across models in fresh sessions, I'd look at the commands first. The classic cause is a command that waits for input or opens a pager (git log, less, a y/n prompt, a dev server that never exits). The agent sees no useful output and tries again. Things that helped me: set `GIT_PAGER=cat` and `PAGER=cat`, prefer non-interactive flags (`--yes`, `CI=true`), and run servers in the background with a timeout. Then add a rule to AGENTS.md: "if the same command fails twice, stop and report the output instead of retrying." If you can paste the last few commands it looped on, it's usually obvious which one is hanging.
  - **u/megablue** (↑1, 2026-10-21 18:42): i would give it a bit of flexibility  
        
      "if the same command fails twice for the same reason, stop and report the output instead of retrying. "
    - **u/SirRobinBlibs** (↑1, 2026-10-22 07:43): Fair. "Twice for the same reason" is the key part. A different error means it's making progress. I'd also let it try one genuinely different approach before stopping, just not the same command a third time.
- **u/43848987815** (↑1, 2026-10-22 00:46): How big has your db got? 
    
    I have to clean mine every couple of months or so because it affects sessions
- **u/Arnafas** (↑1, 2026-10-22 11:06): The only time I saw it happened with glm-5.3-flash (opencode go version) that was called as a sub agent. I also have zai subscription and I never saw it doing this.

---

## Top 10 AI agents for small local LLMs in 2026, tested on Qwen3.5-4B
**u/latent_lurker8587** · 2026-10-21 11:45 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbkx1m/top_10_ai_agents_for_small_local_llms_in_2026/)

[removed]

---

## You may not need another AI coding subscription. This MIT-licensed agent runs on the ones you already pay for
**u/AdExotic6745** · 2026-10-21 10:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbjbrc/you_may_not_need_another_ai_coding_subscription/)

[removed]

---

## Do you use claude code or opencode?
**u/PearVibes** · 2026-10-21 09:45 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbirxq/do_you_use_claude_code_or_opencode/)

I'm trying to pick a default coding agent, and the feature lists don't help much, since both read the codebase, edit files, and run commands from the terminal.

The difference seems to be how much control I get over the model layer to execute the way I want it. Claude Code is managed by Anthropic, runs only Anthropic models, and is covered by a Pro or Max plan. OpenCode works perfectly with a lot of providers and local models and can run headless for remote or async work, but you configure and pay for the models yourself.

My major concern is that I am clueless about which of them will serve me better in a cost-efficient mode. Claude Code feels fine until you hit the weekly limit before Saturday and need extra credits, which aren’t free, lol. On the other hand, model freedom feels chill until you have to keep maintaining provider configs and tracking API spend across several providers.

I actively use Claude Code at the moment because my laptop doesn't have the RAM to run local models; the fan makes a lot of noise and draws down the performance of my PC.

For those heavily running agents every day, what decides it for you, and do you run both for different kinds of work, or do you use one of the two?

---

## Best practices for moving a website from local to vps.
**u/katana1096** · 2026-10-21 09:39 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbiolf/best_practices_for_moving_a_website_from_local_to/)

---

## I built a plugin that gives OpenCode access to Gmail, Calendar, Slack, GitHub, Notion, Linear and more via Composio
**u/DishRadiant1937** · 2026-10-21 08:44 UTC · ↑0 · 2 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbhstg/i_built_a_plugin_that_gives_opencode_access_to/)

**Comentarios:**

- **u/yiestee** (↑1, 2026-10-21 14:06): access to Gmail? Nothing could go wrong with this one...
  - **u/ILoveMyDurdle** (↑1, 2026-10-22 15:57): don't even get me started  
      my manager literally boasts about giving full access of company's bookkeping to Astra because apparently "it's the best"

---

## MiniMax M3.1 Flash is free on Ollama Cloud until Thu 23:59 UTC: the OpenCode setups I verified (Ollama and MiniMax direct)
**u/SirRobinBlibs** · 2026-10-21 08:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbh7nn/minimax_m31_flash_is_free_on_ollama_cloud_until/)

[removed]

---

## A question for the people who are using opencode with their API keys
**u/Wise_Choice7014** · 2026-10-21 08:05 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbh6sf/a_question_for_the_people_who_are_using_opencode/)

&#x200B;

How much is your API monthly Bill ? And do you know how to reduce it ? Like do you have any option or tool to reduce it ? And why is it high or low ? What are the projects that you're working on to consume that much tokens every month ? I am asking that question because i am a little bit curious about that topic

---

## Tokless: 30-second all-in-one toolkit — Zero setup, minimal MCPs, token-efficient tools
**u/ElectricalBet3264** · 2026-10-21 07:57 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbh272/tokless_30second_allinone_toolkit_zero_setup/)

---

## Do I need to have active subscription to spend my credits?
**u/sagiroth** · 2026-10-21 06:44 UTC · ↑1 · 5 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xbfwbw/do_i_need_to_have_active_subscription_to_spend_my/)

I run out of usage and my sub lapsed but I  still have 100$ in credits. I could bot continue using opencode go models and I could bot see opencode zen models either.

**Comentarios:**

- **u/Amarsir** (↑1, 2026-10-21 06:48): They're different keys. Make sure you have both in your harness and select models from zen.
  - **u/sagiroth** (↑1, 2026-10-21 06:50): Oh didnt see option for different key. Thanks will look around
- **u/poop_report** (↑1, 2026-10-21 14:05): You can use Zen models, although it's usually a better deal to have the subscription active, and then use the option to spend credits once your monthly allowance is exhausted.
  - **u/sagiroth** (↑1, 2026-10-21 14:07): I'm burning through 300$ worth of referals and only use cheap models anyway. I use these with claude as workers :)
    - **u/poop_report** (↑1, 2026-10-21 15:11): guess that's why we can't do referrals anymore

---

## Top 10 AI agents for small local LLMs in 2026, tested on Qwen3.5-4B
**u/GapNew4766** · 2026-10-21 00:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xb93er/top_10_ai_agents_for_small_local_llms_in_2026/)

[removed]

---

## Latest CatBench shows it's time to move on to Opus 5.5
**u/wonderkindel** · 2026-10-21 00:33 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xb8x3z/latest_catbench_shows_its_time_to_move_on_to_opus/)

---
