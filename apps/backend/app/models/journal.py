from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class JournalEntry(Base):
    __tablename__ = "journalentry"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    created_at = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="journal_entries")