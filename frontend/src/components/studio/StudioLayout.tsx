import { useEffect, useState } from 'react'
import {
  Server,
  ShieldCheck,
  BookOpen,
  DollarSign,
  ChevronLeft,
  LayoutGrid,
  MessageSquare,
  Sparkles,
  CheckCircle2,
  AlertOctagon,
  PanelRightClose,
  PanelRightOpen,
  GitCompareArrows,
  Loader2,
  X,
} from 'lucide-react'
import { useStudioStore, type CanvasTab } from '../../store/studioStore'
import { api } from '../../api/client'
import type { DesignRequirements, DesignVersionResponse } from '../../types/api'
import ArchCanvas from './ArchCanvas'
import ComponentTab from './tabs/ComponentTab'
import ValidationTab from './tabs/ValidationTab'
import EvidenceTab from './tabs/EvidenceTab'
import CostTab from './tabs/CostTab'

const TABS: { id: CanvasTab; label: string; icon: React.ReactNode }[] = [
  { id: 'component', label: 'Component', icon: <Server className="w-3.5 h-3.5" /> },
  { id: 'validation', label: 'Validation', icon: <ShieldCheck className="w-3.5 h-3.5" /> },
  { id: 'evidence', label: 'Evidence', icon: <BookOpen className="w-3.5 h-3.5" /> },
  { id: 'cost', label: 'Cost', icon: <DollarSign className="w-3.5 h-3.5" /> },
]

function TabBadge({ tab }: { tab: CanvasTab }) {
  const { activeDesign, canvasNodes } = useStudioStore()
  if (tab === 'validation' && activeDesign) {
    const errors = activeDesign.validation_issues.filter((i) => i.severity === 'error').length
    const warnings = activeDesign.validation_issues.filter((i) => i.severity === 'warning').length
    if (errors > 0)
      return <span className="ml-1 px-1.5 py-0.5 rounded-full text-[9px] bg-rose-900/60 text-rose-300 border border-rose-700/50">{errors}</span>
    if (warnings > 0)
      return <span className="ml-1 px-1.5 py-0.5 rounded-full text-[9px] bg-amber-900/60 text-amber-300 border border-amber-700/50">{warnings}</span>
    return <CheckCircle2 className="w-3 h-3 text-emerald-400 ml-1" />
  }
  if (tab === 'evidence' && activeDesign) {
    return <span className="ml-1 text-[9px] text-indigo-400">{activeDesign.evidence_links.length}</span>
  }
  if (tab === 'component') {
    return <span className="ml-1 text-[9px] text-slate-500">{canvasNodes.length}</span>
  }
  return null
}

function makeDesignDiff(
  previous: DesignVersionResponse,
  next: DesignVersionResponse,
  affectedNodeIds: string[],
) {
  const oldNodes = new Map(previous.nodes.map((node) => [node.id, node]))
  const newNodes = new Map(next.nodes.map((node) => [node.id, node]))
  const addedNodes = next.nodes
    .filter((node) => !oldNodes.has(node.id))
    .map((node) => node.slug)
  const removedNodes = previous.nodes
    .filter((node) => !newNodes.has(node.id))
    .map((node) => node.slug)
  const updatedNodes = next.nodes
    .filter((node) => {
      const oldNode = oldNodes.get(node.id)
      return oldNode !== undefined && JSON.stringify(oldNode) !== JSON.stringify(node)
    })
    .map((node) => node.slug)
  const oldEdges = new Set(previous.edges.map((edge) =>
    `${edge.source_id}->${edge.target_id}:${edge.protocol ?? ''}`,
  ))
  const nextNodeNames = new Map(next.nodes.map((node) => [node.id, node.slug]))
  const previousNodeNames = new Map(previous.nodes.map((node) => [node.id, node.slug]))
  const edgeLabel = (
    edge: DesignVersionResponse['edges'][number],
    nodeNames: Map<string, string>,
  ) => `${nodeNames.get(edge.source_id) ?? edge.source_id} → ${
    nodeNames.get(edge.target_id) ?? edge.target_id
  }${edge.protocol ? ` (${edge.protocol})` : ''}`
  const nextEdges = new Set(next.edges.map((edge) =>
    `${edge.source_id}->${edge.target_id}:${edge.protocol ?? ''}`,
  ))
  const requirementKeys: (keyof DesignRequirements)[] = [
    'expected_users',
    'expected_qps',
    'availability_target',
    'data_durability_required',
    'regions',
  ]
  const changedRequirements = requirementKeys.filter(
    (key) => previous.requirements[key] !== next.requirements[key],
  )

  return {
    fromVersion: previous.version_number,
    toVersion: next.version_number,
    addedNodes,
    removedNodes,
    updatedNodes,
    changedRequirements,
    addedEdges: next.edges
      .filter((edge) => !oldEdges.has(`${edge.source_id}->${edge.target_id}:${edge.protocol ?? ''}`))
      .map((edge) => edgeLabel(edge, nextNodeNames)),
    removedEdges: previous.edges
      .filter((edge) => !nextEdges.has(`${edge.source_id}->${edge.target_id}:${edge.protocol ?? ''}`))
      .map((edge) => edgeLabel(edge, previousNodeNames)),
    affectedNodeIds,
  }
}

