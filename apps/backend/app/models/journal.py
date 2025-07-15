from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class JournalEntry(Base):
    __tablename__ = "journalentry"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    encrypted_content = Column(String, nullable=False)
    nonce = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="journal_entries")
    __table_args__ = (UniqueConstraint('user_id', 'date', name='_user_date_uc'),)