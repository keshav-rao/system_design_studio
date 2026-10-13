from typing import Any

import httpx
from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, Any]:
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@router.get("/ready", status_code=status.HTTP_200_OK)
async def readiness_check(
    db: AsyncSession = Depends(get_db),
) -> dict[str, Any]:
    checks: dict[str, str] = {
        "database": "unknown",
        "qdrant": "unknown",
    }

    # Check Database
    try:
        await db.execute(text("SELECT 1"))
        checks["database"] = "healthy"
    except Exception as exc:
        checks["database"] = f"unhealthy: {exc!s}"

    # Check Qdrant
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            res = await client.get(f"{settings.QDRANT_URL}/healthz")
            if res.status_code == 200:
                checks["qdrant"] = "healthy"
            else:
                checks["qdrant"] = f"unexpected_status: {res.status_code}"
    except Exception as exc:
        checks["qdrant"] = f"unreachable: {exc!s}"

    overall_healthy = all(v == "healthy" for v in checks.values())
    return {
        "status": "ok" if overall_healthy else "degraded",
        "checks": checks,
    }
