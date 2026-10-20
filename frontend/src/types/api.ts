// ─── Planner / Validator / Project Types ─────────────────────────────────────

export interface DesignRequirements {
  expected_users?: number | null
  expected_qps?: number | null
  availability_target?: number | null
  data_durability_required: boolean
  regions: number
}

export interface DesignNode {
  id: string
  slug: string
  category: string
  layer: string
  replicas: number
  protocols: string[]
  limits: Record<string, any>
  config: Record<string, any>
}

export interface DesignEdge {
  source_id: string
  target_id: string
  protocol?: string | null
  label?: string | null
}

export type Severity = 'error' | 'warning' | 'info'

export interface ValidationIssue {
  rule_id: string
  severity: Severity
  message: string
  node_ids: string[]
  edge_ids: string[]
  suggestion?: string | null
}

export interface ValidationResult {
  valid: boolean
  total_issues: number
  errors: number
  warnings: number
  infos: number
  issues: ValidationIssue[]
  rules_executed: string[]
  elapsed_ms: number
}

export interface EvidenceLink {
  source_id?: string | null
  source_title: string
  collection: string
  section_path?: string | null
  snippet: string
  relevance_score: number
}

export interface AlternativeConsidered {
  component_slug: string
  considered_against: string
  rationale: string
}

export interface InterviewQuestion {
  id: string
  question: string
  category: string
  options: string[]
  default_value?: any
  explanation?: string | null
}

export interface InterviewAnswer {
  question_id: string
  answer: any
}

export interface InterviewRequest {
  app_description: string
  answers: InterviewAnswer[]
}

export interface InterviewResponse {
  app_description: string
  completed: boolean
  questions: InterviewQuestion[]
  inferred_requirements: DesignRequirements
}

export interface ProjectCreate {
  name: string
  description?: string | null
}

export interface ProjectResponse {
  id: string
  name: string
  description?: string | null
  created_at: string
  updated_at: string
  versions_count: number
}

export interface PlanRequest {
  app_description: string
  requirements?: DesignRequirements | null
  interview_answers: InterviewAnswer[]
}

export interface RedesignRequest {
  change_description: string
  requirements: DesignRequirements
  affected_node_ids: string[]
}

export interface DesignDiff {
  fromVersion: number
  toVersion: number
  addedNodes: string[]
  removedNodes: string[]
  updatedNodes: string[]
  changedRequirements: string[]
  addedEdges: string[]
  removedEdges: string[]
  affectedNodeIds: string[]
}

export interface DesignVersionResponse {
  id: string
  project_id: string
  version_number: number
  title: string
  summary: string
  requirements: DesignRequirements
  nodes: DesignNode[]
  edges: DesignEdge[]
  assumptions: string[]
  evidence_links: EvidenceLink[]
  alternatives_considered: AlternativeConsidered[]
  validation_issues: ValidationIssue[]
  is_valid: boolean
  created_at: string
  affected_node_ids?: string[]
}
