

import chromadb
from chromadb.api.models.Collection import Collection

# Create a persistent ChromaDB client.
# The database files will be stored in backend/vector_store/
client = chromadb.PersistentClient(path="vector_store")

# Create (or retrieve if it already exists) the collection.
collection: Collection = client.get_or_create_collection(
    name="documents"
)


def add_documents(chunks: list[str], embeddings: list[list[float]]) -> None:
    """
    Store document chunks and their embeddings in ChromaDB.

    Args:
        chunks: List of text chunks.
        embeddings: Embedding vector for each chunk.
    """

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )



def search(query_embedding: list[float], top_k: int = 3):
    """
    Search the vector database for the most similar chunks.

    Args:
        query_embedding: Embedding vector of the user's question.
        top_k: Number of results to return.

    Returns:
        The ChromaDB query result.
    """

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )