import {
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  ReferenceArea,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts'
import type { StepRecord } from '../types'
import { C } from '../theme/tokens'

function hhmm(iso: string): string {
  return iso.slice(11, 16)
}

export default function ThreeCurveChart({
  steps,
  playhead,
  showEclipse = false,
  height = 320,
  compact = false,
}: {
  steps: StepRecord[]
  playhead: number
  showEclipse?: boolean
  height?: number
  compact?: boolean
}) {
  const sum = (rec: Record<string, number>) =>
    Object.values(rec).reduce((a, b) => a + b, 0)

  const data = steps.map((s) => ({
    time: hhmm(s.time),
    forecast: s.k <= playhead ? +sum(s.forecast_mw).toFixed(1) : null,
    weatherExpected: s.k <= playhead ? +sum(s.twin_mw).toFixed(1) : null,
    actual: s.k <= playhead ? +sum(s.actual_mw).toFixed(1) : null,
    schedule: s.k <= playhead ? +sum(s.schedule_mw).toFixed(1) : null,
    price: s.da_price,
  }))

  return (
    <ResponsiveContainer width="100%" height={height}>
      <LineChart data={data} margin={{ top: 6, right: 8, bottom: 0, left: 0 }}>
        <CartesianGrid stroke={C.line} />
        <XAxis dataKey="time" interval={11} stroke={C.textDim} fontSize={12} />
        <YAxis
          stroke={C.textDim}
          fontSize={12}
          label={{ value: 'MW', angle: -90, position: 'insideLeft', fill: C.textDim }}
        />
        {!compact && (
          <YAxis
            yAxisId="price"
            orientation="right"
            stroke={C.lineSoft}
            fontSize={11}
            domain={[0, 400]}
            label={{ value: 'EUR/MWh', angle: 90, position: 'insideRight', fill: C.lineSoft }}
          />
        )}
        <Tooltip
          contentStyle={{ background: C.surface1, border: `1px solid ${C.line}` }}
          labelStyle={{ color: C.text }}
        />
        {!compact && <Legend />}
        {showEclipse && (
          <ReferenceArea
            x1="19:15"
            x2="21:15"
            fill={C.sun500}
            fillOpacity={0.1}
            stroke={C.sun500}
            strokeOpacity={0.35}
            label={{ value: 'eclipse 19:20-21:10', position: 'insideTop', fill: C.sun300, fontSize: 12 }}
          />
        )}
        {!compact && (
          <Line
            yAxisId="price"
            dataKey="price"
            name="DA price (EUR/MWh)"
            stroke={C.textFaint}
            strokeDasharray="2 3"
            dot={false}
            strokeWidth={1}
          />
        )}
        <Line
          dataKey="forecast"
          name="expected from forecast"
          stroke={C.neutral}
          strokeDasharray="6 4"
          dot={false}
          strokeWidth={1.5}
          isAnimationActive={false}
        />
        <Line
          dataKey="schedule"
          name="scheduled (after trades)"
          stroke={C.sun500}
          type="stepAfter"
          dot={false}
          strokeWidth={1.5}
          isAnimationActive={false}
        />
        <Line
          dataKey="weatherExpected"
          name="expected from actual weather"
          stroke={C.sun300}
          dot={false}
          strokeWidth={1.5}
          isAnimationActive={false}
        />
        <Line
          dataKey="actual"
          name="actual production"
          stroke={C.text}
          dot={false}
          strokeWidth={2.5}
          isAnimationActive={false}
        />
      </LineChart>
    </ResponsiveContainer>
  )
}
