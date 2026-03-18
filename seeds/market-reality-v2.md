# Market Reality — Agent Commerce Enforcement

> **Version:** v2 (rebuilt 2026-03-17)  
> **Purpose:** Verified fact base for MiroFish Run #4. Every claim is sourced or explicitly labeled.

---

## VERIFIED (sourced — cite URL for each fact)

### Agentic Commerce Is Already Happening at Scale

- **Google announced Agent Payments Protocol (AP2)** — an open protocol for agent-led payments, built as an extension of A2A (Agent2Agent) and MCP. 60+ organizations collaborating including Adyen, American Express, Mastercard, Visa, PayPal, Revolut, Salesforce, Coinbase, Etsy.  
  Source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol (Sept 2025)

- **Stripe launched Agentic Commerce Suite** — Stripe Payment Tokens (SPTs), cryptographically-signed mandates, built-in Radar fraud detection for agent transactions. Mastercard and Visa network tokens deployed in partnership with Stripe.  
  Source: https://stripe.com/blog/agentic-commerce-suite (Dec 2025), https://stripe.com/blog/supporting-additional-payment-methods-for-agentic-commerce

- **Visa introduced Trusted Agent Protocol** — ecosystem-led framework for AI commerce, addressing authorization, bot detection, and consumer visibility behind agents.  
  Source: https://investor.visa.com/news/news-details/2025/Visa-Introduces-Trusted-Agent-Protocol-An-Ecosystem-Led-Framework-for-AI-Commerce/default.aspx

- **Shopify launched Agentic Storefronts** (Winter '26 edition) — merchants list products once, Shopify syndicates to AI channels. Co-developed open standard with Google.  
  Source: https://www.shopify.com/news/winter-26-edition-agentic-storefronts, https://www.shopify.com/news/ai-commerce-at-scale

- **OpenAI + Stripe built Agentic Commerce Protocol (ACP)** — ChatGPT Instant Checkout live with Etsy, Shopify merchants coming.  
  Source: https://openai.com/index/buy-it-in-chatgpt/

### Agent Framework Maintainers (Real People / Companies)

- **LangGraph** — part of LangChain, founded by **Harrison Chase** (launched Oct 2022 while at Robust Intelligence). Chase is CEO of LangChain Inc.  
  Source: https://en.wikipedia.org/wiki/LangChain, https://blog.langchain.com/author/harrison/

- **CrewAI** — founded by **Joao Moura** and **Rob Bailey**.  
  Source: https://tracxn.com/d/companies/crewai/

- **AutoGen / AG2** — originally Microsoft Research project. Lead researcher: **Chi Wang** (ex-Microsoft Research, ex-Meta, founder of AutoGen/FLAML). Broader community maintainers include researchers from IBM, Meta, universities.  
  Source: https://github.com/sonichi, https://arxiv.org/abs/2308.08155

### Real Dispute Resolution Platforms

- **Kleros** — blockchain dispute resolution layer, live on Ethereum. Uses crowdsourced jurors incentivized via PNK tokens. Active at Northwestern Subtech conference 2024. Has Enterprise tier for companies.  
  Source: https://kleros.io/, https://blog.kleros.io/kleros-project-update-2024/

- **GenLayer / InternetCourt** — "AI-native trust layer and synthetic jurisdiction on-chain." AI validator nodes evaluate disputes; launched incentivized testnet Asimov. Partnered with io.net for compute.  
  Source: https://www.genlayer.com/, https://www.genlayer.com/news/genlayer-launches-incentivized-testnet-asimov-the-court-of-the-internet-activates

### No Published Enforcement-Layer Thesis Found

- **a16z** has published on agentic AI broadly (State of AI Dec 2025, Rise of Computer Use Dec 2025, crypto 2025 ideas) but **no specific thesis on agent-to-agent dispute/enforcement infrastructure** was found in public sources as of March 2026.

- **McKinsey, Sequoia** — no specific published thesis on agentic commerce enforcement layer found in search results as of this date.

---

## ASSUMPTIONS (labeled explicitly)

- ASSUMPTION: The volume of agent-initiated transactions will grow faster than existing chargeback/dispute infrastructure can adapt, creating a gap. (Plausible given pace of Stripe/Visa/AP2 launches, but no published market sizing found.)

- ASSUMPTION: Disputes in agent commerce will be materially different from human disputes — agents may not notice fraud or errors without explicit monitoring logic. (Directionally supported by AP2 design philosophy but not quantified.)

- ASSUMPTION: Incumbent rails (Stripe/Visa/Mastercard) will handle the majority of near-term agentic payment enforcement because they already have the merchant relationships and chargeback mechanisms. This is the key threat to any new dispute layer.

- ASSUMPTION: Kleros's juror incentive model may not scale to high-frequency, low-value agent transactions without design changes. (Structural concern, not confirmed by published Kleros data.)

- ASSUMPTION: GenLayer's approach of AI-as-validator is technically differentiated but faces adoption friction vs. established payment rails. (Inference from competitive landscape, not measured.)

---

## OPEN QUESTIONS

1. **Who is liable when an AI agent makes an unauthorized purchase?** — The EU AI Act does not answer this (AILD was withdrawn). No jurisdiction has clear law on agent transaction liability as of Q1 2026.

2. **Will the AP2 mandate chain (Intent Mandate → Cart Mandate) be sufficient for disputes, or will a separate arbitration layer emerge?**

3. **What happens to cross-border agent transactions when agents operate across jurisdictions?** — No framework addresses this yet.

4. **Can Kleros or GenLayer get integrated as the dispute backend for Stripe/AP2, or are they competitive dead-ends vs. incumbent rails?**

5. **How quickly will chargebacks for agent transactions become a systemic problem for card networks?** — UNKNOWN, no public data yet.

6. **Will OpenAI's Agentic Commerce Protocol become the de facto standard, locking out blockchain-based dispute layers?**
