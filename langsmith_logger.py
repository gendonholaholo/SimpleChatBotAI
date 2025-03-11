import logging
import os

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY", "your-langsmith-api-key")
LANGSMITH_PROJECT_NAME = "AI Chatbot Sederhana"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("chatbot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def log_interaction(user_input, chatbot_response):
    """Mencatat interaksi chatbot ke dalam log."""
    try:
        logging.info(f"User: {user_input}")
        logging.info(f"Chatbot: {chatbot_response}")
    except UnicodeEncodeError:
        logging.info(f"Chatbot: [RESPONS TIDAK DAPAT DICETAK - MENGANDUNG KARAKTER KHUSUS]")

if __name__ == "__main__":
    log_interaction("Halo", "Hai! Apa yang bisa saya bantu?")
