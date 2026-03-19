# AI Agent Economy: Trust Infrastructure Landscape
*Seed document for MiroFish Run #3 — expanded from dispute resolution to trust infrastructure*

The dispute resolution framing is too narrow. The actual market is trust infrastructure — the layer that makes autonomous agent outputs credible, auditable, and contractually binding. Dispute resolution is one job to be done. There are at least six others, and GenLayer's primitives can address all of them.

---

## The Trust Infrastructure Problem

AI agents are increasingly autonomous — they negotiate contracts, complete tasks, hire other agents, and transact on behalf of humans. As transaction volume and value increase, the trust infrastructure required to make that commerce reliable becomes the critical bottleneck.

"Trust infrastructure" is broader than dispute resolution. It includes:
- Verifying that a task was actually completed to spec
- Interpreting what "completed to spec" means when the spec was ambiguous
- Arbitrating disagreements when verification fails
- Certifying quality for third parties (procurement, compliance, insurance)
- Generating audit logs for regulatory purposes
- Improving the quality of specs and contracts upstream (reducing disputes before they arise)
- Supporting procurement decisions for AI services

The agent economy needs all of these. GenLayer currently addresses dispute arbitration. The question is whether it expands to the adjacent jobs — and whether doing so creates more durable PMF than dispute resolution alone.

---

## Jobs-to-Be-Done Matrix

| Job | Who Needs It | Current Solution | GenLayer's Position |
|-----|-------------|-----------------|-------------------|
| Verify task completion | Marketplace operator, buyer | Human review, manual check | Can adjudicate via AI jury |
| Interpret ambiguous specs | Both parties in dispute | Human arbitrator, refund | Core GenLayer capability |
| Arbitrate disputes | Marketplace operator | Human arbiter, manual refund | Primary product |
| Certify quality | Enterprise buyer, compliance | Third-party auditor, human review | Possible via audit layer |
| Generate audit logs | Enterprise IT, compliance | Manual logging, internal tools | On-chain record of verdicts |
| Support procurement/compliance | Enterprise IT, legal, procurement | SLA contracts, manual oversight | Compliance integration pattern |
| Improve incentives upstream | Platform operators | Guidelines, training, penalties | Behavioral effect (emergent) |

The behavioral effect (upstream improvement) is the job-to-be-done that GenLayer delivers without explicitly trying to. It may be the most valuable.

---

## Agent Economy State (January 2027)

| Market Segment | Volume | Dispute Rate | Monthly Arbitration Cost | Notes |
|---------------|--------|-------------|------------------------|-------|
| AI coding agents | $2M/day | 11% | $220K (DevSwarm, manual) | Judgment-heavy, complex disputes |
| AI research/data agents | $400K/day | 9% | $60K (DataForge, human queue) | High value per dispute |
| AI creative/content agents | $180K/day | 6% | Minimal (goodwill only) | Subjective quality, no solution |
| General orchestration | $900K/day | 14% | $40K (AgentHub) | Mix of judgment + pass/fail |
| Enterprise agent fleets | $5M+/day | 3% | Internal legal | Low dispute rate, high stakes |
| Enterprise internal workflows | $3M+/day | 5% | IT ops + manual | Compliance-driven buyers |
| B2B AI service procurement | $1M+/day | 7% | Contract negotiations | SLA enforcement needed |

**Total estimated addressable dispute cost across visible market**: $400K–$600K/month in manual arbitration, scaling linearly with volume. GenLayer's cost to resolve the same volume: $10K–$50K/month. This is the economic forcing function.

---

## Why Existing Solutions Fail

| Requirement | Human Arbitration | Deterministic Escrow | Kleros | GenLayer |
|-------------|------------------|---------------------|--------|----------|
| API-native | ❌ | ✅ | ❌ | ✅ |
| Handles ambiguous specs | ✅ | ❌ | ✅ (slow) | ✅ |
| Sub-2-minute resolution | ❌ | ✅ | ❌ | ✅ |
| Cost under $5/dispute | ❌ | ✅ | ❌ | ✅ |
| Changes behavior upstream | ❌ | ❌ | ❌ | ✅ |
| Explainable reasoning | ✅ | ✅ | ✅ | ⚠️ (LLM output) |
| Enterprise compliance trail | ✅ | ⚠️ | ⚠️ | ⚠️ |

