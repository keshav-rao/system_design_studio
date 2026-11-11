import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
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
  ReactFlowProvider,
  useReactFlow,
} from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import { useStudioStore } from '../../store/studioStore'
import type { DesignNode, DesignEdge } from '../../types/api'
import type { ComponentItem } from '../../types/catalog'
import {
  LayoutDashboard,
  ChevronDown,
  Layers,
  X,
} from 'lucide-react'
import { ARCH_TEMPLATES } from '../../data/archTemplates'
import LeftComponentPalette from './LeftComponentPalette'

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
  const layerCount: Record<string, number> = {}
  return nodes.map((n) => {
    const y = n.position?.y ?? (LAYER_Y[n.layer] ?? 300)
    const idx = layerCount[n.layer] ?? 0
    layerCount[n.layer] = idx + 1
    const x = n.position?.x ?? (100 + idx * 260)
    const item = catalogItems?.find((c) => c.slug === n.slug) ?? (window as any).__catalog?.find((c: any) => c.slug === n.slug)
    return {
      id: n.id,
      type: 'arch',
      position: { x, y },
      data: {
        label: n.label ?? item?.name ?? n.slug,
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

// ── Canvas Inner Component (with useReactFlow hook) ─────────────────────────

function ArchCanvasInner() {
  const {
    canvasNodes,
    canvasEdges,
    addEdge: storeAddEdge,
    removeEdge: storeRemoveEdge,
    setSelectedNode,
    selectedNodeId,
    catalog,
    loadTemplate,
    activeTemplateId,
    addNode,
  } = useStudioStore()

  const { screenToFlowPosition } = useReactFlow()
  const reactFlowWrapper = useRef<HTMLDivElement>(null)

  // Canvas layout states
  const [showLeftPalette, setShowLeftPalette] = useState(true)
  const [showTemplateMenu, setShowTemplateMenu] = useState(false)
  const [showLayerGuide, setShowLayerGuide] = useState(true)

  // Expose catalog on window for designNodesToFlow helper
  useEffect(() => {
    ;(window as any).__catalog = catalog
  }, [catalog])

  const initNodes = useMemo(() => designNodesToFlow(canvasNodes, catalog), [canvasNodes, catalog])
  const initEdges = useMemo(() => designEdgesToFlow(canvasEdges), [canvasEdges])

  const [rfNodes, setRfNodes, onNodesChange] = useNodesState(initNodes)
  const [rfEdges, setRfEdges, onEdgesChange] = useEdgesState(initEdges)

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
    [storeAddEdge, setRfEdges]
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

  // ── Drag and Drop from Left Palette onto Open Canvas ─────────────────────
  const onDragOver = useCallback((event: React.DragEvent) => {
    event.preventDefault()
    event.dataTransfer.dropEffect = 'move'
  }, [])

  const onDrop = useCallback(
    (event: React.DragEvent) => {
      event.preventDefault()
      const raw = event.dataTransfer.getData('application/reactflow-component')
      if (!raw) return
      try {
        const item = JSON.parse(raw) as ComponentItem
        const position = screenToFlowPosition({
          x: event.clientX,
          y: event.clientY,
        })
        const newNode: DesignNode = {
          id: `${item.slug}-${Date.now()}`,
          slug: item.slug,
          category: item.category,
          layer: item.layer,
          replicas: 1,
          protocols: item.protocols,
          limits: item.limits,
          config: {},
          label: item.name,
          position,
        }
        addNode(newNode)
      } catch {}
    },
    [screenToFlowPosition, addNode]
  )

  return (
    <div
      ref={reactFlowWrapper}
      className="w-full h-full min-h-full relative overflow-hidden flex"
      style={{ minHeight: '100%', height: '100%', width: '100%' }}
    >
      {/* ── Requirement 2: Left Component Palette (Canva / Miro layout) ───── */}
      <LeftComponentPalette
        isOpen={showLeftPalette}
        onToggle={() => setShowLeftPalette((v) => !v)}
      />

      {/* ── Main Canvas Workspace ────────────────────────────────────────── */}
      <div className="flex-1 w-full h-full relative overflow-hidden">
        <ReactFlow
          nodes={rfNodes}
          edges={rfEdges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          onNodeClick={onNodeClick}
          onPaneClick={onPaneClick}
          onEdgesDelete={onEdgesDelete}
          onDragOver={onDragOver}
          onDrop={onDrop}
          nodeTypes={nodeTypes}
          fitView
          fitViewOptions={{ padding: 0.2 }}
          proOptions={{ hideAttribution: true }}
          className="bg-[#0B0F17] w-full h-full"
          style={{ width: '100%', height: '100%' }}
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

          {/* Controls & MiniMap in Bottom Right */}
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

          {/* Top Right Panel: Palette Toggle & Template Switcher */}
          <Panel position="top-right" className="flex items-center gap-2">
            <button
              onClick={() => setShowLeftPalette((v) => !v)}
              className={`flex items-center gap-1.5 px-3 py-2 text-xs font-semibold rounded-xl transition-all border shadow-lg backdrop-blur-md ${
                showLeftPalette
                  ? 'bg-indigo-600 text-white border-indigo-400 shadow-indigo-600/30'
                  : 'bg-[#111726]/90 hover:bg-[#1a233b] text-slate-200 border-slate-700/80'
              }`}
              title="Toggle Left Component Palette"
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Components</span>
            </button>

            <div className="relative">
              <button
                onClick={() => setShowTemplateMenu((v) => !v)}
                className="flex items-center gap-1.5 px-3 py-2 bg-[#111726]/90 hover:bg-[#1a233b] text-slate-200 text-xs font-medium rounded-xl transition-all border border-slate-700/80 shadow-lg backdrop-blur-md"
              >
                <LayoutDashboard className="w-3.5 h-3.5 text-indigo-400" />
                Templates
                <ChevronDown className="w-3 h-3 text-slate-400 ml-0.5" />
              </button>
              {showTemplateMenu && (
                <div className="absolute right-0 mt-2 w-72 bg-[#111726] border border-slate-700/80 rounded-2xl shadow-2xl p-2 z-30 divide-y divide-slate-800/60">
                  <div className="px-3 py-1.5">
                    <p className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">Canva Templates</p>
                  </div>
                  <div className="py-1 space-y-1">
                    {Object.values(ARCH_TEMPLATES).map((tmpl) => (
                      <button
                        key={tmpl.id}
                        onClick={() => {
                          loadTemplate(tmpl.id)
                          setShowTemplateMenu(false)
                        }}
                        className={`w-full text-left px-3 py-2.5 rounded-xl text-xs transition-all flex flex-col gap-1 ${
                          activeTemplateId === tmpl.id
                            ? 'bg-indigo-600/20 text-white border border-indigo-500/40'
                            : 'text-slate-300 hover:bg-slate-800/80 border border-transparent'
                        }`}
                      >
                        <div className="flex items-center justify-between">
                          <span className="font-semibold text-white">{tmpl.name}</span>
                          <span className="text-[9px] px-1.5 py-0.5 rounded bg-slate-800 text-indigo-300 font-mono font-medium">
                            {tmpl.badge}
                          </span>
                        </div>
                        <span className="text-[10px] text-slate-400 leading-relaxed line-clamp-2">
                          {tmpl.description}
                        </span>
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </Panel>

          {/* ── Requirement 3: Layer Guide Moved to Bottom Right ────────────── */}
          <Panel position="bottom-right" className="mb-28 mr-0 flex flex-col items-end">
            {showLayerGuide ? (
              <div className="bg-[#111726]/95 border border-slate-700/80 rounded-xl p-3 text-[10px] font-mono space-y-1 backdrop-blur-md shadow-2xl w-44">
                <div className="flex items-center justify-between border-b border-slate-800 pb-1 mb-1">
                  <span className="text-slate-300 font-bold text-[9px] uppercase tracking-wider">
                    Layer Guide
                  </span>
                  <button
                    onClick={() => setShowLayerGuide(false)}
                    className="p-0.5 text-slate-400 hover:text-white rounded"
                    title="Collapse layer guide"
                  >
                    <X className="w-3 h-3" />
                  </button>
                </div>
                {Object.entries(LAYER_Y).map(([layer, y]) => (
                  <div key={layer} className="flex items-center justify-between text-slate-400">
                    <span className="capitalize text-slate-300">{layer}</span>
                    <span className="text-[9px] text-indigo-400 font-mono">y≈{y}</span>
                  </div>
                ))}
              </div>
            ) : (
              <button
                onClick={() => setShowLayerGuide(true)}
                className="px-2.5 py-1.5 rounded-lg bg-[#111726]/90 hover:bg-[#1a233b] border border-slate-700/80 text-slate-300 hover:text-white text-[10px] font-mono font-medium shadow-lg backdrop-blur-md flex items-center gap-1.5 transition-all"
                title="Expand Layer Guide"
              >
                <Layers className="w-3 h-3 text-indigo-400" />
                <span>Layer Guide</span>
              </button>
            )}
          </Panel>
        </ReactFlow>
      </div>
    </div>
  )
}

// ── Exported ArchCanvas with Provider ────────────────────────────────────────

export default function ArchCanvas() {
  return (
    <ReactFlowProvider>
      <ArchCanvasInner />
    </ReactFlowProvider>
  )
}
