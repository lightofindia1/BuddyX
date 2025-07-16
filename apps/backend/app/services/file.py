from app.models.file import FileEntry
from app.core.encryption import encrypt
from app.db.session import SessionLocal
import os

KEY = os.getenv("FILE_ENCRYPTION_KEY")

def upload_file(data, user):
    db = SessionLocal()
    enc = encrypt(data.encrypted_content, KEY)
    file = FileEntry(filename=data.filename, encrypted_content=enc["ciphertext"], nonce=enc["nonce"], user_id=user.id, parent_id=data.parent_id, is_folder=False, size=data.size, file_type=data.file_type)
    db.add(file)
    db.commit()
    db.refresh(file)
    return file

def create_folder(name, user, parent_id=None):
    db = SessionLocal()
    folder = FileEntry(filename=name, encrypted_content=None, nonce=None, user_id=user.id, parent_id=parent_id, is_folder=True)
    db.add(folder)
    db.commit()
    db.refresh(folder)
    return folder

def get_user_files(user):
    db = SessionLocal()
    return db.query(FileEntry).filter(FileEntry.user_id == user.id).all()

def get_user_files_hierarchical(user, parent_id=None):
    db = SessionLocal()
    def build_tree(parent_id):
        entries = db.query(FileEntry).filter(FileEntry.user_id == user.id, FileEntry.parent_id == parent_id).all()
        result = []
        for entry in entries:
            item = {
                "id": entry.id,
                "filename": entry.filename,
                "is_folder": entry.is_folder,
                "parent_id": entry.parent_id,
                "size": entry.size,
                "file_type": entry.file_type,
                "children": build_tree(entry.id) if entry.is_folder else None
            }
            result.append(item)
        return result
    return build_tree(parent_id)

def get_file_content(file_id, user):
    db = SessionLocal()
    file = db.query(FileEntry).filter(FileEntry.id == file_id, FileEntry.user_id == user.id, FileEntry.is_folder == False).first()
    if not file:
        return None
    return {
        "filename": file.filename,
        "encrypted_content": file.encrypted_content,
        "nonce": file.nonce,
        "size": file.size,
        "file_type": file.file_type
    }

def move_file(file_id, new_parent_id, user):
    db = SessionLocal()
    file = db.query(FileEntry).filter(FileEntry.id == file_id, FileEntry.user_id == user.id).first()
    if not file:
        return None
    file.parent_id = new_parent_id
    db.commit()
    db.refresh(file)
    return file

def rename_file(file_id, new_name, user):
    db = SessionLocal()
    file = db.query(FileEntry).filter(FileEntry.id == file_id, FileEntry.user_id == user.id).first()
    if not file:
        return None
    file.filename = new_name
    db.commit()
    db.refresh(file)
    return file

def batch_delete_files(file_ids, user):
    db = SessionLocal()
    files = db.query(FileEntry).filter(FileEntry.id.in_(file_ids), FileEntry.user_id == user.id).all()
    for file in files:
        db.delete(file)
    db.commit()
    return {"deleted": [f.id for f in files]}

def batch_move_files(file_ids, new_parent_id, user):
    db = SessionLocal()
    files = db.query(FileEntry).filter(FileEntry.id.in_(file_ids), FileEntry.user_id == user.id).all()
    for file in files:
        file.parent_id = new_parent_id
    db.commit()
    return {"moved": [f.id for f in files]}

def delete_file(file_id, user):
    db = SessionLocal()
    def recursive_delete(entry):
        if entry.is_folder:
            children = db.query(FileEntry).filter(FileEntry.parent_id == entry.id, FileEntry.user_id == user.id).all()
            for child in children:
                recursive_delete(child)
        db.delete(entry)
    file = db.query(FileEntry).filter(FileEntry.id == file_id, FileEntry.user_id == user.id).first()
    if not file:
        return False
    recursive_delete(file)
    db.commit()
    return True