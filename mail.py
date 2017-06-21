import imaplib
import email
import os


def get_all_attachments(imap_server, imap_user, imap_password):

    # session start
    imap_session = imaplib.IMAP4_SSL(imap_server)
    _, account_details = imap_session.login(imap_user, imap_password)
    imap_session.select()
    _, email_stack = imap_session.search(None, 'ALL')

    # check every mail for attachment
    for message_id in email_stack[0].split():
        _, message_parts = imap_session.fetch(message_id, '(RFC822)')
        email_body = message_parts[0][1]
        email_text = email.message_from_bytes(email_body)
        for email_part in email_text.walk():
            file_name = email_part.get_filename()
            if file_name:
                file_path = os.path.join('', 'attachments', file_name)
                file_handler = open(file_path, 'wb')
                file_handler.write(email_part.get_payload(decode=True))
                file_handler.close()

    # session end
    imap_session.close()
    imap_session.logout()
    return "Done"

