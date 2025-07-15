from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class FileEntry(Base):
    __tablename__ = "fileentry"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    encrypted_content = Column(String)
    nonce = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    parent_id = Column(Integer, ForeignKey("fileentry.id"), nullable=True)
    is_folder = Column(Boolean, default=False)
    size = Column(Integer, nullable=True)
    file_type = Column(String, nullable=True)

    user = relationship("User", back_populates="file_entries")
    children = relationship("FileEntry", backref="parent", remote_side=[id])