from pydantic import BaseModel

class VaultEntryBase(BaseModel):
    title: str
    encrypted_data: str

class VaultEntryIn(VaultEntryBase):
    pass

class VaultEntryOut(VaultEntryBase):
    id: int

    class Config:
        orm_mode = True
