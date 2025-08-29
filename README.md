# Local Chatbot (Ollama and FastAPI)

## Prereqs
- Python 3.8+
- Install Ollama: https://ollama.ai/download
- Pull a model:
  - `ollama pull gemma:2b-instruct` (fastest on low-RAM)
  - or `ollama pull mistral:instruct`


## Run (CLI)
```bash
pip install ollama
python chatbot_cli.py
```

## Run (Web)
```
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

Open `index.html` in your browser and use the UI (it sends requests to http://127.0.0.1:8000/chat).
