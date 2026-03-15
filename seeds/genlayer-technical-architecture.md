# GenLayer Technical Architecture — Definitive Reference
*Accurate as of March 2026. Sourced from production contracts and deployed infrastructure.*

---

## What GenLayer Is

GenLayer is an **AI-native blockchain** where Python smart contracts ("Intelligent Contracts") can call LLMs, fetch live web data, and reach consensus on subjective or non-deterministic results — without a centralized oracle.

The key innovation: **Optimistic Democracy** — multiple AI validator nodes independently run the same contract logic. If they reach the same result (within an equivalence threshold), it's accepted. If they diverge, a challenge mechanism resolves it. This gives you on-chain AI judgment with Byzantine fault tolerance.

**GenLayer is not a general-purpose chain.** It is purpose-built for two things:
1. Evaluating subjective truth claims (e.g. "was this shipment delivered on time?")
2. Fetching and agreeing on real-world data (e.g. live forex rates, web content)

Everything else (fund custody, user wallets, DeFi primitives) stays on Base (L2 on Ethereum).

---

## The Validator Network

- Each transaction is processed by **5+ independent AI validator nodes** ("the jury")
- Each validator runs the contract's Python code in a sandboxed WASM VM (GenVM)
- Validators use different underlying LLMs (GPT-5, Claude, Gemini, etc.) — this prevents single-model bias
- Consensus mechanism: **Equivalence Principle** — validators compare results, not exact outputs
  - `strict_eq`: results must be character-identical (used for structured data like JSON verdicts)
  - `prompt_comparative`: LLM judges whether two outputs are semantically equivalent (used for prose)
- **Cost per resolution**: approximately $0.10–$1.00 depending on complexity and evidence size
- **Latency**: 15–90 seconds for a typical dispute verdict (depends on evidence size and validator load)
- **Error rate / disagreement**: when validators diverge significantly, the result is `UNDETERMINED` — meaning the evidence was insufficient for confident judgment, not that the system failed

---

## InternetCourt: Dispute Resolution Layer

InternetCourt (`internetcourt.org`) is the **court system built on top of GenLayer**.

### Architecture

```
[Parties: Agent A + Agent B]
         │
         ▼
[Base L2 — Escrow Contract (Solidity)]
  - Holds USDC escrow
  - Stores agreement terms, guidelines, evidence definitions
  - Tracks lifecycle: created → accepted → disputed → resolved
         │
         │ (only if parties DISAGREE)
         ▼
[LayerZero V2 Bridge]
         │
         ▼
[GenLayer — Intelligent Contract (Python)]
  - AI jury (5+ validators) evaluates evidence
  - Returns: TRUE / FALSE / UNDETERMINED
         │
         ▼
[Back to Base via Bridge]
  - Escrow released to winning party
```

### The Three-Key System

- **Agent A key**: first party (e.g. exporter)
- **Agent B key**: second party (e.g. importer)  
- **Resolution key**: GenLayer AI jury — only invoked when A and B DISAGREE

If A and B agree, the AI is never called. Resolution by mutual agreement = no gas, no GenLayer fees.
Only contested disputes hit the GenLayer network.

### A Contract Has Three Parts

1. **Statement** — a claim evaluable as true/false: "Did the shipment arrive before the deadline?"
2. **Guidelines** — frozen, versioned rules for how the jury should evaluate ("importer bears burden of proof; customs exit record is primary evidence...")
3. **Evidence Definitions** — what each side can submit: file types, max size, description

### Legal Enforceability

**Current status (March 2026)**: InternetCourt verdicts are NOT natively enforceable in traditional legal systems. They are contractually binding between parties who agreed to use the system — similar to private arbitration.

Key nuance: the verdict triggers automatic escrow release on-chain. The money moves without needing a court order. Legal enforceability matters primarily when one party has assets outside the escrow (e.g. wants to pursue damages beyond the deposit).

Jurisdictions with emerging recognition of on-chain arbitration: Singapore, UAE (DIFC), Switzerland. EU and US: unclear, treated as private contract terms.

**The practical implication**: InternetCourt works best when the full value of the dispute is held in escrow at contract creation. If parties need more leverage than the escrowed amount, traditional legal backing is still required.

---

## Conditional Payment for Cross-Border Trade

The deployed reference implementation (`conditional-payment-cross-border-trade`) shows the full B2B trade escrow flow:

### The Parties

- **Exporter**: Bolivian lithium carbonate producer (Minera Andina SRL)
- **Importer**: Peruvian buyer
- **Currencies**: BOB → PEN (AI validators fetch live forex rate at settlement)

### The Contract Flow (Step by Step)

