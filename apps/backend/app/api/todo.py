from fastapi import APIRouter, Depends
from app.schemas.todo import TodoCreate, TodoOut
from app.services.todo import create_todo, get_user_todos
from app.core.deps import get_current_user
from app.models.user import User
from typing import List

router = APIRouter(prefix="/todo", tags=["Todo"])

@router.post("/", response_model=TodoOut)
def create(todo: TodoCreate, current_user: User = Depends(get_current_user)):
    return create_todo(todo, current_user)

@router.get("/", response_model=List[TodoOut])
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_todos(current_user) 