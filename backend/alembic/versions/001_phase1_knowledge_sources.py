"""Phase 1: Knowledge sources, eval questions, and eval runs

Revision ID: 001_phase1
Revises:
Create Date: 2026-10-13 19:50:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "001_phase1"
down_revision: str | None = None
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    # 1. sources table
    op.create_table(
        "sources",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("collection", sa.String(length=50), nullable=False),
        sa.Column("origin_url", sa.String(length=1024), nullable=True),
        sa.Column("licence", sa.String(length=100), nullable=False),
        sa.Column("permission_notes", sa.Text(), nullable=True),
        sa.Column("publication_date", sa.String(length=50), nullable=True),
        sa.Column("ingested_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            "version", sa.String(length=50), server_default="1.0", nullable=False
        ),
        sa.Column("refresh_date", sa.String(length=50), nullable=True),
        sa.Column("chunk_count", sa.Integer(), server_default="0", nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_sources_collection"), "sources", ["collection"], unique=False
    )

    # 2. eval_questions table
    op.create_table(
        "eval_questions",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column(
            "gold_source_ids",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column(
            "gold_design",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=True,
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    # 3. eval_runs table
    op.create_table(
        "eval_runs",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "config",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column(
            "metrics",
            postgresql.JSONB(astext_type=sa.Text()).with_variant(sa.JSON(), "sqlite"),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("eval_runs")
    op.drop_table("eval_questions")
    op.drop_index(op.f("ix_sources_collection"), table_name="sources")
    op.drop_table("sources")
