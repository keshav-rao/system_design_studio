import { useEffect, useState } from 'react'
import {
  Server,
  Sparkles,
  Database,
  ShieldCheck,
  Zap,
} from 'lucide-react'
import { ComponentItem, ComponentListResponse } from './types/catalog'
import ComponentCatalog from './components/catalog/ComponentCatalog'
import CompatibilityChecker from './components/catalog/CompatibilityChecker'

interface HealthResponse {
  status: string
  app: string
  version: string
  environment: string
}

export default function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null)
  const [loadingHealth, setLoadingHealth] = useState<boolean>(true)
  const [activeTab, setActiveTab] = useState<'overview' | 'catalog' | 'compatibility'>('catalog')
  const [components, setComponents] = useState<ComponentItem[]>([])
  const [loadingCatalog, setLoadingCatalog] = useState<boolean>(true)

  const fetchHealth = () => {
    fetch('/api/v1/health')
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error ${res.status}`)
        return res.json()
      })
      .then((data) => {
        setHealth(data)
        setLoadingHealth(false)
      })
      .catch(() => {
        setLoadingHealth(false)
      })
  }

  const fetchCatalog = () => {
    setLoadingCatalog(true)
    fetch('/api/v1/catalog/components?limit=150')
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error ${res.status}`)
        return res.json()
      })
      .then((data: ComponentListResponse) => {
        setComponents(data.items || [])
        setLoadingCatalog(false)
      })
      .catch(() => {
        setLoadingCatalog(false)
      })
  }

  useEffect(() => {
    fetchHealth()
    fetchCatalog()
  }, [])

  return (
    <div className="min-h-screen bg-[#0B0F17] text-slate-100 flex flex-col font-sans">
      {/* Header */}
      <header className="h-16 border-b border-slate-800/80 px-6 flex items-center justify-between bg-[#111726]/80 backdrop-blur-md sticky top-0 z-30">
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => setActiveTab('overview')}>
            <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-blue-600 to-indigo-500 flex items-center justify-center font-bold text-white shadow-lg shadow-blue-500/20">
              S
            </div>
            <div>
              <h1 className="text-base font-semibold text-white tracking-tight">System Design Studio</h1>
              <p className="text-[11px] text-slate-400">AI Architect • Evidence-Backed Engine</p>
            </div>
          </div>

          {/* Navigation Tabs */}
          <nav className="hidden md:flex items-center gap-1 bg-[#0B0F17]/80 p-1 rounded-xl border border-slate-800">
            <button
              onClick={() => setActiveTab('overview')}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                activeTab === 'overview'
                  ? 'bg-slate-800 text-white shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Zap className="w-3.5 h-3.5" />
              Overview
            </button>
            <button
              onClick={() => setActiveTab('catalog')}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                activeTab === 'catalog'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Server className="w-3.5 h-3.5" />
              Component Catalog
              <span className="ml-1 px-1.5 py-0.2 rounded-full text-[10px] bg-slate-900 text-slate-300">
                {components.length}
              </span>
            </button>
            <button
              onClick={() => setActiveTab('compatibility')}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                activeTab === 'compatibility'
                  ? 'bg-indigo-600 text-white shadow-sm shadow-indigo-600/30'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <ShieldCheck className="w-3.5 h-3.5" />
              Compatibility Engine
            </button>
          </nav>
        </div>

        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-900/80 border border-slate-800 text-xs">
            <span
              className={`w-2 h-2 rounded-full ${
                health?.status === 'ok' ? 'bg-emerald-400 shadow-sm shadow-emerald-400' : 'bg-amber-400 animate-pulse'
              }`}
            />
            <span className="text-slate-300 font-mono text-[11px]">
              {loadingHealth ? 'Checking...' : health?.status === 'ok' ? `API Online (${health.version})` : 'Offline'}
            </span>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto p-6 md:p-8">
        {activeTab === 'overview' && (
          <div className="max-w-3xl mx-auto space-y-8 py-8 text-center">
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-950/60 border border-blue-800/60 text-blue-400 text-xs font-medium">
              <Sparkles className="w-3.5 h-3.5 text-blue-400" />
              Phase 2: Structured Component Catalog Initialized
            </div>

            <h2 className="text-4xl font-bold tracking-tight text-white sm:text-5xl">
              Evidence-Backed <br />
              <span className="bg-gradient-to-r from-blue-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
                System Design Studio
              </span>
            </h2>

            <p className="text-slate-400 text-base leading-relaxed">
              Design, validate, and simulate complex architectures grounded in catalog facts, verified failure modes, and deterministic connection compatibility rules.
            </p>

            {/* Phase Metrics */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-left">
              <div
                onClick={() => setActiveTab('catalog')}
                className="p-5 rounded-2xl bg-[#111726]/90 border border-slate-800/80 cursor-pointer hover:border-blue-500/50 transition-all shadow-xl"
              >
                <div className="flex items-center justify-between text-xs text-slate-400 mb-2">
                  <span className="font-semibold text-slate-300">Catalog Blocks</span>
                  <Server className="w-4 h-4 text-blue-400" />
                </div>
                <div className="text-3xl font-extrabold text-white font-mono">{components.length}</div>
                <p className="text-xs text-slate-400 mt-1">Production components with limits & failure modes</p>
              </div>

              <div
                onClick={() => setActiveTab('compatibility')}
                className="p-5 rounded-2xl bg-[#111726]/90 border border-slate-800/80 cursor-pointer hover:border-indigo-500/50 transition-all shadow-xl"
              >
                <div className="flex items-center justify-between text-xs text-slate-400 mb-2">
                  <span className="font-semibold text-slate-300">Compatibility Engine</span>
                  <ShieldCheck className="w-4 h-4 text-indigo-400" />
                </div>
                <div className="text-3xl font-extrabold text-white font-mono">Active</div>
                <p className="text-xs text-slate-400 mt-1">Real-time edge validation & bottleneck detection</p>
              </div>

              <div className="p-5 rounded-2xl bg-[#111726]/90 border border-slate-800/80 shadow-xl">
                <div className="flex items-center justify-between text-xs text-slate-400 mb-2">
                  <span className="font-semibold text-slate-300">Knowledge Base</span>
                  <Database className="w-4 h-4 text-emerald-400" />
                </div>
                <div className="text-3xl font-extrabold text-white font-mono">25 Sources</div>
                <p className="text-xs text-slate-400 mt-1">Hybrid dense + sparse Qdrant vectors indexed</p>
              </div>
            </div>

            <div className="pt-4 flex items-center justify-center gap-3">
              <button
                onClick={() => setActiveTab('catalog')}
                className="px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white font-medium rounded-xl transition-all shadow-lg shadow-blue-500/25 flex items-center gap-2"
              >
                <Server className="w-4 h-4" />
                Explore Component Catalog
              </button>
              <button
                onClick={() => setActiveTab('compatibility')}
                className="px-6 py-3 bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 font-medium rounded-xl transition-all flex items-center gap-2"
              >
                <ShieldCheck className="w-4 h-4" />
                Test Connections (A connects to B)
              </button>
            </div>
          </div>
        )}

        {activeTab === 'catalog' && (
          <ComponentCatalog
            components={components}
            loading={loadingCatalog}
            onRefresh={fetchCatalog}
          />
        )}

        {activeTab === 'compatibility' && (
          <CompatibilityChecker components={components} />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-800/60 py-4 px-6 text-center text-xs text-slate-500">
        System Design Studio • Phase 2 Structured Component Catalog Complete
      </footer>
    </div>
  )
}
