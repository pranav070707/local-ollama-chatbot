
import ollama

MODEL = "gemma:2b-instruct"  # or "mistral:instruct"
history = [{"role": "system", "content": "You are a helpful assistant."}]

print("Local Chatbot. Type 'exit' to quit.\n")
while True:
    user = input("You: ")
    if user.strip().lower() == "exit":
        break
    history.append({"role": "user", "content": user})
    resp = ollama.chat(model=MODEL, messages=history)
    reply = resp["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    print("Bot:", reply, "\n")
