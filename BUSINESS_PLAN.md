# GAUNTLET: Stress-Test Gym for Autonomous Energy Agents

> **"How do enterprises safely deploy autonomous agents in mission-critical energy infrastructure?"**

This is not an agent. Not a simulator. It's the **validation layer** that every energy company needs but cannot justify building in-house.

---
## THE PROBLEM
 
Energy companies are building autonomous agents faster than they can validate them:
- **Trading agents** that execute positions automatically
- **Forecasting agents** that predict solar/wind output
- **O&M agents** that optimize plant operations
But there's no standard way to answer: *"Is this agent safe to deploy?"*
 
Current validation:
- Manual simulation (6 to 12 months)
- Rule-based testing (misses edge cases)
- Hope-and-pray deployment (expensive failures)
**The gap:** Nobody has a stress-test framework that's fast, objective, and auditable.
 
---


---
 
## THE SOLUTION: GAUNTLET
 
A physics-based simulator that:
1. **Runs agents through 3 realistic bad-day scenarios** (cloud bust, equipment fault, eclipse)
2. **Scores them objectively** (% of recoverable losses recovered)
3. **Shows the replay** (leaderboard + animated decision trace)
Result: Proof that an agent works under stress.
 
**Key insight:** The product *isn't the agent*. It's the **evaluation platform**.
 
---

## THE CORE BUSINESS MODEL
 
```
                    GAUNTLET
                  (One Product)
                       │
    ┌──────────────────┼──────────────────┐
    │                  │                  │
AGENT BUILDERS      ASSET OPERATORS    GRID OPERATORS
(Company or Indie)  (Solar Parks)      (TSOs)
    │                  │                  │
    │                  │                  │
NEED:              NEED:                NEED:
"Prove my agent    "Validate my       "Certify my agent
is safe"           plant's resilience" keeps grid safe"
    │                  │                  │
    ▼                  ▼                  ▼
 GAUNTLET SCORES AGENTS
    │
    ├─ Can be white-labeled
    ├─ Can be SaaS
    ├─ Can be consulting projects
```
---



## REVENUE MODEL: THE THREE PATHS
 

 


### PATH 1: White-Label Certification (For Agent Companies like Invertix)

**Why they pay (the core argument):** their customers will not hand mission-critical, money-moving autonomy to an agent they cannot independently verify. Across enterprise AI in 2025 to 2026, fewer than 50% of paid pilots convert to production, and *trust* is the single most-cited blocker. Invertix already monitors 1.8 GW and has a stated commercial pipeline above 10 GW; the bottleneck is not building agents, it is getting customers past the "is it safe to let it act?" gate. Gauntlet is the tool that opens that gate.

**What Gauntlet sells them:** an independent, physics-based certificate the sales team puts on the table. *"This agent passed 55% of a 30-case discrimination battery (mean recovery 49%, worst-case P10 of 10% under Monte Carlo), against 8% for a rules-based baseline on the same bad days."* And the gym proves it can find the agent's failure modes: pointed at this agent in adversarial mode, the generator drives its mean recovery from 49% down to 30%, surfacing exactly where it breaks before a customer asset does. That evidence is what closes the deal.

**How it works:**
- Agent companies embed Gauntlet as their pre-deployment QA and certification layer.
- Every agent, and every iteration, runs through the battery before it touches a customer asset.
- The certificate ships with the sales proposal; annual re-certification renews trust and the contract.

**How they pay:** annual platform fee plus 5% of certified-agent revenue, OR a flat €10K per agent certification with annual re-cert. The fee is a fraction of the revenue it unlocks: at base assumptions Gauntlet returns about €4 to €5 of new ARR for every €1 the agent company pays (full model in the next section).

---
 
### PATH 2: SaaS Subscription (For Asset Operators)
**What:** Solar farms subscribe to run agents through Gauntlet
 
**How it works:**
- Plant operator: "I want to validate my new O&M agent"
- Runs agent through Gauntlet (cloud, fault, eclipse scenarios)
- Gets resilience score + replay
- Renews monthly to test new agents/iterations
 
**Customer:** Independent solar operators, energy trading firms, asset managers
 
---
 
### PATH 3: Consulting Projects (Custom Scenarios)
**What:** Build custom stress scenarios for specific companies
 
**How it works:**
- Customer: "We need to stress-test against [specific failure mode]"
- Gauntlet agent-workforce builds custom scenarios.
- Benchmark the farm agents.
- Deliver report + recommendations

**Examples:**
- "Negative price spike scenario" 
- "Multi-inverter cascade failure"
- "Regulatory compliance validation"

 
**Customer:** Large operators (E.ON, Enerparc), energy consultancies, regulators
 
