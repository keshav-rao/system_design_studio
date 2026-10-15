"""Rule: self-loop-detection

Flags edges where a node connects to itself. Self-loops are almost always
a modelling error in an architecture diagram.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "no-self-loops"


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag edges where source and target are the same node."""
    issues: list[ValidationIssue] = []

    for edge in design.edges:
        if edge.source_id == edge.target_id:
            issues.append(
                ValidationIssue(
                    rule_id=RULE_ID,
                    severity=Severity.ERROR,
                    message=(
                        f"Node '{edge.source_id}' has a self-loop edge. "
                        f"A component should not connect to itself."
                    ),
                    node_ids=[edge.source_id],
                    edge_ids=[f"{edge.source_id}->{edge.target_id}"],
                    suggestion="Remove the self-referencing edge.",
                )
            )

    return issues
