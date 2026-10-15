"""Rule: dangling-nodes

Flags nodes that are completely disconnected from all edges. A component
that neither sends nor receives connections is likely a mistake (it won't
participate in any data flow).
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "no-dangling-nodes"


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag nodes that appear in no edge (as source or target)."""
    issues: list[ValidationIssue] = []

    if not design.edges:
        # If there are no edges at all but multiple nodes, everything is
        # dangling — flag them.
        if len(design.nodes) >= 2:
            for node in design.nodes:
                issues.append(
                    ValidationIssue(
                        rule_id=RULE_ID,
                        severity=Severity.WARNING,
                        message=(
                            f"Node '{node.slug}' (node {node.id}) is not "
                            f"connected to any other component."
                        ),
                        node_ids=[node.id],
                        suggestion=(
                            f"Connect '{node.slug}' to the architecture or "
                            f"remove it if unused."
                        ),
                    )
                )
        return issues

    connected_ids: set[str] = set()
    for edge in design.edges:
        connected_ids.add(edge.source_id)
        connected_ids.add(edge.target_id)

    for node in design.nodes:
        if node.id not in connected_ids:
            issues.append(
                ValidationIssue(
                    rule_id=RULE_ID,
                    severity=Severity.WARNING,
                    message=(
                        f"Node '{node.slug}' (node {node.id}) is not "
                        f"connected to any other component."
                    ),
                    node_ids=[node.id],
                    suggestion=(
                        f"Connect '{node.slug}' to the architecture or "
                        f"remove it if unused."
                    ),
                )
            )

    return issues
