"""
web_search.py

The Web Search tool is responsible for retrieving information
from the Internet.

This is currently a placeholder implementation.
Later it will integrate a real search provider such as Tavily,
SerpAPI, or another web search API.
"""


def web_search(query: str) -> dict:
    """
    Search the web.

    Args:
        query: The user's search query.

    Returns:
        A standardized observation dictionary.
    """

    return {
        "tool": "web_search",
        "success": True,
        "observation": (
            "Web search is not implemented yet. "
            f"Requested query: {query}"
        ),
    }
