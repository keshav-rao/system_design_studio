import { useEffect, useState } from 'react'
import { Sparkles, Brain, Network, ShieldCheck, Database } from 'lucide-react'

const STEPS = [
  { icon: <Brain className="w-5 h-5" />, label: 'Parsing requirements', color: 'text-indigo-400' },
  { icon: <Database className="w-5 h-5" />, label: 'Retrieving knowledge base evidence', color: 'text-blue-400' },
  { icon: <Sparkles className="w-5 h-5" />, label: 'Synthesising architecture with DeepSeek-R1', color: 'text-purple-400' },
  { icon: <Network className="w-5 h-5" />, label: 'Grounding in component catalog', color: 'text-cyan-400' },
  { icon: <ShieldCheck className="w-5 h-5" />, label: 'Running deterministic validator', color: 'text-emerald-400' },
]

export default function GeneratingScreen() {
  const [activeStep, setActiveStep] = useState(0)
  const [dots, setDots] = useState('.')

  useEffect(() => {
    const stepTimer = setInterval(() => {
      setActiveStep((s) => Math.min(s + 1, STEPS.length - 1))
    }, 2800)
    return () => clearInterval(stepTimer)
  }, [])

  useEffect(() => {
    const dotTimer = setInterval(() => {
      setDots((d) => (d.length >= 3 ? '.' : d + '.'))
    }, 400)
    return () => clearInterval(dotTimer)
  }, [])

  return (
    <div className="flex-1 flex items-center justify-center p-8">
      <div className="max-w-md w-full text-center space-y-10">
        {/* Animated orb */}
        <div className="relative flex items-center justify-center">
          <div className="absolute w-40 h-40 rounded-full bg-indigo-600/10 animate-ping" style={{ animationDuration: '2s' }} />
          <div className="absolute w-28 h-28 rounded-full bg-purple-600/15 animate-ping" style={{ animationDuration: '2.5s', animationDelay: '0.5s' }} />
          <div className="w-20 h-20 rounded-full bg-gradient-to-tr from-indigo-600 to-purple-600 flex items-center justify-center shadow-lg shadow-indigo-500/30">
            <Sparkles className="w-8 h-8 text-white" />
          </div>
        </div>

        <div className="space-y-2">
          <h2 className="text-2xl font-bold text-white">
            Generating Architecture{dots}
          </h2>
          <p className="text-sm text-slate-400">
            DeepSeek-R1 is reasoning over your requirements and 25+ knowledge sources.
            This may take 30–90 seconds.
          </p>
        </div>

        {/* Steps */}
        <div className="space-y-3 text-left">
          {STEPS.map((step, idx) => {
            const isPast = idx < activeStep
            const isCurrent = idx === activeStep
            return (
              <div
                key={idx}
                className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-500 ${
                  isCurrent
                    ? 'bg-indigo-950/60 border border-indigo-700/50'
                    : isPast
                    ? 'opacity-40'
                    : 'opacity-20'
                }`}
              >
                <span className={`${step.color} flex-shrink-0`}>{step.icon}</span>
                <span className="text-sm text-slate-300">{step.label}</span>
                {isCurrent && (
                  <span className="ml-auto text-indigo-400 text-xs font-mono animate-pulse">
                    running…
                  </span>
                )}
                {isPast && (
                  <span className="ml-auto text-emerald-400 text-xs">✓</span>
                )}
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
