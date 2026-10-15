import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class FailureMode(BaseModel):
    mode: str = Field(..., description="Failure mode title/scenario")
    impact: str = Field(..., description="Impact on system performance or availability")
    mitigation: str = Field(..., description="Architectural mitigation or fallback")


class CostUnit(BaseModel):
    model: str = Field(
        ..., description="Billing model: provisioned, serverless, tier, transfer"
    )
    unit: str = Field(
        ..., description="Pricing metric (e.g. $/instance-month, $/1M requests)"
    )
    base_monthly_usd: float = Field(0.0, description="Estimated base cost in USD/month")
    free_tier: str | None = Field(None, description="Free tier allowance if applicable")
    notes: str | None = Field(
        None, description="Pricing tier notes and scaling drivers"
    )


class ComponentBase(BaseModel):
    slug: str = Field(
        ..., min_length=2, max_length=100, description="Unique component slug"
    )
    name: str = Field(..., min_length=2, max_length=255, description="Display name")
    category: str = Field(
        ...,
        description=(
            "Category: cdn, gateway, compute, cache, database, queue, "
            "streaming, storage, auth, search, notification, observability, middleware"
        ),
    )
    layer: str = Field(
        ...,
        description=(
            "Architectural layer: edge, gateway, application, data, "
            "async, infra, observability"
        ),
    )
    description: str = Field(
        ..., description="Comprehensive component description and role"
    )
    protocols: list[str] = Field(
        default_factory=list, description="Supported communication protocols"
    )
    limits: dict[str, Any] = Field(
        default_factory=dict,
        description="Hardware, QPS, connection, and capacity limits",
    )
    failure_modes: list[dict[str, Any]] = Field(
        default_factory=list, description="Documented failure modes"
    )
    cost_units: dict[str, Any] = Field(
        default_factory=dict, description="Cost modeling units and drivers"
    )
    alternatives: list[str] = Field(
        default_factory=list, description="Alternative component slugs"
    )
    is_active: bool = Field(True, description="Whether component is active in catalog")


class ComponentCreate(ComponentBase):
    pass


class ComponentUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    layer: str | None = None
    description: str | None = None
    protocols: list[str] | None = None
    limits: dict[str, Any] | None = None
    failure_modes: list[dict[str, Any]] | None = None
    cost_units: dict[str, Any] | None = None
    alternatives: list[str] | None = None
    is_active: bool | None = None


class ComponentResponse(ComponentBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ComponentListResponse(BaseModel):
    total: int
    items: list[ComponentResponse]


class CompatibilityEdgeBase(BaseModel):
    source_slug: str = Field(..., description="Source component slug")
    target_slug: str = Field(..., description="Target component slug")
    is_compatible: bool = Field(
        ..., description="Whether connection is architecturally compatible"
    )
    protocol: str | None = Field(None, description="Communication protocol")
    recommended_pattern: str | None = Field(
        None, description="Recommended architectural pattern"
    )
    constraints: dict[str, Any] = Field(
        default_factory=dict, description="Operational constraints"
    )
    reason: str | None = Field(
        None, description="Rationale for compatibility or incompatibility"
    )


class CompatibilityEdgeCreate(CompatibilityEdgeBase):
    pass


class CompatibilityEdgeResponse(CompatibilityEdgeBase):
    id: uuid.UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CompatibilityCheckRequest(BaseModel):
    source_slug: str = Field(..., description="Source component slug")
    target_slug: str = Field(..., description="Target component slug")


class CompatibilityCheckResponse(BaseModel):
    source_slug: str
    target_slug: str
    compatible: bool
    protocol: str | None = None
    recommended_pattern: str | None = None
    limits: dict[str, Any] = Field(default_factory=dict)
    reason: str
    warnings: list[str] = Field(default_factory=list)
