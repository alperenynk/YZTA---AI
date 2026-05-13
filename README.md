# 🤖 AI Customer Support Chatbot (FastAPI + Gemini)

This project is a simple **customer support chatbot system** built with FastAPI backend and Google Gemini AI.

A minimal HTML/CSS/JS frontend chat UI is included.

---

## 🚀 Features

- 💬 Chat-style customer support UI
- 🤖 Google Gemini AI integration
- 📦 Order tracking system
- 📊 Simple stock API endpoint
- ⚡ FastAPI backend
- 🌐 CORS-enabled frontend connection

---

## 🧠 Project Structure

```
project/
│
├── main.py
├── requirements.txt
├── .env
│
└── index.html
```

---

## ⚙️ Installation

### 1. Clone repo

```bash
git clone https://github.com/alperenynk/YZTA---AI.git
cd YZTA---AI
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run backend

```bash
uvicorn main:app --reload
```

Backend:
http://127.0.0.1:8000

---

## 🌐 Frontend

Open:
```
index.html
```

or use Live Server.

---

## 📡 API Endpoints

### GET /
Returns server status

### GET /stocks
Returns stock data

### POST /ask-ai
Chat with AI

Example:
```json
{
  "message": "128 order status?"
}
```

---

## 🧾 Example Orders

- 1 → Shipped
- 2 → Delivered
- 128 → Shipped (tomorrow delivery)
- 129 → Preparing

---

## 🛠 Tech Stack

- FastAPI
- Google Gemini AI (google-genai)
- HTML / CSS / JS
- Python

---