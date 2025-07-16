from app.models.journal import JournalEntry
from app.db.session import SessionLocal
from app.core.encryption import encrypt, decrypt
from datetime import date as date_type
import os

KEY = os.getenv("JOURNAL_ENCRYPTION_KEY")

def create_or_update_journal_entry(data, user):
    db = SessionLocal()
    entry = db.query(JournalEntry).filter(JournalEntry.user_id == user.id, JournalEntry.date == data.date).first()
    enc = encrypt(data.content, KEY)
    if entry:
        entry.encrypted_content = enc["ciphertext"]
        entry.nonce = enc["nonce"]
    else:
        entry = JournalEntry(
            date=data.date,
            encrypted_content=enc["ciphertext"],
            nonce=enc["nonce"],
            user_id=user.id
        )
        db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_journal_entry(date, user):
    db = SessionLocal()
    entry = db.query(JournalEntry).filter(JournalEntry.user_id == user.id, JournalEntry.date == date).first()
    if not entry:
        return None
    dec = decrypt(entry.encrypted_content, entry.nonce, KEY)
    return {
        "id": entry.id,
        "date": entry.date,
        "content": dec
    }

def delete_journal_entry(date, user):
    db = SessionLocal()
    entry = db.query(JournalEntry).filter(JournalEntry.user_id == user.id, JournalEntry.date == date).first()
    if not entry:
        return False
    db.delete(entry)
    db.commit()
    return True

def list_journal_entries(user):
    db = SessionLocal()
    entries = db.query(JournalEntry).filter(JournalEntry.user_id == user.id).all()
    result = []
    for entry in entries:
        dec = decrypt(entry.encrypted_content, entry.nonce, KEY)
        result.append({
            "id": entry.id,
            "date": entry.date,
            "content": dec
        })
    return result