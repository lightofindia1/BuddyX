"""SQLAlchemy model for Reminder items."""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Reminder(Base):
    __tablename__ = "reminder"

    id = Column(Integer, primary_key=True, index=True)
    remind_at = Column(DateTime, nullable=False)
    message = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    event_id = Column(Integer, ForeignKey("calendarevent.id"), nullable=True)
    todo_id = Column(Integer, ForeignKey("todo.id"), nullable=True)

    user = relationship("User", back_populates="reminders")
    event = relationship("CalendarEvent", back_populates="reminders")
    todo = relationship("Todo", back_populates="reminders") 