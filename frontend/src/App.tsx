import { useEffect, useState } from 'react'
import {
  Zap,
  Server,
  ShieldCheck,
  LayoutDashboard,
  FolderKanban,
  PenTool,
  Key,
} from 'lucide-react'
import { useStudioStore, type AppView } from './store/studioStore'
import { api } from './api/client'
import ProjectsPanel from './components/studio/ProjectsPanel'
import InterviewPanel from './components/studio/InterviewPanel'
import RequirementsReview from './components/studio/RequirementsReview'
import GeneratingScreen from './components/studio/GeneratingScreen'
import StudioLayout from './components/studio/StudioLayout'
import OverviewPanel from './components/studio/OverviewPanel'
import ComponentCatalog from './components/catalog/ComponentCatalog'
import CompatibilityChecker from './components/catalog/CompatibilityChecker'
import WhiteboardCanvas from './components/whiteboard/WhiteboardCanvas'
import ApiKeysModal from './components/studio/ApiKeysModal'

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
      <span className="text-slate-400 hidden sm:inline">
        {status === 'ok' ? 'API Online' : status === 'error' ? 'API Offline' : '…'}
      </span>
    </div>
  )
}

export default function App() {
  const {
    view,
    setView,
    catalog,
    setCatalog,
    catalogLoaded,
    activeProject,
    canvasNodes,
    loadTemplate,
  } = useStudioStore()

  const [showApiKeys, setShowApiKeys] = useState(false)

  // ── URL Synchronization (SPA Client-side routing) ───────────────────────────
  useEffect(() => {
    // Read initial route from URL
    const rawPath = window.location.pathname.replace(/^\/+/, '').split('/')[0]
    const validViews: AppView[] = [
      'overview',
      'canvas',
      'whiteboard',
      'compatibility',
      'catalog',
      'projects',
      'interview',
      'requirements',
      'generating',
    ]
    if (rawPath && validViews.includes(rawPath as AppView)) {
      setView(rawPath as AppView)
    } else if (!rawPath || rawPath === '') {
      window.history.replaceState(null, '', '/overview')
      setView('overview')
    }

    // Handle browser Back / Forward buttons
    const handlePopState = () => {
      const p = window.location.pathname.replace(/^\/+/, '').split('/')[0]
      if (p && validViews.includes(p as AppView)) {
        setView(p as AppView)
      } else {
        setView('overview')
      }
    }

    window.addEventListener('popstate', handlePopState)
    return () => window.removeEventListener('popstate', handlePopState)
  }, [])

  // Sync view changes to browser URL bar
  useEffect(() => {
    const currentPath = window.location.pathname.replace(/^\/+/, '').split('/')[0]
    if (currentPath !== view) {
      window.history.pushState(null, '', `/${view}`)
    }
  }, [view])

  // Bootstrap: load catalog once on mount
  const fetchCatalog = () => {
    api.getComponents(150)
      .then((r) => setCatalog(r.items))
      .catch(() => {})
  }

  useEffect(() => {
    if (!catalogLoaded) {
      fetchCatalog()
    }
  }, [])

  const isCanvas = view === 'canvas'
  const isWhiteboard = view === 'whiteboard'

  return (
    <div className={`w-full ${isCanvas || isWhiteboard ? 'h-screen overflow-hidden' : 'min-h-screen'} bg-[#0B0F17] text-slate-100 flex flex-col font-sans`}>
      {/* ── Top Header Bar ─────────────────────────────────────────────────── */}
      <header className="h-16 border-b border-slate-800/80 px-4 sm:px-6 flex items-center justify-between bg-[#111726]/80 backdrop-blur-md sticky top-0 z-30 flex-shrink-0">
        <div className="flex items-center gap-4 lg:gap-6">
          {/* Brand Logo & Subtitle */}
          <div
            className="flex items-center gap-3 cursor-pointer select-none group"
            onClick={() => setView('overview')}
          >
            <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-indigo-600 via-blue-600 to-purple-500 flex items-center justify-center font-bold text-white shadow-lg shadow-indigo-500/25 group-hover:scale-105 transition-transform">
              S
            </div>
            <div>
              <h1 className="text-sm font-semibold text-white tracking-tight leading-none group-hover:text-indigo-200 transition-colors">
                System Design Studio
              </h1>
              <p className="text-[11px] text-slate-400 font-medium mt-0.5">
                AI Architect • Evidence-Backed Engine
              </p>
            </div>
          </div>

          {/* Navigation Bar: Overview, Canva Template, Compatibility Engine, Catalog, Projects */}
          <nav className="hidden md:flex items-center gap-1 bg-[#0B0F17]/90 p-1 rounded-xl border border-slate-800/90 shadow-inner">
            <button
              onClick={() => setView('overview')}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                view === 'overview'
                  ? 'bg-slate-800 text-white shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40'
              }`}
            >
              <Zap className="w-3.5 h-3.5 text-amber-400" />
              Overview
            </button>

            <button
              onClick={() => {
                if (canvasNodes.length === 0) {
                  loadTemplate('ecommerce')
                }
                setView('canvas')
              }}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                view === 'canvas'
                  ? 'bg-indigo-600 text-white shadow-sm shadow-indigo-600/30 font-semibold'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40'
              }`}
            >
              <LayoutDashboard className="w-3.5 h-3.5 text-indigo-400" />
              Canva Template
              {canvasNodes.length > 0 && (
                <span className="ml-1 px-1.5 py-0.2 rounded-full text-[10px] bg-slate-900/90 text-indigo-300 border border-indigo-500/30">
                  {canvasNodes.length}
                </span>
              )}
            </button>

            <button
              onClick={() => setView('compatibility')}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                view === 'compatibility'
                  ? 'bg-indigo-600 text-white shadow-sm shadow-indigo-600/30 font-semibold'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40'
              }`}
            >
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
              Compatibility Engine
            </button>

            <button
              onClick={() => setView('catalog')}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                view === 'catalog'
                  ? 'bg-blue-600 text-white shadow-sm shadow-blue-600/30 font-semibold'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40'
              }`}
            >
              <Server className="w-3.5 h-3.5 text-blue-400" />
              Component Catalog
              {catalog.length > 0 && (
                <span className="ml-1 px-1.5 py-0.2 rounded-full text-[10px] bg-slate-900 text-slate-300">
                  {catalog.length}
                </span>
              )}
            </button>

            <button
              onClick={() => setView('projects')}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                ['projects', 'interview', 'requirements', 'generating'].includes(view)
                  ? 'bg-purple-600 text-white shadow-sm shadow-purple-600/30 font-semibold'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40'
              }`}
            >
              <FolderKanban className="w-3.5 h-3.5 text-purple-400" />
              Studio Projects
            </button>
          </nav>
        </div>

        {/* Right Info Controls & Canvas (Whiteboard) Navigation */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* API Keys & Routes Button */}
          <button
            onClick={() => setShowApiKeys(true)}
            className="px-2.5 py-1.5 rounded-xl text-xs font-medium transition-all flex items-center gap-1.5 bg-[#0E1526]/90 hover:bg-[#162038] text-slate-300 hover:text-white border border-slate-700/80 hover:border-indigo-500/60 shadow-sm"
            title="Configure API Keys & View Page URLs (/overview, /canvas, ...)"
          >
            <Key className="w-3.5 h-3.5 text-amber-400" />
            <span className="hidden md:inline">API Keys &amp; Routes</span>
          </button>

          {/* Top Right Bar: Canvas (Whiteboard) Feature Button */}
          <button
            onClick={() => setView('whiteboard')}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition-all flex items-center gap-2 border shadow-sm ${
              view === 'whiteboard'
                ? 'bg-gradient-to-r from-indigo-600 via-indigo-500 to-purple-600 text-white border-indigo-400/60 shadow-indigo-600/40 ring-2 ring-indigo-500/30'
                : 'bg-[#0E1526]/90 hover:bg-[#162038] text-slate-200 hover:text-white border-slate-700/80 hover:border-indigo-500/60'
            }`}
            title="Open Canvas (Whiteboard) - SystemSketcher Technical Analysis"
          >
            <PenTool className={`w-3.5 h-3.5 ${view === 'whiteboard' ? 'text-white' : 'text-indigo-400'}`} />
            <span>Canvas (Whiteboard)</span>
            <span className={`text-[10px] font-mono px-1.5 py-0.2 rounded hidden sm:inline ${
              view === 'whiteboard' ? 'bg-black/30 text-indigo-100' : 'bg-indigo-950 text-indigo-300 border border-indigo-800/40'
            }`}>
              SystemSketcher
            </span>
          </button>

          {activeProject && view !== 'projects' && (
            <div className="hidden xl:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900/80 border border-slate-800 text-xs">
              <Zap className="w-3 h-3 text-indigo-400" />
              <span className="text-slate-300 truncate max-w-[140px] font-medium">{activeProject.name}</span>
            </div>
          )}
          <HealthDot />
        </div>
      </header>

      {/* ── Main View Content ──────────────────────────────────────────────── */}
      {isCanvas ? (
        // Canvas gets full remaining height with no padding
        <div className="flex-1 w-full min-h-0 h-[calc(100vh-4rem)] flex flex-col overflow-hidden">
          <StudioLayout />
        </div>
      ) : isWhiteboard ? (
        // Whiteboard Canvas gets full remaining height with its own zoom/pan whiteboard surface
        <div className="flex-1 w-full min-h-0 h-[calc(100vh-4rem)] flex flex-col overflow-hidden">
          <WhiteboardCanvas />
        </div>
      ) : (
        <main className="flex-1 flex flex-col overflow-y-auto">
          {view === 'overview' && <OverviewPanel />}

          {view === 'compatibility' && (
            <div className="max-w-7xl w-full mx-auto p-6 md:p-8">
              <CompatibilityChecker components={catalog} />
            </div>
          )}

          {view === 'catalog' && (
            <div className="max-w-7xl w-full mx-auto p-6 md:p-8">
              <ComponentCatalog
                components={catalog}
                loading={!catalogLoaded}
                onRefresh={fetchCatalog}
              />
            </div>
          )}

          {view === 'projects'     && <ProjectsPanel />}
          {view === 'interview'    && <InterviewPanel />}
          {view === 'requirements' && <RequirementsReview />}
          {view === 'generating'   && <GeneratingScreen />}
        </main>
      )}

      {/* API Keys & Routes Modal */}
      {showApiKeys && (
        <ApiKeysModal isOpen={showApiKeys} onClose={() => setShowApiKeys(false)} />
      )}
    </div>
  )
}
