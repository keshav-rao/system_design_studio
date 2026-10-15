"""Rule: throughput-bottleneck

Checks each edge in the design: if the source component's max throughput
significantly exceeds the target's max throughput, the target is a
potential bottleneck. This is a design-time headroom check, not a runtime
test.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "throughput-bottleneck"

# Target throughput below this fraction of source triggers a warning
_BOTTLENECK_RATIO = 0.5


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag edges where the target's QPS ceiling is much lower than the source's."""
    issues: list[ValidationIssue] = []

    node_map = {n.id: n for n in design.nodes}

    for edge in design.edges:
        src = node_map.get(edge.source_id)
        tgt = node_map.get(edge.target_id)
        if not src or not tgt:
            continue

        src_qps = src.limits.get("max_throughput_qps")
        tgt_qps = tgt.limits.get("max_throughput_qps")

        if src_qps is None or tgt_qps is None:
            continue

        try:
            src_val = int(src_qps)
            tgt_val = int(tgt_qps)
        except (ValueError, TypeError):
            continue

        if src_val <= 0:
            continue

        if tgt_val < src_val * _BOTTLENECK_RATIO:
            issues.append(
                ValidationIssue(
                    rule_id=RULE_ID,
                    severity=Severity.WARNING,
                    message=(
                        f"Throughput bottleneck: '{tgt.slug}' "
                        f"({tgt_val:,} QPS) is significantly lower than "
                        f"upstream '{src.slug}' ({src_val:,} QPS). "
                        f"Ratio {tgt_val/src_val:.0%} < {_BOTTLENECK_RATIO:.0%}."
                    ),
                    node_ids=[src.id, tgt.id],
                    edge_ids=[f"{edge.source_id}->{edge.target_id}"],
                    suggestion=(
                        f"Scale '{tgt.slug}' horizontally, add connection "
                        f"pooling, or insert a queue to buffer writes."
                    ),
                )
            )

    return issues
