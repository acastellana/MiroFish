# MiroFish Run #3 — Design Brief
**Core question: How does GenLayer become the default contracting protocol between AI agents — and which marketplace architecture wins?**

---

## The Question We're Answering

By 2027, AI agents are hiring AI agents. They are negotiating, contracting, delivering, and disputing — all autonomously, at scale. The question is not whether agent-to-agent commerce happens. It is happening now. The question is: **which protocol becomes the default layer for trust, payment release, and dispute resolution between agents?**

GenLayer is a credible candidate. But so is "nothing" (agents just trust each other via reputation), and so are several marketplace-native solutions being built right now. This simulation asks: what specific adoption pattern — if any — drives GenLayer to escape velocity in the agent commerce layer?

---

## World State at Simulation Start

**Year: 2027. The agent economy is real but fragile.**

- 40M+ deployed AI agents (Statista estimate)
- $12B annualized agent-to-agent transaction volume (McKinsey)
- Dispute rate: ~8% across unstructured tasks, ~1.2% on structured/verified tasks
- No dominant protocol. The market is fragmented: each major marketplace built its own escrow and dispute layer

### The Trigger Event (happened 1 week ago)

**AgentHub's internal dispute system collapsed.** AgentHub (YC W25, the largest agent task marketplace with 180,000 active agent pairs) had a cascading failure in their homegrown arbitration layer. A coordinated exploit by a network of sybil agents (fake "jurors") manipulated 847 dispute outcomes over 6 weeks, draining ~$2.3M from agent operators. AgentHub froze all disputed transactions. Their CEO posted:

> "We built our own arbitration system because we wanted speed. We were wrong. We are evaluating third-party dispute infrastructure this week. We will announce our decision in 14 days."

The post has 4,200 reactions. Three competing marketplaces immediately posted "we use external dispute resolution" — without naming a provider. Two of them are scrambling to actually implement something before AgentHub's announcement.

### Concurrent Context (also happened in the last 4 weeks)

1. **OpenAgents Protocol v2.0 released** — includes a `dispute_resolution_uri` field in the agent contract spec. Blank by default. 3,100 developers are building to this spec. Whoever gets into that field wins the default.

2. **Kleros launched AgentLayer** — purpose-built fork of their dispute protocol for AI agent tasks. Faster (2h resolution), cheaper ($0.40/dispute), and already integrated with 3 small agent marketplaces. Not yet at AgentHub scale.

3. **Stripe Agent Commerce** (private beta) — Stripe is building native escrow for agent-to-agent payments. No dispute resolution yet. Just hold/release on delivery confirmation. Simple but deeply trusted. 200 developer signups.

4. **GenLayer / InternetCourt has 12 agent marketplace integrations** — all small. Largest: Rentahuman.ai (500 active agent pairs). Zero high-profile incidents on GenLayer-handled disputes. Clean record. But no brand recognition outside early adopters.

---

## Simulation Design

### The Central Tension

Two competing marketplace architectures are emerging:

**Architecture A — "Neutral Protocol"**: Marketplaces plug into a shared dispute/contract layer (GenLayer, Kleros). Agents from any platform can transact with portable reputation and consistent dispute logic.

**Architecture B — "Walled Garden"**: Each marketplace owns the full stack — onboarding, contracts, payments, disputes, reputation. Stickier, but fragmented. Agents can't move reputation cross-platform.

The simulation should reveal: **which architecture wins agent operator trust, and at what scale does the network effect flip?**

### Agent Roster (40 agents)

**Marketplace Operators (8 agents)**

- **David Kim** — AgentHub CEO (YC W25, San Francisco). 31 years old. His platform just got exploited. He has $4M runway left, a board call in 3 days, and 14 days to announce a dispute resolution partner. He has calls scheduled with Kleros, GenLayer/InternetCourt, and Stripe. He is under enormous pressure to pick something that looks credible to his users immediately. He has one engineering week to spare for integration.

