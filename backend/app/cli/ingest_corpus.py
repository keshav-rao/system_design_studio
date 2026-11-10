"""Ingest the RAG corpus: python -m app.cli.ingest_corpus [--recreate] [--eval]"""

import argparse
import asyncio
import json
import logging
from pathlib import Path

from app.core.config import settings
from app.core.database import AsyncSessionLocal
from app.services.knowledge.providers.qdrant_store import QdrantVectorStore
from app.services.knowledge.service import KnowledgeService


async def main(args: argparse.Namespace) -> None:
    service = KnowledgeService()
    if args.recreate and isinstance(service.vector_store, QdrantVectorStore):
        await service.vector_store.recreate()
    async with AsyncSessionLocal() as db:
        if args.recreate:
            from sqlalchemy import update

            from app.models.source import Source

            await db.execute(update(Source).values(version="stale"))
            await db.commit()
        stats = await service.ingest_corpus(
            db, Path(args.path), collections=args.collections, limit=args.limit
        )
        print(json.dumps(stats))
        if args.eval:
            result = await service.run_evaluation(db)
            print(result.model_dump_json(exclude={"details"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", default=settings.RAG_CORPUS_PATH)
    parser.add_argument("--collections", nargs="*", help="Top-level folders only")
    parser.add_argument("--limit", type=int, help="Max new/changed files")
    parser.add_argument("--recreate", action="store_true", help="Rebuild the index")
    parser.add_argument("--eval", action="store_true", help="Run retrieval eval")
    logging.basicConfig(level=settings.LOG_LEVEL)
    asyncio.run(main(parser.parse_args()))
