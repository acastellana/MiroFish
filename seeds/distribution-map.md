# Distribution Map — How GenLayer Reaches Customers

## Overview

GenLayer has five potential distribution channels. Currently it is investing heavily in only one (marketplace direct) and weakly in another (developer-led). Three channels are effectively zero. This document maps the channels, their current state, and what it would take to activate them.

---

## Channel 1: Developer-Led (Bottom-Up)

**Entry point:** SDK, open-source, blog posts, HN, developer advocates, tutorial series

**How it works:** An indie developer or early-stage engineer discovers GenLayer through content or community. They integrate the SDK. It works. They write about it. Other developers discover GenLayer through their content. Framework maintainers notice the adoption signal and consider integrating.

**Current state: WEAK**
- Yuki Tanaka's viral post is net-negative for GenLayer today (4-day setup vs 30-minute VeritasProtocol)
- No developer advocate on the GenLayer team
- Docs reference v0.3.x while SDK is on v0.4.x
- No evidence schema library, no use-case packs, no 30-minute quickstart
- Tom Okafor (Composio, 18K devs) is routing developers to VeritasProtocol because of SDK simplicity

**What would accelerate it:**
- Ship a 30-minute quickstart that actually works in 30 minutes
- Publish a pre-built evidence schema library (code review, research quality, data annotation)
- Hire a developer advocate whose only job is developer experience
- Get Yuki Tanaka to publish a successful GenLayer tutorial (she's signaled willingness)
- Ship the v0.4.x docs before Run #3 simulation starts

**Who controls this channel:** Tom Okafor, Rachel Torres, Yuki Tanaka, @AgentWatch

**Speed to first deal:** 2-4 months (developer → production → paid)
**Typical deal size:** $200-$2,000/month (early-stage marketplace)
**Scalability:** High — one viral post can drive 1,000 developer trials
**Defensibility:** Low — VeritasProtocol can improve their SDK anytime
**Current GenLayer investment:** Low

---

## Channel 2: Marketplace Operator Direct Sales

**Entry point:** BD outreach to marketplace CEOs, inbound from Rentahuman.ai reference, conference conversations

**How it works:** Daniel Marin (Head of BD) contacts marketplace operators. Operator evaluates GenLayer. Refers to Rentahuman.ai as reference. Eventually commits. Each new production integration becomes a reference for the next.

**Current state: MODERATE**
- 1 production reference (Rentahuman.ai) with strong data (35K tx, 94% acceptance, 0 unresolved)
- 5+ marketplaces in active evaluation (DevSwarm, AgentHub, DataForge, PixelPact, TaskRail)
- Daniel Marin is a team of 1 and stretched thin
- Priya Nair (Rentahuman.ai) is the bottleneck — every prospect wants to talk to her

**What would accelerate it:**
- Second production integration (any marketplace in current evaluation) — triggers contagion
- "Contagion call" mechanism: brief Zara Ahmed (DevSwarm) on AgentHub's trial progress so she can't wait; brief Marcus Chen on Sofia's urgency
- Relieve Priya Nair bottleneck: publish her case study as a self-serve document; record a 20-minute video interview; create a reference FAQ she can send instead of taking calls
- Hire a second BD person or junior AE

**Who controls this channel:** Daniel Marin (GenLayer), Priya Nair (reference bottleneck)

**Speed to first deal:** 30-90 days per marketplace
**Typical deal size:** $2,000-$20,000/month at managed API pricing; less at SDK pricing
**Scalability:** Low per person — BD-intensive, requires Priya Nair calls
**Defensibility:** High — production reference + relationship moat
**Current GenLayer investment:** Medium (1 BD person)

---

## Channel 3: Framework Integration (OEM)

**Entry point:** Partnership with LangGraph, CrewAI, AutoAgent, or other major frameworks

**How it works:** A framework ships GenLayer as the default or recommended dispute backend. 8,000+ developers using the framework get GenLayer as the path of least resistance. No individual sales required.

**Current state: ACTIVE BUT AT RISK**
- LangGraph decision (Day 35): Rachel Torres has the formal VeritasProtocol offer ($200K developer credits + dedicated engineer) and two informal GenLayer calls
- CrewAI RFP (Day 35): Nina Patel running a formal process; enterprise clients want compliance docs
- AutoAgent: Derek Walsh is building a competing open-source module (ships Day 20)

**What would accelerate it:**
- GenLayer must match VeritasProtocol's investment in Rachel Torres: dedicated integration engineer, formal partnership offer, SDK improvements before Day 10
- For CrewAI: compliance documentation is the blocker — SOC 2 timeline, SLA draft
- Dual-recommendation is still a win: Rachel recommends VeritasProtocol for simple, GenLayer for judgment — this is framework distribution for GenLayer's natural segment

**Who controls this channel:** Rachel Torres (LangGraph), Nina Patel (CrewAI)

**Speed to first deal:** 1-3 months (framework ships integration)
**Typical deal size:** No direct revenue — volume (8K devs in LangGraph ecosystem)
**Scalability:** Very high — one integration, massive developer reach
**Defensibility:** Medium — once integrated as default, switching costs emerge
**Current GenLayer investment:** Low (2 informal calls with Rachel; no formal offer)

---

## Channel 4: Enterprise (Top-Down)

**Entry point:** Systems integrators (Accenture, Deloitte), enterprise AI procurement, regulated industry VPs

**How it works:** An enterprise AI deployment project includes dispute resolution as a requirement. A systems integrator evaluates vendors and recommends GenLayer. Or an enterprise buyer (Sandra Lee at Shopify, Aisha Okonkwo at Klarna) adds GenLayer to their vendor shortlist.

**Current state: ZERO**
- GenLayer has not met Accenture (Ben Nakamura is leaning VeritasProtocol by default)
- No SOC 2, no SLA, no managed service — the three enterprise entry requirements
- Sandra Lee's legal team and engineering team are split; no GenLayer engagement with either
- Aisha Okonkwo (Klarna) is waiting 6 months

**What would accelerate it:**
- First meeting with Accenture's AI ventures team (Ben Nakamura) — this is a sales failure, not a product failure
- SOC 2 audit process started immediately (even in progress gives credibility)
- SLA draft document (even without infrastructure to back it up, shows intent)
- Enterprise case study (Shopify or Klarna pilot would unlock this channel)

**Who controls this channel:** Ben Nakamura (Accenture), Sandra Lee (Shopify), Aisha Okonkwo (Klarna)

**Speed to first deal:** 3-6 months (enterprise procurement cycle)
**Typical deal size:** $50,000-$500,000/year
**Scalability:** Medium — each Accenture recommendation covers 50 enterprise clients
**Defensibility:** Very high — enterprise switching costs and compliance lock-in
**Current GenLayer investment:** Zero

---

## Channel 5: Content / Analyst Narrative

**Entry point:** VC blog posts, The Information, market maps, Twitter/X technical analysis

**How it works:** A VC (Fatima Al-Rashidi, Sequoia) or journalist (Jessica Park, The Information) or technical analyst (@AgentWatch) publishes an influential piece that shapes how enterprise buyers and developers evaluate the space. GenLayer appears favorably → inbound inquiries increase → sales cycle shortens.

**Current state: BEHIND**
- Fatima Al-Rashidi's market map publishes in 3 weeks: GenLayer ranked second, "great tech, go-to-market unclear"
- Lior Ben-David (a16z, VeritasProtocol investor) publishes in 8 days: "deterministic-first" framing favors VeritasProtocol
- @AgentWatch: supportive of GenLayer technology but scathing on DX ("operationally negligent")
- Jessica Park (The Information): forcing marketplace CEOs to take public positions — could go either way

**What would accelerate it:**
- Give Fatima Al-Rashidi a compelling adoption narrative before she publishes: behavioral effect data, Rentahuman.ai production numbers, second production reference if available
- Brief @AgentWatch on SDK improvement timeline; they are not hostile to GenLayer, just honest
- Brief Jessica Park on the Rentahuman.ai case study with Priya Nair as primary source
- GenLayer CEO should be available for press in the next 2 weeks — this is a narrative window

**Who controls this channel:** Fatima Al-Rashidi, Jessica Park, @AgentWatch, Lior Ben-David

**Speed to first deal:** Indirect — influences procurement in 30-90 days after publication
**Typical deal size:** Not direct; accelerates all other channels
**Scalability:** Very high — one good article reaches 40K+ readers
**Defensibility:** Low — VeritasProtocol can brief the same analysts
**Current GenLayer investment:** Low (reactive, not proactive)

---

## The Distribution Verdict: Which Channel Wins in 90 Days?

**Primary channel recommendation: Channel 2 (Marketplace Operator Direct Sales) + Channel 3 (Framework Integration) simultaneously**

Reasoning:
- Channel 2 is already warm — 5+ marketplaces in evaluation, one production reference. The bottleneck is converting evaluation to production. A second production reference creates contagion.
- Channel 3 has a 5-week decision window (LangGraph Day 35). Missing it means VeritasProtocol becomes the default for 8,000 developers. Winning even the dual-recommendation gives GenLayer framework distribution for its natural segment.
- Channel 1 (developer-led) is a prerequisite for Channel 3 — the SDK must work in 30 minutes before Rachel Torres will recommend it. So Channel 1 improvements feed Channel 3.
- Channel 4 (enterprise) and Channel 5 (content/analyst) are 3-6 month plays — start them now but don't expect wins in 90 days.

**The one move that changes everything:** Ship the managed REST API (Tier 2). It unblocks Sofia Eriksson (Day 25 deadline), makes the LangGraph integration trivially simple, removes the web3 barrier for enterprise buyers, and gives GenLayer pricing power. It's a 6-week build. Start now.
