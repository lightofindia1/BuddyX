from pydantic import BaseModel
from datetime import datetime

class JournalEntryBase(BaseModel):
    title: str
    encrypted_content: str

class JournalEntryIn(JournalEntryBase):
    pass

class JournalEntryOut(JournalEntryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
