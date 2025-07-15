from pydantic import BaseModel

class VaultEntryIn(BaseModel):
    title: str
    data: str

class VaultEntryOut(VaultEntryIn):
    id: int
    class Config:
        orm_mode = True
