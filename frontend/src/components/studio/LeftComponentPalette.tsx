import { useState } from 'react'
import {
  Search,
  Plus,
  Loader2,
  CheckCircle2,
  AlertCircle,
  X,
  Layers,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react'
import { useStudioStore } from '../../store/studioStore'
import { api } from '../../api/client'
import type { ComponentItem } from '../../types/catalog'
import type { DesignNode } from '../../types/api'

interface LeftComponentPaletteProps {
  isOpen: boolean
  onToggle: () => void
  onAddComponent?: (item: ComponentItem) => void
}

const CATEGORY_TABS = [
  { id: 'all', label: 'All' },
  { id: 'gateway', label: 'Gateway' },
  { id: 'cdn', label: 'CDN' },
  { id: 'compute', label: 'Compute' },
  { id: 'database', label: 'Database' },
  { id: 'cache', label: 'Cache' },
  { id: 'queue', label: 'Queue' },
  { id: 'storage', label: 'Storage' },
  { id: 'observability', label: 'Observability' },
]

const CAT_COLORS: Record<string, { bg: string; border: string; text: string }> = {
  cdn:          { bg: '#0c1d2e', border: '#0ea5e9', text: '#7dd3fc' },
  gateway:      { bg: '#1a0e2e', border: '#7c3aed', text: '#c4b5fd' },
  compute:      { bg: '#0e1a2e', border: '#3b82f6', text: '#93c5fd' },
  cache:        { bg: '#2e1e07', border: '#d97706', text: '#fcd34d' },
  database:     { bg: '#052e1a', border: '#10b981', text: '#6ee7b7' },
  queue:        { bg: '#2e1007', border: '#ea580c', text: '#fdba74' },
  streaming:    { bg: '#2e0a0a', border: '#ef4444', text: '#fca5a5' },
  storage:      { bg: '#052e2e', border: '#14b8a6', text: '#5eead4' },
  auth:         { bg: '#1a0e2e', border: '#9333ea', text: '#d8b4fe' },
  search:       { bg: '#0a0e2e', border: '#6366f1', text: '#a5b4fc' },
  notification: { bg: '#2e0a1a', border: '#ec4899', text: '#f9a8d4' },
  observability:{ bg: '#111827', border: '#6b7280', text: '#d1d5db' },
}

export default function LeftComponentPalette({ isOpen, onToggle, onAddComponent }: LeftComponentPaletteProps) {
  const { catalog, addNode, canvasNodes } = useStudioStore()
  const [search, setSearch] = useState('')
  const [selectedCat, setSelectedCat] = useState('all')
  const [checking, setChecking] = useState<string | null>(null)
  const [checkResult, setCheckResult] = useState<{ slug: string; ok: boolean; reason: string } | null>(null)

  const filtered = catalog.filter((c) => {
    if (!c.is_active) return false
    const matchCat = selectedCat === 'all' || c.category === selectedCat
    const query = search.toLowerCase()
    const matchSearch =
      !query ||
      c.name.toLowerCase().includes(query) ||
      c.slug.toLowerCase().includes(query) ||
      c.category.toLowerCase().includes(query)
    return matchCat && matchSearch
  })

  const handleAdd = async (item: ComponentItem) => {
    if (onAddComponent) {
      onAddComponent(item)
      return
    }

    if (canvasNodes.length > 0) {
      setChecking(item.slug)
      const firstNode = canvasNodes[0]
      try {
        const res = await api.checkCompatibility(firstNode.slug, item.slug)
        setCheckResult({ slug: item.slug, ok: res.compatible, reason: res.reason })
        if (!res.compatible) {
          setTimeout(() => setCheckResult(null), 3000)
        }
      } catch {
        // ignore
      } finally {
        setChecking(null)
      }
    }

    const newNode: DesignNode = {
      id: `${item.slug}-${Date.now()}`,
      slug: item.slug,
      category: item.category,
      layer: item.layer,
      replicas: 1,
      protocols: item.protocols,
      limits: item.limits,
      config: {},
      label: item.name,
    }
    addNode(newNode)
  }

  const handleDragStart = (e: React.DragEvent, item: ComponentItem) => {
    e.dataTransfer.setData('application/reactflow-component', JSON.stringify(item))
    e.dataTransfer.effectAllowed = 'move'
  }

  if (!isOpen) {
    return (
      <div className="absolute top-4 left-4 z-20">
        <button
          onClick={onToggle}
          className="flex items-center gap-2 px-3 py-2 rounded-xl bg-[#111726]/95 hover:bg-[#1a233b] text-slate-200 border border-slate-700/80 shadow-2xl backdrop-blur-md text-xs font-semibold transition-all hover:scale-105 hover:border-indigo-500/60"
          title="Open Component Library (Left Toolbar)"
        >
          <Layers className="w-4 h-4 text-indigo-400" />
          <span>Components</span>
          <span className="text-[10px] bg-indigo-500/20 text-indigo-300 font-mono px-1.5 py-0.2 rounded border border-indigo-500/30">
            {catalog.length || 41}
          </span>
          <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
        </button>
      </div>
    )
  }

  return (
    <aside className="absolute inset-y-0 left-0 w-72 sm:w-80 bg-[#0E1424]/95 border-r border-slate-800 flex flex-col z-20 shadow-2xl backdrop-blur-xl transition-all duration-200">
      {/* Header */}
      <div className="p-3.5 border-b border-slate-800/80 flex items-center justify-between flex-shrink-0 bg-[#0A0F1D]/80">
        <div className="flex items-center gap-2">
          <div className="w-7 h-7 rounded-lg bg-indigo-600/20 border border-indigo-500/40 flex items-center justify-center text-indigo-400">
            <Layers className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-xs font-bold text-white tracking-tight flex items-center gap-1.5">
              Component Palette
              <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                {filtered.length}
              </span>
            </h3>
            <p className="text-[10px] text-slate-400 font-medium">Drag or click to place on canvas</p>
          </div>
        </div>
        <button
          onClick={onToggle}
          className="p-1.5 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-white transition-colors"
          title="Collapse Component Palette"
        >
          <ChevronLeft className="w-4 h-4" />
        </button>
      </div>

      {/* Search Input */}
      <div className="p-3 border-b border-slate-800/60 flex-shrink-0">
        <div className="relative">
          <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search 830+ components…"
            className="w-full bg-[#080C16] border border-slate-700/80 rounded-xl pl-8 pr-7 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 font-sans"
          />
          {search && (
            <button
              onClick={() => setSearch('')}
              className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
            >
              <X className="w-3 h-3" />
            </button>
          )}
        </div>

        {/* Category Pills */}
        <div className="flex items-center gap-1 overflow-x-auto pt-2 pb-0.5 no-scrollbar">
          {CATEGORY_TABS.map((cat) => (
            <button
              key={cat.id}
              onClick={() => setSelectedCat(cat.id)}
              className={`px-2 py-1 rounded-md text-[10px] font-medium whitespace-nowrap transition-all ${
                selectedCat === cat.id
                  ? 'bg-indigo-600 text-white font-semibold shadow-sm shadow-indigo-600/30'
                  : 'bg-slate-900/90 text-slate-400 hover:text-slate-200 border border-slate-800 hover:border-slate-700'
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>
      </div>

      {/* Compatibility Feedback Toast */}
      {checkResult && (
        <div
          className={`mx-3 mt-2 p-2 rounded-lg text-[10px] font-mono flex items-center gap-2 border flex-shrink-0 animate-in fade-in duration-150 ${
            checkResult.ok
              ? 'bg-emerald-950/80 border-emerald-700/60 text-emerald-300'
              : 'bg-rose-950/80 border-rose-700/60 text-rose-300'
          }`}
        >
          {checkResult.ok ? (
            <CheckCircle2 className="w-3.5 h-3.5 flex-shrink-0 text-emerald-400" />
          ) : (
            <AlertCircle className="w-3.5 h-3.5 flex-shrink-0 text-rose-400" />
          )}
          <span className="truncate">{checkResult.reason}</span>
        </div>
      )}

      {/* Component Cards List */}
      <div className="flex-1 overflow-y-auto divide-y divide-slate-800/40 p-2 space-y-1.5 min-h-0">
        {filtered.length === 0 ? (
          <div className="p-8 text-center space-y-2">
            <p className="text-xs text-slate-400 font-semibold">No components match query</p>
            <p className="text-[11px] text-slate-500">Try searching for AWS, Redis, Kafka, or Database</p>
          </div>
        ) : (
          filtered.map((item) => {
            const colors = CAT_COLORS[item.category] ?? {
              bg: '#111827',
              border: '#4b5563',
              text: '#d1d5db',
            }
            const isCheckingItem = checking === item.slug
            return (
              <div
                key={item.slug}
                draggable
                onDragStart={(e) => handleDragStart(e, item)}
                onClick={() => handleAdd(item)}
                className="group p-2.5 rounded-xl border border-slate-800/80 hover:border-indigo-500/60 bg-[#0C111E]/90 hover:bg-[#12192C] transition-all cursor-grab active:cursor-grabbing shadow-sm hover:shadow-md flex items-center justify-between gap-2"
                title="Click to add or drag onto canvas"
              >
                <div className="flex items-center gap-2.5 min-w-0">
                  <div
                    className="w-2.5 h-2.5 rounded-full flex-shrink-0 shadow-sm"
                    style={{ background: colors.border }}
                  />
                  <div className="min-w-0">
                    <p className="text-xs font-semibold text-white group-hover:text-indigo-200 truncate transition-colors">
                      {item.name}
                    </p>
                    <div className="flex items-center gap-1.5 mt-0.5">
                      <span
                        className="text-[9px] font-mono uppercase px-1 py-0.2 rounded"
                        style={{ background: colors.border + '25', color: colors.text }}
                      >
                        {item.category}
                      </span>
                      <span className="text-[9px] font-mono text-slate-500">
                        {item.layer}
                      </span>
                    </div>
                  </div>
                </div>

                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation()
                    handleAdd(item)
                  }}
                  disabled={isCheckingItem}
                  className="p-1 rounded-lg bg-slate-900 border border-slate-700/80 group-hover:bg-indigo-600 group-hover:border-indigo-500 text-slate-400 group-hover:text-white transition-all flex-shrink-0"
                  title="Add to canvas"
                >
                  {isCheckingItem ? (
                    <Loader2 className="w-3.5 h-3.5 animate-spin text-indigo-400" />
                  ) : (
                    <Plus className="w-3.5 h-3.5" />
                  )}
                </button>
              </div>
            )
          })
        )}
      </div>

      {/* Footer Info */}
      <div className="p-3 border-t border-slate-800/80 bg-[#080C16] flex items-center justify-between text-[10px] text-slate-500 flex-shrink-0 font-mono">
        <span>💡 Whiteboard Canvas Layout</span>
        <span>Miro / Canva Style</span>
      </div>
    </aside>
  )
}
