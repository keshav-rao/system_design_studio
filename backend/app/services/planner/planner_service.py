"""Planner Service coordinating the LangGraph workflow, DB persistence, and projects."""

import json
import logging
import uuid
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project
from app.repositories import DesignRepository, ProjectRepository
from app.schemas.planner import (
    DesignSnapshot,
    DesignVersionResponse,
    EvidenceLink,
    InterviewRequest,
    InterviewResponse,
    PlanRequest,
    ProjectCreate,
    RedesignRequest,
)
from app.schemas.validator import (
    DesignDocument,
    DesignEdge,
    DesignNode,
    DesignRequirements,
)
from app.services.catalog.catalog_service import CatalogService
from app.services.knowledge.service import KnowledgeService
from app.services.planner.graph import ArchitecturePlannerGraph
from app.services.planner.interview_service import InterviewService
from app.services.planner.providers import get_llm_adapter
from app.services.planner.providers.base import BaseLLMAdapter
from app.services.validator.validator_service import ValidatorService

logger = logging.getLogger(__name__)


class PlannerService:
    """Service facade for architecture planning and project lifecycle."""

    def __init__(
        self,
        llm_adapter: BaseLLMAdapter | None = None,
        knowledge_service: KnowledgeService | None = None,
        catalog_service: CatalogService | None = None,
        validator_service: ValidatorService | None = None,
    ) -> None:
        self.llm = llm_adapter or get_llm_adapter()
        self.knowledge = knowledge_service
        self.catalog = catalog_service
        self.validator = validator_service or ValidatorService()
        self.interview_service = InterviewService()
        self.graph = ArchitecturePlannerGraph(
            llm_adapter=self.llm,
            knowledge_service=self.knowledge,
            catalog_service=self.catalog,
            validator_service=self.validator,
        )

    # -----------------------------------------------------------------------
    # Projects CRUD
    # -----------------------------------------------------------------------

    async def create_project(self, req: ProjectCreate, db: AsyncSession) -> Project:
        """Create a new architecture design project."""
        return await ProjectRepository(db).create(req.name, req.description)

    async def list_projects(
        self, db: AsyncSession, limit: int = 50, offset: int = 0
    ) -> list[tuple[Project, int]]:
        """List projects with their design version counts."""
        return await ProjectRepository(db).list_with_version_counts(limit, offset)

    async def get_project(
        self, project_id: uuid.UUID, db: AsyncSession
    ) -> Project | None:
        """Retrieve project by ID."""
        return await ProjectRepository(db).get(project_id)

    # -----------------------------------------------------------------------
    # Requirements Interview
    # -----------------------------------------------------------------------

    def interview(self, req: InterviewRequest) -> InterviewResponse:
        """Run an interview iteration to capture and infer NFR requirements."""
        return self.interview_service.process_interview(req)

    # -----------------------------------------------------------------------
    # Plan Generation & Versioning via LangGraph
    # -----------------------------------------------------------------------

    async def generate_plan(
        self,
        project_id: uuid.UUID,
        req: PlanRequest,
        db: AsyncSession,
    ) -> DesignVersionResponse:
        """Execute LangGraph workflow and persist the proposal as a new version."""
        projects = ProjectRepository(db)
        project = await projects.get(project_id)
        if not project:
            raise ValueError(f"Project with ID '{project_id}' not found.")

        final_reqs = req.requirements
        assumed_keys: set[str] = set()
        if not final_reqs and req.interview_answers:
            interview_res = self.interview_service.process_interview(
                InterviewRequest(
                    app_description=req.app_description,
                    answers=req.interview_answers,
                )
            )
            final_reqs = interview_res.inferred_requirements
            answered = {a.question_id for a in req.interview_answers}
            assumed_keys = set(final_reqs.model_dump()) - answered
        elif not final_reqs:
            assumed_keys = set(DesignRequirements.model_fields)

        await projects.set_status(project, "planning")
        state = await self.graph.plan(
            app_description=req.app_description,
            requirements=final_reqs,
        )

        proposal_data: dict[str, Any] = state.get("proposal") or {}
        if not proposal_data:
            await projects.set_status(project, "interviewing")
            raise RuntimeError(
                f"Architecture generation failed: {state.get('error_message')}"
            )

        snapshot = DesignSnapshot.model_validate(
            {
                **proposal_data,
                "title": proposal_data.get("title") or "",
                "validation_issues": state.get("validation_issues", []),
            }
        )
        self._link_node_evidence(snapshot)
        await projects.upsert_requirements(
            project_id, snapshot.requirements.model_dump(), assumed_keys
        )
        designs = DesignRepository(db)
        latest = await designs.latest(project_id)
        design = await designs.create(
            project_id,
            snapshot,
            parent_version=latest.version if latest else None,
            creator="planner",
        )
        await projects.set_status(project, "designed")
        return DesignRepository.to_response(design)

    async def redesign(
        self,
        project_id: uuid.UUID,
        req: RedesignRequest,
        db: AsyncSession,
    ) -> tuple[DesignVersionResponse, list[str]]:
        """Re-plan an affected subgraph and persist it as a new version."""
        designs = DesignRepository(db)
        previous_design = await designs.latest(project_id)
        if previous_design is None:
            raise LookupError(f"No design versions found for project '{project_id}'.")
        previous = DesignRepository.to_snapshot(previous_design)
        previous_edges = [e.model_dump() for e in previous.edges]

        old_requirements = previous.requirements
        old_requirement_values = old_requirements.model_dump()
        new_requirements = req.requirements or old_requirements
        changed_requirements = {
            key
            for key, value in new_requirements.model_dump().items()
            if value != old_requirement_values.get(key)
        }
        old_nodes = previous.nodes
        nodes_by_id = {node.id: node for node in old_nodes}
        unknown_ids = set(req.affected_node_ids) - nodes_by_id.keys()
        if unknown_ids:
            raise ValueError(
                f"Unknown affected node IDs: {', '.join(sorted(unknown_ids))}"
            )

        seeds = set(req.affected_node_ids)
        seeds.update(
            self._nodes_affected_by_change(
                old_nodes, changed_requirements, req.change_description
            )
        )
        if not seeds:
            raise ValueError(
                "Could not determine affected components. Select one or more nodes "
                "or describe a supported requirement/component change."
            )

        scope_ids = set(seeds)
        for edge in previous_edges:
            if edge["source_id"] in seeds:
                scope_ids.add(edge["target_id"])
            if edge["target_id"] in seeds:
                scope_ids.add(edge["source_id"])
        scoped_nodes = [node.model_dump() for node in old_nodes if node.id in scope_ids]
        context = (
            "ITERATIVE REDESIGN: Re-plan only the affected subgraph. "
            "Keep these existing node IDs stable for all retained components and "
            "do not redesign components outside the supplied scope. Return only "
            "the changed subgraph in nodes/edges; include the stable IDs of every "
            "affected node. Preserve connections to unchanged boundary nodes.\n"
            f"Change requested: {req.change_description}\n"
            f"Affected node IDs: {sorted(seeds)}\n"
            f"Subgraph context (includes neighboring boundary nodes): "
            f"{json.dumps(scoped_nodes)}\n"
            f"Existing design summary: {previous.summary}"
        )
        state = await self.graph.plan(
            app_description=(
                f"{previous.title}. Focused redesign request: {req.change_description}"
            ),
            requirements=new_requirements,
            planning_context=context,
        )
        proposal_data: dict[str, Any] = state.get("proposal") or {}
        if not proposal_data:
            raise RuntimeError(
                f"Architecture redesign failed: {state.get('error_message')}"
            )

        proposed_nodes = [
            DesignNode.model_validate(node) for node in proposal_data.get("nodes", [])
        ]
        proposed_edges = proposal_data.get("edges", [])
        proposed_ids = {node.id for node in proposed_nodes}
        if not seeds.issubset(proposed_ids):
            missing_ids = sorted(seeds - proposed_ids)
            raise RuntimeError(
                "Planner did not preserve affected node IDs: "
                + ", ".join(missing_ids)
            )

        merged_node_ids = set(nodes_by_id) | {
            node.id
            for node in proposed_nodes
            if node.id in seeds
            or (
                node.id not in nodes_by_id
                and any(
                    (
                        edge["source_id"] == node.id
                        and edge["target_id"] in seeds
                    )
                    or (
                        edge["target_id"] == node.id
                        and edge["source_id"] in seeds
                    )
                    for edge in proposed_edges
                )
            )
        }
        new_nodes = [
            node
            for node in proposed_nodes
            if (
                node.id in merged_node_ids and node.id not in nodes_by_id
            )
            or node.id in seeds
        ]
        merged_nodes = [
            node.model_dump() for node in old_nodes if node.id not in seeds
        ] + [node.model_dump() for node in new_nodes]
        retained_edges = [
            edge
            for edge in previous_edges
            if edge["source_id"] not in seeds and edge["target_id"] not in seeds
        ]
        new_edges = [
            edge
            for edge in proposed_edges
            if edge["source_id"] in merged_node_ids
            and edge["target_id"] in merged_node_ids
            and (edge["source_id"] in seeds or edge["target_id"] in seeds)
        ]
        merged_edges = self._unique_edges(retained_edges + new_edges)
        validation = self.validator.validate(
            DesignDocument(
                nodes=merged_nodes,
                edges=merged_edges,
                requirements=new_requirements,
            )
        )

        next_version = previous_design.version + 1
        snapshot = DesignSnapshot(
            title=previous.title,
            summary=(
                f"{previous.summary}\n\n"
                f"Redesign v{next_version}: "
                f"{proposal_data.get('summary', previous.summary)}"
            ),
            requirements=new_requirements,
            nodes=[DesignNode.model_validate(n) for n in merged_nodes],
            edges=[DesignEdge.model_validate(e) for e in merged_edges],
            assumptions=list(
                dict.fromkeys(
                    previous.assumptions + proposal_data.get("assumptions", [])
                )
            ),
            evidence_links=self._merge_records(
                [e.model_dump() for e in previous.evidence_links],
                proposal_data.get("evidence_links", []),
            ),
            alternatives_considered=self._merge_records(
                [a.model_dump() for a in previous.alternatives_considered],
                proposal_data.get("alternatives_considered", []),
            ),
            unaddressed_requirements=proposal_data.get(
                "unaddressed_requirements", previous.unaddressed_requirements
            ),
            open_questions=proposal_data.get("open_questions", previous.open_questions),
            validation_issues=validation.issues,
        )
        self._link_node_evidence(snapshot)
        await ProjectRepository(db).upsert_requirements(
            project_id, new_requirements.model_dump(), set()
        )
        design = await designs.create(
            project_id,
            snapshot,
            parent_version=previous_design.version,
            creator="planner",
        )
        return DesignRepository.to_response(design, sorted(seeds)), sorted(seeds)

    @staticmethod
    def _nodes_affected_by_change(
        nodes: list[DesignNode],
        changed_requirements: set[str],
        description: str,
    ) -> set[str]:
        """Map changed NFRs and common component terms to relevant catalog nodes."""
        category_groups: list[set[str]] = []
        if changed_requirements.intersection({"expected_users", "expected_qps"}):
            category_groups.append(
                {"compute", "cache", "database", "queue", "streaming", "gateway"}
            )
        if "availability_target" in changed_requirements:
            category_groups.append(
                {"compute", "cache", "database", "queue", "streaming", "gateway"}
            )
        if "data_durability_required" in changed_requirements:
            category_groups.append({"database", "storage"})
        if "regions" in changed_requirements:
            category_groups.append({node.category for node in nodes})

        terms_by_category = {
            "database": {"database", "db", "postgres", "postgresql", "sql", "mongo"},
            "storage": {"storage", "object", "s3", "durability"},
            "cache": {"cache", "redis"},
            "queue": {"queue", "rabbitmq", "async", "broker"},
            "streaming": {"stream", "kafka", "event"},
            "compute": {"compute", "service", "application", "api", "users", "traffic"},
            "gateway": {"gateway", "proxy", "ingress"},
        }
        words = set(description.lower().replace("-", " ").replace("_", " ").split())
        inferred_categories = {
            category
            for category, terms in terms_by_category.items()
            if words.intersection(terms)
        }
        if words.intersection({"region", "regions", "global", "geography"}):
            inferred_categories.update(node.category for node in nodes)
        category_groups.extend([{category} for category in inferred_categories])
        return {
            node.id
            for node in nodes
            if any(node.category in categories for categories in category_groups)
        }

    @staticmethod
    def _unique_edges(edges: list[dict[str, Any]]) -> list[dict[str, Any]]:
        unique: dict[tuple[str, str, str | None], dict[str, Any]] = {}
        for edge in edges:
            key = (edge["source_id"], edge["target_id"], edge.get("protocol"))
            unique[key] = edge
        return list(unique.values())

    @staticmethod
    def _merge_records(
        existing: list[dict[str, Any]], updated: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        merged: dict[str, dict[str, Any]] = {}
        for record in existing + updated:
            key = str(record.get("source_id") or record.get("component_slug") or record)
            merged[key] = record
        return list(merged.values())

    @staticmethod
    def _link_node_evidence(snapshot: DesignSnapshot) -> None:
        """Give evidence stable IDs and attribute it to the nodes it mentions."""
        for idx, link in enumerate(snapshot.evidence_links):
            if not link.id:
                link.id = link.chunk_id or f"ev{idx + 1}"
        known = {link.id for link in snapshot.evidence_links}
        for node in snapshot.nodes:
            node.evidence_ids = [e for e in node.evidence_ids if e in known]
            if node.evidence_ids:
                continue
            terms = {
                t
                for t in (
                    node.slug.lower().replace("_", "-").split("-")
                    + [node.category.lower()]
                )
                if len(t) > 2
            }
            node.evidence_ids = [
                link.id
                for link in snapshot.evidence_links
                if link.id and _mentions_any(link, terms)
            ]

    async def list_design_versions(
        self, project_id: uuid.UUID, db: AsyncSession
    ) -> list[DesignVersionResponse]:
        """List all historical design versions for a project, newest first."""
        designs = await DesignRepository(db).list_for_project(project_id)
        return [DesignRepository.to_response(d) for d in designs]

    async def get_latest_design_version(
        self, project_id: uuid.UUID, db: AsyncSession
    ) -> DesignVersionResponse | None:
        """Get latest design version for a project."""
        design = await DesignRepository(db).latest(project_id)
        return DesignRepository.to_response(design) if design else None


def _mentions_any(link: EvidenceLink, terms: set[str]) -> bool:
    haystack = " ".join(
        [link.source_title, link.section_path or "", link.snippet]
    ).lower()
    return any(term in haystack for term in terms)