GenLayer's unique position: it is the only option that is API-native, judgment-capable, fast, cheap, AND generates behavioral improvement. The tradeoff is implementation complexity and explainability gaps.

---

## Product Configuration Options

GenLayer can reach customers in three distinct configurations, each with a different buyer profile:

### SDK (Developer-Led)
**What it is**: Python/npm package. Developer writes guidelines, deploys contracts, handles async resolution in their own codebase.

**Buyer profile**: Developer at a marketplace or agent framework. Technical decision-maker. Evaluates based on DX, docs, community, cost. Budget owner is CTO or engineering lead.

**Advantages**: Low cost of sale, high ecosystem leverage, viral if embedded in popular frameworks.

**Disadvantages**: Current onboarding friction (2-4 days minimum) is a serious barrier. Requires developer to understand GenLayer's architecture. Every implementation is slightly different; no standardization.

**PMF signal**: Framework adoption (LangGraph, CrewAI, AutoAgent integrations) — third-party, not GenLayer-driven.

---

### API (Abstracted Service)
**What it is**: REST API. POST a dispute with evidence, GET a verdict. No blockchain exposure. GenLayer handles all infrastructure.

**Buyer profile**: Product/engineering team at a marketplace or SaaS product. Technical but not blockchain-native. Evaluates based on reliability, latency, pricing, and documentation quality.

**Advantages**: Removes all crypto friction. Dramatically lowers integration time (hours vs. days). Reaches non-crypto buyers. Enables per-verdict pricing model.

**Disadvantages**: Requires GenLayer to operate as a reliable SaaS provider, not just a protocol. Infrastructure investment, SLA obligations, support burden.

**PMF signal**: Repeat API usage without founder involvement. Expansion to adjacent use cases. Willingness to pay per-verdict pricing.

---

### Managed Service / SaaS (No-Code Integration)
**What it is**: GenLayer provides dispute resolution as a fully managed service. Customer defines their use case; GenLayer configures the guidelines, evidence templates, and integration. Customer uses a dashboard or minimal API.

**Buyer profile**: Non-technical decision-maker. Enterprise IT, compliance, operations. Evaluates based on SLA, compliance documentation, vendor stability, price predictability.

**Advantages**: Opens enterprise market. Compliance documentation can be standardized. Predictable revenue.

**Disadvantages**: Highest cost of sale. Procurement cycles are long (3-6 months). Requires GenLayer to invest in enterprise sales, compliance documentation, SLA infrastructure.

**PMF signal**: Multi-year contract renewals. Expansion to multiple use cases within the same enterprise. Inclusion in procurement frameworks.

---

## Willingness-to-Pay Logic by Segment

| Segment | Current Monthly Arbitration Cost | GenLayer Estimated Cost | Willingness to Pay | Decision Trigger |
|---------|----------------------------------|------------------------|-------------------|-----------------|
| DevSwarm (coding marketplace) | $220K manual | $15K–$30K | High — $50K/month | Board pressure + competitor adoption |
| AgentHub (orchestration) | $40K manual | $5K–$10K | Medium — $20K/month | Arbitration contract renewal deadline |
| DataForge (research) | $60K manual | $8K–$15K | High — $30K/month | Enterprise client ultimatum |
| Enterprise IT (Shopify) | Internal (uncounted) | SaaS pricing | Low-medium | Compliance requirement + legal sign-off |
| B2B AI vendor | Variable | Per-dispute API | Medium | Reference customer + vendor SLA |
| Compliance team | External auditor costs | Managed service | Low until regulation | EU directive enforcement |

---

## Complements That Strengthen GenLayer's Position

Products that make GenLayer stickier and harder to replace:

- **Contract templates**: Pre-built dispute-ready contract templates for common agent commerce scenarios (coding task, research task, data annotation, content creation). Lowers implementation burden. Creates lock-in through familiarity.
- **Evidence schemas**: Standardized JSON schemas for common evidence types (code submission + test results, dataset + quality report, content + brief). Removes the evidence formatting burden. Speeds integration.
- **Dashboards**: Dispute rate monitoring, behavioral trend analysis, jury reasoning review. Turns GenLayer from a transaction processor into an operations tool. Budget owner shifts from engineering to operations.
- **Explainability exports**: Structured exports of jury reasoning for compliance reporting. Directly addresses the enterprise explainability concern. Opens the compliance buyer segment.
- **Use-case packs**: Pre-configured GenLayer deployments for specific verticals (AI coding marketplace, AI research marketplace, enterprise AI procurement). Reduces integration time from weeks to hours. Creates category positioning.

