from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class EmailAccount(Base):
    __tablename__ = "emailaccount"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    provider = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    display_name = Column(String)
    encrypted_access_token = Column(String)
    encrypted_refresh_token = Column(String)
    token_expiry = Column(DateTime)
    settings = Column(String)  # JSON as string
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="email_accounts")
    messages = relationship("EmailMessage", back_populates="email_account")

class EmailMessage(Base):
    __tablename__ = "emailmessage"
    id = Column(Integer, primary_key=True, index=True)
    email_account_id = Column(Integer, ForeignKey("emailaccount.id"))
    message_id = Column(String)
    thread_id = Column(String)
    date_sent = Column(DateTime)
    date_received = Column(DateTime)
    folder = Column(String)
    is_read = Column(Boolean, default=False)
    is_starred = Column(Boolean, default=False)
    is_important = Column(Boolean, default=False)
    encrypted_content = Column(String, nullable=False)
    nonce = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="email_messages")
    email_account = relationship("EmailAccount", back_populates="messages")