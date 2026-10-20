import { useState, useEffect } from 'react'
import {
  ChevronRight,
  ChevronLeft,
  Sparkles,
  Loader2,
  Users,
  Zap,
  Shield,
  Globe,
  HardDrive,
  MessageSquare,
} from 'lucide-react'
import { useStudioStore } from '../../store/studioStore'
import { api } from '../../api/client'
import type { InterviewQuestion, InterviewAnswer } from '../../types/api'

const CATEGORY_ICONS: Record<string, React.ReactNode> = {
  scale: <Users className="w-4 h-4" />,
  traffic: <Zap className="w-4 h-4" />,
  latency: <Zap className="w-4 h-4 text-amber-400" />,
  durability: <HardDrive className="w-4 h-4 text-emerald-400" />,
  regions: <Globe className="w-4 h-4 text-blue-400" />,
  domain: <MessageSquare className="w-4 h-4 text-purple-400" />,
}

const CATEGORY_COLORS: Record<string, string> = {
  scale: 'from-blue-600/20 to-blue-800/10 border-blue-700/40',
  traffic: 'from-amber-600/20 to-amber-800/10 border-amber-700/40',
  latency: 'from-orange-600/20 to-orange-800/10 border-orange-700/40',
  durability: 'from-emerald-600/20 to-emerald-800/10 border-emerald-700/40',
  regions: 'from-cyan-600/20 to-cyan-800/10 border-cyan-700/40',
  domain: 'from-purple-600/20 to-purple-800/10 border-purple-700/40',
}

