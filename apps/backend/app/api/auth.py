from fastapi import APIRouter
from app.schemas.user import UserLogin
from app.services.auth import login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: UserLogin):
    return login_user(data)
