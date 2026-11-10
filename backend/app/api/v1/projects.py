"""REST API router for Projects, Requirements Interview, and Planner."""

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
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
    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at,
        versions_count=0,
    )


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
    projects = await planner_service.list_projects(db, limit=limit, offset=offset)
    return [
        ProjectResponse(
            id=p.id,
            name=p.name,
            description=p.description,
            created_at=p.created_at,
            updated_at=p.updated_at,
            versions_count=len(p.design_versions) if p.design_versions else 0,
        )
        for p in projects
    ]


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
    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at,
        versions_count=len(project.design_versions) if project.design_versions else 0,
    )


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
        version = await planner_service.generate_plan(project_id, req, db)
        return DesignVersionResponse(
            id=version.id,
            project_id=version.project_id,
            version_number=version.version_number,
            title=version.title,
            summary=version.summary,
            requirements=version.requirements,
            nodes=version.nodes,
            edges=version.edges,
            assumptions=version.assumptions,
            evidence_links=version.evidence_links,
            alternatives_considered=version.alternatives_considered,
            validation_issues=version.validation_issues,
            is_valid=version.is_valid,
            created_at=version.created_at,
        )
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
    return DesignVersionResponse(
        id=version.id,
        project_id=version.project_id,
        version_number=version.version_number,
        title=version.title,
        summary=version.summary,
        requirements=version.requirements,
        nodes=version.nodes,
        edges=version.edges,
        assumptions=version.assumptions,
        evidence_links=version.evidence_links,
        alternatives_considered=version.alternatives_considered,
        validation_issues=version.validation_issues,
        is_valid=version.is_valid,
        created_at=version.created_at,
        affected_node_ids=affected_node_ids,
    )



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
    versions = await planner_service.list_design_versions(project_id, db)
    return [
        DesignVersionResponse(
            id=v.id,
            project_id=v.project_id,
            version_number=v.version_number,
            title=v.title,
            summary=v.summary,
            requirements=v.requirements,
            nodes=v.nodes,
            edges=v.edges,
            assumptions=v.assumptions,
            evidence_links=v.evidence_links,
            alternatives_considered=v.alternatives_considered,
            validation_issues=v.validation_issues,
            is_valid=v.is_valid,
            created_at=v.created_at,
        )
        for v in versions
    ]


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
    return DesignVersionResponse(
        id=v.id,
        project_id=v.project_id,
        version_number=v.version_number,
        title=v.title,
        summary=v.summary,
        requirements=v.requirements,
        nodes=v.nodes,
        edges=v.edges,
        assumptions=v.assumptions,
        evidence_links=v.evidence_links,
        alternatives_considered=v.alternatives_considered,
        validation_issues=v.validation_issues,
        is_valid=v.is_valid,
        created_at=v.created_at,
    )
