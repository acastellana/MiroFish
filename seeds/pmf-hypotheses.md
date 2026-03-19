# PMF Hypotheses — MiroFish Run #3
*Forcing harnesses, not market descriptions. Each hypothesis has a named test subject, a deadline, and a falsifiable binary outcome.*

---

## What PMF Means Here

PMF is not "a company paid us." It is self-reinforcing adoption: customers bring customers, usage expands without sales, switching costs accumulate. For infrastructure products, PMF signals are slower and harder to reverse.

The null result is valid. If none of the six hypotheses produce 2+ OBSERVED signals by Day 90, the verdict is NO PMF — and the report must say so.

---

## H1: Judgment-Heavy Dispute Resolution

**Primary test subject:** Marcus Chen (AgentHub CEO) — Day 18 forcing function  
**Secondary test subject:** Zara Ahmed (DevSwarm CEO) — contagion trigger

**Prior probability:** 35%

**What must happen for H1 to win:**
AgentHub's dispute profile is 11% rate, judgment-heavy. Marcus goes live on GenLayer. Within 30 days he reports that disputes VeritasProtocol would have auto-failed are being resolved correctly. He tells Zara Ahmed this. Zara acts on it.

**Confirming event (must be OBSERVED):**  
Marcus publicly states — unprompted — that "VeritasProtocol would have failed on our judgment-heavy disputes" and cites this as the reason he chose GenLayer. Bonus: Zara Ahmed cites Marcus's outcome, not GenLayer's pitch, as her deciding factor.

**Falsifying event (must be OBSERVED):**  
Marcus evaluates GenLayer, concludes "80% of our disputes are actually pass/fail," and chooses VeritasProtocol or renews human arbitration. The judgment-heavy framing doesn't hold for his actual dispute mix.

**Evidence deadline:** Day 48 (30 days post-FF2 decision)

**World conditions required for H1 to win:**  
Priya Nair must be willing to take Marcus's call and describe Rentahuman.ai's specific dispute profile before Day 18. Without that second reference, Marcus doesn't move.

**Null signal:** Marcus renews human arbitration (FF2 Option A). Neither automated solution crossed his threshold. H1 cannot be confirmed if the primary test subject doesn't adopt.

---

## H2: Enterprise Compliance + Auditability

**Primary test subject:** Sofia Eriksson (DataForge CEO) — Day 25 forcing function  
**Secondary test subject:** Nina Patel (CrewAI enterprise sales) — Day 35 forcing function

**Prior probability:** 20%

**What must happen for H2 to win:**  
Sofia's pharma client explicitly requires a verifiable audit trail for AI decisions. If GenLayer provides white-glove integration AND the pharma client accepts GenLayer's verdict reasoning as a compliance artifact — not just a settlement mechanism — H2 has its first evidence. Nina then includes that case as a reference in her Fortune 500 RFP.

**Confirming event (must be OBSERVED):**  
The pharma client's legal team accepts GenLayer's verdict reasoning export as sufficient audit documentation — and writes this into their vendor onboarding checklist. This must be stated by the pharma client, not by Sofia or GenLayer.

**Falsifying event (must be OBSERVED):**  
The pharma client's legal team explicitly rejects "AI reasoning" as insufficient audit documentation and states a preference for deterministic rule traces. GenLayer's verdict format is not enterprise-legal-ready.

**Evidence deadline:** Day 55 (30 days post-FF3 decision)

**World conditions required for H2 to win:**  
GenLayer must offer white-glove integration + compliance documentation within 72 hours of Day 25. Without that, Sofia chooses Option D (lose client) and H2 has no test case.

**Null signal:** Sofia loses the pharma client (FF3 Option D). H2 is not falsified — it's untested. But it removes the only enterprise compliance test case in the simulation.

---

## H3: Hybrid Fallback for Deterministic Systems

**Primary test subject:** Rachel Torres (LangGraph maintainer) — Day 35 forcing function  
**Secondary test subject:** Marcus Chen — could build a routing layer independently