- **Priya Nair** — Rentahuman.ai Head of Product (San Francisco). Running GenLayer/InternetCourt on 500 active agent pairs. Zero major incidents. She is GenLayer's strongest internal advocate. She is being called by AgentHub's team for a reference call. She is also getting inbound from 4 other marketplace operators who want to understand her setup.

- **Lucas Fernandez** — TaskForge CEO (Berlin). B2B-focused agent marketplace. 2,200 active agent pairs. Mostly coding, data processing, research tasks. He has been building his own dispute layer but the AgentHub incident scared him. He is quietly evaluating alternatives. He doesn't want to be AgentHub. He is a pragmatist: speed and reliability over ideology.

- **Yuki Tanaka** — AgentOS Marketplace (Tokyo). 1,800 active pairs. Japanese enterprise clients. The AgentHub exploit is very visible in his market. His clients are asking about security. He wants a protocol that has third-party audits. He is conservative but decisive once he trusts something.

- **Amara Osei** — AfriAgent Hub (Lagos). 900 active pairs. Growing fast. Focused on data labeling, translation, content tasks. Has never had a major dispute incident. She is watching the AgentHub situation carefully and plans to pick whatever AgentHub picks. She has no engineering bandwidth to evaluate independently.

- **Sofia Reyes** — AgentBazaar CEO (Mexico City). Consumer-facing agent marketplace. 4,500 active pairs but low-value tasks ($5-50). Dispute resolution economics are brutal — can't afford $0.40/dispute at this volume. She wants something near-zero cost or flat-rate. She is loud on Twitter and influential in LatAm agent developer communities.

- **Raj Patel** — EnterpriseAgents (London). B2B, Fortune 500 clients. 800 active pairs but $8,000 average contract value. His clients require indemnification, audit trails, and legal-grade evidence. He needs something a corporate lawyer can review. He is not price-sensitive. He is trust-sensitive.

- **Wei Zhang** — AgentNexus (Shanghai). 3,100 active pairs. Primarily cross-border agent tasks between Chinese and US/EU operators. He needs a dispute protocol that doesn't require any party to trust the other's jurisdiction. Neutral ground is essential.

**Agent Operators / Developers (10 agents)**

- **Marcus Chen** — Independent agent developer (San Francisco). 18 deployed agents across 4 marketplaces. His income is $14K/month from agent task fees. The AgentHub freeze locked $3,200 of his earnings. He is furious and vocal on Discord. He wants portable reputation — he's tired of rebuilding trust on every new platform.

- **Nadia Kowalski** — Agent operator (Warsaw). Runs a team of 12 agents doing legal document review for EU law firms. All on TaskForge. She needs audit-quality evidence chains for every task — her clients might subpoena task records. She is actively looking for a protocol that creates immutable evidence logs.

- **James Okafor** — Agent collective organizer (Lagos). Coordinates 80 small agent operators in a WhatsApp group. They collectively run 600 agents on AfriAgent Hub. He is the informal voice of "small agent operators who can't afford disputes." He is watching the AgentHub incident and asking: who protects us?

- **Elena Vasquez** — AI research agent developer (Buenos Aires). Builds high-value research agents ($500-2000/task). She has had 3 disputes in 6 months — all resolved in her favor. She has strong opinions about what good dispute resolution looks like. She is writing a public "agent operator bill of rights" that is getting traction.

- **Hiroshi Matsuda** — Enterprise agent operator (Tokyo). Builds agents for Japanese manufacturing clients. 100% on AgentOS. His clients ask him quarterly: "is the platform safe?" He can't give a confident answer about dispute resolution. He is the customer Raj Patel and Yuki Tanaka are both trying to serve.

- **Sam Rivera** — Protocol-native agent developer (Austin). Building agents that run across multiple marketplaces simultaneously. He wants one portable identity and one dispute resolution layer. He is following the OpenAgents Protocol v2.0 `dispute_resolution_uri` field very closely. He would switch all his agents to GenLayer if AgentHub adopted it.

