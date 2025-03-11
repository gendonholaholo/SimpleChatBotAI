from config import GROQ_API_KEY, DEFAULT_RESPONSE
import groq
from typing import Dict, Any
from langgraph.graph import StateGraph

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY tidak ditemukan! Pastikan telah diatur dalam file .env.")

groq_client = groq.Client(api_key=GROQ_API_KEY)

def handle_user_input(state: Dict[str, Any]) -> Dict[str, Any]:
    """Memproses input user dan mengirimkan ke model AI"""
    try:
        response = groq_client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": state["user_input"]}]
        )
        chatbot_response = (
            response.choices[0].message.content if response and response.choices else DEFAULT_RESPONSE
        ) or DEFAULT_RESPONSE
    except Exception as e:
        chatbot_response = f"Terjadi kesalahan: {str(e)}"
    
    return {"user_input": state["user_input"], "chatbot_response": chatbot_response}

workflow = StateGraph(Dict[str, Any])
workflow.add_node("handle_user_input", handle_user_input)
workflow.set_entry_point("handle_user_input")
executor = workflow.compile()

def chatbot_response(user_input: str) -> str:
    """Mengembalikan respons dari chatbot berdasarkan input user"""
    result = executor.invoke({"user_input": user_input})
    return result.get("chatbot_response", DEFAULT_RESPONSE)

if __name__ == "__main__":
    print(chatbot_response("Halo!"))
