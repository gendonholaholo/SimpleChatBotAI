import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "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")

LANGSMITH_PROJECT_NAME = "AI Chatbot Sederhana"

CHATBOT_NAME = "SimpleAI"
DEFAULT_RESPONSE = "Maaf, saya tidak mengerti pertanyaan Anda."

print("Konfigurasi berhasil dimuat.")
