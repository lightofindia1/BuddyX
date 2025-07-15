from fastapi import APIRouter, Depends, HTTPException, Path, Query
from app.schemas.reminder import ReminderCreate, ReminderOut
from app.services.reminder import create_reminder, update_reminder, delete_reminder, get_user_reminders, get_reminder, search_reminders
from app.core.deps import get_current_user
from app.models.user import User
from typing import List

router = APIRouter(prefix="/reminder", tags=["Reminder"])

@router.post("/", response_model=ReminderOut)
def create(reminder: ReminderCreate, event_id: int = None, todo_id: int = None, current_user: User = Depends(get_current_user)):
    return create_reminder(reminder, current_user, event_id=event_id, todo_id=todo_id)

@router.put("/{reminder_id}", response_model=ReminderOut)
def update(reminder_id: int, reminder: ReminderCreate, current_user: User = Depends(get_current_user)):
    updated = update_reminder(reminder_id, reminder, current_user)
    if not updated:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return updated

@router.delete("/{reminder_id}")
def delete(reminder_id: int, current_user: User = Depends(get_current_user)):
    deleted = delete_reminder(reminder_id, current_user)
    if not deleted:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return {"ok": True}

@router.get("/", response_model=List[ReminderOut])
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_reminders(current_user)

@router.get("/{reminder_id}", response_model=ReminderOut)
def get_one(reminder_id: int = Path(...), current_user: User = Depends(get_current_user)):
    reminder = get_reminder(reminder_id, current_user)
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return reminder

@router.get("/search", response_model=List[ReminderOut])
def search(
    date: str = Query(None),
    event_id: int = Query(None),
    message: str = Query(None),
    current_user: User = Depends(get_current_user)
):
    return search_reminders(current_user, date, event_id, message) 