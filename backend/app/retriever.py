from app.embeddings import generate_embedding
from app.vector_store import search


def retrieve(question: str, top_k: int = 3) -> list[str]:
    """
    Retrieve the most relevant document chunks for a user's question.

    Args:
        question: The user's question.
        top_k: The maximum number of chunks to retrieve.

    Returns:
        A list of the most relevant document chunks.
    """

    # Convert the question into an embedding vector.
    query_embedding = generate_embedding(question)

    # Search the vector database.
    results = search(query_embedding, top_k)

    # ChromaDB returns documents as a nested list.
    documents = results.get("documents", [])

    if not documents:
        return []

    return documents[0]
