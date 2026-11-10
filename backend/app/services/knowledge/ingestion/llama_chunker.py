from llama_index.core import Document
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter

from app.schemas.knowledge import CollectionType, KnowledgeChunk


class LlamaIndexChunker:
    """
    LlamaIndex chunking: MarkdownNodeParser splits on headings (keeping the
    header path), then SentenceSplitter bounds each section by token count.
    Same interface as HeadingAwareChunker.
    """

    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 64):
        self.markdown_parser = MarkdownNodeParser()
        self.splitter = SentenceSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

    @staticmethod
    def _section_path(title: str, header_path: str, text: str) -> str:
        parts = [p for p in header_path.strip("/").split("/") if p]
        first_line = text.lstrip().split("\n", 1)[0]
        if first_line.startswith("#"):
            parts.append(first_line.lstrip("#").strip())
        return " > ".join(parts) if parts else title

    def chunk_markdown(
        self,
        content: str,
        source_id: str,
        title: str,
        collection: CollectionType,
        licence: str = "CC-BY-4.0",
        publication_date: str | None = None,
        tags: list[str] | None = None,
    ) -> list[KnowledgeChunk]:
        if not content.strip():
            return []
        sections = self.markdown_parser.get_nodes_from_documents(
            [Document(text=content)]
        )
        chunks: list[KnowledgeChunk] = []
        for section in sections:
            text = section.get_content()
            section_path = self._section_path(
                title, str(section.metadata.get("header_path", "/")), text
            )
            for block in self.splitter.split_text(text):
                if not block.strip():
                    continue
                chunks.append(
                    KnowledgeChunk(
                        id=f"{source_id}-chunk-{len(chunks) + 1}",
                        source_id=source_id,
                        collection=collection,
                        title=title,
                        section_path=section_path,
                        licence=licence,
                        publication_date=publication_date,
                        tags=tags or [],
                        text=block,
                        token_count=max(1, len(block.split())),
                    )
                )
        return chunks
