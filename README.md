# 🏗 Engineering Sprint API – System Architecture

## 🔷 1. High-Level Architecture

Client (Browser / Postman)
        ↓
FastAPI Application
        ↓
Business Logic Layer
        ↓
Database (SQLite)
        ↓
External AI Service (OpenAI API)

---

## 🔷 2. Architecture Components

### 1️⃣ Client Layer
- Browser / Postman
- Sends HTTP requests (GET, POST)
- Receives JSON responses

### 2️⃣ API Layer
Built using FastAPI.

Responsibilities:
- Route handling
- Request validation
- Response formatting
- Error handling

Example Endpoints:
- POST /generate
- GET /items

### 3️⃣ Business Logic Layer
- Processes incoming data
- Handles OpenAI API calls
- Applies application rules
- Controls database operations

### 4️⃣ Database Layer
- SQLite database
- Stores generated data
- Managed via ORM / SQL queries

### 5️⃣ External Integration
- OpenAI API for AI-based text generation
- API key secured using .env file

---

## 🔷 3. Data Flow

1. User sends request
2. FastAPI validates input
3. Business logic processes data
4. (Optional) OpenAI API is called
5. Result stored in SQLite
6. JSON response returned to client

---

## 🔷 4. Security Design

- Environment variables stored in `.env`
- SECRET_KEY protected
- OPENAI_KEY not exposed
- Input validation using Pydantic models
- Database not publicly exposed

---

## 🔷 5. Project Structure

engineering_sprint_api/
│
├── app/
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│
├── main.py
├── requirements.txt
├── README.md
└── .env (excluded from GitHub)

---

## 🔷 6. Technology Stack

- Python
- FastAPI
- SQLite
- OpenAI API
- Uvicorn
