from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.models.user import User
from app.core.security import hash_password
from app.models import vault, journal, calendar, file, email, todo, reminder
from app.models.file import FileEntry
from app.models.email import EmailAccount, EmailMessage
from app.models.todo import Todo
from app.models.reminder import Reminder
from app.models.calendar import CalendarEvent
from app.models.vault import VaultEntry
from app.models.journal import JournalEntry

def init_db() -> None:
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        # Check if admin user exists
        admin = db.query(User).filter(User.username == "admin").first()
        if not admin:
            print("Creating default admin user...")
            admin = User(
                username="admin",
                hashed_password=hash_password("admin123")
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
        else:
            print("Admin user already exists.")

if __name__ == "__main__":
    init_db()