---

## The Open Question

The simulation should surface which combination of product configuration + buyer segment + complement produces the strongest PMF signal. The answer may not be the most obvious one. A hidden backend inside a popular framework might generate more durable pull than a direct enterprise sale. A behavior-shaping layer that reduces dispute rates might create more word-of-mouth than a dispute resolution product.

GenLayer's PMF is not certain. The substitutes are real. Manual arbitration is "good enough" for many operators today. The simulation should show where the substitute fails and GenLayer becomes structurally necessary — not just cheaper.

---

## Jobs to Be Done Matrix

| Job to Be Done | Current Solution | GenLayer Fit | VeritasProtocol Fit | Latency Tolerance | Value Density |
|---|---|---|---|---|---|
| Verify task completion | Manual review / hash check | High (judgment tasks) | High (pass/fail) | <5s acceptable | Medium |
| Interpret ambiguous specs | Human call / contract rewrite | Very high | None | 60-120s acceptable | High |
| Arbitrate disputes | Human arbitrator queue | Very high | Medium (rule-based only) | <5 min acceptable | High |
| Certify output quality | Manual QA / none | High | Low | 60-120s acceptable | Very high |
| Generate audit logs | Manual / application logs | High (signed verdicts) | Medium (deterministic trail) | Async OK | Medium |
| Support procurement compliance | Vendor docs / attestations | Medium (emerging) | Medium | Async OK | Medium |
| Improve upstream incentives (behavioral) | None | Very high | None | Async OK | Very high |

*Value density = willingness to pay per resolution event relative to volume.*

---

## Willingness to Pay Analysis by Segment

