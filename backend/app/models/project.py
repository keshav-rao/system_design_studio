"""Projects, requirements, and normalized append-only design versions."""

import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.core.database import Base

JSONType = JSON().with_variant(JSONB, "postgresql")


def _now() -> datetime:
    return datetime.now(UTC)


class User(Base):
    """Owner of projects. v1 runs single-user with one default row."""

    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_now, nullable=False
    )


class Project(Base):
    """A system architecture project."""

    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(32), nullable=False, default="interviewing"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_now, onupdate=_now, nullable=False
    )

    designs: Mapped[list["Design"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
        order_by="desc(Design.version)",
    )
    requirements: Mapped[list["Requirement"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )


class Requirement(Base):
    """Current value of one requirement for a project."""

    __tablename__ = "requirements"
    __table_args__ = (UniqueConstraint("project_id", "key"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True
    )
    key: Mapped[str] = mapped_column(String(100), nullable=False)
    value: Mapped[Any] = mapped_column(JSONType, nullable=True)
    is_assumed: Mapped[bool] = mapped_column(default=False, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_now, onupdate=_now, nullable=False
    )

    project: Mapped[Project] = relationship(back_populates="requirements")


class Design(Base):
    """An immutable design version. The graph lives in design_nodes/design_edges."""

    __tablename__ = "designs"
    __table_args__ = (UniqueConstraint("project_id", "version"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True
    )
    version: Mapped[int] = mapped_column(Integer, nullable=False)
    parent_version: Mapped[int | None] = mapped_column(Integer, nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False, default="")
    requirements: Mapped[dict[str, Any]] = mapped_column(
        JSONType, nullable=False, default=dict
    )
    assumptions: Mapped[list[str]] = mapped_column(
        JSONType, nullable=False, default=list
    )
    alternatives_considered: Mapped[list[dict[str, Any]]] = mapped_column(
        JSONType, nullable=False, default=list
    )
    unaddressed_requirements: Mapped[list[str]] = mapped_column(
        JSONType, nullable=False, default=list
    )
    open_questions: Mapped[list[str]] = mapped_column(
        JSONType, nullable=False, default=list
    )
    validation_status: Mapped[str] = mapped_column(
        String(16), nullable=False, default="valid"
    )
    creator: Mapped[str] = mapped_column(String(16), nullable=False, default="planner")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_now, nullable=False
    )

    project: Mapped[Project] = relationship(back_populates="designs")
    nodes: Mapped[list["DesignNodeRecord"]] = relationship(
        back_populates="design",
        cascade="all, delete-orphan",
        order_by="DesignNodeRecord.sort_order",
    )
    edges: Mapped[list["DesignEdgeRecord"]] = relationship(
        back_populates="design",
        cascade="all, delete-orphan",
        order_by="DesignEdgeRecord.sort_order",
    )
    evidence: Mapped[list["NodeEvidence"]] = relationship(
        back_populates="design",
        cascade="all, delete-orphan",
        order_by="NodeEvidence.sort_order",
    )
    issues: Mapped[list["ValidationIssueRecord"]] = relationship(
        back_populates="design",
        cascade="all, delete-orphan",
        order_by="ValidationIssueRecord.sort_order",
    )


class DesignNodeRecord(Base):
    """One component placed in a design version."""

    __tablename__ = "design_nodes"
    __table_args__ = (UniqueConstraint("design_id", "node_key"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    design_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("designs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    node_key: Mapped[str] = mapped_column(String(100), nullable=False)
    component_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("components.id", ondelete="SET NULL"), nullable=True
    )
    slug: Mapped[str] = mapped_column(String(100), nullable=False)
    label: Mapped[str | None] = mapped_column(String(255), nullable=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    layer: Mapped[str] = mapped_column(String(50), nullable=False)
    replicas: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    protocols: Mapped[list[str]] = mapped_column(JSONType, nullable=False, default=list)
    limits: Mapped[dict[str, Any]] = mapped_column(
        JSONType, nullable=False, default=dict
    )
    config: Mapped[dict[str, Any]] = mapped_column(
        JSONType, nullable=False, default=dict
    )
    rationale: Mapped[str | None] = mapped_column(Text, nullable=True)
    assumptions: Mapped[list[str]] = mapped_column(
        JSONType, nullable=False, default=list
    )
    alternatives: Mapped[list[str]] = mapped_column(
        JSONType, nullable=False, default=list
    )
    position: Mapped[dict[str, float] | None] = mapped_column(
        JSONType, nullable=True
    )
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    design: Mapped[Design] = relationship(back_populates="nodes")


class DesignEdgeRecord(Base):
    """A directed connection between two nodes of a design version."""

    __tablename__ = "design_edges"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    design_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("designs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    source_key: Mapped[str] = mapped_column(String(100), nullable=False)
    target_key: Mapped[str] = mapped_column(String(100), nullable=False)
    protocol: Mapped[str | None] = mapped_column(String(100), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    design: Mapped[Design] = relationship(back_populates="edges")


class NodeEvidence(Base):
    """Evidence cited by a design.

    Rows with ``node_id`` NULL are the design's evidence list; rows with a
    ``node_id`` attribute an evidence item (by ``evidence_key``) to a node.
    """

    __tablename__ = "node_evidence"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    design_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("designs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    node_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("design_nodes.id", ondelete="CASCADE"), nullable=True, index=True
    )
    evidence_key: Mapped[str] = mapped_column(String(255), nullable=False)
    source_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    chunk_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    source_title: Mapped[str] = mapped_column(String(512), nullable=False, default="")
    collection: Mapped[str] = mapped_column(String(100), nullable=False, default="")
    section_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    snippet: Mapped[str] = mapped_column(Text, nullable=False, default="")
    relevance_score: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    design: Mapped[Design] = relationship(back_populates="evidence")


class ValidationIssueRecord(Base):
    """A validator finding stored with its design version."""

    __tablename__ = "validation_issues"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    design_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("designs.id", ondelete="CASCADE"), nullable=False, index=True
    )
    rule_id: Mapped[str] = mapped_column(String(100), nullable=False)
    severity: Mapped[str] = mapped_column(String(16), nullable=False)
    node_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    node_ids: Mapped[list[str]] = mapped_column(JSONType, nullable=False, default=list)
    edge_ids: Mapped[list[str]] = mapped_column(JSONType, nullable=False, default=list)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    suggested_fix: Mapped[str | None] = mapped_column(Text, nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    design: Mapped[Design] = relationship(back_populates="issues")
