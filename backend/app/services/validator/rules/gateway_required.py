"""Rule: gateway-required

When the design has more than one application-layer service, it should
include a gateway or load-balancer component. Without one, clients would
need to know every service address, creating tight coupling and blocking
cross-cutting concerns (rate-limiting, auth, TLS termination).
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "gateway-required"

_GATEWAY_CATEGORIES = frozenset({"gateway"})
_GATEWAY_LAYERS = frozenset({"gateway", "edge"})
_APP_LAYER = "application"


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag designs with multiple app services but no gateway."""
    issues: list[ValidationIssue] = []

    app_nodes = [
        n for n in design.nodes if n.layer.lower() == _APP_LAYER
    ]
    has_gateway = any(
        n.category.lower() in _GATEWAY_CATEGORIES
        or n.layer.lower() in _GATEWAY_LAYERS
        for n in design.nodes
    )

    if len(app_nodes) >= 2 and not has_gateway:
        node_ids = [n.id for n in app_nodes]
        issues.append(
            ValidationIssue(
                rule_id=RULE_ID,
                severity=Severity.WARNING,
                message=(
                    f"Design has {len(app_nodes)} application services "
                    f"but no API gateway or load balancer. Clients must "
                    f"address each service directly."
                ),
                node_ids=node_ids,
                suggestion=(
                    "Add an API gateway (e.g. Kong, NGINX, AWS ALB) in "
                    "front of application services."
                ),
            )
        )

    return issues
