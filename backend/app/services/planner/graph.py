"""LangGraph-driven planning workflow for DeepSeek-R1-Distill-Qwen-32B.

Orchestrates:
1. Evidence Retrieval (RAG from Qdrant)
2. Catalog Grounding (Component specs and limits)
3. Architecture Proposal Generation (DeepSeek-R1)
4. Schema Validation & Reflection Retry Loop (up to 2 retries)
5. Deterministic Validation (Pure rule checking)
"""

import json
import logging
from typing import Any, TypedDict

from langgraph.graph import END, StateGraph

from app.schemas.knowledge import SearchQuery
from app.schemas.planner import ArchitectureProposal, EvidenceLink
from app.schemas.validator import DesignRequirements
from app.services.catalog.catalog_service import CatalogService
from app.services.knowledge.service import KnowledgeService
from app.services.planner.providers.base import BaseLLMAdapter
from app.services.validator.validator_service import ValidatorService

logger = logging.getLogger(__name__)


class PlannerState(TypedDict, total=False):
    """Execution state passed through the LangGraph pipeline."""

    app_description: str
    planning_context: str
    requirements: dict[str, Any]
    retrieved_evidence: list[dict[str, Any]]
    catalog_context: list[str]
    raw_llm_output: str | None
    proposal: dict[str, Any] | None
    validation_issues: list[dict[str, Any]]
    is_valid: bool
    retry_count: int
    max_retries: int
    error_message: str | None


