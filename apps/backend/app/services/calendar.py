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