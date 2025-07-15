from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class FileEntryBase(BaseModel):
    filename: str
    is_folder: bool = False
    parent_id: Optional[int] = None
    size: Optional[int] = None
    file_type: Optional[str] = None

class FileEntryIn(FileEntryBase):
    encrypted_blob: Optional[bytes] = None  # Only for files, not folders

class FileEntryOut(FileEntryBase):
    id: int
    uploaded_at: Optional[datetime] = None
    children: Optional[List['FileEntryOut']] = None  # For folders

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

FileEntryOut.update_forward_refs()
