"""Validator API routes.

POST /api/v1/validator/validate — validate a design document
GET  /api/v1/validator/rules     — list available validation rules
"""

from fastapi import APIRouter, status

from app.schemas.validator import DesignDocument, ValidationResult
from app.services.validator.validator_service import validator_service

router = APIRouter(prefix="/validator", tags=["validator"])


@router.post(
    "/validate",
    response_model=ValidationResult,
    status_code=status.HTTP_200_OK,
    summary="Validate an architecture design against all deterministic rules",
)
async def validate_design(design: DesignDocument) -> ValidationResult:
    """Run all registered validation rules over the supplied design.

    The validation is synchronous and deterministic — no external I/O.
    """
    return validator_service.validate(design)


@router.get(
    "/rules",
    status_code=status.HTTP_200_OK,
    summary="List all available validation rule IDs",
)
async def list_rules() -> dict[str, list[str]]:
    """Return the ordered list of rule IDs."""
    return {"rules": validator_service.rule_ids}