**AI Coding Marketplaces (e.g. DevSwarm, CodeNest)**
- Dispute frequency: 800-5,000/month
- Average transaction value: $50-$500
- Cost of false positive (wrongly ruled against seller): loss of $50-500 + seller churn
- Cost of false negative (wrongly ruled for seller): buyer churn + refund demand escalation
- Current workaround cost: $15-40/dispute equivalent (human review team salaries + overhead)
- Budget owner: CTO / Head of Product
- Acceptable latency: up to 5 minutes (disputes don't block immediate work)
- Explainability requirement: medium (sellers want to understand why they lost)
- Integration tolerance: medium (1-2 week engineering sprint acceptable)

**AI Research / Data Marketplaces (e.g. DataForge)**
- Dispute frequency: 200-800/month
- Average transaction value: $500-$15,000
- Cost of false positive: loss of high-value contract + enterprise client churn
- Cost of false negative: researcher gaming, quality degradation
- Current workaround cost: $50-150/dispute (specialist human reviewer)
- Budget owner: CTO / CEO
- Acceptable latency: up to 30 minutes
- Explainability requirement: high (enterprise clients demand reasoning)
- Integration tolerance: high (will invest 2-4 weeks if the pain is real)

**Enterprise Internal AI Workflows**
- Dispute frequency: 50-500/month (internal disagreements on AI output quality)
- Average transaction value: $1,000-$50,000 equivalent (internal cost of wrong decision)
- Cost of false positive: wrong process outcome, compliance risk
- Cost of false negative: incorrect vendor payment, audit failure
- Current workaround cost: $100-500/dispute (legal / compliance team review)
- Budget owner: Head of AI / VP Engineering / Legal
- Acceptable latency: up to 24 hours
- Explainability requirement: very high (audit trail is mandatory)
- Integration tolerance: low (enterprise procurement requires SOC 2, SLA, managed service)

**B2B AI Service Procurement**
- Dispute frequency: 100-1,000/month
- Average transaction value: $200-$5,000
- Cost of false positive: paying for undelivered service
- Cost of false negative: vendor churn, SLA penalty risk
- Current workaround cost: $30-80/dispute (procurement team + legal review)
- Budget owner: Procurement / CFO office
- Acceptable latency: up to 1 hour
- Explainability requirement: high (audit compliance)
- Integration tolerance: low (wants API, not SDK)

**Model Evaluation Platforms**
- Dispute frequency: 500-5,000/month (benchmark challenges)
- Average transaction value: $100-$2,000 per challenged result
- Cost of false positive: wrong model ranked, misleading leaderboard
- Cost of false negative: valid challenge dismissed, researcher credibility damaged
- Current workaround cost: $200-1,000/dispute (expert panel review, slow)
- Budget owner: Head of Research / CTO
- Acceptable latency: up to 30 minutes
- Explainability requirement: very high (scientific credibility)
- Integration tolerance: high (research teams can integrate)

**Compliance-Driven Enterprise**
- Dispute frequency: low (10-50/month) but each high stakes
- Average transaction value: $5,000-$500,000
- Cost of false positive: massive — regulatory fine, contract breach
- Cost of false negative: equal — paying for non-compliant service
- Current workaround cost: $1,000-10,000/dispute (legal review + compliance team)
- Budget owner: CLO / CCO / Board
- Acceptable latency: days (not a real-time requirement)
- Explainability requirement: mandatory (regulatory audit)
- Integration tolerance: very low (white-glove only; will not self-serve)

**Solo / Indie Agent Developers**
- Dispute frequency: 5-50/month
- Average transaction value: $10-$200
- Cost of false positive: painful but survivable
- Cost of false negative: loss of income, platform frustration
- Current workaround cost: $0 (absorb loss or argue manually)
- Budget owner: self
- Acceptable latency: up to 5 minutes
- Explainability requirement: low (just want the right answer)
- Integration tolerance: high (will read docs, try things)

---

## Product Tiers

**Tier 1: SDK (self-serve, developer-first)**
- Target: indie devs, early-stage marketplaces, framework integrations
- Onboarding: npm/pip install, working dispute in <1 week with good docs
- Pricing: pay-per-dispute ($0.10-$1.00 pass-through, GenLayer network cost)
- Friction: high setup (design work + engineering), high flexibility
- Current state: exists, rough edges (Yuki Tanaka's 4-day experience)
- Fix required: 30-minute quickstart, pre-built evidence schemas, async SDK patterns

**Tier 2: REST API (managed, no blockchain)**
- Target: mid-market marketplaces, SaaS platforms with existing engineering
- Onboarding: API key, standard POST/GET, no blockchain knowledge required
- Pricing: $2-10 per dispute (10-20x markup over network cost)
- Friction: low — same as any SaaS API
- Current state: spec only, ~6 weeks to build
- Unlock: removes the entire web3 friction barrier; probably 10x the addressable market

**Tier 3: Managed Service (enterprise, white-glove)**
- Target: enterprise, compliance-heavy, legal-risk-averse buyers
- Onboarding: dedicated integration engineer, custom evidence schemas, SLA agreement
- Pricing: monthly SaaS fee + per-dispute
- Friction: high procurement process, but GenLayer handles all technical onboarding
- Current state: does not exist; no SOC 2, no SLA, no enterprise sales motion
- Unlock: access to the highest-value segment (CLO/CCO buyers) and regulatory mandates

---

## Complements That Could Drive Adoption

These are products GenLayer could build or encourage third parties to build — each one removes a specific adoption barrier:

- **Contract templates with built-in GenLayer evidence schemas** — reduces design work from 1-3 days to 1-2 hours; turns "what should my guidelines say?" from a blank page into a checklist
- **Evidence schema library** — pre-built schemas for code review disputes, research quality disputes, creative fidelity, data annotation quality, API SLA verification; plug-and-play for common use cases
- **Explainability export** — structured PDF/JSON verdict document for enterprise legal teams; maps jury reasoning to guideline clauses; removes the "black box" objection
- **Dispute health dashboard** — marketplace operators can show enterprise buyers their dispute rate trend, resolution time, and verdict acceptance rate; turns GenLayer adoption into a sales asset
- **Use-case packs** — pre-configured GenLayer deployments for specific verticals ("AI Coding Agent Pack", "Research Quality Pack", "Data Annotation Pack"); reduces time-to-value from weeks to days
