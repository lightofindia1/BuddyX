from fastapi import APIRouter, Depends
from app.schemas.file import FileEntryIn
from app.services.file import upload_file, get_user_files
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/files", tags=["Files"])

@router.post("/")
def upload(file_data: FileEntryIn, current_user: User = Depends(get_current_user)):
    return upload_file(file_data, current_user)

@router.get("/")
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_files(current_user)
