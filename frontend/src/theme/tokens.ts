// JS mirror of tokens.css for chart components (recharts needs literal colors).
// See design/UI_OVERHAUL.md. Red is a STATE (loss/fault), never an agent identity.
export const C = {
  bg: '#0B0B0D',
  surface1: '#131316',
  surface2: '#1C1C21',
  line: '#2A2A30',
  lineSoft: '#1F1F24',
  text: '#F2F2F0',
  textDim: '#A8A29A',
  textFaint: '#6E6A62',
  neutral: '#8A857C',
  sun100: '#FFE3C2',
  sun300: '#FFB066',
  sun500: '#FF7A18',
  sun700: '#C85A0E',
  alert: '#E5341E',
  white: '#FFFFFF',
} as const

// Agent identity, drawn from the warm ramp + neutrals. Distinct by value + label.
export const AGENT_COLOR: Record<string, string> = {
  noop: C.textFaint, // floor
  rules: C.neutral, // baseline
  llm: C.sun500, // reference / hero
  claude: C.white, // warm white, distinct from the oranges
  'ds-cautious': C.sun100,
  'ds-balanced': C.sun300,
  'ds-aggressive': C.sun700,
  deepseek: C.sun300,
}

export const agentColor = (id: string): string => AGENT_COLOR[id] ?? C.neutral

// Score ramp: orange = good (warm/recovered), red = bad (loss). No green.
export function scoreColor(s: number): string {
  if (s >= 0.5) return C.sun500
  if (s > 0.15) return C.sun300
  return C.alert
}
