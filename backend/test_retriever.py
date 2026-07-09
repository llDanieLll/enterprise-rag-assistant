from app.rag.retriever import retrieve

question = "What is this certificate about?"

chunks = retrieve(question)

print("=" * 60)

print("Retrieved Chunks:\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}")
    print("-" * 40)
    print(chunk)
    print()

print("=" * 60)