import { useEffect } from 'react'
import { Zap } from 'lucide-react'
import { useStudioStore } from './store/studioStore'
import { api } from './api/client'
import ProjectsPanel from './components/studio/ProjectsPanel'
import InterviewPanel from './components/studio/InterviewPanel'
import RequirementsReview from './components/studio/RequirementsReview'
import GeneratingScreen from './components/studio/GeneratingScreen'
import StudioLayout from './components/studio/StudioLayout'

// ── Health indicator (small) ─────────────────────────────────────────────────
function HealthDot() {
  const [status, setStatus] = [
    (window as any).__apiStatus ?? 'checking',
    (v: string) => { (window as any).__apiStatus = v },
  ]
  useEffect(() => {
    fetch('/api/v1/health')
      .then((r) => r.ok ? 'ok' : 'error')
      .then(setStatus)
      .catch(() => setStatus('error'))
  }, [])

  return (
    <div className="flex items-center gap-1.5 text-[11px] font-mono">
      <span
        className={`w-2 h-2 rounded-full ${
          status === 'ok'
            ? 'bg-emerald-400 shadow-sm shadow-emerald-400'
            : status === 'error'
            ? 'bg-rose-400 animate-pulse'
            : 'bg-amber-400 animate-pulse'
        }`}
      />
      <span className="text-slate-400">
        {status === 'ok' ? 'API Online' : status === 'error' ? 'API Offline' : '…'}
      </span>
    </div>
  )
}

// ── View labels for header ────────────────────────────────────────────────────
const VIEW_LABELS: Record<string, string> = {
  projects: 'Projects',
  interview: 'Requirements Interview',
  requirements: 'Review Requirements',
  generating: 'Generating…',
  canvas: 'Architecture Canvas',
}

export default function App() {
  const { view, catalog, setCatalog, catalogLoaded, activeProject } = useStudioStore()

  // Bootstrap: load catalog once on mount
  useEffect(() => {
    if (!catalogLoaded) {
      api.getComponents(150)
        .then((r) => setCatalog(r.items))
        .catch(() => {})
    }
  }, [])

  const isCanvas = view === 'canvas'

  return (
    <div className="min-h-screen bg-[#0B0F17] text-slate-100 flex flex-col font-sans">
      {/* ── Header ─────────────────────────────────────────────────────────── */}
      <header className="h-14 border-b border-slate-800/80 px-5 flex items-center justify-between bg-[#111726]/80 backdrop-blur-md sticky top-0 z-30 flex-shrink-0">
        <div className="flex items-center gap-3">
          <div className="w-7 h-7 rounded-lg bg-gradient-to-tr from-indigo-600 to-purple-500 flex items-center justify-center font-bold text-white text-sm shadow-lg shadow-indigo-500/20">
            S
          </div>
          <div>
            <span className="text-sm font-semibold text-white tracking-tight">System Design Studio</span>
            <span className="text-slate-600 mx-2">·</span>
            <span className="text-xs text-slate-400">{VIEW_LABELS[view] ?? view}</span>
          </div>
        </div>

        <div className="flex items-center gap-4">
          {activeProject && view !== 'projects' && (
            <div className="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900/80 border border-slate-800 text-xs">
              <Zap className="w-3 h-3 text-indigo-400" />
              <span className="text-slate-300 truncate max-w-[160px] font-medium">{activeProject.name}</span>
            </div>
          )}
          <HealthDot />
          {catalog.length > 0 && (
            <span className="hidden md:inline text-[11px] font-mono text-slate-500">
              {catalog.length} components
            </span>
          )}
        </div>
      </header>

      {/* ── Main ──────────────────────────────────────────────────────────── */}
      {isCanvas ? (
        // Canvas gets full remaining height with no padding
        <div className="flex-1 overflow-hidden flex flex-col" style={{ height: 'calc(100vh - 3.5rem)' }}>
          <StudioLayout />
        </div>
      ) : (
        <main className="flex-1 flex flex-col overflow-y-auto">
          {view === 'projects'     && <ProjectsPanel />}
          {view === 'interview'    && <InterviewPanel />}
          {view === 'requirements' && <RequirementsReview />}
          {view === 'generating'   && <GeneratingScreen />}
        </main>
      )}
    </div>
  )
}
