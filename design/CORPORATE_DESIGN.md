# Gauntlet | Corporate Design System

Version 1.0. This is the single source of truth for how Gauntlet looks, sounds, and presents itself. It governs the product UI, the pitch deck, the certificate artifact, the website, and any social or print surface. The pitch deck spec ([PITCH_DECK.md](PITCH_DECK.md)) pulls its colors, fonts, and motifs from this document.

---

## 1. Brand foundation

**Name.** Gauntlet. To "run the gauntlet" is to pass through a punishing test and come out proven. The product throws an agent's worst days at it and reports what survived.

**Category.** The validation layer for autonomous energy agents. Think crash-test lab and certification body, not another vendor of agents.

**Positioning statement.**
> Gauntlet is the proving ground where autonomous energy agents earn the trust to act. We simulate the worst days a grid can throw at an agent, score what it recovers in euros, and issue the certificate that closes the deal.

**Brand promise.** Independent, physics-based, reproducible proof. Same agent, same day, same score, every time.

**Personality.** Four traits, each with the line we will not cross:
- **Rigorous**, not academic. We show the math; we do not lecture.
- **Calm under stress**, not dramatic. The scenarios are violent; our tone is steady.
- **Evidence-led**, not boastful. Numbers carry the argument.
- **Neutral**, not partisan. We do not pick winners; the gauntlet does.

**Taglines** (primary first):
1. The proving ground for autonomous energy agents.
2. Prove it can handle the bad day.
3. Run the gauntlet. Earn the trust.

---

## 2. Logo

**Concept.** A ring (the arena, and the eclipse disc) broken by a downward notch on its lower arc that climbs back to the rim. The notch is the Recovery Curve: a bad day hits, the agent reacts, the line recovers. One mark carries the product's core idea and its hero event (the eclipse).

**Lockups.**
- **Primary:** mark to the left of the wordmark GAUNTLET, baseline-aligned, gap equal to the mark's stroke-circle radius.
- **Stacked:** mark centered above the wordmark, for square spaces.
- **Mark only:** app icon, favicon, social avatar, the certificate seal.
- **Wordmark only:** dense UI headers where the mark would be too small to read.

**Wordmark.** Set in Space Grotesk Medium, all caps, letter-spacing +2%. Never restyle the letterforms.

**Clear space.** Keep clear space equal to the cap-height of the "G" on all sides.

**Minimum size.** Mark 24 px / 8 mm. Full lockup 120 px / 32 mm wide.

**Color variants.** Light-on-ink (default), ink-on-light, single-color Corona Amber for hero moments, and pure monochrome for stamps and embossing.

**Misuse (do not):** recolor the wordmark, add a drop shadow or bevel, stretch or condense, rotate the mark, place the light lockup on a low-contrast background, or box the logo in a competing shape.

---

## 3. Color

The system is a dark solar-industrial panel. Backgrounds are near-black and warm, structure is gray, and the palette is closed: black, gray, white, orange, red. Orange is the sun (energy, and what was recovered), red is the bad day (loss and fault), white is the truth and the rival, gray is structure. This is the product palette of record; the product mirrors it in `theme/tokens.css` (see [UI_OVERHAUL.md](UI_OVERHAUL.md)).

### Core palette

| Token | Hex | Role |
|---|---|---|
| `bg` | `#0B0B0D` | Primary background (slides, app shell) |
| `surface-1` | `#131316` | Cards, panels |
| `surface-2` | `#1C1C21` | Raised surfaces, inputs, hover |
| `line` | `#2A2A30` | Borders, dividers, grid lines |
| `text` | `#F2F2F0` | Primary text on dark (warm white) |
| `text-dim` | `#A8A29A` | Secondary text, captions, axis labels |
| `neutral` | `#8A857C` | Baseline agents, structure |

### Sun ramp and alert (the only hues)

