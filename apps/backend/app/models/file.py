from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class FileEntry(Base):
    __tablename__ = "fileentry"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    encrypted_content = Column(String)
    nonce = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="file_entries")