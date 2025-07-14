# BuddyX - Personal Secure Assistant

BuddyX is a personal assistant that handles:
- Vault (Passwords, Secure Notes)
- Journal
- Calendar (Reminders, Birthdays)
- Email Manager
- File Vault

Built using **Python FastAPI + SQLAlchemy** with AES encryption and JWT-based authentication.

## Features
- 🔐 Secure user-based data storage
- 📦 Encrypted storage (AES-GCM)
- 🛡️ JWT Authentication (per-user isolation)
- 🧠 Fully modular services (vault, journal, calendar, etc.)
- 🖥️ Built for cross-platform frontend (Next.js)

---

## Getting Started

1. Clone the repo
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variables (see `.env.example`)
5. Initialize DB: `python app/db/init_db.py`
6. Run backend: `uvicorn main:app --reload`

---

## API Documentation

Available at `/docs` (Swagger) or `/redoc` (ReDoc).

---

## Security

- 🔐 AES-GCM encryption of sensitive fields
- 🧾 JWT access control on all routes
- 🛡️ Passwords stored hashed using bcrypt
- 🌍 CORS policy configurable for frontend origin

---

## Deployment

Supports Docker, render.com, fly.io, or local deployment.

---

## License

MIT License