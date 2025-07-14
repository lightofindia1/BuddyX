from fastapi import APIRouter, Depends
from app.schemas.calendar import CalendarEventIn, CalendarEventOut
from app.services.calendar import create_event, get_user_events
from app.core.deps import get_current_user
from app.models.user import User
from typing import List

router = APIRouter(prefix="/calendar", tags=["Calendar"])

@router.post("/", response_model=CalendarEventOut)
def create(event: CalendarEventIn, current_user: User = Depends(get_current_user)):
    return create_event(event, current_user)

@router.get("/", response_model=List[CalendarEventOut])
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_events(current_user)
