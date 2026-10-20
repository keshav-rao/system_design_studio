import { useState } from 'react'
import {
  Users,
  Zap,
  Shield,
  Globe,
  HardDrive,
  Loader2,
  CheckCircle2,
  AlertCircle,
  ChevronLeft,
  Sparkles,
} from 'lucide-react'
import { useStudioStore } from '../../store/studioStore'
import { api } from '../../api/client'

interface NFRRowProps {
  icon: React.ReactNode
  label: string
  value: string | number | boolean | null | undefined
  sub?: string
}

function NFRRow({ icon, label, value, sub }: NFRRowProps) {
  const display =
    value === null || value === undefined
      ? '—'
      : typeof value === 'boolean'
      ? value
        ? 'Yes'
        : 'No'
      : String(value)
  return (
    <div className="flex items-center gap-4 py-3 border-b border-slate-800/60 last:border-0">
      <div className="w-8 h-8 rounded-lg bg-slate-800/80 flex items-center justify-center flex-shrink-0">
        {icon}
      </div>
      <div className="flex-1 min-w-0">
        <p className="text-xs font-semibold text-slate-400">{label}</p>
        {sub && <p className="text-[11px] text-slate-500">{sub}</p>}
      </div>
      <span className="font-mono text-sm font-semibold text-white">{display}</span>
    </div>
  )
}

export default function RequirementsReview() {
  const {
    appDescription,
    interviewAnswers,
    activeProject,
    setView,
    setGenerating,
    setGenerateError,
    setActiveDesign,
    setCanvasFromDesign,
  } = useStudioStore()

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // Re-derive inferred requirements from the interview answers we stored
  // We'll display raw answers in a table and let the backend infer NFRs.
  const qpsAnswer = interviewAnswers.find((a) =>
    a.question_id.includes('qps') || a.question_id.includes('traffic')
  )
  const usersAnswer = interviewAnswers.find((a) =>
    a.question_id.includes('user') || a.question_id.includes('concurrent')
  )
  const slaAnswer = interviewAnswers.find((a) =>
    a.question_id.includes('availability') || a.question_id.includes('sla')
  )
  const durabilityAnswer = interviewAnswers.find((a) =>
    a.question_id.includes('durability') || a.question_id.includes('storage')
  )
  const regionsAnswer = interviewAnswers.find((a) =>
    a.question_id.includes('region')
  )

  const handleGenerate = async () => {
    if (!activeProject) return
    setLoading(true)
    setGenerating(true)
    setError(null)
    setGenerateError(null)
    setView('generating')
    try {
      const design = await api.generatePlan(activeProject.id, {
        app_description: appDescription,
        interview_answers: interviewAnswers,
      })
      setActiveDesign(design)
      setCanvasFromDesign(design)
      setView('canvas')
    } catch (e: any) {
      const msg = e.message
      setError(msg)
      setGenerateError(msg)
      setView('requirements')
    } finally {
      setLoading(false)
      setGenerating(false)
    }
  }

  return (
    <div className="flex-1 flex items-center justify-center p-8">
      <div className="max-w-2xl w-full space-y-6">
        {/* Header */}
        <div className="text-center space-y-2">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/60 border border-emerald-700/50 text-emerald-300 text-xs font-medium">
            <CheckCircle2 className="w-3.5 h-3.5" />
            Requirements Captured
          </div>
          <h2 className="text-2xl font-bold text-white tracking-tight">
            Review before generating
          </h2>
          <p className="text-slate-400 text-sm">
            Confirm these requirements look correct. The AI planner will ground
            every component decision in your answers and catalog facts.
          </p>
        </div>

        {/* App description */}
        <div className="p-4 rounded-2xl bg-[#111726] border border-slate-800/80">
          <p className="text-xs font-semibold text-slate-400 mb-1.5">System Description</p>
          <p className="text-sm text-slate-100 leading-relaxed">{appDescription}</p>
        </div>

        {/* Inferred NFR summary */}
        <div className="p-4 rounded-2xl bg-[#111726] border border-slate-800/80">
          <p className="text-xs font-semibold text-slate-400 mb-0.5">Inferred Requirements</p>
          <p className="text-[11px] text-slate-500 mb-3">
            Derived from your interview answers
          </p>
          <NFRRow
            icon={<Zap className="w-4 h-4 text-amber-400" />}
            label="Expected QPS"
            value={qpsAnswer?.answer}
            sub="Peak queries per second"
          />
          <NFRRow
            icon={<Users className="w-4 h-4 text-blue-400" />}
            label="Concurrent Users"
            value={usersAnswer?.answer}
            sub="Simultaneous active users"
          />
          <NFRRow
            icon={<Shield className="w-4 h-4 text-indigo-400" />}
            label="Availability Target"
            value={slaAnswer?.answer}
            sub="SLA / uptime requirement"
          />
          <NFRRow
            icon={<HardDrive className="w-4 h-4 text-emerald-400" />}
            label="Data Durability"
            value={durabilityAnswer?.answer ?? 'Required'}
            sub="Persistent durable storage needed"
          />
          <NFRRow
            icon={<Globe className="w-4 h-4 text-cyan-400" />}
            label="Deployment Regions"
            value={regionsAnswer?.answer ?? 1}
            sub="Geographic deployment regions"
          />
        </div>

        {/* Captured answers list */}
        {interviewAnswers.length > 0 && (
          <details className="group">
            <summary className="cursor-pointer text-xs font-medium text-slate-400 hover:text-slate-200 transition-colors list-none flex items-center gap-1.5">
              <span className="group-open:rotate-90 inline-block transition-transform">▶</span>
              View all {interviewAnswers.length} captured answers
            </summary>
            <div className="mt-3 space-y-1.5">
              {interviewAnswers.map((a) => (
                <div
                  key={a.question_id}
                  className="flex items-center justify-between px-3 py-2 rounded-lg bg-[#111726] border border-slate-800/60 text-xs"
                >
                  <span className="font-mono text-slate-400">{a.question_id}</span>
                  <span className="text-slate-200 font-medium">{String(a.answer)}</span>
                </div>
              ))}
            </div>
          </details>
        )}

        {error && (
          <div className="p-4 rounded-xl bg-rose-950/40 border border-rose-800/50 flex items-start gap-3">
            <AlertCircle className="w-4 h-4 text-rose-400 flex-shrink-0 mt-0.5" />
            <div>
              <p className="text-xs font-semibold text-rose-300">Generation failed</p>
              <p className="text-xs text-rose-400/80 mt-1">{error}</p>
              <p className="text-xs text-slate-500 mt-1">
                Make sure the LLM backend (Ollama / vLLM) is running at the configured endpoint.
              </p>
            </div>
          </div>
        )}

        {/* Actions */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => setView('interview')}
            className="flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 text-sm font-medium transition-all"
          >
            <ChevronLeft className="w-4 h-4" />
            Edit Answers
          </button>

          <button
            onClick={handleGenerate}
            disabled={loading || !activeProject}
            className="flex-1 flex items-center justify-center gap-2 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold rounded-xl transition-all shadow-lg shadow-indigo-500/25"
          >
            {loading ? (
              <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
              <Sparkles className="w-4 h-4" />
            )}
            {loading ? 'Generating architecture…' : 'Generate Architecture Plan'}
          </button>
        </div>

        {!activeProject && (
          <p className="text-center text-xs text-amber-400">
            ⚠ No project selected — go back to Projects and create or select one first.
          </p>
        )}
      </div>
    </div>
  )
}
