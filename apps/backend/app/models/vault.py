from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class VaultEntry(Base):
    __tablename__ = "vaultentry"
    id = Column(Integer, primary_key=True, index=True)
    encrypted_data = Column(String, nullable=False)
    nonce = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="vault_entries")