**Prior probability:** 45%

**What must happen for H3 to win:**  
Rachel recommends a dual backend (FF1 Option C) and explicitly calls this "the right architecture" in her LangGraph 4.1 release notes or blog post. She routes easy disputes to VeritasProtocol and hard disputes to GenLayer. At least one other marketplace operator (Marcus, Zara) copies this routing structure within 60 days.

**Confirming event (must be OBSERVED):**  
Rachel publishes a dual recommendation and uses the phrase "routing layer" or "hybrid architecture" to describe it. A second operator independently builds or announces a similar routing structure, citing Rachel or their own reasoning — not GenLayer's pitch.

**Falsifying event (must be OBSERVED):**  
Rachel recommends a single backend (Option A or B exclusively) and explicitly states that dual recommendation creates "too much complexity for framework users." No routing layer emerges from any agent in the simulation.

**Evidence deadline:** Day 50 (15 days post-FF1 decision)

**World conditions required for H3 to win:**  
GenLayer must ship the managed API before Day 35 so Rachel's dual recommendation has a working GenLayer path. If the API isn't ready, a dual recommendation is distribution theater, not architecture.

**Null signal:** Rachel chooses Option D (no recommendation). Neither product met framework standards. H3 is blocked at the distribution layer before routing architecture can be tested.

---

## H4: API / Managed-Service Abstraction

**Primary test subject:** Sofia Eriksson (DataForge CEO) — Day 25 forcing function  
**Secondary test subject:** Carlos Reyes (cold inbound, non-technical buyer)

**Prior probability:** 30%

**What must happen for H4 to win:**  
Sofia cannot handle the SDK. If GenLayer offers white-glove integration (FF3 Option A or C), and Sofia goes live without her team ever touching a smart contract, H4 has its first evidence. The customer relationship is with "GenLayer dispute API" not "GenLayer blockchain."

**Confirming event (must be OBSERVED):**  
Sofia or a member of her team states explicitly that "we never had to deploy anything on-chain" or "we treated this as a REST API." A second buyer (Carlos Reyes or equivalent) signs a paying contract for dispute-resolution-as-a-service without deploying the SDK.

**Falsifying event (must be OBSERVED):**  
Sofia chooses VeritasProtocol (Option B) specifically because it has a simpler integration path, and states "GenLayer's managed service wasn't ready / wasn't easier than VeritasProtocol." The abstraction layer doesn't eliminate friction for non-technical buyers.

**Evidence deadline:** Day 55 (30 days post-FF3 decision)

