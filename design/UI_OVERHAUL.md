# Gauntlet | UI Overhaul Spec

**Status: DRAFT for review.** Nothing gets implemented until this is approved. This spec governs a full restyle of the React/Vite frontend (Arena, Leaderboard, Test Lab, Replay, global shell) and supersedes the color section of [CORPORATE_DESIGN.md](CORPORATE_DESIGN.md) for the product UI.

## Decisions captured (from the brief)

- **Look:** dark solar-industrial. Near-black base, warm orange as the sun/energy accent, red for the bad day and faults, gray for structure, warm white for text. A "warm solarpunk feel," dark rather than lush-green.
- **Palette is closed:** black, gray, white, orange, red. No new hues. Blues, greens, and violets currently in the UI get remapped out.
- **Motion:** moderate plus a few hero moments. Micro-motion everywhere, three staged moments (the bad day plays in, the score reveal, the duel countdown). Never bouncy, never a Flash game.
- **Scope:** all four screens. The Arena is the hero.
- **Goal:** beautiful and serious, with enough play to carry a hackathon demo on a projector.

## What we are killing

- The early-2000s game feel: looping/pulsing animations (the winner banner pulse is already removed), saturated primary blues and greens, hard candy colors.
- Color sprawl. Today the UI uses 27 distinct hex values across blue, green, violet, amber, and red families. We collapse to one warm system.
- Decoration that is not data. Every visual either carries meaning or sets the warm tone.

---

## 1. Design principles

1. **Warm, dark, calm.** The screen is a near-black control room lit by a low sun. Heat (orange) means energy and what was saved; red means the bad day. Calm under stress is the mood.
2. **One hue, many values.** With a closed palette, identity comes from lightness, line style, and labels, not from inventing colors. Orange carries energy and positive outcomes, red is reserved strictly for loss and faults.
3. **Numbers are instruments.** Every score, euro, percent, GW, and P10 is set in mono and is the loudest thing on its card.
4. **Motion reveals, never loops.** Animation enters, settles, and stops. Nothing pulses or bounces forever. Everything honors reduced-motion.
5. **The Arena is the show.** Polish budget concentrates on the duel. Other screens stay consistent and clean.

---

## 2. Color system (the closed palette)

Defined as CSS custom properties in a new `frontend/src/theme/tokens.css`, mirrored as JS in `frontend/src/theme/tokens.ts` for chart components.

```css
:root {
  /* base | near-black, warm */
  --bg:         #0B0B0D;
  --surface-1:  #131316;   /* cards, panels */
  --surface-2:  #1C1C21;   /* raised, inputs, hover */
  --line:       #2A2A30;   /* borders, dividers */
  --line-soft:  #1F1F24;

  /* text | warm */
  --text:       #F2F2F0;   /* primary */
  --text-dim:   #A8A29A;   /* secondary */
  --text-faint: #6E6A62;   /* captions, the floor line */

  /* gray neutral | baselines and structure */
  --neutral:    #8A857C;

  /* sun ramp | orange = energy, positive, recovered */
  --sun-100:    #FFE3C2;
  --sun-300:    #FFB066;
  --sun-500:    #FF7A18;   /* core brand orange */
  --sun-700:    #C85A0E;
  --sun-glow:   rgba(255, 122, 24, 0.14);  /* radial bg, halos */

  /* alert | red = loss and fault, a STATE not an identity */
  --alert:      #E5341E;
  --alert-dim:  #4A1A12;

  /* pure white | max emphasis only, used sparingly */
  --white:      #FFFFFF;

  /* motion */
  --dur-micro:  200ms;
  --dur-ui:     320ms;
  --dur-count:  800ms;
  --ease-out:   cubic-bezier(0.22, 1, 0.36, 1);
  --ease-io:    cubic-bezier(0.65, 0, 0.35, 1);

  /* shape and elevation */
  --r-sm: 6px;  --r-md: 10px;  --r-lg: 16px;
  --glow: 0 0 0 1px rgba(255,122,24,.22), 0 10px 34px rgba(255,122,24,.10);
}
```

### Agent and chart identity

Identity is value plus line style plus a direct label. Red is never an agent color.

| Role | Color | Line style |
|---|---|---|
| Featured agent / left fighter | `--sun-500` orange | solid |
| Rival agent / right fighter | `--text` warm white | solid |
| Oracle (best achievable, benchmark) | `--white` | thin solid |
| Rules baseline | `--neutral` gray | dashed |
| Noop floor (do-nothing) | `--text-faint` | dotted |
| Persona: Cautious | `--sun-100` | solid |
| Persona: Balanced | `--sun-300` | solid |
| Persona: Aggressive | `--sun-700` | solid |
| Recoverable band (money at stake) | `--sun-glow` fill | area |
| Lost band / negative delta / fault marker | `--alert` at low alpha / solid | area / vertical rule |

