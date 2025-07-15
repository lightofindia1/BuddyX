from pydantic import BaseModel
from datetime import date

class JournalEntryIn(BaseModel):
    date: date
    content: str

class JournalEntryOut(BaseModel):
    id: int
    date: date
    content: str

    class Config:
        orm_mode = True
