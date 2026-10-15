# r/opencode — hilos 2026-10-14 → 2026-10-16
_Generado: 2026-10-15T15:23:04.085903+00:00 · 48 hilos · 365 comentarios · fuente: Arctic Shift_

## DeepSeek V4.1 Flash is available for FREE
**u/CoffeeTea021** · 2026-10-15 09:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6gt2y/deepseek_v41_flash_is_available_for_free/)

[DeepSeek V4.1 Flash Free](https://preview.redd.it/0s6so20jklvh1.png?width=1058&format=png&auto=webp&s=b4a35a6bbd0538637637e3bce23923ce6f77bf40)

DeepSeek is available for free on OpenCode for a limited time! It also states that it follows a zero-retention policy and does not use our data for model training.

**Comentarios:**

- **u/SomeOrdinaryKangaroo** (↑-6, 2026-10-15 09:16): deepseek is investigated in china for secretly routing requests to claude, so if they're routing through provider instead of a 3rd party i wouldn't blindly trust the zero retention policy
  - **u/deleted-account69420** (↑6, 2026-10-15 09:22): *investigated in China*
      
      Ok, bring source.
    - **u/apepaolo** (↑1, 2026-10-15 09:46):   
        [https://qz.com/china-deepseek-moonshot-anthropic-data-probe-092326](https://qz.com/china-deepseek-moonshot-anthropic-data-probe-092326)
        
        China's Cyberspace Administration is investigating DeepSeek and Moonshot AI over user data that may have reached Anthropic's servers without customers' knowledge, according to [The Information](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic).   
          
        [https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic)
      - **u/deleted-account69420** (↑1, 2026-10-15 11:07): Any actual reliable source, ex coming directly from China?
        - **u/IAmFitzRoy** (↑2, 2026-10-15 14:08): What’s your problem?  Don’t you trust qz.com ?
            
            🤣
- **u/Original_Goznab** (↑3, 2026-10-15 09:16): I'm so excited.
- **u/lustyphilosopher** (↑6, 2026-10-15 09:18): Do I need to restart my session Or something? Or is this only for v2 users? I've only used DeepSeek and I'm already at 11% of my 5hr window
  - **u/Fabulous-Ladder3267** (↑2, 2026-10-15 10:20): Might need chamge the model that has Free label on it
    - **u/BatNo7925** (↑1, 2026-10-15 12:30): You should be using DeepSeek V4.1 Flash Free. I think it works the same as before: giving each user a small quota to use, which is already great. Although when I first heard the news, I also thought it was similar to Anonymous Model -> ∞, but that's unlikely—all users would abuse it until it went bankrupt.
- **u/NinjaAlaska** (↑3, 2026-10-15 09:23): insane working too lol thx
- **u/IlNaka** (↑4, 2026-10-15 10:11): Limited time and "limited usage" with only 200K context instead of 1M
  - **u/BatNo7925** (↑0, 2026-10-15 12:33): That's the truth. I also thought a free lunch had come along, but I was mistaken. No company would make a completely unlimited free offer and bankrupt itself.
- **u/Fabiox08** (↑1, 2026-10-15 10:28): Yeah! I'm using it now! I don't know if Big Pickle is still better/same or worst than DeepSeek V4.1 Flash.  
    What's your opinion?
- **u/direcirculationissue** (↑1, 2026-10-15 12:05): better or worse than muse spark 1.3?
  - **u/CampMaster69** (↑3, 2026-10-15 12:11): spark is meh. it does the job but it doesn't display too much intelligence, rather grunt work with all edge cases considered. deepseek is not too far ahead to be honest, but still a wee bit better. 
      
        
      heck i feel that 3.8 flash on antigravity has a lot more life.
    - **u/RoundZookeepergame2** (↑0, 2026-10-15 12:35): What a joke comment
  - **u/Odd_Abrocoma_8421** (↑1, 2026-10-15 14:31): no limits
- **u/Cyvster** (↑2, 2026-10-15 12:30): i don't see any deepseek listed as free
- **u/BrownCarter** (↑1, 2026-10-15 13:35): mine is returning 400 error
  - **u/Tasty_Owl_7930** (↑1, 2026-10-15 14:07): its likeky the new endpoint bug from Opencode. you can change the endpoint from ur `opencode.json` into this
      
      ```
      {
        "provider": {
          "opencode": {
            "options": { "baseURL": "https://opencode.ai/zen/v1" }
          }
        }
      }
      ```
      
      source: [https://github.com/anomalyco/opencode/issues/54833#issuecomment-6127009970](https://github.com/anomalyco/opencode/issues/54833#issuecomment-6127009970)
      
      by the official opencode creator (anomalyco)
- **u/dwky11** (↑1, 2026-10-15 13:39): I don't see it yet in my OpenCode models option.
- **u/Sir-Draco** (↑1, 2026-10-15 14:06): I think I’d rather pay for it if they are using a quantized version instead of full weights. It is already cheap. I would like to use it as intended
- **u/Ill-Ear-8763** (↑3, 2026-10-15 10:23): Thank you so much we can use your affiliate link... /s
  - **u/Dry_Cantaloupe4349** (↑1, 2026-10-15 10:37): You don't have to, its not like I get money from it, just a bit of extra credits. Just remove the code if you don't like it.
- **u/Fabiox08** (↑1, 2026-10-15 10:29): Question: Is it free?
  - **u/Dry_Cantaloupe4349** (↑1, 2026-10-15 10:37): Completely

---

## Opencode Zen not Working anymore in 9Router?
**u/devallerie** · 2026-10-15 08:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6g22u/opencode_zen_not_working_anymore_in_9router/)

**Comentarios:**

- **u/ATyp3** (↑1, 2026-10-15 08:49): Not working in Paseo for iPhone either what the fuckkkk

---

## Opencode Zen not working anymore in 9router?
**u/devallerie** · 2026-10-15 08:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6g1ec/opencode_zen_not_working_anymore_in_9router/)

---

## Deepseek is so slow nowadays
**u/Eastern-Passage629** · 2026-10-15 08:00 UTC · ↑2 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6fqd0/deepseek_is_so_slow_nowadays/)

Until about a week ago, I was able to reach speeds of 300 tokens per second, but now the maximum is 100, and at certain times it even drops to 50. Yes, I know a lot more users have started using it, but can’t this be improved? Why isn’t the service we’re paying for consistent? At the very least, it should stay reliable. Dropping from 300 to 50 is ridiculous.

**Comentarios:**

- **u/ItzHolmes-** (↑3, 2026-10-15 08:03): Will be still slow now considering its freee
  - **u/Strict-Prune-879** (↑2, 2026-10-15 08:07): ou c'est gratuit????
- **u/imoshudu** (↑1, 2026-10-15 08:58): Opencode go is slowseek.
    
    Commandcode goat keeps deepseek speed up. 
    
    I regret paying for the former. That's before we speak about other providers.

---

## Cheepseek what ?
**u/Jazzlike-Form9669** · 2026-10-15 07:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6fn1n/cheepseek_what/)

You guys are paying $10 to get $60 of dumbseek -- 80TPS slow like turtle ::) 



What if you can get $60 of deepseek + glm , in $5 -- 350 TPS

**Comentarios:**

