"""Normalized design storage, requirements, users, and catalog links

Replaces the denormalized ``design_versions`` table with ``designs``,
``design_nodes``, ``design_edges``, ``node_evidence`` and
``validation_issues``. Existing rows are migrated, then ``design_versions``
is dropped. Downgrade rebuilds ``design_versions`` from the new tables.

Revision ID: 004_normalized
Revises: 003_phase4
Create Date: 2026-11-10 20:00:00.000000

"""

import uuid
from collections.abc import Sequence
from typing import Any

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "004_normalized"
down_revision: str | None = "003_phase4"
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None

JSONB = postgresql.JSONB(astext_type=sa.Text())
DEFAULT_USER_EMAIL = "local@system-design-studio"


def _json_col(name: str, default: str = "[]", nullable: bool = False) -> sa.Column:
    return sa.Column(
        name,
        JSONB,
        server_default=None if nullable else default,
        nullable=nullable,
    )


def _created_at() -> sa.Column:
    return sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=sa.text("now()"),
        nullable=False,
    )


def _design_fk() -> sa.Column:
    return sa.Column(
        "design_id",
        sa.UUID(),
        sa.ForeignKey("designs.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )


def _sort_order() -> sa.Column:
    return sa.Column("sort_order", sa.Integer(), server_default="0", nullable=False)


# Lightweight table handles for data migration.
design_versions_t = sa.table(
    "design_versions",
    sa.column("id", sa.UUID()),
    sa.column("project_id", sa.UUID()),
    sa.column("version_number", sa.Integer()),
    sa.column("title", sa.String()),
    sa.column("summary", sa.Text()),
    sa.column("requirements", JSONB),
    sa.column("nodes", JSONB),
    sa.column("edges", JSONB),
    sa.column("assumptions", JSONB),
    sa.column("evidence_links", JSONB),
    sa.column("alternatives_considered", JSONB),
    sa.column("validation_issues", JSONB),
    sa.column("is_valid", sa.Boolean()),
    sa.column("created_at", sa.DateTime(timezone=True)),
)
designs_t = sa.table(
    "designs",
    sa.column("id", sa.UUID()),
    sa.column("project_id", sa.UUID()),
    sa.column("version", sa.Integer()),
    sa.column("parent_version", sa.Integer()),
    sa.column("title", sa.String()),
    sa.column("summary", sa.Text()),
    sa.column("requirements", JSONB),
    sa.column("assumptions", JSONB),
    sa.column("alternatives_considered", JSONB),
    sa.column("validation_status", sa.String()),
    sa.column("creator", sa.String()),
    sa.column("created_at", sa.DateTime(timezone=True)),
)
nodes_t = sa.table(
    "design_nodes",
    sa.column("id", sa.UUID()),
    sa.column("design_id", sa.UUID()),
    sa.column("node_key", sa.String()),
    sa.column("component_id", sa.UUID()),
    sa.column("slug", sa.String()),
    sa.column("category", sa.String()),
    sa.column("layer", sa.String()),
    sa.column("replicas", sa.Integer()),
    sa.column("protocols", JSONB),
    sa.column("limits", JSONB),
    sa.column("config", JSONB),
    sa.column("sort_order", sa.Integer()),
)
edges_t = sa.table(
    "design_edges",
    sa.column("id", sa.UUID()),
    sa.column("design_id", sa.UUID()),
    sa.column("source_key", sa.String()),
    sa.column("target_key", sa.String()),
    sa.column("protocol", sa.String()),
    sa.column("notes", sa.Text()),
    sa.column("sort_order", sa.Integer()),
)
evidence_t = sa.table(
    "node_evidence",
    sa.column("id", sa.UUID()),
    sa.column("design_id", sa.UUID()),
    sa.column("node_id", sa.UUID()),
    sa.column("evidence_key", sa.String()),
    sa.column("source_id", sa.String()),
    sa.column("chunk_id", sa.String()),
    sa.column("source_title", sa.String()),
    sa.column("collection", sa.String()),
    sa.column("section_path", sa.Text()),
    sa.column("snippet", sa.Text()),
    sa.column("relevance_score", sa.Float()),
    sa.column("sort_order", sa.Integer()),
)
issues_t = sa.table(
    "validation_issues",
    sa.column("id", sa.UUID()),
    sa.column("design_id", sa.UUID()),
    sa.column("rule_id", sa.String()),
    sa.column("severity", sa.String()),
    sa.column("node_id", sa.String()),
    sa.column("node_ids", JSONB),
    sa.column("edge_ids", JSONB),
    sa.column("message", sa.Text()),
    sa.column("suggested_fix", sa.Text()),
    sa.column("sort_order", sa.Integer()),
)


def _status_from_issues(issues: list[dict[str, Any]]) -> str:
    severities = {str(i.get("severity", "")).lower() for i in issues}
    if "error" in severities:
        return "errors"
    if "warning" in severities:
        return "warnings"
    return "valid"


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column("email", sa.String(320), nullable=False, unique=True),
        _created_at(),
    )
    op.add_column(
        "projects",
        sa.Column(
            "user_id",
            sa.UUID(),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )
    op.create_index("ix_projects_user_id", "projects", ["user_id"])
    op.add_column(
        "projects",
        sa.Column(
            "status", sa.String(32), server_default="interviewing", nullable=False
        ),
    )

    op.create_table(
        "requirements",
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column(
            "project_id",
            sa.UUID(),
            sa.ForeignKey("projects.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("key", sa.String(100), nullable=False),
        _json_col("value", nullable=True),
        sa.Column("is_assumed", sa.Boolean(), server_default="false", nullable=False),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.UniqueConstraint("project_id", "key"),
    )

    op.create_table(
        "designs",
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column(
            "project_id",
            sa.UUID(),
            sa.ForeignKey("projects.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("parent_version", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("summary", sa.Text(), server_default="", nullable=False),
        _json_col("requirements", "{}"),
        _json_col("assumptions"),
        _json_col("alternatives_considered"),
        _json_col("unaddressed_requirements"),
        _json_col("open_questions"),
        sa.Column(
            "validation_status", sa.String(16), server_default="valid", nullable=False
        ),
        sa.Column("creator", sa.String(16), server_default="planner", nullable=False),
        _created_at(),
        sa.UniqueConstraint("project_id", "version"),
    )

    op.create_table(
        "design_nodes",
        sa.Column("id", sa.UUID(), primary_key=True),
        _design_fk(),
        sa.Column("node_key", sa.String(100), nullable=False),
        sa.Column(
            "component_id",
            sa.UUID(),
            sa.ForeignKey("components.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("slug", sa.String(100), nullable=False),
        sa.Column("label", sa.String(255), nullable=True),
        sa.Column("category", sa.String(50), nullable=False),
        sa.Column("layer", sa.String(50), nullable=False),
        sa.Column("replicas", sa.Integer(), server_default="1", nullable=False),
        _json_col("protocols"),
        _json_col("limits", "{}"),
        _json_col("config", "{}"),
        sa.Column("rationale", sa.Text(), nullable=True),
        _json_col("assumptions"),
        _json_col("alternatives"),
        _json_col("position", nullable=True),
        _sort_order(),
        sa.UniqueConstraint("design_id", "node_key"),
    )

    op.create_table(
        "design_edges",
        sa.Column("id", sa.UUID(), primary_key=True),
        _design_fk(),
        sa.Column("source_key", sa.String(100), nullable=False),
        sa.Column("target_key", sa.String(100), nullable=False),
        sa.Column("protocol", sa.String(100), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        _sort_order(),
    )

    op.create_table(
        "node_evidence",
        sa.Column("id", sa.UUID(), primary_key=True),
        _design_fk(),
        sa.Column(
            "node_id",
            sa.UUID(),
            sa.ForeignKey("design_nodes.id", ondelete="CASCADE"),
            nullable=True,
            index=True,
        ),
        sa.Column("evidence_key", sa.String(255), nullable=False),
        sa.Column("source_id", sa.String(64), nullable=True),
        sa.Column("chunk_id", sa.String(64), nullable=True),
        sa.Column("source_title", sa.String(512), server_default="", nullable=False),
        sa.Column("collection", sa.String(100), server_default="", nullable=False),
        sa.Column("section_path", sa.Text(), nullable=True),
        sa.Column("snippet", sa.Text(), server_default="", nullable=False),
        sa.Column("relevance_score", sa.Float(), server_default="0", nullable=False),
        _sort_order(),
    )

    op.create_table(
        "validation_issues",
        sa.Column("id", sa.UUID(), primary_key=True),
        _design_fk(),
        sa.Column("rule_id", sa.String(100), nullable=False),
        sa.Column("severity", sa.String(16), nullable=False),
        sa.Column("node_id", sa.String(100), nullable=True),
        _json_col("node_ids"),
        _json_col("edge_ids"),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("suggested_fix", sa.Text(), nullable=True),
        _sort_order(),
    )

    op.create_table(
        "component_alternatives",
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column(
            "component_id",
            sa.UUID(),
            sa.ForeignKey("components.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "alternative_id",
            sa.UUID(),
            sa.ForeignKey("components.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("when_to_prefer", sa.Text(), nullable=True),
        sa.UniqueConstraint("component_id", "alternative_id"),
    )

    for side in ("source", "target"):
        op.add_column(
            "component_compatibilities",
            sa.Column(
                f"{side}_component_id",
                sa.UUID(),
                sa.ForeignKey("components.id", ondelete="CASCADE"),
                nullable=True,
            ),
        )
        op.create_index(
            f"ix_component_compatibilities_{side}_component_id",
            "component_compatibilities",
            [f"{side}_component_id"],
        )

    _migrate_data_up()

    op.drop_index("ix_design_versions_project_version", table_name="design_versions")
    op.drop_index("ix_design_versions_project_id", table_name="design_versions")
    op.drop_table("design_versions")


def _migrate_data_up() -> None:
    bind = op.get_bind()

    user_id = uuid.uuid4()
    bind.execute(
        sa.text("INSERT INTO users (id, email) VALUES (:id, :email)"),
        {"id": user_id, "email": DEFAULT_USER_EMAIL},
    )
    bind.execute(sa.text("UPDATE projects SET user_id = :id"), {"id": user_id})
    bind.execute(
        sa.text(
            "UPDATE projects SET status = 'designed' WHERE id IN "
            "(SELECT DISTINCT project_id FROM design_versions)"
        )
    )
    bind.execute(
        sa.text(
            "UPDATE component_compatibilities cc SET "
            "source_component_id = (SELECT id FROM components c "
            "WHERE lower(c.slug) = lower(cc.source_slug)), "
            "target_component_id = (SELECT id FROM components c "
            "WHERE lower(c.slug) = lower(cc.target_slug))"
        )
    )
    component_ids = {
        slug.lower(): cid
        for slug, cid in bind.execute(sa.text("SELECT slug, id FROM components"))
    }

    rows = bind.execute(
        sa.select(design_versions_t).order_by(
            design_versions_t.c.project_id, design_versions_t.c.version_number
        )
    ).mappings()
    last_version: dict[Any, int] = {}
    for row in rows:
        design_id = uuid.uuid4()
        issues = list(row["validation_issues"] or [])
        bind.execute(
            designs_t.insert().values(
                id=design_id,
                project_id=row["project_id"],
                version=row["version_number"],
                parent_version=last_version.get(row["project_id"]),
                title=row["title"],
                summary=row["summary"] or "",
                requirements=row["requirements"] or {},
                assumptions=row["assumptions"] or [],
                alternatives_considered=row["alternatives_considered"] or [],
                validation_status=_status_from_issues(issues),
                creator="planner",
                created_at=row["created_at"],
            )
        )
        last_version[row["project_id"]] = row["version_number"]

        for order, node in enumerate(row["nodes"] or []):
            slug = str(node.get("slug", ""))
            bind.execute(
                nodes_t.insert().values(
                    id=uuid.uuid4(),
                    design_id=design_id,
                    node_key=str(node.get("id")),
                    component_id=component_ids.get(slug.lower()),
                    slug=slug,
                    category=str(node.get("category", "")),
                    layer=str(node.get("layer", "")),
                    replicas=int(node.get("replicas") or 1),
                    protocols=node.get("protocols") or [],
                    limits=node.get("limits") or {},
                    config=node.get("config") or {},
                    sort_order=order,
                )
            )
        for order, edge in enumerate(row["edges"] or []):
            bind.execute(
                edges_t.insert().values(
                    id=uuid.uuid4(),
                    design_id=design_id,
                    source_key=str(edge.get("source_id")),
                    target_key=str(edge.get("target_id")),
                    protocol=edge.get("protocol"),
                    notes=edge.get("label"),
                    sort_order=order,
                )
            )
        for order, link in enumerate(row["evidence_links"] or []):
            bind.execute(
                evidence_t.insert().values(
                    id=uuid.uuid4(),
                    design_id=design_id,
                    node_id=None,
                    evidence_key=f"ev{order + 1}",
                    source_id=link.get("source_id"),
                    chunk_id=None,
                    source_title=str(link.get("source_title", "")),
                    collection=str(link.get("collection", "")),
                    section_path=link.get("section_path"),
                    snippet=str(link.get("snippet", "")),
                    relevance_score=float(link.get("relevance_score") or 0.0),
                    sort_order=order,
                )
            )
        for order, issue in enumerate(issues):
            node_ids = list(issue.get("node_ids") or [])
            bind.execute(
                issues_t.insert().values(
                    id=uuid.uuid4(),
                    design_id=design_id,
                    rule_id=str(issue.get("rule_id", "")),
                    severity=str(issue.get("severity", "info")),
                    node_id=node_ids[0] if node_ids else None,
                    node_ids=node_ids,
                    edge_ids=list(issue.get("edge_ids") or []),
                    message=str(issue.get("message", "")),
                    suggested_fix=issue.get("suggestion"),
                    sort_order=order,
                )
            )


def downgrade() -> None:
    op.create_table(
        "design_versions",
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column(
            "project_id",
            sa.UUID(),
            sa.ForeignKey("projects.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("version_number", sa.Integer(), server_default="1", nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        _json_col("requirements", "{}"),
        _json_col("nodes"),
        _json_col("edges"),
        _json_col("assumptions"),
        _json_col("evidence_links"),
        _json_col("alternatives_considered"),
        _json_col("validation_issues"),
        sa.Column("is_valid", sa.Boolean(), server_default="true", nullable=False),
        _created_at(),
    )
    op.create_index(
        "ix_design_versions_project_id", "design_versions", ["project_id"]
    )
    op.create_index(
        "ix_design_versions_project_version",
        "design_versions",
        ["project_id", "version_number"],
        unique=True,
    )

    bind = op.get_bind()
    for design in bind.execute(sa.select(designs_t)).mappings():
        did = design["id"]
        nodes = [
            {
                "id": n["node_key"],
                "slug": n["slug"],
                "category": n["category"],
                "layer": n["layer"],
                "replicas": n["replicas"],
                "protocols": n["protocols"] or [],
                "limits": n["limits"] or {},
                "config": n["config"] or {},
            }
            for n in bind.execute(
                sa.select(nodes_t)
                .where(nodes_t.c.design_id == did)
                .order_by(nodes_t.c.sort_order)
            ).mappings()
        ]
        edges = [
            {
                "source_id": e["source_key"],
                "target_id": e["target_key"],
                "protocol": e["protocol"],
                "label": e["notes"],
            }
            for e in bind.execute(
                sa.select(edges_t)
                .where(edges_t.c.design_id == did)
                .order_by(edges_t.c.sort_order)
            ).mappings()
        ]
        evidence = [
            {
                "source_id": ev["source_id"],
                "source_title": ev["source_title"],
                "collection": ev["collection"],
                "section_path": ev["section_path"],
                "snippet": ev["snippet"],
                "relevance_score": ev["relevance_score"],
            }
            for ev in bind.execute(
                sa.select(evidence_t)
                .where(evidence_t.c.design_id == did, evidence_t.c.node_id.is_(None))
                .order_by(evidence_t.c.sort_order)
            ).mappings()
        ]
        issues = [
            {
                "rule_id": i["rule_id"],
                "severity": i["severity"],
                "message": i["message"],
                "node_ids": i["node_ids"] or [],
                "edge_ids": i["edge_ids"] or [],
                "suggestion": i["suggested_fix"],
            }
            for i in bind.execute(
                sa.select(issues_t)
                .where(issues_t.c.design_id == did)
                .order_by(issues_t.c.sort_order)
            ).mappings()
        ]
        bind.execute(
            design_versions_t.insert().values(
                id=did,
                project_id=design["project_id"],
                version_number=design["version"],
                title=design["title"],
                summary=design["summary"],
                requirements=design["requirements"] or {},
                nodes=nodes,
                edges=edges,
                assumptions=design["assumptions"] or [],
                evidence_links=evidence,
                alternatives_considered=design["alternatives_considered"] or [],
                validation_issues=issues,
                is_valid=design["validation_status"] != "errors",
                created_at=design["created_at"],
            )
        )

    for side in ("source", "target"):
        op.drop_index(
            f"ix_component_compatibilities_{side}_component_id",
            table_name="component_compatibilities",
        )
        op.drop_column("component_compatibilities", f"{side}_component_id")
    op.drop_table("component_alternatives")
    op.drop_table("validation_issues")
    op.drop_table("node_evidence")
    op.drop_table("design_edges")
    op.drop_table("design_nodes")
    op.drop_table("designs")
    op.drop_table("requirements")
    op.drop_index("ix_projects_user_id", table_name="projects")
    op.drop_column("projects", "status")
    op.drop_column("projects", "user_id")
    op.drop_table("users")
