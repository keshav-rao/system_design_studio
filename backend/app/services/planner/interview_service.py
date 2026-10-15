"""Requirements interview service: fixed sizing questions + adaptive domain follow-ups."""

from typing import Any

from app.schemas.planner import (
    InterviewQuestion,
    InterviewRequest,
    InterviewResponse,
)
from app.schemas.validator import DesignRequirements


class InterviewService:
    """Manages conversational requirements capture before architecture generation."""

    FIXED_QUESTIONS: list[InterviewQuestion] = [
        InterviewQuestion(
            id="expected_users",
            question="What is the expected concurrent or daily active user scale?",
            category="scale",
            options=["1,000", "10,000", "100,000", "1,000,000+"],
            default_value="10,000",
            explanation="Drives compute instance scaling, connection pool sizing, and caching necessity.",
        ),
        InterviewQuestion(
            id="expected_qps",
            question="What is your estimated peak query rate (queries per second)?",
            category="traffic",
            options=["100 QPS", "1,000 QPS", "5,000 QPS", "20,000+ QPS"],
            default_value="1,000 QPS",
            explanation="High QPS (> 1,000) mandates caching tiers and async queuing to avoid database saturation.",
        ),
        InterviewQuestion(
            id="availability_target",
            question="What is your uptime SLA target?",
            category="durability",
            options=[
                "99.0% (3.6 days downtime/year)",
                "99.9% (8.7 hours/year)",
                "99.99% (52 minutes/year)",
            ],
            default_value="99.9%",
            explanation="Higher SLAs require multi-instance replication without single points of failure.",
        ),
        InterviewQuestion(
            id="regions",
            question="How many geographical regions will this service be deployed in?",
            category="regions",
            options=["Single Region", "Multi-Region (2+ regions)"],
            default_value="Single Region",
            explanation="Multi-region deployments require distributed consensus and cross-region replication.",
        ),
        InterviewQuestion(
            id="data_durability_required",
            question="Does this system manage persistent transactional state that must survive restarts?",
            category="durability",
            options=[
                "Yes (Persistent transactional store required)",
                "No (Stateless or ephemeral compute)",
            ],
            default_value="Yes",
            explanation="Requires an ACID relational database, document store, or durable object storage.",
        ),
    ]

    def get_adaptive_questions(self, app_desc: str) -> list[InterviewQuestion]:
        """Generate domain-specific adaptive questions based on user application description."""
        desc_lower = app_desc.lower()
        adaptive = []

        if any(
            w in desc_lower for w in ["dating", "tinder", "swipe", "match", "proximity"]
        ):
            adaptive.append(
                InterviewQuestion(
                    id="geo_and_matching",
                    question="Do you require real-time geospatial proximity queries and sub-10ms mutual swipe matching?",
                    category="domain",
                    options=[
                        "Yes (Requires in-memory geospatial indexes like Redis Geo and Set intersections)",
                        "No (Standard relational queries are sufficient)",
                    ],
                    default_value="Yes",
                    explanation="Fast reciprocal matching requires low-latency in-memory data structures.",
                )
            )

        if any(
            w in desc_lower for w in ["chat", "message", "stream", "live", "websocket"]
        ):
            adaptive.append(
                InterviewQuestion(
                    id="realtime_messaging",
                    question="Do you need persistent bi-directional WebSockets or pub/sub fanout for live messaging?",
                    category="domain",
                    options=[
                        "Yes (WebSocket gateway + message queue)",
                        "No (HTTP polling is acceptable)",
                    ],
                    default_value="Yes",
                    explanation="Full duplex communication requires dedicated connection multiplexers.",
                )
            )

        if any(
            w in desc_lower for w in ["payment", "bank", "crypto", "checkout", "order"]
        ):
            adaptive.append(
                InterviewQuestion(
                    id="strict_acid",
                    question="Are strict ACID financial transactions and idempotency keys required?",
                    category="domain",
                    options=[
                        "Yes (Strong consistency with ACID Postgres/CockroachDB)",
                        "Eventual consistency ok",
                    ],
                    default_value="Yes",
                    explanation="Prevents double-charging and race conditions during concurrent checkouts.",
                )
            )

        return adaptive

    def process_interview(self, req: InterviewRequest) -> InterviewResponse:
        """Evaluate answers, determine if completed, and infer DesignRequirements."""
        answers_map = {a.question_id: a.answer for a in req.answers}

        all_questions = self.FIXED_QUESTIONS + self.get_adaptive_questions(
            req.app_description
        )
        answered_ids = set(answers_map.keys())

        # An interview is complete if all fixed questions have been answered or if user answers >= 3
        # If user supplied answers to fixed questions, we consider it completed
        completed = len(answered_ids) >= len(all_questions) or (
            len(answered_ids) >= len(self.FIXED_QUESTIONS)
        )

        inferred = self._infer_requirements(answers_map, req.app_description)

        remaining_questions = [q for q in all_questions if q.id not in answered_ids]

        return InterviewResponse(
            app_description=req.app_description,
            completed=completed or len(remaining_questions) == 0,
            questions=remaining_questions,
            inferred_requirements=inferred,
        )

    def _infer_requirements(
        self, answers: dict[str, Any], app_desc: str
    ) -> DesignRequirements:
        """Map user answers to structured DesignRequirements."""
        # Defaults
        users = 10000
        qps = 1000
        availability = 99.9
        regions = 1
        durability = True

        # Parse users
        if "expected_users" in answers:
            ans = str(answers["expected_users"]).replace(",", "").replace("+", "")
            for token in ans.split():
                if token.isdigit():
                    users = int(token)
                    break

        # Parse QPS
        if "expected_qps" in answers:
            ans = str(answers["expected_qps"]).replace(",", "").replace("+", "")
            for token in ans.split():
                if token.isdigit():
                    qps = int(token)
                    break

        # Parse availability
        if "availability_target" in answers:
            ans = str(answers["availability_target"])
            if "99.99" in ans:
                availability = 99.99
            elif "99.9" in ans:
                availability = 99.9
            elif "99.0" in ans:
                availability = 99.0

        # Parse regions
        if "regions" in answers:
            ans = str(answers["regions"]).lower()
            if "multi" in ans or "2" in ans:
                regions = 2
            else:
                regions = 1

        # Parse durability
        if "data_durability_required" in answers:
            ans = str(answers["data_durability_required"]).lower()
            durability = "no" not in ans

        return DesignRequirements(
            expected_users=users,
            expected_qps=qps,
            availability_target=availability,
            regions=regions,
            data_durability_required=durability,
        )
