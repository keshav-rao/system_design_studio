# Backend Schema

## Storage split
- PostgreSQL stores structured catalog, project, requirement, design, evidence-link, and evaluation data.
- Qdrant stores dense and sparse knowledge indexes. Payload mirrors chunk metadata so filters do not require joins.

## PostgreSQL tables
- `users` (optional for single-user v1): `id` UUID PK, `email` unique, `created_at`.
- `projects`: `id`, `user_id`, `name`, `description`, status (`interviewing`, `planning`, `designed`), timestamps.
- `requirements`: `id`, `project_id`, `key`, JSONB `value`, `is_assumed`, `updated_at`.
- `designs`: versioned append-only snapshots with `id`, `project_id`, `version`, nullable `parent_version`, JSONB `graph`, validation status (`valid`, `warnings`, `errors`), creator (`planner`, `user`), `created_at`.
- `design_nodes`: `id`, `design_id`, `component_id`, `label`, JSONB `config`, `rationale`, JSONB assumptions and alternatives, JSONB position.
- `design_edges`: `id`, `design_id`, source/target node IDs, protocol, notes.
- `node_evidence`: node ID, chunk ID, source ID, relevance score.
- `validation_issues`: `id`, `design_id`, `rule_id`, severity (`info`, `warning`, `error`), nullable node ID, message, suggested fix.
- `components`: `id`, unique slug, name, category, purpose, JSONB inputs/outputs/scaling traits/failure modes/limits/cost units, optional docs source, `updated_at`.
- `component_compatibility`: source and target component IDs, interface, allowed flag, JSONB conditions.
- `component_alternatives`: component ID, alternative ID, when to prefer.
- `sources`: `id`, title, collection (`foundations`, `patterns`, `cloud_docs`, `capacity`, `case_studies`), optional origin URL, licence, permission notes, publication/ingestion dates, version, optional refresh date.
- `eval_questions`: ID, question, JSONB gold source IDs, optional JSONB gold design.
- `eval_runs`: ID, JSONB config (model, embedder, reranker, prompt version), JSONB metrics, creation time.

Use UUID primary keys where applicable, foreign keys for relations, and Alembic for every schema change.

## Qdrant
- Collection: `knowledge_chunks`.
- Vectors: dense BAAI/bge-m3 plus sparse keyword vectors.
- Payload: source ID, collection, title, section path, page, licence, publication date, tags, text.
- Index filters for collection, tags, publication date, and licence.

## Pydantic contracts
```python
class Component(BaseModel):
    id: str
    catalog_slug: str
    label: str
    config: dict = {}
    rationale: str
    evidence_ids: list[str]
    assumptions: list[str] = []
    alternatives: list[str] = []

class Connection(BaseModel):
    source: str
    target: str
    protocol: str
    notes: str | None = None

class ArchitectureProposal(BaseModel):
    summary: str
    components: list[Component]
    connections: list[Connection]
    unaddressed_requirements: list[str] = []
    open_questions: list[str] = []

class ValidationIssue(BaseModel):
    rule_id: str
    severity: Literal["info", "warning", "error"]
    node_id: str | None
    message: str
    suggested_fix: str | None
```

## Data-layer rules
- Catalog is the source of truth: only known `catalog_slug` values are valid.
- Designs are append-only; edits create a new version.
- Time-sensitive facts carry dates; refresh jobs flag sources past `refresh_after`.
- Use Alembic migrations for schema changes; never edit the database by hand.
