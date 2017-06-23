import config
import mail
import ocr

# recievers = ['astakhovfilat@gmail.com']


# mail.send_mail(config.smtp.server, config.smtp.port, config.smtp.user, config.smtp.password,
#                   config.smtp.sender, recievers, mail.messages['not found'])

image = mail.get_last_attachment(config.imap.server, config.imap.user, config.imap.password)
text = ocr.image_to_text(image)
print(text)

