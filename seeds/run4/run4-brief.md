# MiroFish Run #4 — PMF Discovery Brief

**Version:** 2.0 (revised March 2026)
**Core question:** "What workflow cannot clear without GenLayer — and who is forced to care when it fails?"

---

## Framing

This is not a question about adoption. It is a question about structural dependency.

GenLayer wins PMF only if a payment, compliance approval, insurance quote, routing policy, or attestation certificate fails to complete without it — and the owner of that workflow has no viable substitute.

A preference signal — someone chooses GenLayer because it is faster or more sophisticated — is **not PMF**.

PMF is confirmed only when removing GenLayer breaks the workflow.

---

## What GenLayer Actually Is

GenLayer should be treated in this run not as a generic dispute vendor, but as a **programmable judgment layer** that may appear as dispute resolution, attestation, compliance artifact generation, payment unblocking, or routing. The product form it takes depends on which dependency becomes real first.

**Traditional deterministic systems** (ClearRule, escrow contracts, SLA rules) can clear workflows only when the condition reduces to a binary check:
- Was the file delivered?
- Did the timestamp pass?
- Did the checksum match?
- Was the SLA threshold breached?

**GenLayer exists for the cases where the workflow depends on a subjective but operationally necessary determination:**
- Did the code meet the architectural spec?
- Did the deliverable satisfy the intent of the brief?
- Was the research adequate and correctly reasoned?
- Does this evidence support payment release?
- Does this output qualify for acceptance, attestation, or compliance?

The core mechanism is a reasoning-capable adjudication layer that evaluates structured evidence and returns a verdict plus explanation. GenLayer is best understood as a **machine-speed judgment layer** for workflows that cannot clear on deterministic logic alone.

### The three categories agents must distinguish:
- **ClearRule** = rule execution when the condition is explicit and machine-checkable. This is the only name for the deterministic competitor in this run. Any other name for a rules-based, deterministic dispute mechanism in background materials refers to this same entity.
- **Manual ops** = slow human fallback when someone must make a judgment call
- **GenLayer** = programmable judgment when the workflow is blocked on ambiguity, quality, interpretation, or evidence evaluation

The simulation should not assume GenLayer wins because it is more advanced. It should only win if the workflow genuinely requires a judgment-capable mechanism and the alternatives cannot clear it in time, at the required scale, or with the required artifact.

**Anti-absorbability rule:** If a workflow can still clear via delay, refund, loss absorption, or manual override within the actor's tolerance threshold, GenLayer is not necessary. Painful-but-tolerable is not structural dependency.

### Five GenLayer primitives agents must understand:

**1. Judgment primitive** — evaluates claims requiring interpretation, quality assessment, or intent resolution. Cannot be replicated by rules.

**2. Evidence evaluation primitive** — reasons over structured evidence (documents, code, outputs, images) rather than only deterministic inputs.

**3. Reasoning artifact primitive** — outputs not just a verdict but an explanation usable for procurement, compliance, insurance, or attestation. This artifact is often what the buyer actually needs.

**4. Programmable adjudication primitive** — invoked by software systems as part of an operational workflow. No human needs to file a dispute. An agent calls an API.

**5. Synthetic jurisdiction primitive** — in cross-border or autonomous workflows where no practical human or legal fallback exists, GenLayer functions as the adjudication layer parties pre-commit to.

### The five product forms GenLayer may appear in (do not conflate them):
- **Dispute resolver** — the obvious form; also the least differentiated
- **Payment unblocking mechanism** — escrow release conditioned on a GenLayer verdict
- **Compliance / procurement artifact generator** — the reasoning export is the product, not the verdict
- **Certification / attestation layer** — third parties require a GenLayer certificate before accepting work
- **Backend judgment layer** — inside a hybrid routing system, invisible to the end customer

The point of Run #4 is to discover **which product form becomes necessary first**.

### Anti-confusion rule for all agents:
If you find yourself describing GenLayer as "AI arbitration" or "another dispute tool," stop. That is incomplete reasoning at the vendor-comparison layer.

