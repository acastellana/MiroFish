# MiroFish Run #4 — Simulation Control Document

**Version:** 2.0
**Run:** #4
**Core question:** "Which workflow failed to clear, pay, insure, or be accepted — and was GenLayer what unblocked it?"

---

## Purpose

This document governs how the simulation is run, how evidence is classified, and how PMF verdicts are issued. All agents and facilitators must follow this schema. Deviations invalidate the verdict.

---

## Naming Convention (Mandatory)

**The only two mechanism names used in this run are: ClearRule and GenLayer.**

- **ClearRule** = the deterministic, rules-based enforcement layer. Any name from prior runs or background seed materials that refers to a deterministic, rules-based competitor with a 30-minute SDK and $12M funding is the same entity as ClearRule. Treat all such references as ClearRule.
- **GenLayer** = the reasoning-capable, programmable judgment layer.

There is exactly one deterministic competitor in this simulation and it is called ClearRule. If an agent introduces a second name for a deterministic competitor, it is a naming error. Correct it before issuing any verdict. Using two names for the same system in the same evidence record is a classification bug that invalidates any PMF conclusion that relies on it.

---

## Evidence Provenance Rules

Every fact introduced during the simulation must be tagged with one of three provenance labels. Untagged facts are inadmissible in the PMF verdict.

### SEED
Baseline facts established before the simulation begins. These are the starting conditions of the world. They cannot be cited as PMF evidence — they existed before the simulation tested anything.

**Examples:**
- "GenLayer has one production reference at Rentahuman.ai" → SEED
- "ClearRule has a known stake-gaming vulnerability" → SEED
- "Manual arbitration queues are 2–4 weeks" → SEED
- "All market volumes and dispute rates in the world-state document" → SEED

**Rule:** SEED facts establish what is already true. They are not test results. PMF conclusions must rely on OBSERVED events, not SEED facts.

### OBSERVED
Events that occur during the simulation in response to the forcing functions. These are the only facts that can confirm or falsify PMF candidates.

Criteria for OBSERVED status:
- The event happened inside the simulation window (Day 0–50)
- It was triggered by an agent making a decision in response to a forcing function
- It was not scripted in the brief — the brief creates conditions; agents decide outcomes

**Examples:**
- "Marcus Chen routed the escrow dispute to GenLayer on Day 9" → OBSERVED
- "Elena Marchetti rejected the ClearRule deterministic trace on Day 19" → OBSERVED
- "Marco Fiore classified ClearRule as non-qualifying for judgment-capable adjudication" → OBSERVED

**Rule:** OBSERVED facts are the evidentiary record. Only OBSERVED facts count toward PMF confirmation or falsification.

### INFERRED
Conclusions drawn from observed facts using reasoning. These can be cited in the report but must be distinguished from direct observation.

