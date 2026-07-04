import ollama  # type: ignore


def generate_embedding(text: str | list[str]) -> list[float] | list[list[float]]:
    """
    Generate embedding vectors.

    Args:
        text: Either a single string or a list of strings.

    Returns:
        - If the input is a single string, returns one embedding vector.
        - If the input is a list of strings, returns one embedding vector per string.
    """

    response = ollama.embed(
        model="nomic-embed-text",
        input=text,
    )

    if isinstance(text, str):
        return response["embeddings"][0]

    return response["embeddings"]