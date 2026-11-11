import { useState, useRef } from 'react'
import {
  PenTool,
  ZoomIn,
  ZoomOut,
  Copy,
  Check,
  Download,
  ExternalLink,
  Terminal,
  Sparkles,
  ArrowRight,
  Grid,
} from 'lucide-react'
import { useStudioStore } from '../../store/studioStore'
import {
  SYSTEM_SKETCHER_MARKDOWN,
  SYSTEM_SKETCHER_METADATA,
  EXAMPLE_DIAGRAM_JSON,
  TECH_STACK_TABLE,
  RESEARCH_CONFIDENCE_TABLE,
  NEXT_STEPS_CHECKLIST,
} from '../../data/systemSketcherData'

type GridStyle = 'dots' | 'grid' | 'blueprint' | 'clean'
type ViewMode = 'canvas' | 'document'

export default function WhiteboardCanvas() {
  const { setView, addNode, addEdge } = useStudioStore()

  // Whiteboard controls
  const [zoom, setZoom] = useState<number>(100)
  const [gridStyle, setGridStyle] = useState<GridStyle>('dots')
  const [viewMode, setViewMode] = useState<ViewMode>('canvas')
  const [activeSection, setActiveSection] = useState<string>('sec-1')
  
  // Copy state feedbacks
  const [copiedCmd, setCopiedCmd] = useState(false)
  const [copiedMd, setCopiedMd] = useState(false)
  const [copiedJson, setCopiedJson] = useState(false)
  const [loadedToStudio, setLoadedToStudio] = useState(false)

  // Interactive checklist state
  const [checkedItems, setCheckedItems] = useState<Record<number, boolean>>({})

  const canvasRef = useRef<HTMLDivElement>(null)

  const toggleCheck = (idx: number) => {
    setCheckedItems((prev) => ({ ...prev, [idx]: !prev[idx] }))
  }

  const handleCopyCmd = (cmd: string) => {
    navigator.clipboard.writeText(cmd)
    setCopiedCmd(true)
    setTimeout(() => setCopiedCmd(false), 2000)
  }

  const handleCopyMd = () => {
    navigator.clipboard.writeText(SYSTEM_SKETCHER_MARKDOWN)
    setCopiedMd(true)
    setTimeout(() => setCopiedMd(false), 2000)
  }

  const handleCopyJson = () => {
    navigator.clipboard.writeText(JSON.stringify(EXAMPLE_DIAGRAM_JSON, null, 2))
    setCopiedJson(true)
    setTimeout(() => setCopiedJson(false), 2000)
  }

  const handleDownloadMd = () => {
    const blob = new Blob([SYSTEM_SKETCHER_MARKDOWN], { type: 'text/markdown;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = 'SystemSketcher_Technical_Analysis.md'
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    URL.revokeObjectURL(url)
  }

  const handleLoadDiagramToStudio = () => {
    EXAMPLE_DIAGRAM_JSON.nodes.forEach((n) => {
      addNode({
        id: n.id,
        slug: n.id,
        category: n.type === 'database' ? 'database' : n.type === 'api_gateway' ? 'gateway' : 'compute',
        layer: n.type === 'database' ? 'data' : n.type === 'api_gateway' ? 'gateway' : 'application',
        label: n.label,
        replicas: 1,
        protocols: ['http', 'https'],
        limits: {},
        config: {},
        position: { x: n.x, y: n.y },
      })
    })

    EXAMPLE_DIAGRAM_JSON.edges.forEach((e) => {
      addEdge({
        source_id: e.source,
        target_id: e.target,
        protocol: 'HTTPS / SQL',
        label: e.id,
      })
    })

    setLoadedToStudio(true)
    setTimeout(() => {
      setView('canvas')
    }, 800)
  }

  const scrollToSection = (id: string) => {
    setActiveSection(id)
    const el = document.getElementById(id)
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  // Background pattern CSS
  const getCanvasBg = () => {
    switch (gridStyle) {
      case 'dots':
        return {
          backgroundColor: '#090D16',
          backgroundImage: 'radial-gradient(rgba(99, 102, 241, 0.22) 1.5px, transparent 1.5px)',
          backgroundSize: '24px 24px',
        }
      case 'grid':
        return {
          backgroundColor: '#090D16',
          backgroundImage:
            'linear-gradient(to right, rgba(255, 255, 255, 0.05) 1px, transparent 1px), linear-gradient(to bottom, rgba(255, 255, 255, 0.05) 1px, transparent 1px)',
          backgroundSize: '32px 32px',
        }
      case 'blueprint':
        return {
          backgroundColor: '#071529',
          backgroundImage:
            'linear-gradient(rgba(56, 189, 248, 0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(56, 189, 248, 0.1) 1px, transparent 1px)',
          backgroundSize: '20px 20px',
        }
      case 'clean':
      default:
        return {
          backgroundColor: '#0B0F17',
        }
    }
  }

  const SECTIONS = [
    { id: 'sec-1', title: '1. Executive Summary' },
    { id: 'sec-2', title: '2. Product Overview' },
    { id: 'sec-3', title: '3. Main Features' },
    { id: 'sec-4', title: '4. Product Architecture' },
    { id: 'sec-5', title: '5. Diagram Data Structure' },
    { id: 'sec-6', title: '6. REA — Reverse Engineer Anything' },
    { id: 'sec-7', title: '7. Reverse-Engineering Methodology' },
    { id: 'sec-8', title: '8. Recommended Tech Stack' },
    { id: 'sec-9', title: '9. Final Assessment' },
    { id: 'sec-10', title: '10. Next Steps' },
  ]

  return (
    <div className="relative w-full h-[calc(100vh-4rem)] flex flex-col bg-[#0B0F17] text-slate-100 overflow-hidden select-text">
      {/* ── Floating Whiteboard Toolbar ────────────────────────────────────────── */}
      <div className="h-14 border-b border-slate-800 bg-[#0E1424]/95 backdrop-blur-md px-4 sm:px-6 flex items-center justify-between z-20 flex-shrink-0 shadow-lg">
        {/* Left: Branding & Section Switcher */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2">
            <span className="p-1.5 rounded-lg bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
              <PenTool className="w-4 h-4" />
            </span>
            <div>
              <h2 className="text-xs sm:text-sm font-bold text-white flex items-center gap-1.5">
                Whiteboard Canvas
                <span className="hidden md:inline px-1.5 py-0.2 rounded text-[10px] bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 font-mono">
                  REA Discovery
                </span>
              </h2>
            </div>
          </div>

          <div className="hidden lg:flex items-center gap-1 border-l border-slate-800 pl-3">
            <label className="text-[11px] text-slate-400 font-medium">Jump:</label>
            <select
              value={activeSection}
              onChange={(e) => scrollToSection(e.target.value)}
              className="bg-slate-900 border border-slate-800 rounded-lg text-xs text-slate-300 py-1 px-2 focus:outline-none focus:ring-1 focus:ring-indigo-500"
            >
              {SECTIONS.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.title}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Center: Canvas View Controls (Zoom, Grids, View Mode) */}
        <div className="hidden sm:flex items-center gap-2 bg-[#080C14] p-1 rounded-xl border border-slate-800/80 shadow-inner">
          <button
            onClick={() => setZoom((z) => Math.max(50, z - 10))}
            className="p-1.5 hover:bg-slate-800 rounded text-slate-400 hover:text-white transition-colors"
            title="Zoom out"
          >
            <ZoomOut className="w-3.5 h-3.5" />
          </button>
          <span className="text-[11px] font-mono font-medium text-slate-300 w-11 text-center select-none">
            {zoom}%
          </span>
          <button
            onClick={() => setZoom((z) => Math.min(150, z + 10))}
            className="p-1.5 hover:bg-slate-800 rounded text-slate-400 hover:text-white transition-colors"
            title="Zoom in"
          >
            <ZoomIn className="w-3.5 h-3.5" />
          </button>
          <button
            onClick={() => setZoom(100)}
            className="px-1.5 py-1 text-[10px] hover:bg-slate-800 rounded text-slate-400 hover:text-white transition-colors font-mono"
            title="Reset Zoom"
          >
            100%
          </button>

          <div className="h-3 w-px bg-slate-800 mx-1" />

          {/* Grid Style Toggle */}
          <button
            onClick={() => {
              const styles: GridStyle[] = ['dots', 'grid', 'blueprint', 'clean']
              const next = styles[(styles.indexOf(gridStyle) + 1) % styles.length]
              setGridStyle(next)
            }}
            className="p-1.5 hover:bg-slate-800 rounded text-slate-400 hover:text-indigo-400 transition-colors flex items-center gap-1 text-[11px]"
            title={`Canvas Grid: ${gridStyle}`}
          >
            <Grid className="w-3.5 h-3.5" />
            <span className="capitalize hidden md:inline text-[10px]">{gridStyle}</span>
          </button>

          <div className="h-3 w-px bg-slate-800 mx-1" />

          {/* View Mode Toggle */}
          <div className="flex items-center gap-0.5">
            <button
              onClick={() => setViewMode('canvas')}
              className={`px-2 py-1 rounded-md text-[11px] font-medium transition-all ${
                viewMode === 'canvas'
                  ? 'bg-indigo-600 text-white'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Canvas
            </button>
            <button
              onClick={() => setViewMode('document')}
              className={`px-2 py-1 rounded-md text-[11px] font-medium transition-all ${
                viewMode === 'document'
                  ? 'bg-indigo-600 text-white'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Document
            </button>
          </div>
        </div>

        {/* Right: Actions (Copy REA, Copy MD, Download, Direct Studio Load) */}
        <div className="flex items-center gap-2">
          {/* Quick REA copy button */}
          <button
            onClick={() => handleCopyCmd(SYSTEM_SKETCHER_METADATA.setupCommand)}
            className="px-2.5 py-1.5 rounded-lg text-xs font-mono font-medium transition-all flex items-center gap-1.5 bg-indigo-950/60 hover:bg-indigo-900/60 text-indigo-300 border border-indigo-700/50"
            title="Copy REA Setup Command"
          >
            <Terminal className="w-3.5 h-3.5 text-indigo-400" />
            <span className="hidden md:inline">npx rea-agents setup</span>
            {copiedCmd ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
          </button>

          {/* Copy Full Markdown */}
          <button
            onClick={handleCopyMd}
            className="p-1.5 sm:px-2.5 sm:py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-800"
            title="Copy Full Report Markdown"
          >
            {copiedMd ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5 text-slate-400" />}
            <span className="hidden sm:inline">{copiedMd ? 'Copied' : 'Copy MD'}</span>
          </button>

          {/* Download MD file */}
          <button
            onClick={handleDownloadMd}
            className="p-1.5 sm:px-2.5 sm:py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-800"
            title="Download SystemSketcher Report (.md)"
          >
            <Download className="w-3.5 h-3.5 text-slate-400" />
            <span className="hidden sm:inline">Download</span>
          </button>
        </div>
      </div>

      {/* ── Whiteboard Canvas Surface ─────────────────────────────────────────── */}
      <div
        ref={canvasRef}
        className="flex-1 w-full overflow-y-auto overflow-x-hidden transition-all duration-150 p-4 sm:p-8 md:p-12"
        style={getCanvasBg()}
      >
        <div
          className={`mx-auto transition-transform duration-200 origin-top ${
            viewMode === 'canvas' ? 'max-w-6xl space-y-8' : 'max-w-4xl space-y-10'
          }`}
          style={{ transform: `scale(${zoom / 100})` }}
        >
          {/* ── Whiteboard Sticky Notes & Top Banner ─────────────────────────── */}
          {viewMode === 'canvas' && (
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 pb-2">
              {/* Sticky Note 1 */}
              <div className="bg-[#2D2312] border-2 border-[#D97706]/60 rounded-xl p-4 shadow-xl transform -rotate-1 hover:rotate-0 transition-transform">
                <div className="flex items-center justify-between text-[#FCD34D] text-[11px] font-bold font-mono uppercase mb-1">
                  <span>📌 Key Asset</span>
                  <span>830+</span>
                </div>
                <p className="text-amber-200/90 text-xs font-medium leading-relaxed">
                  Huge advertised component library with AWS, cloud infra, data stores, messaging & monitoring symbols.
                </p>
              </div>

              {/* Sticky Note 2 */}
              <div className="bg-[#112338] border-2 border-[#0EA5E9]/60 rounded-xl p-4 shadow-xl transform rotate-1 hover:rotate-0 transition-transform">
                <div className="flex items-center justify-between text-[#7DD3FC] text-[11px] font-bold font-mono uppercase mb-1">
                  <span>🧠 AI Core Principle</span>
                  <span>Structured</span>
                </div>
                <p className="text-sky-200/90 text-xs font-medium leading-relaxed">
                  AI must generate structured diagram graph modifications (Nodes + Edges JSON), not merely static images.
                </p>
              </div>

              {/* Sticky Note 3 */}
              <div className="bg-[#1A1333] border-2 border-[#A855F7]/60 rounded-xl p-4 shadow-xl transform -rotate-1 hover:rotate-0 transition-transform">
                <div className="flex items-center justify-between text-[#E9D5FF] text-[11px] font-bold font-mono uppercase mb-1">
                  <span>💾 JSON Export</span>
                  <span>Editable</span>
                </div>
                <p className="text-purple-200/90 text-xs font-medium leading-relaxed">
                  Diagrams preserved as editable application state data, enabling restoration, diffing, and code generation.
                </p>
              </div>

              {/* Sticky Note 4 */}
              <div className="bg-[#0D281E] border-2 border-[#10B981]/60 rounded-xl p-4 shadow-xl transform rotate-1 hover:rotate-0 transition-transform">
                <div className="flex items-center justify-between text-[#6EE7B7] text-[11px] font-bold font-mono uppercase mb-1">
                  <span>⚡ REA Setup</span>
                  <span>Ready</span>
                </div>
                <p className="text-emerald-200/90 text-xs font-medium leading-relaxed">
                  CLI: <code className="text-[10px] bg-black/40 px-1 py-0.5 rounded text-emerald-300">npx rea-agents@latest setup</code>
                  <br />Doctor check ready for verification.
                </p>
              </div>
            </div>
          )}

          {/* ── Document Canvas Card Header ───────────────────────────────────── */}
          <div className="bg-[#101728]/90 border border-slate-700/80 rounded-2xl p-6 sm:p-8 shadow-2xl backdrop-blur-xl relative overflow-hidden">
            <div className="absolute top-0 right-0 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />

            <div className="space-y-4">
              <div className="flex flex-wrap items-center gap-2">
                <span className="px-3 py-1 rounded-full text-xs font-semibold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40">
                  Research and Technical Discovery Report
                </span>
                <span className="px-2.5 py-1 rounded-full text-xs font-mono bg-slate-800 text-slate-300 border border-slate-700">
                  📅 11 November 2026
                </span>
              </div>

              <h1 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white tracking-tight leading-tight">
                SystemSketcher — Product Reverse Engineering &amp; Technical Analysis
              </h1>

              {/* Metadata Badges Bar */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
                <a
                  href={SYSTEM_SKETCHER_METADATA.website}
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center justify-between p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-indigo-500/50 transition-colors group"
                >
                  <div>
                    <p className="text-[10px] text-slate-400 font-mono uppercase">Target Website</p>
                    <p className="text-xs font-semibold text-indigo-300 group-hover:text-indigo-200">
                      systemsketcher.com
                    </p>
                  </div>
                  <ExternalLink className="w-3.5 h-3.5 text-slate-500 group-hover:text-indigo-400" />
                </a>

                <div className="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
                  <p className="text-[10px] text-slate-400 font-mono uppercase">Related Tool</p>
                  <p className="text-xs font-semibold text-purple-300">
                    REA — Reverse Engineer Anything
                  </p>
                </div>

                <div
                  onClick={() => handleCopyCmd(SYSTEM_SKETCHER_METADATA.setupCommand)}
                  className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-emerald-500/50 cursor-pointer transition-colors group flex items-center justify-between"
                  title="Click to copy setup command"
                >
                  <div>
                    <p className="text-[10px] text-slate-400 font-mono uppercase">REA Setup Command</p>
                    <code className="text-xs font-semibold text-emerald-300 font-mono">
                      npx rea-agents@latest setup
                    </code>
                  </div>
                  <Copy className="w-3.5 h-3.5 text-slate-500 group-hover:text-emerald-400" />
                </div>
              </div>
            </div>
          </div>

          {/* ── Section 1: Executive Summary ─────────────────────────────────── */}
          <div
            id="sec-1"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-4"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-indigo-500" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                1. Executive Summary
              </h2>
            </div>

            <p className="text-slate-300 text-sm leading-relaxed">
              SystemSketcher is a browser-based system architecture diagramming product designed to help developers and software architects visually design, communicate, and refine software infrastructure.
            </p>

            <div className="pt-2">
              <p className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">
                Its central value proposition combines three capabilities:
              </p>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800/90 space-y-1">
                  <span className="text-xs font-bold text-indigo-400 font-mono">01. Visual Canvas</span>
                  <p className="text-xs text-slate-300 leading-snug">
                    A visual diagramming canvas for designing system architectures.
                  </p>
                </div>
                <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800/90 space-y-1">
                  <span className="text-xs font-bold text-blue-400 font-mono">02. Component Library</span>
                  <p className="text-xs text-slate-300 leading-snug">
                    A reusable component library containing more than 830 advertised components.
                  </p>
                </div>
                <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800/90 space-y-1">
                  <span className="text-xs font-bold text-purple-400 font-mono">03. AI Assistance</span>
                  <p className="text-xs text-slate-300 leading-snug">
                    AI-assisted architecture suggestions and diagram creation.
                  </p>
                </div>
              </div>
            </div>

            <p className="text-slate-300 text-sm leading-relaxed">
              The product aims to simplify the process of translating an abstract software architecture into a visual representation.
            </p>

            <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 space-y-2">
              <p className="text-xs font-semibold text-slate-300">The public website advertises:</p>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-300">
                <li className="flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  Visual system architecture editing.
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  A large component library.
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  Drag-and-drop diagram construction.
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  AI-powered suggestions.
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  Sample architecture diagrams.
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  PNG and JSON export.
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  Access without mandatory sign-up.
                </li>
              </ul>
            </div>

            <div className="p-3.5 rounded-xl bg-amber-950/40 border border-amber-800/40 text-amber-200/90 text-xs leading-relaxed">
              <strong>Note:</strong> This report separates publicly advertised functionality from proposed technical architecture. The exact production implementation, internal source code, API endpoints, and backend infrastructure have not been verified.
            </div>
          </div>

          {/* ── Section 2: Product Overview ──────────────────────────────────── */}
          <div
            id="sec-2"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-5"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-blue-500" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                2. Product Overview
              </h2>
            </div>

            <div className="space-y-3">
              <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                2.1 What is SystemSketcher?
              </h3>
              <p className="text-slate-300 text-sm leading-relaxed">
                SystemSketcher is a visual system design environment. It enables users to represent how different parts of an application communicate with one another.
              </p>
              <p className="text-slate-300 text-xs">For example, a typical web application might contain:</p>
              <div className="flex flex-wrap gap-2 pt-1">
                {[
                  'Frontend application',
                  'API gateway',
                  'Backend services',
                  'Authentication service',
                  'Database',
                  'Cache',
                  'Message queue',
                  'Cloud storage',
                  'Monitoring infrastructure',
                ].map((item) => (
                  <span
                    key={item}
                    className="px-2.5 py-1 rounded-lg text-xs bg-slate-900 border border-slate-700/80 text-slate-300 font-mono"
                  >
                    {item}
                  </span>
                ))}
              </div>
              <p className="text-slate-300 text-sm leading-relaxed pt-2">
                Instead of explaining all these components through text, users can arrange them on a canvas and connect them through visual relationships.
              </p>
            </div>

            <div className="space-y-3 pt-2">
              <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                2.2 Target Audience
              </h3>
              <p className="text-slate-300 text-xs">The likely target audience includes:</p>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
                {[
                  'Software architects',
                  'Backend developers',
                  'Full-stack developers',
                  'Cloud engineers',
                  'DevOps engineers',
                  'Engineering students',
                  'System design interview candidates',
                  'Technical founders & product teams',
                ].map((role) => (
                  <div key={role} className="p-2.5 rounded-lg bg-slate-900/90 border border-slate-800 text-slate-300 flex items-center gap-1.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                    <span>{role}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="space-y-2 pt-2">
              <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                2.3 Main Product Value
              </h3>
              <p className="text-slate-300 text-sm leading-relaxed">
                The product reduces the effort required to create and communicate architecture diagrams. Its AI capabilities potentially reduce the need to manually construct every component and connection.
              </p>
            </div>
          </div>

          {/* ── Section 3: Main Features and Functionalities ─────────────────── */}
          <div
            id="sec-3"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-6"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-emerald-500" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                3. Main Features and Functionalities
              </h2>
            </div>

            {/* 3.1 Visual Canvas */}
            <div className="space-y-2">
              <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                3.1 Visual Architecture Canvas
              </h3>
              <p className="text-slate-300 text-sm">
                The canvas is the primary workspace. Expected capabilities to investigate include:
              </p>
              <div className="flex flex-wrap gap-2 text-xs">
                {[
                  'Component placement',
                  'Drag-and-drop interactions',
                  'Node selection',
                  'Component movement',
                  'Connection creation',
                  'Diagram arrangement',
                  'Zooming and panning',
                  'Component deletion',
                  'Diagram editing',
                  'Undo and redo',
                ].map((cap) => (
                  <span key={cap} className="px-2.5 py-1 rounded-md bg-indigo-950/40 border border-indigo-800/40 text-indigo-200">
                    ✓ {cap}
                  </span>
                ))}
              </div>
              <p className="text-[11px] text-slate-400 italic">
                The exact availability of each interaction must be confirmed through hands-on browser inspection.
              </p>
            </div>

            {/* 3.2 Component Library */}
            <div className="space-y-3 pt-2">
              <div className="flex items-center justify-between">
                <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                  3.2 Component Library (830+ Components Advertised)
                </h3>
                <span className="text-xs font-mono text-emerald-400 bg-emerald-950/50 border border-emerald-800/40 px-2 py-0.5 rounded">
                  830+ Advertised
                </span>
              </div>
              <p className="text-slate-300 text-sm leading-relaxed">
                The catalog is a significant part of the product because it allows users to build diagrams using recognizable infrastructure symbols.
              </p>
              <div className="grid grid-cols-1 md:grid-cols-5 gap-3 pt-1">
                <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1.5">
                  <p className="text-xs font-bold text-sky-400 uppercase">Cloud Infra</p>
                  <ul className="text-[11px] text-slate-300 space-y-0.5">
                    <li>• AWS services</li>
                    <li>• Compute resources</li>
                    <li>• Serverless functions</li>
                    <li>• Load balancers</li>
                    <li>• API gateways</li>
                    <li>• Networking services</li>
                    <li>• Cloud storage</li>
                  </ul>
                </div>

                <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1.5">
                  <p className="text-xs font-bold text-emerald-400 uppercase">Databases &amp; Storage</p>
                  <ul className="text-[11px] text-slate-300 space-y-0.5">
                    <li>• PostgreSQL</li>
                    <li>• MySQL</li>
                    <li>• MongoDB</li>
                    <li>• Redis</li>
                    <li>• Object storage</li>
                    <li>• Search indexes</li>
                    <li>• Distributed databases</li>
                  </ul>
                </div>

                <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1.5">
                  <p className="text-xs font-bold text-indigo-400 uppercase">Applications</p>
                  <ul className="text-[11px] text-slate-300 space-y-0.5">
                    <li>• Web applications</li>
                    <li>• Mobile applications</li>
                    <li>• Backend services</li>
                    <li>• Authentication services</li>
                    <li>• External APIs</li>
                    <li>• Microservices</li>
                  </ul>
                </div>

                <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1.5">
                  <p className="text-xs font-bold text-amber-400 uppercase">Messaging &amp; Events</p>
                  <ul className="text-[11px] text-slate-300 space-y-0.5">
                    <li>• Message queues</li>
                    <li>• Event brokers</li>
                    <li>• Kafka-style streaming</li>
                    <li>• Event consumers</li>
                    <li>• Notification services</li>
                  </ul>
                </div>

                <div className="p-3 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1.5">
                  <p className="text-xs font-bold text-purple-400 uppercase">DevOps &amp; Monitoring</p>
                  <ul className="text-[11px] text-slate-300 space-y-0.5">
                    <li>• Docker</li>
                    <li>• Kubernetes</li>
                    <li>• CI/CD</li>
                    <li>• Logging</li>
                    <li>• Metrics</li>
                    <li>• Monitoring systems</li>
                  </ul>
                </div>
              </div>
              <p className="text-[11px] text-slate-400 italic">
                These are representative categories for technical classification, not a verified complete catalog of SystemSketcher.
              </p>
            </div>

            {/* 3.3 Connections and Relationships */}
            <div className="space-y-2 pt-2">
              <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                3.3 Connections and Relationships
              </h3>
              <p className="text-slate-300 text-sm">
                Connections describe how components communicate (e.g. Frontend to API gateway, API gateway to backend service, Backend service to database, Application to cache, Producer to message queue).
              </p>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs">
                {['Source component', 'Destination component', 'Connection direction', 'Optional labels', 'Connection styling', 'Routing information'].map((c) => (
                  <div key={c} className="p-2 rounded-lg bg-slate-900/80 border border-slate-800 text-slate-300 font-mono">
                    ↔ {c}
                  </div>
                ))}
              </div>
            </div>

            {/* 3.4 AI-Assisted Design */}
            <div className="space-y-2 pt-2">
              <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                3.4 AI-Assisted Architecture Design
              </h3>
              <p className="text-slate-300 text-sm">
                AI is one of the main differentiators of the product. The publicly advertised AI functionality includes architecture suggestions. Broader capabilities worth investigating:
              </p>
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2 text-xs">
                {[
                  'Natural-language architecture generation',
                  'Architecture improvement suggestions',
                  'Diagram generation',
                  'Section-based editing',
                  'Sketch-to-diagram workflows',
                  'Architecture recommendations',
                ].map((item) => (
                  <div key={item} className="p-2.5 rounded-lg bg-purple-950/30 border border-purple-800/40 text-purple-200">
                    ⚡ {item}
                  </div>
                ))}
              </div>
            </div>

            {/* 3.5 & 3.6 Export & Samples */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
              <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                <h3 className="text-sm font-semibold text-indigo-300">3.5 Export Functionality</h3>
                <div className="space-y-1.5 text-xs text-slate-300">
                  <p>
                    <strong className="text-white">PNG export:</strong> Creates a visual image of the architecture; useful for presentations and documentation.
                  </p>
                  <p>
                    <strong className="text-white">JSON export:</strong> Preserves a structured representation; useful for diagram restoration, processing, and integration with other tools.
                  </p>
                </div>
              </div>

              <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                <h3 className="text-sm font-semibold text-indigo-300">3.6 Sample Architectures</h3>
                <div className="space-y-1.5 text-xs text-slate-300">
                  <p><strong className="text-white">E-commerce:</strong> Product catalog, Order management, Payment processing, Inventory, Database, Cache.</p>
                  <p><strong className="text-white">URL shortener:</strong> URL input, Hash generation, Mapping storage, Redirection service, Database.</p>
                  <p><strong className="text-white">Video streaming:</strong> Video upload, Transcoding, Storage, CDN delivery, Metadata DB.</p>
                </div>
              </div>
            </div>
          </div>

          {/* ── Section 4: Product Architecture — Proposed Technical Model ───── */}
          <div
            id="sec-4"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-6"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-purple-500" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                4. Product Architecture — Proposed Technical Model
              </h2>
            </div>

            <p className="text-xs text-slate-400 italic">
              The following architecture represents a reasonable implementation model for a product like SystemSketcher. It is not a confirmed representation of its production infrastructure.
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {/* 4.1 Frontend Layer */}
              <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                <h3 className="text-xs font-bold text-sky-400 uppercase tracking-wide">4.1 Frontend Layer</h3>
                <p className="text-xs text-slate-300">
                  <strong>Responsibilities:</strong> User interface, Architecture canvas, Component sidebar, Toolbar, Properties panel, Diagram interaction, Export controls.
                </p>
                <p className="text-xs text-indigo-300 font-mono">
                  Recommended: React, TypeScript, SVG / Canvas, Graph editor library (XYFlow/React Flow).
                </p>
              </div>

              {/* 4.2 Diagram State Management */}
              <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                <h3 className="text-xs font-bold text-indigo-400 uppercase tracking-wide">4.2 Diagram State Management</h3>
                <div className="text-xs text-slate-300 space-y-1">
                  <p><strong>Nodes:</strong> ID, Component type, Display name, Position, Dimensions, Icon, Properties.</p>
                  <p><strong>Edges:</strong> ID, Source node, Destination node, Direction, Label, Styling.</p>
                  <p><strong>Diagram metadata:</strong> Diagram ID, Name, Version, Created/Updated dates, Viewport settings.</p>
                </div>
              </div>

              {/* 4.3 Component Registry */}
              <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                <h3 className="text-xs font-bold text-emerald-400 uppercase tracking-wide">4.3 Component Registry</h3>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Maintains available architecture components: Unique identifier, Component name, Category, Icon, Description, Default properties, Vendor, and optional documentation references.
                </p>
              </div>

              {/* 4.5 & 4.6 Persistence & Export */}
              <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                <h3 className="text-xs font-bold text-amber-400 uppercase tracking-wide">4.5 Persistence &amp; 4.6 Export Engine</h3>
                <p className="text-xs text-slate-300">
                  <strong>Persistence:</strong> User profiles, Saved diagrams, Component metadata, Templates, Versions, Preferences.
                </p>
                <p className="text-xs text-slate-300">
                  <strong>Export Engine:</strong> PNG rendering, JSON serialization/deserialization, Diagram restoration, SVG output.
                </p>
              </div>
            </div>

            {/* 4.4 AI Orchestration Workflow */}
            <div className="p-5 rounded-xl bg-gradient-to-r from-purple-950/40 via-indigo-950/40 to-slate-900/80 border border-indigo-500/30 space-y-3">
              <h3 className="text-xs font-bold text-indigo-300 uppercase tracking-wide flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
                4.4 AI Orchestration Layer (Step-by-Step Processing)
              </h3>
              <p className="text-xs text-slate-300">
                User instruction: <em className="text-indigo-200">"Create an e-commerce architecture using AWS, Redis, PostgreSQL, and an API gateway."</em>
              </p>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
                {[
                  '1. Interpret requirements',
                  '2. Identify component types',
                  '3. Generate node definitions',
                  '4. Generate connection definitions',
                  '5. Arrange the diagram',
                  '6. Validate resulting graph',
                  '7. Return structured JSON',
                  '8. Render onto canvas',
                ].map((step) => (
                  <div key={step} className="p-2 rounded-lg bg-black/40 border border-indigo-500/20 text-xs text-indigo-200 font-mono">
                    {step}
                  </div>
                ))}
              </div>
              <p className="text-[11px] text-amber-300/90 font-medium">
                ★ Core Design Principle: AI should generate structured diagram operations, not simply return an image.
              </p>
            </div>
          </div>

          {/* ── Section 5: Example Diagram Data Structure ────────────────────── */}
          <div
            id="sec-5"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-5"
          >
            <div className="flex items-center justify-between border-b border-slate-800/80 pb-3">
              <div className="flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-cyan-400" />
                <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                  5. Example Diagram Data Structure
                </h2>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={handleCopyJson}
                  className="px-2.5 py-1 rounded-lg text-xs font-mono font-medium transition-all flex items-center gap-1.5 bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800"
                >
                  {copiedJson ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                  <span>{copiedJson ? 'Copied JSON' : 'Copy JSON'}</span>
                </button>
                <button
                  onClick={handleLoadDiagramToStudio}
                  disabled={loadedToStudio}
                  className="px-3 py-1 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-600/30"
                  title="Load this diagram into the main Studio Architecture Canvas"
                >
                  <ArrowRight className="w-3.5 h-3.5" />
                  <span>{loadedToStudio ? 'Opening Canvas…' : 'Load into Studio Canvas'}</span>
                </button>
              </div>
            </div>

            <p className="text-slate-300 text-sm">
              The following is an illustrative schema for a SystemSketcher-like application (proposed data structure):
            </p>

            {/* Interactive Visual Graph Preview */}
            <div className="p-4 rounded-xl bg-[#090D16] border border-slate-800 space-y-3">
              <p className="text-[11px] font-mono text-slate-400 uppercase tracking-wide">
                Interactive Graph Visualizer (Section 5 Schema)
              </p>
              <div className="flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-6 py-4">
                {/* Node 1 */}
                <div className="p-3.5 rounded-xl bg-[#0e1a2e] border-2 border-[#3b82f6] text-center shadow-lg w-40">
                  <div className="text-[10px] font-mono text-sky-400 uppercase">application</div>
                  <div className="text-xs font-bold text-white mt-1">Frontend</div>
                  <div className="text-[9px] font-mono text-slate-400 mt-0.5">id: "frontend" (100, 100)</div>
                </div>

                <div className="flex items-center gap-1 text-slate-500 font-mono text-xs">
                  <span className="hidden sm:inline">────</span>
                  <span className="px-1.5 py-0.5 rounded bg-slate-900 border border-slate-800 text-[10px] text-indigo-300">
                    connection-1
                  </span>
                  <span>──▶</span>
                </div>

                {/* Node 2 */}
                <div className="p-3.5 rounded-xl bg-[#1a0e2e] border-2 border-[#7c3aed] text-center shadow-lg w-40">
                  <div className="text-[10px] font-mono text-purple-400 uppercase">api_gateway</div>
                  <div className="text-xs font-bold text-white mt-1">API Gateway</div>
                  <div className="text-[9px] font-mono text-slate-400 mt-0.5">id: "api" (350, 100)</div>
                </div>

                <div className="flex items-center gap-1 text-slate-500 font-mono text-xs">
                  <span className="hidden sm:inline">────</span>
                  <span className="px-1.5 py-0.5 rounded bg-slate-900 border border-slate-800 text-[10px] text-emerald-300">
                    connection-2
                  </span>
                  <span>──▶</span>
                </div>

                {/* Node 3 */}
                <div className="p-3.5 rounded-xl bg-[#052e1a] border-2 border-[#10b981] text-center shadow-lg w-40">
                  <div className="text-[10px] font-mono text-emerald-400 uppercase">database</div>
                  <div className="text-xs font-bold text-white mt-1">PostgreSQL</div>
                  <div className="text-[9px] font-mono text-slate-400 mt-0.5">id: "database" (600, 100)</div>
                </div>
              </div>
            </div>

            {/* Code Block */}
            <div className="rounded-xl overflow-hidden border border-slate-800 bg-[#070B12]">
              <div className="bg-[#0D121F] px-4 py-2 border-b border-slate-800 flex items-center justify-between">
                <span className="text-xs font-mono text-slate-400">diagram_schema.json</span>
                <span className="text-[10px] font-mono text-slate-500">JSON</span>
              </div>
              <pre className="p-4 text-xs font-mono text-indigo-200 overflow-x-auto leading-relaxed">
{JSON.stringify(EXAMPLE_DIAGRAM_JSON, null, 2)}
              </pre>
            </div>
          </div>

          {/* ── Section 6: REA — Reverse Engineer Anything ──────────────────── */}
          <div
            id="sec-6"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-6"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                6. REA — Reverse Engineer Anything
              </h2>
            </div>

            <div className="space-y-2">
              <h3 className="text-sm sm:text-base font-semibold text-indigo-300">
                6.1 What is REA?
              </h3>
              <p className="text-slate-300 text-sm leading-relaxed">
                REA stands for Reverse Engineer Anything. It is a toolkit designed to help coding agents investigate software systems through structured analysis workflows.
              </p>
              <p className="text-slate-300 text-xs">
                It can be used for suitable reverse-engineering tasks involving: Websites, JavaScript applications, Software projects, Application bundles, Native binaries (where supported), Application behavior and architecture.
              </p>
            </div>

            {/* Installation Box */}
            <div className="space-y-2">
              <h3 className="text-sm font-semibold text-indigo-300">
                6.2 Installation Command
              </h3>
              <div className="flex items-center justify-between p-3.5 rounded-xl bg-[#090D16] border border-emerald-500/40">
                <code className="text-xs sm:text-sm font-mono text-emerald-300 font-bold">
                  npx rea-agents@latest setup
                </code>
                <button
                  onClick={() => handleCopyCmd('npx rea-agents@latest setup')}
                  className="px-3 py-1.5 rounded-lg text-xs font-mono bg-emerald-950/80 hover:bg-emerald-900 border border-emerald-600/50 text-emerald-200 flex items-center gap-1.5"
                >
                  {copiedCmd ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                  <span>{copiedCmd ? 'Copied' : 'Copy'}</span>
                </button>
              </div>
            </div>

            {/* Proposed Setup Process */}
            <div className="space-y-2">
              <h3 className="text-sm font-semibold text-indigo-300">
                6.3 Proposed Setup Process
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                {[
                  '1. Check Node.js and npm',
                  '2. Select a supported coding agent',
                  '3. Run the REA setup command',
                  '4. Review proposed config changes',
                  '5. Approve the setup',
                  '6. Restart the coding agent',
                  '7. Run diagnostics',
                  '8. Verify MCP connectivity',
                  '9. Verify REA tools available',
                ].map((step, idx) => (
                  <div key={idx} className="p-2.5 rounded-lg bg-slate-900/90 border border-slate-800 text-slate-300 font-mono">
                    {step}
                  </div>
                ))}
              </div>
            </div>

            {/* Diagnostics */}
            <div className="space-y-2">
              <h3 className="text-sm font-semibold text-indigo-300">
                6.4 Installation Verification
              </h3>
              <p className="text-xs text-slate-400">For Codex, the documented diagnostic command is:</p>
              <div className="p-3 rounded-lg bg-[#070B12] border border-slate-800 font-mono text-xs text-indigo-300 flex items-center justify-between">
                <span>npx -y rea-agents@latest doctor --client codex --json</span>
                <button
                  onClick={() => handleCopyCmd('npx -y rea-agents@latest doctor --client codex --json')}
                  className="text-slate-400 hover:text-white"
                >
                  <Copy className="w-3 h-3" />
                </button>
              </div>
              <p className="text-xs text-slate-400 pt-1">Expected health indicator:</p>
              <pre className="p-3 rounded-lg bg-[#070B12] border border-slate-800 font-mono text-xs text-emerald-400">
{`{
  "healthy": true
}`}
              </pre>
            </div>

            {/* Setup limitation */}
            <div className="p-4 rounded-xl bg-rose-950/30 border border-rose-800/40 text-rose-200 text-xs leading-relaxed space-y-1">
              <p className="font-bold text-rose-300">6.5 Important Setup Limitation</p>
              <p>
                The installation requires execution in a supported local development environment. A browser-based ChatGPT conversation does not automatically provide access to the user's local terminal. Therefore, the installation must be performed and verified in the selected coding agent's environment.
              </p>
              <p className="font-mono text-[11px] text-amber-300 font-semibold pt-1">
                Current status: Setup plan prepared; installation and local verification pending.
              </p>
            </div>
          </div>

          {/* ── Section 7: Reverse-Engineering Methodology ──────────────────── */}
          <div
            id="sec-7"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-5"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-amber-400" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                7. Reverse-Engineering Methodology for SystemSketcher
              </h2>
            </div>

            <p className="text-slate-300 text-sm">
              A complete technical investigation should be divided into five phases:
            </p>

            <div className="grid grid-cols-1 md:grid-cols-5 gap-3">
              {[
                {
                  phase: 'Phase 1',
                  name: 'Public Website Analysis',
                  inspect: 'Homepage, product description, navigation, sample architectures, export options, docs, pricing.',
                  deliverable: 'Product specification',
                },
                {
                  phase: 'Phase 2',
                  name: 'Browser Interaction Analysis',
                  inspect: 'Main canvas, component sidebar, toolbar, search, dialogs, drag & drop, shortcuts, AI workflows.',
                  deliverable: 'UI component inventory & interaction map',
                },
                {
                  phase: 'Phase 3',
                  name: 'Network Investigation',
                  inspect: 'Initial load, canvas init, search, diagram gen, AI requests, saving, exporting. API endpoints & formats.',
                  deliverable: 'Network & API behavior report',
                },
                {
                  phase: 'Phase 4',
                  name: 'Frontend Asset Analysis',
                  inspect: 'JS bundles, CSS, component definitions, dependencies, icon assets, state, serialization, routing.',
                  deliverable: 'Frontend technology report',
                },
                {
                  phase: 'Phase 5',
                  name: 'Technical Reconstruction',
                  inspect: 'Combine findings into PRD, system architecture, UI hierarchy, data model, API map, roadmap.',
                  deliverable: 'Full technical reconstruction doc',
                },
              ].map((p, idx) => (
                <div key={idx} className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-2 flex flex-col justify-between">
                  <div className="space-y-1.5">
                    <span className="text-[10px] font-mono uppercase text-indigo-400 font-bold">{p.phase}</span>
                    <h4 className="text-xs font-bold text-white leading-snug">{p.name}</h4>
                    <p className="text-[11px] text-slate-400 leading-relaxed">{p.inspect}</p>
                  </div>
                  <div className="pt-2 border-t border-slate-800">
                    <span className="text-[10px] text-emerald-400 font-mono block">
                      📌 {p.deliverable}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* ── Section 8: Recommended Technology Stack ─────────────────────── */}
          <div
            id="sec-8"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-6"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-indigo-400" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                8. Recommended Technology Stack for Building a Similar Product
              </h2>
            </div>

            <p className="text-xs text-slate-400 italic">
              The following is a proposed stack, not a statement of SystemSketcher's actual stack.
            </p>

            {/* Tech Stack Table */}
            <div className="overflow-x-auto rounded-xl border border-slate-800 bg-[#090D16]">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-900/90 border-b border-slate-800 text-slate-400 font-mono uppercase text-[10px]">
                  <tr>
                    <th className="py-2.5 px-4">Layer</th>
                    <th className="py-2.5 px-4">Recommended Technology</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60 font-mono text-slate-300">
                  {TECH_STACK_TABLE.map((row) => (
                    <tr key={row.layer} className="hover:bg-slate-800/30">
                      <td className="py-2 px-4 font-semibold text-indigo-300">{row.layer}</td>
                      <td className="py-2 px-4 text-slate-200">{row.tech}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Suggested Development Priorities */}
            <div className="space-y-3 pt-2">
              <h3 className="text-sm font-semibold text-indigo-300">
                Suggested Development Priorities (Stages 1 — 5)
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-5 gap-3">
                <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1">
                  <span className="text-[10px] font-mono text-indigo-400 font-bold">Stage 1</span>
                  <p className="text-xs font-semibold text-white">Core Editor</p>
                  <p className="text-[11px] text-slate-400">Canvas, Drag-and-drop, Nodes/edges, Selection, Zoom/pan, Undo/redo.</p>
                </div>
                <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1">
                  <span className="text-[10px] font-mono text-blue-400 font-bold">Stage 2</span>
                  <p className="text-xs font-semibold text-white">Component Library</p>
                  <p className="text-[11px] text-slate-400">Search, Categories, Vendor icons, Custom items, Properties.</p>
                </div>
                <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1">
                  <span className="text-[10px] font-mono text-cyan-400 font-bold">Stage 3</span>
                  <p className="text-xs font-semibold text-white">Diagram Engine</p>
                  <p className="text-[11px] text-slate-400">JSON schema, Import/export, Validation, Auto-layout, Restoration.</p>
                </div>
                <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1">
                  <span className="text-[10px] font-mono text-purple-400 font-bold">Stage 4</span>
                  <p className="text-xs font-semibold text-white">AI Integration</p>
                  <p className="text-[11px] text-slate-400">NL generation, Suggestions, Structured modifications, Validation.</p>
                </div>
                <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1">
                  <span className="text-[10px] font-mono text-emerald-400 font-bold">Stage 5</span>
                  <p className="text-xs font-semibold text-white">Product Features</p>
                  <p className="text-[11px] text-slate-400">PNG export, Templates, Saving, Sharing, User accounts.</p>
                </div>
              </div>
            </div>
          </div>

          {/* ── Section 9: Final Assessment ─────────────────────────────────── */}
          <div
            id="sec-9"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-5"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-rose-400" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                9. Final Assessment
              </h2>
            </div>

            <p className="text-slate-300 text-sm leading-relaxed">
              SystemSketcher's product concept is built around a straightforward but valuable idea: make software architecture design visual, accessible, reusable, and AI-assisted.
            </p>

            <div className="space-y-2">
              <p className="text-xs font-semibold text-slate-300">Its most important product assets are:</p>
              <ol className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2 text-xs">
                {[
                  '1. Interactive architecture editor',
                  '2. Extensive component library',
                  '3. Underlying diagram data model',
                  '4. AI-assisted generation & refinement',
                  '5. Reusable architecture templates',
                  '6. Export and integration capabilities',
                ].map((item) => (
                  <li key={item} className="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300 font-medium">
                    {item}
                  </li>
                ))}
              </ol>
            </div>

            <p className="text-xs text-indigo-300 font-medium leading-relaxed bg-indigo-950/40 border border-indigo-800/40 p-3 rounded-xl">
              For someone looking to develop a similar product, the diagram engine and component library are the foundational investments. AI should be built on top of a reliable structured diagram model rather than used as a substitute for one.
            </p>

            {/* Research Confidence Table */}
            <div className="space-y-2 pt-2">
              <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wide">
                Research Confidence Matrix
              </h3>
              <div className="overflow-x-auto rounded-xl border border-slate-800 bg-[#090D16]">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-900/90 border-b border-slate-800 text-slate-400 font-mono uppercase text-[10px]">
                    <tr>
                      <th className="py-2 px-4">Area</th>
                      <th className="py-2 px-4">Confidence</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800/60 font-mono">
                    {RESEARCH_CONFIDENCE_TABLE.map((row) => (
                      <tr key={row.area} className="hover:bg-slate-800/30">
                        <td className="py-1.5 px-4 text-slate-300">{row.area}</td>
                        <td className="py-1.5 px-4">
                          <span
                            className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                              row.confidence === 'High'
                                ? 'bg-emerald-950 text-emerald-400 border border-emerald-800/50'
                                : row.confidence === 'Pending'
                                ? 'bg-amber-950 text-amber-400 border border-amber-800/50'
                                : 'bg-slate-800 text-slate-400 border border-slate-700'
                            }`}
                          >
                            {row.confidence}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          {/* ── Section 10: Next Steps (Interactive Whiteboard Checklist) ────── */}
          <div
            id="sec-10"
            className="bg-[#111726]/90 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl space-y-5"
          >
            <div className="flex items-center gap-2 border-b border-slate-800/80 pb-3">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              <h2 className="text-lg sm:text-xl font-bold text-white tracking-tight">
                10. Next Steps
              </h2>
            </div>

            <p className="text-slate-300 text-xs">
              The recommended next actions are (interactive whiteboard checklist):
            </p>

            <div className="space-y-2">
              {NEXT_STEPS_CHECKLIST.map((step, idx) => {
                const isChecked = !!checkedItems[idx]
                return (
                  <div
                    key={idx}
                    onClick={() => toggleCheck(idx)}
                    className={`flex items-center gap-3 p-2.5 rounded-xl border transition-all cursor-pointer ${
                      isChecked
                        ? 'bg-emerald-950/20 border-emerald-800/50 text-emerald-300'
                        : 'bg-slate-900/80 border-slate-800/90 text-slate-300 hover:border-slate-700'
                    }`}
                  >
                    <div
                      className={`w-4 h-4 rounded flex items-center justify-center border transition-colors ${
                        isChecked
                          ? 'bg-emerald-500 border-emerald-400 text-black'
                          : 'border-slate-600 bg-slate-950'
                      }`}
                    >
                      {isChecked && <Check className="w-3 h-3 stroke-[3]" />}
                    </div>
                    <span className={`text-xs ${isChecked ? 'line-through text-slate-500' : ''}`}>
                      {step}
                    </span>
                  </div>
                )
              })}
            </div>

            <div className="p-4 rounded-xl bg-indigo-950/40 border border-indigo-700/50 space-y-1 text-xs">
              <p className="font-bold text-indigo-300">Final Objective</p>
              <p className="text-slate-300 leading-relaxed">
                Move from a high-level understanding of SystemSketcher to an evidence-backed technical specification that can guide the development of a comparable system architecture design platform.
              </p>
            </div>

            <div className="p-3.5 rounded-xl bg-amber-950/40 border border-amber-800/50 text-amber-200/90 text-xs leading-relaxed">
              <strong>Important:</strong> This document is an initial public-product analysis and proposed technical reconstruction. It is not a completed source-code reverse engineering report or proof of REA installation.
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
