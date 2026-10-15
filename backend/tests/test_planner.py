"""Tests for Phase 4: Requirements Interview, LangGraph, and Dating App.

Verifies:
1. Requirements interview fixed and adaptive questions.
2. LangGraph retry mechanism when LLM outputs invalid JSON.
3. End-to-end dating-app proposal generation:
   - Schema valid ArchitectureProposal
   - Grounded in catalog facts and knowledge base evidence
   - Passes deterministic validation
   - Persisted as an immutable DesignVersion in PostgreSQL / SQLite
4. REST API integration for /projects, /interview, and /plan.
"""


import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.planner import (
    ArchitectureProposal,
    InterviewAnswer,
    InterviewRequest,
    PlanRequest,
    ProjectCreate,
)
from app.schemas.validator import DesignRequirements
from app.services.planner.graph import ArchitecturePlannerGraph
from app.services.planner.interview_service import InterviewService
from app.services.planner.planner_service import PlannerService
from app.services.planner.providers.mock_adapter import MockLLMAdapter


class TestInterviewService:
    """Tests for the interactive requirements capture."""

    def test_fixed_questions_presence(self) -> None:
        service = InterviewService()
        req = InterviewRequest(app_description="Simple web application")
        res = service.process_interview(req)
        assert len(res.questions) >= 5
        q_ids = [q.id for q in res.questions]
        assert "expected_users" in q_ids
        assert "expected_qps" in q_ids
        assert "availability_target" in q_ids
        assert "regions" in q_ids
        assert "data_durability_required" in q_ids
        assert res.completed is False

    def test_adaptive_dating_app_questions(self) -> None:
        service = InterviewService()
        req = InterviewRequest(
            app_description="Tinder-like dating app with instant swipe matching"
        )
        res = service.process_interview(req)
        q_ids = [q.id for q in res.questions]
        assert "geo_and_matching" in q_ids

    def test_infer_requirements_from_answers(self) -> None:
        service = InterviewService()
        req = InterviewRequest(
            app_description="High-scale dating app",
            answers=[
                InterviewAnswer(question_id="expected_users", answer="100,000"),
                InterviewAnswer(question_id="expected_qps", answer="5,000 QPS"),
                InterviewAnswer(question_id="availability_target", answer="99.99%"),
                InterviewAnswer(question_id="regions", answer="Multi-Region"),
                InterviewAnswer(question_id="data_durability_required", answer="Yes"),
            ],
        )
        res = service.process_interview(req)
        assert res.completed is True
        nfr = res.inferred_requirements
        assert nfr.expected_users == 100000
        assert nfr.expected_qps == 5000
        assert nfr.availability_target == 99.99
        assert nfr.regions == 2
        assert nfr.data_durability_required is True


class TestLangGraphPlanner:
    """Tests for the LangGraph-orchestrated architecture planning workflow."""

    @pytest.mark.asyncio
    async def test_dating_app_proposal_generation(self) -> None:
        """Verify the dating-app golden proposal generation."""
        adapter = MockLLMAdapter()
        graph = ArchitecturePlannerGraph(llm_adapter=adapter)

        reqs = DesignRequirements(
            expected_users=100000,
            expected_qps=5000,
            availability_target=99.95,
            data_durability_required=True,
            regions=1,
        )

        state = await graph.plan(
            app_description=(
                "Build a high-concurrency Tinder-scale dating app with real-time"
                " swipe matching"
            ),
            requirements=reqs,
        )

        assert state.get("proposal") is not None
        prop_data = state["proposal"]
        proposal = ArchitectureProposal.model_validate(prop_data)

        # 1. Proposal schema validity
        assert "Tinder" in proposal.title or "Geospatial" in proposal.title
        assert len(proposal.nodes) >= 4
        assert len(proposal.edges) >= 3

        # 2. Grounding in catalog components
        node_slugs = [n.slug for n in proposal.nodes]
        assert "redis-cache" in node_slugs
        assert "postgresql" in node_slugs
        assert "fastapi" in node_slugs
        assert "kong-gateway" in node_slugs

        # 3. Grounding in evidence
        assert len(proposal.evidence_links) >= 1
        assert any(
            "Redis" in ev.snippet or "Caching" in ev.snippet
            for ev in proposal.evidence_links
        )

        # 4. Alternatives considered
        assert len(proposal.alternatives_considered) >= 1

        # 5. Deterministic validation outcome
        assert state["is_valid"] is True
        error_issues = [
            i for i in state["validation_issues"] if i.get("severity") == "error"
        ]
        assert len(error_issues) == 0

    @pytest.mark.asyncio
    async def test_langgraph_retry_recovers_from_invalid_json(self) -> None:
        """Verify that LangGraph retries and recovers from broken LLM output."""

        # Fail once, then return valid JSON on retry
        adapter = MockLLMAdapter(fail_first_n_times=1)
        graph = ArchitecturePlannerGraph(llm_adapter=adapter)

        state = await graph.plan(
            app_description="Dating app",
            max_retries=2,
        )

        # Must have retried and recovered
        assert state.get("retry_count") == 1
        assert state.get("proposal") is not None
        assert state.get("is_valid") is True

    @pytest.mark.asyncio
    async def test_langgraph_exhausts_retries_on_permanent_failure(self) -> None:
        """Verify that LangGraph terminates cleanly if retries are exceeded."""
        adapter = MockLLMAdapter(fail_first_n_times=10)
        graph = ArchitecturePlannerGraph(llm_adapter=adapter)

        state = await graph.plan(
            app_description="Dating app",
            max_retries=2,
        )

        assert state.get("proposal") is None
        assert state.get("is_valid") is False
        assert state.get("error_message") is not None


