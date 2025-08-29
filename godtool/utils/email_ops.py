import imaplib
import email
import json
import os

def load_config():
    with open(os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')) as f:
        return json.load(f)

def connect_mailbox():
    cfg = load_config()
    mail = imaplib.IMAP4_SSL(cfg['imap_server'], cfg['imap_port'])
    mail.login(cfg['email'], cfg['password'])
    mail.select(cfg['inbox_folder'])
    return mail, cfg

def sort_emails_by_sender(target_sender):
    mail, cfg = connect_mailbox()

    # Search for all emails from target_sender that are UNSEEN (unread)
    status, data = mail.search(None, f'(UNSEEN FROM "{target_sender}")')
    email_ids = data[0].split()

    if not email_ids:
        print(f"No unread emails from {target_sender}")
        mail.logout()
        return

    for eid in email_ids:
        status, msg_data = mail.fetch(eid, '(RFC822)')

        # Safety checks to avoid type errors
        if not msg_data or not isinstance(msg_data[0], tuple):
            print(f"Skipping email ID {eid.decode()}: unexpected data format")
            continue

        raw_email = msg_data[0][1]
        if not isinstance(raw_email, (bytes, bytearray)):
            print(f"Skipping email ID {eid.decode()}: raw email is not bytes")
            continue

        msg = email.message_from_bytes(raw_email)
        subject = msg.get('Subject', 'No Subject')

        print(f"Sorting email with subject: {subject}")

        # Move email to sorted folder
        result = mail.copy(eid, cfg['sorted_folder'])
        if result[0] == 'OK':
            mail.store(eid, '+FLAGS', '\\Deleted')  # mark original as deleted
        mail.expunge()

    mail.logout()
    print(f"Sorted {len(email_ids)} emails from {target_sender} into folder {cfg['sorted_folder']}")

