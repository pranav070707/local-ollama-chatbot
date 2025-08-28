# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

MODEL = "gemma:2b-instruct"

class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []  # [{role: "user"/"assistant"/"system", content: "..."}]

@app.post("/chat")
def chat(req: ChatRequest):
    # start with a gentle system prompt
    messages = [{"role": "system", "content": "You are a concise, helpful assistant."}]
    messages += req.history
    messages.append({"role": "user", "content": req.message})

    out = ollama.chat(model=MODEL, messages=messages)
    reply = out["message"]["content"]

    # return new turn to append on the client side
    return {"reply": reply}
