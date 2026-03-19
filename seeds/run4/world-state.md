# MiroFish Run #4 — World State (January 2027)

**Status: SEED. These facts establish baseline world conditions. None may be cited as PMF evidence.**

**IMPORTANT: All market volumes, dispute rates, coverage bands, platform metrics, and adoption counts in this document are simulation seed assumptions, not real-world claims. They are set to create realistic forcing conditions, not to reflect verified external data.**

---

## Agent Marketplace Volumes by Segment

Total estimated GMV across AI agent marketplaces: **~$2.1B annualized** (January 2027 seed assumption). Growing ~18% QoQ (seed assumption). Dispute rate: 4–9% by volume, 2–4% by GMV (seed assumption — high-value disputes disproportionately concentrated in software delivery and data/analytics).

| Segment | Annualized GMV | Dispute Rate | Avg Dispute Value | Dominant Enforcement |
|---|---|---|---|---|
| 1. Software / code delivery | $480M | 8.4% | $12K | Manual + platform review |
| 2. Data / analytics | $310M | 6.1% | $28K | Manual arbitration |
| 3. Creative / content | $220M | 3.2% | $1.8K | Refund / no enforcement |
| 4. Research / analysis | $190M | 5.7% | $9K | Manual review |
| 5. Legal / compliance | $140M | 4.1% | $45K | Human arbitration (slow) |
| 6. Infrastructure / DevOps | $280M | 2.8% | $6K | SLA + deterministic rule |
| 7. Financial modeling | $160M | 7.3% | $38K | Manual + escalation |
| 8. Multimodal / agentic tasks | $220M | 9.1% | $15K | Ad hoc / platform discretion |
| 9. Cross-border / autonomous | $100M | 11.4% | $31K | No formal mechanism; loss absorption |

**Key observation (seed):** Segments 1, 2, 5, 7, and 9 have the highest dispute value and weakest enforcement. Segment 9 (cross-border autonomous) has the highest dispute rate and effectively no enforcement — parties absorb losses or accept chargebacks.

---

## Current Enforcement Mechanisms and Failure Rates

### Manual Arbitration (Industry Baseline)
- Coverage: ~60% of platforms offer some form (seed assumption)
- Queue time: 2–4 weeks typical; 6+ weeks at scale
- Failure modes: Adjudicator bias, inconsistency, inability to evaluate technical outputs, no audit trail
- Failure rate on subjective quality disputes: ~35% (buyer or seller escalates or abandons) — seed assumption
- Status: Accepted as sufficient for low-value disputes. Breaks down above $10K and on subjective work quality claims.

### Deterministic Rule Engines
- Coverage: Used by infrastructure/DevOps and SLA-based platforms
- Works: Binary conditions (uptime %, delivery timestamp, file checksum)
- Fails: Any subjective quality claim — "does this code meet the architectural spec?" returns "not applicable"
- ClearRule is the fictional leading example; its deterministic trace is exportable but carries no reasoning

### ClearRule (Staking-Based Adjudication — Fictional)
- Production references: 1 (TaskRail, infrastructure segment) — fictional reference
- Mechanism: Parties stake tokens; protocol applies weighted-stake resolution to pre-defined rule anchors
- Known vulnerability: Stake-gaming — large stake positions placed immediately before dispute filing skew outcomes
- Staking caps: Announced on roadmap; not yet shipped as of Day 0
- AI augmentation roadmap: Announced; no public timeline; not yet a functional capability
- Failure rate on ambiguous/subjective disputes: Returns "not applicable" — cannot process the dispute at all
- Dispute fraud exposure: High under coordinated attack (FF5 seed condition)

### Platform Discretion (Ad Hoc)
- The majority of edge cases are resolved by platform ops teams making judgment calls
- No audit trail, no consistency, no scalability
- Accepted as default in most Segment 3, 4, and 8 platforms

### GenLayer (AI Jury Adjudication)
- Production references: 1 (Rentahuman.ai, Segment 8) — real reference
- Mechanism: AI jury of validators evaluates both parties' evidence; produces reasoning artifact + verdict
- Observed behavioral effect at Rentahuman.ai: Dispute rate changed post-integration; directional signal but not independently measured or audited (SEED — not PMF evidence)
- Resolution time: ~90 seconds for standard disputes
- Gaming resistance: High — stake-weighting not used; jury is multi-model, reasoning-based
- **Current gaps (SEED — context only, not PMF falsification criteria):**
  - No managed API (integration requires async architecture + evidence formatting layer)
  - No SOC 2 certification (blocks most enterprise procurement without manual exception)
  - Evidence formatting burden: parties must structure submissions in GenLayer's schema
  - Reasoning artifact format not yet standardized across buyers
  - Async complexity: integration takes 2–6 weeks for a competent engineering team

