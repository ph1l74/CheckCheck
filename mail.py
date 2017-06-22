import imaplib
import smtplib
import email
from io import BytesIO as bio


messages = {"undefined": "Изображение не распознано, отправьте изображение в лучшем качестве",
            "not found": "В письме, которое Вы отправили нет прикрелпенного изображения"}


def get_all_attachments(imap_server, imap_user, imap_password):

    files = []

    # session start
    imap_session = imaplib.IMAP4_SSL(imap_server)
    _, account_details = imap_session.login(imap_user, imap_password)
    imap_session.select()
    _, email_stack = imap_session.search(None, 'ALL')

    # check every mail for attachment
    for email_id in email_stack[0].split():
        _, message_parts = imap_session.fetch(email_id, '(RFC822)')
        email_body = message_parts[0][1]
        email_text = email.message_from_bytes(email_body)
        for email_part in email_text.walk():
            file_name = email_part.get_filename()
            if file_name:
                file_in_bytes = bio(email_part.get_payload(decode=True))
                files.append((file_name, file_in_bytes))

    # session end
    imap_session.close()
    imap_session.logout()

    return files


def get_last_attachment(imap_server, imap_user, imap_password):

    files = []

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
    email_body = message_parts[0][1]
    email_text = email.message_from_bytes(email_body)

    for email_part in email_text.walk():
        file_name = email_part.get_filename()
        if file_name:
            file_in_bytes = bio(email_part.get_payload(decode=True))
            files.append((file_name, file_in_bytes))

    # session end
    imap_session.close()
    imap_session.logout()

    return files


def send_mail(smtp_host, smtp_port, smtp_user, smtp_password,  smtp_sender, smtp_recievers, mail_message):

    # connection to SMTP server
    mail = smtplib.SMTP(smtp_host, smtp_port)
    mail.starttls()
    mail.login(smtp_user, smtp_password)

    #sending mail
    mail.sendmail(smtp_sender, smtp_recievers, mail_message)

    # close SMTP-connection
    mail.quit()

    return True
