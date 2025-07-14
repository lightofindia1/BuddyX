# BuddyX Environment Variables

| Key                | Required | Description                                |
|--------------------|----------|--------------------------------------------|
| SECRET_KEY         | ✅        | JWT signing key (any strong random string) |
| ENCRYPTION_KEY     | ✅        | 32-byte base64 AES key                     |
| DATABASE_URL       | ✅        | SQLAlchemy DB URL                          |
| ACCESS_TOKEN_EXPIRE_MINUTES | ❌ | Defaults to 60                            |

### .env.example

```
SECRET_KEY=super-secret-key
ENCRYPTION_KEY=<32-byte-base64-key>
DATABASE_URL=sqlite:///./buddyx.db
ACCESS_TOKEN_EXPIRE_MINUTES=60
```