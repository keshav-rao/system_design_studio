import { useState } from 'react'
import {
  CheckCircle2,
  XCircle,
  AlertTriangle,
  ArrowRight,
  ShieldAlert,
  Layers,
  Zap,
  Gauge,
  Sparkles,
} from 'lucide-react'
import { ComponentItem, CompatibilityCheckResponse } from '../../types/catalog'

interface CompatibilityCheckerProps {
  components: ComponentItem[]
}

const PRESET_TESTS = [
  { source: 'fastapi-app-server', target: 'postgresql', label: 'FastAPI -> PostgreSQL (Valid)' },
  { source: 'cloudflare-cdn', target: 'postgresql', label: 'CDN -> PostgreSQL (Antipattern)' },
  { source: 'fastapi-app-server', target: 'redis-cache', label: 'FastAPI -> Redis Cache (Valid)' },
  { source: 'postgresql', target: 'apache-kafka', label: 'DB -> Kafka (Needs Outbox)' },
  { source: 'websocket-gateway', target: 'redis-pubsub', label: 'WS Gateway -> Redis PubSub' },
  { source: 'fastapi-app-server', target: 'aws-s3', label: 'FastAPI -> S3 (Presigned)' },
]

export default function CompatibilityChecker({ components }: CompatibilityCheckerProps) {
  const [sourceSlug, setSourceSlug] = useState<string>(components[0]?.slug || 'fastapi-app-server')
  const [targetSlug, setTargetSlug] = useState<string>(components[1]?.slug || 'postgresql')
  const [loading, setLoading] = useState<boolean>(false)
  const [result, setResult] = useState<CompatibilityCheckResponse | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleCheck = async (src: string = sourceSlug, tgt: string = targetSlug) => {
    setLoading(true)
    setError(null)
    try {
      const res = await fetch(`/api/v1/catalog/compatibility/check?source=${encodeURIComponent(src)}&target=${encodeURIComponent(tgt)}`)
      if (!res.ok) {
        throw new Error(`Failed to check compatibility (HTTP ${res.status})`)
      }
      const data: CompatibilityCheckResponse = await res.json()
      setResult(data)
    } catch (err: any) {
      setError(err.message || 'Check failed')
    } finally {
      setLoading(false)
    }
  }

  const applyPreset = (src: string, tgt: string) => {
    setSourceSlug(src)
    setTargetSlug(tgt)
    handleCheck(src, tgt)
  }

  const sourceComp = components.find((c) => c.slug === sourceSlug)
  const targetComp = components.find((c) => c.slug === targetSlug)

  return (
    <div className="space-y-6">
      {/* Header card */}
      <div className="p-6 rounded-2xl bg-[#111726]/90 border border-slate-800/80 shadow-2xl backdrop-blur-md">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
          <div>
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-medium mb-2">
              <Zap className="w-3.5 h-3.5 text-blue-400" />
              Phase 2 Architectural Engine
            </div>
            <h2 className="text-xl font-bold text-white tracking-tight">
              Component Compatibility & Limits Checker
            </h2>
            <p className="text-slate-400 text-sm mt-0.5">
              Verify whether Component A can interface with Component B, check protocols, recommended patterns, and identify bottlenecks.
            </p>
          </div>

          <button
            onClick={() => handleCheck()}
            disabled={loading}
            className="self-start md:self-auto px-5 py-2.5 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-medium text-sm rounded-xl transition-all shadow-lg shadow-blue-500/25 flex items-center gap-2 disabled:opacity-50"
          >
            <Sparkles className="w-4 h-4" />
            {loading ? 'Evaluating...' : 'Run Compatibility Check'}
          </button>
        </div>

        {/* Quick Presets */}
        <div className="mb-6">
          <span className="text-xs text-slate-400 font-medium block mb-2">
            Quick Verification Presets:
          </span>
          <div className="flex flex-wrap gap-2">
            {PRESET_TESTS.map((p) => (
              <button
                key={p.label}
                onClick={() => applyPreset(p.source, p.target)}
                className={`px-3 py-1.5 rounded-lg text-xs font-mono transition-all border ${
                  sourceSlug === p.source && targetSlug === p.target
                    ? 'bg-blue-600/30 border-blue-500/60 text-blue-200'
                    : 'bg-slate-900/60 hover:bg-slate-800/60 border-slate-800 text-slate-300'
                }`}
              >
                {p.label}
              </button>
            ))}
          </div>
        </div>

        {/* Interactive Selectors */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 items-center relative">
          {/* Source Component */}
          <div className="p-4 rounded-xl bg-[#0B0F17]/90 border border-slate-800/80 space-y-2">
            <div className="flex items-center justify-between text-xs text-slate-400">
              <span className="font-semibold text-slate-300 flex items-center gap-1.5">
                <Layers className="w-3.5 h-3.5 text-blue-400" /> Source Component (A)
              </span>
              {sourceComp && (
                <span className="px-2 py-0.5 rounded-full text-[10px] bg-slate-800 text-slate-300 uppercase font-mono">
                  {sourceComp.layer}
                </span>
              )}
            </div>
            <select
              value={sourceSlug}
              onChange={(e) => setSourceSlug(e.target.value)}
              className="w-full bg-[#131B2E] border border-slate-700/80 rounded-lg px-3 py-2 text-sm text-slate-100 font-medium focus:outline-none focus:border-blue-500"
            >
              {components.map((c) => (
                <option key={c.slug} value={c.slug}>
                  {c.name} ({c.category})
                </option>
              ))}
            </select>
            {sourceComp && (
              <p className="text-xs text-slate-400 line-clamp-2 pt-1">{sourceComp.description}</p>
            )}
          </div>

          {/* Target Component */}
          <div className="p-4 rounded-xl bg-[#0B0F17]/90 border border-slate-800/80 space-y-2">
            <div className="flex items-center justify-between text-xs text-slate-400">
              <span className="font-semibold text-slate-300 flex items-center gap-1.5">
                <Layers className="w-3.5 h-3.5 text-indigo-400" /> Target Component (B)
              </span>
              {targetComp && (
                <span className="px-2 py-0.5 rounded-full text-[10px] bg-slate-800 text-slate-300 uppercase font-mono">
                  {targetComp.layer}
                </span>
              )}
            </div>
            <select
              value={targetSlug}
              onChange={(e) => setTargetSlug(e.target.value)}
              className="w-full bg-[#131B2E] border border-slate-700/80 rounded-lg px-3 py-2 text-sm text-slate-100 font-medium focus:outline-none focus:border-indigo-500"
            >
              {components.map((c) => (
                <option key={c.slug} value={c.slug}>
                  {c.name} ({c.category})
                </option>
              ))}
            </select>
            {targetComp && (
              <p className="text-xs text-slate-400 line-clamp-2 pt-1">{targetComp.description}</p>
            )}
          </div>
        </div>
      </div>

      {/* Result Display */}
      {error && (
        <div className="p-4 rounded-xl bg-red-950/40 border border-red-800/60 text-red-300 text-sm flex items-center gap-3">
          <XCircle className="w-5 h-5 text-red-400 flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {result && (
        <div
          className={`p-6 rounded-2xl border transition-all duration-300 shadow-2xl backdrop-blur-md ${
            result.compatible
              ? 'bg-emerald-950/20 border-emerald-800/60 shadow-emerald-950/20'
              : 'bg-rose-950/20 border-rose-800/60 shadow-rose-950/20'
          }`}
        >
          {/* Status banner */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-5 border-b border-slate-800/60">
            <div className="flex items-center gap-3">
              {result.compatible ? (
                <div className="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                  <CheckCircle2 className="w-6 h-6" />
                </div>
              ) : (
                <div className="w-10 h-10 rounded-xl bg-rose-500/20 border border-rose-500/30 flex items-center justify-center text-rose-400">
                  <ShieldAlert className="w-6 h-6" />
                </div>
              )}
              <div>
                <div className="flex items-center gap-2">
                  <span
                    className={`text-xs px-2.5 py-0.5 rounded-full font-bold uppercase tracking-wider ${
                      result.compatible
                        ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                        : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                    }`}
                  >
                    {result.compatible ? 'Compatible Connection' : 'Incompatible / Antipattern'}
                  </span>
                </div>
                <h3 className="text-base font-semibold text-white mt-1 flex items-center gap-2">
                  <span>{sourceSlug}</span>
                  <ArrowRight className="w-4 h-4 text-slate-500" />
                  <span>{targetSlug}</span>
                </h3>
              </div>
            </div>

            {/* Protocol & Pattern Tags */}
            <div className="flex flex-wrap items-center gap-2">
              {result.protocol && (
                <div className="px-3 py-1 rounded-lg bg-slate-900 border border-slate-800 text-xs font-mono text-slate-300">
                  <span className="text-slate-500 mr-1.5">Protocol:</span>
                  <span className="text-indigo-400 font-semibold">{result.protocol}</span>
                </div>
              )}
              {result.recommended_pattern && (
                <div className="px-3 py-1 rounded-lg bg-blue-950/50 border border-blue-800/60 text-xs font-mono text-blue-300">
                  <span className="text-blue-400 mr-1.5">Pattern:</span>
                  <span>{result.recommended_pattern}</span>
                </div>
              )}
            </div>
          </div>

          {/* Rationale explanation */}
          <div className="py-4">
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-1">
              Architectural Rationale & Rules
            </span>
            <p className="text-slate-200 text-sm leading-relaxed bg-[#0B0F17]/60 p-4 rounded-xl border border-slate-800/60">
              {result.reason}
            </p>
          </div>

          {/* Warnings */}
          {result.warnings && result.warnings.length > 0 && (
            <div className="mb-4 p-3.5 rounded-xl bg-amber-950/30 border border-amber-800/50 space-y-1.5">
              <div className="flex items-center gap-2 text-amber-400 text-xs font-semibold">
                <AlertTriangle className="w-4 h-4" />
                <span>Bottlenecks & Operational Constraints</span>
              </div>
              <ul className="text-xs text-amber-200/90 list-disc list-inside space-y-1">
                {result.warnings.map((w, idx) => (
                  <li key={idx}>{w}</li>
                ))}
              </ul>
            </div>
          )}

          {/* Limits Comparison Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
            <div className="p-3.5 rounded-xl bg-[#0B0F17]/80 border border-slate-800">
              <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
                <span className="flex items-center gap-1.5">
                  <Gauge className="w-3.5 h-3.5 text-blue-400" /> Max Pipeline QPS
                </span>
              </div>
              <div className="text-base font-bold text-white font-mono">
                {result.limits.effective_throughput_qps != null
                  ? `${result.limits.effective_throughput_qps.toLocaleString()} QPS`
                  : 'Unbounded / Dynamic'}
              </div>
              <span className="text-[11px] text-slate-500">
                Effective bottleneck throughput limit
              </span>
            </div>

            <div className="p-3.5 rounded-xl bg-[#0B0F17]/80 border border-slate-800">
              <div className="text-xs text-slate-400 mb-1">Source Limits ({sourceSlug})</div>
              <div className="text-xs font-mono text-slate-300 space-y-1">
                {Object.entries(result.limits.source_limits || {}).slice(0, 2).map(([k, v]) => (
                  <div key={k} className="flex justify-between">
                    <span className="text-slate-500">{k}:</span>
                    <span>{String(v)}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="p-3.5 rounded-xl bg-[#0B0F17]/80 border border-slate-800">
              <div className="text-xs text-slate-400 mb-1">Target Limits ({targetSlug})</div>
              <div className="text-xs font-mono text-slate-300 space-y-1">
                {Object.entries(result.limits.target_limits || {}).slice(0, 2).map(([k, v]) => (
                  <div key={k} className="flex justify-between">
                    <span className="text-slate-500">{k}:</span>
                    <span>{String(v)}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
