import logging
import os
from dotenv import load_dotenv

load_dotenv()

LANGSMITH_PROJECT_NAME = "AI Chatbot Sederhana"

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
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
        logging.info("Chatbot: [RESPONS TIDAK DAPAT DICETAK - MENGANDUNG KARAKTER KHUSUS]")

if __name__ == "__main__":
    log_interaction("Halo", "Hai! Apa yang bisa saya bantu?")
