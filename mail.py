import imaplib
import smtplib
import email
import re

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
            files.append(file_in_bytes)
    return files


def get_mail_sender(message_parts):

    re_mask = re.compile(r'[a-zA-Z0-9._-]*@[a-zA-Z0-9._-]*')
    email_body = message_parts[0][1]
    email_text = email.message_from_bytes(email_body)
    email_sender_text = email_text['From']
    email_sender = re_mask.findall(email_sender_text)

    return email_sender


def get_attachments(imap_object, count=1):

    imap_server = imap_object.server
    imap_user = imap_object.user
    imap_password = imap_object.password

    files = []

    # session start
    imap_session = imaplib.IMAP4_SSL(imap_server)
    _, account_details = imap_session.login(imap_user, imap_password)
    imap_session.select()
    _, email_stack = imap_session.search(None, 'ALL')


    # get list of emails id and choose the last one
    email_id_list = email_stack[0].split()

    for i in range(count, 0, -1):
        _, message_parts = imap_session.fetch(email_id_list[-i], '(RFC822)')
        message_files = get_mail_files(message_parts)
        sender = get_mail_sender(message_parts)
        files.append([sender, message_files])

    # session end
    imap_session.close()
    imap_session.logout()

    return files


def send_mail(smtp_object, smtp_reciever, mail_message):

    # load from config
    smtp_host = smtp_object.server
    smtp_port = smtp_object.port
    smtp_user = smtp_object.user
    smtp_password = smtp_object.password
    smtp_sender = smtp_object.sender

    # make empty tuple and append with smtp_reciver
    smtp_recievers = []
    smtp_recievers.append(smtp_reciever)

    message = MIMEText(mail_message)
    message['Subject'] = 'Python Script'
    message['From'] = smtp_sender
    message['To'] = smtp_recievers[0]

    # connection to SMTP server
    mail = smtplib.SMTP_SSL(smtp_host, smtp_port)
    mail.login(smtp_user, smtp_password)

    #sending mail and quit
    mail.send_message(message)
    mail.quit()

    return "Mail sent"
