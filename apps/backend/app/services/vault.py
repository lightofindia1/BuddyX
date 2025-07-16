from app.models.vault import VaultEntry
from app.db.session import SessionLocal
from app.core.encryption import encrypt, decrypt
import json
import os

KEY = os.getenv("VAULT_ENCRYPTION_KEY")

def create_vault_entry(data, user):
    db = SessionLocal()
    to_encrypt = json.dumps({
        "title": data.title,
        "data": data.data
    })
    enc = encrypt(to_encrypt, KEY)
    entry = VaultEntry(encrypted_data=enc["ciphertext"], nonce=enc["nonce"], user_id=user.id)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_user_vault_entries(user):
    db = SessionLocal()
    entries = db.query(VaultEntry).filter(VaultEntry.user_id == user.id).all()
    result = []
    for entry in entries:
        dec = json.loads(decrypt(entry.encrypted_data, entry.nonce, KEY))
        dec["id"] = entry.id
        result.append(dec)
    return result

def get_vault_entry(vault_id, user):
    db = SessionLocal()
    entry = db.query(VaultEntry).filter(VaultEntry.id == vault_id, VaultEntry.user_id == user.id).first()
    return entry

def update_vault_entry(vault_id, data, user):
    db = SessionLocal()
    entry = db.query(VaultEntry).filter(VaultEntry.id == vault_id, VaultEntry.user_id == user.id).first()
    if not entry:
        return None
    if hasattr(data, 'title'):
        entry.title = data.title
    if hasattr(data, 'encrypted_data'):
        enc = encrypt(data.encrypted_data, KEY)
        entry.encrypted_data = enc["ciphertext"]
        entry.nonce = enc["nonce"]
    db.commit()
    db.refresh(entry)
    return entry

def rename_vault_entry(vault_id, new_title, user):
    db = SessionLocal()
    entry = db.query(VaultEntry).filter(VaultEntry.id == vault_id, VaultEntry.user_id == user.id).first()
    if not entry:
        return None
    entry.title = new_title
    db.commit()
    db.refresh(entry)
    return entry

def delete_vault_entry(vault_id, user):
    db = SessionLocal()
    entry = db.query(VaultEntry).filter(VaultEntry.id == vault_id, VaultEntry.user_id == user.id).first()
    if not entry:
        return False
    db.delete(entry)
    db.commit()
    return True

def batch_delete_vault_entries(vault_ids, user):
    db = SessionLocal()
    entries = db.query(VaultEntry).filter(VaultEntry.id.in_(vault_ids), VaultEntry.user_id == user.id).all()
    for entry in entries:
        db.delete(entry)
    db.commit()
    return {"deleted": [e.id for e in entries]}
