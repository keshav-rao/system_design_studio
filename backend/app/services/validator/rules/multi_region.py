"""Rule: multi-region-consistency

When a design targets multiple regions (regions >= 2) and has a database,
it should address cross-region replication / consistency. This rule checks
that there are enough database replicas to span regions.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "multi-region-consistency"


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Warn when multi-region designs lack adequate DB replication."""
    issues: list[ValidationIssue] = []

    if design.requirements.regions < 2:
        return issues

    db_nodes = [
        n for n in design.nodes if n.category.lower() == "database"
    ]

    if not db_nodes:
        return issues  # data_store_required handles the missing DB case

    for db in db_nodes:
        if db.replicas < design.requirements.regions:
            issues.append(
                ValidationIssue(
                    rule_id=RULE_ID,
                    severity=Severity.WARNING,
                    message=(
                        f"Design targets {design.requirements.regions} regions "
                        f"but database '{db.slug}' (node {db.id}) has only "
                        f"{db.replicas} replica(s). Cross-region failover "
                        f"may not be possible."
                    ),
                    node_ids=[db.id],
                    suggestion=(
                        f"Increase replicas for '{db.slug}' to at least "
                        f"{design.requirements.regions} or use a globally "
                        f"distributed database (e.g. CockroachDB, Spanner)."
                    ),
                )
            )

    return issues