- **u/AdFun4897** (↑3, 2026-10-15 07:59): No @Jazzlike-Form9669, we wont put our credit cards in your sketchy vibecoded ai slop website
  - **u/Jazzlike-Form9669** (↑-3, 2026-10-15 08:12): Haha , whole opencode is vibecoded lol. Software by typing is dead now , everything is AI assisted coding, if you are in delulu , I am really sorry for you
- **u/Strict-Prune-879** (↑1, 2026-10-15 08:05): c'est quoi ton site?
- **u/alex9001** (↑1, 2026-10-15 08:08): Drop the site so we can report it
  - **u/Jazzlike-Form9669** (↑1, 2026-10-15 08:12): To FBI 😧

---

## DeepSeek V4.1 Flash is FREE in OpenCode 🔥
**u/afanasenka** · 2026-10-15 07:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6fj9m/deepseek_v41_flash_is_free_in_opencode/)

**Comentarios:**

- **u/Artium99** (↑25, 2026-10-15 07:49): How???
  - **u/Melodic-Leather-5170** (↑60, 2026-10-15 08:01): you are the product
    - **u/Familiar-Ear-1223** (↑4, 2026-10-15 10:19): We better off using ollama 20$ for privacy sake
    - **u/Old-Juggernut-101** (↑4, 2026-10-15 12:09): Honestly, I don't care. I've don't nothing of significance that csn be stolen. I am a mere student. Ill take being thr product lol
    - **u/NMiguelCosta-PT** (↑11, 2026-10-15 12:17): ChatGPT/Claude users have literally had their private conversations reported to the police over potential crimes and illegal behavior, and these companies have also stolen scientists' research. You're really naive if you think these big companies aren't stealing your data just because you pay them, as if they're under any moral obligation to respect your privacy after stealing the entire world's intellectual property while governments basically let AI labs do whatever they want. You're ALWAYS the product.
      - **u/mtftl** (↑1, 2026-10-15 14:40): This has to be the permanent mindset using any cloud AI inference. Everyone is playing this game. The only consideration is how comfortable you are with a third party knowing what you request and your patterns of requesting it, then deciding how to proceed.
  - **u/xatey93152** (↑1, 2026-10-15 08:06): Wrapper of free model
  - **u/xRebellion_** (↑16, 2026-10-15 08:10): Free models trade your usage for training data, of course use it only if you don't mind that.
    - **u/NMiguelCosta-PT** (↑10, 2026-10-15 12:18): Imagine thinking only free models do that lol
      - **u/xRebellion_** (↑1, 2026-10-15 12:21): That's why local models are the way to go. Sadly it's only accessible for those who has beefy GPUs with high VRAMs right now.
        - **u/XL-Dildo-Brazilian** (↑1, 2026-10-15 13:09): how much vram we need to run deep seek 4.1 or mimo 2.6 flash locally? can we mix 96GB vram and dram? say my dram is 128GB and vram is 96GB, 96gb isnt enough i assume so we gotta use dram to fill the other gap?
          - **u/SommerBlau67** (↑2, 2026-10-15 13:26): bro to run deepseek you'll need a few GPUs, it takes like 1664Gb in VRAM
  - **u/PrudentJelly116** (↑1, 2026-10-15 08:10): 200k context. probably Q2 or Q4 . and advertisement budget.
    - **u/Infinite-Local5435** (↑11, 2026-10-15 08:13): deepseek is natively served at mxfp4 already
      - **u/Saifl** (↑11, 2026-10-15 09:38): Deadass it seems so dumb to me when people are saying 4 bit quants of deepseek are bad when its native at 4 bit. These people just throw around words thinking they know shit
        - **u/Ivanjacob** (↑2, 2026-10-15 10:34): Yeah cheap stuff attracts idiots
        - **u/PrudentJelly116** (↑0, 2026-10-15 12:48): Who says bad 🙂 i answered to question. Im using that now
  - **u/SomeOrdinaryKangaroo** (↑-8, 2026-10-15 08:32): Because it sucks compared to Sonnet 5.5 so demand is low enough that they can pay from their own pockets
  - **u/Zeeplankton** (↑2, 2026-10-15 08:53): I've been using it through openrouter the last few days and deepseek is quanting or something. Flopping on weird things, hard.
  - **u/MediumReplacement454** (↑3, 2026-10-15 09:09): Don't worry its going to go away in a few weeks once they have enough data for "AGI"
  - **u/lewwdsv1** (↑1, 2026-10-15 10:41): The normal paid tier is still there, the free one just takes your data so they can train on it. The usual
    - **u/squirrelscrush** (↑1, 2026-10-15 13:30): Even the Go variant can use your data if you don't choose ZDR.
  - **u/insultingDuck** (↑1, 2026-10-15 13:17): That thing will eventually enumerate your directory, and see what else is out there.
    - **u/squirrelscrush** (↑1, 2026-10-15 13:31): That's an issue with the harness tbh
- **u/synaps33** (↑1, 2026-10-15 07:50): wait, Wait, WHAIT... WHAAAT 0.0?
- **u/kmorg80** (↑1, 2026-10-15 07:51): nice
- **u/Square_Confection_62** (↑3, 2026-10-15 07:52): limited to 200k context?
  - **u/AlexandraMaryWindsor** (↑1, 2026-10-15 07:58): Useless. How dare they!
- **u/Cyclone0701** (↑6, 2026-10-15 07:53): Go or zen?
- **u/Pressimize** (↑-2, 2026-10-15 07:53): Muse 1.3 spark as well as step 5 are better models anyways and have been free before.
  - **u/gaspoweredcat** (↑2, 2026-10-15 08:01): Not sure they are, they aren't bad but I trust them more for reviews than actual implementation
- **u/ImportantSpread7499** (↑1, 2026-10-15 07:53): Any idea on the usage/rate limit of it?
- **u/Blue-Sea2255** (↑5, 2026-10-15 07:57): What? More info pls.... For all users? No limit? What about data retention? And more info pls.
  - **u/YoRt3m** (↑11, 2026-10-15 08:09): Just assume it's limited and there's data retention
- **u/ResponsibilityOwn361** (↑1, 2026-10-15 08:00): wtf!!
- **u/qqYn7PIE57zkf6kn** (↑1, 2026-10-15 08:02): damn you are fast.
- **u/throwaroo202020** (↑1, 2026-10-15 08:04): Again omg
- **u/elitegenes** (↑1, 2026-10-15 08:11): This is perfect for any throwaway work.
- **u/for4f** (↑7, 2026-10-15 08:11): lol perfect timing, flash has been my daily driver for weeks. fast enough that i stopped thinking about which model i'm on for most stuff, just falls over on the gnarly multi-file refactors. free is a no-brainer, go break things
- **u/straightouttacristo** (↑6, 2026-10-15 08:19): so slow but very happy!
- **u/Riad_idk** (↑1, 2026-10-15 08:21): "cry of happiness"
- **u/RaisinImpressive3749** (↑2, 2026-10-15 08:27): is it usable in opencode harness only? hopefully can use it in Pi
  - **u/GLR1997** (↑1, 2026-10-15 14:05): Openchamber > OhMyPi
