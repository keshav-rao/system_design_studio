import re

from app.schemas.knowledge import CollectionType, KnowledgeChunk


class HeadingAwareChunker:
    """
    Heading-aware document chunker.
    Parses Markdown headings (#, ##, ###, etc.) to maintain a hierarchical
    breadcrumb section path (e.g. 'Foundations > Consistency > CAP Theorem')
    and segments body text into semantic chunks bounded by token/char limits.
    """

    def __init__(self, target_chunk_size: int = 1200, chunk_overlap: int = 150):
        self.target_chunk_size = target_chunk_size
        self.chunk_overlap = chunk_overlap

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
        tags = tags or []
        lines = content.splitlines()

        # State machine tracking current heading stack
        heading_stack: list[tuple[int, str]] = []  # [(level, heading_text)]
        current_section_lines: list[str] = []
        chunks: list[KnowledgeChunk] = []

        heading_regex = re.compile(r"^(#{1,6})\s+(.*)$")

        def flush_current_section():
            if not current_section_lines:
                return

            section_text = "\n".join(current_section_lines).strip()
            if not section_text:
                return

            section_path = (
                " > ".join(h[1] for h in heading_stack) if heading_stack else title
            )

            # Sub-divide if section_text exceeds target_chunk_size
            sub_chunks = self._split_text_into_blocks(section_text)
            for _i, block in enumerate(sub_chunks):
                chunk_id = f"{source_id}-chunk-{len(chunks) + 1}"
                token_estimate = max(1, len(block.split()))
                chunks.append(
                    KnowledgeChunk(
                        id=chunk_id,
                        source_id=source_id,
                        collection=collection,
                        title=title,
                        section_path=section_path,
                        licence=licence,
                        publication_date=publication_date,
                        tags=tags,
                        text=block,
                        token_count=token_estimate,
                    )
                )
            current_section_lines.clear()

        for line in lines:
            match = heading_regex.match(line.strip())
            if match:
                # Heading encountered: flush previous section
                flush_current_section()
                level = len(match.group(1))
                h_text = match.group(2).strip()

                # Pop higher or equal levels from stack
                while heading_stack and heading_stack[-1][0] >= level:
                    heading_stack.pop()
                heading_stack.append((level, h_text))
            else:
                current_section_lines.append(line)

        # Flush final section
        flush_current_section()

        # Fallback if content had no headings
        if not chunks and content.strip():
            blocks = self._split_text_into_blocks(content.strip())
            for i, b in enumerate(blocks):
                chunks.append(
                    KnowledgeChunk(
                        id=f"{source_id}-chunk-{i+1}",
                        source_id=source_id,
                        collection=collection,
                        title=title,
                        section_path=title,
                        licence=licence,
                        publication_date=publication_date,
                        tags=tags,
                        text=b,
                        token_count=max(1, len(b.split())),
                    )
                )

        return chunks

    def _split_text_into_blocks(self, text: str) -> list[str]:
        """Split text by paragraphs, respecting target_chunk_size and overlap."""
        if len(text) <= self.target_chunk_size:
            return [text]

        paragraphs = text.split("\n\n")
        blocks: list[str] = []
        current_block: list[str] = []
        current_len = 0

        for p in paragraphs:
            p_len = len(p)
            if current_len + p_len > self.target_chunk_size and current_block:
                block_content = "\n\n".join(current_block).strip()
                if block_content:
                    blocks.append(block_content)
                # Keep last paragraph for overlap if within overlap budget
                if (
                    self.chunk_overlap > 0
                    and len(current_block[-1]) <= self.chunk_overlap
                ):
                    current_block = [current_block[-1], p]
                    current_len = len(current_block[0]) + p_len
                else:
                    current_block = [p]
                    current_len = p_len
            else:
                current_block.append(p)
                current_len += p_len + 2

        if current_block:
            tail = "\n\n".join(current_block).strip()
            if tail:
                blocks.append(tail)

        return blocks
