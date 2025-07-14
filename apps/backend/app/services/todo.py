from app.models.todo import Todo
from app.models.reminder import Reminder
from app.db.session import SessionLocal

def create_todo(data, user):
    db = SessionLocal()
    todo = Todo(
        title=data.title,
        description=data.description,
        due_date=data.due_date,
        completed=data.completed,
        user_id=user.id
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    # Handle nested reminders
    if hasattr(data, 'reminders') and data.reminders:
        for reminder_data in data.reminders:
            reminder = Reminder(
                remind_at=reminder_data.remind_at,
                message=reminder_data.message,
                user_id=user.id,
                todo_id=todo.id
            )
            db.add(reminder)
        db.commit()
    db.refresh(todo)
    return todo

def get_user_todos(user):
    db = SessionLocal()
    return db.query(Todo).filter(Todo.user_id == user.id).all() 