- **u/Rajucg** (↑1, 2026-10-15 08:31): Sound like we are invited to stress test opencode infra
- **u/iwenttothelocalshop** (↑5, 2026-10-15 08:32): Christmas came early
- **u/TronnaLegacy** (↑11, 2026-10-15 08:34): I just paid for OpenCode Go Plus a few hours ago lol
  - **u/CryptoRider57** (↑5, 2026-10-15 08:46): same
  - **u/holmedog** (↑13, 2026-10-15 11:28): Still worth it, you get usage throttled even on the free models after a certain usage in Zen.  Go uses  the free models without consuming your monthly allowance
    - **u/box_of_hornets** (↑5, 2026-10-15 11:51): Does this mean if I have opencode Go I can just use this indefinitely all month? I'm spending like 600-800 USD a month on DeepSeek 4.1 Flash so this would be a game changer, even if it is slower and less reliable
      - **u/gato001k1** (↑1, 2026-10-15 12:11): What are you building?
      - **u/Justanotherperson32** (↑3, 2026-10-15 12:39): How are you using so many tokens?
      - **u/squirrelscrush** (↑4, 2026-10-15 13:26): If you're using so many tokens, it's better to just get a Claude Pro subscription lol
        - **u/box_of_hornets** (↑1, 2026-10-15 14:45): I ran the numbers and would need 4 max subscriptions - it would cut my bill in half actually, if I could do that, but Anthropic specifically forbid running agent fleets on subscriptions and detect and kill subscriptions when they see the activity (from what I see on the internet)
- **u/EstablishmentAny4525** (↑1, 2026-10-15 08:57): This is mind blowing. My favourite model that I love paying for is now free!
- **u/citizenjc** (↑1, 2026-10-15 09:22): I'd this true at all? Just tested, no dice
- **u/trashbytes** (↑1, 2026-10-15 09:24): Can we use it with other harnesses like Hermes Agent for example? Don't seem to be able to select it there.
  - **u/jakobwells** (↑2, 2026-10-15 11:21): Free models are restricted to use in OpenCode.
    - **u/trashbytes** (↑3, 2026-10-15 11:31): Thank you! That confirms it.
    - **u/NMiguelCosta-PT** (↑1, 2026-10-15 12:22): No, they're not. I have used them in Codex in the past with codex-router and there's many other ways to use them in any harness.
      - **u/GoldPossession7284** (↑1, 2026-10-15 13:13): as políticas novas deles proibem que você use, esse é o ponto, agora se você vai fazer um proxy ou não para usar externamente como eu fiz... ai é outra história
      - **u/jakobwells** (↑1, 2026-10-15 13:19): This changed in September, so you might both be right depending on when you tried it. Receipts first, same key and same endpoint, plain curl, no OpenCode anywhere in the picture:
          
              $ curl https://opencode.ai/zen/v1/chat/completions \    -H "Authorization: Bearer ***" -H 'Content-Type: application/json' \    -d '{"model":"deepseek-v4.1-flash-free","messages":[{"role":"user","content":"hi"}],"max_tokens":8}'HTTP 403{"type":"FreeTierError","message":"OpenCode's free tier can only be used from within OpenCode. ..."}
          
              $ curl https://opencode.ai/zen/v1/chat/completions \    -H "Authorization: Bearer ***" -H 'Content-Type: application/json' \    -d '{"model":"deepseek-v4.1-flash","messages":[{"role":"user","content":"hi"}],"max_tokens":8}'HTTP 200{"id":"chatcmpl-29b890ff61914b5a84ff9fbee88e713d","model":"deepseek-v4.1-flash","choices":[...]}
          
          Five different free ids give that same 403: deepseek-v4.1-flash-free, mimo-v2.6-flash-free, nemotron-3.5-lightning-free, jev-1.13-free, space-bunny-free. The paid model answers fine from the same shell, so it is not the key and not curl, it is the free tier.
          
          Now the part that explains your side. Until mid-September that check was much weaker. Someone filed #42500 in August asking them to drop it: "The anonymous free tier at [https://opencode.ai/zen/v1](https://opencode.ai/zen/v1) is served only to requests carrying the opencode client's User-Agent. Any other OpenAI-compatible client (Cline, Roo Code, Continue, Aider, mimo) gets 429 FreeUsageLimitError." Spoof the UA, or send X-Opencode-Client and X-Opencode-Session, and you were through.
          
          That closed on 17 September. A pile of issues lands that day with the new error, #49433, #49435, #49438, #49479 and more. From #49433, same day: "just started for me too after a few weeks of it working fine." A maintainer confirmed it the next day in #49621: "We've been tightening our logic to fight abuse. You cannot use the free tier in other harnesses (this is only a limitation for the free tier nothing else)."
          
          So if codex-router worked for you back in August, it did work. The header path hung on for a few days after the 17th and then stopped.
          
          Free tier only though. Paid Zen and Go still answer from any client. If it is still working for you today, paste the response, I would genuinely like to see it.
- **u/Ok_Stuff_4959** (↑1, 2026-10-15 09:44): You all go ahead, I'll stick with Big Pickle  :P
- **u/BlokZNCR** (↑3, 2026-10-15 09:46): Mimo 2.6 vs Muse 1.3 vs Deepseek 4.1
    
    what is more logical?
  - **u/Toluwalashe** (↑2, 2026-10-15 11:16): Muse
  - **u/LuckyFemboy_** (↑3, 2026-10-15 11:38): DS > Mimo > Muse
    - **u/Yousv** (↑2, 2026-10-15 12:15): is that the case for general coding overall or just "logic"?
      - **u/LuckyFemboy_** (↑5, 2026-10-15 12:26): That ranking was about logic/reasoning, not general coding overall. My workflow is more like agentic coding: inspect, propose, implement, debug, automate. So it's logic-heavy general coding, not just logic.
        - **u/Yousv** (↑2, 2026-10-15 12:32): thanks for your insights!
          - **u/LuckyFemboy_** (↑2, 2026-10-15 12:42): One more thing: even in English, Muse Spark isn't particularly strong overall. And once you move outside coding — especially with non-English input and long-context creative/worldbuilding tasks — it can fall apart. I once tried to port several roleplay/worldbuilding universes I'd written in a non-English language into a sillyTavern, and it ended up mixing up different characters' biographies and producing generic AI slop. So that's not just a logic issue; it's a broader language/context handling issue.
            - **u/Yousv** (↑1, 2026-10-15 12:45): in your opinion and based on your experience, which currently available free model performs the best for coding and less generic writing and hallucinations overall?
                I've been torn between muse, mimo and all the new random models and so far muse seems like the one that could fix much of the issues i had.
              - **u/LuckyFemboy_** (↑2, 2026-10-15 14:07): Not sure why you'd lean toward Muse after what I said earlier. I already mentioned it falls apart outside coding, especially with non-English input and long-context creative tasks. But to be direct: for coding + less generic writing + fewer hallucinations, my pick is still DeepSeek.
                  
                  For OpenCode specifically, I mostly use Mimo, but it feels less smart there than in FreeBuff. I recently compared Mimo with Space Bunny Alpha and Muse Spark 1.3. Muse Spark 1.3 was bad across the board for me. Space Bunny Alpha is okay for coding but weak at writing and hallucinates sometimes. I haven't used DeepSeek free in OpenCode much yet because it only recently appeared there, but based on my use outside OpenCode, I'd choose DeepSeek 10 out of 10 times.
                  
                  So overall: DeepSeek > Mimo > Space Bunny Alpha > Muse. If you mostly do English coding, Muse might be tolerable, but for writing and non-English work, no.
                - **u/Yousv** (↑1, 2026-10-15 14:19): I'm not leaning towards it after what you said that was just what i was using up until now, will definitely switch tho after what you said, thanks!
            - **u/Odd-Elderberry-6328** (↑1, 2026-10-15 14:59): I've did the same, porting Chinese cards to English using muse, it not worked well with cards with NSFW information, because he was trying to remove it, but for sfw cards, it works well
  - **u/Mementem** (↑2, 2026-10-15 14:00): i would recommend staying away from muse spark 1.3, 
      
      i just don't trust lizard man with my data.
      
      if they are hosting the full DS model, and not a quant, i would use that
    - **u/warpaint_james** (↑2, 2026-10-15 14:11): I use it for my open source recomp project. Sure, suck up the open source recomp, thanks for the help
