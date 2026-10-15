"""Rule: cache-before-database

When the design expects high throughput (>= 1 000 QPS or >= 10 000 users)
and has a database, it should also include a caching layer to prevent the
database from becoming a bottleneck.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "cache-before-db"

_QPS_THRESHOLD = 1_000
_USERS_THRESHOLD = 10_000


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag high-throughput designs that lack a cache in front of a database."""
    issues: list[ValidationIssue] = []

    reqs = design.requirements
    high_traffic = (
        (reqs.expected_qps is not None and reqs.expected_qps >= _QPS_THRESHOLD)
        or (
            reqs.expected_users is not None
            and reqs.expected_users >= _USERS_THRESHOLD
        )
    )

    if not high_traffic:
        return issues

    has_db = any(n.category.lower() == "database" for n in design.nodes)
    has_cache = any(n.category.lower() == "cache" for n in design.nodes)

    if has_db and not has_cache:
        db_ids = [
            n.id for n in design.nodes if n.category.lower() == "database"
        ]
        issues.append(
            ValidationIssue(
                rule_id=RULE_ID,
                severity=Severity.WARNING,
                message=(
                    f"Design expects high traffic "
                    f"(QPS={reqs.expected_qps}, users={reqs.expected_users}) "
                    f"but has no cache layer in front of the database."
                ),
                node_ids=db_ids,
                suggestion=(
                    "Add a cache component (e.g. Redis, Memcached) with a "
                    "cache-aside or read-through pattern."
                ),
            )
        )

    return issues
