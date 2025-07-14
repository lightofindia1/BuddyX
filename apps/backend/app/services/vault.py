from app.models.vault import VaultEntry
from app.core.encryption import encrypt, decrypt
from app.db.session import SessionLocal

KEY = "<your_base64_key>"

def create_vault_entry(data, user):
    db = SessionLocal()
    enc = encrypt(data.encrypted_data, KEY)
    entry = VaultEntry(title=data.title, encrypted_data=enc["ciphertext"], nonce=enc["nonce"], user_id=user.id)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_user_vault_entries(user):
    db = SessionLocal()
    return db.query(VaultEntry).filter(VaultEntry.user_id == user.id).all()
