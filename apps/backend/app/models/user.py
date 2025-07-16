from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    vault_entries = relationship("VaultEntry", back_populates="user")
    journal_entries = relationship("JournalEntry", back_populates="user")
    calendar_events = relationship("CalendarEvent", back_populates="user")
    file_entries = relationship("FileEntry", back_populates="user")
    email_accounts = relationship("EmailAccount", back_populates="user")
    email_messages = relationship("EmailMessage", back_populates="user")
    todos = relationship("Todo", back_populates="user")
    reminders = relationship("Reminder", back_populates="user")