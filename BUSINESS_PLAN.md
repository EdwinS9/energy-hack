# GAUNTLET: Stress-Test Gym for Autonomous Energy Agents

> **"How do enterprises safely deploy autonomous agents in mission-critical energy infrastructure?"**

This is not an agent. Not a simulator. It's the **validation layer** that every energy company needs but cannot justify building in-house.

---


## DETAILED FIT ANALYSIS BY SPONSOR

### INVERTIX: "The Agent Certification Platform"

#### Problem Invertix Faces
- 200+ agent companies globally, but no industry standard for validation
- Customers demand proof: "Is this agent safe?" "What's the worst-case loss?"
- Invertix sells agents; Gauntlet certifies them → no conflict of interest

#### How Gauntlet Solves It

**#1.1 Data-Center Siting & Power:**
- Agent makes siting recommendations based on power availability + carbon + cost
- Gauntlet scenario: Grid congestion + PPA default → Agent still finds optimal site
- Proof: Agent is robust across market conditions

**#1.2 Renewable Forecasting:**
- Agent forecasts solar/wind 24h ahead to guide trading
- Gauntlet scenario: Forecast error (cloud bust) + price spike → Agent still makes money
- Proof: Forecast model doesn't overfit to sunny days

**Open Track (Satellite, Trading):**
- Agent uses satellite imagery to find solar sites / trade electricity
- Gauntlet scenario: Satellite failure + sudden weather shift → Agent adapts
- Proof: Agent is resilient to data failures

#### Revenue Model
- **Agent Licensing:** €10K–€15K/month per agent (pay for each agent Invertix fields)
- **Leaderboard SaaS:** €15K/month (host benchmark for 50+ agents)
- **Consulting:** €80K projects (custom scenarios)
- **White-Label:** 20–30% revenue share (Invertix-branded Gauntlet)

**Year 1 Target:** €470K ARR from Invertix customers

#### Key Success Metric
**Gauntlet-Certified Badge:** Invertix can market "40% better than rule-based under stress"

---

### ENERPARC: "The Plant Resilience Platform"

#### Problem Enerparc Faces
- 10 years of real inverter data from 2 plants; what patterns actually matter?
- One missed fault = €50K/day in lost generation
- Operators need to know: "Where are my weak points? What can I fix?"

#### How Gauntlet Solves It

**#2.1 Digital Twin (ML Model):**
- Build baseline model of plant output vs. weather
- Gauntlet scenario: Inverter failure + high temperature + soiling → Expected output drops 60%
- Proof: O&M team can validate their twin against worst-case scenarios

**#2.2 Digital Twin (O&M Agents):**
- Agent classifies error codes + routes service tickets automatically
- Gauntlet scenario: Simultaneous inverter failures at peak output → Can agent detect both?
- Proof: Agent doesn't miss cascading faults

**Open Track (Custom PV Scenarios):**
- Enerparc defines custom "bad days" specific to their plants
- Gauntlet scenario: Multi-day soiling creep + partial inverter failure
- Proof: Plant is insurance-grade under their worst-case

#### Revenue Model
- **Plant Subscriptions:** €8K–€15K/month per asset (host their twin + monitor)
- **Monte Carlo Analysis:** €15K–€30K per plant (500-scenario robustness)
- **Regulatory Reports:** €5K–€10K per audit (audit-ready PDF)
- **Custom Scenarios:** €10K–€25K projects (industry-specific bad days)

**Year 1 Target:** €530K ARR from Enerparc customers

#### Key Success Metric
**Resilience Score:** "Plant A: 88% resilience. Plant B: 76% (top 10% risk)"

---

### E.ON: "The Grid Safety Validation Platform"

#### Problem E.ON Faces
- Must keep grid N-1 secure (survive loss of any single line without cascading failures)
- Autonomous dispatch agents are new; regulators demand proof they don't break safety
- One cascading failure = €100M+ in costs + grid blackout

#### How Gauntlet Solves It

**#3.1 Grid Operation Agents:**
- Agent proposes dispatch actions (curtail, ramp, switch) when grid is stressed
- Gauntlet scenario: Line trip during high wind → Agent keeps grid N-1 secure
- Proof: Agent never violated safety constraints across 500 contingencies

