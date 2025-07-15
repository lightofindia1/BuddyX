from fastapi import APIRouter
from app.schemas.user import UserLogin
from app.services.auth import login_user
from apps.backend.main import limiter
from slowapi.decorator import limiter as route_limiter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
@route_limiter("5/minute")
def login(data: UserLogin):
    return login_user(data)
