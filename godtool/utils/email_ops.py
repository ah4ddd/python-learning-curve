import imaplib
import email
import json
import os
from datetime import datetime

def load_config():
    """Load email configuration from settings.json"""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
    try:
        with open(config_path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            "Configuration file not found. Please create config/settings.json with your email settings."
        )
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON in configuration file.")

def connect_mailbox():
    """Connect to email server and return mail connection and config"""
    cfg = load_config()

    # Validate required fields
    required_fields = ['email', 'password', 'imap_server', 'imap_port']
    for field in required_fields:
        if field not in cfg or not cfg[field]:
            raise ValueError(f"Missing required configuration: {field}")

    try:
        print(f"🔌 Connecting to {cfg['imap_server']}...")
        mail = imaplib.IMAP4_SSL(cfg['imap_server'], cfg['imap_port'])
        mail.login(cfg['email'], cfg['password'])

        # Select inbox folder
        inbox = cfg.get('inbox_folder', 'INBOX')
        result = mail.select(inbox)

        if result[0] != 'OK':
            raise Exception(f"Failed to select folder: {inbox}")

        print(f"✅ Connected successfully to {cfg['email']}")
        return mail, cfg

    except imaplib.IMAP4.error as e:
        raise Exception(f"IMAP connection error: {e}")
    except Exception as e:
        raise Exception(f"Email connection failed: {e}")

def create_folder_if_not_exists(mail, folder_name):
    """Create email folder if it doesn't exist"""
    try:
        # List folders to check if it exists
        result, folders = mail.list()

        if result == 'OK':
            folder_exists = any(f'"{folder_name}"' in folder.decode() for folder in folders)

            if not folder_exists:
                result = mail.create(folder_name)
                if result[0] == 'OK':
                    print(f"📁 Created folder: {folder_name}")
                else:
                    print(f"⚠️  Could not create folder: {folder_name}")
                    return False
        return True

    except Exception as e:
        print(f"⚠️  Error managing folder {folder_name}: {e}")
        return False

def sort_emails_by_sender(target_sender):
    """Sort unread emails from a specific sender into a designated folder"""
    try:
        mail, cfg = connect_mailbox()

        # Get sorted folder name
        sorted_folder = cfg.get('sorted_folder', 'Sorted')

        # Create sorted folder if it doesn't exist
        create_folder_if_not_exists(mail, sorted_folder)

        print(f"🔍 Searching for unread emails from: {target_sender}")

        # Search for unread emails from target sender
        search_criteria = f'(UNSEEN FROM "{target_sender}")'
        status, data = mail.search(None, search_criteria)

        if status != 'OK':
            raise Exception("Failed to search emails")

        email_ids = data[0].split() if data[0] else []

        if not email_ids:
            print(f"📭 No unread emails found from {target_sender}")
            mail.logout()
            return

        print(f"📬 Found {len(email_ids)} unread emails from {target_sender}")

        sorted_count = 0
        failed_count = 0

        for eid in email_ids:
            try:
                # Fetch email details
                status, msg_data = mail.fetch(eid, '(RFC822)')

                if status != 'OK' or not msg_data:
                    print(f"⚠️  Could not fetch email ID {eid.decode()}")
                    failed_count += 1
                    continue

                # Safety check for message data
                if not isinstance(msg_data[0], tuple) or len(msg_data[0]) < 2:
                    print(f"⚠️  Invalid email data for ID {eid.decode()}")
                    failed_count += 1
                    continue

                raw_email = msg_data[0][1]
                if not isinstance(raw_email, (bytes, bytearray)):
                    print(f"⚠️  Invalid email format for ID {eid.decode()}")
                    failed_count += 1
                    continue

                # Parse email
                msg = email.message_from_bytes(raw_email)
                subject = msg.get('Subject', 'No Subject')
                sender = msg.get('From', 'Unknown Sender')
                date = msg.get('Date', 'Unknown Date')

                print(f"📧 Processing: {subject[:50]}{'...' if len(subject) > 50 else ''}")

                # Copy email to sorted folder
                copy_result = mail.copy(eid, sorted_folder)
                if copy_result[0] == 'OK':
                    # Mark original as deleted
                    mail.store(eid, '+FLAGS', '\\Deleted')
                    sorted_count += 1
                    print(f"✅ Moved email: {subject[:30]}...")
                else:
                    print(f"❌ Failed to move email: {subject[:30]}...")
                    failed_count += 1

            except Exception as e:
                print(f"❌ Error processing email ID {eid.decode()}: {e}")
                failed_count += 1
                continue

        # Expunge deleted emails
        mail.expunge()
        mail.logout()

        # Summary
        print(f"\n📊 Email Sorting Summary:")
        print(f"   ✅ Successfully sorted: {sorted_count}")
        print(f"   ❌ Failed: {failed_count}")
        print(f"   📁 Moved to folder: {sorted_folder}")

        if sorted_count > 0:
            print(f"🎉 Successfully sorted {sorted_count} emails from {target_sender}")

    except Exception as e:
        print(f"❌ Email sorting failed: {e}")
        raise

def get_email_stats():
    """Get basic email statistics"""
    try:
        mail, cfg = connect_mailbox()

        # Count total emails
        status, total = mail.search(None, 'ALL')
        total_count = len(total[0].split()) if total[0] else 0

        # Count unread emails
        status, unread = mail.search(None, 'UNSEEN')
        unread_count = len(unread[0].split()) if unread[0] else 0

        mail.logout()

        print(f"📊 Email Statistics:")
        print(f"   📧 Total emails: {total_count}")
        print(f"   📬 Unread emails: {unread_count}")
        print(f"   📖 Read emails: {total_count - unread_count}")

        return {
            'total': total_count,
            'unread': unread_count,
            'read': total_count - unread_count
        }

    except Exception as e:
        print(f"❌ Error getting email stats: {e}")
        return None

def list_recent_senders(limit=10):
    """List recent email senders"""
    try:
        mail, cfg = connect_mailbox()

        # Search for recent emails (last 100)
        status, data = mail.search(None, 'ALL')
        email_ids = data[0].split()[-100:] if data[0] else []

        senders = {}

        for eid in email_ids[-limit:]:  # Get last N emails
            try:
                status, msg_data = mail.fetch(eid, '(ENVELOPE)')
                if status == 'OK' and msg_data:
                    # Parse envelope data (simplified)
                    envelope_str = msg_data[0][1].decode('utf-8', errors='ignore')
                    # This is a simplified approach - in production, you'd want proper envelope parsing

            except Exception:
                continue

        mail.logout()

        print(f"👥 Recent Email Senders (showing last {len(senders)}):")
        for sender, count in sorted(senders.items(), key=lambda x: x[1], reverse=True):
            print(f"   📧 {sender}: {count} emails")

    except Exception as e:
        print(f"❌ Error listing senders: {e}")
