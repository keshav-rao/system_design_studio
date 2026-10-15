import { useState } from 'react'
import { X, Plus, AlertCircle } from 'lucide-react'

interface AdminComponentModalProps {
  isOpen: boolean
  onClose: () => void
  onCreated: () => void
}

const CATEGORIES = [
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

const LAYERS = ['edge', 'gateway', 'application', 'data', 'async', 'infra', 'observability']

export default function AdminComponentModal({ isOpen, onClose, onCreated }: AdminComponentModalProps) {
  const [slug, setSlug] = useState('')
  const [name, setName] = useState('')
  const [category, setCategory] = useState('compute')
  const [layer, setLayer] = useState('application')
  const [description, setDescription] = useState('')
  const [protocols, setProtocols] = useState('HTTP, HTTPS')
  const [maxQps, setMaxQps] = useState<number>(10000)
  const [latencyP99, setLatencyP99] = useState<number>(15)
  const [costModel, setCostModel] = useState('provisioned')
  const [costBaseUsd, setCostBaseUsd] = useState<number>(20)
  const [alternatives, setAlternatives] = useState('')
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState<string | null>(null)

  if (!isOpen) return null

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSubmitting(true)
    setError(null)

    const payload = {
      slug: slug.trim().toLowerCase(),
      name: name.trim(),
      category: category.trim().toLowerCase(),
      layer: layer.trim().toLowerCase(),
      description: description.trim(),
      protocols: protocols
        .split(',')
        .map((p) => p.trim())
        .filter(Boolean),
      limits: {
        max_throughput_qps: Number(maxQps),
        latency_p99_ms: Number(latencyP99),
      },
      failure_modes: [],
      cost_units: {
        model: costModel,
        unit: '$/month',
        base_monthly_usd: Number(costBaseUsd),
      },
      alternatives: alternatives
        .split(',')
        .map((a) => a.trim().toLowerCase())
        .filter(Boolean),
      is_active: true,
    }

    try {
      const res = await fetch('/api/v1/catalog/components', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })

      if (!res.ok) {
        const errData = await res.json()
        throw new Error(errData.detail || `HTTP Error ${res.status}`)
      }

      onCreated()
      onClose()
    } catch (err: any) {
      setError(err.message || 'Creation failed')
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm">
      <div className="bg-[#111726] border border-slate-800 rounded-2xl w-full max-w-xl max-h-[90vh] overflow-y-auto shadow-2xl">
        <div className="flex items-center justify-between p-6 border-b border-slate-800/80 sticky top-0 bg-[#111726] z-10">
          <div>
            <h3 className="text-lg font-bold text-white">Add Catalog Component</h3>
            <p className="text-xs text-slate-400">Register new architectural building block</p>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-4 text-sm">
          {error && (
            <div className="p-3 rounded-lg bg-rose-950/40 border border-rose-800/50 text-rose-300 text-xs flex items-center gap-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0" />
              <span>{error}</span>
            </div>
          )}

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Display Name *
              </label>
              <input
                required
                type="text"
                placeholder="e.g. ScyllaDB NoSQL"
                value={name}
                onChange={(e) => {
                  setName(e.target.value)
                  if (!slug) {
                    setSlug(e.target.value.toLowerCase().replace(/\s+/g, '-'))
                  }
                }}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Unique Slug *
              </label>
              <input
                required
                type="text"
                placeholder="e.g. scylladb"
                value={slug}
                onChange={(e) => setSlug(e.target.value)}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 font-mono text-xs focus:outline-none focus:border-blue-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Category *
              </label>
              <select
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
              >
                {CATEGORIES.map((cat) => (
                  <option key={cat} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Architectural Layer *
              </label>
              <select
                value={layer}
                onChange={(e) => setLayer(e.target.value)}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
              >
                {LAYERS.map((lay) => (
                  <option key={lay} value={lay}>
                    {lay}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-300 mb-1">
              Description *
            </label>
            <textarea
              required
              rows={2}
              placeholder="Detailed description of architectural role, constraints, and patterns..."
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-300 mb-1">
              Protocols (comma separated)
            </label>
            <input
              type="text"
              placeholder="e.g. HTTPS, gRPC, TCP"
              value={protocols}
              onChange={(e) => setProtocols(e.target.value)}
              className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Max QPS Throughput
              </label>
              <input
                type="number"
                value={maxQps}
                onChange={(e) => setMaxQps(Number(e.target.value))}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Latency p99 (ms)
              </label>
              <input
                type="number"
                value={latencyP99}
                onChange={(e) => setLatencyP99(Number(e.target.value))}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Cost Model
              </label>
              <input
                type="text"
                placeholder="provisioned, serverless, tier"
                value={costModel}
                onChange={(e) => setCostModel(e.target.value)}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-300 mb-1">
                Base Monthly Cost ($)
              </label>
              <input
                type="number"
                value={costBaseUsd}
                onChange={(e) => setCostBaseUsd(Number(e.target.value))}
                className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-300 mb-1">
              Alternative Slugs (comma separated)
            </label>
            <input
              type="text"
              placeholder="e.g. cassandra, dynamodb"
              value={alternatives}
              onChange={(e) => setAlternatives(e.target.value)}
              className="w-full bg-[#0B0F17] border border-slate-700/80 rounded-lg px-3 py-2 text-slate-100 focus:outline-none focus:border-blue-500"
            />
          </div>

          <div className="flex items-center justify-end gap-3 pt-4 border-t border-slate-800">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={submitting}
              className="px-5 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-medium transition-all shadow-md shadow-blue-500/20 flex items-center gap-2 disabled:opacity-50"
            >
              <Plus className="w-4 h-4" />
              {submitting ? 'Creating...' : 'Register Component'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
