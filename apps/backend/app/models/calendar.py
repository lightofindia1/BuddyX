from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class CalendarEvent(Base):
    __tablename__ = "calendarevent"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(DateTime)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="calendar_events")
    reminders = relationship("Reminder", back_populates="event")