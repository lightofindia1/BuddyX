# 🧠 BuddyX - Architecture and Tech Stack

## 🏗️ System Architecture

```
                   +----------------------+
                   |    Frontend (Next.js)|
                   |  - Web/Desktop/Mobile|
                   +----------+-----------+
                              |
                HTTPS + JWT   |
                              v
                   +----------+-----------+
                   |   FastAPI Backend    |
                   |  - Auth              |
                   |  - Vault             |
                   |  - Journal           |
                   |  - Calendar          |
                   |  - Files             |
                   |  - Email             |
                   +----+-------------+---+
                        |             |
           SQLAlchemy   |             | AES Encryption
                        v             v
               +--------+-----+   +---+-------------+
               |  PostgreSQL  |   |  Local or Cloud |
               |  Encrypted   |   |   File Storage  |
               |   Database   |   +-----------------+
               +--------------+
```

---

## 🧰 Tech Stack

### 🖥️ Frontend

- **Framework**: Next.js (React-based)
- **Language**: TypeScript
- **UI Framework**: Tailwind CSS
- **State Management**: Redux Toolkit
- **Platform Targeting**: 
  - Desktop: via Electron
  - Mobile: via Expo

---

### ⚙️ Backend

- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Auth**: JWT via `python-jose`
- **ORM**: SQLAlchemy (with Alembic)
- **Password Hashing**: `passlib[bcrypt]`
- **Encryption**: AES-GCM via `cryptography`
- **Containerization**: Docker

---

### 🗄️ Database

- **Primary DB**: PostgreSQL (or SQLite for local)
- **ORM Migrations**: Alembic

**Schema Models:**
- `User` (hashed password)
- `VaultEntry` (AES-encrypted, per user)
- `JournalEntry`
- `CalendarEvent`
- `FileEntry`
- `EmailEntry`

---

### 🔒 Security

- Per-user data isolation using `user_id`
- JWT auth with expiry + user claims
- AES-GCM encrypted fields
- Passwords hashed using bcrypt
- Secret keys via environment variables
- CORS policy enabled
- Swagger disabled in production

---

### 🧪 Testing

- **Unit Tests**: pytest
- **API Tests**: Postman
- **Security Linting**: `bandit`, `pip-audit`
