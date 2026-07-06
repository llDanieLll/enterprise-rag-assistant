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

    # ChromaDB returns nested lists for each requested field.
    documents = results.get("documents", [])
    metadatas = results.get("metadatas", [])
    distances = results.get("distances", [])

    if not documents:
        return []

    print("=" * 80)
    print("Retrieved Results")
    print("=" * 80)

    metadata_list = metadatas[0] if metadatas else [None] * len(documents[0])
    distance_list = distances[0] if distances else [None] * len(documents[0])

    for doc, meta, dist in zip(documents[0], metadata_list, distance_list):
        if dist is not None:
            print(f"Distance : {dist:.4f}")
        else:
            print("Distance : N/A")

        filename = meta.get("filename", "Unknown") if meta else "Unknown"
        print(f"Filename : {filename}")
        print("-" * 60)
        print(doc)
        print("=" * 80)

    return documents[0]
