import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

if not GROQ_API_KEY or not LANGSMITH_API_KEY:
    raise ValueError("Harap setel GROQ_API_KEY dan LANGSMITH_API_KEY di file .env!")

LANGSMITH_PROJECT_NAME = "AI Chatbot Sederhana"

CHATBOT_NAME = "SimpleAI"
DEFAULT_RESPONSE = "Maaf, saya tidak mengerti pertanyaan Anda."

print("Konfigurasi berhasil dimuat.")
