from app.rag import generate_answer

question = "What certificate did Jiahao Qiu receive?"

answer = generate_answer(question)

print("=" * 60)
print("Question:")
print(question)

print("\nAnswer:")
print(answer)
print("=" * 60)
