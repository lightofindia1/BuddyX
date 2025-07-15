from fastapi import APIRouter, Depends, Path, Body, Query
from app.schemas.calendar import CalendarEventIn, CalendarEventOut
from app.services.calendar import (
    create_event, get_user_events, get_event, update_event, delete_event, search_events
)
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

@router.get("/{event_id}", response_model=CalendarEventOut)
def get_one(event_id: int = Path(...), current_user: User = Depends(get_current_user)):
    event = get_event(event_id, current_user)
    if not event:
        return {"error": "Event not found or not owned by user."}
    return event

@router.put("/{event_id}", response_model=CalendarEventOut)
def update(event_id: int = Path(...), data: CalendarEventIn = Body(...), current_user: User = Depends(get_current_user)):
    event = update_event(event_id, data, current_user)
    if not event:
        return {"error": "Event not found or not owned by user."}
    return event

@router.delete("/{event_id}")
def delete(event_id: int = Path(...), current_user: User = Depends(get_current_user)):
    result = delete_event(event_id, current_user)
    if not result:
        return {"error": "Event not found or not owned by user."}
    return {"deleted": event_id}

@router.get("/search", response_model=List[CalendarEventOut])
def search(
    date: str = Query(None),
    title: str = Query(None),
    current_user: User = Depends(get_current_user)
):
    return search_events(current_user, date, title)
