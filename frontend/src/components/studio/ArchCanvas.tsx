import { useCallback, useEffect, useMemo, useState } from 'react'
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  addEdge,
  useNodesState,
  useEdgesState,
  Handle,
  Position,
  type Node,
  type Edge,
  type Connection,
  type NodeTypes,
  BackgroundVariant,
  Panel,
  MarkerType,
} from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import { useStudioStore } from '../../store/studioStore'
import { api } from '../../api/client'
import type { DesignNode, DesignEdge } from '../../types/api'
import type { ComponentItem } from '../../types/catalog'
import {
  Plus,
  Search,
  X,
  AlertCircle,
  CheckCircle2,
  Loader2,
} from 'lucide-react'

// ── Category colors ──────────────────────────────────────────────────────────

const CAT_GRADIENT: Record<string, { bg: string; border: string; text: string }> = {
  cdn:          { bg: '#0c1d2e', border: '#0ea5e9', text: '#7dd3fc' },
  gateway:      { bg: '#1a0e2e', border: '#7c3aed', text: '#c4b5fd' },
  compute:      { bg: '#0e1a2e', border: '#3b82f6', text: '#93c5fd' },
  cache:        { bg: '#2e1e07', border: '#d97706', text: '#fcd34d' },
  database:     { bg: '#052e1a', border: '#10b981', text: '#6ee7b7' },
  queue:        { bg: '#2e1007', border: '#ea580c', text: '#fdba74' },
  streaming:    { bg: '#2e0a0a', border: '#ef4444', text: '#fca5a5' },
  storage:      { bg: '#052e2e', border: '#14b8a6', text: '#5eead4' },
  auth:         { bg: '#1a0e2e', border: '#9333ea', text: '#d8b4fe' },
  search:       { bg: '#0a0e2e', border: '#6366f1', text: '#a5b4fc' },
  notification: { bg: '#2e0a1a', border: '#ec4899', text: '#f9a8d4' },
  observability:{ bg: '#111827', border: '#6b7280', text: '#d1d5db' },
  middleware:   { bg: '#0e2e14', border: '#22c55e', text: '#86efac' },
  workflow:     { bg: '#052e2e', border: '#06b6d4', text: '#67e8f9' },
  analytics:    { bg: '#2e0e2e', border: '#a855f7', text: '#e879f9' },
}

const LAYER_LABELS: Record<string, string> = {
  edge: 'Edge',
  gateway: 'Gateway',
  application: 'App',
  data: 'Data',
  async: 'Async',
  infra: 'Infra',
  observability: 'Obs',
}

// ── Custom node ─────────────────────────────────────────────────────────────

function ArchNode({ data }: { data: any }) {
  const colors = CAT_GRADIENT[data.category] ?? { bg: '#111827', border: '#4b5563', text: '#d1d5db' }
  return (
    <div
      className="rounded-xl px-3.5 py-2.5 min-w-[140px] max-w-[200px] cursor-pointer transition-all duration-150 relative shadow-lg"
      style={{
        background: colors.bg,
        border: `1.5px solid ${colors.border}`,
        boxShadow: data.selected
          ? `0 0 0 2px ${colors.border}, 0 4px 24px ${colors.border}50`
          : `0 2px 8px rgba(0,0,0,0.4)`,
      }}
    >
      <Handle
        type="target"
        position={Position.Top}
        className="!w-2.5 !h-2.5 !bg-indigo-400 !border-2 !border-[#0B0F17]"
      />
      <div className="flex items-center gap-1.5 mb-1">
        <div
          className="w-2 h-2 rounded-full flex-shrink-0"
          style={{ background: colors.border }}
        />
        <span className="text-[9px] font-mono uppercase tracking-wide" style={{ color: colors.text }}>
          {data.category} · {LAYER_LABELS[data.layer] ?? data.layer}
        </span>
      </div>
      <p className="text-white text-xs font-semibold leading-snug">{data.label}</p>
      <p className="text-[9px] font-mono mt-0.5" style={{ color: colors.text + 'cc' }}>
        {data.slug}
      </p>
      {data.replicas > 1 && (
        <span className="text-[9px] font-mono mt-1 inline-block px-1.5 py-0.5 rounded"
          style={{ background: colors.border + '30', color: colors.text }}>
          ×{data.replicas}
        </span>
      )}
      <Handle
        type="source"
        position={Position.Bottom}
        className="!w-2.5 !h-2.5 !bg-indigo-400 !border-2 !border-[#0B0F17]"
      />
    </div>
  )
}