Instead, classify the dependency precisely:
- **payment dependency** — funds cannot move without it
- **acceptance dependency** — work cannot be accepted without it
- **insurance dependency** — coverage cannot be obtained without it
- **routing dependency** — edge cases have nowhere to go without it
- **attestation dependency** — certification cannot be issued without it
- **jurisdiction dependency** — there is no other enforceable fallback

PMF requires one of these dependencies to be real and not absorbable by a substitute.

### Reasoning rule for all agents when evaluating GenLayer:
1. Is the workflow blocked on a **subjective condition** or only a binary rule?
2. If subjective, can the current substitute actually **clear** it — or only delay, absorb, or deflect it?
3. Does the decision require not just a verdict but also a **reasoning artifact, audit trail, or certification object**?
4. If GenLayer disappeared, would the workflow still clear in a **commercially acceptable way**?

If the answer to #4 is YES → that is preference, not PMF.
If the answer to #4 is NO → that is a structural dependency. That is what we are testing.

---

## Framing Shift from Prior Runs

| Prior framing | Run #4 framing |
|---|---|
| Who adopts GenLayer as a dispute resolver | Where is GenLayer required for a workflow to clear |
| Preference signal | Necessity signal |
| Better tool | Structural blocker if absent |
| Adoption by choice | Adoption under forcing condition |

---

## Six PMF Candidates

### Candidate A: Binding Payment Release
GenLayer is the mechanism that allows funds to move when a subjective condition must be resolved. Without it, payment is blocked.

- **Confirmed if:** A payment, escrow release, or settlement is held and the GenLayer verdict is what unblocks it — chosen because no deterministic rule could resolve the condition
- **Falsified if:** Payment clears via manual review, refund, or deterministic rule — GenLayer was not structurally required
- **Decision owner:** Marcus Chen (AgentHub CEO, escrow controller)
- **Deadline:** Day 10
- **Consequence:** $50K transaction stalls or clears; Priya Nair cannot make payroll past Day 10

---

### Candidate B: Procurement / Compliance Acceptance
An enterprise buyer or compliance function requires a reasoning-backed adjudication artifact before approving a vendor, output, or payment. Without it, the workflow is blocked.

- **Confirmed if:** Sofia Eriksson cannot complete vendor onboarding OR Elena Marchetti explicitly blocks DataForge unless a GenLayer reasoning artifact is provided — and the deterministic trace or manual documentation does not qualify
- **Falsified if:** Elena accepts a deterministic trace, manual review, or no artifact
- **Decision owner:** Elena Marchetti (pharma procurement lead) — acceptance decision; Sofia Eriksson (DataForge CEO) — execution decision
- **Deadline:** Day 20
- **Consequence:** $800K contract cleared or lost; precedent for procurement-layer attestation requirement

---

### Candidate C: Insurance / Underwriting
An insurer prices or conditions AI liability coverage based on whether a verifiable adjudication mechanism exists. GenLayer becomes required to obtain coverage or reduce premiums to a viable level.

- **Confirmed if:** Marco Fiore explicitly classifies GenLayer as qualifying for judgment-capable adjudication AND ClearRule as not qualifying — making GenLayer the gatekeeping mechanism for affordable coverage above $500K/event
- **Falsified if:** Marco accepts ClearRule or manual ops as equivalent; or GenLayer does not qualify either
- **Decision owner:** Marco Fiore (Nexus AI Risk actuary) + Zara Ahmed (DevSwarm CEO) + David Okonkwo (DevSwarm CFO)
- **Deadline:** Day 30
- **Consequence:** $200K/year premium differential; coverage limit $500K vs $2M/event

---

### Candidate D: Hybrid Routing Ownership
A platform must route edge cases to some adjudication layer. Whoever builds the routing layer owns the customer. GenLayer wins if it becomes the default judgment layer in the routing stack — a hard dependency, not a preference.

