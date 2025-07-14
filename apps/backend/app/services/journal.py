from app.models.journal import JournalEntry
from app.db.session import SessionLocal
from datetime import datetime

def create_journal_entry(data, user):
    db = SessionLocal()
    entry = JournalEntry(content=data.content, created_at=str(datetime.utcnow()), user_id=user.id)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_user_journals(user):
    db = SessionLocal()
    return db.query(JournalEntry).filter(JournalEntry.user_id == user.id).all()