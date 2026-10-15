"""Rule: invalid-edge-references

Flags edges whose source_id or target_id does not match any node in the
design. This is a structural integrity check — broken references mean the
graph is malformed.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "valid-edge-refs"


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag edges that reference non-existent nodes."""
    issues: list[ValidationIssue] = []

    node_ids = {n.id for n in design.nodes}

    for edge in design.edges:
        missing: list[str] = []
        if edge.source_id not in node_ids:
            missing.append(f"source '{edge.source_id}'")
        if edge.target_id not in node_ids:
            missing.append(f"target '{edge.target_id}'")

        if missing:
            issues.append(
                ValidationIssue(
                    rule_id=RULE_ID,
                    severity=Severity.ERROR,
                    message=(
                        f"Edge {edge.source_id}->{edge.target_id} references "
                        f"non-existent node(s): {', '.join(missing)}."
                    ),
                    edge_ids=[f"{edge.source_id}->{edge.target_id}"],
                    suggestion="Fix the edge to reference valid node IDs.",
                )
            )

    return issues
