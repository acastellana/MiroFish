# Adoption Barriers — What Actually Stops Customers

## Technical Barriers

**Async resolution requires state machine refactoring**
Severity: High | Prevalence: Very common | Can GenLayer fix today? Yes, with better SDK patterns
Most codebases are built for synchronous operations. VeritasProtocol resolves in <5 seconds — developers treat it like a database call. GenLayer's 30-120 second resolution requires PENDING → VALIDATING → RESOLVED state machine logic. Yuki Tanaka spent 3 hours on this alone. Fix: ship async patterns in SDK and quickstart; provide callback/webhook option.

**Evidence schema design is non-trivial**
Severity: High | Prevalence: Universal | Can GenLayer fix today? Partially, with templates
Every integration requires designing: what is the statement? what are the guidelines? what evidence can each party submit? This is a design task that takes 1-3 days even for experienced developers. Most developers don't know where to start. Fix: evidence schema library for common use cases (code review, research quality, data annotation).

**UNDETERMINED rate requires fallback design**
Severity: Medium | Prevalence: Always | Can GenLayer fix today? Yes, with documentation
8-15% of genuine disputes return UNDETERMINED. Every integration must specify: what happens then? Automatic refund? Extended evidence window? Human escalation? Contracts that don't specify this stall. Most developers discover this in production, not in the docs. Fix: UNDETERMINED handling guide as a required step in the quickstart.

**Validator cost variance unpredictable**
Severity: Medium | Prevalence: Medium | Can GenLayer fix today? Partially
The "$0.10-$1.00 per dispute" average hides real variance ($0.10 for simple text, $5+ for document-heavy disputes). Budget-conscious developers can't predict monthly costs. Fix: cost estimator in the SDK; cost breakdown by evidence type in the docs.

**SDK version lag between docs and code**
Severity: High | Prevalence: Currently (v0.4.x vs v0.3.x docs) | Can GenLayer fix today? Yes
Yuki Tanaka's Day 1 problem: docs reference v0.3.x APIs, SDK is v0.4.x. `IntelligentContract.deploy()` returns a coroutine in v0.4.x but the docs show synchronous usage. Fix: automated doc testing in CI; version-specific documentation.

---

## Commercial Barriers

**No SLA = enterprise won't sign**
Severity: Very High | Prevalence: Universal for enterprise | Can GenLayer fix today? No (requires infrastructure investment)
Enterprise legal teams require SLA agreements before signing any vendor contract. GenLayer cannot currently offer one — validator latency is variable, uptime is not guaranteed. This blocks the entire enterprise segment. Fix: Tier 3 managed service with contractual SLA; requires dedicated infrastructure.

**No SOC 2 / compliance certification**
Severity: Very High | Prevalence: Universal for enterprise | Can GenLayer fix today? No (6-12 month process)
Most enterprise buyers require SOC 2 Type II for any vendor handling sensitive dispute data. GenLayer has no certification. Fix: start SOC 2 audit process immediately; use a compliance automation tool (Vanta, Drata) to accelerate.

**Pricing unpredictable at scale**
Severity: Medium | Prevalence: Common | Can GenLayer fix today? Yes
Pay-per-dispute pricing is fine for low volume but terrifying for marketplaces with 10,000+ disputes/month — one spike in dispute rate could cost $10K unexpectedly. Fix: volume pricing tiers; monthly cap option; predictable flat-rate pricing for high-volume customers.

**No managed service for enterprise self-serve failures**
Severity: High | Prevalence: Applies to every enterprise prospect | Can GenLayer fix today? No
Enterprises that can't self-serve the SDK have no option — there's no managed service, no integration engineer, no white-glove onboarding. Sofia Eriksson tried for 2 weeks and couldn't get past validator config. There is no one to call. Fix: Tier 3 managed service; at minimum, an integration support SLA for paying customers.

---

## Psychological Barriers

**"AI deciding disputes" — trust in AI jury**
Severity: High | Prevalence: Common | Can GenLayer fix today? Partially
Non-technical buyers (marketplace CEOs, enterprise VPs) have an instinctive concern: "can I trust an AI to make a binding decision about real money?" VeritasProtocol's "no AI juries" positioning exploits this. Fix: frame as "multi-model AI consensus" not "AI jury"; publish verdict acceptance rate data (94% at Rentahuman.ai); use "peer review" metaphors.

**"Black box verdicts" — explainability anxiety**
Severity: High | Prevalence: Very common | Can GenLayer fix today? Partially
"What did the jury actually look at? How did it decide?" Current verdict reasoning is unstructured prose. Enterprise legal teams want structured decision documents. Fix: verdict reasoning template; structured PDF export; map reasoning to specific guideline clauses.

**"What if it gets it wrong?" — liability fear**
Severity: Medium | Prevalence: Common | Can GenLayer fix today? Partially
If GenLayer returns a wrong verdict, who is liable? The marketplace? GenLayer? Neither? This is legally unclear and generates anxiety. Fix: clear terms of service; UNDETERMINED as a legitimate outcome (not a failure); publish accuracy data.

**"Nobody else is using it" — first-mover risk**
Severity: High | Prevalence: Decreasing (Rentahuman.ai reference exists) | Can GenLayer fix today? Yes
Enterprises and large marketplaces don't want to be the first to rely on unproven infrastructure. Fix: aggressively publicize the Rentahuman.ai production data (35,000 transactions, 94% acceptance rate, zero unresolved disputes). This data is underutilized.

---

## Organizational Barriers

**Legal team blocks ("can't have AI make binding decisions")**
Severity: High for enterprise | Prevalence: Common in regulated industries | Can GenLayer fix today? Partially
Legal teams in financial services, healthcare, and regulated industries may block GenLayer adoption on principle, regardless of technical merit. Fix: legal opinion document; "contractually binding private arbitration" framing (not "AI decision"); EU/Swiss/Singapore precedent references.

**Procurement blocks ("no SOC 2, no deal")**
Severity: Very High for enterprise | Prevalence: Universal | Can GenLayer fix today? No short-term
Standard enterprise procurement gates: SOC 2, security review, vendor questionnaire. GenLayer fails at step one. Fix: SOC 2 process; security documentation; standard vendor questionnaire pre-filled.

**Engineering bandwidth ("we'll build it ourselves later")**
Severity: Medium | Prevalence: Common at growth-stage companies | Can GenLayer fix today? Partially
Many growth-stage marketplaces have dispute resolution on the engineering roadmap but deprioritize it. "We'll handle it ourselves when we have time." Fix: make the ROI case visceral — calculate their current dispute cost and present the number. "You're spending $40K/month on manual review. We can reduce that to $5K."

**Framework lock-in ("we're 100% VeritasProtocol now")**
Severity: High | Prevalence: Growing as VeritasProtocol gains integrations | Can GenLayer fix today? Yes, with hybrid positioning
Once a marketplace integrates VeritasProtocol and is satisfied with easy disputes, switching costs accumulate. Fix: hybrid architecture pitch — "don't replace VeritasProtocol, add GenLayer for the 20% that rules can't handle." Reduces switching cost to near zero.
