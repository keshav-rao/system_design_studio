import io
from typing import BinaryIO

import pypdf

from app.schemas.knowledge import CollectionType, KnowledgeChunk
from app.services.knowledge.ingestion.chunker import HeadingAwareChunker


class PDFParser:
    """Extracts text and page numbers from PDF documents and chunks them."""

    def __init__(self, chunker: HeadingAwareChunker | None = None):
        self.chunker = chunker or HeadingAwareChunker()

    def parse_pdf(
        self,
        pdf_source: bytes | BinaryIO | str,
        source_id: str,
        title: str,
        collection: CollectionType,
        licence: str = "CC-BY-4.0",
        publication_date: str | None = None,
        tags: list[str] | None = None,
    ) -> list[KnowledgeChunk]:
        tags = tags or []
        chunks: list[KnowledgeChunk] = []

        if isinstance(pdf_source, bytes):
            reader = pypdf.PdfReader(io.BytesIO(pdf_source))
        elif isinstance(pdf_source, str):
            reader = pypdf.PdfReader(pdf_source)
        else:
            reader = pypdf.PdfReader(pdf_source)

        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            if not text.strip():
                continue

            page_chunks = self.chunker.chunk_markdown(
                content=text,
                source_id=source_id,
                title=f"{title} (p. {page_num})",
                collection=collection,
                licence=licence,
                publication_date=publication_date,
                tags=tags,
            )
            for c in page_chunks:
                c.page = page_num
                chunks.append(c)

        return chunks