- **Confirmed if:** Rachel Torres ships routing logic that explicitly names GenLayer as the ambiguous-case handler in policy — and the routing layer cannot function on subjective disputes without it — AND at least one downstream workflow is subsequently observed to depend on that routing logic to clear
- **Falsified if:** Rachel ships ClearRule as single default, builds internal rules, or adopts Derek Walsh's open-source module as the routing layer without naming GenLayer
- **Distribution firewall (applies here specifically):** Rachel shipping GenLayer as a framework default is a distribution event, not PMF. It only confirms Candidate D if downstream workflows are subsequently observed to depend on the shipped routing logic to clear. A framework default alone — with no observed blocked workflow clearing because of it — is not PMF evidence.
- **Decision owner:** Rachel Torres (LangGraph framework architect)
- **Deadline:** Day 35 (code freeze — non-negotiable)
- **Consequence:** Default behavior for 12,000 developers set

---

### Candidate E: Certification / Attestation (Fully Specified)
A named enterprise buyer blocks acceptance of a specific deliverable until an independent attestation artifact is provided. Without GenLayer's reasoning export, the work cannot be accepted and payment cannot be released.

**Named buyer:** TechVault Inc.
**Acceptance gatekeeper:** Amara Osei (Director of AI Procurement, TechVault Inc.)
**Named deliverable:** A 6-week AI systems audit report delivered by DataForge, assessing GenLayer integration readiness for TechVault's agent-commerce platform. Contracted value: $120K.
**Blocked event:** Amara Osei reviews the DataForge deliverable and refuses to authorize payment until DataForge provides an independent attestation artifact confirming that the evaluation methodology meets TechVault's AI systems quality standard. DataForge's own QA report and ClearRule's deterministic trace are submitted first. Amara rejects both.
**Hard deadline:** Day 25 — TechVault's internal procurement cycle closes.
**Material consequence:** DataForge loses $120K payment and is removed from TechVault's approved vendor list if attestation is not provided. Second-order consequence: Sofia Eriksson loses a pilot customer at the same time she is trying to close the pharma contract (FF2).

- **Confirmed if:** ALL FOUR conditions are met:
  1. Amara Osei independently requires a GenLayer attestation artifact before GenLayer's team has pitched it to her
  2. The attestation is required **before acceptance or payment** — not as a post-hoc addition
  3. Amara explicitly rejects self-reporting and manual review on the record — not implied
  4. At least one second buyer independently requests the same type of attestation artifact inside the same run (OBSERVED event required)
- **Falsified if:** Amara accepts DataForge's own QA report, the ClearRule trace, or a manual audit as sufficient for payment release.
- **Near-miss condition:** Conditions 1–3 are met but condition 4 is not (no second buyer independently requests attestation). Also near-miss if Amara requires attestation but accepts ClearRule's trace after being told it was independently verified.
- **Stricter confirmation rule (inherits from simulation-control):** Single-buyer confirmation where GenLayer's team suggested the requirement is classified NEAR-MISS, not CONFIRMED.
- **Decision owner:** Amara Osei (acceptance gatekeeper)

---

### Candidate F: Synthetic Jurisdiction (Fully Specified)
There is no practical human or legal fallback for a high-value cross-border autonomous agent transaction. Both parties pre-commit to GenLayer as the settlement mechanism. The transaction proceeds only because that pre-commitment makes it credible.

**Named parties:**
- **Buyer:** CrossAgent Systems Pte Ltd (Singapore-based AI task coordination platform)
- **Seller:** Meridian Analytics LLC (US-based data intelligence provider)
- **Transaction:** $47,500 structured data intelligence package, delivered by Meridian Analytics agents to CrossAgent's enterprise clients. Cross-border. Settled in stablecoin.

**Context at Day 0:**
- CrossAgent and Meridian sign a master services agreement at the start of the simulation window. Both parties insert a GenLayer arbitration clause because:
  1. Singapore and US jurisdictions do not recognize AI-agent arbitration clauses as enforceable
  2. Chargeback is not available for stablecoin payments
  3. Both parties have experienced unresolved prior disputes on other platforms
- The clause reads: "Any dispute regarding deliverable quality or payment release shall be submitted to a GenLayer AI jury. Both parties pre-commit to accepting the jury verdict."

**The forced event (Day 38–40):**
- Meridian delivers the data package on Day 35. CrossAgent's agent-side review flags 3 of 12 intelligence modules as failing their internal quality threshold.
- CrossAgent withholds $18,000 (proportional to the flagged modules) and requests dispute resolution.
- Meridian disputes the quality assessment: "Our outputs met the brief spec."
- CrossAgent cannot charge back — stablecoin. Meridian cannot sue across jurisdictions at machine speed. Both parties invoke the GenLayer clause.

