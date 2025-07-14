from app.models.email import EmailMessage
from app.db.session import SessionLocal

def send_email(data, user):
    db = SessionLocal()
    email = EmailMessage(subject=data.subject, body=data.body, from_addr=data.from_addr, to_addr=data.to_addr, user_id=user.id)
    db.add(email)
    db.commit()
    db.refresh(email)
    return email

def get_user_emails(user):
    db = SessionLocal()
    return db.query(EmailMessage).filter(EmailMessage.user_id == user.id).all()
