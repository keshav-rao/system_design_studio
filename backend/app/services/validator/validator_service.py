"""Validator service — orchestrates all deterministic validation rules.

Each rule is a pure function in a separate module under
``app.services.validator.rules``.  The service discovers them, runs them
over a :class:`DesignDocument`, and aggregates the results into a single
:class:`ValidationResult`.
"""

import time
from types import ModuleType

from app.schemas.validator import (
    DesignDocument,
    Severity,
    ValidationIssue,
    ValidationResult,
)

# Import every rule module explicitly so static analysis and mypy can
# verify them.  Each module must expose ``RULE_ID: str`` and
# ``validate(design: DesignDocument) -> list[ValidationIssue]``.
from app.services.validator.rules import (
    async_processing,
    cache_before_db,
    data_store_required,
    gateway_required,
    multi_region,
    no_dangling_nodes,
    no_duplicate_edges,
    no_edge_to_db,
    no_self_loops,
    no_spof,
    throughput_bottleneck,
    valid_edge_refs,
)

# Ordered list of rule modules — structural checks first, then semantic.
_RULE_MODULES: list[ModuleType] = [
    valid_edge_refs,
    no_self_loops,
    no_duplicate_edges,
    no_dangling_nodes,
    no_spof,
    no_edge_to_db,
    gateway_required,
    cache_before_db,
    async_processing,
    data_store_required,
    multi_region,
    throughput_bottleneck,
]


class ValidatorService:
    """Runs all registered validation rules over a design document."""

    def __init__(self, rules: list[ModuleType] | None = None) -> None:
        self._rules = rules if rules is not None else _RULE_MODULES

    @property
    def rule_ids(self) -> list[str]:
        """Return the ordered list of rule IDs."""
        return [mod.RULE_ID for mod in self._rules]

    def validate(self, design: DesignDocument) -> ValidationResult:
        """Run all rules and return aggregated results.

        This method is synchronous and pure — it performs no I/O,
        no database access, and no network calls.
        """
        start = time.perf_counter()

        all_issues: list[ValidationIssue] = []
        rules_executed: list[str] = []

        for rule_mod in self._rules:
            rule_id: str = rule_mod.RULE_ID
            rules_executed.append(rule_id)
            issues = rule_mod.validate(design)
            all_issues.extend(issues)

        elapsed_ms = (time.perf_counter() - start) * 1000

        errors = sum(1 for i in all_issues if i.severity == Severity.ERROR)
        warnings = sum(1 for i in all_issues if i.severity == Severity.WARNING)
        infos = sum(1 for i in all_issues if i.severity == Severity.INFO)

        return ValidationResult(
            valid=errors == 0,
            total_issues=len(all_issues),
            errors=errors,
            warnings=warnings,
            infos=infos,
            issues=all_issues,
            rules_executed=rules_executed,
            elapsed_ms=round(elapsed_ms, 3),
        )


# Module-level singleton
validator_service = ValidatorService()
