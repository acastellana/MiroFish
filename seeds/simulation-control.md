# Simulation Control Document
*This file governs how the simulation generates evidence and what counts as PMF*

## Evidence Provenance Rules

Every claim about the market that appears in simulation output must be tagged:
- [SEED] = from seed documents; set before simulation started; CANNOT be PMF evidence unless it changed
- [OBSERVED] = something that happened during the simulation (an agent said it, did it, or responded to it)
- [INFERRED] = logical deduction from observed events

The final report cannot use [SEED] facts as proof that a hypothesis was confirmed.

## What Counts as PMF Evidence

COUNTS:
- An agent (not the GenLayer team) chose to use GenLayer without being asked [OBSERVED]
- An agent renewed or expanded usage without founder involvement [OBSERVED]
- An agent changed their workflow because of GenLayer [OBSERVED] — e.g., started writing different specs
- An agent paid list price without negotiation [OBSERVED]
- A third party built something on top of GenLayer without being asked [OBSERVED]

DOES NOT COUNT:
- GenLayer announced a partnership or pilot [SEED or DISTRIBUTION]
- An agent expressed interest or positive sentiment [SEED assumption or weak INFERRED]
- A framework integrated GenLayer as default [DISTRIBUTION — not PMF until end users use it]
- An analyst published a positive piece [DISTRIBUTION — not PMF]
- Dispute volume on GenLayer increased [DISTRIBUTION — PMF only if combined with repeat + paid + behavior-change]

## Verdict Logic

Step 1: Count OBSERVED PMF signals per hypothesis (not SEED, not INFERRED).
Step 2: For each hypothesis, identify at least one OBSERVED disconfirming signal.
Step 3: If no hypothesis has 2+ OBSERVED PMF signals → VERDICT: NO PMF
Step 4: If hybrid architecture emerged → answer routing/customer/pricing/replaceability before verdict
Step 5: If distribution events occurred without PMF signals → explicitly label them DISTRIBUTION ONLY

## The Binding Question

Before issuing any PMF verdict, the report must answer:

"Which specific agent treated the GenLayer verdict as binding enough to move money or change workflow — and did this happen without GenLayer team involvement?"

If the answer is "none" or "only with GenLayer involvement" → VERDICT: NO PMF

## The Hypothesis Ranking Rule

Even in a NO PMF scenario, the report must rank H1-H6 by evidence strength.
Ranking criteria: number of OBSERVED signals per hypothesis (not SEED assumptions).
H5 ranking is penalized if fewer than 2 independent customers observed behavioral change.
