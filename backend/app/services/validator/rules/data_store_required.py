"""Rule: data-store-required

A design that requires data durability must include at least one database
or storage component. Without persistent storage, user data would be lost
on restart.
"""

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
)

RULE_ID = "data-store-required"

_DURABLE_CATEGORIES = frozenset({"database", "storage"})


def validate(design: DesignDocument) -> list[ValidationIssue]:
    """Flag designs that need durability but lack persistent storage."""
    issues: list[ValidationIssue] = []

    if not design.requirements.data_durability_required:
        return issues

    has_store = any(
        n.category.lower() in _DURABLE_CATEGORIES for n in design.nodes
    )

    if not has_store:
        issues.append(
            ValidationIssue(
                rule_id=RULE_ID,
                severity=Severity.ERROR,
                message=(
                    "Design requires data durability but contains no "
                    "database or storage component."
                ),
                suggestion=(
                    "Add a database (e.g. PostgreSQL, DynamoDB) or object "
                    "storage (e.g. S3) to persist data."
                ),
            )
        )

    return issues
