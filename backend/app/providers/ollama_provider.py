

"""Ollama chat provider.

This provider implements the ChatProvider interface using a locally running
Ollama server. It can be used with models such as Qwen2.5:3B.
"""

from ollama import chat

from app.providers.base import ChatProvider


class OllamaProvider(ChatProvider):
    """Chat provider backed by a local Ollama model."""

    def chat(
        self,
        message: str,
        context: list[str] | None = None,
        model: str | None = None,
        **kwargs,
    ) -> dict:
        """Generate a response using Ollama."""

        model_name = model or "qwen2.5:3b"

        prompt = message
        if context:
            prompt = (
                "Use the following context to answer the user's question.\n\n"
                f"Context:\n{'\n'.join(context)}\n\n"
                f"Question:\n{message}"
            )

        response = chat(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return {
            "message": response["message"]["content"],
            "model": model_name,
        }