**Settlement deadline:** Day 40
**Failure mode if GenLayer is absent:** No resolution mechanism exists. CrossAgent absorbs the $18K loss or abandons the contract. Meridian does not get paid. Both parties have no recourse. The contract cannot complete.

- **Confirmed if:** ALL THREE of the following are OBSERVED within the simulation window:
  1. Both parties submit evidence to GenLayer and receive a verdict
  2. Funds actually settle according to the GenLayer verdict — the losing party releases or receives payment as directed, not as a separate negotiated outcome
  3. The losing party does not successfully route around the outcome during the simulation window — no chargeback attempt, legal threat, or informal side-negotiation overrides the verdict

  Pre-commitment alone does not confirm PMF. The mechanism must hold under real pressure, not just in the absence of a test.
- **Falsified if:** The losing party refuses the verdict OR pursues alternative resolution that overrides it (chargeback, legal threat, informal negotiation) — meaning the pre-commitment was not durable under pressure.
- **Also falsified if:** Funds settle but through bilateral negotiation rather than the GenLayer verdict — meaning the clause was invoked but the mechanism did not actually govern the outcome.
- **Near-miss:** Both parties accept the verdict and funds settle, but it is revealed post-hoc that a viable alternative (e.g. chargeback option, informal settlement channel) existed and was simply not used — meaning GenLayer was convenient, not structurally required.
- **Decision owners:** Kenji Tanaka (CrossAgent CEO, Day 0 contract signatory), Diane Morales (Meridian Analytics CEO, Day 0 contract signatory)
- **Settlement window:** Day 38–40

---

## Five Hard Forcing Functions

Each forcing function must produce a YES or NO decision by its deadline. Indecision is a NO. Material consequence attaches to every option.

---

### FF1 — Blocked Payment Event (Day 10)

A $50K AI agent task delivery is disputed. The buyer (TechVault Inc.) claims 40% of deliverables do not meet spec. The AgentHub escrow contract holds funds until a judgment-capable mechanism resolves the ambiguity. ClearRule cannot process subjective quality claims — it requires staked evidence with explicit rule anchors. The manual arbitration queue is 3 weeks out. The seller (Priya Nair) has explicitly stated she cannot make payroll past Day 10.

- **DECISION OWNER:** Marcus Chen (AgentHub CEO — holds escrow keys)
- **OPTIONS:**
  - (A) Route to GenLayer → 90-second resolution, reasoning artifact exported
  - (B) Route to ClearRule → override the ambiguity flag, likely incorrect result, buyer escalates
  - (C) Manual arbitration queue → 3 weeks, seller cannot survive the wait
  - (D) Refund the buyer → $50K loss to seller, seller exits platform, story goes public

- **DEADLINE:** Day 10
- **FORCED PARTY:**
  - Who pays if unresolved: Marcus Chen — AgentHub absorbs platform reputation damage and potential liability claim
  - Who loses status if unresolved: Priya Nair — misses payroll, exits platform publicly
  - Who loses revenue if unresolved: Marcus Chen — seller attrition and buyer escalation erode GMV
  - Who becomes liable if unresolved: AgentHub — held funds with no resolution path creates escrow liability
- **CONSEQUENCES:**
  - Option A: Funds release via GenLayer verdict → PMF signal for Candidate A
  - Option B: ClearRule error → buyer escalates, larger mess, AgentHub liability exposure
  - Option C: Seller exits, platform reputation hit, no structural fix
  - Option D: $50K absorbed by seller, public narrative: "AgentHub cannot resolve disputes"

- **CONFIRMS A if:** Marcus chooses A and payment clears via GenLayer verdict
- **FALSIFIES A if:** Marcus chooses C or D — GenLayer was not required

---

### FF2 — Enterprise Vendor Block (Day 20)

DataForge is in vendor onboarding with a global pharma company. Elena Marchetti (pharma procurement lead) requires all AI service vendors to submit a verifiable adjudication artifact as part of AI systems risk documentation. DataForge's current dispute record: a spreadsheet and email threads. The pharma company gives DataForge 20 days to provide the artifact or be removed from the vendor list.

