"""Data access for projects, users, and requirements."""

import uuid
from typing import Any

from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Design, Project, Requirement, User

DEFAULT_USER_EMAIL = "local@system-design-studio"


class ProjectRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_or_create_default_user(self) -> User:
        user = (
            await self.db.execute(select(User).where(User.email == DEFAULT_USER_EMAIL))
        ).scalar_one_or_none()
        if user is None:
            user = User(id=uuid.uuid4(), email=DEFAULT_USER_EMAIL)
            self.db.add(user)
            await self.db.flush()
        return user

    async def create(self, name: str, description: str | None) -> Project:
        user = await self.get_or_create_default_user()
        project = Project(
            id=uuid.uuid4(),
            user_id=user.id,
            name=name,
            description=description,
            status="interviewing",
        )
        self.db.add(project)
        await self.db.commit()
        await self.db.refresh(project)
        return project

    async def get(self, project_id: uuid.UUID) -> Project | None:
        return await self.db.get(Project, project_id)

    async def list_with_version_counts(
        self, limit: int = 50, offset: int = 0
    ) -> list[tuple[Project, int]]:
        counts = (
            select(Design.project_id, func.count(Design.id).label("n"))
            .group_by(Design.project_id)
            .subquery()
        )
        stmt = (
            select(Project, func.coalesce(counts.c.n, 0))
            .outerjoin(counts, counts.c.project_id == Project.id)
            .order_by(desc(Project.created_at))
            .limit(limit)
            .offset(offset)
        )
        rows = (await self.db.execute(stmt)).all()
        return [(row[0], int(row[1])) for row in rows]

    async def count_versions(self, project_id: uuid.UUID) -> int:
        stmt = select(func.count(Design.id)).where(Design.project_id == project_id)
        return int((await self.db.execute(stmt)).scalar_one())

    async def set_status(self, project: Project, status: str) -> None:
        project.status = status
        await self.db.commit()

    async def upsert_requirements(
        self,
        project_id: uuid.UUID,
        values: dict[str, Any],
        assumed_keys: set[str],
    ) -> None:
        existing = {
            r.key: r
            for r in (
                await self.db.execute(
                    select(Requirement).where(Requirement.project_id == project_id)
                )
            ).scalars()
        }
        for key, value in values.items():
            row = existing.get(key)
            if row is None:
                row = Requirement(id=uuid.uuid4(), project_id=project_id, key=key)
                self.db.add(row)
            row.value = value
            row.is_assumed = key in assumed_keys
        await self.db.flush()

    async def list_requirements(self, project_id: uuid.UUID) -> list[Requirement]:
        stmt = (
            select(Requirement)
            .where(Requirement.project_id == project_id)
            .order_by(Requirement.key)
        )
        return list((await self.db.execute(stmt)).scalars())
