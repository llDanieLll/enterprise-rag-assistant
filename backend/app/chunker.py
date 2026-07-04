from typing import List


def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
    """
    Split a long string into fixed-size chunks.

    Args:
        text: The extracted document text.
        chunk_size: Maximum number of characters in each chunk.

    Returns:
        A list of text chunks.
    """

    text = text.strip()

    if not text:
        return []

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size].strip()

        if chunk:
            chunks.append(chunk)

    return chunks