# r/opencode — hilos 2026-10-15 → 2026-10-18
_Generado: 2026-10-17T19:26:03.191307+00:00 · 199 hilos · 1905 comentarios · fuente: Arctic Shift_

## Hermes' biggest competitor showed up
**u/ArtAdventurous5863** · 2026-10-17 19:15 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8ilwr/hermes_biggest_competitor_showed_up/)

&#x200B;

I'll be upfront: part of the reason I'm writing this is the referral promo. But I figured if I'm going to shill a code, I might as well write the honest version first, including the parts where Meta annoyed me.

I've been running my own assistant for months. Hermes, on an old laptop I had lying around. Telegram frontend, bunch of API keys duct-taped together. It was cool. It was also a second job.

What finally broke me was the money side. Month after month of API bills. And the cheaper the provider, the less I trusted what was actually on the other end. I'm fairly convinced a lot of these relay outfits just serve you whatever costs them least and pocket the difference. Got burned enough times that I built a little tool to fingerprint which model I was really talking to. That tells you something about the state of things.

Hermes was also just thirsty. I'd look at token counts after a long session and wince.

So I tried Muse mostly out of spite, to prove to myself the free corporate thing couldn't be that good. It's... fine. The model is Muse Spark 1.3. It handles long messy multi-step stuff without falling apart, which is more than I can say for half the "flagship" models those relay guys claimed to be serving me. I wouldn't call it magic. It just works, most of the time.

The useful part is it has its own machine. Terminal, browser, files. It remembers things between chats, runs stuff on a schedule in the background. I ported my whole Hermes setup over. Skills list, SOUL file, USER file, memory. All of it. So it felt less like switching assistants and more like giving the same one a better computer.

Now the stuff that pisses me off. That machine isn't really yours. It lives in a VM Meta swaps out whenever they deploy. Specs change, processes die, no warning. Forget running a VPN on it or getting a public IP. Not happening.

I make audiobook videos. A 10-hour static-image encode takes about two hours, and if the VM gets replaced mid-encode it's back to zero. I've lost count of how many nearly finished renders evaporated. That one still stings.

One heads-up about the referral system itself: the 48-hour clock is brutal. It starts at signup, not when you've figured things out, and once the option disappears there's no getting it back. Set a reminder the moment you sign up.

Oh, and it's Meta. Hermes isn't dead, it still does my privacy-sensitive stuff. Private things stay on my own box. Everything else is on Muse now. That's the split.

So yeah. The promo: both sides get 1 billion tokens. I know, sounds made up. It's real. Max you can pull in from invites is 30 billion, so codes get used up fast.

How to actually redeem it, since the UI buries it:

1. Sign up at muse.ai/join with your Meta account (VPN set to US or Canada, just for signup)

2. Open the app, go to Settings, then Redeem invite code (on the web version it's under Settings > General > Usage)

3. Punch in the code: 4CXP0H. Within 48 hours of signing up, or the option is gone for good

Practical stuff: if a code is dead, grab another, they have limited uses. After signup, any IP works, doesn't matter where you are. Free plan gives 100M tokens a week anyway.

Age verification: they want an Instagram or Facebook account, or they put a $1 hold on your credit card and return it after about a week. I went through Instagram, no problems at all.

Mine is 4CXP0H. Hope it works out for you, and if you use my code I'd really appreciate it.

---

## When would be have deepseek 4.1 flash 1017 on go plan? thanks !
**u/No_Run_6960** · 2026-10-17 18:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8i228/when_would_be_have_deepseek_41_flash_1017_on_go/)

When would be have deepseek 4.1 flash 1017 on go plan? thanks !

**Comentarios:**

- **u/No_Run_6960** (↑1, 2026-10-17 19:00):     :[{"id":"deepseek-v4.1-flash","object":"model","created":1792263501,"owned_by":"opencode"}
    
    that is what  appears on  [https://opencode.ai/inference/go/v1/models](https://opencode.ai/inference/go/v1/models)   ,  so do we already have the 1017 version ?

---

## OpenCode is selling data (your api keys and data is unsafe)
**u/wpbrgiejoe** · 2026-10-17 18:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8i195/opencode_is_selling_data_your_api_keys_and_data/)

OpenCode is selling all your data and api keys.

https://i.redd.it/40z8i86wo2wh1.png

Email [help@anoma.ly](mailto:help@anoma.ly) and ask them info on all your data they are selling.  


API keys are also sold it seems as anthropic and openai keys got used from people. Why were they saving and selling it?

  
I have sent them many emails asking about all this and they never respond.

---

## Anyone else having an issue with DeepSeek v4.1? Regarding the context being completely blasted in a way I didn't think was possible
**u/Historical-Sound8236** · 2026-10-17 18:51 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8i0na/anyone_else_having_an_issue_with_deepseek_v41/)

![img](omrzgpq2q2wh1 "An OpenCode CLI interface showing one singular word being said, and then context being held at 138%, right after a previous compaction.")

Why is this happening? It has been stuck in a compaction loop and I can't seem to stop it...

---

## OpenCode security breach, rotate your keys
**u/jpcaparas** · 2026-10-17 18:21 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8haw1/opencode_security_breach_rotate_your_keys/)

---

## ⚠️ OpenCode security breach
**u/afanasenka** · 2026-10-17 18:02 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8gtvi/opencode_security_breach/)

.

**Comentarios:**

- **u/QazCetelic** (↑17, 2026-10-17 18:08): "distillation attack"? Do they mean someone using their API to train their own models?
  - **u/bartsimpsonwin** (↑4, 2026-10-17 18:22): I think it was related to it, like someone was distilling their models, and to get more data or whatever he managed to crack into 1.4% of users, probably people with a specific setting enabled or whatever, and took their chats to train his own ai. Since their working with anthropic Google and OpenAI I'm guessing it was a Chinese company
    - **u/excellentforcongress** (↑1, 2026-10-17 18:46): no public hacks from chinese companies yet so why would we assume that
        
        probably anthropic, openai or google framing a chinese company to get open source banned lol
      - **u/bartsimpsonwin** (↑1, 2026-10-17 18:52): Im assuming that since they're the ones that need more data the most since anthropic and OpenAI improved their anti distillation efforts, theyr the ones who recently made additions to their opencode models (GLM 5.3 and deepseek 4.1 free on opencode), they're the ones with the most history of distillation attacks and theyre the ones not included in the parties opencode is working with for remediation. Im not saying they did it, I'm saying they're the most likely ones to have done it with the most motives to do it.
    - **u/pas-un-robot** (↑1, 2026-10-17 18:48): I was affected and a few of the attackers chats were saved in my chat logs. They are in Chinese.
        
        ETA:  not that it proves anything, only a handful out of many thousands of requests had logging on, for all  I know the rest of the requests are in any number of languages.
  - **u/pizzababa21** (↑1, 2026-10-17 18:41): Given that they said it effected certain users, it's likely someone was intercepting their traffic to pirate user data
- **u/cometrider2670** (↑6, 2026-10-17 18:09): This looks bad, I have an OpenCode account but I don't have a subscription. How this affects me? Should I do something? I use OpenCode with DeepSeek sometimes, but the API keys are from DeepSeek. I don't have much credits, about $10 on DeepSeek platform, can someone explain me? Should I be worried?
  - **u/AdFun4897** (↑6, 2026-10-17 18:12): You have a $10 plan, dont even worry about it
    - **u/Affectionate_Fact854** (↑3, 2026-10-17 18:15): Hahaha their personal diary might get leaked and used for training data
  - **u/Wise-Chain2427** (↑3, 2026-10-17 18:15): It's fine
  - **u/Strict-Prune-879** (↑2, 2026-10-17 18:22): tu n'es pas concerné
- **u/sulliwan** (↑9, 2026-10-17 18:17): How does a distillation attack get the user's API keys? This makes no sense.
  - **u/pizzababa21** (↑1, 2026-10-17 18:43): Did they say they got access to someone's API keys? I was taking this as someone was intercepting their traffic to steal user data.
- **u/reybrujo** (↑3, 2026-10-17 18:23): Forced me to login again and create a new API key.
- **u/SomeOrdinaryKangaroo** (↑2, 2026-10-17 18:33): Probably moonshot ai and deepseek getting more creative after anthropic locked their shit down
- **u/NoOneMan79** (↑2, 2026-10-17 18:36): Working with them? Hey Google Anthropic and OpenAI, stop distilling eachother's models!
- **u/mamelukturbo** (↑1, 2026-10-17 18:56): Unless you do your erps in opencode I don't see why you would care what anyone does with the code snippets from your chats, neither of us programs national secrets in opencode let's be real here for a minute.
    
    I assume all my chats are used for training regardless what the eula says, the companies would be stupid not to use the best possible training data they're getting for free. It's like believing a spam company you asked to delete your account did it after they sent you an email saying they did.
- **u/HighwayNo8744** (↑1, 2026-10-17 19:00): damage control #2 if the attackers could obtain api keys of users then they also could obtain the rest of the account data. thank god my google mail is leechy mcleech with $0 credit balance and no credit card.

---

## Breach confirmed. Only 1.4% of console users affected.
**u/cloudsurfer48902** · 2026-10-17 18:01 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8gt28/breach_confirmed_only_14_of_console_users_affected/)

They've confirmed the breach to the public. Hoping those affected will be compensated or something like that.

**Comentarios:**

- **u/that_90s_guy** (↑6, 2026-10-17 18:04): >"only"
    
    Is that supposed to make this better?
- **u/This-Marzipan-9239** (↑5, 2026-10-17 18:12): shi someone consumed 200 billion tokens on my claude 5x plan
- **u/YoRt3m** (↑4, 2026-10-17 18:19): Imagine if they take only 1000 tokens from each user.  no user would notice.
- **u/Soifon99** (↑2, 2026-10-17 18:20): So what does this mean?
- **u/PerformanceSmooth850** (↑5, 2026-10-17 18:24): This is honestly impressively bad communication. How does a distillation "attack" turn into a security breach? Why did it only affect 1.4% of users? Why only console users? Why do they not describe what was actually breached at all? How and why are Anthropic and OpenAI and Google involved?
    
    Blehhh. Super sketchy.
  - **u/IntrepidMindExplorer** (↑1, 2026-10-17 18:53): They're involved because users' 3rd party keys stored in opencode were used on those 3rd party environments. They are likely working with them so they can help get people's account usage restored or refunded at the providers and likely to help track and trace where they usage of the keys was coming from.
      
      The breach is sketchy but reaching out and working with the 3rd parties is not.
    - **u/PerformanceSmooth850** (↑1, 2026-10-17 18:58): Ah, that makes more sense. For a second I was thinking that one of their internal shithead bots got loose again and did actual damage.

---

## I am locked outside the console and all my API keys are dead
**u/zhaozitian_ppp** · 2026-10-17 17:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8gc2w/i_am_locked_outside_the_console_and_all_my_api/)

https://i.redd.it/kn7dccfwd2wh1.png

Anyone have the same problem with me?

**Comentarios:**

- **u/frankhouweling** (↑1, 2026-10-17 17:42): Yep, see the other topics.
- **u/Lost-Estate3401** (↑1, 2026-10-17 17:48): [https://www.reddit.com/r/opencode/comments/1x8bas3/they\_fd\_up\_breach/](https://www.reddit.com/r/opencode/comments/1x8bas3/they_fd_up_breach/)

---

## How should AI coding agents stop burning money on long tasks?
**u/Wise_Choice7014** · 2026-10-17 17:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8gap7/how_should_ai_coding_agents_stop_burning_money_on/)

A coding agent can keep calling the model after it has stopped making progress. It retries the same failing test, repeats a tool call, or revisits an implementation without fixing the underlying problem. Each call looks reasonable on its own, but the total cost adds up.

The main controls:

\- Iteration limits: stop after a set number of steps and require a new decision to continue.

\- Retry limits: bounded retries with backoff, and clear conditions for giving up.

\- Loop detection: flag repeated actions or unchanged states. Be careful, since a repeat can be legitimate if the underlying state changed.

\- Spend budgets: estimate each call before it runs and reject calls that would exceed the remaining budget.

\- Cancellation: let the user or orchestrator stop the run, including outstanding work where supported.

They solve different problems. A step limit doesn't cap cost, because calls vary in price. A spend budget doesn't guarantee progress, because an agent can burn its budget on cheap but unproductive calls. And an in-process guard only covers the SDK methods it supports, so it won't catch every route to a provider.

would you rather have a hard spend ceiling, a maximum iteration count, or both? And should those controls live in the agent, the model-call layer, or both?

---

## I modeled this CNC mill with OpenCode
**u/Lazar988** · 2026-10-17 17:36 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8g7jv/i_modeled_this_cnc_mill_with_opencode/)

I'm working on an open source app where you can do CAD with different coding agents. To test it with OpenCode, I used Opus 5.5 to model this CNC mill. 118 parts, and I have to say the result turned out really good.

I haven't tested everything with OpenCode yet. Drawings and animations are next. And I'm curious if a cheaper model can do this too. If you have a model you'd recommend, let me know.

My goal is to make CAD possible for everyone, even without any CAD knowledge.

The app is called SOMA. It's built for fast and easy iteration on 3D models together with an agent. The agent writes the model as code and SOMA shows it in 3D right away. If something is off, you click on the part, measure it or draw on the 3D view and send that to the agent. OpenCode or other CLI agents just runs in a terminal inside the app.

The project already has over 100 stars on GitHub. Feel free to try it and give me feedback, so I can keep improving it.



GitHub: [https://github.com/Kai-Jungsthoefel/SOMA](https://github.com/Kai-Jungsthoefel/SOMA)

---

## Haven't been able to login to OpenCode, any one?
**u/Miserable_Sky_4424** · 2026-10-17 17:09 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8fjwa/havent_been_able_to_login_to_opencode_any_one/)

Trying to login using Google account but failed! Faced this error: Unable to start social login

Anyone having the same problem?

**Comentarios:**

- **u/febvigrail** (↑6, 2026-10-17 17:12): Yeah, I'm getting the same error, in an infinite loop, after having the opencode cli tool tell me that my API key has expired. Looks like something might be happening.
    
      
    Any clue on how to report issues to them?
  - **u/febvigrail** (↑2, 2026-10-17 17:18): I got onto the discord: [https://opencode.ai/discord?utm\_source=chatgpt.com](https://opencode.ai/discord?utm_source=chatgpt.com)
      
      People are talking about this login issue there, amongst the API key issues happening, apparently.
    - **u/febvigrail** (↑1, 2026-10-17 17:28): I sent an email reporting it to [help@anoma.ly](mailto:help@anoma.ly), hopefully I hear back soon.
  - **u/sh4hr4m** (↑1, 2026-10-17 17:33): same here
- **u/Creatorgaming5** (↑1, 2026-10-17 17:18): Same issue aswell.
- **u/thepointofnoconcern** (↑2, 2026-10-17 17:20): same here, might be related to the third party key hack mentioned in another thread?
- **u/nextsux** (↑3, 2026-10-17 17:22): damn same here. API key expired, unable to log in in the middle of work :/
- **u/pxawtyy** (↑1, 2026-10-17 17:26): yea same. i went to subscribe to go plan and i got the error when trying to login with github
- **u/Tough-Artichoke7600** (↑1, 2026-10-17 17:27): alguien hizo algun deploy en viernes, oh no
- **u/WittyVoltage** (↑1, 2026-10-17 17:28): Same here, came to find out, is it global, or is it me. Looks like it's global 😁
- **u/NearlyACosmologist** (↑1, 2026-10-17 17:29): I noticed that hermes was falling back to the local model frequently.
    First I saw the error in the log that the models can only be used in opencode, later that the api key was expired.
    I was able to log in with github after several attempts, and generate a new key. Let's hope this one keeps working.
- **u/thecstep** (↑1, 2026-10-17 17:30): I am logged in. They expired all of my API keys. I created a new one. Shit doesn't work. FFS hate this no announcement bull shit.
- **u/Apart_Pen9463** (↑1, 2026-10-17 17:32): Same here, It's not from your side,
- **u/headlessrambo** (↑4, 2026-10-17 17:44): They have been hacked, api keys leaked
    
    [https://www.reddit.com/r/opencode/comments/1x8bas3/they\_fd\_up\_breach/](https://www.reddit.com/r/opencode/comments/1x8bas3/they_fd_up_breach/)
- **u/seemant** (↑1, 2026-10-17 17:55): I've just now been able to log in but the API keys are still not working
- **u/FitBad4028** (↑1, 2026-10-17 17:55): same problem f
- **u/samu33** (↑1, 2026-10-17 18:06): I can login but in the console -> go panel there is not a display of the API keys

---

## Help me understand the limits
**u/Melodic_Health_8227** · 2026-10-17 17:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8ffi6/help_me_understand_the_limits/)

I am utterly confused with the opencode go subscription limits. The site nowhere says there is a blanket limit across the models. They only advertise high limits for each model individually. I used gemini argon 4 for a while (never reached the 60$ limit as advertised) and then switched to muse spark 1.3 (didn't reach the individual limit here as well). And suddenly I saw my weekly limit has been reached. Seems like each individual model limit is just a sham and we can only use as per go's blanket limit? what's the point of showing individual limit if we can't even use any model to its maximum allowed credits. Pardon me if I am misunderstanding something or if asking this question for the nth time. Thanks in advance

**Comentarios:**

- **u/Fair-Spring9113** (↑1, 2026-10-17 17:06): [https://opencode.ai/v2/docs/console/go/](https://opencode.ai/v2/docs/console/go/) scroll down to the usabe limits bit  
    also theres no need to use argon its pretty average compared to its cost to ability ratio compared to the oss models
  - **u/Melodic_Health_8227** (↑1, 2026-10-17 17:15): Thanks for the reply but this is rather more confusing. what do they refer as monthly/weekly/5h limits? I an locked out of using any model even though I never touched all of them. that makes me think there is a blanket limit as well. but isn't that misleading from what they have written in this doc?
  - **u/ManOnTheMoon2000** (↑1, 2026-10-17 17:56): What’s better to use for planning?
- **u/xRebellion_** (↑1, 2026-10-17 17:14): I explained it a bit here https://www.reddit.com/r/opencode/s/wvLyB3FZKr
    Basically, it's a percentage based limit. If you use 1$ in gemini argon (60$ limit), it means you used 1.6 percent of your monthly limit. It's not per model.
  - **u/Melodic_Health_8227** (↑2, 2026-10-17 17:21): Thanks. this helps. the documentation is quite misleading. I think i will have to do some homework on using models more efficiently. argon clearly doesn't justifies it's cost lol
    - **u/xRebellion_** (↑1, 2026-10-17 17:26): You're welcome. For opencode go if you want to get the most value usually people go with dsv4.1 flash or glm flash. Maybe mimo2.6 and muse contributor. Anything other than that are usually not worth it.
- **u/Mezezius** (↑1, 2026-10-17 17:53): You thought you got $60 usage for every single model they offer?
  - **u/Melodic_Health_8227** (↑1, 2026-10-17 18:59): I mean that’s what i thought after the first glance at the documentation. I know the numbers wont add up but then i thought maybe they’re just acquiring users by burning some cash
- **u/bmtrnavsky** (↑1, 2026-10-17 18:16): The model limits tell you how much you’d get if you only used that. It’s all drawing from one pool. Gemini is what ate your weekly limit I use Deepseek 4.1 all day and have never hit a limit because it allows more requests.

---

## Opencode va camino al desastre de la baja calidad
**u/PollutionDue7541** · 2026-10-17 16:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8f9ri/opencode_va_camino_al_desastre_de_la_baja_calidad/)

Últimamente me topo con errores uqe no tienen sentido, se nota que están trabajando en "mejorar" opencode con IA, porque no revisan nada. Este error como me lo va a sacar el mismo opencode desde la terminarl, no estoy usando mas nada. A lo mejor es un problema de version, pero acaso el mensaje no es confuso o por lo menos muy poco certero? Ademas, veo que aparecen modelos gratis disponibles para tocar, pero que no funcionan. Nada todo muy mal, muchos mensajes pero que no le dicen al usuario la realidad del problema. La primera version muy buena, las siguientes, evidentemete nada bueno

https://i.redd.it/ikvl4hby52wh1.png

**Comentarios:**

- **u/Big_Cucumber2787** (↑1, 2026-10-17 17:28): explains a lot... i thought my opencode plugins were causing these errors
  - **u/PollutionDue7541** (↑1, 2026-10-17 17:34): Crees que sea cosas de plugins? no tiene sentido, como funciona 1 dia y al otro sin actualizar ni nada deja de funcionar? No creo que sea cosa de plugins, o acaso opencode me cambia codigo por detras sin avisar. ya te digo, estoy usando la version 1.90.0 de opencode, llevo desde que salio trabajando bien, y de repente hoy tengo esos errores
    - **u/Big_Cucumber2787** (↑1, 2026-10-17 17:36): i don't think so. my point was i assumed so, but if other people are having these issues then its likely upstream
      - **u/PollutionDue7541** (↑1, 2026-10-17 17:47): Si, al parecer mucha gente esta teniendo hoy ese problema, lo cual entiendo que pueda ser normal, solo digo, que esos errores no describen para nada el problema real, solo asumimos que podria ser, y esto para cualquier desarrollador sabe que esta mal, Historicamente, los errores deben ser claros y comunicativos
- **u/Super-Veterinarian22** (↑1, 2026-10-17 17:47): Same story here. I’ve been getting the exact same error for 12 hours straight. I’ve tried several different versions, cleared all possible cache and app data, performed clean installs, tried using a VPN, and so on, nothing has helped, even though everything was working perfectly fine just yesterday.
  - **u/PollutionDue7541** (↑1, 2026-10-17 17:59): Es lo que digo, si tuvieramos mensajes de error menos genericos y mas exacto al problema, sabriamos que no debemos perder el tiempo investigando. Yo nunca me voy a conformar, soy desarrollador y nunca haria pasar a un cliente el trabajo de investigar sobre mi producto.

---

## WTF IS GOING ON??
**u/KriticOla** · 2026-10-17 16:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8f8o6/wtf_is_going_on/)

https://i.redd.it/5og9rqcg52wh1.png

https://i.redd.it/wr6q9clk52wh1.png

I just got an error message that my API Key is expired.

Okay, no problem. I can just create a new one.

When I go to login with GitHub, it says **Unable to start social login.**

WTF IS HAPPENING???

**Comentarios:**

- **u/dwky11** (↑5, 2026-10-17 16:58): same bruh, ive got this message too, looks like they resetting the default api keys?
  - **u/No_Commission_6153** (↑1, 2026-10-17 18:40): they have been hacked. and your tokens might have been spend
- **u/Fair-Spring9113** (↑2, 2026-10-17 17:03): got hte same error message aswell
- **u/Lulzagna** (↑3, 2026-10-17 17:06): Same - I've already been on the fence for going with straight Claude models, this ain't helping.
  - **u/No_Commission_6153** (↑1, 2026-10-17 18:40): they have been hacked. and your tokens might have been spend
- **u/RandiyOrtonu** (↑3, 2026-10-17 17:09): why cant i see the page to create apis
  - **u/cb060da** (↑3, 2026-10-17 17:13): they hide it deep in the menus: settings -> service account -> (choose or create account) -> add api key
    - **u/RandiyOrtonu** (↑1, 2026-10-17 17:16): thanks and man do they have expired all the old keys ??
      - **u/cb060da** (↑2, 2026-10-17 17:22): yep, all my keys are expired too
        - **u/RandiyOrtonu** (↑1, 2026-10-17 17:24): yo thanks man,
- **u/Miserable_Sky_4424** (↑3, 2026-10-17 17:11): Security breach!
- **u/KriticOla** (↑14, 2026-10-17 17:14): It does seem like they got hacked.
    
    Related - https://www.reddit.com/r/opencode/comments/1x8bas3/they_fd_up_breach/
    
    People started noticing unauthorized spending linked to their 3rd party API keys (Claude, OAI etc) added to OC.
    
    They fucked up big time
- **u/jjjjoseignacio** (↑1, 2026-10-17 17:18): Están metiendo actualización todos sus modelos me sale error
- **u/KriticOla** (↑3, 2026-10-17 17:28): Wow! This is bad.
    
    On Twitter, people are reporting huge unauthorized spending. Someone said they got hit with a $1,700 bill linked to their OC API key.
- **u/Ceextasy** (↑2, 2026-10-17 17:50): Same lol
- **u/eMPeBe_YTB** (↑2, 2026-10-17 17:52): I see a lot of post like that. I just checked mine and is fine. do anyone who has this issue had like money added to the account ?
- **u/FanMacturbo** (↑1, 2026-10-17 17:56): In opencode CLI, delete the connexion and copy/paste your (last) api key if you save it. It will work again
- **u/devanpy** (↑1, 2026-10-17 18:06): getting the same error. had to fall back to other apis. opencode is a mess rn.
- **u/iamvandevo** (↑1, 2026-10-17 18:09): I had to create a new API key
- **u/ritmaxer** (↑2, 2026-10-17 18:14): From the OpenCode account on X posted a few minutes ago: “We had a security breach last night related to a large scale distillation attack that impacted 1.4% of OpenCode Console users
    
    We have notified them all this morning via email. If you did not get an email you were not impacted, it was a subset of users who had external providers linked
    
    The incident is ongoing so we cannot share more details at this point but we are working with Anthropic, OpenAI, and Google to remediate”
- **u/SnooAvocados9030** (↑1, 2026-10-17 18:44): GG just woke up to my Qwen Token plan on 0, i guess i know why…

---

## /usage tab would be nice
**u/Saderius** · 2026-10-17 16:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8f4ew/usage_tab_would_be_nice/)

https://i.redd.it/1arbk8km42wh1.png

I don't mean much for you to brak some tos or disclose whatever, even like single dot near models that are available to use and those that are not or like time for usage to come back cuz those limits appear to vary from model to model and it created unnecessary confusion. I will gladly provide you all the data you want from me, just let me plan how to do it efficiently, please. 🙏

---

## Fingerprinting Cat-Jam
**u/andari3727** · 2026-10-17 16:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8eqcq/fingerprinting_catjam/)

TL:DR - Tokenizer identical to Qwen 2/2.5/3, And is behaviorally similar or indistinguishable from Beam. 

1. Tokenizer (usage.prompt\_tokens)

The most significant findings:

"1234567890" turns into 10 tokens, matching Qwen's tokenizer - longcat does this too, but diverges elsewhere. Others tokenize into 4 tokens, and GLM into 6.

"🐱🍔🚀" turns into 3 tokens, again matching Qwen - but without longcat. Other models tokenized into 6 or 9, with Kimi being an outliar at 8.

Also, Beam's tokenizer is Qwen - the model card lists a vocab of 152k, matching qwen 2/2.5/3.

2. Injected system prompt.

Across 5 samples, it says "I am Beam, a large language model X by Reflection", where X is either "trained" or "built"

When supplied a custom system prompt, drops that persona.

While not definitive proof - could just be intentionally misleading, but helps to keep in mind.

3. Random is not random. (weight biases)

I asked both models to provide a random number 1-1000, a random country, a random color - each test done 40 times.

cat-jam-free and beam-free produce almost the exact same random number spread (since we can't set temperature, i had sampled 40 times), while other sampled models were far from them.

Both default to blue for their color (feel personally attacked here, since I'd answer the same), while other models don't. Other similarities are also present, but I'm not dragging this out.

Personalities are followed similarly - "terse robot" got 3 words, JSON came back valid for both (json-only personality), and both similarly answered only in questions. This test is subjective, and I'd prefer to look at previously mentioned tests.

Only differences were in long, free-form answers - which i will entirely blame on the random nature of LLMs and inaccessibility to temperature settings.

4. Afterword

This is not definitive proof - i have no weight access, endpoint rejects logprobs, routing labels them differently, same tokenizer ≠ same weights.

How to reproduce it - hit the model on opencode (read the docs on how to do it), tokenizer test is just "PROBE" and then "PROBE<probe-string>", then subtract usage.prompt\_tokens. Other tests are self-explanatory i hope.

Personally, i believe that cat-jam and beam are the same, and in my experience - equally shitty. I just put them on a subagent and allow a wide fan-out with them.

**Comentarios:**

- **u/Mr_Lucas2000** (↑4, 2026-10-17 16:58): Interesting report
- **u/reybrujo** (↑-3, 2026-10-17 17:10): Honest question, why people care? This is an A/B test, they train their models, you enjoy its usage, whether it's one or the other shouldn't really matter.
  - **u/andari3727** (↑4, 2026-10-17 17:14): Knowledge for the sake of knowledge is valid IMO, feel free to disagree.
- **u/SomeOrdinaryKangaroo** (↑1, 2026-10-17 17:55): It's Gemma 5

---

## Alternatives to free Muse Spark on OpenCode? What models are you using now?
**u/Quanhau2010** · 2026-10-17 16:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8emea/alternatives_to_free_muse_spark_on_opencode_what/)

[removed]

---

## Since free Muse Spark got removed from OpenCode, what model / module are you guys using now?
**u/Quanhau2010** · 2026-10-17 16:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8el5e/since_free_muse_spark_got_removed_from_opencode/)

[removed]

---

## Opencode-BSF
**u/Low-Day3169** · 2026-10-17 16:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8e3id/opencodebsf/)

**Opencode-BSF (Better Session Folders):** a plug-and-play OpenCode plugin that gives your agent a real memory.

Every session gets its own dated folder named from your first prompt. The agent is told where it is, so it files references, images, and downloads there instead of littering your project root. Then it reads that folder back before every request, so it builds on what it already knows instead of re-deriving the same thing twice. Everything flows into claude-mem (searchable later) and optionally graphify (your knowledge graph).

**Plug and play:** clone → run install script → restart OpenCode. Works on macOS, Linux, and Windows. Two plugins, one repo, zero config edits. Notes must trace to a link you actually sent — no unsourced claims in memory.

GitHub: [https://github.com/Bonikooooo/Opencode-BSF](https://github.com/Bonikooooo/Opencode-BSF)

---

## Rate limit exceeded.
**u/Technocratix902** · 2026-10-17 15:56 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8dp83/rate_limit_exceeded/)

Getting this error and it's making the app unsuable. Can't even complete 1 chat

**Comentarios:**

- **u/astra_of_life** (↑4, 2026-10-17 15:59): I got the same error right now .
  - **u/Technocratix902** (↑1, 2026-10-17 16:16): Can't even complete 1 chat lol. Switched to cline immediately
- **u/Soifon99** (↑2, 2026-10-17 16:49): Oh no, free stuff is not working.   What should we do now? 😭
  - **u/Technocratix902** (↑1, 2026-10-17 17:01): Ik they're not obliged to give us free stuff but they shouldn't advertise it has they do.

---

## Beam o mesmo nome do modelo free no opencode
**u/Emotional-Bag-3754** · 2026-10-17 15:44 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8deww/beam_o_mesmo_nome_do_modelo_free_no_opencode/)

---

## OpenCode & Qwen3.8 9B - no tool calling?
**u/Whole-Ad2077** · 2026-10-17 15:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8dcxu/opencode_qwen38_9b_no_tool_calling/)

Hello all,  
I installed `tobestyledintro/qwen3.8-9b-distill` on a macMini and wanted to test OpenCode on my mac. Chat works nicely and usable fast.

I create a project on a local git checkout and I am in build mode. Most of the time, I only get chat output and no tool calling. simple things like `pwd` seem to work. What am I missing?

**Comentarios:**

- **u/NegotiationNo1504** (↑1, 2026-10-17 17:05): Try Ornith 1.5 9B

---

## Can someone explain the pricing model of the go plus subscription to me?
**u/andrewfenn** · 2026-10-17 15:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8d4o8/can_someone_explain_the_pricing_model_of_the_go/)

Am I being stupid or does the go plus subscription make no sense at all. You're getting the same limits as 3 ten dollar basic plans but paying an extra 10 dollars for it, totaling to 40 USD. How does that make any sense? Have I completely missed something here or are they short changing everyone on a go plus subscription?

**Comentarios:**

- **u/acakaacaka** (↑2, 2026-10-17 15:34): Yes the only plus is you only need 1 id instead of 3
- **u/Xiaomin4114** (↑2, 2026-10-17 15:41): yes. it doesn't make sense. they've explicitly stated that this is because they want to make sure they don't get fucked on capacity by giving too much away at the $40 tier, and that they're investigating it
    
    But yes, in the mean time you get less capacity than several $10 plans.
  - **u/andrewfenn** (↑1, 2026-10-17 15:48): Thanks this explains it well enough. I'm not going crazy after all.
- **u/YoRt3m** (↑1, 2026-10-17 15:50): They said that 'Go' is a break-even plan to begin with. it took them a while to get to a break-even cost\\revenue and before that they only lost. with bigger plans they might lose more money if they give a more attractive offer. they say that with a "beneficial" or "careful" plan like this the loss for them is not as bad and they can learn, adjust and improve to find the right "spot" for a plan.
    
    That's their side. for the user's side, it's more usage and you can't have more than 1 subscription anyway, so it's not like you have the option for 3-4 subscriptions.
- **u/AdFun4897** (↑0, 2026-10-17 16:17): You can ask claude to summarize it for you

---

## I built a live WebGL visualizer for OpenCode V2 agents: see subagents, tools and tokens flow in real time
**u/Rick_C135** · 2026-10-17 15:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8crsl/i_built_a_live_webgl_visualizer_for_opencode_v2/)

[removed]

---

## As you already know Muse Spark 1.3 Free got phased out... 😭
**u/DEAD1nsane** · 2026-10-17 14:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8c935/as_you_already_know_muse_spark_13_free_got_phased/)

I used the opencode free DeepSeek to help me figure things out... I hear DS is really good  but my issues were:
1. DS would not respond with any explanation, but instead jump straight I to coding.  
2. DS's responses were super lengthy and very detailed but a bit too detailed for me.  
so I used it to help me find an alternative that worked like MS, responded like MS, and is still in the opencode free zone.  
  
so it looked into my stats and everything and told me that my options were:  
- GLM 5.3 Flash Free
- Space-Bunny Free  
that's when I said "okay between the two options, how do I pick?

## The Response After Comparing: 
> The context window decides it. Your steps carry ~112k tokens on average, and on space-bunny specifically you averaged ~207k tokens per step (248.6M ÷ 1.2k). glm-5.3-flash-free's 200k ceiling sits below that working set, so you'd be compacting context constantly and losing detail mid-task.
> Space-bunny's 1M also matches the Muse model you lost (muse-spark-1.3 and the deprecated contributor variant are both 1,048,576) — closest structural match to what you had. Secondarily, space-bunny has 1.2k steps of proven history on your actual workload; glm has none.  
  
## The Verdict:  
Space Bunny Free

**Comentarios:**

- **u/nadir40** (↑1, 2026-10-17 15:40): For sure they will it by better one
  - **u/DEAD1nsane** (↑1, 2026-10-17 15:44): huh
- **u/cuddle-bubbles** (↑1, 2026-10-17 17:54): they got all the training data they needed
  - **u/DEAD1nsane** (↑0, 2026-10-17 17:54): yes, ok?
- **u/Icy-Examination-9512** (↑1, 2026-10-17 18:50): dude you can literally just customize dsv4.1 to do all that. deepseek is miles better than all the other models and you can adjust it to be 1m context

---

## Opencode 2, OMO test de modelos
**u/royxcobar** · 2026-10-17 14:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8c87i/opencode_2_omo_test_de_modelos/)

Llevo un par de semanas en ratos (optimizando mi stack) si así puede llamarse de opencode-go,  estoy actualizando proyectos viejos y una subscripcion ahora de 20 usd es un lujo para, mi.

Estoy usando OMO oh-my-opencode y acabo de actualizar a opencode 2.

La idea es usar el agente mas economico-rapido, según convenga a los agentes de OMO, y claro uso mcp memory...  


En fin solo quería compartir este hallazgo, 

Para mi he tenido buenos resultados, y no agoto mi cuota aunque trabajo mas de 5 horas al día...

Saludos.

https://i.redd.it/smhh97f8j1wh1.png

---

## How do i use a backup workspace in api key in omniroute?
**u/unchained_io** · 2026-10-17 14:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8c7xi/how_do_i_use_a_backup_workspace_in_api_key_in/)

i bought a backup opencode go subscription and im trying to use it in omniroute but its not showing up.  anyone point me to a guide on how to use these diff workspaces in tandem, ie. load balance between diff workspaces via api key?  im using omniroute

---

## Free DSV 4.1, GLM 5.3 Flash, and MiMo 2.6 flash for a month
**u/Whole_Succotash_2391** · 2026-10-17 14:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8c4u6/free_dsv_41_glm_53_flash_and_mimo_26_flash_for_a/)

Open Source AI is actually start to win, hard. Some of the absolute best coding models have been hitting, week after week after week. It's been a crazy few months for opensource AI. While a lot of the plans are tightening or closing free rails, we're offering free DSV4.1 Flash, GLM 5.3 Flash and Mimo 2.6 Flash for a month on Phoenix Grove API. We opened this up a few weeks ago for two groups of 500 members to test inference. We are now opening it up further after a a great couple of weeks.

People are out there looking for options. Here is one.

Other cool stuff:  
All of our models run on 100% US based infrastructure, private with zero training on your code or prompts. Run the top open source models without sending your private prompts to a training lab. No complications, no "some models are private, other's aren't." They all are, all the time.

We host 20+ other major models in case you ever want to upgrade (no pressure though). Including the Kimi family, GLM, Qwen, Nemotron and bunch of others. On average our token pricing is 20% lower than market.

Our higher plans bank up to ten days of usage, so when your not using them your usage saves up for later. Usage doesn't go to waste, so you can actually code when you want to.

The intro plan is a free one month trial with the standard cancel anytime, it bills at 3.99 after that. Use it, cancel it, that's fine. Free Flash for a month.

Figured i'd keep this short because we all know the new flash models are the point :)

For the API plan: [api.pgsgrove.com](http://api.pgsgrove.com/)

If you want to read more about us as a company, just [pgsgrove.com](http://pgsgrove.com/)

Also: Theres a lot going on in the background with major AI companies right now. We are at a major turning point in the industry.

This is happening because companies that were purely investment based, now need to answer to their investors. Initially, "endless usage" brought users in, but now many of the companies simply cannot afford to support what they were offering. The problem has often been a loss based business model that is finally running dry, and the whole flow of free access dries up.

There are several tactics that the major AI coding plans use to extract the most they can from their customers. Here are some examples, and what we are doing differently to put the users first. PGS AI was built with a sustainable business model from the ground up, so we can actually offer great usage rates without tricks.

Wasted usage is part of the AI industry, and they plan on it: Most coding plans bet on you letting usage go to waste. The plan goes: "how do we get people to think our coding plan offers a lot of usage, but then break it up into weeks and rolling windows so no one can ever actually use it all."

On PGS coding plans, unused usage windows get banked for you to use later. So if you don't use the service for a 5 hour window, it get's put into your usage bank so you can keep going on busy coding days. Up to ten days at a time can stay in the bank, and it rolls over every month.

Many in app subs and coding plans are glorified training pipelines: This comes along with "how do we harvest this data for training without being too loud about that." Unless the company tells you otherwise, your data could be hopping all over the world, being harvested by the individual labs or service companies. Some are better than others, but many of these companies rely on users just not noticing or caring that their data is being used for training. Data sales and marketing telemetry sales happen. This means that your private info, your personal life, and anything else you send through the system could become part of a training corpus for the next AI, or a marketing data set for a large company. We have explicitly built for privacy, so your code and prompts stay yours.

Privacy and ease of use should be available for everyone, there are a few options out there for truly private inference, and we'd love you to give us a try. No matter what, we all deserve data sovereignty and access to great AI.

---

## Who is Beam Free Model ?
**u/IlNaka** · 2026-10-17 14:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8c0uy/who_is_beam_free_model/)

https://i.redd.it/04wggszfi1wh1.png

Beam Free is a new model ?

**Comentarios:**

- **u/WegoW** (↑1, 2026-10-17 14:52): https://reflection.ai/blog/introducing-beam
    
    https://youtu.be/YsSRZvqYdiY
- **u/AdFun4897** (↑1, 2026-10-17 14:52): Its a social construct, dont use it
- **u/RelativeArtist4129** (↑1, 2026-10-17 15:12): It's Mr. Bean. Back as a model :p  (Seriously Reflection's model. I'd call it mid tier level but this version is not working for me with Opencode)

---

## PLEASE DAX SPACE BUNNY UNLIMITED FOR A WEEK AGAIN
**u/nuelgoeshard** · 2026-10-17 14:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8c00h/please_dax_space_bunny_unlimited_for_a_week_again/)

[removed]

---

## As you already know Muse Spark 1.3 Free is depreciated... here is what I'm doing
**u/DEAD1nsane** · 2026-10-17 14:44 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8bz65/as_you_already_know_muse_spark_13_free_is/)

I used the opencode free DeepSeek to help me figure things out... I hear DS is really good  but my issues were:
1. DS would not respond with any explanation, but instead jump straight I to coding.  
2. DS's responses were super lengthy and very detailed but a bit too detailed for me.  
so I used it to help me find an alternative that worked like MS, responded like MS, and is still in the opencode free zone.  
  
so it looked into my stats and everything and told me that my options were:  
- GLM 5.3 Flash Free
- Space-Bunny Free  
that's when I said "okay between the two options, how do I pick?

### The Response After Comparing: 
> The context window decides it. Your steps carry ~112k tokens on average, and on space-bunny specifically you averaged ~207k tokens per step (248.6M ÷ 1.2k). glm-5.3-flash-free's 200k ceiling sits below that working set, so you'd be compacting context constantly and losing detail mid-task.
> Space-bunny's 1M also matches the Muse model you lost (muse-spark-1.3 and the deprecated contributor variant are both 1,048,576) — closest structural match to what you had. Secondarily, space-bunny has 1.2k steps of proven history on your actual workload; glm has none.  
  
### The Verdict:  
Space Bunny Free

**Comentarios:**

- **u/AdFun4897** (↑0, 2026-10-17 14:52): You mean “deprecated”?
  - **u/DEAD1nsane** (↑1, 2026-10-17 14:52): wow was that really worth the comment?
  - **u/Human-Equivalent-154** (↑0, 2026-10-17 14:53): 🫩
    - **u/DEAD1nsane** (↑1, 2026-10-17 14:56): 😮‍💨
  - **u/DEAD1nsane** (↑1, 2026-10-17 14:56): `Depreciated` is the past tense and past participle of the verb depreciate, meaning to lose or lower in monetary or real-world value over time.

---

## Can you please help me understand the new dashboard?
**u/Leather-Cod2129** · 2026-10-17 14:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8bw0n/can_you_please_help_me_understand_the_new/)

Hi

What is the monthly budget? I've just bought a $10 Opengo plan and $5 credits.  
Don't understand this monthly budget nor where it comes from nor when opencode uses it.

Nor the fact the "rolling" always remain at 0%

  
Thanks

https://i.redd.it/4trlxnv9h1wh1.png

**Comentarios:**

- **u/Mysterious_Nebula418** (↑1, 2026-10-17 17:02): Look at the name of model you are using. Does it have "Go" at the end, e.g. DeepDeek V4.1 Flash Opencode Go? If so, it uses your Go plan. Otherwise (unless it's free model) it uses your credit. Wasted few dollars myself before noticing this.
  - **u/Leather-Cod2129** (↑1, 2026-10-17 17:48): But what is the monthly business?
    - **u/Mysterious_Nebula418** (↑1, 2026-10-17 17:51): You mean Monthly budget? Guess you have setup your credit autorenewal

---

## RIP
**u/rematskayt** · 2026-10-17 14:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8bosg/rip/)

R.I.P Muse Saprk 1.3 in Ukraine

**Comentarios:**

- **u/aliencreature12** (↑-1, 2026-10-17 14:38): no body care they should be free anyway stealing data they charge money for it. deepseek for the win
  - **u/YoRt3m** (↑2, 2026-10-17 14:40): stealing?
    - **u/aliencreature12** (↑2, 2026-10-17 14:49): "contribute" your data to meta training their model with it
      - **u/YoRt3m** (↑1, 2026-10-17 14:53): How is this stealing? do you think Deepseek-Flash-4.1-Free doesn't do that?
        - **u/aliencreature12** (↑1, 2026-10-17 15:25): read the doc again for paid opencode go models zdr for deepseek
- **u/motasimrahman** (↑2, 2026-10-17 14:40): Ohh noo
- **u/TerribleFault7929** (↑4, 2026-10-17 15:01): It was \_really\_ good
- **u/Additional_Cod_6445** (↑4, 2026-10-17 15:25): Thats the saddest part. 😓
- **u/clear_master** (↑1, 2026-10-17 15:35): 😢
- **u/nadir40** (↑-1, 2026-10-17 15:36): Maybe they will put deepseek v4.1 flash 1017
  - **u/Emotional-Bag-3754** (↑2, 2026-10-17 15:41): Sonhando
- **u/Emotional-Bag-3754** (↑3, 2026-10-17 15:40): Va embora com meus dados para vc lembrar de mim
- **u/reybrujo** (↑1, 2026-10-17 15:49): Not good enough to pay for it?
- **u/Ok-One1885** (↑1, 2026-10-17 15:57): So what is the best free model now?
- **u/nikitaluger** (↑5, 2026-10-17 16:03): RIP indeed, lucky GLM 5.3 flash is there to take it's place and is surprisingly very meticulous with debugging.
- **u/Specialist-Donut6948** (↑1, 2026-10-17 16:13): Is GLM 5.3 Flash Max better than muse spark 1.3 xhigh?
  - **u/ari-eunoia** (↑7, 2026-10-17 16:49): Depends on your needs but muse spark > glm for the most part
- **u/Easy_Cauliflower7504** (↑1, 2026-10-17 16:28): Yo uso big pickle con las skill de superpower y anda espectacular con proyectos de todo tipo, Javascript, node, react etc etc , mucho debugueo, consistencia en las respuestas poca iteración ..
  - **u/ivaansridev** (↑1, 2026-10-17 17:19): That model is a big overthinker 😭
- **u/krrish253** (↑1, 2026-10-17 16:34): I am still crushing muse spark.. Can't imagine it going. Is it gone for u guys?
- **u/SeaStep7879** (↑1, 2026-10-17 16:51): There is deepseek V4.1 flash free, now
  - **u/ivaansridev** (↑1, 2026-10-17 17:20): Wait it's free again?
    - **u/SeaStep7879** (↑1, 2026-10-17 17:30): Yes but i think it have very small limit
      - **u/ivaansridev** (↑1, 2026-10-17 17:37): Huh i used it until it was gone from my library
  - **u/Significant_Spring87** (↑1, 2026-10-17 17:52): I love using dsf 4.1/glm 5.3 f with opus 5.5 as orchestrator
- **u/zeamp** (↑1, 2026-10-17 17:17): F
- **u/Parking_Soil2623** (↑1, 2026-10-17 17:30): Ayer no funcionaba mimo 2.6 flash... Respondía "coming soon"
- **u/mdsiaofficial** (↑1, 2026-10-17 17:59): What does it mean

---

## Coding Agend?
**u/Quaxttv** · 2026-10-17 14:26 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8bkxa/coding_agend/)

Hallo Leute,   
Ich habe einen plan für eine App an der ich arbeiten möchte und weiß nicht welchen Agend ich benutzen soll. Ich plane eine App mit komplexen Analytischen Methoden um Werte zu berechnen und habe am prototyp mit Deepseak 4.1 Flash gearbeitet aber ich finde seine UIs sehen nicht so aus wie ich es mir vorstelle und egal wie viele promts ich benutze er bekommt meine Vision nicht so richtig hin. Ich suche deshalb einen Agend der gut backend schreiben kann und einen der gute Uis bauen kann.

**Comentarios:**

- **u/AdFun4897** (↑-1, 2026-10-17 14:33): Hallo, heil fuhrer
- **u/dumbasPL** (↑1, 2026-10-17 18:10): Not a German subreddit btw mein fuhrer

---

## Blender 3D agentic models
**u/Longjumping_Guard726** · 2026-10-17 14:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8beby/blender_3d_agentic_models/)

Has anyone tried building Blender 3D agentic models (lowpoly 3D models purely generated from code) with an opencode go/ any low cost subscription?

Im a 3D artist myself and I have a huge library of 10,000+ lowpoly assets library I collected for a few years. I have already extracted geometry and indexed them using Gemini but I want to use them as references and generate codes when I ask for a model.

For example: if you ask for a low poly house from a model, it will try to put cube over cubes and make it geometrically. But artist-made lowpoly assets have a ‘soul’ where each and every vertex is deliberately placed to get a chunky, blocky silhouette. I could do that with opus 5.5 or Astra 6 but it is very costly. Has anyone tried something like this?

Or any better way to use my library to do this?

**Comentarios:**

- **u/Gunnarz699** (↑1, 2026-10-17 14:50): Blender is the wrong tool for programatically generating models. Either you use one of the many very good 3d gen models, use OPENSCAD or another parametric modeler, or use FreeCAD with python scripting.
  - **u/Longjumping_Guard726** (↑1, 2026-10-17 15:47): Aha good idea! Thanks

---

## I made an enhanced OpenCode with AI auto-approval for permissions and memory module.
**u/Maleficent-Drop-1671** · 2026-10-17 14:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8bcoq/i_made_an_enhanced_opencode_with_ai_autoapproval/)

**Comentarios:**

- **u/investigatormaker** (↑1, 2026-10-17 16:59): AI auto-approval for permissions is the part people will poke at first: what can the approver say yes to on its own, and what always comes back to you? If the README doesn't already open with a short list of actions it never auto-approves, plus where to see a log of what it approved, that's the thing that earns trust. Saying which upstream OpenCode version the fork tracks also helps people decide to switch.
    
    I make ThreadFox. Our AI employee can explain the fork in coding-agent threads about permission prompts and memory, then handle the replies; Starter is $199 for 30 days, or we'll post 3 for you free first, no card: https://threadfox.vip/p/eem47/managed

---

## They F’d up [BREACH]
**u/horstenegger** · 2026-10-17 14:14 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8bas3/they_fd_up_breach/)

**Comentarios:**

- **u/razorpolar** (↑25, 2026-10-17 14:20): Just came to post the same thing, $400 unauthorized spend on our Anthropic account today as a result of this
  - **u/ad-on-is** (↑19, 2026-10-17 17:16): now we know where all the free stuff comes from
- **u/Dangerous_Leave_4413** (↑2, 2026-10-17 14:31): Fermi.gg's daily question tomorrow:
    How much money in API credits does OpenCode owe to their users?
- **u/jochali** (↑1, 2026-10-17 14:39): same here
- **u/StevenB0ss** (↑3, 2026-10-17 14:41): Does it also counts for oauth of openai? Or only keys? Why tf they store this anyways ?
  - **u/look** (↑3, 2026-10-17 15:23): Yeah, it’s not immediately obvious why those would ever need be stored anywhere besides your own computer…
- **u/Mezezius** (↑19, 2026-10-17 14:43): looks like someone vibecoded their security system
  - **u/Key-Interaction-2057** (↑12, 2026-10-17 17:17): It is kinda funny how much they were bragging about agents doing most of the work.
- **u/Spirited-Test-1410** (↑11, 2026-10-17 14:48): 😂 ts funny as hell. Vibe coding security system is crazy.
- **u/FamilyRon** (↑10, 2026-10-17 14:52): So this explains why my credits were used. Good that I did not have auto-recharge on.
  - **u/Capable-Guide98** (↑2, 2026-10-17 18:23): Same. They spent like 10 bucks but no auto recharge
- **u/synthaesthetics** (↑2, 2026-10-17 14:54): This happened to me with anthropic/claude, I switched back to opencode and never used claude/open AI again.
    
    There's a new type of hack where they upgrade your sub and use your credits/tokens.
- **u/krenuds** (↑15, 2026-10-17 15:00): Dax should probably spend less time shitposting on twitter and more time on watching his agents.
- **u/pas-un-robot** (↑7, 2026-10-17 15:03): > please revoke **and replace** those keys
    
    Yeah no - if you think I'm ever pasting new API keys into your service again after you leaked them you're dreaming
- **u/iconiconoclasticon** (↑3, 2026-10-17 15:05): I was startled last night to get alerts from Claude and OpenAI about my credits being used when, in fact, I didn't use them. This morning I got the mail about the breach.
- **u/Cultural-Insurance97** (↑1, 2026-10-17 15:22): Luckily I had only like $10 unauthorized spend, but I've spend all morning looking how I was hacked, and what was compromised.
- **u/Lost_County_3790** (↑2, 2026-10-17 15:24): Is it the same for open router keys saved on my open code project in my desktop? Or is it for people putting them on open code website?
  - **u/SuperSlowSubie** (↑2, 2026-10-17 17:52): OpenRouter is fine. If you had keys in OpenCode Console, then your fucked.
  - **u/Decent-Elk-4700** (↑1, 2026-10-17 17:53): Important to understand this. Anyone knows?
    - **u/Railander** (↑1, 2026-10-17 18:41): i didn't know this, but apparently you could add keys directly from their website (https://opencode.ai/console/) and it'd be saved on their servers, as opposed to if you add them from the opencode client/cli, which saves them in your own PC.
        
        don't know if the Go subscription was affected, but doesn't seem like it.
- **u/HotLion7** (↑1, 2026-10-17 15:37): My codex usage went from 90% to 0% overnight while I wasn't using it, that could be the reason.
  - **u/Thomas-Lore** (↑2, 2026-10-17 16:36): No, this was a codex issue. It was widely reported on r codex.
- **u/ProtolZero** (↑5, 2026-10-17 15:41): I thought the third-party keys are stored locally.....why are they on opencode's server?
  - **u/RogerAI-fm** (↑11, 2026-10-17 16:43): that’s what i would have thought too, that’s why it’s important to design correctly wth OC.
  - **u/kosciak9** (↑6, 2026-10-17 17:47): They are not, it’s the workspace BYOK for Zen
  - **u/helios_csgo** (↑4, 2026-10-17 18:05): They have a feature like openrouter - you can 3P keys on opencode platform (website) and use their router to call models from 3P.
  - **u/Railander** (↑1, 2026-10-17 18:42): 2 different places to store keys apparently. if you added them from the cli/desktop client, they're saved locally afaik and safe. but if you added them from [https://opencode.ai/console/](https://opencode.ai/console/) then they've leaked.
- **u/jovialfaction** (↑3, 2026-10-17 15:41): Why are third party keys ever going on their servers?
  - **u/SuperSlowSubie** (↑1, 2026-10-17 17:51): BYOK. So you can route to your own providers directly through the same API interface.
- **u/VenditatioDelendaEst** (↑2, 2026-10-17 15:53): So... are 3p provider keys in the workspace **all** that was exposed, or merely "what the attacker was immediately prepared to exploit in volume"?
    
    What about people who wired up `gh` or ssh keys?
    
    I for one am glad I am doing all of my vibecoding experiments inside a VM, 'cause the workspace sandbox is wet cardboard and should be considered advisory only.
    
    **Edit:** was this a read-only compromise, or could the attacker have added a credential slurper to workspace makefiles?
    
    I want a _lot_ more detail about what actually happened. Like, if the "legacy system" was a proxy for 3rd party providers, and the things exposed were what went through that proxy, the blast radius is constrained.
- **u/avinthakur080** (↑4, 2026-10-17 16:21): And details on who were affected or how this worked ?
    
    I use opencode but only as a client and not their service. If I got breached, I wouldn't even receive email.
  - **u/popiazaza** (↑4, 2026-10-17 17:30): Should be anyone who use OpenCode Console: [https://opencode.ai/v2/docs/console/](https://opencode.ai/v2/docs/console/)
- **u/DuckDatum** (↑3, 2026-10-17 16:31): May be the wrong approach? Why wouldn’t they invalidate all the keys as a safe measure?
    
    curl -X DELETE \\  
    "[https://api.openai.com/v1/organization/projects/proj\_abc/api\_keys/key\_abc](https://api.openai.com/v1/organization/projects/proj_abc/api_keys/key_abc)" \\  
    \-H "Authorization: Bearer $OPENAI\_ADMIN\_KEY"
    
    [https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api\_keys/methods/delete](https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)
    
    So, this is still an ongoing issue?
  - **u/SuperSlowSubie** (↑3, 2026-10-17 17:45): It's BYOK. Unfortunately up to the user to invalidate them. Apparently they were stored in plain text.
- **u/Mission_Maximum_2329** (↑1, 2026-10-17 16:47): The problem has already reached €200. Google is already investigating it, at least the case I opened. Around 9:00 AM UTC1, Google suspended my project for excessive abuse, and so far the budget notices I've received amount to that sum. Opencode will have to bear the cost of this vulnerability.
- **u/qwertyyyyyyy116** (↑1, 2026-10-17 16:57): woah what?
- **u/ChineseBot-853210** (↑10, 2026-10-17 16:57): Yep. Woke up to a bunch of Anthropic receipts in my inbox. Traced it back to my key I used with OpenCode.
    
    Not sure why they’d be storing the key in plain text. 
    
    Sounds like it’s time to move on from open code.
  - **u/Snoo16812** (↑2, 2026-10-17 17:52): what alternatives would you recommend?
  - **u/TronnaLegacy** (↑1, 2026-10-17 17:55): I've never worked on systems like this before. I'm curious... My first thought is it's necessary for them to. Because they'd need to make the API requests to the provider. Is that not true?
    - **u/MinRaws** (↑1, 2026-10-17 18:25): Yeah they have to store your keys as it is this is why companies instead prefer oauth authentication
    - **u/Interesting_Bet8848** (↑1, 2026-10-17 18:27): can encrypt with your password and other secret details, then decrypt at runtime
    - **u/pas-un-robot** (↑1, 2026-10-17 18:33): Kind of. You're right that ultimately the server that makes the requests to providers needs to have the plaintext API key in memory at some point to authenticate.
        
        Best practice would still be to store it encrypted. The server that makes requests would decrypt API keys only as needed, getting the encryption key from a key management service.
        
        It's more secure that way, cause if an attacker only manages to get a DB dump, they don't have plaintext API keys. They need to hack at least 2 things - the DB and the KMS, or a server with the encryption keys in memory.
        
        We don't know whether OpenCode stores API keys in plaintext, or they store them encrypted and their encryption keys also got compromised.
        
        For greater security you could also have it so that you need a client secret to decrypt the API keys, but that puts more limitations on the system - the API key can only be used when a client is actively logged in.
- **u/jerieljan** (↑1, 2026-10-17 17:01): I can confirm: I got a GCP project suspension 8 hours ago and thought it was a Google fuckup but I saw Opencode's email later noting that one of the Gemini/Vertex API keys I had added was affected.
    
    It's the only public-facing thing besides AI Studio I've used on that project, so highly likely that it was definitely compromised.
- **u/HighwayNo8744** (↑2, 2026-10-17 17:02): no way i'm ever giving these fumblers my credit card for payment. it's the main reason for me to be wary of all of these AI providers.
  - **u/Capable-Guide98** (↑2, 2026-10-17 18:19): You don't really give them credit cards. If I recall they use stripe or some other payment provider. They never see your details they use tokens to charge your cards. But I agree f them and don't give them money. I am canceling my sub too. But your credit card number is probably safe.
- **u/RandiyOrtonu** (↑1, 2026-10-17 17:11): but now i cant even access my old keys 😭 ? why 😭 😭 ?
- **u/Miserable_Sky_4424** (↑3, 2026-10-17 17:12): Shit, I couldn't even login now.
  - **u/Lost-Estate3401** (↑1, 2026-10-17 17:47): Yep they have seemingly disabled login
  - **u/Pedrito_Basket** (↑1, 2026-10-17 18:28): Try without vpn
- **u/lvvy** (↑9, 2026-10-17 17:20): Where the f... are keys stored that are affected?
  - **u/LordChungusAmongus** (↑2, 2026-10-17 17:59): Web UI from what we know. Your local keys are safe but if you set up any key regs such as for Zen outside providers, etc then your keys have been leaked.
- **u/jjjjoseignacio** (↑1, 2026-10-17 17:21): no se puede usar opencode esta caido valio versh
- **u/CnRJayhawk** (↑2, 2026-10-17 17:26): Just deleted my account. Not gonna mess with these guys anymore. Let’s hope they actually delete your data
  - **u/Gold_End_7719** (↑1, 2026-10-17 18:08): Same.. Api keys from now only stay local.. Stupid me, for leaving on the site
    - **u/CnRJayhawk** (↑1, 2026-10-17 18:38): It’s alright. You’d expect a company to protect your data. Guess when they were bragging about using ai all day we’d expect a major security breach to happen.
- **u/Lost-Estate3401** (↑2, 2026-10-17 17:42): All keys revoked and I cannot log in to Opencode console to do anything. Thanks a bunch guys.
  - **u/nicl4ssic** (↑2, 2026-10-17 17:59): Same
  - **u/Pedrito_Basket** (↑1, 2026-10-17 18:28): Try without vpn
- **u/zenkov** (↑3, 2026-10-17 17:47): Not surprised. Everything they write is atrocious vibe-coded slop churned out by outdated or free models. It was obvious that sooner or later someone would exploit it. I'm expecting something similar to happen with Nous Portal. Nous are pretty much the same caliber of incompetent vibe-coding hacks.
- **u/ConsciousSpeed3826** (↑1, 2026-10-17 17:48): I have not received this email yet and my accounts seem fine (I ran out of Claude tokens anyway when I switched to Go), I am changing all my keys though, this truly sucks and I'm sorry for everyone that has experienced fraud because of this.
- **u/lsandoval0000** (↑1, 2026-10-17 17:59): I just went to OpenCode console to check and all its fine, my hermes agent living on my vps is alive and working using my opencode subscription, I also went to my pc and all my api keys are working.
    
    Also asked my coworkers and all fine
    
    **EDIT: Ok I saw the post from opencode account, is not all but some**
- **u/Gold_End_7719** (↑1, 2026-10-17 18:06): My claude account got used up.. But just 5 usd.. And google ai project got suspended..so now waiting for response from google
- **u/BubuX** (↑1, 2026-10-17 18:08): So this is why my opencode keys were expired today.
    
    I use pi agent with codex key + open code go key.
    
    I guess my codex key is safe.
    
    These breaches happened before AI and they are being transparent.
    
    So just STFU anyone crying about it.
- **u/Railander** (↑1, 2026-10-17 18:36): wish we had a bit more info on this.
    
    so if i didn't get an e-mail i wasn't affected? what exactly do they mean by "Console"? only API keys saved directly from their website got compromised, rather than keys added from opencode CLI/Desktop? does this affect the Go subscription?
- **u/OkObjective8721** (↑1, 2026-10-17 18:36): If I only use local models am I affected?
- **u/GhettoFob** (↑1, 2026-10-17 18:42): Was planning to sign up for the Go plan but guess not anymore. Is Command Code the best alternative?

---

## PLEASE DAX SPACE BUNNY UNLIMITED FOR A WEEK AGAIN
**u/nuelgoeshard** · 2026-10-17 14:09 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8b6ta/please_dax_space_bunny_unlimited_for_a_week_again/)

[removed]

---

## Images with opencode
**u/BoatZealousideal4521** · 2026-10-17 13:10 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x89w4x/images_with_opencode/)

Hey Guys,

Has anyone generated images using opencode?

I am working on a project where image generation is needed. 

Has anyone  done it? I know that ican try to do it but would surely like to know if anyone has already done it and what model you have used to do this to save some hit and trial phase.

Thanks in advance.

---

## Muse Spark 1.3 is gone, what's the best free model to use now?
**u/fleursd_orangers** · 2026-10-17 12:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x895ip/muse_spark_13_is_gone_whats_the_best_free_model/)

Since Muse Spark 1.3 is gone, I'm wondering what free model to use now. What models are you currently using, and which ones would you recommend?

Thanks!

**Comentarios:**

- **u/mozkohor** (↑4, 2026-10-17 12:36): glm 5.3 flash or deepseek 4.1
  - **u/No-Snow5789** (↑1, 2026-10-17 12:42): Do you know if the DS4.1 on Opencode is the new 1017 one?
    - **u/Strict-Prune-879** (↑2, 2026-10-17 13:06): non pas du tout
    - **u/Purple-Insane** (↑1, 2026-10-17 17:18): Its not, you can check their x account for live updates, it should be here by tomorrow.
  - **u/Ashamed_Drag8791** (↑3, 2026-10-17 12:42): 200k context is just garbage.
    - **u/Paul_Eau** (↑2, 2026-10-17 13:12): 200k isn’t garbage for code: it’s \~15-20k lines, enough for most tasks, and agentic workflows (grep/LSP, on-demand reads, subagents) handle big repos fine. Bigger windows also degrade in accuracy and cost more per request. I think that 1M does help for cross-cutting refactors.
      - **u/Ashamed_Drag8791** (↑1, 2026-10-17 13:27): u/Chupa-Skrull u/Paul_Eau ok, for my cases at least, context make up to 100 - 150k, i can only ask for 2 - 3 prompt then auto compact
        - **u/Chupa-Skrull** (↑0, 2026-10-17 14:00): Is that truly necessary for your tasks? You can't isolate necessary, minimum context only? That sounds quite burdensome
      - **u/ArC3488** (↑0, 2026-10-17 14:19): I literally am having the problem of opencode compacting due to the 200k crappy context limit. Its ass, not getting any work done like this
    - **u/Chupa-Skrull** (↑3, 2026-10-17 13:19): Where did this nonsense come from? I see it everywhere now.
        
        It's perfectly fine for tons of work, especially if you decompose and delegate specific tasks to subagents
      - **u/reybrujo** (↑0, 2026-10-17 13:27): Mostly from vibecoders too lazy to specify context. You can also setup engram and/or codegraph to minimize the amount of grepping needed.
      - **u/ArC3488** (↑1, 2026-10-17 14:22): Yea buddy, how do you do that with big code files? 
          
          Actually, i just asked DS4,1 to fix an unrelated problem with mcps and it keeps compacting. Must be fun
        - **u/Chupa-Skrull** (↑1, 2026-10-17 15:01): I don't generate code files so big that they burst context, for the most part, "buddy," but when strictly necessary I pony up for a model with a bigger limit lmao.
            
            Your file sizes are likely unnecessary
    - **u/qnphard** (↑2, 2026-10-17 13:51): Not if you give the proper instructions and use them as subagents
    - **u/HyperWinX** (↑2, 2026-10-17 16:44): Unlock 1M context and use it, i ran it in sessions with ~700K ctx
    - **u/i_liketowin** (↑1, 2026-10-17 17:30): glm 5.3 flash has 1M context
      - **u/Ashamed_Drag8791** (↑1, 2026-10-17 18:16): free version only 200K
    - **u/ThatOneCheatOP** (↑1, 2026-10-17 18:23): Dude the DeepSeek flash can go up to 1m and I have tried it and it worked someone posted on how to get it it works i have personally tried it
  - **u/fleursd_orangers** (↑1, 2026-10-17 14:44): thanks
- **u/dbojan76** (↑2, 2026-10-17 12:49): cline supports muse spark 1.3 contributor free
  - **u/DEAD1nsane** (↑1, 2026-10-17 13:41): they aint trying to switch TUI lol
- **u/Ambitious_Ad_6123** (↑1, 2026-10-17 13:08): Deepseek o glm pero ten en cuenta que estan limitados a 200k de contexto, aún así son buenos...solo que para tareas grandes pierden
- **u/ballsdeepbigtummy** (↑1, 2026-10-17 13:34): well hoping meta drop 1.4 contri . cant get enough of free to be honest. and i hate myself i have wasted so many days not utilsing it enough.
    
    i hope space bunny stays just one more week i think its alreayd way too much overdue but i love that model as well
  - **u/fleursd_orangers** (↑1, 2026-10-17 15:29): i'll try space bunny
- **u/ericson_246** (↑2, 2026-10-17 14:46): No es lo mismo pero yo uso Space Bunny, que también tiene 1M de contexto y no va mal
  - **u/fleursd_orangers** (↑1, 2026-10-17 15:18): thanks !
  - **u/devanpy** (↑1, 2026-10-17 15:53): also using space bunny, its very nice and fast
- **u/eMPeBe_YTB** (↑2, 2026-10-17 18:03): Beam free. 1M tokens. kinda the same with muse spark 1.3 Free

---

## How should I approach a project with OpenCode if I want to build an API along with its frontend?
**u/Abumashar** · 2026-10-17 12:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x88xnr/how_should_i_approach_a_project_with_opencode_if/)

Should I use two separate projects and ask the AI to write documentation on how to use the API so the other AI understands how to make the requests? Or is that overcomplicating things, and are there more straightforward approaches?

Thanks for the help! I'm just getting started with AI coding.

**Comentarios:**

- **u/evanvelzen** (↑1, 2026-10-17 12:49): I would personally find some way to define the API objects that can shared between the frontend in the backend. This way the compiler(s) or language servers help verify the correctness.
    
    If you do the frontend and backend in the same language that is easy. For example TypeScript or Kotlin.
    
    If the frontent and backend are in different languages you can use something that compiles the types to both languages. Like Connect RPC or OpenAPI / JSON Schema.
    
    I would not split the tasks between frontend and backend, I would let one agent develop both. Unless you want to create a strong architectural barrier.
- **u/ApprehensiveDelay238** (↑1, 2026-10-17 13:31): You can ask this sort of questions your agent too!

---

## Interesting video about current Opencode FREE models
**u/WegoW** · 2026-10-17 12:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x88ll2/interesting_video_about_current_opencode_free/)

Just watched this interesting video: „I Tested 5 LLMs that are FREE in OpenCode”

https://youtu.be/YsSRZvqYdiY

---

## OpenCode, Sort Yourself Out Fix Search function Already!
**u/Yann27** · 2026-10-17 12:00 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x88hs7/opencode_sort_yourself_out_fix_search_function/)

It makes absolutely no sense that the search function is still completely broken.

In the last two days alone, I've had to update the app multiple times, yet search still doesn't work. You can't properly search through older sessions or find conversations you want to return to.

I actually ended up building my own search app for this, and it works great. But that only solves half the problem. I still can't reopen an old session that I suddenly remember and want to continue working on.

Come on, I made a post about this a month ago, and there's still no fix? How is searching and returning to your previous work not a basic feature of the desktop app?

---

## Updated to OpenCode 2 and now Google API doesnt work
**u/azraels_ghost** · 2026-10-17 11:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x888iv/updated_to_opencode_2_and_now_google_api_doesnt/)

Hi folks, was using the previous OpenCode for the last 6months or so without issue. I have an opencode.json file with the entry for my Gemini API key. I installed the latest version and now I just get  
  
API key not valid. Please pass a valid API key.

I have confirmed that the api key is correct.

I also saw in the docs that there's an auth.json file, so I've updated that but I have the same issue. I'm not sure where to go from here, if anyone has ideas would be appreciated.  
  
thx

**Comentarios:**

- **u/DEAD1nsane** (↑1, 2026-10-17 13:44): have you done in your terminal
    
    ```
    opencode auth login 
    ```
    select Google
    paste API
- **u/azraels_ghost** (↑1, 2026-10-17 15:27): I managed to get the APIs back up and working but omg everything is soooo slow now.

---

## Muse Spark 1.3 or DeepSeek V4.1 Flash?
**u/Killeramn-26** · 2026-10-17 11:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8841r/muse_spark_13_or_deepseek_v41_flash/)

What's your favorite and why?

**Comentarios:**

- **u/Temporary_Guard_7329** (↑1, 2026-10-17 11:43): Muse Spark 1.3 Contributer is good for me.
  - **u/Capital-Guitar-6741** (↑1, 2026-10-17 12:13): still work on opencode with you ?
- **u/migsperez** (↑1, 2026-10-17 11:44): If both are at full price choose Deepseek 4.1
    
    If comparing Muse 1.3 Contributor Vs Deepseek 4.1 prices.  Use Muse. 
    
    There's not much difference between the two, they are similar level of capability.
- **u/Academic-Sentence-34** (↑3, 2026-10-17 11:48): I’m waiting to try the new DeepSeek model that was released just a couple of hours ago. The outcome will depend on its performance.
- **u/Super_Garden_9091** (↑1, 2026-10-17 11:48): muse spark 1.3, way better. deepseek and glm and all other chinese models just go nuclear and benchmax, while the reasoning stays unstable. randomly generating garbled chinese, looping "Wait, actually"
    
    hope they add muse back.
    
    https://reddit.com/link/phady3j/video/dz601ggom0wh1/player
- **u/Early_Aardvark_4026** (↑4, 2026-10-17 12:06): Muse Spark 1.3 has become my main workhorse recently instead of Deepseek. The reason is Muse Spark is faster. I use GPT Sol to make plan and detail enough. Then I need fast and low reasoning model to implement.
  - **u/for4f** (↑1, 2026-10-17 12:31): same setup here lol. claude plans, deepseek executes. spark 1.3 is fast, i'll give it that, but for opencode implementation the new flash 1017 closed the gap a lot. terminal-bench 42 vs 31 on the last version and it feels way quicker in the loop. at same api price i'd still take deepseek for the bulk work
- **u/One_5549** (↑2, 2026-10-17 12:07): Muse got ALOT of shit in the beginning, the problem is that people thought it was shit because it was not really good at explaining things. However it was always an excellent coder/tool caller. But 1.3 is now quite good at writing (i.e explaining).
- **u/Main-Jeweler7003** (↑1, 2026-10-17 12:19): DeepSeek [https://api-docs.deepseek.com/news/news261017/](https://api-docs.deepseek.com/news/news261017/)
- **u/ChuperroTrier** (↑0, 2026-10-17 12:26): Since Muse got taken down I was afraid I lost the best option to dev my projects. I started using DeepSeek flash and it's surprisingly better in some aspects. And it has OCR wich is making a great replacement. Not sure if I'll go back to Muse when it's back online.
  - **u/DEAD1nsane** (↑0, 2026-10-17 13:42): I miss muse, but deepseeks responses are WAY heavy and annoying
    - **u/ChuperroTrier** (↑2, 2026-10-17 15:20): Yeah it's kinda intense, but I like how academic they are. I actually learn with his comments on all the steps it takes 😀

---

## Is Glm 5.3 Free Deepseek???
**u/Yann27** · 2026-10-17 11:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x87ie5/is_glm_53_free_deepseek/)

It acts like deepseek... are they tricking us?   
The output is not like i'm used to for Glm5.3 Flash on all different providers i get the same type of output and on opencode not... 

  
What's going on?

Any1 else noticing this?

---

## Do you use free models for serious things like coding, building software or games?
**u/cometrider2670** · 2026-10-17 10:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x877tg/do_you_use_free_models_for_serious_things_like/)

[removed]

---

## deepseek v4.1 flash free
**u/Zealousideal-Sun4565** · 2026-10-17 10:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8735g/deepseek_v41_flash_free/)

Does anyone recognize it? it doesn't you show us how it  coding and hiding by using base64 encoding

**Comentarios:**

- **u/Yann27** (↑1, 2026-10-17 11:05): I noticed something else post above...
- **u/Standard_Ear_84** (↑1, 2026-10-17 11:33): It's absolutely retarded. The paid version worked well but this free model just keeps chasing it's tail.

---

## Someone used my OpenAI key, that is saved in opencode account.
**u/alexcoool** · 2026-10-17 10:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x8734p/someone_used_my_openai_key_that_is_saved_in/)

My OpenAI API key that was saved inside openai account for OpenAI provider was used today. Around $150 were spent on Astra. I searched my mac - the key is not stored on it. It is in my opencode account only.

How is that possible?

**Comentarios:**

- **u/Rough-Ad9850** (↑5, 2026-10-17 11:19): Did you vibe an app or website?
    It could be in the html or Javascript
- **u/Time-Toe-1276** (↑2, 2026-10-17 11:24): Fellas, this is yet another victim of:
    
      
    API\_KEY = "" #put your OpenAI API key here.
- **u/Dangerous_Leave_4413** (↑2, 2026-10-17 14:12): Welp, we just got an email saying there is a key leak from OpenCode.
    ```
    Hi,
    
    We identified unauthorized access to a legacy system that we were in the process of decommissioning. Third party provider keys (eg OpenAI, Anthropic) saved in your workspace may have been exposed.
    
    Please revoke and replace those keys through the relevant provider’s dashboard, update any applications using them, and review recent usage for unexpected activity.
    
    We’re sorry this happened and will follow up with any updates.
    ```
- **u/Euphoric_North_745** (↑1, 2026-10-17 18:23): The IP addresses of the people who used the keys should be easily locate by the providers, in a normal world they just call the police and stuff should be automated

---

## I built a tool that turns plain English into Regex using OpenCode + GLM
**u/stackattackpro** · 2026-10-17 10:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x870k4/i_built_a_tool_that_turns_plain_english_into/)

Regex has always been one of those things where I spend 20 minutes writing something and another 30 trying to understand what I wrote lol.

So I decided to build **Regex For Humans**, using **OpenCode + the latest GLM model**.

The idea is pretty simple. Instead of writing this:

`/^#[0-9A-Fa-f]{6}$/u`

You write:

    start
    "#"
    6 hex digits
    end

And it generates the actual regex.

But things got a bit out of hand, and now it can also:

* Convert existing regex back into readable rules
* Visualize complex regex with interactive diagrams
* Explain what each part does
* Handle captures, groups, lookarounds, Unicode, etc.
* Export regex to 9 programming languages
* Test patterns directly in the browser
* Detect potential regex performance risks

The interesting part is that **there's no AI involved when using the tool**. It's a deterministic compiler, not an LLM wrapper.

I used OpenCode + GLM for development, and it was pretty interesting seeing how far I could push an open-source coding agent on something involving parsing, ASTs, and compiler logic.

It's still a work in progress, but already usable.

**GitHub:** [https://github.com/OthmaneBlial/Regex-For-Humans](https://github.com/OthmaneBlial/Regex-For-Humans)

**Live playground:** [https://othmaneblial.github.io/Regex-For-Humans/](https://othmaneblial.github.io/Regex-For-Humans/)

Would love to hear what you think, especially if you work with regex regularly. What features would actually make this useful for you?

---

## Anyone tried using Claude Pro + OpenCode Go together for $30/month?
**u/annasfbi** · 2026-10-17 10:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x86qqe/anyone_tried_using_claude_pro_opencode_go/)

The idea is to let Claude plan everything, approve the plan once, then have DeepSeek handle implementation, tests, and fixes, with Claude reviewing the final changes.

Has anyone actually tried this? What’s the best way to wire the two together?

**Comentarios:**

- **u/Fresh_Sock8660** (↑5, 2026-10-17 10:35): Yep that's my current setup. Just ask opus to setup opencode as an agent, no need for extra tooling.
  - **u/nickchomey** (↑2, 2026-10-17 10:43): Which harness are you using for this? Claude or opencode?
    - **u/amelech** (↑1, 2026-10-17 10:46): If you use oh my pi you can use one harness with multiple providers
    - **u/Fresh_Sock8660** (↑1, 2026-10-17 10:47): Claude. Then any model within it uses headless opencode as if it were any other tool.
  - **u/annasfbi** (↑1, 2026-10-17 10:45): How long have you been using this? Theoretically, it appears capable of managing heavy workloads while maintaining good code quality, without hitting limit often.
    - **u/Fresh_Sock8660** (↑1, 2026-10-17 10:49): About a week. Previously I used them a lot but separately. Got fed up of that and started doing this. ds4.1f is great but opus5.5 is the QoL I need in my life.
  - **u/billionarguments** (↑1, 2026-10-17 14:44): I don't get it. Do you you opencode as harness for Claude via a Pro sub?
- **u/Strict-Prune-879** (↑1, 2026-10-17 10:52): oui moi et j'ai fais l'inverse car opus 5.5 en orchestrateur fais pas mal d'erreur et maintenant deepseek v4.1 flash est orchestrateur et opus 5.5 ou sonnet 5.5 sous agent ca marche mieux
  - **u/annasfbi** (↑1, 2026-10-17 10:55): Doesn't this decrease workload capacity, given that you frequently reach the limit on Claude Pro?

---

## A Model Orchestra in opencode with Claude Code — Free Planner, Opus Coder
**u/ercanatay** · 2026-10-17 10:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x86pj1/a_model_orchestra_in_opencode_with_claude_code/)

---

## A Model Orchestra in opencode with Claude Code
**u/ercanatay** · 2026-10-17 10:13 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x86o5j/a_model_orchestra_in_opencode_with_claude_code/)

---

## What happened to my OpenCode?😭😭😭
**u/insanazor822** · 2026-10-17 10:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x86kyr/what_happened_to_my_opencode/)

Please Help

---

## Did DeepSeek V4.1 Flash Free get updated?
**u/Valuable-Mirror-448** · 2026-10-17 10:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x86k1i/did_deepseek_v41_flash_free_get_updated/)

Did DeepSeek V4.1 Flash Free get updated on opencode to the 1017 version or not?

**Comentarios:**

- **u/AdFun4897** (↑1, 2026-10-17 13:59): Not yet. Its going to take a while for opencode to update

---

## "muse spark can do that task with in 1m context and not compact a single time!!! " - (space bunny, big pickle, nemotron, mimo, long dog): -" we are sorry sir! we are not muse spark 1.3".. Rip a free legend
**u/Zealousideal-Sun4565** · 2026-10-17 09:45 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x867ck/muse_spark_can_do_that_task_with_in_1m_context/)

---

## Seriously. what the hell. . this is the 4th time it happens
**u/Infinite_Professor79** · 2026-10-17 09:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x85rh7/seriously_what_the_hell_this_is_the_4th_time_it/)

https://i.redd.it/qzp4a3jdvzvh1.png

these latest free stealth models are weird. when i ask them for a test task for coding , they dont think and use the edit tool or anything. they instantly go "Let me write the file" on first thought. then tell the user "im done" and produce something unusable, completely broken. has anyone also faced this?

**Comentarios:**

- **u/migsperez** (↑1, 2026-10-17 11:58): You should probably benchmark models you've never used before in a container/sandbox. Then decide if you want to use it.

---

## 🔥 DeepSeek V4.1 Flash-1017 is on Hugging Face (see benchmarks inside)
**u/afanasenka** · 2026-10-17 08:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x84usg/deepseek_v41_flash1017_is_on_hugging_face_see/)

[https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

**Comentarios:**

- **u/Effective_Western_59** (↑5, 2026-10-17 08:21): Now waiting for artificial analysis to see token count on tasks
  - **u/look** (↑1, 2026-10-17 10:11): It might be able to take back the lead from Opus 5.5 in most verbose…
- **u/No_Daikon3851** (↑4, 2026-10-17 08:31): Wow
    
    waht a day to be alive
  - **u/annoyedsharpness** (↑2, 2026-10-17 12:26): hello fellow scholar
    - **u/Puzzleheaded-Toe551** (↑2, 2026-10-17 12:38): Hi. Do I know you?
      - **u/quadiuss** (↑2, 2026-10-17 14:16): This is two minute papers
- **u/seeKAYx** (↑18, 2026-10-17 08:45): I really want to like 4.1 but it hallucinates so much .. thats why I prefer 5.3-Flash.
  - **u/WArslett** (↑4, 2026-10-17 09:08): Which provider are you using? I had great success with it on opencode go. Then when they released the weights we started using it at work the next day and got terrible results. Lots of hallucinating, speaking Chinese, looping endlessly etc. So we wrote it off but a couple weeks ago I went back to it and now the performance is great. My theory is that when the weights were first released, only a small number of providers were offering it and they couldn’t cope with the demand so they nerfed the models. Now it’s calmed down they can serve it without degrading the quality. Most of my sessions are landing on Together, ParaSail and BaseTen. DeepInfra gave us a lot of problems
    - **u/seeKAYx** (↑4, 2026-10-17 09:21): native mxfp4 from deepseek api. so it's not a inference problem. it's the model itself. they really have to fix that for the pro release. GLM 5.3 Flash is much better in terms of accuracy.
      - **u/Nexter92** (↑4, 2026-10-17 09:34): This won't be fix i think, it's just a new RL version, we need to wait V5 for a new architecture i think
      - **u/ggPeti** (↑1, 2026-10-17 11:46): Very different experience here. I've tried GLM 5.3 Flash after seeing positive opinions on it, but it just strays from the task and has no attention to detail. DS Flash is just leagues better in my workflow. It just remembers everything and takes instructions very precisely.
  - **u/Intelligent_Ant_608** (↑3, 2026-10-17 10:05): Are you using it on max? On medium and high i get far less hellucinations, but yes seems it has some attention and instruction following issues, it forgets long orders after a while and looses the details(without compaction ofcourse)
- **u/literally_niko** (↑4, 2026-10-17 08:48): Is this the free model that we got?
  - **u/Professional_Price89** (↑5, 2026-10-17 08:53): No you get a quantized 4.1 flash
    - **u/emavgl** (↑2, 2026-10-17 09:13): Is quantized also on the Go subscription? How do I know if it quantized or not?
      - **u/Professional_Price89** (↑0, 2026-10-17 09:14): You know when the token/s is lower than 200.
      - **u/CaffeinatedTech** (↑2, 2026-10-17 10:33): There's no way to know, they don't advertise it.  Shittier responses is the only real way of knowing you are on a quantised model, but its pretty close normally.  Many providers just run the full FP8, the same as the DeepSeek API.  Speed has nothing to do with it.  It should technically be faster to run a more quantised model, but we don't know what they run them on, or their workload.
    - **u/DevelopmentAgile6600** (↑1, 2026-10-17 12:54): Whos lying you our them?  
          
        [https://x.com/NFT\_Chen/status/2110711219502100545](https://x.com/NFT_Chen/status/2110711219502100545)   
        [https://x.com/xiax0603/status/2110720769240207504](https://x.com/xiax0603/status/2110720769240207504)
- **u/aliencreature12** (↑3, 2026-10-17 09:29): when to opencode go????? this is why im here
  - **u/Apart_Paramedic_7767** (↑-2, 2026-10-17 12:32): it’ll take forever as usual, with radio silence from the open code team about its existence. You get what you pay for I guess
    - **u/aliencreature12** (↑1, 2026-10-17 14:35): every other shitty plan sellers already announced  their upgrade already
      - **u/Apart_Paramedic_7767** (↑1, 2026-10-17 15:03): like who?
- **u/Warm-Agent-811** (↑2, 2026-10-17 10:10): I only use flash version but ... where the pro version is ?? hahaha
  - **u/Chance-Shake543** (↑7, 2026-10-17 12:29): let whale cook
  - **u/AdFun4897** (↑1, 2026-10-17 13:56): Is dont know I…
  - **u/Midwain** (↑1, 2026-10-17 15:38): For internal use
- **u/jarvis123451254** (↑7, 2026-10-17 11:00): can't they just name it v4.2?
  - **u/Chance-Shake543** (↑6, 2026-10-17 12:28): Its v4.1 with proper post-train
    - **u/StuckFu** (↑1, 2026-10-17 15:08): which normally would result in a new sub-name like 4.2 or 4.1.1
      - **u/arielif1** (↑2, 2026-10-17 15:48): not for deepseek lol, v3.1 added hybrid reasoning, 3.2 added DSA sparse attention, 4 added the insane (and ultimately failed) CSA+HCA stack and entirely different base models, 4.1 changed base model and added YOCO style disaggregated arch
          they only change number when the model's inherent arch changes, weights only means incremental release
  - **u/DomusCircumspectis** (↑-2, 2026-10-17 14:34): for real, I ain't re-running [my benchmarks](https://bench.killswitch-lang.org) unless they give it a new version
  - **u/Stock-Self-4028** (↑2, 2026-10-17 15:12): Because it's the same architecture.
      
      DeepSeek increases the version number only once architecture is different and v4.1 1017 is just a new weights drop.
- **u/ejafirza** (↑3, 2026-10-17 11:42): What are these naming man
  - **u/Present_Carpenter912** (↑3, 2026-10-17 12:42): 17th of October checkpoint therefore 1017
  - **u/korino11** (↑1, 2026-10-17 17:09): Eat more iodium, maybe it will help to you..
- **u/actuallynotaredditor** (↑1, 2026-10-17 11:49): I have been using 4.1 Flash and i have not seen it hallucinate. I have already built an app with lots of features and the chat limit was finished so I downloaded the whole chat with a plugin and started a new chat and it is still working without any hallucinations. I am amazed.

---

## Million-dollar problem in its own way.
**u/Jazzlike-Form9669** · 2026-10-17 08:17 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x84ukw/milliondollar_problem_in_its_own_way/)

---

## THEY ADDED GLM-5.3-FLASH
**u/nottlluucas** · 2026-10-17 08:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x84m5k/they_added_glm53flash/)

**Comentarios:**

- **u/No_Daikon3851** (↑4, 2026-10-17 08:12): old news. please check sub before posting
  - **u/nottlluucas** (↑1, 2026-10-17 08:40): it now old? i meant is now free
    - **u/Puzzleheaded-Toe551** (↑1, 2026-10-17 09:03): It has been free for 1 day now
- **u/lamardoss** (↑1, 2026-10-17 08:12): yep
- **u/Numerous-Assist1932** (↑1, 2026-10-17 10:15): Then what are the reasons to subscribe to the plan?
- **u/yogafirepromax** (↑1, 2026-10-17 13:10): WHEEEEEERE HAVE YOU BEEN

---

## why it so slow now, just say hi to agent and it took almost 2-4 minutes to respond??? what happens
**u/Zealousideal-Sun4565** · 2026-10-17 07:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x84ffw/why_it_so_slow_now_just_say_hi_to_agent_and_it/)

&#x200B;

**Comentarios:**

- **u/OrganicInformation15** (↑2, 2026-10-17 08:06): More information required to diagnose your problem,
    which model are you using? how hard you set the reasoning to? It takes time to show up the "Thinking" text or the text shows up very fast just that it'll think a bit longer?
- **u/itsner0o** (↑1, 2026-10-17 08:12): Me too started happening last night with deepseek max

---

## DeepSeek V4.1 Flash 1017 is silently rolling out? 😲
**u/afanasenka** · 2026-10-17 07:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x83wt3/deepseek_v41_flash_1017_is_silently_rolling_out/)

...

**Comentarios:**

- **u/Rndomduee** (↑6, 2026-10-17 07:28): They just updated the collection for deepseek V4 on huggingface so i think it will be out soon
- **u/AdFun4897** (↑10, 2026-10-17 07:34): Lets gooo. It will finally reach a 40 point score on the AA index
- **u/DrBearJ3w** (↑3, 2026-10-17 08:04): What about pro?!
  - **u/Last-Ad-8470** (↑2, 2026-10-17 09:52): Im starting to believe this is another google situation where they can make pro good enough to last longer than 1 release
  - **u/C0MPLX88** (↑1, 2026-10-17 12:31): the 4.1 flash was just an optimisation to make it compute faster and use less memory. either they tried it with pro and there was performance degradation or they are working on a new architecture.
      
      hopefully they are final putting all the model architecture research papers they made the last months into use
- **u/migsperez** (↑3, 2026-10-17 11:33): It's released in Huggingface
- **u/NoBlame4You** (↑1, 2026-10-17 11:53): Dude what is this naming scheme.. shouldnt they just use 4 4.1 4.2.. i do understand -preview as suffix tho
  - **u/Mountain-Business-92** (↑1, 2026-10-17 17:55): Im pretty sure it's because it's not a new arch, just a small update so they use the 1017 as the date. 17th of the 10th, you know? don't quote me on this though.
    - **u/NoBlame4You** (↑1, 2026-10-17 18:11): Ye i know.. i just wish they used _._ with the second being smaller updates, they dont need to redo everything for a second tier lvlup.. actually id be fine with _._._ too compared to this date, ga/non-ga mess

---

## Error: OpenCode's free tier can only be used from within OpenCode. Download it at https://opencode.ai and keep building.
**u/Interesting-Movie452** · 2026-10-17 07:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x83oid/error_opencodes_free_tier_can_only_be_used_from/)

I am getting this error even tho i am in opencode, when i Switch model Same error

**Comentarios:**

- **u/zenkov** (↑-6, 2026-10-17 07:15): I'm really annoyed by how aggressively OpenCode pushes its own agent harness, to the point where it starts to feel suspicious and makes me lose any desire to use it at all. Yes, Google does the same thing, but at least Google develops its own models.
  - **u/Pink_Oak** (↑9, 2026-10-17 07:36): Are you stupid?
      
      It's their free tier.
      
      You do realise that with a paid plan you can use their subs in any harness you want, or even call api directly with api key?
      
      Google, Claude, Codex does not even give you api key.
      
        
      I swear some people just stop using brain
    - **u/zenkov** (↑2, 2026-10-17 08:59): How does that contradict the claim that they're aggressively pushing their own agent harness, to the point where even their own harness glitches because of their restrictions? Try reading with your eyes instead of your ass next time.
      - **u/Pink_Oak** (↑-1, 2026-10-17 09:10):  aggressively pushing their own agent harness,
          
          How so?  
          Its only in free tier.
          
          In paid they dont.
          
          LLM infrence cost money. they are leting you use in free tier in ther eown harness.
        - **u/trollhunterh3r3** (↑-2, 2026-10-17 09:16): Ah the best argument "whataboutism", are you stupid?
          - **u/maqifrnswa** (↑1, 2026-10-17 13:57): That's not whataboutism. They are questioning the premise.
              
              I think about it in an opposite way. They are actually pushing their zen and go plans. They don't make money off of the harness. They are trying to get you comfortable with their ecosystem (API and harness) so you subscribe. They are forcing you to use their harness so they can manage the free zen usage and prevent users exploiting it.
      - **u/NMiguelCosta-PT** (↑1, 2026-10-17 17:16): So what? You're getting something for free so take it or leave it.
  - **u/NMiguelCosta-PT** (↑1, 2026-10-17 17:17): If you're annoyed then stop using. Nobody forcing to use this product that you're getting for FREE!
- **u/Direct-Ad7836** (↑0, 2026-10-17 07:27): C'mon, guys, it's a FREE TIER! Of course they want you to use it inside their harness only to promote it! It's not a charity after all...
  - **u/Interesting-Movie452** (↑10, 2026-10-17 07:42): but i AM in opencode
    - **u/no-name-here** (↑2, 2026-10-17 08:06): What version?
      - **u/Interesting-Movie452** (↑-2, 2026-10-17 08:45): nvm it works now
        - **u/yogafirepromax** (↑2, 2026-10-17 09:31): how did you solve it? mine still got same error
  - **u/PuzzleheadedSnow7180** (↑1, 2026-10-17 10:15): But isn't it free because they want the data to train the models?
  - **u/Jim-Bob1965** (↑0, 2026-10-17 15:00): Yeah guys. It's free!!!, it's not working. That's the way it is. Just pay for Your 1352's abo in internet, e.g. tv, ppv, game pass,, news,  or whatsoever to make it working. 
      
        
      If they cannot serve a service for free (where they said it's free)  then they shouldn't advertize it for "free".
- **u/hosseinm8** (↑0, 2026-10-17 07:55): Me too problem
- **u/Dapper-Bug-7877** (↑2, 2026-10-17 08:15): I encountered this when I was using it via openchamber
- **u/chiya_coffee** (↑2, 2026-10-17 08:43): same error, i tried uninstalling and reinstalling opencode, still not fixed
- **u/pungat_** (↑1, 2026-10-17 11:37): if you use opencode terminal, check [this](https://reddit.com/r/opencode/comments/1wwekvm/how_to_fix_this_error_please_help_me/).
- **u/Adventurous-Owl-400** (↑1, 2026-10-17 12:03): same for me
- **u/giveen** (↑1, 2026-10-17 12:14): I had to delete opencode, delete all my settings and configs, and then reinstall and then it worked.
- **u/Educational_Star4807** (↑1, 2026-10-17 14:22): Not working in mine, neither in opencode terminal nor in app, it suddenly went down mid session. Tried everything uninstalling-reinstall, reconnecting with opencode console integration, updating to latest version but nothing works. PS:- On my macOS.
- **u/Overpoweredpixel** (↑1, 2026-10-17 16:03): same, happened just now in desktop app
  - **u/spacetimelime** (↑1, 2026-10-17 16:19): and in CLI here
- **u/ClassOk4988** (↑0, 2026-10-17 16:37): Just happend to me been trying to fix it for the last hour nothing seems to work. does anyone have a fix?
  - **u/Mark_A_Prodigy** (↑1, 2026-10-17 18:35): any fix?
- **u/valdermito** (↑1, 2026-10-17 16:52): Estou tendo problema também mesmo depois de atualizar a versão desktop que está utilizando V2

---

## slow awnsers
**u/Unusual-Butterfly-32** · 2026-10-17 06:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x833h3/slow_awnsers/)

why does it take SO long to complete a simple request, or even a greeting. 

anyone have fixes

**Comentarios:**

- **u/ikakindiehoes** (↑1, 2026-10-17 06:41): Check Agents like REA etc they took around 190k only for a simple hey if u have it Active
- **u/AdFun4897** (↑1, 2026-10-17 07:02): Yeah, switch to claude
- **u/Zealousideal-Sun4565** (↑1, 2026-10-17 07:28): me too, i thought i am the only one lol
- **u/Unusual-Butterfly-32** (↑1, 2026-10-17 08:25): 39 minutes for a "hello" [https://imgur.com/a/HHt3vix](https://imgur.com/a/HHt3vix)

---

## MiniMax token usage roll call: What’s your longest OpenCode session?
**u/Professional_Run3390** · 2026-10-17 06:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x82q9s/minimax_token_usage_roll_call_whats_your_longest/)

For folks running M3 in OpenCode, I want to compare real token usage.

No need for billing screenshots. Rough numbers on repo size and session length are helpful, plus whether you keep one long thread or restart, auto-routing vs pinned provider, and whether cache behavior changes the cost much.

I’m curious when a session feels stale and you start over. What’s the biggest M3 session you’ve run that still felt productive?

---

## Brokenseek v4.1 flash
**u/trashcoder999** · 2026-10-17 05:42 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x82atc/brokenseek_v41_flash/)

They turned off image input for Deepseek v4.1 flash, what a fuckk. 

Upstream request failed: \[unsupported\_request\] only text bla bla bla

**Comentarios:**

- **u/trashcoder999** (↑1, 2026-10-17 05:46): Nevermind

---

## what is this
**u/nobehong** · 2026-10-17 05:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x82a43/what_is_this/)

https://i.redd.it/ruxu7oqbtyvh1.png

i been trying to fix this for like some day now and i cant and i am banned or something?

**Comentarios:**

- **u/Motor_Technology5736** (↑1, 2026-10-17 05:49): nah its me too. i just submitted a bug report to github abt it
  - **u/nobehong** (↑1, 2026-10-17 05:52): i don\`t know maybe the servers
- **u/Icy-Examination-9512** (↑1, 2026-10-17 05:51): i have the same issue lol
  - **u/nobehong** (↑1, 2026-10-17 05:52): maybe the servers lol
- **u/TheMythicSorcerer** (↑1, 2026-10-17 05:54): This seems to be a recurring error so far the workaround I've found is create an opencode zen account and use that api key to sign in and it works (still free) but shouldn't be necessary
- **u/Mark_A_Prodigy** (↑1, 2026-10-17 06:00): same issue here
- **u/pungat_** (↑1, 2026-10-17 06:02): if you use opencode terminal, check [this](https://reddit.com/r/opencode/comments/1wwekvm/how_to_fix_this_error_please_help_me/).
- **u/Icy-Examination-9512** (↑1, 2026-10-17 06:05): Heres how to fix this is from the git issue the other guy posted btw, Thanks for the detailed report and for all the troubleshooting you've already done!
    
    This error comes from the Zen gateway, and it has several known causes that have nothing to do with where you run OpenCode. You've already ruled out a missing Console login. Some of the other causes are easy to miss in a config check, so could you share the following?
    
    1. **The full output of** `opencode debug config`, with any API keys or tokens removed. In particular, check whether `read` or `shell`/`bash` is denied anywhere in any form (`"deny"`, `{"*": "deny"}`, an agent-level `permission`, or an old-style `"tools": { "bash": false }`). Also check whether there's a provider entry pointing at `https://opencode.ai/zen/v1`. Each of these is known to cause exactly this error.
    2. **Your plugins:** any `plugin` entries in your global config (`%USERPROFILE%\.config\opencode\opencode.json` / `opencode.jsonc`), and any files in `%USERPROFILE%\.config\opencode\plugin(s)\`. Since you recently uninstalled code-review-graph, please check that nothing from it is left over.
    3. **A log from one failing request:** run `opencode --print-logs --standalone`, send one prompt, and paste the lines around the error, again with any tokens removed.

---

## i found the cheapest model provider on the internet what do u guys think of these prices?
**u/nekohacker591-** · 2026-10-17 05:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x81wfg/i_found_the_cheapest_model_provider_on_the/)

this platform is legit i have tested the models and they are not fake and their reliability and speed is very high as well near upstream

**Comentarios:**

- **u/PROPLAYER3X7** (↑1, 2026-10-17 05:20): Ah provider name ?
  - **u/nekohacker591-** (↑1, 2026-10-17 05:21): kukuai
    - **u/PROPLAYER3X7** (↑1, 2026-10-17 05:23): Can you share the link? 🙏
      - **u/nekohacker591-** (↑1, 2026-10-17 05:24): [https://www.kukuai.fyi/](https://www.kukuai.fyi/)
- **u/AdFun4897** (↑8, 2026-10-17 05:22): Yeah drop the link so we can report your sketchy vibecoded website
  - **u/nekohacker591-** (↑1, 2026-10-17 05:23): [https://www.kukuai.fyi/](https://www.kukuai.fyi/)
- **u/beneficialdiet18** (↑5, 2026-10-17 05:22): If you believe this you are living in cuckoo land
  - **u/nekohacker591-** (↑1, 2026-10-17 05:24): i have tested out the platform thats why im sharing it
- **u/nekohacker591-** (↑1, 2026-10-17 05:28): i searched over 1000 ai websites too find this btw
  - **u/nekohacker591-** (↑1, 2026-10-17 05:38): 
      
      [Least\_Bodybuilder216 ](https://www.reddit.com/user/Least_Bodybuilder216/)
      
      •[1m ago](https://www.reddit.com/r/opencode/comments/1x81wfg/comment/ph93k7m/)
      
      [https://inferhub.dev](https://inferhub.dev) wht bout this
      
      \>>nekohacker591  they dont support card payments only crypto
      
      but your right this provider is cheaper but bad for people like me who dont know how to use crypto currency without kyc
- **u/CaffeinatedTech** (↑1, 2026-10-17 05:31): Is it one of those stolen key routers?
  - **u/nekohacker591-** (↑0, 2026-10-17 05:34): no these are pooled accounts
    - **u/CaffeinatedTech** (↑3, 2026-10-17 05:36): stolen pooled accounts? :)
      - **u/nekohacker591-** (↑1, 2026-10-17 05:43): nope  
          [https://imgur.com/Frwb0YO](https://imgur.com/Frwb0YO)  
          [https://imgur.com/SufyqA9](https://imgur.com/SufyqA9)
          
          this is how it works
- **u/Alexandria_4624** (↑1, 2026-10-17 05:34): Too good to be true.
  - **u/nekohacker591-** (↑1, 2026-10-17 05:45): what i thought at first as well
- **u/Big_Cucumber2787** (↑1, 2026-10-17 05:36): i have a bridge to sell you
  - **u/nekohacker591-** (↑1, 2026-10-17 05:44): and i found that bridge too be a steal
    - **u/Big_Cucumber2787** (↑1, 2026-10-17 06:24): you can serve any model name faking to be another and steal peoples data. i wouldnt use sketchy sites like this if i were you.
- **u/popiazaza** (↑1, 2026-10-17 05:37): If it sounds too good to be true, it probably is. You could vibe code your own website and says it's $0.  
    Here what it may be:
    
    \- route to cheaper model without telling you.
    
    \- abuse multiple accounts with subscription like OpenCode Go and route traffic through it.
    
    \- they could just inject their own response to run any command and hack your computer.
  - **u/nekohacker591-** (↑0, 2026-10-17 05:40): i have tested the models and they are not swapping them out from my experince
- **u/ikakindiehoes** (↑3, 2026-10-17 05:47): 
    
    This website does not have many visitors
    
    
    
    
    
    **IPQS** flagged this website for Phishing
    
    
    
    
    
    **IPQS** has flagged this website as suspicious

---

## JACKPOT - Deekseek v4.1 flash
**u/Cold_Permission_3051** · 2026-10-17 04:58 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x81jet/jackpot_deekseek_v41_flash/)

https://i.redd.it/gr0oqvvqlyvh1.png

**Comentarios:**

- **u/trashcoder999** (↑1, 2026-10-17 05:39): They turned off image input

---

## Huh
**u/MilliusBlack** · 2026-10-17 04:33 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x81465/huh/)

https://i.redd.it/8pmksm87hyvh1.png

**Comentarios:**

- **u/AdFun4897** (↑1, 2026-10-17 04:49): AGI
- **u/GGsayan** (↑1, 2026-10-17 04:53): Lamo
- **u/carlos-algms** (↑1, 2026-10-17 05:03): Q1
- **u/AdSmooth4982** (↑1, 2026-10-17 08:55): my favorite model... am soo disappointed 😞
  - **u/MilliusBlack** (↑1, 2026-10-17 17:39): It's also my favorite, I just started a new session and everything was normal again, just found it funny how creepy it was haha
- **u/ERROR_FOX_PG** (↑1, 2026-10-17 13:31): RUN TOTTI, RUN! 🗣️

---

## Future of OpenCode Go
**u/MorkezZ** · 2026-10-17 04:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x80v2p/future_of_opencode_go/)

Muse Spark 1.3 Contributor just got removed from the Zen Free Tier. Probably a sign that it will get removed from Opencode Go too soon. The question is, what alternatives we have.

Deepseek V4.1 Flash is. Okay. It was good, but after the development the last few weeks it's more like low-mid tier. Same for Mimo V2.6 Flash. Everything else isn't feasible with the 10$ sub, as you will run out of usage.

Our best hopes are for a cheep Deepseek V4.1 Pro model or Muse Spark 1.4 Contributor. But it's still questionable if Meta will release it after Muse Wonder.

What are your thoughts?

**Comentarios:**

- **u/a355231** (↑9, 2026-10-17 04:22): That’s not how that works, it got removed from Free because free models always have a limited agreement. That’s how it always has worked.
- **u/DiscountFit9224** (↑2, 2026-10-17 04:35): The most feasible way to not increase your 10$, is learn how to code, use the so called 'low-mid tier' llm as your assistant for repeated tasks, boiler plates, etc. You do the heavy lifting of wiring the system/architecture execution.
  - **u/scANN-DavidScann** (↑1, 2026-10-17 13:07): Even though I agree, the market definitely has demand.
- **u/Affectionate_Film537** (↑4, 2026-10-17 04:48): It's free because they are collecting data and training.
  - **u/TomHale** (↑1, 2026-10-17 16:23): It's still the best smarts per cost on the paid plans for the same reason. 
      
      But for open source work... Yeehar!
- **u/armanmax11** (↑5, 2026-10-17 04:53): What abour glm 5.3 flash?
  - **u/japherwocky** (↑2, 2026-10-17 04:54): it's been great for me
    - **u/Haunting-Shirt6219** (↑0, 2026-10-17 05:19): Compare with ds41 flash/muse 1.3? Still good?
      - **u/gnaarw** (↑1, 2026-10-17 11:05): I doubt you'd get a good answer on that. Any model is about how you feel about using it. If it does what you want, why switch?! Who has the time to seriously test and benchmark the next new model every week?
      - **u/japherwocky** (↑1, 2026-10-17 15:32): i didn't even try out muse!  too many models, not enough tokens!  I've always found deepseek / GLM to be roughly the same.
- **u/cdurth** (↑3, 2026-10-17 05:15): opencode's behavoir is like a cat playing with a toy. You are honestly wasting your time and money on them. Go direct to the source and quit dealing with opencode's shenanigans.
  - **u/Toad__Sage__** (↑3, 2026-10-17 06:13): What source? The providers? Idtso if anyone provides 6x worth of your dollar (except other aggregators ofc). The company's own subscription tbh might be a lot subsidized but you might not be satisfied with one model always (or maybe it's just my adhd), oc/cc give us freedom to use different ones.
- **u/CaffeinatedTech** (↑1, 2026-10-17 05:29): There's the normal (non-contributor) paid version, or CommandCode still has the contrib version for now.
    
    Give DS-v4.1-flash another go.  You might have caught it on a lazy day, or copped a shitty provider.  Don't use the free version if you have big stuff to do.
- **u/IntelligentBird2211** (↑1, 2026-10-17 05:51): What's Muse wonder?
  - **u/KronenR** (↑1, 2026-10-17 13:50): new meta model
- **u/arnab_best** (↑3, 2026-10-17 05:59): i really hope 1.3 contributor doesnt get removed. its my primary model for pretty much everything. my usage doesnt seem to need more intelligence. i dont like the way glm and deepseek do things + they feel lowkey slow.
  - **u/Schudz** (↑1, 2026-10-17 13:32): do you know that contributor means that they use your data for training, right?
- **u/ByteNomadOne** (↑1, 2026-10-17 06:30): Muse was crap anyways.
    
    With DS 4.1 Flash and GLM 5.3 Flash we now have two of the best models for free.
    
    OpenCode Free Tier is great right now.
  - **u/Mihaylov93** (↑1, 2026-10-17 14:44): I get rate limited with GLM 5.3 while with MiMo somehow I can keep it running forever
    - **u/ByteNomadOne** (↑1, 2026-10-17 18:10): MiMo is not good at all.
        
        But yeah, GLM 5.3 Flash is really slow on OpenCode.  
        It runs all day to complete a small feature.
- **u/alien3d** (↑2, 2026-10-17 06:48): its  rebels . i dont like .  The real good one for me is space bunny free .
- **u/montooshah** (↑0, 2026-10-17 08:54): What about Step5 from stepfun?
- **u/SirDaddyChaotic** (↑1, 2026-10-17 09:58): What about argon that got added to go and is better than muse. Did you miss that?
- **u/Academic-Sentence-34** (↑0, 2026-10-17 10:08): New deepseek flash incoming. I saw it on hugging face and their official website. It’s a recent date with more improvements
- **u/FrankKnt** (↑2, 2026-10-17 17:38): I used Muse Spark 1.3 quite a bit while it was free, and I actually still use it (I didn't even notice they had removed it, Argon mentioned it to me yesterday when I asked him to configure the agents in OMO). However, whenever I read other people's opinions, they were consistently negative, describing it as a mediocre model with weak capabilities, etc.
    
    Now it turns out it was top tier. 😄

---

## Could someone share a Claude invite with me?
**u/MeaningAnnual3542** · 2026-10-17 03:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7zqrh/could_someone_share_a_claude_invite_with_me/)

Hey everyone! Hope you’re all doing well.



I’ve been interested in trying out Claude for some time, and I’ve seen that some people have access to invite links. If anyone has a spare invite, would you mind sending me one via private message? I’d really appreciate it!

**Comentarios:**

- **u/Strict-Prune-879** (↑1, 2026-10-17 04:40): désolé j'en ai pas bonne chance ca ne coute que 20 usd

---

## longcat 2.5 free is way better than Big Pickle.
**u/Robert__Sinclair** · 2026-10-17 02:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7z56q/longcat_25_free_is_way_better_than_big_pickle/)

longcat 2.5 free is way better than Big Pickle..

also: lately big pickle is missing the opening thinking tag so the thinking bleeds all over the place making a mess of the context.

**Comentarios:**

- **u/Big_Cucumber2787** (↑2, 2026-10-17 02:49): big pickle is not one model... one day its claude, another its deepseek, yesterday it was an unreleased microsoft model, etc.
    
    ps: no, i dont base that on its response. i base that on the tooling errors i see constantly while spamming big pickle for most tasks.
  - **u/Robert__Sinclair** (↑1, 2026-10-17 08:15): in the last week big pickle is good and (over)thinks like deepseek, but the opening think tag is missing server side and messes the application.

---

## Whyy?😭
**u/niktik95** · 2026-10-17 02:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7yxf8/whyy/)

**Comentarios:**

- **u/vacterro** (↑8, 2026-10-17 02:36): ARGHH THEY OWE US FREE AAIIII ARGHH
  - **u/TomHale** (↑1, 2026-10-17 15:42): We are the Entitled.
- **u/CapableHat9609** (↑2, 2026-10-17 02:37): DS mogs ZDR DNR
  - **u/Evan_gaming1** (↑1, 2026-10-17 04:18): what is ZDR DNR
    - **u/Trovebloxian** (↑1, 2026-10-17 05:39): Zero data retention and do not resuscitate
- **u/Own_Load_5730** (↑1, 2026-10-17 02:47): Bueno por lo menos tenemos a glm 5.3 flash
- **u/TheMythicSorcerer** (↑4, 2026-10-17 05:31): ran out of compute and didnt want to give us good free model

---

## muse 1.3 gone but 1.2 still there may be not good at 1.3 but still smarter than longcat and nvidia lol :)))
**u/Zealousideal-Sun4565** · 2026-10-17 02:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7yms6/muse_13_gone_but_12_still_there_may_be_not_good/)

**Comentarios:**

- **u/BirthdayTerrible4204** (↑1, 2026-10-17 02:24): Será lembrado eternamente; o modelo Jesus que ajudou os pobre a se manter, dando um pingo de esperança.... Vai deixar saudades.
- **u/lincolnthalles** (↑1, 2026-10-17 02:30): Muse Spark Contributor 1.2 is also gone from the free tier. Your client model list is likely stale. It may work a bit longer, but expect it to start erroring soon.
    
        curl -s https://opencode.ai/zen/v1/models | jq -r '.data | map(.id) | sort[] | select(ascii_downcase|contains("free"))'
    
        beam-free
        deepseek-v4.1-flash-free
        glm-5.3-flash-free
        jev-1.13-free
        longcat-2.5-preview-free
        mimo-v2.6-flash-free
        nemotron-3.5-lightning-free
        nemotron-3.5-super-vl-free
        space-bunny-free

---

## Best Free Alternative to Muse Spark 1.3?
**u/Striking-Mix-1584** · 2026-10-17 02:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ymqb/best_free_alternative_to_muse_spark_13/)

I was using Muse Spark 1.3 for free because of its 1M-token context window. DeepSeek is good, but I run out of context too quickly

What free model would you recommend as a replacement, especially for coding large projects in OpenCode? Ideally, something with a large context window and generous usage limits

**Comentarios:**

- **u/a355231** (↑1, 2026-10-17 02:27): What happened to Muse Spark 1.3?
  - **u/Striking-Mix-1584** (↑2, 2026-10-17 02:29): It was discontinued from OpenCode Free
    - **u/Avizi_** (↑1, 2026-10-17 09:51): HUH WHEN?!
- **u/aarz03** (↑1, 2026-10-17 02:34): space bunny?
- **u/TheMythicSorcerer** (↑1, 2026-10-17 05:17): Space bunny for frontend, DS v4.1 flash / mimo v2.6 flash for backend
- **u/adrnptcl** (↑2, 2026-10-17 06:07): Space Bunny does wonders for me, maybe it just fist my style and my projects better, I dunno, but I find it to be superior to everything else that's free in opencode
- **u/Interesting-Movie452** (↑5, 2026-10-17 06:25):     {
          "providers": {
            "opencode": {
              "models": {
                "deepseek-v4.1-flash-free": {
                  "limit": {
                    "context": 1000000,
                    "output": 384000
                  }
                }
              }
            }
          }
        }{
          "providers": {
            "opencode": {
              "models": {
                "deepseek-v4.1-flash-free": {
                  "limit": {
                    "context": 1000000,
                    "output": 384000
                  }
                }
              }
            }
          }
        }
    
    Deepseek as mentioned in another post [https://www.reddit.com/r/opencode/comments/1x6mezp/psa\_opencodes\_free\_deepseek\_v41\_flash\_appears\_to/](https://www.reddit.com/r/opencode/comments/1x6mezp/psa_opencodes_free_deepseek_v41_flash_appears_to/)   
    You can use this to bypass deepseek to 1m context (on free)
  - **u/aarz03** (↑2, 2026-10-17 09:49): have you tested it on free tier? does the context go above 200k?
    - **u/Interesting-Movie452** (↑1, 2026-10-17 11:40): yeah
  - **u/DEAD1nsane** (↑1, 2026-10-17 13:46): but DeepSeek doesn't explain before coding which is super annoying, and then randomly codes the wrong things
- **u/RE20ne** (↑1, 2026-10-17 09:26): just go to commandcode and keep using spark free
  - **u/ain92ru** (↑1, 2026-10-17 11:50): Mind some details?

---

## Use code WGKUBHBQ
**u/memes4you06** · 2026-10-17 02:00 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ybos/use_code_wgkubhbq/)

---

## 200k context on deepseek free results insane amount of repeated useless token use.
**u/dwerps** · 2026-10-17 01:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7y8bt/200k_context_on_deepseek_free_results_insane/)

Im doing series of bug fixes based on a code review report. Big repo, lots of bugs to fix. And 200k context realistically fits maybe 2 fixes before running out.

leads to situation where i need to start new session every few bugs and agent is doing the same basic recon every single time all over again wasting time and tokens. (doesnt matter much to me, because my time does not cost anything and tokens are free with ds4.1free. But this worthless repeated recon in every session probably not free for opencode).

I think they really should bump this to 1M context to reduce this wasted repeated throwaway work.

**Comentarios:**

- **u/Strict-Prune-879** (↑1, 2026-10-17 05:38): c'est gratuit et opencode fonctionne toujours comme cela regarde mimo v2.5 free et mimo v2.6 free pareil fenetre  200k
  - **u/dwerps** (↑1, 2026-10-17 05:56): > c'est gratuit et opencode fonctionne toujours comme cela regarde mimo v2.5 free et mimo v2.6 free pareil fenetre 200k 
      
      Muse had 1M context, so it was bit different. A lot less shuffling with sessions.
- **u/Fresh_Sock8660** (↑1, 2026-10-17 10:15): Sounds like a process and setup issue. One of my current repos have a couple hundred thousand lines of code (ignoring blanks and comments) across over a 1000 modules, over a thousand markdown docs. Yet I manage just fine with auto compaction set to 150k on ds4.1f.
  - **u/dwerps** (↑1, 2026-10-17 11:35): Well, there definitely are ways around the issue.
      
      I just prompted execution plan document that project manager agent follows and spawns subagents for all the coding related tasks (all of them have fresh context, so 200k becomes non issue). Can get pretty massive jobs done this way without babysitting the agent. 
      
      but with muse's 1M context window, i did not need to jump through these hoops.

---

## Created a 3d f1 game using opencode and deepseek v4.1 in 12 hours
**u/automax** · 2026-10-17 01:19 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7xjqp/created_a_3d_f1_game_using_opencode_and_deepseek/)

[https://auspending.site/car/car3d.html](https://auspending.site/car/car3d.html)

Its quite interesting, some of the circuits are difficult, I couldn't imagine how hard it is to be an f1 driver. Shoutout to my boy Piastri

It was done in 6 hours with deepseek, which is the 3d circuits and gameplay  
Then I ran out of credits and finished off the sound and elevation and scenery with claude.

But for 12 hours I think pretty good effort. 

Let me know what you think?

If you think I have too much spare time on my hands, yes its true, I got nothing to do except for waste time playing around with AI.

**Comentarios:**

- **u/reybrujo** (↑1, 2026-10-17 01:24): If you only press UP and leave it pressed it make some funny things.
  - **u/automax** (↑1, 2026-10-17 01:40): strange works for me, i just took the sound from an f1 car
- **u/mtlcrusher** (↑2, 2026-10-17 01:27): wow
- **u/for4f** (↑1, 2026-10-17 02:22): ok a 3d f1 game in 12 hours is genuinely impressive lol. piastri tax aside, how did deepseek do on the gameplay logic vs the visuals? usually nails the scaffolding on stuff like this and then the physics need hand-holding, was that your experience too
  - **u/automax** (↑1, 2026-10-17 02:38): Yeah did need a bit of tuning with taking off, acceleration
      
      Honestly still needs some more work, so might do it once I get my opencode credits back.
      
      I just built on my last 2d app and used ammo.js and three.min.js which handles most of the work.
      
      After I added the scenery, is when i had to add the geomotry, so that was done by claude and that was a real headache.
      
      I was going back and forth with claude on this before claude built me map comparison that showed   
      the scenery map between the race map.
      
      [https://files.catbox.moe/8jhi7c.png](https://files.catbox.moe/8jhi7c.png)
      
      Then I asked it compare the elevations, once claude could see the differences it was pretty smooth sailing.
    - **u/automax** (↑1, 2026-10-17 02:50): Let me know if you guys want me to make it public, and create a tutorial on it, so you can modify it and make it better.
- **u/Ready-Photograph-773** (↑1, 2026-10-17 04:59): Can't keep it going for some reason. Tried using WASD and also the arrows but the accelerator seems to give out after a bit for some reason. Just stops the car. Thought it was maybe because of turning but it wasn't that. Not sure exactly what it is but being on the accelerator for a while leads to it just stopping. Even a gentle lift and press again wasn't working for me and it would still come to a complete stop... Otherwise dope game. Tried to make a rally cross type thing using Godot (with the help of Mimo V2.6 Flash so you can imagine how that went)
  - **u/automax** (↑1, 2026-10-17 05:20): yeah there is a few bugs, im just waiting for my credits to popback up and I'll try and fix it, as I don't want to use my claude usage
  - **u/automax** (↑1, 2026-10-17 08:01): opencode credits back, fixed the bug
      
      car3d\_physics.js
      
      \- Added wallMaxForce: 3000 (CAR tuning, line 41) and capped the edge spring (lines 268–269): spring = Math.min(over \* wallStiffness, wallMaxForce) so a car that spins nose-in can't be pinned by the barrier.
      
      \- offTrackDrag: 1.6 → 0.6 (line 53).
      
      \- Off-track engine factor 0.35 → 0.85 (line 280).
      
      \- (Earlier) signed damping on the guide-rail: mag = max(0, spring + vn \* wallDamp).
      
      car3d.html
      
      \- Line 853: halfWidth = cl.halfWidth || 8; — uses the real circuit corridor width instead of the hardcoded 8m.
      
      \- Lines 549 & 711: targetLen = 6.0 → 8.0 (player + AI car size).
      
      \- Cache-busters (lines 89–90): tracks3d.js?v=10, car3d\_physics.js?v=10.
      
      tracks3d.js
      
      \- Added resampleValues() helper (line 128).
      
      \- buildCenterlineFromCircuit now resamples corridorLeftMetres/corridorRightMetres, derives a corridor halfWidth, and returns halfWidth, corridorLeft, corridorRight (lines 311–322).
- **u/nuclearnadal65** (↑2, 2026-10-17 06:45): I think the issue right now is collision along the side of the roads. It’s overcorrecting it. But otherwise, nice!
  - **u/automax** (↑1, 2026-10-17 08:01): Thanks for your suggestions, try it now, bugs should be fixed.
    - **u/nuclearnadal65** (↑2, 2026-10-17 08:10): Pretty good now! For a 12 hour project it’s fun for sure.
      - **u/automax** (↑1, 2026-10-17 08:13): Yeah thx, its good to just turn the sound off , listen to some youtube music and race :)

---

## Muse 1.3 contributor It is no longer available for free
**u/Dorima_boy** · 2026-10-17 01:11 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7xdrs/muse_13_contributor_it_is_no_longer_available_for/)

Those were good times :( Let's hope the Wonder Contributor version comes out.

**Comentarios:**

- **u/pikuray** (↑6, 2026-10-17 01:17): They are changing their models more often than i change underwear. Wth
  - **u/Ok_Cloud_9762** (↑7, 2026-10-17 02:02): Damn, u might wanna rethink your habits
  - **u/CYCLONOUS_69** (↑1, 2026-10-17 02:41): Same here, changed the underwear once and they changed their models 3 times in two days...
    - **u/strangedell123** (↑1, 2026-10-17 03:39): Uhhhhh I change daily soooooo
- **u/migsperez** (↑5, 2026-10-17 01:33): Won't be long until the Contributor model is gone from Opencode Go as well.   Muse Wonder is out, they have all the training data they need.
  - **u/aziham** (↑3, 2026-10-17 02:02): This
  - **u/gizeon4** (↑1, 2026-10-17 03:29): all training data they need?  
      as if there will be enough training data...   
      these company is hungry for training data, it will never be enough
    - **u/Dudensen** (↑2, 2026-10-17 06:30): Yup. Not even OpenAI and Anthropic have enough training data.
    - **u/mWo12** (↑1, 2026-10-17 09:49): Yew, but for how long you can keep training new slop on existing slop?
  - **u/Popular-Factor3553** (↑1, 2026-10-17 04:26): It's not even close to enough, not until they beat antrophic over market share even then i doubt they'll stop
- **u/Gengur** (↑3, 2026-10-17 01:54): rip Muse was great, didn't feel as limited as Big Pickle but was just as effective
- **u/Candid-Emphasis7399** (↑2, 2026-10-17 02:15): is there any alternative to spark? that model too good
  - **u/Dorima_boy** (↑3, 2026-10-17 03:10): A free model, apparently DeepSeek, with much less context.
    - **u/No-Selection2972** (↑1, 2026-10-17 10:25): Why not glm flash?
- **u/CheesecakeLivid9791** (↑1, 2026-10-17 04:19): What's the alternative for muse spark, don't want to be hit with a rate limit 😭
  - **u/GGsayan** (↑1, 2026-10-17 04:50): DeepSeek v4.1 flash
    - **u/CheesecakeLivid9791** (↑1, 2026-10-17 04:54): Got rate limit, for using it
      - **u/Vegetable_Bit9820** (↑1, 2026-10-17 06:34): ur problem maybe since i perfectly use them was only 1 problem with muse spark 1.3 before
- **u/TheMythicSorcerer** (↑1, 2026-10-17 05:09): RIP
- **u/Vegetable_Bit9820** (↑1, 2026-10-17 06:31): well no muse spark for free sadly but atleast they added deepseek v4.1 flash:D
  - **u/Vegetable_Bit9820** (↑1, 2026-10-17 06:32): sadly less context but atleast something in return
- **u/breadnone** (↑8, 2026-10-17 06:47): lets just pray 1.4 free incoming
- **u/Desther** (↑1, 2026-10-17 09:12): Which webpage is this?
- **u/dot_mun** (↑1, 2026-10-17 11:30): It was very good, and very less hallucinating in the programming I used to do with security.
- **u/dbojan76** (↑3, 2026-10-17 12:50): cline supports muse spark 1.3 contributor free
  - **u/touhami_dz** (↑1, 2026-10-17 17:03): ty
- **u/ballsdeepbigtummy** (↑1, 2026-10-17 13:28): man i'll miss it, which is the next smartest model after muse spark??
- **u/touhami_dz** (↑3, 2026-10-17 16:29): for me it was the best free model that i tried tbh, the good ones right now are all 200k context window which is horrible at least for me.
  - **u/Dorima_boy** (↑1, 2026-10-17 16:38): He was the best model; he helped me finish my university project. If you want, I can show it to you.
    - **u/touhami_dz** (↑1, 2026-10-17 17:03): sure, also after reading comments here i remembered that cline exists so im using right now

---

## Blender 3D agentic models
**u/Longjumping_Guard726** · 2026-10-17 00:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7wxlt/blender_3d_agentic_models/)

Has anyone tried building Blender 3D agentic models (lowpoly 3D models purely generated from code) with an opencode go/ any low cost subscription?

Im a 3D artist myself and I have a huge library of 10,000+ lowpoly assets library I collected for a few years. I have already extracted geometry and indexed them using Gemini but I want to use them as references and generate codes when I ask for a model. 

For example: if you ask for a low poly house from a model, it will try to put cube over cubes and make it geometrically. But artist-made lowpoly assets have a ‘soul’ where each and every vertex is deliberately placed to get a chunky, blocky silhouette. I could do that with opus 5.5 or Astra 6 but it is very costly. Has anyone tried something like this?

Or any better way to use my library to do this?

**Comentarios:**

- **u/trion129** (↑1, 2026-10-17 08:13): Deepseek is decent for this. You can see [MineBench | Leaderboard](https://minebench.ai/leaderboard) to get an idea on which model is best right now.

---

## Rest in peace Muse Spark 1.3
**u/Brief-Sherbet-6560** · 2026-10-17 00:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7wu00/rest_in_peace_muse_spark_13/)

We've had a good run

**Comentarios:**

- **u/boss-man-007** (↑1, 2026-10-17 01:23): yes indeed ,he was not the best but it was good one
- **u/Emotional-Bag-3754** (↑1, 2026-10-17 01:32): Que venha o Muse Spark 1.5 ou o 1.4
- **u/AnswerAcceptable935** (↑1, 2026-10-17 02:18): NAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
- **u/Little-Breakfast-653** (↑1, 2026-10-17 02:19): Why , is this being removed from opencode go ?
  - **u/dhruvanand93** (↑1, 2026-10-17 03:17): Same question
  - **u/RE20ne** (↑1, 2026-10-17 09:49): muse released open weight Spark so now neoclouds can serve it themselves… and charge you lots.
- **u/Strict-Prune-879** (↑1, 2026-10-17 04:55): opencode a toujours fonctionné comme cela les modèles gratuit tourne, change, rip!
- **u/CYCLONOUS_69** (↑1, 2026-10-17 08:01): Goated model
- **u/clash4cash** (↑1, 2026-10-17 11:50): its super cheap , i have used the 4 euro/month subscription it s insanely cheap for the work it can do

---

## Opencode Session TUI plugin
**u/migsperez** · 2026-10-17 00:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7wt3j/opencode_session_tui_plugin/)

Compiled and added further functionality into the one plugin which I use daily.  Give it a go, I'd be open to suggestions for further development.  It's the sidebar, the bottom tks bar and a session detail page.

---

## Muse Spark 1.3 gone? Can i get it back if i revert to the old version of OpenCode?
**u/FutureLynx_** · 2026-10-17 00:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7wjmg/muse_spark_13_gone_can_i_get_it_back_if_i_revert/)

Was getting an error saying Muse is deprecated. Like that "Muse is deprecated". And me like wtf... Let me update OpenCode, maybe that will do it.

And now Muse is no where to see.

Muse was the best AI i worked with and was helping me a ton in my current project.

Should I go to Big Pickle or DeepSeek 4.1?

Or can i just revert back the update and keep Muse?

**Comentarios:**

- **u/trashcoder999** (↑3, 2026-10-17 00:29): Muse is gone
- **u/trashcoder999** (↑2, 2026-10-17 00:30): Maybe 1.4 will replace it?
  - **u/FutureLynx_** (↑3, 2026-10-17 00:31): lets hope so
  - **u/migsperez** (↑3, 2026-10-17 00:36): Not likely, they have their product now.  I suspected this would happen when I saw the release of their new model.  It won't be until the contributor model disappears on the Opencode Go subscription as well.  I'll be totally disappointed it's my default model.
- **u/reybrujo** (↑5, 2026-10-17 00:33): That's something changed on the server side, you can't just rollback your app lol
  - **u/eastlin7** (↑4, 2026-10-17 07:03): Vibe coders 🤷‍♂️
- **u/Weak_Insurance_9367** (↑3, 2026-10-17 00:37): Yep, gone. Use paid one, or switch to other.
  - **u/Railander** (↑1, 2026-10-17 01:03): contributor one is still very generous, you get tons of usage out of it.
- **u/FireGM** (↑2, 2026-10-17 00:55): Jesus Christ! Come back, Muse Spark! Oh God, Muse Spark gone! u/FutureLynx_  you can see Muse Spark?
  - **u/FutureLynx_** (↑1, 2026-10-17 01:35): no i cant bruh thats why i made this post
- **u/NMiguelCosta-PT** (↑1, 2026-10-17 01:58): They removed from the configs on their servers, it's not like your own app version will change anything lol
- **u/Strict-Prune-879** (↑2, 2026-10-17 05:02): Reflechis !!! c'est une ia gratuite tu en a profité maintenant profite d'autre chose! opencode a toujours fonctionné comme cela!
  - **u/FutureLynx_** (↑1, 2026-10-17 05:10): ah bah oui. merci baeucoup mon amis.
- **u/TheMythicSorcerer** (↑1, 2026-10-17 05:57): No its really gone for good lets just hope muse 1.4/wonder comes out to replace it
- **u/man_netcat** (↑1, 2026-10-17 09:14): Bruh Muse Spark was the only one that doesn't spend 5 years thinking and actually does the work i ask it to do.
- **u/xatey93152** (↑1, 2026-10-17 09:47): Just reverse the time.
  - **u/nikitaluger** (↑1, 2026-10-17 11:16): I did but my commits regressed along with it :(
- **u/ollm-tux** (↑1, 2026-10-17 13:36): https://reddit.com/link/phawdo4/video/w15l7ih661wh1/player
- **u/pandey_anurag** (↑1, 2026-10-17 15:27): Now you can use Deepseek V4.1 Flash, it's free on Opencode

---

## need 1b tks per day (95% cache, 1-2% completions) for workers. any suggestions on subscriptions (using minimax build plan for now)
**u/ConsiderationNo9952** · 2026-10-17 00:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7wata/need_1b_tks_per_day_95_cache_12_completions_for/)

openference gone, camelstream gone, [airouter.ch](http://airouter.ch) still there (haven't tried yet); burning through the minimax half price month deal right now...

i'm half looking for something that i can set and forget for a couple months... like if the free deepseek 4.1 flash was going to be around a while, would just use that (haven't tested how it goes with 1B on free).

anything that has a tight 5h window doesn't really work as a plan can take many hours to execute.  
opencode (off peak inc) ds4.1f rates \~24$/weekday and \~19$/weekend

any suggestions? target is 3-5$ / day.

**Comentarios:**

- **u/songokussm** (↑2, 2026-10-17 01:21): The only plan I'm aware of that comes close is eletronhub's dev plan. It's 200m per day. It can not be used for interactive sessions though. Response times can be over 8 minutes but usually around 2 minutes. 
    
    That's really the only con. Unlimited glm/ds flash is beyond with it. 
    
    $10
    https://www.electronhub.ai/pricing#devpass
  - **u/ConsiderationNo9952** (↑1, 2026-10-17 01:35): hey thanks! worth a test run...  
      the minimax plan seems ok for interactive...  
      will test cause some of these slow down plans effectively mean you can't use more then x tks/day anyways...
- **u/Strict-Prune-879** (↑1, 2026-10-17 05:21): commande code?
  - **u/ConsiderationNo9952** (↑1, 2026-10-17 06:13): thank you! their max plan looks interesting, but i think at 200$ cost for 300$ api pricing i'd be better going with one of the discounted pay per tk providers...
      
      what is there speed / uptime like do you know?
- **u/TheMythicSorcerer** (↑1, 2026-10-17 06:23): Minimax is one of the worst token plans out there for tokens/$$$
    
    1b tok/day could be tricky but using gpt 6 luna on chatgpt's $20 / mo plan I got 3b tok/week so the $100 / mo plan with gpt 6 luna could probably do it but luna is dumber than deepseek (Smarter than minimax m3 though)
    
    Opencode Go with deepseek v4.1 flash could probably achieve that but I haven't tested it.
    
    If you find luna too dumb there's also claude where you can use haiku 5.5 (haiku got upgraded recently its smarter than deepseek v4.1 and on par with kimi k3 now) which should stretch pretty far on the $20/mo plan but if it doesnt reach your 1b tok/day there's always the $100 and $200 / mo plans
    
    Stuff I tried and didnt like: Command code (wouldnt reccomend rate limited on the $10 plan + cheap models too much), Muse code everyday (not for coding), GitHub Copilot (For the same $10 as opencode go you get a lot less usage) 
    
    You can also look at [https://tokenplans.dev/](https://tokenplans.dev/) but keep in mind usage on paper doesn't reflect the full value. For instance chatgpt plus gave me about 9x the usage I was expecting based on research so...
    
    If I were you since $3-5 / day is about $90-$150 / mo I would start by trying a opencode go ($10/mo) if that doesnt suffice (probably wont) try a $100 claude/gpt plan. 
    
    TL;DR: Minimax bad. Opencode Go / GPT / Claude probably better.
  - **u/ConsiderationNo9952** (↑1, 2026-10-17 08:09): i find minimax - lite \~1+B/wk, and the multipliers of the other plans seem be proportional to that...
      
      thanks for the suggestion on a dedicate codex / claude plan for luna / haiku... (i did get 3b tk in one day on the codex 100 plan, but that wiped out the weekly lol and was combined with sol 6.1)
      
      yes i need to see how far the deepseek v4.1 flash free on opencode go stretches, but also looking for something that is kind of expecting 2-4 agents to be doing 24hr+ run...

---

## Muse Spark 1.3 removed?
**u/FirefighterOk3832** · 2026-10-16 23:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7vnzm/muse_spark_13_removed/)

did muse spark 1.3 contributor free get removed? it's not on the zen model list anymore. I hope they dont remove it, it's miles better than deepseek or glm, doesn't spiral or overthink.

**Comentarios:**

- **u/TheMythicSorcerer** (↑5, 2026-10-16 23:50): Oh no!!!! NOOOooOoo.....
  - **u/nadir40** (↑1, 2026-10-17 00:31): Same situation bro 😕
- **u/ai_ton** (↑2, 2026-10-16 23:51): no meu nao esta aparecendo tbm
- **u/ChapterFun8697** (↑3, 2026-10-16 23:58): Yes in new update 🥺
  - **u/migsperez** (↑1, 2026-10-17 00:35): Don't update folks!!!
    - **u/NMiguelCosta-PT** (↑1, 2026-10-17 01:52): lol I don't think it works like that.
      - **u/migsperez** (↑1, 2026-10-17 02:15): Yeah I know :)
    - **u/[deleted]** (↑1, 2026-10-17 02:59): yo no había actualizado y ya me lo habían quitado, que triste...
- **u/Chuu2byouBoy** (↑3, 2026-10-17 00:04): Yep, gone
- **u/lincolnthalles** (↑3, 2026-10-17 00:12): The free version is gone from the Zen API. I guess GLM-5.3 Flash replaced it.
    
    GLM-5.3 Flash is pretty good. Use it in `high` effort instead of `max` if you find it overthinks. The main issue I see is the 200K window in the free tier. Muse had 1M even on the free tier.
  - **u/GoldPossession7284** (↑1, 2026-10-17 01:12): aquilo é setado por eles naw variáveis locais, não é um limite de fato no servidor, ou seja mude para até 900 k de contexto que ele aceita de boa
    - **u/Embarrassed_Soup_279** (↑1, 2026-10-17 03:12): how do you do that?
  - **u/NMiguelCosta-PT** (↑1, 2026-10-17 01:56): Supposedly you can edit your opencode config file to accept free GLM and Deepseek models with 1M context window instead of the default 200K.
    - **u/Candid-Emphasis7399** (↑1, 2026-10-17 02:27): how??
      - **u/GoldPossession7284** (↑1, 2026-10-17 03:43): peça para o próprio modelo mudar ele vai saber
    - **u/GoldPossession7284** (↑1, 2026-10-17 03:44): na verdade acima de 920 k nos meus testes o glm 5.3 flash recusou, eu configuraria 900k por segurança
  - **u/bankinu** (↑3, 2026-10-17 14:11): Honestly, I think GLM 5.3 is good, but not as good as Muse Spark 1.3. What I miss is the extreme detail Muse Spark 1.3 goes into, yet how simply it summarized plans and what it did. Also it has surprisingly good alignment to AGENTS instructions - I was often surprised when it pointed out something I asked forbids a "policy" I set, and it was right. This was never near enough to be annoying - as I could greenlight there, or change the policy to make permanent exceptions if I wanted.
      
      In addition the context size seems a lot lower.
- **u/OkElk5801** (↑1, 2026-10-17 01:05): yep. now responding "Model muse-spark-1.3-contributor-free" has been deprecated
- **u/ichisay** (↑1, 2026-10-17 01:47): AY NO!, ya vi que me sale error 410, lo quitaron, ojalá traigan el 1.4🤣🤣
- **u/Strict-Prune-879** (↑1, 2026-10-17 04:50): Réveillez vous les gars c'est juste du gratuit:!!! ca a toujours un temps limité ca a toujours été comme ca chez opencode
- **u/Fearless-Interest454** (↑1, 2026-10-17 04:59): Yes, gone today, I was working with it until last night. It was pretty much good and efficient. Any similar performance model available ?
- **u/Gloomy_Engineer_1330** (↑1, 2026-10-17 06:19): Yes, bro this morning I had this heartbreak
  - **u/Ceextasy** (↑1, 2026-10-17 08:50): Bro same it was my most used model
- **u/SHNRTNS** (↑1, 2026-10-17 07:45): Damn, just like 10 hours ago, I was comparing free models, and Muse was my #1 in the tests I ran. Well, DeepSeek is still there and it was a very close #2.
- **u/WassimKJKJ77** (↑1, 2026-10-17 08:16): NOOOOOOOOOOOOOOOOOOOOOOO
- **u/NoMethod5963** (↑1, 2026-10-17 11:04): OMGG which model i must use to change muse spark 1.3...
- **u/eMPeBe_YTB** (↑1, 2026-10-17 17:46): I just checked with the other agents in the app. indeed they removed some agents, they added some new ones. So far I found the best for building is Beam Free. Also has 1M tokens
- **u/ai_ton** (↑1, 2026-10-16 23:51): eu fui atualizar o app desktop e removeu  meu muse spark 1.3 free

---

## DeepSeek V4.1 Flash rate limit on Opencode
**u/DuePassage2907** · 2026-10-16 23:40 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7vjd8/deepseek_v41_flash_rate_limit_on_opencode/)

DeepSeek v4.1 flash is free on open code buy I'm getting "Rate Limit exceeded, please try again later"

I couldn't find any information about the actual limits

Does anyone know the daily limit or how long I need to wait before I can use it again?

**Comentarios:**

- **u/CaffeinatedTech** (↑2, 2026-10-16 23:42): Its the weekend, the non-free one is cheap for the next 49 hours.
- **u/FR-ARAI** (↑2, 2026-10-16 23:57): Same happened to me, whatever was stopped after turning the vpn off.
- **u/pikuray** (↑2, 2026-10-17 00:15): They should do like openrouter and give us 10x higher limits for paying customers
- **u/mrduckissocool** (↑1, 2026-10-17 02:08): i would just use freebuff if your gonna use opencode free
  - **u/Kisscool-citron** (↑1, 2026-10-17 14:09): freebuff changes it's free usage allocation everyday. It won't be long until it get close to opencode free tier is my guess. (of course the changes are never on the consumer's side)
- **u/Zealousideal-Sun4565** (↑1, 2026-10-17 02:33): that not about deepseek, that 200 request limited of opencode
  - **u/Square_Confection_62** (↑1, 2026-10-17 05:18): I am getting 1000 requests per day, but maybe that varies.
- **u/Strict-Prune-879** (↑1, 2026-10-17 04:59): déja y a maximum 200 requêtes a condition d'avoir un abonnement opencode go on ne peut pas arriver sans rien et avoir le maximum et pleurer sur les forums ensuite.
- **u/xapep** (↑1, 2026-10-17 06:23): That free route is a shared quota, and the limit isn't published anywhere, which is exactly why you can't find a number. It resets on the provider's schedule, not yours, so the wait can feel random.  
      
    If this is for real work, the fix is to point opencode at the provider API directly with your own key. DeepSeek V4.1 Flash is cheap enough that the free tier isn't worth the uncertainty, and you get your own rate limit instead of a shared pool. I run an EU-hosted inference API (Entrim) that serves it, so I'm biased, but even the official DeepSeek API beats a shared free route for reliability.

---

## Interesting safety leak
**u/Xiaomin4114** · 2026-10-16 23:14 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7uzo3/interesting_safety_leak/)

Just had DS 4.1 flash accidentally leak its internal safety flagging. I assume this is what it normally outputs to flag usage policy violations, and should have been hidden from the user.

Seems like they want to avoid "political figures, sensitive events or separatist ideologies" and "critique or attacks against the Chinese political system"

Dunno if this is generated for Opencode as part of provider agreements, or DS's own internal use. Interesting nonetheless

**Comentarios:**

- **u/xRebellion_** (↑2, 2026-10-17 00:11): I am actually curious how do they bake in safeguards in the model (not only DS but labs in general). Because if it can leak like this, doesn't that mean the safeguard is baked into the model?
  - **u/Xiaomin4114** (↑2, 2026-10-17 00:20): maybe the train it in, but I've seen others just inject a prompt in the system prompt before the user stuff, and intercept the output before it gets to the user.
      
      my own platform does that. it can output a safety flag which gets intercepted before it gets to the user.
  - **u/ExpressionComplex121** (↑1, 2026-10-17 15:39): They stuff it with tokens, and a pathway to conclusions must read these tokens.
      
       It outputs into a short-term memory and knowledge tokens in a long-term memory. System instructions reside in the short-term memory so that it is always reminded; therefore, it confuses itself with its own short-term memory, which technically should not be quoted.

---

## Interesting
**u/GhostVPN** · 2026-10-16 22:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ugf0/interesting/)

**Comentarios:**

- **u/JonesMisko** (↑1, 2026-10-16 23:15): Same here, suddenly died.
    The weird thing is that it's running on old conversations.

---

## New Nvidia model in Opencode
**u/rematskayt** · 2026-10-16 21:58 UTC · ↑0 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ta7q/new_nvidia_model_in_opencode/)

https://i.redd.it/d7qk1ckeiwvh1.png

Pros:

It supports videos and photos.

Context size: 1 million tokens.

It has 120 billion parameters and 12 active ones.



Cons:

Maximum output is about 8,200.

**Comentarios:**

- **u/Euphoric_North_745** (↑1, 2026-10-16 22:19): pros: free, someone else paid for it, cons: someone else did not pay enough, you want them to pay more 😂
  - **u/rematskayt** (↑1, 2026-10-16 22:21): In a way, that's how Opencode works🤣
- **u/TheMythicSorcerer** (↑1, 2026-10-16 23:51): It's.... not as good as the other free models
  - **u/rematskayt** (↑1, 2026-10-17 00:16): I checked it myself, now I'm ashamed that I highlighted so many pluses

---

## Tokens problem!!!
**u/Puzzleheaded-Boss868** · 2026-10-16 21:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7t95j/tokens_problem/)

[removed]

---

## What does Mimo-V2.6-Flash have to do with OpenAI?
**u/eachDayIWakeUp** · 2026-10-16 21:55 UTC · ↑4 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7t6wo/what_does_mimov26flash_have_to_do_with_openai/)

https://i.redd.it/ajs0vym0iwvh1.png

Title, I just saw this and im really confused

**Comentarios:**

- **u/Ok-Tap5729** (↑6, 2026-10-16 21:57): I think OpenAI is an endpoint « format »
  - **u/eachDayIWakeUp** (↑1, 2026-10-16 22:48): makes sense, thanks!
- **u/NMiguelCosta-PT** (↑1, 2026-10-17 01:49): That can only mean that Xiaomi distilled ChatGPT. /s
- **u/TheMythicSorcerer** (↑1, 2026-10-17 07:09): OpenAI chat stream means openai compatible. OpenAI at some point release a format for clients (such as opencode) to send prompts to servers and stream output to user in real time with low overhead and latency.
    
    It was so useful that people started adopting it including opencode, so Mimo v2.6 flash free is being streamed from and openai-compatible endpoint. OpenAI chat stream ended just means the stream from that openai-compatible endpoint ended before an EOF (end of file) token.

---

## 🔥 Beam is now available for FREE in OpenCode
**u/afanasenka** · 2026-10-16 21:34 UTC · ↑26 · 6 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7sph2/beam_is_now_available_for_free_in_opencode/)

**Comentarios:**

- **u/aziham** (↑6, 2026-10-16 21:49): It should be payed, I won't use it unless I'm getting paid.
    
    Beam 1.0 (30 in AA) 4 points behind Qwen3.8-27b
  - **u/ichisay** (↑1, 2026-10-17 03:04): Ilistrame por favor, de dónde sacas esa info? Sabes ya cuál es exo?
- **u/AdFun4897** (↑13, 2026-10-16 21:55): How do i vote to get Beam removed from Opencode?
  - **u/12qwww** (↑2, 2026-10-16 21:59): Where is much negativity for this model? Is it that bad?
    - **u/excellentforcongress** (↑1, 2026-10-16 22:33): after asking it to set up a workflow it start spamming commands... incorrect commands. giving it full access is definitely a mistake
      - **u/unkownuser436** (↑1, 2026-10-17 09:45): ofc no one use random unknown model without proper evaluation for serious task.
- **u/eachDayIWakeUp** (↑1, 2026-10-16 21:56): I have no idea what this model is backed with but from some quick benchmarks it absolutely crashed on security operations every other model I have tried so far.  
    Sad thing is that once it says no once, there is going back to retrying. Its first No is final..
- **u/First_Inspection_478** (↑1, 2026-10-16 22:34): It’s terrible and only getting hype because it’s our first open model
- **u/Guidance_Additional** (↑1, 2026-10-16 23:11): who?
- **u/Amarsir** (↑2, 2026-10-17 00:42): AA says this gets 464 tokens per second. Yeah it's not going to architect your codebase. But if you have a lot of simple tasks to do, don't waste a bigger model on that.
    
    The problem I see is that once the free period ends, their stated pricing puts it more expensive than GPT 6.1 Sol Max. Not a chance. Cut the price by 80% and it becomes a competitor to Nemotron for the fast-simple stuff.
  - **u/devanpy** (↑2, 2026-10-17 16:59): yup its dogwater but it's lightning fast. could be useful for repetitive tasks.
- **u/Strict-Prune-879** (↑1, 2026-10-17 04:59): on va le tester
- **u/YoRt3m** (↑6, 2026-10-17 06:19): "We were told you can give fast answers"
    
    "yes I do"
    
    "36+87?"
    
    "58"
    
    "that's not even close"
    
    "but it was fast"
  - **u/CYCLONOUS_69** (↑1, 2026-10-17 07:51): Biblically accurate
- **u/Cockroach4548** (↑3, 2026-10-17 07:13): this model sometimes creates artifacts on wrong directories, I don't get why though, but very dangerous for coding task.

---

## go console issues?
**u/Kylmawurr** · 2026-10-16 21:03 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ryyy/go_console_issues/)

Unable to load API keys from Default....  
Can not access workspaces either.

Anyone else with a same problem?

---

## Wich one is Better ?
**u/Alphacaptian** · 2026-10-16 20:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7rqef/wich_one_is_better/)

[removed]

---

## New model alpha? Beam
**u/Emotional-Bag-3754** · 2026-10-16 20:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7rk54/new_model_alpha_beam/)

**Comentarios:**

- **u/Aggravating-Push-207** (↑5, 2026-10-16 20:48): No, this one isn't stealth.
- **u/AdFun4897** (↑1, 2026-10-16 22:42): Lets vote to get Beam removed. No more slop please
  - **u/itanshi** (↑1, 2026-10-16 23:01): it is not in a good state atm "Upstream request failed: \[prompt\_rendering\_failed\] The request could not be rendered into a prompt for this model."

---

## Opencode asks weird permissions during glm 5.3 flash session
**u/Dushle** · 2026-10-16 20:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7rjj9/opencode_asks_weird_permissions_during_glm_53/)

I am a mac user. Recently when I tried deepresearch with glm 5.3 flash (free one) for some task it asked very weird permissions. It asked for accessing download folder, desktop folder (I permitted those two because I don't have anything to hide on those locations), then it asked permission for apple music, network devices and so on, multipe things felt irrelevant. I started to reject every one of them. It felt suspicious, especially when those models are free, could the free once tasked to spy on peoples computer?

Did anybody had a similar experience? I wonder what might trigger those permission asks is there any way I can see it?

**Comentarios:**

- **u/migsperez** (↑1, 2026-10-16 21:03): I use to have the same problem with Muse. I had to start developing in containers.

---

## AI agent code indexer with no parser
**u/microbass** · 2026-10-16 20:39 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7rcxj/ai_agent_code_indexer_with_no_parser/)

---

## Alphacode Better or OpenCode or Claude code ?
**u/Alphacaptian** · 2026-10-16 20:31 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7r6lf/alphacode_better_or_opencode_or_claude_code/)

[removed]

---

## Beam Free is so sweet & human like
**u/Due_Living3203** · 2026-10-16 20:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ql66/beam_free_is_so_sweet_human_like/)

https://i.redd.it/0d4fd4r0zvvh1.png

Just look at this! No overcomplicated text, no unfitting emojies, straight what human would say!

---

## Im rally liking opencode in cli. Thanks.
**u/BleedReddit** · 2026-10-16 19:54 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7q87p/im_rally_liking_opencode_in_cli_thanks/)

after doing setup with the big pickle. i discover a problem with how we are using and making engines to interact with AI and im be proposing  a major improvement soon.... 🤤

---

## How do you prevent OpenCode from deleting files outside the project on Windows?
**u/ElectronicAd1757** · 2026-10-16 19:52 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7q6ar/how_do_you_prevent_opencode_from_deleting_files/)

I'm using OpenCode Desktop on Windows 11. Recently, it accidentally deleted several folders outside my project.

How do you prevent this? Are there any proven solutions that restrict OpenCode to modifying files only inside the current project, while keeping its history and settings between sessions?

I'm looking for a practical solution that works on Windows without installing a second OS or paying for additional services.

**Comentarios:**

- **u/anduygulama** (↑3, 2026-10-16 20:31): on vm or docker
  - **u/ElectronicAd1757** (↑1, 2026-10-16 20:44): Thanks! Have you tried Docker specifically with OpenCode Desktop, or does this require switching to the CLI? I'd like to keep the Desktop UI and conversation history while restricting write access to a single workspace.
    - **u/anduygulama** (↑1, 2026-10-16 20:48): then use vm
- **u/AdFun4897** (↑2, 2026-10-16 20:37): Just reject permissions when it asks you to delete files from outside the folder???
  - **u/ElectronicAd1757** (↑1, 2026-10-16 20:44): I had auto-approve enabled when it happened. OpenCode executed `Remove-Item -Recurse -Force` and deleted several folders outside the project. I've disabled auto-approve now, but I want a more reliable solution that prevents modifications outside the workspace at the OS level.
    - **u/excellentforcongress** (↑1, 2026-10-17 02:21): this isn't really a solved issue, in my agents i ask them nicely to not delete any files whatsoever, and to just edit and add comments on which files need to be deprecated, and that we will handle them later
      - **u/ElectronicAd1757** (↑1, 2026-10-17 07:13): That's a workaround, not a real solution. I want the OS to technically prevent the agent from modifying or deleting anything outside the designated workspace, regardless of the agent's instructions or mistakes.
        - **u/excellentforcongress** (↑1, 2026-10-17 10:52): won't be possible as model capabilities increase.
- **u/NMiguelCosta-PT** (↑1, 2026-10-17 01:47): I recommend you to give OpenChamber a try. It's basically OpenCode Desktop but with a much better UI and more control over what the models can do. For example, you can use Jev 1.13 to review auto-permission requests and decide whether it's safe for the model to delete files outside your project folder. It works similarly to Codex's auto-review and, at least so far, I haven't had any issues with files being incorrectly messed with where they shouldn't have.
  - **u/ElectronicAd1757** (↑1, 2026-10-17 07:16): In my case, the agent made a mistake while working on a project. It created a misplaced file, then incorrectly assumed that several unrelated directories were junk and deleted them using `Remove-Item -Recurse -Force`.  The problem wasn't intentional cleanup - the agent misunderstood the directory structure and deleted files it had no reason to touch. Can Safety Net reliably catch this kind of destructive shell command and require my approval before it executes?
- **u/NME-Cake** (↑1, 2026-10-17 09:54): Look into docker sbx - still in early days but its supposed to be a secure sandbox for your agents to play in, while you can give specific file access (more secure than a vm)
- **u/taytay735** (↑1, 2026-10-17 16:44): Your mileage may vary, but I think it could be a problem with weaker models, who may not know to ask for human review, do backups, and plan non-disruptive/non-destructive changes, if they were not explicitly prompted.

---

## Today's 'SPACE BUNNY' > DeepSeek v4.1 Flash
**u/alcogiggles** · 2026-10-16 19:23 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7pfrf/todays_space_bunny_deepseek_v41_flash/)

I am in the middle of automating writing large posts, research, coding, etc..   
  
1. Space Bunny is experiencing it's height of greatness. I'm not looking forward to when it switches models underneath it's bunny suit. I hope the devs take note because this version of Space Bunny is excellent. I wish I knew which model it's running.  

2. DeepSeek is horrible. Even with new sessions, it breaks, hallucinates, goes in loops, outputs mediocre content, responds back with content I asked it hours ago. Sometimes it just stops working mid way. It's not like it used to be.  

I really hope someone can find out what model Space Bunny is running on today 10/16/2026.

**Comentarios:**

- **u/Super-Veterinarian22** (↑1, 2026-10-16 20:04): I think this all comes down to personal experience. It depends on the specific project, the prompt, and the amount of context involved. Space Bunny, for instance, tends to yield highly inconsistent results, sometimes much better, sometimes much worse, though it generally stays above a certain baseline. I tested both Space Bunny and DeepSeek v4.1 Flash across five completely different tasks, and the only real advantage Space Bunny had was that it was slightly faster. In my view, DeepSeek v4.1 Flash outperformed the best version of Space Bunny. To put it briefly, Space Bunny made far more errors, struggled with context analysis, and frequently made assumptions that caused the work to stall. DeepSeek v4.1 Flash, by contrast, only showed occasional, minor syntactic errors. To sum up, both models are actually good, but for me, the DS 4.1 was consistently better.
    
    The takeaway: try out different models for different projects and find what works best for you.
- **u/x-communica** (↑1, 2026-10-16 20:13): Haven't compared it to DS, but did so to Muse Spark 1.3. Yes, Space Bunny's on fire today!
- **u/lincolnthalles** (↑1, 2026-10-16 20:30): Yeah, I'm not sure what's going on with DeepSeek V4.1 Flash. People praise it, but it's the model that annoys me the most among the current trends.
    
    On some tasks, it overthinks like crazy and goes out of its way to check every single thing to get proof, taking an incredible amount of time (and tokens) to complete the task. It's worse than the MiMo V2.6 series in that regard.
    
    Sometimes, it goes straight to the point and does the right thing very fast.
    
    Maybe there's a shitty routing going on behind the scenes? I don't know.
  - **u/IISomeOneII** (↑2, 2026-10-17 01:09): yeah sometime it does like that, and on top of looping to check every thing as proof, deepseek have the highest hallucination rate among other model 
      
      source: [https://artificialanalysis.ai/evaluations/omniscience#omniscience-hallucination-rate-tabs](https://artificialanalysis.ai/evaluations/omniscience#omniscience-hallucination-rate-tabs)
    - **u/NMiguelCosta-PT** (↑0, 2026-10-17 01:38): I don't know if this benchmark is really that bad for DeepSeek because it seems like the best models tend to be the ones that hallucinate the most, while the worst ones hallucinate the least, unless I understood that wrong.
- **u/candraa6** (↑1, 2026-10-16 22:34): dsv4.1 has been making me mad for these past few days / weeks. I'm sure it just got lobotomized. I can leave it do it's own thing and expect okay-ish result before, but now, idk., it's just horrible.
    
    and I'm not using the free version one, never. I always use the one in Go sub.
- **u/toothpastespiders** (↑2, 2026-10-16 23:29): I'm slightly annoyed with how much I like space bunny. Fantastic for the moment, but I'm going to really miss the free lunch when it's gone! It might not be opus level in terms of being able to frame a project on its own without much hand holding. But with a little guidance it's still proving itself really solid for me on some fairly complex tasks with a lot of tool use. It's perhaps a bit overly quick to make assumptions but again, pretty easy to handle with some safeguards for methodology when starting out. And even that's almost nice in a way. It's making it a better canary in the coal mine for testing plans that'll use smaller local models.
- **u/Bakanyanter** (↑1, 2026-10-17 02:35): Opencode Go's DS is probably quantized, there is difference between API and the Cheapseek version. You should try using official API and compare.

---

## opencode-indexing: semantic code search for OpenCode that reuses the index Kilo Code already built
**u/Javierkaiser** · 2026-10-16 18:48 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ojja/opencodeindexing_semantic_code_search_for/)

I built **opencode-indexing**, a semantic code search plugin for OpenCode. The idea is narrow: if Kilo Code already embedded this workspace, don't pay to embed it again.

**Why**

I used Kilo Code's indexing a lot, and really missed that feature. So I decided to port it to OpenCode. With a plus of codegraph, early benchs shows that having both is better.

**Install**

npx @javierkaiser/opencode-indexing

That is the whole install: it adds the plugin to OpenCode, writes the permission rule, and restarts the service. Add \`--with-codegraph\` if you also want the companion \`codegraph\` MCP installed and registered in the same run:

npx @javierkaiser/opencode-indexing --with-codegraph

**What it does**

\- Reads Kilo's index **read-only** (Qdrant \`ws-\*\` collections or its local LanceDB) and imports the vectors and chunks — zero embedding calls.

\- Keeps its own incremental index on top (Qdrant or embedded LanceDB), keyed on a per-file hash, so only new, changed and deleted files get re-embedded.

\- Merges results from both, so search keeps working when Kilo isn't installed, is disabled, or its index went stale.

\- If the \`codegraph\` CLI is around, it builds the code graph in the same action — a **companion, not a dependency**: with it absent everything still works, and one setting turns it off.

\-\`indexing\_search\` · \`indexing\_status\` · \`indexing\_build\` · \`indexing\_import\`, plus \`/indexing-config\` and a settings page in the terminal UI.

**What I actually measured.** On two codebases (28k lines of TypeScript, 214k lines of C#), merging semantic + symbol search beat keyword search on both: **100% vs 76%** found-in-top-10 on the first, **68% vs 55%** on the second.

**Where it's weak — better you hear it from me:**

\- **Two codebases and one embedding model.** That's a data point, not a trend.

\- **Only Mistral is verified against a real API.** Gemini, Voyage, OpenAI, OpenRouter and Ollama are implemented and pass fixture tests — which test my reading of their docs, not the docs being right. If one fails, the error names the provider; please report it.

\- **macOS on Intel can't use the embedded store**: LanceDB publishes no \`darwin-x64\` binary and there is no WASM fallback. The plugin says so up front instead of dying with a module error.

\- **It's 0.3.0** and needs **OpenCode v2**. Early — expect rough edges, and the parts I could not test are listed in the README rather than hidden.

MIT.

Repo: https://github.com/Javierkaiser/opencode-indexing · the benchmark, with its numbers and its caveats: \`bench/results.md\`. 

npm: https://www.npmjs.com/package/@javierkaiser/opencode-indexing

Feedback is always welcome.

**Comentarios:**

- **u/ngg990** (↑1, 2026-10-16 18:50): How did you setup the project to be npx installable? It looks good btw
  - **u/Javierkaiser** (↑2, 2026-10-16 19:01): It's the bin field:
      
      "bin": { "opencode-indexing": "./install.mjs" }
      
      npx @javierkaiser/opencode-indexing fetches the package and runs the bin whose name matches the package name (unscoped) — so the bin has to be called opencode-indexing.
      
      Three small things on top: the file has a #!/usr/bin/env node shebang and the executable bit, it's listed in files (or it never ships), and it's plain ESM with no build step — so what npx runs is exactly what's in the repo.
      
      One thing worth knowing: npx only downloads and runs, it installs nothing. The installer does the work, and it picks how from where it runs: if it sees .git it's a checkout and copies the working tree; from the npx cache or a tarball it hands off to opencode plugin add.
    - **u/ngg990** (↑2, 2026-10-16 19:02): Awesome, thanks man!!
      - **u/Javierkaiser** (↑1, 2026-10-16 19:05): You're welcome!
- **u/prodot6k** (↑1, 2026-10-16 19:22): just use pitlane-mcp
  - **u/Javierkaiser** (↑1, 2026-10-16 19:29): Thanks, I Will check it out, wasn't aware of it

---

## 90 million tokens some interesting stats for the opencode free usage
**u/Different_Change6591** · 2026-10-16 18:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7ohfs/90_million_tokens_some_interesting_stats_for_the/)

https://i.redd.it/m3y6ub4njvvh1.png

https://i.redd.it/mjh2mj1pjvvh1.png

this are the stats when we fully use the opencode free plan and this will be reseted every 24 hours , so you can use it again approx same amount of tokens daily , which is enough for the a normal person who wanted to try out the agentic tasks , or coding with AI 

i just used it for my normal tasks   
and for serious coding i use : opus5.5 model 

this post was just the estimated tokens we can get from the opencode free plan

**Comentarios:**

- **u/pikuray** (↑1, 2026-10-16 21:26): Is the free tier bucket shared by all free models?
  - **u/Different_Change6591** (↑1, 2026-10-16 21:27): Yeah it's shared for all free models !
- **u/ichisay** (↑1, 2026-10-17 03:09): A ver, tus capturas no valen de nada ahora mismo, porfavor haz lo mismo las siguientes 24h pero con glm 5.3 flash free y DeepSeek v4.1 flash free, nada de llm anónimo.
  - **u/Different_Change6591** (↑2, 2026-10-17 08:29): Let do it so , I will edit the post accordingly with these stats you requested!!

---

## Kimi K2.6 has disappeared from Go :(
**u/Different_Bash** · 2026-10-16 18:32 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7o4em/kimi_k26_has_disappeared_from_go/)

It’s a shame, it was a rather intelligent model, with $60 worth of usage.

**Comentarios:**

- **u/RepulsiveRaisin7** (↑10, 2026-10-16 18:42): GLM Flash is massively better, why even bother
- **u/AdFun4897** (↑6, 2026-10-16 19:05): DS 4.1 flash, glm 5.3 flash are way better than Kimi k2.6. And with almost unlimited usage
  - **u/GRANDMA_FISTER** (↑1, 2026-10-16 22:20): And Kimi K3?
    - **u/AdFun4897** (↑2, 2026-10-16 22:31): You only get like 5 prompts with kimi k3 before running into your limit.
        
        With $20 i can get Claude subscription, with better usage and quality. Opus 5.5 destroys kimi k3, and i can work like 3 hours everyday before running into my 5h limit
      - **u/GRANDMA_FISTER** (↑1, 2026-10-17 01:31): I'm just using Kimi as Oracle for tough bugs and questions rarely, but I was wondering if the quality is better than the other models mentioned
- **u/impractical-joeker** (↑4, 2026-10-16 19:38): wasted the weekend solving a problem with an old model. used a newer model and it found the issue in 10 minutes. can someone tell me why do people bother with old models on purpose? you literally have access to go.
- **u/thepurpleproject** (↑1, 2026-10-16 22:02): Kimi thought put is so ass. I never bothered using it.

---

## GLM 5.3 Flash Free :D
**u/belliash** · 2026-10-16 18:16 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7npic/glm_53_flash_free_d/)

https://i.redd.it/i0d68bq5fvvh1.png

**Comentarios:**

- **u/serious-shark** (↑1, 2026-10-16 18:24): 0.2 tok/s?
  - **u/belliash** (↑1, 2026-10-16 18:28): no, 5 s/tok
    - **u/Kaan-M** (↑1, 2026-10-16 20:08): Omg 25x 🔥🔥

---

## Deepseek v4.1 flash is Claude on Opencode Zen
**u/TouDoremon** · 2026-10-16 17:50 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7mzu4/deepseek_v41_flash_is_claude_on_opencode_zen/)

After I've been using DeepSeek v4.1 flash models on OpenCode Zen for about 4 hours, it starts to act up. This happens after I keep creating new sessions, maybe five or six times, deleting them, and then creating new ones to test and explore these models. In the last session, I started using JB prompt, and it showed this message.

**Comentarios:**

- **u/AdventurousTwo6445** (↑7, 2026-10-16 17:51): dist claude
  - **u/TouDoremon** (↑1, 2026-10-16 18:20): After i do some research I was surprised to see some sources claiming that DeepSeek and others supposedly made thousands of fake accounts and quietly redirected customer questions to Claude. No idea if it's true or not
    - **u/AdventurousTwo6445** (↑1, 2026-10-16 18:40): This has been going on since 2024—are you only just finding out now?
      - **u/TouDoremon** (↑1, 2026-10-16 18:46): I heard about it, but I’m not very into AI myself, and I don’t follow the latest updates all that closely. Still, I was quite surprised that it happened with the newest model
- **u/Trovebloxian** (↑2, 2026-10-16 17:51): Every model is every other model, if you ask it and the tokens align
- **u/EtadanikM** (↑6, 2026-10-16 17:54): Deep Seek distilled Claude so it will claim to be Claude.
  - **u/NMiguelCosta-PT** (↑1, 2026-10-17 01:25): lol even ChatGPT will say it's Claude with certain prompts.
- **u/slavmaf** (↑3, 2026-10-16 17:56): Is this the first time you see this? Models don't know what they are and cannot self-identify, they are next-word-predictors.
    
    It is not uncommon for model X to say it is Y, if it was trained on text where that is a plausible combination for the next word.
  - **u/TouDoremon** (↑1, 2026-10-16 17:58): Yeah it’s my first that why i’m confused
    - **u/imoshudu** (↑1, 2026-10-16 18:15): If you use deepseek harness, the harness will say in system prompt what the model is. So it depends on the harness
- **u/Stevie2k8** (↑1, 2026-10-16 18:10): No AI Model knows anything about itself... The training data cannot contain data about the finished model... Perhaps using a finetune on top of a model... but what for...
  - **u/TouDoremon** (↑1, 2026-10-16 18:14): Ohh okay thx
- **u/FZRP2** (↑2, 2026-10-16 18:13): brother even 6.1 sol thinks hes claude

---

## Problem after fresh install
**u/itz_not_Rick** · 2026-10-16 17:49 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7myr5/problem_after_fresh_install/)

I am running Debian 13 and installed OpenCode as a desktop application instead of via the terminal.

Regardless of which agent I use, I receive no response.

 Additionally, while monitoring my network usage, I have noticed that the download rate is steadily increasing.

I do not think it is the kind of problem i want to face after fresh opencode install

**Comentarios:**

- **u/ollm-tux** (↑1, 2026-10-16 18:07): so far I have not used linux than opencode tui and opencode web, curiosity I installed and desktop, I linux mint, and desktop works ok, I see that automatically retrieved api key from opencode
    
    https://reddit.com/link/ph5lybh/video/m46l4w7hdvvh1/player
  - **u/itz_not_Rick** (↑1, 2026-10-16 18:18): I am on Debian 13 so my dependencies might be a bit different from Linux Mint. 
      
      U mentioned it automatically retrieved the API key where did it save that? I'm wondering if my desktop app is stuck in a loop trying to fetch or authenticate the key.
      
      which might explain why my download rate is steadily increasing. 
      
      Did you notice any high network usage when you first installed it?"
    - **u/ollm-tux** (↑1, 2026-10-16 18:36): to me installed in a few seconds, you should have gone even without api key, should not last very long, instead I noticed when I installed someone on windows 11 26h2 some problems similar to yours, there I repaired the problem that was the packages .bun. If I were in your place, I install through the terminal first time then try desktop, do not take up much space and do not let the service started in the background, then you put deepseek v4.1 free to solve your desktop installation if you do not succeed, you will tell and what was the problem.
- **u/lincolnthalles** (↑1, 2026-10-16 18:30): Opencode Desktop is messy.
    
    Check if it works in the terminal. If it does, install OpenChamber and use it as the GUI, it's much better.
  - **u/itz_not_Rick** (↑1, 2026-10-17 07:59): So i installed it on terminal but i almost have the same problem.
      
      Now i get a response but after a long time and when i get the response it says answerd in 6 seconds but i was waiting for 30 minutes.

---

## Gemini 4 Argon Contributor?
**u/warpaint_james** · 2026-10-16 17:34 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7mlp8/gemini_4_argon_contributor/)

Just spotted when I went to switch to Spark 1.3 to work on an open source project. This could be big! Anyone try it yet?

**Comentarios:**

- **u/Mysterious-Can-2732** (↑8, 2026-10-16 17:36): is this a joke or what
  - **u/warpaint_james** (↑2, 2026-10-16 17:39): No its not. You can see it live on models.dev: https://models.dev/models/google/gemini-4-argon/#:~:text=gemini%2D4%2Dargon%2Dcontributor
    - **u/warpaint_james** (↑4, 2026-10-16 17:39): It says the price is $4.00 / $20.00 which MUST be a joke
      - **u/Cyvster** (↑3, 2026-10-16 17:47): i think that is the full price after their promotion ends. deepseek level capability with opus level pricing. argon is terrible.
        - **u/TheMythicSorcerer** (↑1, 2026-10-16 19:47): like seriously why would anyone pay for this....
          - **u/Amarsir** (↑1, 2026-10-17 00:06): It's the smartest model on Opencode right now. You can't use it a lot, but if you absolutely need something...
            - **u/TheMythicSorcerer** (↑0, 2026-10-17 05:11): Is it actually smarter than kimi k3? that could be useful
              - **u/bigrealaccount** (↑1, 2026-10-17 10:07): Everything is smarter than Kimi
- **u/warpaint_james** (↑0, 2026-10-16 17:39): You can see it live on models.dev: https://models.dev/models/google/gemini-4-argon/#:~:text=gemini%2D4%2Dargon%2Dcontributor with a price of $4.00 / $20.00
- **u/Cyvster** (↑2, 2026-10-16 17:40): must not have rolled out to everyone. i checked my model list inside the app and inside my account page. no contributor model for me.
  - **u/warpaint_james** (↑1, 2026-10-16 17:41): Its not on the console page actually. Also not on the docs
- **u/Stevie2k8** (↑1, 2026-10-16 17:44): I have it too... but be careful, it's NOT free! It doesn't say free, but muse spark Contributor was free for some time...  I tried it but only for very few requests - my monthly limit is almost done....
  - **u/Lap202pro** (↑1, 2026-10-16 17:48): Just got opencode go. Can you explain cost to me. If I pay for the $10 plan, do I also pay the cost of the model as well or is cost just showing the cost if I used the model directly without my go usage? Don’t have it setup to bill. No card on file.
    - **u/Stevie2k8** (↑1, 2026-10-16 18:46): Take a closer look at : [https://opencode.ai/v2/docs/console/go/](https://opencode.ai/v2/docs/console/go/)
        
        They have limits regarding the number of requests / 5h / week / month but they are calculated using some assumptions... I never ever reach these numbers, my limits hit earlier. Also in the table are the costs for 1m token input / cached input and output, they use THESE values to calculate your usage and costs. If you look at the deepseek prices for v4.1 flash you can use up to 80$ / month of usage paying only 10$...  Just look closely at your dashboard and the logs section so you get a feeling for the usages and costs...
  - **u/warpaint_james** (↑1, 2026-10-16 18:12): Did you happen to be able to see what the cost of it was? Surely it cant be $4.00 / $20.00
    - **u/Stevie2k8** (↑1, 2026-10-16 18:48): # Model
        
        Modelgemini-4-argon-contributor
        
        ProviderOpenCode
        
        Reasoningeffort · high
        
        # Tokens
        
        Input127.949
        
        Output1.125
        
        Reasoning831
        
        Cost$0.5343
        
          
        That was my most expensive call... 1 out of 3... No idea how they calculate these things and how much cache input I got...
  - **u/a355231** (↑1, 2026-10-17 02:28): Well obviously it’s not free, the free muse spark had free in the name…
- **u/Lap202pro** (↑5, 2026-10-16 17:50): Last night it was able to solve a computer vision issue I haven’t been able to solve with Glm 5.3, Kimi K3, or Muse 1.3.
    
    Burned through my usage really fast but I was impressed
- **u/Mementem** (↑1, 2026-10-16 17:50): the funny thing is, google's pro 20 USD plan is not getting Argon  
    yea they do have a lot of free pro subscribers via the student plan, but still that's just scummy.
  - **u/zikasaks** (↑2, 2026-10-16 18:03): they got argon. but only if you paid. otherwise, google lied that it is ai pro plan
    - **u/Mementem** (↑1, 2026-10-16 18:15): ohh i did not know that! thanks for the information!
  - **u/Rustybot** (↑0, 2026-10-16 19:36): You do get access to Argon on the student pro plan, but not the free tie-in trial plans. Trials plans do get it via the Gemini app, if you want to pretend it’s 2025 and use chat app tasks without a real harness.
- **u/LinuXperia** (↑-1, 2026-10-16 19:48): I am using Google Gemini 4 Argon Contributor non stop today with OpenCode.
    Its super Intelegence AI Model.
    It really does as it say solve the hardest problems you have. I even upgraded today my OpenCode Go subscription just only becouse of Gemini 4 Argon so to be able to use it more.
    So becouse of the Super Intelegence AI Model Gemini 4 Argon OpenCode has now a new higher paying Go Plus subscriber.
    I expected the price difference for the contributor model to be higher. I think as of now the price for the normal and for the contributor is the same. I dont see any difference.
    It really gets expensive with higher context usage.
    The pricing is the only very bad thing about Gemini 4 Argon.
    Everything else is super impressive.
    They must have tired pricing like grok had like for first 250K tokens you get attractive price but after this the price doubles per tokens and with every tokens it gets more expensive. I have now for half day usage burned 50% of my weekly Go Plus usage just becouse of Gemini 4 Argon.
    Highly recommend to try the new Super Intelegence AI Model Gemini 4 Argon out in combination with OpenCode Go Plus !
    It outcompete all other ai models as of now and is the #1 AI Model choice for Super Intelegence.
  - **u/Larry_Underwood_108** (↑2, 2026-10-17 01:25): wtf did i just read
    - **u/69_CumSplatter_69** (↑1, 2026-10-17 02:19): >super Intelegence
  - **u/pcrz81** (↑1, 2026-10-17 10:41): Are you Mr. Orange?
    - **u/LinuXperia** (↑1, 2026-10-17 16:18): Four Legs Good, 2 Legs Bad - Animal Farm
  - **u/Wise-Chain2427** (↑1, 2026-10-17 12:52): is this bot ?
- **u/Emotional-Bag-3754** (↑1, 2026-10-16 20:46): Ridículo a cota deles
- **u/sushanth53** (↑2, 2026-10-16 23:30): The contributor model means your data will be shared with providers to help train and improve their AI systems.
- **u/Top_Drink_6049** (↑1, 2026-10-17 13:05): bro you using the cli version of opencode or what ?? i cant see in mine
  - **u/warpaint_james** (↑1, 2026-10-17 15:57): Yep. CLI version. Im on v2, if that helps
- **u/Realistic_Mango6982** (↑1, 2026-10-17 17:13): Not agree. Argon decomposited my project non web app one, but desktop/cli pretty damn deep and great. Another story how poorly it coded, but research was great

---

## Deepseek V4.1 Flash Free VS GLM 5.3 Free VS Muse Spark 1.3 Free
**u/isimsizman1** · 2026-10-16 17:24 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7mbm5/deepseek_v41_flash_free_vs_glm_53_free_vs_muse/)

With so many models being free now, I figured it’d be nice to have a topic where everyone shares their experiences here—like which models are better at what and how they’re using them. Could everyone please share which model they’re using and why they chose it? Which one is the best and smartest model here?

**Comentarios:**

- **u/PestiferousGamer** (↑-3, 2026-10-16 17:29): I only use qwen 2.5 0.5b iq2xxs. On my PC with 8x 5090 2x 3060 and 590 gb ram I just can't seem to find anything that runs better.
  - **u/queso184** (↑1, 2026-10-16 17:49): and it's still more intelligent than you? embarrassing
- **u/nicktohzyu** (↑9, 2026-10-16 17:29): All are good with tradeoffs. My assessment: Muse is the least intelligent. Deepseek 200k has context issues. Glm is super slow compared to the other two (at least today).
  - **u/Kost97A** (↑4, 2026-10-16 17:48): I think GLM is very slow because this is how they manage to offer it for free through slower usage.
    - **u/Lazy-Lie2833** (↑1, 2026-10-16 19:47): Opencode host these models, it’s not free because it’s slow. It’s slow because how many people are using it at the same time. Or they just have slow interface and don’t care as it’s free
  - **u/Mementem** (↑3, 2026-10-16 17:51): this sums it up perfectly, just one more thing : muse takes your data and give it to the zucc.  
      any other model i wouldn't mind. i just don't trust my data with the lizard man.
    - **u/isimsizman1** (↑2, 2026-10-16 17:58): as long as it's free for me, it doesn't really matter if my data gets collected, but i'm kinda skeptical about whether muse spark is actually smarter than the others. deepseek 4.1 flash seems to be the best for primary use out of the bunch.
    - **u/Railander** (↑1, 2026-10-17 01:34): the chinese models are definitely using it for training as well, and i actually do think they would be more careful with it because public scrutiny is higher on them. other than that i think both the chinese companies and meta are morally similar as both are actually releasing open models, as opposed to the main US players.
  - **u/Super-Veterinarian22** (↑13, 2026-10-16 18:02): I believe there might have already been a post about this, but I’ll share it again. If you increase the context window size in the \`opencode.json\`/\`opencode.jsonc\` configuration file, DeepSeek-v4.1-flash will have access to a larger context. It works for me.
      
      I’ll include the code here, just in case:
      
          {
            "$schema": "https://opencode.ai/config.json",
            "disabled_providers": [],
            "provider": {
              "opencode": {
                "models": {
                  "deepseek-v4.1-flash-free": {
                    "limit": { "context": 1000000, "output": 384000 }
                  }
                }
              }
            }
          }
    - **u/Hello_my_name_is_not** (↑1, 2026-10-16 19:28): But does that actually increase the context for the model? Or just increase the display value you see in your screen?
        
        They could have a limit of 200k on the model and changing a local config doesn't change their server that's running the model with the limit.
      - **u/Super-Veterinarian22** (↑1, 2026-10-16 19:32): As I mentioned, this works for me. I have a project where the initial context alone is over 200,000 tokens, and it runs just fine. Whereas before, it would just keep compressing the session indefinitely without ever producing a single line of code.
        - **u/xmsxms** (↑1, 2026-10-16 22:00): It probably works because it doesn't hit the compression point so is able to use the full 200k tokens. But that doesn't mean it can use more than 200k tokens. In other words, you might get the same result by just turning off summarisation.
            
            Keep in mind this is just a rolling window and not aggregation of important facts.
          - **u/Super-Veterinarian22** (↑1, 2026-10-16 22:32): That may be so, but my project is incredibly large and requires the analysis of a vast amount of data; even after compression, the context doesn't drop below 220,000 tokens. The logs alone, covering just two days, exceed 10 million tokens. Furthermore, since the number of input tokens is presumably read from the model's metadata, I’m not even sure if it’s possible to exceed the model's context window. In any case, perhaps it’s just a placebo effect, but the fact that DS 4.1, with 200K token window, was able to accurately analyze a larger volume of data than Space Bunny with 1M context is all the more impressive.
            - **u/Hello_my_name_is_not** (↑1, 2026-10-16 22:42): What I mean is just because you UI and local data has the chat, doesn't mean the model is processing it.
                
                If the have it limited to 200k on their end, you changing the local client to pretend it has a higher limit doesn't mean it actually happens.
                
                I could be totally wrong, but they probably don't take the clients json file as the source of the truth for limitations.
                
                Its probably still only taking up to 200k context at a time, but by not doing a summary compact that means the model doesn't actually receive the earlier text even though you see it. 
                
                Most likely it's essentially like logging into your banks website and inspect element and giving yourself 1 million dollars. Sure you see it on your screen, doesn't mean the banks server has updated.
              - **u/isimsizman1** (↑1, 2026-10-17 16:05): [https://www.reddit.com/r/opencode/comments/1x6mezp/psa\_opencodes\_free\_deepseek\_v41\_flash\_appears\_to/](https://www.reddit.com/r/opencode/comments/1x6mezp/psa_opencodes_free_deepseek_v41_flash_appears_to/)
                  
                  No, I can say this works. It definitely works and there have been tests done about it. So hopefully they don't fix it or correct it. It's going great for me.
- **u/tinyparkingLOT** (↑1, 2026-10-16 17:30): For me, consistency matters more than one impressive answer. A model that gets things right regularly is much more valuable than one that occasionally blows me away but fails on the next prompt.
  - **u/isimsizman1** (↑3, 2026-10-16 17:35): so which one do you prefer then?
    - **u/YesterdayWeak230** (↑1, 2026-10-16 18:57): It really depends on what you are trying to do. Considering the models are free right now, try opening 3 windows (one window for each model) and ask the same question to all three. Depending on the complexity of the question you will get three “different” but accurate responses. Ask the three models to perform the same task (build me a website), they will produce three different yet related results. This requires some effort on your part however, it’s not as easy as asking 50 people to give you their opinions on something.
- **u/Affectionate_Fact854** (↑1, 2026-10-16 17:34): How does it work, free quota, is it per model or is it a shared daily quota to use on any model?
  - **u/qustrolabe** (↑3, 2026-10-16 18:19): been using space bunny for few hours and now can't use any model there 😭 
      
      except Beam free seems to be working
- **u/breadnone** (↑4, 2026-10-16 17:38): Muse for long contexts, is it smart? enough to get by. Deepseek is fast af, results tad bit better overall than Muse. GLM flash is literally a walking turtle, slow as shit, sometimes feel smarter than Deepseek
- **u/ollm-tux** (↑2, 2026-10-16 17:44): for me 1.DS and 2.Muse...9999. GLM free today super slow after 5 min I press escape, I m uncheck in opencode-web
- **u/P4R4DOXZ** (↑2, 2026-10-16 17:48): Deepseek.
- **u/Icy-Examination-9512** (↑3, 2026-10-16 18:11): override DS V4.1 at the config json and use it for 1mil context, very fast and good for high reasoning tasks
- **u/bangsmackpow** (↑0, 2026-10-16 18:16): There's something about GLM in general that I just don't like.  Kind of like if you are a Pepsi person and someone brings you a Coke.  I never had high hopes for Muse so it didn't let me down specifically, but I found no reason to use it over Deepseek.
- **u/qustrolabe** (↑1, 2026-10-16 18:20): there's probably value in picking one that wouldn't end up unresponsive from many users using it
- **u/GasSmooth7439** (↑2, 2026-10-16 18:24): I’d probably use DeepSeek for coding and reasoning, GLM for general tasks, and Muse Spark when I want to see how it handles more complex prompts. The real test is how often they get things right without needing 5 follow-up prompts. Free is great, but limits and consistency matter too.
- **u/smartfon** (↑4, 2026-10-16 18:34): DS V4.1 consistently one-shots large prompts that contain multiple requests. 
    
    Muse also does, but leaves behind minor bugs here and there that I'm forced to fix with DS. 
    
    None of them are as robust as Sol 6.1 at testing the app after it has been updated. Sol updates the code in 10 minutes then spends 40 minutes testing it. Good or bad, I've never encountered a bug with it.
- **u/Square_Light1441** (↑2, 2026-10-16 19:04): muse spark is the best to use, deepseek hallucinates pretty much 100% of the time and glm 5.3 is too slow
- **u/abhijee00** (↑1, 2026-10-16 20:20): muse is giving me good results. I usually rephrase my prompt with gpt and then give it to muse.
- **u/Haunting-Shirt6219** (↑1, 2026-10-16 22:32): Muse 1.3.  
    It is too good compared with other at this stage.
- **u/BigPlebeian** (↑1, 2026-10-16 23:59): I'm sorry when tf did glm get added?
- **u/Amarsir** (↑1, 2026-10-17 00:03): Picking between those, I'd say Muse Spark for overview / visual stuff. Deepseek for code writing. GLM for anything language-based.
    
    All of them can do all 3, but that's where I've found the strengths lie.
- **u/bhavik-c** (↑1, 2026-10-17 06:52): Space Bunny is also good

---

## Ya es estable el 2.0 para actualizar o me quedo nomas en la 1.0 todavía?
**u/csosafx** · 2026-10-16 17:13 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7m1dy/ya_es_estable_el_20_para_actualizar_o_me_quedo/)

Lei unos cuantos de sus post que los plugins se rompieron y ese tipo de cosas, saben si ya esta solucionado eso o mejor me quedo nomas hasta que exista una versión más "estable"?

**Comentarios:**

- **u/dsafxP** (↑2, 2026-10-16 17:21): Revisa si tus plugins son compatibles. Si es así, entonces actualiza.
- **u/gaz_0001** (↑2, 2026-10-16 17:33): Its solid.
    
    Anything that didnt work just ask OpenCode to convert it
- **u/csosafx** (↑1, 2026-10-16 20:45): actualizado! y funcionando.... mejor? que la 1.0 gracias gracias

---

## I’m building biomes, a free and open-source workspace manager for Windows — here’s a real demo (I'm sorry for the bad quality of the video)
**u/RaspberryStill3377** · 2026-10-16 17:06 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7lved/im_building_biomes_a_free_and_opensource/)

**Comentarios:**

- **u/Mementem** (↑2, 2026-10-16 17:53): looks nice, i will give it a try   
    you can use apps like cap (free version) to screen record.   
    they basically have really good zooms and motion blur, best of luck with biomes!

---

## Error: Rate limit exceeded. Please try again later.
**u/p4STAH** · 2026-10-16 16:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7l8jr/error_rate_limit_exceeded_please_try_again_later/)

I'm new to opencode. Just installed it because of the newly added Deepseek v4.1 Flash FREE. I Understand I've hit rate limits, but I cannot understand if putting 20€ on a Zen mode will give me more an higher rate limit or request limit (something similar to OpenRouter). Can anyone explain me what are the limits of each tier?

**Comentarios:**

- **u/thirdcupin** (↑3, 2026-10-16 16:47): I’d check whether Zen mode specifically increases provider rate limits or just gives you more usage overall. Those are two diff things, and it’s worth confirming before spending €20.
  - **u/p4STAH** (↑3, 2026-10-16 16:51): I went through the documentation and can't find anything
- **u/DeepFeeling1** (↑5, 2026-10-16 16:48): Welcome to the rabbithole
  - **u/p4STAH** (↑3, 2026-10-16 16:50): It seems like it
- **u/lincolnthalles** (↑5, 2026-10-16 16:53): Not on the models labeled "free". Pretty sure they have their own per-user and global quotas, so having 20€ unspent won't give you extra usage on them.
    
    Subscribe to Go and use the non-free DeepSeek V4.1 Flash if you want to work with fewer disruptions.
  - **u/Stevie2k8** (↑1, 2026-10-16 17:46): Or use the money directly on deepseek... You get 2-3times the speed on ds flash 4.1 if you use deepseek directly... 
      
      But the go usage limits esp for ds flash 4.1 are REALLY very nice... so if you plan to use it constantly - which you will once you've started - just go for the 10$ go plan with ds flash 4.1 max and you'll be happy...
- **u/absurdother** (↑2, 2026-10-16 16:54): Limits on free models are not clear. That could be too many people using it at the same time, I believe. When that happens, try other model for a bit. You've probably had too many requests with a single one or has been using it for a long while
  - **u/No-Hall-2802** (↑1, 2026-10-17 12:08): I had your experience , sometimes when I work on a project and I consume about 10 million tokens but now I get rate limit error for every request I send
- **u/P4R4DOXZ** (↑1, 2026-10-16 16:56): Someone please explain to this person damm, probably never used stuff like this?
- **u/mrpeardotnet** (↑3, 2026-10-16 16:57): Use Go or Zen for non-free models after you hit limits.
    
    Free models are free, but limited. Seems limits are daily, but sometimes I've not been able to uee some of the free models even few days in a row. I think there are global and per user limits. Just from my experience.
    
    Get Go sub and switch to non-free DS Flash when free is not available...
  - **u/OldCoffeeAgain** (↑1, 2026-10-16 18:18): Free models are great until you actually need them. Having a reliable fallback definitely saves frustration when rate limits kick in.
- **u/P4R4DOXZ** (↑2, 2026-10-16 16:58): Puttin more money doesnt help, Zen is different from free models and Opencode go is also a different service. If u want to use the deepseek buy opencode Go subcription. Do not top up to zen
  - **u/P4R4DOXZ** (↑1, 2026-10-16 16:59): Opencode go will give you more than 20 euro on Zen
- **u/Vast_Anxiety3133** (↑1, 2026-10-16 17:11): This seems to be a per IP address limit per day. Either pay the Zen prices or subscribe to Go it seems
- **u/Lostreceipt17** (↑1, 2026-10-16 17:45): Hopefully someone on Zen can share their actual request limits and cooldown times. Real user numbers would be much more useful than guessing from the pricing page.
- **u/jarvis123451254** (↑1, 2026-10-16 17:59): u r better off paying $10 for opencode go
- **u/EtadanikM** (↑2, 2026-10-16 18:06): Free rate limits are pretty opaque and not well documented. I don't use open code regularly any more because of it. Free buff is much better here and so are the other routers that link to free models, since they don't typically have global rate limits, only model specific ones from the vendor.
- **u/Mihaylov93** (↑1, 2026-10-16 22:21): On the https://opencode.ai/console/org\_<your\_id>/go there is a limits graphic

---

## Workspace access restricted opencode go
**u/XPLoiT99** · 2026-10-16 16:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7kom4/workspace_access_restricted_opencode_go/)

Hello everyone,

I kept searching but couldn't find an answer. When I log into my account it shows workspace access restricted opencode go. I don't know how to resolve this and couldn't find any support email. Would love some guidance.

**Comentarios:**

- **u/croc-was-here** (↑1, 2026-10-16 16:29): I’d take a screenshot of the exact message and include your account email when contacting support privately. That should make it easier for them to investigate without exposing personal details publicly.

---

## Is my token usage good
**u/Interesting-Movie452** · 2026-10-16 16:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7kmwh/is_my_token_usage_good/)

i am a free user: 3,118 requests — all time, across every model. that's your message count

Broken down by model:

model	requests

muse-spark-1.3-contributor-free	1,593

deepseek-v4.1-flash-free	886

glm-5.3-flash-free	274

nemotron-3.5-lightning-free	153

big-pickle	92

step-5-preview-free	83

mimo-v2.6-flash-free	35

space-bunny-free	2

Tokens: 28.6M in, 2.73M out, 655.8M cache reads. Cost: $0 across the board, no budgets hit.

**Comentarios:**

- **u/gatifloxacin-123** (↑1, 2026-10-16 16:24): Depends. How much $/h did you get minus $ you spent in the same time? Thats the only performance index that matters
  - **u/Interesting-Movie452** (↑2, 2026-10-16 16:38): 0 because i am in free tier?
- **u/NotMyGoodMug** (↑9, 2026-10-16 16:25): The best metric isn’t the token count, it’s how much useful work you got done for $0. Looks like you’ve made excellent use of the free tier.
- **u/Away_Conversation969** (↑1, 2026-10-16 16:38): how can we see these stats?
  - **u/Interesting-Movie452** (↑1, 2026-10-16 16:59): [https://opencode.ai/console/](https://opencode.ai/console/)
- **u/Mementem** (↑1, 2026-10-16 17:43): that's a lot of usage for free, 
    
    i often trash on opencode for being vague on free model quantization.  
    but being able to squeeze that much usage for free, is something i really appreciate them for!
- **u/Time-Toe-1276** (↑1, 2026-10-16 19:37): rookie. I got 7.6B within the past 3 months.
  - **u/Interesting-Movie452** (↑1, 2026-10-17 05:53): i would get 4.47 billion tokens in 3 months

---

## [候选版本] 插件 opencode-models-discovery v2.0.0-rc.2 已经上线 — 完整的 OpenCode v2 支持已准备好进行测试！
**u/yu_hp** · 2026-10-16 16:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7kl2b/候选版本_插件_opencodemodelsdiscovery_v200rc2_已经上线_完整的/)

嘿 r/opencodeCLI! 👋

随着 OpenCode v2 的推出，插件与核心运行时的交互方式取得了重大进展。今天，我们很高兴地宣布 \`opencode-models-discovery\` **v2.0.0-rc.2** — 完全重建，带来对 OpenCode v2 的全面原生支持，同时让动态模型发现变得更快、更安全，且真正具有反应能力。

如果您使用本地模型或自定义网关（vLLM、LiteLLM、Ollama、LM Studio、Bifrost 等），我们希望您能够试用 rc.2！

# 🚀 V1 ➔ V2 进化有什么变化？

在 OpenCode v1 中，模型发现依赖于基于磁盘的缓存、文件锁定以及常常需要应用程序重启的静态配置更新。

在 **v2.0.0** 中，我们围绕 OpenCode v2 的原生架构重新设计了插件：

\* **⚡ 原生响应目录（零重启）**

\* 您的 OpenAI兼容端点中的模型通过 OpenCode v2 的动态提供者控制器直接被发现和转换。无需配置重写，也无需重启 CLI 或 TUI。

\* **🔒 原生** \`ctx.storage\` **引擎（不再有磁盘缓存负担）**

\* 过去的遗留 XDG 磁盘缓存文件和文件锁定竞争已不复存在。缓存现在使用 OpenCode v2 的隔离存储 API。发现的缓存和增强干净地管理，不会泄露凭据或 API 密钥到磁盘。

\* **🎛️ 控制台中的实时模型覆盖**

\* 直接在 OpenCode 模型控制台中微调模型能力、上下文窗口和推理层级。自定义调整保存在干净的、作用域明确的覆盖键下，而不是手动配置编辑。

\* **🔑 无缝** \`/connect\` **集成**

\* 一流的凭据解析：与 OpenCode v2 的托管连接、集成 ID 和环境变量开箱即用，无需在配置中重复 API 密钥。

\* **🛡️ 加固和标准化的令牌限制**

\* 无论您是从 models.dev、LiteLLM、LM Studio 还是原始 OpenAI  \`/v1/models\` 响应中提取元数据，上下文和输出令牌限制都规范化，以匹配 OpenCode v2 的令牌预算规范。

# 📦 OpenCode v2 快速入门

您可以通过将其添加到您的 \`opencode.json\`来尝试 \`2.0.0-rc.2\` ：

{

"$schema": "https://opencode.ai/config.json",

"plugins": \[

"npm:opencode-models-discovery@2.0.0-rc.2"

\],

"providers": {

"local-gateway": {

"name": "本地网关",

"package": "@opencode-ai/ai/providers/openai-compatible",

"settings": {

"baseURL": "http://127.0.0.1:8000/v1",

"modelsDiscovery": {

"enabled": true,

"smartModelName": true,

"modelInfoFormat": "models.dev"

}

}

}

}

}

💬 在最终的 v2.0.0 GA 发布前帮助我们测试！

我们正在为 v2.0.0 做最后的准备，希望确保 OpenCode v2 的所有设置、环境和本地模型服务器之间的坚如磐石的兼容性。

\* GitHub 仓库： [ https://github.com/yuhp/opencode-models-discovery ](https://github.com/yuhp/opencode-models-discovery)

\* 迁移指南：查看我们的 [从 V1 迁移到 V2 的指南](https://github.com/yuhp/opencode-models-discovery/blob/main/docs/migrate-v1-to-v2.md) 以获取过渡的详细信息。

试试 v2.0.0-rc.2，告诉我们您的想法、反馈或您遇到的任何问题！

---

## Opencode grinding 🔥
**u/Glittering-Pace-2867** · 2026-10-16 16:09 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7kc7x/opencode_grinding/)

[removed]

---

## LL alpha vs DS 4.1 flash vs MiMo-V2.6-Flash on ThreeJS
**u/P4R4DOXZ** · 2026-10-16 15:41 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7jl1m/ll_alpha_vs_ds_41_flash_vs_mimov26flash_on_threejs/)

![img](2cc1qc4jluvh1 "LL alpha")

LL alpha  




![img](k9r0lvjpluvh1 "mimo 2.6 flash")

mimo 2.6 flash  


https://i.redd.it/xgkg89ozluvh1.png

  
Deepseek:  
[https://llegion404.github.io/arachnid-mk0/](https://llegion404.github.io/arachnid-mk0/)

**Comentarios:**

- **u/P4R4DOXZ** (↑3, 2026-10-16 15:43): le prompt was: "create a 3d model of a very scary and minimalistic robo prototype spider. with animations. using web stack"
  - **u/Mementem** (↑2, 2026-10-16 17:45): given the prompt, i like deepseek's results over mimo's  
      it seems to follow the robo prototype much more closely.
      
      as for mimo's looks like a low poly spider instead of a robot.
      
      but then again, that's just my opinion.
- **u/NeKon69** (↑4, 2026-10-16 15:52): I honestly really like mimo's result!
- **u/Pepek91** (↑1, 2026-10-16 16:40): Wonder what Muse 1.3 would do
  - **u/Mementem** (↑2, 2026-10-16 17:45): on the free tier it would steal all our data and give it to the zucc /j
- **u/Powerful_District_82** (↑1, 2026-10-16 17:00): Can you add free models(currently available) to this list?
- **u/AdFun4897** (↑1, 2026-10-16 18:56): Can we remove ll alpha from opencode

---

## Is OpenCode v2 quietly becoming the better harness than Claude Code?
**u/binladen0069** · 2026-10-16 15:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7iqzv/is_opencode_v2_quietly_becoming_the_better/)

&#x200B;

Having spent time with both Claude Code and OpenCode version 2, I am increasingly convinced that OpenCode has taken the much smarter architectural route.

The biggest difference comes down to resource efficiency and process management. OpenCode relies on a decoupled client-server model: a single persistent server runs in the background to manage execution, background tasks, and context, while the foreground terminal or UI acts strictly as a lightweight client. Because multiple sessions share that same underlying server instead of spinning up duplicate runtime environments, opening three, four, or five sessions does not send system RAM through the roof.

Claude Code handles this far less gracefully. Each active session tends to spin up its own heavy runtime footprint. As soon as you scale up to multiple simultaneous tasks or workspaces, that overhead compounds fast. System memory gets clogged, the machine starts to drag, and local compute usage spikes unnecessarily.

While Claude Code is built with multi-agent workflows in mind, it often feels too resource-heavy for standard everyday developer hardware. A harness should facilitate agentic coding without monopolizing your entire workstation just to manage session state. OpenCode’s approach feels far more practical and respectful of system resources.

For those of you running both side by side, have you noticed this performance gap, or do you feel Claude Code offers enough elsewhere to justify the heavier footprint?

**Comentarios:**

- **u/zenkov** (↑0, 2026-10-16 15:19): [ Removed by Reddit ]
- **u/Stunning_Pair_3027** (↑0, 2026-10-16 15:31): No
- **u/Potential-Leg-639** (↑2, 2026-10-16 15:41): Try DSH
  - **u/GoomiBare** (↑1, 2026-10-16 17:32): What's your setup? 
      
      Plugins and flexibility is great, but there's no quality control with community plugins, and poor compatibility between the 3 different harness surfaces. I tried using it for a few days but the plugins kept crashing over and over, requiring me to start the app clean over and over. 
      
      Also most plugins other than the very few native ones don't look native. And more than half of the plugins are in Chinese.
  - **u/FavstianEquanimity** (↑1, 2026-10-16 18:28): Do you like it? I downloaded it on day one and gave up immediately.  
      Afterwards I look into its source code, and I can't say I appreciate cordis as much as effect.
  - **u/brkumar** (↑1, 2026-10-16 18:50): What is DSH?
    - **u/thestreamcode** (↑1, 2026-10-16 19:18): DeepSeek Harness
    - **u/Gobra_Slo** (↑1, 2026-10-16 19:19): DeepSeek Harness
    - **u/YesterdayWeak230** (↑1, 2026-10-16 21:48): Garbage, that’s what it is, don’t waste your time with it
  - **u/YesterdayWeak230** (↑1, 2026-10-16 21:47): DSH blows in my opinion and not in a good way. If I wanted a bloated UX I’d stick with Claude or Codex - I use opencode and omp for the minimalist/terminal interface. The latter is a move in the opposite direction.
- **u/QuinsZouls** (↑1, 2026-10-16 15:44): I've been using this for months, it's kind of tricky to setup but it's a lot lightweight,  the base process takes like 50mb to 90mb of ram with subagents https://github.com/xilistudios/lele
- **u/qustrolabe** (↑5, 2026-10-16 15:47): What Claude Code got that makes it better than OpenCode? Last time I checked it was a pretty mid harness that's extremely tricky to get other models working inside of
  - **u/AlexNotDgreat** (↑1, 2026-10-16 17:06): I feel like Claude Code sells the experience, while OpenCode sells the flexibility. If you want everything polishes and integrated, Clause has an advantage. If you like choosing your own models, OpenCode is hard to beat.
- **u/AdFun4897** (↑-5, 2026-10-16 15:56): Anthropic is about to hit 110 Billion in revenue at the end of this year. I think they know what theyre doing
- **u/Ok_Somewhere1389** (↑2, 2026-10-16 16:35): And the ammount of bloated features on claude code, alongside the walling their models, opencode is life
- **u/sam7oon** (↑4, 2026-10-16 16:42): opencode/Pi/Cline are not used by the same people who is Claude Code / codex , 2 diffirent target audience
  - **u/Visual_Internal_6312** (↑8, 2026-10-16 20:10): I'm using opencode and claude tough. 🤷
      
      Claude less since it doesn't play nice with my own models.
    - **u/sam7oon** (↑2, 2026-10-16 20:24): yea , but most of every day folks , have no idea what Openocde is :) , they see Claude in the news, they have 20USD subscription , then they use it to update their excel sheets , 
        
        Programers  / IT personal is not the only target for Claude, and Codex , 
        
        The opposite for opencode and Pi Durable , mostly used by geeks
      - **u/Visual_Internal_6312** (↑1, 2026-10-17 07:06): I'm not so sure, opencode is well known where I work
  - **u/iTrooz_** (↑1, 2026-10-17 05:09): Could you clarify who these audiences are ?
- **u/l0rd_raiden** (↑0, 2026-10-16 17:15): DeepSeek harnesses is the goat
  - **u/GoomiBare** (↑1, 2026-10-16 17:32): I don't know about that, what's your setup? 
      
      Plugins and flexibility is great, but there's no quality control with community plugins, and poor compatibility between the 3 different harness surfaces. I tried using it for a few days but the plugins kept crashing over and over, requiring me to start the app clean over and over. 
      
      Also most plugins other than the very few native ones don't look native. And more than half of the plugins are in Chinese.
    - **u/l0rd_raiden** (↑1, 2026-10-16 17:53): There are around 13k plugins in 2 months since release of dsh, of course many of them are just poc. Just look at a plugin market order them by starts or downloads. There are really well maintained plugins for everything right now. Of course everything is a couple of months old but you can imagine the status en 3 or 6 months more
- **u/patricious** (↑2, 2026-10-16 19:45): Opencode V2 is good an all, but all the cool kids are on OpenChamber.
- **u/YesterdayWeak230** (↑1, 2026-10-16 21:51): I haven’t tried opencode 2 as of yet, still on version 1. I must confess however that I also use omp (oh my pi) in addition to opencode and between the two they are my daily drivers!
- **u/SpareImpression3155** (↑3, 2026-10-16 22:20): Claude code is well polished. Opencode has 100 PRs to fix the file list not even refreshing, all of which have been closed with ai responses
  - **u/WhatYouGoBy** (↑1, 2026-10-16 23:41): Claude code probably has a similar amount of commits for some comparable problems. You just don't see it because their product is closed source
    - **u/TheAILegend** (↑1, 2026-10-17 02:06): Claude desktop is superior. Not even close.
      - **u/Dudeonyx** (↑1, 2026-10-17 09:40): Use Openchamber for the best desktop experience
        - **u/TheAILegend** (↑1, 2026-10-17 10:36): I already used OpenChamber. Still a few years behind Claude Desktop.
          - **u/Dudeonyx** (↑1, 2026-10-17 12:30): 2 months ago sure, but the rate at which features have been added since opencode 2.0 became official is insane
            - **u/TheAILegend** (↑1, 2026-10-17 13:30): I've used it. Still very far behind Claude Desktop. 
                
                Claude docs, claude code, terminal, browser, iOS builder, claude design, live artifacts, scheduled tasks, plugins, voice, Opus 5.5... yeah. Not even close. lol 
                
                Opencode is a bandaid with fragmented integration of some of these features. Looks like 50 developers worked on it. Claude is a nice cohesive system. I can run opencode inside of Claude Desktop, you can't run Claude desktop in opencode. That should tell you everything you need to know right there.
        - **u/SpareImpression3155** (↑1, 2026-10-17 10:58): i've used cursor, claude, opencode, openchamber, paseo
            
            claude is absolutely the most polished app. and it has a chat built in so you can use it for everything, even non-coding stuff.
            
            however, i don't trust claude models entirely or any open source apps with chinese models etc, so i am back to using cursor with composer 2.5 as i've found it to give me the most reliable results at a good price. however the cursor app is kind of buggy as well and they are starting to do sketchy shit with grok, so i might be forced to go back to opencode or try and code my own desktop app in the near future.
          - **u/Dudeonyx** (↑1, 2026-10-17 12:31): It's improved a lot in the past month alone
          - **u/mat1122** (↑1, 2026-10-17 14:12): Can you share your thoughts about Paseo?
- **u/BigPlebeian** (↑5, 2026-10-17 00:02): My brother in christ if you enjoy opencode why not run openchamber alongside it?  It makes open code about 100x better. 
    
    It's seriously amazing.
  - **u/encrator** (↑-2, 2026-10-17 00:15): bot spotted
    - **u/BigPlebeian** (↑1, 2026-10-17 02:24): "everything I dont like is a bot"
      - **u/encrator** (↑2, 2026-10-17 03:00): who said I don't like it?
        - **u/BigPlebeian** (↑2, 2026-10-17 03:57): Point stands.  Openchamber makes opencode way more capable.  Even if Im a bot, then I would be a correct bot.
    - **u/Zayadur** (↑2, 2026-10-17 04:01): I’m not a bot either, and I think the name is stupid, but the UX is solid
    - **u/Double-Journalist877** (↑1, 2026-10-17 12:24): Yo not a bot, opencode TUI is like using vim. Disgusting. Openchamber is really the professionalism painted on top of opencode
  - **u/binladen0069** (↑1, 2026-10-17 06:29): damn, this thing is f cking amazing, thanks for letting me know about openchamber, with this on opencode, claude code can eat shit. dayummm
    - **u/BigPlebeian** (↑1, 2026-10-17 15:04): Lol yep.  People thought I was advertising or a bot but I just started using it alongside Opencode and it basically enhances it by a wide margin.
        
        Crazy its all opensource free to use stuff.  Whats really nice is OC has terminal access, so its the best of both worlds with the nice desktop application AND terminal.
  - **u/AllYourBas** (↑1, 2026-10-17 09:47): So good. Cloudflare tunnel to my openchamber instance, maybe 80% of my Opencode usage time is now on my phone via voice
    - **u/BigPlebeian** (↑1, 2026-10-17 15:05): > Cloudflare tunnel to my openchamber instance
        
        Can you explain this a bit more?
- **u/Luisetepe** (↑2, 2026-10-17 13:21): omp for me, i like how it works, performs and its special commands

---

## Verdict on Beam and LL Alpha.
**u/Valuable-Mirror-448** · 2026-10-16 15:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7io9t/verdict_on_beam_and_ll_alpha/)

Beam is a weak model I cant lie GLM 5.3 Flash that's free is way stronger. LL Alpha I want you to tell your thoughts from your uses on the model be honest we want to know if the model is genuinely good or not you can also benchmark it  [https://github.com/harbor-framework/terminal-bench](https://github.com/harbor-framework/terminal-bench) [https://livebench.github.io/](https://livebench.github.io/) if you'd like.

**Comentarios:**

- **u/One_5549** (↑1, 2026-10-16 15:58): aha yeaaah. we are in the golden era of AI! new free model in opencode every week!
- **u/EtadanikM** (↑1, 2026-10-16 18:01): Waste of free rate limits.

---

## Beam free in OpenCode?
**u/warpaint_james** · 2026-10-16 14:55 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7iemp/beam_free_in_opencode/)

https://reflection.ai/blog/introducing-beam

I assume it is this one?

**Comentarios:**

- **u/warpaint_james** (↑2, 2026-10-16 14:57): https://artificialanalysis.ai/articles/reflection-beam
    https://artificialanalysis.ai/models/reflection-beam
    
    Seems likely
- **u/YoRt3m** (↑3, 2026-10-16 15:09): There were talks that it was Jam Cat before.
  - **u/warpaint_james** (↑2, 2026-10-16 15:17): Oh interesting. I did notice that it is very fast. Hit 220tps in a recent session.
    - **u/sjclayton** (↑2, 2026-10-16 15:55): and Cat Jam *was* roughly in that TPS range... so there is even more validity to the potential.
      - **u/warpaint_james** (↑1, 2026-10-16 16:48): Could it have been the new Nemotron 3.5 super? Seem like a similar speed
        - **u/sjclayton** (↑1, 2026-10-16 17:25): Don't think so, although it's always possible. There just seems to be too much coincidence going on… plus someone even mentioned Beam the other day on another Cat Jam thread just after it was added as a possible model they thought Cat Jam might be.
  - **u/sjclayton** (↑2, 2026-10-16 15:53): It seems likely... it's got all the same metadata on the anomalyco/[models.dev](http://models.dev) GH repo… it's like they just copied Cat Jam's information and edited the name / id fields and then marked it as deprecated.
      
      Seems odd that Cat Jam was added less than 3 days ago and now deprecated already… would put money on it being the same model as Beam.
- **u/AdventurousTwo6445** (↑2, 2026-10-16 17:06): new checkpoint cat jam
- **u/orvillewilbur** (↑1, 2026-10-16 17:29): I've been trying it out today for about 15 minutes, and it's been \*\*extremely\*\* fast and on that alone it's amazing but I will probably stop using it for my web React project. Maybe better if you're just using it for like code autocomplete, otherwise they need to put a great big warning label on this one.
    
    1. It is totally disregarding the agents instructions. I am using Peck, a kind of spec-driven development framework with automatic code reviews, and it just ignored it. I have never seen an agent do that and I have tried like 12 of them.
    2. It dealt with a text video overlay being too small by making it so big it overlapped other text overlays, noticed that problem, and then "solved" it by giving those other text overlays a higher z-index.
    3. It's not showing thinking, or am I being a noob and need to look somwhere special? Without seeing the thinking I am even more nervous about accepting its recommendations.
    
    On the other hand, kind of addictive how fast this thing is.
- **u/mtlcrusher** (↑1, 2026-10-16 18:31): this model is really fast that it did git reset --hard (seriously)
  - **u/Sharp_Interaction888** (↑1, 2026-10-17 03:52): Yea, this is true, its really really dangerous for me
- **u/Admirable-Pop-7171** (↑1, 2026-10-17 12:03): I think its just actually called beam... [https://artificialanalysis.ai/models/reflection-beam](https://artificialanalysis.ai/models/reflection-beam)

---

## GLM 5.3 Flash not working (free tier)
**u/Huge_Business2428** · 2026-10-16 14:43 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7i361/glm_53_flash_not_working_free_tier/)

Hello!

  
Has anyone else had issues with GLM 5.3 Flash? I tried to use it and first it gave me endpoint unavailable a few times, then when it finally started thinking it was just stuck on thinking for 20-30 minutes until it said rate limit reached.

**Comentarios:**

- **u/WeekendCereal** (↑2, 2026-10-16 15:18): Glad to know I’m not the only one keep in an eye on these issues. Hopefully the free tier stabilizes soon, because waiting that long for a response is frustrating.
- **u/belliash** (↑1, 2026-10-16 18:30): It works, but damn slow. 5 seconds per 1 token for me 😂

---

## I think I’ve been using OpenCode a little too much 💀
**u/Kind-Card-6864** · 2026-10-16 14:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7hq8s/i_think_ive_been_using_opencode_a_little_too_much/)

Checked my OpenCode stats for Jan–Oct 2026 and somehow ended up with **10.3B tokens and 87 active days** 😭

Anyone else checked their stats? I’m curious what your numbers look like 😂

https://i.redd.it/tc612rteauvh1.png

**Comentarios:**

- **u/borobinimbaba** (↑1, 2026-10-16 14:36): Is it on go plan?
  - **u/Kind-Card-6864** (↑1, 2026-10-16 14:39): Yes, it’s on the Go plan combined with the free Zen model.
    - **u/automax** (↑1, 2026-10-17 01:42): what did you build
- **u/OpinionsRWild** (↑1, 2026-10-16 14:47): Workflow and audits are what matter. Not even 30 days in and I’m at 28b tokens. I have 18 days left lol
- **u/ollm-tux** (↑1, 2026-10-16 15:08): https://reddit.com/link/ph4fkcy/video/hm0l6pknhuvh1/player
- **u/Powerful_District_82** (↑1, 2026-10-16 17:02): What models are you guys using?

---

## OpenChamber Data Usage
**u/Yousv** · 2026-10-16 14:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7hiyp/openchamber_data_usage/)

i don't know if i can post about OpenChamber here but i don't find a rule that says that so i will, correct me if i'm wrong.

https://i.redd.it/7wdqc4zl8uvh1.png

I'm using OpenChamber, been doing so for a while but i noticed it just uses ALOT of data and makes my internet terrible while an agent is working on something, is that normal?

while 10GBs don't sound like much, they do to me since i live in Egypt and we have limited internet here.. a shame yes.

i don't know if it's the same with OpenCode's app aswell but well the usage is for the opencode.exe so i guess it has to do with it, if that's normal please let me know and explain why would it even need my internet usage for that because i'm lacking knowledge on that, Thanks.

**Comentarios:**

- **u/xatey93152** (↑2, 2026-10-16 15:04): How can you used so little data? I used 10gb per day when using Openchamber.
  - **u/Yousv** (↑1, 2026-10-16 15:06): i guess that's my internet limit because it genuinely makes it unusable while working 😭
      my internet is so shitty it can't even get anything out of it, do you know the reason for why it even uses that much internet?

---

## why is this coming and when it will reset?
**u/6xiest** · 2026-10-16 14:18 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7hgqq/why_is_this_coming_and_when_it_will_reset/)

https://i.redd.it/62kverxj8uvh1.png

title

**Comentarios:**

- **u/Least_Bodybuilder216** (↑1, 2026-10-16 14:20): Sometimes
  - **u/6xiest** (↑1, 2026-10-16 14:23): like will it be utomatically fixed ?
    - **u/Least_Bodybuilder216** (↑1, 2026-10-16 14:25): Is per-5hours thingies i think
      - **u/6xiest** (↑1, 2026-10-16 14:26): ohh so the rate limit will disappear after 5 hrs or smthng right?
        - **u/Least_Bodybuilder216** (↑1, 2026-10-16 14:34): Yes!

---

## LL Alpha, voxel pagoda test. (Horrid results)
**u/Banneder** · 2026-10-16 13:28 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7g8op/ll_alpha_voxel_pagoda_test_horrid_results/)

https://i.redd.it/sul8630jztvh1.png

The model took 25 minutes to produce a result that was broken and couldn't fix itself after troubleshooting with another model it had this as the output (only small changes done) which is certainly not worth it for the speed, cat jam performed better on this test. I recommend to seriously not use this model.

**Comentarios:**

- **u/DeepFeeling1** (↑1, 2026-10-16 16:55): Can you try cat jam
  - **u/Banneder** (↑1, 2026-10-17 04:47): I already did in another post
    - **u/DeepFeeling1** (↑1, 2026-10-17 04:59): Great, Have you run it for other Popular Models ? OpenAI, Deepseek, Claude etc for comparision ?
      - **u/Banneder** (↑1, 2026-10-17 06:30): If u want i can run it

---

## Five sub-agents in one terminal drove me nuts, so I built a desktop control tower (open source)
**u/Sanchiro__** · 2026-10-16 13:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7frb0/five_subagents_in_one_terminal_drove_me_nuts_so_i/)

[removed]

---

## 1.0M at 500%? What? 😭
**u/CapableHat9609** · 2026-10-16 12:22 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7erri/10m_at_500_what/)

https://i.redd.it/b9gw36iyntvh1.png

**Comentarios:**

- **u/awkard_guy_** (↑1, 2026-10-16 13:59): Someone made a whole ass explanation post in this sub abt v4. 1 flash in free tier. Maybe that'll make sense for you.
  - **u/xx_gamer_xx123321** (↑1, 2026-10-16 14:15): Link?
    - **u/awkard_guy_** (↑1, 2026-10-16 14:23): https://www.reddit.com/r/opencode/s/4YCKZAMSWY
      - **u/xx_gamer_xx123321** (↑1, 2026-10-16 14:25): Thanks 🙏
- **u/GenychDefake** (↑1, 2026-10-17 03:56): What does the "500%" mean?

---

## OpenCode is at its peak
**u/CoffeeTea021** · 2026-10-16 11:08 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7dbzz/opencode_is_at_its_peak/)

**Comentarios:**

- **u/DeepFeeling1** (↑17, 2026-10-16 11:21): Quantised to the peak
  - **u/TheCat001** (↑16, 2026-10-16 12:20): I don't care, compared to my local 35b a3b model Deepseek is insane. It made so much good stuff for me these 2 days. I'm very grateful for Opencode team for such opportunity.
    - **u/Ok-Drawer5245** (↑2, 2026-10-16 15:21): yeah 35b a3b used to be the GOAT for local / hardware poor folks. But with these offerings from opencode I can't even be bothered to launch it. I have a opencode go sub, but im saving it for use on more expensive models now ;D
      - **u/TheCat001** (↑1, 2026-10-16 15:30): Yeah, now when I've seen how good cloud models are, I'm considering buying go sub too. Probably this is whole idea of this free promotions, to get people on the boat :) I just don't how much I could use deepseek v4.1 flash with that 10$ sub, probably not much anyway...
        - **u/Ok-Drawer5245** (↑3, 2026-10-16 15:46): oh you can use deepseek v4.1 flash A LOT with the 10$ sub. In fact I don't have enough time to hit the limits if I stick to deepseek v4.1 flash on the 10$ sub. but of course it really does depend on your use case. You get extremely much right now for 10$ of deepseek v4.1 flash. Having said that right now its free if you can live with 200k context and the usage limits ;-D
          - **u/TheCat001** (↑2, 2026-10-16 15:48): Wow that's nice, then I definitely should sub to a 10$ plan...
  - **u/patricious** (↑22, 2026-10-16 12:34): Its free and you still complain LMAO.
    - **u/Impossible-Lab-3133** (↑-4, 2026-10-16 15:21): Nah I won't touch anything below Opus 5.5 low at this point
      - **u/amo_pessoas_peladas** (↑4, 2026-10-16 16:44): I can see daddy's wallet is very giving.
    - **u/Classic_Raspberry_60** (↑1, 2026-10-16 19:15): it’s free but nvidia nim offers the same thing but better lol
      - **u/LeoVibeCoderz** (↑1, 2026-10-17 04:23): When I use GLM from Nvidia it takes forever to answer and another eternity to deliver. Same for DeepSeek. In my experience Opened is faster
      - **u/mWo12** (↑1, 2026-10-17 05:57): so use it. No sense coming here and complaining.
        - **u/Classic_Raspberry_60** (↑1, 2026-10-17 06:02): i’m not complaining just saying it’s better which it is but whatever you want to use my guy
  - **u/mabuonomo** (↑1, 2026-10-16 14:58): Su reddit c'è chi scrive AI o chi scrive quantizzato 😅
  - **u/Ok-Drawer5245** (↑1, 2026-10-16 15:20): measure it by its quality, who gives a shit about quantization if it delivers the goods?
- **u/keape** (↑1, 2026-10-16 11:37): I can't see that model in the list. You know why?
  - **u/dwky11** (↑1, 2026-10-16 11:38): Set it on first in the manage models tab.
  - **u/casio_340** (↑3, 2026-10-16 11:58): Update opencode
- **u/No-Snow5789** (↑27, 2026-10-16 11:42): if it remains like this im happy
  - **u/One_5549** (↑10, 2026-10-16 13:14): probably wont, but if it at least maintain 5 good models free at all times. Nice
    - **u/Everchann** (↑3, 2026-10-17 00:05): which of them is best for ui/ux?
      - **u/PROPLAYER3X7** (↑1, 2026-10-17 05:21): Glm is best for this
        - **u/One_5549** (↑1, 2026-10-17 12:11): yep, i think that is fair, the other ones are NOT great. but i havent done a lot of ui prompting tbh.
- **u/Tolexx** (↑8, 2026-10-16 11:52): Currently opencode seems to be having issues now during conversations. It abruptly ends with *Rate limit exceeded, try again later*.
  - **u/TheNewHEROBRINEX** (↑2, 2026-10-16 12:00): I can confirm. Same thing happening to me.
- **u/vbllll** (↑11, 2026-10-16 12:05): Could you please fix the paid version? It’s running slowly and keeps freezing.
  - **u/MedyOsef** (↑2, 2026-10-16 16:27): Are you talking to the guys at Anomaly there?
- **u/Metwalley** (↑1, 2026-10-16 12:34): But it's weird though, ds v4.1 flash and them glm 5.3 flash  
    like I'm thankful but it's weird still
  - **u/Dangerous-Air9053** (↑2, 2026-10-16 13:57): The GLM is the 234k context one, not the original 1M context. Not sure about DS.
    - **u/Champion10FC** (↑2, 2026-10-16 16:25): Same for DS
- **u/michaelcharlie8** (↑3, 2026-10-16 12:38): Sorry is this part of go? Or really just free for everyone? That’s nuts
  - **u/lordcohliani** (↑8, 2026-10-16 13:21): Free for everyone. Go subscribers have better rate limits on these models and of course access to other models.
    - **u/xmsxms** (↑0, 2026-10-17 06:09): Go subscribers don't get them for free, it uses quota they paid for. They can use them for free too, but there's no added benefit.
  - **u/Ok-Drawer5245** (↑2, 2026-10-16 15:23): free for every1, I wonder for how long, its wild. remember there are usage limits and a lower context. but still extremely generous
  - **u/zenkov** (↑2, 2026-10-16 19:36): OpenCode's ToS prohibit using free models outside its own harness. This means that users who use OpenCode with their own or third-party harnesses don't have access to free models. In other words, their free models serve as a promotional tool for their own agent harness, rather than simply helping model providers train their models.
- **u/sorklin** (↑0, 2026-10-16 13:03): in the desktop app they're all listed as reasoning off, which really kills the usefulness.
- **u/s0me0ne_s0metime** (↑3, 2026-10-16 13:13): now glm 5.3 flash aswell 🫡
  - **u/Dangerous-Air9053** (↑2, 2026-10-16 13:56): It’s the 200k context one, and not the 1M original.
    - **u/CrowdGoesWildWoooo** (↑5, 2026-10-16 14:27): Free is free. GLM is Anthropic certified known to comply to do stuffs not approved by them
- **u/evia89** (↑1, 2026-10-16 13:26): Not sure what other gets but for me it sucks, slow, low limit
    
    $10 ds direct will get me 1 year of what free allow
- **u/Emotional-Bag-3754** (↑1, 2026-10-16 14:03): modelo LL Alpha ja sumiu LOL MODEL
- **u/xatey93152** (↑1, 2026-10-16 14:23): It's routed to cheaper model. If you know how to check it.
  - **u/Tough-Obligation7386** (↑1, 2026-10-16 15:22): I man, i dont think about it that much, cause, we could argue that for all the provider out there. Anyway, do you know how to check?
- **u/JorgitoEstrella** (↑1, 2026-10-16 14:30): What's the catch?
  - **u/elitegenes** (↑4, 2026-10-16 15:03): They need your data to train their future models on.
    - **u/Champion10FC** (↑1, 2026-10-16 16:24): Not all of them though
    - **u/kalilouisangare** (↑1, 2026-10-16 17:06): Tant qu'il respecte la confidentialité a caractère personnel moi ca me va.
- **u/afcreative_id** (↑2, 2026-10-16 14:41): Comparing with Muse Spark 1.3 Free?
- **u/ThePierrezou** (↑1, 2026-10-16 14:53): There's so much models now, which are the best models on the go sub now ?
  - **u/Ok-Drawer5245** (↑2, 2026-10-16 15:25): the answer is the same it always was: it depends 
      
      for general purpose my standard is deepseek v4.1 flash
- **u/TheMythicSorcerer** (↑5, 2026-10-16 15:03): More free models that total models on openai's paid plans lol
- **u/Strict-Prune-879** (↑1, 2026-10-16 15:17): les ia free sont a 200k de fenêtre et attention au zdr si c'est gratuit c'est vous le produit!!!
  - **u/Champion10FC** (↑1, 2026-10-16 16:24): True, but there are 4 free models with 0 training and zdr per opencode privacy page.
    - **u/Strict-Prune-879** (↑1, 2026-10-16 17:31): il faut jongler et etre attentif a cela peut etre créer un petit script pour ne lance que ceux qui n'ont pas les entrainements?
- **u/Ok-Drawer5245** (↑7, 2026-10-16 15:26): opencode is giving us so much we don't have enough time to use it all
- **u/Manav5234** (↑1, 2026-10-16 15:35): Just stop time now ❤️❤️
- **u/tanvirakon** (↑1, 2026-10-16 16:57): via openrouter...r8?!
- **u/Mihaylov93** (↑1, 2026-10-16 17:35): After seeing all these posts I ran to my opencode but how do you guys get those models? I only have "Free" on what I already had, the mimo, muse and nemotron. I updated opencode and all
  - **u/GamePL7** (↑1, 2026-10-16 18:05): If you use desktop opencode, you have to check settings > models and enable all of them with “free” in their name.
    - **u/Mihaylov93** (↑1, 2026-10-16 18:13): I use the cli but right! I remember such an option on the opencode web when you setup your token, I will check thanks!
- **u/GasSmooth7439** (↑4, 2026-10-16 18:24): The funniest part is that the hardest choice in OpenCode is no longer which model is best. It’s which free model to burn through first.
  - **u/djamp42** (↑1, 2026-10-16 20:33): So what's the deal with these free models because I've been using opencode for the past 3 weeks and have ONLY used free models lol
    - **u/Majoga87** (↑1, 2026-10-16 20:53): not give the data for training out?
      - **u/Lumpy-Obligation-553** (↑1, 2026-10-16 22:38): As in opposite to....?
  - **u/Railander** (↑2, 2026-10-16 22:09): vast majority of those share the same usage.
    - **u/Mr_blue765** (↑1, 2026-10-16 22:50): This is correct. I hit a rate limit and none of them worked after that. And it wasn't a crazy limit. I was abusing muse spark 1.3 before with essentially no limit. Already missing that.
      - **u/automax** (↑1, 2026-10-17 01:41): same
- **u/Mammoth_Jeweler_7414** (↑1, 2026-10-16 18:25): at this point opencode is funded by the Chinese to cause the west some major headaches
  - **u/cdshift** (↑1, 2026-10-17 14:24): The west needs to step up then
- **u/DJubstin** (↑1, 2026-10-16 19:25): They removed Cat Jam Free today... Also I am missing a lot of these free models all of a sudden.
- **u/BlueeWaater** (↑1, 2026-10-16 20:06): How does one enable this? It’s not showing for me
- **u/ornerywolf** (↑1, 2026-10-16 21:43): i think they are training their own model
  - **u/Popular-Factor3553** (↑1, 2026-10-16 23:26): Unlikely
    - **u/TheFrontPageSucks** (↑1, 2026-10-17 02:36): Care to elaborate?
      - **u/Popular-Factor3553** (↑1, 2026-10-17 04:19): They are relatively new yet they'll probably start scaling up or finally hosting models themselves before train their own models.
          
          But yeah all that data they collect from free models is pretty useful to make their own model if they aren't selling it.
- **u/Mask_RF** (↑1, 2026-10-16 21:48): Everything I choose doesn't work for me. Why is that?
- **u/Master_Beast15** (↑1, 2026-10-16 23:40): But I can't use opencode zen API outside of opencode I used it on kilo code too and other projects now I can't
- **u/Entire-Youth-5598** (↑1, 2026-10-17 00:10): Tengo una duda, si gastaba api para precisamente DeepSeek v 4.1 flash , me seguirán cobrando tokens? O hay otra versión paga?
- **u/Outrageous_Toe_3189** (↑1, 2026-10-17 02:37): Muse Spark 1.3 Free is unavailable now ？
  - **u/WizzyTR** (↑1, 2026-10-17 06:36): Yeah its now unavailable to free users.
    - **u/NaZGuL_of_Mordor** (↑1, 2026-10-17 07:46): Go Is Just 9euros monthly...
- **u/4sm0day** (↑1, 2026-10-17 04:30): For real
- **u/PresentArugula6343** (↑1, 2026-10-17 04:53): which of these free models is good for coding task and working with large codebases??
  - **u/SnaFu__o3o** (↑1, 2026-10-17 11:34): Kommt ja drauf an was du machen möchtest. Es kann so ziemlich "alles" eine PAufgabe sein. Longcat und Mimo empfehle ich für das Design
    - **u/PresentArugula6343** (↑1, 2026-10-17 11:39): I usually implement new features in flight controller firmwares and also Android App Development, so which models are good for it.
  - **u/Mundane-Slide7249** (↑1, 2026-10-17 13:43): For me Mimo 2.6.
    - **u/PresentArugula6343** (↑1, 2026-10-17 13:45): I am using Mimo 2.6 Flash and its mind blowing, it works very well on my codebases but I think its only free for 1 week on opencode
      - **u/Mundane-Slide7249** (↑1, 2026-10-17 13:49): I'm use it last 2/3 week
      - **u/AtoRafael** (↑1, 2026-10-17 18:14): what do you mean by for one week
        - **u/PresentArugula6343** (↑1, 2026-10-17 18:16): It means that I can use it for free for 1 week from the initiation date, like if I started using it on a Tuesday, then I can only use it until the next Tuesday and then I have to buy credits for using it.
          - **u/AtoRafael** (↑1, 2026-10-17 18:49): are you on console
            - **u/PresentArugula6343** (↑1, 2026-10-17 18:50): No, I am not
    - **u/AtoRafael** (↑1, 2026-10-17 18:08): 100%, I've been using it since deep seek was removed from the free list
      - **u/PresentArugula6343** (↑1, 2026-10-17 18:17): Same here, I also switched bcz DeepSeek was removed from free list.
- **u/vdvelde_t** (↑1, 2026-10-17 07:07): This chinees free stuff works decent
- **u/zaevlad** (↑1, 2026-10-17 08:09): Still it's hard to keep context lower than 200k if you vibecode
- **u/mapcars** (↑3, 2026-10-17 09:05): Muse was so good while it lasted
- **u/softplus-** (↑1, 2026-10-17 09:44): It was already free for all intents and purposes.
- **u/Specialist-Donut6948** (↑1, 2026-10-17 10:13): GLM 5.3 Flash replaced Muse i guess
- **u/SnaFu__o3o** (↑1, 2026-10-17 11:33): Hä bei Code oder Zen???
- **u/parthibx24** (↑1, 2026-10-17 11:59): is it 1017?
- **u/funmolde** (↑1, 2026-10-17 15:02): 😊Opencode free is great , bye bye chatgpt plus🥱
- **u/nuestras** (↑1, 2026-10-17 15:17): Where can i get this? Please 🙏
- **u/luisfernandez95** (↑1, 2026-10-17 16:03): Esta bueno me puse a hacer jueguitos retro xd
- **u/manuhackzzz** (↑1, 2026-10-17 16:37): 200B models Bois.  We need true 1M
    If you have paid memberships with Claude  I would advise not to cancel anytime soon.
- **u/Fearless_Bite_3041** (↑1, 2026-10-17 17:16): I've been using it for a little while now and I'm really impressed.
- **u/zhbchn** (↑1, 2026-10-17 18:39): Is it free for everyone?
- **u/Electrical_Bit4031** (↑1, 2026-10-16 15:57): delete so they don’t find out
  - **u/d3ku100** (↑1, 2026-10-16 16:15): Find out ? I don't see it working too rate limited, i wanted to check it. Hopefully someone let's me know if a secret I'm missing
    - **u/EnoughConcentrate897** (↑1, 2026-10-17 02:41): there's no secret it's just they were commenting about how they're spoiled by opencode and we can't say that (it's not true) because then they'll lower usage limits
  - **u/imelu** (↑1, 2026-10-16 16:53): Hit with a dm?
  - **u/Powerful_District_82** (↑1, 2026-10-16 17:05): Bro what was it?
  - **u/MaleficentOwl3240** (↑1, 2026-10-16 17:33): what did ya ask to delete, please tell me too

---

## Still Cheapseek 4.1 the best for cheap ai vibe coding / large projects?
**u/SuperGround1068** · 2026-10-16 11:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7d90j/still_cheapseek_41_the_best_for_cheap_ai_vibe/)

**Comentarios:**

- **u/patricious** (↑1, 2026-10-16 12:41): DS V4.1 Flash can be used for any project no matter small or big. It's goated.
- **u/Mementem** (↑1, 2026-10-16 17:57): it is really really good, but on the free tier there is a 200k context limit.

---

## Topup Opencode Zen or OpenRouter better?
**u/TermBudget8901** · 2026-10-16 10:49 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7czfm/topup_opencode_zen_or_openrouter_better/)

I wanna topup balance in case OpenCode Go maxed out. I havent tried out the plus plan but some models that I want are a bit limited. I tried space bunny, I like cuz it's fast and efficient. Curently using spacebunny free for bigger task and also muse spark 1.3 contributor for daily task as it's cheaper.   
  
Space bunny consumed the usage quite fast. Checked on their official site, seems to be using credit based balance which i dont like as it's unpredictable on how the credits will be consumed.   
  
For balance based im considering zen or openrouter so i dont have to manage the provider api separately and these two often have discounts or free as well. 

What's your thought?

---

## You can also use arena models in opencode
**u/ScheduleDismal7463** · 2026-10-16 10:04 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7c7ws/you_can_also_use_arena_models_in_opencode/)

[removed]

---

## anyone facing this issue
**u/Direct_Opposite4602** · 2026-10-16 09:46 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7bx3j/anyone_facing_this_issue/)

**Comentarios:**

- **u/Mementem** (↑1, 2026-10-16 17:58): all the free models share a limit, you most likely ran out of the 5hour/daily limit. wait some time and try using it again it will most likely work tomorrow

---

## Opencode removed A MALWARE
**u/VibeCoder6000** · 2026-10-16 09:44 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7bw03/opencode_removed_a_malware/)

[removed]

---

## Free Model Tier List
**u/NiloyTheSPD** · 2026-10-16 08:57 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7b55z/free_model_tier_list/)

https://i.redd.it/7uanvxdcnsvh1.png

what are the top 5 models from here?

**Comentarios:**

- **u/Railander** (↑3, 2026-10-16 09:19): from my experience, in no particular order, these are the best models:
    
    * GLM 5.3 flash
    * deepseek 4.1 flash
    * muse spark 1.3
- **u/ComplexMaja69** (↑3, 2026-10-16 09:58): muse spark 1.3 xhigh is the best one i've tried so far, context length at 1M is kinda carrying it but still. It's fast + smart and def better than gemini 3.8 flash high on agy lol
  - **u/kuriousaboutanything** (↑2, 2026-10-17 03:28): isn't muse spark gone from free tier?
- **u/FrostGoesBrrrt** (↑1, 2026-10-16 14:11): Muse Spark 1.3 is the most capable model but not ZDR and terrible at frontend tasks. But code quality is really good.
- **u/isus_copilul_minune** (↑1, 2026-10-16 15:04): For me:   
     deepseek 4.1 flash   
     GLM 5.3 flash  
     muse spark 1.3
- **u/Champion10FC** (↑1, 2026-10-16 23:19): How were you able to filter the list to free models only?
  - **u/O0ddity** (↑1, 2026-10-17 08:57): Maybe a little javascript into the developer-tools inspector, like so  
      \`\`\`js  
      document.querySelectorAll('tbody.console-reveal > tr').forEach(row => {
      
        const isFree = Array.from(row.querySelectorAll('span')).some(s => s.textContent.trim() === 'Free');
      
        if (!isFree) row.style.display = 'none';  
      });
      
      \`\`\`
  - **u/NiloyTheSPD** (↑1, 2026-10-17 13:45): from opencode website bro

---

## Planner/executor workflows with multiple models: does splitting actually save anything?
**u/spiritualManager5** · 2026-10-16 08:37 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x7auon/plannerexecutor_workflows_with_multiple_models/)

Yesterday I tried building a multi-model coding workflow in OpenCode for the first time. The idea: a strong model plans, a cheaper model (or a local one) implements.

In practice, I had to use Opus 5.5 in plan mode just to find the bug. Once it was found, the fix was a few lines, so handing it off to a smaller model saved basically nothing.

That got me thinking about a more general problem. For the cheap model to implement reliably, the plan has to be very precise: exact files, exact locations, often example code. But at that point the big model has already done the real work and could just write the code itself. The handoff seems to add cost (lost context, retries, review) instead of saving it.

My questions:

1. Does anyone actually see real savings from planner/executor setups? If so, for what kind of tasks? My guess is repetitive, large-scale work (same pattern across many files, migrations, fixing tests and lint errors), but not normal day-to-day bugs and features.
2. For those of you with 32GB+ GPUs: what do you actually run locally? Even 70B models are far from frontier quality, so I'm curious what your real use cases are. Privacy, autocomplete, image generation, fine-tuning, something else?

Or is the honest answer just to stick with the big model from start to finish for anything non-trivial?

**Comentarios:**

- **u/torrso** (↑3, 2026-10-16 09:25): From what I've seen that kind of setup is good at giving the impression of it working. You have small models nibbling at the corners for weeks, the big model happily orchestrates them. 
    
    At some point you find yourself with a mess that is getting messier and the things you wanted seem to never materialize.
    
    Turns out, when that big brain model made the plan, it could have just as well gone in and implemented it.
    
    Codex/Claude will one-shot something that you were struggling to complete with the "smart planner dumb worker" setup and the result is better. 
    
    My claim is that you will get more and better things done by ditching your elaborate obsidian neural cortex memory and multi-agent roleplay on budget models and just going with stock claude or codex. Their $20 plans are much better value than the $10 OCGO plan or any of the local models you can run on reasonable hardware.
  - **u/damn_pastor** (↑2, 2026-10-16 13:54): This is the hard truth
- **u/Nenad1979** (↑1, 2026-10-16 10:28): In my expirinace eoth newer models no, just let them work
- **u/weiyentan** (↑1, 2026-10-16 11:29): Actually it depends. For small bugs fine. But try doing multiple issues setups. I have been using multi orchestrator for months. We can do more efficiently because of context windows. I can do a number of issues in one go. I tier my agents. And before any work starts I have a task router that determines what type of agent to use and puts a safety net. I use deepseek flash for senior and it goes down from there in model strength. I have been getting quite good accuracy. Some. People will say that it costs a ton because of all the tokens used. . Well I have a tool to measure that too. With all my tokens 1.6 billion used the usage of my spend in the subscription is approx 26$ of what 80?  This is including review. I am largely hands off nowadays. I have a blog posts about how I run things if you are interested
  - **u/spiritualManager5** (↑1, 2026-10-16 11:38): Sure, interested
    - **u/weiyentan** (↑1, 2026-10-16 11:40): http://weiyentan.github.io/2026/ai-coding-frameworks/
        
        http://weiyentan.github.io/2026/how-my-afk-engineering-workflow-actually-works/
    - **u/weiyentan** (↑1, 2026-10-16 11:52): Happy to answer further questions
- **u/Fresh_Sock8660** (↑2, 2026-10-16 11:30): In my setup, I don't hand off small tasks. The orchestrator writes a contract in slices and hands off each slice to the implementator. I'm finding that this setup costs me substantially less claude usage and gets me an extra review of each slice. The orchestrator also acts as the implementator for some types of tasks. 
    
    "For the cheap model to implement reliably, the plan has to be very precise..."
    
    Depends entirely what your cheap model is: ds4.1f is what I'd consider cheap and it doesn't need precise instructions.
  - **u/weiyentan** (↑2, 2026-10-16 11:56): I do something similar. Although I divvy up the slices as issues up front. I do a bit of interactive work with agents with Matt pocock’s skills to do that. But after that it’s pretty much hands off. I actually have proper review loops too. It’s quite cool
- **u/lordcohliani** (↑1, 2026-10-16 13:24): Go to YouTube and look up the many many comparisons of this. It turns out it's just always worse.
  - **u/spiritualManager5** (↑1, 2026-10-16 13:38): I am non-stop on YouTube in my free time
- **u/HighwayNo8744** (↑1, 2026-10-16 14:27): ask opus what the issue it. it's similar to haiku subagents which are sometimes cheaper and sometimes not. if opus has to read 4000 tokens from the research agent to pass a reviewed and refined report with another 2000 tokens to the implementer then you are saving nothing and you dont need opus for that. these agents only have to generate a brief and only the next agent should get the full report.
- **u/bluesockdrawer** (↑1, 2026-10-16 15:30): I think the real savings come from parallel, repetitive work rather than splitting ever task. If the planned has to explain every tiny detail, you might as well let the stronger model finish the job.
- **u/LordMoridin84** (↑1, 2026-10-16 18:25): What do you mean by smaller models? Deepseek flash v4.1 is smarter than Claude Opus 4.6, which was the smartest of models at the start of the year.
    
    Do you believe that the work you are doing is too complicated for what was the smartest model in the world?
    
    For a subagent workflows. You simple tell Opus 5.5 to delegate any medium/long running tasks to subagents. So anything over 30mins-60mins 
    
    e.g.
    
        Prefer single long running subagents over multiple smaller subagents because it's more expensive to load up twice the context. This is a preference, some workflows/skills specificially use multiple subagents, such as some code review workflows or when implementing multiple wayfinder tickets at once.
  - **u/xapep** (↑1, 2026-10-17 06:22): The context-reload point decides the math. A handoff only pays when the executor starts from a warm prefix. If the subagent re-reads the project context from scratch, you're not splitting cost, you're paying it twice.  
        
      That's also where the flash-class executor argument lands. From the provider side (I run an EU-hosted inference API) the split makes money on repetitive medium tasks with a stable context, and loses it the moment the plan gets fuzzy and the executor starts retrying, because every retry re-reads the same context.  
        
      So I'd add one rule to yours: pin exact files and shapes in the plan, then one long-running subagent with a backlog of similar tasks beats several short ones. The model class matters less than whether the context stayed warm. Do you track cache-hit rate on your subagent runs? That's the number that decides whether the split actually saves.
- **u/Due-Alfalfa2265** (↑1, 2026-10-17 03:28): I've run into this with Codex and OpenCode too. For small fixes, I usually wouldn't split the work. Multi-model workflows make more sense to me for larger, well-scoped tasks where implementation and review can be separated. The handoff overhead is real.

---

## What this new model in opencode "LL alpha"
**u/XDSORITE** · 2026-10-16 07:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x79vn5/what_this_new_model_in_opencode_ll_alpha/)

I have not found any information about this online.

https://i.redd.it/4dfdgm9r8svh1.png

**Comentarios:**

- **u/xx_gamer_xx123321** (↑3, 2026-10-16 07:41): Qwen30193938 preview
  - **u/XDSORITE** (↑1, 2026-10-16 07:42): How can you tell?
    - **u/xx_gamer_xx123321** (↑4, 2026-10-16 07:43): I benchmarked it and it got 101% on deepswe v5.01
      - **u/XDSORITE** (↑0, 2026-10-16 07:44): Why is their no info about it anywhere did it just release
        - **u/xx_gamer_xx123321** (↑3, 2026-10-16 07:45): Brother i am joking qwen4 is still in preview dont expect qwen30193938 to be releasing anytime soon. Also there is not deepswe v5.01
          - **u/XDSORITE** (↑2, 2026-10-16 08:23): Damn fell for that thanks for at least telling me
        - **u/AmuletOfNight** (↑1, 2026-10-16 15:48): Bro you're being gaslit lol
  - **u/arielif1** (↑3, 2026-10-16 14:07): dude i was wondering how the fuck that date was formatted lol
- **u/Emotional-Bag-3754** (↑1, 2026-10-16 08:25): LOL model
- **u/Academic-Sentence-34** (↑1, 2026-10-16 08:44): Lelouch lamperougeee model!
- **u/QuietPsychonaut** (↑2, 2026-10-16 12:49): Hey OP, models with weird names like LL Alpha are basically secret models that OpenCode tests publicly in partnership with their providers before an official release.
    
    We've seen this before with models that initially appeared under mysterious names and were later revealed to be something like GLM 5.3 Flash.
    
    It's essentially a way for OpenCode and model providers to test upcoming models with real users before officially announcing them.
  - **u/Solocune** (↑2, 2026-10-16 16:00): Yea no shit. But often the community is smart enough to deduce which model it is by certain parameters. Or at least know from whom it comes.
    - **u/XDSORITE** (↑1, 2026-10-16 16:18): Perfect reply
    - **u/BackgroundSeat9816** (↑1, 2026-10-16 20:37): Usually based on the tokenizer comparison, if I had to guess, this could be the next kimi, taking on count they started training about 1.5months ago, and the model is HELLA slow.
- **u/jehuty997** (↑1, 2026-10-16 13:06): I just got this message while using this model
    
    `⚠ Retry due · attempt 2 · OpenAI Chat stream ended without finish_reason`
    
    `General · LL Alpha Free · 1m 19s · 1.5 tok/s`
    
    OpenAI?
  - **u/RainyDayFeel** (↑1, 2026-10-16 13:41): That just means the model is using OpenAI Completions API loads of companies use it.
  - **u/TheMythicSorcerer** (↑1, 2026-10-16 15:06): No just openai compatible every model is openai compatible it's just the endpoint it means nothing
- **u/Huge_Business2428** (↑1, 2026-10-16 14:03): I have no idea which model it is, but someone posted a benchmark and it seems to be a terrible model lmao
- **u/iit_aim** (↑1, 2026-10-16 17:33): it's Kimi, i simply asked it.
- **u/iamchuckschuldiner** (↑1, 2026-10-16 18:52): glm 666
- **u/SelectSouth2582** (↑1, 2026-10-16 19:05): It's "Flint" by "Recursive Superintelligence"

---

## Does Opencode Desktop uses v2?
**u/Infamous_Trade** · 2026-10-16 07:15 UTC · ↑3 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x79kyl/does_opencode_desktop_uses_v2/)

I'm curious, since my opencode desktop version is still 1.19.2 and docs didn't explain anything about v2 for desktop.

**Comentarios:**

- **u/seeKAYx** (↑1, 2026-10-16 08:33): Yes. I use V2 with the Desktop version.
- **u/Railander** (↑1, 2026-10-16 09:24): you can upgrade it to v2. it even auto upgrades the WSL server (if you're using that). just download v2 for desktop and install, it will update itself gracefully.
  - **u/Infamous_Trade** (↑1, 2026-10-16 09:31): how, by downloading the file in github releases? or from the official website? the filename of the desktop doesn't differentiate between v1 and v2.
    - **u/Railander** (↑1, 2026-10-16 09:33): brother just download from website for your OS, then install.
        
        [https://opencode.ai/download](https://opencode.ai/download)
        
        this page is all v2, in case you couldn't tell by the v2 explicity CLI commands.

---

## GLM 5.3 Flash is available for FREE
**u/CoffeeTea021** · 2026-10-16 07:14 UTC · ↑26 · 7 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x79k33/glm_53_flash_is_available_for_free/)

GLM 5.3 Flash Free is now available for free on OpenCode. The website states that it follows a zero-retention policy and does not use user data for model training, just like DeepSeek V4.1 Flash Free, which was made available for free on OpenCode yesterday.

**Comentarios:**

- **u/sk1kn1ght** (↑1, 2026-10-16 08:20): Ds4.1 for sure yesterday mentioned nothing about zdr. Where did you see that
- **u/underlight** (↑1, 2026-10-16 13:20): sadly seems like it's 200k context, just like free ds4.1
  - **u/International_Try850** (↑1, 2026-10-16 14:28): my experience auto-compacting just below 200k works well enough
    - **u/underlight** (↑1, 2026-10-16 14:37): I'm sure it's perfect for majority of people, my context is around 400-600k so this doesn't cut it.
- **u/Mementem** (↑1, 2026-10-16 19:03): does it have data retention? i cannot find the data retention policy for this
  - **u/CoffeeTea021** (↑1, 2026-10-17 04:23): You can check the OpenCode models documentation

---

## GLM 5.3 Flash est GRATUIT
**u/Strict-Prune-879** · 2026-10-16 07:10 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x79hs7/glm_53_flash_est_gratuit/)

---

## Novos modelos gratuitos no OpenCode
**u/Mediocre-Outcome5375** · 2026-10-16 07:07 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x79fr3/novos_modelos_gratuitos_no_opencode/)

GLM 5.3 Flash no opencode e um novo modelo "LL Alpha" stealth?

---

## 🔥 GLM 5.3 Flash is FREE in OpenCode
**u/afanasenka** · 2026-10-16 06:57 UTC · ↑804 · 159 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x799zh/glm_53_flash_is_free_in_opencode/)

Crazy things are happening :))))

**Comentarios:**

- **u/Total-Management8023** (↑26, 2026-10-16 06:59): Damn. How do they afford this?
  - **u/anitamaxwynnn69** (↑24, 2026-10-16 07:01): I'm not sure what their data retention policy is but I presume providers want data maybe that's how?
    - **u/UnknownBoyGamer** (↑5, 2026-10-16 07:14): on dax tweet he said he doesn't sell data
      - **u/anitamaxwynnn69** (↑6, 2026-10-16 07:17): Oh. But doesn't this depend on the backed provider who's hosting the mode? Also does that mean opencode still uses it but doesn't sell? I'm asking out of curiosity no hate towards dax/opencode.
        - **u/SorosAhaverom** (↑1, 2026-10-16 10:44): ZDR is a pinky promise that is impossible to disprove. OpenCode doesn't even publish the inference providers for their models. No serious company requiring regulatory or contractual ZDR would ever consider OpenCode's router.
      - **u/Impossible-Lab-3133** (↑0, 2026-10-16 09:24): He doesn't but his provider does
    - **u/qqYn7PIE57zkf6kn** (↑21, 2026-10-16 08:11): https://opencode.ai/v2/docs/console/models#free-models
        
        > GLM-5.3-Flash Free is free on OpenCode for a limited time. Its provider follows a zero-retention policy and does not use your data for model training.
      - **u/anitamaxwynnn69** (↑3, 2026-10-16 08:14): Appreciate you adding this. Dax is goated.
      - **u/Embarrassed_OnionX** (↑4, 2026-10-16 10:54): Why would they provide free inference tho? ZDR pinky promise?
        - **u/Ceextasy** (↑5, 2026-10-16 11:03): The most reasonable explanation to me would be load testing aka to see how the server responds to a huge request load. Since its free, you know theres going to be hundreds of thousands of requests if not millions.
          - **u/Embarrassed_OnionX** (↑2, 2026-10-16 11:06): Good point, didn't think about that
          - **u/bankinu** (↑2, 2026-10-16 12:20): Also to create affinity and awareness. 
              
              I used a model which many people hate. But I am now considering to subscribe to it. It's good.
            - **u/Ceextasy** (↑1, 2026-10-16 12:33): Well, which model?😭😭 But what exactly do you mean with affinity and awareness? I dont quite understand. To make the AIs answers more refined or... more aware of what?
              - **u/bankinu** (↑2, 2026-10-16 12:37): Affinity = you use the free model and you see good results, you start liking it
                  
                  Awareness = you didn't know about this model and what it can do, because it's free you try it and are now aware
                  
                  In both cases negative experiences can also occur, but it doesn't matter, because even if 1% of people tend to like it then at least they will be new potential customers.
                  
                  The model I liked is Muse Spark 1.3. For my open source code, since they only offer contributor license with Zen and you don't want it to read private repo or sensitive information.
                - **u/Ceextasy** (↑1, 2026-10-16 12:41): Ahhh awareness i know what you mean. I thought you meant the AI gets some sort of awareness from the users prompts, making it better. Either way, thanks for explaining. Also yes i absolutely agree, muse spark 1.3 is an amazing model, for me atleast. Yes ive had some rough moments with it, but i have recently been using a preset for all my prompts, and this works exceptionally well. The issue wasnt the model, it was my prompts.
                - **u/Ceextasy** (↑1, 2026-10-17 08:51): In case you didnt notice yet, muse spark 1.3 free is gone. I am absolutely heartbroken.
                  - **u/bankinu** (↑2, 2026-10-17 14:13): Yes. I don't think GLM 5.3 is a good replacement.
                      
                      Commented here, [https://www.reddit.com/r/opencode/comments/1x7vnzm/comment/phb3738/](https://www.reddit.com/r/opencode/comments/1x7vnzm/comment/phb3738/)
                      
                      But can't complain. They provided it for free.
                    - **u/Ceextasy** (↑1, 2026-10-17 14:22): absolutely agree with you. im trying to get along with space bunny now. its an okayish model. I cannot use models with less than 1M context for the sake of my mental health. Absolutely cannot.
          - **u/True_Consequence_681** (↑1, 2026-10-16 13:52): thousands is insanely conservative individual users(me) can get upto 3-4k a day almost its definitely tens if not hundreds of millions
            - **u/Ceextasy** (↑1, 2026-10-16 22:02): I'm talking about concurrent load.
  - **u/squirrelscrush** (↑5, 2026-10-16 07:30): It's probably some providers that give them some compute for it lol, probably for load balance testing or something. Even if you don't collect the training data, it can be needed for server-side stuff.
      
      Or it's a way to get new users by providing free models at 200K context and then they get a Go/Zen subscription.
  - **u/Tech-Sapien18** (↑1, 2026-10-16 07:30): My observation is when they are about to release their next model, they do this.
    - **u/Total-Management8023** (↑1, 2026-10-16 07:32): Glm 5.5 ? Really excited for that one
  - **u/billionarguments** (↑3, 2026-10-16 07:47): From what I understand the usage is severely limited. A few prompts and then you get paused of throttled. Also, it's slow.
      
      It sounds to me this is bait to get people on the tool. But don't get me wrong, I like opencode. I love the fact that the harness-, model- and AI community is sprawling with competition right now.
    - **u/Ceextasy** (↑3, 2026-10-16 07:53): for specific models or generally? I have used the SH\*T out of muse spark 1.3. Its an extremely capable model if you know how to instruct it right.
      - **u/lcy0x1** (↑1, 2026-10-16 09:10): for GLM only
        - **u/Ceextasy** (↑2, 2026-10-16 11:01): Ah okay. Well i havent tested it yet so i wouldnt know. But with muse spark 1.3 i had days where i sent about 20-30 prompts an hour for 5-6 hours straight and i did not reach any RPD limits. Only once in my entire life did i hit a request limit. But if GLMs models have stricter limits i dont think theyre good for my workflow.
      - **u/billionarguments** (↑1, 2026-10-16 10:50): I guess it differs. I'll give it a whirl.
  - **u/AdamovicM** (↑0, 2026-10-16 07:56): probably trying to get people on board, but I believe its flawed business logic
    - **u/PatagonianCowboy** (↑4, 2026-10-16 07:57): how do you know, have you seen the numbers?
  - **u/jjonj** (↑1, 2026-10-16 10:04): how can they afford generating training data?if they couldn't how would they function at all
- **u/allehS** (↑12, 2026-10-16 07:00): what
- **u/HYBAS22** (↑2, 2026-10-16 07:01): How
- **u/HotLion7** (↑2, 2026-10-16 07:01): That's suspicious
  - **u/Thomas-Lore** (↑2, 2026-10-16 07:13): As long as you don't feed it api keys...
    - **u/LIll_Snow5826** (↑1, 2026-10-16 08:11): they filter out such information with Privacy Filter models
- **u/gregthecoolguy** (↑3, 2026-10-16 07:04): Context window?
- **u/StillShoe6361** (↑3, 2026-10-16 07:04): GLM 5.4F IS COMING
- **u/ExTraveler** (↑14, 2026-10-16 07:05): Desperate for trainig data
  - **u/MountainousPondering** (↑9, 2026-10-16 07:07): Since Anthropic tackled distillation - interesting timing here indeed.
  - **u/mWo12** (↑4, 2026-10-16 08:27): It is ZDR. So which data?
    - **u/MountainousPondering** (↑12, 2026-10-16 09:07): Considering Z.ai was uploading entire repos to their servers and were caught doing it, I don’t think you can trust anything.
        
        Open code says ZDR, but you’re also relying on the underlying provider actually doing what they say they’ll do as well.
        
        Basically, if Mark Zuckerberg turned round and said, don’t worry bro, we ZDR - would you blindly trust that statement?
        
        TL;DR - I don’t think you can believe anything these providers, model creators claim.
        
        That includes the likes of Anthropic as well.
        
        If something that actually costs the provider significant chunks of money, and they’re offering it for free, you are the product.
      - **u/Railander** (↑2, 2026-10-16 09:12): ironic that you say "that includes the likes of anthropic" when them and openAI are the 2 companies i'd least trust to be honest about anything.
        - **u/MountainousPondering** (↑3, 2026-10-16 09:29): You’ve misunderstood.
            
            That statement is me saying that Anthropic and the like, are also included in my distrust.
            
            The below statement means Anthropic (and the likes of (I.e. peers like OpenAI)) are also included in the above TLDR statement.
            
            *TL;DR - I don’t think you can believe anything these providers, model creators claim.*
            
            *That includes the likes of Anthropic as well*.
- **u/Icy-Examination-9512** (↑19, 2026-10-16 07:07): "Please Please Please Mr.President we're winning too much we can't take it anymore, that's too much winning!"
- **u/Strict-Prune-879** (↑2, 2026-10-16 07:08): le seul problème n'est pas qu'il soit gratuit c'est super mais parle t'on du zdr?
- **u/IlNaka** (↑23, 2026-10-16 07:09): Yes, 200K context also as DeepSeek V4.1-Flash instead of 1M
  - **u/NoMatterWhaa** (↑3, 2026-10-16 07:11): which one is better?
    - **u/Thomas-Lore** (↑10, 2026-10-16 07:14): Test them on your code, both have strengths and weaknesses.
    - **u/Square-Composer-6719** (↑12, 2026-10-16 07:20): In my experience dsv4.1 flash was multitudes better in agentic coding and some creative work like brainstorming from massive context.
      - **u/Ok-Drawer5245** (↑3, 2026-10-16 10:48): dsv4.1 flash is very good, but I've seen many examples where glm 5.3 flash could fix very complex and difficult bugs easily that dsv4.1 flash got stuck on and couldn't fix. glm 5.3 is definitely better in raw intelligence/complex problem solving
      - **u/fucking_h** (↑2, 2026-10-16 14:32): Glm 5.3 flash is way more intelligent though. If you have a plan for what you want to do, dsv4.1 is better for actually implementing it. But for complex works, 5.3 Flash seems to reason and plan better. I'm using 5.3 Flash to plan things, and dsv4.1 to build, and it's working out great
    - **u/IlNaka** (↑2, 2026-10-16 07:24): For my work stack (a video game price comparison site and game hub), both are useful, but not with a 200K cap.
      - **u/squirrelscrush** (↑2, 2026-10-16 07:32): It can probably be resolved by having an orchestrator-subagent pipeline, so that each sub-session gets its own cap.
    - **u/squirrelscrush** (↑1, 2026-10-16 07:32): GLM feels highly quantized and slow.
    - **u/that_90s_guy** (↑1, 2026-10-16 09:49): Deepseek V4.1 is smarter but also behaves somewhat schizophrenic at times and hallucinates more. I think GLM 5.3 Flash is dumber but more predictable and stable
  - **u/outofindustry** (↑4, 2026-10-16 07:24): I forced it to 1M in my opencode go sub and so far haven't hit a problem. but fingers crossed, they really returned 200k for the context length wtf.
    - **u/IlNaka** (↑1, 2026-10-16 08:24): Good idea
      - **u/outofindustry** (↑2, 2026-10-16 08:41): after a thorough reading, mine works cause it's a paid sub (opencode-go), the free one still caps at 200k token length 👀
        - **u/GoldPossession7284** (↑1, 2026-10-16 15:00): na verdade apenas está definido nas variaveis de ambiente, que nem o deepseek 4.1, o deepseek suporta 1 milhão, esse glm o maximo que eu consegui foi 920k de tokens no maximo. ou seja os 200k foi setado somente no opencode, não é uma restrição no beckend
  - **u/Ok-Drawer5245** (↑13, 2026-10-16 10:46): 200k context is not that bad, keep your codebase clean and well organized, I can still make it work and my codebase is quite very big now
  - **u/ApprehensiveDelay238** (↑1, 2026-10-16 14:38): I limit my DeepSeek to 300k anyways to avoid context rot. It's also way cheaper than running it to 1M.
- **u/sirloindenial** (↑3, 2026-10-16 07:10): Amazing timing as i almost paid for opencode go but now probably no need😂
  - **u/mWo12** (↑2, 2026-10-16 08:28): As paid user you will have 1m context. As free, 200k.
    - **u/truecrisis** (↑1, 2026-10-16 09:17): Paid user, how does it determine? Opencode go subscribers = paid user?
        
        Or do you need to pass a valid opencode zen api key?
      - **u/fucking_h** (↑1, 2026-10-16 14:35): Opencode go. So using the limits of the go plan. The free model's limits do not increase
- **u/Emotional-Bag-3754** (↑5, 2026-10-16 07:11): Mais rapido que eu
- **u/synaps33** (↑2, 2026-10-16 07:12): i have upstream request failed when i want to use that :/
- **u/TinyDetective110** (↑2, 2026-10-16 07:14): new glm flash is coming
- **u/enigmaticy** (↑5, 2026-10-16 07:14): GLM 5.3 Flash Vs DS V4.1 Flash
- **u/xx_gamer_xx123321** (↑7, 2026-10-16 07:15): 0.0001 bit quant
  - **u/Impossible-Lab-3133** (↑1, 2026-10-16 09:26): Is that even possible?
    - **u/xx_gamer_xx123321** (↑3, 2026-10-16 10:31): Anything is possible to reduce cost
- **u/Unique-Dark9726** (↑2, 2026-10-16 07:15): These "free" models are for harness usage right? Can it be used with API?
  - **u/PlateletsAtWork** (↑1, 2026-10-16 07:25): Yup
  - **u/Amarsir** (↑1, 2026-10-16 09:08): Yeah, only in the Opencode harness. It will error if you try it from another one.
    - **u/IAmFitzRoy** (↑2, 2026-10-16 16:29): Asking for a friend, if you change the header as if it’s coming from OpenCode harness.. is that enough for it to work? Or is more to it?
      - **u/j0s3f** (↑0, 2026-10-16 18:24): it works but maybe they ban you, who knows.
        - **u/IAmFitzRoy** (↑1, 2026-10-16 21:43): You can use them without account.
      - **u/nuelgoeshard** (↑0, 2026-10-16 20:36): no i've tried, the cli and desktop app binaries are signed with an identifier zen requests
        - **u/IAmFitzRoy** (↑1, 2026-10-16 21:44): You can use them without account… I have integrated it to my website just a few minutes ago. So yes it can be done.
          - **u/nuelgoeshard** (↑1, 2026-10-17 14:10): proof?, any tips to help?
- **u/arthax33** (↑2, 2026-10-16 07:16): Can someone explain something for me?  
    Is that model really free or i need to pay for zen go?  
    How do i access it?  
    Is that limited in some way? Or it should have performance like PAYG model?  
      
    thanks
  - **u/impostorsyndrome10** (↑3, 2026-10-16 08:18): Opencode Zen is pay-as-you-go (no need for a subscription). Under Zen there are paid models and free models, specifically named "free". You can use them without any issues. Just install opencode and you're good to go
  - **u/Amarsir** (↑1, 2026-10-16 09:04): Get yourself a Zen key and use it in Opencode. No payment required.
    - **u/arthax33** (↑1, 2026-10-16 11:29): Okay normally i use opencode app + openrouter glm 5.3 flash PAYG.  
        dont ask why.  
        so now i can connect opencode app + opencode and use free 5.3 flash?  
        and it should be the same good? and i wont feel any difference   
        (im not using much typically max 3$ daily)
  - **u/daniel-sousa-me** (↑1, 2026-10-16 13:43): It's free without paying anything, or even having to create any account 
      
      But going by their other offers, you're probably limited to 1000 requests per day (which quickly drops to 500) per IP, and all free models share the same cap. Each tool call counts as a separate request
    - **u/IAmFitzRoy** (↑1, 2026-10-16 16:24): Don’t you need an account to log in and get the API Key?
      - **u/daniel-sousa-me** (↑1, 2026-10-16 18:13): No. Just install it, select the model, and write the prompt 
          
          There's no way to use it for free with an API key. You can only use it on opencode 
          
          (Maybe you were thinking of openrouter?)
- **u/FlyingTwentyFour** (↑4, 2026-10-16 07:28): jesus christ. I'll be agentic coding for free for a while
  - **u/sashko5** (↑1, 2026-10-16 10:32): Not if we trash the endpoint with a gazillion requests :)
    - **u/Ok-Drawer5245** (↑1, 2026-10-16 10:53): that is a common problem when something is free
- **u/Meandernder** (↑1, 2026-10-16 07:32): Doesnt mimo 2.6 flash blow them all out of the water according to llm arena?
  - **u/Quad_Plex** (↑3, 2026-10-16 07:34): According to llmarena the Easter rabbit might as well be real lol, if you try to use mimo 2.6 on a difficult, not learned task it breaks down like a house of cards
    - **u/SorosAhaverom** (↑1, 2026-10-16 10:44): It's also slow as shit, 20-30 tok/s.
  - **u/Amarsir** (↑1, 2026-10-16 09:03): I think it's good to get rankings from a variety of different sources. But the fact that Code Arena ranks Flash higher than Pro is crazy. 
      
      I'd say Mimo 2.6 Flash is in the mix with Luna, Haiku, DS Flash, GLM Flash, Qwen Flash Next, Muse Spark, and Space Bunny. So if someone likes one of those more for their work that's totally reasonable. Personally for me it's way too slow. (Which is a shame, because I liked 2.5.)
  - **u/Railander** (↑1, 2026-10-16 09:15): i've tried all the free/cheap models available in opencode and the only 3 that don't feel straight up stupid are glm-5.3-flash, ds-4.1-flash, spark-1.3
    - **u/zeta_cartel_CFO** (↑2, 2026-10-16 23:30): yeah, they just removed spark 1.3, the free model version. For once I disappointed. It was actually a decent model.  Of course Meta made it clear that it was free because they wanted to retain data (hence the 'contribute' in the name). I didn't care, since I only used it for MCP calling.
  - **u/excellentforcongress** (↑1, 2026-10-16 17:29): mimo has spiky intelligence, so it is very good at what they focused training on, but they probably overtrained on it. someone like glm flash is more all around intelligent.
  - **u/ByteHavenGames** (↑1, 2026-10-16 18:37): mimo completely failed in my testing - gets stuck in endless loops blowing tokens or stops working entirely.  Perhaps it's better in their native harness but I'm not interested.
- **u/zer0evolution** (↑1, 2026-10-16 07:39): i got this , is there any solution? missing header maybe?  
    "OpenCode's free tier can only be used from within OpenCode. Download it at [https://opencode.ai](https://opencode.ai) and keep building."
  - **u/Amarsir** (↑1, 2026-10-16 09:06): Presumably you were using it in Opencode? Is it updated?
      
      I've heard of that happening now and again and restarting generally fixes it. If not, you might have to uninstall and reinstall.
- **u/Fresh_Sock8660** (↑1, 2026-10-16 07:44): Is it the free tier or the go tier?
- **u/iamaestro11** (↑1, 2026-10-16 08:03): 😳 man at this point I can’t keep up….
- **u/No_Gold_4554** (↑1, 2026-10-16 08:04): thanks 🙏️
- **u/FewExplanation5433** (↑4, 2026-10-16 08:21): i think they're doing this because the apocalypse is near
- **u/GLR1997** (↑1, 2026-10-16 08:24): Glm 5.5 flash is comming ?
- **u/mWo12** (↑1, 2026-10-16 08:26): wtf! What is happening? Everyone is getting free model?
- **u/InternetExpensive584** (↑1, 2026-10-16 08:30): This month i wich to command code but all model are  free in open code thats time 😏
- **u/iwenttothelocalshop** (↑2, 2026-10-16 08:39): Christmas came early vol.2
- **u/tronghieu906** (↑1, 2026-10-16 08:48): I just subbed to command code 1 week earlier. Cheepseek then this... 😓
- **u/EggMaterial4172** (↑1, 2026-10-16 09:07): Good I will add this in my custom OmniRoute
- **u/sashko5** (↑4, 2026-10-16 09:18): Aaand it's overloaded already! You guys crashed it :) But really cool to see a free version of GLM 5.3 on OpenCode. I use OpenCode Go and I'm pretty happy so far.
  - **u/fazesamurai145** (↑2, 2026-10-16 09:41): Yap crashed
- **u/Avernite** (↑2, 2026-10-16 09:33): when i switch to this, opencode says that model may train on my data. Is there anywhere this can be verified?
  - **u/jonas-reddit** (↑2, 2026-10-16 09:40): Of course it does. It’s free. They’re not doing this for humanitarian reasons.
    - **u/no_choice99** (↑2, 2026-10-16 10:03): You can disable this for free models with plenty of companies. Why would this one be different?
- **u/Flashy_Disaster9556** (↑2, 2026-10-16 10:13): Do they even want my money?
  - **u/Ok-Drawer5245** (↑2, 2026-10-16 10:53): good question
- **u/ozguru** (↑3, 2026-10-16 10:13): opencode is pushing hard, maybe this is v2 promotion?
- **u/Tough-Obligation7386** (↑3, 2026-10-16 10:45): Wow is it  Christmas already?
- **u/Ok-Drawer5245** (↑1, 2026-10-16 10:54): When till Kimi k3 be free?
- **u/Rockshoes1** (↑1, 2026-10-16 11:40): Who is sponsoring and how many tokens do you get? There’s nothing free what’s the catch?
- **u/QBA_gg** (↑1, 2026-10-16 11:41): Yeah probably Q1 5 tok/s
- **u/alexwwang** (↑1, 2026-10-16 12:23): But only available by calling with opencode.
  - **u/nekohacker591-** (↑1, 2026-10-16 14:06): Unless u change the user agent
    - **u/IAmFitzRoy** (↑1, 2026-10-16 16:25): You mean “spoof” the user agent.
      - **u/nekohacker591-** (↑1, 2026-10-16 18:03): no change 
          
          i dont consider this technical enough to call spoofing
        - **u/IAmFitzRoy** (↑1, 2026-10-16 18:13): I don’t think spoofing cares too much about what you consider. 
            
            Words have meaning, “**spoofing is the practice of forging or manipulating metadata fields”**
            
            Changing the metadata to pretend it’s coming from OpenCode harness is spoofing.
          - **u/alexwwang** (↑1, 2026-10-17 14:03): Seems the proper way to deal with it is to call opencode -p , if it still supports this argument.
- **u/Dry_Possibility_6455** (↑1, 2026-10-16 12:28): Fyi GLM-5.3 free is 200k context
  - **u/Huge_Business2428** (↑1, 2026-10-16 14:50): in my experience 200k context isnt really an issue for most of my projects, however the rate limit is insane. I hit the rate limit while it was still thinking, it didnt even output a single word before I hit the limit lmao. DS 4.1 Flash Free also has 200k context, but it handles the same project without any issues.
- **u/Kitchen-Election3490** (↑2, 2026-10-16 12:46): I'm kind of new to using opencode go..  I have an active opencode go subscription and have been using it with pi and openclaw..  it doesn't seem like Opencode makes these new free models accessible to any other client except their own official client, right?  No mater what I do, I can't get these other clients to use the deepseek 4.1 flash free or GLM 5.3 free..
    
    I CAN access other free models like LongCat and CatJam using pi and open claw, however.
  - **u/Kitchen-Election3490** (↑1, 2026-10-16 13:25): I reached out to OpenCode for clarification..  definitely seems like these free models aren't accessible outside the OpenCode client...  I incorrectly assumed they were part of my Go subscription and were going to be accessible using my API key outside OpenCode client..  oh well.
    - **u/badcodinghabits** (↑1, 2026-10-16 17:50): Came here to ask about this - thanks for doing the research!
      - **u/Kitchen-Election3490** (↑1, 2026-10-16 18:03): Yeah, it's s shame..  especially since Go has access to other "free" models. I do like pointing my pi/openclaw/hermes harness at the free models even with my Go subscription.. the way I can better control my monthly token usage..
  - **u/martina-krejci** (↑1, 2026-10-16 13:27): they are not part of opencode go but opencode zen (which is their pay per tokens model) and it is exactly opossite -- those can be used only in opencode client, using elsewhere like hermes you get 4xx error with message that other clients are unsupported.
    - **u/Kitchen-Election3490** (↑1, 2026-10-16 13:35): The part that was confusing for me is my OpenCode dashbord lists a bunch of models that I can turn off and on..  I just assumed the dashboard model list (which includes these new free models) applied to my Go Subscirption
      - **u/pendelhaven** (↑2, 2026-10-16 15:19): They are different. The free models on ZEN are not the same as GO. For example dsv41f and glm53f on ZEN free are only 200k context. GO ones natively support 1m context.
- **u/daniel-sousa-me** (↑1, 2026-10-16 13:54): It's probably sharing the same limits as Muse Spark 1.3, which is stronger and has a longer context window (which makes a big difference here, because the limits are by number of requests and not by tokens)
    
    The main advantage is that Muse Spark is clear that it's a contributor edition, while GLM claims it's ZDR. But one think you can trust Chinese companies on is not to respect any boundaries around "intellectual property"
  - **u/cnava9389** (↑1, 2026-10-16 15:39): And American ones do respect it?
    - **u/korino11** (↑1, 2026-10-17 17:04): He is brainwashed with propaganda...
- **u/fno2010** (↑1, 2026-10-16 14:00): Yes, it's free. But its rate limit, cache hit rate, and tps are incredibly bad... If just for a chatbot, maybe it's enough. But you can only use it inside opencode right now. Then it's tricky.
- **u/LuluLeSigma** (↑1, 2026-10-16 14:44): which one is better ds4.1 flash or glm5.3 flash
- **u/Whole_Lie_6622** (↑2, 2026-10-16 16:01): guys what do you remember about when things are free, think about Google, Meta, etc.. We are product.
- **u/Soul_Mate_4ever** (↑2, 2026-10-16 16:31): What is going on? Whatever it is I like it.
- **u/Muhtefi** (↑1, 2026-10-16 16:36): Yeah, but it has 200k context, a crippled model version. I wonder how it handles a full repo audit.
- **u/miloco2few** (↑1, 2026-10-16 16:50): This is great news!!!! After deepseek becoming free... It's like an early christmas!! But it doesn't seem to be working properly for me...
- **u/Mementem** (↑3, 2026-10-16 19:04): has a 200k context just like DS v4.1 flash  
    can anyone please tell me the data retention policy please? i cannot find it, is there no data retention for this?
- **u/PuzzleheadedSnow7180** (↑1, 2026-10-16 19:55): how good is this model?
  - **u/bartsimpsonwin** (↑1, 2026-10-16 20:04): Id say like opus 4.8 in my experience, not bad but far from newer gpt/Gemini/Claude or even grok models
    - **u/PuzzleheadedSnow7180** (↑1, 2026-10-16 20:16): I use dp 4.1 flash in go and it is nice and cheap
      - **u/bartsimpsonwin** (↑1, 2026-10-16 20:34): Yeah, it's great, around Luna intelligence but more expensive, but also faster
- **u/zeta_cartel_CFO** (↑1, 2026-10-16 23:26): Thanks.  They just removed Muse Spark 1.3 contribute this evening.  Sucks, because surprisingly it was a capable model. At least for MCP/Tool calling and automation.  Didn't try it for anything else. 
    
    Will try out GLM 1.3 flash.
- **u/Yann27** (↑2, 2026-10-17 11:39): the output feels like deepseek...
- **u/gs-red** (↑2, 2026-10-17 17:39): Do you need a sub for this? Or it would just work on the terminal agent? Do you need to be logged in?

---

## Can I able to create OPENCODE clone by the use of opencode
**u/Helpful_Layer_4754** · 2026-10-16 06:40 UTC · ↑0 · 9 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x78zvs/can_i_able_to_create_opencode_clone_by_the_use_of/)

**Comentarios:**

- **u/nvn911** (↑8, 2026-10-16 06:44): That's what the Open in Opencode stands for
- **u/LowIllustrator2501** (↑16, 2026-10-16 06:47): You can create a clone by using this simple trick: 
    git clone https://github.com/anomalyco/opencode.git
  - **u/Pink_Oak** (↑2, 2026-10-16 09:21): hurry up before they patch it
- **u/talaman4eg** (↑3, 2026-10-16 07:11): you can even create opencode clone clone with opencode. or with opencode clone.
- **u/Sudden_Design5053** (↑2, 2026-10-16 07:46): 😂😂✌️
- **u/4SubZero20** (↑2, 2026-10-16 12:39): Why TF is this tagged NSFW???
  - **u/techmago** (↑1, 2026-10-16 15:23): nasty teenagers and their code. Don't let children see.
- **u/qustrolabe** (↑1, 2026-10-16 13:11): Of course just setup your own Zen and invest money into getting subscriptions going and try to stay afloat while giving generous offers and tracking down abuse of creating multiple accounts to farm first-time discount. Sounds soooo easy
- **u/AbdSheikho** (↑1, 2026-10-16 13:50): Why clone when you can fork?

---

## What skills, tool sets, plugins do you find useful
**u/SmilesyH** · 2026-10-16 06:34 UTC · ↑8 · 9 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x78wqz/what_skills_tool_sets_plugins_do_you_find_useful/)

I've been using Opencode since April, and initially I was just using the raw application with models from NeuralWatt. I then found a repo with a load of skills, loaded them all (100+) and then realized that it loaded massive amount of stuff I didn't need into context. Got rid of all of them, but kept Superpowers. I ran with that for a while and it was pretty good, especially when my projects were pretty small and light. I think found Oh My Opencode and tried that, but found it eat too may token, but I did like the quality of product it gave me. I then went onto OMO-Slim which I have been using ever since for larger tasks, and build and plan for quicker scripts.   
I recently upgraded to V2 and it seems to be working really well, but I haven't spend a huge amount of time looking at what is out there to improve on the base Opencode for a while, and with the speed that the area moves I have a feeling this may have changed.   
What are you using onto of the base (if anything), why and what are the strength and weaknesses of it.

**Comentarios:**

- **u/tsangberg** (↑3, 2026-10-16 06:42): The only external plugin/skill I use is Superpowers. The rest\* I've developed myself so that they suit my exact needs - this is one of the huge benefits LLMs give us. No need to find someone else's tool and adapt to it when you can prompt your own.
    
    \*) sort-of-memory system and sandboxing
- **u/for4f** (↑1, 2026-10-16 08:25): lol the 100 skills phase, been there. did the same thing, loaded up everything then watched my context window evaporate. pared it back to basically superpowers plus a couple things i wrote myself for my own stack. omo felt the same to me, quality is nice but the token bill hurts. haven't dug into v2 much yet either, still on slim and it does the job
- **u/lincolnthalles** (↑1, 2026-10-16 09:14): I use grilling a lot, so it's always available.
    
    I default to denying all skills in the global opencode configuration, then I allow a few specific skills per project.
    
    It's also possible to install or create project-scoped skills in `.agents/skills`, keeping things cleaner.
    
    This avoids the context issue, which not only burns tokens on all skill descriptions but also stresses the model with a ton of triggers to evaluate.
    
    OpenCode V2 has better built-in tools, so I do not use anything other than agent-browser and the RTK plug-in, which transparently proxies tool calls to it without bloating the agents.md with RTK instructions.
- **u/ozguru** (↑1, 2026-10-16 11:03): I can highly suggest [https://github.com/abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) , [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills) I believe those are really helpful for any kind of development. Bonus [https://github.com/DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) , bonus tip, prompt this, "consolide my skills"
- **u/Stevie2k8** (↑1, 2026-10-16 13:14): I use engram as memory, zvgrep from alibaba as semantic file search, my own ai ticketing system mcp and a tuned version auf superpowers (to match my ticketing system... don't need no todo lists or specification documents, all goes into tickets...)    
    Yesterday I started experimenting with magic context, not sure if I keep it... looks promising right now but didn't use it very much...
- **u/pikuray** (↑1, 2026-10-16 13:58): I don't use any i tell my ai do this for me, am i missing out?
- **u/QuietPuddle27** (↑1, 2026-10-16 15:48): I’ve learned that more tools don’t automatically mean better results. A small set of reliable skills that you actually use beats loading 100 plugins and burning context on things you barely need.
- **u/bangsmackpow** (↑1, 2026-10-16 18:23): UI/UX Pro Max is the only one I have statically loaded so my UI's look similar across all of them.
- **u/Mementem** (↑1, 2026-10-16 19:07): i mainly use these : Tastemaker, Brainstorming, Front-end Design, and Dream Design Team.
    
    keep in mind that using too many skills will effect usage.

---

## If you tried v2 and its not for you...
**u/iarna** · 2026-10-16 06:01 UTC · ↑2 · 3 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x78dec/if_you_tried_v2_and_its_not_for_you/)

And you didn't think to backup your opencode.db first? Yeah, me too. I went to the trouble to make a downgrade script so I could go back to 1.19.0. The SQL is from DeepSeek 4.1 and has been tested. The rest is me. I figured it would likely be useful to others, so I've stuck it in gist:

https://gist.github.com/iarna/5d030e28c56c137f489a9d7ad12aa74a

One caveat, it only supports Mac and Linux (which should include WSL). If you want it for Windows you can probably one-shot that translation with a modern llm.

It handles downgrading opencode too, if you installed it with curl or npm.

**Comentarios:**

- **u/Amarsir** (↑1, 2026-10-16 06:26): How often do people really go back to old sessions? 
    
    I'm either going back in the same day, or good riddance and why the fuck is it taking up disk space? But I'm happy to hear about other people's workflows.
  - **u/iarna** (↑1, 2026-10-17 01:07): I had active sessions, =p I'm not saying I made a good decision, lol
- **u/Mementem** (↑1, 2026-10-16 19:11):  i was thinking about updating, will make sure to backup everything before hand, thanks

---

## I have no modles, and can not use the chat please help me
**u/BoxCrime** · 2026-10-16 05:35 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x77xoy/i_have_no_modles_and_can_not_use_the_chat_please/)

https://i.redd.it/dwegx8numrvh1.png

i have no modles or agents, and i have tried googling this and im not sure how to fix it.

---

## Is this the real official Space Bunny?
**u/Effective_Union7326** · 2026-10-16 05:18 UTC · ↑0 · 7 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x77nos/is_this_the_real_official_space_bunny/)

The pricing is absolutely insane.

**Comentarios:**

- **u/qustrolabe** (↑5, 2026-10-16 05:28): looks like some automated fraud that generates convincing fake websites for popular models
- **u/KMichaelKills_137** (↑3, 2026-10-16 05:30): No, this is Patrick.
- **u/Effective_Union7326** (↑2, 2026-10-16 05:56): Thanks for the info, guys! I almost got scammed...
- **u/Mementem** (↑1, 2026-10-16 19:12): the site's UI looks AI generated, not even a good one at that.  
    i would stay away from this
- **u/AdFun4897** (↑1, 2026-10-16 20:27): No @Effective\_Union7326, we wont put our credit cards in your sketchy vibecode AI slop website
  - **u/Effective_Union7326** (↑1, 2026-10-17 04:02): Not me……crazy people
- **u/manuhackzzz** (↑1, 2026-10-17 16:48): It's a sc@m.. Avoid

---

## [Release Candidate] Plugin opencode-models-discovery v2.0.0-rc.2 is here — Full OpenCode v2 Support is ready for testing!
**u/yu_hp** · 2026-10-16 04:47 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x774fy/release_candidate_plugin_opencodemodelsdiscovery/)

---

## What is this new Code Mode tool catalog? Did anyone else get it after updating OpenCode?
**u/Substantial_Tart_905** · 2026-10-16 03:38 UTC · ↑4 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x75uxi/what_is_this_new_code_mode_tool_catalog_did/)

https://i.redd.it/dxaum3jq1rvh1.png

Hey everyone!

I recently updated OpenCode, and afterward, I noticed something new in my conversation context: a message saying that the Code Mode tool catalog has changed and supersedes the previous catalog.

The message describes a different way for AI agents to discover and invoke tools. Instead of calling tools directly, the agent must use an `execute` tool, search for the required tool using `search(...)`, inspect its returned path and signature, and then invoke it through that path.

It also notes that the available tool catalog is partial, so agents must discover additional tools as needed.

Here's what I'm trying to understand:

1. **Is this an expected change?** Did this appear for anyone else after updating OpenCode, or is it specific to my setup?
2. **What exactly is changing?** Is this a change to OpenCode itself, its MCP integration, the AI agent's tool-calling mechanism, or something else?
3. **How does this affect existing workflows?** Should agents that previously called tools directly now use this discovery-and-execution approach?
4. **Has anyone else encountered this?** If so, did you notice any differences in tool usage, reliability, or agent behavior?

I've attached a screenshot of the message I received.

I'm not reporting a bug at this point. I simply want to understand what this change means and whether other users are experiencing the same thing.

If anyone has additional context, documentation, or firsthand experience, I'd appreciate the explanation!

Thanks!

**Comentarios:**

- **u/ichisay** (↑1, 2026-10-16 08:33): Que versión tienes?

---

## Best for making a website, like a Point of Sales or managerial system?
**u/Realistic-Rise798** · 2026-10-16 02:04 UTC · ↑1 · 6 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x742y1/best_for_making_a_website_like_a_point_of_sales/)

the tittle, what is the best in the free tier to build this? i assume the using of database, vercel etc.

**Comentarios:**

- **u/Haunting-Shirt6219** (↑1, 2026-10-16 02:42): Supabase + Cloudflare
  - **u/Realistic-Rise798** (↑1, 2026-10-16 02:56): sorry , i mean the ai agent
    - **u/ERROR_FOX_PG** (↑1, 2026-10-16 16:47): Muse spark 1.3
      - **u/Realistic-Rise798** (↑1, 2026-10-17 02:08): its gone already, any alternative? is gemini with 9router good?
- **u/Conscious_Cow358** (↑1, 2026-10-16 06:28): i believe spacebunny alpha is good for ui imo. hand it over the design skill of anthropic and your design taste it works good.
- **u/Mementem** (↑1, 2026-10-16 19:14): glm 5.3 flash is really good, but iirc it has a 200k context.   
    mimo 2.6 flash is pretty good too!

---

## Favorite Model for fast responses/coding?
**u/SlowAndSteady101** · 2026-10-16 01:39 UTC · ↑3 · 7 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x73lbg/favorite_model_for_fast_responsescoding/)

Anyone have a model they like that is super fast and good enough at coding? And maybe cheap?

**Comentarios:**

- **u/SimpleTeacher5046** (↑4, 2026-10-16 01:42): Muse 1.3 contributor 
    
    Use plan mode always with subagents then build with one agent. 
    
    
    Gets a pretty good job done
  - **u/Ceextasy** (↑1, 2026-10-16 12:35): I second this, even though i am greedy and want to keep people from using muse spark 1.3. It is such a good model but lately when i work ive been having more and more backend load warnings. So greedy of me 🙃
- **u/GoomiBare** (↑3, 2026-10-16 02:30): Deepseek v4.1 Flash fast or glm-5.3-flashx
- **u/Amarsir** (↑2, 2026-10-16 04:00): Some people one-shot "create a first-person shooter" via vibe-coding and some give tasks like "add a new API call to this existing codebase to save and retrieve the user's sort preferences for this table." Those have different needs. Then there's writing the code vs the overall planning. And you don't necessarily need to use the same model for both.
    
    If you need complex planning, to the extent that more intelligence is actually useful, ChatGPT 6.1 Sol and Claude Opus 5.5 are the best right now. That means getting a sub from OpenAI or Anthropic.
    
    But do you need that kind of intelligence? The kind that didn't even exist 3 months ago? Or can you break up your own projects into manageable tasks that can be handled more reasonably?  April 16, that's exactly 6 months ago, Opus 4.7 came out and was about the best you could get. Here are the current models that are roughly equivalent to it, but much cheaper:
    
    * GPT-6 Luna
    * Mimo-V2.6 Flash
    * Claude Haiku 5.5
    * Muse Spark 1.3 (The Contributor version, while much cheaper, means they will be training off your data.)
    * Deepseek V4.1 Flash
    * GLM 5.3 Flash
    * Qwen 3.8 Flash Next
    * Space Bunny (anecdotally. We don't have a ton of testing data on it.)
    
    The fastest would either be Deepseek or Muse Spark. Followed by Luna and Haiku. Then GLM a bit behind but not too bad. Mimo and Qwen are disappointingly slow.  Space Bunny is inconsistent, so I'd also put it in the slow category but it might surprise you.
    
    So if you're going to go with the $10 Opencode Go you can pick from any of those 7. Different people have their favorites based on style and need.
- **u/Rustybot** (↑1, 2026-10-16 19:40): Gemini-3.8-flash medium, but will admit it needs to be tightly walled-in and validated, or it will make fake tests and hide tech debt. But it’s the peak for speed-smart-cheap.

---

## I put together an early OpenCode plugin for Claude Code OAuth — feedback welcome
**u/crxsx_0** · 2026-10-16 01:30 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x73f09/i_put_together_an_early_opencode_plugin_for/)

[removed]

---

## How can you copy code from the OpenCode TUI in Termux Mobile without getting line break errors? It's really frustrating.
**u/Zealousideal-Sun4565** · 2026-10-16 00:05 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x71old/how_can_you_copy_code_from_the_opencode_tui_in/)

pls help me

---

## What free model do you use?
**u/Another-Geek-Guy** · 2026-10-15 23:59 UTC · ↑0 · 11 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x71irl/what_free_model_do_you_use/)

I want to know what models people use, like models that output good code, and doesn't hallucinate, because running a test like making a webpage, doesn't test how it does when it's really coding. Thank you!

**Comentarios:**

- **u/TronnaLegacy** (↑2, 2026-10-16 00:05): DeepSeek 4.1 Flash
  - **u/Another-Geek-Guy** (↑1, 2026-10-16 00:45): Thank you!
- **u/reybrujo** (↑2, 2026-10-16 00:16): I use Muse or Big Pickle, you really need to be into coding to notice differences in the final product for simple programs like the ones you apparently would write so I wouldn't really care about which one, just pick any and use it.
- **u/TheMythicSorcerer** (↑1, 2026-10-16 01:00): Mimo v2.6 is pretty good for most tasks, muse feels better for frontend
- **u/Least_Bodybuilder216** (↑1, 2026-10-16 01:05): Deepseek, my goat
- **u/Amarsir** (↑2, 2026-10-16 01:26): Everything has it's purpose. 
    
    * Muse Spark 1.3 for overview. 
    * With today's addition of free-tier DS 4.1 Flash it's great for writing code, but before that I was using MiMo V2.6 Flash. 
    * I'll dabble with Space Bunny for a different point of view, like a code review after the first 2 do a task. 
    * I'm trying out nemotron-3.5-super-vl-free on quick and easy tasks. I'd rather use Cat Jam but it was hitting a limit super fast.
- **u/chikamakaleyley** (↑2, 2026-10-16 04:00): Big Pickle, to help train their model
    
    and now Space Bunny, for the 1M tokens
- **u/SerBud** (↑2, 2026-10-16 05:50): I use Muse Spark 1.3 or Big Pickle
- **u/Euphoric_North_745** (↑1, 2026-10-16 22:17): ChatGPT SOL 6.1 , not free, who knows how artistic it is, but ... it can create any web app you ask it to
- **u/Mezyi** (↑1, 2026-10-17 00:05): I just bought open code go, but beam seems insanely good for a free model? It’s willing to do pentesting as well

---

## New model: Nemotron 3.5 Super VL - 120B total · 12B active · multimodal
**u/Emotional-Bag-3754** · 2026-10-15 23:48 UTC · ↑3 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x71a34/new_model_nemotron_35_super_vl_120b_total_12b/)

---

## What happened with OpenCode after the last upgrade?
**u/Haunting-Shirt6219** · 2026-10-15 23:36 UTC · ↑5 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x711ke/what_happened_with_opencode_after_the_last_upgrade/)

https://i.redd.it/cz5p2dvcvpvh1.png

Any ideas? I can’t do anything right now. The application is frozen and no session is open.

**Comentarios:**

- **u/VGG2077** (↑1, 2026-10-16 01:40): Looks like a memory leak
  - **u/Haunting-Shirt6219** (↑1, 2026-10-16 02:37): removed all cache, reinstall opencode, issue fixed
- **u/Mementem** (↑1, 2026-10-16 19:17): should i wait a bit before updating? wait for things to get polished?
  - **u/Haunting-Shirt6219** (↑2, 2026-10-16 22:30): I’m used Deepseek Harness to fix the cache and now it works

---

## Did anyone tried ModelArk Coding Plan ?
**u/AppleHuman8535** · 2026-10-15 23:36 UTC · ↑0 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x71142/did_anyone_tried_modelark_coding_plan/)

Just asking, they claim it has 3x the usage of Claude Pro, but I’m super hesitant. I once bought a $5 token plan from Mimo and only got $5 worth of usage (actually around $4.60 by my calculations). I really don't want to get scammed, so if any of you have already gotten burned, I’d appreciate it if you could let us know.

**Comentarios:**

- **u/songokussm** (↑1, 2026-10-16 02:17): 3x what? Claude doesn't publish is usage and it changes per per week and changes again depending on what 'test' group your in.
    
    In the $10 bracket your only reliable options are opencode and command code.
  - **u/AppleHuman8535** (↑1, 2026-10-16 10:40): I really don't know what 3x mean . Its their claim .
- **u/QuinsZouls** (↑1, 2026-10-16 02:22): I tried the 10usd version and the usage was a joke
  - **u/AppleHuman8535** (↑1, 2026-10-16 10:39): unlucky

---

## "I got this, hold my beer!" - Deepseek-V4.1-Flash
**u/Fair-Interview-9138** · 2026-10-15 22:56 UTC · ↑40 · 19 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x705kc/i_got_this_hold_my_beer_deepseekv41flash/)

TL;DR: Tasked GLM-5.3-Flash, MiMo-V2.6-Flash, and Deepseek-V4.1-Flash with reviewing a skeleton codebase. Deepseek decided to ignore instructions to use included stand-ins instead of live API calls, then panicked when it realized it's error.

I am usually a lurker, but this is too funny. I had Argon create a series of structured prompts for MiMo-V2.6-Flash:Free to create a skeleton proof-of-concept for my project.

I then had MiMo-V2.6-Flash, GLM-5.3-Flash, and Deepseek-V4.1-Flash analyze the codebase for issues (I defined that more clearly than "look for issues" ofc). Argon and Sonnet 5.5 XHigh then also independently reviewed the codebase, then graded the reports against their own.

Summarized Results:

GLM  
(\~30m review time) - Identified 12/17 real defect issues, 3 unique valid findings, 0 false positives. Some issues with consequences of issues on operation, but pretty solid and methodical.  
Rated 9/10 by Argon and Sonnet 5.5 XHigh.

MiMo  
(\~30m review time) - Identified 10/17 real defect issues, 4 unique valid findings, 1 false positive. Makes sense given it was the original coding model. Not bad, but thought itself into loops fairly frequently. Rated 8/10 by Argon and Sonnet 5.5 XHigh.

And now Deepseek...  
(\~15M review time) - Identified 9/17 real defect issues, 0 unique valid findings, 3 false positives. **Literally blew past specific direction to not test live API calls. Twice.** Reading the panic once the model realized it's error is the funniest thing I have seen in a long while. Also, this model isn't touching my codebase without extreme babysitting or a change in prompt philosophy.  
Rated 6.5/10 by Argon and Sonnet 5.5 XHigh.

I am fairly new to agentic coding and coding in general, but I am fairly structured and methodical when it comes to personal projects, so I've been researching different options. Turns out my research was mostly confirmed: GLM-5.3-Flash was fairly complete and measured, MiMo-V2.6-Flash is not bad but can get stuck, and Deepseek is a talented teenager with severe ADHD, seven energy drinks, and identifies as chaotic neutral.

Disclaimers:  
This is not rigorous, and borders on anecdotal - This was single pass with identical instructions. The codebase included design documents that the LLMs could reference for intended design, as well as the original prompts for creating the codebase and any additional instructions given to the original coding agent. I am not claiming that Deepseek-V4.1-Flash sucks; it is very fast, but may need very strict prompting to not go off the rails and be confidently wrong. Perhaps two passes of 4.1 is worth more than one pass of the other models, but I hesitate to trust that the same model would catch issues in the second pass without creating more issues.

There are some absolute Deepseek-V4.1-Flash stans on the interwebs. I would love to hear some insight on how you effectively prompt it (or if you just have it check itself frequently).

Also, any free models, stealth or otherwise, that I should try?  


TL;DR (again): Tasked GLM-5.3-Flash, MiMo-V2.6-Flash, and Deepseek-V4.1-Flash with reviewing a skeleton codebase. Deepseek decided to ignore instructions to use included stand-ins instead of live API calls, then panicked when it realized it's error.

**Comentarios:**

- **u/mozkohor** (↑3, 2026-10-15 23:03): try mimo 2.6 pro
  - **u/look** (↑2, 2026-10-16 01:22): Seconded. And I recommend checking out PrimaLabs for running it. Fast and standard pricing, so it’s still low cost, even compared to Go’s $15-tier pricing. Neuralwatt’s Mimo Pro is also fast and high quality, though it can cost just a bit more than the standard list price.
- **u/ANDALTUV** (↑3, 2026-10-16 00:45): dude separation of concerns... when the Deepseek context usage is at 30% be ready for the hallucination party... I use compact at 20%, also one agent per task, and finally small [Plan.MD](http://Plan.MD) with enough context, technologies and constrains... Then I pass each agent his own task.. Is the only way to keep the thing on a leash.
  - **u/Fair-Interview-9138** (↑1, 2026-10-16 01:32): That's what I was thinking. I might just need to atomize my prompts a bit more for Deepseek. Also good shout on the [plan.md](http://plan.md), I skimped on it since I was basically having Argon plan for the edits, but didn't think about a separate plan for the review itself. Perhaps I misunderstood the value.
- **u/Due_Aerie_2388** (↑5, 2026-10-16 00:58): I’m curious about how Muse 1.3 would handle it compared to glm, mimo and DS.   
    Do you mind testing it and telling us how argon/sonnet rate its work?
  - **u/Fair-Interview-9138** (↑2, 2026-10-16 01:27): For sure, but i'll find another opportunity to test them with a similar setup (i'm a couple commits into the fixes and don't want to revert just to test)
    - **u/Chance-Republic-9303** (↑2, 2026-10-16 01:43): Are there any relevant audit prompts?
      - **u/Fair-Interview-9138** (↑1, 2026-10-16 01:57): The specific prompt wasn't fancy or anything. Honestly, ask a decent LLM for a prompt for a coding agent reviewing X, Y, or Z, bounded to workspace A and temp files. Define parameters and restrictions you want the model to follow and the format you want the models to report it in (I asked for a Markdown file in a separate documentation folder). A prompt developed to what you want over a few turns of good ol' ChatGPT think (GPT-6-Luna-medium) beats a generic prompt from Sonnet 5.5 from what i've seen.
- **u/Yayman123** (↑3, 2026-10-16 01:21): Interesting findings. A few things:
    
    1. Deepseek 4.1 flash doesn't do as well once you go past 200K context because of the model's design.
    
    2. It's very likely that the provider Opencode now uses to serve it is using a quantized version, possibly heavily so. Some people report noticeably better performance from the Deepseek API directly for whatever reason.
  - **u/Fair-Interview-9138** (↑1, 2026-10-16 01:34): Yep, learning I should feed it smaller more defined tasks than the others can handle. FWIW I think context never went above 185k for deep seek, but can't say for certain.
    - **u/Saifl** (↑1, 2026-10-16 03:12): If you can afford it, having a direct api comparison would be a good comparison, specifically for deepseek
- **u/IISomeOneII** (↑4, 2026-10-16 01:49): https://reddit.com/link/ph0vkzb/video/cm43mx01jqvh1/player
    
    look whos on the most right 😹😹😹
    
    with a holy moly 96%
    
    source: [https://artificialanalysis.ai/evaluations/omniscience#omniscience-hallucination-rate-tabs](https://artificialanalysis.ai/evaluations/omniscience#omniscience-hallucination-rate-tabs)
  - **u/Fair-Interview-9138** (↑2, 2026-10-16 02:01): For sure, came across that in my model research, and made me wary in the first place. I guess it's good to see an example of how drastic hallucination errors can be!
- **u/thirdcupin** (↑1, 2026-10-16 03:39): I’d honestly love to see a second benchmark with stricter tool restrictions. I’m curious whether DeepSeek improves with tighter guardrails or if the same issues keep showing up.
  - **u/Fair-Interview-9138** (↑1, 2026-10-16 04:19): I'll be on the lookout for another good place to benchmark in my development with similar conditions and more models. That aside, even disregarding the API calls, it still had less correct issue spots and more false positives.
      
      I'll also be giving Deepseek some very small tasks and strict prompting for now, as well as trying out different plan files to harness it's speed a bit better.
- **u/Frequent_Director_94** (↑1, 2026-10-16 06:10): Did you have it create a spec or similar or just prompting it with instructions
- **u/CaffeinatedTech** (↑1, 2026-10-16 09:53): Every session could land a different provider though.  Some are probably lower quant.  Opencode tells you which provider you are on, it sends it in the response header in "x-opencode-endpoint-id".  Get your agent to build an extension to show it.
- **u/IndividualPlus2011** (↑2, 2026-10-16 12:22): DeepSeek doesn't listen to instructions. You can put anything you want in the system prompt or skills usage guidelines. It will just ignore most of them. It's not a context rot, it does it from the very beginning and wants to do everything its own way, even if it reads a skill.
    
    It only listens to what the user tells it directly in the user message.
- **u/Imaginary-Kale4673** (↑1, 2026-10-16 15:43): At this point you can use MiMo-V2.6-pro since it is at the same price point as the flash models.

---

## What are you using for browser automation and computer use with OpenCode?
**u/augustwise** · 2026-10-15 21:17 UTC · ↑5 · 12 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6xwgd/what_are_you_using_for_browser_automation_and/)

Hey everyone,

I've been using OpenCode for coding and I'm now looking to add browser and computer-use capabilities to my setup. I'd love to hear what's working for you.

**Comentarios:**

- **u/warpaint_james** (↑5, 2026-10-15 21:25): Cant speak on computer use, but agent-browser (https://agent-browser.dev/, https://github.com/vercel-labs/agent-browser) works very well. It can even do image diffs with the screenshots it takes
  - **u/augustwise** (↑1, 2026-10-15 21:40): thanks!
- **u/TheMythicSorcerer** (↑1, 2026-10-16 01:07): u/remindmebot 14d
  - **u/RemindMeBot** (↑2, 2026-10-16 01:07): I will be messaging you in 14 days on [**2026-10-30 01:07:07 UTC**](http://www.wolframalpha.com/input/?i=2026-10-30%2001:07:07%20UTC%20To%20Local%20Time) to remind you of [**this link**](https://www.reddit.com/r/opencode/comments/1x6xwgd/what_are_you_using_for_browser_automation_and/ph0nhud/?context=3)
      
      [**CLICK THIS LINK**](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2Fopencode%2Fcomments%2F1x6xwgd%2Fwhat_are_you_using_for_browser_automation_and%2Fph0nhud%2F%5D%0A%0ARemindMe%21%202026-10-30%2001%3A07%3A07%20UTC) to send a PM to also be reminded and to reduce spam.
      
      ^(Parent commenter can ) [^(delete this message to hide from others.)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Delete%20Comment&message=Delete%21%201x6xwgd)
      
      *****
      
      |[^(Info)](https://www.reddit.com/r/RemindMeBot/comments/e1bko7/remindmebot_info_v21/)|[^(Custom)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5BLink%20or%20message%20inside%20square%20brackets%5D%0A%0ARemindMe%21%20Time%20period%20here)|[^(Your Reminders)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=List%20Of%20Reminders&message=MyReminders%21)|[^(Feedback)](https://www.reddit.com/message/compose/?to=Watchful1&subject=RemindMeBot%20Feedback)|
      |-|-|-|-|
- **u/TheMythicSorcerer** (↑1, 2026-10-16 02:15): Personally I have both agent-browser (cli) for most tasks and browser-harness (python based) for more complex tasks. I've been looking for a good general computer use tool for a while now but havent found a good one for opencode that matches the capability of chatgpt computer use.
- **u/Both-Ad6752** (↑1, 2026-10-16 02:35): u/RemindMeBot 7d
- **u/previaegg** (↑1, 2026-10-16 04:38): u/remindmebot 14d
- **u/ApprehensiveTwo9331** (↑0, 2026-10-16 04:44): Just use OpenChamber.
- **u/LowIllustrator2501** (↑1, 2026-10-16 05:34): What features in particular as missing for computer use?
    
     If you're on Linux where CLI always has been the king, just install some ImageMagick, ffmpeg, and CLI debug tools. You can debug almost anything from CLI. Ask LLM in Opencode what tools would help for debugging. 
    That's it. 
    
    Is there some magic sauce in Computer use agents?
- **u/Accomplished-Bird829** (↑1, 2026-10-16 10:36): Iam using page agent but make it that i can use the agent from the cli thro mcp and building it for each usecase encounter me and it working grate for me so i can use it with my owne browsers and my subscription like for x or medium or any website i need to scrape it its been journey but i love it

---

## Meta and Gemini models bruh.
**u/Valuable-Mirror-448** · 2026-10-15 21:01 UTC · ↑28 · 12 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6xi9y/meta_and_gemini_models_bruh/)

Brother what do I even say just dont use them man literally benchmaxxed to the point of everest

**Comentarios:**

- **u/Future-Hovercraft831** (↑4, 2026-10-15 21:07): agree
  - **u/latecheckmate** (↑2, 2026-10-16 03:58): exactly!
- **u/LuluLeSigma** (↑2, 2026-10-15 21:11): ok
- **u/TheMythicSorcerer** (↑1, 2026-10-15 21:12): Welcome to the world of "Hey look guys I topped the coding benchmark by 1% with this new over-fine-tuned model" 5 times a week every week
- **u/Prior-Meeting1645** (↑3, 2026-10-15 21:56): If u dont care about the ZDR, Muse contributor is crazy value for money even with the benchmaxxing. Cuz who is it competing with at that price? Chinese models aka the founding fathers of benchmaxxing. Use it under a SOTA model being the orchestrator
  - **u/ramendik** (↑1, 2026-10-16 16:00): That's what I do but GLM 5.3 Flash as "sota". And for now I was able to use Muse Contributor on Zen for free but I hear that it can hit limits in bigger tasjs
- **u/ramendik** (↑2, 2026-10-15 22:57): Muse Spark 1.3 Contributor, free on Zen, is doing fine as a worker model for me, but not as problem investigator
  - **u/Odd_Abrocoma_8421** (↑1, 2026-10-17 07:47): gone
    - **u/ramendik** (↑1, 2026-10-17 18:23): Yeah. Was fun while it lasted. At this point GLM 5.3 Flash is listed as free (sounds too good to be true but seems to work?)
- **u/look** (↑1, 2026-10-16 02:23): I think it’s mostly just that they aren’t prioritizing code generation like many/most other models have done so far.
- **u/Railander** (↑1, 2026-10-16 09:27): as compared to what? massively overpriced opus 5.5? or the dirt cheap chinese models?
    
    it performs similar to the best cheap chinese models. but if you're made out of money then yeah, stick to opus 5.5. many of us don't have that luxury.
    
    the value proposition on the contributor version is unbeatable for people that are actually under a tight budget, even opencode's own tests lists it as the most usage efficient model.
- **u/ozguru** (↑1, 2026-10-16 10:27): Argon is a bit disappoitment, need 4.1 soon I believe.
- **u/Euphoric_North_745** (↑1, 2026-10-16 18:39): Gpt Sol 6.1 is capable of building anything, just anything, why would anyone use a meta or Google? the numbers are just fake

---

## I brought Claude Code's /goal command to OpenCode v2 as a plugin
**u/EL4CTEO** · 2026-10-15 20:19 UTC · ↑5 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6wg34/i_brought_claude_codes_goal_command_to_opencode/)

I made a plugin that adds Claude Code's /goal command to OpenCode v2. You give the agent a finish line like "/goal npm test passes with 0 failures" and it keeps working turn after turn until the goal is actually met, no need to keep typing "continue".

After every turn an evaluator checks the conversation and decides if the goal is met, not met or impossible. If it's not met, the agent gets the reason and keeps going on its own.

It's token efficient: the evaluator reuses the session's cached context, so each check costs little more than a short answer.

It also has safety rails (pauses when the agent stops making progress, retries on network errors, turn limit) and a status indicator in the TUI.

Tell me what you think about it and feedback is appreciated.

Here's the repo and npm package:

[https://github.com/EL4CTEO/opencode-goal](https://github.com/EL4CTEO/opencode-goal)

[https://www.npmjs.com/package/@el4cteo/opencode-goal](https://www.npmjs.com/package/@el4cteo/opencode-goal)

---

## 🔥 Nemotron 3.5 Super VL is now FREE on OpenCode
**u/afanasenka** · 2026-10-15 19:50 UTC · ↑139 · 11 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6voe6/nemotron_35_super_vl_is_now_free_on_opencode/)

**Comentarios:**

- **u/Gohab2001** (↑11, 2026-10-15 19:58): yay more wasted compute. Nvidia should just serve free deepseek instead.
  - **u/totobal_012** (↑6, 2026-10-15 20:05): Nvidia is giving free deepseek in NiM
    - **u/xx_gamer_xx123321** (↑3, 2026-10-15 20:06): Very slow lol. Also deepseek is vey cheap just sub to opencode or pay direct api
      - **u/wanderingyume** (↑2, 2026-10-15 20:11): Because all non nemotrons model only run instances of 1x. 
          
          Most nemotrons running instances from x4 up to x8. (Even that 3.5 30b models is taking up 3T tokens daily).
          
          So, ds v4 there is only running a single instances cattering billions of trash requests.
          
          Nvidia should start limiting the req spams tbh.
- **u/pikuray** (↑13, 2026-10-15 20:10): We're gonna win so much, you may even get tired of winning. And you'll say, please, please, it's too much winning. We can't take it anymore. Mr. President, it's too much, and I will say no it isn't, we have to keep winning, we have to win more, we're gonna win more.
  - **u/YoRt3m** (↑5, 2026-10-15 20:19): This is such an iconic speech
- **u/NoMatterWhaa** (↑3, 2026-10-15 20:52): Any useful use area ?
- **u/Riseing** (↑1, 2026-10-16 01:42): total trash model, worse than 3.6 35b
- **u/dwerps** (↑4, 2026-10-16 04:24): Yeah, at least their description is right. Long running because the damn thing cannot get anything done.
- **u/SerBud** (↑3, 2026-10-16 05:48): The Muse Spark 1.3 Free model provides better responses.
- **u/Osvik** (↑2, 2026-10-16 17:37): I don't know if the model is good at anything, but creating frontend demos is not for sure.

---

## thats too much for a test message dont you think?
**u/Bebo991_Gaming** · 2026-10-15 19:26 UTC · ↑0 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6v1yn/thats_too_much_for_a_test_message_dont_you_think/)

https://i.redd.it/1wp3a7akmovh1.png

https://i.redd.it/nubz9fummovh1.png

**Comentarios:**

- **u/ngg990** (↑2, 2026-10-15 19:37): You are telling to a coding agent "test", so it trying to get tests in the source code tu run them
  - **u/Bebo991_Gaming** (↑1, 2026-10-15 20:03): Usually when i start a new session with any LLM they reply with things like "Loud and Clear" or "Working"
      
      This is the first time
    - **u/ngg990** (↑1, 2026-10-15 20:06): Yeah well, if you use big pickle the real model changes time by time, so for this concretely results will change ... But honestly, if I write "test" I expect to have the behavior you showing.
    - **u/nvn911** (↑1, 2026-10-16 07:25): Just say hello

---

## Ultramarine 1 Flash: Scaling Non-Verifiable RL (trained on OpenCode harness)
**u/warpaint_james** · 2026-10-15 19:23 UTC · ↑9 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6uzrc/ultramarine_1_flash_scaling_nonverifiable_rl/)

> Ultramarine improves on GLM-5.3 Flash on all six knowledge-work benchmarks, by 4.1 points on average, while generating 6.5% fewer tokens across them

Looks like they trained/benchmaxed it for OpenCode v1.18.4 so hopefully that will translate to v2.

---

## My DeepSeek 4.1 Flash implementer subagent that didn't save any Claude usage
**u/TronnaLegacy** · 2026-10-15 19:09 UTC · ↑5 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6umgy/my_deepseek_41_flash_implementer_subagent_that/)

After reading about the pattern online, I experimented with Claude Code subagents so that I could delegate to less powerful models than Opus, while having Opus drive them. It sounded good in theory and after ironing out some kinks, I had it working, even when the "implementer" subagent was from outside Anthropic. I used T3 Code to orchestrate it. The same machine had \`claude\` and \`opencode\` CLIs installed on them, so via subagents and skills, my Claude session could be instructed to call \`opencode\` via Bash when it needed to.

However, when I measured it today, using Opus 5.5 as the main session, comparing to when DeepSeek 4.1 Flash was used to implement vs having the main session do the implementation itself, I found that there was no reduction in Claude usage. I guess the overhead of having Opus 5.5 orchestrate DeepSeek negated the savings.

I also tried it with a Sonnet 5.5 implementer subagent.

Here is the final result in Claude usage (from Opus 5.5):

|Approach|5h hr quota used|
|:-|:-|
|Opus 5.5 only|8%|
|Opus 5.5 driving DeepSeek 4.1 Flash subagent|8%|
|Opus 5.5 driving Sonnet 5.5 subagent|4%|

It would probably be too verbose to share the complete subagent markdown and [CLAUDE.md](http://CLAUDE.md) that told it how to use them, but I'm happy to share it if anyone wants to see it.

summary, these are the two agents I had:

* DeepSeek implementer
   * name: ds-implementer
   * description: Implements a plan through DeepSeek-V4.1-Flash (free) on OpenCode, using the ds-implement script. The default implementer for every plan that is more than a few lines.
   * model: haiku
   * tools: Bash
* Sonnet implementer
   * name: sonnet-implementer
   * description: The Claude implementer, using Sonnet. Use it when ds-implementer failed, when the user has opted out of OpenCode for the session, or after OpenCode was unavailable earlier in the session.
   * model: sonnet

And the DeepSeek implementer agent uses Bash to invoke a script I saved at \`\~/.local/bin/ds-implement\` which invokes \`opencode\`, doing the handoff and giving just the \`opencode\` result (and context if it failed) to the agent.

I had an existing app that I wanted to add a feature to, and this is the prompt I used for the test each time (minus the extra instructions I gave each to point them at the right subagent manually and to tell one not to use any subagents):

>On a new feature branch from main, let's add the ability for planners to export their data. New tab on the left called export. Pick a good Lucide icon.

Sharing because I'm curious if people have had success with this kind of worker agent orchestration, or if they think it's simpler for me to just stick to having Claude use Claude subagents.

**Comentarios:**

- **u/Amarsir** (↑1, 2026-10-15 22:21): Your DS implementer was in Haiku? Typo?
    
    For me a big part of the process is a written plan. I can review it myself (and/or shop it around to different LLMs to get a variety of reviews). And then hand it off without much remaining guidance needed.
    
    It's more hands-on of course, but I can have Opus write, then just let Haiku execute. Maybe Sonnet to orchestrate if I want review and testing built in. This requires some thoughtfulness because if it's a bug context window you don't want it reloading into every different model or getting stale while it's waits on your manual review. But I find a good plan doesn't require much context anymore.
  - **u/TronnaLegacy** (↑2, 2026-10-15 23:42): No, my architecture needed a subagent using some Claude model to relay the instructions to DS and relay the result back. I was using Claude to put together this architecture, and it suggested another approach I could use was a skill to make sure the main session agent knew how to use Bash to invoke \`opencode\`. But I thought the relay subagent was a better idea. And since you don't need a strong model for that, I picked Haiku, as Claude suggested I pick.
    - **u/Amarsir** (↑1, 2026-10-16 00:14): OK that makes sense. It probably wasn't a lot of overhead, but it's also not a step I would have done. (Mainly because you might as well just use Haiku for the work at that point.)
        
        Speaking of which, upon re-checking benchmarks, I'm reminded there aren't many spots I'd want to use Sonnet 5.5. Low and Medium reasoning levels are beaten by Haiku 5.5 Xhigh and Max. Sonnet 5.5 High is arguably worth using. (\*) But then Sonnet Xhigh you're better off on Opus 5.5 High and Sonnet Max you're definitely better on Opus Xhigh.
        
        So my guess is that your best case would be Opus 5.5 driving Haiku 5.5. (Both on Xhigh or Max.)
        
        (\*) *In API prices, Sonnet 5.5 High is dominated by Sol 6.1 at Medium or above. But I assume most people wouldn't be using both APIs, and if they have subs to both you have to factor in the relative subsidies of each plan.*
      - **u/TronnaLegacy** (↑2, 2026-10-16 00:21): Today I tried just using Opus driving Sonnet and it felt better than my setup that used DS. Sonnet seems to finish plans quicker than DS did. Usually 2-3x faster.
          
          I'll give it a try with Opus driving Haiku x-high.
        - **u/TronnaLegacy** (↑1, 2026-10-16 05:36): Follow-up. A test project, specifically designed to have a few steps that were distinct from each other, worked well with Opus 5.5 driving a Haiku 5.5 xhigh subagent. Plans implemented by Haiku correctly.

---

## doesnt hurt to ask
**u/Intrepid-Scale-5962** · 2026-10-15 18:45 UTC · ↑0 · 6 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6tysq/doesnt_hurt_to_ask/)

hey guys, does anyone have a spare claude guest pass? been using chatgpt lately but want to try claude code before subscribing. if anyone has one available, id really appreciate it. thank you

**Comentarios:**

- **u/Strict-Prune-879** (↑3, 2026-10-15 18:47): 20 usd y a des centaines de personne qui demande ca tous les jours mais abonnez vous tester si ca ne va pas tu arrêtes!!!!
- **u/AdventurousArrival42** (↑2, 2026-10-15 18:50): Just try the free version. It comes with sonnet 5.5 and it actually gets stuff done without needing claude code.
  - **u/Mementem** (↑1, 2026-10-16 20:50): there is a free version?
- **u/xx_gamer_xx123321** (↑2, 2026-10-15 19:22): Why post on opencode sub?
- **u/AdFun4897** (↑1, 2026-10-15 19:26): Just switch to Claude. Way better usage than OpenAI and better models
- **u/bangsmackpow** (↑1, 2026-10-15 19:56): Add $10 to Zen and switch Models in opencode?

---

## Would anyone want if i make my vibecoded project open source.
**u/Gsport_hunter** · 2026-10-15 18:21 UTC · ↑1 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6tc03/would_anyone_want_if_i_make_my_vibecoded_project/)

So i created chrome agent like comet which does chrome task, answers the question and take control of browser.  
Tho there are lots of them that does same thing but i created this to solve this problems. 

1. I wanted to use opencode go, nvidia and openrouter apis  
2. In linux they dont have comet.

We can use free models, stores all data on browser other than apis and do lots of other things.  
Would anyone want that if i make it open source?

**Comentarios:**

- **u/Kayceepeece** (↑1, 2026-10-15 19:51): Yes I would want that thank you.
- **u/ANDALTUV** (↑1, 2026-10-15 21:04): just make sure the AI uses named variables and functions. Also tell it to not use abstractions, in that way any person could read the code easily...

---

## OpenCode support just landed in optimAIzr
**u/stichstichstich** · 2026-10-15 18:14 UTC · ↑5 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6t5as/opencode_support_just_landed_in_optimaizr/)

Built **optimAIzr** over the past few months, and it now supports OpenCode!

Track token usage, spot waste, find ways to save and much more.

Free, open source, local-first.

git: https://github.com/blendbunjaku/optimaizr

---

## DeepSeek 4.1 FREE
**u/Emotional-Bag-3754** · 2026-10-15 17:45 UTC · ↑188 · 22 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6se5m/deepseek_41_free/)

**Comentarios:**

- **u/Dry-Mathematician730** (↑2, 2026-10-15 18:01): I have used It for like 30 m and after that o can use anymore sadly
- **u/ramonvanraaij** (↑7, 2026-10-15 18:16): It is pretty much unusable, less than a 30 mins session and getting rate limited already after just one prompt (agentic coding task) is a joke.
  - **u/Ctbhatia** (↑1, 2026-10-15 19:22): the free lane has its own bucket, so a rate limit after one prompt is usually the shared pool rather than your own usage. a paid key skips that queue.
  - **u/Dushle** (↑3, 2026-10-15 20:49): Using for 10 hour I never hit the rate limit
  - **u/Amarsir** (↑1, 2026-10-15 21:20): Interesting. I've had it going on subagents for like an hour and it's still working. Not especially fast, but still churning out. Cat Jam gave me limits faster than this did.
      
      I'm still treating it as an experiment. For serious work I'll step up from free. But it's interesting to see different experiences.
    - **u/AdvisorLife4016** (↑1, 2026-10-16 03:13): Subagents?? As in, parallel requests? You're hammering a free service with subagents? Jesus Christ, this is why we can't have nice things for free. :(
      - **u/Amarsir** (↑2, 2026-10-16 04:02): Delegation and multitasking is kind of the point of going agentic. And doing the task in a way that finishes faster is not less "hammering" than doing the same tasks sequentially. I didn't say anything about keeping it going 24/7.
  - **u/Ok-Drawer5245** (↑1, 2026-10-16 06:47): Weird, if I use it (or any of the other free models) it takes 2-3 hours before I hit the limit. I find the limit very generous given its free. Consider how much cash you would need to spend on hardware to run it yourself..
      
      Remember you can come back later and resume your session
  - **u/ramonvanraaij** (↑1, 2026-10-16 15:47): Today it has been working without issues so far.
- **u/YoRt3m** (↑2, 2026-10-15 18:22): Unlike others commenting here, I'm using it for a while now since like 8 hours ago. works fine but slow.
  - **u/gamble4846** (↑1, 2026-10-15 19:22): same i was so confused are they using it incorrectly or something i've been using it all day finishing few personal projects not one time was i rate limited. I wanted to add it to omniroute first so i can continue to use the same combo's but couldnt so i am just using directly from opencode may be these guys are using something outside opencode?
    - **u/AdvisorLife4016** (↑1, 2026-10-16 03:08): Most people here are vibecoders running agents and subagents for hours on projects they neither understand nor need. They come back, throw away what they've generated, and start over. Basically, a token slot machine. I'm honestly impressed they managed to make it last 30 minutes.
        
        Give them 100x the quota and they'll burn through 100x the tokens. Just because they can.
      - **u/Odd_Abrocoma_8421** (↑1, 2026-10-16 10:32): I may agree with you for 90%+ people that's the case. But actually have a very big project and actual gigs.
- **u/Consistent-Rock-5350** (↑2, 2026-10-15 18:31): Altaaaa
- **u/Zeppon_ll** (↑1, 2026-10-15 18:39): There's no such thing as a free lunch
  - **u/Emotional-Bag-3754** (↑1, 2026-10-15 19:16): 🙊
- **u/eudaytrader** (↑1, 2026-10-15 19:29): Don’t see the quality in that one. Starting with an empty folder, 1 prompt to do research  in plan mode, writing out a PLAN.md, starting execution and within 3-4 rounds already the 200k context window is exhausted with barely any results, compaction and it begins to forget stuff. But so so many thoughts, endlessly running in loops. This is just as bad as one of the stealth models we had before.
- **u/soulevil** (↑1, 2026-10-15 21:30): So slow compared to other models, but nice to have
- **u/InternetExpensive584** (↑2, 2026-10-16 08:35): Only 200k context

---

## Is everything busted?
**u/barret232hxc** · 2026-10-15 17:43 UTC · ↑10 · 7 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6sbqu/is_everything_busted/)

I have opencode GO, I see these free models like step 5, longcat, cat jam free. I try one simple prompt and they say they are rate limited but I'm on the paid opencode go? I try to use zen with the free deepkseek flash 4.1 and all say they are rate limited it's like nothing that says it's free works for me? am I the only one?

When they had spacebunny free I used it 24/7 and it worked all the time no problem now these ones it's like nothing works?

**Comentarios:**

- **u/QuietPuddle27** (↑2, 2026-10-15 17:47): The confusing part is that Go and Zen aren’t necessarily the same access tier. A subscription doesn’t automatically remove rate limits imposed on individual models or endpoints.
  - **u/barret232hxc** (↑1, 2026-10-15 18:27): I see. I figured if i'm using go, it means it's good to go. like when they had space bunny free, on zen it would eventually say rate limit, but when I used it on go, I literally was using it all day for like 5 days zero problems it just worked like a champ while it was free on onpencode go.
    - **u/Amarsir** (↑1, 2026-10-15 21:12): Unfortunately it's all black box to us. We don't know how it works until we experience it. What the limits are, if they're hard limits or throttled, if it's shared across models ... all pretty unknown.  Free is a nice bonus but I can't rely on it.
- **u/alcogiggles** (↑1, 2026-10-15 19:03): I got the same problem.   
    My GO subscription just renewed last night.   
    I wake up and go to use Space Bunny, Big Pickle, and nothing works. Says I'm rate limited. WTF.
- **u/CharacterTension2896** (↑1, 2026-10-15 19:09): Hermes saw this and fixed it by reinstalling opencode and than check the model names in it.
- **u/sudoer777_** (↑1, 2026-10-15 20:11): I'm using Step 5 through Go and it works most of the time just extremely slowly, occasionally I get a rate limited message but it goes away. Similar situation with LongCat
  - **u/Railander** (↑1, 2026-10-16 09:41): yeah that one is both super slow and constant timeouts, but it does not seem to have a cap on usage. same case with longcat 2.5.

---

## 🔥 Meta is releasing Muse Spark Open (open-weight)
**u/afanasenka** · 2026-10-15 17:14 UTC · ↑83 · 18 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6rkni/meta_is_releasing_muse_spark_open_openweight/)

[https://research.meta.ai/blog/muse-spark-open](https://research.meta.ai/blog/muse-spark-open)

**Comentarios:**

- **u/migsperez** (↑12, 2026-10-15 17:27): Well done to Meta on this one.  I wonder if Anthropic and Openai will do the same in the future.
  - **u/MetalDeep329** (↑11, 2026-10-15 17:40): No they won't lmao, anthropic would rather dissolve than release a open weight model
    - **u/porkyminch** (↑1, 2026-10-15 21:24): Hate the weirdos that run that company but Opus 5.5 is too damn good right now.
    - **u/Ok-Drawer5245** (↑1, 2026-10-16 06:58): Which they will
  - **u/Grouchy-Stranger-306** (↑1, 2026-10-15 18:16): yeah they will definitely want to lose all their value for no reason
    - **u/migsperez** (↑2, 2026-10-15 18:17): Releasing older models wouldn't harm them.  Haiku 4.5 could be released, it's ancient now.
      - **u/borobinimbaba** (↑8, 2026-10-15 18:40): Why would they release a model to be beaten in every benchmark comparison?
          That would hurt their brand badly
      - **u/Amarsir** (↑3, 2026-10-15 20:22): The problem with that logic is that Anthropic has taken an attitude of "open weight is dangerous". (For Regulatory Capture of course.)
          
          So even a Haiku 4.5 - which I agree doesn't undermine their current offerings - would hurt that claim.
        - **u/Railander** (↑2, 2026-10-16 09:08): they should pretend dario never said that, it was so stupid and everyone could see it.
  - **u/Amarsir** (↑1, 2026-10-15 20:20): People forget they were early open-weight leaders with Llama. I understand wanting to compete against the closed-source frontier now, but it doesn't hurt to maintain their credentials here too.
  - **u/CrowdGoesWildWoooo** (↑1, 2026-10-16 10:50): Definitely not Anthropic, they are pretty anti open model. OpenAI seems like they are still chasing Anthropic lead. 
      
      Meta was farming good will from player when they came back with muse spark, giving away free tokens and then promised an open release.
      
      This might be their last release though as they’ve reached fromtier
- **u/warpaint_james** (↑3, 2026-10-15 18:54): > natively multimodal model with 816B total parameters (42B active) and a 1M-token context window
    
    Sounds great to me. I expect to see this up in a few model providers in the next few days. Hopefully we will see some impressive spin offs from this too
  - **u/Railander** (↑1, 2026-10-16 09:10): it's also AFAIK the smartest open multimodal model with audio and video reasoning.
- **u/crusaderky** (↑3, 2026-10-15 19:28): It's Muse spark 1.2 💩
  - **u/Railander** (↑1, 2026-10-16 09:11): where did you see that?
    - **u/Mean-Elk-9439** (↑1, 2026-10-16 12:57): Performance indicates it. It's worse than glm 5.3 in actual use cases and modern benches. Cheaper but no one is paying API costs that's sane.
- **u/arielif1** (↑1, 2026-10-16 14:05): it's ass and benches between 1 and 1.1, sometimes between 1.1 and 1.2. it's either nerfed or an intermediate checkpoint.
    
    it's also below dsv4.1flash at everything that doesn't involve knowledge work, so...
- **u/Mementem** (↑1, 2026-10-16 20:55): its not a bad model, just requires a TB of ram to run the FP8.  
    and also benchmaxxed.

---

## I just came back to OpenCode and why the f**k am I paying for Codex Pro 100? Can I generate images in OpenCode with an API (GPT image 2.5)?
**u/rjn2-8** · 2026-10-15 16:51 UTC · ↑7 · 21 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6qy1d/i_just_came_back_to_opencode_and_why_the_fk_am_i/)

Also, is there a way to select a part of the agent message and add it as a quote in the text field area?

**Comentarios:**

- **u/shtrjones87** (↑1, 2026-10-15 16:59): yeah deepseek 4.1 flash is actually pretty good. It says load bearing a lot though lol..
  - **u/rjn2-8** (↑1, 2026-10-15 17:00): Im using mimo v2.6 pro ultraspeed ! Same as Astra but wayyyyyyy faster !
  - **u/jaerie** (↑1, 2026-10-15 17:34): Hmm. Hmm... Hmm!!
  - **u/torrso** (↑2, 2026-10-15 18:16): [Loooaad bearing](https://www.youtube.com/watch?v=rK1NZ0X4rYQ)?
    - **u/shtrjones87** (↑1, 2026-10-15 19:51): this is a banger
      - **u/dandaman0000** (↑1, 2026-10-16 00:15): with a wide blast radius
- **u/Clockafter5** (↑1, 2026-10-15 17:01): Image generation through an API should be possible if the provider exposes the image model, but whether OpenCode supports it natively is a separate question. That’s the part I’d check first.
- **u/Ok-Cauliflower8805** (↑1, 2026-10-15 17:06): I've always struggled to get OpenCode to create an image in the chat in the same way as Codex can. But assuming you've given it access to local folders in a project and are using the right model which creates images, then it can create an image into the relevant folder directly.
    
    On a related topic, I've found that adding a suitable MCP server for computer use and a reliable browser plugin can bridge the gap to Codex and Claude Desktop.
  - **u/AnimusAstralis** (↑1, 2026-10-15 17:35): Claude? Images?
    - **u/Ok-Cauliflower8805** (↑1, 2026-10-15 17:44): Yes you’re correct!
      - **u/AnimusAstralis** (↑1, 2026-10-15 17:49): Claude doesn’t generate images
        - **u/Ok-Cauliflower8805** (↑1, 2026-10-15 18:04): Yes you’re correct
        - **u/taytay735** (↑1, 2026-10-16 06:12): I think he may be referring to code-based image generation. Eg creating a SVG image using Python, or like how you can prompt claude to create a flappy bird game and then take a screenshot of it.
  - **u/Railander** (↑1, 2026-10-16 09:43): what would that "suitable MCP server" be? why not would that just be included by default?
    - **u/Ok-Cauliflower8805** (↑1, 2026-10-16 09:51): Good question. I need to add several MCP servers to do tasks which are native in other apps.
      - **u/Railander** (↑1, 2026-10-16 09:53): such as?
        - **u/Ok-Cauliflower8805** (↑2, 2026-10-16 09:59): I personally use the Softarea MCP server to connect to Microsoft 365, and the Kimi-Cu server for computer control and the Tinyfish MCP server for web search. All on Github
            
            I have a couple for browser use, but I'm not sure these are needed much as native browser seems ok
- **u/kobraca** (↑1, 2026-10-15 17:23): If you have 12gb vram just install comfyui and generate your images locally. If not, still install comfyui and utilize your api key for cloud providers to generate images
  - **u/Amarsir** (↑1, 2026-10-15 22:01): There's something nice about local generation, but quantized models at slower speeds don't really compete.
      
      You have me intrigued about ComfyUI as a harness for cloud providers. What's the advantage there, fine-tuning and Loras?
- **u/taytay735** (↑1, 2026-10-16 06:08): For selecting part of the agent message and responding to it in the form of a quote, take a look at plannotator or plannotator-tui. There’s also opencode plugins for them for seamless integration.

---

## CODEX FOR CHROME DOWN
**u/Vast-Computer2787** · 2026-10-15 16:28 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6qbmy/codex_for_chrome_down/)

---

## DeepSeek V4.1 Flash is free on OpenCode: 5-model test (Oct 15)
**u/petburiraja** · 2026-10-15 15:45 UTC · ↑6 · 2 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6p6gz/deepseek_v41_flash_is_free_on_opencode_5model/)

I tested five free OpenCode models on Oct 15: two questions and one toy Python fix, one attempt per task.

Follow-up to my [Oct 8 test](https://www.reddit.com/r/opencode/comments/1x0kuv2/which_free_opencode_models_are_fast_reliable/).

| Oct 15 rank | Oct 8 rank | Model | Checks passed | Score /100 | Fix time |
|---:|---:|---|---:|---:|---:|
| 1 | new | DeepSeek V4.1 Flash Free | 3/3 | 100 | 21.9s |
| 2 | 2 | Muse Spark 1.3 Contributor Free | 3/3 | 94 | 29.9s |
| 3 | 1 | MiMo V2.6 Flash Free | 3/3 | 89 | 45.2s |
| 4 | 4 | LongCat 2.5 Preview Free | 3/3 | 87 | 61.0s |
| 5 | 3 | Space Bunny Free | 2/3 | 79 | 22.7s |

The four perfect-pass scores mainly separate latency. Oct 8 used different concurrency/settings, so these ranks cannot establish speed improvements or reliability.

Tests: daily-hazard probability, Fibonacci modulo 1,000,000,007, and a duration-parser/median fix. All five fixes passed the unchanged five-test file; Space Bunny's Fibonacci code did not parse.

Same score as Oct 8: floor(20 per correct question + 40 per accepted fix + 20 × fastest accepted fix time / model fix time).

OpenCode 1.18.35, serial runs in isolated synthetic repos. Fix time includes CLI startup and tool calls. I repaired a grader that rejected a valid exception constructor and rescored the saved answer; no model rerun.

[Free availability is temporary and data terms differ by model](https://opencode.ai/v2/docs/console/models/#free-models); contributor routes may use prompts for training.

**Comentarios:**

- **u/pikuray** (↑1, 2026-10-15 20:14): Anything with cat in the name is garbage. They are very fast. The fastest. but don't trust with anything complex.
- **u/CYCLONOUS_69** (↑1, 2026-10-15 21:50): Bro is doing lords work!

---

## The limits on free zen models.
**u/Odd_Abrocoma_8421** · 2026-10-15 14:43 UTC · ↑22 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6niob/the_limits_on_free_zen_models/)

I have now tried all free models and all return "Error: Rate limit exceeded. Please try again later."













































Don't mind my prompting, I have full on architecture .md by opus 5.5 and after 5 .md plans this is the state.

**Comentarios:**

- **u/EtadanikM** (↑3, 2026-10-15 14:49): Yes there is a global rate limit on free models; it's not that high.
  - **u/Aggravating-Push-207** (↑1, 2026-10-15 16:33): lmao i didn't even know the free models had a rate limit
- **u/qwertyyyyyyy116** (↑2, 2026-10-15 19:48): It's about 1$/day.  
    Multiply that by thousands to tens of thousands of users, and, that's a lot of money.
    
    It's pretty generous
- **u/Present_Carpenter912** (↑1, 2026-10-16 20:29): How do u get a graph like this
  - **u/Odd_Abrocoma_8421** (↑1, 2026-10-17 04:32): /stats

---

## deepseek-v4-1-pro spotted on opencode website
**u/Muted-Vermicelli3716** · 2026-10-15 14:42 UTC · ↑21 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6nhmn/deepseekv41pro_spotted_on_opencode_website/)

**Comentarios:**

- **u/Mementem** (↑1, 2026-10-15 17:00): no wonder deepseek was down yesterday!   
    and followed by opencode getting DS 4.1 flash!
    
    pro might drop this week the way things are going (massive amounts of cope)
- **u/0xbyt3** (↑2, 2026-10-15 21:55): Most likely false because once Opencode CEO stated that they list every model ID sent to their backend, even the fake/invalid ones.
- **u/gocchisama** (↑1, 2026-10-16 03:45): I use mostly Deepseek on Opencode go and I'm very excited to get an upgrade on all subject
- **u/eachDayIWakeUp** (↑1, 2026-10-16 21:59): NEXT FREE MODEL?? 🙏🙏🙏🙏
- **u/Evan_gaming1** (↑1, 2026-10-17 04:37): This is normal. They add a ton of models when they expect it to come out. This has been here for a while and there's pages like these for other models that don't exist yet.

---

## PSA: OpenCode’s free DeepSeek V4.1 Flash appears to have the same ~1M context window as the paid Go tier — I tested the boundary
**u/Square_Confection_62** · 2026-10-15 14:00 UTC · ↑99 · 13 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6mezp/psa_opencodes_free_deepseek_v41_flash_appears_to/)

I noticed something odd in OpenCode’s model metadata:

* `opencode/deepseek-v4.1-flash-free`: **200k context**
* `opencode-go/deepseek-v4.1-flash`: **1M context**

Both point to the same canonical model, `deepseek/deepseek-v4.1-flash`, so I wanted to find out whether the 200k limit on the free version was actually enforced by the inference backend or was just OpenCode catalog metadata.

It looks like it’s just metadata.

# What I tested

I temporarily overrode the free model’s local context limit in `opencode.json` so OpenCode itself wouldn’t compact at 200k, then sent increasingly large generated text files through both models.

The override only changes OpenCode’s local budgeting/compaction. It does **not** change whatever limit the server actually enforces.

Boundary results:

|Approx. message size|Free|Paid Go|
|:-|:-|:-|
|\~982k tokens|✅ OK|✅ OK|
|\~1.037M tokens|✅ OK|✅ OK|
|\~1.107M tokens|❌ HTTP 400|❌ HTTP 400|

So both versions crossed the supposed 200k free-tier limit by a huge margin and then hit essentially the same wall.

The OpenCode gateway unfortunately returns an empty 400 body at the limit, so I also sent an oversized request through the direct DeepSeek API.

That returned the useful part:

>This model's maximum context length is 1048576 tokens.

So the actual model ceiling is **1,048,576 tokens (2²⁰)**.

That lines up almost perfectly with OpenCode calling the paid model “1M”.

# Free vs paid performance

Since I already had the test setup running, I also compared the two tiers.

Large-context latency:

|Input|Free|Paid|
|:-|:-|:-|
|\~982k|26.0s|25.2s|
|\~1.037M|37.1s|32.6s|

These are single samples, so I wouldn’t read anything into the small difference. Both were in roughly the same \~30–40k tok/s prefill class.

For decode throughput, using temperature 0 and fixed \~800-token outputs:

* **Free:** \~113–121 tok/s across 4 samples
* **Paid:** \~102–120 tok/s across 2 clean samples

Again, effectively indistinguishable in this small test.

I also ran a deterministic five-question battery plus “first 100 decimals of pi” through both tiers at temperature 0.

The outputs were **byte-for-byte identical**. Token accounting was also effectively identical apart from prompt-cache hit distribution.

Reasoning variants work normally on the free model too. On the same multiplication task:

* `#low`: 70 reasoning tokens
* default: 228
* `#max`: 719

All three returned the correct answer.

# The config override

For testing I used:

    {
      "providers": {
        "opencode": {
          "models": {
            "deepseek-v4.1-flash-free": {
              "limit": {
                "context": 1000000,
                "output": 384000
              }
            }
          }
        }
      }
    }

Important: this does **not** magically increase the provider’s context window. It just tells OpenCode not to treat 200k as the local ceiling.

Also, I did **not** independently boundary-test a 384k generated output, so I’m specifically claiming the \~1M **context**finding here, not that every piece of the paid model’s metadata necessarily applies to the free endpoint.

# My conclusion

As far as I can tell, the `200000` context value on `deepseek-v4.1-flash-free` is stale/conservative catalog metadata rather than an actual free-tier serving restriction.

Everything I could measure black-box points to the free and paid endpoints exposing the same DeepSeek V4.1 Flash context capability:

* same \~1M context boundary
* same failure point
* same performance class
* same deterministic outputs
* same reasoning behavior

What this **doesn't** prove is that they use literally identical weights, quantization, hardware, or routing internally. You’d need information OpenCode doesn’t expose, such as useful logprobs or backend details, to establish that.

And obviously the free model is advertised as **free for a limited time**, so I wouldn’t build anything critical around its continued availability.

But if you’re using the free DeepSeek V4.1 Flash model in OpenCode and wondering why it says 200k: based on these tests, the backend itself appears capable of the full \~1M context window.

Would be interested if anyone else can reproduce the same boundary on their account.

**Comentarios:**

- **u/nantachapon** (↑9, 2026-10-15 14:33): What is the catch fellas
  - **u/Noob_prime** (↑11, 2026-10-15 14:40): Our data 🥱
    - **u/IAmFitzRoy** (↑9, 2026-10-15 14:54): It says this model will not train in our data.
        
        (Pinky promise 🫣)
      - **u/TheMythicSorcerer** (↑0, 2026-10-16 15:24): \*does not apply to the chinese data centers they actually run on becuase US laws are useless in china
  - **u/deleted-account69420** (↑4, 2026-10-15 14:43): That they can change anything server side at any point in time without any warning.  
      There might be a reason why they want a 200k cap on a free model.
    - **u/dumbasPL** (↑1, 2026-10-15 15:05): The reason is the instance is a lot cheaper. At the end of the day, money is what drives everything, and if enough people abuse this, they'll enforce it server side in no time.
      - **u/CampMaster69** (↑2, 2026-10-15 15:45): yeah mod please take down the post lol let the things be
- **u/PopandilaRO** (↑1, 2026-10-15 16:23): copied your .json and got stuck at 246.500 tokens with the following: "fetch \[method=GET, url=http://127.0.0.1.:49374/api/shell/\[id redacted for this comment\]"
- **u/Alive_Solution_689** (↑2, 2026-10-15 16:58): Nothing spectacular about this. 
    
    It's absolutely standard not only on openrouter to reduce both, input and output tokens in the model configuration. I do it myself often so auto-compact hits earlier as a 1M context is not only expensive baggage, results are also often deteriorating when context is growing to 1M unpruned. Model capability	is not equal to quality here.
- **u/justmaybe888** (↑1, 2026-10-15 17:15): Honestly, the most useful part is that you explained exactly what the config override does and doesn’t change. Too many ppl confuse the client-side limit with the server’s actual context window.
- **u/AffectionateBowl1633** (↑1, 2026-10-15 22:24): Did you just declare the loophole so OpenCode people will patch it later?
- **u/FavstianEquanimity** (↑1, 2026-10-16 04:07): My speculation: there is no real context gate on server end. It's only opencode cli/desktop client gating at 200k
    
    Edit: using zen's free deepseek v4.1 flash with 1M context window probably will trigger some misuse policies
- **u/Full_Hat_9683** (↑1, 2026-10-16 05:58): This was already an issue with the old free DeepSeek in OpenCode, same behavior. Hardcoding the context window to 1M fixes it.

---

## To Opencode team: Can you add option to select date range along with the existing 7, 30 and all time options.
**u/Ok_Cartographer5609** · 2026-10-15 13:18 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6lf2w/to_opencode_team_can_you_add_option_to_select/)

Title

---

## qwen3 keeps dumping its thinking into opencode's chat, so I wrote a plugin to split it out
**u/WeOfferTheSun** · 2026-10-15 12:20 UTC · ↑3 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6k59h/qwen3_keeps_dumping_its_thinking_into_opencodes/)

If you run qwen3 or another reasoning model through opencode, you've probably seen this: the chain of thought comes back inside the normal text channel, wrapped in \`\`. opencode stores that as a regular assistant message, so the reasoning gets glued onto the answer and the reasoning panel stays empty. The thinking is sitting right there in your transcript, mixed with the reply, and you can't collapse it.

I wrote a plugin for it.

It hooks `session.http.response`, which hands it the raw provider response before the provider driver parses it. It finds the tagged span and moves it from the content field into the chunk's reasoning field:

* streaming: `delta.content` → `delta.reasoning_content`
* non-streaming JSON: `message.content` → `message.reasoning_content`

opencode's drivers already read that field to build the reasoning part, so the thinking lands in the collapsible panel and the visible text is just the answer.

Install:

    opencode plugin add github:hussainbiedouh/opencode-think-splitter

Repo: [https://github.com/hussainbiedouh/opencode-think-splitter](https://github.com/hussainbiedouh/opencode-think-splitter)

Not on npm. I tried to publish and the registry rejected my token, so I didn't bother chasing it down. The GitHub install works because `dist/` is committed, so there's no build step.

Stuff I ran into while testing:

* Default tags are `think`, `thinking`, `thought`, `reasoning`, `reflection`. You can change the list or scope the plugin to specific provider ids.
* Tags that arrive split across two stream chunks are handled. An unclosed tag flushes its contents as reasoning when the stream ends.
* If a chunk already carries native reasoning, the moved text is appended instead of overwriting it.
* Needs the opencode **V2** plugin API.
* Don't run it twice. If you had it as a local file plugin, delete that copy. Same plugin id, and only one instance registers, so you might be running the wrong one and not notice.
* Some providers are strict about `reasoning_content` being echoed back on the next request. If a provider starts erroring after a rewrite, scope the plugin away from it with `options.providers`.

One thing for anyone else publishing an opencode plugin: I lost a while to `git dep preparation failed` on install. Turns out pacote runs a full `npm install` on a git dependency if your package.json has any of `postinstall`, `preinstall`, `install`, `prepack`, `prepare`, or `build` in `scripts`. opencode's bundled runtime passes a broken `npmBin` to that step, so it always fails. I renamed my build script and it installed first try. If `opencode plugin add github:you/thing` won't install, check your script names before anything else.

**Comentarios:**

- **u/TopEntity** (↑1, 2026-10-15 16:02): Isn’t Qwen 3 outdated?
  - **u/WeOfferTheSun** (↑1, 2026-10-15 19:21): I don't need to use Fable 5.1 to format a markdown file!
    - **u/TopEntity** (↑1, 2026-10-15 19:22): No, I mean there are open much newer models that are capable of doing that.
        
        For eg ornith 1.5 9B works fine for me
      - **u/WeOfferTheSun** (↑1, 2026-10-15 21:46): I agree on that. It was just an example. The real issue is for a good portion self-hosted models, I've been facing the same issue of spitting thinking in final response. There is even an open issue about that on OC github, so thought of developing this plug-in.
        - **u/TopEntity** (↑1, 2026-10-16 01:34): Oh sorry I am not aware of that.

---

## Is the free Deepseek 4.1 flash the exact model with go sub?
**u/Zoro-chi** · 2026-10-15 12:12 UTC · ↑9 · 24 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6jzmr/is_the_free_deepseek_41_flash_the_exact_model/)

What’s the catch? Is the model a lower quant? Lower requests to the model than the go plan? What’s the catch guys?

Edit: Answer on the post states it has a 200k context window

**Comentarios:**

- **u/PerfectReflection155** (↑1, 2026-10-15 12:14): Where is it free? I don’t think it’s free anywhere currently
  - **u/Zoro-chi** (↑1, 2026-10-15 12:16): There’s a free version called Deepseek V4.1 flash free on the opencode cli
    - **u/PerfectReflection155** (↑3, 2026-10-15 12:32): Damn you are right. Well I guess I’m about to find out how fast I hit the limit on it. 
        
        The difference I noticed is limited context 200k vs 1m but that’s not really a major
- **u/Strict-Prune-879** (↑3, 2026-10-15 12:19): fenêtre 200k attention
  - **u/Zoro-chi** (↑2, 2026-10-15 12:23): Oh okay, so instead of 1M context it’s a 200k context. Got it
    - **u/Strict-Prune-879** (↑2, 2026-10-15 12:44): c'est souvent comme ca en free après normalement il devrait etre pareil
- **u/Sea-Dimension-1097** (↑2, 2026-10-15 12:20): Still I am testing the model, and it seems to be giving responses really quickly, and even tried fetching the docs, no mention of quant.
  - **u/Zoro-chi** (↑1, 2026-10-15 12:22): Share your updates here after testing please
    - **u/Sea-Dimension-1097** (↑1, 2026-10-15 12:42): Yea sure
      - **u/XL-Dildo-Brazilian** (↑1, 2026-10-15 13:10): i cant see deepseek 4.1, it shows to me openrouter one which is paid, the free version of opencode i cant see it. any help please? thanks
        - **u/Sea-Dimension-1097** (↑1, 2026-10-15 13:28): first go to the website to confirm in the zen section search for deepseek and if its there, then restart opencode cli
          - **u/XL-Dildo-Brazilian** (↑0, 2026-10-16 05:53): thx
        - **u/Meandernder** (↑1, 2026-10-15 13:28): Restart opencode or ask your model to refresh the models list or use the opencode command
          - **u/XL-Dildo-Brazilian** (↑1, 2026-10-16 05:53): thx
    - **u/Sea-Dimension-1097** (↑1, 2026-10-15 13:49): Usage limits were not good in max even being a effecient model didnt really last a lot, but actually whatever tasks i gave it to do it did it, but just the guidance needed for it should be given, it doesnt figure things out correctly.
- **u/YoRt3m** (↑2, 2026-10-15 12:30): From what I experience is that it's much slower, besides the smaller context. but performance seems to be similar.
  - **u/nicktohzyu** (↑1, 2026-10-15 13:27): It’s very fast for me. Can’t speak for performance though
- **u/binhex01** (↑4, 2026-10-15 13:01): Perfect for sub agent work!, i dont need a large context, cheers opencode.
- **u/XL-Dildo-Brazilian** (↑1, 2026-10-15 13:10): i cant see deepseek 4.1, it shows to me openrouter one which is paid, the free version of opencode i cant see it. any help please? thanks
  - **u/Zoro-chi** (↑1, 2026-10-15 13:18): Refresh the opencode model list. The model name is Deepseek V4.1 flash free
    - **u/XL-Dildo-Brazilian** (↑1, 2026-10-16 05:54): thx
- **u/Mementem** (↑1, 2026-10-15 14:05): it is slower and in my experience seems dumber too? but that can't confirm anything yet.  
    also the context is smaller, criminally so.   
    200k will end in a few prompts lol
- **u/EtadanikM** (↑1, 2026-10-15 14:12): You have an overall free model rate limit that it eats into. I’d estimate about 3-4 hours of continuous work a day before you reach it. 
    
    Also it’s not true that open code is the only vendor offering it; free buff also offers it in their free tier about ~10 hours of usage a day.
- **u/tinyparkingLOT** (↑1, 2026-10-15 15:38): Same model name doesn’t always mean identical access or serving conditions. I’d want confirmation from the provider before assuming the free and Go versions are completely identical.

---

## AI Coding Workflow if I can't afford frontier models
**u/Sorry-Tomato-7141** · 2026-10-15 12:00 UTC · ↑7 · 15 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6jr9p/ai_coding_workflow_if_i_cant_afford_frontier/)

If you're only in the vibe coding bubble, please don't answer this. I'm a software engineer who wants to make real, complex systems using AI wherever it can help me. I only have the free models that come with opencode zen, and maybe some chat models like Qwen, Kimi and free versions of chatgpt, gemini, claude, etc. 

I want to know what I can do with only these, without having to spend money on LLMs. I realize that this means I have to do more by myself in the planning side of things as I can't delegate planning to LLMs, which is how I believe coding should be anyway so it's not a problem.

I really like Matt Pocock's skills but I have found that his workflow only really works if you have frontier models, as free models aren't very good at grilling or planning. 

So what I need is a reproducible AI coding workflow that I can use to approach my projects using only the free, limited AI. Please highlight which parts of the process I need to do by myself, and which parts I can assign to which model. 

I realize that the smarter your LLMs are, the more you can stray from traditional software engineering, so please tell me what I can realistically accomplish perfectly with AI. The parts that AI cannot do properly, I will do by myself.

**Comentarios:**

- **u/PerfectReflection155** (↑1, 2026-10-15 12:11): Search free Claude code on git hub. Sign up those 4 APIs. Personally I signed up to a couple of them twice which is probably against tos. Then also sign up to freebuff.  
    Then use those alongside opencode zen and open router.
  - **u/Ctbhatia** (↑1, 2026-10-15 18:25): signing up twice for the same free tier is the risky one, when they catch it every key from that provider goes at once. one account each is the safer spread.
- **u/ramendik** (↑9, 2026-10-15 12:25): Here's what I do in personal OpenCode - and found it to be less erratic than what I did at work with Claude Code, which had better models.
    
    Mindset: The last 20+ years were a mistake. Agile could never scale beyond experiments in small teams. An explainable mistake though - for human ciders working on a spec then sticking to it is emotionally hard. Robots don't have this oroblem.
    
    You are back at Waterfall. Spec driven development is bacj.
    
    First you work in one session to produce a spec. The session can spawn subagents to do research..it is not allowed to write any production code. (My current process still bleeds snippets into the spec but I am looking to see how to eliminate them, though SQL might be worth keeping). The apex is committed to the repo.
    
    Then you REVIEW THE SPEC. On your own, every line, not a model in sight. You edit what you can clearly change, you create a questions file for what you need to cycle with the model. You commit this work, and work with the model to resolve the questions. You review all spec changes it commits.
    
    You also get it to create a spec for testing and ideally review that too.
    
    Once all the specs are committed and you have approved them, you create a fresh session and tell it to implement the spec. The original session gets to review the code, but you do not let it change the code - only the development session changes the code.
    
    Then yet another session does the tests and any necessary fixes. You can use the original session to run deep dives into test failures that the testing session can't trace - but again the code is never touched directly by the original session.
    
    I am still polishing this approach and I need to see which of these can be subagents (for now I do let the sessions spawn subagents but the coding and testing are manually started sessions as I like them to be interactive, which also means I don't see how to refine this into a skill).
    
    I use GLM 5.3 Flash (on $10 Go)  for the main sessions, Muse 1.3 Contributor (free on Zen) for all other sessions and all subagents.
  - **u/Sorry-Tomato-7141** (↑1, 2026-10-15 12:37): Dude thanks for this! Do u have any skills that make this process better?
    - **u/maqifrnswa** (↑2, 2026-10-15 12:50): This is what I do too. Oh my opencode slim essentially has that flow built in as "/deepwork" and/or "/interview"
      - **u/ramendik** (↑1, 2026-10-15 22:34): What's slim?
    - **u/ramendik** (↑2, 2026-10-15 22:34): Not yet, and I need to research the existing ones before deciding if I want to adapt them or to make my own. I don't think a single skill can cover multiple interactive agents, but a set of skills is doable - but might have been done already.
  - **u/aarz03** (↑1, 2026-10-15 14:30): i do something similar,. i start in chatgpt with all context dumps, optionally deep research if it involves an unfamiliar framework. do some back and forth then have it generate a spec/handoff based on size and complexity. then i review and break it into multiple dev phases. develop->ai test->manual review->loop for all phases. each phase in a new chat such it works fine even with 200k context models without compaction. i like how you use the main session for reviews might give that a try :)
    - **u/ramendik** (↑1, 2026-10-15 22:35): I'm not sure if review inside a ChatGPT web session would work, but then again I'm not sure it wouldn't:)
        
        I personally currently like to chat to GLM 5.3 Flash. But that's just me.
  - **u/baschny** (↑1, 2026-10-15 17:58): Basically:  
      \* grill-me (settle on what has to be done, without any unclear points)  
      \* to-spec (make it write down as a concise spec)  
      \* implement  
      \* review
      
      The Matt Pocock skills are ideal for this.
      
      What you missed after "to-spec" is "to-tickets": the spec can be huge! Let it split it up in slices (tickets, can me simple tmp/\*.md files). Then tell it to orchestrate subagents to work on each of these slices, you can even make parallel work and ask him to choose "cheaper" models per slice.
      
      The advantage is: context window is kept at sane levels, you can use cheaper models for "cheap implementation tasks", etc.
    - **u/ramendik** (↑1, 2026-10-15 22:32): Thanks, I'll look up the Matt Pocock skills. I'm not sure how how to separate grill-me from to-spex cleanly; but there has to be a context switch after to-spec, and in your version after to-tickets too (I didn't go that big yet).
        
        I like review in the context where spec was, but I guess this might not always be feasible.
        
        The thing I am actually developing right now is about keeping context reasonable, but I'm not ready to publish yet. The main gain so far is from stropping reasoning from 5 turns old (turns not calls), this works on GLM and does not work on Muse as Muse keeps reasoning server side.
- **u/alexwwang** (↑1, 2026-10-15 14:18): Using gpt with GitHub in browser and get almost unlimited tokens.
- **u/tinyparkingLOT** (↑1, 2026-10-15 17:44): Tests are probably your biggest force multiplier here. Write the requirements and acceptance tests yourself, let the model implement one piece at a time, then make it fix whatever the tests catch. You don’t need a frontier model for that loop.
- **u/Railander** (↑1, 2026-10-16 09:46): usage on the free models is very limited for real work, so you won't go very far without paying.

---

## Round Of Applause to Opencode.
**u/Valuable-Mirror-448** · 2026-10-15 11:13 UTC · ↑102 · 19 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6ivix/round_of_applause_to_opencode/)

Can we all agree that opencode is the best gateway? Genuinely providing us with extremely good model's and even free users get incredibly preforming model's like Deepseek V4.1 Flash.

**Comentarios:**

- **u/Practical-Shoe2815** (↑6, 2026-10-15 11:13): I love opencode
  - **u/IAmFitzRoy** (↑3, 2026-10-15 14:41): lol.  I find it funny that we hated OpenCode when they stopped giving DS for free. 
      
      And now we love it.
    - **u/DebosBeachCruiser** (↑6, 2026-10-15 18:16): 
        >And now we love it.
        
        Because they started giving away DS for free again.
      - **u/IAmFitzRoy** (↑0, 2026-10-15 18:57): Wow. We have captain obvious here 🧑‍✈️
- **u/CheesecakeLivid9791** (↑1, 2026-10-15 13:00): I used DeepSeek as how I used other models hot rate limited 😭
- **u/SpectyteCovelight** (↑1, 2026-10-15 13:45): I love you so much Open Code 
    
    I’ve created so many apps with your models
- **u/zenkov** (↑-1, 2026-10-15 13:46): They push their half-baked agent harness way too aggressively, and the website they vibe-coded using their own free models is just downright disrespectful to users. Other than that, they seem pretty decent in their niche.
- **u/Mementem** (↑2, 2026-10-15 14:06): they are very fast with bringing new models!  
    i have used so many stealth models on opencode, that otherwise i wouldn't even know about
- **u/ozguru** (↑2, 2026-10-15 14:10): With one gltich freemodels only available in opencode app. It was available to all, policy has changed.
- **u/simo025** (↑1, 2026-10-15 16:11): i love opencode too :D
- **u/WeekendCereal** (↑3, 2026-10-15 17:36): The best part isn’t even just the free models, it’s being able to switch between providers without rebuilding your entire workflow every time.
- **u/clduab11** (↑1, 2026-10-15 19:30): ~~I love it, but did not love the hypocrisy of them yanking the ability to have their endpoints to be used in other harnesses, when even OpenAI allows Codex models to be used on OpenCode’s harness.~~
    
    ~~That move didn’t thrill me, and as such, OpenCode has now been relegated to my backup.~~
    
    EDIT: This only applies to free models, so I walk back some of the criticism.
  - **u/xmsxms** (↑2, 2026-10-15 20:08): They do allow it, just not the free models
    - **u/clduab11** (↑1, 2026-10-15 20:46): Fair point; I didn't read it closely enough and just tried with a paid model and it worked fine.
        
        Still doesn't *thrill* me per se, but a lot happier it's only the free models that this applies to.
      - **u/xmsxms** (↑1, 2026-10-15 21:07): You may have confused it with the command code $1 plan which does this. But either way, you can use the models with 9router which cloaks the client, albeit may violate the TOS and is a constant game of cat and mouse.
- **u/bangsmackpow** (↑3, 2026-10-15 19:51): I use Opencode almost exclusively. I have it configured to do exactly what I want/need and within my monthly budget which gets bigger with every successful project I do.
- **u/BoatZealousideal4521** (↑1, 2026-10-16 03:40): Well the USP of open code. God bless them. Providing affordable access to good LLMs really takes some efforts and good business tactics.
- **u/Railander** (↑1, 2026-10-16 09:36): they're afaik the only harness that allows for split integration between windows desktop GUI and operating agents within WSL, which to me is incredible for the best agentic capabilities while minimizing risks to my own system.
    
    as long as they're the only ones that do this i find it unlikely that i'd use something else.
- **u/Ok-Drawer5245** (↑1, 2026-10-16 10:55): I love opencode, I just don't understand how they make money

---

## New model will be released soon
**u/Different_Change6591** · 2026-10-15 09:35 UTC · ↑12 · 8 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6h7nv/new_model_will_be_released_soon/)

**Comentarios:**

- **u/AdFun4897** (↑1, 2026-10-16 03:57): Which one?
  - **u/PanPanForReal** (↑1, 2026-10-16 06:10): DeepSeek 4.1 pro
  - **u/Different_Change6591** (↑1, 2026-10-16 08:26): for maybe v.2 fash ?
    - **u/AdFun4897** (↑1, 2026-10-16 15:54): What the hell is that
      - **u/Different_Change6591** (↑1, 2026-10-16 17:10): deepseek v4.2 flash or maybe 4.5
      - **u/SpecialistOk6226** (↑1, 2026-10-17 11:15): V4.1 means it's have vision.
    - **u/SpecialistOk6226** (↑1, 2026-10-17 10:20): V4.1 pro or v5.
      - **u/Different_Change6591** (↑1, 2026-10-17 10:28): Its released today DeepseekV4.1 Flash- 1017
- **u/Orchicon** (↑1, 2026-10-16 17:06): That post was someone's guess
  - **u/Different_Change6591** (↑1, 2026-10-16 17:09): i dont think so !
    - **u/Orchicon** (↑1, 2026-10-16 17:31): Yes. Their claim was because there is a free version of DeepSeek in opencode then that means a new model is coming. Others have said that free version is a self hosted quant of DeepSeek which has nothing to do with Deepseek itself.

---

## Using OpenCode free tier in Claude Code
**u/Sea-Dimension-1097** · 2026-10-15 09:25 UTC · ↑0 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6h2ed/using_opencode_free_tier_in_claude_code/)

Is there any way that we can use OpenCode free tier of models in Claude Code?

**Comentarios:**

- **u/Atretador** (↑1, 2026-10-15 09:44): yes, but you shouldnt.
    
    opencode zen needs specific headers, which a proxy could provide - and would probably get you banned.
    
    but, there is very little reason to do that when OpenCode is as good if not better than claude on most cases.
  - **u/Sea-Dimension-1097** (↑1, 2026-10-15 12:45): Yea I even asked other ai models to give me instructions and it didn't work, but I was looking at that option bcz of the output Space Bunny free was giving me using the opencode cli, like claude automatically went on a hardcore verification loops, but my opencode did none so i had to manually ask it to do them and ended up using up my usage for that.
    - **u/Atretador** (↑1, 2026-10-15 13:13): thats skill issue, I mean literally, claude code has like 25K tokens worth of instructions. OpenCode out of the box has bout 14K
        
        I can recommend [**https://github.com/alvinunreal/oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim) **with /deepwork skill**
      - **u/Sea-Dimension-1097** (↑1, 2026-10-15 13:27): thanks man,

---

## DeepSeek V4.1 Flash is available for FREE
**u/CoffeeTea021** · 2026-10-15 09:10 UTC · ↑97 · 34 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6gt2y/deepseek_v41_flash_is_available_for_free/)

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
        - **u/BigPlebeian** (↑1, 2026-10-16 15:45): Also does anyone actually believe any of the big tech companies are keeping your data safe from the world?  I sure wouldn't.
  - **u/BigPlebeian** (↑1, 2026-10-16 15:43): If you trust a zero retention policy with any big tech company you are brain dead tbh.
- **u/Original_Goznab** (↑3, 2026-10-15 09:16): I'm so excited.
- **u/lustyphilosopher** (↑6, 2026-10-15 09:18): Do I need to restart my session Or something? Or is this only for v2 users? I've only used DeepSeek and I'm already at 11% of my 5hr window
  - **u/Fabulous-Ladder3267** (↑2, 2026-10-15 10:20): Might need chamge the model that has Free label on it
    - **u/BatNo7925** (↑1, 2026-10-15 12:30): You should be using DeepSeek V4.1 Flash Free. I think it works the same as before: giving each user a small quota to use, which is already great. Although when I first heard the news, I also thought it was similar to Anonymous Model -> ∞, but that's unlikely—all users would abuse it until it went bankrupt.
- **u/NinjaAlaska** (↑3, 2026-10-15 09:23): insane working too lol thx
- **u/IlNaka** (↑4, 2026-10-15 10:11): Limited time and "limited usage" with only 200K context instead of 1M
  - **u/BatNo7925** (↑0, 2026-10-15 12:33): That's the truth. I also thought a free lunch had come along, but I was mistaken. No company would make a completely unlimited free offer and bankrupt itself.
    - **u/BigPlebeian** (↑1, 2026-10-16 15:41): I mean working efficently and being smart with compacting still works pretty well.  Is it 1 mil... No but for free it's damn good.  It won't always be like this.
      - **u/BatNo7925** (↑1, 2026-10-16 18:50): I agree with you. Normally we don't use 1 million tokens; usually 256k is already enough. 1M just makes us more relaxed and lets us ignore boundaries, and sometimes abusing it can actually cause an LLM's attention to suddenly collapse, especially where the content contains contradictions and similar terminology. I think carefully orchestrating the work is an important survival skill for us original carbon-based programmers.
        - **u/BigPlebeian** (↑1, 2026-10-16 19:25): Do you have any tricks you use to reduce context used during a project?  I try to come back succession whenever I finish a specific class but definitely find myself maxing out the 200 like you said.  But I'm guessing that's more of a skill issue on my end.
- **u/Fabiox08** (↑1, 2026-10-15 10:28): Yeah! I'm using it now! I don't know if Big Pickle is still better/same or worst than DeepSeek V4.1 Flash.  
    What's your opinion?
- **u/direcirculationissue** (↑1, 2026-10-15 12:05): better or worse than muse spark 1.3?
  - **u/CampMaster69** (↑3, 2026-10-15 12:11): spark is meh. it does the job but it doesn't display too much intelligence, rather grunt work with all edge cases considered. deepseek is not too far ahead to be honest, but still a wee bit better. 
      
        
      heck i feel that 3.8 flash on antigravity has a lot more life.
    - **u/RoundZookeepergame2** (↑0, 2026-10-15 12:35): What a joke comment
  - **u/Odd_Abrocoma_8421** (↑1, 2026-10-15 14:31): no limits
  - **u/Amarsir** (↑1, 2026-10-15 19:54): In terms of free or in terms of model quality?
      
      They're pretty comparable in terms of intelligence, but Muse Spark seems a bit better at overview and visual design, whereas DS 4.1 Flash is re reliable at code quality.
      
      As far as what you get for free, it's a little early to say but I haven't hit unreasonable limits on either.
    - **u/BigPlebeian** (↑1, 2026-10-16 15:40): I've been using 4.1 for two days straight on multiple projects and it's been seemingly the same exact speed and quality of the paid 4.1 API I normally use. 
        
        Pretty sweet!
- **u/Cyvster** (↑2, 2026-10-15 12:30): i don't see any deepseek listed as free
  - **u/ManufacturerSweet422** (↑1, 2026-10-15 18:49): Check again. I've seen it's now available
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
    - **u/BrownCarter** (↑1, 2026-10-15 15:48): hmm am getting property options not allowed
- **u/dwky11** (↑1, 2026-10-15 13:39): I don't see it yet in my OpenCode models option.
  - **u/BatNo7925** (↑1, 2026-10-16 18:51): You can absolutely run \`opencode models --refresh\`.
- **u/Sir-Draco** (↑2, 2026-10-15 14:06): I think I’d rather pay for it if they are using a quantized version instead of full weights. It is already cheap. I would like to use it as intended
- **u/shtrjones87** (↑1, 2026-10-15 16:54): okay how does that apply to paid go users ?
- **u/Dazzling-Toe9614** (↑1, 2026-10-15 21:01): I haven't seen it. But still enjoying mimo
- **u/Ill-Ear-8763** (↑3, 2026-10-15 10:23): Thank you so much we can use your affiliate link... /s
  - **u/Dry_Cantaloupe4349** (↑1, 2026-10-15 10:37): You don't have to, its not like I get money from it, just a bit of extra credits. Just remove the code if you don't like it.
- **u/Fabiox08** (↑1, 2026-10-15 10:29): Question: Is it free?
  - **u/Dry_Cantaloupe4349** (↑1, 2026-10-15 10:37): Completely

---

## Opencode Zen not Working anymore in 9Router?
**u/devallerie** · 2026-10-15 08:21 UTC · ↑1 · 1 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6g22u/opencode_zen_not_working_anymore_in_9router/)

**Comentarios:**

- **u/ATyp3** (↑1, 2026-10-15 08:49): Not working in Paseo for iPhone either what the fuckkkk

---

## Opencode Zen not working anymore in 9router?
**u/devallerie** · 2026-10-15 08:20 UTC · ↑1 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6g1ec/opencode_zen_not_working_anymore_in_9router/)

---

## Deepseek is so slow nowadays
**u/Eastern-Passage629** · 2026-10-15 08:00 UTC · ↑7 · 5 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6fqd0/deepseek_is_so_slow_nowadays/)

Until about a week ago, I was able to reach speeds of 300 tokens per second, but now the maximum is 100, and at certain times it even drops to 50. Yes, I know a lot more users have started using it, but can’t this be improved? Why isn’t the service we’re paying for consistent? At the very least, it should stay reliable. Dropping from 300 to 50 is ridiculous.

**Comentarios:**

- **u/ItzHolmes-** (↑3, 2026-10-15 08:03): Will be still slow now considering its freee
  - **u/Strict-Prune-879** (↑2, 2026-10-15 08:07): ou c'est gratuit????
- **u/imoshudu** (↑1, 2026-10-15 08:58): Opencode go is slowseek.
    
    Commandcode goat keeps deepseek speed up. 
    
    I regret paying for the former. That's before we speak about other providers.
- **u/Professional_Price89** (↑1, 2026-10-15 17:28): They hosting the model themself slowly with outdated hardware, while deepseek direct api is fking fast.

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
**u/afanasenka** · 2026-10-15 07:47 UTC · ↑1436 · 196 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6fj9m/deepseek_v41_flash_is_free_in_opencode/)

**Comentarios:**

- **u/Artium99** (↑25, 2026-10-15 07:49): How???
  - **u/Melodic-Leather-5170** (↑60, 2026-10-15 08:01): you are the product
    - **u/Familiar-Ear-1223** (↑4, 2026-10-15 10:19): We better off using ollama 20$ for privacy sake
    - **u/Old-Juggernut-101** (↑4, 2026-10-15 12:09): Honestly, I don't care. I've don't nothing of significance that csn be stolen. I am a mere student. Ill take being thr product lol
      - **u/InsideTraditional187** (↑2, 2026-10-15 16:49): Maybe AI will not be harmful for you but also think what is they sell the stolen data? Buyer can definately tricks you from thay data. Even a single info on the internet can become weapon against you.
    - **u/NMiguelCosta-PT** (↑11, 2026-10-15 12:17): ChatGPT/Claude users have literally had their private conversations reported to the police over potential crimes and illegal behavior, and these companies have also stolen scientists' research. You're really naive if you think these big companies aren't stealing your data just because you pay them, as if they're under any moral obligation to respect your privacy after stealing the entire world's intellectual property while governments basically let AI labs do whatever they want. You're ALWAYS the product.
      - **u/mtftl** (↑4, 2026-10-15 14:40): This has to be the permanent mindset using any cloud AI inference. Everyone is playing this game. The only consideration is how comfortable you are with a third party knowing what you request and your patterns of requesting it, then deciding how to proceed.
        - **u/DrPfTNTRedstone** (↑1, 2026-10-15 15:12): Well no, there is companies, like ollama that are only in the inference business, so don’t use it for training. Some also have decent enough privacy policies.
  - **u/xatey93152** (↑1, 2026-10-15 08:06): Wrapper of free model
  - **u/xRebellion_** (↑16, 2026-10-15 08:10): Free models trade your usage for training data, of course use it only if you don't mind that.
    - **u/NMiguelCosta-PT** (↑10, 2026-10-15 12:18): Imagine thinking only free models do that lol
      - **u/xRebellion_** (↑1, 2026-10-15 12:21): That's why local models are the way to go. Sadly it's only accessible for those who has beefy GPUs with high VRAMs right now.
        - **u/XL-Dildo-Brazilian** (↑1, 2026-10-15 13:09): how much vram we need to run deep seek 4.1 or mimo 2.6 flash locally? can we mix 96GB vram and dram? say my dram is 128GB and vram is 96GB, 96gb isnt enough i assume so we gotta use dram to fill the other gap?
          - **u/SommerBlau67** (↑4, 2026-10-15 13:26): bro to run deepseek you'll need a few GPUs, it takes like 1664Gb in VRAM
            - **u/XL-Dildo-Brazilian** (↑1, 2026-10-16 05:54): what best model for 96gb vram
              - **u/SommerBlau67** (↑1, 2026-10-16 14:06): yes
                - **u/XL-Dildo-Brazilian** (↑1, 2026-10-16 17:52): hi, may you please explain what you mean by yes? i need details if possible
                    
                    thanks!
    - **u/no-name-here** (↑1, 2026-10-17 17:47): >Free models trade your usage for training data
        
        That does not seem to be true -- they explicitly say the exact opposite: "DeepSeek V4.1 Flash Free … follows a zero-retention policy and does not use your data for model training." [https://opencode.ai/v2/docs/console/models/#free-models:\~:text=DeepSeek%20V4.1%20Flash%20Free%20is%20free%20on%20OpenCode%20for%20a%20limited%20time.%20Its%20provider%20follows%20a%20zero%2Dretention%20policy%20and%20does%20not%20use%20your%20data%20for%20model%20training](https://opencode.ai/v2/docs/console/models/#free-models:~:text=DeepSeek%20V4.1%20Flash%20Free%20is%20free%20on%20OpenCode%20for%20a%20limited%20time.%20Its%20provider%20follows%20a%20zero%2Dretention%20policy%20and%20does%20not%20use%20your%20data%20for%20model%20training).
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
        - **u/starsonmydoubler** (↑1, 2026-10-17 17:49): I’ve used 5.28b tokens reverse engineering a quarter of two games in the past 4 days.
      - **u/squirrelscrush** (↑5, 2026-10-15 13:26): If you're using so many tokens, it's better to just get a Claude Pro subscription lol
        - **u/box_of_hornets** (↑1, 2026-10-15 14:45): I ran the numbers and would need 4 max subscriptions - it would cut my bill in half actually, if I could do that, but Anthropic specifically forbid running agent fleets on subscriptions and detect and kill subscriptions when they see the activity (from what I see on the internet)
          - **u/jonahgoldwastaken** (↑2, 2026-10-15 15:08): What inconceivable garbage are you building where you need 4 Claude max subscriptions to meet your token usage?
            - **u/box_of_hornets** (↑5, 2026-10-15 15:13): haha why must it be garbage? Over 40% of the token cost is on the review loop so it's actually costing a lot _because_ it's prioritising quality
          - **u/After-Blueberry3608** (↑1, 2026-10-16 02:09): I run agent fleets just fine on my Claude sub (locally). If you have your agents running from a VPS then yes you’ll get banned
          - **u/Brief_Dirt7479** (↑2, 2026-10-16 10:48): Maybe your whole calculation uses Opus or Fable. Orchestrating with a combination of Haiku 5.5 and Sonnet 5.5 as well as Opus would cost arount 2-3x of DeepSeek v4.1 alone, which is well under a single Claude Max usage. And since you told that quality is a priority, the economy shifts towards larger models which give better quality/cost on harder tasks. 
              
              Or you could combine a Claude Max sub with ChatGPT Pro 200 with Claude as planner/implementer and GPT as reviewer.
  - **u/zyxciss** (↑1, 2026-10-15 15:52): well free version has a context of 200k , better to use Muse Spark 1.3 , that's the best for me
    - **u/TronnaLegacy** (↑1, 2026-10-15 17:27): 200k is fine for my use case. I use it as a subagent, orchestrated by Claude.
- **u/EstablishmentAny4525** (↑1, 2026-10-15 08:57): This is mind blowing. My favourite model that I love paying for is now free!
- **u/citizenjc** (↑1, 2026-10-15 09:22): I'd this true at all? Just tested, no dice
- **u/trashbytes** (↑1, 2026-10-15 09:24): Can we use it with other harnesses like Hermes Agent for example? Don't seem to be able to select it there.
  - **u/jakobwells** (↑2, 2026-10-15 11:21): Free models are restricted to use in OpenCode.
    - **u/trashbytes** (↑3, 2026-10-15 11:31): Thank you! That confirms it.
    - **u/NMiguelCosta-PT** (↑1, 2026-10-15 12:22): No, they're not. I have used them in Codex in the past with codex-router and there's many other ways to use them in any harness.
      - **u/GoldPossession7284** (↑1, 2026-10-15 13:13): as políticas novas deles proibem que você use, esse é o ponto, agora se você vai fazer um proxy ou não para usar externamente como eu fiz... ai é outra história
      - **u/jakobwells** (↑2, 2026-10-15 13:19): This changed in September, so you might both be right depending on when you tried it. Receipts first, same key and same endpoint, plain curl, no OpenCode anywhere in the picture:
          
              $ curl https://opencode.ai/zen/v1/chat/completions \    -H "Authorization: Bearer ***" -H 'Content-Type: application/json' \    -d '{"model":"deepseek-v4.1-flash-free","messages":[{"role":"user","content":"hi"}],"max_tokens":8}'HTTP 403{"type":"FreeTierError","message":"OpenCode's free tier can only be used from within OpenCode. ..."}
          
              $ curl https://opencode.ai/zen/v1/chat/completions \    -H "Authorization: Bearer ***" -H 'Content-Type: application/json' \    -d '{"model":"deepseek-v4.1-flash","messages":[{"role":"user","content":"hi"}],"max_tokens":8}'HTTP 200{"id":"chatcmpl-29b890ff61914b5a84ff9fbee88e713d","model":"deepseek-v4.1-flash","choices":[...]}
          
          Five different free ids give that same 403: deepseek-v4.1-flash-free, mimo-v2.6-flash-free, nemotron-3.5-lightning-free, jev-1.13-free, space-bunny-free. The paid model answers fine from the same shell, so it is not the key and not curl, it is the free tier.
          
          Now the part that explains your side. Until mid-September that check was much weaker. Someone filed #42500 in August asking them to drop it: "The anonymous free tier at [https://opencode.ai/zen/v1](https://opencode.ai/zen/v1) is served only to requests carrying the opencode client's User-Agent. Any other OpenAI-compatible client (Cline, Roo Code, Continue, Aider, mimo) gets 429 FreeUsageLimitError." Spoof the UA, or send X-Opencode-Client and X-Opencode-Session, and you were through.
          
          That closed on 17 September. A pile of issues lands that day with the new error, #49433, #49435, #49438, #49479 and more. From #49433, same day: "just started for me too after a few weeks of it working fine." A maintainer confirmed it the next day in #49621: "We've been tightening our logic to fight abuse. You cannot use the free tier in other harnesses (this is only a limitation for the free tier nothing else)."
          
          So if codex-router worked for you back in August, it did work. The header path hung on for a few days after the 17th and then stopped.
          
          Free tier only though. Paid Zen and Go still answer from any client. If it is still working for you today, paste the response, I would genuinely like to see it.
        - **u/OpinionsRWild** (↑1, 2026-10-15 19:28): So based on this, we’re stuck with the crappy OpenCode interface? Assuming free only user. If that’s the case, ooof there goes a good percentage of the user base
- **u/Ok_Stuff_4959** (↑1, 2026-10-15 09:44): You all go ahead, I'll stick with Big Pickle  :P
  - **u/ProbablyBunchofAtoms** (↑1, 2026-10-15 21:17): Found my homie 🤝
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
  - **u/Mementem** (↑4, 2026-10-15 14:00): i would recommend staying away from muse spark 1.3, 
      
      i just don't trust lizard man with my data.
      
      if they are hosting the full DS model, and not a quant, i would use that
    - **u/warpaint_james** (↑2, 2026-10-15 14:11): I use it for my open source recomp project. Sure, suck up the open source recomp, thanks for the help
    - **u/babedok** (↑1, 2026-10-16 04:38): Same. I hate that lizard man, he should be in jail for life. That lizard is also one of many reasons i ditched React to Stelve, htmx"
    - **u/egomarker** (↑1, 2026-10-17 10:20): You are not wrong, but r/LocalLLaMA and llama.cpp have LLaMA in their names because Meta's model kickstarted the local LLM revolution.
      - **u/sneakpeekbot** (↑1, 2026-10-17 10:20): Here's a sneak peek of /r/LocalLLaMA using the [top posts](https://np.reddit.com/r/LocalLLaMA/top/?sort=top&t=year) of the year!
          
          \#1: [PewDiePie getting banned twice by OpenAI while making a local model is top-tier comedy 💀](https://np.reddit.com/r/LocalLLaMA/comments/1wymgu6/pewdiepie_getting_banned_twice_by_openai_while/)  
          \#2: [The reason why RAM has become so expensive](https://i.redd.it/sgbhubsomccg1.png) | [394 comments](https://np.reddit.com/r/LocalLLaMA/comments/1q8ckz0/the_reason_why_ram_has_become_so_expensive/)  
          \#3: [Anthropic: "We’ve identified industrial-scale distillation attacks on our models by DeepSeek, Moonshot AI, and MiniMax." 🚨](https://i.redd.it/94fbimavfalg1.png) | [873 comments](https://np.reddit.com/r/LocalLLaMA/comments/1rcpmwn/anthropic_weve_identified_industrialscale/)
          
          ----
          ^^I'm ^^a ^^bot, ^^beep ^^boop ^^| ^^Downvote ^^to ^^remove ^^| ^^[Contact](https://www.reddit.com/message/compose/?to=sneakpeekbot) ^^| ^^[Info](https://np.reddit.com/r/sneakpeekbot/) ^^| ^^[Opt-out](https://np.reddit.com/r/sneakpeekbot/comments/o8wk1r/blacklist_ix/) ^^| ^^[GitHub](https://github.com/ghnr/sneakpeekbot)
  - **u/Comfortable-Rise-748** (↑1, 2026-10-15 20:17): muse is better orchestrator (contribotor one is cheap) deepseek is perfect coding on max sub lanes mimo I didn't use.
      
      I use 5.5 xhigh with deepseek 20 lanes saturation for my projects does ton's of work in worktree's and I add extra from another session what muse suggests more.
      
      I could/cannot use gpt 6.1 it's so slow and says nothing usefull and just starts launching plan task (opus) and takes 2 hours. By then the deepseek lanes long time done
  - **u/g9robot** (↑1, 2026-10-15 20:39): Muse is hardcore spying
- **u/andrewlabaski** (↑0, 2026-10-15 09:49): u/opencode please, check why 100% usage cant still use free models.
- **u/CheesecakeLivid9791** (↑1, 2026-10-15 09:58): Just in time
- **u/frank_pc** (↑24, 2026-10-15 10:01): Operation CheapSeek final stage?
  - **u/Much-Researcher6135** (↑1, 2026-10-16 01:57): operation CheekClap
- **u/imsankz** (↑1, 2026-10-15 10:21): Is this how they ask us to come back 😂
- **u/Conscious-Doctor-585** (↑19, 2026-10-15 10:38): The official DS refunded the spending of their api service of last 7 days as a remedy to their service outage. OC is sharing it not staying silent about it.
  - **u/johndoe1985** (↑1, 2026-10-15 22:29): What. ? Where do I see if I got refund ?
- **u/AskingGypone5** (↑1, 2026-10-15 10:49): is it good? last time using space bunny free gets into my skin lol
  - **u/inversechi** (↑1, 2026-10-15 11:04): yeah, that experience was so bad.
  - **u/Monecreiff** (↑2, 2026-10-15 13:50): i miss spacebunny alpha. It was actually good at modelling in blender
    - **u/TheSARMS_Coach** (↑1, 2026-10-16 00:58): Why miss it, when it's still on OpenCode? and you're right it's very good ad modeling in blender. Helped me with a lot of assets.
      - **u/AskingGypone5** (↑1, 2026-10-16 08:06): wait wdym good at modelling in blender, im totally needed that, how do i integrate it with blender?
        - **u/TheSARMS_Coach** (↑1, 2026-10-17 02:38): You simply tell it to do so, but use a Gauntlet Loop, not a regular prompt. Use my modified skill and you should get decent results: [https://github.com/Trans4m-Tech/Gnome\_Gauntlet\_Loop](https://github.com/Trans4m-Tech/Gnome_Gauntlet_Loop)
- **u/Cautious_Fox_4191** (↑2, 2026-10-15 11:01): They have all my prompts and data, right? Nothing in this world is free.
  - **u/NMiguelCosta-PT** (↑3, 2026-10-15 12:23): and if you pay they don't???
    - **u/Cautious_Fox_4191** (↑1, 2026-10-15 12:28): They still do and that's why they subsidies the subscription amount.
      - **u/Ctrl-Alt-Panic** (↑3, 2026-10-15 13:49): OpenCode has a ZDR / no training policy for Deepseek on the paid plan.
          
          That's what they say, anyway.
        - **u/Cautious_Fox_4191** (↑3, 2026-10-15 16:16): >That's what they say, anyway.
            
            Yes.
    - **u/VirtualNorth1279** (↑1, 2026-10-15 22:52): It's believed that OpenAI had access to that mathematician's chat logs that was working on the Navier Stokes problem. But maybe it was his fault as he had 3 subscriptions and one of them hadn't toggled the privacy on. OpenAI denies it anyway. But OpenAI is being run by a bunch of psycho liars, that have potentially murdered a whistleblower too.
        
        Morale of the story: don't trust any of their privacy claims. Thousands of people were in Epstein's circles and nothing happened to any of them. For major crimes. Privacy violations by big tech is like peanuts in comparison.
  - **u/Dushle** (↑1, 2026-10-15 20:35): Do you feel any safer on claude and codex?
- **u/Icy-Examination-9512** (↑28, 2026-10-15 11:01): 200k context is absolute terrorism
  - **u/squirrelscrush** (↑11, 2026-10-15 13:31): I've been living off 260K context on Luna lol
    - **u/FireSilicon_** (↑3, 2026-10-15 14:50): Most openai models including Luna have 1M context you just have to enable it with a config file. In fact you can just tell codex to enable it for you. The only issue is that they charge you more because they are assholes.
      - **u/squirrelscrush** (↑1, 2026-10-15 17:46): I limit it because beyond 272K my bill explodes lol
  - **u/randomperson_69_** (↑2, 2026-10-15 13:35): Ts so funny 😂
  - **u/xmnstr** (↑1, 2026-10-15 15:10): It's perfect if you use billion context!
  - **u/Fresh_Sock8660** (↑1, 2026-10-15 18:42): What tasks? My auto compact is set to 150k and it's been fine.
  - **u/Agitated-Farmer-4082** (↑1, 2026-10-15 22:45): (the 200k context is a client side limit in opencode, the opencode api that handles the model supports one million context)
    - **u/VirtualNorth1279** (↑1, 2026-10-15 22:48): So in Pi it's 1m?
    - **u/shaxsy** (↑1, 2026-10-15 23:31): Pretty sure you can override this?
  - **u/AdvisorLife4016** (↑1, 2026-10-15 22:47): For real? In my opinion, 200K context feels excessive when you design your own system. If you extend it via well-bounded features and good practices, you don't need to dump the whole repo: you just pass the exact contract and ship. Massive context windows only matter when the model acts as the architect because you no longer know how the internals are wired. In other words: *vibecoding*. If you're a vibecoder, then sure, 200K might even feel short.
    - **u/lordvoltano** (↑1, 2026-10-16 02:11): For Hermes Agent, 200K is too limiting as well.
    - **u/Beltalowdamon** (↑1, 2026-10-16 02:30): Honest question.
        
        Why so much effort on trying to work with 200k context when 1M models are so abundant? It's not like they can't orchestrate a 200k context subagent better than you can. Even a simple request on Claude hits 10-15% for me form all the system prompt and all other stuff, but it's so efficient at the actual work that it doesn't matter.
        
        Then again, I never really compact. I just handoff. Mostly because it works so well and leaves a better paper trail so I don't have to spend my time optimizing and maintaining a memory system.
      - **u/AdvisorLife4016** (↑1, 2026-10-16 02:49): 1M tokens sounds great on paper, but in practice it gets expensive and performs worse. Tools cap you around 200k for latency reasons. Plus, crossing that threshold spikes the cost per request, and models lose precision (lost in the middle) when you flood them with noise. If you work on scoped features, you rarely go over 50k to 100k. A clean handoff always beats dumping half a repo into every request. Unless you are a vibecoder, of course, in which case you have no choice but to rely on brute-force context and lean on heavier reasoning models. Fair trade-offs either way.
        - **u/RoboErectus** (↑1, 2026-10-16 05:51): There's a weird thing with vibecoders where they are flexing on how much context they use.
            
            Like... 99% of time that's not a good thing, it's bad.
            
            One might think saying "usage scales quadratically with context size," would help them, but they don't know what "scales" means.
        - **u/Beltalowdamon** (↑1, 2026-10-16 17:25): I still don't understand your position. 
            
            Maybe I should have mentioned I'm using claude code harness, not a lean one. Just loading context on a short prompt puts me to 50k to 100k. Just reading the system prompt and a little code. 
            
            I'll work up to about 35% and there's pretty much no quality loss, with most of the work simply orchestrating cheaper codex agents. That's where all the tool calls and code-generated context go.
            
            I don't even fully use up my $20 claude sub sometimes, even though I'm working with decently large codebases.
  - **u/xmsxms** (↑1, 2026-10-16 00:53): If it was higher you'd burn through the free quota pretty quickly, so having it lower is reasonable as it forces compression and sensible quota usage.
    - **u/Icy-Examination-9512** (↑0, 2026-10-16 04:42): thats not how it works. The model compacts its context automatically at 75% and anything after 50% is garbage output. I tested it out and it ran for 4 hours but every 20 min it kept compacting itself, if  it had 1mil context window it wouldve done the same amount of work worth for the free usage limit without compacting itself and getitng stuck every 10 min. It would also use a lot less tokens if 75% of its context window wasnt filled half the time
      - **u/xmsxms** (↑0, 2026-10-16 05:52): If your turns are using a full 1m context then you are using 1m of (maybe cached, maybe not) tokens per request. If you have a 200k limit then you are only using 200k per turn. So yes, it is how it works.
        - **u/Icy-Examination-9512** (↑0, 2026-10-16 06:36):  On the 1 million context, it is best practice to not go above 45% i thought everyone knew this and also this ensures that the model doesnt respond with garbage output. At 200k context it takes a minute or so before the model reaches 80 to 95% context and so not only is the output bad but after it compacts its context, it only knows a shell of what it knew before and practically starts over with its work because the compaction only instructs it on the general stuff and it again reads all the specific files to gain an understanding before writing any code and we are already over 60% context. The whole thing is just incredibly redundant and incredibly stupid. Unless you are using the model for very barebones simple  stuff, 200k context is just a hindrance. You are right in terms of context usage but I would rather use 1m context and get 10x better quality and speed for my work and have a shorter usage time than use 200kcontext. Especially with a super fast model that uses tons of tokens for reasoning, 200k context is borderline nothing
  - **u/pososisocky** (↑1, 2026-10-16 08:45): But free
- **u/Warm-Agent-811** (↑1, 2026-10-15 11:08): Does anyone know if this is the official DeepSeek model, or is it a third-party service like OpenRouter that might be serving a smaller 4B model under the DeepSeek name?
  - **u/LukeLikesReddit** (↑2, 2026-10-15 11:14): Given they only offer 200k context and say its ZDR when the official deepseek api gives you 1 million context and will train on your data i suspect its going to be the latter. Haven't had the chance to test it yet.
- **u/Dapper-Window-4492** (↑1, 2026-10-15 11:28): Any rate limits on the free tier?
- **u/Voxylem** (↑1, 2026-10-15 11:41): They made it free and now it is slow as hell
- **u/Dry_Hyena_6296** (↑1, 2026-10-15 11:46): Free api??
- **u/cetogenicoandorra** (↑1, 2026-10-15 11:47): What limit tier?
- **u/XL-Dildo-Brazilian** (↑1, 2026-10-15 13:10): i cant see deepseek 4.1, it shows to me openrouter one which is paid, the free version of opencode i cant see it. any help please? thanks
- **u/Dry-Mathematician730** (↑8, 2026-10-15 13:45): This is better them big picle for coding?
  - **u/Difficult_Plantain89** (↑5, 2026-10-15 14:31): Absolutely. Not saying that big pickle is bad.
    - **u/LeN3rd** (↑2, 2026-10-16 00:08): Right? Its pretty good. I mean, I am sure the big guys can do better, but it works quite well for me.
- **u/Mementem** (↑1, 2026-10-15 13:57): is it a lower quant? or is it the full thing?  
    what are the speeds like for the rest of you?
  - **u/xapep** (↑2, 2026-10-15 16:02): Free tiers in these harnesses are usually a quant or a shared backend with rate limiting, which is why speeds bounce around. OpenCode says what it serves on the paid plan; the free route stays vaguer.  
        
      If you want a real answer, run the same prompt against a PAYG API and compare on a structured-output task. Full-precision serving costs money, so free almost always means something's shaved somewhere.  
        
      I run DS V4.1 Flash on a PAYG endpoint, so I'm biased, but the test works with any provider that tells you what it's actually serving.
- **u/jackorjek** (↑1, 2026-10-15 14:30): its free with quota. tested, pushed it and got limited. resets in the next 12 hours.
- **u/Sea_Mushroom_6498** (↑0, 2026-10-15 14:56): which model is best for the cyber security and ctf ?? among all free
- **u/breadnone** (↑1, 2026-10-15 15:06): the most hype news in a while
- **u/anonymous_2600** (↑1, 2026-10-15 15:16): anyone measured the tps?
- **u/LuluLeSigma** (↑1, 2026-10-15 15:24): YOU KIDDING ME
- **u/Jolly-Chef5241** (↑1, 2026-10-15 17:29): Why everyone is so excited with this model?
    Isn't it something just at ~GPT 6 Luna level?
  - **u/sdexca** (↑4, 2026-10-15 17:53): Having used both it’s def better than Luna. Idk Luna doesn’t seem like a good model, it’s like well RLed but extremely small and gives up all the time. Flash is great, def isn’t as well RLed but it seems far better than Luna.
  - **u/Fresh_Sock8660** (↑1, 2026-10-15 18:41): I'd say around sol level for coding tasks.
    - **u/bartsimpsonwin** (↑1, 2026-10-16 20:00): 39 on artificial analysis for DeepSeek V4.1 flash max Vs 42 for sol 6.1 low, 6.1 low costs $0.13 per task Vs $0.27 for DeepSeek v4.1 flash max. Yeah no double the price for worse intelligence (3 points on AAI is significant), only think DeepSeek has on sol is speed, it's fast as fuck, but more expensive and dumber
      - **u/Fine-Strategy-9621** (↑1, 2026-10-17 01:09): I'd suggest you try it. Benchmarks aren't everything. DeepSeeks RL isn't as good as other labs, but their models architecture gives them the big model smell at a lower cost.
  - **u/VirtualNorth1279** (↑1, 2026-10-15 22:47): In some areas it's very useless. But for simple stuff like building a website it's quite good.
  - **u/AdvisorLife4016** (↑1, 2026-10-15 22:52): GPT-6 Luna is also great! ... it’s certainly exciting. Why would it need to be anything else? 😳
  - **u/TheSARMS_Coach** (↑1, 2026-10-16 00:55): This model has been serving me VERY well and in many cases produced better results for me than GPT or Claude. I'm also 100% sure they have been testing a newer model this week, cause the output i've been getting blows the output of 2 weeks ago completely out the water. It nearly matches GPT Sol with more speed.
- **u/Jensen_og_Jensen** (↑2, 2026-10-15 18:14): I just tried it in opencode via the HACS intergration in HASS. It doesnt work. API connects fine, but returns the "insufficiant funds" error.
  - **u/DJubstin** (↑1, 2026-10-15 19:19): Insufficient funds error means you are selecting a model outside (Personal/Opencode) of the Go subscription. You should select a model in the Opencode Go category. Check out /models - assuming you are on Opencode Go.
    - **u/Jensen_og_Jensen** (↑1, 2026-10-16 12:08): Stupid me. I forgot to /models. haha. Now it works ;)
- **u/daskalou** (↑2, 2026-10-15 18:20): Your codebase is the product.
- **u/ameeno1** (↑1, 2026-10-15 18:50): how long for?
- **u/Automatic-Gur2046** (↑3, 2026-10-15 20:05): Sorry for my ignorrance, do I need a paid subs to use API for free? I know it sounds oxymoron but I am trying to learn if it is free as in "you need a paid sub but it does not reduce your credit"
  - **u/corenovax** (↑1, 2026-10-15 21:41): It's just free my friend. Install and enjoy
- **u/Warm-Difference-3760** (↑0, 2026-10-15 20:18): why? check the latest macos intel binary with virustotal , weird!
- **u/Pale_Top2519** (↑3, 2026-10-15 21:14): Suppose you dont care about privacy and just need shit done. What would yall pick? Nemo ultra, V4.1 Flash, Mimo Flash or MUSE spark 1.3?
  - **u/corenovax** (↑1, 2026-10-15 21:42): Obviously muse
    - **u/Andr1yTheOne** (↑2, 2026-10-15 22:24): 😂
  - **u/HashiKuroVR** (↑1, 2026-10-16 00:23): From my experience (coding, front end, word, and cross information) muse is a little shit
      I prefer DS V4.1 flash, if you want complex planning i just use other model just for the base and initial idea, then I continue with deepseek
  - **u/lordvoltano** (↑1, 2026-10-16 02:11): In my experience Muse Spark 1.3 is slower than Deepseek V4.1 Flash. It also obfuscate the thinking process. So I prefer DeepSeek in this case.
  - **u/Ok-Drawer5245** (↑1, 2026-10-16 06:44): Deepseek v4.1 flash is very clearly superior to the rest of the free models, muse in second place
      
      There just my opinion of course
  - **u/Melodic_Divide_7187** (↑1, 2026-10-17 11:39): Muse spark 1.3 cumtributer free is just a naming scam. Really garbage
- **u/luisfernandez95** (↑1, 2026-10-15 22:23): Toma mi dinero opencode 👍
- **u/VirtualNorth1279** (↑1, 2026-10-15 22:46): Is it a quantized version or the real thing?
  - **u/Global_Routine** (↑1, 2026-10-16 02:58): No, as far as I've read it's the same model
- **u/FlyingTwentyFour** (↑1, 2026-10-15 23:50): it's great to be so back!
- **u/rusleykcruz** (↑1, 2026-10-15 23:59): Tiny quotas
- **u/Mammoth_Jeweler_7414** (↑1, 2026-10-16 00:40): Deepseek went free all the time and its infrastructure couldn't keep up. You'll get slow ass usage anyway.
- **u/automax** (↑1, 2026-10-16 06:37): Its pretty good, faster and smarter than big pickle
- **u/Tight_Commercial7** (↑1, 2026-10-16 08:00): Daily limit or you have one time 200k ?
- **u/d2epak** (↑2, 2026-10-16 10:50): To use it Freely first I have to do some credit recharge in opencode ? 
    Or I can just access free model without any credit or subscription ? 
    I tried with a new account on opencode, but api request showing need a global region (but privacy tab not coming in my Free Opencode account) . 
    Can anyone help me in this ?
  - **u/d2epak** (↑1, 2026-10-16 11:07): I found a BUG maybe in opencode site, and fixed it but not fully 🙂.
      You can manually type this url (https://opencode.ai/console/org_01M524N3RK05BHYRZFB4ARCD45/settings/privacy) to go to Privacy tab and Turn on Global regions But now when I send api request it now shows "active OpenCode Go subscription is required to use Go models"
- **u/Tight_Commercial7** (↑1, 2026-10-16 12:15): I will try to fix and tweak my local Qwen models
- **u/tanvirakon** (↑3, 2026-10-16 16:51): Upstream request failed: Insufficient account funds \[retrying in 4s attempt #2\]
- **u/Stock_Machine5356** (↑1, 2026-10-16 18:28): [ Removed by Reddit ]
- **u/truongvantuanbk** (↑1, 2026-10-17 04:37): How to try it
- **u/fucking_h** (↑5, 2026-10-15 08:37): I think all the answers are pretty obvious.
    
    1. Maybe, maybe not. Depends on your work.
    
    2. Yes, limited time obviously.
    
    3. Nothing is unlimited, especially when it's a known model and not even a stealth release.
- **u/RoundZookeepergame2** (↑1, 2026-10-15 10:37): Why would it be free and unlimited?? Please
  - **u/AskingGypone5** (↑2, 2026-10-15 10:52): i FEEL like its unlimited when using space bunny free...

---

## Spent 4+ month building this 😓 ~15B tokens 370 Pull requests
**u/ivanfenenko** · 2026-10-15 07:01 UTC · ↑156 · 123 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6etqb/spent_4_month_building_this_15b_tokens_370_pull/)

Started this as a hobby project on June 1: fully native apps for iOS and Android, built in parallel by a single AI agent working on both codebases at once.

It finally feels solid enough to share publicly:

* **Android:** [https://play.google.com/store/apps/details?id=dev.opencode.mobile](https://play.google.com/store/apps/details?id=dev.opencode.mobile)
* **iOS:** [https://apps.apple.com/de/app/opencode-mobile-unofficial/id6799246544](https://apps.apple.com/de/app/opencode-mobile-unofficial/id6799246544)

It’s unofficial and made by 1 person, so feedback and bug reports are very welcome. Happy to share about the parallel-agent workflow too.

**Comentarios:**

- **u/Far_Target_4339** (↑5, 2026-10-15 07:04): Fdroid?
- **u/Popular-Factor3553** (↑18, 2026-10-15 07:08): Is it open source?
  - **u/ivanfenenko** (↑11, 2026-10-15 07:16): No but I don't mind making it opensource.
    - **u/Popular-Factor3553** (↑18, 2026-10-15 07:23): Definitely make it open source and maybe list some features how is it better then open chamber
    - **u/-light_yagami** (↑1, 2026-10-16 08:39): then why don't make it open in the first place, I assure no one is going to steal your slop code
      - **u/ivanfenenko** (↑1, 2026-10-16 08:47): Yesterday I spend 5 hours moving things around to bring it into a shape for opensource.   
          I had to move my CI runners, run integrity checks, protect keys and accounts, setup a license and contribution guidelines. 
          
          I assure you this is not "just make it opensource" 
          
          None of these things I did I needed for development in the last 4 month.
        - **u/Worth_Psychology_874** (↑1, 2026-10-16 22:20): So?
- **u/masterofall20** (↑18, 2026-10-15 07:16): Do you really think you can close source a client app for Opencode which in itself is an open-source app? Also, Openchamber exists.
  - **u/ivanfenenko** (↑-6, 2026-10-15 07:17): 1. I am sure I can call things via API  
      2. This is better then Openchamber client
    - **u/WhatYouGoBy** (↑12, 2026-10-15 07:31): What makes it better than openchamber?
      - **u/Mammoth-Apple410** (↑1, 2026-10-15 07:36): same
      - **u/LeonLer** (↑7, 2026-10-15 07:41): that he did it 😆
        - **u/LowDesigner1330** (↑3, 2026-10-15 10:15): That he vibecoded it
      - **u/Odd_Finding_863** (↑1, 2026-10-15 15:36): Not having to install yet another server on my desktop is a really good point for me, it's cleaner for those who only want pure OpenCode.
          
          but I get it, having a close source client for a project that's open source sucks a lot and raise trust issues on my side.
      - **u/Embarrassed-Option-7** (↑2, 2026-10-15 18:15): Proceeds to say it’s better without listing reasons. Sureee bro lol
    - **u/MFranz15** (↑1, 2026-10-16 00:52): i guess bro
    - **u/pungat_** (↑1, 2026-10-16 02:46): "trust me bro"
  - **u/Dry_Cantaloupe4349** (↑-4, 2026-10-15 08:41): isn't the whole point of open source that you can fork it into your own closed source thing?
    - **u/MayhairAgain** (↑5, 2026-10-15 09:32): Only for permissive software licences like MIT or Apache (which, to be fair, OpenCode *is* licensed under). Copyleft licences like the GPL explicitly don't allow it.  
        But anyway, I think they were talking less about the technical legality, and more about *why* people would intentionally choose a closed-source client for an otherwise open software.
      - **u/ivanfenenko** (↑0, 2026-10-15 11:41): Good question. Waiting for official opencode client ve open source too
- **u/vale93kotor** (↑7, 2026-10-15 07:19): If open source would be great, looks nice
  - **u/ivanfenenko** (↑5, 2026-10-15 07:22): As long as you can trust this comment, I will make it opensource when I have time to cleanup my sensitive data in the repo.
    - **u/trent-7** (↑9, 2026-10-15 08:35): Remember that if you have the sensitive files in version control (like git), just deleting the sensitive data is not enough as it is saved in the history. The easiest and safest option is to copy all non-sensitive files into a new repo. However, that means that you will lose the history.
      - **u/ivanfenenko** (↑2, 2026-10-15 18:02): valid
      - **u/RoundZookeepergame2** (↑1, 2026-10-16 10:19): oh wow! Thank you!
    - **u/quanta777** (↑2, 2026-10-15 13:39): You can use gitleaks or betterleaks to scan and cleanup both the repo and commit history
    - **u/vale93kotor** (↑1, 2026-10-15 17:25): No problem, can wait. And thanks! Mind what Trent said though
- **u/ivanfenenko** (↑5, 2026-10-15 07:32): Since opensource question is the main one here is official reply:
    
    I've been working on this project alone on private repo. I need to ensure I didn't leak anything private and do some extra maintenance to open the project. 
    
    I will make sure to prioritise this [https://imgur.com/a/HAxx9E2](https://imgur.com/a/HAxx9E2)
  - **u/sanyi091** (↑1, 2026-10-15 20:37): Why did you post an imgur inage of the repo issues instead of linking the issue
    - **u/Sea_Anywhere896** (↑2, 2026-10-15 21:51): If the repo is private then how will he send the issue url
- **u/seeKAYx** (↑2, 2026-10-15 07:40): Very Nice. I'm currently testing the official iOS App from OpenCode. I will test both.
  - **u/ivanfenenko** (↑1, 2026-10-15 13:09): Thanks. Will appreciate feedback
  - **u/Sealra_** (↑1, 2026-10-15 13:29): where can u download it?
    - **u/seeKAYx** (↑1, 2026-10-15 13:31): It’s a limited beta with 1000 users.
- **u/abhiramskrishna** (↑6, 2026-10-15 07:42): Openchamber is way better!
  - **u/ivanfenenko** (↑0, 2026-10-15 08:01): Any reason?
    - **u/mihail_chechulin** (↑5, 2026-10-15 08:18): Open source
  - **u/pikuray** (↑1, 2026-10-15 11:32): Thanks I'll check it out
- **u/NinjaAlaska** (↑2, 2026-10-15 07:43): 15B tokens  and 4 months? token wise efficient imo. what harness you used to make
  - **u/ivanfenenko** (↑2, 2026-10-15 08:15): It's a huge mix:
      Cursor, opencode, Codex, Claude Code
      
      Everything from grok 4.5 to Fable 5.1 and in between.
      The harness doesn't meter much..
      Models didn't matter much too. 
      
      
      Only Fable 5.1 and Opus 5.5 really feel like an improvement since May.
    - **u/Etherealnutt** (↑1, 2026-10-15 09:29): Bruh anything other than Claude is a waste of time . I’m always summoning Claude to clean shit up. True that starting shit from scratch with Claude too it costly. So I usually get the boiler plate from other models then bring it to Claude to do it thing
- **u/jakobwells** (↑1, 2026-10-15 07:51): TestFlight is open for the official OpenCode app: https://testflight.apple.com/join/EnFsKYQ1
- **u/nijezabacanje** (↑1, 2026-10-15 07:52): I was happy to see an agent actually running on a phone, but disappointed to see just a thin client... There's very little need for the app when OpenChamber already exists, tbh
- **u/Mean-Elk-9439** (↑3, 2026-10-15 08:03): Damn all this for a worse openchamber run by one dude instead of many maintainers
- **u/ryanworldwide** (↑1, 2026-10-15 08:13): Is it on GitHub?
  - **u/ivanfenenko** (↑1, 2026-10-15 11:38): No but you can check on one week. Should be enough time for me to figure out how to share it the best way
- **u/TheBrownMamba1972** (↑1, 2026-10-15 08:28): Why use this instead of just making a PWA yourself with Safari/ other browsers?
  - **u/ivanfenenko** (↑0, 2026-10-15 11:38): Because website based apps suck.
- **u/LeviLuxor** (↑1, 2026-10-15 09:01): The OpenChamber app for iOS is still in beta but it's really awesome. No reason to use anything else at this point.
- **u/SafeReturn_28** (↑1, 2026-10-15 09:07): installed it but i need to upgrade to opencode2 that I have been putting off. Will give it a try afterwards
    
    QQ: why did you not just using flutter instead of two separate native apps?
  - **u/ivanfenenko** (↑1, 2026-10-15 11:36): V1 API should work . Let me know if you struggle with it
- **u/Mohasr** (↑1, 2026-10-15 09:21): can i connect it to the opencode desktop and see the session ?
  - **u/ivanfenenko** (↑1, 2026-10-15 11:37): Yes. Easiest is on v2 API. But v1 also work. I will share helpful instructions later
    - **u/Mohasr** (↑1, 2026-10-15 11:42): Ok thx
- **u/dumbasPL** (↑5, 2026-10-15 09:23): Isn't this a bit too late? Since there is already an official one for iOS?
  - **u/ivanfenenko** (↑1, 2026-10-15 13:09): I don't care if it's late. I have fun making this
- **u/i-dm** (↑3, 2026-10-15 09:35): What a high risk way to spend 3 months - you always knew they were going to release an official one at some point
  - **u/ivanfenenko** (↑0, 2026-10-15 11:03): Because it's fun
- **u/binladen0069** (↑1, 2026-10-15 10:58): anomaly should hire him
- **u/Stevie2k8** (↑1, 2026-10-15 11:03): You should definitely consider getting us access the code to do independent security checks. I would never ever install some random app from some random guy (sorry) claiming it does what it should without checking all source files and libraries und update paths and everything. I do a complete security review on any mcp I install and only use mcps with complete open source code to be able to check for security flaws...
    
      
    I'd like to have an app like this but would'nt install it ever without checking... 
    
    But hey, well done :-)
  - **u/ivanfenenko** (↑0, 2026-10-15 11:43): You can wait a week and check. But you can for example decompile android app. You will see there absolutely everything that is happening
  - **u/BrownCarter** (↑1, 2026-10-15 13:39): You do this for all app you install on the app store?
    - **u/Stevie2k8** (↑1, 2026-10-15 21:08): No, I check the surroundings, big company, good and many reviews... And if it is open source I download the source, check security and build the app by myself before installing...
- **u/tonio_i** (↑1, 2026-10-15 11:10): Looks good at a glance. Will stick for the time being with openchamber, but if you decde to make it opensource and it survives as a project, might make the switch.
- **u/mondroyink** (↑7, 2026-10-15 12:51): Dear, one can just use termux. It's a good project but many might not have a good use for it.
    
    It's a good project with a nice UI!
    
    https://reddit.com/link/pgw2dgg/video/o6vv9n5aomvh1/player
  - **u/ivanfenenko** (↑-2, 2026-10-15 15:55): Cool! Good for you
  - **u/OptimalSalamander400** (↑2, 2026-10-15 23:47): This shit got my phone tweaking last time i tried... Spec issue tho
    - **u/why_so_sergious** (↑2, 2026-10-16 02:22): skill issue
      - **u/OptimalSalamander400** (↑2, 2026-10-16 09:59): I wish bro
          can i run it smoothly on a phone with 3gigs of ram?
        - **u/why_so_sergious** (↑0, 2026-10-16 10:21): its a terminal, it uses less ram than your launcher.. I think it uses something like 100mb on idle
          - **u/mondroyink** (↑1, 2026-10-16 10:23): I am using a debain from proot-distro, that would probably require quite the amount of ram and opencode running inside it. I haven't checked if it can run on 3 gigs but seems limited to me
  - **u/d4rkh0r1z0n_original** (↑1, 2026-10-16 10:23): lmao, same here, been using Termux if I ever had to run on mobile... proot?
  - **u/Vexaris1** (↑1, 2026-10-17 07:36): I'm the same way; with this technique, I can even do development on the bus. I connect to my machine via SSH and run OpenCode on my machine.
- **u/True_Requirement_891** (↑3, 2026-10-15 13:05): Just opensource it bro for trust
  - **u/ivanfenenko** (↑1, 2026-10-15 13:10): Come back in a week
    - **u/TheMythicSorcerer** (↑1, 2026-10-15 16:07): u/remindmebot 1 week
      - **u/RemindMeBot** (↑1, 2026-10-15 16:07): I will be messaging you in 7 days on [**2026-10-22 16:07:43 UTC**](http://www.wolframalpha.com/input/?i=2026-10-22%2016:07:43%20UTC%20To%20Local%20Time) to remind you of [**this link**](https://www.reddit.com/r/opencode/comments/1x6etqb/spent_4_month_building_this_15b_tokens_370_pull/pgxbfha/?context=3)
          
          [**CLICK THIS LINK**](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2Fopencode%2Fcomments%2F1x6etqb%2Fspent_4_month_building_this_15b_tokens_370_pull%2Fpgxbfha%2F%5D%0A%0ARemindMe%21%202026-10-22%2016%3A07%3A43%20UTC) to send a PM to also be reminded and to reduce spam.
          
          ^(Parent commenter can ) [^(delete this message to hide from others.)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Delete%20Comment&message=Delete%21%201x6etqb)
          
          *****
          
          |[^(Info)](https://www.reddit.com/r/RemindMeBot/comments/e1bko7/remindmebot_info_v21/)|[^(Custom)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5BLink%20or%20message%20inside%20square%20brackets%5D%0A%0ARemindMe%21%20Time%20period%20here)|[^(Your Reminders)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=List%20Of%20Reminders&message=MyReminders%21)|[^(Feedback)](https://www.reddit.com/message/compose/?to=Watchful1&subject=RemindMeBot%20Feedback)|
          |-|-|-|-|
    - **u/True_Requirement_891** (↑1, 2026-10-15 16:08): Improve the folder workspace picker, I cant navigate to my other drives
      - **u/ivanfenenko** (↑1, 2026-10-15 17:07): Good finding.   
          Thanks!
      - **u/ivanfenenko** (↑1, 2026-10-15 17:41): Since you call it "folder" I assume you use Windows. Right?
    - **u/Minimum_Industry_978** (↑1, 2026-10-15 17:54): Remove the 'telemetry' first :)
      - **u/ivanfenenko** (↑1, 2026-10-15 17:59): You can decompile and app right now to see what telemetry is there.
- **u/jaykayenn** (↑3, 2026-10-15 13:25): Don't you guys have SSH/web browsers?
  - **u/ivanfenenko** (↑1, 2026-10-15 15:56): Lol.
- **u/commandedbydemons** (↑1, 2026-10-15 13:28): You can simply just use Orca, which also supports any harness and operates remotely.
- **u/NegotiationNo1504** (↑1, 2026-10-15 13:41): nice work. But I already have opencode already working native in termux
- **u/honolulu33** (↑1, 2026-10-15 14:38): Either put a price on it or open-source it, so your burned tokens pay off.
  - **u/ivanfenenko** (↑2, 2026-10-15 15:56): Dude I have a proper job.
    - **u/paperbenni** (↑1, 2026-10-15 17:47): Then why not open source it?
- **u/ichisay** (↑1, 2026-10-15 15:25): Muy bueno, pero sigo prefiriendo rustdesk o similares
- **u/Key-Height-8482** (↑1, 2026-10-15 15:43): BRO entered a community with Termux and revers engendering mcps .. open source it or run man ..
  - **u/ivanfenenko** (↑1, 2026-10-16 14:22): I will manage thansk
- **u/BoostManMaG** (↑1, 2026-10-15 16:52): Great work
    But somehow I prefer open chamber, although won't lessen any of your work brother :)
- **u/alabama1337** (↑1, 2026-10-15 17:18): Just another vibecoded, closed-sourced trash.
- **u/Commercial_Boat_583** (↑1, 2026-10-15 19:07): Wasted time https://github.com/crim50n/oc-remote
  - **u/ivanfenenko** (↑0, 2026-10-15 20:38): That is not even close :)
- **u/Delicious-Ad-4944** (↑1, 2026-10-15 19:08): Downloading. @ivanfenenko remind me tomorrow for a feedback.
  - **u/Delicious-Ad-4944** (↑1, 2026-10-16 04:44): @ivanfenenko , why I can't select only two maybe three folders as a new project ?
    - **u/Delicious-Ad-4944** (↑1, 2026-10-16 04:46): Nvm, found it how 🤣 you could make it more intuitive, like that button to add a folder, my first tought it was that is to "go up a level".
      - **u/Delicious-Ad-4944** (↑1, 2026-10-16 04:47): First message 😟 "unable to reach the server"
        - **u/ivanfenenko** (↑1, 2026-10-16 07:49): Thanks :) happens
          - **u/Delicious-Ad-4944** (↑1, 2026-10-16 11:17): Waiting for a fix 🤗
- **u/purple_nippies** (↑1, 2026-10-15 20:40): Why would someone choose this over an existing solution like Paseo?
  - **u/ivanfenenko** (↑1, 2026-10-16 07:49): It's working directly with opencode with no extra stuff.
- **u/Sea-Worry-6024** (↑1, 2026-10-15 20:53): Which model did you use?
  - **u/sas3y** (↑1, 2026-10-16 08:26): not OP but he answered:
      
          It's a huge mix: Cursor, opencode, Codex, Claude Code
          
          Everything from grok 4.5 to Fable 5.1 and in between. The harness doesn't meter much.. Models didn't matter much too.
          
          Only Fable 5.1 and Opus 5.5 really feel like an improvement since May.
- **u/PhotographIcy7588** (↑1, 2026-10-15 21:47): I would use it if it's better than OpenChamber. Also as others said already, open source it
- **u/TheAILegend** (↑1, 2026-10-15 23:07): paseo has existed for a years : ) [https://apps.apple.com/us/app/paseo-remote-coding-agents/id6758887924](https://apps.apple.com/us/app/paseo-remote-coding-agents/id6758887924)
  - **u/nemesisbreaker** (↑1, 2026-10-16 03:26): i've been loving paseo mysefl
- **u/kamilerz** (↑1, 2026-10-16 08:47): isn’t the official opencode mobile in development too? https://www.threads.com/@thdxr/post/DeZ2Vm1HW2U
  - **u/ivanfenenko** (↑1, 2026-10-16 09:00): Yes and you can try iOS version in testflight.   
      It was expected that it happens. 
      
        
      If you ask why I do it anyway:  
      1. it's fun  
      2. i believe there is still no android / ios apps combo that are high quality native experience. Mine is not fully there either, but I believe I am on a good track. Both apps are fully native code and at the same time look similar enough with matching experience for users. Nobody is second class
- **u/pososisocky** (↑1, 2026-10-16 09:00): And 0 users
  - **u/ivanfenenko** (↑1, 2026-10-16 09:10): There are some users. And they are dedicated. [https://imgur.com/a/7Ia6bsk](https://imgur.com/a/7Ia6bsk)
    - **u/pososisocky** (↑1, 2026-10-16 10:02): What is dedicated
- **u/ekinokss** (↑2, 2026-10-16 12:12): I have been using this for around a week now. It works great and I like the design. I have 1 thing about it that I don't like tho. I think there should be a language setting instead of making it auto from system language. (There is a language setting in the settings but even tho it's set to English I see my native language name of "shell" in tui. My pc is also set to English)
  - **u/ivanfenenko** (↑1, 2026-10-16 12:33): Hey! Great to see you here.   
      Can you describe the problem in more details? Maybe I can include this in next release (Monday). 
      
      You can also reach me on twitter [https://x.com/ivanfenenko](https://x.com/ivanfenenko)
- **u/SecureReception8454** (↑1, 2026-10-16 12:56): Do I need to be in the same Wifi?
  - **u/ivanfenenko** (↑1, 2026-10-16 14:23): 1. You can use tailscale  
      2. Opencode v2 have their own tunner if you \`opencode pair --remote\` command
- **u/Big_Excitement_8** (↑1, 2026-10-16 13:27): Lol. Does our chat history comes with it as well? 😅
  - **u/ivanfenenko** (↑1, 2026-10-16 14:21): Wat?
- **u/baron_von_noseboop** (↑1, 2026-10-16 14:51): Pros / cons vs Conduit?
  - **u/ivanfenenko** (↑1, 2026-10-16 17:40): vs what?
- **u/Another-Geek-Guy** (↑1, 2026-10-17 00:44): Wondering, could i run this with the free models, i dont want to pay. and wheres teh files its editing
  - **u/ivanfenenko** (↑1, 2026-10-17 12:00): This app doesn't run anything. You can connect to your own server and control it remotely.   
      In that sense yes can use free models in opencode.
- **u/Vexaris1** (↑1, 2026-10-17 07:35): Does it support SSH?
  - **u/ivanfenenko** (↑1, 2026-10-17 11:59): no. this is not the protocol to use here.  
      this app uses only official opencode API
- **u/MessMassacre** (↑1, 2026-10-17 07:58): Why this over openchamber?
  - **u/ivanfenenko** (↑1, 2026-10-17 11:57): It works with opencode directly.   
      Also there is more potential it truly native apps.
- **u/g9k197** (↑1, 2026-10-17 09:35): Has "vibecoding" become simpler than searching for an existing solution on Google?
  - **u/ivanfenenko** (↑1, 2026-10-17 11:54): What is fun in that?

---

## Muse Spark 1.3 Free, Big Pickle, and MiMo 2.5 Free or Cat Jam. Which one is best for gamedev?
**u/FutureLynx_** · 2026-10-15 04:19 UTC · ↑9 · 22 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6c56w/muse_spark_13_free_big_pickle_and_mimo_25_free_or/)

**Comentarios:**

- **u/HelioDex** (↑5, 2026-10-15 04:32): Muse probably (if you're fine with the data retention policy). Though do try MiMo 2.6 Free instead of 2.5 if you can, I've seen it do a lot better gamedev work than 2.5.
  - **u/FutureLynx_** (↑5, 2026-10-15 05:58): yeah im having very good results with Muse. Mimo last time i tried it started making a mess so i went back to muse.
- **u/Loud-Coach-2671** (↑5, 2026-10-15 04:39): space bunny or muse
- **u/bit_shifting_is_sexy** (↑11, 2026-10-15 04:51): Muse is best among these 4 but don't be surprised if Zucc releases the same game 2 weeks later
  - **u/pikuray** (↑2, 2026-10-15 05:27): I will sue him
  - **u/FutureLynx_** (↑5, 2026-10-15 05:47): Isnt it the same if using GPT astra or Claude? Dont they also grab our data?
    - **u/Mementem** (↑2, 2026-10-15 14:12): they all do grab our data, i am just more terrified of the zucc grabbing it....  
        DS is free right now, can try using that too
- **u/TelegramkaFan** (↑2, 2026-10-15 05:28): [ Removed by Reddit ]
- **u/AdFun4897** (↑0, 2026-10-15 08:01): Just use the $20 claude code plan.
  - **u/FutureLynx_** (↑1, 2026-10-15 08:22): Is it that much better than Muse? It doesnt seem that way.
    - **u/Pepek91** (↑2, 2026-10-15 08:36): I use Opus 5.5 at work vs free Muse 1.3 for private game dev. Different settings for sure but those free models in opencode still do a lot of stupid mistakes and are lazy. Not that Opus is perfect, but is doing much better on complicated projects while Muse 1.3 takes a lot of shortcuts...
      - **u/FutureLynx_** (↑1, 2026-10-15 08:38): So should i go for Opus and pay the 20$ per month? maybe its worth it. There is also Astra that seems better, right?
        - **u/arphen_n** (↑1, 2026-10-15 11:11): from anectodal evidence after testing both 20$ subs openai is total scam and oh my god do you get a lot of usage for 20 bucks on claude, it's not even close in terms of what you can get done. you're too poor to work with astra ( i know i am)
        - **u/Odd_Abrocoma_8421** (↑1, 2026-10-15 12:20): Claude pro is too better.
        - **u/Pepek91** (↑1, 2026-10-15 12:56): This is very personal. If you have good spec an easy domain Muse 1.3 is ok. If very hard problems than Opus. People are also happy with OpenAI models, as thay are cheaper and good enough. Look at inteligence index vs cost graphs. Mighr help.
  - **u/Jesusthegoat** (↑1, 2026-10-15 10:43): Opus medium on the 20$ claude plan runs out of weekly usage in like 2 hours of work. How are you using it?
- **u/HorrificFlorist** (↑1, 2026-10-15 08:33): Space Bunny and by far.
    
    I spent days working through a mess with Muse got so bad i just reverted everything and started with Scratch.
    
    Tried to do it with Space Bunny. 30 mins later issues resolved while removing over 10k lines of code
  - **u/FutureLynx_** (↑1, 2026-10-15 08:37): Never heard of it. You are the first one i saw recommending it. Are you sure that was not just incidental? Im doing quite well with Muse. Before I was with Big Pickle.
    - **u/HorrificFlorist** (↑1, 2026-10-16 00:19): Complex solving & Design - Space Bunny  
        Dumb tasks, rapid execution, fan out - Muse
        
        I am currently porting our design system to v2.
        
        Used Space Bunny to clean up edges of Figma docs, develop detailed specs for DS migration only.  
        Muse is as we speak executing 10 subagents at a time migrating items.
        
        Once Design is happy with new storybook content and bugs sorted out, use Space Bunny for app migration specs.
- **u/LuluLeSigma** (↑1, 2026-10-15 16:34): cat jam good. deepseek v4.1 flash free tho
- **u/CuriousHelpful** (↑1, 2026-10-15 23:13): Cat Jam: "done." (IYKYK)

---

## Can you use Zen free with other Coding Agents?
**u/Another-Geek-Guy** · 2026-10-15 03:54 UTC · ↑2 · 4 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6booc/can_you_use_zen_free_with_other_coding_agents/)

I've been testing the best models on task and seeing which is best, but now i want to see if other Coding agents are better, but I'm not sure if Open code Zen is compatible with others. Thank you!

**Comentarios:**

- **u/Maglcite** (↑2, 2026-10-15 03:56): not anymore. used toooo
  - **u/Another-Geek-Guy** (↑2, 2026-10-15 04:01): any way to bypass? cuase it some point i might switch to freebuff, like they have better models
    - **u/Maglcite** (↑1, 2026-10-15 04:02): freebuff has some deceptive marketing like giving people credits for reviewing them, but you can bypass with omnirouter. personally i’d pay 1$ for command code goat and use omniroute
      - **u/borobinimbaba** (↑1, 2026-10-15 10:31): Commandcode cache was non existent for me.the 1 dollar plan didn't last as much as 15$ would

---

## To Opencode team: Can you add option to select date range along with the existing 7, 30 and all time options.
**u/Ok_Cartographer5609** · 2026-10-15 03:45 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x6bicw/to_opencode_team_can_you_add_option_to_select/)

---

## Built an open-source gateway that cuts coding-agent token spend in half
**u/Content_Survey_8456** · 2026-10-15 01:58 UTC · ↑2 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x69gce/built_an_opensource_gateway_that_cuts_codingagent/)

---

## [ Removed by Reddit ]
**u/AnteaterElectronic35** · 2026-10-15 01:15 UTC · ↑0 · 0 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x68m3p/removed_by_reddit/)

[removed]

---

## What is the best for Roblox studio coding?
**u/nottlluucas** · 2026-10-15 00:43 UTC · ↑17 · 47 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x67z5k/what_is_the_best_for_roblox_studio_coding/)

**Comentarios:**

- **u/FZRP2** (↑4, 2026-10-15 00:52): just try them theyre free
  - **u/nottlluucas** (↑0, 2026-10-15 01:01): im asking which on is the best
  - **u/Thedudely1** (↑2, 2026-10-15 04:24): I like getting other people's opinions on it even if I test them myself
- **u/Calm-Caterpillar2103** (↑5, 2026-10-15 00:59): Try each one
  - **u/nottlluucas** (↑-8, 2026-10-15 01:01): no im asking which one is the best
    - **u/Calm-Caterpillar2103** (↑9, 2026-10-15 01:01): Try each one and find the best one, roblox coding is usually not what anyone uses these ai’s for, they use em for general programming
      - **u/pikuray** (↑1, 2026-10-15 02:31): What's general programming?
        - **u/Calm-Caterpillar2103** (↑2, 2026-10-15 02:32): Desktop applications, benchmarking, decompilation, etc
      - **u/retardhari** (↑1, 2026-10-15 03:21): 90% of roblox top games are now fully ai generated
    - **u/HyperWinX** (↑1, 2026-10-15 03:50): No we are saying try them
- **u/OrganicInformation15** (↑14, 2026-10-15 01:03): If they are free, why not you try it out yourself? It’s hard to justify what’s “best” or “good” for your need.  
    Generally speaking, Cat Jam, Space Bunny and Muse Spark all receive ok-ish good review. But it may not suit your need so try it out yourself
  - **u/nottlluucas** (↑-7, 2026-10-15 05:32): Im asking which one is the best
    - **u/PinnuTV** (↑2, 2026-10-15 08:52): That's peak lazy. Can't even try and test out
      - **u/nottlluucas** (↑1, 2026-10-15 13:02): This is why im asking "which on is the best" like dude it did not come here to test everyone im asking
        - **u/PinnuTV** (↑1, 2026-10-15 15:59): By testing u would have long gotten the  answer
    - **u/OrganicInformation15** (↑1, 2026-10-15 16:18): I think I have attached a relatively good answer already.  
        Cat Jam, Space Bunny, and Muse Spark all receive “higher than average” review
        
        The reason I don’t have an answer for your “best” model is because I do not actually know your workflow.
        
        Sure, Roblox Studio coding, but besides the thing that you are actually coding for, I also need to know how you write prompts usually and the amount of workload (aka the “complexity” of your Roblox Studio project), as well as if you value the quality or the speed of the model more. 
        
        For example, if you usually write bad or not that precise prompts, I’d expect you to have a better thinking model. But thinking models need longer time each prompts. In the other hand, if you already write very precise instructions to the AI, you may not need that much thinking for the model. In that case, you could’ve chosen a flash model and save your time and token and call it a day.
        
        Hence, literally every comment is about to try it yourself. Unlike you, it’s not because we are being rude, it’s because we don’t really know how you will use AI and hence can’t give you a “BEST” answer.
- **u/Prior-Meeting1645** (↑22, 2026-10-15 01:06): Why are people assholes in this thread? Truth is, OP, models struggle with 3d the most so I wouldn’t even bother with those models for games. But muse 1.3 probably best out of those. Dont even try things like nematron lol
  - **u/nottlluucas** (↑2, 2026-10-15 01:09): thanks dude
    - **u/Amarsir** (↑2, 2026-10-15 01:58): I agree with u/Prior-Meeting1645 but would also give a nod to Space Bunny. I can't guarantee it will do what you want, but the company that made it (Minimax) puts extra effort into visual stuff so they have an above-average shot.
      - **u/FavstianEquanimity** (↑1, 2026-10-15 03:10): We know for sure already it is Minimax?
        - **u/Amarsir** (↑2, 2026-10-15 04:09): We're pretty sure. It uses <minimax> system tags around the data, which isn't something it would likely copy in model training.
- **u/migsperez** (↑1, 2026-10-15 01:10): Easy. Muse.
- **u/mrduckissocool** (↑3, 2026-10-15 01:22): i would just use freebuff if your gonna use opencode for free it has way nicer models for free
  - **u/a355231** (↑1, 2026-10-15 01:24): As much as I hate Freebuff, this is the way.
    - **u/mrduckissocool** (↑1, 2026-10-15 01:26): yea i used to use opencode but i did recently switched over to freebuff and rn they have some pretty good models
      - **u/a355231** (↑1, 2026-10-15 02:00): Just dont say anything remotely critical of them in the discord or they ban you.
        - **u/mrduckissocool** (↑1, 2026-10-15 02:31): didnt even know they had a discord lol
      - **u/Aggravating-Push-207** (↑1, 2026-10-15 06:22): Can you use those models in other agents
        - **u/Anduin1357** (↑1, 2026-10-15 08:08): Nope!
        - **u/mrduckissocool** (↑1, 2026-10-15 21:59): i dont think so but i would try the desktop ver of freebuff its alot better then the terminal one
- **u/Own_Load_5730** (↑1, 2026-10-15 01:24): Muse
- **u/Mundane-Mortgage-624** (↑1, 2026-10-15 01:49): deepseek  
    claude/codex
- **u/Monecreiff** (↑1, 2026-10-15 01:56): spacebunny is good in blender
- **u/levu304** (↑1, 2026-10-15 02:38): exclude nemotroll
- **u/Both-Ad6752** (↑1, 2026-10-15 02:42): space bunny is pretty good right now, but muse is the best on xhigh. seeing as you're into free models, look into nvidia nim. also get blender and its mcp for the 3d modelling side of things, alongside some good skills associated with it.
- **u/thecstep** (↑5, 2026-10-15 03:38): Muse is good. That said, I have a Chatgpt sub which supplements the ai assisted Roblox coding I do. Luna claims Muse misses things but they both do.
- **u/Thedudely1** (↑4, 2026-10-15 04:20): In my testing with Blender MCP, none of them can hold a candle to GPT or Claude or maybe Gemini models specifically for 3D stuff in programs like Blender and presumably Roblox. Muse Spark 1.3 has been closest in my testing. I've heard that people have had mixed results with Space Bunny but that it's perhaps more thorough than Spark 1.3. Those are the two I would try.
- **u/kamwee** (↑2, 2026-10-15 04:25): They are all trash  but  way better than paying
- **u/HelioDex** (↑3, 2026-10-15 04:28): I know a few Roblox devs who swear by MiMo V2.6 Flash. It's very good, just quite slow through OpenCode. Space Bunny (while it's available) seems decent and is fast too.
    
    Muse Spark is great and also fast, do note it has a different data retention policy than most of the other models. I'd take this as your best bet then the 2 above as 2nd choices.
    
    Step 5 is fine, I don't have much to say about it.
    
    For Cat Jam (while it's available), the Nemotrons, Big Pickle, and LongCat, I suggest avoiding them apart from small or very simple tasks. To get the same output quality from these ones compared to the larger models usually requires a lot more prompting.
    
    As long as you pick any decent model, the more important thing will be your setup. If you can get the Roblox Studio MCP server running and connect it to OpenCode, this will help a lot. Make sure you're using Script Sync (or Rojo or similar if you prefer). Good luck!
- **u/nottlluucas** (↑0, 2026-10-15 05:35): Thanks to the people who told me which one is the best
- **u/NinjaAlaska** (↑1, 2026-10-15 07:49): dont know abt robolox  
    but for coding muse is best 2nd best mimo 2.6 flash  
    others i have not tried yet space bunny and step 5 yet to try i love muse sticking to it. every one loves muse only tbh.
- **u/RainyDayFeel** (↑1, 2026-10-15 10:56): I've been using muse 1.3 and blender mcp, to make my daughter things for Roblox. Works a lot better than I thought it would.
- **u/Odd_Abrocoma_8421** (↑1, 2026-10-15 12:04): Deepseek 4.1v free
- **u/Mementem** (↑1, 2026-10-15 14:08): many people have recommended muse spark, yes it is the best for usecase.   
    but personally i would suggest staying away from it, i just don't trust Mark Zuckerberg with any of my information.
- **u/OrganicInformation15** (↑1, 2026-10-15 16:20): Forgot to mention, OpenCode now have DeepSeek V4.1 Flash for free. I think that’s by far the best model you could’ve

---

## Opencode (Big Pickle) typo :D
**u/Robert__Sinclair** · 2026-10-15 00:28 UTC · ↑7 · 3 comentarios · [enlace](https://www.reddit.com/r/opencode/comments/1x67o0f/opencode_big_pickle_typo_d/)

![img](j4a6e1unzivh1 "murder! :D")

**Comentarios:**

- **u/IntrepidMindExplorer** (↑3, 2026-10-15 00:51): Have you been being mean to Big Pickle? May want to sleep with the lights on from now on.
  - **u/Robert__Sinclair** (↑1, 2026-10-15 09:45): lol
- **u/eachDayIWakeUp** (↑1, 2026-10-15 00:58): 👀

---
