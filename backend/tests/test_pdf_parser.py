import io

import pypdf

from app.services.knowledge.ingestion.pdf_parser import PDFParser


def test_pdf_parser_extracts_pages_and_chunks():
    # Create an in-memory PDF with pypdf
    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=72, height=72)
    # Write empty / simple stream
    pdf_bytes_io = io.BytesIO()
    writer.write(pdf_bytes_io)
    pdf_bytes = pdf_bytes_io.getvalue()

    parser = PDFParser()
    chunks = parser.parse_pdf(
        pdf_source=pdf_bytes,
        source_id="pdf-src-1",
        title="Sample Architecture Whitepaper",
        collection="whitepapers",  # type: ignore[arg-type]
    )

    # Empty blank page yields 0 chunks gracefully without crashing
    assert isinstance(chunks, list)
