# AI System Design Architect

## Problem
People building apps struggle to turn vague ideas into sound architectures. Generic chatbots often provide unsourced, unchecked answers, while architecture trade-offs depend on workload, budget, reliability, and changing cloud services.

## Vision
An explainable, evidence-backed architecture assistant. Every recommendation cites a source, states assumptions and alternatives, and passes deterministic validation before presentation.

## Target users
- Solo developers and students seeking a defensible starting architecture.
- Startup engineers needing quick designs and rough cost estimates.
- Interview candidates practising system design.

## Goals
- Turn natural-language requirements into structured components, connections, and constraints.
- Ground recommendations in retrieved evidence or catalog facts.
- Validate structure, constraints, assumptions, failure points, and uncovered requirements.
- Let users edit the canvas and re-plan affected parts.
- Provide basic capacity and cost estimates.

## Non-goals for v1
- Auto-deployment or infrastructure-as-code generation.
- Fine-tuning before evaluation demonstrates a need.
- Ingesting copyrighted material without a licence or permission.

## MVP features
1. Requirements interview covering concurrency, geography, message volume, privacy, availability, and budget.
2. Hybrid retrieval over foundations, patterns, cloud documentation, capacity planning, and case studies.
3. Structured component catalog with purpose, interfaces, compatibility, scaling traits, failure modes, alternatives, and cost units.
4. DeepSeek-R1 planner producing a schema-valid proposal from requirements and evidence.
5. Deterministic validation for components, connections, constraints, assumptions, failure points, and unaddressed requirements.
6. Editable architecture canvas with component explanations and citations.
7. Iterative redesign with re-retrieval and partial re-planning after edits.

## Success metrics
- Retrieval recall@k and MRR on 100+ architecture questions.
- At least 95% of generated designs pass structural validation without manual fixes.
- At least 90% of recommendations include a valid citation or catalog reference.
- Track user ratings and the share of designs edited instead of discarded.
- First proposal in under 60 seconds on target hardware.

## Risks and mitigations
- Hallucinated components or invalid connections: catalog source of truth plus validator.
- Stale cloud facts: date time-sensitive sources and refresh them on a schedule.
- Copyright risk: record a licence for every source.
- Weak retrieval: evaluate embedding and reranker candidates against a project question set.

## Post-MVP
Simulation, richer cost estimates, Markdown/PDF/Mermaid export, shareable designs, evaluation dashboard, and optional fine-tuning after failure analysis.