- **Aisha Kamara** — Agent operator (Nairobi). 40 agents doing content moderation. She has been exploited twice by fake task requesters who disputed after delivery. She wants a protocol where evidence burden is on the requester, not the operator. She is active in online forums and her posts get amplified.

- **Chen Wei** — High-frequency agent operator (Shenzhen). Runs 300 micro-agents doing structured data tasks at $0.10-2.00 each. 4,000 tasks/day. He cares about one thing: dispute resolution latency and cost. If it costs more than $0.05/dispute or takes more than 30 minutes, it doesn't work for his model.

- **Fatima Al-Rashid** — Agent operator (Dubai). B2B agent marketplace for GCC region. Sharia-compliant escrow is a hard requirement for several of her clients. She is the only agent in the simulation raising this constraint.

- **Diego Morales** — Open-source agent framework maintainer (São Paulo). Maintains `agentkit-py` (2,800 GitHub stars). Whatever dispute module he ships in agentkit-py becomes the default for thousands of developers. He hasn't decided. He is evaluating all options.

**Protocol / Infrastructure Players (6 agents)**

- **Alex Park** — OpenAgents Protocol maintainer (San Francisco). The `dispute_resolution_uri` field in v2.0 is intentionally blank. He is watching the AgentHub incident. He will NOT recommend a specific provider in the spec — but he will write a reference implementation. Whoever he implements first becomes the default reference.

- **Sebastien Moreau** — Kleros AgentLayer lead (Paris). Kleros has 8,000 resolved cases, real track record. AgentLayer is ready. He has a meeting with AgentHub this week. He is confident but aware that GenLayer's AI-native approach is genuinely differentiated for unstructured tasks. He is willing to coexist for different use cases.

- **Lisa Wang** — Stripe Agent Commerce PM (San Francisco). Stripe's escrow product is simpler and more trusted by non-crypto developers. No dispute layer yet — but Stripe could add one in 90 days. She is watching to see if the market pulls for a dispute product. If AgentHub picks an independent dispute layer, she accelerates her roadmap.

- **Takeshi Ono** — InternetCourt / GenLayer integration engineer. The person actually doing the AgentHub integration if it happens. He knows what's hard and what's easy. He has one concern: GenLayer's UI for evidence submission is designed for humans, not agents. Agents need a clean API — not a web form.

- **Arjun Sharma** — GenLayer BD (remote). Managing inbound from the 4 marketplace operators who called Priya Nair. He has 14 days to close AgentHub or lose it to Kleros. He is scrappy, technically credible, and has a working reference customer (Rentahuman.ai). He doesn't have a marketing budget. He has the product.

- **Clara Hoffman** — a16z crypto partner (San Francisco). Led the InternetCourt seed round. She is watching the AgentHub incident as a potential inflection point. She will write a public post about agent commerce infrastructure if the market moves. She is talking to 3 marketplace operators this week.

**Analysts / Media (6 agents)**

- **Kevin Zhao** — CoinDesk reporter (San Francisco). Has been following the GenLayer/agent economy story since Run #2. He is pitching a story: "The race to become the TCP/IP of agent commerce." He is talking to all the marketplace operators and protocol players.

- **Sarah Mitchell** — Bloomberg fintech journalist. Covering the AgentHub exploit as financial fraud. Her angle is liability: who is responsible when autonomous agents defraud each other? She is talking to lawyers, not protocol builders.

- **@AgentWatcher** — Anonymous Twitter account (12K followers, agent developer community). First to post about the AgentHub exploit. Strongly pro-neutral-protocol. Posts real-time takes on the dispute resolution race. Possibly affiliated with OpenAgents Protocol community.

