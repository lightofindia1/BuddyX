from fastapi import APIRouter, Depends
from app.schemas.journal import JournalEntryIn
from app.services.journal import create_journal_entry, get_user_journals
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/journal", tags=["Journal"])

@router.post("/")
def create(entry: JournalEntryIn, current_user: User = Depends(get_current_user)):
    return create_journal_entry(entry, current_user)

@router.get("/")
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_journals(current_user)
