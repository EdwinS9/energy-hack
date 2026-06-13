import type { Results, Trace } from './types'

const env = (import.meta as any).env
const API = env?.VITE_API_URL ?? (env?.PROD ? '' : 'http://localhost:8000')
// Static deploy reads JSON baked under /data instead of calling the Python
// backend. Opt in explicitly with VITE_STATIC=1 at build time (the Vercel
// deploy). Live /simulate, chaos injection and on-the-fly reports are
// unavailable then (the Arena replays precomputed base episodes). Local
// `make demo` and `make ui` leave it unset, so they use the live backend.
export const STATIC_MODE: boolean = env?.VITE_STATIC === '1'
const DATA = `${env?.BASE_URL ?? '/'}data`
const sub = (data: DataSource) => (data === 'real' ? 'real/' : '')

async function getJson<T>(url: string, what: string): Promise<T> {
  const r = await fetch(url)
  if (!r.ok) throw new Error(`${what}: ${r.status}`)
  return r.json() as Promise<T>
}

export type DataSource = 'synthetic' | 'real'

export async function fetchResults(data: DataSource = 'synthetic'): Promise<Results> {
  if (STATIC_MODE) return getJson(`${DATA}/${sub(data)}results.json`, 'results')
  return getJson(`${API}/results?data=${data}`, 'results')
}

export async function fetchEpisode(
  scenario: string,
  agent: string,
  data: DataSource = 'synthetic',
): Promise<Trace> {
  if (STATIC_MODE) return getJson(`${DATA}/${sub(data)}${scenario}_${agent}.json`, 'episode')
  return getJson(`${API}/episodes/${scenario}/${agent}?data=${data}`, 'episode')
}

export interface ChaosFault {
  park: string
  step: number
  magnitude?: number
}
export interface ChaosClouds {
  park: string
  start_step: number
  end_step: number
  depth?: number
}
export interface HumanAction {
  k: number
  type: 'trade' | 'dispatch_crew'
  park: string
  delta_mw?: number
  hours?: number
}

export interface SimRequest {
  scenario: string
  agent: string
  seed?: number
  data?: DataSource
  faults?: ChaosFault[]
  clouds?: ChaosClouds[]
  human_actions?: HumanAction[]
}

export async function simulate(req: SimRequest): Promise<Trace> {
  // Static deploy has no live backend: replay the precomputed base episode.
  // Chaos and human actions are ignored (and their controls are hidden).
  if (STATIC_MODE) return fetchEpisode(req.scenario, req.agent, req.data ?? 'synthetic')
  const r = await fetch(`${API}/simulate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(req),
  })
  if (!r.ok) throw new Error(`simulate: ${r.status}`)
  return r.json()
}

// ---- intelligent test-case generator ----

export interface AgentKpis {
  mean: number
  pass_rate: number
  p10: number
}
export interface BatteryCase {
  name: string
  label: string
  category: string
  stake: number
  floor: number
  oracle: number
  fitness: number
  agents: Record<string, AgentKpis>
}
export interface AgentReport extends AgentKpis {
  hardest: { name: string; label: string; mean: number }
}
export interface WorkerInfo {
  id: string
  label: string
  kind: string
}
export interface Battery {
  mode: string
  seed: number
  mc_n: number
  k: number
  contestants: string[]
  workers: WorkerInfo[]
  cases: BatteryCase[]
  report: Record<string, AgentReport>
  persona_single_run?: boolean
}

export function reportCsvUrl(mode: string): string {
  return STATIC_MODE ? `${DATA}/report/${mode}.csv` : `${API}/report/battery/${mode}.csv`
}
export function reportPdfUrl(mode: string): string {
  return STATIC_MODE ? `${DATA}/report/${mode}.pdf` : `${API}/report/battery/${mode}.pdf`
}

export async function fetchBatteryModes(): Promise<string[]> {
  if (STATIC_MODE) return (await getJson<{ modes: string[] }>(`${DATA}/batteries.json`, 'batteries')).modes
  return (await getJson<{ modes: string[] }>(`${API}/batteries`, 'batteries')).modes
}

export async function fetchBattery(mode: string): Promise<Battery> {
  if (STATIC_MODE) return getJson(`${DATA}/battery/${mode}.json`, 'battery')
  return getJson(`${API}/battery/${mode}`, 'battery')
}
