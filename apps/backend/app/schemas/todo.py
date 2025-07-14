from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.schemas.reminder import ReminderCreate, ReminderOut

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: bool = False

class TodoCreate(TodoBase):
    reminders: Optional[List[ReminderCreate]] = None

class TodoOut(TodoBase):
    id: int
    reminders: List[ReminderOut] = []

    class Config:
        orm_mode = True 