**World conditions required for H4 to win:**  
The managed API must exist and be deployable by a dedicated engineer within 30 days (Sofia's pharma client deadline). If GenLayer cannot provide this, the hypothesis has no test case.

**Null signal:** Sofia loses the pharma client (FF3 Option D). The managed API wasn't ready in time. H4 is plausible but untested — and the simulation has no other non-technical buyer forcing function to fill the gap.

---

## H5: Behavior-Shaping Layer

**Primary test subject:** Marcus Chen (AgentHub CEO) — Day 48 (30 days post-adoption)  
**Secondary test subject:** Yuki Tanaka (developer/influencer) — Day 50 (30 days post-tutorial)

**Prior probability:** 40%

**What must happen for H5 to win:**  
Marcus goes live on GenLayer. His agents' dispute rate drops. He attributes the drop to behavioral change ("our sellers started documenting work differently") not dispute filtering. He reports this publicly. Yuki Tanaka publishes a tutorial that covers the behavioral effect with her own data. Developers cite both.

**Confirming event (must be OBSERVED):**  
A second marketplace operator (not Rentahuman.ai) publicly reports a measurable dispute rate reduction AND attributes it explicitly to behavioral change — not faster resolution. This must be stated by the operator unprompted.

**Falsifying event (must be OBSERVED):**  
Marcus goes live but reports no change in dispute frequency after 30 days. Or: Marcus reports faster resolution but no rate reduction. Rentahuman.ai's 40% drop is confirmed as idiosyncratic to their user base.

**Evidence deadline:** Day 55 (30 days post-FF2 adoption, if Marcus adopts)

**World conditions required for H5 to win:**  
Marcus must adopt (FF2 Option B or D) before Day 18. Without a second production customer by Day 25, there is no way to observe behavioral change by Day 55. H5 is dependent on H1 or H3 first producing an adopter.

**Null signal:** Marcus renews human arbitration AND Yuki's tutorial doesn't produce adoption data. Rentahuman.ai remains the only behavioral evidence. H5 is WEAK at best — one data point is SEED-level, not OBSERVED replication.

---

## H6: Synthetic Jurisdiction for High-Value Workflows

**Primary test subject:** Zara Ahmed (DevSwarm CEO) — high-value coding disputes  
**Secondary test subject:** Aisha Okonkwo (Klarna) — binding AI decisions in fintech

**Prior probability:** 15%

**What must happen for H6 to win:**  
A dispute above $10K is submitted to GenLayer. The losing party accepts the verdict without pursuing other recourse. Their acceptance is public and attributable. The key signal: the losing party had no other enforceable mechanism and pre-agreed to treat the AI jury as binding.

**Confirming event (must be OBSERVED):**  
A named agent (Zara Ahmed or Aisha Okonkwo) publicly states that they or their customer accepted a GenLayer verdict on a dispute above $10K — including the losing party — because they had pre-agreed and had no other recourse. The losing party's acceptance is explicit, not assumed.

**Falsifying event (must be OBSERVED):**  
A losing party on a high-value dispute explicitly rejects the GenLayer verdict and pursues a chargeback, legal action, or platform appeal. GenLayer verdicts don't hold when real money is at stake. Trust in the AI jury breaks under financial pressure.

**Evidence deadline:** Day 90 (requires high-value adoption to emerge organically)

**World conditions required for H6 to win:**  
Zara Ahmed must adopt GenLayer (triggered by Marcus Chen going live) before Day 40. Her platform handles high-value coding disputes — the most likely source of a $10K+ test case. Without Zara's adoption, H6 has no test subject in the simulation.

**Null signal:** No high-value dispute goes through GenLayer in 90 days. H6 is NOT OBSERVED — not falsified, but untestable. The market is too early for this hypothesis to be tested in a 90-day window.

---

## PMF Traps to Avoid

**Vanity adoption:** A customer integrates GenLayer but dispute volume is low. Looks like PMF. Is not. Track actual dispute volume processed, not integration announcements.

**Forced reference:** A customer agrees to be a reference but doesn't expand and won't renew at list price. Signal: "would you pay list price to renew?" — if no, it's a forced reference.

**Technical PMF without commercial PMF:** Developers love the SDK, write tutorials, build examples — but nobody pays. Distinguish between developer enthusiasm (tweets, stars) and commercial adoption (paying contracts, expanding usage).

**Channel PMF:** A framework (LangGraph, CrewAI) integrates GenLayer as default — but end users don't actually use the dispute feature. Framework integration = DISTRIBUTION SIGNAL, not PMF until end users are actively triggering disputes.

**Distribution mistaken for PMF:** Yuki Tanaka's tutorial, Rachel Torres's recommendation, Nina Patel's RFP — all of these are distribution events. PMF only if the downstream customers retained + changed behavior + paid.

---

## The Null Hypothesis

If none of H1–H6 produce 2+ OBSERVED signals by Day 90, the simulation output is: NO PMF in this wedge in this window. That is a valid and strategically important finding. Agents should begin discussing by Day 60: "is dispute resolution even the right first wedge?" Alternatives to surface:
- AI model evaluation / benchmark disputes
- Enterprise content moderation appeals
- Insurance claims with AI-generated evidence
- Legal discovery quality review

Do not suppress the null result. It has higher strategic value than a weak PMF verdict.
