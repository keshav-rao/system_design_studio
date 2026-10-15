import uuid
from typing import Any

from sqlalchemy import delete, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.catalog_seed import SEED_COMPATIBILITIES, SEED_COMPONENTS
from app.models.catalog import Component, ComponentCompatibility
from app.schemas.catalog import (
    CompatibilityCheckResponse,
    CompatibilityEdgeCreate,
    ComponentCreate,
    ComponentUpdate,
)


class CatalogService:
    """Service handling component catalog queries, mutations, seed ingestion,

    and architectural compatibility analysis.
    """

    async def get_components(
        self,
        db: AsyncSession,
        category: str | None = None,
        layer: str | None = None,
        search: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> tuple[list[Component], int]:
        stmt = select(Component).where(Component.is_active.is_(True))

        if category:
            stmt = stmt.where(Component.category == category.lower().strip())
        if layer:
            stmt = stmt.where(Component.layer == layer.lower().strip())
        if search:
            search_term = f"%{search.strip().lower()}%"
            stmt = stmt.where(
                or_(
                    func.lower(Component.name).like(search_term),
                    func.lower(Component.slug).like(search_term),
                    func.lower(Component.description).like(search_term),
                )
            )

        # Count total
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_result = await db.execute(count_stmt)
        total = total_result.scalar_one_or_none() or 0

        # Paginated items ordered by category and name
        stmt = (
            stmt.order_by(Component.category, Component.name)
            .limit(limit)
            .offset(offset)
        )
        result = await db.execute(stmt)
        items = list(result.scalars().all())

        return items, total

    async def get_component_by_slug_or_id(
        self, db: AsyncSession, identifier: str
    ) -> Component | None:
        identifier = identifier.strip()
        # Check if UUID
        try:
            val_uuid = uuid.UUID(identifier)
            stmt = select(Component).where(Component.id == val_uuid)
            res = await db.execute(stmt)
            comp = res.scalar_one_or_none()
            if comp:
                return comp
        except ValueError:
            pass

        # Check by slug
        stmt = select(Component).where(func.lower(Component.slug) == identifier.lower())
        res = await db.execute(stmt)
        return res.scalar_one_or_none()

    async def create_component(
        self, db: AsyncSession, comp_in: ComponentCreate
    ) -> Component:
        comp = Component(
            slug=comp_in.slug.strip().lower(),
            name=comp_in.name.strip(),
            category=comp_in.category.strip().lower(),
            layer=comp_in.layer.strip().lower(),
            description=comp_in.description.strip(),
            protocols=comp_in.protocols,
            limits=comp_in.limits,
            failure_modes=comp_in.failure_modes,
            cost_units=comp_in.cost_units,
            alternatives=comp_in.alternatives,
            is_active=comp_in.is_active,
        )
        db.add(comp)
        await db.commit()
        await db.refresh(comp)
        return comp

    async def update_component(
        self, db: AsyncSession, comp_id: uuid.UUID, comp_in: ComponentUpdate
    ) -> Component | None:
        stmt = select(Component).where(Component.id == comp_id)
        res = await db.execute(stmt)
        comp = res.scalar_one_or_none()
        if not comp:
            return None

        update_data = comp_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            if value is not None:
                setattr(comp, field, value)

        await db.commit()
        await db.refresh(comp)
        return comp

    async def delete_component(self, db: AsyncSession, comp_id: uuid.UUID) -> bool:
        stmt = select(Component).where(Component.id == comp_id)
        res = await db.execute(stmt)
        comp = res.scalar_one_or_none()
        if not comp:
            return False

        await db.delete(comp)
        await db.commit()
        return True

    async def add_compatibility_edge(
        self, db: AsyncSession, edge_in: CompatibilityEdgeCreate
    ) -> ComponentCompatibility:
        # Check existing edge
        stmt = select(ComponentCompatibility).where(
            func.lower(ComponentCompatibility.source_slug)
            == edge_in.source_slug.strip().lower(),
            func.lower(ComponentCompatibility.target_slug)
            == edge_in.target_slug.strip().lower(),
        )
        res = await db.execute(stmt)
        existing = res.scalar_one_or_none()

        if existing:
            existing.is_compatible = edge_in.is_compatible
            existing.protocol = edge_in.protocol
            existing.recommended_pattern = edge_in.recommended_pattern
            existing.constraints = edge_in.constraints
            existing.reason = edge_in.reason
            await db.commit()
            await db.refresh(existing)
            return existing

        edge = ComponentCompatibility(
            source_slug=edge_in.source_slug.strip().lower(),
            target_slug=edge_in.target_slug.strip().lower(),
            is_compatible=edge_in.is_compatible,
            protocol=edge_in.protocol,
            recommended_pattern=edge_in.recommended_pattern,
            constraints=edge_in.constraints,
            reason=edge_in.reason,
        )
        db.add(edge)
        await db.commit()
        await db.refresh(edge)
        return edge

    async def check_compatibility(
        self, db: AsyncSession, source_slug: str, target_slug: str
    ) -> CompatibilityCheckResponse:
        src_slug = source_slug.strip().lower()
        tgt_slug = target_slug.strip().lower()

        # Fetch source and target components
        src_comp = await self.get_component_by_slug_or_id(db, src_slug)
        tgt_comp = await self.get_component_by_slug_or_id(db, tgt_slug)

        warnings: list[str] = []
        limits_summary: dict[str, Any] = {}

        if not src_comp:
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=False,
                reason=f"Source component '{source_slug}' was not found in catalog.",
                warnings=["Source component missing."],
            )

        if not tgt_comp:
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=False,
                reason=f"Target component '{target_slug}' was not found in catalog.",
                warnings=["Target component missing."],
            )

        # Assemble combined limits
        src_limits = src_comp.limits or {}
        tgt_limits = tgt_comp.limits or {}

        src_qps = src_limits.get("max_throughput_qps")
        tgt_qps = tgt_limits.get("max_throughput_qps")
        effective_qps = None
        if src_qps is not None and tgt_qps is not None:
            effective_qps = min(int(src_qps), int(tgt_qps))
            if int(tgt_qps) < int(src_qps) * 0.5:
                warnings.append(
                    f"Throughput bottleneck: Target '{tgt_comp.name}' throughput "
                    f"({tgt_qps:,} QPS) is significantly lower than source "
                    f"'{src_comp.name}' ({src_qps:,} QPS). "
                    "Horizontal scaling or connection pooling is required."
                )
        elif tgt_qps is not None:
            effective_qps = int(tgt_qps)
        elif src_qps is not None:
            effective_qps = int(src_qps)

        limits_summary["effective_throughput_qps"] = effective_qps
        limits_summary["source_limits"] = src_limits
        limits_summary["target_limits"] = tgt_limits

        # Query explicit compatibility edge in DB
        stmt = select(ComponentCompatibility).where(
            func.lower(ComponentCompatibility.source_slug) == src_slug,
            func.lower(ComponentCompatibility.target_slug) == tgt_slug,
        )
        edge_res = await db.execute(stmt)
        edge = edge_res.scalar_one_or_none()

        if edge:
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=edge.is_compatible,
                protocol=edge.protocol,
                recommended_pattern=edge.recommended_pattern,
                limits=limits_summary,
                reason=edge.reason or "Explicit architectural rule defined in catalog.",
                warnings=warnings,
            )

        # Fallback category-level compatibility evaluation
        src_cat = src_comp.category
        tgt_cat = tgt_comp.category
        src_layer = src_comp.layer
        tgt_layer = tgt_comp.layer

        # Antipattern rules
        if src_layer == "edge" and tgt_layer == "data":
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=False,
                reason=(
                    f"CRITICAL ANTIPATTERN: Edge components ({src_comp.name}) must "
                    f"never connect directly to data stores ({tgt_comp.name}). "
                    "Requests must pass through an authenticated API Gateway and "
                    "Application layer."
                ),
                limits=limits_summary,
                warnings=warnings
                + ["Exposes internal data layer to public perimeter."],
            )

        if src_cat == "database" and tgt_cat in ("queue", "streaming"):
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=False,
                reason=(
                    f"ANTIPATTERN: Databases ({src_comp.name}) cannot push directly "
                    f"to message queues or event streams ({tgt_comp.name}) without a "
                    "Change Data Capture (CDC) agent (like Debezium) or an "
                    "application-level Transactional Outbox worker."
                ),
                limits=limits_summary,
                warnings=warnings
                + ["Dual write hazards without transactional outbox pattern."],
            )

        if src_cat in ("database", "storage") and tgt_cat == "database":
            # Direct DB to DB unless identical or replica
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=False,
                reason=(
                    f"Direct database-to-database coupling ({src_comp.name} -> "
                    f"{tgt_comp.name}) violates service isolation boundaries. "
                    "Sync via application event streams or batch ETL."
                ),
                limits=limits_summary,
                warnings=warnings + ["Cross-database coupling."],
            )

        if src_cat == "gateway" and tgt_cat == "database":
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=False,
                reason=(
                    f"ANTIPATTERN: API Gateway ({src_comp.name}) must not connect "
                    f"directly to Database ({tgt_comp.name}). Business logic and ORM "
                    "transactions must reside in the compute/application layer."
                ),
                limits=limits_summary,
                warnings=warnings + ["Missing application service tier."],
            )

        # Common valid category patterns
        if src_cat in ("gateway", "cdn") and tgt_layer in ("application", "gateway"):
            common_proto = (
                "HTTPS"
                if "HTTPS" in src_comp.protocols and "HTTPS" in tgt_comp.protocols
                else "HTTP"
            )
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=True,
                protocol=common_proto,
                recommended_pattern="Reverse Proxy / API Gateway Routing",
                limits=limits_summary,
                reason=(
                    f"Standard routing from {src_comp.name} to downstream "
                    f"application service {tgt_comp.name}."
                ),
                warnings=warnings,
            )

        if src_layer == "application" and tgt_layer == "data":
            proto = (
                "TCP/SQL"
                if tgt_cat == "database"
                else "RESP"
                if tgt_cat == "cache"
                else "HTTPS"
            )
            pattern = (
                "Connection Pooling (PgBouncer/HikariCP)"
                if tgt_cat == "database"
                else "Cache-Aside / Read-Through"
                if tgt_cat == "cache"
                else "REST / Storage SDK Client"
            )
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=True,
                protocol=proto,
                recommended_pattern=pattern,
                limits=limits_summary,
                reason=(
                    f"Application services ({src_comp.name}) safely query "
                    f"{tgt_comp.name} using driver protocols."
                ),
                warnings=warnings,
            )

        if src_layer == "application" and tgt_layer == "async":
            proto = (
                "AMQP"
                if tgt_cat == "queue"
                else "Kafka Protocol"
                if tgt_cat == "streaming"
                else "HTTPS"
            )
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=True,
                protocol=proto,
                recommended_pattern="Asynchronous Task Dispatch / Event Publication",
                limits=limits_summary,
                reason=(
                    f"Application services ({src_comp.name}) dispatch background "
                    f"work or publish events to {tgt_comp.name}."
                ),
                warnings=warnings,
            )

        # Default compatibility check based on shared protocols
        shared_protocols = [p for p in src_comp.protocols if p in tgt_comp.protocols]
        if shared_protocols:
            return CompatibilityCheckResponse(
                source_slug=src_slug,
                target_slug=tgt_slug,
                compatible=True,
                protocol=shared_protocols[0],
                recommended_pattern="Direct Network Integration",
                limits=limits_summary,
                reason=(
                    f"Both components share compatible protocols "
                    f"({', '.join(shared_protocols)})."
                ),
                warnings=warnings,
            )

        return CompatibilityCheckResponse(
            source_slug=src_slug,
            target_slug=tgt_slug,
            compatible=False,
            reason=(
                f"No compatible network protocols or documented connection pattern "
                f"found between {src_comp.name} (protocols: {src_comp.protocols}) "
                f"and {tgt_comp.name} (protocols: {tgt_comp.protocols})."
            ),
            limits=limits_summary,
            warnings=warnings + ["Protocol mismatch."],
        )

    async def seed_catalog(
        self, db: AsyncSession, force: bool = False
    ) -> dict[str, int]:
        """Seeds the standard 38+ components and compatibility matrix idempotently."""
        if force:
            await db.execute(delete(ComponentCompatibility))
            await db.execute(delete(Component))
            await db.commit()

        components_seeded = 0
        for comp_data in SEED_COMPONENTS:
            slug = comp_data["slug"].strip().lower()
            stmt = select(Component).where(func.lower(Component.slug) == slug)
            res = await db.execute(stmt)
            existing = res.scalar_one_or_none()

            if existing:
                existing.name = comp_data["name"]
                existing.category = comp_data["category"]
                existing.layer = comp_data["layer"]
                existing.description = comp_data["description"]
                existing.protocols = comp_data["protocols"]
                existing.limits = comp_data["limits"]
                existing.failure_modes = comp_data["failure_modes"]
                existing.cost_units = comp_data["cost_units"]
                existing.alternatives = comp_data["alternatives"]
            else:
                comp = Component(
                    slug=slug,
                    name=comp_data["name"],
                    category=comp_data["category"],
                    layer=comp_data["layer"],
                    description=comp_data["description"],
                    protocols=comp_data["protocols"],
                    limits=comp_data["limits"],
                    failure_modes=comp_data["failure_modes"],
                    cost_units=comp_data["cost_units"],
                    alternatives=comp_data["alternatives"],
                    is_active=True,
                )
                db.add(comp)
                components_seeded += 1

        await db.commit()

        # Seed compatibility edges
        edges_seeded = 0
        for edge_data in SEED_COMPATIBILITIES:
            src = edge_data["source_slug"].strip().lower()
            tgt = edge_data["target_slug"].strip().lower()

            edge_stmt = select(ComponentCompatibility).where(
                func.lower(ComponentCompatibility.source_slug) == src,
                func.lower(ComponentCompatibility.target_slug) == tgt,
            )
            edge_res = await db.execute(edge_stmt)
            existing_edge = edge_res.scalar_one_or_none()

            if existing_edge:
                existing_edge.is_compatible = edge_data["is_compatible"]
                existing_edge.protocol = edge_data.get("protocol")
                existing_edge.recommended_pattern = edge_data.get("recommended_pattern")
                existing_edge.constraints = edge_data.get("constraints", {})
                existing_edge.reason = edge_data.get("reason")
            else:
                new_edge = ComponentCompatibility(
                    source_slug=src,
                    target_slug=tgt,
                    is_compatible=edge_data["is_compatible"],
                    protocol=edge_data.get("protocol"),
                    recommended_pattern=edge_data.get("recommended_pattern"),
                    constraints=edge_data.get("constraints", {}) or {},
                    reason=edge_data.get("reason"),
                )
                db.add(new_edge)
                edges_seeded += 1

        await db.commit()

        return {
            "components_total": len(SEED_COMPONENTS),
            "components_inserted": components_seeded,
            "edges_total": len(SEED_COMPATIBILITIES),
            "edges_inserted": edges_seeded,
        }


catalog_service = CatalogService()
