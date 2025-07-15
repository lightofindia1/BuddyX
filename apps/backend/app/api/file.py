from fastapi import APIRouter, Depends
from app.schemas.file import FileEntryIn
from app.services.file import upload_file, get_user_files, create_folder
from app.core.deps import get_current_user
from app.models.user import User
from fastapi import Body, Path
from app.services.file import move_file
from app.services.file import rename_file
from app.services.file import batch_delete_files, batch_move_files
from app.services.file import get_file_content
from fastapi import Query
from app.services.file import get_user_files_hierarchical
from app.services.file import delete_file

router = APIRouter(prefix="/files", tags=["Files"])

@router.post("/")
def upload(file_data: FileEntryIn, current_user: User = Depends(get_current_user)):
    return upload_file(file_data, current_user)

@router.get("/")
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_files(current_user)

@router.post("/folder")
def create_folder_api(
    name: str = Body(..., embed=True),
    parent_id: int = Body(None, embed=True),
    current_user: User = Depends(get_current_user)
):
    return create_folder(name, current_user, parent_id)

@router.patch("/{file_id}/move")
def move_file_api(
    file_id: int = Path(...),
    new_parent_id: int = Body(..., embed=True),
    current_user: User = Depends(get_current_user)
):
    result = move_file(file_id, new_parent_id, current_user)
    if not result:
        return {"error": "File or folder not found or not owned by user."}
    return result

@router.patch("/{file_id}/rename")
def rename_file_api(
    file_id: int = Path(...),
    new_name: str = Body(..., embed=True),
    current_user: User = Depends(get_current_user)
):
    result = rename_file(file_id, new_name, current_user)
    if not result:
        return {"error": "File or folder not found or not owned by user."}
    return result

@router.post("/batch-delete")
def batch_delete_api(
    file_ids: list = Body(..., embed=True),
    current_user: User = Depends(get_current_user)
):
    return batch_delete_files(file_ids, current_user)

@router.post("/batch-move")
def batch_move_api(
    file_ids: list = Body(..., embed=True),
    new_parent_id: int = Body(..., embed=True),
    current_user: User = Depends(get_current_user)
):
    return batch_move_files(file_ids, new_parent_id, current_user)

@router.get("/{file_id}/download")
def download_file_api(
    file_id: int = Path(...),
    current_user: User = Depends(get_current_user)
):
    result = get_file_content(file_id, current_user)
    if not result:
        return {"error": "File not found, not owned by user, or is a folder."}
    return result

@router.delete("/{file_id}")
def delete_file_api(
    file_id: int = Path(...),
    current_user: User = Depends(get_current_user)
):
    result = delete_file(file_id, current_user)
    if not result:
        return {"error": "File or folder not found or not owned by user."}
    return {"deleted": file_id}

@router.get("/tree")
def get_files_tree_api(
    parent_id: int = Query(None),
    current_user: User = Depends(get_current_user)
):
    return get_user_files_hierarchical(current_user, parent_id)