class TestPlannerServiceAndPersistence:
    """Tests for PlannerService database persistence and versioning."""

    @pytest.mark.asyncio
    async def test_create_project_and_generate_version(
        self, test_db: AsyncSession
    ) -> None:
        adapter = MockLLMAdapter()
        service = PlannerService(llm_adapter=adapter)

        # 1. Create project
        proj = await service.create_project(
            ProjectCreate(
                name="Dating App Architecture", description="Tinder clone project"
            ),
            db=test_db,
        )
        assert proj.id is not None
        assert proj.name == "Dating App Architecture"

        # 2. Generate Plan version 1
        plan_req = PlanRequest(
            app_description="Tinder dating application with real-time swipe matching",
            interview_answers=[
                InterviewAnswer(question_id="expected_users", answer="100,000"),
                InterviewAnswer(question_id="expected_qps", answer="5,000 QPS"),
                InterviewAnswer(question_id="availability_target", answer="99.95%"),
            ],
        )

        v1 = await service.generate_plan(proj.id, plan_req, db=test_db)
        assert v1.version_number == 1
        assert v1.project_id == proj.id
        assert len(v1.nodes) >= 4
        assert v1.is_valid is True

        # 3. Retrieve versions
        versions = await service.list_design_versions(proj.id, db=test_db)
        assert len(versions) == 1

        latest = await service.get_latest_design_version(proj.id, db=test_db)
        assert latest is not None
        assert latest.id == v1.id

        # 4. Generate version 2
        v2 = await service.generate_plan(proj.id, plan_req, db=test_db)
        assert v2.version_number == 2

        versions_after = await service.list_design_versions(proj.id, db=test_db)
        assert len(versions_after) == 2
        assert versions_after[0].version_number == 2


# =========================================================================
# API Integration Tests
# =========================================================================


@pytest.mark.asyncio
async def test_project_and_planner_api(async_client: AsyncClient) -> None:
    # 1. Interview endpoint
    resp = await async_client.post(
        "/api/v1/projects/interview",
        json={"app_description": "Tinder-like dating app with location matching"},
    )
    assert resp.status_code == 200
    interview_data = resp.json()
    assert "questions" in interview_data
    assert any(q["id"] == "geo_and_matching" for q in interview_data["questions"])

    # 2. Create project
    create_resp = await async_client.post(
        "/api/v1/projects",
        json={"name": "Dating App Project", "description": "Tinder system design"},
    )
    assert create_resp.status_code == 201
    project_data = create_resp.json()
    project_id = project_data["id"]

    # 3. List projects
    list_resp = await async_client.get("/api/v1/projects")
    assert list_resp.status_code == 200
    assert len(list_resp.json()) >= 1

    # 4. Plan generation endpoint
    plan_resp = await async_client.post(
        f"/api/v1/projects/{project_id}/plan",
        json={
            "app_description": "Tinder dating app with real-time swipe matching",
            "requirements": {
                "expected_users": 100000,
                "expected_qps": 5000,
                "availability_target": 99.95,
                "data_durability_required": True,
                "regions": 1,
            },
        },
    )
    assert plan_resp.status_code == 201
    version_data = plan_resp.json()
    assert version_data["version_number"] == 1
    assert version_data["is_valid"] is True
    assert len(version_data["nodes"]) >= 4

    # 5. Get designs list & latest
    designs_resp = await async_client.get(f"/api/v1/projects/{project_id}/designs")
    assert designs_resp.status_code == 200
    assert len(designs_resp.json()) == 1

    latest_resp = await async_client.get(
        f"/api/v1/projects/{project_id}/designs/latest"
    )
    assert latest_resp.status_code == 200
    assert latest_resp.json()["id"] == version_data["id"]