- **u/andrewlabaski** (↑0, 2026-10-15 09:49): u/opencode please, check why 100% usage cant still use free models.
- **u/CheesecakeLivid9791** (↑1, 2026-10-15 09:58): Just in time
- **u/frank_pc** (↑24, 2026-10-15 10:01): Operation CheapSeek final stage?
- **u/imsankz** (↑1, 2026-10-15 10:21): Is this how they ask us to come back 😂
- **u/Conscious-Doctor-585** (↑19, 2026-10-15 10:38): The official DS refunded the spending of their api service of last 7 days as a remedy to their service outage. OC is sharing it not staying silent about it.
- **u/AskingGypone5** (↑1, 2026-10-15 10:49): is it good? last time using space bunny free gets into my skin lol
  - **u/inversechi** (↑1, 2026-10-15 11:04): yeah, that experience was so bad.
  - **u/Monecreiff** (↑1, 2026-10-15 13:50): i miss spacebunny alpha. It was actually good at modelling in blender
- **u/Cautious_Fox_4191** (↑2, 2026-10-15 11:01): They have all my prompts and data, right? Nothing in this world is free.
  - **u/NMiguelCosta-PT** (↑3, 2026-10-15 12:23): and if you pay they don't???
    - **u/Cautious_Fox_4191** (↑1, 2026-10-15 12:28): They still do and that's why they subsidies the subscription amount.
      - **u/Ctrl-Alt-Panic** (↑2, 2026-10-15 13:49): OpenCode has a ZDR / no training policy for Deepseek on the paid plan.
          
          That's what they say, anyway.
- **u/Icy-Examination-9512** (↑28, 2026-10-15 11:01): 200k context is absolute terrorism
  - **u/squirrelscrush** (↑7, 2026-10-15 13:31): I've been living off 260K context on Luna lol
    - **u/FireSilicon_** (↑1, 2026-10-15 14:50): Most openai models including Luna have 1M context you just have to enable it with a config file. In fact you can just tell codex to enable it for you. The only issue is that they charge you more because they are assholes.
  - **u/randomperson_69_** (↑1, 2026-10-15 13:35): Ts so funny 😂
- **u/Warm-Agent-811** (↑1, 2026-10-15 11:08): Does anyone know if this is the official DeepSeek model, or is it a third-party service like OpenRouter that might be serving a smaller 4B model under the DeepSeek name?
  - **u/LukeLikesReddit** (↑2, 2026-10-15 11:14): Given they only offer 200k context and say its ZDR when the official deepseek api gives you 1 million context and will train on your data i suspect its going to be the latter. Haven't had the chance to test it yet.
- **u/Dapper-Window-4492** (↑1, 2026-10-15 11:28): Any rate limits on the free tier?
- **u/Voxylem** (↑1, 2026-10-15 11:41): They made it free and now it is slow as hell
- **u/Dry_Hyena_6296** (↑1, 2026-10-15 11:46): Free api??
- **u/cetogenicoandorra** (↑1, 2026-10-15 11:47): What limit tier?
- **u/XL-Dildo-Brazilian** (↑1, 2026-10-15 13:10): i cant see deepseek 4.1, it shows to me openrouter one which is paid, the free version of opencode i cant see it. any help please? thanks
- **u/Dry-Mathematician730** (↑5, 2026-10-15 13:45): This is better them big picle for coding?
  - **u/Difficult_Plantain89** (↑2, 2026-10-15 14:31): Absolutely. Not saying that big pickle is bad.
- **u/Mementem** (↑1, 2026-10-15 13:57): is it a lower quant? or is it the full thing?  
    what are the speeds like for the rest of you?
- **u/jackorjek** (↑1, 2026-10-15 14:30): its free with quota. tested, pushed it and got limited. resets in the next 12 hours.
- **u/Sea_Mushroom_6498** (↑0, 2026-10-15 14:56): which model is best for the cyber security and ctf ?? among all free
- **u/fucking_h** (↑5, 2026-10-15 08:37): I think all the answers are pretty obvious.
    
    1. Maybe, maybe not. Depends on your work.
    
    2. Yes, limited time obviously.
    
    3. Nothing is unlimited, especially when it's a known model and not even a stealth release.
- **u/RoundZookeepergame2** (↑1, 2026-10-15 10:37): Why would it be free and unlimited?? Please
  - **u/AskingGypone5** (↑2, 2026-10-15 10:52): i FEEL like its unlimited when using space bunny free...

---

## New user here - what are the usage limits of opencode free?
**u/hillman_avenger** · 2026-10-14 19:59 UTC · ↑1 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x61fo6/new_user_here_what_are_the_usage_limits_of/)

I've just started using OpenCode and it seems great.  I'm pretty new to AI in general.  I'm using Big Pickle since it's the default, but it seems fine.  What are the usage limits, and what happens when I exceed them?  And is there any way to find out how much I've used or got left?

**Comentarios:**

- **u/Time-Worker9846** (↑2, 2026-10-14 20:05): No one knows the limit. After you exceed them you need to wait until the next day (midnight UTC).
- **u/Vast_Anxiety3133** (↑2, 2026-10-14 20:07): Once it was like 30 Cents of Muse Spark 1.3, so really not much compared to the 2 USD you get of Muse Spark Contributor with Go per day (30 day basis). On the other hand much, you get up to 9 USD of free inference per month
- **u/CYCLONOUS_69** (↑3, 2026-10-14 21:51): Can’t say exactly but I do use on avg 500M tokens a day and that’s for free
  - **u/hillman_avenger** (↑2, 2026-10-15 06:05): How do I find out how many tokens I've used?

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
  - **u/ngg990** (↑2, 2026-10-14 19:54): A mí me pasó que estaba haciendo un plugin para la 1.8 y me sacaron la V2 y me tocó migrar todo, fue menos doloroso de lo que pensaba. La TUI de la V2 me gusta mucho más
    - **u/ichisay** (↑1, 2026-10-14 20:01): Puse a la IA a tratar de portar el plugin de mempalace y le llevó un medio día entero casi jajajaja
      - **u/ngg990** (↑1, 2026-10-14 20:02): Adiós los 80 dolars cheapseek credits jajaja
        - **u/ichisay** (↑1, 2026-10-14 20:03): No xddd, pero si el límite gratis de Muse free
          - **u/ngg990** (↑1, 2026-10-14 20:04): Yo es que tengo todo configurado para usar DeepSeek y no me gustan los cambios xdddd