function RedesignDialog({ onClose }: { onClose: () => void }) {
  const {
    activeProject,
    activeDesign,
    selectedNodeId,
    setActiveDesign,
    setCanvasFromDesign,
    setRedesignDiff,
  } = useStudioStore()
  const [changeDescription, setChangeDescription] = useState('')
  const [affectedNodeIds, setAffectedNodeIds] = useState<string[]>(
    selectedNodeId ? [selectedNodeId] : [],
  )
  const [requirements, setRequirements] = useState<DesignRequirements>(
    activeDesign?.requirements ?? {
      expected_users: null,
      expected_qps: null,
      availability_target: null,
      data_durability_required: true,
      regions: 1,
    },
  )
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  if (!activeDesign || !activeProject) return null

  const toggleNode = (nodeId: string) => {
    setAffectedNodeIds((current) =>
      current.includes(nodeId)
        ? current.filter((id) => id !== nodeId)
        : [...current, nodeId],
    )
  }
  const updateNumber = (
    field: 'expected_users' | 'expected_qps' | 'availability_target' | 'regions',
    value: string,
  ) => {
    setRequirements((current) => ({
      ...current,
      [field]: value === '' && field !== 'regions' ? null : Number(value),
    }))
  }
  const submit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setLoading(true)
    setError(null)
    try {
      const updated = await api.redesign(activeProject.id, {
        change_description: changeDescription,
        requirements,
        affected_node_ids: affectedNodeIds,
      })
      setRedesignDiff(makeDesignDiff(
        activeDesign,
        updated,
        updated.affected_node_ids ?? affectedNodeIds,
      ))
      setActiveDesign(updated)
      setCanvasFromDesign(updated)
      onClose()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Redesign failed.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4">
      <form
        onSubmit={submit}
        className="w-full max-w-xl max-h-[90vh] overflow-y-auto rounded-2xl border border-slate-700 bg-[#111726] shadow-2xl"
      >
        <div className="flex items-center justify-between border-b border-slate-800 p-4">
          <div>
            <h2 className="text-sm font-semibold text-white">Iterative redesign</h2>
            <p className="mt-1 text-xs text-slate-400">
              Re-plan the affected subgraph; unchanged components remain intact.
            </p>
          </div>
          <button type="button" onClick={onClose} className="text-slate-400 hover:text-white" aria-label="Close redesign">
            <X className="h-4 w-4" />
          </button>
        </div>
        <div className="space-y-5 p-4">
          <label className="block text-xs font-medium text-slate-300">
            What changed?
            <textarea
              required
              minLength={5}
              value={changeDescription}
              onChange={(event) => setChangeDescription(event.target.value)}
              placeholder="e.g. Increase expected users to 500,000, or replace the primary database"
              className="mt-1.5 min-h-20 w-full resize-y rounded-xl border border-slate-700 bg-[#0B0F17] p-3 text-sm text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:outline-none"
            />
          </label>

          <fieldset>
            <legend className="text-xs font-medium text-slate-300">
              Requirements (change only what needs updating)
            </legend>
            <div className="mt-2 grid grid-cols-2 gap-3">
              {([
                ['expected_users', 'Concurrent users'],
                ['expected_qps', 'Peak QPS'],
                ['availability_target', 'Availability %'],
                ['regions', 'Regions'],
              ] as const).map(([field, label]) => (
                <label key={field} className="text-[11px] text-slate-400">
                  {label}
                  <input
                    type="number"
                    min={field === 'availability_target' ? 0 : field === 'regions' ? 1 : 0}
                    max={field === 'availability_target' ? 100 : undefined}
                    step={field === 'availability_target' ? 0.01 : 1}
                    value={requirements[field] ?? ''}
                    onChange={(event) => updateNumber(field, event.target.value)}
                    className="mt-1 block w-full rounded-lg border border-slate-700 bg-[#0B0F17] px-2.5 py-2 text-slate-100 focus:border-indigo-500 focus:outline-none"
                  />
                </label>
              ))}
            </div>
            <label className="mt-3 flex items-center gap-2 text-xs text-slate-300">
              <input
                type="checkbox"
                checked={requirements.data_durability_required}
                onChange={(event) => setRequirements((current) => ({
                  ...current,
                  data_durability_required: event.target.checked,
                }))}
                className="accent-indigo-500"
              />
              Durable storage is required
            </label>
          </fieldset>

          <fieldset>
            <legend className="text-xs font-medium text-slate-300">
              Focus nodes (optional; requirement changes are detected automatically)
            </legend>
            <div className="mt-2 max-h-36 space-y-1 overflow-y-auto rounded-xl border border-slate-800 p-2">
              {activeDesign.nodes.map((node) => (
                <label key={node.id} className="flex items-center gap-2 rounded-lg px-2 py-1.5 text-xs text-slate-300 hover:bg-slate-800/60">
                  <input
                    type="checkbox"
                    checked={affectedNodeIds.includes(node.id)}
                    onChange={() => toggleNode(node.id)}
                    className="accent-indigo-500"
                  />
                  <span className="font-mono">{node.slug}</span>
                  <span className="ml-auto text-slate-500">{node.category}</span>
                </label>
              ))}
            </div>
          </fieldset>
          {error && (
            <p role="alert" className="rounded-lg border border-rose-800/60 bg-rose-950/40 p-3 text-xs text-rose-300">
              {error}
            </p>
          )}
        </div>
        <div className="flex justify-end gap-2 border-t border-slate-800 p-4">
          <button type="button" onClick={onClose} className="rounded-lg px-3 py-2 text-xs text-slate-300 hover:bg-slate-800">
            Cancel
          </button>
          <button
            type="submit"
            disabled={loading || changeDescription.trim().length < 5}
            className="flex items-center gap-2 rounded-lg bg-indigo-600 px-4 py-2 text-xs font-semibold text-white hover:bg-indigo-500 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <GitCompareArrows className="h-3.5 w-3.5" />}
            {loading ? 'Re-planning…' : 'Re-plan affected subgraph'}
          </button>
        </div>
      </form>
    </div>
  )
}

