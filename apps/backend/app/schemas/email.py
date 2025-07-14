from pydantic import BaseModel
from datetime import datetime

class EmailMessageBase(BaseModel):
    subject: str
    encrypted_body: str
    sender: str
    receiver: str

class EmailMessageIn(EmailMessageBase):
    pass

class EmailMessageOut(EmailMessageBase):
    id: int
    sent_at: datetime

    class Config:
        orm_mode = True
