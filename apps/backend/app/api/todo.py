from fastapi import APIRouter, Depends, Path, Body, Query
from app.schemas.todo import TodoCreate, TodoOut
from app.services.todo import (
    create_todo, get_user_todos, get_todo, update_todo, delete_todo, set_todo_completed, search_todos
)
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

@router.get("/{todo_id}", response_model=TodoOut)
def get_one(todo_id: int = Path(...), current_user: User = Depends(get_current_user)):
    todo = get_todo(todo_id, current_user)
    if not todo:
        return {"error": "Todo not found or not owned by user."}
    return todo

@router.put("/{todo_id}", response_model=TodoOut)
def update(todo_id: int = Path(...), data: TodoCreate = Body(...), current_user: User = Depends(get_current_user)):
    todo = update_todo(todo_id, data, current_user)
    if not todo:
        return {"error": "Todo not found or not owned by user."}
    return todo

@router.delete("/{todo_id}")
def delete(todo_id: int = Path(...), current_user: User = Depends(get_current_user)):
    result = delete_todo(todo_id, current_user)
    if not result:
        return {"error": "Todo not found or not owned by user."}
    return {"deleted": todo_id}

@router.patch("/{todo_id}/complete", response_model=TodoOut)
def set_complete(todo_id: int = Path(...), completed: bool = Body(..., embed=True), current_user: User = Depends(get_current_user)):
    todo = set_todo_completed(todo_id, completed, current_user)
    if not todo:
        return {"error": "Todo not found or not owned by user."}
    return todo

@router.get("/search", response_model=List[TodoOut])
def search(
    due_date: str = Query(None),
    completed: bool = Query(None),
    title: str = Query(None),
    current_user: User = Depends(get_current_user)
):
    return search_todos(current_user, due_date, completed, title) 