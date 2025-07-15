from fastapi import APIRouter, Depends, Path, Body
from app.schemas.vault import VaultEntryIn
from app.services.vault import (
    create_vault_entry, get_user_vault_entries, get_vault_entry,
    update_vault_entry, rename_vault_entry, delete_vault_entry, batch_delete_vault_entries
)
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/vault", tags=["Vault"])

@router.post("/")
def create(entry: VaultEntryIn, current_user: User = Depends(get_current_user)):
    return create_vault_entry(entry, current_user)

@router.get("/")
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_vault_entries(current_user)

@router.get("/{vault_id}")
def get_one(vault_id: int = Path(...), current_user: User = Depends(get_current_user)):
    entry = get_vault_entry(vault_id, current_user)
    if not entry:
        return {"error": "Vault entry not found or not owned by user."}
    return entry

@router.put("/{vault_id}")
def update(vault_id: int = Path(...), data: VaultEntryIn = Body(...), current_user: User = Depends(get_current_user)):
    entry = update_vault_entry(vault_id, data, current_user)
    if not entry:
        return {"error": "Vault entry not found or not owned by user."}
    return entry

@router.patch("/{vault_id}/rename")
def rename(vault_id: int = Path(...), new_title: str = Body(..., embed=True), current_user: User = Depends(get_current_user)):
    entry = rename_vault_entry(vault_id, new_title, current_user)
    if not entry:
        return {"error": "Vault entry not found or not owned by user."}
    return entry

@router.delete("/{vault_id}")
def delete(vault_id: int = Path(...), current_user: User = Depends(get_current_user)):
    result = delete_vault_entry(vault_id, current_user)
    if not result:
        return {"error": "Vault entry not found or not owned by user."}
    return {"deleted": vault_id}

@router.post("/batch-delete")
def batch_delete(
    vault_ids: list = Body(..., embed=True),
    current_user: User = Depends(get_current_user)
):
    return batch_delete_vault_entries(vault_ids, current_user)
