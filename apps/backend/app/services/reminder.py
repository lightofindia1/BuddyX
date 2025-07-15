from app.models.reminder import Reminder
from app.db.session import SessionLocal

def create_reminder(data, user, event_id=None, todo_id=None):
    db = SessionLocal()
    reminder = Reminder(
        remind_at=data.remind_at,
        message=data.message,
        user_id=user.id,
        event_id=event_id,
        todo_id=todo_id
    )
    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return reminder

def update_reminder(reminder_id, data, user):
    db = SessionLocal()
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id, Reminder.user_id == user.id).first()
    if not reminder:
        return None
    reminder.remind_at = data.remind_at
    reminder.message = data.message
    db.commit()
    db.refresh(reminder)
    return reminder

def delete_reminder(reminder_id, user):
    db = SessionLocal()
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id, Reminder.user_id == user.id).first()
    if not reminder:
        return False
    db.delete(reminder)
    db.commit()
    return True

def get_user_reminders(user):
    db = SessionLocal()
    return db.query(Reminder).filter(Reminder.user_id == user.id).all()

def get_reminder(reminder_id, user):
    db = SessionLocal()
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id, Reminder.user_id == user.id).first()
    return reminder

def search_reminders(user, date=None, event_id=None, message=None):
    db = SessionLocal()
    query = db.query(Reminder).filter(Reminder.user_id == user.id)
    if date:
        query = query.filter(Reminder.remind_at == date)
    if event_id:
        query = query.filter(Reminder.event_id == event_id)
    if message:
        query = query.filter(Reminder.message.ilike(f"%{message}%"))
    return query.all() 