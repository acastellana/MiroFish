# MiroFish Run #2 — Design Brief
**Core question: Which product on top of GenLayer finds PMF first, and what is its GTM?**

---

## The Question We're Answering

GenLayer is infrastructure. Infrastructure doesn't have PMF — products built on it do.

We have four candidate products:

| Product | What it does | Current state |
|---------|-------------|---------------|
| **A. Conditional Payment (Trade Escrow)** | AI-verified B2B cross-border payment escrow replacing LCs | Demo deployed, 1 reference scenario (Bolivia→Peru lithium) |
| **B. InternetCourt (General Dispute Resolution)** | Court-as-a-service for any agent-to-agent agreement | Architecture deployed, no live cases |
| **C. AI Task Escrow SDK** | "Pay on delivery" for AI agent hiring AI agent | Spec-level, no deployment |
| **D. Dispute Resolution API (SaaS)** | Marketplace dispute engine: POST evidence → GET verdict | Spec-level, no deployment |

The simulation should produce a ranked answer: which product reaches escape velocity first, in which market, via which channel, with which customer type?

---

## World State at Simulation Start

**This simulation starts 3 days after a major public incident. All agents know about it. It is the dominant topic.**

### The Incident (3 days ago — Day -3)

FreshCargo shipment #23 — an $85,000 lithium carbonate export from Minera Andina SRL (Bolivia) to a Peruvian importer — returned UNDETERMINED from GenLayer. The importer's customs document images were too low-resolution for the AI jury to read the border crossing timestamp. The importer is withholding the $85,000. FreshCargo CEO María Quispe posted on LinkedIn 3 days ago:

> "We are working with GenLayer to resolve this. In the meantime, we have paused new shipments on the platform pending a process review. We remain committed to this technology but we owe our clients certainty."

The post has 847 comments. EscrowChain's BD director responded publicly: "Rules don't have resolution failures. This is why we use deterministic logic, not AI." Bloomberg is writing a follow-up piece. The LatAm fintech VC who was about to wire a $500K check to FreshCargo is now on hold.

### Concurrent Context (also happened in the last 2 weeks)

