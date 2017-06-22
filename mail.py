import imaplib
import smtplib
import email

from email.mime.text import  MIMEText
from io import BytesIO


messages = {"undefined": "Изображение не распознано, отправьте изображение в лучшем качестве",
            "not found": "В письме, которое Вы отправили нет прикрелпенного изображения"}


def get_mail_files(message_parts):

    files = []

    # take only attachments
    email_body = message_parts[0][1]

    # take in bytes
    email_text = email.message_from_bytes(email_body)

    # write all bytes in list
    for email_part in email_text.walk():
        file_name = email_part.get_filename()
        if file_name:
            file_in_bytes = BytesIO(email_part.get_payload(decode=True))
            files.append((file_name, file_in_bytes))

    return files


def get_attachments(imap_server, imap_user, imap_password):

    # session start
    imap_session = imaplib.IMAP4_SSL(imap_server)
    _, account_details = imap_session.login(imap_user, imap_password)
    imap_session.select()
    _, email_stack = imap_session.search(None, 'ALL')

     # check every mail for attachment
    for email_id in email_stack[0].split():
        _, message_parts = imap_session.fetch(email_id, '(RFC822)')
        files = get_mail_files(message_parts)

    # session end
    imap_session.close()
    imap_session.logout()

    return files


def get_last_attachment(imap_server, imap_user, imap_password):

    # session start
    imap_session = imaplib.IMAP4_SSL(imap_server)
    _, account_details = imap_session.login(imap_user, imap_password)
    imap_session.select()
    _, email_stack = imap_session.search(None, 'ALL')

    # get list of emails id and choose the last one
    email_id_list = email_stack[0].split()
    email_id_latest = email_id_list[-1]

    # read email with last id
    _, message_parts = imap_session.fetch(email_id_latest, '(RFC822)')
    files = get_mail_files(message_parts)

    # session end
    imap_session.close()
    imap_session.logout()

    return files


def send_mail(smtp_host, smtp_port, smtp_user, smtp_password,  smtp_sender, smtp_recievers, mail_message):

    message = MIMEText(mail_message)
    message['Subject'] = 'Python Script'
    message['From'] = smtp_sender
    message['To'] = smtp_recievers[0]

    # connection to SMTP server
    mail = smtplib.SMTP_SSL(smtp_host, smtp_port)
    mail.login(smtp_user, smtp_password)

    #sending mail and quit
    mail.sendmail(smtp_sender, smtp_recievers, message.as_string())
    mail.quit()

