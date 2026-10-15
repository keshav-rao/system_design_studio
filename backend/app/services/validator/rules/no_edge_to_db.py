"""Rule: edge-to-database-direct

Flags connections that go directly from edge/CDN components to database
components, bypassing the application layer. This is a well-known
antipattern: edge should talk to an API gateway or application server,
never directly to the data tier.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "no-edge-to-db"

_EDGE_LAYERS = frozenset({"edge"})
_DATA_CATEGORIES = frozenset({"database", "cache", "queue", "streaming", "storage"})


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Return issues for direct edge-to-data connections."""
    issues: list[ValidationIssue] = []

    node_map = {n.id: n for n in design.nodes}

    for edge in design.edges:
        src = node_map.get(edge.source_id)
        tgt = node_map.get(edge.target_id)
        if not src or not tgt:
            continue

        if (
            src.layer.lower() in _EDGE_LAYERS
            and tgt.category.lower() in _DATA_CATEGORIES
        ):
            issues.append(
                ValidationIssue(
                    rule_id=RULE_ID,
                    severity=Severity.ERROR,
                    message=(
                        f"Edge component '{src.slug}' (node {src.id}) connects "
                        f"directly to data component '{tgt.slug}' (node {tgt.id}). "
                        f"Route through an application or gateway layer instead."
                    ),
                    node_ids=[src.id, tgt.id],
                    edge_ids=[f"{edge.source_id}->{edge.target_id}"],
                    suggestion=(
                        "Insert an API gateway or application server between "
                        f"'{src.slug}' and '{tgt.slug}'."
                    ),
                )
            )

    return issues