---

## REVENUE UPLIFT FOR AGENT COMPANIES (THE NUMBERS)

This is the heart of the white-label pitch: **Gauntlet is a sales accelerator.** It moves four levers on an agent company's P&L.

**Lever 1 | Conversion rate (the big one).** Certification attacks the #1 named blocker (trust) in the longest, leakiest stage of the funnel: POC to production, where industry conversion is under 50%. A neutral certificate turns "we think it's safe" into "here is the proof."

**Lever 2 | Sales-cycle compression.** A bespoke "prove it's safe" validation runs 6 to 12 months. A standardized Gauntlet certification runs in days, pulling revenue forward and freeing a capacity-constrained team (Invertix is scaling 5 to 20 people in 2026) to run more deals per year.

**Lever 3 | Price premium and larger initial scope.** A certified, benchmarked agent is trusted with more MW on day one and can carry a premium versus an unproven competitor.

**Lever 4 | Catastrophe and churn avoidance.** One autonomous failure (a mistimed eclipse-day trade, a missed silent fault) loses the contract and poisons the reference that gates the next several GW. The gym catches it before deployment.

### Worked example: Invertix (all assumptions labeled)

| Input | Value | Basis |
|---|---|---|
| Commercial pipeline | 10 GW | Invertix's stated pipeline |
| Paid autonomous-agent ARPU | €2,500 / MW / yr (= €2.5M per GW) | est. (see note) |
| POC to production conversion, no certification | 40% | industry: under 50% |
| Conversion with certification | 52% (+12 pp) | conservative; certification targets the named #1 blocker |

> **ARPU note:** blends O&M / monitoring SaaS (€1,000 to €3,000/MW/yr) with a forecasting and intraday-optimization value share. German intraday averaged €89/MWh in 2025 and solar runs ~1,000 MWh/MW/yr, so ~€89K/MW/yr of energy is at stake; capturing 3 to 5% of avoided forecast and imbalance loss is €2,700 to €4,500/MW/yr of value created, of which the agent prices a slice. Note "monitored" GW is not yet "paid autonomous" GW; the pipeline converts over several years, so the uplift below is steady-state value realized as it ramps, not Year-1 cash.

**Result (conversion lever alone):**

| | Converted (paid) | ARR @ €2.5M/GW |
|---|---|---|
| Without Gauntlet | 10 GW × 40% = 4.0 GW | €10.0M |
| With Gauntlet | 10 GW × 52% = 5.2 GW | €13.0M |
| **Uplift** | **+1.2 GW** | **+€3.0M ARR/yr (+30%)** |

Levers 2 to 4 stack on top of this and are not counted in the €3.0M.

### What Gauntlet earns, and the ROI to the agent company

- Gauntlet fee: 5% of certified revenue = 5% × €13.0M = **€650K/yr from one account.**
- Invertix nets +€3.0M of new ARR for a €650K fee → **~4.6x return; every €1 paid to Gauntlet returns ~€4.6 in new ARR.** Charging on the *total* certified book (not just incremental) is fair because certification de-risks the entire deployed book, lowering churn across all of it. Even crediting only the incremental €3.0M, the ROI clears 4x.

### Sensitivity: incremental ARR Gauntlet unlocks for Invertix

Incremental ARR = 10 GW × (conversion uplift) × (ARPU per GW).

| Conversion uplift | ARPU €2.0M/GW | €2.5M/GW (base) | €3.0M/GW | €4.0M/GW |
|---|---|---|---|---|
| +8 pp  | €1.6M | €2.0M | €2.4M | €3.2M |
| +12 pp (base) | €2.4M | **€3.0M** | €3.6M | €4.8M |
| +15 pp | €3.0M | €3.75M | €4.5M | €6.0M |
| +20 pp | €4.0M | €5.0M | €6.0M | €8.0M |

Even the pessimistic corner (modest +8 pp uplift, low €2.0M/GW ARPU) clears €1.6M/yr in new ARR, comfortably above Gauntlet's fee. **The pitch survives across the whole grid.**

---

## MARKET SIZE (GROUNDED)

- **TAM.** The EU has ~406 GW of solar (end 2025), heading to ~671 GW by 2028 (SolarPower Europe). As autonomous agents take over asset management, the validation layer captures ~5% of agent-software revenue. If 30% of capacity becomes agent-managed at ~€2.5M/GW/yr, that is ~122 GW × €2.5M × 5% ≈ **€15M/yr today, scaling past €25M/yr by 2028** before SaaS, consulting, wind, and storage.
- **SAM.** EU "AI worker for energy" vendors (Invertix and peers) plus the in-house agent teams at large operators (Enerparc, E.ON) building autonomy on their own books.
- **SOM (beachhead, Year 1 to 2).** 3 to 5 white-label accounts at €0.3M to €0.7M/yr each = **€1M to €3.5M ARR** without touching the long-tail SaaS market. Invertix alone models to ~€0.65M/yr.

