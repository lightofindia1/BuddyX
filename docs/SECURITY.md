# BuddyX Security Overview

## 🔐 Authentication

- JWT tokens (HS256)
- 60-minute expiry (configurable)
- Tokens stored on frontend in secure store

## 🔏 Encryption

- AES-GCM encryption for:
  - Vault data (passwords/notes)
  - Files (contents)
- Encryption key is base64 and stored in environment variables

## 🛡️ Password Management

- Passwords are hashed with `bcrypt`
- Salted and hashed using `passlib.hash.bcrypt`

## ✅ Secure API

- All sensitive endpoints require valid JWT
- User-specific data filtered by `user.id`
- No sensitive data exposed in root or unauthenticated routes

## 🧪 Validation

- Pydantic schema validation used for all input data
- No direct SQL execution (ORM prevents SQL Injection)
- File uploads restricted (if used)

## 🧰 Recommendations

- Use HTTPS in production
- Set a strong 32-byte base64 encryption key
- Secure environment variables and Docker secrets