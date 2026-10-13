import uuid

from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.knowledge import (
    CollectionType,
    EvalRunResult,
    KnowledgeIngestRequest,
    SearchQuery,
    SearchResponse,
    SourceResponse,
)
from app.services.knowledge.ingestion.pdf_parser import PDFParser
from app.services.knowledge.service import KnowledgeService, get_knowledge_service

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.post(
    "/ingest",
    response_model=SourceResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Ingest a document into the knowledge base",
)
async def ingest_document(
    request: KnowledgeIngestRequest,
    db: AsyncSession = Depends(get_db),
    service: KnowledgeService = Depends(get_knowledge_service),
) -> SourceResponse:
    try:
        return await service.ingest_document(request, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Document ingestion failed: {e!s}",
        ) from e


@router.post(
    "/upload",
    response_model=SourceResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload and ingest a Markdown or PDF file",
)
async def upload_document(
    file: UploadFile = File(...),
    title: str = Query(...),
    collection: CollectionType = Query(...),
    licence: str = Query("CC-BY-4.0"),
    publication_date: str | None = Query(None),
    tags: str | None = Query(None, description="Comma-separated tags"),
    db: AsyncSession = Depends(get_db),
    service: KnowledgeService = Depends(get_knowledge_service),
) -> SourceResponse:
    content_bytes = await file.read()
    filename = file.filename or "uploaded_file"
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []

    if filename.endswith(".pdf"):
        pdf_parser = PDFParser(chunker=service.chunker)
        temp_source_id = str(uuid.uuid4())
        chunks = pdf_parser.parse_pdf(
            pdf_source=content_bytes,
            source_id=temp_source_id,
            title=title,
            collection=collection,
            licence=licence,
            publication_date=publication_date,
            tags=tag_list,
        )
        # Assemble text for ingest
        aggregated_text = "\n\n".join(c.text for c in chunks)
        req = KnowledgeIngestRequest(
            title=title,
            collection=collection,
            content=aggregated_text,
            licence=licence,
            publication_date=publication_date,
            tags=tag_list,
        )
        return await service.ingest_document(req, db)
    else:
        # Default to text / Markdown decode
        text_content = content_bytes.decode("utf-8", errors="replace")
        req = KnowledgeIngestRequest(
            title=title,
            collection=collection,
            content=text_content,
            licence=licence,
            publication_date=publication_date,
            tags=tag_list,
        )
        return await service.ingest_document(req, db)


@router.post(
    "/search",
    response_model=SearchResponse,
    status_code=status.HTTP_200_OK,
    summary="Hybrid search over knowledge base with optional reranking",
)
async def search_knowledge(
    query: SearchQuery,
    service: KnowledgeService = Depends(get_knowledge_service),
) -> SearchResponse:
    try:
        return await service.search(query)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Search failed: {e!s}",
        ) from e


@router.get(
    "/sources",
    response_model=list[SourceResponse],
    status_code=status.HTTP_200_OK,
    summary="List ingested sources",
)
async def list_sources(
    collection: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
    service: KnowledgeService = Depends(get_knowledge_service),
) -> list[SourceResponse]:
    return await service.list_sources(collection, db)


@router.get(
    "/sources/{source_id}",
    response_model=SourceResponse,
    status_code=status.HTTP_200_OK,
    summary="Retrieve details of a single source",
)
async def get_source(
    source_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    service: KnowledgeService = Depends(get_knowledge_service),
) -> SourceResponse:
    source = await service.get_source(source_id, db)
    if not source:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Source {source_id} not found",
        )
    return source


@router.post(
    "/seed",
    status_code=status.HTTP_200_OK,
    summary="Seed default permitted documents across five collections",
)
async def seed_documents(
    db: AsyncSession = Depends(get_db),
    service: KnowledgeService = Depends(get_knowledge_service),
) -> dict[str, int]:
    count = await service.seed_default_documents(db)
    return {"seeded_sources": count}


@router.post(
    "/eval",
    response_model=EvalRunResult,
    status_code=status.HTTP_200_OK,
    summary="Run retrieval evaluation on 10 hand-written benchmark questions",
)
async def run_evaluation(
    db: AsyncSession = Depends(get_db),
    service: KnowledgeService = Depends(get_knowledge_service),
) -> EvalRunResult:
    try:
        return await service.run_evaluation(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Evaluation failed: {e!s}",
        ) from e
