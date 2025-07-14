from app.models.file import FileEntry
from app.core.encryption import encrypt
from app.db.session import SessionLocal

KEY = "<your_base64_key>"

def upload_file(data, user):
    db = SessionLocal()
    enc = encrypt(data.encrypted_content, KEY)
    file = FileEntry(filename=data.filename, encrypted_content=enc["ciphertext"], nonce=enc["nonce"], user_id=user.id)
    db.add(file)
    db.commit()
    db.refresh(file)
    return file

def get_user_files(user):
    db = SessionLocal()
    return db.query(FileEntry).filter(FileEntry.user_id == user.id).all()