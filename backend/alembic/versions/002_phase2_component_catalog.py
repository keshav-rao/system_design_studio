"""Phase 2: Component catalog and compatibility matrix

Revision ID: 002_phase2
Revises: 001_phase1
Create Date: 2026-10-13 22:30:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "002_phase2"
down_revision: str | None = "001_phase1"
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    # 1. components table
    op.create_table(
        "components",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("category", sa.String(length=50), nullable=False),
        sa.Column("layer", sa.String(length=50), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column(
            "protocols",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column(
            "limits",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column(
            "failure_modes",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column(
            "cost_units",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column(
            "alternatives",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index(op.f("ix_components_slug"), "components", ["slug"], unique=True)
    op.create_index(
        op.f("ix_components_category"), "components", ["category"], unique=False
    )
    op.create_index(op.f("ix_components_layer"), "components", ["layer"], unique=False)

    # 2. component_compatibilities table
    op.create_table(
        "component_compatibilities",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("source_slug", sa.String(length=100), nullable=False),
        sa.Column("target_slug", sa.String(length=100), nullable=False),
        sa.Column("is_compatible", sa.Boolean(), nullable=False),
        sa.Column("protocol", sa.String(length=100), nullable=True),
        sa.Column("recommended_pattern", sa.String(length=255), nullable=True),
        sa.Column(
            "constraints",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_component_compatibilities_source_slug"),
        "component_compatibilities",
        ["source_slug"],
        unique=False,
    )
    op.create_index(
        op.f("ix_component_compatibilities_target_slug"),
        "component_compatibilities",
        ["target_slug"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_component_compatibilities_target_slug"),
        table_name="component_compatibilities",
    )
    op.drop_index(
        op.f("ix_component_compatibilities_source_slug"),
        table_name="component_compatibilities",
    )
    op.drop_table("component_compatibilities")
    op.drop_index(op.f("ix_components_layer"), table_name="components")
    op.drop_index(op.f("ix_components_category"), table_name="components")
    op.drop_index(op.f("ix_components_slug"), table_name="components")
    op.drop_table("components")
