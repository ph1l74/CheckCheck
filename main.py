import config
import mail
import ocr
import db


def check():
    attachments = mail.get_attachments(config.imap)
    recognized_text = []
    if attachments:
        print("Got some files")
        for attachment in attachments:
            sender = attachment[0][0]
            files =  attachment[1]
            print(len(files))
            if files:
                for file in files:
                    text = ocr.image_to_text()
                    recognized_text.append(text)
            else:
                mail.send_mail(config.smtp, sender, mail.messages['not found'])
                if len(recognized_text) == len(files):
                    for text in recognized_text:
                        new_reciept = db.Reciept()
                        new_reciept.id = text
                        new_reciept.add()
                else:
                    mail.send_mail(config.smtp, sender, mail.messages['undefined'])

check()