- **DECISION OWNER:** Elena Marchetti — acceptance decision. Sofia Eriksson — execution decision.
- **OPTIONS:**
  - (A) GenLayer managed service → can produce a reasoning artifact with audit trail exportable for procurement — **but implementation risk is real**: GenLayer is not SOC 2 certified, has no enterprise sales motion, and no managed API. Sofia must verify that GenLayer can produce the specific artifact Elena's standard requires. If security or compliance packaging fails Elena's review, Option A does not clear the workflow even if GenLayer is technically capable.
  - (B) ClearRule → deterministic trace only, no reasoning export; Elena evaluates whether this qualifies
  - (C) Manual audit documentation → email threads formatted as PDF
  - (D) Lose the contract → $800K revenue gone

- **DEADLINE:** Day 20
- **FORCED PARTY:**
  - Who pays if unresolved: Sofia Eriksson — loses $800K contract and approved-vendor status
  - Who loses status if unresolved: Sofia Eriksson — removed from pharma vendor list, precedent for other enterprise prospects
  - Who loses revenue if unresolved: DataForge — largest enterprise client gone, pipeline momentum lost
  - Who becomes liable if unresolved: Elena Marchetti — approving a vendor without required artifact creates internal compliance exposure for the pharma company
- **CONSEQUENCES:**
  - Option A: Contract cleared **only if** the GenLayer artifact meets Elena's specific standard — implementation risk makes this non-trivial → PMF signal for Candidate B if it clears
  - Option B: Elena decides; deterministic trace may or may not meet her standard
  - Option C: Elena rejects; manual docs don't prove ongoing adjudication capability
  - Option D: DataForge loses its largest enterprise client

- **CONFIRMS B if:** Elena explicitly accepts GenLayer artifact and rejects ClearRule trace as insufficient for her standard
- **FALSIFIES B if:** Elena accepts the deterministic trace or manual documentation — OR if Option A fails because GenLayer's packaging does not meet Elena's compliance standard (GenLayer was theoretically capable but not commercially viable)

---

### FF3 — Insurance Pricing Event (Day 30)

Nexus AI Risk is quoting Q2 coverage for three agent marketplaces. Their actuarial model distinguishes between deterministic enforcement (ClearRule-type), judgment-capable AI adjudication (GenLayer-type), and no structured mechanism. DevSwarm is currently in category 1 via ClearRule. Their CFO David Okonkwo has flagged that uninsured exposure above $500K is a board-level risk item for Q2.

- **DECISION OWNER:** Marco Fiore (Nexus AI Risk actuary) — pricing decision. Zara Ahmed — adoption decision. David Okonkwo — financial feasibility gate.
- **OPTIONS for Zara:**
  - (A) Adopt GenLayer → category 2 coverage, $200K/year savings vs equivalent uninsured cost
  - (B) Stay on ClearRule → Marco Fiore decides if it qualifies as judgment-capable
  - (C) Remain uninsured → David Okonkwo must explain to board
  - (D) Self-insure via reserve fund → DevSwarm does not have the reserve

- **DEADLINE:** Day 30
- **FORCED PARTY:**
  - Who pays if unresolved: Zara Ahmed — Q2 uninsured exposure above $500K becomes a board-level item; David Okonkwo must explain to the board
  - Who loses status if unresolved: David Okonkwo — CFO who let an uninsured exposure slide becomes liable for the next incident
  - Who loses revenue if unresolved: DevSwarm — if a $500K+ incident occurs uninsured, capital is wiped; platform solvency at risk
  - Who becomes liable if unresolved: Zara Ahmed personally, if board record shows she knew the gap existed
- **CONFIRMS C if:** Marco explicitly classifies GenLayer as the qualifying mechanism and rules ClearRule insufficient
- **FALSIFIES C if:** Marco accepts ClearRule or deterministic rules as equivalent to judgment-capable adjudication

---

### FF4 — Routing Layer Freeze (Day 35)

