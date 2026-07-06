# Enterprise RAG Assistant

An enterprise-ready Retrieval-Augmented Generation (RAG) assistant built from scratch with FastAPI, Ollama, and ChromaDB.

This project demonstrates how organizations can securely connect Large Language Models (LLMs) to private company knowledge without retraining the model. Instead of relying solely on the model's built-in knowledge, the assistant retrieves relevant internal documents and uses them as context before generating an answer.

---

## Features

- Upload one or more PDF documents
- Automatic document chunking
- Local embedding generation
- ChromaDB vector storage
- Semantic similarity retrieval
- Retrieval-Augmented Generation (RAG)
- Streaming responses
- Conversation memory
- Multi-document support with metadata
- FastAPI REST backend
- Local LLM inference using Ollama

---

## Tech Stack

| Component | Technology |
|-----------|-------------------------|
| Backend | FastAPI |
| RAG Pipeline | Custom RAG Pipeline |
| Local LLM | Ollama |
| Model | Qwen2.5:3B (configurable via Ollama) |
| Vector Database | ChromaDB |
| Embeddings | Ollama Embedding Model |
| Document Loader | PyMuPDF (fitz) |
| API Testing | Swagger UI |
| Language | Python |

---

## Project Structure

```
enterprise-rag-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── rag.py
│   │   ├── retriever.py
│   │   ├── vector_store.py
│   │   ├── embeddings.py
│   │   ├── chunker.py
│   │   ├── pdf_loader.py
│   │   └── models.py
│   ├── uploads/
│   └── vector_store/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md
```

---

## Architecture

```
               User Question
                     │
                     ▼
               FastAPI Endpoint
                     │
                     ▼
                  Retriever
                     │
                     ▼
             Chroma Vector Store
                     │
      Semantic Similarity Search
                     │
                     ▼
       Relevant Document Chunks
                     │
                     ▼
         Conversation History
                     │
                     ▼
            Prompt Construction
                     │
                     ▼
            Ollama (Qwen2.5)
                     │
                     ▼
                 Final Answer
```

---

## How RAG Works

Traditional LLMs only answer based on what they learned during training.

RAG (Retrieval-Augmented Generation) adds an external knowledge source.

The workflow is:

1. Load documents
2. Split into smaller chunks
3. Convert chunks into embeddings
4. Store embeddings in ChromaDB
5. User asks a question
6. Retrieve the most relevant chunks
7. Send both the question and retrieved context to the LLM
8. Generate an accurate answer grounded in the documents

This allows the model to answer questions using private enterprise knowledge without fine-tuning.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your_username>/enterprise-rag-assistant.git

cd enterprise-rag-assistant/backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama from:

https://ollama.com

Pull the model:

```bash
ollama pull llama3
```

Verify:

```bash
ollama list
```

---

## Run the Application

Start Ollama first.

Then launch FastAPI:

```bash
uvicorn app.main:app --reload
```

In another terminal, start the frontend (or open `frontend/index.html` if using a static server).

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test the API.

---

## Example Workflow

1. Place a PDF inside the `data/` folder.
2. Run the document loader.
3. Chunks are embedded and stored in ChromaDB.
4. Ask a question through the API.
5. The assistant retrieves relevant context.
6. Llama 3 generates the final response.

---

## Example Question

```
What is Retrieval-Augmented Generation?
```

Example response:

```
Retrieval-Augmented Generation (RAG) combines semantic retrieval with a language model by first searching a vector database for relevant document chunks and then using those chunks as context for answer generation.
```

---

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- FastAPI Backend Development
- ChromaDB Vector Database
- Semantic Search
- Prompt Engineering
- Conversation Memory
- Streaming LLM Responses
- Multi-document Retrieval
- Ollama Local LLM Deployment
- AI System Architecture

---

## Future Improvements

- AI agent with dynamic tool selection
- Web search tool integration
- Source citation in responses
- User authentication
- Docker deployment
- Hybrid search (keyword + vector)
- Long-term memory
- Multi-step agent planning

---

## Learning Outcomes

Through this project I learned:

- How enterprise AI systems connect LLMs with private knowledge.
- How vector embeddings enable semantic search.
- How to implement a custom RAG pipeline from scratch using FastAPI, Ollama, and ChromaDB.
- How ChromaDB stores and retrieves document embeddings.
- How FastAPI exposes AI functionality as REST APIs.
- How Ollama enables fully local LLM inference.

---

## License

This project is for educational and portfolio purposes.