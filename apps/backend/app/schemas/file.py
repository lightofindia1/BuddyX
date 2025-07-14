from pydantic import BaseModel
from datetime import datetime

class FileEntryBase(BaseModel):
    filename: str
    encrypted_blob: bytes

class FileEntryIn(FileEntryBase):
    pass

class FileEntryOut(FileEntryBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True
