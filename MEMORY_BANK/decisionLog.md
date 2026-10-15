# Decision Log

## Initial Decisions (Phase 0)
1. **RAG before fine-tuning**: Architecture rules and cloud pricing evolve rapidly; citations and evidence retrieval provide transparency, while fine-tuning is deferred until evaluation demonstrates specific behavioral shortcomings.
2. **Structured Component Catalog**: Catalog serves as hard ground truth for allowed connections, interface matching, scaling limits, and tool alternatives (e.g., Redis vs AWS ElastiCache, Nginx vs ALB).
3. **Deterministic Validator**: Architectures must pass programmatic checks; generative model output is never presented without deterministic validation.
4. **Async SQLAlchemy + AsyncPG**: Non-blocking async database layer with Alembic async migrations for PostgreSQL.
5. **FastAPI + Pydantic v2**: High performance, strict type safety, automatic OpenAPI docs generation.
6. **Dual Health Probing**: Lightweight liveness probe (`/health`) and comprehensive readiness probe (`/api/v1/health/ready`) checking DB and Qdrant connectivity.

## Phase 3 Decisions (Deterministic Validator)
1. **Isolated Pure-Function Rule Architecture**: Each architectural rule is isolated in its own file under `backend/app/services/validator/rules/`, implementing a clean signature `(design: DesignDocument) -> list[ValidationIssue]`. No database or network I/O is permitted inside rules, guaranteeing sub-millisecond execution and deterministic testability.
2. **Catalog-Informed Dynamic Bottleneck Detection**: Rather than hardcoded heuristics alone, rules leverage declared node operational limits (`limits.qps`, `limits.max_throughput_mbps`) and topology layers (`edge`, `gateway`, `application`, `data`, `async`) to identify capacity mismatches and architectural antipatterns.
3. **Structured Non-Functional Requirements (NFR)**: Non-functional constraints (`expected_users`, `expected_qps`, `availability_target`, `regions`, `data_durability_required`) are passed with the design document, allowing rules (such as `cache_before_db`, `async_processing`, `multi_region`, and `data_store_required`) to dynamically evaluate appropriateness for the requested workload.
4. **Sub-Second Performance SLA**: Rule execution is measured and returned in `ValidationResult.elapsed_ms`. A full run across all 12 rules executes in < 5 milliseconds, far exceeding the Phase 3 requirement of under 1 second.

## Phase 4 Decisions (LangGraph Planner & DeepSeek-R1-Distill-Qwen-32B)
1. **LangGraph State Machine for Planning**: Adopted LangGraph (`StateGraph`) to coordinate the multi-stage planner lifecycle (`retrieve_evidence` -> `ground_catalog` -> `generate_proposal` -> `parse_and_validate` -> `run_deterministic_validator` with conditional loop `reflect_and_retry`). This guarantees strict separation between evidence retrieval, LLM proposal generation, schema adherence retries, and pure-function validation.
2. **DeepSeek-R1 Chain-of-Thought Handling**: DeepSeek-R1 produces `<think>...</think>` tokens during generation. The LLM adapters (`OllamaAdapter` and `VLLMAdapter`) cleanly strip internal thinking blocks while preserving valid structured JSON for Pydantic parsing.
3. **Resilient Local & Offline Fallback**: In addition to Ollama and vLLM providers, a deterministic `MockLLMAdapter` is provided for offline development and CI. When Ollama/vLLM endpoints are unreachable or the model is not yet loaded, adapters gracefully fall back to mock generation with logged warnings rather than crashing the system.
4. **Hugging Face Bucket Integration**: Model weights for `DeepSeek-R1-Distill-Qwen-32B` hosted in user bucket `keshavrao887/DeepSeek-R1-Distill-Qwen-32B-bucket` are supported via configuration settings and the automated `scripts/sync_model_bucket.ps1` synchronization utility.
5. **Immutable Design Version Snapshots**: Proposals are persisted as append-only `DesignVersion` records linked to parent `Project` entities, preserving exact requirements, node/edge configurations, evidence citations, alternative tradeoffs, and deterministic validation issues.
