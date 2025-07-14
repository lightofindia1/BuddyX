from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class VaultEntry(Base):
    __tablename__ = "vaultentry"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    encrypted_data = Column(String)
    nonce = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="vault_entries")