export default function StudioLayout() {
  const {
    activeProject,
    activeDesign,
    activeCanvasTab,
    setCanvasTab,
    setView,
    sidebarOpen,
    setSidebarOpen,
    setCatalog,
    catalogLoaded,
    canvasNodes,
    redesignDiff,
  } = useStudioStore()
  const [redesignOpen, setRedesignOpen] = useState(false)

  // Load catalog if not loaded
  useEffect(() => {
    if (!catalogLoaded) {
      api.getComponents(150).then((r) => setCatalog(r.items)).catch(() => {})
    }
  }, [catalogLoaded])

  const validationSummary = activeDesign?.is_valid
    ? { label: 'Valid', cls: 'text-emerald-400', icon: <CheckCircle2 className="w-3 h-3" /> }
    : activeDesign
    ? { label: `${activeDesign.validation_issues.filter(i => i.severity === 'error').length} errors`, cls: 'text-rose-400', icon: <AlertOctagon className="w-3 h-3" /> }
    : null

  return (
    <div className="flex flex-col h-full min-h-0">
      {/* Canvas toolbar */}
      <div className="h-11 flex items-center justify-between px-4 border-b border-slate-800/80 bg-[#0d1117]/90 flex-shrink-0">
        <div className="flex items-center gap-3">
          <button
            onClick={() => setView('projects')}
            className="flex items-center gap-1.5 text-slate-400 hover:text-slate-200 text-xs font-medium transition-colors"
          >
            <ChevronLeft className="w-3.5 h-3.5" />
            Projects
          </button>
          <span className="text-slate-700">/</span>
          <span className="text-slate-300 text-xs font-medium truncate max-w-[160px]">
            {activeProject?.name ?? 'Unnamed'}
          </span>
          {activeDesign && (
            <>
              <span className="text-slate-700">/</span>
              <span className="text-slate-500 text-xs font-mono">v{activeDesign.version_number}</span>
            </>
          )}
        </div>

        <div className="flex items-center gap-3">
          {validationSummary && (
            <div className={`flex items-center gap-1 text-xs ${validationSummary.cls}`}>
              {validationSummary.icon}
              <span className="font-mono">{validationSummary.label}</span>
            </div>
          )}

          <button
            onClick={() => setRedesignOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-indigo-950/60 hover:bg-indigo-900/60 border border-indigo-800/50 text-indigo-300 text-xs font-medium transition-all"
          >
            <Sparkles className="w-3 h-3" />
            Redesign
          </button>

          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="p-1.5 rounded-lg bg-slate-800/60 hover:bg-slate-800 text-slate-400 hover:text-white transition-all"
          >
            {sidebarOpen ? <PanelRightClose className="w-4 h-4" /> : <PanelRightOpen className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {redesignDiff && (
        <details className="border-b border-indigo-900/60 bg-indigo-950/20 px-4 py-2 text-xs">
          <summary className="cursor-pointer list-none text-indigo-200">
            <GitCompareArrows className="mr-1.5 inline h-3.5 w-3.5" />
            Version diff: v{redesignDiff.fromVersion} → v{redesignDiff.toVersion}
            <span className="ml-2 text-slate-400">
              {redesignDiff.addedNodes.length} added · {redesignDiff.removedNodes.length} removed · {redesignDiff.updatedNodes.length} updated nodes
            </span>
          </summary>
          <div className="mt-2 grid gap-1 text-slate-300 sm:grid-cols-2">
            <p>Changed requirements: {redesignDiff.changedRequirements.join(', ') || 'none'}</p>
            <p>
              Connections: +{redesignDiff.addedEdges.length} / −{redesignDiff.removedEdges.length}
            </p>
            <p>Added: {redesignDiff.addedEdges.join(', ') || 'none'}</p>
            <p>Removed: {redesignDiff.removedEdges.join(', ') || 'none'}</p>
            <p>Replanned node IDs: {redesignDiff.affectedNodeIds.join(', ') || 'inferred from requirements'}</p>
            <p>
              Nodes: {[
                ...redesignDiff.addedNodes.map((name) => `+ ${name}`),
                ...redesignDiff.removedNodes.map((name) => `− ${name}`),
                ...redesignDiff.updatedNodes.map((name) => `~ ${name}`),
              ].join(', ') || 'no node-level changes'}
            </p>
          </div>
        </details>
      )}

      {/* Canvas area + sidebar */}
      <div className="flex flex-1 min-h-0 overflow-hidden">
        {/* Canvas */}
        <div className="flex-1 min-w-0 relative">
          {canvasNodes.length === 0 ? (
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="text-center space-y-4">
                <LayoutGrid className="w-12 h-12 text-slate-700 mx-auto" />
                <p className="text-slate-400 text-sm font-semibold">Canvas is empty</p>
                <p className="text-slate-600 text-xs">
                  Generate a plan first, or add components manually with the button below.
                </p>
                <div className="flex flex-col sm:flex-row gap-2 justify-center">
                  <button
                    onClick={() => setView('interview')}
                    className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold transition-all"
                  >
                    <MessageSquare className="w-3.5 h-3.5" />
                    Start Interview
                  </button>
                </div>
              </div>
            </div>
          ) : (
            <div className="absolute inset-0">
              <ArchCanvas key={activeDesign?.id ?? 'manual'} />
            </div>
          )}
        </div>

        {/* Right sidebar */}
        {sidebarOpen && (
          <div className="w-72 flex-shrink-0 border-l border-slate-800/80 bg-[#0d1117] flex flex-col overflow-hidden">
            {/* Tab bar */}
            <div className="flex border-b border-slate-800/80 flex-shrink-0">
              {TABS.map((tab) => (
                <button
                  key={tab.id}
                  onClick={() => setCanvasTab(tab.id)}
                  className={`flex-1 flex items-center justify-center gap-1 py-2.5 text-[11px] font-medium transition-all ${
                    activeCanvasTab === tab.id
                      ? 'text-white border-b-2 border-indigo-500 bg-indigo-950/20'
                      : 'text-slate-500 hover:text-slate-300'
                  }`}
                >
                  {tab.icon}
                  <span className="hidden sm:inline">{tab.label}</span>
                  <TabBadge tab={tab.id} />
                </button>
              ))}
            </div>

            {/* Tab content */}
            <div className="flex-1 overflow-hidden flex flex-col min-h-0">
              {activeCanvasTab === 'component' && <ComponentTab />}
              {activeCanvasTab === 'validation' && <ValidationTab />}
              {activeCanvasTab === 'evidence' && <EvidenceTab />}
              {activeCanvasTab === 'cost' && <CostTab />}
            </div>
          </div>
        )}
      </div>
      {redesignOpen && <RedesignDialog onClose={() => setRedesignOpen(false)} />}
    </div>
  )
}
