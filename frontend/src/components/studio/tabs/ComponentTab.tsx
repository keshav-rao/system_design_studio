import { useStudioStore } from '../../../store/studioStore'
import type { ComponentItem } from '../../../types/catalog'
import {
  Server,
  Zap,
  Link2,
  AlertTriangle,
  X,
  ArrowLeftRight,
  Plus,
  Minus,
  Settings2,
  ChevronDown,
  ChevronUp,
} from 'lucide-react'
import { useState } from 'react'

const CATEGORY_COLOR: Record<string, string> = {
  cdn: 'bg-sky-900/60 text-sky-300 border-sky-700/50',
  gateway: 'bg-violet-900/60 text-violet-300 border-violet-700/50',
  compute: 'bg-blue-900/60 text-blue-300 border-blue-700/50',
  cache: 'bg-amber-900/60 text-amber-300 border-amber-700/50',
  database: 'bg-emerald-900/60 text-emerald-300 border-emerald-700/50',
  queue: 'bg-orange-900/60 text-orange-300 border-orange-700/50',
  streaming: 'bg-rose-900/60 text-rose-300 border-rose-700/50',
  storage: 'bg-teal-900/60 text-teal-300 border-teal-700/50',
  auth: 'bg-purple-900/60 text-purple-300 border-purple-700/50',
  search: 'bg-indigo-900/60 text-indigo-300 border-indigo-700/50',
  notification: 'bg-pink-900/60 text-pink-300 border-pink-700/50',
  observability: 'bg-slate-700/60 text-slate-300 border-slate-600/50',
  middleware: 'bg-lime-900/60 text-lime-300 border-lime-700/50',
  workflow: 'bg-cyan-900/60 text-cyan-300 border-cyan-700/50',
  analytics: 'bg-fuchsia-900/60 text-fuchsia-300 border-fuchsia-700/50',
}

interface ReplaceModalProps {
  nodeId: string
  currentSlug: string
  catalog: ComponentItem[]
  onClose: () => void
}

