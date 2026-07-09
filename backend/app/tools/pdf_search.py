"""
pdf_search.py

The PDF Search tool is responsible only for retrieving relevant
chunks from the uploaded documents.

It does NOT call the LLM.
It simply returns observations for the Agent.
"""

from app.rag.retriever import retrieve


def pdf_search(question: str) -> dict:
    """
    Search the uploaded PDF documents.

    Args:
        question: The user's question.

    Returns:
        A standardized observation dictionary.
    """

    chunks = retrieve(question)

    return {
        "tool": "pdf_search",
        "success": True,
        "observation": chunks,
    }
