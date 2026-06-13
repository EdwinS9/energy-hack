import { useEffect, useRef, useState } from 'react'
import { useReducedMotion } from 'framer-motion'

// Count-up from 0 (on mount) or from the previous value (on change).
// Honors prefers-reduced-motion by snapping to the final value.
export default function AnimatedNumber({
  value,
  duration = 800,
  format = (n: number) => Math.round(n).toLocaleString(),
}: {
  value: number
  duration?: number
  format?: (n: number) => string
}) {
  const reduce = useReducedMotion()
  const [display, setDisplay] = useState(reduce ? value : 0)
  const fromRef = useRef(reduce ? value : 0)
  const raf = useRef<number | null>(null)

  useEffect(() => {
    if (reduce) {
      setDisplay(value)
      fromRef.current = value
      return
    }
    const from = fromRef.current
    const start = performance.now()
    const tick = (t: number) => {
      const p = Math.min(1, (t - start) / duration)
      const eased = 1 - Math.pow(1 - p, 3)
      setDisplay(from + (value - from) * eased)
      if (p < 1) raf.current = requestAnimationFrame(tick)
      else fromRef.current = value
    }
    raf.current = requestAnimationFrame(tick)
    return () => {
      if (raf.current) cancelAnimationFrame(raf.current)
    }
  }, [value, duration, reduce])

  return <>{format(display)}</>
}
