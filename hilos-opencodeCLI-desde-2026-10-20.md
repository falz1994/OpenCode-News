# r/opencodeCLI — hilos 2026-10-20 → 2026-10-21
_Generado: 2026-10-20T17:05:13.641105+00:00 · 8 hilos · 2 comentarios · fuente: Arctic Shift_

## First time working on OpenCode
**u/Local-Item-2241** · 2026-10-20 15:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xavvoz/first_time_working_on_opencode/)

Hi! Over the past few weeks, I've been watching how everyone is doing something completely different with the help of OpenCode and Claude, so I decided to bring an idea I'd been planning for months to life.  
I’m trying to make my first turn-based strategy video game, and this is what I’ve managed to accomplish over the past two weeks. I designed the cards, menus, interfaces, etc., all by myself, and with the help of DeepSeek, I brought everything to life and made it functional.  
Right now, I have a very early version of what I have planned for the project, so I’d like to connect with people who are more involved and can guide me or even be a part of this.  
If anyone wants to try out the game (a very early version), I’d be happy to share it with you 🙏🏽

---

## OpenCode กำลังอยู่ในจุดสูงสุด
**u/PaPangPot** · 2026-10-20 14:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaubla/opencode_กำลงอยในจดสงสด/)

---

## I made an Android app for OpenCode (iOS coming soon)
**u/beppe28** · 2026-10-20 14:41 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xatybu/i_made_an_android_app_for_opencode_ios_coming_soon/)

I’ve been working on an Android app to follow my OpenCode sessions from my phone. I can check what the agent is doing and send prompts without going back to my computer.

It connects to `opencode serve`. You can follow the conversation live, check what files changed and approve or reject permissions directly from the notification.

It’s written in Kotlin + Jetpack Compose, built for the OpenCode V2 API. I generate the API client from the OpenAPI spec so I don’t have to keep the models in sync by hand.

This is my own project, I’m not part of the OpenCode team. Sharing it here in case someone else finds it useful.

The code is open source and there’s a signed APK:

Source: [https://github.com/beppe2880/opencode-mobile](https://github.com/beppe2880/opencode-mobile)  
APK: [https://github.com/beppe2880/opencode-mobile/releases/latest](https://github.com/beppe2880/opencode-mobile/releases/latest)

---

## OpenCode Needs To Fix This :
**u/Amazing-Platform9285** · 2026-10-20 14:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xatgw9/opencode_needs_to_fix_this/)

https://i.redd.it/db9thudtsmwh1.png

Don't Ruin The Best Free Coding CLI .

---

## i built kimo - a free open-source (mit) video editor with no gui that your opencode/codex/cursor agent can drive over mcp. rough right now, tell me what breaks
**u/LieTop7965** · 2026-10-20 06:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaklwi/i_built_kimo_a_free_opensource_mit_video_editor/)

hey - i built kimo, a free open-source (mit) video editor with no gui that ai coding agents drive over mcp. you tell your agent (opencode, codex, cursor, or any other mcp client) what to do and it drives the whole timeline as tool calls: cut, trim, keyframe, titles/captions, colour grade, tracking, particles, audio, export. the agent can also render a single frame back to itself to check its own work before committing.

it's one ~15 mb cpu-only rust binary, runs on a 2 gb box. i'm a college student (naman) and i built it, so a few things are still rough - the ui doesn't exist because there is no ui, and some edge cases in tracking and captions still need work. would really love you to try it and tell me what breaks.

site: https://getkimo.tech
github: https://github.com/naman-sharma12345/kimo

**Comentarios:**

- **u/kantorcodes1** (↑1, 2026-10-20 08:18): One registry generating the MCP tools, the CLI and the fuzz coverage at once is the part most agent-facing tools get wrong. Usually the CLI and the agent surface drift apart within a few releases.
    
    On the gated tools: what decides which of the 378 calls are exposed vs the 16 gated ones? Is that a static allowlist or something the client can negotiate?

---

## All agents - across platforms and harness working right in your OpenCode v2 TUI
**u/ZealousidealTown1974** · 2026-10-20 02:49 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xagr8f/all_agents_across_platforms_and_harness_working/)

---

## OpenCode Hacked
**u/RelevantEmergency707** · 2026-10-20 01:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaf1wq/opencode_hacked/)

---

## I want to try the Pi harness. Does OpenCode support it?
**u/itherseed** · 2026-10-20 01:24 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencodeCLI/comments/1xaf0f8/i_want_to_try_the_pi_harness_does_opencode/)

I was thinking of trying other harnesses using the models of OpenCode Go. Does OpenCode allow users to do that, or will I get limited/banned for using anything else than their product? I was trying to find some official documentation allowing it or prohibiting it but haven't found anything. Thanks in advance.

**Comentarios:**

- **u/migsperez** (↑4, 2026-10-20 02:21): Yes opencode go does support it. But not the free models.

---