### Migration map (current hex to token)

| Current | Count | Family | Becomes |
|---|---|---|---|
| `#0d1117` `#11151c` | 6 | bg | `--bg` |
| `#161b22` `#21262d` | 13 | panel | `--surface-1` / `--surface-2` |
| `#30363d` | 18 | border | `--line` |
| `#8b949e` `#6e7681` | 37 | gray | `--text-dim` / `--text-faint` / `--neutral` |
| `#e6edf3` | 6 | text | `--text` |
| `#388bfd` `#1f6feb` `#58a6ff` `#0f2440` | 13 | **blue (drop)** | `--text` (rival) / `--sun-500` (links) / `--surface-2` (bg) |
| `#3fb950` | 6 | **green (drop)** | `--sun-500` (recovered/pass) |
| `#6e40c9` `#a371f7` `#c9b6f0` | 6 | **violet (drop)** | `--sun-300` / `--sun-100` (personas) |
| `#f85149` `#ffb3ad` `#b62324` `#58181b` `#2d1517` `#6e4046` `#3d1214` | 19 | red | `--alert` / `--alert-dim` |
| `#d29922` `#e3b341` `#cc785c` `#e0a589` | 16 | amber/terracotta | `--sun-500` / `--sun-300` / `--sun-100` |

Acceptance: after migration, a grep for the dropped hex values returns zero.

---

## 3. Typography

Keep the three families from CORPORATE_DESIGN.md. They already fit the serious-warm tone.

- **Display / headline:** Space Grotesk (500, 700).
- **Body / UI:** Inter (400, 500, 600).
- **Data / metrics:** JetBrains Mono (400, 500, 700). Every number.

Load via self-hosted woff2 (no external CDN dependency at demo time). Scale per CORPORATE_DESIGN.md.

---

## 4. Background and texture (the warm tone)

- A single radial **sun-glow** anchored low-center: `radial-gradient(120% 80% at 50% 110%, var(--sun-glow), transparent 60%)` over `--bg`. This is the horizon light. It is the only ambient color on most screens.
- A faint 1px grid in `--line-soft` at low opacity for the control-room feel, behind content, never over text.
- Optional very subtle film grain (SVG noise at ~3% opacity) for a premium, non-flat surface. Behind a flag; cut if it costs frame rate.
- Cards are `--surface-1` with a `--line` hairline. Active or hero cards gain `--glow` (a soft orange halo), which is the only "lit" treatment.

---

## 5. Motion system

Library: **Framer Motion**. Defaults from the tokens above.

**Micro-motion (everywhere):**
- Entrances: fade plus 8px rise, `--dur-ui`, `--ease-out`. Lists stagger 50ms.
- Hover/press on controls: `--dur-micro`, scale to 1.0 only (no grow-past-1 bounce), border warms to `--sun-500`.
- Number reveals: count-up over `--dur-count`, mono, ease-out.
- Charts: path draw-in over 800ms ease-out; bars grow from baseline.

**Hero moment 1: the bad day plays in (Arena and Replay).** As the playhead advances, the recovery curve draws live, the eclipse window glows in (`--sun-glow` band), and fault events drop a `--alert` vertical with a single 400ms flash. The euro counter ticks in mono.

**Hero moment 2: the score reveal (Arena finish).** At the end, the final delta counts up, then the winner panel fades and rises in (no bounce), with a single one-shot orange glow settle on the winning side (the looping pulse is gone for good).

**Hero moment 3: the duel countdown (Arena start).** A 1.2s "3 . 2 . 1 . GO" or a sweeping start bar before the race, then the curves begin drawing. Skippable on click.

**Reduced motion:** `@media (prefers-reduced-motion: reduce)` disables count-ups, draw-ins, countdown, and the settle glow; final states render instantly. This is mandatory, not optional.

---

## 6. Per-screen redesign

### 6.1 Global shell (foundation for everything)
- Top bar: wordmark left, the SYNTHETIC / REAL toggle and primary nav center/right. Toggle is a segmented control in `--surface-2` with the active segment lit `--sun-500` text on a hairline.
- Content max-width with generous gutters; 8px spacing scale; consistent card component.
- Background sun-glow and grid applied here so all screens inherit.
- Buttons: primary is `--sun-500` fill, `--bg` label; secondary is `--line` border, `--text` label, warms on hover.

### 6.2 Arena (HERO)
- A true split duel: two mirrored columns (left fighter orange, right fighter white) sharing a center spine that holds the chaos-injection controls and the live clock.
- Each side shows the agent name, its live euro position in big mono, and its recovery curve drawing in real time.
- Chaos controls (inject cloud front, inject fault, eclipse) are a clean center rail, each a labeled control that drops its marker onto both curves when fired.
- Start: the countdown hero moment. Finish: the score reveal hero moment, with the redesigned static winner panel (fade-and-rise, one-shot glow, no loop). Keep the "X WINS, saves N EUR over the rival" line, set in mono.
- Judge-plays-it controls inherit the same control styling.

