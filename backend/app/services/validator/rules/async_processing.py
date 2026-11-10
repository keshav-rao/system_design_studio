"""Rule: async-processing-for-heavy-writes

Designs with high write throughput (>= 5 000 QPS) should include an async
processing component (queue or streaming platform) to decouple write
acceptance from write processing, preventing upstream back-pressure and
improving fault tolerance.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "async-for-heavy-writes"

_WRITE_QPS_THRESHOLD = 5_000
_ASYNC_CATEGORIES = frozenset({"queue", "streaming"})


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag high-write designs missing asynchronous processing."""
    issues: list[ValidationIssue] = []

    reqs = design.requirements
    if reqs.expected_qps is None or reqs.expected_qps < _WRITE_QPS_THRESHOLD:
        return issues

    has_async = any(
        n.category.lower() in _ASYNC_CATEGORIES for n in design.nodes
    )

    if not has_async:
        issues.append(
            ValidationIssue(
                rule_id=RULE_ID,
                severity=Severity.WARNING,
                message=(
                    f"Design expects {reqs.expected_qps:,} QPS but has no "
                    f"message queue or streaming component for asynchronous "
                    f"write decoupling."
                ),
                suggestion=(
                    "Add a message queue (e.g. RabbitMQ, SQS) or a streaming "
                    "platform (e.g. Kafka, Kinesis) to decouple heavy writes."
                ),
            )
        )

    return issues
