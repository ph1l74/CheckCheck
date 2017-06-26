import config
import mail
import ocr
import db

def Check():

    image = mail.get_last_attachment(config.imap)
    sender = ""

    if image:
        sender, text = ocr.image_to_text(image)
        if text:
            new_reciept = db.Reciept()
            new_reciept.id = text
            new_reciept.add()
        else:
            mail.send_mail(config.smtp, sender, mail.messages['undefined'])
    else:
        mail.send_mail(config.smtp, sender, mail.messages['not found'])

Check()