# AI Chatbot Sederhana dengan LangChain, LangGraph, LangSmith, dan Groq API

## Deskripsi Proyek
Proyek ini adalah chatbot sederhana yang menggunakan **Groq API** untuk memberikan respons berdasarkan pertanyaan pengguna. Sistem ini dibangun dengan:

- **LangChain** untuk menangani logika chatbot.
- **LangGraph** untuk percakapan bercabang.
- **LangSmith** untuk debugging dan logging.
- **Groq API** sebagai engine LLM.

## Struktur Direktori
```
ai-chatbot/
│── main.py               # Entry point aplikasi
│── config.py             # Konfigurasi API dan token
│── chat_logic.py         # Logika chatbot
│── langsmith_logger.py   # Logging & monitoring
│── requirements.txt      # Dependensi proyek
│── README.md             # Dokumentasi proyek
```

## Instalasi
1. Clone repository ini.
2. Install dependensi dengan:
   ```pwsh
   pip install -r requirements.txt
   ```
3. Setel API Key dalam environment variables:
   ```pwsh
   export GROQ_API_KEY="your-groq-api-key"
   export LANGSMITH_API_KEY="your-langsmith-api-key"
   ```
4. Jalankan chatbot:
   ```pwsh
   python main.py
   ```

## Penggunaan
- Ketik pertanyaan atau perintah.
- Ketik `exit`, `keluar`, atau `quit` untuk keluar dari chatbot.

## Lisensi
~Mas Gendon