---
 
## GO-TO-MARKET
 
### PHASE 1: Hackathon (September 2026)
**Goal:** Build MVP, win competition, get inbound leads
 
---
 
### PHASE 2: Pilot Phase (Oct to Dec 2026)
**Goal:** Land first customers, validate business model
 
**Actions:**
- Direct outreach to 15 to 20 prospects
  - 3 to 5 solar operators
  - 2 to 3 trading firms
  - 1 to 2 Invertix contacts (white-label discussion)
- Offer free trial (1 scenario, 15 min setup)
- Convert 1 to 2 of them into pilot contracts (€5K to €10K projects)

---
 
### PHASE 3: Scale Phase (Jan to June 2027)
**Goal:** 3 to 5 paying customers, establish recurring revenue
 
**Actions:**
- Convert pilot customers to annual contracts
- 3 to 5 new SaaS customers (word-of-mouth + cold outreach)
- 1 to 2 consulting projects
- Invertix white-label agreement signed

---
 
## PRICING STRATEGY
 
### SaaS Tiers (Monthly)
```
STARTER
├─ 1 agent scenario
├─ Email support
└─ Monthly report
 
PROFESSIONAL     
├─ 3 agents
├─ Custom scenario
├─ Slack support
└─ Weekly digest
 
ENTERPRISE      
├─ Unlimited agents
├─ Custom scenarios (2/mo)
├─ Dedicated account manager
└─ SLA guarantee
```
 
### White-Label (Commission Model)
```
Per-Agent Revenue Share:
├─ Agent company charges its customer (no change to their list price)
├─ Gauntlet takes 5% of certified-agent revenue
└─ OR: flat €10K/agent initial certification + annual re-cert

Why it is an easy yes:
├─ Gauntlet's fee is a fraction of the ARR it unlocks
├─ Base case: ~€650K/yr fee unlocks ~€3.0M new ARR (~4.6x ROI)
└─ Priced on the value created, not on Gauntlet's cost to run

Multi-Year Deal (Invertix base case):
├─ 10 GW pipeline, 52% certified conversion, €2.5M/GW ARPU
├─ Certified book €13.0M ARR → Gauntlet 5% = ~€650K/yr
└─ Target: €0.5M to €1M/year from Invertix alone as the book grows
```
 
---
## FINANCIAL SUMMARY
 
### Revenue Targets
| Timeline | Customers | MRR | ARR |
|----------|-----------|-----|-----|
| Month 1 to 3 | 1 to 2 | €2K to €5K | €30K to €60K |
| Month 4 to 6 | 3 to 5 | €10K to €20K | €150K to €300K |
| Month 7 to 12 | 5 to 10 | €30K to €50K | €500K to €1M |
| Year 1 Total | | | **€500K to €1M** |

Year 1 is carried by SaaS plus consulting plus the first white-label pilot. The white-label engine is the Year 2+ scaler: a single account like Invertix ramps to ~€0.65M/yr on its own as its certified book grows, and 3 to 5 such accounts is €1M to €3.5M of high-margin recurring revenue.

### Unit Economics (white-label account)
- ARR per account: ~€650K. Software gross margin ~85% → ~€550K annual gross profit.
- CAC (enterprise, founder-led, long cycle): ~€100K to €150K fully loaded.
- **Payback: under 4 months. LTV:CAC: roughly 12:1 to 18:1** over a 4-year account life. The white-label account, not the SaaS seat, is what carries the economics.
 


## CONCLUSION
 
Gauntlet is a **real product solving a real problem** with:
- ✅ A quantified value prop for the buyer: certification lifts a certified agent company's converted ARR ~30% (~€3.0M/yr on Invertix's 10 GW pipeline) for a ~4.6x return on our fee
- ✅ Multiple revenue streams (white-label, SaaS, consulting)
- ✅ Clear path to customers (hackathon judges, cold outreach, sponsor partner)
- ✅ Derived unit economics (12:1 to 18:1 LTV:CAC, under 4-month payback on a white-label account)
- ✅ Defensible moat (real data, real scenarios, neutrality)
- ✅ Buildable MVP in 10 hours
- ✅ €500K to €1M Year 1 revenue, scaling to €1M to €3.5M as white-label accounts ramp
**Next action:** Build the MVP, win the hackathon, start cold outreach immediately.
 
---
 
**Date:** June 2026 | **Status:** Ready for Execution
 