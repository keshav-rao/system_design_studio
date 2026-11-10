import hashlib
import json
import logging
import re
import uuid
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

from llama_index.core import SimpleDirectoryReader

logger = logging.getLogger(__name__)

CORPUS_EXTENSIONS = [".md", ".markdown", ".txt", ".rst", ".json", ".pdf", ".html"]
ROOT_COLLECTION = "corpus_root"


@dataclass
class CorpusDocument:
    rel_path: str
    title: str
    collection: str
    text: str
    content_hash: str
    licence: str = "unspecified"
    origin_url: str | None = None
    publication_date: str | None = None
    tags: list[str] = field(default_factory=list)

    @property
    def source_id(self) -> uuid.UUID:
        return uuid.uuid5(uuid.NAMESPACE_URL, f"corpus://{self.rel_path}")


def _load_manifest(root: Path) -> dict[str, dict]:
    manifest_path = root / "corpus_manifest.json"
    if not manifest_path.exists():
        return {}
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        logger.warning("Could not read corpus manifest: %s", e)
        return {}
    return {d["path"]: d for d in data.get("documents", []) if "path" in d}


def _title(text: str, path: Path) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()[:255]
    return path.stem.replace("_", " ").replace("-", " ").strip()[:255]


def iter_corpus_documents(
    root: Path, collections: list[str] | None = None
) -> Iterator[CorpusDocument]:
    """content_hash covers the text and all indexed metadata, so manifest edits
    trigger re-indexing."""
    """Read every supported file under root with LlamaIndex, one file at a time."""
    root = root.resolve()
    manifest = _load_manifest(root)
    reader = SimpleDirectoryReader(
        input_dir=str(root),
        recursive=True,
        required_exts=CORPUS_EXTENSIONS,
        filename_as_id=True,
    )
    for docs in reader.iter_data():
        if not docs:
            continue
        path = Path(docs[0].metadata["file_path"])
        rel_path = path.relative_to(root).as_posix()
        parts = rel_path.split("/")
        collection = parts[0] if len(parts) > 1 else ROOT_COLLECTION
        if collections and collection not in collections:
            continue
        text = "\n\n".join(d.get_content() for d in docs)
        if not text.strip():
            continue
        meta = manifest.get(rel_path, {})
        title = _title(text, path)
        licence = meta.get("licence", "unspecified")
        origin_url = meta.get("source_url")
        publication_date = meta.get("last_verified")
        tags = list(parts[:-1]) + [
            str(meta[k]) for k in ("topic", "component") if meta.get(k)
        ]
        fingerprint = json.dumps(
            [text, title, collection, licence, origin_url, publication_date, tags]
        )
        yield CorpusDocument(
            rel_path=rel_path,
            title=title,
            collection=collection,
            text=text,
            content_hash=hashlib.sha256(fingerprint.encode("utf-8")).hexdigest()[:16],
            licence=licence,
            origin_url=origin_url,
            publication_date=publication_date,
            tags=tags,
        )
