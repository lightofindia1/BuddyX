from app.models.email import EmailAccount, EmailMessage
from app.db.session import SessionLocal
from app.core.encryption import encrypt, decrypt
import json
from datetime import datetime

KEY = "<your_base64_key>"

# EmailAccount services
def create_email_account(data, user):
    db = SessionLocal()
    to_encrypt = json.dumps({
        "access_token": data.access_token,
        "refresh_token": data.refresh_token
    })
    enc = encrypt(to_encrypt, KEY)
    account = EmailAccount(
        user_id=user.id,
        provider=data.provider,
        email_address=data.email_address,
        display_name=data.display_name,
        encrypted_access_token=enc["ciphertext"],
        encrypted_refresh_token=enc["nonce"],
        token_expiry=data.token_expiry,
        settings=data.settings,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def get_user_email_accounts(user):
    db = SessionLocal()
    accounts = db.query(EmailAccount).filter(EmailAccount.user_id == user.id).all()
    result = []
    for acc in accounts:
        dec = json.loads(decrypt(acc.encrypted_access_token, acc.encrypted_refresh_token, KEY))
        result.append({
            "id": acc.id,
            "provider": acc.provider,
            "email_address": acc.email_address,
            "display_name": acc.display_name,
            "token_expiry": acc.token_expiry,
            "settings": acc.settings,
            "created_at": acc.created_at,
            "updated_at": acc.updated_at
        })
    return result

# EmailMessage services
def create_email_message(data, user):
    db = SessionLocal()
    to_encrypt = json.dumps({
        "subject": data.subject,
        "body_plain": data.body_plain,
        "body_html": data.body_html,
        "from_addr": data.from_addr,
        "to_addrs": data.to_addrs,
        "cc_addrs": data.cc_addrs,
        "bcc_addrs": data.bcc_addrs,
        "reply_to": data.reply_to,
        "attachments": data.attachments
    })
    enc = encrypt(to_encrypt, KEY)
    msg = EmailMessage(
        email_account_id=data.email_account_id,
        message_id=data.message_id,
        thread_id=data.thread_id,
        subject=data.subject,
        body_plain=data.body_plain,
        body_html=data.body_html,
        from_addr=data.from_addr,
        to_addrs=data.to_addrs,
        cc_addrs=data.cc_addrs,
        bcc_addrs=data.bcc_addrs,
        reply_to=data.reply_to,
        attachments=data.attachments,
        date_sent=data.date_sent,
        date_received=data.date_received,
        folder=data.folder,
        is_read=data.is_read,
        is_starred=data.is_starred,
        is_important=data.is_important,
        encrypted_content=enc["ciphertext"],
        nonce=enc["nonce"],
        user_id=user.id
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

def get_user_emails(user):
    db = SessionLocal()
    emails = db.query(EmailMessage).filter(EmailMessage.user_id == user.id).all()
    result = []
    for email in emails:
        dec = json.loads(decrypt(email.encrypted_content, email.nonce, KEY))
        result.append({
            "id": email.id,
            "email_account_id": email.email_account_id,
            "message_id": email.message_id,
            "thread_id": email.thread_id,
            "subject": dec.get("subject"),
            "body_plain": dec.get("body_plain"),
            "body_html": dec.get("body_html"),
            "from_addr": dec.get("from_addr"),
            "to_addrs": dec.get("to_addrs"),
            "cc_addrs": dec.get("cc_addrs"),
            "bcc_addrs": dec.get("bcc_addrs"),
            "reply_to": dec.get("reply_to"),
            "attachments": dec.get("attachments"),
            "date_sent": email.date_sent,
            "date_received": email.date_received,
            "folder": email.folder,
            "is_read": email.is_read,
            "is_starred": email.is_starred,
            "is_important": email.is_important
        })
    return result
