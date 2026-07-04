from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from app.pdf_loader import extract_text
from app.chunker import chunk_text
from app.embeddings import generate_embedding
from app.vector_store import add_documents
from app.rag import stream_answer
from pydantic import BaseModel

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Assistant Backend is running!"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded PDF
    destination = UPLOAD_DIR / file.filename

    with open(destination, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from the PDF
    text = extract_text(str(destination))

    # Split the text into chunks
    chunks = chunk_text(text)

    # Generate embeddings for all chunks
    embeddings = generate_embedding(chunks)

    # Store chunks and embeddings in ChromaDB
    add_documents(chunks, embeddings)

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "status": "indexed"
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    return StreamingResponse(
        stream_answer(request.question),
        media_type="text/plain"
    )