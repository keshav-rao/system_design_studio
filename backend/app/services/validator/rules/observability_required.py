"""Rule: observability-required

Production-grade architectures should include at least one observability
component (monitoring, logging, tracing). Without observability you cannot
detect or diagnose issues in production.

This rule fires as INFO when there's only a single node (prototype/MVP)
and as WARNING when there are multiple services.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "observability-required"

_OBSERVABILITY_CATEGORY = "observability"


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag designs that lack observability tooling."""
    issues: list[ValidationIssue] = []

    has_observability = any(
        n.category.lower() == _OBSERVABILITY_CATEGORY for n in design.nodes
    )

    if has_observability:
        return issues

    if len(design.nodes) <= 1:
        return issues  # single-node MVP, skip

    severity = Severity.WARNING if len(design.nodes) >= 3 else Severity.INFO

    issues.append(
        ValidationIssue(
            rule_id=RULE_ID,
            severity=severity,
            message=(
                f"Design has {len(design.nodes)} components but no "
                f"observability tooling (monitoring, logging, or tracing)."
            ),
            suggestion=(
                "Add an observability stack (e.g. Prometheus + Grafana, "
                "Datadog, ELK, or OpenTelemetry Collector)."
            ),
        )
    )

    return issues