1. **InternetCourt public beta launched** — announced on Product Hunt (#3 of the day) and HN (312 points). First 100 contracts free. AI agent developers are actively experimenting.

2. **EscrowChain (Stripe-backed) launched publicly** with Flexport partnership. Immediately positioned around "deterministic, auditable, legally enforceable" — the anti-AI message.

3. **Rentahuman.ai integrated InternetCourt** for their agent marketplace — 500 active agent-to-agent transactions now using GenLayer for dispute resolution. Working smoothly. Zero UNDETERMINEDs so far (agent task evidence is structured JSON, not scanned documents).

4. **GenLayer team posted a technical post-mortem** on the UNDETERMINED incident: root cause was evidence submission UX (no minimum image resolution requirement). Fix: added resolution validation before submission. Existing case: will offer extended evidence resubmission window.

This is the world the simulation starts in. The first question every agent must answer: **does the UNDETERMINED incident kill Product A, or is it a recoverable process failure?** And while Product A deals with the fallout, is Product B/C quietly pulling ahead?

---

## Simulation Design

### Agent Roster (~45 agents with persona histories)

**Product A world (Trade Escrow):**

- **María Quispe** — FreshCargo CEO (La Paz, Bolivia). 42 years old. Built FreshCargo over 12 years from a 2-person customs broker to a 35-person freight forwarding company. 620 SME clients, mostly bolivian miners and agricultural exporters. Has been burned twice by banks refusing her clients LC applications. Took a personal risk adopting GenLayer. Now publicly defending it while privately furious at the UNDETERMINED outcome. She has been talking to EscrowChain's BD director for a coffee meeting "just to understand the competitive landscape." Her board is asking hard questions.

- **Carlos Mendoza** — Owner of Minera Andina SRL (Oruro, Bolivia). His $85K is locked. He has 8 employees and a payroll due in 10 days. He trusted FreshCargo's recommendation. He is not technical. He wants his money and an explanation he can understand. He is posting on a bolivian exporters WhatsApp group with 200 members.

- **Alejandro Rivas** — BBVA Trade Finance Director (Madrid). Manages $200M in LC portfolio across LatAm. Has been watching GenLayer with detached interest — until the UNDETERMINED incident, which he is now citing in every internal meeting as proof that AI-based trade finance is not ready. He is preparing a LinkedIn post about "why proven instruments matter."

- **Sophie Leclerc** — EU DG FISMA regulatory officer (Brussels). Working on AI Act implementation. The FreshCargo incident landed in her inbox via a fintech lobbying group. She is drafting a consultation paper on AI systems in financial dispute resolution. She has not spoken to GenLayer. She is cautious but not hostile — she wants to understand before regulating.

- **James Hartley** — EscrowChain BD Director (London). 34 years old. Ex-Stripe. Has been cold-calling every freight forwarder in LatAm since the Flexport partnership announcement. He has a meeting with Cargonaut (FreshCargo's largest competitor) tomorrow. He is genuinely opportunistic about the incident — not malicious, just doing his job.

- **Ana Vargas** — Peruvian importer (Lima). The importer in the FreshCargo incident. She didn't choose GenLayer — her supplier did. She has the $85K locked in a contract she barely understood. She hired a local lawyer to review the situation. She is not a villain — she's confused and defensive.

- **Rafael Torres** — LatAm fintech VC (Monashees, São Paulo). Was 2 weeks from wiring $500K to FreshCargo as a seed check. On hold. Has invested in 3 fintech infrastructure companies. He understands the technology. He is now doing deep diligence calls on UNDETERMINED failure rates and asking for access to GenLayer's internal metrics.

- **Elena Savchenko** — Geneva trade finance lawyer. Has been building a legal framework for smart contract arbitration. Privately believes the UNDETERMINED incident is actually the best thing that could have happened — it proves the system has a safety valve (UNDETERMINED is better than a wrong verdict). She is writing a blog post about this.

**Product B/C/D world (Agent Economy):**

- **Marcus Chen** — AI agent developer (San Francisco). Building on GenLayer SDK. Has 3 agents deployed using InternetCourt contracts. Zero disputes so far but he's stress-testing edge cases. He watched the FreshCargo incident and his reaction was: "completely different use case — my agents submit structured JSON, not scanned documents. This doesn't affect me." He is posting technical content about his integration.

- **Priya Nair** — Rentahuman.ai PM (Product). Running the InternetCourt integration. 500 transactions live. First UNDETERMINED risk: a coding task where the test suite itself was disputed. She resolved it by adding "evidence definition: test suite must be submitted at contract creation, not dispute time." She is building internal playbooks. She wants more features from GenLayer.

- **David Kim** — AgentHub CEO (YC W25, San Francisco). Agent infrastructure platform. Has been watching the Rentahuman.ai integration with interest. His agents have a 12% dispute rate. He is evaluating whether to integrate GenLayer or build his own arbitration. He is talking to Marcus Chen and Priya Nair informally.

- **Sebastien Moreau** — Kleros community lead (Paris). Watching InternetCourt launch with competitive interest. Has been posting technical comparisons: "GenLayer is faster and cheaper but has no track record. Kleros has 8,000 resolved cases. Trust takes time." He is not hostile — he's positioning for a world where both platforms coexist for different use cases.

- **Jennifer Walsh** — YC partner. Has seen 12 pitches for "dispute resolution infrastructure" in the last year. Most failed because they couldn't answer: "who pays per dispute, and how many disputes happen?" She is watching GenLayer's numbers. The agent economy integration is more interesting to her than trade finance.

- **Tom Baker** — legal tech VC (Bessemer). "Private arbitration market is already solved by Kleros. What GenLayer is doing in trade finance is interesting but the legal enforceability problem will take 5+ years to solve in any meaningful jurisdiction. I'm watching but not investing."

- **Alex Park** — OpenAgents Protocol maintainer. Wants to recommend a dispute resolution layer in the standard. Was going to recommend Kleros. Now evaluating GenLayer. Watching the FreshCargo incident to assess reliability before recommending to 2,400 developers who follow the standard.

**Media:**

- **Sarah Mitchell** — Bloomberg fintech journalist. Wrote the original skeptical piece. Now has a follow-up deadline in 5 days. She is reaching out to María Quispe, Carlos Mendoza, and EscrowChain for comment. She will publish regardless of whether GenLayer responds. Her framing: "AI trade finance stumbles on first real test."

- **Kevin Zhao** — CoinDesk reporter. More sympathetic to crypto/web3. Covering the InternetCourt launch and agent economy angle. Sees the trade escrow incident as a distraction from the more interesting agent commerce story.

- **@TradeTruth** — Anonymous Twitter/X account (likely a competing trade finance consultant). First to post about the UNDETERMINED incident before FreshCargo's official statement. 12,000 followers in trade finance. Posts technical critiques with insider knowledge. Possibly connected to a traditional trade finance firm.

---

## Success Criteria (Define Before Running)

The simulation is useful if, after reading the report, Albert can answer:

1. **Which product has the clearest path to 10 paying customers in 6 months?**
2. **What is the specific ICP** — precise enough that a salesperson could call them tomorrow?
3. **What is the single biggest GTM risk** that could kill the leading product?
4. **Did Product A recover from the UNDETERMINED incident**, or did it permanently damage the category?
5. **Did Products B/C/D accelerate while Product A was in crisis** — and if so, does that change the priority order?

---

## Report Prompt (Use Exactly)

> You are GenLayer's CEO. You have just observed 90 days of market simulation. The simulation started 3 days after the FreshCargo UNDETERMINED incident — when the company was in crisis. Four products were competing for attention simultaneously: trade escrow (Product A), InternetCourt general dispute resolution (Product B), AI Task Escrow SDK (Product C), and Dispute Resolution API (Product D). Based purely on what you observed in the simulation, answer these five questions. Do not summarize. Do not describe. Answer each with a specific, actionable recommendation backed by evidence from the simulation:
>
> (1) Which product had the strongest organic pull signal — where did adoption happen without being pushed by the team?
> (2) Who is the specific ideal customer for the leading product — described with enough precision that a salesperson could identify and call them tomorrow?
> (3) What GTM motion produced the first replicable sale — channel, trigger event, and message?
> (4) Did Product A (trade escrow) recover from the UNDETERMINED incident, or did it lose the freight forwarder channel to EscrowChain permanently?
> (5) What is the one move GenLayer should make in the next 30 days that no one in the simulation is currently advocating for?

---

## Simulation Parameters

- **Seed files (upload all 5)**:
  - `genlayer-technical-architecture.md`
  - `competitive-landscape-and-trigger-event.md`
  - `market-reality.md`
  - `agent-economy-landscape.md`
  - `PMF-ANALYSIS.md`
- **Simulation requirement** (paste as the prompt): *"It is June 2026, 3 days after the FreshCargo UNDETERMINED incident. GenLayer has four products in market simultaneously: trade escrow (Product A), InternetCourt general dispute (Product B), AI Task Escrow SDK (Product C), Dispute Resolution API (Product D). EscrowChain (Stripe-backed) is competing directly on Product A. Rentahuman.ai has 500 live agent transactions on Product B. Simulate 90 days of market reaction: who recovers, who grows, who wins the freight forwarder channel, and which product finds PMF first?"*
- **Rounds**: 60
- **Agent count**: ~45
- **Platforms**: Reddit (debate) + Twitter (rapid reaction)
- **Model**: gpt-5-nano (~$0.15 total)

---

## What We're NOT Doing

- Not validating our existing thesis (Run #1 did that)
- Not asking "is GenLayer a good idea"
- Not simulating general public opinion

We are running a narrow, adversarial, crisis-starting simulation with geographically-specific agents, a pre-encoded failure event, and four competing products — designed to answer one question: **which product, which customer, which motion.**
