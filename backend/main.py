from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os
import re

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

orders = {
    1: {
        "status": "Kargoya verildi",
        "eta": "Yarın teslim"
    },
    2: {
        "status": "Teslim edildi",
        "eta": "Teslim edildi"
    },
    128: {
        "status": "Kargoya verildi",
        "eta": "Yarın teslim"
    },
    129: {
        "status": "Hazırlanıyor",
        "eta": "2 gün içinde"
    }
}

stocks = [
    {"name": "Kahve", "stock": 3},
    {"name": "Çay", "stock": 25}
]

class Message(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "AI Sipariş Asistanı çalışıyor"}


@app.get("/stocks")
def get_stocks():
    return stocks


@app.post("/ask-ai")
def ask_ai(data: Message):
    try:
        message = data.message

        numbers = re.findall(r"\d+", message)

        if not numbers:
            return {"response": "Lütfen sipariş numarası belirtin."}

        order_id = int(numbers[0])

        if order_id not in orders:
            return {"response": "Sipariş bulunamadı."}

        order = orders[order_id]

        prompt = f"""
Kullanıcı mesajı:
{message}

Sipariş bilgisi:
{order}

Sen bir müşteri destek asistanısın.
"""

        response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=prompt
)

        return {
            "response": str(response.text),
            "order": order
        }

    except Exception as e:
        return {"error": str(e)}