# Competitive Landscape — Agent Commerce Enforcement

> **Version:** v2 (rebuilt 2026-03-17)  
> **Purpose:** MiroFish Run #4 scenario setup. Fictional agents are explicitly labeled.

---

## VERIFIED — Real Players (with sources)

### Incumbent Rails — Moving Fast on Agentic Commerce

| Company | What they're doing | Source |
|---|---|---|
| **Stripe** | Agentic Commerce Suite: SPTs, signed mandate chain, Radar fraud detection, ACP with OpenAI | stripe.com/blog/agentic-commerce-suite |
| **Visa** | Trusted Agent Protocol for AI commerce authorization | investor.visa.com |
| **Mastercard** | Agentic network tokens, deployed via Stripe partnership | stripe.com/blog/supporting-additional-payment-methods |
| **Google** | Agent Payments Protocol (AP2), 60+ org coalition, extends A2A+MCP | cloud.google.com/blog/...ap2-protocol |
| **OpenAI** | Agentic Commerce Protocol (ACP) + Stripe; ChatGPT Instant Checkout live | openai.com/index/buy-it-in-chatgpt/ |
| **Shopify** | Agentic Storefronts; co-developed open standard with Google | shopify.com/news/winter-26-edition-agentic-storefronts |

**Key insight:** Incumbents are not waiting. They are defining the enforcement standard themselves, building it into existing payment rails. This is the primary competitive threat to any standalone dispute layer.

### Decentralized / Blockchain-Based Dispute Layers

| Company | What they do | Status | Source |
|---|---|---|---|
| **Kleros** | Crowdsourced blockchain dispute resolution, PNK token jurors, Ethereum | Live (mainnet), Enterprise tier | kleros.io |
| **GenLayer** | AI-validator consensus for disputes/contracts, synthetic jurisdiction, EVM-compatible | Incentivized testnet (Asimov) as of early 2025 | genlayer.com |

### Agent Framework Maintainers (Infrastructure Layer)

| Framework | Maintainer / Founder | Notes |
|---|---|---|
| **LangGraph / LangChain** | Harrison Chase (CEO, LangChain Inc.) | Oct 2022 launch; widely deployed |
| **CrewAI** | Joao Moura, Rob Bailey | Enterprise multi-agent platform |
| **AutoGen / AG2** | Chi Wang (ex-Microsoft Research) + community | Originally MSFT Research; now independent community fork |

---

## VERIFIED — Regulatory Reality

### EU AI Act (in force)
- The EU AI Act is in force. High-risk AI systems require risk management, record-keeping, human oversight, and incident reporting. General-purpose AI models with systemic risk have additional obligations.
- The Act governs **AI systems** but does **not** define dispute resolution requirements for autonomous agent transactions. No per-transaction mandate exists.
- Source: https://artificialintelligenceact.eu/high-level-summary/

### EU AI Liability Directive (AILD) — WITHDRAWN
- The European Commission **officially withdrew the AILD on 11 February 2025**, citing lack of stakeholder agreement and calls for regulatory simplification.
- The AILD **never contained** a €10,000 dispute threshold, never contained a dispute resolution mandate, and was never adopted into law.
- New AI liability rules are not expected until the AI Act is fully implemented (UNKNOWN timeline).
- Sources: https://www.ai-liability-directive.com/, https://iapp.org/news/a/european-commission-withdraws-ai-liability-directive-from-consideration, https://www.twobirds.com/en/insights/2025/proposed-eu-ai-liability-rules-withdrawn

### Regulatory Vacuum (Confirmed)
- No jurisdiction has clear law on liability for autonomous agent transactions as of Q1 2026.
- Existing product liability (EU Product Liability Directive) and consumer protection law was designed for humans and physical goods; application to AI agent transactions is legally unsettled.
- Source: https://www.jurisconsul.com/post/agentic-law-in-the-european-union-governing-autonomous-ai-agents

### "VeritasProtocol" — NOT a real agent dispute company
- Search results return:
  - **Veritas Protocol** (veritasprotocol.com) = Web3 smart contract security auditor, not a dispute resolution platform
  - **Veritus Agent** (veritusagent.ai) = AI debt collection agent, unrelated
  - **VERITAS OS** = GitHub auditable LLM decision infrastructure project
- **Conclusion: "VeritasProtocol" as an agent dispute resolution company is fictional. Do not use as a real company in scenario.**

---

## SCENARIO SETUP — FICTIONAL SCENARIO AGENTS

> ⚠️ ALL entries below are explicitly fictional. They are scenario constructs for simulation purposes only. None represent real companies, real people, or real events.

### FICTIONAL: Dispute Layer Startup
**FICTIONAL: "ArbitraNet"** — a fictional startup building AI-native dispute resolution as a service, targeting agent-to-agent commerce. Integrating with LangGraph and CrewAI as middleware. Seeking adoption from enterprises that distrust incumbent rail arbitration.
- *Why fictional:* No real company in this exact position has been verified. Kleros and GenLayer are real but are blockchain-native; ArbitraNet represents a "pure SaaS" middle path that may or may not exist.

### FICTIONAL: Enterprise Early Adopter
**FICTIONAL: "Meridian Logistics"** — a fictional mid-market logistics company that deploys CrewAI agents for procurement and is the first to face a $UNKNOWN disputed agent transaction that existing chargeback mechanisms fail to resolve.
- *Why useful:* Creates a realistic trigger event without inventing a real company's behavior.

### FICTIONAL: Regulatory Pressure Agent
**FICTIONAL: "Commissioner Andersen"** — a fictional EU official raising the question of agent transaction liability at a fictional European FinTech summit. Does NOT represent any real EU official or real event.
- *Why fictional:* The regulatory vacuum is real, but specific officials pushing agent-specific rules are not confirmed.

---

## Adversarial Scenario: Incumbents Win

**The scenario where GenLayer (and any standalone dispute layer) LOSES:**

1. Stripe expands Agentic Commerce Suite to include binding arbitration via existing card network rules.
2. Visa's Trusted Agent Protocol becomes the de facto trust standard; agents without a Visa credential cannot transact.
3. OpenAI's ACP becomes the default agent transaction protocol (OpenAI already has >500M user accounts).
4. Shopify/Stripe/Mastercard jointly define chargeback rules for agent transactions — no new court needed.
5. Blockchain-based dispute layers (Kleros, GenLayer) are relegated to crypto-native edge cases only.

**Probability: UNKNOWN.** The incumbents have a substantial head start in execution (all products launched 2025). The question is whether their enforcement coverage is sufficient for complex multi-agent disputes, or whether gaps emerge that require a neutral layer.
