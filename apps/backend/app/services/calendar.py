from app.models.calendar import CalendarEvent
from app.models.reminder import Reminder
from app.db.session import SessionLocal

def create_event(data, user):
    db = SessionLocal()
    event = CalendarEvent(title=data.title, date=data.date, description=data.description, user_id=user.id)
    db.add(event)
    db.commit()
    db.refresh(event)
    # Handle nested reminders
    if hasattr(data, 'reminders') and data.reminders:
        for reminder_data in data.reminders:
            reminder = Reminder(
                remind_at=reminder_data.remind_at,
                message=reminder_data.message,
                user_id=user.id,
                event_id=event.id
            )
            db.add(reminder)
        db.commit()
    db.refresh(event)
    return event

def get_user_events(user):
    db = SessionLocal()
    return db.query(CalendarEvent).filter(CalendarEvent.user_id == user.id).all()

def get_event(event_id, user):
    db = SessionLocal()
    event = db.query(CalendarEvent).filter(CalendarEvent.id == event_id, CalendarEvent.user_id == user.id).first()
    return event

def update_event(event_id, data, user):
    db = SessionLocal()
    event = db.query(CalendarEvent).filter(CalendarEvent.id == event_id, CalendarEvent.user_id == user.id).first()
    if not event:
        return None
    if hasattr(data, 'title'):
        event.title = data.title
    if hasattr(data, 'date'):
        event.date = data.date
    if hasattr(data, 'description'):
        event.description = data.description
    db.commit()
    db.refresh(event)
    return event

def delete_event(event_id, user):
    db = SessionLocal()
    event = db.query(CalendarEvent).filter(CalendarEvent.id == event_id, CalendarEvent.user_id == user.id).first()
    if not event:
        return False
    db.delete(event)
    db.commit()
    return True

def search_events(user, date=None, title=None):
    db = SessionLocal()
    query = db.query(CalendarEvent).filter(CalendarEvent.user_id == user.id)
    if date:
        query = query.filter(CalendarEvent.date == date)
    if title:
        query = query.filter(CalendarEvent.title.ilike(f"%{title}%"))
    return query.all()