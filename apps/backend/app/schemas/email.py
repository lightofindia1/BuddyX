from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime

class EmailAccountIn(BaseModel):
    provider: str
    email_address: str
    display_name: Optional[str] = None
    access_token: Optional[str] = None  # Provided by client, encrypted in service
    refresh_token: Optional[str] = None
    token_expiry: Optional[datetime] = None
    settings: Optional[Any] = None  # JSON/dict

class EmailAccountOut(BaseModel):
    id: int
    provider: str
    email_address: str
    display_name: Optional[str] = None
    token_expiry: Optional[datetime] = None
    settings: Optional[Any] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    class Config:
        orm_mode = True

class EmailMessageIn(BaseModel):
    email_account_id: int
    message_id: Optional[str] = None
    thread_id: Optional[str] = None
    subject: Optional[str] = None
    body_plain: Optional[str] = None
    body_html: Optional[str] = None
    from_addr: Optional[str] = None
    to_addrs: Optional[List[str]] = None
    cc_addrs: Optional[List[str]] = None
    bcc_addrs: Optional[List[str]] = None
    reply_to: Optional[str] = None
    attachments: Optional[List[Any]] = None  # List of attachment metadata
    date_sent: Optional[datetime] = None
    date_received: Optional[datetime] = None
    folder: Optional[str] = None
    is_read: Optional[bool] = False
    is_starred: Optional[bool] = False
    is_important: Optional[bool] = False

class EmailMessageOut(EmailMessageIn):
    id: int
    class Config:
        orm_mode = True
