# Enterprise AI Runtime

This project began as an enterprise-ready Retrieval-Augmented Generation (RAG) assistant but is now evolving into a modular AI Runtime designed to handle planning, execution, retrieval, and tool calling in a flexible and extensible manner.

---

## Core Architecture

- **RuntimeState**: Maintains the current state of the runtime, including context, memory, and execution history.
- **Planner**: Responsible for generating actionable plans based on the current state and user requests.
- **Plan**: Represents a sequence of steps or actions derived by the planner to fulfill a request.
- **Executor**: Executes the plan by invoking appropriate tools and managing execution flow.
- **Toolbox**: A registry and manager of available tools that the executor can call upon.
- **RAG**: Handles retrieval-augmented generation by integrating document retrieval with language model responses.
- **Providers**: Abstract interfaces to external services such as LLMs, calculators, and web search.

---

## Architecture Diagram

```mermaid
flowchart TD
    U[User Request] --> S[RuntimeState]
    S --> P[Planner]
    P --> PL[Plan]
    PL --> E[Executor]
    E --> T[Toolbox]
    T --> R[Retriever]
    T --> C[Calculator]
    T --> W[Web Search]
    T --> L[LLM Provider]
    R --> ER[Execution Result]
    C --> ER
    W --> ER
    L --> ER
    ER --> SM[State Manager (Coming Soon)]
    SM --> S
```

---

## Project Structure

```
enterprise-ai-runtime/
│
├── backend/
│   ├── app/
│   │   ├── planner/
│   │   ├── runtime/
│   │   ├── providers/
│   │   ├── rag/
│   │   ├── tools/
│   │   ├── toolbox.py
│   │   └── main.py
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

## Current Runtime Workflow

1. The **RuntimeState** captures the current context and user input.
2. The **Planner** analyzes the state and formulates a **Plan**.
3. The **Executor** carries out the plan by interacting with the **Toolbox**.
4. The **Toolbox** invokes appropriate tools such as retrievers, calculators, web search, or LLM providers.
5. Each tool returns an **Execution Result**.
6. The results update the **RuntimeState**, enabling iterative and dynamic processing.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your_username>/enterprise-ai-runtime.git

cd enterprise-ai-runtime/backend
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

## Roadmap

- [x] RuntimeState  
- [x] Planner  
- [x] Plan  
- [x] Executor  
- [x] Toolbox  
- [ ] ExecutionResult  
- [ ] StateManager  
- [ ] Runtime Engine  
- [ ] LLM-based Planner  

---

## Design Principles

- Clear separation of responsibilities between components ensures modularity and maintainability.
- The **Planner** decides what actions to take; the **Executor** performs those actions.
- The **Toolbox** serves as the central registry and access point for all runtime tools.
- The runtime evolves through explicit state transitions, enabling flexible and iterative workflows.

---

This project demonstrates a professional approach to building an extensible AI Runtime suitable for enterprise applications and advanced AI system architectures.