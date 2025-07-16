from fastapi import APIRouter, Body
from app.schemas.user import UserLogin
from app.services.auth import login_user, refresh_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: UserLogin):
    return login_user(data)

@router.post("/refresh")
def refresh(token: str = Body(..., embed=True)):
    return refresh_access_token(token)
