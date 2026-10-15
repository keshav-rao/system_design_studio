import { useState } from 'react'
import {
  Search,
  Filter,
  Zap,
  DollarSign,
  AlertOctagon,
  Plus,
  RefreshCw,
  Server,
  ChevronDown,
  ChevronUp,
} from 'lucide-react'
import { ComponentItem } from '../../types/catalog'
import AdminComponentModal from './AdminComponentModal'

interface ComponentCatalogProps {
  components: ComponentItem[]
  loading: boolean
  onRefresh: () => void
}

const CATEGORIES = [
  'all',
  'cdn',
  'gateway',
  'compute',
  'cache',
  'database',
  'queue',
  'streaming',
  'storage',
  'auth',
  'search',
  'notification',
  'observability',
  'middleware',
  'workflow',
  'analytics',
]

export default function ComponentCatalog({
  components,
  loading,
  onRefresh,
}: ComponentCatalogProps) {
  const [search, setSearch] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('all')
  const [expandedId, setExpandedId] = useState<string | null>(null)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [seeding, setSeeding] = useState(false)
  const [seedMessage, setSeedMessage] = useState<string | null>(null)

  const handleSeed = async () => {
    setSeeding(true)
    setSeedMessage(null)
    try {
      const res = await fetch('/api/v1/catalog/seed?force=true', { method: 'POST' })
      if (!res.ok) throw new Error('Seeding failed')
      const data = await res.json()
      setSeedMessage(`Seeded ${data.components_total} components and ${data.edges_total} compatibility edges!`)
      onRefresh()
    } catch (err: any) {
      setSeedMessage(`Error: ${err.message}`)
    } finally {
      setSeeding(false)
    }
  }

  const filteredComponents = components.filter((c) => {
    const matchesCat =
      selectedCategory === 'all' || c.category.toLowerCase() === selectedCategory.toLowerCase()
    const matchesSearch =
      !search ||
      c.name.toLowerCase().includes(search.toLowerCase()) ||
      c.slug.toLowerCase().includes(search.toLowerCase()) ||
      c.description.toLowerCase().includes(search.toLowerCase())
    return matchesCat && matchesSearch
  })

  return (
    <div className="space-y-6">
      {/* Top Bar */}
      <div className="p-6 rounded-2xl bg-[#111726]/90 border border-slate-800/80 shadow-2xl backdrop-blur-md flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-medium mb-2">
            <Server className="w-3.5 h-3.5" />
            Structured Architecture Catalog
          </div>
          <h2 className="text-xl font-bold text-white tracking-tight">
            Component Building Blocks ({components.length} Total)
          </h2>
          <p className="text-slate-400 text-sm mt-0.5">
            Hardware limits, failure modes, cost models, and alternative options for every architectural component.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={handleSeed}
            disabled={seeding}
            className="px-3.5 py-2 bg-slate-900 hover:bg-slate-800 border border-slate-700/80 text-slate-200 text-xs font-medium rounded-xl transition-all flex items-center gap-2"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${seeding ? 'animate-spin' : ''}`} />
            {seeding ? 'Seeding...' : 'Reset & Seed Catalog'}
          </button>
          <button
            onClick={() => setIsModalOpen(true)}
            className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold rounded-xl transition-all shadow-md shadow-blue-500/20 flex items-center gap-2"
          >
            <Plus className="w-4 h-4" />
            Add Component
          </button>
        </div>
      </div>

      {seedMessage && (
        <div className="p-3.5 rounded-xl bg-blue-950/40 border border-blue-800/50 text-blue-200 text-xs font-medium">
          {seedMessage}
        </div>
      )}

      {/* Filters & Search */}
      <div className="flex flex-col md:flex-row gap-4">
        {/* Search */}
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search components by name, slug, or keywords (e.g. postgres, redis, kafka)..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full bg-[#111726] border border-slate-800 rounded-xl pl-10 pr-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-blue-500"
          />
        </div>
      </div>

      {/* Category Pills */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-thin">
        <Filter className="w-4 h-4 text-slate-400 flex-shrink-0" />
        {CATEGORIES.map((cat) => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            className={`px-3 py-1 rounded-full text-xs font-medium whitespace-nowrap transition-all border ${
              selectedCategory === cat
                ? 'bg-blue-600 border-blue-500 text-white shadow-sm shadow-blue-500/30'
                : 'bg-[#111726] hover:bg-slate-850 border-slate-800 text-slate-400 hover:text-slate-200'
            }`}
          >
            {cat.toUpperCase()}
          </button>
        ))}
      </div>

      {/* Component Grid */}
      {loading ? (
        <div className="py-20 text-center text-slate-400">Loading catalog components...</div>
      ) : filteredComponents.length === 0 ? (
        <div className="py-20 text-center text-slate-500 bg-[#111726]/40 rounded-2xl border border-slate-800/60">
          No components found matching your search.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredComponents.map((c) => {
            const isExpanded = expandedId === c.id
            return (
              <div
                key={c.id}
                className="p-5 rounded-2xl bg-[#111726]/80 border border-slate-800/80 hover:border-slate-700/80 transition-all flex flex-col justify-between shadow-lg"
              >
                <div>
                  {/* Card Header */}
                  <div className="flex items-start justify-between gap-2 mb-2">
                    <div>
                      <h3 className="font-semibold text-white text-base leading-snug">{c.name}</h3>
                      <span className="text-xs font-mono text-slate-400">{c.slug}</span>
                    </div>
                    <div className="flex items-center gap-1.5 flex-shrink-0">
                      <span className="px-2 py-0.5 rounded-md text-[10px] font-mono uppercase bg-blue-950/80 border border-blue-800/50 text-blue-300">
                        {c.category}
                      </span>
                      <span className="px-2 py-0.5 rounded-md text-[10px] font-mono uppercase bg-slate-800 text-slate-300">
                        {c.layer}
                      </span>
                    </div>
                  </div>

                  {/* Description */}
                  <p className="text-xs text-slate-300 line-clamp-3 mb-4 leading-relaxed">
                    {c.description}
                  </p>

                  {/* Limits summary chips */}
                  <div className="space-y-1.5 mb-4">
                    <span className="text-[11px] font-semibold text-slate-400 flex items-center gap-1">
                      <Zap className="w-3 h-3 text-amber-400" /> Key Architectural Limits:
                    </span>
                    <div className="flex flex-wrap gap-1.5 text-[11px] font-mono">
                      {c.limits?.max_throughput_qps && (
                        <span className="px-2 py-0.5 rounded bg-[#0B0F17] border border-slate-800 text-slate-300">
                          {c.limits.max_throughput_qps.toLocaleString()} QPS
                        </span>
                      )}
                      {c.limits?.latency_p99_ms && (
                        <span className="px-2 py-0.5 rounded bg-[#0B0F17] border border-slate-800 text-slate-300">
                          {c.limits.latency_p99_ms}ms p99
                        </span>
                      )}
                      {c.limits?.connection_limit && (
                        <span className="px-2 py-0.5 rounded bg-[#0B0F17] border border-slate-800 text-slate-300">
                          {c.limits.connection_limit.toLocaleString()} conns
                        </span>
                      )}
                    </div>
                  </div>

                  {/* Protocols */}
                  {c.protocols && c.protocols.length > 0 && (
                    <div className="mb-4">
                      <span className="text-[11px] font-semibold text-slate-400 block mb-1">
                        Protocols:
                      </span>
                      <div className="flex flex-wrap gap-1">
                        {c.protocols.map((p) => (
                          <span
                            key={p}
                            className="px-2 py-0.5 rounded text-[10px] bg-slate-900 border border-slate-800 text-indigo-300 font-mono"
                          >
                            {p}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Cost Units */}
                  {c.cost_units && (
                    <div className="p-2.5 rounded-xl bg-[#0B0F17]/90 border border-slate-800/80 mb-3 text-xs">
                      <div className="flex items-center justify-between text-slate-300 font-mono">
                        <span className="flex items-center gap-1 text-slate-400 text-[11px]">
                          <DollarSign className="w-3 h-3 text-emerald-400" /> Base Cost:
                        </span>
                        <span className="font-semibold text-emerald-400">
                          ${c.cost_units.base_monthly_usd ?? 0}/mo
                        </span>
                      </div>
                      {c.cost_units.free_tier && (
                        <span className="text-[10px] text-slate-400 line-clamp-1 block mt-1">
                          Free tier: {c.cost_units.free_tier}
                        </span>
                      )}
                    </div>
                  )}

                  {/* Failure modes toggle */}
                  {c.failure_modes && c.failure_modes.length > 0 && (
                    <div>
                      <button
                        onClick={() => setExpandedId(isExpanded ? null : c.id)}
                        className="text-[11px] text-blue-400 hover:text-blue-300 flex items-center gap-1 font-medium transition-colors"
                      >
                        <AlertOctagon className="w-3 h-3" />
                        {isExpanded
                          ? 'Hide Failure Modes'
                          : `View ${c.failure_modes.length} Failure Modes`}
                        {isExpanded ? (
                          <ChevronUp className="w-3 h-3" />
                        ) : (
                          <ChevronDown className="w-3 h-3" />
                        )}
                      </button>

                      {isExpanded && (
                        <div className="mt-2.5 space-y-2 p-3 rounded-xl bg-[#0B0F17] border border-slate-800/90 text-[11px]">
                          {c.failure_modes.map((fm, idx) => (
                            <div key={idx} className="border-b border-slate-800/60 pb-1.5 last:border-0 last:pb-0">
                              <span className="font-semibold text-rose-300 block">{fm.mode}</span>
                              <p className="text-slate-400 mt-0.5">{fm.impact}</p>
                              <p className="text-emerald-400/90 mt-0.5">
                                <span className="font-medium text-slate-400">Mitigation: </span>
                                {fm.mitigation}
                              </p>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>

                {/* Alternatives footer */}
                {c.alternatives && c.alternatives.length > 0 && (
                  <div className="pt-3 border-t border-slate-800/60 mt-3 flex items-center justify-between text-[11px] text-slate-500 font-mono">
                    <span>Alternatives:</span>
                    <span className="text-slate-400 line-clamp-1">{c.alternatives.join(', ')}</span>
                  </div>
                )}
              </div>
            )
          })}
        </div>
      )}

      {/* Admin Add Component Modal */}
      <AdminComponentModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onCreated={onRefresh}
      />
    </div>
  )
}
