"""Planner Service coordinating the LangGraph workflow, DB persistence, and projects."""

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
