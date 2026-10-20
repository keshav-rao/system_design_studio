"""Planner Service coordinating the LangGraph workflow, DB persistence, and projects."""

import json
import logging
import uuid
from typing import Any

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.project import DesignVersion, Project
from app.schemas.planner import (
    InterviewRequest,
    InterviewResponse,
    PlanRequest,
    ProjectCreate,
    RedesignRequest,
)
from app.schemas.validator import DesignDocument, DesignNode, DesignRequirements
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
        project = Project(
            id=uuid.uuid4(),
            name=req.name,
            description=req.description,
        )
        db.add(project)
        await db.commit()
        await db.refresh(project)
        return project

    async def list_projects(
        self, db: AsyncSession, limit: int = 50, offset: int = 0
    ) -> list[Project]:
        """List all architecture projects."""
        stmt = (
            select(Project)
            .options(selectinload(Project.design_versions))
            .order_by(desc(Project.created_at))
            .limit(limit)
            .offset(offset)
        )
        result = await db.execute(stmt)
        return list(result.scalars().all())

    async def get_project(
        self, project_id: uuid.UUID, db: AsyncSession
    ) -> Project | None:
        """Retrieve project by ID."""
        stmt = (
            select(Project)
            .options(selectinload(Project.design_versions))
            .where(Project.id == project_id)
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

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
    ) -> DesignVersion:
        """Execute LangGraph workflow and persist proposal as a DesignVersion."""
        project = await self.get_project(project_id, db)
        if not project:
            raise ValueError(f"Project with ID '{project_id}' not found.")

        # Determine next version number
        stmt = (
            select(DesignVersion.version_number)
            .where(DesignVersion.project_id == project_id)
            .order_by(desc(DesignVersion.version_number))
            .limit(1)
        )
        last_version = (await db.execute(stmt)).scalar_one_or_none() or 0
        next_version = last_version + 1

        # Resolve requirements: from explicit request or inferred from interview
        final_reqs = req.requirements
        if not final_reqs and req.interview_answers:
            interview_res = self.interview_service.process_interview(
                InterviewRequest(
                    app_description=req.app_description,
                    answers=req.interview_answers,
                )
            )
            final_reqs = interview_res.inferred_requirements

        # Run LangGraph pipeline
        state = await self.graph.plan(
            app_description=req.app_description,
            requirements=final_reqs,
        )

        proposal_data: dict[str, Any] = state.get("proposal") or {}
        if not proposal_data:
            # Fallback if generation failed even after retries
            raise RuntimeError(
                f"Architecture generation failed: {state.get('error_message')}"
            )

        # Build and store DesignVersion snapshot
        design_version = DesignVersion(
            id=uuid.uuid4(),
            project_id=project_id,
            version_number=next_version,
            title=proposal_data.get("title", f"Design v{next_version}"),
            summary=proposal_data.get("summary", ""),
            requirements=proposal_data.get("requirements", {}),
            nodes=proposal_data.get("nodes", []),
            edges=proposal_data.get("edges", []),
            assumptions=proposal_data.get("assumptions", []),
            evidence_links=proposal_data.get("evidence_links", []),
            alternatives_considered=proposal_data.get("alternatives_considered", []),
            validation_issues=state.get("validation_issues", []),
            is_valid=state.get("is_valid", False),
        )

        db.add(design_version)
        await db.commit()
        await db.refresh(design_version)
        return design_version

    async def redesign(
        self,
        project_id: uuid.UUID,
        req: RedesignRequest,
        db: AsyncSession,
    ) -> tuple[DesignVersion, list[str]]:
        """Re-plan an affected subgraph and persist it as a new version."""
        previous = await self.get_latest_design_version(project_id, db)
        if previous is None:
            raise LookupError(f"No design versions found for project '{project_id}'.")

        old_requirements = DesignRequirements.model_validate(previous.requirements)
        old_requirement_values = old_requirements.model_dump()
        new_requirements = req.requirements or old_requirements
        changed_requirements = {
            key
            for key, value in new_requirements.model_dump().items()
            if value != old_requirement_values.get(key)
        }
        old_nodes = [DesignNode.model_validate(node) for node in previous.nodes]
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
        for edge in previous.edges:
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
            for edge in previous.edges
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

        design_version = DesignVersion(
            id=uuid.uuid4(),
            project_id=project_id,
            version_number=previous.version_number + 1,
            title=previous.title,
            summary=(
                f"{previous.summary}\n\n"
                f"Redesign v{previous.version_number + 1}: "
                f"{proposal_data.get('summary', previous.summary)}"
            ),
            requirements=new_requirements.model_dump(),
            nodes=merged_nodes,
            edges=merged_edges,
            assumptions=list(
                dict.fromkeys(
                    previous.assumptions + proposal_data.get("assumptions", [])
                )
            ),
            evidence_links=self._merge_records(
                previous.evidence_links, proposal_data.get("evidence_links", [])
            ),
            alternatives_considered=self._merge_records(
                previous.alternatives_considered,
                proposal_data.get("alternatives_considered", []),
            ),
            validation_issues=[issue.model_dump() for issue in validation.issues],
            is_valid=validation.valid,
        )
        db.add(design_version)
        await db.commit()
        await db.refresh(design_version)
        return design_version, sorted(seeds)

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

    async def list_design_versions(
        self, project_id: uuid.UUID, db: AsyncSession
    ) -> list[DesignVersion]:
        """List all historical design versions for a project."""
        stmt = (
            select(DesignVersion)
            .where(DesignVersion.project_id == project_id)
            .order_by(desc(DesignVersion.version_number))
        )
        result = await db.execute(stmt)
        return list(result.scalars().all())

    async def get_latest_design_version(
        self, project_id: uuid.UUID, db: AsyncSession
    ) -> DesignVersion | None:
        """Get latest design version for a project."""
        stmt = (
            select(DesignVersion)
            .where(DesignVersion.project_id == project_id)
            .order_by(desc(DesignVersion.version_number))
            .limit(1)
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