const nodeTypes: NodeTypes = { arch: ArchNode }

// ── Add Component Drawer ─────────────────────────────────────────────────────

function AddComponentDrawer({ onClose }: { onClose: () => void }) {
  const { catalog, addNode, canvasNodes } = useStudioStore()
  const [search, setSearch] = useState('')
  const [checking, setChecking] = useState<string | null>(null)
  const [checkResult, setCheckResult] = useState<{ slug: string; ok: boolean; reason: string } | null>(null)

  const filtered = catalog.filter(
    (c) =>
      c.is_active &&
      (c.name.toLowerCase().includes(search.toLowerCase()) ||
        c.slug.toLowerCase().includes(search.toLowerCase()) ||
        c.category.toLowerCase().includes(search.toLowerCase()))
  )

  const handleAdd = async (item: ComponentItem) => {
    // If there are existing nodes, check compatibility with first node as quick heuristic
    if (canvasNodes.length > 0) {
      setChecking(item.slug)
      const firstNode = canvasNodes[0]
      try {
        const res = await api.checkCompatibility(firstNode.slug, item.slug)
        setCheckResult({ slug: item.slug, ok: res.compatible, reason: res.reason })
        if (!res.compatible) {
          setTimeout(() => setCheckResult(null), 2500)
          setChecking(null)
          // Still allow adding — it's a warning, not a blocker
        }
      } catch {
        // Silently ignore compatibility check failure
      } finally {
        setChecking(null)
      }
    }

    const newNode: DesignNode = {
      id: `${item.slug}-${Date.now()}`,
      slug: item.slug,
      category: item.category,
      layer: item.layer,
      replicas: 1,
      protocols: item.protocols,
      limits: item.limits,
      config: {},
    }
    addNode(newNode)
    onClose()
  }

  return (
    <div className="absolute inset-y-0 right-0 w-72 bg-[#111726] border-l border-slate-800 flex flex-col z-20 shadow-2xl">
      <div className="flex items-center justify-between p-4 border-b border-slate-800">
        <h3 className="text-sm font-semibold text-white">Add Component</h3>
        <button onClick={onClose} className="text-slate-400 hover:text-white">
          <X className="w-4 h-4" />
        </button>
      </div>
      <div className="p-3 border-b border-slate-800/60">
        <div className="relative">
          <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search catalog…"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full bg-[#0B0F17] border border-slate-700 rounded-xl pl-8 pr-3 py-2 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            autoFocus
          />
        </div>
      </div>
      {checkResult && (
        <div
          className={`mx-3 mt-2 p-2.5 rounded-xl text-[11px] border flex items-start gap-2 ${
            checkResult.ok
              ? 'bg-emerald-950/50 border-emerald-700/40 text-emerald-300'
              : 'bg-amber-950/50 border-amber-700/40 text-amber-300'
          }`}
        >
          {checkResult.ok ? (
            <CheckCircle2 className="w-3.5 h-3.5 flex-shrink-0 mt-0.5" />
          ) : (
            <AlertCircle className="w-3.5 h-3.5 flex-shrink-0 mt-0.5" />
          )}
          <span>{checkResult.reason}</span>
        </div>
      )}
      <div className="flex-1 overflow-y-auto divide-y divide-slate-800/40">
        {filtered.length === 0 ? (
          <p className="p-6 text-center text-xs text-slate-500">No components found.</p>
        ) : (
          filtered.slice(0, 50).map((item) => {
            const colors = CAT_GRADIENT[item.category] ?? { border: '#4b5563', text: '#d1d5db' }
            return (
              <button
                key={item.slug}
                onClick={() => handleAdd(item)}
                disabled={checking === item.slug}
                className="w-full flex items-center gap-3 px-4 py-2.5 hover:bg-slate-800/60 transition-colors text-left group"
              >
                <div
                  className="w-2 h-2 rounded-full flex-shrink-0"
                  style={{ background: colors.border }}
                />
                <div className="flex-1 min-w-0">
                  <p className="text-xs font-semibold text-white group-hover:text-white">{item.name}</p>
                  <p className="text-[10px] font-mono" style={{ color: colors.text + 'bb' }}>
                    {item.slug} · {item.category}
                  </p>
                </div>
                {checking === item.slug ? (
                  <Loader2 className="w-3.5 h-3.5 animate-spin text-slate-400" />
                ) : (
                  <Plus className="w-3.5 h-3.5 text-slate-500 group-hover:text-white transition-colors" />
                )}
              </button>
            )
          })
        )}
      </div>
    </div>
  )
}

