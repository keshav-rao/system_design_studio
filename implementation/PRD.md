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

## MVP features
1. Requirements interview covering concurrency, geography, message volume, privacy, availability, and budget.
2. Hybrid retrieval (LlamaIndex + Qdrant) over the full `rag_knowledge_base/` corpus: fundamentals, cloud frameworks, component guides, reference architectures, performance, cost/capacity, ADRs, microservices patterns, and vendor docs.
3. Structured component catalog with purpose, interfaces, compatibility, scaling traits, failure modes, alternatives, and cost units.
4. DeepSeek-R1 planner, orchestrated as a LangGraph agent, producing a schema-valid proposal from requirements and evidence.
5. Deterministic validation for components, connections, constraints, assumptions, failure points, and unaddressed requirements.
6. Infinite whiteboard canvas (SystemSketcher-style) with a searchable component palette, drawing tools, templates, smart catalog-aware suggestions, component explanations, and citations.
7. Iterative redesign with re-retrieval and partial re-planning after edits.

## Success metrics
- Retrieval recall@k and MRR on 100+ architecture questions.
- At least 95% of generated designs pass structural validation without manual fixes.
- At least 90% of recommendations include a valid citation or catalog reference.
- Track user ratings and the share of designs edited instead of discarded.
- First proposal in under 60 seconds on target hardware.

## Target hardware (minimum, development/test)
- CPU: AMD Ryzen 9 7950X or Intel i9-14900K
- RAM: 64 GB DDR5
- GPU: NVIDIA RTX 4090 (24 GB VRAM)
- Storage: 2 TB NVMe SSD

With DeepSeek-R1-Distill-Qwen-32B quantized (~20 GB VRAM), the embedder and reranker run on CPU by default.

## Risks and mitigations
- Hallucinated components or invalid connections: catalog source of truth plus validator.
- Stale cloud facts: date time-sensitive sources and refresh them on a schedule.
- Source provenance: everything in `rag_knowledge_base/` (including books) is the authoritative corpus; record title, origin, and licence/permission notes for every source.
- Weak retrieval: evaluate embedding and reranker candidates against a project question set.

## Post-MVP
Simulation, richer cost estimates, PDF export, sketch-to-diagram (requires a vision model), shareable designs, multi-user sign-in, evaluation dashboard, and optional fine-tuning after failure analysis.
