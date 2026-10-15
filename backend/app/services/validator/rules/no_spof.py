"""Rule: no-single-point-of-failure

Flags data-layer components (databases, caches, queues, streaming, storage)
that have only one replica and no alternatives in the design.

A single-instance data store with no failover is the classic SPOF.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "no-spof"

# Categories where a single replica is dangerous
_DATA_CATEGORIES = frozenset({
    "database",
    "cache",
    "queue",
    "streaming",
    "storage",
})


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Return issues for single-replica data-layer components."""
    issues: list[ValidationIssue] = []

    # Build a set of categories present in the design
    categories_present: dict[str, list[str]] = {}
    for node in design.nodes:
        categories_present.setdefault(node.category.lower(), []).append(node.id)

    for node in design.nodes:
        cat = node.category.lower()
        if cat not in _DATA_CATEGORIES:
            continue

        if node.replicas >= 2:
            continue

        # Check if there is at least one other node in the same category
        siblings = categories_present.get(cat, [])
        if len(siblings) >= 2:
            continue

        issues.append(
            ValidationIssue(
                rule_id=RULE_ID,
                severity=Severity.ERROR,
                message=(
                    f"Component '{node.slug}' (node {node.id}) is a single "
                    f"point of failure: 1 replica with no same-category "
                    f"failover in the design."
                ),
                node_ids=[node.id],
                suggestion=(
                    f"Add replicas (replicas >= 2) or a failover instance "
                    f"for '{node.slug}'."
                ),
            )
        )

    return issues
