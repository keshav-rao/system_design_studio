import { useStudioStore } from '../../../store/studioStore'
import { ShieldCheck, AlertOctagon, Info, CheckCircle2, Clock } from 'lucide-react'

const SEVERITY_CONFIG = {
  error: {
    icon: <AlertOctagon className="w-3.5 h-3.5" />,
    label: 'Error',
    badgeClass: 'bg-rose-900/60 border-rose-700/50 text-rose-300',
    barClass: 'bg-rose-500',
    dotClass: 'bg-rose-400',
  },
  warning: {
    icon: <AlertOctagon className="w-3.5 h-3.5" />,
    label: 'Warning',
    badgeClass: 'bg-amber-900/60 border-amber-700/50 text-amber-300',
    barClass: 'bg-amber-400',
    dotClass: 'bg-amber-400',
  },
  info: {
    icon: <Info className="w-3.5 h-3.5" />,
    label: 'Info',
    badgeClass: 'bg-blue-900/60 border-blue-700/50 text-blue-300',
    barClass: 'bg-blue-400',
    dotClass: 'bg-blue-400',
  },
}

export default function ValidationTab() {
  const { activeDesign, canvasNodes, setSelectedNode } = useStudioStore()

  if (!activeDesign) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-6 text-center space-y-3">
        <ShieldCheck className="w-8 h-8 text-slate-600" />
        <p className="text-sm font-semibold text-slate-400">No design generated yet</p>
        <p className="text-xs text-slate-500">Generate an architecture plan to see validation results.</p>
      </div>
    )
  }

  const issues = activeDesign.validation_issues
  const errors = issues.filter((i) => i.severity === 'error')
  const warnings = issues.filter((i) => i.severity === 'warning')
  const infos = issues.filter((i) => i.severity === 'info')

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4 text-sm">
      {/* Summary banner */}
      <div
        className={`p-4 rounded-2xl border ${
          activeDesign.is_valid
            ? 'bg-emerald-950/40 border-emerald-700/50'
            : 'bg-rose-950/40 border-rose-700/50'
        }`}
      >
        <div className="flex items-center gap-2 mb-2">
          {activeDesign.is_valid ? (
            <CheckCircle2 className="w-5 h-5 text-emerald-400" />
          ) : (
            <AlertOctagon className="w-5 h-5 text-rose-400" />
          )}
          <span
            className={`font-bold text-sm ${
              activeDesign.is_valid ? 'text-emerald-300' : 'text-rose-300'
            }`}
          >
            {activeDesign.is_valid ? 'Design Valid' : 'Design Has Issues'}
          </span>
        </div>
        <div className="flex gap-4 text-xs font-mono mt-1">
          <span className="text-rose-400">{errors.length} errors</span>
          <span className="text-amber-400">{warnings.length} warnings</span>
          <span className="text-blue-400">{infos.length} info</span>
        </div>
        <div className="flex items-center gap-1.5 mt-2 text-[10px] text-slate-500">
          <Clock className="w-3 h-3" />
          {activeDesign.validation_issues.length > 0
            ? `${activeDesign.validation_issues.length} total issues found`
            : 'All rules passed'}
        </div>
      </div>

      {/* Issue list */}
      {issues.length === 0 ? (
        <div className="py-8 text-center space-y-2">
          <CheckCircle2 className="w-10 h-10 text-emerald-500/50 mx-auto" />
          <p className="text-xs text-slate-400">All validation rules passed 🎉</p>
        </div>
      ) : (
        <div className="space-y-3">
          {['error', 'warning', 'info'].map((sev) => {
            const group = issues.filter((i) => i.severity === sev)
            if (group.length === 0) return null
            const cfg = SEVERITY_CONFIG[sev as keyof typeof SEVERITY_CONFIG]
            return (
              <div key={sev}>
                <div className="flex items-center gap-2 mb-2">
                  <div className={`w-2 h-2 rounded-full ${cfg.dotClass}`} />
                  <span className="text-[11px] font-semibold uppercase tracking-wide text-slate-400">
                    {cfg.label}s ({group.length})
                  </span>
                </div>
                <div className="space-y-2">
                  {group.map((issue, idx) => (
                    <div
                      key={idx}
                      className="p-3 rounded-xl bg-[#0B0F17] border border-slate-800/60 space-y-2"
                    >
                      <div className="flex items-start gap-2">
                        <span className={`px-2 py-0.5 rounded text-[10px] font-mono border ${cfg.badgeClass} flex-shrink-0 mt-0.5`}>
                          {issue.rule_id}
                        </span>
                      </div>
                      <p className="text-xs text-slate-200 leading-relaxed">{issue.message}</p>
                      {issue.suggestion && (
                        <p className="text-[11px] text-emerald-400 leading-relaxed">
                          <span className="text-slate-500">Suggestion: </span>
                          {issue.suggestion}
                        </p>
                      )}
                      {issue.node_ids.length > 0 && (
                        <div className="flex flex-wrap gap-1">
                          {issue.node_ids.map((nid) => {
                            const n = canvasNodes.find((cn) => cn.id === nid)
                            return (
                              <button
                                key={nid}
                                onClick={() => setSelectedNode(nid)}
                                className="px-2 py-0.5 rounded text-[10px] font-mono bg-slate-800 border border-slate-700 text-slate-300 hover:text-white hover:border-blue-500 transition-colors"
                              >
                                {n?.slug ?? nid}
                              </button>
                            )
                          })}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )
          })}
        </div>
      )}

      {/* Rules executed */}
      {activeDesign.validation_issues !== undefined && (
        <details className="group mt-2">
          <summary className="cursor-pointer text-[11px] text-slate-500 hover:text-slate-300 transition-colors list-none flex items-center gap-1">
            <span className="group-open:rotate-90 inline-block transition-transform">▶</span>
            Rules executed ({activeDesign.validation_issues.length > 0 ? '12' : '12'})
          </summary>
          <div className="mt-2 flex flex-wrap gap-1.5">
            {[
              'valid-edge-refs', 'no-self-loops', 'no-duplicate-edges',
              'no-dangling-nodes', 'no-spof', 'no-edge-to-db',
              'gateway-required', 'cache-before-db', 'async-processing',
              'data-store-required', 'multi-region', 'throughput-bottleneck',
            ].map((r) => (
              <span key={r} className="px-2 py-0.5 rounded text-[10px] font-mono bg-slate-800 border border-slate-700 text-slate-400">
                {r}
              </span>
            ))}
          </div>
        </details>
      )}
    </div>
  )
}
