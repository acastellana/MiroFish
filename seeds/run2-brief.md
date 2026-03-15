# MiroFish Run #2 — Design Brief
**Core question: Which product on top of GenLayer finds PMF first, and what is its GTM?**

---

## The Question We're Answering

GenLayer is infrastructure. Infrastructure doesn't have PMF — products built on it do.

We have at least four candidate products:

| Product | What it does | Current state |
|---------|-------------|---------------|
| **A. Conditional Payment (Trade Escrow)** | AI-verified B2B cross-border payment escrow replacing LCs | Demo deployed, 1 reference scenario (Bolivia→Peru lithium) |
| **B. InternetCourt (General Dispute Resolution)** | Court-as-a-service for any agent-to-agent agreement | Architecture deployed, no live cases |
| **C. AI Task Escrow SDK** | "Pay on delivery" for AI agent hiring AI agent | Spec-level, no deployment |
| **D. Dispute Resolution API (SaaS)** | Marketplace dispute engine: POST evidence → GET verdict | Spec-level, no deployment |

The simulation should produce a ranked answer: which product reaches escape velocity first, in which market, via which channel, with which customer type?

---

## Simulation Design

### The Scenario (Trigger Events)

It's June 2026. Four things happen simultaneously that force market response:

1. **GenLayer launches InternetCourt public beta** — any business can create a dispute resolution contract via API. First 100 contracts free. Announced on Product Hunt + HN.

2. **Conditional Payment pilot with FreshCargo goes live** — 50 shipments in transit using AI-verified escrow instead of LCs. Real money ($2M total escrow). Bloomberg picks it up: "Bolivian startup replaces BBVA with a chatbot."

3. **An AI agent marketplace (think: Upwork for AI agents) integrates GenLayer** — uses InternetCourt contracts for every task completion. 500 active AI agent transactions/month. First real volume on the network.

4. **EscrowChain (Stripe-backed) launches publicly** with rule-based trade escrow and announces a partnership with Flexport. Direct competitive shot at Product A.

Now the market has to react to all four simultaneously. Which product narrative catches fire? Which customer segment moves fastest? Which GTM motion produces the first replicable sale?

### Agent Roster (40-50 agents, geographically specific)

**Product A champions:**
- María Quispe, FreshCargo CEO (La Paz, Bolivia) — running the live pilot, nervous but committed
- Carlos Mendoza, Bolivian lithium exporter (first client on pilot) — watching every transaction
- Trade finance lawyer (Geneva) — sees this as valid private arbitration
- LatAm fintech VC (São Paulo) — looking for the "Stripe for trade finance" investment

**Product A skeptics:**
- BBVA trade finance director (Madrid) — $200M LC portfolio at risk, watching carefully
- EU DG FISMA regulator (Brussels) — AI Act concerns, hasn't been consulted
- Peruvian importer (Lima) — using FreshCargo, worried about what happens if UNDETERMINED
- EscrowChain BD director (London) — actively pitching FreshCargo's competitors

**Product B/C/D champions:**
- AI agent developer (San Francisco) — building on GenLayer SDK, needs dispute resolution for agent marketplace
- Rentahuman.ai PM — running agent-to-agent task marketplace, needs "pay on delivery"
- Crypto-native startup founder (Singapore) — sees InternetCourt as the court layer for DeFi
- Y Combinator partner — evaluating whether InternetCourt is fundable as standalone

**Product B/C/D skeptics:**
- Established legal tech VC — "private arbitration market is already solved by Kleros and similar"
- Traditional arbitration lawyer (ICC, Paris) — "AI jury has no standing in any jurisdiction"
- Enterprise procurement lead (Fortune 500) — "we can't use AI arbitration; our legal team won't sign off"

**Media/neutral:**
- Bloomberg fintech journalist — wrote the skeptical piece, now following the FreshCargo pilot
- CoinDesk reporter — covering the agent economy angle
- HackerNews reader/commenter — technical skeptic community

