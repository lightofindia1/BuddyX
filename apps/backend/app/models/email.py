from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class EmailMessage(Base):
    __tablename__ = "emailmessage"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    body = Column(Text)
    from_addr = Column(String)
    to_addr = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="email_messages")