class ArchitecturePlannerGraph:
    """Compiles and executes the LangGraph architecture generation workflow."""

    def __init__(
        self,
        llm_adapter: BaseLLMAdapter,
        knowledge_service: KnowledgeService | None = None,
        catalog_service: CatalogService | None = None,
        validator_service: ValidatorService | None = None,
    ) -> None:
        self.llm = llm_adapter
        self.knowledge = knowledge_service
        self.catalog = catalog_service
        self.validator = validator_service or ValidatorService()
        self.workflow = self._build_graph()

    def _build_graph(self) -> Any:
        workflow = StateGraph(PlannerState)

        # Register nodes
        workflow.add_node("retrieve_evidence", self._retrieve_evidence_node)
        workflow.add_node("ground_catalog", self._ground_catalog_node)
        workflow.add_node("generate_proposal", self._generate_proposal_node)
        workflow.add_node("parse_and_validate", self._parse_and_validate_node)
        workflow.add_node("reflect_and_retry", self._reflect_and_retry_node)
        workflow.add_node("run_deterministic_validator", self._run_validator_node)

        # Set entry point
        workflow.set_entry_point("retrieve_evidence")

        # Linear flow to generation
        workflow.add_edge("retrieve_evidence", "ground_catalog")
        workflow.add_edge("ground_catalog", "generate_proposal")
        workflow.add_edge("generate_proposal", "parse_and_validate")

        # Conditional branch on schema validity
        workflow.add_conditional_edges(
            "parse_and_validate",
            self._check_schema_decision,
            {
                "valid": "run_deterministic_validator",
                "retry": "reflect_and_retry",
                "failed": END,
            },
        )

        workflow.add_edge("reflect_and_retry", "generate_proposal")
        workflow.add_edge("run_deterministic_validator", END)

        return workflow.compile()

    # -----------------------------------------------------------------------
    # Graph Nodes
    # -----------------------------------------------------------------------

    async def _retrieve_evidence_node(self, state: PlannerState) -> dict[str, Any]:
        """Query Qdrant for relevant evidence chunks."""
        app_desc = state.get("app_description", "")
        evidence_list: list[dict[str, Any]] = []

        if self.knowledge:
            try:
                search_res = await self.knowledge.search(
                    SearchQuery(query=app_desc, limit=4, use_reranker=True)
                )
                for item in search_res.results:
                    link = EvidenceLink(
                        source_id=str(item.source_id) if item.source_id else None,
                        source_title=item.title,
                        collection=(
                            item.collection.value
                            if hasattr(item.collection, "value")
                            else str(item.collection)
                        ),
                        section_path=item.section_path,
                        snippet=(
                            item.text[:280] + ("..." if len(item.text) > 280 else "")
                        ),
                        relevance_score=float(round(item.score, 3)),
                    )
                    evidence_list.append(link.model_dump())
            except Exception as e:
                logger.warning("RAG retrieval failed gracefully: %s", e)

        return {"retrieved_evidence": evidence_list}

    async def _ground_catalog_node(self, state: PlannerState) -> dict[str, Any]:
        """Fetch catalog components to ground the prompt."""
        catalog_summaries: list[str] = [
            "cloudflare (cdn, edge): 100k QPS",
            "kong-gateway (gateway, gateway): 50k QPS",
            "fastapi (compute, application): 20k QPS",
            "redis-cache (cache, data): 100k QPS, supports Geospatial indexing & Sets",
            "postgresql (database, data): 15k QPS, ACID transactional store",
            "rabbitmq (queue, async): 30k QPS AMQP message broker",
            "kafka (streaming, async): 200k QPS distributed commit log",
            "s3 (storage, data): 10k QPS object storage",
        ]
        return {"catalog_context": catalog_summaries}

    async def _generate_proposal_node(self, state: PlannerState) -> dict[str, Any]:
        """Prompt DeepSeek-R1-Distill-Qwen-32B for ArchitectureProposal JSON."""
        app_desc = state.get("app_description", "")
        reqs = state.get("requirements", {})
        evidence = state.get("retrieved_evidence", [])
        catalog = state.get("catalog_context", [])
        error_msg = state.get("error_message")
        planning_context = state.get("planning_context")

        system_prompt = (
            "You are a Principal Cloud Architect using System Design Studio. "
            "You MUST output ONLY a valid JSON object representing an "
            "ArchitectureProposal. Do not include conversational preamble or "
            "markdown codeblocks outside JSON."
        )

        prompt_lines = [
            f"Design an architecture for the following system: {app_desc}",
            f"Non-Functional Requirements: {json.dumps(reqs)}",
        ]
        if planning_context:
            prompt_lines.extend(["", planning_context])
        prompt_lines.append("Grounding Evidence from Knowledge Base:")
        for ev in evidence:
            prompt_lines.append(f"- [{ev.get('source_title')}]: {ev.get('snippet')}")

        prompt_lines.append("\nAllowed Component Catalog Building Blocks:")
        for c in catalog:
            prompt_lines.append(f"- {c}")

        if error_msg:
            prompt_lines.append(
                f"\nIMPORTANT CORRECTION: Your previous output failed schema validation"
                f" with error: {error_msg}. Ensure all required fields (title, summary,"
                " nodes, edges, requirements, assumptions) are provided and nodes match"
                " catalog slugs."
            )

        prompt = "\n".join(prompt_lines)
        raw_output = await self.llm.generate(
            prompt=prompt, system_prompt=system_prompt
        )

        return {"raw_llm_output": raw_output}

    async def _parse_and_validate_node(self, state: PlannerState) -> dict[str, Any]:
        """Parse JSON output from LLM into Pydantic model."""
        raw_text = state.get("raw_llm_output", "") or ""
        retry_count = state.get("retry_count", 0)

        try:
            parsed_json = json.loads(raw_text)
            proposal = ArchitectureProposal.model_validate(parsed_json)
            return {
                "proposal": proposal.model_dump(),
                "error_message": None,
            }
        except Exception as e:
            logger.warning(
                "ArchitectureProposal validation error on attempt %d: %s",
                retry_count + 1,
                e,
            )
            return {
                "proposal": None,
                "error_message": str(e),
                "retry_count": retry_count + 1,
            }

    def _check_schema_decision(self, state: PlannerState) -> str:
        """Route to validator, retry loop, or failure."""
        if state.get("proposal") is not None:
            return "valid"
        if state.get("retry_count", 0) <= state.get("max_retries", 2):
            return "retry"
        return "failed"

    async def _reflect_and_retry_node(self, state: PlannerState) -> dict[str, Any]:
        """Log retry attempt for LLM self-correction."""
        logger.info(
            "Retrying architecture generation (Attempt %d/%d). Error: %s",
            state.get("retry_count", 1),
            state.get("max_retries", 2),
            state.get("error_message"),
        )
        return {}

    async def _run_validator_node(self, state: PlannerState) -> dict[str, Any]:
        """Execute deterministic validator rules over the proposal."""
        prop_data = state.get("proposal")
        if not prop_data:
            return {"validation_issues": [], "is_valid": False}

        proposal = ArchitectureProposal.model_validate(prop_data)
        doc = proposal.as_design_document()
        val_result = self.validator.validate(doc)

        issues_data = [i.model_dump() for i in val_result.issues]
        return {
            "validation_issues": issues_data,
            "is_valid": val_result.valid,
        }

    # -----------------------------------------------------------------------
    # Public Execution
    # -----------------------------------------------------------------------

    async def plan(
        self,
        app_description: str,
        requirements: DesignRequirements | None = None,
        max_retries: int = 2,
        planning_context: str | None = None,
    ) -> PlannerState:
        """Run the full LangGraph planning pipeline."""
        reqs_dict = (
            requirements.model_dump()
            if requirements
            else DesignRequirements().model_dump()
        )

        initial_state: PlannerState = {
            "app_description": app_description,
            "planning_context": planning_context or "",
            "requirements": reqs_dict,
            "retrieved_evidence": [],
            "catalog_context": [],
            "raw_llm_output": None,
            "proposal": None,
            "validation_issues": [],
            "is_valid": False,
            "retry_count": 0,
            "max_retries": max_retries,
            "error_message": None,
        }

        final_state = await self.workflow.ainvoke(initial_state)
        return final_state
