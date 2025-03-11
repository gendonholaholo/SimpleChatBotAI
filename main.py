from chat_logic import chatbot_response
from langsmith_logger import log_interaction

def main():
    print("Selamat datang di SimpleAI Chatbot (dengan LangGraph)!")
    
    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["exit", "keluar", "quit"]:
            print("Chatbot: Terima kasih telah menggunakan SimpleAI. Sampai jumpa!")
            break

        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

        log_interaction(user_input, response)

if __name__ == "__main__":
    main()