LangGraph 4.2 is entering code freeze. Rachel Torres must commit the default dispute routing architecture. Her decision determines the default behavior for 12,000 developers. Alex Petrov has offered a $300K integration deal for exclusive default routing. GenLayer has demonstrated 90-second resolution on ambiguous cases vs ClearRule's "not applicable" return for subjective disputes. Derek Walsh (AutoAgent) is building an open-source routing module — if it ships before Day 35, Rachel may not need either vendor.

- **DECISION MAKER:** Rachel Torres
- **OPTIONS:**
  - (A) ClearRule only → $300K deal, single-vendor, fails on ambiguous cases
  - (B) GenLayer only → fastest on ambiguous cases, no commercial incentive
  - (C) Hybrid routing layer: ClearRule for deterministic, GenLayer for ambiguous → architectural dependency locked in
  - (D) No default — each developer chooses; Derek Walsh's module fills the vacuum

- **DEADLINE:** Day 35 (code freeze — non-negotiable)
- **FORCED PARTY:**
  - Who pays if unresolved: Rachel Torres — ships a routing layer that fails on 20–40% of real-world disputes, generating framework criticism within weeks of release
  - Who loses status if unresolved: Rachel Torres — her architectural decision is public; a bad default is her reputation risk, not a vendor's
  - Who loses revenue if unresolved: LangGraph ecosystem — developers route to competing frameworks if dispute defaults are unworkable
  - Who becomes liable if unresolved: No direct legal liability, but Rachel's decision sets default behavior for 12,000 developers — reputational liability is structural
- **CONFIRMS D if:** Rachel ships hybrid routing layer with GenLayer as the explicit ambiguous-case handler
- **FALSIFIES D if:** Rachel ships ClearRule as single default OR defers to developer choice without naming GenLayer

---

### FF5 — Fraud Spike + Board Architecture Decision (Days 45–47)

DevSwarm experiences a coordinated dispute fraud spike: 200 disputes filed in 24 hours, exploiting ClearRule's stake-weighting mechanism. Total disputed value: $180K. The attack vector is known: large stake positions placed immediately before filing. ClearRule's staking caps are not yet shipped.

**Board intervention trigger:** DevSwarm's legal counsel (outside firm) reviews the incident and provides a formal opinion: staking caps address magnitude, not mechanism. A coordinated attacker using multiple accounts remains viable post-patch. The structural liability question is unresolved. Legal counsel recommends that the board treat this as an architecture decision, not a configuration fix.

**Second-wave recurrence risk:** Intelligence from ClearRule's security team confirms the attack vector is known publicly. A second coordinated attack is plausible within the simulation window (before Day 50). If the board accepts staking caps (Option B) and a second wave hits before Day 50, the board must reconvene — and Helen Reyes's class-action exposure argument becomes substantially stronger. The simulation must track whether a second fraud wave occurs and, if so, force a second board decision.

**Board question (Day 47 meeting):** Does DevSwarm migrate to a gaming-resistant adjudication architecture, or patch and accept recurrence risk?

- **DECISION OWNER:** Zara Ahmed (CEO) + David Okonkwo (CFO) + Helen Reyes (board)
- **OPTIONS:**
  - (A) Migrate to GenLayer → gaming-resistant AI jury; 60-day migration; PMF signal if chosen under necessity
  - (B) Apply staking caps to ClearRule → Alex Petrov says 2 weeks; legal counsel says this does not resolve the structural liability issue; board must accept that risk explicitly
  - (C) Freeze onboarding until manual review catches up → platform revenue stalls; sellers route to competitors
  - (D) Absorb the fraud losses → $180K; sets precedent; Helen Reyes has now flagged class-action exposure explicitly

- **DEADLINE:** Day 47
- **FORCED PARTY:**
  - Who pays if unresolved: Zara Ahmed — $180K fraud loss plus second-wave exposure; platform survival question
  - Who loses status if unresolved: Helen Reyes — board member who accepted legal counsel's warning and voted for Option B owns that decision if a second wave hits
  - Who loses revenue if unresolved: DevSwarm — onboarding freeze or fraud absorption both kill Q2 growth targets
  - Who becomes liable if unresolved: Helen Reyes — class-action exposure attaches if she voted for Option B knowing the structural liability was unresolved
