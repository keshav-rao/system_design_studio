import { useStudioStore } from '../../../store/studioStore'
import { BookOpen, ExternalLink, Star } from 'lucide-react'

const COLLECTION_COLOR: Record<string, string> = {
  foundations: 'bg-blue-900/60 text-blue-300 border-blue-700/50',
  patterns: 'bg-purple-900/60 text-purple-300 border-purple-700/50',
  cloud_docs: 'bg-sky-900/60 text-sky-300 border-sky-700/50',
  capacity: 'bg-amber-900/60 text-amber-300 border-amber-700/50',
  case_studies: 'bg-emerald-900/60 text-emerald-300 border-emerald-700/50',
}

function ScoreBar({ score }: { score: number }) {
  const pct = Math.min(100, Math.round(score * 100))
  return (
    <div className="flex items-center gap-2">
      <div className="flex-1 h-1.5 bg-slate-800 rounded-full overflow-hidden">
        <div
          className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full transition-all"
          style={{ width: `${pct}%` }}
        />
      </div>
      <span className="text-[10px] font-mono text-slate-400">{score.toFixed(2)}</span>
    </div>
  )
}

export default function EvidenceTab() {
  const { activeDesign } = useStudioStore()

  if (!activeDesign) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-6 text-center space-y-3">
        <BookOpen className="w-8 h-8 text-slate-600" />
        <p className="text-sm font-semibold text-slate-400">No evidence yet</p>
        <p className="text-xs text-slate-500">Generate a plan to see RAG citations.</p>
      </div>
    )
  }

  const evidence = activeDesign.evidence_links
  const alternatives = activeDesign.alternatives_considered
  const assumptions = activeDesign.assumptions

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-5 text-sm">
      {/* Summary */}
      <div className="p-3.5 rounded-xl bg-[#111726] border border-indigo-800/40">
        <h3 className="text-xs font-semibold text-slate-300 mb-1">
          Design: {activeDesign.title}
        </h3>
        <p className="text-xs text-slate-400 leading-relaxed line-clamp-4">
          {activeDesign.summary}
        </p>
      </div>

      {/* Evidence citations */}
      <div>
        <div className="flex items-center gap-2 mb-3">
          <BookOpen className="w-3.5 h-3.5 text-indigo-400" />
          <h4 className="text-xs font-semibold text-white">
            Knowledge Base Citations ({evidence.length})
          </h4>
        </div>
        {evidence.length === 0 ? (
          <p className="text-xs text-slate-500 py-4 text-center">
            No RAG evidence links found.
          </p>
        ) : (
          <div className="space-y-3">
            {evidence.map((ev, idx) => (
              <div
                key={idx}
                className="p-3.5 rounded-xl bg-[#0B0F17] border border-slate-800/60 space-y-2"
              >
                <div className="flex items-start justify-between gap-2">
                  <p className="text-xs font-semibold text-white leading-snug">
                    {ev.source_title}
                  </p>
                  <span
                    className={`px-2 py-0.5 rounded text-[10px] font-mono border flex-shrink-0 ${
                      COLLECTION_COLOR[ev.collection] ??
                      'bg-slate-800 text-slate-300 border-slate-700'
                    }`}
                  >
                    {ev.collection}
                  </span>
                </div>
                {ev.section_path && (
                  <p className="text-[10px] font-mono text-slate-500">{ev.section_path}</p>
                )}
                <blockquote className="text-xs text-slate-400 leading-relaxed border-l-2 border-indigo-700/50 pl-3 italic">
                  "{ev.snippet}"
                </blockquote>
                <div className="space-y-0.5">
                  <p className="text-[10px] text-slate-500 mb-1">Relevance</p>
                  <ScoreBar score={ev.relevance_score} />
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Alternatives considered */}
      {alternatives.length > 0 && (
        <div>
          <div className="flex items-center gap-2 mb-3">
            <Star className="w-3.5 h-3.5 text-amber-400" />
            <h4 className="text-xs font-semibold text-white">
              Alternatives Evaluated ({alternatives.length})
            </h4>
          </div>
          <div className="space-y-2">
            {alternatives.map((alt, idx) => (
              <div
                key={idx}
                className="p-3 rounded-xl bg-[#0B0F17] border border-slate-800/60 space-y-1.5"
              >
                <div className="flex items-center gap-2">
                  <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-indigo-950/60 border border-indigo-800/50 text-indigo-300">
                    {alt.component_slug}
                  </span>
                  <span className="text-[10px] text-slate-500">vs.</span>
                  <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-slate-800 border border-slate-700 text-slate-400">
                    {alt.considered_against}
                  </span>
                </div>
                <p className="text-xs text-slate-300 leading-relaxed">{alt.rationale}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Assumptions */}
      {assumptions.length > 0 && (
        <div>
          <h4 className="text-xs font-semibold text-white mb-2 flex items-center gap-1.5">
            <ExternalLink className="w-3.5 h-3.5 text-slate-400" />
            Architectural Assumptions
          </h4>
          <ul className="space-y-1.5">
            {assumptions.map((a, idx) => (
              <li key={idx} className="flex items-start gap-2 text-xs text-slate-400 leading-relaxed">
                <span className="text-slate-600 flex-shrink-0 mt-0.5">•</span>
                {a}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}