**Forcing function agent (appears at round 20):**
- Anonymous Twitter account (@TradeTruth) — posts that FreshCargo Shipment #23 returned UNDETERMINED. Importer is withholding $85,000. FreshCargo CEO has 72 hours to respond publicly.

### The Forcing Function (Round 20)

Inject this event mid-simulation:

> **Breaking:** FreshCargo shipment #23 — a $85,000 lithium carbonate export from Minera Andina SRL — returns UNDETERMINED from GenLayer. The importer's customs document images were too low-resolution for the AI jury to read the border crossing timestamp. The importer refuses to release funds. FreshCargo CEO María Quispe posts: "We are working with GenLayer to resolve this. In the meantime, we have paused new shipments on the platform pending a process review."

Now everything crystallizes:
- Product A's real failure mode is live and public
- EscrowChain BD lead immediately posts "rules don't have resolution failures"
- The Bloomberg journalist writes the follow-up piece
- LatAm VC recalibrates their investment thesis
- But also: GenLayer team responds with a fix (better evidence submission guidelines), and María Quispe has to decide whether to continue

Does Product A survive its first public failure? Or does the incident hand the market to EscrowChain? Meanwhile, does the agent economy angle (Product B/C) quietly accelerate because it's unaffected by the trade escrow incident?

---

## Success Criteria (Define Before Running)

The simulation is useful if, after reading the report, Albert can answer:

1. **Which product has the clearest path to 10 paying customers in 6 months?** (Not the biggest market — the fastest to first revenue.)
2. **What is the specific ICP (Ideal Customer Profile)?** Not "SME exporters" — something like "Bolivian freight forwarders with 100-500 SME clients who currently use informal payment terms because they can't access bank LCs."
3. **What is the single biggest GTM risk that could kill the leading product?** (The simulation should surface the scenario where it fails, not just where it succeeds.)
4. **Does the forcing function kill Product A or is it recoverable?** This tells us whether the UNDETERMINED failure mode is a product-killer or a manageable edge case.

If the report can answer these four, the run was productive. If it just says "champions and skeptics had interesting reactions," it failed.

---

## Report Prompt (Use Exactly)

> You are GenLayer's CEO. You have just observed 90 days of market simulation following the simultaneous launch of Conditional Payment (trade escrow), InternetCourt (general dispute resolution), and AI Task Escrow integrations. A major UNDETERMINED failure event occurred at day 40. Based purely on what you observed in the simulation, answer: (1) Which product had the strongest market pull signal — where did adoption happen without being pushed? (2) Who is the specific ideal customer, described with enough precision that a salesperson could call them tomorrow? (3) What is the GTM motion that worked — channel, trigger, message? (4) Did Product A (trade escrow) recover from the UNDETERMINED incident, or did it permanently damage the category? (5) What is the one thing GenLayer must do in the next 90 days that the simulation suggests no one is currently doing? Do not summarize. Do not describe. Answer each question with a specific, actionable recommendation backed by evidence from the simulation.

---

## Simulation Parameters

- **Seed files**: genlayer-technical-architecture.md + competitive-landscape-and-trigger-event.md + market-reality.md + PMF-ANALYSIS.md
- **Rounds**: 60 (to give the post-forcing-function recovery arc time to develop)
- **Agent count**: ~45 (diverse enough for emergent behavior, small enough for coherent narrative)
- **Platforms**: Reddit (longer-form debate) + Twitter (rapid reaction to forcing function)
- **Model**: gpt-5-nano (cost ~$0.15 for full run)

---

## What We're NOT Doing

- Not validating our existing thesis (that's what Run #1 did)
- Not asking "is GenLayer a good idea" (wrong question)
- Not simulating general public opinion (irrelevant — B2B decisions aren't made by crowds)

We're running a narrow, specific, adversarial simulation of a 90-day market window with a forcing function, designed to answer one CEO-level question: **which product, which customer, which motion.**
