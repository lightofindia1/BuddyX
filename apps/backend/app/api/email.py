from fastapi import APIRouter, Depends, Path, Body, Request
from app.schemas.email import EmailAccountIn, EmailAccountOut, EmailMessageIn, EmailMessageOut
from app.services.email import (
    create_email_account, get_user_email_accounts,
    create_email_message, get_user_emails
)
from app.core.deps import get_current_user
from app.models.user import User
from typing import List
from app.core.limiter import limiter

router = APIRouter(prefix="/email", tags=["Email"])

# EmailAccount endpoints
@router.post("/accounts/", response_model=EmailAccountOut)
def create_account(account: EmailAccountIn, current_user: User = Depends(get_current_user)):
    return create_email_account(account, current_user)

@router.get("/accounts/", response_model=List[EmailAccountOut])
def list_accounts(current_user: User = Depends(get_current_user)):
    return get_user_email_accounts(current_user)

# EmailMessage endpoints
@router.post("/messages/", response_model=EmailMessageOut)
def create_message(msg: EmailMessageIn, current_user: User = Depends(get_current_user)):
    return create_email_message(msg, current_user)

@router.get("/messages/", response_model=List[EmailMessageOut])
@limiter.limit("100/minute")
def list_messages(request: Request, current_user: User = Depends(get_current_user)):
    return get_user_emails(current_user)
