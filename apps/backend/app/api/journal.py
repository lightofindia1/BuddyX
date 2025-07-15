from fastapi import APIRouter, Depends, Path, Body
from app.schemas.journal import JournalEntryIn, JournalEntryOut
from app.services.journal import (
    create_or_update_journal_entry, get_journal_entry, delete_journal_entry, list_journal_entries
)
from app.core.deps import get_current_user
from app.models.user import User
from typing import List
from datetime import date

router = APIRouter(prefix="/journal", tags=["Journal"])

@router.put("/{entry_date}", response_model=JournalEntryOut)
def create_or_update(entry_date: date = Path(...), data: JournalEntryIn = Body(...), current_user: User = Depends(get_current_user)):
    # Ensure the date in path and body match
    if data.date != entry_date:
        return {"error": "Date in path and body must match."}
    return create_or_update_journal_entry(data, current_user)

@router.get("/{entry_date}", response_model=JournalEntryOut)
def get_one(entry_date: date = Path(...), current_user: User = Depends(get_current_user)):
    entry = get_journal_entry(entry_date, current_user)
    if not entry:
        return {"error": "Journal entry not found or not owned by user."}
    return entry

@router.delete("/{entry_date}")
def delete(entry_date: date = Path(...), current_user: User = Depends(get_current_user)):
    result = delete_journal_entry(entry_date, current_user)
    if not result:
        return {"error": "Journal entry not found or not owned by user."}
    return {"deleted": str(entry_date)}

@router.get("/", response_model=List[JournalEntryOut])
def list_all(current_user: User = Depends(get_current_user)):
    return list_journal_entries(current_user)