// ── Helpers: convert DesignNode/Edge → ReactFlow nodes/edges ────────────────

const LAYER_Y: Record<string, number> = {
  edge: 40,
  gateway: 160,
  application: 290,
  data: 430,
  async: 560,
  infra: 690,
  observability: 820,
}

function designNodesToFlow(nodes: DesignNode[], catalogItems?: ComponentItem[]): Node[] {
  // Group by layer for X positioning
  const layerCount: Record<string, number> = {}
  return nodes.map((n) => {
    const y = LAYER_Y[n.layer] ?? 300
    const idx = layerCount[n.layer] ?? 0
    layerCount[n.layer] = idx + 1
    const x = 100 + idx * 260
    const item = catalogItems?.find((c) => c.slug === n.slug) ?? (window as any).__catalog?.find((c: any) => c.slug === n.slug)
    return {
      id: n.id,
      type: 'arch',
      position: { x, y },
      data: {
        label: item?.name ?? n.slug,
        slug: n.slug,
        category: n.category,
        layer: n.layer,
        replicas: n.replicas,
      },
    }
  })
}

function designEdgesToFlow(edges: DesignEdge[]): Edge[] {
  return edges.map((e, idx) => ({
    id: `e-${e.source_id}-${e.target_id}-${idx}`,
    source: e.source_id,
    target: e.target_id,
    type: 'smoothstep',
    label: e.label ?? e.protocol ?? undefined,
    animated: true,
    markerEnd: { type: MarkerType.ArrowClosed, color: '#6366f1' },
    style: { stroke: '#6366f1', strokeWidth: 1.5 },
    labelStyle: { fill: '#94a3b8', fontSize: 10, fontFamily: 'monospace' },
    labelBgStyle: { fill: '#0B0F17', fillOpacity: 0.9 },
  }))
}

// ── Main Canvas ─────────────────────────────────────────────────────────────

