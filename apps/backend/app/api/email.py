from fastapi import APIRouter, Depends
from app.schemas.email import EmailMessageIn
from app.services.email import send_email, get_user_emails
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/email", tags=["Email"])

@router.post("/")
def send(msg: EmailMessageIn, current_user: User = Depends(get_current_user)):
    return send_email(msg, current_user)

@router.get("/")
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_emails(current_user)
