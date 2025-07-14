from passlib.hash import argon2
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, Dict

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# --- Password Hashing ---

def hash_password(password: str) -> str:
    """Hash the password using Argon2."""
    return argon2.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """Verify password against the Argon2 hash."""
    return argon2.verify(password, hashed)

# --- JWT Token Handling ---

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Optional[Dict]:
    """Decode and validate the JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
