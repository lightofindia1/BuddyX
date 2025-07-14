import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_aes_gcm(data: bytes, key: bytes) -> dict:
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return {
        'ciphertext': base64.b64encode(ciphertext).decode(),
        'nonce': base64.b64encode(cipher.nonce).decode(),
        'tag': base64.b64encode(tag).decode()
    }

def decrypt_aes_gcm(encrypted: dict, key: bytes) -> bytes:
    nonce = base64.b64decode(encrypted['nonce'])
    ciphertext = base64.b64decode(encrypted['ciphertext'])
    tag = base64.b64decode(encrypted['tag'])
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