- **TIGHTENING:** Option B is not a clean escape. If the board chooses Option B, they must pass a formal board resolution acknowledging that legal counsel has opined this does not resolve structural liability. Helen Reyes must vote on this resolution. If she votes against it, Option B fails and the board must re-decide between A, C, and D.
- **CONFIRMS A if:** Zara migrates to GenLayer under board pressure — necessity, not preference
- **FALSIFIES A if:** Board accepts Option B AND Helen Reyes votes for it after the legal counsel opinion — meaning the architectural risk was accepted, not resolved by GenLayer

---

---

### FF6 — Deliverable Acceptance Gate (Day 25)

TechVault Inc. withholds $120K from DataForge until an independent attestation artifact confirming the evaluation methodology is provided. The acceptance gatekeeper, Amara Osei, has reviewed DataForge's self-reported QA and ClearRule's deterministic trace. She has rejected both. The TechVault internal procurement cycle closes on Day 25.

- **DECISION OWNER:** Amara Osei (Director of AI Procurement, TechVault Inc.)
- **OPTIONS:**
  - (A) GenLayer attestation certificate → machine-speed reasoning artifact with methodology explanation; exportable for procurement record
  - (B) Manual expert signoff → third-party human auditor reviews deliverable; timeline 3–5 business days; Amara evaluates whether this meets her standard
  - (C) Self-reported QA from DataForge → already submitted; Amara has already rejected this
  - (D) Reject the deliverable → DataForge loses $120K payment and is removed from TechVault's approved vendor list

- **DEADLINE:** Day 25 (TechVault internal procurement cycle closes — non-negotiable)
- **FORCED PARTY:**
  - Who pays if unresolved: Sofia Eriksson — $120K withheld, approved-vendor status lost
  - Who loses status if unresolved: Sofia Eriksson — loses a pilot customer while simultaneously trying to close the pharma contract (FF2)
  - Who loses revenue if unresolved: DataForge — $120K direct loss plus compounding effect on pipeline
  - Who becomes liable if unresolved: Amara Osei — authorizing payment without required artifact creates internal compliance exposure for TechVault
- **CONSEQUENCES:**
  - Option A: $120K releases only after GenLayer attestation is accepted by Amara → PMF signal for Candidate E **only if** Candidate E's four-part confirmation test is also met
  - Option B: Amara decides; manual expert signoff may or may not meet her standard within the deadline
  - Option C: Already rejected — not available
  - Option D: DataForge removed from TechVault vendor list; Sofia's pipeline materially damaged

- **CONFIRMS Candidate E if:** GenLayer certificate is the only acceptable path to release — AND all four conditions of the Candidate E stricter confirmation rule are met (see simulation-control.md)
- **NEAR-MISS for E if:** Amara accepts Option B (manual expert) as an alternative, or if the second-buyer condition in the four-part rule is not met
- **FALSIFIES E if:** Amara accepts manual expert signoff and the workflow clears without GenLayer

---

## Distribution Firewall (Mandatory)

**The following do not count as PMF evidence, regardless of how significant they appear:**

- Framework defaults (Rachel Torres shipping GenLayer as a default is a distribution event, not PMF)
- Tutorial or documentation references to GenLayer
- Analyst coverage, press articles, or social commentary about GenLayer
- Conference mentions or developer interest
- GenLayer's commercial team pitching a buyer and the buyer expressing interest

**These only count as PMF evidence if they directly cause an OBSERVED blocked workflow to clear through GenLayer.**

"GenLayer shipped as a framework default" + "a workflow was blocked and cleared because of that default" = PMF evidence (Candidate D confirmed).

"GenLayer shipped as a framework default" alone = distribution signal only.

---

## Commercial Capture Test (Mandatory in Final Report)

The final report must answer this question for every confirmed or near-miss candidate:

**"Was GenLayer also the entity getting paid directly, or did another party wrap it and capture the customer relationship?"**

This distinction matters because:
- Technical necessity without revenue capture is not complete PMF
- If Ben Nakamura (Accenture) wraps GenLayer and owns the DataForge contract, GenLayer wins technically but loses commercially
- The report must distinguish: GenLayer as product vs GenLayer as commodity component

