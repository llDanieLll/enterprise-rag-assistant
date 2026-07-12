

"""Base interface for chat providers.

A ChatProvider is responsible for generating a response from a language model.
The Executor depends only on this interface and does not know whether the
implementation uses Ollama, OpenAI, or another backend.
"""

from abc import ABC, abstractmethod
from typing import Any


class ChatProvider(ABC):
    """Abstract interface implemented by all chat providers."""

    @abstractmethod
    def chat(
        self,
        message: str,
        context: list[str] | None = None,
        model: str | None = None,
        **kwargs: Any,
    ) -> dict:
        """Generate a response from a language model.

        Args:
            message: The user's message.
            context: Optional retrieved context to include.
            model: Optional model identifier.
            **kwargs: Provider-specific options.

        Returns:
            A dictionary containing at least:
                {
                    "message": <assistant response>
                }
        """
        raise NotImplementedError