- **u/IntrepidMindExplorer** (↑1, 2026-10-14 19:54): It exists.
    
    [https://opencode.ai/v2/docs](https://opencode.ai/v2/docs)
    
    [https://github.com/anomalyco/opencode/releases/tag/v2.0.29](https://github.com/anomalyco/opencode/releases/tag/v2.0.29)
  - **u/ichisay** (↑1, 2026-10-14 20:01): El Desktop viene con la 1.19, que yo sepa
    - **u/IntrepidMindExplorer** (↑1, 2026-10-14 20:11): [https://imgur.com/a/EdSyHWZ](https://imgur.com/a/EdSyHWZ)
        
        I can at least verify that the Linux .deb package in the /v2/docs url I posted is indeed V2.
    - **u/IntrepidMindExplorer** (↑1, 2026-10-14 20:18): I see. The github repo is still v1.19. Yeah, that is a bit odd.
    - **u/IntrepidMindExplorer** (↑1, 2026-10-14 20:20): [https://github.com/anomalyco/opencode/releases/tag/v2.0.29](https://github.com/anomalyco/opencode/releases/tag/v2.0.29)
        
        Have to search for the v2 tags, it's there.
      - **u/ichisay** (↑1, 2026-10-14 21:28): Yo uso Windows, en principio Desktop se instala con 1.19 a no ser que se configure que use el cli de v2. No sé si en Linux eso es diferente y ya usa v2
        - **u/IntrepidMindExplorer** (↑2, 2026-10-14 22:00): V2 CLI and Desktop running on Win10. I just installed it on a test VM. The v2 desktop installer comes bundled with the v2 CLI but can be downloaded separately.
            
            When asking Big Pickle what versions I was running:  
            "You're running OpenCode v2.0.29.
            
            I found this by locating the desktop app install at C:\\Users\\test\\AppData\\Local\\Programs\\@opencodedesktop, which bundles the CLI as resources\\opencode-cli.exe. Both the opencode-cli.version file and opencode-cli.exe --version report the same:
            
            opencode v2.0.29"
            
            [https://imgur.com/a/KscPACe](https://imgur.com/a/KscPACe)
          - **u/ichisay** (↑2, 2026-10-14 22:11): Increíble, quizás mi error era trtr de ctualizar Desktop 1.19 a v2, gracias por ayudar con esto

---

## How to know which model works best each repo?
**u/OkPride1321** · 2026-10-14 19:16 UTC · ↑1 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x60c0d/how_to_know_which_model_works_best_each_repo/)

Do you guess ever face problem like which model to use sonnet, opus, cheap chinese models? which is most cost effcient.I used to just throw opus and sonnet on any problem but i want to ask you what you guess do?

**Comentarios:**

- **u/RepulsiveRaisin7** (↑3, 2026-10-14 19:21): A good model does well in many different situations so I don't find myself switching a whole lot. My main model is GLM 5.3 Flash, it's intelligent and pretty cheap. For review, I invoke Deepseek 4.1 Flash because a second pair of eyes is always better than one. On Opencode Go, you might flip these since DS is cheaper.
    
    Models like Opus are needed when you have a very complicated task or a task that is poorly specified. High-end models are best at planning, but you don't "need" them for implementation. Some people use Opus for everything and I think that's kinda dumb, but that's their choice.
  - **u/BrownCarter** (↑1, 2026-10-14 20:14): Would planning use fewer tokens?
    - **u/evia89** (↑1, 2026-10-15 02:27): Never
      - **u/Strange_Owl_6291** (↑1, 2026-10-15 05:21): Never is not a good answer. Sometimes depending on, is more correct. 
          
          Different projects, different changes, different agent scaffolding all makes a difference if a plan helps. 
          
          For vibe engineering you probably never need a plan (but it would sometimes help). Build something complex and plans more often help implementation (if used right).
          
          But even more importantly. There is no one size fits all solution in agentic engineering. Listen to people, try for yourself on your work, then make up your mind.
- **u/AdFun4897** (↑0, 2026-10-14 19:37): Just use Opus 5.5 on medium with Claude Code $20 plan for most tasks. One shots most taks, and better usage than any of the top models on opencode go
- **u/IAmFitzRoy** (↑1, 2026-10-14 19:38): It depends what are you doing. Coding? Categorizing? One-off decisions? Vision related? To you need tools? Web-search grounding? RAG?
    
    You want something fast/expensive? slow/cheap?
    
    Every use case will point to a different model.
- **u/Safe-Imagination8538** (↑1, 2026-10-14 19:47): id skip leaderboards for this and build a tiny eval from the repo itself. take 10-20 bugs you already fixed, reset to the commit before the fix, let each model try with the same harness and the same step limit, then run the tests. also log the time. on my 12gb card a big moe was about 5x slower per agent step than qwen 35b-a3b, and in a small test the step limit decided more of the result than the model did
- **u/Ctbhatia** (↑1, 2026-10-14 20:26): score cost per accepted fix rather than per token, a cheap model that needs a second pass loses to the expensive one that lands it first.
- **u/weiyentan** (↑2, 2026-10-14 20:39): I use multi orchestration set up not omo. I preface all my work through matt pococks skills and use labels to perform work. Issues get batched and this forms a pipeline of work to be done
- **u/DEAD1nsane** (↑1, 2026-10-15 03:34): I use **Muse Spark 1.3 Free** for everything
- **u/xapep** (↑1, 2026-10-15 09:39): Stop picking per repo, pick per task. That's the whole trick.  
      
    Most repos are 80% mechanical work (refactors, tests, boilerplate, small fixes) where a cheap model gets it done, and 20% genuinely ambiguous stuff (new architecture, weird bug hunts) where the strong model earns its price. Default opencode to the cheap model, escalate to sonnet or opus when the task is new or under-specified.  
      
    The other half is measuring. Going by feel is how you end up paying opus prices for haiku-level work. Track pass rate and tokens per task for a week and you'll see which tasks the cheap model botches on the first try. A cheap model that needs three retries already costs more than opus once.  
      
    Context usually matters more than the model: if the agent re-reads half the repo on every turn, no model choice saves you.

---

## Cat jam free
**u/Few-Advertising-3538** · 2026-10-14 18:57 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5zt6h/cat_jam_free/)

Muse spark 1.4??? Very fast, only problem is low context. Possibly for the beta only? I'm recording around 200tps which is inline with 1.3 just no images.. weird.

**Comentarios:**

- **u/AmuletOfNight** (↑2, 2026-10-14 22:35): Why would they release muse spark 1.4 when they just released muse wonder?
  - **u/a355231** (↑1, 2026-10-15 02:18): “Why would Claude release Sonnet 5.5 when they just released Opus 5.5?”

---

## What model is Space Bunny running right now? It's really good. We need to know.
**u/alcogiggles** · 2026-10-14 17:59 UTC · ↑2 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5y9y6/what_model_is_space_bunny_running_right_now_its/)

The model is reminding me of Big Pickle from June/July when it was incredible. How do we can find out right now what model Space Bunny is using?

**Comentarios:**

- **u/AdFun4897** (↑1, 2026-10-14 18:06): Its probably a new minimax model
- **u/A_Far_Hitman** (↑3, 2026-10-14 18:10): I have noticed in zen, when free muse limit is over, I can't use space bunny
    
    Other free models work fine
  - **u/daniel-sousa-me** (↑9, 2026-10-15 00:43): Stealth models used to be unlimited but now when I run out of any free model, I can't use any of the others :'(
- **u/Amarsir** (↑1, 2026-10-14 19:33): We think Minimax 3.1. They might use a different naming scheme but it's almost certainly them.
    
    I don't know why they're waiting so long to reveal though. Even if they're still developing, just take credit and work on the next release. The main effect of the codename is that it's not properly benchmarked and credited. Which is fine if you're not sure. But if you see that people like it, all waiting does is ensure that by the time you reveal the competition has advanced.
  - **u/Global_Persimmon_469** (↑2, 2026-10-14 19:50): Minimax has a 3.1 flash preview version on their chat
- **u/warpaint_james** (↑2, 2026-10-14 19:35): Yeah just tried it out until I got limited. It is really nice to use. Fast, competent, verbose but not overly so. Almost anticipated a lot of what I wanted
- **u/alcogiggles** (↑2, 2026-10-14 19:46): I'm having it build a couple of python-based desktop tools and it's fast.   
    It doesn't waste tokens trying to add fillers in our conversation either. It's really efficient in responses.   
    It brainstorms ideas for me really nicely, better than chatgpt.   
    I like how it researches, does its own due-diligence against its own recommendations too.   
    It pressure tests it's own implementations. 
    
    It fixes things that deepseek 4.1 flash couldn't.
- **u/Lirezh** (↑6, 2026-10-14 19:56): According to [spacebunnyalpha.com](http://spacebunnyalpha.com) it is a router. Nobody knows for sure what it  is until officially released.  
    Like a Pareto variant with GPT Sol in the mix.
    
    I found Spacebunny to be unreliable, it can be stunning and it can be bad - it's hard to use it for something.
  - **u/Evan_gaming1** (↑1, 2026-10-15 03:47): this is your source? it says gpt 6.1 sol is the main model in the mix, even though space bunny came out BEFORE 6.1 sol.... okay
    - **u/Lirezh** (↑1, 2026-10-15 14:51): yes - and you did not read it even properly before commenting...  
        It says the core model changes the moment 6.1 was released, it was SOL 6 before.  
        So it not only uses output that looks almost identical to SOL 6.1, it also used output that was almost identical to the previous SOL 6 model right before.  
        So yes, that is good evidence - the best we have afaik
- **u/LinkiooN** (↑2, 2026-10-14 20:13): i have seen minimax way too many times when it broke on me so I am guessing it's some Minimax model
- **u/horrbort** (↑-1, 2026-10-14 20:51): It is deep seek pro 4.1

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
  - **u/Ctbhatia** (↑1, 2026-10-14 22:31): the handoff works better if it ends on the exact next tool call, not a summary, otherwise the new session re-derives the plan from scratch. have you tried it across a model swap?
- **u/repepeper** (↑1, 2026-10-14 18:40): /compact and /fork ? or pocock's /handoff
  - **u/Ctbhatia** (↑1, 2026-10-14 22:34): a handoff file is the safest of those, it survives the swap without either model having to keep the old context. is the swap mid-task or between tasks?

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
- **u/Evan_gaming1** (↑1, 2026-10-15 03:30): What is that Sisyphus Ultraworker thing?
  - **u/Dependent-Ad2705** (↑2, 2026-10-15 07:00): oh my openagent project thing, it's hot af, give it a try
- **u/levu304** (↑1, 2026-10-15 03:54): bump v2
  - **u/Environmental-Ad3110** (↑1, 2026-10-15 11:07): What
- **u/Environmental-Ad3110** (↑1, 2026-10-15 07:05): edit: problem just gone after like 10 hours, idk what was that i did nothing to fix that lol. Guess this is Opencode problem.

---

## My last month's model stats
**u/LinsaFTW** · 2026-10-14 14:38 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5sy11/my_last_months_model_stats/)

**Comentarios:**

- **u/GRANDMA_FISTER** (↑1, 2026-10-14 17:43): What are you using them for that Luna is the only one writing to cache?
  - **u/LinsaFTW** (↑1, 2026-10-14 18:53): I am not sure, maybe something to do with those models or the platform? I use opencode and write java
- **u/ramendik** (↑1, 2026-10-15 02:09): Wait. muse spark 1.3 contributor is free on Zen? Or do you hit limits there?
  - **u/LinsaFTW** (↑1, 2026-10-15 02:28): It's OpenCode GO, my usage of free is below (i ordered by price)

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
    - **u/Infamous-Grand-5778** (↑1, 2026-10-14 21:52): no....? it averages out to like $0.05/mil tokens
      - **u/Infamous-Grand-5778** (↑0, 2026-10-14 21:52): also its 60mil per week not per month i wrote it wrong mb
- **u/xapep** (↑2, 2026-10-14 20:11): GLM 5.3 Flash is a good first try for this, I'd reach for it before the big labs' models for RE-adjacent work. On the uncensored part, keep expectations realistic: open models refuse a lot less, but none are actually filter-free, and phrasing matters more than people think. Framing the task as security research usually gets you further than hunting for a model with zero refusals.  
      
    You also don't need a subscription for any of this. GLM 5.3 Flash is pay-as-you-go on several providers; ours is EU-hosted and OpenAI-compatible, so you only pay for what a session actually burns. The comparison that matters is per-token across providers: the cheapest option moves with your context sizes and cache behavior, not with the sticker.
  - **u/slaxerz** (↑1, 2026-10-15 00:26): You are a provider?
    - **u/xapep** (↑1, 2026-10-15 09:43): Yeah, I'm with an inference provider, so full disclosure: we serve GLM 5.3 Flash among the open models (EU-hosted, OpenAI-compatible). The rec isn't tied to us though, the model is on several pay-as-you-go providers, so it's a fine first try wherever you land. What decides your cost in the end is per-token pricing against your real context sizes, that's the comparison worth running before you commit.

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
            - **u/Ctbhatia** (↑2, 2026-10-14 19:42): ah so the pane was never the gate, the plan-level list is. did that list actually stop the haiku spawns, or just hide them from the picker?
              - **u/Cyvster** (↑1, 2026-10-14 20:18): i'm not sure what opus actually did to fix it. there were a lot of problems. opencode 2.0 was ignore the config file completely. opus had to do a lot of stuff to limit models.
                - **u/Ctbhatia** (↑1, 2026-10-14 20:28): so it was reading the old config path the whole time, that explains why none of the limits took. does the new layout warn when a key is ignored, or does it fail silently?

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
  - **u/evia89** (↑2, 2026-10-14 20:18): > horse test
      
      out of the box task, not inside training database

---

## Experience Opencode v2 on termux
**u/Tasty_Owl_7930** · 2026-10-14 12:56 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5qiki/experience_opencode_v2_on_termux/)

So recently, Opencode released v2. and I've tested it on my Tecno KL4 device. Compared to v1, the v2 is smoother and more responsive, with no lag at all. and I'm running 9router and astrojs together with.

Btw i used proot distro fedora

**Comentarios:**

- **u/[deleted]** (↑1, 2026-10-14 13:18): [removed]
- **u/LuluLeSigma** (↑3, 2026-10-14 13:34): why is there a weird dynamic island
  - **u/shameless_inc** (↑1, 2026-10-14 14:12): There are Android apps that give you such a feature. Maybe the screen recorder triggered it to show up without anything else in it. Or maybe it's just the normal overlay that lets op control the recording.
    - **u/DEAD1nsane** (↑1, 2026-10-14 20:12): na. no android has a dynamic island that's ios.
        
        but there is a app called Material Capsule which is *kinda* like it.
  - **u/DEAD1nsane** (↑1, 2026-10-14 20:11): iphone
    - **u/LuluLeSigma** (↑1, 2026-10-15 06:16): well no. first there is no termux for iphone and the status bar aint iphone
      - **u/DEAD1nsane** (↑1, 2026-10-15 06:17): I didn't even see the status bar lol  ya makes sense. he's using a app
      - **u/DEAD1nsane** (↑1, 2026-10-15 06:18): https://play.google.com/store/apps/details?id=com.pryshedko.mtisland
          
          this is what I use
- **u/tinmicto** (↑1, 2026-10-14 14:34): I see you're using termux-launcher,  do you mind trying out the opencode thats in "tlstore" ? 
    
    Works natively and is v2. You can either install using the tlstore TUI or "tlstore install opencode" should also work.
  - **u/DEAD1nsane** (↑1, 2026-10-14 20:13): https://www.reddit.com/r/termux/s/DQjpAp4U3K
  - **u/Tasty_Owl_7930** (↑1, 2026-10-14 22:56): what is tlstore?
    - **u/tinmicto** (↑1, 2026-10-15 07:08): its a small tui app store that comes with termux-launcher. if you're on recent version of termux-launcher you get it by running "tlstore" 
        
          
        primarily made to distribute some of my favorite terminal apps like Sigye clock and fastfetch with .gif support, it now has some more apps including opencode v2.
- **u/JuraganMinyak** (↑1, 2026-10-14 15:18): What is the keyboard that you use?
  - **u/Tasty_Owl_7930** (↑2, 2026-10-14 22:58): the original keyboard from termux launcher 
      [https://github.com/PickleHik3/termux-launcher](https://github.com/PickleHik3/termux-launcher)
- **u/HandIllustrious8260** (↑1, 2026-10-14 16:23): what did you do to your termux
  - **u/Tasty_Owl_7930** (↑1, 2026-10-14 22:58): i used termux launcher 
      [https://github.com/PickleHik3/termux-launcher](https://github.com/PickleHik3/termux-launcher)
- **u/DEAD1nsane** (↑1, 2026-10-14 20:11): https://www.reddit.com/r/termux/s/DQjpAp4U3K
    
    already have a post for this, no proof needed.
  - **u/Tasty_Owl_7930** (↑1, 2026-10-14 22:57): i tried the Hopper2333 release before, but its go error cuz my android refuse termux to access /tmp
    - **u/DEAD1nsane** (↑1, 2026-10-14 23:30): my release is not hope2333, and theirs is not native as they claim
    - **u/DEAD1nsane** (↑1, 2026-10-14 23:31): https://www.reddit.com/r/opencode/s/9a2pBBkMxD
        
        
        here I made post on r/opencode too

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
  - **u/Aggravating-Push-207** (↑4, 2026-10-14 18:39): Or, hear me out: use real $?
- **u/xapep** (↑1, 2026-10-14 15:25): The $80 bump applies from your next billing cycle, not mid-cycle, so an already-started month keeps the old cap until renewal. Your Go dashboard shows the cycle date, and the allowance should step up after it. Docs being quiet on this is normal, worth a support ping if your renewal is close and it doesn't step.  
      
    Same models with no cap: direct DeepSeek API is the overflow lane nobody mentions. It's cache-aware per-token, no monthly ceiling beyond what you load on it, so mid-cycle walls like this one stop mattering. Keep a small balance there and the sub limit becomes a billing detail instead of a blocker.
- **u/Careless-Sugar-5144** (↑1, 2026-10-15 14:37): Same for me. I bought 3x$10 workspace 😅

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
  - **u/3amae404** (↑1, 2026-10-15 00:09): Thanks for the recording, it helped a lot. Found the bug: installing OpenCode a second time (the "Try again" button, or an update) made Buddy's Linux lose the OpenCode program, hence "opencode: not found". It's fixed in Buddy 2.1.7: update Buddy (GitHub releases, or Buddy offers it), then tap Install OpenCode again. If it still fails, could you send the first error you see?
    - **u/OptimizedGamingHQ** (↑1, 2026-10-15 04:33): Why are do I get this error when using OpenCode free models?
        
        https://reddit.com/link/pgu4gy8/video/h5cktcue7kvh1/player
      - **u/3amae404** (↑1, 2026-10-15 06:34): That one came from OpenCode's free service: it sometimes turns requests down or answers very slowly, and Buddy only showed "OpenCode: error". Buddy 2.1.8 is out: chats now use Big Pickle by default (it answered in 3 s for me, the old default took over 30 s), Buddy waits for slow models instead of giving up, and errors now say what went wrong. Update Buddy and try again. If one free model keeps failing, pick another at the top of the chat.
        - **u/OptimizedGamingHQ** (↑1, 2026-10-15 08:03): Thank you. And I'm happy to help you catch these bugs early on
            
            Is there an ability to change effort level (can affect the response time to quality ratio) or if its in plan or build mode like the desktop app has?
          - **u/3amae404** (↑1, 2026-10-15 08:05): Thanks, that helped a lot already!
              
              Effort: for Claude Code and Codex you can pick it in the menu at the top of the chat. For OpenCode not yet, because its effort options (variants) are different for each model, so Buddy uses the model's default.
              
              Plan/build: Buddy always runs OpenCode in build mode, since it has to act on the phone. There's no plan mode switch for now.
              
              Both are fair asks, I've noted them.
            - **u/OptimizedGamingHQ** (↑1, 2026-10-15 08:07): Thank you. By the way, how do you get it to control your phone? Using OpenCode models, when I give it a task like take me to my homepage it says it has no ability to see or interact with my screen.
                
                Am I doing something wrong or it only works with Claude?
              - **u/3amae404** (↑1, 2026-10-15 08:20): You did nothing wrong, good catch, that was a real bug: since OpenCode 2, Buddy's instructions weren't reaching the model, so it had the phone tools but didn't know it was a phone assistant. Fixed in Buddy 2.1.9, update and try "take me to my homepage" again.
                - **u/OptimizedGamingHQ** (↑1, 2026-10-15 08:43): It says it doesn't have write permissions when trying to get it to build something. Possible fix?
                  - **u/3amae404** (↑1, 2026-10-15 08:50): That one is on purpose: by default Buddy doesn't let the agent run commands or edit files, so it can only use the phone. To build apps, turn on Settings → Developer mode. Then it can work in its own folder and build and install apps. It's only in the GitHub version, since Google Play doesn't allow apps that build and install other apps.
- **u/Dry_Scientist_5984** (↑1, 2026-10-15 06:35): I see why it needs accessibility, how do you prove trustworthy?
  - **u/3amae404** (↑1, 2026-10-15 07:02): Fair question, and you shouldn't take my word for it. What you can check:
      • It's all open source (Apache 2.0), and the APK on GitHub releases is built by GitHub Actions from that public code, so you can read the workflow and the source it builds.
      • Buddy has no servers and no analytics. The screen content goes only to the AI provider you picked (Anthropic, OpenAI or the OpenCode model), while it works on something you asked.
      • Sending, posting, paying, deleting and adding to cart always stop on an approval card. Buddy enforces that itself, not the model, so a model can't skip it.
      • You can turn the accessibility service off in Android settings any time.
      If you find a way around the approvals, please report it privately on GitHub and I'll fix it fast.
- **u/alexzzzz** (↑1, 2026-10-15 07:30): I installed Termux on my phone, set up ssh access, and then just asked my Opencode on PC to install Opencode on my phone.
  - **u/3amae404** (↑1, 2026-10-15 07:42): Nice, that's actually how Buddy started: Claude Code in Termux. That gets you a shell, but the agent still can't see or tap other apps. Buddy adds that part: an accessibility service so the agent can read the screen and tap through apps, a bubble to ask it from anywhere, and approval cards before it sends, pays or deletes. If you only need the shell, Termux is perfect.

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
  - **u/SkanePrime** (↑2, 2026-10-15 06:11): It checks your Console account directly, so usage from other machines should show up too, as long as you’re using the same account/workspace. It refreshes every 60 seconds while OpenCode is open, or you can refresh it yourself with /quota.
- **u/squirrelscrush** (↑1, 2026-10-15 02:35): Doesn't the opencode-quota plugin do the same while also giving the stats on token usage and allows for most providers?
  - **u/SkanePrime** (↑1, 2026-10-15 06:22): Yeaaa, there’s overlap, I mainly wanted a V2-friendly sidebar with reset timers and a little /quota popup. Mine shows provider allowances and balances, but doesn’t track token usage.
    - **u/squirrelscrush** (↑1, 2026-10-15 14:12): btw it's great work, I liked the UI aesthetic, it feels much more polished and beautiful.
  - **u/SkanePrime** (↑1, 2026-10-15 06:22): Would you find token tracking useful here though? Like tokens used this session, daily spend, or something else? Happy to look into it if it’d help.
    - **u/squirrelscrush** (↑1, 2026-10-15 13:56): I feel there can be an opportunity to show the price, token usage, cache hit rate for each message too. And some kind of reminder system for a set price limit, probably it can be set in a .jsonc file.
      - **u/SkanePrime** (↑1, 2026-10-15 14:00): Ohh, per-message stats would be useful. Especially cache hit rate. And a configurable spend reminder sounds handy too. Would you want that limit per session or per day tho? I’d probably keep the detailed stats in /quota so the sidebar stays tidy
        - **u/squirrelscrush** (↑1, 2026-10-15 14:50): The reminders can be per day, that sounds better with subscriptions
            
            The detailed stats in /quota would be the correct choice
- **u/aarz03** (↑1, 2026-10-15 08:47): how does quota work for free tier? does this plugin work for free tier aswell?
  - **u/SkanePrime** (↑1, 2026-10-15 13:55): It depends on the provider. The plugin just shows whatever quota info your connected account. I haven’t tested free-tier accounts yet though. Which provider are you using?
    - **u/aarz03** (↑1, 2026-10-15 14:03): im talking about the free opencode models (might be referred as zen-free)

---

## Gemini 4 Argon is now in OpenCode Go 🔥
**u/afanasenka** · 2026-10-14 07:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x5l5bm/gemini_4_argon_is_now_in_opencode_go/)

$60 usage til Nov 30

**Comentarios:**

- **u/andari3727** (↑2, 2026-10-14 07:53): oh my god
  - **u/FiccoFicco** (↑1, 2026-10-14 20:05): expensive junk
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
  - **u/GRANDMA_FISTER** (↑1, 2026-10-14 22:37): What does this mean, contributor use?
    - **u/Calm-Caterpillar2103** (↑1, 2026-10-15 00:58): r/commentmitosis but basically they train off of your messages I think
      - **u/GRANDMA_FISTER** (↑1, 2026-10-15 01:16): Oh, interesting. Well honestly, if it's well subsidized, I don't mind. Just gotta be careful with personal stuff I guess
        - **u/Calm-Caterpillar2103** (↑1, 2026-10-15 01:17): Yeah, it doesn’t matter because 10 messages later your already hitting the 5 hour limit and used 3% of your monthly quota
  - **u/GRANDMA_FISTER** (↑1, 2026-10-14 22:37): What does this mean, contributor use?
- **u/evanvelzen** (↑1, 2026-10-14 13:30): I have used this the last 2 days and this will be my daily driver. 
    
    I am sometimes dissapointed by DeepSeek v4.1 Flash and Muse Spark 1.3. Gemini Flash 3.8 was always a better coder but at its price point you were better off using Claude Opus or Sonnet.
- **u/MeOneThanks** (↑7, 2026-10-14 17:42): I gave it a simple task: redesign a static web page (just a one-pager, nothing crazy)  
    It ended up reading 105 files and then ran out of my rolling 5h quota. not a single word from the model.
  - **u/RedditAtWork23** (↑1, 2026-10-14 18:22): Congratulations you have made google and the nsa proud today
- **u/Fit-Inevitable6294** (↑1, 2026-10-15 02:53): Yuck !!!

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
        - **u/Original_Goznab** (↑1, 2026-10-15 09:14): No they don't. They can find out their name with some research but they don't know it.
          - **u/Robert__Sinclair** (↑1, 2026-10-15 09:43): Yes they do. Is setup in the finetuning and post learning. You don't know much about LLMs, do you?
- **u/Meandernder** (↑1, 2026-10-14 01:20): Maybe it got bored
  - **u/Robert__Sinclair** (↑2, 2026-10-14 01:30): Your code is that bad? :P
    - **u/Meandernder** (↑1, 2026-10-14 09:07): Huh who is the op if this post? Excuse me i must be mistaken.
- **u/the_man_inTheShack** (↑1, 2026-10-14 08:10): I've been using big pickle for a few months now and overall it has been pretty good - especially since around the end of August when there was a big improvement. But never fast, and for the last couple of weeks been suffering from sleeping sickness more and more. Then yesterday I started using qwen3.8 locally, I wont be going back. Fast and every bit as good as big pickle has been at its best so far. I do have a good rig tho' 32G vram and running qwen3,8 27b 6bit quant with k & v set to int8 and a 128k context.
- **u/justmaybe888** (↑1, 2026-10-14 08:47): I wish providers were more transparent about there changes. Even a small update explaining what happens would save everyone so much guessing.
- **u/[deleted]** (↑1, 2026-10-14 12:02): [removed]
- **u/alcogiggles** (↑1, 2026-10-15 04:26): Mid June to Early July was the golden age of Big Pickle.   
    There will never be another like it.   
    But yesterday's experience with Space Bunny was super similar.   
    Crossing my fingers Space Bunny stays like this for awhile.

---
