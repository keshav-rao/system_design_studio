from app.services.knowledge.ingestion.chunker import HeadingAwareChunker


def test_heading_aware_chunking_hierarchy():
    chunker = HeadingAwareChunker(target_chunk_size=500, chunk_overlap=50)

    markdown_text = """# Foundations
This is introduction text.

## Consistent Hashing
Consistent hashing is used to map keys and servers to a circular hash ring.
When nodes are added or removed, minimal keys are remapped.

### Virtual Nodes
Virtual nodes ensure uniform key distribution across servers.
Heterogeneous servers receive proportionally more vnodes.

## Database Sharding
Sharding partitions rows across multiple databases horizontally.
"""

    chunks = chunker.chunk_markdown(
        content=markdown_text,
        source_id="src-123",
        title="Distributed Systems Guide",
        collection="foundations",
        licence="CC-BY-4.0",
        publication_date="2024-01-01",
        tags=["distributed", "hashing"],
    )

    assert len(chunks) >= 3

    # Check first section
    c0 = chunks[0]
    assert c0.source_id == "src-123"
    assert c0.collection == "foundations"
    assert "Foundations" in c0.section_path
    assert c0.licence == "CC-BY-4.0"
    assert c0.tags == ["distributed", "hashing"]

    # Check subsection breadcrumb
    vnode_chunk = next(c for c in chunks if "Virtual Nodes" in c.section_path)
    assert (
        "Foundations > Consistent Hashing > Virtual Nodes" in vnode_chunk.section_path
    )
    assert "vnodes" in vnode_chunk.text.lower()


def test_chunker_handles_plain_text():
    chunker = HeadingAwareChunker(target_chunk_size=300)
    plain_text = (
        "This is a simple plain text document without any markdown headers.\n\n"
        "It still contains useful system knowledge."
    )

    chunks = chunker.chunk_markdown(
        content=plain_text,
        source_id="src-plain",
        title="Plain Doc",
        collection="capacity",
    )

    assert len(chunks) == 1
    assert chunks[0].section_path == "Plain Doc"
    assert chunks[0].title == "Plain Doc"
    assert chunks[0].collection == "capacity"
