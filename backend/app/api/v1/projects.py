"""REST API router for Projects, Requirements Interview, and Planner."""

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.project import Project
from app.repositories import ProjectRepository
from app.schemas.planner import (
    DesignVersionResponse,
    InterviewRequest,
    InterviewResponse,
    PlanRequest,
    ProjectCreate,
    ProjectResponse,
    RedesignRequest,
)
from app.services.catalog.catalog_service import catalog_service
from app.services.knowledge.service import KnowledgeService, get_knowledge_service
from app.services.planner.planner_service import PlannerService
from app.services.validator.validator_service import ValidatorService

router = APIRouter(prefix="/projects", tags=["projects", "planner"])


def get_planner_service(
    knowledge_service: KnowledgeService = Depends(get_knowledge_service),
) -> PlannerService:
    """Dependency provider for PlannerService."""
    return PlannerService(
        knowledge_service=knowledge_service,
        catalog_service=catalog_service,
        validator_service=ValidatorService(),
    )


def _project_response(project: Project, versions_count: int) -> ProjectResponse:
    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        status=project.status,
        created_at=project.created_at,
        updated_at=project.updated_at,
        versions_count=versions_count,
    )


# ---------------------------------------------------------------------------
# Project Lifecycle Endpoints
# ---------------------------------------------------------------------------


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new system design project",
)
async def create_project(
    req: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    planner_service: PlannerService = Depends(get_planner_service),
) -> ProjectResponse:
    project = await planner_service.create_project(req, db)
    return _project_response(project, 0)


@router.get(
    "",
    response_model=list[ProjectResponse],
    summary="List all system design projects",
)
async def list_projects(
    limit: int = 50,
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
    planner_service: PlannerService = Depends(get_planner_service),
) -> list[ProjectResponse]:
    rows = await planner_service.list_projects(db, limit=limit, offset=offset)
    return [_project_response(p, count) for p, count in rows]


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
    summary="Get project details by ID",
)
async def get_project(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    planner_service: PlannerService = Depends(get_planner_service),
) -> ProjectResponse:
    project = await planner_service.get_project(project_id, db)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID '{project_id}' not found.",
        )
    count = await ProjectRepository(db).count_versions(project_id)
    return _project_response(project, count)


# ---------------------------------------------------------------------------
# Requirements Interview Endpoints
# ---------------------------------------------------------------------------


@router.post(
    "/interview",
    response_model=InterviewResponse,
    summary="Conduct requirements interview (fixed + adaptive questioning)",
)
async def conduct_interview(
    req: InterviewRequest,
    planner_service: PlannerService = Depends(get_planner_service),
) -> InterviewResponse:
    return planner_service.interview(req)


# ---------------------------------------------------------------------------
# Plan Generation & Design Versioning Endpoints
# ---------------------------------------------------------------------------


@router.post(
    "/{project_id}/plan",
    response_model=DesignVersionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Generate architecture proposal via LangGraph and DeepSeek-R1",
)
async def generate_plan(
    project_id: uuid.UUID,
    req: PlanRequest,
    db: AsyncSession = Depends(get_db),
    planner_service: PlannerService = Depends(get_planner_service),
) -> DesignVersionResponse:
    try:
        return await planner_service.generate_plan(project_id, req, db)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Planning generation failed: {e}",
        ) from e


@router.post(
    "/{project_id}/redesign",
    response_model=DesignVersionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Re-plan an affected design subgraph and create a new version",
)
async def redesign(
    project_id: uuid.UUID,
    req: RedesignRequest,
    db: AsyncSession = Depends(get_db),
    planner_service: PlannerService = Depends(get_planner_service),
) -> DesignVersionResponse:
    try:
        version, affected_node_ids = await planner_service.redesign(
            project_id, req, db
        )
    except LookupError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
        ) from e
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Architecture redesign failed: {e}",
        ) from e
    return version


@router.get(
    "/{project_id}/designs",
    response_model=list[DesignVersionResponse],
    summary="List all design versions for a project",
)
async def list_design_versions(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    planner_service: PlannerService = Depends(get_planner_service),
) -> list[DesignVersionResponse]:
    return await planner_service.list_design_versions(project_id, db)


@router.get(
    "/{project_id}/designs/latest",
    response_model=DesignVersionResponse,
    summary="Get latest design version for a project",
)
async def get_latest_design_version(
    project_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    planner_service: PlannerService = Depends(get_planner_service),
) -> DesignVersionResponse:
    v = await planner_service.get_latest_design_version(project_id, db)
    if not v:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No design versions found for project '{project_id}'.",
        )
    return v