| Token | Hex | Meaning | Use |
|---|---|---|---|
| `sun-100` | `#FFE3C2` | Pale energy | Lightest agent in the ramp, soft highlights |
| `sun-300` | `#FFB066` | Warm energy | Mid agent, secondary accents |
| `sun-500` | `#FF7A18` | Core brand orange, the sun | Primary buttons, the reference agent, recovered band, score reveals |
| `sun-700` | `#C85A0E` | Deep energy | Hottest agent, deep accents |
| `alert` | `#E5341E` | Loss and fault, a STATE | Fail badges, fault markers, negative deltas, chaos actions |
| `alert-dim` | `#4A1A12` | Loss background | Fault-card and chaos-button backgrounds |
| `white` | `#FFFFFF` | Max emphasis, the rival, the oracle | Sparingly: the benchmark line, the right fighter |

### Gradient

**Sun gradient:** `#FF8A00` to `#FFD166`, 135 degrees. Reserved for hero moments only (title slide, the eclipse, the certified-score reveal). Never use it behind body text.

### Usage rules
- One accent per view carries the meaning. Do not paint a slide in many accents at once.
- Orange is precious. If everything glows, nothing reads as the signal.
- Red is a state, never an identity. It means loss or fault, not "agent B."
- Agent identity comes from value (the sun ramp), line style, and labels, not from new hues.
- Text contrast: `text` on `bg` and `surface-1` clears WCAG AA. Never set `text-dim` on `surface-1` below 13 px.

---

## 4. Typography

Three families, each with a job. Headlines feel engineered, body stays neutral and readable, and every number that carries a result is set in mono so it reads like instrumentation.

| Role | Family | Weights | Fallback stack |
|---|---|---|---|
| Display / headline | Space Grotesk | 500, 700 | `"Space Grotesk", "Archivo", system-ui, sans-serif` |
| Body / UI | Inter | 400, 500, 600 | `"Inter", system-ui, -apple-system, sans-serif` |
| Data / metrics | JetBrains Mono | 400, 500, 700 | `"JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace` |

### Type scale

| Level | Size / line | Family | Use |
|---|---|---|---|
| Display | 64 / 68 | Space Grotesk 700 | Title slide, hero numbers |
| H1 | 40 / 44 | Space Grotesk 700 | Slide titles |
| H2 | 28 / 34 | Space Grotesk 500 | Section heads |
| H3 | 20 / 28 | Space Grotesk 500 | Card titles |
| Body | 16 / 24 | Inter 400 | Paragraphs, bullets |
| Small | 13 / 18 | Inter 400 | Captions, footnotes, sources |
| Data L | 48 / 52 | JetBrains Mono 700 | Big metric reveals (the score) |
| Data M | 16 / 22 | JetBrains Mono 500 | Table figures, percentages, P10 |

### Rules
- Every result is mono: scores, percentages, euro figures, P10, MW and GW, dates of the bad day.
- Headlines are short and declarative. No headline runs past two lines at H1.
- Sentence case for body, all caps only for the wordmark and small eyebrow labels (letter-spacing +6%).

---

## 5. Iconography and imagery

**Icons.** Line style, 1.5 px stroke at a 24 px frame, rounded joins, 2 px corner radius. One consistent set maps to the product's vocabulary:
- cloud = weather bust
- bolt with a slash = silent fault
- eclipse disc = the eclipse scenario
- gauge = the score
- medal = the leaderboard
- shield with a check = certified

**Imagery direction.** Avoid the clichd stock photo of blue-sky solar panels. The visual world is dark and schematic: grid topology lines, charts as texture, the eclipse disc and its corona. Where a photograph is needed, apply a duotone of `bg` plus `sun-500` so it sits inside the system.

**The bad-day motif.** A faint Recovery Curve can run as a watermark across section dividers: the line dips, the recoverable band shades, the line climbs. It is the brand's heartbeat.

---

## 6. Data visualization

Charts are the product, so they are held to the highest standard. Gauntlet shows results, never decoration.

**The Recovery Curve (signature chart).**
- X axis: time across the trading/operating day. Y axis: cumulative euro position.
- `text-faint` floor line (dotted) = the do-nothing or worst path.
- `white` line = the oracle (best achievable), the benchmark.
- Per-agent line in its assigned value from the sun ramp.
- The band between floor and oracle is the recoverable money at stake, shaded faint `sun-500`. The lost portion shades faint `alert`.
- Fault events drop a thin `alert` vertical; the eclipse window is a faint `sun-500` glow band.

