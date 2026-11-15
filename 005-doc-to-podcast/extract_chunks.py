"""Stage 1: Semantic PDF & Markdown chunker using PyMuPDF (fitz)."""

import re
import fitz


def extract_clean_chunks(pdf_path: str, max_chars: int = 4000) -> list[str]:
    """Extract clean text chunks from a PDF or Markdown document."""
    doc = fitz.open(pdf_path)
    chunks: list[str] = []
    buf = ""
    for page in doc:
        text = page.get_text("text")
        clean = re.sub(r"\s+", " ", text).strip()
        if not clean:
            continue
        if len(buf) + len(clean) > max_chars:
            if buf.strip():
                chunks.append(buf.strip())
            buf = ""
        buf += clean + " "
    if buf.strip():
        chunks.append(buf.strip())
    return chunks
