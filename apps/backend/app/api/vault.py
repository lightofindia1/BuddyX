from fastapi import APIRouter, Depends
from app.schemas.vault import VaultEntryIn, VaultEntryOut
from app.services.vault import create_vault_entry, get_user_vault_entries
from app.core.deps import get_current_user
from app.models.user import User
from typing import List

router = APIRouter(prefix="/vault", tags=["Vault"])

@router.post("/", response_model=VaultEntryOut)
def create(entry: VaultEntryIn, current_user: User = Depends(get_current_user)):
    return create_vault_entry(entry, current_user)

@router.get("/", response_model=List[VaultEntryOut])
def read_all(current_user: User = Depends(get_current_user)):
    return get_user_vault_entries(current_user)