**Leaderboard.**
- Agent name with a color chip, score as a `sun-500`-to-`alert` bar (warm = recovered, red = lost), figures in Data M mono.
- P10 (tail risk) shown as a whisker behind the bar so the worst case is always visible next to the mean.
- Always include the `noop` and `rules` baselines for context.

**Agent color assignments (consistent everywhere). Identity is value plus line style plus label; red is never an agent.**

| Agent | Color | Line |
|---|---|---|
| `llm` (the reference brain) | `sun-500` `#FF7A18` | solid |
| `claude` | `white` `#F2F2F0` | solid |
| `ds-cautious` | `sun-100` `#FFE3C2` | solid |
| `ds-balanced` | `sun-300` `#FFB066` | solid |
| `ds-aggressive` | `sun-700` `#C85A0E` | solid |
| `rules` (baseline) | `neutral` `#8A857C` | dashed |
| `noop` (floor) | `text-faint` `#6E6A62` | dotted |

**Chart hygiene.** No 3D, no gradients inside data bars, no pie charts. Gridlines in `line` at low opacity. Label the unit once, clearly. The headline number sits above the chart in Data L mono.

---

## 7. Product and presentation surfaces

**App UI.** The product lives in the dark solar-industrial world: `bg` shell with a low sun-glow and grain, `surface-1` cards, mono metrics, the Test Lab and Arena views. New UI inherits the tokens above. Buttons: primary is `sun-500` fill with `bg` text; secondary is `line` border with `text` label that warms to `sun-500` on hover.

**The certificate (the money artifact).** A dark card, mark-only seal top-left, the agent name, the headline score in Data L, a compact Recovery Curve thumbnail, the battery pass-rate and P10, the date and a reproducibility hash. This is the object the agent company puts in front of its customer, so it must look like it came from a lab, not a marketing team.

**Slides.** See [PITCH_DECK.md](PITCH_DECK.md) for the master and per-slide spec.

---

## 8. Voice and tone

We sound like a test lab that respects the reader's time.

**Principles.**
- Precise. Name the scenario, the metric, the number.
- Calm. The day is violent; the sentence is steady.
- Evidence-led. The number makes the claim; we do not inflate it with adjectives.
- Plainspoken. A grid operator and an investor both understand us on first read.

**Vocabulary (use these).** the gym, run the gauntlet, the bad day, scenario, battery, recover, recoverable losses, certify, certificate, P10, tail risk, discrimination, adversarial, the floor, the oracle.

**Do / don't.**
- Do: "The rules agent false-dispatched a crew on the cloud front and lost EUR 4,200. The certified agent held position and recovered 78%."
- Don't: "Our revolutionary AI delivers game-changing resilience for the energy transition."

**Copy bans (house style).** No em dashes or en dashes (use commas, periods, or pipes). No "not just X, but Y" constructions. No rule-of-three padding where the third item is filler. No self-praise ("no fluff", "honestly", "to be fair"). No glaze openers. Let the evidence open.

---

## 9. Applications checklist

- **Pitch deck:** 16:9, `bg` master, see PITCH_DECK.md.
- **Certificate:** dark card, seal, score in mono, reproducibility hash.
- **One-pager:** problem, the number (+30% converted ARR), the certificate, the ask.
- **Social card:** mark + one stat in Data L on `bg` with a single Recovery Curve.
- **README badge:** mark-only on `surface-1`, "Gauntlet-certified" in mono.

---

## Quick reference (paste into any tool)

```
COLORS (closed palette: black, gray, white, orange, red)
bg #0B0B0D  surface-1 #131316  surface-2 #1C1C21  line #2A2A30
text #F2F2F0  text-dim #A8A29A  neutral #8A857C
sun-100 #FFE3C2  sun-300 #FFB066  sun-500 #FF7A18  sun-700 #C85A0E
alert #E5341E (loss/fault, a STATE)  white #FFFFFF (rival/oracle, sparingly)
sun gradient: #FF8A00 -> #FFD166 @135deg (hero only)

FONTS
Headline: Space Grotesk (500/700)
Body:     Inter (400/500/600)
Data:     JetBrains Mono (400/500/700)   <- all numbers

MOTIF
Recovery Curve: line dips on the bad day, recovers; band = money at stake.
Numbers always mono. One accent per view. Orange is precious. Red is a state, not an agent.
```
