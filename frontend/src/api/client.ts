// Thin API client – all fetch calls live here so components stay clean.

const BASE = '/api/v1'

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options?.headers },
    ...options,
  })
  if (!res.ok) {
    const text = await res.text()
    throw new Error(`API ${res.status}: ${text}`)
  }
  return res.json() as Promise<T>
}

// ── Projects ────────────────────────────────────────────────────────────────

import type {
  ProjectCreate,
  ProjectResponse,
  InterviewRequest,
  InterviewResponse,
  PlanRequest,
  RedesignRequest,
  DesignVersionResponse,
} from '../types/api'
import type { ComponentItem, ComponentListResponse } from '../types/catalog'

export const api = {
  // Catalog
  getComponents: (limit = 150) =>
    request<ComponentListResponse>(`/catalog/components?limit=${limit}`),

  // Projects
  createProject: (body: ProjectCreate) =>
    request<ProjectResponse>('/projects', {
      method: 'POST',
      body: JSON.stringify(body),
    }),

  listProjects: () => request<ProjectResponse[]>('/projects'),

  // Interview
  interview: (body: InterviewRequest) =>
    request<InterviewResponse>('/projects/interview', {
      method: 'POST',
      body: JSON.stringify(body),
    }),

  // Plan generation
  generatePlan: (projectId: string, body: PlanRequest) =>
    request<DesignVersionResponse>(`/projects/${projectId}/plan`, {
      method: 'POST',
      body: JSON.stringify(body),
    }),

  redesign: (projectId: string, body: RedesignRequest) =>
    request<DesignVersionResponse>(`/projects/${projectId}/redesign`, {
      method: 'POST',
      body: JSON.stringify(body),
    }),

  // Design versions
  listDesigns: (projectId: string) =>
    request<DesignVersionResponse[]>(`/projects/${projectId}/designs`),

  getLatestDesign: (projectId: string) =>
    request<DesignVersionResponse>(`/projects/${projectId}/designs/latest`),

  // Compatibility check
  checkCompatibility: (sourceSlug: string, targetSlug: string) =>
    request<any>(`/catalog/compatibility/check`, {
      method: 'POST',
      body: JSON.stringify({ source_slug: sourceSlug, target_slug: targetSlug }),
    }),
}

export type { ComponentItem }
