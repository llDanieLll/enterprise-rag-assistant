import ollama

from app.retriever import retrieve


MODEL_NAME = "qwen2.5:0.5b"


def build_prompt(question: str, context_chunks: list[str]) -> str:
    """
    Build the prompt sent to the LLM.
    """

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the information provided in the context.

If the answer cannot be found in the context, say:
"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt.strip()



def generate_answer(question: str) -> str:
    """
    Retrieve relevant document chunks and generate an answer.
    """

    context_chunks = retrieve(question)

    prompt = build_prompt(question, context_chunks)

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



def stream_answer(question: str):
    """
    Retrieve relevant document chunks and stream the LLM response.
    """

    context_chunks = retrieve(question)

    prompt = build_prompt(question, context_chunks)

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