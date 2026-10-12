import { useEffect, useState } from 'react'

interface HealthResponse {
  status: string
  app: string
  version: string
  environment: string
}

export default function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null)
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch('/api/v1/health')
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error ${res.status}`)
        return res.json()
      })
      .then((data) => {
        setHealth(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <div className="min-h-screen bg-[#0B0F17] text-slate-100 flex flex-col font-sans">
      {/* Header */}
      <header className="h-16 border-b border-slate-800/80 px-6 flex items-center justify-between bg-[#111726]/80 backdrop-blur-md sticky top-0 z-10">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-blue-600 to-indigo-500 flex items-center justify-center font-bold text-white shadow-lg shadow-blue-500/20">
            S
          </div>
          <div>
            <h1 className="text-base font-semibold text-white tracking-tight">System Design Studio</h1>
            <p className="text-xs text-slate-400">AI Architect • Evidence-Backed Engine</p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-900/80 border border-slate-800 text-xs">
            <span
              className={`w-2 h-2 rounded-full ${
                health?.status === 'ok' ? 'bg-emerald-400 shadow-sm shadow-emerald-400' : 'bg-amber-400 animate-pulse'
              }`}
            />
            <span className="text-slate-300">
              API Status: {loading ? 'Checking...' : health?.status === 'ok' ? 'Online (v0.1.0)' : error ? `Error: ${error}` : 'Offline'}
            </span>
          </div>
          <button className="px-3.5 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-md text-xs font-medium transition-all shadow-md shadow-blue-600/20">
            New Project
          </button>
        </div>
      </header>

      {/* Main Container */}
      <main className="flex-1 max-w-6xl w-full mx-auto p-8 flex flex-col justify-center">
        <div className="max-w-2xl mx-auto text-center space-y-6">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-950/60 border border-blue-800/60 text-blue-400 text-xs font-medium">
            <span className="w-1.5 h-1.5 rounded-full bg-blue-400"></span>
            Phase 0 Foundation Initialized
          </div>

          <h2 className="text-4xl font-bold tracking-tight text-white sm:text-5xl">
            Design & Simulate <br />
            <span className="bg-gradient-to-r from-blue-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
              High-Level Architectures
            </span>
          </h2>

          <p className="text-slate-400 text-base leading-relaxed">
            From interactive interview questions on cache, load balancers, and databases to real-time load testing simulations (1 to 100k users) and granular cost spreadsheets.
          </p>

          {/* Quick status card */}
          <div className="p-6 rounded-xl bg-[#131B2E] border border-slate-800 text-left space-y-3 shadow-xl">
            <div className="flex items-center justify-between text-xs text-slate-400 font-mono">
              <span>Environment Check</span>
              <span className="text-emerald-400">READY</span>
            </div>
            <div className="grid grid-cols-2 gap-4 text-xs font-mono">
              <div className="p-3 rounded-lg bg-[#0B0F17] border border-slate-800/80">
                <span className="text-slate-500 block">FastAPI Backend</span>
                <span className="text-slate-200 font-semibold">{health ? `${health.app} (${health.version})` : 'FastAPI 0.143'}</span>
              </div>
              <div className="p-3 rounded-lg bg-[#0B0F17] border border-slate-800/80">
                <span className="text-slate-500 block">Storage & Vectors</span>
                <span className="text-slate-200 font-semibold">Postgres 16 + Qdrant</span>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-800/60 py-4 px-6 text-center text-xs text-slate-500">
        System Design Studio • Phase 0 Foundation Complete
      </footer>
    </div>
  )
}