export default function InterviewPanel() {
  const {
    appDescription,
    setAppDescription,
    interviewQuestions,
    interviewAnswers,
    setInterviewState,
    addAnswer,
    setView,
    activeProject: _activeProject,
    setGenerating: _setGenerating,
    setGenerateError: _setGenerateError,
    setActiveDesign: _setActiveDesign,
    setCanvasFromDesign: _setCanvasFromDesign,
  } = useStudioStore()

  const [step, setStep] = useState<'describe' | 'questions'>('describe')
  const [descDraft, setDescDraft] = useState(appDescription)
  const [currentIdx, setCurrentIdx] = useState(0)
  const [currentAnswer, setCurrentAnswer] = useState<string>('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const q: InterviewQuestion | undefined = interviewQuestions[currentIdx]

  // Pre-fill current answer from store
  useEffect(() => {
    if (q) {
      const stored = interviewAnswers.find((a) => a.question_id === q.id)
      setCurrentAnswer(stored ? String(stored.answer) : q.default_value != null ? String(q.default_value) : '')
    }
  }, [currentIdx, q, interviewAnswers])

  const submitDescription = async () => {
    if (descDraft.trim().length < 5) return
    setLoading(true)
    setError(null)
    try {
      const res = await api.interview({ app_description: descDraft.trim(), answers: [] })
      setAppDescription(descDraft.trim())
      setInterviewState(res.questions, [], res.completed)
      if (res.completed) {
        setStep('questions') // skip to review if backend says done
      } else {
        setStep('questions')
        setCurrentIdx(0)
      }
    } catch (e: any) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }

  const saveCurrentAnswer = (): InterviewAnswer[] => {
    const updated: InterviewAnswer[] = [
      ...interviewAnswers.filter((a) => a.question_id !== q?.id),
      ...(q ? [{ question_id: q.id, answer: currentAnswer }] : []),
    ]
    return updated
  }

  const nextQuestion = async () => {
    if (!q) return
    const allAnswers = saveCurrentAnswer()
    addAnswer({ question_id: q.id, answer: currentAnswer })

    if (currentIdx < interviewQuestions.length - 1) {
      setCurrentIdx(currentIdx + 1)
      return
    }

    // Last question – submit and check if more questions needed
    setLoading(true)
    setError(null)
    try {
      const res = await api.interview({
        app_description: appDescription,
        answers: allAnswers,
      })
      setInterviewState(res.questions, allAnswers, res.completed)
      if (res.completed) {
        setView('requirements')
      } else {
        setCurrentIdx(0)
      }
    } catch (e: any) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }

  const skipToReview = () => {
    if (q) addAnswer({ question_id: q.id, answer: currentAnswer })
    setView('requirements')
  }


  if (step === 'describe') {
    return (
      <div className="flex-1 flex items-center justify-center p-8">
        <div className="max-w-2xl w-full space-y-8">
          {/* Badge */}
          <div className="flex justify-center">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-indigo-950/60 border border-indigo-700/50 text-indigo-300 text-xs font-medium">
              <Sparkles className="w-3.5 h-3.5" />
              AI Requirements Interview
            </div>
          </div>

          <div className="text-center space-y-2">
            <h2 className="text-3xl font-bold text-white tracking-tight">
              Describe your system
            </h2>
            <p className="text-slate-400 text-sm leading-relaxed">
              Tell us what you're building. Be as brief or detailed as you like —
              we'll ask follow-up questions to lock down NFRs.
            </p>
          </div>

          <div className="space-y-4">
            <textarea
              id="app-description"
              value={descDraft}
              onChange={(e) => setDescDraft(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) submitDescription()
              }}
              placeholder="e.g. A dating app like Tinder — real-time geospatial matching, live notifications, 10M users..."
              rows={5}
              className="w-full bg-[#111726] border border-slate-700 rounded-2xl p-4 text-slate-100 placeholder-slate-500 text-sm focus:outline-none focus:border-indigo-500 resize-none transition-colors leading-relaxed"
              autoFocus
            />

            {error && (
              <div className="p-3 rounded-xl bg-rose-950/40 border border-rose-800/50 text-rose-300 text-xs">
                {error}
              </div>
            )}

            {/* Example prompts */}
            <div className="flex flex-wrap gap-2">
              {[
                'Dating app like Tinder with real-time matching',
                'Video streaming platform like YouTube',
                'Ride-sharing app like Uber with live GPS tracking',
                'E-commerce marketplace with high write throughput',
              ].map((ex) => (
                <button
                  key={ex}
                  onClick={() => setDescDraft(ex)}
                  className="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs text-slate-400 hover:text-slate-200 transition-all"
                >
                  {ex}
                </button>
              ))}
            </div>

            <button
              onClick={submitDescription}
              disabled={loading || descDraft.trim().length < 5}
              className="w-full flex items-center justify-center gap-2 py-3.5 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold rounded-2xl transition-all shadow-lg shadow-indigo-500/25"
            >
              {loading ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <ChevronRight className="w-4 h-4" />
              )}
              {loading ? 'Preparing questions…' : 'Start Interview'}
            </button>
          </div>
        </div>
      </div>
    )
  }

  // ── QUESTIONS STEP ────────────────────────────────────────────────────────
  if (!q) {
    // All questions answered, move to review
    return (
      <div className="flex-1 flex items-center justify-center p-8">
        <div className="text-center space-y-4">
          <div className="w-16 h-16 rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center mx-auto">
            <Shield className="w-7 h-7 text-emerald-400" />
          </div>
          <h3 className="text-xl font-bold text-white">Requirements gathered</h3>
          <p className="text-slate-400 text-sm">Review and generate your architecture plan.</p>
          <button
            onClick={() => setView('requirements')}
            className="px-6 py-3 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold rounded-xl transition-all"
          >
            Review Requirements →
          </button>
        </div>
      </div>
    )
  }

  const progress = ((currentIdx + 1) / interviewQuestions.length) * 100

  return (
    <div className="flex-1 flex items-center justify-center p-8">
      <div className="max-w-2xl w-full space-y-6">
        {/* Progress */}
        <div className="space-y-2">
          <div className="flex items-center justify-between text-xs text-slate-400">
            <span>Question {currentIdx + 1} of {interviewQuestions.length}</span>
            <span className="capitalize font-medium text-slate-300">{q.category}</span>
          </div>
          <div className="h-1.5 bg-slate-800 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full transition-all duration-500"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {/* Question card */}
        <div
          className={`p-6 rounded-2xl border bg-gradient-to-br ${CATEGORY_COLORS[q.category] ?? CATEGORY_COLORS.domain}`}
        >
          <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wide text-slate-400 mb-3">
            {CATEGORY_ICONS[q.category] ?? <MessageSquare className="w-4 h-4" />}
            {q.category}
          </div>

          <h3 className="text-lg font-semibold text-white mb-1 leading-snug">{q.question}</h3>

          {q.explanation && (
            <p className="text-xs text-slate-400 leading-relaxed mb-4">{q.explanation}</p>
          )}

          {/* Answer options or free text */}
          {q.options && q.options.length > 0 ? (
            <div className="grid grid-cols-2 gap-2 mt-4">
              {q.options.map((opt) => (
                <button
                  key={opt}
                  onClick={() => setCurrentAnswer(opt)}
                  className={`px-4 py-2.5 rounded-xl text-sm font-medium border transition-all text-left ${
                    currentAnswer === opt
                      ? 'bg-indigo-600 border-indigo-500 text-white shadow-lg shadow-indigo-500/20'
                      : 'bg-[#0B0F17]/80 border-slate-700 text-slate-300 hover:border-slate-600 hover:text-white'
                  }`}
                >
                  {opt}
                </button>
              ))}
            </div>
          ) : (
            <input
              type="text"
              value={currentAnswer}
              onChange={(e) => setCurrentAnswer(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && nextQuestion()}
              placeholder={q.default_value != null ? String(q.default_value) : 'Your answer…'}
              className="w-full mt-4 bg-[#0B0F17]/80 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-100 placeholder-slate-500 text-sm focus:outline-none focus:border-indigo-500 transition-colors"
              autoFocus
            />
          )}
        </div>

        {error && (
          <div className="p-3 rounded-xl bg-rose-950/40 border border-rose-800/50 text-rose-300 text-xs">
            {error}
          </div>
        )}

        {/* Navigation */}
        <div className="flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            {currentIdx > 0 && (
              <button
                onClick={() => {
                  addAnswer({ question_id: q.id, answer: currentAnswer })
                  setCurrentIdx(currentIdx - 1)
                }}
                className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 text-sm font-medium transition-all"
              >
                <ChevronLeft className="w-4 h-4" />
                Back
              </button>
            )}
            <button
              onClick={skipToReview}
              className="px-4 py-2 rounded-xl text-slate-500 hover:text-slate-300 text-sm transition-colors"
            >
              Skip to review
            </button>
          </div>

          <button
            onClick={nextQuestion}
            disabled={loading}
            className="flex items-center gap-2 px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white font-semibold rounded-xl transition-all shadow-lg shadow-indigo-500/20"
          >
            {loading ? (
              <Loader2 className="w-4 h-4 animate-spin" />
            ) : (
              <>
                {currentIdx === interviewQuestions.length - 1 ? 'Finish' : 'Next'}
                <ChevronRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  )
}
