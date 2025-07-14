from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReminderBase(BaseModel):
    remind_at: datetime
    message: Optional[str] = None

class ReminderCreate(ReminderBase):
    pass

class ReminderOut(ReminderBase):
    id: int
    event_id: Optional[int] = None
    todo_id: Optional[int] = None

    class Config:
        orm_mode = True 