**#3.2 Foundation Model Validation:**
- GridSFM is fast but may be inaccurate on novel topologies
- Gauntlet scenario: Unusual grid state + rare weather combo → Does GridSFM still work?
- Proof: Model is validated on edge cases before production

**Open Track (Grid Scenarios):**
- E.ON defines custom contingencies (unusual tie-lines, transmission constraints)
- Gauntlet scenario: Cascade failure (3 lines trip in sequence) → Grid stays safe
- Proof: Novel topologies don't break the agent

#### Revenue Model
- **Grid Licenses:** €40K–€75K/month per operator (host + monitor 24/7)
- **Contingency Screening:** €15K per batch of 100 novel scenarios
- **Regulatory Audits:** €25K per compliance report (ENTSO-E O-OP)
- **Real-Time Monitoring:** €10K/month add-on (production deployment support)

**Year 1 Target:** €500K ARR from E.ON customers

#### Key Success Metric
**N-1 Certification:** "Agent maintains N-1 security in 99.2% of Monte Carlo scenarios"

---

## WHY GAUNTLET WORKS FOR ALL THREE

### 1. Universal Problem: Agent Validation
| Company | Their Problem | Gauntlet Answer |
|---------|---|---|
| Invertix | "Is our agent deployable?" | "Run it through Gauntlet and we'll show you." |
| Enerparc | "Is our asset safe with this agent?" | "Gauntlet will find your worst-case scenario." |
| E.ON | "Does this agent break N-1 security?" | "We've tested 500 contingencies. Here's the proof." |

### 2. Neutral Arbitrator Position
- Gauntlet doesn't sell agents (Invertix does)
- Gauntlet doesn't operate plants (Enerparc does)
- Gauntlet doesn't run grids (E.ON does)
- Gauntlet validates all of them equally → Trusted by all

### 3. Scalable Scenario Model
- Start with 3 core scenarios (S1, S2, S3)
- Each customer can define custom scenarios
- Monte Carlo multiplies any scenario to 500 variations
- Revenue scales as scenario library grows

### 4. Real Physics + Real Data
- pvlib (PV modeling) + pandapower (grid modeling)
- Real SMARD prices, Open-Meteo weather, ENTSO-E topologies
- Pre-downloaded data moat (defensible)
- Real scenarios (August 12, 2026 eclipse) win trust

---

## COMPETITIVE POSITIONING BY SPONSOR

### How Gauntlet Beats Alternatives for Each Sponsor

#### INVERTIX ALTERNATIVE: "Build Validation In-House"
| Factor | In-House | Gauntlet |
|--------|----------|----------|
| Setup Cost | €500K–€1M | €0 (SaaS) |
| Time to Deploy | 6–12 months | 2 weeks |
| Maintenance | Ongoing | Covered |
| Real-World Scenarios | Hard to build | Ready to go |
| **Winner** | ❌ | ✅ Gauntlet |

#### ENERPARC ALTERNATIVE: "Hire Consultants"
| Factor | Consultants | Gauntlet |
|--------|---|---|
| Cost per Analysis | €100K–€200K | €20K–€30K |
| Time | 3–6 months | 2 weeks |
| Recurring Insights | No | Yes (continuous) |
| Historical Comparison | Limited | Full database |
| **Winner** | ❌ | ✅ Gauntlet |

#### E.ON ALTERNATIVE: "Use Pandapower Directly"
| Factor | Pandapower | Gauntlet |
|---|---|---|
| Learning Curve | Steep (expert needed) | Shallow (ops-friendly) |
| Scenario Library | None (you build it) | 3+ pre-built + custom |
| Regulatory Reports | Manual | Audit-ready PDF |
| Explainability | Limited | Full decision logs |
| **Winner** | ❌ | ✅ Gauntlet |



## GO-TO-MARKET SEQUENCE

### Month 1: Hackathon MVP
- [ ] Launch with S3 (eclipse) scenario fully playable
- [ ] LLM worker agent ships
- [ ] React UI with leaderboard + replay
- [ ] Pitch to 100+ energy executives at hackathon
- [ ] Target: 10+ inbound inquiry leads