---

## Insurance Market State (AI Liability)

AI liability insurance is a nascent, high-margin, low-competition market as of January 2027 (seed assumption).

- **Active carriers:** 4 globally (Nexus AI Risk, CoverAI, Helios Underwriters, Marsh AI Solutions) — all fictional simulation actors
- **Premium range:** $80K–$500K/year for marketplaces; highly variable based on GMV, dispute volume, enforcement mechanism — seed assumption
- **Standard coverage limits:** $250K–$2M per event; most carriers will not quote above $500K/event for platforms with no structured adjudication — seed assumption
- **Known pricing factors:** GMV, dispute rate, enforcement mechanism quality, manual fallback availability
- **Adjudication mechanism pricing:** No industry standard. Each carrier uses proprietary criteria. Nexus AI Risk is the first to explicitly price "judgment-capable adjudication" as a risk reduction factor.
- **Market gap:** No carrier has published a standard for what constitutes a "verifiable adjudication mechanism" — this is the gap that FF3 exploits.

---

## Regulatory Pressure

### EU AI Act (Accurate framing as of the simulation's world-state)
- High-risk AI systems face transparency, documentation, and human oversight requirements
- AI agent marketplaces operating in high-risk segments face scrutiny on how disputes involving AI outputs are resolved
- No specific mandate for an adjudication mechanism exists in the Act as of January 2027 (seed)
- Enterprise procurement functions are interpreting compliance obligations broadly — they want documented adjudication trails even where not explicitly required
- Practical effect: Procurement leads like Elena Marchetti are creating internal requirements that exceed what is explicitly mandated

### Cross-Border / Jurisdictional Vacuum
- Agent-to-agent transactions across jurisdictions have no enforceable dispute resolution mechanism
- Arbitration clauses in smart contracts are unenforceable in most jurisdictions when both parties are autonomous agents
- This is the structural condition for Candidate F (Synthetic Jurisdiction)

---

## ClearRule State (Day 0) — Fictional Actor

- **Production deployments:** 1 confirmed (TaskRail — fictional)
- **Roadmap (announced, not shipped):** Staking caps v1; AI augmentation layer (Q3 2027 target, outside simulation window)
- **Commercial traction:** $300K integration deal offered to LangGraph; active sales to 4 other platforms — all fictional in-world context
- **Known vulnerabilities:** Stake-gaming (exploited in FF5 seed condition)
- **Defensive posture:** ClearRule CEO Alex Petrov is aware of GenLayer's advantage on ambiguous cases; AI augmentation roadmap announcement is a counter-move

---

## GenLayer State (Day 0) — Real Product

- **Production deployments:** 1 confirmed (Rentahuman.ai, Segment 8) — real
- **Observed effect:** Dispute rate change at Rentahuman.ai post-integration — directional positive, not independently audited
- **Resolution time:** 90 seconds median on standard disputes
- **Gaming resistance:** Demonstrated; no stake-weighting in jury mechanism
- **Current gaps (SEED — context only):**
  - No managed API
  - No SOC 2
  - Evidence formatting burden
  - Reasoning artifact format not standardized
  - Integration timeline: 2–6 weeks

---

## Key Frictions That Shape Forcing Functions

These frictions are SEED conditions. They create the forcing pressure but do not constitute PMF findings.

1. **No managed API:** Every GenLayer integration is a custom project. This slows FF2 (DataForge has 20 days) and raises the bar for FF5 (DevSwarm migration is 60 days).
2. **No SOC 2:** Elena Marchetti's pharma company will require security documentation. GenLayer cannot currently provide this. This is the key risk in FF2.
3. **Async complexity:** GenLayer's 90-second resolution requires async architecture. Platforms built on synchronous request-response need refactoring.
4. **Evidence formatting burden:** Parties must submit structured evidence. In contested disputes, the weaker party may not format correctly.
5. **Reasoning artifact format:** Not standardized. A buyer asking for a "GenLayer attestation certificate" will receive output that requires interpretation — this affects FF2 and Candidate E.
6. **No independent measurement:** The Rentahuman.ai behavioral effect is observed but not audited. Skeptics can reject it; believers will use it.
