import { useState } from 'react'
import {
  Key,
  Globe,
  Check,
  Copy,
  ExternalLink,
  ShieldCheck,
  Eye,
  EyeOff,
  Sparkles,
  X,
  Database,
  Terminal,
} from 'lucide-react'
import { useStudioStore } from '../../store/studioStore'

interface ApiKeysModalProps {
  isOpen: boolean
  onClose: () => void
}

interface ApiKeysState {
  geminiApiKey: string
  deepseekApiKey: string
  openaiApiKey: string
  ollamaBaseUrl: string
  qdrantUrl: string
}

const STORAGE_KEY = 'system_design_studio_api_keys'

export default function ApiKeysModal({ isOpen, onClose }: ApiKeysModalProps) {
  const { setView } = useStudioStore()

  const [keys, setKeys] = useState<ApiKeysState>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY)
      if (saved) return JSON.parse(saved)
    } catch {}
    return {
      geminiApiKey: '',
      deepseekApiKey: '',
      openaiApiKey: '',
      ollamaBaseUrl: 'http://localhost:11434',
      qdrantUrl: 'http://localhost:6333',
    }
  })

  const [showKeys, setShowKeys] = useState<Record<string, boolean>>({})
  const [savedSuccess, setSavedSuccess] = useState(false)
  const [copiedPath, setCopiedPath] = useState<string | null>(null)

  const toggleShow = (id: string) => {
    setShowKeys((prev) => ({ ...prev, [id]: !prev[id] }))
  }

  const handleSave = () => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(keys))
      setSavedSuccess(true)
      setTimeout(() => setSavedSuccess(false), 2000)
    } catch {}
  }

  const handleCopy = (path: string) => {
    const fullUrl = `${window.location.origin}${path}`
    navigator.clipboard.writeText(fullUrl)
    setCopiedPath(path)
    setTimeout(() => setCopiedPath(null), 1500)
  }

  if (!isOpen) return null

  const ROUTES = [
    {
      path: '/overview',
      name: 'Overview Dashboard',
      description: 'System Design Studio metrics, templates, and quick starts',
      view: 'overview',
      badge: 'Live',
    },
    {
      path: '/canvas',
      name: 'Architecture Canvas',
      description: 'Miro/Canva-style whiteboard with left component palette & inspector',
      view: 'canvas',
      badge: 'Interactive',
    },
    {
      path: '/whiteboard',
      name: 'SystemSketcher Whiteboard',
      description: 'Technical analysis report, REA CLI tools, and architecture cards',
      view: 'whiteboard',
      badge: 'REA Discovery',
    },
    {
      path: '/compatibility',
      name: 'Compatibility Engine',
      description: 'Deterministic connection validation matrix and protocol verification',
      view: 'compatibility',
      badge: 'Matrix',
    },
    {
      path: '/catalog',
      name: 'Component Catalog',
      description: 'Catalog of 830+ cloud infrastructure & software building blocks',
      view: 'catalog',
      badge: 'Catalog',
    },
    {
      path: '/projects',
      name: 'Studio Projects',
      description: 'Manage architecture projects, requirements interviews, and plans',
      view: 'projects',
      badge: 'Planner',
    },
  ]

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4">
      <div className="w-full max-w-2xl bg-[#0F1626] border border-slate-700/80 rounded-2xl shadow-2xl flex flex-col max-h-[90vh] overflow-hidden">
        {/* Header */}
        <div className="p-4 sm:p-5 border-b border-slate-800 flex items-center justify-between bg-[#0A0F1D]/80 flex-shrink-0">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-xl bg-indigo-600/20 border border-indigo-500/40 flex items-center justify-center text-indigo-400">
              <Key className="w-4 h-4" />
            </div>
            <div>
              <h2 className="text-sm sm:text-base font-bold text-white tracking-tight">
                API Keys &amp; URL Route Navigation
              </h2>
              <p className="text-xs text-slate-400">
                Configure your LLM providers, services, and inspect application page URLs
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-white transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-6">
          {/* Section 1: Page URLs & Routes */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="text-xs font-bold text-indigo-300 uppercase tracking-wider flex items-center gap-1.5">
                <Globe className="w-3.5 h-3.5" />
                Application URLs &amp; Routing
              </h3>
              <span className="text-[10px] font-mono text-slate-400">
                Current URL: <code className="text-indigo-400">{window.location.pathname}</code>
              </span>
            </div>

            <div className="grid grid-cols-1 gap-2">
              {ROUTES.map((route) => {
                const isCurrent = window.location.pathname === route.path
                const isCopied = copiedPath === route.path
                return (
                  <div
                    key={route.path}
                    className={`p-3 rounded-xl border transition-all flex items-center justify-between gap-3 ${
                      isCurrent
                        ? 'bg-indigo-950/40 border-indigo-500/50 shadow-sm'
                        : 'bg-slate-900/60 border-slate-800/80 hover:border-slate-700'
                    }`}
                  >
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <code className="text-xs font-mono font-bold text-indigo-300">
                          {route.path}
                        </code>
                        <span className="text-[9px] font-mono px-1.5 py-0.2 rounded bg-slate-800 text-slate-400 border border-slate-700">
                          {route.badge}
                        </span>
                        {isCurrent && (
                          <span className="text-[9px] font-semibold text-emerald-400 bg-emerald-950/60 border border-emerald-800/50 px-1.5 py-0.2 rounded">
                            Active Page
                          </span>
                        )}
                      </div>
                      <p className="text-[11px] text-slate-400 mt-0.5 truncate">
                        {route.description}
                      </p>
                    </div>

                    <div className="flex items-center gap-1.5 flex-shrink-0">
                      <button
                        onClick={() => handleCopy(route.path)}
                        className="px-2 py-1 rounded-md text-[10px] font-mono bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center gap-1"
                        title="Copy full URL"
                      >
                        {isCopied ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
                        <span>{isCopied ? 'Copied' : 'Copy'}</span>
                      </button>
                      <button
                        onClick={() => {
                          setView(route.view as any)
                          onClose()
                        }}
                        className="px-2.5 py-1 rounded-md text-[10px] font-semibold bg-indigo-600 hover:bg-indigo-500 text-white flex items-center gap-1 shadow-sm"
                      >
                        <span>Go</span>
                        <ExternalLink className="w-3 h-3" />
                      </button>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>

          {/* Section 2: LLM & Services API Keys */}
          <div className="space-y-3 pt-2 border-t border-slate-800/80">
            <div className="flex items-center justify-between">
              <h3 className="text-xs font-bold text-indigo-300 uppercase tracking-wider flex items-center gap-1.5">
                <ShieldCheck className="w-3.5 h-3.5" />
                AI Model &amp; Service API Keys
              </h3>
              <span className="text-[10px] font-mono text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">
                Secure &amp; Client-Persisted
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {/* Gemini API Key */}
              <div className="space-y-1">
                <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
                  Gemini API Key
                </label>
                <div className="relative">
                  <input
                    type={showKeys['gemini'] ? 'text' : 'password'}
                    value={keys.geminiApiKey}
                    onChange={(e) => setKeys({ ...keys, geminiApiKey: e.target.value })}
                    placeholder="AIzaSy…"
                    className="w-full bg-[#080C14] border border-slate-700 rounded-xl px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 font-mono pr-8"
                  />
                  <button
                    type="button"
                    onClick={() => toggleShow('gemini')}
                    className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
                  >
                    {showKeys['gemini'] ? <EyeOff className="w-3 h-3" /> : <Eye className="w-3 h-3" />}
                  </button>
                </div>
              </div>

              {/* DeepSeek API Key */}
              <div className="space-y-1">
                <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5 text-purple-400" />
                  DeepSeek API Key
                </label>
                <div className="relative">
                  <input
                    type={showKeys['deepseek'] ? 'text' : 'password'}
                    value={keys.deepseekApiKey}
                    onChange={(e) => setKeys({ ...keys, deepseekApiKey: e.target.value })}
                    placeholder="sk-…"
                    className="w-full bg-[#080C14] border border-slate-700 rounded-xl px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 font-mono pr-8"
                  />
                  <button
                    type="button"
                    onClick={() => toggleShow('deepseek')}
                    className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
                  >
                    {showKeys['deepseek'] ? <EyeOff className="w-3 h-3" /> : <Eye className="w-3 h-3" />}
                  </button>
                </div>
              </div>

              {/* OpenAI API Key */}
              <div className="space-y-1">
                <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5 text-emerald-400" />
                  OpenAI API Key
                </label>
                <div className="relative">
                  <input
                    type={showKeys['openai'] ? 'text' : 'password'}
                    value={keys.openaiApiKey}
                    onChange={(e) => setKeys({ ...keys, openaiApiKey: e.target.value })}
                    placeholder="sk-proj-…"
                    className="w-full bg-[#080C14] border border-slate-700 rounded-xl px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 font-mono pr-8"
                  />
                  <button
                    type="button"
                    onClick={() => toggleShow('openai')}
                    className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
                  >
                    {showKeys['openai'] ? <EyeOff className="w-3 h-3" /> : <Eye className="w-3 h-3" />}
                  </button>
                </div>
              </div>

              {/* Ollama Base URL */}
              <div className="space-y-1">
                <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                  <Terminal className="w-3.5 h-3.5 text-sky-400" />
                  Ollama Base URL
                </label>
                <input
                  type="text"
                  value={keys.ollamaBaseUrl}
                  onChange={(e) => setKeys({ ...keys, ollamaBaseUrl: e.target.value })}
                  placeholder="http://localhost:11434"
                  className="w-full bg-[#080C14] border border-slate-700 rounded-xl px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 font-mono"
                />
              </div>
            </div>

            {/* Qdrant URL */}
            <div className="space-y-1 pt-1">
              <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                <Database className="w-3.5 h-3.5 text-amber-400" />
                Qdrant Vector Database URL
              </label>
              <input
                type="text"
                value={keys.qdrantUrl}
                onChange={(e) => setKeys({ ...keys, qdrantUrl: e.target.value })}
                placeholder="http://localhost:6333"
                className="w-full bg-[#080C14] border border-slate-700 rounded-xl px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 font-mono"
              />
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-slate-800 bg-[#0A0F1D] flex items-center justify-between flex-shrink-0">
          <span className="text-[11px] text-slate-500">
            Keys are stored securely in local browser storage
          </span>
          <div className="flex items-center gap-2">
            <button
              onClick={onClose}
              className="px-3 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors"
            >
              Close
            </button>
            <button
              onClick={handleSave}
              className="px-4 py-1.5 rounded-xl text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-600/30 flex items-center gap-1.5"
            >
              {savedSuccess ? <Check className="w-3.5 h-3.5 text-emerald-300" /> : <Key className="w-3.5 h-3.5" />}
              <span>{savedSuccess ? 'Saved Keys!' : 'Save Configuration'}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
