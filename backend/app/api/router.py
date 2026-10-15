from fastapi import APIRouter

from app.api.v1.catalog import router as catalog_router
from app.api.v1.health import router as health_router
from app.api.v1.knowledge import router as knowledge_router
from app.api.v1.projects import router as projects_router
from app.api.v1.validator import router as validator_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
api_router.include_router(knowledge_router)
api_router.include_router(catalog_router)
api_router.include_router(validator_router)
api_router.include_router(projects_router)

