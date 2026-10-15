"""Rule: duplicate-edges

Flags duplicate edges (same source_id → target_id pair appearing more
than once). Duplicate connections are typically a modelling mistake and
clutter the diagram.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "no-duplicate-edges"


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag duplicate directed edges."""
    issues: list[ValidationIssue] = []

    seen: set[tuple[str, str]] = set()
    for edge in design.edges:
        key = (edge.source_id, edge.target_id)
        if key in seen:
            issues.append(
                ValidationIssue(
                    rule_id=RULE_ID,
                    severity=Severity.WARNING,
                    message=(
                        f"Duplicate edge from '{edge.source_id}' to "
                        f"'{edge.target_id}'. "
                        f"Remove the redundant connection."
                    ),
                    edge_ids=[f"{edge.source_id}->{edge.target_id}"],
                    suggestion="Remove the duplicate edge.",
                )
            )
        seen.add(key)

    return issues
