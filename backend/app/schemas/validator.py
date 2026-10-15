"""Pydantic v2 schemas for design validation input/output.

A DesignDocument describes an architecture proposal: nodes (components) and
edges (connections).  The validator runs deterministic rules over this
structure and produces a list of ValidationIssues.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Severity
# ---------------------------------------------------------------------------

class Severity(StrEnum):
    """How serious the violation is."""

    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


# ---------------------------------------------------------------------------
# Design input
# ---------------------------------------------------------------------------

class DesignNode(BaseModel):
    """A single component placed in the design."""

    id: str = Field(..., description="Unique node identifier in this design")
    slug: str = Field(
        ..., description="Component catalog slug (e.g. 'postgresql', 'redis-cache')"
    )
    category: str = Field(
        ..., description="Component category from the catalog"
    )
    layer: str = Field(
        ...,
        description=(
            "Architectural layer: edge, gateway, application, "
            "data, async, infra, observability"
        ),
    )
    replicas: int = Field(
        1, ge=1, description="Number of replicas / instances"
    )
    protocols: list[str] = Field(
        default_factory=list,
        description="Protocols this node exposes or consumes",
    )
    limits: dict[str, Any] = Field(
        default_factory=dict,
        description="Operational limits from the catalog",
    )
    config: dict[str, Any] = Field(
        default_factory=dict,
        description="User-specified configuration overrides",
    )


class DesignEdge(BaseModel):
    """A directed connection between two nodes."""

    source_id: str = Field(..., description="Source node id")
    target_id: str = Field(..., description="Target node id")
    protocol: str | None = Field(
        default=None, description="Communication protocol used on this edge"
    )
    label: str | None = Field(
        default=None, description="Human-readable label for the edge"
    )


class DesignRequirements(BaseModel):
    """High-level requirements that the design must satisfy."""

    expected_users: int | None = Field(
        default=None, ge=0, description="Expected concurrent user count"
    )
    expected_qps: int | None = Field(
        default=None, ge=0, description="Expected queries per second"
    )
    availability_target: float | None = Field(
        default=None,
        ge=0.0,
        le=100.0,
        description="Availability SLA target as a percentage (e.g. 99.99)",
    )
    data_durability_required: bool = Field(
        default=True, description="Whether the design must include durable storage"
    )
    regions: int = Field(
        default=1, ge=1, description="Number of deployment regions"
    )


class DesignDocument(BaseModel):
    """Complete architecture design to validate."""

    nodes: list[DesignNode] = Field(
        ..., min_length=1, description="Components in the design"
    )
    edges: list[DesignEdge] = Field(
        default_factory=list, description="Connections between components"
    )
    requirements: DesignRequirements = Field(
        default_factory=DesignRequirements,
        description="Non-functional requirements",
    )


# ---------------------------------------------------------------------------
# Validation output
# ---------------------------------------------------------------------------

class ValidationIssue(BaseModel):
    """One problem or recommendation found by a rule."""

    rule_id: str = Field(..., description="Unique rule identifier (e.g. 'no-spof')")
    severity: Severity = Field(..., description="Error, warning, or info")
    message: str = Field(..., description="Human-readable explanation")
    node_ids: list[str] = Field(
        default_factory=list,
        description="Node IDs involved in this issue",
    )
    edge_ids: list[str] = Field(
        default_factory=list,
        description="Edge source->target pairs involved (as 'src_id->tgt_id')",
    )
    suggestion: str | None = Field(
        default=None, description="Actionable fix suggestion"
    )


class ValidationResult(BaseModel):
    """Aggregated validation output for a design."""

    valid: bool = Field(
        ..., description="True if zero errors (warnings are acceptable)"
    )
    total_issues: int = Field(..., description="Total issue count")
    errors: int = Field(default=0, description="Count of ERROR severity issues")
    warnings: int = Field(default=0, description="Count of WARNING severity issues")
    infos: int = Field(default=0, description="Count of INFO severity issues")
    issues: list[ValidationIssue] = Field(
        default_factory=list, description="All issues found"
    )
    rules_executed: list[str] = Field(
        default_factory=list, description="Rule IDs that were evaluated"
    )
    elapsed_ms: float = Field(
        default=0.0, description="Total validation time in milliseconds"
    )

