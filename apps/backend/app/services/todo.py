from app.models.todo import Todo
from app.models.reminder import Reminder
from app.db.session import SessionLocal
from app.core.encryption import encrypt, decrypt
import json

def create_todo(data, user):
    db = SessionLocal()
    to_encrypt = json.dumps({
        "title": data.title,
        "description": data.description
    })
    enc = encrypt(to_encrypt, "<your_base64_key>")
    todo = Todo(
        encrypted_content=enc["ciphertext"],
        nonce=enc["nonce"],
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
    todos = db.query(Todo).filter(Todo.user_id == user.id).all()
    result = []
    for todo in todos:
        dec = json.loads(decrypt(todo.encrypted_content, todo.nonce, "<your_base64_key>"))
        result.append({
            "id": todo.id,
            "title": dec["title"],
            "description": dec["description"],
            "due_date": todo.due_date,
            "completed": todo.completed,
            # reminders will be handled elsewhere
        })
    return result

def get_todo(todo_id, user):
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    return todo

def update_todo(todo_id, data, user):
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        return None
    if hasattr(data, 'title'):
        todo.title = data.title
    if hasattr(data, 'description'):
        todo.description = data.description
    if hasattr(data, 'due_date'):
        todo.due_date = data.due_date
    if hasattr(data, 'completed'):
        todo.completed = data.completed
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(todo_id, user):
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        return False
    db.delete(todo)
    db.commit()
    return True

def set_todo_completed(todo_id, completed, user):
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        return None
    todo.completed = completed
    db.commit()
    db.refresh(todo)
    return todo

def search_todos(user, due_date=None, completed=None, title=None):
    db = SessionLocal()
    query = db.query(Todo).filter(Todo.user_id == user.id)
    if due_date:
        query = query.filter(Todo.due_date == due_date)
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    if title:
        query = query.filter(Todo.title.ilike(f"%{title}%"))
    return query.all() 