# Buyer Economics — Who Pays and Why
*Unit economics and purchasing logic by segment*

## The Core Question

At what point does buying GenLayer (at $2-10/dispute for managed API, or $0.10-1.00 for SDK) become economically obvious compared to the current workaround?

The formula: **GenLayer makes sense when [cost of current workaround per dispute] > [GenLayer price per dispute] + [switching cost amortized over dispute volume]**

---

## Segment Analysis

### Indie Developer / Solo Agent Builder
- Monthly disputes: 5-50
- Average transaction value: $10-$200
- Current workaround: absorb the loss or argue manually (cost: $0 direct, but lost time and income)
- Cost of false positive: $10-200 (lost payment)
- Cost of false negative: $10-200 (wrongly refunded)
- Switching cost to GenLayer: 4 days (current SDK experience) → ideally 4 hours with better docs
- Payback period: immediate if dispute rate > 5/month and average value > $50
- Budget owner: self (personal credit card)
- Pricing sensitivity: very high — $2/dispute feels expensive at 20 disputes/month ($40/month)
- Deal size: $20-100/month
- **Who buys first:** solo devs with high-value contracts ($100+) and frequent disputes (10+/month). Yuki Tanaka profile.

### Early-Stage Marketplace (< $500K/month GMV)
- Monthly disputes: 50-500
- Average transaction value: $50-$500
- Current workaround: manual review team (1 person, $5K/month salary) or refund-always policy
- Cost of false positive: seller churn (high — small marketplaces depend on top sellers)
- Cost of false negative: buyer churn + refund cost
- Workaround cost per dispute: $10-100 (fully loaded)
- Switching cost: 2-week engineering sprint ($15-30K one-time)
- GenLayer SDK cost at 200 disputes/month: $20-200/month
- GenLayer managed API cost at 200 disputes/month: $400-2,000/month
- Payback period: SDK: immediate. API: 1-3 months depending on manual review cost.
- Budget owner: CTO or founder
- Pricing sensitivity: high — will choose SDK over API to save cost
- Deal size: $200-2,000/month
- **Who buys first:** marketplaces where manual review person is the bottleneck. Marcus Chen profile (AgentHub).

### Mid-Market Marketplace ($500K-$5M/month GMV)
- Monthly disputes: 500-5,000
- Average transaction value: $100-$2,000
- Current workaround: dedicated support team (3-5 people, $30-50K/month) + partial automation
- Cost of false positive: enterprise client churn ($10K-$100K annual contract at risk)
- Cost of false negative: top seller departure, reputation damage
- Workaround cost per dispute: $15-40 (fully loaded)
- Switching cost: 4-8 week engineering project ($50-100K one-time)
- GenLayer managed API cost at 2,000 disputes/month: $4,000-20,000/month
- Savings vs current: $10,000-60,000/month in manual review costs
- Payback period: 1-3 months
- Budget owner: Head of Product or CTO; CFO sign-off above $10K/month
- Pricing sensitivity: medium — will pay for the managed API if the ROI case is clear
- Deal size: $5,000-20,000/month
- **Who buys first:** marketplaces with a clear cost center (Zara Ahmed at DevSwarm spending $220K/month on manual resolution).

### Enterprise Internal AI Workflows
- Monthly disputes (internal): 50-500
- Average transaction value equivalent: $1,000-$50,000 (internal cost of wrong AI decision)
- Current workaround: legal/compliance team review ($100-500/dispute)
- Cost of false positive: compliance breach, regulatory risk
- Cost of false negative: incorrect vendor payment, audit failure
- Workaround cost per dispute: $150-500 (fully loaded legal review)
- Switching cost: enterprise procurement (SOC 2 required, SLA required, legal review) = 3-6 months
- GenLayer managed service: $10,000-50,000/month + per-dispute
- Savings vs current: significant if dispute volume is high
- Budget owner: VP Engineering, CLO, or board-level
- Pricing sensitivity: low — they care about compliance and auditability, not price per dispute
- Deal size: $50,000-500,000/year
- **Who buys first:** enterprises with explicit regulatory pressure (EU AI Directive) or an internal AI governance mandate. Sandra Lee at Shopify profile.

### B2B AI Service Procurement Platform
- Monthly disputes: 200-2,000
- Average transaction value: $500-$10,000
- Current workaround: procurement team manual review ($30-80/dispute)
- Cost of false positive: paying for undelivered service
- Cost of false negative: vendor churn, SLA penalty
- Workaround cost per dispute: $40-80 (fully loaded)
- Switching cost: API integration (2-4 weeks, $20-40K), plus evidence schema design
- GenLayer managed API cost at 1,000 disputes/month: $2,000-10,000/month
- Savings vs current: $30,000-70,000/month in manual review costs
- Payback period: immediate to 3 months
- Budget owner: Procurement / CFO office
- Pricing sensitivity: medium — procurement teams optimize for cost efficiency
- Deal size: $2,000-10,000/month
- **Who buys first:** platforms with a SaaS integration budget and high dispute volume.

---

## Unit Economics Summary

**At what dispute volume does managed API ($5/dispute avg) beat manual review?**

| Manual review cost/dispute | Break-even monthly disputes | Monthly savings at 1,000 disputes |
|---|---|---|
| $15 (minimal team) | 1,500 disputes | $10,000 |
| $25 (typical support team) | 600 disputes | $20,000 |
| $40 (specialist reviewer) | 300 disputes | $35,000 |
| $100 (legal/compliance) | 100 disputes | $95,000 |

**Key insight:** For marketplaces with specialist review ($40+/dispute), the break-even is only 300 disputes/month — achievable for any mid-market marketplace.

---

## Who Buys First: Ranked

1. **Mid-market marketplace with visible cost center** (Zara Ahmed/DevSwarm, Marcus Chen/AgentHub) — clear ROI, empowered buyer, 30-90 day sales cycle
2. **Early-stage marketplace where founder is the reviewer** — personal pain, fast decision, low contract value but zero CAC
3. **Enterprise with regulatory pressure** — slow cycle (3-6 months) but largest deal size
4. **B2B AI service procurement** — medium cycle, clear savings, but requires managed API (not yet built)
5. **Solo developer** — fast decision, but low ACV and SDK experience must improve first
