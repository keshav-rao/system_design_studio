import { useStudioStore } from '../../../store/studioStore'
import { DollarSign, TrendingUp, AlertTriangle } from 'lucide-react'

interface CostRow {
  slug: string
  name: string
  category: string
  replicas: number
  baseMonthly: number
  model: string
  unit: string
  freeTier?: string | null
}

export default function CostTab() {
  const { canvasNodes, catalog } = useStudioStore()

  const rows: CostRow[] = canvasNodes.map((node) => {
    const item = catalog.find((c) => c.slug === node.slug)
    const cu = item?.cost_units as any
    return {
      slug: node.slug,
      name: item?.name ?? node.slug,
      category: node.category,
      replicas: node.replicas,
      baseMonthly: typeof cu?.base_monthly_usd === 'number' ? cu.base_monthly_usd : 0,
      model: cu?.model ?? 'provisioned',
      unit: cu?.unit ?? '—',
      freeTier: cu?.free_tier ?? null,
    }
  })

  const totalMonthly = rows.reduce((sum, r) => sum + r.baseMonthly * r.replicas, 0)
  const highCost = rows.filter((r) => r.baseMonthly * r.replicas > 500)

  const CATEGORY_EMOJIS: Record<string, string> = {
    cdn: '🌐',
    gateway: '🔀',
    compute: '⚙️',
    cache: '⚡',
    database: '🗄️',
    queue: '📬',
    streaming: '🌊',
    storage: '💾',
    auth: '🔐',
    search: '🔍',
    notification: '🔔',
    observability: '📊',
    middleware: '🔧',
    workflow: '🔄',
    analytics: '📈',
  }

  if (canvasNodes.length === 0) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-6 text-center space-y-3">
        <DollarSign className="w-8 h-8 text-slate-600" />
        <p className="text-sm font-semibold text-slate-400">No components on canvas</p>
        <p className="text-xs text-slate-500">Add components to estimate monthly costs.</p>
      </div>
    )
  }

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4 text-sm">
      {/* Total */}
      <div className="p-4 rounded-2xl bg-gradient-to-br from-emerald-950/60 to-emerald-900/20 border border-emerald-700/40">
        <div className="flex items-center gap-2 mb-1">
          <DollarSign className="w-4 h-4 text-emerald-400" />
          <span className="text-xs font-semibold text-emerald-300">Estimated Monthly</span>
        </div>
        <div className="text-3xl font-extrabold text-white font-mono">
          ${totalMonthly.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}
          <span className="text-sm text-slate-400 font-normal ml-1">/mo</span>
        </div>
        <p className="text-[10px] text-slate-500 mt-1">
          Base costs only — excludes egress, support plans, and premium tiers.
        </p>
      </div>

      {/* High-cost warnings */}
      {highCost.length > 0 && (
        <div className="p-3 rounded-xl bg-amber-950/40 border border-amber-700/40">
          <div className="flex items-center gap-1.5 text-amber-400 text-xs font-semibold mb-1">
            <AlertTriangle className="w-3.5 h-3.5" />
            High-cost components
          </div>
          <div className="space-y-0.5">
            {highCost.map((r) => (
              <p key={r.slug} className="text-[11px] text-amber-300/80">
                {r.name} — ${(r.baseMonthly * r.replicas).toFixed(0)}/mo
              </p>
            ))}
          </div>
        </div>
      )}

      {/* Per-component breakdown */}
      <div>
        <div className="flex items-center gap-2 mb-2">
          <TrendingUp className="w-3.5 h-3.5 text-slate-400" />
          <h4 className="text-xs font-semibold text-white">Per-Component Breakdown</h4>
        </div>
        <div className="space-y-2">
          {rows
            .slice()
            .sort((a, b) => b.baseMonthly * b.replicas - a.baseMonthly * a.replicas)
            .map((r) => {
              const rowTotal = r.baseMonthly * r.replicas
              const pct = totalMonthly > 0 ? (rowTotal / totalMonthly) * 100 : 0
              return (
                <div
                  key={r.slug}
                  className="p-3 rounded-xl bg-[#0B0F17] border border-slate-800/60 space-y-2"
                >
                  <div className="flex items-center justify-between gap-2">
                    <div className="flex items-center gap-2 min-w-0">
                      <span className="text-base">{CATEGORY_EMOJIS[r.category] ?? '📦'}</span>
                      <div className="min-w-0">
                        <p className="text-xs font-semibold text-white truncate">{r.name}</p>
                        <p className="text-[10px] font-mono text-slate-500">{r.slug} × {r.replicas}</p>
                      </div>
                    </div>
                    <span className="font-mono text-sm font-bold text-emerald-400 flex-shrink-0">
                      ${rowTotal.toFixed(0)}
                    </span>
                  </div>

                  {/* Mini bar */}
                  <div className="h-1 bg-slate-800 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-emerald-500/70 rounded-full transition-all"
                      style={{ width: `${pct}%` }}
                    />
                  </div>

                  <div className="flex items-center justify-between text-[10px] text-slate-500 font-mono">
                    <span>{r.model} • {r.unit}</span>
                    <span>{pct.toFixed(1)}% of total</span>
                  </div>

                  {r.freeTier && (
                    <p className="text-[10px] text-blue-400">✓ Free tier: {r.freeTier}</p>
                  )}
                </div>
              )
            })}
        </div>
      </div>

      <p className="text-[10px] text-slate-600 text-center pb-2">
        Costs are estimates from catalog seed data and may differ from provider pricing.
      </p>
    </div>
  )
}
