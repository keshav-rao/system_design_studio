"""Data access for normalized, append-only design versions."""

import uuid

from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.catalog import Component
from app.models.project import (
    Design,
    DesignEdgeRecord,
    DesignNodeRecord,
    NodeEvidence,
    ValidationIssueRecord,
)
from app.schemas.planner import (
    AlternativeConsidered,
    DesignSnapshot,
    DesignVersionResponse,
    EvidenceLink,
)
from app.schemas.validator import (
    DesignEdge,
    DesignNode,
    DesignRequirements,
    Severity,
    ValidationIssue,
)

_LOAD_GRAPH = (
    selectinload(Design.nodes),
    selectinload(Design.edges),
    selectinload(Design.evidence),
    selectinload(Design.issues),
)


def validation_status(issues: list[ValidationIssue]) -> str:
    severities = {issue.severity for issue in issues}
    if Severity.ERROR in severities:
        return "errors"
    if Severity.WARNING in severities:
        return "warnings"
    return "valid"


class DesignRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def next_version(self, project_id: uuid.UUID) -> int:
        stmt = select(func.max(Design.version)).where(Design.project_id == project_id)
        return int((await self.db.execute(stmt)).scalar_one_or_none() or 0) + 1

    async def latest(self, project_id: uuid.UUID) -> Design | None:
        stmt = (
            select(Design)
            .options(*_LOAD_GRAPH)
            .where(Design.project_id == project_id)
            .order_by(desc(Design.version))
            .limit(1)
        )
        return (await self.db.execute(stmt)).scalar_one_or_none()

    async def list_for_project(self, project_id: uuid.UUID) -> list[Design]:
        stmt = (
            select(Design)
            .options(*_LOAD_GRAPH)
            .where(Design.project_id == project_id)
            .order_by(desc(Design.version))
        )
        return list((await self.db.execute(stmt)).scalars())

    async def create(
        self,
        project_id: uuid.UUID,
        snapshot: DesignSnapshot,
        *,
        parent_version: int | None,
        creator: str,
    ) -> Design:
        version = await self.next_version(project_id)
        component_ids = await self._component_ids({n.slug for n in snapshot.nodes})
        design = Design(
            id=uuid.uuid4(),
            project_id=project_id,
            version=version,
            parent_version=parent_version,
            title=snapshot.title or f"Design v{version}",
            summary=snapshot.summary,
            requirements=snapshot.requirements.model_dump(),
            assumptions=list(snapshot.assumptions),
            alternatives_considered=[
                a.model_dump() for a in snapshot.alternatives_considered
            ],
            unaddressed_requirements=list(snapshot.unaddressed_requirements),
            open_questions=list(snapshot.open_questions),
            validation_status=validation_status(snapshot.validation_issues),
            creator=creator,
        )
        self.db.add(design)

        links_by_key: dict[str, EvidenceLink] = {}
        for order, link in enumerate(snapshot.evidence_links):
            key = link.id or f"ev{order + 1}"
            links_by_key[key] = link
            design.evidence.append(self._evidence_row(key, link, None, order))

        for order, node in enumerate(snapshot.nodes):
            record = DesignNodeRecord(
                id=uuid.uuid4(),
                node_key=node.id,
                component_id=component_ids.get(node.slug.lower()),
                slug=node.slug,
                label=node.label,
                category=node.category,
                layer=node.layer,
                replicas=node.replicas,
                protocols=list(node.protocols),
                limits=dict(node.limits),
                config=dict(node.config),
                rationale=node.rationale,
                assumptions=list(node.assumptions),
                alternatives=list(node.alternatives),
                position=node.position,
                sort_order=order,
            )
            design.nodes.append(record)
            for ev_order, key in enumerate(dict.fromkeys(node.evidence_ids)):
                link = links_by_key.get(key) or EvidenceLink(
                    id=key, source_title=key, collection="", snippet=""
                )
                design.evidence.append(
                    self._evidence_row(key, link, record.id, ev_order)
                )

        for order, edge in enumerate(snapshot.edges):
            design.edges.append(
                DesignEdgeRecord(
                    id=uuid.uuid4(),
                    source_key=edge.source_id,
                    target_key=edge.target_id,
                    protocol=edge.protocol,
                    notes=edge.label,
                    sort_order=order,
                )
            )

        for order, issue in enumerate(snapshot.validation_issues):
            design.issues.append(
                ValidationIssueRecord(
                    id=uuid.uuid4(),
                    rule_id=issue.rule_id,
                    severity=str(issue.severity),
                    node_id=issue.node_ids[0] if issue.node_ids else None,
                    node_ids=list(issue.node_ids),
                    edge_ids=list(issue.edge_ids),
                    message=issue.message,
                    suggested_fix=issue.suggestion,
                    sort_order=order,
                )
            )

        await self.db.commit()
        loaded = await self._get_loaded(design.id)
        assert loaded is not None
        return loaded

    async def _get_loaded(self, design_id: uuid.UUID) -> Design | None:
        stmt = (
            select(Design)
            .options(*_LOAD_GRAPH)
            .where(Design.id == design_id)
            .execution_options(populate_existing=True)
        )
        return (await self.db.execute(stmt)).scalar_one_or_none()

    async def _component_ids(self, slugs: set[str]) -> dict[str, uuid.UUID]:
        if not slugs:
            return {}
        lowered = {s.lower() for s in slugs}
        stmt = select(Component.slug, Component.id).where(
            func.lower(Component.slug).in_(lowered)
        )
        return {slug.lower(): cid for slug, cid in (await self.db.execute(stmt)).all()}

    @staticmethod
    def _evidence_row(
        key: str, link: EvidenceLink, node_id: uuid.UUID | None, order: int
    ) -> NodeEvidence:
        return NodeEvidence(
            id=uuid.uuid4(),
            node_id=node_id,
            evidence_key=key,
            source_id=link.source_id,
            chunk_id=link.chunk_id,
            source_title=link.source_title,
            collection=link.collection,
            section_path=link.section_path,
            snippet=link.snippet,
            relevance_score=link.relevance_score,
            sort_order=order,
        )

    @staticmethod
    def to_snapshot(design: Design) -> DesignSnapshot:
        evidence_by_node: dict[uuid.UUID, list[str]] = {}
        design_links: list[EvidenceLink] = []
        for row in design.evidence:
            if row.node_id is None:
                design_links.append(
                    EvidenceLink(
                        id=row.evidence_key,
                        chunk_id=row.chunk_id,
                        source_id=row.source_id,
                        source_title=row.source_title,
                        collection=row.collection,
                        section_path=row.section_path,
                        snippet=row.snippet,
                        relevance_score=row.relevance_score,
                    )
                )
            else:
                evidence_by_node.setdefault(row.node_id, []).append(row.evidence_key)

        return DesignSnapshot(
            title=design.title,
            summary=design.summary,
            requirements=DesignRequirements.model_validate(design.requirements or {}),
            nodes=[
                DesignNode(
                    id=n.node_key,
                    slug=n.slug,
                    category=n.category,
                    layer=n.layer,
                    replicas=n.replicas,
                    protocols=list(n.protocols or []),
                    limits=dict(n.limits or {}),
                    config=dict(n.config or {}),
                    label=n.label,
                    rationale=n.rationale,
                    evidence_ids=evidence_by_node.get(n.id, []),
                    assumptions=list(n.assumptions or []),
                    alternatives=list(n.alternatives or []),
                    position=n.position,
                )
                for n in design.nodes
            ],
            edges=[
                DesignEdge(
                    source_id=e.source_key,
                    target_id=e.target_key,
                    protocol=e.protocol,
                    label=e.notes,
                )
                for e in design.edges
            ],
            assumptions=list(design.assumptions or []),
            evidence_links=design_links,
            alternatives_considered=[
                AlternativeConsidered.model_validate(a)
                for a in design.alternatives_considered or []
            ],
            unaddressed_requirements=list(design.unaddressed_requirements or []),
            open_questions=list(design.open_questions or []),
            validation_issues=[
                ValidationIssue(
                    rule_id=i.rule_id,
                    severity=Severity(i.severity),
                    message=i.message,
                    node_ids=list(i.node_ids or []),
                    edge_ids=list(i.edge_ids or []),
                    suggestion=i.suggested_fix,
                )
                for i in design.issues
            ],
        )

    @classmethod
    def to_response(
        cls, design: Design, affected_node_ids: list[str] | None = None
    ) -> DesignVersionResponse:
        snapshot = cls.to_snapshot(design)
        return DesignVersionResponse(
            **snapshot.model_dump(),
            id=design.id,
            project_id=design.project_id,
            version_number=design.version,
            parent_version=design.parent_version,
            creator=design.creator,
            validation_status=design.validation_status,
            is_valid=design.validation_status != "errors",
            created_at=design.created_at,
            affected_node_ids=affected_node_ids or [],
        )