export default function ArchCanvas() {
  const {
    canvasNodes,
    canvasEdges,
    addEdge: storeAddEdge,
    removeEdge: storeRemoveEdge,
    setSelectedNode,
    selectedNodeId,
    catalog,
  } = useStudioStore()

  // Expose catalog on window for designNodesToFlow helper
  useEffect(() => {
    ;(window as any).__catalog = catalog
  }, [catalog])

  const initNodes = useMemo(() => designNodesToFlow(canvasNodes, catalog), [canvasNodes, catalog])
  const initEdges = useMemo(() => designEdgesToFlow(canvasEdges), [canvasEdges])

  const [rfNodes, setRfNodes, onNodesChange] = useNodesState(initNodes)
  const [rfEdges, setRfEdges, onEdgesChange] = useEdgesState(initEdges)
  const [showAddDrawer, setShowAddDrawer] = useState(false)

  // Sync store → ReactFlow when canvasNodes/edges change
  useEffect(() => {
    setRfNodes((prev) => {
      const posMap = new Map(prev.map((n) => [n.id, n.position]))
      return designNodesToFlow(canvasNodes, catalog).map((n) => ({
        ...n,
        position: posMap.get(n.id) ?? n.position,
        selected: n.id === selectedNodeId,
        data: { ...n.data, selected: n.id === selectedNodeId },
      }))
    })
  }, [canvasNodes, selectedNodeId, catalog, setRfNodes])

  useEffect(() => {
    setRfEdges(designEdgesToFlow(canvasEdges))
  }, [canvasEdges, setRfEdges])

  const onConnect = useCallback(
    (params: Connection) => {
      if (!params.source || !params.target) return
      setRfEdges((eds) =>
        addEdge(
          {
            ...params,
            animated: true,
            markerEnd: { type: MarkerType.ArrowClosed, color: '#6366f1' },
            style: { stroke: '#6366f1', strokeWidth: 1.5 },
          },
          eds
        )
      )
      storeAddEdge({ source_id: params.source, target_id: params.target })
    },
    [storeAddEdge]
  )

  const onNodeClick = useCallback(
    (_: React.MouseEvent, node: Node) => {
      setSelectedNode(node.id)
    },
    [setSelectedNode]
  )

  const onPaneClick = useCallback(() => {
    setSelectedNode(null)
  }, [setSelectedNode])

  const onEdgesDelete = useCallback(
    (deleted: Edge[]) => {
      deleted.forEach((e) => storeRemoveEdge(e.source, e.target))
    },
    [storeRemoveEdge]
  )

  return (
    <div className="w-full h-full relative" style={{ minHeight: '100%' }}>
      <ReactFlow
        nodes={rfNodes}
        edges={rfEdges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onNodeClick={onNodeClick}
        onPaneClick={onPaneClick}
        onEdgesDelete={onEdgesDelete}
        nodeTypes={nodeTypes}
        fitView
        fitViewOptions={{ padding: 0.2 }}
        proOptions={{ hideAttribution: true }}
        className="bg-[#0B0F17]"
        defaultEdgeOptions={{
          animated: true,
          markerEnd: { type: MarkerType.ArrowClosed, color: '#6366f1' },
          style: { stroke: '#6366f1', strokeWidth: 1.5 },
        }}
      >
        <Background
          variant={BackgroundVariant.Dots}
          gap={28}
          size={1}
          color="#1e293b"
        />
        <Controls
          className="bg-[#111726] border border-slate-700 rounded-xl overflow-hidden shadow-xl"
          showInteractive={false}
          position="bottom-right"
        />
        <MiniMap
          className="border border-slate-700 rounded-xl overflow-hidden shadow-xl"
          nodeColor={(n) => {
            const cat = (n.data as any)?.category ?? ''
            return CAT_GRADIENT[cat]?.border ?? '#4b5563'
          }}
          style={{ background: '#0B0F17', width: 140, height: 90 }}
          position="bottom-right"
        />

        <Panel position="top-right" className="flex gap-2">
          <button
            onClick={() => setShowAddDrawer(true)}
            className="flex items-center gap-1.5 px-3.5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-xl transition-all shadow-lg shadow-indigo-500/25 border border-indigo-500/50"
          >
            <Plus className="w-3.5 h-3.5" />
            Add Component
          </button>
        </Panel>

        {/* Layer guide */}
        <Panel position="bottom-left">
          <div className="bg-[#111726]/90 border border-slate-800 rounded-xl p-3 text-[10px] font-mono space-y-0.5 backdrop-blur-sm">
            <p className="text-slate-500 font-semibold mb-1.5 text-[9px] uppercase tracking-wider">Layer Guide</p>
            {Object.entries(LAYER_Y).map(([layer, y]) => (
              <div key={layer} className="flex items-center gap-2 text-slate-400">
                <span className="w-12 text-[9px] font-mono text-slate-500">y≈{y}</span>
                <span className="capitalize">{layer}</span>
              </div>
            ))}
          </div>
        </Panel>
      </ReactFlow>

      {/* Add Component Drawer overlay */}
      {showAddDrawer && (
        <AddComponentDrawer onClose={() => setShowAddDrawer(false)} />
      )}
    </div>
  )
}