function ReplaceModal({ nodeId, currentSlug, catalog, onClose }: ReplaceModalProps) {
  const { replaceNode, canvasNodes } = useStudioStore()
  const [search, setSearch] = useState('')
  const current = canvasNodes.find((n) => n.id === nodeId)
  if (!current) return null

  const filtered = catalog.filter(
    (c) =>
      c.slug !== currentSlug &&
      (c.name.toLowerCase().includes(search.toLowerCase()) ||
        c.slug.toLowerCase().includes(search.toLowerCase()))
  )

  const doReplace = (item: ComponentItem) => {
    replaceNode(nodeId, {
      ...current,
      slug: item.slug,
      category: item.category,
      layer: item.layer,
      protocols: item.protocols,
      limits: item.limits,
    })
    onClose()
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
      <div className="w-full max-w-md bg-[#111726] border border-slate-700 rounded-2xl shadow-2xl">
        <div className="flex items-center justify-between p-4 border-b border-slate-800">
          <h3 className="text-sm font-semibold text-white">Replace Component</h3>
          <button onClick={onClose} className="text-slate-400 hover:text-white">
            <X className="w-4 h-4" />
          </button>
        </div>
        <div className="p-3">
          <input
            type="text"
            placeholder="Search catalog…"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full bg-[#0B0F17] border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            autoFocus
          />
        </div>
        <div className="max-h-72 overflow-y-auto divide-y divide-slate-800/60">
          {filtered.slice(0, 30).map((item) => (
            <button
              key={item.slug}
              onClick={() => doReplace(item)}
              className="w-full flex items-center gap-3 px-4 py-2.5 hover:bg-slate-800/60 transition-colors text-left"
            >
              <span
                className={`px-2 py-0.5 rounded text-[10px] font-mono border ${CATEGORY_COLOR[item.category] ?? 'bg-slate-800 text-slate-300 border-slate-700'}`}
              >
                {item.category}
              </span>
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-white">{item.name}</p>
                <p className="text-[10px] text-slate-400 font-mono">{item.slug}</p>
              </div>
            </button>
          ))}
          {filtered.length === 0 && (
            <p className="py-8 text-center text-xs text-slate-500">No components found.</p>
          )}
        </div>
      </div>
    </div>
  )
}

export default function ComponentTab() {
  const {
    selectedNodeId,
    canvasNodes,
    canvasEdges,
    catalog,
    removeNode,
    updateNodeConfig,
    setSelectedNode,
  } = useStudioStore()
  const [showReplace, setShowReplace] = useState(false)
  const [showLimits, setShowLimits] = useState(false)

  const node = canvasNodes.find((n) => n.id === selectedNodeId)
  const catalogItem = node ? catalog.find((c) => c.slug === node.slug) : null
  const connectedEdges = node
    ? canvasEdges.filter((e) => e.source_id === node.id || e.target_id === node.id)
    : []

  if (!selectedNodeId || !node) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-6 text-center space-y-3">
        <div className="w-12 h-12 rounded-2xl bg-slate-800/80 flex items-center justify-center">
          <Server className="w-6 h-6 text-slate-500" />
        </div>
        <p className="text-sm font-semibold text-slate-400">No component selected</p>
        <p className="text-xs text-slate-500 leading-relaxed">
          Click any node on the canvas to inspect its properties,
          limits, failure modes, and connections.
        </p>
      </div>
    )
  }

  const catColor = CATEGORY_COLOR[node.category] ?? 'bg-slate-700/60 text-slate-300 border-slate-600/50'

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4 text-sm">
      {/* Header */}
      <div className="flex items-start justify-between gap-2">
        <div className="flex-1 min-w-0">
          <h3 className="font-bold text-white text-base leading-snug">
            {catalogItem?.name ?? node.slug}
          </h3>
          <p className="text-xs font-mono text-slate-400 mt-0.5">{node.slug}</p>
        </div>
        <button
          onClick={() => { removeNode(node.id); setSelectedNode(null) }}
          className="flex-shrink-0 p-1.5 rounded-lg hover:bg-rose-900/40 text-slate-500 hover:text-rose-400 transition-all"
          title="Remove from canvas"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {/* Badges */}
      <div className="flex flex-wrap gap-1.5">
        <span className={`px-2 py-0.5 rounded-md text-[10px] font-mono border ${catColor}`}>
          {node.category}
        </span>
        <span className="px-2 py-0.5 rounded-md text-[10px] font-mono bg-slate-800 border border-slate-700 text-slate-300">
          {node.layer}
        </span>
        <span className="px-2 py-0.5 rounded-md text-[10px] font-mono bg-slate-800 border border-slate-700 text-slate-300">
          ×{node.replicas} replica{node.replicas !== 1 ? 's' : ''}
        </span>
      </div>

      {/* Description */}
      {catalogItem?.description && (
        <p className="text-xs text-slate-400 leading-relaxed border-l-2 border-slate-700 pl-3">
          {catalogItem.description}
        </p>
      )}

      {/* Protocols */}
      {node.protocols.length > 0 && (
        <div>
          <p className="text-[11px] font-semibold text-slate-400 mb-1.5 flex items-center gap-1">
            <Link2 className="w-3 h-3" /> Protocols
          </p>
          <div className="flex flex-wrap gap-1">
            {node.protocols.map((p) => (
              <span key={p} className="px-2 py-0.5 rounded text-[10px] font-mono bg-indigo-950/60 border border-indigo-800/50 text-indigo-300">
                {p}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Limits */}
      {Object.keys(node.limits).length > 0 && (
        <div>
          <button
            onClick={() => setShowLimits(!showLimits)}
            className="text-[11px] font-semibold text-slate-400 flex items-center gap-1 mb-1.5 hover:text-slate-200 transition-colors"
          >
            <Zap className="w-3 h-3 text-amber-400" /> Operational Limits
            {showLimits ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
          </button>
          {showLimits && (
            <div className="space-y-1 text-xs">
              {Object.entries(node.limits).map(([k, v]) => (
                <div key={k} className="flex items-center justify-between px-2.5 py-1.5 rounded-lg bg-[#0B0F17] border border-slate-800/60">
                  <span className="font-mono text-slate-400">{k.replace(/_/g, ' ')}</span>
                  <span className="font-mono font-semibold text-amber-300">{String(v)}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Replicas control */}
      <div>
        <p className="text-[11px] font-semibold text-slate-400 mb-1.5 flex items-center gap-1">
          <Settings2 className="w-3 h-3" /> Replica Count
        </p>
        <div className="flex items-center gap-2">
          <button
            onClick={() => updateNodeConfig(node.id, { _replicas: Math.max(1, node.replicas - 1) })}
            className="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 flex items-center justify-center text-slate-300 transition-colors"
          >
            <Minus className="w-3 h-3" />
          </button>
          <span className="font-mono text-white font-semibold text-sm min-w-[2rem] text-center">
            {node.replicas}
          </span>
          <button
            onClick={() => updateNodeConfig(node.id, { _replicas: node.replicas + 1 })}
            className="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 flex items-center justify-center text-slate-300 transition-colors"
          >
            <Plus className="w-3 h-3" />
          </button>
        </div>
      </div>

      {/* Connected edges */}
      {connectedEdges.length > 0 && (
        <div>
          <p className="text-[11px] font-semibold text-slate-400 mb-1.5 flex items-center gap-1">
            <ArrowLeftRight className="w-3 h-3" /> Connections ({connectedEdges.length})
          </p>
          <div className="space-y-1">
            {connectedEdges.map((e, idx) => {
              const isSource = e.source_id === node.id
              const otherId = isSource ? e.target_id : e.source_id
              const otherNode = canvasNodes.find((n) => n.id === otherId)
              return (
                <div key={idx} className="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-[#0B0F17] border border-slate-800/60 text-xs">
                  <span className={`text-[10px] ${isSource ? 'text-blue-400' : 'text-purple-400'}`}>
                    {isSource ? '→' : '←'}
                  </span>
                  <span className="font-mono text-slate-300">{otherNode?.slug ?? otherId}</span>
                  {e.protocol && (
                    <span className="ml-auto text-[10px] font-mono text-slate-500">{e.protocol}</span>
                  )}
                </div>
              )
            })}
          </div>
        </div>
      )}

      {/* Failure modes */}
      {catalogItem && catalogItem.failure_modes.length > 0 && (
        <div>
          <p className="text-[11px] font-semibold text-rose-400 mb-1.5 flex items-center gap-1">
            <AlertTriangle className="w-3 h-3" /> Failure Modes
          </p>
          <div className="space-y-2">
            {catalogItem.failure_modes.map((fm: any, idx: number) => (
              <div key={idx} className="p-2.5 rounded-xl bg-[#0B0F17] border border-rose-900/40 text-xs">
                <p className="font-semibold text-rose-300">{fm.mode}</p>
                <p className="text-slate-400 mt-0.5">{fm.impact}</p>
                <p className="text-emerald-400 mt-1"><span className="text-slate-500">Fix: </span>{fm.mitigation}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Alternatives */}
      {catalogItem && catalogItem.alternatives.length > 0 && (
        <div>
          <p className="text-[11px] font-semibold text-slate-400 mb-1.5">Alternatives</p>
          <div className="flex flex-wrap gap-1">
            {catalogItem.alternatives.map((alt) => (
              <span key={alt} className="px-2 py-0.5 rounded text-[10px] font-mono bg-slate-800 border border-slate-700 text-slate-400">
                {alt}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Replace action */}
      <div className="pt-2 border-t border-slate-800/60">
        <button
          onClick={() => setShowReplace(true)}
          className="w-full flex items-center justify-center gap-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 hover:text-white text-xs font-semibold transition-all"
        >
          <ArrowLeftRight className="w-3.5 h-3.5" />
          Replace Component
        </button>
      </div>

      {showReplace && node && (
        <ReplaceModal
          nodeId={node.id}
          currentSlug={node.slug}
          catalog={catalog}
          onClose={() => setShowReplace(false)}
        />
      )}
    </div>
  )
}
