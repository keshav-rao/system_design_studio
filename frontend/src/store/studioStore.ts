import { create } from 'zustand'
import type {
  ProjectResponse,
  DesignVersionResponse,
  InterviewQuestion,
  InterviewAnswer,
  DesignNode,
  DesignEdge,
  DesignDiff,
} from '../types/api'
import type { ComponentItem } from '../types/catalog'
import { ARCH_TEMPLATES, DEFAULT_TEMPLATE } from '../data/archTemplates'

// ── View Enum ────────────────────────────────────────────────────────────────

export type AppView =
  | 'overview'        // Overview / landing dashboard
  | 'canvas'          // Canva template / Architecture canvas
  | 'compatibility'   // Connection compatibility engine
  | 'catalog'         // Component catalog explorer
  | 'projects'        // Projects list / manager
  | 'interview'       // Requirements interview wizard
  | 'requirements'    // Review gathered requirements
  | 'generating'      // Spinning while plan is generated

export type CanvasTab = 'component' | 'validation' | 'evidence' | 'cost'

// ── State ────────────────────────────────────────────────────────────────────

interface StudioState {
  // Component catalog
  catalog: ComponentItem[]
  catalogLoaded: boolean

  // Projects
  projects: ProjectResponse[]
  activeProject: ProjectResponse | null

  // Interview
  appDescription: string
  interviewQuestions: InterviewQuestion[]
  interviewAnswers: InterviewAnswer[]
  interviewCompleted: boolean

  // Design version (from planner)
  activeDesign: DesignVersionResponse | null
  redesignDiff: DesignDiff | null
  generating: boolean
  generateError: string | null

  // Canvas local edits (on top of activeDesign)
  canvasNodes: DesignNode[]
  canvasEdges: DesignEdge[]

  // UI state
  view: AppView
  activeCanvasTab: CanvasTab
  selectedNodeId: string | null
  sidebarOpen: boolean
  activeTemplateId: string | null

  // Actions
  setCatalog: (items: ComponentItem[]) => void
  setProjects: (projects: ProjectResponse[]) => void
  selectProject: (project: ProjectResponse) => void
  loadTemplate: (templateId?: string) => void

  setAppDescription: (desc: string) => void
  setInterviewState: (q: InterviewQuestion[], a: InterviewAnswer[], completed: boolean) => void
  addAnswer: (answer: InterviewAnswer) => void

  setActiveDesign: (design: DesignVersionResponse | null) => void
  setRedesignDiff: (diff: DesignDiff | null) => void
  setGenerating: (v: boolean) => void
  setGenerateError: (e: string | null) => void

  // Canvas mutations
  setCanvasFromDesign: (design: DesignVersionResponse) => void
  addNode: (node: DesignNode) => void
  removeNode: (nodeId: string) => void
  replaceNode: (nodeId: string, newNode: DesignNode) => void
  addEdge: (edge: DesignEdge) => void
  removeEdge: (sourceId: string, targetId: string) => void
  updateNodeConfig: (nodeId: string, config: Record<string, any>) => void

  // UI
  setView: (v: AppView) => void
  setCanvasTab: (t: CanvasTab) => void
  setSelectedNode: (id: string | null) => void
  setSidebarOpen: (v: boolean) => void
  resetInterview: () => void
}

// ── Store ────────────────────────────────────────────────────────────────────

