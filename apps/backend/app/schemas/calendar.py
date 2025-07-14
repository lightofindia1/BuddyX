from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.schemas.reminder import ReminderCreate, ReminderOut

class CalendarEventBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: datetime

class CalendarEventIn(CalendarEventBase):
    reminders: Optional[List[ReminderCreate]] = None

class CalendarEventOut(CalendarEventBase):
    id: int
    created_at: Optional[datetime] = None
    reminders: List[ReminderOut] = []

    class Config:
        orm_mode = True
