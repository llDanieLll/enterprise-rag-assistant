# Enterprise RAG Assistant

An enterprise-ready Retrieval-Augmented Generation (RAG) assistant built with FastAPI, LangChain, Ollama, and ChromaDB.

This project demonstrates how organizations can securely connect Large Language Models (LLMs) to private company knowledge without retraining the model. Instead of relying solely on the model's built-in knowledge, the assistant retrieves relevant internal documents and uses them as context before generating an answer.

---

## Features

- Upload private company documents (PDF)
- Automatically split documents into chunks
- Generate vector embeddings
- Store embeddings in ChromaDB
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using Ollama
- REST API built with FastAPI
- Ready for enterprise knowledge bases

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | FastAPI |
| LLM Framework | LangChain |
| Local LLM | Ollama |
| Model | Llama 3 |
| Vector Database | ChromaDB |
| Embeddings | Ollama Embeddings |
| Document Loader | LangChain PDF Loader |
| API Testing | Swagger UI |
| Language | Python |

---

## Project Structure

```
enterprise-rag-assistant/
│
├── app/
│   ├── main.py
│   ├── rag.py
│   └── pdf_loader.py
│
├── data/
│   └── sample.pdf
│
├── chroma_db/
│
├── requirements.txt
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
            LangChain Retriever
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
            Prompt Construction
                     │
                     ▼
            Ollama (Llama 3)
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

cd enterprise-rag-assistant
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
- LangChain Pipelines
- Prompt Engineering
- Vector Databases
- Embedding Models
- Semantic Search
- FastAPI Development
- REST API Design
- Local LLM Deployment
- Enterprise AI Architecture

---

## Future Improvements

- Multi-document upload
- Conversation memory
- User authentication
- Streaming responses
- Citation of retrieved sources
- Docker deployment
- PostgreSQL integration
- Cloud deployment (AWS/Azure/GCP)
- Hybrid search (keyword + vector)
- Admin dashboard

---

## Learning Outcomes

Through this project I learned:

- How enterprise AI systems connect LLMs with private knowledge.
- How vector embeddings enable semantic search.
- How LangChain orchestrates retrieval pipelines.
- How ChromaDB stores and retrieves document embeddings.
- How FastAPI exposes AI functionality as REST APIs.
- How Ollama enables fully local LLM inference.

---

## License

This project is for educational and portfolio purposes.