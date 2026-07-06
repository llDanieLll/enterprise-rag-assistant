import ollama # type: ignore

from app.retriever import retrieve
from app.models import Message


MODEL_NAME = "qwen2.5:3b"


def build_prompt(
    question: str,
    context_chunks: list[str],
    history: list[Message],
) -> str:
    """
    Build the prompt sent to the LLM.
    """

    context = "\n\n".join(context_chunks)

    conversation = "\n".join(
        f"{message.role.capitalize()}: {message.content}"
        for message in history
    )

    prompt = f"""
You are a helpful AI assistant.

Use the conversation history to understand previous messages and resolve references such as "he", "she", "it", or "that".

Use the retrieved document context when answering questions about the uploaded documents.

If the answer cannot be found in either the conversation history or the retrieved document context, reply:
"I don't know based on the available information."

========================
Conversation History
========================
{conversation if conversation else 'None'}

========================
Document Context
========================
{context if context else 'None'}

========================
Current Question
========================
{question}

Answer:
"""

    return prompt.strip()



def generate_answer(
    question: str,
    history: list[Message],
) -> str:
    """
    Retrieve relevant document chunks and generate an answer.
    """

    context_chunks = retrieve(question)

    prompt = build_prompt(question, context_chunks, history)

    print("=" * 80)
    print("PROMPT SENT TO LLM")
    print("=" * 80)
    print(prompt)
    print("=" * 80)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]



def stream_answer(
    question: str,
    history: list[Message],
):
    """
    Retrieve relevant document chunks and stream the LLM response.
    """

    context_chunks = retrieve(question)

    prompt = build_prompt(question, context_chunks, history)

    print("=" * 80)
    print("PROMPT SENT TO LLM")
    print("=" * 80)
    print(prompt)
    print("=" * 80)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        stream=True,
    )

    for chunk in response:
        yield chunk["message"]["content"]