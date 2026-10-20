import { useEffect, useState } from 'react'
import {
  FolderOpen,
  Plus,
  Loader2,
  ChevronRight,
  Sparkles,
  Clock,
  Layers,
  Server,
} from 'lucide-react'
import { useStudioStore } from '../../store/studioStore'
import { api } from '../../api/client'
import type { ProjectResponse } from '../../types/api'

export default function ProjectsPanel() {
  const {
    projects,
    setProjects,
    selectProject,
    setView,
    catalog,
    resetInterview,
    setActiveDesign,
    setCanvasFromDesign,
  } = useStudioStore()

  const [loading, setLoading] = useState(false)
  const [creating, setCreating] = useState(false)
  const [newName, setNewName] = useState('')
  const [newDesc, setNewDesc] = useState('')
  const [showForm, setShowForm] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [loadingDesign, setLoadingDesign] = useState<string | null>(null)

  useEffect(() => {
    setLoading(true)
    api.listProjects()
      .then(setProjects)
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [])

  const createProject = async () => {
    if (newName.trim().length < 2) return
    setCreating(true)
    setError(null)
    try {
      const p = await api.createProject({ name: newName.trim(), description: newDesc.trim() || null })
      setProjects([p, ...projects])
      setNewName('')
      setNewDesc('')
      setShowForm(false)
      handleOpenProject(p, true)
    } catch (e: any) {
      setError(e.message)
    } finally {
      setCreating(false)
    }
  }

  const handleOpenProject = async (p: ProjectResponse, isNew = false) => {
    resetInterview()
    selectProject(p)

    if (!isNew && p.versions_count > 0) {
      // Load the latest design directly to canvas
      setLoadingDesign(p.id)
      try {
        const design = await api.getLatestDesign(p.id)
        setActiveDesign(design)
        setCanvasFromDesign(design)
        setView('canvas')
      } catch {
        // If loading fails, go to interview
        setView('interview')
      } finally {
        setLoadingDesign(null)
      }
    } else {
      setView('interview')
    }
  }

  return (
    <div className="flex-1 flex flex-col items-center justify-center p-8">
      <div className="max-w-2xl w-full space-y-8">
        {/* Hero */}
        <div className="text-center space-y-3">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-indigo-950/60 border border-indigo-700/50 text-indigo-300 text-xs font-medium">
            <Sparkles className="w-3.5 h-3.5" />
            Phase 5 — Interactive Architecture Canvas
          </div>
          <h1 className="text-4xl font-extrabold text-white tracking-tight">
            System Design Studio
          </h1>
          <p className="text-slate-400 text-sm leading-relaxed max-w-lg mx-auto">
            Go from idea → AI-driven interview → validated architecture diagram
            with evidence-backed, catalog-grounded components.
          </p>

          {/* Stats bar */}
          <div className="flex items-center justify-center gap-6 pt-2">
            <div className="text-center">
              <p className="text-2xl font-bold text-white font-mono">{catalog.length}</p>
              <p className="text-[11px] text-slate-500">Catalog components</p>
            </div>
            <div className="w-px h-8 bg-slate-800" />
            <div className="text-center">
              <p className="text-2xl font-bold text-white font-mono">12</p>
              <p className="text-[11px] text-slate-500">Validator rules</p>
            </div>
            <div className="w-px h-8 bg-slate-800" />
            <div className="text-center">
              <p className="text-2xl font-bold text-white font-mono">{projects.length}</p>
              <p className="text-[11px] text-slate-500">Projects</p>
            </div>
          </div>
        </div>

        {/* New project form */}
        {showForm ? (
          <div className="p-5 rounded-2xl bg-[#111726] border border-indigo-800/50 space-y-3 shadow-xl">
            <h3 className="text-sm font-semibold text-white">New Project</h3>
            <input
              type="text"
              placeholder="Project name (e.g. Tinder Clone Architecture)"
              value={newName}
              onChange={(e) => setNewName(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && createProject()}
              className="w-full bg-[#0B0F17] border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
              autoFocus
            />
            <input
              type="text"
              placeholder="Description (optional)"
              value={newDesc}
              onChange={(e) => setNewDesc(e.target.value)}
              className="w-full bg-[#0B0F17] border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
            {error && (
              <p className="text-xs text-rose-400">{error}</p>
            )}
            <div className="flex gap-2">
              <button
                onClick={() => { setShowForm(false); setError(null) }}
                className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-all"
              >
                Cancel
              </button>
              <button
                onClick={createProject}
                disabled={creating || newName.trim().length < 2}
                className="flex-1 flex items-center justify-center gap-2 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white text-sm font-semibold transition-all"
              >
                {creating ? <Loader2 className="w-4 h-4 animate-spin" /> : <Plus className="w-4 h-4" />}
                {creating ? 'Creating…' : 'Create & Start Interview'}
              </button>
            </div>
          </div>
        ) : (
          <button
            onClick={() => setShowForm(true)}
            className="w-full flex items-center justify-center gap-2 py-4 rounded-2xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white font-semibold text-sm transition-all shadow-lg shadow-indigo-500/25 border border-indigo-500/30"
          >
            <Plus className="w-4 h-4" />
            New Architecture Project
          </button>
        )}

        {/* Project list */}
        <div>
          <div className="flex items-center gap-2 mb-4">
            <FolderOpen className="w-4 h-4 text-slate-400" />
            <h2 className="text-sm font-semibold text-white">Existing Projects</h2>
          </div>

          {loading ? (
            <div className="py-10 text-center text-slate-500 text-sm flex items-center justify-center gap-2">
              <Loader2 className="w-4 h-4 animate-spin" />
              Loading projects…
            </div>
          ) : projects.length === 0 ? (
            <div className="py-10 text-center rounded-2xl border border-dashed border-slate-800 text-slate-500 text-sm">
              No projects yet. Create your first one above.
            </div>
          ) : (
            <div className="space-y-2">
              {projects.map((p) => (
                <button
                  key={p.id}
                  onClick={() => handleOpenProject(p)}
                  disabled={loadingDesign === p.id}
                  className="w-full flex items-center gap-4 p-4 rounded-2xl bg-[#111726] border border-slate-800/80 hover:border-indigo-700/50 transition-all text-left group shadow-md"
                >
                  <div className="w-10 h-10 rounded-xl bg-indigo-950/60 border border-indigo-800/50 flex items-center justify-center flex-shrink-0">
                    {p.versions_count > 0 ? (
                      <Layers className="w-5 h-5 text-indigo-400" />
                    ) : (
                      <Server className="w-5 h-5 text-slate-500" />
                    )}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-semibold text-white group-hover:text-indigo-200 transition-colors truncate">
                      {p.name}
                    </p>
                    {p.description && (
                      <p className="text-xs text-slate-500 truncate">{p.description}</p>
                    )}
                    <div className="flex items-center gap-3 mt-1 text-[10px] text-slate-600 font-mono">
                      <span className="flex items-center gap-1">
                        <Clock className="w-3 h-3" />
                        {new Date(p.updated_at).toLocaleDateString()}
                      </span>
                      <span className="flex items-center gap-1">
                        <Layers className="w-3 h-3" />
                        {p.versions_count} version{p.versions_count !== 1 ? 's' : ''}
                      </span>
                    </div>
                  </div>
                  {loadingDesign === p.id ? (
                    <Loader2 className="w-4 h-4 text-slate-400 animate-spin flex-shrink-0" />
                  ) : (
                    <ChevronRight className="w-4 h-4 text-slate-500 group-hover:text-indigo-400 transition-colors flex-shrink-0" />
                  )}
                </button>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
