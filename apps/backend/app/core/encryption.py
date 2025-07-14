import base64
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_key() -> str:
    """Generate a new 256-bit key and return as base64 string."""
    key = AESGCM.generate_key(bit_length=256)
    return base64.b64encode(key).decode()

def encrypt(plaintext: str, base64_key: str) -> dict:
    """
    Encrypt plaintext using AES-GCM.
    Returns: dict with base64 ciphertext, nonce, and tag (tag is included in ciphertext).
    """
    key = base64.b64decode(base64_key)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return {
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "nonce": base64.b64encode(nonce).decode()
    }

def decrypt(base64_ciphertext: str, base64_nonce: str, base64_key: str) -> str:
    """
    Decrypt base64-encoded AES-GCM encrypted text.
    """
    key = base64.b64decode(base64_key)
    nonce = base64.b64decode(base64_nonce)
    ciphertext = base64.b64decode(base64_ciphertext)
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode()
