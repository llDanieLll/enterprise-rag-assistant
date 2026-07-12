

"""Smoke test for the OllamaProvider.

Run this script manually to verify that:
1. The Ollama server is running.
2. The local Qwen model is available.
3. The ChatProvider abstraction works correctly.
"""

from app.providers.ollama_provider import OllamaProvider


provider = OllamaProvider()


print("=" * 60)
print("Ollama Provider Smoke Test")
print("=" * 60)

try:
    result = provider.chat(
        message="What is 2 + 2? Answer in one short sentence.",
    )

    print("\nProvider Response")
    print("-" * 60)
    print(f"Model   : {result['model']}")
    print(f"Message : {result['message']}")
    print("\nSmoke test PASSED.")

except Exception as exc:
    print("\nSmoke test FAILED.")
    print(f"Exception: {type(exc).__name__}")
    print(exc)