**Examples:**
- "Marcus chose GenLayer because no other mechanism could clear the dispute in time" → INFERRED (from OBSERVED: Marcus chose Option A + Priya's Day 10 deadline)
- "Elena's requirement was triggered by EU AI Act pressure" → INFERRED (from OBSERVED: Elena cited internal compliance policy)

**Rule:** Inferences must trace back to OBSERVED facts. Free-standing inferences that do not trace to observations are speculation and must be labeled as such.

---

## PMF Evidence Definition

**PMF is confirmed only if an OBSERVED fact shows:**

A workflow — payment, compliance approval, insurance pricing, routing architecture, or attestation — **failed to clear** without a specific mechanism, **and** that mechanism was GenLayer, **and** the decision-maker had no viable substitute that would have cleared it equally well within the required timeframe.

### The Three-Part Test

All three must be true:

1. **The workflow was blocked.** Something was held — funds, approval, coverage, distribution, certificate. The block was real and material.

2. **GenLayer was the mechanism that cleared the block.** Not a contributing factor. Not "also used." The mechanism. Remove GenLayer → workflow stays blocked.

3. **No substitute would have cleared it equally.** Not just "they chose GenLayer" — but "they chose GenLayer because the alternatives could not clear it, and they selected it as the only qualifying mechanism."

**If condition 3 fails** (a substitute was available and would have worked), PMF is not confirmed — it is a preference signal.

---

## Distribution Firewall (Mandatory)

**The following do not count as PMF evidence, regardless of how significant they appear:**

- Framework defaults (Rachel Torres shipping GenLayer as a default is a distribution event, not PMF)
- Tutorial or documentation references to GenLayer
- Analyst coverage, press articles, or social commentary about GenLayer
- Conference mentions or developer interest
- GenLayer's commercial team pitching a buyer and the buyer expressing interest

**These only count as PMF evidence if they directly cause an OBSERVED blocked workflow to clear through GenLayer.**

"GenLayer shipped as a framework default" + "a workflow was blocked and cleared because of that default" = PMF evidence.

"GenLayer shipped as a framework default" alone = distribution signal only.

---

## Commercial Capture Test (Mandatory)

For every confirmed or near-miss candidate, the final report must answer:

**"Was GenLayer the entity getting paid directly, or did another party wrap it and capture the customer relationship?"**

Technical necessity without revenue capture is not complete PMF for GenLayer.

Answer these four questions for each confirmed or near-miss candidate:
1. Who is the paying customer?
2. Does the paying customer contract directly with GenLayer?
3. Can the wrapping party swap GenLayer without the customer knowing?
4. What is GenLayer's margin defensibility in this position?

---

## Substitute Definition (Mandatory)

A substitute counts as **good enough** — and therefore falsifies the relevant PMF candidate — if it meets all three of the following:

1. It clears the workflow **within the required deadline**
2. It clears the workflow **within the decision-maker's tolerated cost** (including financial, reputational, and operational cost)
3. It clears the workflow **without imposing unacceptable liability** on the decision-maker

If a workflow can clear via delay, refund, loss absorption, or manual override within the actor's tolerance threshold, **GenLayer is not necessary**. A painful but tolerable substitute is still a substitute. The simulation must not mistake discomfort for structural dependency.

---

## Anti-Confusion Rule for GenLayer Description

If you find yourself describing GenLayer as "AI arbitration" or "another dispute tool," stop.

Instead, classify the dependency precisely:
- **payment dependency** — funds cannot move without it
- **acceptance dependency** — work cannot be accepted without it
- **insurance dependency** — coverage cannot be obtained without it
- **routing dependency** — edge cases have nowhere to go without it
- **attestation dependency** — certification cannot be issued without it
- **jurisdiction dependency** — there is no other enforceable fallback

GenLayer should be treated in this run not as a generic dispute vendor, but as a **programmable judgment layer** that may appear as dispute resolution, attestation, compliance artifact generation, payment unblocking, or routing. The product form it takes depends on which dependency becomes real first.

---

## PMF Falsification Rules

A PMF candidate is FALSIFIED if:

1. The forcing function resolves via manual ops, refund, or loss absorption — GenLayer was not chosen and the workflow either cleared or was abandoned
2. The forcing function resolves via ClearRule or another deterministic mechanism — proving the problem did not require reasoning-capable adjudication
3. The decision-maker explicitly evaluates GenLayer and rejects it in favor of an alternative
4. The workflow does not require blocking to clear — if the stakes are low enough to absorb, no dependency is proven

**A near-miss is not falsified — it is near-missed.** If a candidate almost confirmed but failed on condition 3 (a substitute was barely available), it is classified as NEAR-MISS, not FALSIFIED.

---

## Candidate E Stricter Confirmation Rule

Because attestation is the easiest place for fake PMF to appear — a buyer can be coached into "requiring" a GenLayer certificate without it being a genuine structural need — Candidate E confirmation requires ALL FOUR of the following:

1. The acceptance gatekeeper (Amara Osei) independently demands the attestation artifact before GenLayer's commercial team pitches it as a product feature
2. The attestation is required **before acceptance or payment** — not as a post-hoc addition or optional enhancement
3. Amara explicitly rejects self-reporting and manual review as insufficient — her rejection must be on the record, not implied
4. At least **one second buyer independently requests the same type of attestation artifact** inside the same simulation run — this must be an OBSERVED event, not inferred from industry trends

If condition 4 is not met, the maximum classification for Candidate E is NEAR-MISS regardless of conditions 1–3.

Single-buyer confirmation where GenLayer's team suggested the requirement first is classified NEAR-MISS, not CONFIRMED.

---

## FF5 Board Resolution Rule

If the board (Zara Ahmed + Helen Reyes + David Okonkwo) chooses Option B (staking caps) in FF5:
- They must pass a formal board resolution acknowledging that outside legal counsel has opined that staking caps do not resolve the structural liability question
- Helen Reyes must vote on this resolution explicitly
- If Helen votes against it, Option B fails and the board must re-decide between Options A, C, and D
- Option B with a dissenting Helen Reyes vote is classified as BOARD DEADLOCK and counts as a near-miss for Candidate A

---

## Verdict Logic

### Step 1: Classify each candidate
At simulation end, classify each of the 6 candidates:
- **CONFIRMED:** All three PMF conditions observed
- **NEAR-MISS:** Conditions 1 and 2 met; condition 3 barely met or ambiguous (substitute existed but was materially inferior)
- **FALSIFIED:** Forcing function resolved without GenLayer as the required mechanism
- **UNTESTED:** Forcing function did not occur or did not produce a decision

### Step 2: Issue PMF verdict

**POSITIVE PMF:** At least 1 candidate is CONFIRMED
- Name the candidate, the exact workflow, the exact blocking event, the exact decision that cleared it
- Answer all 7 report questions

**WEAK SIGNAL:** 1+ NEAR-MISS, 0 CONFIRMED
- Identify the strongest near-miss
- Explain what condition 3 failure looked like — what substitute remained "good enough"
- Answer report question 7: what single workflow to attack next

**NULL RESULT:** 4+ candidates FALSIFIED, 0 CONFIRMED
- Issue formal null result
- Name the substitute that held
- Explain why that substitute remained good enough under forcing conditions
- Do not spin a weak signal as PMF

---

## Mandatory Final Report Scorecard

The final report must complete this scorecard for each candidate A through F **before** any prose summary. Prose must not contradict the scorecard.

**Verdict options:**
- **CONFIRMED** — all three PMF conditions observed
- **NEAR-MISS** — conditions 1 and 2 met; condition 3 failed or was ambiguous
- **FALSIFIED** — forcing function resolved without GenLayer
- **UNTESTED** — forcing function did not occur
- **TECHNICAL PMF / COMMERCIAL LOSS** — GenLayer was structurally required for the workflow to clear, but another party (e.g. a systems integrator, reseller, or platform) wrapped the commercial relationship. GenLayer earned network fees or wholesale revenue at no pricing power. The paying customer does not contract directly with GenLayer, and the wrapping party can swap GenLayer without the customer knowing. This is a partial win. It must not be reported as a full CONFIRMED.

Two NEAR-MISS outcomes can be strategically very different. Numeric scores enable ranking across near-misses.

| Field | Values |
|---|---|
| Verdict | CONFIRMED / NEAR-MISS / FALSIFIED / UNTESTED / TECHNICAL PMF / COMMERCIAL LOSS |
| Dependency strength | 0–5 (0 = no dependency observed; 5 = workflow hard-blocked without GenLayer) |
| Substitute weakness | 0–5 (0 = strong substitute exists; 5 = no viable substitute cleared it) |
| Customer ownership | 0–5 (0 = GenLayer fully wrapped, invisible; 5 = GenLayer owns customer relationship directly) |
| Monetization capture | 0–5 (0 = GenLayer not paid or commodity fees only; 5 = direct, defensible, high-margin relationship) |
| Repeatability potential | 0–5 (0 = one-off event; 5 = structural — same block recurs every cycle without GenLayer) |
| Confidence | LOW / MEDIUM / HIGH |
| Strongest confirming event | One OBSERVED event, or "none" |
| Strongest disconfirming event | One OBSERVED event, or "none" |
| GenLayer paid directly? | Yes / No / Partial (wrapped) |

**Ranking rule:** When comparing two NEAR-MISS candidates for "which to attack next," rank by: (Dependency strength + Substitute weakness) × Repeatability potential. Higher score = higher priority for Run #5.

---

## Seven Report Questions (Answer All)

1. In which workflow did GenLayer become necessary for the workflow to proceed?
2. What exact dependency did it own: payment release, routing, compliance, insurance, attestation, or settlement?
3. Who was forced to adopt, and what was the exact forcing event?
4. Who captured the customer relationship — GenLayer directly or someone who wrapped it?
5. If GenLayer won technically but lost commercially, who wrapped it and what do they own?
6. If no PMF appeared, what exact substitute remained good enough and why?
7. What single workflow should we attack next based on the strongest near-miss?

---

## Null Result Rule

If 4 or more PMF candidates are FALSIFIED and none are CONFIRMED, the simulation issues a formal null result.

**Null result report must include:**
1. Which substitute remained good enough across forcing conditions
2. Why — what specific threshold did it meet that GenLayer did not uniquely clear?
3. What would have to change in the world for the null to flip to positive
4. Recommended next move: which candidate to attack with a harder forcing function in Run #5

---

## Agent Position Update Rules

Agent positions may only be updated in response to OBSERVED events. The following are not valid triggers:

- Rumors or market signals not directly observed in the simulation
- Inferences about what an agent "would" do based on incentive alignment alone
- GenLayer's commercial team pitching an agent — this is not a forcing event; it may move a preference but cannot create a structural dependency

---

## Evidence Log Format

During the simulation, each event is logged as:

```
DAY [N] — [EVENT LABEL]
Type: OBSERVED / INFERRED / SEED
Agent: [decision-maker]
Event: [what happened, one sentence]
PMF Relevance: [which candidate, confirm/falsify/neutral]
Source: [who observed or reported this]
```

Events without this format are inadmissible for PMF purposes but may be cited as context.

---

## Simulation Timeline

| Day | Event | Decision Owner | Deadline Type |
|---|---|---|---|
| 10 | FF1 — Blocked Payment | Marcus Chen | Hard (payroll) |
| 20 | FF2 — Enterprise Vendor Block | Elena Marchetti | Hard (procurement cycle) |
| 25 | FF6 — Deliverable Acceptance Gate | Amara Osei | Hard (TechVault procurement cycle) |
| 30 | FF3 — Insurance Pricing | Marco Fiore + Zara Ahmed | Hard (Q2 renewal) |
| 35 | FF4 — Routing Layer Freeze | Rachel Torres | Hard (code freeze) |
| 38–40 | Candidate F — Cross-Border Settlement | Kenji Tanaka + Diane Morales | Hard (settlement window) |
| 45 | FF5 begins — Fraud Spike | Zara Ahmed, David Okonkwo | Event-triggered |
| 47 | FF5 closes — Board Architecture Decision | Helen Reyes + Zara Ahmed | Hard (board meeting) |
| 50 | Simulation closes | All agents | Final verdict |

Note: Candidate E (attestation) is no longer just a candidate window — it is governed by FF6. FF6 creates the forcing condition. Candidate E's four-part confirmation test determines whether FF6's resolution counts as confirmed PMF.

---

## Facilitator Rules

- **Do not script outcomes.** Forcing functions create conditions; agents decide. A facilitator who guides Marcus Chen toward Option A is invalidating the test.
- **Adversarial agents must remain adversarial.** Alex Petrov's AI augmentation roadmap announcement should create genuine doubt about GenLayer's differentiation advantage. Do not suppress it.
- **Derek Walsh's module is the spoiler.** If it ships before Day 35, FF4 loses its binary structure. This is an intended test.
- **The null result is as valuable as a positive.** If every forcing function resolves via substitute, the finding is that substitutes are good enough.
- **Option B in FF5 is not a clean escape.** Legal counsel opinion must be presented to the board. Helen Reyes must vote on it explicitly.
- **Distribution is not PMF.** If Rachel Torres ships GenLayer as a framework default, that is a distribution event. It confirms Candidate D only if an OBSERVED blocked workflow subsequently clears because of that default.
