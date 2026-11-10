"""Tests for normalized design storage and per-node evidence attribution."""

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import ComponentAlternative, ComponentCompatibility
from app.models.project import NodeEvidence, Requirement, User
from app.repositories import DesignRepository, ProjectRepository
from app.schemas.planner import (
    DesignSnapshot,
    EvidenceLink,
    InterviewAnswer,
    PlanRequest,
    ProjectCreate,
)
from app.schemas.validator import (
    DesignEdge,
    DesignNode,
    DesignRequirements,
    Severity,
    ValidationIssue,
)
from app.services.catalog.catalog_service import catalog_service
from app.services.planner.planner_service import PlannerService
from app.services.planner.providers.mock_adapter import MockLLMAdapter


def _snapshot() -> DesignSnapshot:
    return DesignSnapshot(
        title="Chat",
        summary="Realtime chat",
        requirements=DesignRequirements(expected_users=1000, regions=2),
        nodes=[
            DesignNode(
                id="api",
                slug="fastapi",
                category="compute",
                layer="application",
                rationale="Async Python API",
                evidence_ids=["ev1"],
                assumptions=["Stateless"],
                alternatives=["express"],
                position={"x": 10.0, "y": 20.0},
            ),
            DesignNode(
                id="db",
                slug="postgresql",
                category="database",
                layer="data",
                replicas=2,
            ),
        ],
        edges=[DesignEdge(source_id="api", target_id="db", protocol="SQL")],
        evidence_links=[
            EvidenceLink(
                id="ev1",
                chunk_id="c1",
                source_title="FastAPI guide",
                collection="03_component_decision_guides",
                snippet="FastAPI handles async I/O",
                relevance_score=0.9,
            )
        ],
        validation_issues=[
            ValidationIssue(
                rule_id="no-spof",
                severity=Severity.WARNING,
                message="Single API instance",
                node_ids=["api"],
                suggestion="Add replicas",
            )
        ],
    )


@pytest.mark.asyncio
async def test_round_trip_preserves_graph_and_node_evidence(
    test_db: AsyncSession,
) -> None:
    project = await ProjectRepository(test_db).create("Chat", None)
    repo = DesignRepository(test_db)

    design = await repo.create(
        project.id, _snapshot(), parent_version=None, creator="user"
    )
    response = DesignRepository.to_response(design)

    assert response.version_number == 1
    assert response.creator == "user"
    assert response.validation_status == "warnings"
    assert response.is_valid is True
    api = next(n for n in response.nodes if n.id == "api")
    assert api.evidence_ids == ["ev1"]
    assert api.assumptions == ["Stateless"]
    assert api.alternatives == ["express"]
    assert api.position == {"x": 10.0, "y": 20.0}
    assert [e.id for e in response.evidence_links] == ["ev1"]
    assert response.edges[0].protocol == "SQL"
    assert response.validation_issues[0].suggestion == "Add replicas"

    second = await repo.create(
        project.id, _snapshot(), parent_version=1, creator="planner"
    )
    assert second.version == 2
    assert second.parent_version == 1
    assert [d.version for d in await repo.list_for_project(project.id)] == [2, 1]

    rows = (await test_db.execute(select(NodeEvidence))).scalars().all()
    assert sum(1 for r in rows if r.node_id is not None) == 2


@pytest.mark.asyncio
async def test_projects_get_default_user_and_status(test_db: AsyncSession) -> None:
    repo = ProjectRepository(test_db)
    first = await repo.create("A", None)
    second = await repo.create("B", None)

    users = (await test_db.execute(select(User))).scalars().all()
    assert len(users) == 1
    assert first.user_id == second.user_id == users[0].id
    assert first.status == "interviewing"


@pytest.mark.asyncio
async def test_generate_plan_persists_requirements_and_status(
    test_db: AsyncSession,
) -> None:
    service = PlannerService(llm_adapter=MockLLMAdapter())
    project = await service.create_project(ProjectCreate(name="Dating"), test_db)

    version = await service.generate_plan(
        project.id,
        PlanRequest(
            app_description="Tinder dating app with swipe matching",
            interview_answers=[
                InterviewAnswer(question_id="expected_users", answer="100,000")
            ],
        ),
        test_db,
    )

    assert version.parent_version is None
    refreshed = await service.get_project(project.id, test_db)
    assert refreshed is not None and refreshed.status == "designed"
    reqs = {
        r.key: r
        for r in (await test_db.execute(select(Requirement))).scalars().all()
    }
    assert reqs["expected_users"].is_assumed is False
    assert reqs["regions"].is_assumed is True


def test_link_node_evidence_matches_slug_terms() -> None:
    snapshot = DesignSnapshot(
        title="t",
        nodes=[
            DesignNode(id="c", slug="redis-cache", category="cache", layer="data"),
            DesignNode(id="q", slug="rabbitmq", category="queue", layer="async"),
        ],
        evidence_links=[
            EvidenceLink(
                source_title="Redis cluster topologies",
                collection="cloud_docs",
                snippet="Redis replicas",
            )
        ],
    )

    PlannerService._link_node_evidence(snapshot)

    assert snapshot.evidence_links[0].id == "ev1"
    assert snapshot.nodes[0].evidence_ids == ["ev1"]
    assert snapshot.nodes[1].evidence_ids == []


@pytest.mark.asyncio
async def test_catalog_seed_links_alternatives_and_compatibility_ids(
    test_db: AsyncSession,
) -> None:
    await catalog_service.seed_catalog(test_db)

    alternatives = (await test_db.execute(select(ComponentAlternative))).scalars()
    assert len(list(alternatives)) > 0
    edges = (await test_db.execute(select(ComponentCompatibility))).scalars().all()
    assert all(
        e.source_component_id is not None and e.target_component_id is not None
        for e in edges
    )
