from app.pdf_loader import extract_text
from app.chunker import chunk_text

text = extract_text("/Users/daniel/Desktop/enterprise-rag-assistant/backend/uploads/Resume_intern.pdf")

chunks = chunk_text(text)

print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n----- Chunk {i + 1} -----")
    print(chunk)