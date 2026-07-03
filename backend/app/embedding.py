import ollama # type: ignore


def generate_embedding(text: str) -> list[float]:
    """
    Generate an embedding vector for a piece of text.

    Args:
        text: Input text.

    Returns:
        A list of floating-point numbers representing the embedding.
    """

    response = ollama.embed(
        model="nomic-embed-text",
        input=text
    )

    return response["embeddings"][0]