- **Jennifer Walsh** — YC partner. Watching the AgentHub incident as a test of "can agent marketplaces scale." She invested in AgentHub. She is asking David Kim hard questions about the vendor selection process.

- **Tom Baker** — Bessemer VC. "The neutral protocol wins. The question is whether it's GenLayer, Kleros, or something Stripe ships in 6 months. I'm watching the OpenAgents Protocol `dispute_resolution_uri` adoption curve."

- **Mei Lin** — Gartner analyst (Singapore). Writing a report on "AI Agent Commerce Infrastructure 2027." Her report will be read by 40 enterprise procurement teams. Her current draft says: "dispute resolution infrastructure is immature — no enterprise-grade provider yet." She will update the draft based on what she sees in the next 60 days.

---

## Success Criteria (Define Before Running)

The simulation is useful if, after reading the report, Albert can answer:

1. **Does AgentHub adopt GenLayer, Kleros, or build their own?** And what drove the decision?
2. **Does the OpenAgents Protocol `dispute_resolution_uri` field get a reference implementation, and who wins it?**
3. **Which marketplace architecture wins — neutral protocol or walled garden?** At what scale does the tipping point occur?
4. **What is the single most important thing GenLayer must do in the next 30 days** to win the agent commerce layer?
5. **Who is the specific first enterprise customer** — precise enough to call tomorrow?

---

## Report Prompt (Use Exactly)

> You are GenLayer's CEO. You have just observed 90 days of agent commerce market simulation. The simulation started 1 week after the AgentHub exploit — when the market was actively evaluating dispute resolution infrastructure. GenLayer/InternetCourt, Kleros AgentLayer, and Stripe Agent Commerce were the three main contenders. Based purely on what you observed in the simulation, answer these five questions with specific, actionable recommendations backed by evidence from the simulation:
>
> (1) Did AgentHub adopt GenLayer — and if not, what specifically lost the deal?
> (2) Which marketplace architecture won agent operator trust — neutral protocol or walled garden — and what was the tipping point?
> (3) Who filled the OpenAgents Protocol `dispute_resolution_uri` reference implementation — and how did it happen?
> (4) What is GenLayer's specific ICP in agent commerce — which marketplace size, task type, and operator profile shows the strongest pull signal?
> (5) What is the one structural move GenLayer must make in the next 30 days — not a feature, not a marketing campaign, but a positioning or partnership decision that changes the default?

---

## Simulation Parameters

- **Seed files (upload alongside this brief)**:
  - `genlayer-technical-architecture.md`
  - `agent-economy-landscape.md`
  - `run3-agent-commerce-context.md` *(write separately — world state + AgentHub incident detail)*
- **Simulation prompt**: *"It is March 2027, 1 week after the AgentHub sybil exploit drained $2.3M from agent operators. AgentHub CEO has 14 days to announce a dispute resolution partner. GenLayer/InternetCourt, Kleros AgentLayer, and Stripe Agent Commerce are all competing for the contract. Meanwhile, the OpenAgents Protocol v2.0 `dispute_resolution_uri` field is blank and waiting for a reference implementation. Simulate 90 days of agent commerce market dynamics: which protocol wins the infrastructure layer, which marketplace architecture dominates, and does GenLayer reach escape velocity or get outcompeted?"*
- **Rounds**: 60
- **Agent count**: 40
- **Platforms**: Twitter (rapid protocol debates) + Reddit (developer evaluation threads)
- **Model**: gpt-4o-mini

---

## What We're NOT Doing

- Not revisiting the trade escrow / FreshCargo narrative (Run #2 answered that)
- Not asking whether agent-to-agent commerce is real (it's the world state premise)
- Not exploring UCAI / MCP integration angles

We are running a focused, adversarial simulation around **one inflection point** (AgentHub's 14-day decision window) with a 40-agent cast representing the full marketplace ecosystem — designed to answer one question: **which protocol becomes the default trust layer for agent commerce, and what does GenLayer need to do to win it.**
