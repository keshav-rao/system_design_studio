import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.catalog import (
    CompatibilityCheckResponse,
    CompatibilityEdgeCreate,
    CompatibilityEdgeResponse,
    ComponentCreate,
    ComponentListResponse,
    ComponentResponse,
    ComponentUpdate,
)
from app.services.catalog.catalog_service import catalog_service

router = APIRouter(prefix="/catalog", tags=["catalog"])


@router.get(
    "/components",
    response_model=ComponentListResponse,
    status_code=status.HTTP_200_OK,
    summary="List components with optional category, layer, or keyword filter",
)
async def list_components(
    category: Annotated[str | None, Query(description="Filter by category")] = None,
    layer: Annotated[
        str | None, Query(description="Filter by architectural layer")
    ] = None,
    search: Annotated[
        str | None, Query(description="Search by name, slug or description")
    ] = None,
    limit: Annotated[int, Query(ge=1, le=200)] = 100,
    offset: Annotated[int, Query(ge=0)] = 0,
    db: AsyncSession = Depends(get_db),
) -> ComponentListResponse:
    items, total = await catalog_service.get_components(
        db, category=category, layer=layer, search=search, limit=limit, offset=offset
    )
    return ComponentListResponse(
        total=total, items=[ComponentResponse.model_validate(c) for c in items]
    )


@router.get(
    "/components/{slug_or_id}",
    response_model=ComponentResponse,
    status_code=status.HTTP_200_OK,
    summary="Get detailed component specifications, limits, failure modes and costs",
)
async def get_component(
    slug_or_id: str,
    db: AsyncSession = Depends(get_db),
) -> ComponentResponse:
    comp = await catalog_service.get_component_by_slug_or_id(db, slug_or_id)
    if not comp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Component '{slug_or_id}' not found in catalog.",
        )
    return ComponentResponse.model_validate(comp)


@router.post(
    "/components",
    response_model=ComponentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new component in the catalog",
)
async def create_component(
    comp_in: ComponentCreate,
    db: AsyncSession = Depends(get_db),
) -> ComponentResponse:
    existing = await catalog_service.get_component_by_slug_or_id(db, comp_in.slug)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"A component with slug '{comp_in.slug}' already exists.",
        )
    comp = await catalog_service.create_component(db, comp_in)
    return ComponentResponse.model_validate(comp)


@router.put(
    "/components/{component_id}",
    response_model=ComponentResponse,
    status_code=status.HTTP_200_OK,
    summary="Update an existing component",
)
async def update_component(
    component_id: uuid.UUID,
    comp_in: ComponentUpdate,
    db: AsyncSession = Depends(get_db),
) -> ComponentResponse:
    updated = await catalog_service.update_component(db, component_id, comp_in)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Component ID '{component_id}' not found.",
        )
    return ComponentResponse.model_validate(updated)


@router.delete(
    "/components/{component_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a component from the catalog",
)
async def delete_component(
    component_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
) -> None:
    deleted = await catalog_service.delete_component(db, component_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Component ID '{component_id}' not found.",
        )


@router.get(
    "/compatibility/check",
    response_model=CompatibilityCheckResponse,
    status_code=status.HTTP_200_OK,
    summary="Check architectural connection compatibility between two components",
)
async def check_compatibility(
    source: Annotated[
        str, Query(description="Source component slug (e.g. 'fastapi-app-server')")
    ],
    target: Annotated[
        str, Query(description="Target component slug (e.g. 'postgresql')")
    ],
    db: AsyncSession = Depends(get_db),
) -> CompatibilityCheckResponse:
    return await catalog_service.check_compatibility(
        db, source_slug=source, target_slug=target
    )


@router.post(
    "/compatibility",
    response_model=CompatibilityEdgeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add or update a component compatibility edge",
)
async def add_compatibility_edge(
    edge_in: CompatibilityEdgeCreate,
    db: AsyncSession = Depends(get_db),
) -> CompatibilityEdgeResponse:
    edge = await catalog_service.add_compatibility_edge(db, edge_in)
    return CompatibilityEdgeResponse.model_validate(edge)


@router.post(
    "/seed",
    status_code=status.HTTP_200_OK,
    summary="Seed or update the standard 38+ components and compatibility matrix",
)
async def seed_catalog(
    force: Annotated[
        bool, Query(description="If true, clears existing catalog prior to seeding")
    ] = False,
    db: AsyncSession = Depends(get_db),
) -> dict[str, int]:
    return await catalog_service.seed_catalog(db, force=force)