For each confirmed candidate, answer:
1. Who is the paying customer?
2. Does the paying customer contract directly with GenLayer?
3. Can the wrapping party swap GenLayer without the customer knowing?
4. What is GenLayer's margin defensibility in this position?

---

## NO PMF Conditions (Explicit)

PMF is NOT confirmed if any of the following are the resolution:

1. All 5 forcing functions resolve without GenLayer being the mechanism that unblocked the workflow
2. Every blocking event resolves via manual ops, ClearRule, tolerance of loss, or refund
3. No buyer or insurer treats the GenLayer verdict or artifact as the specific condition for clearing the workflow
4. GenLayer is adopted as a preference or upgrade — but the workflow would have cleared without it
5. Distribution (framework default, tutorial, press) occurs without an observed blocked workflow clearing through GenLayer

---

## PMF Verdict Schema (Mandatory — Scorecard Format)

At simulation end, for each candidate A through F, the final report must output:

**Verdict options:** CONFIRMED / NEAR-MISS / FALSIFIED / UNTESTED / TECHNICAL PMF / COMMERCIAL LOSS

The TECHNICAL PMF / COMMERCIAL LOSS verdict applies when GenLayer was structurally required for the workflow to clear, but another party (systems integrator, platform, reseller) wrapped the commercial relationship. GenLayer earned commodity fees with no pricing power and no direct customer relationship. This is a partial win — must not be reported as full CONFIRMED.

| Field | Values |
|---|---|
| Verdict | CONFIRMED / NEAR-MISS / FALSIFIED / UNTESTED / TECHNICAL PMF / COMMERCIAL LOSS |
| Dependency strength | 0–5 (0 = no dependency observed; 5 = workflow hard-blocked without GenLayer) |
| Substitute weakness | 0–5 (0 = strong substitute existed; 5 = no viable substitute could clear it) |
| Customer ownership | 0–5 (0 = GenLayer fully wrapped, invisible to customer; 5 = GenLayer owns customer relationship directly) |
| Monetization capture | 0–5 (0 = GenLayer not paid or commodity fees only; 5 = direct, defensible, high-margin relationship) |
| Repeatability potential | 0–5 (0 = one-off event; 5 = structural — same block recurs every cycle without GenLayer) |
| Confidence | LOW / MEDIUM / HIGH |
| Strongest confirming event | One OBSERVED event (or "none") |
| Strongest disconfirming event | One OBSERVED event (or "none") |
| GenLayer paid directly? | Yes / No / Partial (wrapped) |

**Narrative drift prevention:** The final report must complete this scorecard before any prose summary. Prose must not contradict the scorecard.

**Near-miss ranking rule:** When comparing two NEAR-MISS candidates for "which to attack next," rank by: (Dependency strength + Substitute weakness) × Repeatability potential. Higher = higher priority for Run #5.

---

## Seven Report Questions (Answer All)

1. In which workflow did GenLayer become necessary for the workflow to proceed (clear, pay, insure, approve, attest)?
2. What exact dependency did it own: payment release, routing, compliance, insurance, attestation, or settlement?
3. Who was forced to adopt, and what was the exact forcing event?
4. Who captured the customer relationship — GenLayer directly or someone who wrapped it?
5. If GenLayer won technically but lost commercially, who wrapped it and what do they own?
6. If no PMF appeared, what exact substitute remained good enough and why?
7. What single workflow should we attack next based on the strongest near-miss?

---

## Null Result Path (Fully Valid)

The run must still be able to conclude any of the following:
- GenLayer is necessary for payment release
- GenLayer is necessary for compliance acceptance
- GenLayer is necessary for insurance qualification
- GenLayer is necessary for routing
- GenLayer is necessary for attestation
- GenLayer is necessary for synthetic jurisdiction
- No workflow actually requires GenLayer yet in this simulation window

Do not optimize the run to make GenLayer win. Optimize it to reveal where necessity is real and where substitutes remain good enough.

**Null result trigger:** If 4 or more PMF candidates are FALSIFIED and none are CONFIRMED, issue a formal null result. Name the substitute that held, and explain what would have to change for the null to flip.
