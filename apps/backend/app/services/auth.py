from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.user import User
from app.schemas.user import UserLogin
from app.core.security import verify_password, create_access_token

def login_user(data: UserLogin):
    db: Session = SessionLocal()
    user = db.query(User).filter(User.username == data.username).first()
    
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(data={"sub": user.username})
    
    return {
        "id": user.id,
        "username": user.username,
        "access_token": token,
        "token_type": "bearer"
    }
