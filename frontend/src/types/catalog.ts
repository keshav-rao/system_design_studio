export interface FailureMode {
  mode: string
  impact: string
  mitigation: string
}

export interface CostUnits {
  model: string
  unit: string
  base_monthly_usd?: number
  free_tier?: string
  notes?: string
}

export interface ComponentItem {
  id: string
  slug: string
  name: string
  category: string
  layer: string
  description: string
  protocols: string[]
  limits: Record<string, any>
  failure_modes: FailureMode[]
  cost_units: CostUnits
  alternatives: string[]
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface ComponentListResponse {
  total: number
  items: ComponentItem[]
}

export interface CompatibilityCheckResponse {
  source_slug: string
  target_slug: string
  compatible: boolean
  protocol?: string | null
  recommended_pattern?: string | null
  limits: {
    effective_throughput_qps?: number | null
    source_limits?: Record<string, any>
    target_limits?: Record<string, any>
  }
  reason: string
  warnings: string[]
}