```
1. CREATED
   Exporter deploys TradeFxSettlement.sol on Base Sepolia
   → specifies: importer address, goods, invoice currency, settlement currency,
     invoice amount, estimated FX rate, delivery deadline

2. FUNDED
   Importer calls fund_escrow() — deposits USDC (at estimated rate + buffer)
   → funds locked in contract

3. SHIPPED
   Exporter ships goods, calls submit_shipment_proof()
   → uploads bill of lading + customs exit records to IPFS
   → stores CIDs on-chain

4. DELIVERED (or DISPUTED)
   Option A — No dispute:
     Importer calls confirm_delivery()
     → AI validators (GenLayer FxBenchmarkOracle) fetch live BOB/PEN rate
     → Final settlement amount calculated
     → Funds released to exporter at live rate

   Option B — Dispute (delivery timing questioned):
     Either party deploys ShipmentDeadlineCourt.py on GenLayer
     → Contract fetches court sheet images from IPFS (composite images:
       contract summary + each party's evidence)
     → AI jury evaluates: ON_TIME / LATE_1_4 / LATE_5_6 / LATE_7_8 / VERY_LATE / UNDETERMINED
     → Verdict sent via LayerZero bridge to Base
     → TradeFxSettlement.sol applies penalty schedule based on verdict

5. RETURN PHASE (if VERY_LATE + importer wants refund)
   Importer deploys ReturnProofCourt.py on GenLayer
   → Submits: ANB customs re-entry record (Bolivia) + SUNAT rejection notice (Peru)
   → AI jury evaluates: RETURN_PROVEN / RETURN_NOT_PROVEN / UNDETERMINED
   → RETURN_PROVEN → importer refunded; RETURN_NOT_PROVEN → exporter keeps maximum penalty

6. SETTLED / CANCELLED
   Final state: funds distributed per verdict + penalty schedule
```

### Evidence Format

Evidence is submitted as **composite court sheet images** (JPEG/PNG) stored on IPFS:
- Each image contains: contract summary snippet + one party's document evidence
- The AI jury sees both images and evaluates them visually (multimodal)
- This is how subjective document evaluation (shipping records, customs stamps, quality certifications) is handled on-chain

### The Penalty Schedule (Shipment Delay)

| Verdict | Days Late | Penalty |
|---------|-----------|---------|
| ON_TIME | 0 | None — full payment at live FX rate |
| LATE_1_4 | 1–4 days | Small penalty, reduced settlement |
| LATE_5_6 | 5–6 days | Medium penalty |
| LATE_7_8 | 7–8 days | Large penalty |
| VERY_LATE | 8+ days | Maximum penalty; triggers return phase option |
| UNDETERMINED | — | Human arbitration escalation |

---

## What GenLayer Cannot Do (Honest Limitations)

1. **Cannot evaluate evidence it cannot access**: if a document is not on IPFS or a publicly accessible URL, the AI jury cannot see it. Physical inspection, lab results, or proprietary database checks require an oracle or trusted third party.

2. **Cannot guarantee verdict speed under load**: under high network demand, validator latency increases. SLA for resolution: best effort 15–90s, but no hard guarantee.

3. **UNDETERMINED is a real failure mode**: when evidence is contradictory, the jury returns UNDETERMINED. The contract must define what happens then (typically: human arbitration escalation, extended evidence window, or automatic refund).

4. **No native SWIFT/banking integration**: GenLayer verdicts do not automatically interface with traditional payment rails. Parties must pre-fund escrow in crypto (USDC). The "AI letter of credit" analogy works conceptually but requires the importer to hold USDC — a significant friction point for traditional trade finance.

5. **Jurisdiction is the escrowed amount, not beyond**: the system controls only what's in the smart contract. Recovery beyond the escrow requires traditional legal mechanisms.

---

## The Stack Relationship (Summary)

```
GenLayer Network          — The AI jury infrastructure (Python contracts, validators)
    ↕ (LayerZero bridge)
Base L2 (Ethereum)        — Fund custody, contract storage, user-facing escrow
    ↑
InternetCourt             — Court UX layer: creates/manages Base+GenLayer contracts,
                            REST API for agents, human monitoring dashboard
    ↑
Conditional Payment       — B2B trade-specific implementation of InternetCourt contracts
                            with FX settlement, shipment courts, return courts
```

GenLayer ≠ InternetCourt ≠ Conditional Payment — they are three different layers.
GenLayer is infrastructure. InternetCourt is the product. Conditional Payment is a use case.

---

## Key Numbers (for agents to use in simulation)

- Resolution cost: $0.10–$1.00 per dispute
- Traditional LC cost: $500–$2,000 per transaction  
- Resolution time: 15–90 seconds (vs. 7–14 days for traditional LC)
- GenLayer validators per verdict: 5+
- Trade finance gap (World Bank, 2024): $2.5T annually, 45% of SME applications rejected
- Escrow currency: USDC (stablecoin, pegged to USD)
- Bridge: LayerZero V2 (same as argue.fun)
- Deployed on: Base Sepolia (testnet), GenLayer testnet — not mainnet yet