### 6.3 Leaderboard
- Ranked rows in a single table-card. Rank in mono, agent name with a small color chip (per the identity table), score as a horizontal bar in the agent's color.
- P10 (tail risk) shown as a thin whisker behind the bar so the worst case sits next to the mean.
- A small inline sparkline of the recovery curve per row. Baselines (rules, noop) always visible for context, in gray dashed/dotted.
- Scores count up on load; rows stagger in.

### 6.4 Test Lab and certificate
- Generator controls (mode toggle: discrimination / adversarial, target, seed) as a compact panel in `--surface-2`.
- The certification report as the centerpiece: per-agent pass-rate, worst-case P10, and the hardest case, in a mono cert table. Pass cells warm to `--sun-500`, fail cells to `--alert`.
- Case cards grouped by failure-mode category (FAULT, WEATHER, ECLIPSE, COMBO), each card a `--surface-1` tile with the case label, money-at-stake, and a mini curve.
- The worker-comparison charts (recharts) restyled to the palette: grouped bars by category, risk-return scatter. Download PDF/CSV buttons as secondary buttons.
- **The certificate artifact** (the money object): a dark card, mark seal, agent name, the headline score in Data L mono, a compact recovery-curve thumbnail, battery pass-rate and P10, date, and reproducibility hash. Must read as lab-grade.

### 6.5 Replay
- The bad-day chart at full width: floor (faint dotted), oracle (white), agent line (orange), recoverable band (sun-glow fill), lost band (alert low-alpha).
- The eclipse window rendered as a warm `--sun-glow` shaded band (the sun dimming), fault events as `--alert` verticals with small icons.
- The schedule/trades overlaid as markers on the agent line. Playhead scrubber in mono with the live euro position.

---

## 7. Implementation plan

**Stack:** keep React + Vite + recharts. Add `framer-motion`. Introduce `theme/tokens.css` and `theme/tokens.ts`, then refactor `styles.css` and components to consume tokens (no more inline hex). recharts colors come from `tokens.ts`.

**Phasing** (rough hackathon hours; Arena + shell + leaderboard is the minimum demo-critical path if time is short):

| Phase | Work | Est. |
|---|---|---|
| P0 Foundation | tokens.css + tokens.ts, refactor styles.css to tokens, install framer-motion, reduced-motion setup, font self-hosting | 2 to 3h |
| P1 Global shell | layout, nav, toggle, sun-glow background, type pass | 2h |
| P2 Arena (HERO) | split duel, control rail, live curves recolor, countdown + score reveal + winner panel redo | 3 to 4h |
| P3 Leaderboard | ranked rows, amber ramp, P10 whisker, sparklines, count-ups | 2h |
| P4 Test Lab + cert | report restyle, case cards, certificate artifact, comparison charts, downloads | 3h |
| P5 Replay | chart recolor, eclipse glow band, fault markers, trades | 2h |
| P6 Polish + QA | motion tuning, reduced-motion pass, color-audit grep, projector check | 2h |

Total roughly 16 to 18h, parallelizable. Suggest building P0 to P2 first and demoing the Arena early.

**Risks:** recharts animation control is limited, so the hero curve draw-in may need a thin custom SVG layer; the grain texture may cost frame rate (flagged off by default); self-hosting fonts needs the woff2 files added to the repo.

---

## 8. Acceptance and verification

Per the project's verify-by-running rule, done means:
- `make demo`, then exercise each screen in a browser: run an Arena duel to the finish (countdown, live draw, score reveal, static winner panel with no loop), generate a battery in Test Lab, open the certificate, replay a bad day with the eclipse band.
- Toggle the OS reduced-motion setting and confirm all animation falls back to instant final states.
- Color audit: grep the frontend for the dropped hex values (blues, greens, violets) and confirm zero matches; confirm only palette tokens are used.
- Projector check: legible at distance, high contrast, no color that washes out under a beamer.

---

## 9. Open items (need from you or assets)

- Logo mark as SVG (the ring-with-recovery-notch from CORPORATE_DESIGN.md) for the shell and certificate seal.
- Confirm self-hosted fonts are acceptable (Space Grotesk, Inter, JetBrains Mono woff2 in-repo).
- Confirm the grain texture is wanted, or drop it.
- Should this overhaul also update the color section of CORPORATE_DESIGN.md to match (recommended), so the brand doc and product agree?

---

**Once you approve, I will start at P0 and build up, demoing the Arena as soon as P2 lands.**