export const useStudioStore = create<StudioState>()((set) => ({
  catalog: [],
  catalogLoaded: false,
  projects: [],
  activeProject: null,

  appDescription: '',
  interviewQuestions: [],
  interviewAnswers: [],
  interviewCompleted: false,

  activeDesign: null,
  redesignDiff: null,
  generating: false,
  generateError: null,

  canvasNodes: DEFAULT_TEMPLATE.nodes,
  canvasEdges: DEFAULT_TEMPLATE.edges,

  view: 'overview',
  activeCanvasTab: 'component',
  selectedNodeId: null,
  sidebarOpen: true,
  activeTemplateId: DEFAULT_TEMPLATE.id,

  // Catalog
  setCatalog: (items) => set({ catalog: items, catalogLoaded: true }),

  // Projects
  setProjects: (projects) => set({ projects }),
  selectProject: (project) => set({
    activeProject: project,
    activeDesign: null,
    redesignDiff: null,
    canvasNodes: [],
    canvasEdges: [],
  }),
  loadTemplate: (templateId) => {
    const tmpl = (templateId && ARCH_TEMPLATES[templateId]) ? ARCH_TEMPLATES[templateId] : DEFAULT_TEMPLATE
    set({
      canvasNodes: [...tmpl.nodes],
      canvasEdges: [...tmpl.edges],
      activeTemplateId: tmpl.id,
      activeDesign: null,
      selectedNodeId: null,
      view: 'canvas',
    })
  },

  // Interview
  setAppDescription: (desc) => set({ appDescription: desc }),
  setInterviewState: (q, a, completed) =>
    set({ interviewQuestions: q, interviewAnswers: a, interviewCompleted: completed }),
  addAnswer: (answer) =>
    set((s) => ({
      interviewAnswers: [
        ...s.interviewAnswers.filter((a) => a.question_id !== answer.question_id),
        answer,
      ],
    })),
  resetInterview: () =>
    set({
      appDescription: '',
      interviewQuestions: [],
      interviewAnswers: [],
      interviewCompleted: false,
      activeDesign: null,
      canvasNodes: [],
      canvasEdges: [],
      generateError: null,
    }),

  // Design
  setActiveDesign: (design) => set({ activeDesign: design }),
  setRedesignDiff: (diff) => set({ redesignDiff: diff }),
  setGenerating: (v) => set({ generating: v }),
  setGenerateError: (e) => set({ generateError: e }),

  // Canvas
  setCanvasFromDesign: (design) =>
    set({ canvasNodes: design.nodes, canvasEdges: design.edges }),

  addNode: (node) =>
    set((s) => ({ canvasNodes: [...s.canvasNodes, node] })),

  removeNode: (nodeId) =>
    set((s) => ({
      canvasNodes: s.canvasNodes.filter((n) => n.id !== nodeId),
      canvasEdges: s.canvasEdges.filter(
        (e) => e.source_id !== nodeId && e.target_id !== nodeId
      ),
      selectedNodeId: s.selectedNodeId === nodeId ? null : s.selectedNodeId,
    })),

  replaceNode: (nodeId, newNode) =>
    set((s) => ({
      canvasNodes: s.canvasNodes.map((n) => (n.id === nodeId ? newNode : n)),
      canvasEdges: s.canvasEdges.map((e) => ({
        ...e,
        source_id: e.source_id === nodeId ? newNode.id : e.source_id,
        target_id: e.target_id === nodeId ? newNode.id : e.target_id,
      })),
      selectedNodeId: s.selectedNodeId === nodeId ? newNode.id : s.selectedNodeId,
    })),

  addEdge: (edge) =>
    set((s) => {
      const exists = s.canvasEdges.some(
        (e) => e.source_id === edge.source_id && e.target_id === edge.target_id
      )
      if (exists) return {}
      return { canvasEdges: [...s.canvasEdges, edge] }
    }),

  removeEdge: (sourceId, targetId) =>
    set((s) => ({
      canvasEdges: s.canvasEdges.filter(
        (e) => !(e.source_id === sourceId && e.target_id === targetId)
      ),
    })),

  updateNodeConfig: (nodeId, config) =>
    set((s) => ({
      canvasNodes: s.canvasNodes.map((n) =>
        n.id === nodeId ? { ...n, config: { ...n.config, ...config } } : n
      ),
    })),

  // UI
  setView: (v) => set({ view: v }),
  setCanvasTab: (t) => set({ activeCanvasTab: t }),
  setSelectedNode: (id) => set({ selectedNodeId: id }),
  setSidebarOpen: (v) => set({ sidebarOpen: v }),
}))
