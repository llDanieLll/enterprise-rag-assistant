from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from app.rag.pdf_loader import extract_text
from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embedding
from vector_store import add_documents
from app.rag.rag import stream_answer
from pydantic import BaseModel
from app.models import Message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)



class ChatRequest(BaseModel):
    question: str
    history: list[Message] = []


@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Assistant Backend is running!"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    print("1. Upload started")

    destination = UPLOAD_DIR / file.filename

    with open(destination, "wb") as buffer:
        buffer.write(await file.read())

    print("2. File saved")

    text = extract_text(str(destination))
    print("3. Text extracted")

    chunks = chunk_text(text)
    print(f"4. {len(chunks)} chunks created")

    embeddings = generate_embedding(chunks)
    print("5. Embeddings generated")

    add_documents(
        chunks,
        embeddings,
        file.filename,
    )
    print("6. Documents stored")

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "status": "indexed"
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    print(request.history)
    return StreamingResponse(
        stream_answer(
            request.question,
            request.history,
        ),
        media_type="text/plain"
    )