### Month 2–3: Pilot Phase
- [ ] Cold email 30 target prospects (10 per company)
- [ ] Convert 2–3 into pilot conversations
- [ ] Land 1 pilot contract (€20K consulting)
- [ ] Customer type: Early adopter (Enerparc asset operator or E.ON grid team)

### Month 4–6: Scale Phase
- [ ] Deliver 1st pilot results
- [ ] Convert to annual contract (€10K–€50K/mo)
- [ ] 1st 3 paying customers signed
- [ ] Publish case study (if customer permits)
- [ ] Launch S1 + S2 scenarios
- [ ] Revenue: €200K–€300K cumulative

### Month 7–12: Ramp Phase
- [ ] 5+ paying customers active
- [ ] Monte Carlo layer live
- [ ] White-label option for Invertix
- [ ] Revenue: €500K ARR + €200K–€400K in consulting
- [ ] Target: €700K–€900K cumulative Year 1

---

## SUCCESS CRITERIA BY SPONSOR

### INVERTIX SUCCESS = Agent Adoption + Benchmark Competition
- ✅ 8+ agents using Gauntlet by end of Year 1
- ✅ Leaderboard is public + drives traffic to Invertix website
- ✅ Customers quote Gauntlet scores in sales pitches ("Our agent beats rule-based by 40%")
- ✅ White-label deal signed (Invertix rebrands Gauntlet as their QA tool)

### ENERPARC SUCCESS = Plant Coverage + Resilience Proof
- ✅ 15+ plants subscribed by end of Year 1
- ✅ At least 1 plant: "We fixed a blind spot identified by Gauntlet"
- ✅ Regulatory audit passed citing Gauntlet results
- ✅ NRR ≥ 110% (expansion from 1 plant → 3+ plants)

### E.ON SUCCESS = Grid Security Certification + Regulatory Buy-In
- ✅ 2–3 TSOs/DSOs signed by end of Year 1
- ✅ E.ON agent approved by regulator citing Gauntlet validation
- ✅ Regulatory body (ENTSO-E) aware of Gauntlet as validation standard
- ✅ Real-time monitoring: Agent running in production with Gauntlet oversight

---

## RISK MITIGATION BY SPONSOR

### If Invertix Track Underperforms
- **Fallback:** Double down on Enerparc + E.ON
- **Pivot:** Position as "O&M agent validation" instead of "trading agent validation"
- **Revenue:** Still €2M+ from other two tracks

### If Enerparc Track Underperforms
- **Fallback:** Focus on E.ON grid operators (longer sales cycle but higher ACV)
- **Pivot:** Target independent solar operators (easier sales than corporate Enerparc)
- **Revenue:** Still €2M+ from other two tracks

### If E.ON Track Underperforms
- **Fallback:** Accelerate Invertix + Enerparc adoption
- **Pivot:** Sell to aggregators / DSOs instead of TSOs (faster sales, smaller deals)
- **Revenue:** Still €2M+ from other two tracks

**Bottom Line:** Diversified portfolio across three companies = resilient business model.

---

## APPENDIX: QUICK REFERENCE MATRIX

### By Decision-Maker Type

| Decision-Maker | Company | Track | Pain Point | Gauntlet Value |
|---|---|---|---|---|
| **CTO, Agent Company** | Invertix | #1.1, #1.2 | "Is my agent safe?" | Certification badge |
| **VP Engineering, Trading Firm** | Invertix | #1.2 | "Beat rule-based baseline?" | 40% recovery advantage |
| **VP Operations, Solar Farm** | Enerparc | #2.1, #2.2 | "Avoid €50K/day downtime?" | Resilience score |
| **O&M Manager, Solar Farm** | Enerparc | #2.2 | "Fix maintenance backlog?" | Alert prioritization |
| **Grid Operations Manager, TSO** | E.ON | #3.1, #3.2 | "Keep N-1 secure?" | N-1 certification |
| **Regulatory Compliance, TSO** | E.ON | #3.1, #3.2 | "Audit the agent?" | Audit-ready report |

---

**Document Version:** 1.0 | **Date:** June 2026 | **Status:** Final