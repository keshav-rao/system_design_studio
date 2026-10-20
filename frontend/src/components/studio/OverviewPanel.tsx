import {
  Sparkles,
  Server,
  ShieldCheck,
  LayoutDashboard,
  FolderKanban,
  ArrowRight,
} from 'lucide-react'
import { useStudioStore } from '../../store/studioStore'
import { ARCH_TEMPLATES } from '../../data/archTemplates'

export default function OverviewPanel() {
  const { catalog, canvasNodes, setView, loadTemplate } = useStudioStore()

  return (
    <div className="max-w-6xl w-full mx-auto px-6 py-10 space-y-12">
      {/* ── Hero ─────────────────────────────────────────────────────────── */}
      <div className="max-w-3xl mx-auto space-y-6 text-center">
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-950/80 border border-indigo-700/60 text-indigo-300 text-xs font-medium shadow-lg shadow-indigo-950/40">
          <Sparkles className="w-3.5 h-3.5 text-indigo-400 animate-pulse" />
          AI Architect • Evidence-Backed Engine
        </div>

        <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-white leading-[1.15]">
          Evidence-Backed <br />
          <span className="bg-gradient-to-r from-blue-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
            System Design Studio
          </span>
        </h1>

        <p className="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl mx-auto">
          Design, validate, and simulate complex cloud architectures grounded in production catalog facts, verified failure modes, and deterministic connection compatibility rules.
        </p>

        {/* Primary CTA Buttons */}
        <div className="pt-2 flex flex-wrap items-center justify-center gap-3">
          <button
            onClick={() => {
              if (canvasNodes.length === 0) {
                loadTemplate('ecommerce')
              }
              setView('canvas')
            }}
            className="px-6 py-3 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm rounded-xl transition-all shadow-xl shadow-indigo-600/30 flex items-center gap-2 border border-indigo-500/50 hover:scale-[1.02] active:scale-[0.98]"
          >
            <LayoutDashboard className="w-4 h-4 text-white" />
            Open Canva Template
            <ArrowRight className="w-4 h-4 text-indigo-200" />
          </button>

          <button
            onClick={() => setView('compatibility')}
            className="px-5 py-3 bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 font-medium text-sm rounded-xl transition-all flex items-center gap-2 hover:border-slate-600"
          >
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            Compatibility Engine
          </button>

          <button
            onClick={() => setView('catalog')}
            className="px-5 py-3 bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 font-medium text-sm rounded-xl transition-all flex items-center gap-2 hover:border-slate-600"
          >
            <Server className="w-4 h-4 text-blue-400" />
            Component Catalog ({catalog.length || 38})
          </button>
        </div>
      </div>

      {/* ── Feature Cards Grid ────────────────────────────────────────────── */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Card 1: Canva Template */}
        <div
          onClick={() => {
            if (canvasNodes.length === 0) loadTemplate('ecommerce')
            setView('canvas')
          }}
          className="group p-5 rounded-2xl bg-[#111726]/90 border border-slate-800/80 cursor-pointer hover:border-indigo-500/60 transition-all duration-200 shadow-xl hover:shadow-indigo-500/10 flex flex-col justify-between"
        >
          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="w-9 h-9 rounded-xl bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400 group-hover:scale-110 transition-transform">
                <LayoutDashboard className="w-4 h-4" />
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-indigo-950/80 text-indigo-300 border border-indigo-800/60">
                Live Studio
              </span>
            </div>
            <h3 className="text-base font-semibold text-white group-hover:text-indigo-200 transition-colors">
              Canva Template
            </h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              Interactive node graph canvas with automated layers, custom connection wires, and inspector tabs.
            </p>
          </div>
          <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs font-medium text-indigo-400 group-hover:text-indigo-300">
            <span>{canvasNodes.length > 0 ? `${canvasNodes.length} nodes placed` : '3 Templates ready'}</span>
            <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>

        {/* Card 2: Compatibility Engine */}
        <div
          onClick={() => setView('compatibility')}
          className="group p-5 rounded-2xl bg-[#111726]/90 border border-slate-800/80 cursor-pointer hover:border-emerald-500/60 transition-all duration-200 shadow-xl hover:shadow-emerald-500/10 flex flex-col justify-between"
        >
          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="w-9 h-9 rounded-xl bg-emerald-600/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
                <ShieldCheck className="w-4 h-4" />
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-800/60">
                Deterministic
              </span>
            </div>
            <h3 className="text-base font-semibold text-white group-hover:text-emerald-200 transition-colors">
              Compatibility Engine
            </h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              Test A-to-B connections, protocol alignment, latency mismatch, and verified anti-patterns in real time.
            </p>
          </div>
          <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs font-medium text-emerald-400 group-hover:text-emerald-300">
            <span>Real-time check</span>
            <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>

        {/* Card 3: Component Catalog */}
        <div
          onClick={() => setView('catalog')}
          className="group p-5 rounded-2xl bg-[#111726]/90 border border-slate-800/80 cursor-pointer hover:border-blue-500/60 transition-all duration-200 shadow-xl hover:shadow-blue-500/10 flex flex-col justify-between"
        >
          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="w-9 h-9 rounded-xl bg-blue-600/20 border border-blue-500/30 flex items-center justify-center text-blue-400 group-hover:scale-110 transition-transform">
                <Server className="w-4 h-4" />
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-blue-950/80 text-blue-300 border border-blue-800/60">
                Structured
              </span>
            </div>
            <h3 className="text-base font-semibold text-white group-hover:text-blue-200 transition-colors">
              Component Catalog
            </h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              Production building blocks with QPS throughput limits, P99 latency, cost models, and failure modes.
            </p>
          </div>
          <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs font-medium text-blue-400 group-hover:text-blue-300">
            <span>{catalog.length || 38} blocks loaded</span>
            <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>

        {/* Card 4: Studio Projects / AI Planner */}
        <div
          onClick={() => setView('projects')}
          className="group p-5 rounded-2xl bg-[#111726]/90 border border-slate-800/80 cursor-pointer hover:border-purple-500/60 transition-all duration-200 shadow-xl hover:shadow-purple-500/10 flex flex-col justify-between"
        >
          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="w-9 h-9 rounded-xl bg-purple-600/20 border border-purple-500/30 flex items-center justify-center text-purple-400 group-hover:scale-110 transition-transform">
                <FolderKanban className="w-4 h-4" />
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-purple-950/80 text-purple-300 border border-purple-800/60">
                RAG Engine
              </span>
            </div>
            <h3 className="text-base font-semibold text-white group-hover:text-purple-200 transition-colors">
              Studio Projects
            </h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              Automated requirement interview and multi-tier architectural generation with LangGraph and Qdrant.
            </p>
          </div>
          <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs font-medium text-purple-400 group-hover:text-purple-300">
            <span>Interview wizard</span>
            <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>
      </div>

      {/* ── Canva Templates Showcase ─────────────────────────────────────── */}
      <div className="p-6 rounded-2xl bg-[#111726]/60 border border-slate-800/90 shadow-xl space-y-5">
        <div className="flex items-center justify-between flex-wrap gap-2">
          <div>
            <h2 className="text-lg font-semibold text-white flex items-center gap-2">
              <LayoutDashboard className="w-5 h-5 text-indigo-400" />
              Canva Architecture Templates
            </h2>
            <p className="text-xs text-slate-400 mt-0.5">
              Launch pre-validated, evidence-backed production designs instantly onto the interactive canvas.
            </p>
          </div>
          <button
            onClick={() => {
              loadTemplate('ecommerce')
              setView('canvas')
            }}
            className="px-3.5 py-1.5 bg-indigo-600/20 hover:bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 text-xs font-semibold rounded-lg transition-colors flex items-center gap-1.5"
          >
            Launch Default Template
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {Object.values(ARCH_TEMPLATES).map((tmpl) => (
            <div
              key={tmpl.id}
              className="p-4 rounded-xl bg-[#0B0F17]/80 border border-slate-800 hover:border-indigo-500/50 transition-all flex flex-col justify-between group"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-indigo-300 font-medium">
                    {tmpl.badge}
                  </span>
                  <span className="text-[11px] font-mono text-slate-500">
                    {tmpl.nodes.length} nodes · {tmpl.edges.length} edges
                  </span>
                </div>
                <h4 className="text-sm font-semibold text-white group-hover:text-indigo-200 transition-colors">
                  {tmpl.name}
                </h4>
                <p className="text-xs text-slate-400 mt-1 line-clamp-2 leading-relaxed">
                  {tmpl.description}
                </p>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-800/60 flex items-center justify-between">
                <div className="flex -space-x-1 overflow-hidden">
                  {tmpl.nodes.slice(0, 4).map((n) => (
                    <span
                      key={n.id}
                      className="inline-block px-1.5 py-0.5 rounded text-[9px] font-mono bg-slate-800 text-slate-300 border border-slate-700"
                    >
                      {n.category}
                    </span>
                  ))}
                </div>
                <button
                  onClick={() => {
                    loadTemplate(tmpl.id)
                    setView('canvas')
                  }}
                  className="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg transition-colors shadow-sm"
                >
                  Load Template
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
