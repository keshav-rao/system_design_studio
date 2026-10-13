import uuid
from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

CollectionType = Literal[
    "foundations", "patterns", "cloud_docs", "capacity", "case_studies"
]


class KnowledgeChunk(BaseModel):
    id: str
    source_id: str
    collection: CollectionType
    title: str
    section_path: str
    page: int | None = None
    licence: str
    publication_date: str | None = None
    tags: list[str] = Field(default_factory=list)
    text: str
    token_count: int = 0
    dense_vector: list[float] | None = None
    sparse_indices: list[int] | None = None
    sparse_values: list[float] | None = None


class SourceBase(BaseModel):
    title: str
    collection: CollectionType
    origin_url: str | None = None
    licence: str = "CC-BY-4.0"
    permission_notes: str | None = None
    publication_date: str | None = None
    version: str = "1.0"
    refresh_date: str | None = None


class KnowledgeIngestRequest(SourceBase):
    content: str
    tags: list[str] = Field(default_factory=list)


class SourceResponse(SourceBase):
    id: uuid.UUID
    ingested_at: datetime
    chunk_count: int = 0

    model_config = {"from_attributes": True}


class KnowledgeFilter(BaseModel):
    collections: list[CollectionType] | None = None
    tags: list[str] | None = None
    licence: str | None = None
    publication_date: str | None = None


class SearchQuery(BaseModel):
    query: str
    limit: int = Field(default=10, ge=1, le=50)
    filter: KnowledgeFilter | None = None
    use_reranker: bool = True
    min_score: float = Field(default=0.0, ge=0.0)


class SearchResult(BaseModel):
    chunk_id: str
    source_id: str
    title: str
    collection: str
    section_path: str
    text: str
    score: float
    licence: str
    publication_date: str | None = None
    tags: list[str] = Field(default_factory=list)
    page: int | None = None


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]
    total: int
    retrieval_mode: str = "hybrid"


class EvalQuestionSchema(BaseModel):
    id: str
    question: str
    gold_source_ids: list[str]
    gold_topics: list[str] = Field(default_factory=list)


class EvalRunResult(BaseModel):
    total_questions: int
    mrr: float  # Mean Reciprocal Rank
    recall_at_3: float
    recall_at_5: float
    passed: bool
    details: list[dict[str, Any]]
